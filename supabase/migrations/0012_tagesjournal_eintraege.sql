-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration · Phase 1
-- Tagesjournal-Einträge (Barometer + Notiz je Tag/Kind)
--
-- Ersetzt localStorage['kt_tagesjournal'] aus KLARTEXT_Tagesjournal.html.
-- Die "Übergabe"-Funktion dieser Seite nutzt bereits sendForward() und
-- ist damit durch die bestehende Tabelle weiterleitungen abgedeckt.
--
-- Reine Datenstruktur. Keine RLS in dieser Migration.
-- ════════════════════════════════════════════════════════════

create table tagesjournal_eintraege (
  id                    uuid primary key default gen_random_uuid(),
  kind_id               uuid references kinder(id),
  ersteller_id          uuid references profiles(id),
  datum                 date not null,
  barometer_farbe       text check (barometer_farbe in ('gruen','gelb','orange','rot','grau')),
  barometer_zeit        time,
  notiz                 text,
  besonderheit          text,
  besonderheit_details  text,
  created_at            timestamptz not null default now()
);
