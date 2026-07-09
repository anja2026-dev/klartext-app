-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration
-- Tages-Barometer (FM-05): TK als Quelle zulassen
--
-- barometer_kind existiert bereits (0007_barometer.sql) und ist für
-- das Fallmanagement-Formular voll kompatibel: farbe deckt bereits
-- exakt die geforderten 5 Stufen ab (gruen/gelb/orange/rot/grau), RLS
-- (barometer_kind_tk_admin_all) gewährt TK/Admin bereits vollen
-- Zugriff (for all). Einzige Lücke: source erlaubt bisher nur
-- 'kind-self' (Kind-Selbstauskunft) und 'ingra', nicht aber einen
-- direkt von TK im Fallmanagement erfassten Eintrag - wird hier um
-- 'tk' ergänzt, damit die Quelle korrekt zugeordnet bleibt statt sie
-- fälschlich als 'ingra' zu speichern.
-- ════════════════════════════════════════════════════════════

alter table barometer_kind drop constraint barometer_kind_source_check;
alter table barometer_kind add constraint barometer_kind_source_check
  check (source in ('kind-self','ingra','tk'));
