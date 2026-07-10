-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration
-- Fehlende SELECT-Policies für "Kinder", "INGRA", "TK" nachziehen
--
-- Per Supabase-Dashboard bestätigt: "Kinder" (groß) und "INGRA" haben
-- RLS aktiv, aber KEINE Policy - die Data API liefert dort daher
-- grundsätzlich nichts zurück, unabhängig von Login oder vorhandenen
-- Daten. Das ist die Ursache dafür, dass neu angelegte Test-Kinder/
-- INGRA-Profile im Frontend nirgends erscheinen.
--
-- Die alte Tabelle "kinder" (klein) hat bereits eine funktionierende
-- Blanket-Policy authenticated_can_select_kinder. Dieses neue Schema
-- (TK/INGRA/Kinder) hat noch keine Mehrmandanten-Feingranularität wie
-- die migrierten Tabellen aus 0002/0003 (kein traeger_id-Bezug über
-- profiles, keine FK auf auth.users) - Zugriffskontrolle läuft
-- bislang über sessionStorage-Seiten-Guards im Frontend, nicht über
-- RLS. Diese Migration zieht daher dieselbe simple Blanket-Logik nach,
-- die bereits an anderer Stelle im Schema existiert (vgl.
-- qualifikationen_read_all in 0001_auth_rollen.sql: for select to
-- authenticated using (true)).
--
-- "TK" wird aktuell von keinem Frontend-Code direkt gelesen, wurde
-- aber im selben Dashboard-Vorgang wie "Kinder"/"INGRA" angelegt und
-- vermutlich hat dieselbe Lücke - Policy wird hier vorsorglich mit
-- ergänzt (rein additiv, kein Risiko falls bereits etwas existiert).
-- ════════════════════════════════════════════════════════════

create policy authenticated_can_select_kinder
  on "Kinder" for select
  to authenticated
  using (true);

create policy authenticated_can_select_ingra
  on "INGRA" for select
  to authenticated
  using (true);

create policy authenticated_can_select_tk
  on "TK" for select
  to authenticated
  using (true);
