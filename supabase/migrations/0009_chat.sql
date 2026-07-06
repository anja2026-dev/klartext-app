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
