-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration · Phase 3
-- Wochenplan-Grundstruktur
--
-- Eigenständig von kinder_wochenplan (0002, feste Mo-Fr-Einsatzzeiten
-- je Kind): wochenplan bildet einen versionierten Plan je Kalenderwoche
-- ab, dessen Einträge optional auf eine konkrete Maßnahme verweisen
-- können.
--
-- Reine Datenstruktur. Noch keine Frontend-Anbindung.
-- ════════════════════════════════════════════════════════════

create table wochenplan (
  id           uuid primary key default gen_random_uuid(),
  kind_id      uuid not null references kinder(id),
  woche        date not null,   -- Montag der jeweiligen Kalenderwoche als Identifikator
  erstellt_am  timestamptz not null default now()
);

create table wochenplan_eintraege (
  id             uuid primary key default gen_random_uuid(),
  wochenplan_id  uuid not null references wochenplan(id) on delete cascade,
  tag            text not null check (tag in ('MO','DI','MI','DO','FR','SA','SO')),
  startzeit      time,
  endzeit        time,
  beschreibung   text,
  massnahme_id   uuid references fall_massnahmen(id)
);

-- ── RLS ──────────────────────────────────────────────────────────
-- Nur "sehen" wurde für INGRA/Trainer/Eltern gefordert -> read-only.
-- Schreiben bleibt vorerst TK/Admin vorbehalten (gleiches Muster wie
-- die Korrektur in 0005 für fall_risikostatus/fall_timeline).

alter table wochenplan enable row level security;
alter table wochenplan_eintraege enable row level security;

create policy wochenplan_tk_admin_all
  on wochenplan for all
  using (
    exists (
      select 1 from kinder k
      join profiles p on p.traeger_id = k.traeger_id
      where k.id = wochenplan.kind_id
        and p.id = auth.uid()
        and p.rolle in ('tk','admin')
    )
  );

create policy wochenplan_select_ingra
  on wochenplan for select
  using (exists (select 1 from ingra_kinder ik where ik.kind_id = wochenplan.kind_id and ik.ingra_id = auth.uid()));

create policy wochenplan_select_trainer
  on wochenplan for select
  using (exists (select 1 from trainer_kinder tk where tk.kind_id = wochenplan.kind_id and tk.trainer_id = auth.uid()));

create policy wochenplan_select_eltern
  on wochenplan for select
  using (exists (select 1 from eltern_kinder ek where ek.kind_id = wochenplan.kind_id and ek.eltern_id = auth.uid()));

-- wochenplan_eintraege erbt Sichtbarkeit vom zugehörigen Wochenplan
-- (die EXISTS-Subquery unterliegt selbst den obigen Policies auf wochenplan).
create policy wochenplan_eintraege_tk_admin_all
  on wochenplan_eintraege for all
  using (
    exists (
      select 1 from wochenplan w
      join kinder k on k.id = w.kind_id
      join profiles p on p.traeger_id = k.traeger_id
      where w.id = wochenplan_eintraege.wochenplan_id
        and p.id = auth.uid()
        and p.rolle in ('tk','admin')
    )
  );

create policy wochenplan_eintraege_select
  on wochenplan_eintraege for select
  using (exists (select 1 from wochenplan w where w.id = wochenplan_eintraege.wochenplan_id));
