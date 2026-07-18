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
