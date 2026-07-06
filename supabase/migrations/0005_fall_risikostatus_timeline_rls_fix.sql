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
