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
