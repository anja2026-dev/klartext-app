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
