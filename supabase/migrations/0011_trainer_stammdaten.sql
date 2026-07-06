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
