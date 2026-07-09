-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration
-- Fallakte-Formular (FM-01): erweiterte Stammdaten + Mehrfach-Listen
--
-- Ergänzt fallakten (0004_fallmanagement.sql) um die im Formular
-- benötigten Einzelfelder. Die bereits bestehenden Freitextspalten
-- bezugsperson/bezugsperson_kontakt/ziele bleiben unverändert erhalten
-- (kein Drop), werden vom neuen Formular aber nicht mehr befüllt -
-- Bezugspersonen, Netzwerk-Kontakte und Ziele sind jetzt Mehrfach-Listen
-- in eigenen Tabellen (siehe unten), da eine Fallakte davon mehrere
-- haben kann.
-- ════════════════════════════════════════════════════════════

alter table fallakten
  add column rechtsgrundlage      text check (rechtsgrundlage in ('sgb_viii_35a','sgb_ix_54','sonstige')),
  add column kostentraeger        text,
  add column stundenumfang        text,
  add column befristet_bis        date,
  add column ingra_id             uuid references profiles(id),
  add column vertretung_ingra_id  uuid references profiles(id);

comment on column fallakten.ingra_id is
  'Zuständige INGRA für die Fallakte. Vorbelegt aus kinder_zuordnung.ingra_id, im Formular änderbar.';
comment on column fallakten.vertretung_ingra_id is
  'Vertretung der zuständigen INGRA, frei wählbar aus profiles (rolle=ingra).';

-- ── Bezugspersonen: mehrere pro Fallakte ────────────────────────
create table fallakte_bezugspersonen (
  id           uuid primary key default gen_random_uuid(),
  fallakte_id  uuid not null references fallakten(id) on delete cascade,
  name         text not null,
  rolle        text,
  created_at   timestamptz not null default now()
);

-- ── Netzwerk: externe Kontakte, mehrere pro Fallakte ────────────
create table fallakte_netzwerk (
  id           uuid primary key default gen_random_uuid(),
  fallakte_id  uuid not null references fallakten(id) on delete cascade,
  name         text not null,
  rolle        text,
  kontakt      text,
  created_at   timestamptz not null default now()
);

-- ── Ziele: strukturierte Mehrfach-Liste (ersetzt fallakten.ziele) ──
create table fall_ziele (
  id           uuid primary key default gen_random_uuid(),
  fallakte_id  uuid not null references fallakten(id) on delete cascade,
  ziel         text not null,
  indikator    text,
  zieldatum    date,
  created_at   timestamptz not null default now()
);

-- ── RLS: gleiche Sichtbarkeit wie die zugehörige Fallakte (Muster aus
--    fall_risikostatus_ueber_fallakte / fall_timeline_ueber_fallakte in
--    0004_fallmanagement.sql) ─────────────────────────────────────
alter table fallakte_bezugspersonen enable row level security;
alter table fallakte_netzwerk enable row level security;
alter table fall_ziele enable row level security;

create policy fallakte_bezugspersonen_ueber_fallakte
  on fallakte_bezugspersonen for all
  using (exists (select 1 from fallakten f where f.id = fallakte_bezugspersonen.fallakte_id));

create policy fallakte_netzwerk_ueber_fallakte
  on fallakte_netzwerk for all
  using (exists (select 1 from fallakten f where f.id = fallakte_netzwerk.fallakte_id));

create policy fall_ziele_ueber_fallakte
  on fall_ziele for all
  using (exists (select 1 from fallakten f where f.id = fall_ziele.fallakte_id));
