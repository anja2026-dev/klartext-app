-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration
-- Kinder-Zuordnung (Schule/INGRA/Trainer/TK)
--
-- gruppe_id bewusst weggelassen: eine "gruppen"-Tabelle existiert im
-- Schema nicht (nur die Freitextfelder kita_gruppe/wf_gruppenleitung
-- auf kinder), eine Fremdschlüssel-Referenz darauf würde die Migration
-- zum Scheitern bringen. Kann in einer eigenen Migration nachgezogen
-- werden, sobald eine echte gruppen-Tabelle angelegt ist.
--
-- Reine Datenstruktur. Keine RLS in dieser Migration.
-- ════════════════════════════════════════════════════════════

create table kinder_zuordnung (
  id          uuid primary key default gen_random_uuid(),
  kind_id     uuid references kinder(id) on delete cascade,
  schule_id   uuid references schulen(id) on delete set null,
  ingra_id    uuid references profiles(id) on delete set null,
  trainer_id  uuid references profiles(id) on delete set null,
  tk_id       uuid references profiles(id) on delete set null,
  aktiv       boolean default true,
  timestamp   timestamptz default now()
);
