-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration
-- Antwort-Feld für weiterleitungen (TK-Inbox)
--
-- Firebase `forward` hatte antwort/antwortVon/antwortTs/beantwortet -
-- dieses Äquivalent fehlte bisher in weiterleitungen. Ergänzt um die
-- TK-Inbox in KLARTEXT_Weiterleitungen.html wieder mit Antwortfunktion
-- auszustatten (Status wechselt beim Antworten auf 'erledigt').
-- ════════════════════════════════════════════════════════════

alter table weiterleitungen add column antwort text;
alter table weiterleitungen add column beantwortet_von text;
alter table weiterleitungen add column beantwortet_am timestamptz;
