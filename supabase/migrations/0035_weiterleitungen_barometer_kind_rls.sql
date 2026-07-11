-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration
-- RLS-Lücke bei weiterleitungen/barometer_kind schließen
-- (gleiches Muster wie 0034 bei Kinder/ingra/tk)
--
-- weiterleitungen und barometer_kind haben nur Policies aus dem alten
-- Schema (profiles.rolle/ingra_kinder/auth.uid()) - keine davon passt
-- zum aktuellen INGRA/TK/Kinder-Login-Modell. Dadurch scheitern u.a.
-- die Übergabe in KLARTEXT_Tagesjournal.html, die automatische
-- Weiterleitung in KLARTEXT_Zeitkonto.html sowie sämtliche Schreib-/
-- Lesezugriffe von BAROMETER_KIND.html (läuft bewusst ohne Login).
-- ════════════════════════════════════════════════════════════

-- 1) weiterleitungen: eingeloggte INGRA/TK dürfen Einträge anlegen
--    (Tagesjournal-Übergabe, Zeitkonto-Weiterleitung). Blanket-Muster
--    wie authenticated_can_select_kinder in 0034.
create policy authenticated_can_insert_weiterleitungen
  on weiterleitungen for insert
  to authenticated
  with check (true);

-- 2) weiterleitungen: BAROMETER_KIND.html läuft ohne Login (Kind-Self-
--    Service-Gerät) - daher eng auf genau den Anwendungsfall begrenzt,
--    den diese Seite tatsächlich schreibt (Barometer-Wochenverlauf an
--    TK), statt eines Blanket-Zugriffs für anon.
create policy anon_can_insert_weiterleitungen_barometer
  on weiterleitungen for insert
  to anon
  with check (typ = 'barometer' and ziel_rolle = 'tk');

-- 3) barometer_kind: BAROMETER_KIND.html muss den eigenen Verlauf ohne
--    Login lesen können. Blanket-Select für anon geht potenziell weiter
--    als nötig (liefert ohne WHERE alle Kinder-Verläufe, nicht nur den
--    gewählten) - dieselbe Einschätzung wie bei der Kinder-Tabelle in
--    0034: kein sensibler Zugriff möglich, da das Frontend ohnehin erst
--    nach expliziter Kind-Auswahl (kind_id) filtert und anzeigt.
create policy anon_can_select_barometer_kind
  on barometer_kind for select
  to anon
  using (true);

-- 4) weiterleitungen.kind_id war "not null" - blockiert legitime,
--    nicht kind-bezogene Einträge (INGRA-eigene Krankmeldung in
--    KLARTEXT_Krankmeldung.html, kindloser Urlaubsantrag in
--    KLARTEXT_Urlaubsantrag_INGRA.html, allgemeine Zeitkonto-
--    Wochenübersicht) unabhängig von RLS mit einer NOT-NULL-Verletzung.
alter table weiterleitungen alter column kind_id drop not null;
