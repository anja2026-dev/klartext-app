-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration · Phase 0/1
-- Auth- & Rollen-Grundgerüst
--
-- Ersetzt das bisherige Login-Modell (gemeinsame Klartext-Passwörter
-- + sessionStorage-Flag in KLARTEXT_Login.html) durch echte,
-- individuelle Supabase-Auth-Konten mit rollenbasierter RLS.
--
-- Diese Migration legt NUR die Datenstruktur an.
-- Es gibt noch keine Frontend-Anbindung (kein Login-Flow geändert).
-- ════════════════════════════════════════════════════════════

create extension if not exists pgcrypto;

-- ── Träger (Mandant) ───────────────────────────────────────────
create table traeger (
  id          uuid primary key default gen_random_uuid(),
  name        text not null,
  adresse     text,
  created_at  timestamptz not null default now()
);

-- ── Rollen als eigener Typ, damit Policies sauber vergleichen können ──
create type klartext_rolle as enum ('ingra','tk','lk','eltern','trainer','admin');
create type ingra_subrolle as enum ('fest','springer','pool','vertretung');

-- ── Profile: 1:1 mit auth.users, ersetzt geteilte Rollen-Passwörter ──
create table profiles (
  id              uuid primary key references auth.users(id) on delete cascade,
  traeger_id      uuid references traeger(id),
  vorname         text,
  nachname        text,
  email           text,
  telefon         text,
  rolle           klartext_rolle not null,
  ingra_subrolle  ingra_subrolle,
  qualifikationen text[] not null default '{}',
  fuehrerschein   boolean not null default false,
  fahrzeug        boolean not null default false,
  aktiv           boolean not null default true,
  created_at      timestamptz not null default now(),
  updated_at      timestamptz not null default now()
);

comment on table profiles is
  'Ersetzt KLARTEXT_Login.html: ein echtes Konto pro Person statt ein Passwort pro Rolle.';
comment on column profiles.rolle is
  'Nur per service_role-Funktion änderbar, niemals durch den Nutzer selbst (siehe unten).';

-- ── Qualifikationen-Katalog (Lookup, z.B. für Vertretungssuche) ──
create table qualifikationen_katalog (
  code          text primary key,
  beschreibung  text,
  pflicht_fuer  text
);

-- ── updated_at automatisch pflegen ──────────────────────────────
create or replace function set_updated_at()
returns trigger language plpgsql as $$
begin
  new.updated_at = now();
  return new;
end;
$$;

create trigger trg_profiles_updated_at
  before update on profiles
  for each row execute function set_updated_at();

-- ── RLS: Rollen werden ab jetzt in der DB erzwungen, nicht im Frontend ──
alter table traeger enable row level security;
alter table profiles enable row level security;
alter table qualifikationen_katalog enable row level security;

-- Jede:r sieht das eigene Profil
create policy profiles_select_own
  on profiles for select
  using (id = auth.uid());

-- Jede:r darf nur die eigenen Kontaktfelder ändern — NICHT die eigene Rolle
create policy profiles_update_own_no_role_change
  on profiles for update
  using (id = auth.uid())
  with check (id = auth.uid());

revoke update (rolle, ingra_subrolle, traeger_id) on profiles from authenticated;

-- Admin sieht/verwaltet alle Profile eines Trägers
create policy profiles_admin_all
  on profiles for all
  using (
    exists (
      select 1 from profiles p
      where p.id = auth.uid() and p.rolle = 'admin'
    )
  );

-- Qualifikationskatalog ist für alle eingeloggten Rollen lesbar
create policy qualifikationen_read_all
  on qualifikationen_katalog for select
  to authenticated
  using (true);

-- Träger-Stammdaten: lesbar für Mitglieder desselben Trägers
create policy traeger_select_member
  on traeger for select
  using (
    exists (
      select 1 from profiles p
      where p.id = auth.uid() and p.traeger_id = traeger.id
    )
  );
