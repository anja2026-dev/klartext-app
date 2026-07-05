-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration · Phase 3
-- Barometer-Grundstruktur
--
-- barometer_kind ersetzt Firebase /barometer_kind (BAROMETER_KIND.html)
-- und löst dabei den in der Analyse gefundenen Fehler, dass der
-- lokale Verlauf (localStorage['baro_kind_eintraege']) keine childId
-- führte und Kinder so in derselben Liste vermischt wurden.
--
-- barometer_ingra ist neu (BAROMETER_INGRA.html nutzt bisher nur
-- localStorage, kein Firebase-Gegenstück) und folgt dem in
-- KLARTEXT_Vertretungsassistent_Architektur.html dokumentierten
-- Schema (Stufe 1–6, für die Vertretungs-Scoring-Logik).
--
-- Reine Datenstruktur. Noch keine Frontend-Anbindung.
-- ════════════════════════════════════════════════════════════

create table barometer_kind (
  id           uuid primary key default gen_random_uuid(),
  kind_id      uuid not null references kinder(id),
  farbe        text not null check (farbe in ('gruen','gelb','orange','rot','grau')),
  notiz        text,
  source       text not null check (source in ('kind-self','ingra')),
  created_at   timestamptz not null default now()
);

create table barometer_ingra (
  id           uuid primary key default gen_random_uuid(),
  ingra_id     uuid not null references profiles(id),
  datum        date not null default current_date,
  uhrzeit      time not null default current_time,
  stufe        smallint check (stufe between 1 and 6),
  farbe        text check (farbe in ('gruen','gelb','rot')),
  notiz        text,
  created_at   timestamptz not null default now()
);

comment on table barometer_ingra is
  'Tagesaktuelle Selbsteinschätzung der INGRA, siehe Vertretungslogik (Stufe 1-2 grün · 3-4 gelb · 5-6 rot).';

-- ── RLS: barometer_kind ──────────────────────────────────────────
-- Schreiben: zugewiesene INGRA (auch wenn das Kind selbst am Gerät
-- wählt, trägt die begleitende INGRA ein) + TK/Admin. Kein Eltern-Zugriff.
alter table barometer_kind enable row level security;

create policy barometer_kind_tk_admin_all
  on barometer_kind for all
  using (
    exists (
      select 1 from kinder k
      join profiles p on p.traeger_id = k.traeger_id
      where k.id = barometer_kind.kind_id
        and p.id = auth.uid()
        and p.rolle in ('tk','admin')
    )
  );

create policy barometer_kind_ingra_select
  on barometer_kind for select
  using (exists (select 1 from ingra_kinder ik where ik.kind_id = barometer_kind.kind_id and ik.ingra_id = auth.uid()));

create policy barometer_kind_ingra_insert
  on barometer_kind for insert
  with check (exists (select 1 from ingra_kinder ik where ik.kind_id = barometer_kind.kind_id and ik.ingra_id = auth.uid()));

-- ── RLS: barometer_ingra ─────────────────────────────────────────
-- Jede INGRA verwaltet ausschließlich die eigene Selbsteinschätzung;
-- TK/Admin lesen trägerweit (Grundlage der Vertretungs-Scoring-Logik).
alter table barometer_ingra enable row level security;

create policy barometer_ingra_own_all
  on barometer_ingra for all
  using (ingra_id = auth.uid());

create policy barometer_ingra_tk_admin_select
  on barometer_ingra for select
  using (
    exists (
      select 1 from profiles p_self
      join profiles p_tk on p_tk.traeger_id = p_self.traeger_id
      where p_self.id = barometer_ingra.ingra_id
        and p_tk.id = auth.uid()
        and p_tk.rolle in ('tk','admin')
    )
  );
