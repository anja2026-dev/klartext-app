-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration · Phase 1
-- Kinder-Stammdaten (einzige Quelle)
--
-- Ersetzt zwei konkurrierende, nicht synchronisierte Datensätze:
--   - Firebase /children  (genutzt von Weiterleiten, TK-Inbox, Chat,
--     Barometer-Kind, Zeitkonto, Krankmeldung, Urlaubsantrag)
--   - localStorage['children'] (genutzt nur von Kinderverwaltung.html)
-- durch eine einzige Tabelle, die alle Module referenzieren.
--
-- Reine Datenstruktur. Noch keine Frontend-Anbindung.
-- ════════════════════════════════════════════════════════════

-- ── Schulen / Einsatzorte ──────────────────────────────────────
create table schulen (
  id          uuid primary key default gen_random_uuid(),
  traeger_id  uuid references traeger(id),
  name        text not null,
  adresse     text,
  ort         text,
  plz         text,
  lat         numeric,
  lng         numeric,
  schultyp    text check (schultyp in ('grundschule','foerderschule','realschule','gymnasium','sonstige')),
  kontakt     text,
  aktiv       boolean not null default true,
  created_at  timestamptz not null default now()
);

-- ── Kinder: einzige Quelle für alle TK-Module ──────────────────
create table kinder (
  id                    uuid primary key default gen_random_uuid(),
  traeger_id            uuid not null references traeger(id),
  name                  text not null,
  klasse                text,
  geburtsdatum          date,
  bedarfsart            text,
  schule_id             uuid references schulen(id),
  kita_name             text,
  kita_gruppe           text,
  werkstatt_name        text,
  wf_bereich            text,
  arbeitsplatz          text,
  einsatzort            text,
  leistungserbringer    text,   -- "Träger der Maßnahme" (Freitext, ≠ traeger_id)
  kostentraeger         text,
  aktenzeichen          text,   -- Kandidat für Vault-Verschlüsselung (siehe DSGVO-Analyse #10)
  lehrkraft_name        text,
  bezugserzieher_name   text,
  wf_gruppenleitung     text,
  ansprechpartner       text,
  arbeitszeiten         text,
  einwilligung_erfasst  boolean not null default false,   -- schließt DSGVO-Befund #9
  einwilligung_datum    date,
  aktiv                 boolean not null default true,
  ausgetreten_am        date,
  created_at            timestamptz not null default now(),
  updated_at            timestamptz not null default now()
);

comment on table kinder is
  'Einzige Quelle für Kinderdaten. Ersetzt Firebase /children UND localStorage[''children''].';

create trigger trg_kinder_updated_at
  before update on kinder
  for each row execute function set_updated_at();

-- ── Wochenplan (Einsatzzeiten je Kind) ──────────────────────────
create table kinder_wochenplan (
  id         uuid primary key default gen_random_uuid(),
  kind_id    uuid not null references kinder(id) on delete cascade,
  wochentag  text not null check (wochentag in ('MO','DI','MI','DO','FR')),
  von        time,
  bis        time
);

-- ── RLS ──────────────────────────────────────────────────────────
alter table schulen enable row level security;
alter table kinder enable row level security;
alter table kinder_wochenplan enable row level security;

-- Schulen: lesbar für alle eingeloggten Rollen des eigenen Trägers
create policy schulen_select_traeger
  on schulen for select
  using (
    exists (
      select 1 from profiles p
      where p.id = auth.uid() and p.traeger_id = schulen.traeger_id
    )
  );

-- Kinder: TK und Admin verwalten alle Kinder des eigenen Trägers
create policy kinder_tk_admin_all
  on kinder for all
  using (
    exists (
      select 1 from profiles p
      where p.id = auth.uid()
        and p.traeger_id = kinder.traeger_id
        and p.rolle in ('tk','admin')
    )
  );

-- INGRA sieht nur Kinder, denen sie über einen aktiven Einsatz zugeordnet ist
-- (Tabelle "einsaetze" folgt in einer späteren Migration — Policy wird dort ergänzt)

create policy kinder_wochenplan_select_traeger
  on kinder_wochenplan for select
  using (
    exists (
      select 1 from kinder k
      join profiles p on p.traeger_id = k.traeger_id
      where k.id = kinder_wochenplan.kind_id and p.id = auth.uid()
    )
  );
