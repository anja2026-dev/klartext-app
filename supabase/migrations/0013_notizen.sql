-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration · Phase 1
-- Notizen (Notizblock)
--
-- Ersetzt localStorage['kt_notizen_liste'] aus KLARTEXT_Notizblock.html.
--
-- Reine Datenstruktur. Keine RLS in dieser Migration.
-- ════════════════════════════════════════════════════════════

create table notizen (
  id            uuid primary key default gen_random_uuid(),
  ersteller_id  uuid references profiles(id),
  datum         date not null,
  thema         text,
  text          text not null,
  created_at    timestamptz not null default now()
);
