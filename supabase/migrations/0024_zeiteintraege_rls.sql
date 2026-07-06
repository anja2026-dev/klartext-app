-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration · Phase 1
-- RLS: zeiteintraege
--
-- INGRA: eigene Einträge (ingra_id) lesen+schreiben.
-- Zugewiesene INGRA (ingra_kinder): kind_id-Einträge nur SEHEN.
-- TK/Admin: alles lesen+schreiben.
-- Eltern/Trainer: kein Zugriff (keine Policy). Kein anonymer Zugriff.
-- ════════════════════════════════════════════════════════════

alter table zeiteintraege enable row level security;

create policy zeiteintraege_select
  on zeiteintraege for select
  to authenticated
  using (
    ingra_id = auth.uid()
    or (
      kind_id is not null
      and exists (
        select 1 from ingra_kinder ik
        where ik.kind_id = zeiteintraege.kind_id and ik.ingra_id = auth.uid()
      )
    )
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  );

create policy zeiteintraege_insert
  on zeiteintraege for insert
  to authenticated
  with check (
    ingra_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  );

create policy zeiteintraege_update
  on zeiteintraege for update
  to authenticated
  using (
    ingra_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  )
  with check (
    ingra_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  );

create policy zeiteintraege_delete
  on zeiteintraege for delete
  to authenticated
  using (
    ingra_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  );
