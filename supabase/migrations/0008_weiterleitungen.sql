-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration · Phase 2
-- Weiterleitungs-Grundstruktur
--
-- Ersetzt Firebase /forward (KLARTEXT_Weiterleiten.html schreibt,
-- KLARTEXT_TK_Inbox.html / TK_Uebergaben.html lesen). Eltern/Lehrkraft
-- erhalten Inhalte weiterhin nur über token-basierte Weiterleitungs-
-- Links (KLARTEXT_Forward_Read.html-Muster), nicht über direkten
-- authentifizierten Tabellenzugriff — daher keine Eltern/LK-Policies
-- hier, konsistent mit der Entscheidung aus der Fallmanagement-Migration.
--
-- Reine Datenstruktur. Noch keine Frontend-Anbindung.
-- ════════════════════════════════════════════════════════════

create table weiterleitungen (
  id              uuid primary key default gen_random_uuid(),
  kind_id         uuid not null references kinder(id),
  von_profil      uuid references profiles(id),
  von_rolle       text,
  ziel_rolle      text not null default 'tk',
  typ             text not null check (typ in ('uebergabe','barometer','hinweis')),
  text            text,
  dringlichkeit   text not null check (dringlichkeit in ('normal','erhoben','dringend')) default 'normal',
  status          text not null check (status in ('offen','gelesen','erledigt')) default 'offen',
  besonderheiten  text,
  details         text,
  anhang_pfad     text,   -- Storage-Referenz statt Freitext-"Anhang" wie bisher
  created_at      timestamptz not null default now(),
  updated_at      timestamptz not null default now()
);

comment on table weiterleitungen is
  'Ersetzt Firebase /forward. anhang_pfad verweist auf Supabase Storage statt auf einen reinen Freitext-Hinweis.';

create trigger trg_weiterleitungen_updated_at
  before update on weiterleitungen
  for each row execute function set_updated_at();

-- ── RLS ──────────────────────────────────────────────────────────
alter table weiterleitungen enable row level security;

-- TK/Admin: volle Sicht + Statuspflege (das ist die eigentliche "TK-Inbox")
create policy weiterleitungen_tk_admin_all
  on weiterleitungen for all
  using (
    exists (
      select 1 from kinder k
      join profiles p on p.traeger_id = k.traeger_id
      where k.id = weiterleitungen.kind_id
        and p.id = auth.uid()
        and p.rolle in ('tk','admin')
    )
  );

-- Zugewiesene INGRA darf für ihre Kinder Weiterleitungen anlegen
create policy weiterleitungen_ingra_insert
  on weiterleitungen for insert
  with check (exists (select 1 from ingra_kinder ik where ik.kind_id = weiterleitungen.kind_id and ik.ingra_id = auth.uid()));

-- Absender:in sieht die eigenen gesendeten Weiterleitungen (z.B. Status verfolgen)
create policy weiterleitungen_select_eigene
  on weiterleitungen for select
  using (von_profil = auth.uid());
