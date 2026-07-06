-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration · Phase 1
-- RLS: krankmeldungen
--
-- INGRA: eigene Meldungen (ingra_id) lesen+schreiben.
-- Zugewiesene INGRA (ingra_kinder): kind_id-Einträge (typ='kind') nur SEHEN.
-- TK/Admin: alles lesen+schreiben.
-- Eltern/Trainer: kein Zugriff (keine Policy). Kein anonymer Zugriff.
-- ════════════════════════════════════════════════════════════

alter table krankmeldungen enable row level security;

create policy krankmeldungen_select
  on krankmeldungen for select
  to authenticated
  using (
    ingra_id = auth.uid()
    or (
      kind_id is not null
      and exists (
        select 1 from ingra_kinder ik
        where ik.kind_id = krankmeldungen.kind_id and ik.ingra_id = auth.uid()
      )
    )
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  );

create policy krankmeldungen_insert
  on krankmeldungen for insert
  to authenticated
  with check (
    ingra_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  );

create policy krankmeldungen_update
  on krankmeldungen for update
  to authenticated
  using (
    ingra_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  )
  with check (
    ingra_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  );

create policy krankmeldungen_delete
  on krankmeldungen for delete
  to authenticated
  using (
    ingra_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  );
