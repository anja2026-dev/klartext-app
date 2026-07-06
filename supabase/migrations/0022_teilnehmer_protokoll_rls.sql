-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration · Phase 1
-- RLS: teilnehmer_protokoll
--
-- INGRA: eigene Einträge (ersteller_id) lesen+schreiben.
-- TK/Admin: alles lesen+schreiben.
-- Eltern/Trainer: kein Zugriff (keine Policy). Kein anonymer Zugriff.
-- (Kein kind_id in dieser Tabelle -> keine ingra_kinder-Klausel nötig.)
-- ════════════════════════════════════════════════════════════

alter table teilnehmer_protokoll enable row level security;

create policy teilnehmer_protokoll_select
  on teilnehmer_protokoll for select
  to authenticated
  using (
    ersteller_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  );

create policy teilnehmer_protokoll_insert
  on teilnehmer_protokoll for insert
  to authenticated
  with check (
    ersteller_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  );

create policy teilnehmer_protokoll_update
  on teilnehmer_protokoll for update
  to authenticated
  using (
    ersteller_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  )
  with check (
    ersteller_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  );

create policy teilnehmer_protokoll_delete
  on teilnehmer_protokoll for delete
  to authenticated
  using (
    ersteller_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  );
