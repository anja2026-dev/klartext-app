-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration · Phase 1
-- Zeiteinträge (Zeitkonto)
--
-- Ersetzt Firebase /time_entry + localStorage['kt_eintraege'] aus
-- KLARTEXT_Zeitkonto.html.
--
-- Reine Datenstruktur. Keine RLS in dieser Migration.
-- ════════════════════════════════════════════════════════════

create table zeiteintraege (
  id             uuid primary key default gen_random_uuid(),
  ingra_id       uuid references profiles(id),
  kind_id        uuid references kinder(id),
  datum          date not null,
  von_uhrzeit    time not null,
  bis_uhrzeit    time not null,
  pause_minuten  int not null default 0,
  dauer_stunden  numeric,
  typ            text,
  notiz          text,
  created_at     timestamptz not null default now()
);
