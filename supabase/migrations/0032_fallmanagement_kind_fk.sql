-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration
-- Fallmanagement/Kinderzuordnung auf "Kinder" (groß) umstellen
--
-- "kinder" (klein) wurde nie mit echten Daten befüllt - kein Insert
-- in kinder existiert im Frontend-Code, keine Migration hat je Daten
-- hineingeschrieben. "Kinder" (groß) ist die einzige echte/vollständig
-- gepflegte Tabelle. Analog zu 0031_neues_schema_kind_fk.sql (dort für
-- die 5 INGRA-Alltagsmodule) werden hier die verbleibenden
-- Fremdschlüssel auf "Kinder" umgehängt: fallakten, fall_massnahmen,
-- barometer_kind, kinder_zuordnung - die Tabellen, die
-- TK_Fallmanagement.html und TK_Kinderzuordnung.html beschreiben.
--
-- "kinder" (klein) wird NICHT gelöscht - bleibt als Sicherheitsnetz
-- unbenutzt bestehen, falls doch irgendwo referenziert.
-- ════════════════════════════════════════════════════════════

alter table fallakten drop constraint fallakten_kind_id_fkey;
alter table fallakten add constraint fallakten_kind_id_fkey
  foreign key (kind_id) references "Kinder"(id);

alter table fall_massnahmen drop constraint fall_massnahmen_kind_id_fkey;
alter table fall_massnahmen add constraint fall_massnahmen_kind_id_fkey
  foreign key (kind_id) references "Kinder"(id);

alter table barometer_kind drop constraint barometer_kind_kind_id_fkey;
alter table barometer_kind add constraint barometer_kind_kind_id_fkey
  foreign key (kind_id) references "Kinder"(id);

alter table kinder_zuordnung drop constraint kinder_zuordnung_kind_id_fkey;
alter table kinder_zuordnung add constraint kinder_zuordnung_kind_id_fkey
  foreign key (kind_id) references "Kinder"(id) on delete cascade;
