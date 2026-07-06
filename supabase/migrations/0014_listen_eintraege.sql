-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration · Phase 1
-- Listen-Einträge (To-do-Liste)
--
-- Ersetzt localStorage['klartext_todo_list'] aus KLARTEXT_Listen.html.
-- kategorie ist bereits mehrkategorie-fähig angelegt, auch wenn der
-- bestehende Code aktuell nur die Kategorie 'todo' schreibt.
--
-- Reine Datenstruktur. Keine RLS in dieser Migration.
-- ════════════════════════════════════════════════════════════

create table listen_eintraege (
  id            uuid primary key default gen_random_uuid(),
  ersteller_id  uuid references profiles(id),
  kategorie     text not null default 'todo',
  text          text not null,
  erledigt      boolean not null default false,
  created_at    timestamptz not null default now()
);
