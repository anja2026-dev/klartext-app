-- ================================================================
-- 0001_auth_rollen.sql
-- ================================================================
-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration · Phase 0/1
-- Auth- & Rollen-Grundgerüst
--
-- Ersetzt das bisherige Login-Modell (gemeinsame Klartext-Passwörter
-- + sessionStorage-Flag in KLARTEXT_Login.html) durch echte,
-- individuelle Supabase-Auth-Konten mit rollenbasierter RLS.
--
-- Diese Migration legt NUR die Datenstruktur an.
-- Es gibt noch keine Frontend-Anbindung (kein Login-Flow geändert).
-- ════════════════════════════════════════════════════════════

create extension if not exists pgcrypto;

-- ── Träger (Mandant) ───────────────────────────────────────────
create table traeger (
  id          uuid primary key default gen_random_uuid(),
  name        text not null,
  adresse     text,
  created_at  timestamptz not null default now()
);

-- ── Rollen als eigener Typ, damit Policies sauber vergleichen können ──
create type klartext_rolle as enum ('ingra','tk','lk','eltern','trainer','admin');
create type ingra_subrolle as enum ('fest','springer','pool','vertretung');

-- ── Profile: 1:1 mit auth.users, ersetzt geteilte Rollen-Passwörter ──
create table profiles (
  id              uuid primary key references auth.users(id) on delete cascade,
  traeger_id      uuid references traeger(id),
  vorname         text,
  nachname        text,
  email           text,
  telefon         text,
  rolle           klartext_rolle not null,
  ingra_subrolle  ingra_subrolle,
  qualifikationen text[] not null default '{}',
  fuehrerschein   boolean not null default false,
  fahrzeug        boolean not null default false,
  aktiv           boolean not null default true,
  created_at      timestamptz not null default now(),
  updated_at      timestamptz not null default now()
);

comment on table profiles is
  'Ersetzt KLARTEXT_Login.html: ein echtes Konto pro Person statt ein Passwort pro Rolle.';
comment on column profiles.rolle is
  'Nur per service_role-Funktion änderbar, niemals durch den Nutzer selbst (siehe unten).';

-- ── Qualifikationen-Katalog (Lookup, z.B. für Vertretungssuche) ──
create table qualifikationen_katalog (
  code          text primary key,
  beschreibung  text,
  pflicht_fuer  text
);

-- ── updated_at automatisch pflegen ──────────────────────────────
create or replace function set_updated_at()
returns trigger language plpgsql as $$
begin
  new.updated_at = now();
  return new;
end;
$$;

create trigger trg_profiles_updated_at
  before update on profiles
  for each row execute function set_updated_at();

-- ── RLS: Rollen werden ab jetzt in der DB erzwungen, nicht im Frontend ──
alter table traeger enable row level security;
alter table profiles enable row level security;
alter table qualifikationen_katalog enable row level security;

-- Jede:r sieht das eigene Profil
create policy profiles_select_own
  on profiles for select
  using (id = auth.uid());

-- Jede:r darf nur die eigenen Kontaktfelder ändern — NICHT die eigene Rolle
create policy profiles_update_own_no_role_change
  on profiles for update
  using (id = auth.uid())
  with check (id = auth.uid());

revoke update (rolle, ingra_subrolle, traeger_id) on profiles from authenticated;

-- Admin sieht/verwaltet alle Profile eines Trägers
create policy profiles_admin_all
  on profiles for all
  using (
    exists (
      select 1 from profiles p
      where p.id = auth.uid() and p.rolle = 'admin'
    )
  );

-- Qualifikationskatalog ist für alle eingeloggten Rollen lesbar
create policy qualifikationen_read_all
  on qualifikationen_katalog for select
  to authenticated
  using (true);

-- Träger-Stammdaten: lesbar für Mitglieder desselben Trägers
create policy traeger_select_member
  on traeger for select
  using (
    exists (
      select 1 from profiles p
      where p.id = auth.uid() and p.traeger_id = traeger.id
    )
  );


-- ================================================================
-- 0002_kinder_stammdaten.sql
-- ================================================================
-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration · Phase 1
-- Kinder-Stammdaten (einzige Quelle)
--
-- Ersetzt zwei konkurrierende, nicht synchronisierte Datensätze:
--   - Firebase /children  (genutzt von Weiterleiten, TK-Inbox, Chat,
--     Barometer-Kind, Zeitkonto, Krankmeldung, Urlaubsantrag)
--   - localStorage['children'] (genutzt nur von Kinderverwaltung.html)
-- durch eine einzige Tabelle, die alle Module referenzieren.
--
-- Reine Datenstruktur. Noch keine Frontend-Anbindung.
-- ════════════════════════════════════════════════════════════

-- ── Schulen / Einsatzorte ──────────────────────────────────────
create table schulen (
  id          uuid primary key default gen_random_uuid(),
  traeger_id  uuid references traeger(id),
  name        text not null,
  adresse     text,
  ort         text,
  plz         text,
  lat         numeric,
  lng         numeric,
  schultyp    text check (schultyp in ('grundschule','foerderschule','realschule','gymnasium','sonstige')),
  kontakt     text,
  aktiv       boolean not null default true,
  created_at  timestamptz not null default now()
);

-- ── Kinder: einzige Quelle für alle TK-Module ──────────────────
create table kinder (
  id                    uuid primary key default gen_random_uuid(),
  traeger_id            uuid not null references traeger(id),
  name                  text not null,
  klasse                text,
  geburtsdatum          date,
  bedarfsart            text,
  schule_id             uuid references schulen(id),
  kita_name             text,
  kita_gruppe           text,
  werkstatt_name        text,
  wf_bereich            text,
  arbeitsplatz          text,
  einsatzort            text,
  leistungserbringer    text,   -- "Träger der Maßnahme" (Freitext, ≠ traeger_id)
  kostentraeger         text,
  aktenzeichen          text,   -- Kandidat für Vault-Verschlüsselung (siehe DSGVO-Analyse #10)
  lehrkraft_name        text,
  bezugserzieher_name   text,
  wf_gruppenleitung     text,
  ansprechpartner       text,
  arbeitszeiten         text,
  einwilligung_erfasst  boolean not null default false,   -- schließt DSGVO-Befund #9
  einwilligung_datum    date,
  aktiv                 boolean not null default true,
  ausgetreten_am        date,
  created_at            timestamptz not null default now(),
  updated_at            timestamptz not null default now()
);

comment on table kinder is
  'Einzige Quelle für Kinderdaten. Ersetzt Firebase /children UND localStorage[''children''].';

create trigger trg_kinder_updated_at
  before update on kinder
  for each row execute function set_updated_at();

-- ── Wochenplan (Einsatzzeiten je Kind) ──────────────────────────
create table kinder_wochenplan (
  id         uuid primary key default gen_random_uuid(),
  kind_id    uuid not null references kinder(id) on delete cascade,
  wochentag  text not null check (wochentag in ('MO','DI','MI','DO','FR')),
  von        time,
  bis        time
);

-- ── RLS ──────────────────────────────────────────────────────────
alter table schulen enable row level security;
alter table kinder enable row level security;
alter table kinder_wochenplan enable row level security;

-- Schulen: lesbar für alle eingeloggten Rollen des eigenen Trägers
create policy schulen_select_traeger
  on schulen for select
  using (
    exists (
      select 1 from profiles p
      where p.id = auth.uid() and p.traeger_id = schulen.traeger_id
    )
  );

-- Kinder: TK und Admin verwalten alle Kinder des eigenen Trägers
create policy kinder_tk_admin_all
  on kinder for all
  using (
    exists (
      select 1 from profiles p
      where p.id = auth.uid()
        and p.traeger_id = kinder.traeger_id
        and p.rolle in ('tk','admin')
    )
  );

-- INGRA sieht nur Kinder, denen sie über einen aktiven Einsatz zugeordnet ist
-- (Tabelle "einsaetze" folgt in einer späteren Migration — Policy wird dort ergänzt)

create policy kinder_wochenplan_select_traeger
  on kinder_wochenplan for select
  using (
    exists (
      select 1 from kinder k
      join profiles p on p.traeger_id = k.traeger_id
      where k.id = kinder_wochenplan.kind_id and p.id = auth.uid()
    )
  );


-- ================================================================
-- 0003_kinder_rls_erweiterung.sql
-- ================================================================
-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration · Phase 1
-- Erweiterte RLS für "kinder": rollenspezifische Zuweisungen
--
-- Ergänzt 0002_kinder_stammdaten.sql um granularere Sichtbarkeit:
--   - INGRA sieht nur zugewiesene Kinder ihres Trägers
--   - Eltern sehen nur ihr eigenes Kind
--   - Trainer sehen nur zugewiesene Kinder ihres Trägers
-- TK/Admin behalten die bestehende volle Sicht aus 0002.
--
-- Reine Datenstruktur. Noch keine Frontend-Anbindung.
-- ════════════════════════════════════════════════════════════

-- ── Zuweisungstabellen ──────────────────────────────────────────
create table ingra_kinder (
  ingra_id       uuid not null references profiles(id) on delete cascade,
  kind_id        uuid not null references kinder(id) on delete cascade,
  zugewiesen_am  timestamptz not null default now(),
  primary key (ingra_id, kind_id)
);

create table eltern_kinder (
  eltern_id      uuid not null references profiles(id) on delete cascade,
  kind_id        uuid not null references kinder(id) on delete cascade,
  zugewiesen_am  timestamptz not null default now(),
  primary key (eltern_id, kind_id)
);

create table trainer_kinder (
  trainer_id     uuid not null references profiles(id) on delete cascade,
  kind_id        uuid not null references kinder(id) on delete cascade,
  zugewiesen_am  timestamptz not null default now(),
  primary key (trainer_id, kind_id)
);

comment on table ingra_kinder is 'Welche INGRA welchem Kind zugeordnet ist.';
comment on table eltern_kinder is 'Welches Eltern-Profil zu welchem Kind gehört.';
comment on table trainer_kinder is 'Welcher Trainer welches Kind begleitet.';

alter table ingra_kinder enable row level security;
alter table eltern_kinder enable row level security;
alter table trainer_kinder enable row level security;

-- Jede Rolle sieht die eigenen Zuweisungszeilen ...
create policy ingra_kinder_select_own
  on ingra_kinder for select
  using (ingra_id = auth.uid());

create policy eltern_kinder_select_own
  on eltern_kinder for select
  using (eltern_id = auth.uid());

create policy trainer_kinder_select_own
  on trainer_kinder for select
  using (trainer_id = auth.uid());

-- ... TK/Admin verwalten alle Zuweisungen ihres Trägers
create policy ingra_kinder_tk_admin_all
  on ingra_kinder for all
  using (
    exists (
      select 1 from profiles p
      join kinder k on k.id = ingra_kinder.kind_id
      where p.id = auth.uid() and p.rolle in ('tk','admin') and p.traeger_id = k.traeger_id
    )
  );

create policy eltern_kinder_tk_admin_all
  on eltern_kinder for all
  using (
    exists (
      select 1 from profiles p
      join kinder k on k.id = eltern_kinder.kind_id
      where p.id = auth.uid() and p.rolle in ('tk','admin') and p.traeger_id = k.traeger_id
    )
  );

create policy trainer_kinder_tk_admin_all
  on trainer_kinder for all
  using (
    exists (
      select 1 from profiles p
      join kinder k on k.id = trainer_kinder.kind_id
      where p.id = auth.uid() and p.rolle in ('tk','admin') and p.traeger_id = k.traeger_id
    )
  );

-- ── Erweiterte Sichtbarkeit auf "kinder" ─────────────────────────
-- Zusätzlich zur bestehenden kinder_tk_admin_all-Policy aus 0002.
-- RLS-Policies für dieselbe Aktion (select) werden mit OR verknüpft.

create policy kinder_ingra_zugewiesen
  on kinder for select
  using (
    exists (
      select 1 from ingra_kinder ik
      join profiles p on p.id = ik.ingra_id
      where ik.kind_id = kinder.id
        and ik.ingra_id = auth.uid()
        and p.traeger_id = kinder.traeger_id
    )
  );

create policy kinder_eltern_eigenes_kind
  on kinder for select
  using (
    exists (
      select 1 from eltern_kinder ek
      where ek.kind_id = kinder.id and ek.eltern_id = auth.uid()
    )
  );

create policy kinder_trainer_zugewiesen
  on kinder for select
  using (
    exists (
      select 1 from trainer_kinder tk
      join profiles p on p.id = tk.trainer_id
      where tk.kind_id = kinder.id
        and tk.trainer_id = auth.uid()
        and p.traeger_id = kinder.traeger_id
    )
  );


-- ================================================================
-- 0004_fallmanagement.sql
-- ================================================================
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


-- ================================================================
-- 0005_fall_risikostatus_timeline_rls_fix.sql
-- ================================================================
-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration · Phase 3
-- Korrektur: fall_risikostatus/fall_timeline — Schreiben nur TK/Admin
--
-- 0004 hatte für beide Tabellen eine einzige "for all"-Policy, die
-- Sichtbarkeit von der zugehörigen Fallakte erbte — das erlaubte
-- versehentlich auch INGRA/Trainer das Schreiben, sobald sie
-- überhaupt Lesezugriff auf den Fall hatten. Diese Migration trennt
-- Lesen und Schreiben: TK/Admin lesen+schreiben, INGRA/Trainer nur
-- lesen (für zugewiesene Fälle), Eltern weiterhin ohne Zugriff.
-- ════════════════════════════════════════════════════════════

drop policy if exists fall_risikostatus_ueber_fallakte on fall_risikostatus;
drop policy if exists fall_timeline_ueber_fallakte on fall_timeline;

-- ── fall_risikostatus ────────────────────────────────────────────
create policy fall_risikostatus_tk_admin_all
  on fall_risikostatus for all
  using (
    exists (
      select 1 from fallakten f
      join kinder k on k.id = f.kind_id
      join profiles p on p.traeger_id = k.traeger_id
      where f.id = fall_risikostatus.fallakte_id
        and p.id = auth.uid()
        and p.rolle in ('tk','admin')
    )
  );

create policy fall_risikostatus_select_ingra
  on fall_risikostatus for select
  using (
    exists (
      select 1 from fallakten f
      join ingra_kinder ik on ik.kind_id = f.kind_id
      where f.id = fall_risikostatus.fallakte_id and ik.ingra_id = auth.uid()
    )
  );

create policy fall_risikostatus_select_trainer
  on fall_risikostatus for select
  using (
    exists (
      select 1 from fallakten f
      join trainer_kinder tk on tk.kind_id = f.kind_id
      where f.id = fall_risikostatus.fallakte_id and tk.trainer_id = auth.uid()
    )
  );

-- ── fall_timeline ────────────────────────────────────────────────
create policy fall_timeline_tk_admin_all
  on fall_timeline for all
  using (
    exists (
      select 1 from fallakten f
      join kinder k on k.id = f.kind_id
      join profiles p on p.traeger_id = k.traeger_id
      where f.id = fall_timeline.fallakte_id
        and p.id = auth.uid()
        and p.rolle in ('tk','admin')
    )
  );

create policy fall_timeline_select_ingra
  on fall_timeline for select
  using (
    exists (
      select 1 from fallakten f
      join ingra_kinder ik on ik.kind_id = f.kind_id
      where f.id = fall_timeline.fallakte_id and ik.ingra_id = auth.uid()
    )
  );

create policy fall_timeline_select_trainer
  on fall_timeline for select
  using (
    exists (
      select 1 from fallakten f
      join trainer_kinder tk on tk.kind_id = f.kind_id
      where f.id = fall_timeline.fallakte_id and tk.trainer_id = auth.uid()
    )
  );


-- ================================================================
-- 0006_wochenplan.sql
-- ================================================================
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


-- ================================================================
-- 0007_barometer.sql
-- ================================================================
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


-- ================================================================
-- 0008_weiterleitungen.sql
-- ================================================================
-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration · Phase 2
-- Weiterleitungs-Grundstruktur
--
-- Ersetzt Firebase /forward (KLARTEXT_Weiterleiten.html schreibt,
-- KLARTEXT_TK_Inbox.html / TK_Uebergaben.html lesen). Eltern/Lehrkraft
-- erhalten Inhalte weiterhin nur über token-basierte Weiterleitungs-
-- Links (KLARTEXT_Forward_Read.html-Muster), nicht über direkten
-- authentifizierten Tabellenzugriff — daher keine Eltern/LK-Policies
-- hier, konsistent mit der Entscheidung aus der Fallmanagement-Migration.
--
-- Reine Datenstruktur. Noch keine Frontend-Anbindung.
-- ════════════════════════════════════════════════════════════

create table weiterleitungen (
  id              uuid primary key default gen_random_uuid(),
  kind_id         uuid not null references kinder(id),
  von_profil      uuid references profiles(id),
  von_rolle       text,
  ziel_rolle      text not null default 'tk',
  typ             text not null check (typ in ('uebergabe','barometer','hinweis')),
  text            text,
  dringlichkeit   text not null check (dringlichkeit in ('normal','erhoben','dringend')) default 'normal',
  status          text not null check (status in ('offen','gelesen','erledigt')) default 'offen',
  besonderheiten  text,
  details         text,
  anhang_pfad     text,   -- Storage-Referenz statt Freitext-"Anhang" wie bisher
  created_at      timestamptz not null default now(),
  updated_at      timestamptz not null default now()
);

comment on table weiterleitungen is
  'Ersetzt Firebase /forward. anhang_pfad verweist auf Supabase Storage statt auf einen reinen Freitext-Hinweis.';

create trigger trg_weiterleitungen_updated_at
  before update on weiterleitungen
  for each row execute function set_updated_at();

-- ── RLS ──────────────────────────────────────────────────────────
alter table weiterleitungen enable row level security;

-- TK/Admin: volle Sicht + Statuspflege (das ist die eigentliche "TK-Inbox")
create policy weiterleitungen_tk_admin_all
  on weiterleitungen for all
  using (
    exists (
      select 1 from kinder k
      join profiles p on p.traeger_id = k.traeger_id
      where k.id = weiterleitungen.kind_id
        and p.id = auth.uid()
        and p.rolle in ('tk','admin')
    )
  );

-- Zugewiesene INGRA darf für ihre Kinder Weiterleitungen anlegen
create policy weiterleitungen_ingra_insert
  on weiterleitungen for insert
  with check (exists (select 1 from ingra_kinder ik where ik.kind_id = weiterleitungen.kind_id and ik.ingra_id = auth.uid()));

-- Absender:in sieht die eigenen gesendeten Weiterleitungen (z.B. Status verfolgen)
create policy weiterleitungen_select_eigene
  on weiterleitungen for select
  using (von_profil = auth.uid());


-- ================================================================
-- 0009_chat.sql
-- ================================================================
-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration · Phase 2
-- TK-Chat-Grundstruktur
--
-- Reine Datenstruktur. Noch keine Frontend-Anbindung.
-- ════════════════════════════════════════════════════════════

create table chat_nachrichten (
  id                uuid primary key default gen_random_uuid(),
  kind_id           uuid not null references kinder(id),
  sender_id         uuid references profiles(id),
  empfaenger_rollen klartext_rolle[] not null default '{tk}',
  text              text not null,
  erstellt_am       timestamptz not null default now()
);

-- ── RLS ──────────────────────────────────────────────────────────
alter table chat_nachrichten enable row level security;

-- TK/Admin: volle Sicht + Schreiben, trägerweit
create policy chat_nachrichten_tk_admin_all
  on chat_nachrichten for all
  using (
    exists (
      select 1 from kinder k
      join profiles p on p.traeger_id = k.traeger_id
      where k.id = chat_nachrichten.kind_id
        and p.id = auth.uid()
        and p.rolle in ('tk','admin')
    )
  );

-- INGRA: nur Lesen, beschränkt auf zugewiesene Kinder
create policy chat_nachrichten_ingra_select
  on chat_nachrichten for select
  using (exists (select 1 from ingra_kinder ik where ik.kind_id = chat_nachrichten.kind_id and ik.ingra_id = auth.uid()));

-- Eltern: kein Zugriff (keine Policy für 'eltern' angelegt).


-- ================================================================
-- 0010_chat_ingra_insert.sql
-- ================================================================
-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration · Phase 2
-- Erweiterung: INGRA darf chat_nachrichten senden
--
-- Ergänzt 0009_chat.sql um eine Insert-Policy für INGRA, beschränkt
-- auf zugewiesene Kinder. TK/Admin (for all aus 0009) und die
-- fehlenden Schreibrechte für Trainer/Eltern bleiben unverändert.
-- ════════════════════════════════════════════════════════════

create policy chat_nachrichten_ingra_insert
  on chat_nachrichten for insert
  with check (
    sender_id = auth.uid()
    and exists (
      select 1 from ingra_kinder ik
      where ik.kind_id = chat_nachrichten.kind_id and ik.ingra_id = auth.uid()
    )
  );


-- ================================================================
-- 0011_trainer_stammdaten.sql
-- ================================================================
-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration · Phase 1
-- Trainer-Stammdaten
--
-- Eigenständig von trainer_kinder (0003, Kind-Zuweisung): bildet
-- trainerspezifische Stammdaten ab, unabhängig davon, welchem Kind
-- ein Trainer aktuell zugeordnet ist.
--
-- Reine Datenstruktur. Noch keine Frontend-Anbindung.
-- ════════════════════════════════════════════════════════════

create table trainer_stammdaten (
  id               uuid primary key default gen_random_uuid(),
  profile_id       uuid not null unique references profiles(id) on delete cascade,
  traeger_id       uuid references traeger(id),
  qualifikationen  text[] not null default '{}',
  zertifizierungen text[] not null default '{}',
  betreute_kurse   text[] not null default '{}',
  schwerpunkt      text,
  aktiv            boolean not null default true,
  created_at       timestamptz not null default now(),
  updated_at       timestamptz not null default now()
);

comment on table trainer_stammdaten is
  'Trainerspezifische Stammdaten (Qualifikationen, Zertifizierungen, betreute Kurse), unabhängig von Kind-Zuweisungen (trainer_kinder).';

create trigger trg_trainer_stammdaten_updated_at
  before update on trainer_stammdaten
  for each row execute function set_updated_at();

-- ── RLS ──────────────────────────────────────────────────────────
alter table trainer_stammdaten enable row level security;

-- Trainer verwaltet die eigenen Stammdaten vollständig
create policy trainer_stammdaten_own_all
  on trainer_stammdaten for all
  using (profile_id = auth.uid());

-- TK/Admin verwalten Trainer-Stammdaten ihres Trägers
create policy trainer_stammdaten_tk_admin_all
  on trainer_stammdaten for all
  using (
    exists (
      select 1 from profiles p
      where p.id = auth.uid()
        and p.rolle in ('tk','admin')
        and p.traeger_id = trainer_stammdaten.traeger_id
    )
  );


-- ================================================================
-- 0012_tagesjournal_eintraege.sql
-- ================================================================
-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration · Phase 1
-- Tagesjournal-Einträge (Barometer + Notiz je Tag/Kind)
--
-- Ersetzt localStorage['kt_tagesjournal'] aus KLARTEXT_Tagesjournal.html.
-- Die "Übergabe"-Funktion dieser Seite nutzt bereits sendForward() und
-- ist damit durch die bestehende Tabelle weiterleitungen abgedeckt.
--
-- Reine Datenstruktur. Keine RLS in dieser Migration.
-- ════════════════════════════════════════════════════════════

create table tagesjournal_eintraege (
  id                    uuid primary key default gen_random_uuid(),
  kind_id               uuid references kinder(id),
  ersteller_id          uuid references profiles(id),
  datum                 date not null,
  barometer_farbe       text check (barometer_farbe in ('gruen','gelb','orange','rot','grau')),
  barometer_zeit        time,
  notiz                 text,
  besonderheit          text,
  besonderheit_details  text,
  created_at            timestamptz not null default now()
);


-- ================================================================
-- 0013_notizen.sql
-- ================================================================
-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration · Phase 1
-- Notizen (Notizblock)
--
-- Ersetzt localStorage['kt_notizen_liste'] aus KLARTEXT_Notizblock.html.
--
-- Reine Datenstruktur. Keine RLS in dieser Migration.
-- ════════════════════════════════════════════════════════════

create table notizen (
  id            uuid primary key default gen_random_uuid(),
  ersteller_id  uuid references profiles(id),
  datum         date not null,
  thema         text,
  text          text not null,
  created_at    timestamptz not null default now()
);


-- ================================================================
-- 0014_listen_eintraege.sql
-- ================================================================
-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration · Phase 1
-- Listen-Einträge (To-do-Liste)
--
-- Ersetzt localStorage['klartext_todo_list'] aus KLARTEXT_Listen.html.
-- kategorie ist bereits mehrkategorie-fähig angelegt, auch wenn der
-- bestehende Code aktuell nur die Kategorie 'todo' schreibt.
--
-- Reine Datenstruktur. Keine RLS in dieser Migration.
-- ════════════════════════════════════════════════════════════

create table listen_eintraege (
  id            uuid primary key default gen_random_uuid(),
  ersteller_id  uuid references profiles(id),
  kategorie     text not null default 'todo',
  text          text not null,
  erledigt      boolean not null default false,
  created_at    timestamptz not null default now()
);


-- ================================================================
-- 0015_teilnehmer_protokoll.sql
-- ================================================================
-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration · Phase 1
-- Teilnehmer-Protokoll
--
-- Ersetzt localStorage['kt_tn_protokoll'] aus
-- KLARTEXT_Teilnehmer_Protokoll.html.
--
-- Reine Datenstruktur. Keine RLS in dieser Migration.
-- ════════════════════════════════════════════════════════════

create table teilnehmer_protokoll (
  id            uuid primary key default gen_random_uuid(),
  ersteller_id  uuid references profiles(id),
  name          text not null,
  datum         date,
  einrichtung   text,
  vorschlaege   text,
  anmerkungen   text,
  created_at    timestamptz not null default now()
);


-- ================================================================
-- 0016_urlaubsantraege.sql
-- ================================================================
-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration · Phase 1
-- Urlaubsanträge
--
-- Ersetzt Firebase /vacation_request aus
-- KLARTEXT_Urlaubsantrag_INGRA.html.
--
-- Reine Datenstruktur. Keine RLS in dieser Migration.
-- ════════════════════════════════════════════════════════════

create table urlaubsantraege (
  id          uuid primary key default gen_random_uuid(),
  ingra_id    uuid references profiles(id),
  kind_id     uuid references kinder(id),
  von_datum   date not null,
  bis_datum   date not null,
  tage        int,
  vertretung  text,
  notiz       text,
  status      text not null default 'beantragt' check (status in ('beantragt','genehmigt','abgelehnt')),
  created_at  timestamptz not null default now()
);


-- ================================================================
-- 0017_zeiteintraege.sql
-- ================================================================
-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration · Phase 1
-- Zeiteinträge (Zeitkonto)
--
-- Ersetzt Firebase /time_entry + localStorage['kt_eintraege'] aus
-- KLARTEXT_Zeitkonto.html.
--
-- Reine Datenstruktur. Keine RLS in dieser Migration.
-- ════════════════════════════════════════════════════════════

create table zeiteintraege (
  id             uuid primary key default gen_random_uuid(),
  ingra_id       uuid references profiles(id),
  kind_id        uuid references kinder(id),
  datum          date not null,
  von_uhrzeit    time not null,
  bis_uhrzeit    time not null,
  pause_minuten  int not null default 0,
  dauer_stunden  numeric,
  typ            text,
  notiz          text,
  created_at     timestamptz not null default now()
);


-- ================================================================
-- 0018_krankmeldungen.sql
-- ================================================================
-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration · Phase 1
-- Krankmeldungen
--
-- Ersetzt Firebase /sick_note_ingra + /sick_note sowie
-- localStorage['kz_meldungen'] aus KLARTEXT_Krankmeldung.html.
-- Zwei Unterarten laut bestehendem Code: typ='ingra' (eigene
-- Krankmeldung, Zeitraum von/bis) und typ='kind' (Ausfall eines
-- Kindes, Einzeltag mit Grund/Zeit).
--
-- Reine Datenstruktur. Keine RLS in dieser Migration.
-- ════════════════════════════════════════════════════════════

create table krankmeldungen (
  id          uuid primary key default gen_random_uuid(),
  ingra_id    uuid references profiles(id),
  typ         text not null check (typ in ('ingra','kind')),
  kind_id     uuid references kinder(id),
  von_datum   date,
  bis_datum   date,
  datum       date,
  grund       text,
  zeit        text,
  notiz       text,
  created_at  timestamptz not null default now()
);


-- ================================================================
-- 0019_tagesjournal_eintraege_rls.sql
-- ================================================================
-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration · Phase 1
-- RLS: tagesjournal_eintraege
--
-- INGRA: eigene Einträge (ersteller_id) lesen+schreiben.
-- Zugewiesene INGRA (ingra_kinder): kind_id-Einträge nur SEHEN.
-- TK/Admin: alles lesen+schreiben.
-- Eltern/Trainer: kein Zugriff (keine Policy). Kein anonymer Zugriff
-- (alle Policies "to authenticated").
-- ════════════════════════════════════════════════════════════

alter table tagesjournal_eintraege enable row level security;

create policy tagesjournal_eintraege_select
  on tagesjournal_eintraege for select
  to authenticated
  using (
    ersteller_id = auth.uid()
    or (
      kind_id is not null
      and exists (
        select 1 from ingra_kinder ik
        where ik.kind_id = tagesjournal_eintraege.kind_id and ik.ingra_id = auth.uid()
      )
    )
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  );

create policy tagesjournal_eintraege_insert
  on tagesjournal_eintraege for insert
  to authenticated
  with check (
    ersteller_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  );

create policy tagesjournal_eintraege_update
  on tagesjournal_eintraege for update
  to authenticated
  using (
    ersteller_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  )
  with check (
    ersteller_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  );

create policy tagesjournal_eintraege_delete
  on tagesjournal_eintraege for delete
  to authenticated
  using (
    ersteller_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  );


-- ================================================================
-- 0020_notizen_rls.sql
-- ================================================================
-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration · Phase 1
-- RLS: notizen
--
-- INGRA: eigene Einträge (ersteller_id) lesen+schreiben.
-- TK/Admin: alles lesen+schreiben.
-- Eltern/Trainer: kein Zugriff (keine Policy). Kein anonymer Zugriff.
-- (Kein kind_id in dieser Tabelle -> keine ingra_kinder-Klausel nötig.)
-- ════════════════════════════════════════════════════════════

alter table notizen enable row level security;

create policy notizen_select
  on notizen for select
  to authenticated
  using (
    ersteller_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  );

create policy notizen_insert
  on notizen for insert
  to authenticated
  with check (
    ersteller_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  );

create policy notizen_update
  on notizen for update
  to authenticated
  using (
    ersteller_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  )
  with check (
    ersteller_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  );

create policy notizen_delete
  on notizen for delete
  to authenticated
  using (
    ersteller_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  );


-- ================================================================
-- 0021_listen_eintraege_rls.sql
-- ================================================================
-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration · Phase 1
-- RLS: listen_eintraege
--
-- INGRA: eigene Einträge (ersteller_id) lesen+schreiben.
-- TK/Admin: alles lesen+schreiben.
-- Eltern/Trainer: kein Zugriff (keine Policy). Kein anonymer Zugriff.
-- (Kein kind_id in dieser Tabelle -> keine ingra_kinder-Klausel nötig.)
-- ════════════════════════════════════════════════════════════

alter table listen_eintraege enable row level security;

create policy listen_eintraege_select
  on listen_eintraege for select
  to authenticated
  using (
    ersteller_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  );

create policy listen_eintraege_insert
  on listen_eintraege for insert
  to authenticated
  with check (
    ersteller_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  );

create policy listen_eintraege_update
  on listen_eintraege for update
  to authenticated
  using (
    ersteller_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  )
  with check (
    ersteller_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  );

create policy listen_eintraege_delete
  on listen_eintraege for delete
  to authenticated
  using (
    ersteller_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  );


-- ================================================================
-- 0022_teilnehmer_protokoll_rls.sql
-- ================================================================
-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration · Phase 1
-- RLS: teilnehmer_protokoll
--
-- INGRA: eigene Einträge (ersteller_id) lesen+schreiben.
-- TK/Admin: alles lesen+schreiben.
-- Eltern/Trainer: kein Zugriff (keine Policy). Kein anonymer Zugriff.
-- (Kein kind_id in dieser Tabelle -> keine ingra_kinder-Klausel nötig.)
-- ════════════════════════════════════════════════════════════

alter table teilnehmer_protokoll enable row level security;

create policy teilnehmer_protokoll_select
  on teilnehmer_protokoll for select
  to authenticated
  using (
    ersteller_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  );

create policy teilnehmer_protokoll_insert
  on teilnehmer_protokoll for insert
  to authenticated
  with check (
    ersteller_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  );

create policy teilnehmer_protokoll_update
  on teilnehmer_protokoll for update
  to authenticated
  using (
    ersteller_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  )
  with check (
    ersteller_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  );

create policy teilnehmer_protokoll_delete
  on teilnehmer_protokoll for delete
  to authenticated
  using (
    ersteller_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  );


-- ================================================================
-- 0023_urlaubsantraege_rls.sql
-- ================================================================
-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration · Phase 1
-- RLS: urlaubsantraege
--
-- INGRA: eigene Anträge (ingra_id) lesen+schreiben.
-- Zugewiesene INGRA (ingra_kinder): kind_id-Einträge nur SEHEN.
-- TK/Admin: alles lesen+schreiben.
-- Eltern/Trainer: kein Zugriff (keine Policy). Kein anonymer Zugriff.
-- ════════════════════════════════════════════════════════════

alter table urlaubsantraege enable row level security;

create policy urlaubsantraege_select
  on urlaubsantraege for select
  to authenticated
  using (
    ingra_id = auth.uid()
    or (
      kind_id is not null
      and exists (
        select 1 from ingra_kinder ik
        where ik.kind_id = urlaubsantraege.kind_id and ik.ingra_id = auth.uid()
      )
    )
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  );

create policy urlaubsantraege_insert
  on urlaubsantraege for insert
  to authenticated
  with check (
    ingra_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  );

create policy urlaubsantraege_update
  on urlaubsantraege for update
  to authenticated
  using (
    ingra_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  )
  with check (
    ingra_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  );

create policy urlaubsantraege_delete
  on urlaubsantraege for delete
  to authenticated
  using (
    ingra_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  );


-- ================================================================
-- 0024_zeiteintraege_rls.sql
-- ================================================================
-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration · Phase 1
-- RLS: zeiteintraege
--
-- INGRA: eigene Einträge (ingra_id) lesen+schreiben.
-- Zugewiesene INGRA (ingra_kinder): kind_id-Einträge nur SEHEN.
-- TK/Admin: alles lesen+schreiben.
-- Eltern/Trainer: kein Zugriff (keine Policy). Kein anonymer Zugriff.
-- ════════════════════════════════════════════════════════════

alter table zeiteintraege enable row level security;

create policy zeiteintraege_select
  on zeiteintraege for select
  to authenticated
  using (
    ingra_id = auth.uid()
    or (
      kind_id is not null
      and exists (
        select 1 from ingra_kinder ik
        where ik.kind_id = zeiteintraege.kind_id and ik.ingra_id = auth.uid()
      )
    )
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  );

create policy zeiteintraege_insert
  on zeiteintraege for insert
  to authenticated
  with check (
    ingra_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  );

create policy zeiteintraege_update
  on zeiteintraege for update
  to authenticated
  using (
    ingra_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  )
  with check (
    ingra_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  );

create policy zeiteintraege_delete
  on zeiteintraege for delete
  to authenticated
  using (
    ingra_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  );


-- ================================================================
-- 0025_krankmeldungen_rls.sql
-- ================================================================
-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration · Phase 1
-- RLS: krankmeldungen
--
-- INGRA: eigene Meldungen (ingra_id) lesen+schreiben.
-- Zugewiesene INGRA (ingra_kinder): kind_id-Einträge (typ='kind') nur SEHEN.
-- TK/Admin: alles lesen+schreiben.
-- Eltern/Trainer: kein Zugriff (keine Policy). Kein anonymer Zugriff.
-- ════════════════════════════════════════════════════════════

alter table krankmeldungen enable row level security;

create policy krankmeldungen_select
  on krankmeldungen for select
  to authenticated
  using (
    ingra_id = auth.uid()
    or (
      kind_id is not null
      and exists (
        select 1 from ingra_kinder ik
        where ik.kind_id = krankmeldungen.kind_id and ik.ingra_id = auth.uid()
      )
    )
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  );

create policy krankmeldungen_insert
  on krankmeldungen for insert
  to authenticated
  with check (
    ingra_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  );

create policy krankmeldungen_update
  on krankmeldungen for update
  to authenticated
  using (
    ingra_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  )
  with check (
    ingra_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  );

create policy krankmeldungen_delete
  on krankmeldungen for delete
  to authenticated
  using (
    ingra_id = auth.uid()
    or exists (select 1 from profiles p where p.id = auth.uid() and p.rolle in ('tk','admin'))
  );


-- ================================================================
-- 0026_kinder_zuordnung.sql
-- ================================================================
-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration
-- Kinder-Zuordnung (Schule/INGRA/Trainer/TK)
--
-- gruppe_id bewusst weggelassen: eine "gruppen"-Tabelle existiert im
-- Schema nicht (nur die Freitextfelder kita_gruppe/wf_gruppenleitung
-- auf kinder), eine Fremdschlüssel-Referenz darauf würde die Migration
-- zum Scheitern bringen. Kann in einer eigenen Migration nachgezogen
-- werden, sobald eine echte gruppen-Tabelle angelegt ist.
--
-- Reine Datenstruktur. Keine RLS in dieser Migration.
-- ════════════════════════════════════════════════════════════

create table kinder_zuordnung (
  id          uuid primary key default gen_random_uuid(),
  kind_id     uuid references kinder(id) on delete cascade,
  schule_id   uuid references schulen(id) on delete set null,
  ingra_id    uuid references profiles(id) on delete set null,
  trainer_id  uuid references profiles(id) on delete set null,
  tk_id       uuid references profiles(id) on delete set null,
  aktiv       boolean default true,
  timestamp   timestamptz default now()
);


-- ================================================================
-- 0027_kinder_zuordnung_rls.sql
-- ================================================================
-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration
-- RLS: kinder_zuordnung
--
-- admin_all: auth.role() liefert nur 'authenticated'/'anon'/'service_role'
-- (JWT-Ebene), niemals die App-Rolle 'admin' aus profiles.rolle - eine
-- Policy mit auth.role() = 'admin' würde daher nie greifen. Wie in
-- allen anderen RLS-Migrationen dieses Schemas (z.B. zeiteintraege_rls,
-- krankmeldungen_rls) stattdessen über profiles.rolle geprüft.
-- ════════════════════════════════════════════════════════════

alter table kinder_zuordnung enable row level security;

create policy "admin_all" on kinder_zuordnung
  for all
  using (
    exists (select 1 from profiles p where p.id = auth.uid() and p.rolle = 'admin')
  );

create policy "tk_manage" on kinder_zuordnung
  for all
  using ( tk_id = auth.uid() );

create policy "ingra_read" on kinder_zuordnung
  for select
  using ( ingra_id = auth.uid() );

create policy "trainer_read" on kinder_zuordnung
  for select
  using ( trainer_id = auth.uid() );


-- ================================================================
-- 0028_fallakte_formular.sql
-- ================================================================
-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration
-- Fallakte-Formular (FM-01): erweiterte Stammdaten + Mehrfach-Listen
--
-- Ergänzt fallakten (0004_fallmanagement.sql) um die im Formular
-- benötigten Einzelfelder. Die bereits bestehenden Freitextspalten
-- bezugsperson/bezugsperson_kontakt/ziele bleiben unverändert erhalten
-- (kein Drop), werden vom neuen Formular aber nicht mehr befüllt -
-- Bezugspersonen, Netzwerk-Kontakte und Ziele sind jetzt Mehrfach-Listen
-- in eigenen Tabellen (siehe unten), da eine Fallakte davon mehrere
-- haben kann.
-- ════════════════════════════════════════════════════════════

alter table fallakten
  add column rechtsgrundlage      text check (rechtsgrundlage in ('sgb_viii_35a','sgb_ix_54','sonstige')),
  add column kostentraeger        text,
  add column stundenumfang        text,
  add column befristet_bis        date,
  add column ingra_id             uuid references profiles(id),
  add column vertretung_ingra_id  uuid references profiles(id);

comment on column fallakten.ingra_id is
  'Zuständige INGRA für die Fallakte. Vorbelegt aus kinder_zuordnung.ingra_id, im Formular änderbar.';
comment on column fallakten.vertretung_ingra_id is
  'Vertretung der zuständigen INGRA, frei wählbar aus profiles (rolle=ingra).';

-- ── Bezugspersonen: mehrere pro Fallakte ────────────────────────
create table fallakte_bezugspersonen (
  id           uuid primary key default gen_random_uuid(),
  fallakte_id  uuid not null references fallakten(id) on delete cascade,
  name         text not null,
  rolle        text,
  created_at   timestamptz not null default now()
);

-- ── Netzwerk: externe Kontakte, mehrere pro Fallakte ────────────
create table fallakte_netzwerk (
  id           uuid primary key default gen_random_uuid(),
  fallakte_id  uuid not null references fallakten(id) on delete cascade,
  name         text not null,
  rolle        text,
  kontakt      text,
  created_at   timestamptz not null default now()
);

-- ── Ziele: strukturierte Mehrfach-Liste (ersetzt fallakten.ziele) ──
create table fall_ziele (
  id           uuid primary key default gen_random_uuid(),
  fallakte_id  uuid not null references fallakten(id) on delete cascade,
  ziel         text not null,
  indikator    text,
  zieldatum    date,
  created_at   timestamptz not null default now()
);

-- ── RLS: gleiche Sichtbarkeit wie die zugehörige Fallakte (Muster aus
--    fall_risikostatus_ueber_fallakte / fall_timeline_ueber_fallakte in
--    0004_fallmanagement.sql) ─────────────────────────────────────
alter table fallakte_bezugspersonen enable row level security;
alter table fallakte_netzwerk enable row level security;
alter table fall_ziele enable row level security;

create policy fallakte_bezugspersonen_ueber_fallakte
  on fallakte_bezugspersonen for all
  using (exists (select 1 from fallakten f where f.id = fallakte_bezugspersonen.fallakte_id));

create policy fallakte_netzwerk_ueber_fallakte
  on fallakte_netzwerk for all
  using (exists (select 1 from fallakten f where f.id = fallakte_netzwerk.fallakte_id));

create policy fall_ziele_ueber_fallakte
  on fall_ziele for all
  using (exists (select 1 from fallakten f where f.id = fall_ziele.fallakte_id));


-- ================================================================
-- 0029_fall_timeline_formular.sql
-- ================================================================
-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration
-- Verlauf-Formular (FM-04): Fakten von Einschätzung trennen
--
-- fall_timeline existiert bereits (0004_fallmanagement.sql), aber mit
-- anderen Spalten (ereignis/beobachtung/rueckmeldung als lose
-- Freitextfelder, keine ereignistyp-Kategorisierung, kein fakten/
-- einschaetzung-Split). Nicht "passend" wie fall_massnahmen - deshalb
-- hier erweitert statt unverändert übernommen. Die alten Spalten
-- bleiben unangetastet (kein Drop), werden vom neuen Formular aber
-- nicht mehr befüllt.
--
-- RLS bleibt unverändert: die bestehende Policy
-- fall_timeline_ueber_fallakte (Sichtbarkeit über die zugehörige
-- Fallakte) gilt unabhängig von den Spalten weiter.
-- ════════════════════════════════════════════════════════════

alter table fall_timeline
  add column ereignistyp   text check (ereignistyp in ('beobachtung','gespraech','vorfall','uebergabe')),
  add column fakten        text,
  add column einschaetzung text;

comment on column fall_timeline.fakten is
  'Beobachtbare Fakten - bewusst getrennt von einschaetzung, um Beobachtung nicht mit Deutung zu vermischen.';
comment on column fall_timeline.einschaetzung is
  'Fachliche Einschätzung/Deutung - getrennt von fakten (siehe dort).';


-- ================================================================
-- 0030_barometer_kind_tk_source.sql
-- ================================================================
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


-- ================================================================
-- 0031_neues_schema_kind_fk.sql
-- ================================================================
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


-- ================================================================
-- 0032_fallmanagement_kind_fk.sql
-- ================================================================
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


-- ================================================================
-- 0033_weiterleitungen_antwort.sql
-- ================================================================
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


-- ================================================================
-- 0034_neues_schema_select_policies.sql
-- ================================================================
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
--
-- Nachtrag: per Browser-Konsole bestätigt (404 auf .from('INGRA')) heißt
-- die INGRA-Tabelle tatsächlich "ingra" (klein, unquotiert), nicht "INGRA"
-- - anders als bei "Kinder"/"TK". Policy-Ziel unten entsprechend korrigiert,
-- bevor diese Migration angewendet wird (sonst "relation does not exist").
-- ════════════════════════════════════════════════════════════

create policy authenticated_can_select_kinder
  on "Kinder" for select
  to authenticated
  using (true);

create policy authenticated_can_select_ingra
  on ingra for select
  to authenticated
  using (true);

create policy authenticated_can_select_tk
  on "TK" for select
  to authenticated
  using (true);


-- ================================================================
-- 0035_weiterleitungen_barometer_kind_rls.sql
-- ================================================================
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


-- ================================================================
-- 0036_person_auth_map.sql
-- ================================================================
-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration
-- person_auth_map: E-Mail → echte Supabase-Auth-UID
--
-- Erster Baustein für eine echte KlarApp-Kontaktliste. Die Tabellen
-- des "neuen Schemas" (ingra/"TK"/"Kinder", siehe 0034) haben KEINE
-- Verknüpfung zu auth.users - ihre Zeilen werden nur per E-Mail-
-- Abgleich der eigenen Login-Session zugeordnet (vgl. aktuelleIngraId()
-- in KLARTEXT_Tagesjournal.html/KLARTEXT_Zeitkonto.html etc.). Für eine
-- echte KlarApp-Kontaktliste wird aber die auth.users.id ANDERER
-- Personen benötigt, um Firebase-Konversationen (conv.members[uid])
-- korrekt zu verlinken - die gibt es bisher nirgends zum Nachschlagen.
--
-- Diese Tabelle schließt genau diese Lücke: jede Person schreibt bei
-- jedem Login ihre eigene Zeile (E-Mail → eigene auth.users.id,
-- Anzeigename, aktuell gewählte Rolle).
--
-- role ist bewusst text statt des klartext_rolle-Enums aus 0001, da
-- das Login-Rollen-Dropdown auch "ingra-beta" kennt - ein Wert, den
-- das Enum nicht abdeckt.
--
-- Reine Datenstruktur - wird manuell im SQL-Editor ausgeführt, nicht
-- automatisch.
-- ════════════════════════════════════════════════════════════

create table person_auth_map (
  email     text primary key,
  auth_uid  uuid not null,
  name      text,
  role      text
);

comment on table person_auth_map is
  'E-Mail -> echte auth.users.id, gepflegt bei jedem Login. Baustein für die echte KlarApp-Kontaktliste (siehe CHAT_New.html).';

alter table person_auth_map enable row level security;

-- Alle eingeloggten Nutzer dürfen die komplette Kontaktliste lesen
-- (gleiche Blanket-Logik wie authenticated_can_select_ingra in 0034).
create policy person_auth_map_select_all
  on person_auth_map for select
  to authenticated
  using (true);

-- Jede Person darf nur ihre EIGENE Zeile anlegen: auth_uid muss der
-- eigenen Auth-UID entsprechen UND email muss der eigenen, im JWT
-- hinterlegten Login-E-Mail entsprechen. Nur auth_uid = auth.uid() zu
-- prüfen reicht nicht - ohne den email-Abgleich könnte sich jemand
-- eine fremde, noch nie eingeloggte E-Mail-Adresse mit der eigenen UID
-- vorab sichern und damit die echte Person später aussperren.
create policy person_auth_map_insert_own
  on person_auth_map for insert
  to authenticated
  with check (
    auth_uid = auth.uid()
    and email = auth.jwt() ->> 'email'
  );

-- Und beim Login-Upsert entsprechend auch nur die eigene Zeile
-- aktualisieren dürfen. email ebenfalls an den JWT-Claim gebunden -
-- sonst könnte die eigene, bestehende Zeile per UPDATE ... SET email
-- auf eine fremde E-Mail-Adresse umbenannt werden (gleiche Lücke wie
-- bei person_auth_map_insert_own, nur über UPDATE statt INSERT).
create policy person_auth_map_update_own
  on person_auth_map for update
  to authenticated
  using (auth_uid = auth.uid())
  with check (
    auth_uid = auth.uid()
    and email = auth.jwt() ->> 'email'
  );


-- ================================================================
-- 0037_krankmeldungen_schema_korrektur.sql
-- ================================================================
-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration
-- Nachtrag/Dokumentation: krankmeldungen wurde bereits live auf das
-- "neue Schema" umgestellt
--
-- Die Migrationen 0018_krankmeldungen.sql und 0025_krankmeldungen_rls.sql
-- im Repo spiegeln nicht mehr den tatsächlichen Live-Zustand wider.
-- Laut direkter Prüfung der Live-DB (SQL-Editor) gilt inzwischen:
--   - krankmeldungen.ingra_id  -> FK auf ingra(id)   (nicht profiles(id))
--   - krankmeldungen.kind_id   -> FK auf "Kinder"(id) (nicht kinder(id))
-- Passend dazu wurde KLARTEXT_Krankmeldung.html umgestellt: ladeMeld()/
-- speichKrank() lösen ingra_id jetzt über aktuelleIngraId() auf
-- (E-Mail aus der Auth-Session -> ingra.id), nicht mehr über die rohe
-- Auth-UID. weiterleitungen.von_profil bleibt unverändert die echte
-- Auth-UID (dort existiert diese Diskrepanz nicht).
--
-- WICHTIG - Vertrauenswürdigkeit dieser Migration:
-- Ich habe KEINEN Zugriff auf die Live-Datenbank und kann die exakte
-- Formulierung der unten stehenden RLS-Policies nicht gegen die
-- tatsächlich aktiven Policies verifizieren. Die FK-Ziele (ingra_id ->
-- ingra(id), kind_id -> "Kinder"(id)) wurden explizit bestätigt: dieser
-- Teil ist verlässlich. Die RLS-Policies unten sind eine PLAUSIBLE
-- REKONSTRUKTION nach dem in dieser Session bereits etablierten Muster
-- (Auflösung von auth.uid() -> ingra.id über person_auth_map, analog
-- zu aktuelleIngraId() im Tagesjournal) - vor dem Ausführen unbedingt
-- gegen die tatsächlich aktive Policy-Definition in der Live-DB prüfen
-- und bei Abweichungen anpassen, statt blind auszuführen.
--
-- Diese Migration NICHT ausführen, wenn die Live-DB bereits entsprechend
-- geändert ist (sonst schlagen "add constraint"/"create policy" fehl,
-- weil die Ziele schon existieren) - sie dient hier primär als
-- schriftliche Dokumentation des Ist-Zustands fürs Repo.
-- ════════════════════════════════════════════════════════════

-- ── FKs auf das neue Schema umstellen ──────────────────────────
alter table krankmeldungen drop constraint if exists krankmeldungen_ingra_id_fkey;
alter table krankmeldungen drop constraint if exists krankmeldungen_kind_id_fkey;

alter table krankmeldungen
  add constraint krankmeldungen_ingra_id_fkey foreign key (ingra_id) references ingra(id);
alter table krankmeldungen
  add constraint krankmeldungen_kind_id_fkey foreign key (kind_id) references "Kinder"(id);

-- ── RLS: ingra_id ist jetzt ingra(id), nicht mehr auth.uid() direkt -
-- Auflösung der eigenen ingra_id über person_auth_map (auth_uid -> email
-- -> ingra.id), analog zu aktuelleIngraId() in KLARTEXT_Krankmeldung.html/
-- KLARTEXT_Tagesjournal.html. Rekonstruktion, siehe Hinweis oben.
drop policy if exists krankmeldungen_select on krankmeldungen;
drop policy if exists krankmeldungen_insert on krankmeldungen;
drop policy if exists krankmeldungen_update on krankmeldungen;
drop policy if exists krankmeldungen_delete on krankmeldungen;

create policy krankmeldungen_select
  on krankmeldungen for select
  to authenticated
  using (
    ingra_id in (
      select i.id from ingra i
      join person_auth_map m on m.email = i.email
      where m.auth_uid = auth.uid()
    )
    or exists (
      select 1 from person_auth_map m
      where m.auth_uid = auth.uid() and m.role in ('tk', 'admin')
    )
  );

create policy krankmeldungen_insert
  on krankmeldungen for insert
  to authenticated
  with check (
    ingra_id in (
      select i.id from ingra i
      join person_auth_map m on m.email = i.email
      where m.auth_uid = auth.uid()
    )
  );

create policy krankmeldungen_update
  on krankmeldungen for update
  to authenticated
  using (
    ingra_id in (
      select i.id from ingra i
      join person_auth_map m on m.email = i.email
      where m.auth_uid = auth.uid()
    )
  )
  with check (
    ingra_id in (
      select i.id from ingra i
      join person_auth_map m on m.email = i.email
      where m.auth_uid = auth.uid()
    )
  );

create policy krankmeldungen_delete
  on krankmeldungen for delete
  to authenticated
  using (
    ingra_id in (
      select i.id from ingra i
      join person_auth_map m on m.email = i.email
      where m.auth_uid = auth.uid()
    )
  );


-- ================================================================
-- 0038_fallmanagement_case_management.sql
-- ================================================================
-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration
-- Case-Management: fallakte + Fallbesprechungen + Meldebogen §8a +
-- Fallabschluss
--
-- HINTERGRUND (Live-DB-Befund, vor dem Schreiben dieser Migration
-- geprüft): Die ursprünglich für dieses Feature vorgesehene
-- Grundlage - fallakten/fall_risikostatus/fall_massnahmen/fall_timeline
-- aus 0004/0005/0028/0029 - existiert live in Supabase NICHT. Eine
-- direkte SQL-Prüfung des public-Schemas ergab als vollständige
-- Tabellenliste nur: Kinder, barometer_kind, externe_portale, ingra,
-- kind_ingra_zuteilung, kinder, krankmeldungen, person_auth_map,
-- portale. Auch "profiles" (0001) existiert nicht - das komplette
-- rollenbasierte RLS-Muster aus 0001_auth_rollen.sql ist damit
-- gegenstandslos für alles, was auf "Kinder" (groß) aufbaut.
--
-- TK_Fallmanagement.html und TK_Kinderzuordnung.html laufen aktuell
-- gegen genau diese nie live gegangenen Tabellen und sind daher schon
-- vor dieser Migration nicht funktionsfähig (Formulare/Frontend werden
-- in einem separaten, späteren Task neu an das hier geschaffene Schema
-- angebunden - nicht Teil dieser Migration).
--
-- Diese Migration baut deshalb bewusst NICHT auf 0004-0032 auf,
-- sondern schafft ein schlankes, neues Fallakte-Konzept direkt auf der
-- tatsächlich aktiven Grundlage: Kinder (groß), ingra, kind_ingra_
-- zuteilung, person_auth_map - demselben Fundament, auf dem
-- KLARTEXT_Tagesjournal.html, KLARTEXT_Krankmeldung.html,
-- KLARTEXT_Urlaubsantrag_INGRA.html, KLARTEXT_Zeitkonto.html und
-- TK_Vertretungsassistent.html bereits nachweislich laufen.
--
-- Gegenüber der alten, nie live gegangenen Fallakte-Vorstellung fallen
-- bewusst weg (siehe Absprache): Risikostatus-Ampel-Verlauf,
-- Bezugspersonen-/Netzwerk-Listen, strukturierte Ziele-Liste,
-- Maßnahmen-Tracking, laufende Verlauf-Chronik mit Ereignistyp-
-- Kategorisierung, Rechtsgrundlage/Kostenträger/Stundenumfang/
-- Befristung, ein separates Vertretungs-INGRA-Feld (kind_ingra_
-- zuteilung deckt das bereits ab) sowie freie Ressourcen-/
-- Besonderheiten-Textfelder. Das neue Schema ist bewusst minimal und
-- erweiterbar, kein Nachbau des alten Umfangs.
--
-- RLS-Modell: "Kinder"/ingra/kind_ingra_zuteilung haben live keine
-- feingranulare RLS (nur Blanket-"authenticated using (true)", siehe
-- 0034) - Zugriffskontrolle lief bisher rein über Frontend-Guards.
-- Für die hier neu geschaffenen, teils hochsensiblen Tabellen
-- (insbesondere den Meldebogen §8a) wird echte, in der Datenbank
-- durchgesetzte RLS aufgebaut, nicht nur Frontend-Vertrauen. Einzige
-- verlässliche Brücke von auth.uid() zu einer Rolle ist person_auth_map
-- (email -> auth_uid -> role je aktuellem Login), analog zu der in
-- 0037 für krankmeldungen rekonstruierten Policy-Logik.
--
-- Additiv, nichts Bestehendes verändert oder gelöscht. Wird manuell im
-- Supabase SQL Editor ausgeführt, nicht automatisch.
-- ════════════════════════════════════════════════════════════

-- ── Hilfsfunktionen für RLS ─────────────────────────────────────
-- Ob die eingeloggte Person laut ihrer letzten Login-Zeile in
-- person_auth_map die Rolle TK oder Admin hat.
create or replace function ist_tk_oder_admin()
returns boolean
language sql
stable
security definer
set search_path = public
as $$
  select exists (
    select 1 from person_auth_map m
    where m.auth_uid = auth.uid() and m.role in ('tk', 'admin')
  );
$$;

-- Die ingra.id der eingeloggten Person, aufgelöst über die Login-
-- E-Mail aus person_auth_map (analog zu aktuelleIngraId() im
-- Frontend, z.B. KLARTEXT_Tagesjournal.html). NULL, wenn die
-- eingeloggte Person keine INGRA ist oder noch nie eingeloggt war.
create or replace function aktuelle_ingra_id()
returns uuid
language sql
stable
security definer
set search_path = public
as $$
  select i.id from ingra i
  join person_auth_map m on m.email = i.email
  where m.auth_uid = auth.uid()
  limit 1;
$$;

-- Ob die eingeloggte INGRA einem Kind zugeordnet ist - entweder
-- regulär (Kinder.ingra_id) oder per aktiver Vertretung
-- (kind_ingra_zuteilung, rolle='vertretung', aktiv=true) - identisches
-- Zuordnungsmuster wie in KLARTEXT_Tagesjournal.html.
create or replace function ist_ingra_fuer_kind(p_kind_id uuid)
returns boolean
language sql
stable
security definer
set search_path = public
as $$
  select
    exists (
      select 1 from "Kinder" k
      where k.id = p_kind_id and k.ingra_id = aktuelle_ingra_id()
    )
    or exists (
      select 1 from kind_ingra_zuteilung z
      where z.kind_id = p_kind_id
        and z.ingra_id = aktuelle_ingra_id()
        and z.rolle = 'vertretung'
        and z.aktiv = true
    );
$$;

-- ── fallakte: schlanker neuer Fall-Datensatz ─────────────────────
-- Muss vor ist_ingra_fuer_fallakte() angelegt werden, da diese
-- Funktion die Tabelle referenziert.
create table fallakte (
  id            uuid primary key default gen_random_uuid(),
  kind_id       uuid not null references "Kinder"(id),
  status        text not null check (status in ('laufend', 'review', 'abgeschlossen')) default 'laufend',
  erstellt_von  uuid references auth.users(id) default auth.uid(),
  created_at    timestamptz not null default now()
);

comment on table fallakte is
  'Schlanker Fall-Datensatz auf Basis von "Kinder" (nicht der alten, nie live gegangenen fallakten aus 0004/0028). Anker für Fallbesprechungen, Meldebogen §8a und Fallabschluss.';
comment on column fallakte.status is
  'Fallstatus-Workflow: laufend -> review -> abgeschlossen.';

-- Dieselbe Prüfung, ausgehend von einer fallakte_id statt kind_id -
-- spart den Join in jeder einzelnen Policy der drei Kind-Tabellen.
create or replace function ist_ingra_fuer_fallakte(p_fallakte_id uuid)
returns boolean
language sql
stable
security definer
set search_path = public
as $$
  select exists (
    select 1 from fallakte fa
    where fa.id = p_fallakte_id and ist_ingra_fuer_kind(fa.kind_id)
  );
$$;

comment on function ist_tk_oder_admin() is
  'RLS-Hilfsfunktion: prüft die Rolle der eingeloggten Person über person_auth_map.role (gepflegt bei jedem Login, siehe 0036).';
comment on function aktuelle_ingra_id() is
  'RLS-Hilfsfunktion: löst auth.uid() über person_auth_map (E-Mail) zur passenden ingra.id auf.';
comment on function ist_ingra_fuer_kind(uuid) is
  'RLS-Hilfsfunktion: prüft reguläre Zuordnung (Kinder.ingra_id) und aktive Vertretung (kind_ingra_zuteilung) für die eingeloggte INGRA.';
comment on function ist_ingra_fuer_fallakte(uuid) is
  'RLS-Hilfsfunktion: wie ist_ingra_fuer_kind, ausgehend von einer fallakte_id.';

-- ── tk_fallbesprechungen: reines TK-Modul, kein INGRA-Zugriff ────
create table tk_fallbesprechungen (
  id                uuid primary key default gen_random_uuid(),
  fallakte_id       uuid not null references fallakte(id) on delete cascade,
  tk_id             uuid references auth.users(id) default auth.uid(),
  datum             date not null default current_date,
  protokoll_text    text,
  ziele_text        text,
  naechster_termin  date,
  created_at        timestamptz not null default now()
);

comment on table tk_fallbesprechungen is
  'Fallbesprechungsprotokolle. Reines TK-Modul - keine Weiterleitung an INGRA, kein INGRA-Zugriff.';

-- ── meldebogen_8a: Schutzauftrag-Meldebogen, strikt vertraulich ──
create table meldebogen_8a (
  id                uuid primary key default gen_random_uuid(),
  fallakte_id       uuid not null references fallakte(id) on delete cascade,
  ingra_id          uuid references auth.users(id) default auth.uid(),
  tk_id             uuid references auth.users(id),
  meldedatum        date not null default current_date,
  sachverhalt_text  text,
  einschaetzung     text,
  massnahmen        text,
  status            text not null check (status in ('offen', 'in_arbeit', 'abgeschlossen')) default 'offen',
  created_at        timestamptz not null default now()
);

comment on table meldebogen_8a is
  'Schutzauftrag-Meldebogen nach §8a SGB VIII. Strikt vertraulich: TK/Admin lesen und schreiben alles, meldende INGRA sieht ausschließlich die eigene(n) Meldung(en), keinen Zugriff auf fremde Einträge.';
comment on column meldebogen_8a.ingra_id is
  'Meldende Person. Wird beim Anlegen serverseitig gegen die eingeloggte INGRA geprüft (siehe RLS unten) - kann nicht auf eine fremde Person gesetzt werden.';

-- ── fallabschluss: Abschluss-Checkliste + Bericht ────────────────
create table fallabschluss (
  id                       uuid primary key default gen_random_uuid(),
  fallakte_id              uuid not null references fallakte(id) on delete cascade,
  abschlussdatum           date not null default current_date,
  ziele_erreicht           boolean not null default false,
  uebergabe_dokumentiert   boolean not null default false,
  eltern_informiert        boolean not null default false,
  unterlagen_vollstaendig  boolean not null default false,
  abschlussbericht_text    text,
  erstellt_von             uuid references auth.users(id) default auth.uid(),
  created_at               timestamptz not null default now()
);

comment on table fallabschluss is
  'Fallabschluss-Bericht mit einfacher Checkliste. TK/Admin lesen/schreiben, INGRA liest (für zugeordnete Kinder), kein INGRA-Schreibzugriff.';

-- ── RLS ────────────────────────────────────────────────────────
alter table fallakte enable row level security;
alter table tk_fallbesprechungen enable row level security;
alter table meldebogen_8a enable row level security;
alter table fallabschluss enable row level security;

-- fallakte: TK/Admin lesen+schreiben alles, INGRA liest nur für
-- zugeordnete Kinder (kein INGRA-Schreibzugriff - Fallmanagement
-- bleibt TK-Aufgabe).
create policy fallakte_tk_admin_all
  on fallakte for all
  using (ist_tk_oder_admin());

create policy fallakte_ingra_select
  on fallakte for select
  using (ist_ingra_fuer_kind(kind_id));

-- tk_fallbesprechungen: ausschließlich TK/Admin, kein INGRA-Zugriff.
create policy tk_fallbesprechungen_tk_admin_all
  on tk_fallbesprechungen for all
  using (ist_tk_oder_admin());

-- meldebogen_8a: TK/Admin lesen+schreiben alles. INGRA darf für
-- zugeordnete Kinder eine eigene Meldung anlegen (mit erzwungenem
-- ingra_id = eigene Person, verhindert Vortäuschen einer fremden
-- Meldung) und sieht danach ausschließlich die eigenen Meldungen -
-- kein Lesezugriff auf fremde Einträge. Gleiches Insert-dann-nur-
-- eigenes-lesen-Muster wie weiterleitungen_ingra_insert /
-- weiterleitungen_select_eigene in 0008_weiterleitungen.sql.
create policy meldebogen_8a_tk_admin_all
  on meldebogen_8a for all
  using (ist_tk_oder_admin());

create policy meldebogen_8a_ingra_insert
  on meldebogen_8a for insert
  with check (
    ingra_id = auth.uid()
    and ist_ingra_fuer_fallakte(fallakte_id)
  );

create policy meldebogen_8a_ingra_select_eigene
  on meldebogen_8a for select
  using (ingra_id = auth.uid());

-- fallabschluss: TK/Admin lesen+schreiben alles, INGRA liest nur für
-- zugeordnete Kinder (kein INGRA-Schreibzugriff).
create policy fallabschluss_tk_admin_all
  on fallabschluss for all
  using (ist_tk_oder_admin());

create policy fallabschluss_ingra_select
  on fallabschluss for select
  using (ist_ingra_fuer_fallakte(fallakte_id));


-- ================================================================
-- 0039_fall_chronik_risikostatus.sql
-- ================================================================
-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration
-- Verlauf-Chronik (fall_timeline) + Risikostatus-Ampel (fall_risikostatus)
--
-- Zieht zwei der in 0038 bewusst zurückgestellten Bausteine additiv
-- auf dem dort geschaffenen schlanken Schema nach (fallakte + die
-- vier RLS-Hilfsfunktionen ist_tk_oder_admin/aktuelle_ingra_id/
-- ist_ingra_fuer_kind/ist_ingra_fuer_fallakte). Live-Voraussetzung
-- (fallakte existiert) vor dem Schreiben dieser Migration bestätigt.
--
-- fall_timeline: laufendes, chronologisches Beobachtungslog - kein
-- Einzelprotokoll wie tk_fallbesprechungen. Fakten/Einschätzung
-- bewusst getrennt (wie im alten, nie live gegangenen fall_timeline
-- aus 0029). Lesezugriff für INGRA gilt für alle Einträge des
-- zugeordneten Falls (nicht nur selbst erstellte) - identisches
-- Prinzip wie die ursprüngliche fall_timeline_select_ingra-Policy aus
-- 0005: eine laufende Chronik ist als gemeinsame Fallgeschichte
-- gedacht, nicht als Sammlung isolierter Einzelbeiträge pro Person.
-- Schreibzugriff (Einträge anlegen) bleibt aber auf die eigene Person
-- bezogen (erstellt_von = auth.uid(), erzwungen).
--
-- fall_risikostatus: laufender Ampel-Verlauf statt Einzelstatusfeld.
-- "Historie muss erhalten bleiben" wird hier bewusst auch technisch
-- durchgesetzt: TK/Admin dürfen Einträge anlegen und lesen, aber
-- weder ändern noch löschen (kein UPDATE/DELETE) - eine fehlerhafte
-- Ampel-Einschätzung wird durch einen neuen, korrigierenden Eintrag
-- ergänzt statt die Historie zu überschreiben. Der "aktuelle" Status
-- ergibt sich aus dem Eintrag mit dem neuesten created_at je
-- fallakte_id - bewusst kein zusätzliches, separates Statusfeld,
-- keine eigene View (nicht angefragt, hier zusätzlich einzuführende
-- Komplexität) - einfach "order by created_at desc limit 1" auf
-- fallakte_id filtern.
--
-- Additiv, nichts Bestehendes verändert oder gelöscht. Wird manuell im
-- Supabase SQL Editor ausgeführt, nicht automatisch.
-- ════════════════════════════════════════════════════════════

-- ── fall_timeline: laufende Verlauf-Chronik ──────────────────────
create table fall_timeline (
  id                 uuid primary key default gen_random_uuid(),
  fallakte_id        uuid not null references fallakte(id) on delete cascade,
  ereignistyp        text check (ereignistyp in ('beobachtung', 'gespraech', 'vorfall', 'uebergabe')),
  fakten_text        text,
  einschaetzung_text text,
  erstellt_von       uuid references auth.users(id) default auth.uid(),
  created_at         timestamptz not null default now()
);

comment on table fall_timeline is
  'Laufendes, chronologisches Beobachtungslog pro Fall - viele Einträge über die Zeit, kein Einzelprotokoll wie tk_fallbesprechungen.';
comment on column fall_timeline.fakten_text is
  'Beobachtbare Fakten - bewusst getrennt von einschaetzung_text, um Beobachtung nicht mit Deutung zu vermischen (wie im alten fall_timeline aus 0029).';
comment on column fall_timeline.einschaetzung_text is
  'Fachliche Einschätzung/Deutung - getrennt von fakten_text (siehe dort).';

-- ── fall_risikostatus: laufender Ampel-Verlauf ───────────────────
create table fall_risikostatus (
  id             uuid primary key default gen_random_uuid(),
  fallakte_id    uuid not null references fallakte(id) on delete cascade,
  ampel          text not null check (ampel in ('gruen', 'gelb', 'rot')),
  begruendung_text text,
  gesetzt_von    uuid references auth.users(id) default auth.uid(),
  created_at     timestamptz not null default now()
);

comment on table fall_risikostatus is
  'Laufender Ampel-Verlauf (kein Einzelstatusfeld) - Historie bleibt vollständig erhalten, siehe RLS unten. Aktueller Status = Eintrag mit neuestem created_at je fallakte_id.';

-- ── RLS ────────────────────────────────────────────────────────
alter table fall_timeline enable row level security;
alter table fall_risikostatus enable row level security;

-- fall_timeline: TK/Admin voller Zugriff (lesen, schreiben, auch
-- korrigieren/löschen - anders als beim Risikostatus gibt es hier
-- keine ausdrückliche Unveränderlichkeits-Anforderung).
create policy fall_timeline_tk_admin_all
  on fall_timeline for all
  using (ist_tk_oder_admin());

-- INGRA liest ALLE Einträge des zugeordneten Falls (gemeinsame
-- Chronik, siehe Erläuterung oben) ...
create policy fall_timeline_ingra_select
  on fall_timeline for select
  using (ist_ingra_fuer_fallakte(fallakte_id));

-- ... darf aber nur eigene Einträge anlegen (erstellt_von serverseitig
-- gegen die eigene auth.uid() erzwungen, kein Vortäuschen fremder
-- Urheberschaft) und nur für Fälle, denen sie zugeordnet ist.
create policy fall_timeline_ingra_insert
  on fall_timeline for insert
  with check (
    erstellt_von = auth.uid()
    and ist_ingra_fuer_fallakte(fallakte_id)
  );

-- fall_risikostatus: TK/Admin dürfen anlegen und lesen, aber bewusst
-- NICHT ändern oder löschen (kein "for all") - die Ampel-Historie
-- bleibt vollständig erhalten. Zwei separate Policies statt einer.
create policy fall_risikostatus_tk_admin_select
  on fall_risikostatus for select
  using (ist_tk_oder_admin());

create policy fall_risikostatus_tk_admin_insert
  on fall_risikostatus for insert
  with check (ist_tk_oder_admin());

-- INGRA liest den Ampel-Verlauf für zugeordnete Fälle, kein
-- Schreibzugriff (Risikoeinschätzung bleibt TK-Aufgabe).
create policy fall_risikostatus_ingra_select
  on fall_risikostatus for select
  using (ist_ingra_fuer_fallakte(fallakte_id));


-- ================================================================
-- 0040_kind_buch.sql
-- ================================================================
-- ════════════════════════════════════════════════════════════
-- KLARTEXT · Supabase-Migration
-- "Unser Buch" - Sammlung von Beobachtungen/Aussagen zu einem Kind,
-- gegliedert nach Kategorie (mag/hilft/stress/staerken/sonstiges)
--
-- Additiv, nichts Bestehendes verändert oder gelöscht. Wird manuell im
-- Supabase SQL Editor ausgeführt, nicht automatisch.
-- ════════════════════════════════════════════════════════════

create table kind_buch_eintraege (
  id uuid primary key default gen_random_uuid(),
  kind_id uuid not null references "Kinder"(id),
  kategorie text not null check (kategorie in ('mag','hilft','stress','staerken','sonstiges')),
  text text not null,
  verfasst_von text not null default 'ingra' check (verfasst_von in ('kind','ingra')),
  ingra_id uuid references ingra(id),
  erstellt_am timestamptz not null default now()
);

alter table kind_buch_eintraege enable row level security;

-- Gleiches Blanket-Muster wie tagesjournal_eintraege (bereits live
-- geprüft: authenticated = voller Zugriff, Kind-Zuordnung läuft
-- bewusst im Frontend, nicht in RLS — Konsistenz mit dem Rest des
-- neuen Schemas, kein neues Muster einführen):
create policy authenticated_can_select_kind_buch_eintraege
  on kind_buch_eintraege for select to authenticated using (true);
create policy authenticated_can_insert_kind_buch_eintraege
  on kind_buch_eintraege for insert to authenticated with check (true);
create policy authenticated_can_update_kind_buch_eintraege
  on kind_buch_eintraege for update to authenticated using (true) with check (true);
create policy authenticated_can_delete_kind_buch_eintraege
  on kind_buch_eintraege for delete to authenticated using (true);


-- ================================================================
-- 0041_admin_rolle_einschraenken.sql
-- ================================================================
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


