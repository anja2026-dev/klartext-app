-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration · Phase 1
-- RLS: notizen
--
-- INGRA: eigene Einträge (ersteller_id) lesen+schreiben.
-- TK/Admin: alles lesen+schreiben.
-- Eltern/Trainer: kein Zugriff (keine Policy). Kein anonymer Zugriff.
-- (Kein kind_id in dieser Tabelle -> keine ingra_kinder-Klausel nötig.)
-- ════════════════════════════════════════════════════════════

alter table notizen enable row level security;

create policy notizen_select
  on notizen for select
  to authenticated
  using (
    ersteller_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  );

create policy notizen_insert
  on notizen for insert
  to authenticated
  with check (
    ersteller_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  );

create policy notizen_update
  on notizen for update
  to authenticated
  using (
    ersteller_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  )
  with check (
    ersteller_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  );

create policy notizen_delete
  on notizen for delete
  to authenticated
  using (
    ersteller_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  );
