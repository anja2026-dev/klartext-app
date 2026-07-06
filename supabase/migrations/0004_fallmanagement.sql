-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration · Phase 3
-- Fallmanagement-Grundstruktur
--
-- Vereint zwei in der Analyse gefundene, inkompatible Implementierungen:
--   - Fallmanagement-Assistent.html  (localStorage-Key 'fm-caseFile',
--     kein Kind-Bezug, immer nur EIN Fall gleichzeitig)
--   - TK_Fallmanagement.html         (localStorage-Key 'tkr-case_file',
--     anderes Format, ebenfalls ohne Kind-Bezug)
-- sowie FM_Massnahmen_DB.html (eigene, isolierte localStorage-Liste
-- ohne jeden Kind-Bezug) in eine zusammenhängende, kind-bezogene
-- Struktur mit beliebig vielen gleichzeitig aktiven Fällen.
--
-- Reine Datenstruktur. Noch keine Frontend-Anbindung.
-- ════════════════════════════════════════════════════════════

-- ── Fallakte: der fehlende Kind-Bezug, der heute Mehrfach-Fälle verhindert ──
create table fallakten (
  id                     uuid primary key default gen_random_uuid(),
  kind_id                uuid not null references kinder(id),
  erstellt_von           uuid references profiles(id),
  bezugsperson           text,
  bezugsperson_kontakt   text,
  besonderheiten         text,
  ziele                  text,
  ressourcen             text,
  aktiv                  boolean not null default true,
  created_at             timestamptz not null default now(),
  updated_at             timestamptz not null default now()
);

comment on table fallakten is
  'Ersetzt Fallmanagement-Assistent.html + TK_Fallmanagement.html. Ein Kind kann mehrere (auch historische) Fallakten haben.';

create trigger trg_fallakten_updated_at
  before update on fallakten
  for each row execute function set_updated_at();

-- ── Risikostatus (Ampel-Verlauf je Fallakte) ────────────────────
create table fall_risikostatus (
  id             uuid primary key default gen_random_uuid(),
  fallakte_id    uuid not null references fallakten(id) on delete cascade,
  ampel          text not null check (ampel in ('gruen','gelb','rot')),
  begruendung    text,
  gesetzt_von    uuid references profiles(id),
  created_at     timestamptz not null default now()
);

-- ── Maßnahmen: ersetzt FM_Massnahmen_DB.html, jetzt mit Kind-/Fall-Bezug ──
-- traeger_id ist eigenständig (nicht über kind_id abgeleitet), damit
-- auch trägerweite Maßnahmen-Vorlagen ohne Kind-Zuordnung möglich bleiben.
create table fall_massnahmen (
  id             uuid primary key default gen_random_uuid(),
  traeger_id     uuid not null references traeger(id),
  fallakte_id    uuid references fallakten(id) on delete cascade,
  kind_id        uuid references kinder(id),
  titel          text not null,
  beschreibung   text,
  kategorie      text check (kategorie in ('paedagogisch','sozial','elternarbeit','schule','umfeld','ressourcen')),
  verantwortlich uuid references profiles(id),
  prioritaet     text check (prioritaet in ('niedrig','mittel','hoch')),
  status         text not null check (status in ('offen','in_arbeit','abgeschlossen')) default 'offen',
  zeitraum_von   date,
  zeitraum_bis   date,
  created_at     timestamptz not null default now(),
  updated_at     timestamptz not null default now()
);

comment on column fall_massnahmen.fallakte_id is
  'NULL = trägerweite Maßnahmen-Vorlage (ersetzt den generischen Katalog aus FM_Massnahmen_DB.html), sonst einer konkreten Fallakte zugeordnet.';

create trigger trg_fall_massnahmen_updated_at
  before update on fall_massnahmen
  for each row execute function set_updated_at();

-- ── Chronik (Verlauf/Beobachtungen je Fallakte) ─────────────────
create table fall_timeline (
  id             uuid primary key default gen_random_uuid(),
  fallakte_id    uuid not null references fallakten(id) on delete cascade,
  datum          date not null default current_date,
  ereignis       text,
  beobachtung    text,
  rueckmeldung   text,
  erstellt_von   uuid references profiles(id),
  created_at     timestamptz not null default now()
);

-- ── RLS ──────────────────────────────────────────────────────────
-- Bewusst KEIN Eltern-Zugriff auf Fallmanagement-Tabellen: das sind
-- interne Arbeitsdokumente, keine für Eltern bestimmte Ansicht
-- (Eltern erhalten Inhalte weiterhin nur über Weiterleitungs-Links,
-- nicht durch direkten Datenbankzugriff).

alter table fallakten enable row level security;
alter table fall_risikostatus enable row level security;
alter table fall_massnahmen enable row level security;
alter table fall_timeline enable row level security;

-- TK/Admin: volle Sicht auf alle Fallakten ihres Trägers
create policy fallakten_tk_admin_all
  on fallakten for all
  using (
    exists (
      select 1 from profiles p
      join kinder k on k.id = fallakten.kind_id
      where p.id = auth.uid() and p.rolle in ('tk','admin') and p.traeger_id = k.traeger_id
    )
  );

-- INGRA/Trainer: nur Fallakten der ihnen zugewiesenen Kinder
create policy fallakten_ingra_zugewiesen
  on fallakten for select
  using (
    exists (
      select 1 from ingra_kinder ik
      where ik.kind_id = fallakten.kind_id and ik.ingra_id = auth.uid()
    )
  );

create policy fallakten_trainer_zugewiesen
  on fallakten for select
  using (
    exists (
      select 1 from trainer_kinder tk
      where tk.kind_id = fallakten.kind_id and tk.trainer_id = auth.uid()
    )
  );

-- Risikostatus/Maßnahmen/Timeline: dieselbe Sichtbarkeit wie die zugehörige Fallakte
create policy fall_risikostatus_ueber_fallakte
  on fall_risikostatus for all
  using (exists (select 1 from fallakten f where f.id = fall_risikostatus.fallakte_id));

create policy fall_timeline_ueber_fallakte
  on fall_timeline for all
  using (exists (select 1 from fallakten f where f.id = fall_timeline.fallakte_id));

create policy fall_massnahmen_tk_admin_all
  on fall_massnahmen for all
  using (
    exists (
      select 1 from profiles p
      where p.id = auth.uid() and p.rolle in ('tk','admin') and p.traeger_id = fall_massnahmen.traeger_id
    )
  );

create policy fall_massnahmen_zugewiesen
  on fall_massnahmen for select
  using (
    fall_massnahmen.kind_id is not null
    and (
      exists (select 1 from ingra_kinder ik where ik.kind_id = fall_massnahmen.kind_id and ik.ingra_id = auth.uid())
      or exists (select 1 from trainer_kinder tk where tk.kind_id = fall_massnahmen.kind_id and tk.trainer_id = auth.uid())
    )
  );
