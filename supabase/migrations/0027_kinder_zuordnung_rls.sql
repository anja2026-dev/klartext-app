-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration
-- RLS: kinder_zuordnung
--
-- admin_all: auth.role() liefert nur 'authenticated'/'anon'/'service_role'
-- (JWT-Ebene), niemals die App-Rolle 'admin' aus profiles.rolle - eine
-- Policy mit auth.role() = 'admin' würde daher nie greifen. Wie in
-- allen anderen RLS-Migrationen dieses Schemas (z.B. zeiteintraege_rls,
-- krankmeldungen_rls) stattdessen über profiles.rolle geprüft.
-- ════════════════════════════════════════════════════════════

alter table kinder_zuordnung enable row level security;

create policy "admin_all" on kinder_zuordnung
  for all
  using (
    exists (select 1 from profiles p where p.id = auth.uid() and p.rolle = 'admin')
  );

create policy "tk_manage" on kinder_zuordnung
  for all
  using ( tk_id = auth.uid() );

create policy "ingra_read" on kinder_zuordnung
  for select
  using ( ingra_id = auth.uid() );

create policy "trainer_read" on kinder_zuordnung
  for select
  using ( trainer_id = auth.uid() );
