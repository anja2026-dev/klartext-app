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
