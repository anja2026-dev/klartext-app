-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration · Phase 1
-- RLS: listen_eintraege
--
-- INGRA: eigene Einträge (ersteller_id) lesen+schreiben.
-- TK/Admin: alles lesen+schreiben.
-- Eltern/Trainer: kein Zugriff (keine Policy). Kein anonymer Zugriff.
-- (Kein kind_id in dieser Tabelle -> keine ingra_kinder-Klausel nötig.)
-- ════════════════════════════════════════════════════════════

alter table listen_eintraege enable row level security;

create policy listen_eintraege_select
  on listen_eintraege for select
  to authenticated
  using (
    ersteller_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  );

create policy listen_eintraege_insert
  on listen_eintraege for insert
  to authenticated
  with check (
    ersteller_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  );

create policy listen_eintraege_update
  on listen_eintraege for update
  to authenticated
  using (
    ersteller_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  )
  with check (
    ersteller_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  );

create policy listen_eintraege_delete
  on listen_eintraege for delete
  to authenticated
  using (
    ersteller_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  );
