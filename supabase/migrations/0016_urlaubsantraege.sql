-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration · Phase 1
-- Urlaubsanträge
--
-- Ersetzt Firebase /vacation_request aus
-- KLARTEXT_Urlaubsantrag_INGRA.html.
--
-- Reine Datenstruktur. Keine RLS in dieser Migration.
-- ════════════════════════════════════════════════════════════

create table urlaubsantraege (
  id          uuid primary key default gen_random_uuid(),
  ingra_id    uuid references profiles(id),
  kind_id     uuid references kinder(id),
  von_datum   date not null,
  bis_datum   date not null,
  tage        int,
  vertretung  text,
  notiz       text,
  status      text not null default 'beantragt' check (status in ('beantragt','genehmigt','abgelehnt')),
  created_at  timestamptz not null default now()
);
