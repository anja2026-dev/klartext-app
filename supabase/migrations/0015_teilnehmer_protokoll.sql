-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration · Phase 1
-- Teilnehmer-Protokoll
--
-- Ersetzt localStorage['kt_tn_protokoll'] aus
-- KLARTEXT_Teilnehmer_Protokoll.html.
--
-- Reine Datenstruktur. Keine RLS in dieser Migration.
-- ════════════════════════════════════════════════════════════

create table teilnehmer_protokoll (
  id            uuid primary key default gen_random_uuid(),
  ersteller_id  uuid references profiles(id),
  name          text not null,
  datum         date,
  einrichtung   text,
  vorschlaege   text,
  anmerkungen   text,
  created_at    timestamptz not null default now()
);
