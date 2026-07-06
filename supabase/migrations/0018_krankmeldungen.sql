-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration · Phase 1
-- Krankmeldungen
--
-- Ersetzt Firebase /sick_note_ingra + /sick_note sowie
-- localStorage['kz_meldungen'] aus KLARTEXT_Krankmeldung.html.
-- Zwei Unterarten laut bestehendem Code: typ='ingra' (eigene
-- Krankmeldung, Zeitraum von/bis) und typ='kind' (Ausfall eines
-- Kindes, Einzeltag mit Grund/Zeit).
--
-- Reine Datenstruktur. Keine RLS in dieser Migration.
-- ════════════════════════════════════════════════════════════

create table krankmeldungen (
  id          uuid primary key default gen_random_uuid(),
  ingra_id    uuid references profiles(id),
  typ         text not null check (typ in ('ingra','kind')),
  kind_id     uuid references kinder(id),
  von_datum   date,
  bis_datum   date,
  datum       date,
  grund       text,
  zeit        text,
  notiz       text,
  created_at  timestamptz not null default now()
);
