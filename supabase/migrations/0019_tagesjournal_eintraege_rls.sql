-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration · Phase 1
-- RLS: tagesjournal_eintraege
--
-- INGRA: eigene Einträge (ersteller_id) lesen+schreiben.
-- Zugewiesene INGRA (ingra_kinder): kind_id-Einträge nur SEHEN.
-- TK/Admin: alles lesen+schreiben.
-- Eltern/Trainer: kein Zugriff (keine Policy). Kein anonymer Zugriff
-- (alle Policies "to authenticated").
-- ════════════════════════════════════════════════════════════

alter table tagesjournal_eintraege enable row level security;

create policy tagesjournal_eintraege_select
  on tagesjournal_eintraege for select
  to authenticated
  using (
    ersteller_id = auth.uid()
    or (
      kind_id is not null
      and exists (
        select 1 from ingra_kinder ik
        where ik.kind_id = tagesjournal_eintraege.kind_id and ik.ingra_id = auth.uid()
      )
    )
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  );

create policy tagesjournal_eintraege_insert
  on tagesjournal_eintraege for insert
  to authenticated
  with check (
    ersteller_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  );

create policy tagesjournal_eintraege_update
  on tagesjournal_eintraege for update
  to authenticated
  using (
    ersteller_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  )
  with check (
    ersteller_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  );

create policy tagesjournal_eintraege_delete
  on tagesjournal_eintraege for delete
  to authenticated
  using (
    ersteller_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  );
