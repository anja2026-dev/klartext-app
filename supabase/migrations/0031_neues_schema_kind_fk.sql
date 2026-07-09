-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration
-- Umstieg auf neues Schema (TK / INGRA / Kinder) für die 7 INGRA-
-- Alltagsmodule (Tagesjournal, Notizblock, Listen, Teilnehmer-
-- Protokoll, Zeitkonto, Krankmeldung, Urlaubsantrag)
--
-- Die Tabellen TK / INGRA / Kinder (großes K) wurden bereits separat
-- in Supabase angelegt und ersetzen für diese Module profiles/kinder/
-- kinder_zuordnung. ACHTUNG: "Kinder" ist ein eigener, quotierter
-- Bezeichner - eine andere Tabelle als das bestehende "kinder"
-- (klein), das von TK_Fallmanagement.html, BAROMETER_KIND.html u.a.
-- weiterhin unverändert genutzt wird und hier nicht angefasst wird.
--
-- kind_id auf tagesjournal_eintraege/weiterleitungen/krankmeldungen/
-- urlaubsantraege/zeiteintraege verwies bisher per Fremdschlüssel auf
-- "kinder" (klein). Ohne Anpassung würde jedes Insert mit einer
-- Kinder.id (neues Schema, unabhängig generierte UUIDs) an dieser
-- Constraint scheitern. Fremdschlüssel werden daher auf "Kinder"
-- (groß) umgehängt - nur bei den Tabellen dieser 7 Module, nicht bei
-- anderen (z.B. fallakten, barometer_kind), die weiterhin "kinder"
-- (klein) verwenden.
-- ════════════════════════════════════════════════════════════

alter table tagesjournal_eintraege drop constraint tagesjournal_eintraege_kind_id_fkey;
alter table tagesjournal_eintraege add constraint tagesjournal_eintraege_kind_id_fkey
  foreign key (kind_id) references "Kinder"(id);

alter table weiterleitungen drop constraint weiterleitungen_kind_id_fkey;
alter table weiterleitungen add constraint weiterleitungen_kind_id_fkey
  foreign key (kind_id) references "Kinder"(id);

alter table krankmeldungen drop constraint krankmeldungen_kind_id_fkey;
alter table krankmeldungen add constraint krankmeldungen_kind_id_fkey
  foreign key (kind_id) references "Kinder"(id);

alter table urlaubsantraege drop constraint urlaubsantraege_kind_id_fkey;
alter table urlaubsantraege add constraint urlaubsantraege_kind_id_fkey
  foreign key (kind_id) references "Kinder"(id);

alter table zeiteintraege drop constraint zeiteintraege_kind_id_fkey;
alter table zeiteintraege add constraint zeiteintraege_kind_id_fkey
  foreign key (kind_id) references "Kinder"(id);

-- teilnehmer_protokoll hatte bisher keinen Kind-Bezug (nur ein freies
-- name-Textfeld "Name der Teilnehmerin / des Teilnehmers"). Neue,
-- optionale Spalte für die Verknüpfung mit einem konkreten Kind - das
-- bestehende name-Feld bleibt erhalten (weiterhin nutzbar, wenn der/die
-- Teilnehmer:in kein erfasstes Kind ist, z.B. bei einer Fortbildung).
alter table teilnehmer_protokoll add column kind_id uuid references "Kinder"(id);
