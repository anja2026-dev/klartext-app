-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration
-- person_auth_map: E-Mail → echte Supabase-Auth-UID
--
-- Erster Baustein für eine echte KlarApp-Kontaktliste. Die Tabellen
-- des "neuen Schemas" (ingra/"TK"/"Kinder", siehe 0034) haben KEINE
-- Verknüpfung zu auth.users - ihre Zeilen werden nur per E-Mail-
-- Abgleich der eigenen Login-Session zugeordnet (vgl. aktuelleIngraId()
-- in KLARTEXT_Tagesjournal.html/KLARTEXT_Zeitkonto.html etc.). Für eine
-- echte KlarApp-Kontaktliste wird aber die auth.users.id ANDERER
-- Personen benötigt, um Firebase-Konversationen (conv.members[uid])
-- korrekt zu verlinken - die gibt es bisher nirgends zum Nachschlagen.
--
-- Diese Tabelle schließt genau diese Lücke: jede Person schreibt bei
-- jedem Login ihre eigene Zeile (E-Mail → eigene auth.users.id,
-- Anzeigename, aktuell gewählte Rolle).
--
-- role ist bewusst text statt des klartext_rolle-Enums aus 0001, da
-- das Login-Rollen-Dropdown auch "ingra-beta" kennt - ein Wert, den
-- das Enum nicht abdeckt.
--
-- Reine Datenstruktur - wird manuell im SQL-Editor ausgeführt, nicht
-- automatisch.
-- ════════════════════════════════════════════════════════════

create table person_auth_map (
  email     text primary key,
  auth_uid  uuid not null,
  name      text,
  role      text
);

comment on table person_auth_map is
  'E-Mail -> echte auth.users.id, gepflegt bei jedem Login. Baustein für die echte KlarApp-Kontaktliste (siehe CHAT_New.html).';

alter table person_auth_map enable row level security;

-- Alle eingeloggten Nutzer dürfen die komplette Kontaktliste lesen
-- (gleiche Blanket-Logik wie authenticated_can_select_ingra in 0034).
create policy person_auth_map_select_all
  on person_auth_map for select
  to authenticated
  using (true);

-- Jede Person darf nur ihre EIGENE Zeile anlegen: auth_uid muss der
-- eigenen Auth-UID entsprechen UND email muss der eigenen, im JWT
-- hinterlegten Login-E-Mail entsprechen. Nur auth_uid = auth.uid() zu
-- prüfen reicht nicht - ohne den email-Abgleich könnte sich jemand
-- eine fremde, noch nie eingeloggte E-Mail-Adresse mit der eigenen UID
-- vorab sichern und damit die echte Person später aussperren.
create policy person_auth_map_insert_own
  on person_auth_map for insert
  to authenticated
  with check (
    auth_uid = auth.uid()
    and email = auth.jwt() ->> 'email'
  );

-- Und beim Login-Upsert entsprechend auch nur die eigene Zeile
-- aktualisieren dürfen. email ebenfalls an den JWT-Claim gebunden -
-- sonst könnte die eigene, bestehende Zeile per UPDATE ... SET email
-- auf eine fremde E-Mail-Adresse umbenannt werden (gleiche Lücke wie
-- bei person_auth_map_insert_own, nur über UPDATE statt INSERT).
create policy person_auth_map_update_own
  on person_auth_map for update
  to authenticated
  using (auth_uid = auth.uid())
  with check (
    auth_uid = auth.uid()
    and email = auth.jwt() ->> 'email'
  );
