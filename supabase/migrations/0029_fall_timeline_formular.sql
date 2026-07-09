-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration
-- Verlauf-Formular (FM-04): Fakten von Einschätzung trennen
--
-- fall_timeline existiert bereits (0004_fallmanagement.sql), aber mit
-- anderen Spalten (ereignis/beobachtung/rueckmeldung als lose
-- Freitextfelder, keine ereignistyp-Kategorisierung, kein fakten/
-- einschaetzung-Split). Nicht "passend" wie fall_massnahmen - deshalb
-- hier erweitert statt unverändert übernommen. Die alten Spalten
-- bleiben unangetastet (kein Drop), werden vom neuen Formular aber
-- nicht mehr befüllt.
--
-- RLS bleibt unverändert: die bestehende Policy
-- fall_timeline_ueber_fallakte (Sichtbarkeit über die zugehörige
-- Fallakte) gilt unabhängig von den Spalten weiter.
-- ════════════════════════════════════════════════════════════

alter table fall_timeline
  add column ereignistyp   text check (ereignistyp in ('beobachtung','gespraech','vorfall','uebergabe')),
  add column fakten        text,
  add column einschaetzung text;

comment on column fall_timeline.fakten is
  'Beobachtbare Fakten - bewusst getrennt von einschaetzung, um Beobachtung nicht mit Deutung zu vermischen.';
comment on column fall_timeline.einschaetzung is
  'Fachliche Einschätzung/Deutung - getrennt von fakten (siehe dort).';
