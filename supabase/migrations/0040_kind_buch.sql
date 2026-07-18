-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration
-- "Unser Buch" - Sammlung von Beobachtungen/Aussagen zu einem Kind,
-- gegliedert nach Kategorie (mag/hilft/stress/staerken/sonstiges)
--
-- Additiv, nichts Bestehendes verändert oder gelöscht. Wird manuell im
-- Supabase SQL Editor ausgeführt, nicht automatisch.
-- ════════════════════════════════════════════════════════════

create table kind_buch_eintraege (
  id uuid primary key default gen_random_uuid(),
  kind_id uuid not null references "Kinder"(id),
  kategorie text not null check (kategorie in ('mag','hilft','stress','staerken','sonstiges')),
  text text not null,
  verfasst_von text not null default 'ingra' check (verfasst_von in ('kind','ingra')),
  ingra_id uuid references ingra(id),
  erstellt_am timestamptz not null default now()
);

alter table kind_buch_eintraege enable row level security;

-- Gleiches Blanket-Muster wie tagesjournal_eintraege (bereits live
-- geprüft: authenticated = voller Zugriff, Kind-Zuordnung läuft
-- bewusst im Frontend, nicht in RLS — Konsistenz mit dem Rest des
-- neuen Schemas, kein neues Muster einführen):
create policy authenticated_can_select_kind_buch_eintraege
  on kind_buch_eintraege for select to authenticated using (true);
create policy authenticated_can_insert_kind_buch_eintraege
  on kind_buch_eintraege for insert to authenticated with check (true);
create policy authenticated_can_update_kind_buch_eintraege
  on kind_buch_eintraege for update to authenticated using (true) with check (true);
create policy authenticated_can_delete_kind_buch_eintraege
  on kind_buch_eintraege for delete to authenticated using (true);
