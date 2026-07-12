-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration
-- Nachtrag/Dokumentation: krankmeldungen wurde bereits live auf das
-- "neue Schema" umgestellt
--
-- Die Migrationen 0018_krankmeldungen.sql und 0025_krankmeldungen_rls.sql
-- im Repo spiegeln nicht mehr den tatsächlichen Live-Zustand wider.
-- Laut direkter Prüfung der Live-DB (SQL-Editor) gilt inzwischen:
--   - krankmeldungen.ingra_id  -> FK auf ingra(id)   (nicht profiles(id))
--   - krankmeldungen.kind_id   -> FK auf "Kinder"(id) (nicht kinder(id))
-- Passend dazu wurde KLARTEXT_Krankmeldung.html umgestellt: ladeMeld()/
-- speichKrank() lösen ingra_id jetzt über aktuelleIngraId() auf
-- (E-Mail aus der Auth-Session -> ingra.id), nicht mehr über die rohe
-- Auth-UID. weiterleitungen.von_profil bleibt unverändert die echte
-- Auth-UID (dort existiert diese Diskrepanz nicht).
--
-- WICHTIG - Vertrauenswürdigkeit dieser Migration:
-- Ich habe KEINEN Zugriff auf die Live-Datenbank und kann die exakte
-- Formulierung der unten stehenden RLS-Policies nicht gegen die
-- tatsächlich aktiven Policies verifizieren. Die FK-Ziele (ingra_id ->
-- ingra(id), kind_id -> "Kinder"(id)) wurden explizit bestätigt: dieser
-- Teil ist verlässlich. Die RLS-Policies unten sind eine PLAUSIBLE
-- REKONSTRUKTION nach dem in dieser Session bereits etablierten Muster
-- (Auflösung von auth.uid() -> ingra.id über person_auth_map, analog
-- zu aktuelleIngraId() im Tagesjournal) - vor dem Ausführen unbedingt
-- gegen die tatsächlich aktive Policy-Definition in der Live-DB prüfen
-- und bei Abweichungen anpassen, statt blind auszuführen.
--
-- Diese Migration NICHT ausführen, wenn die Live-DB bereits entsprechend
-- geändert ist (sonst schlagen "add constraint"/"create policy" fehl,
-- weil die Ziele schon existieren) - sie dient hier primär als
-- schriftliche Dokumentation des Ist-Zustands fürs Repo.
-- ════════════════════════════════════════════════════════════

-- ── FKs auf das neue Schema umstellen ──────────────────────────
alter table krankmeldungen drop constraint if exists krankmeldungen_ingra_id_fkey;
alter table krankmeldungen drop constraint if exists krankmeldungen_kind_id_fkey;

alter table krankmeldungen
  add constraint krankmeldungen_ingra_id_fkey foreign key (ingra_id) references ingra(id);
alter table krankmeldungen
  add constraint krankmeldungen_kind_id_fkey foreign key (kind_id) references "Kinder"(id);

-- ── RLS: ingra_id ist jetzt ingra(id), nicht mehr auth.uid() direkt -
-- Auflösung der eigenen ingra_id über person_auth_map (auth_uid -> email
-- -> ingra.id), analog zu aktuelleIngraId() in KLARTEXT_Krankmeldung.html/
-- KLARTEXT_Tagesjournal.html. Rekonstruktion, siehe Hinweis oben.
drop policy if exists krankmeldungen_select on krankmeldungen;
drop policy if exists krankmeldungen_insert on krankmeldungen;
drop policy if exists krankmeldungen_update on krankmeldungen;
drop policy if exists krankmeldungen_delete on krankmeldungen;

create policy krankmeldungen_select
  on krankmeldungen for select
  to authenticated
  using (
    ingra_id in (
      select i.id from ingra i
      join person_auth_map m on m.email = i.email
      where m.auth_uid = auth.uid()
    )
    or exists (
      select 1 from person_auth_map m
      where m.auth_uid = auth.uid() and m.role in ('tk', 'admin')
    )
  );

create policy krankmeldungen_insert
  on krankmeldungen for insert
  to authenticated
  with check (
    ingra_id in (
      select i.id from ingra i
      join person_auth_map m on m.email = i.email
      where m.auth_uid = auth.uid()
    )
  );

create policy krankmeldungen_update
  on krankmeldungen for update
  to authenticated
  using (
    ingra_id in (
      select i.id from ingra i
      join person_auth_map m on m.email = i.email
      where m.auth_uid = auth.uid()
    )
  )
  with check (
    ingra_id in (
      select i.id from ingra i
      join person_auth_map m on m.email = i.email
      where m.auth_uid = auth.uid()
    )
  );

create policy krankmeldungen_delete
  on krankmeldungen for delete
  to authenticated
  using (
    ingra_id in (
      select i.id from ingra i
      join person_auth_map m on m.email = i.email
      where m.auth_uid = auth.uid()
    )
  );
