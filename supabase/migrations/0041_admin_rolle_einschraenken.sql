-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration
-- Admin-Rolle in person_auth_map serverseitig auf ein Konto beschränken
--
-- Bisher konnte jede eingeloggte Person sich über person_auth_map_insert_own
-- / person_auth_map_update_own (0036) eine beliebige Rolle selbst zuweisen,
-- inklusive 'admin' - nur clientseitig in KLARTEXT_Login.html seit Kurzem
-- auf klartext.mentoring@gmx.de beschränkt (reiner UI-Schutz, keine echte
-- Durchsetzung). Diese Migration schließt die Lücke serverseitig: die
-- 'admin'-Rolle wird per RLS nur noch akzeptiert, wenn die authentifizierte
-- JWT-E-Mail exakt klartext.mentoring@gmx.de ist. Alle anderen Rollen
-- (ingra, ingra-beta, tk, trainer, lk, eltern, ...) bleiben unverändert frei
-- wählbar - es wird ausschließlich der 'admin'-Fall zusätzlich eingeschränkt.
--
-- "is distinct from" statt "<>" für den Rollen-Vergleich, damit ein
-- (praktisch nicht vorkommendes, aber theoretisch mögliches) NULL in role
-- nicht durch NULL-Semantik versehentlich die gesamte WITH-CHECK-Bedingung
-- durchfallen lässt (RLS akzeptiert eine Zeile nur bei explizit TRUE).
--
-- Bewusst NICHT Teil dieser Migration: eine Bereinigung bereits bestehender
-- person_auth_map-Zeilen mit role = 'admin' für andere E-Mail-Adressen.
-- RLS wirkt nur auf künftige INSERT/UPDATE-Versuche, nicht rückwirkend auf
-- schon vorhandene Daten. Prüfen lässt sich das live mit:
--   select email, role from person_auth_map where role = 'admin';
-- Falls dort weitere Zeilen als klartext.mentoring@gmx.de auftauchen,
-- müssten die separat manuell bereinigt werden (nicht Teil dieses Fixes).
--
-- Additiv, nichts Bestehendes gelöscht - ersetzt nur die WITH-CHECK-
-- Bedingung der beiden Schreib-Policies aus 0036 (drop + create, gleiches
-- Muster wie in 0037_krankmeldungen_schema_korrektur.sql). Wird manuell im
-- Supabase SQL Editor ausgeführt, nicht automatisch.
-- ════════════════════════════════════════════════════════════

drop policy if exists person_auth_map_insert_own on person_auth_map;

create policy person_auth_map_insert_own
  on person_auth_map for insert
  to authenticated
  with check (
    auth_uid = auth.uid()
    and email = auth.jwt() ->> 'email'
    and (
      role is distinct from 'admin'
      or auth.jwt() ->> 'email' = 'klartext.mentoring@gmx.de'
    )
  );

drop policy if exists person_auth_map_update_own on person_auth_map;

create policy person_auth_map_update_own
  on person_auth_map for update
  to authenticated
  using (auth_uid = auth.uid())
  with check (
    auth_uid = auth.uid()
    and email = auth.jwt() ->> 'email'
    and (
      role is distinct from 'admin'
      or auth.jwt() ->> 'email' = 'klartext.mentoring@gmx.de'
    )
  );
