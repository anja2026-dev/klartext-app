# Shop-Paket — Ausschlussliste (Strang 38, Schritt 3)

Diese Liste dokumentiert, welche Dateien/Ordner aus `klartext-app` **nicht** in das
Supabase-freie Shop-/PWA-Produkt übernommen werden dürfen, und warum. Grundlage für
`build_shop_package.sh`. Nichts wird aus dem Haupt-Repo gelöscht — die Träger-Version
(Case-Management, Supabase) bleibt vollständig erhalten (Task #233, geparkt).

## 1. Funktional Supabase-/Firebase-abhängige HTML-Seiten (31)

Verifiziert per Grep auf tatsächliche API-Aufrufe (`supabase.from/auth/storage/channel`,
`firebase.initializeApp/auth/database`, `createClient(`, `import ... from './supabase/...'`),
nicht nur Text-Erwähnungen:

```
BAROMETER_KIND.html
CHAT_List.html
CHAT_New.html
CHAT_View.html
DASHBOARD.html                      → ersetzt durch DASHBOARD_Lite.html
DASHBOARD_mobile.html
Kinderverwaltung.html
KLARTEXT_Feedback_INGRA.html
KLARTEXT_Feedback_TK.html
KLARTEXT_Forward_Read.html
KLARTEXT_Krankmeldung.html
KLARTEXT_Listen.html
KLARTEXT_Login.html                 → ersetzt durch KLARTEXT_Login_Shop.html
KLARTEXT_Logout.html
KLARTEXT_Notizblock.html
KLARTEXT_Portale.html
KLARTEXT_Setup_Demo_Kinder.html
KLARTEXT_Tagesjournal.html
KLARTEXT_Teilnehmer_Protokoll.html
KLARTEXT_TK_Inbox.html
KLARTEXT_UnserBuch.html
KLARTEXT_Urlaubsantrag_INGRA.html
KLARTEXT_Weiterleiten.html
KLARTEXT_Weiterleitungen.html
KLARTEXT_Zeitkonto.html
TK_Fallmanagement.html
TK_Kinderzuordnung.html
TK_Landing.html
TK_Uebergaben.html
TK_Vertretungsassistent.html
feedback.html
feedbackAdmin.html
```

## 2. Interne Planungs-/Architektur-Dokumente (2)

Nicht kundenrelevant, unabhängig von Supabase — interne Konzeptseiten für die
App-Weiterentwicklung, kein Trainings-/Lerninhalt:

```
Admin_Backend.html
KLARTEXT_Vertretungsassistent_Architektur.html
```

## 3. Ordner, komplett ausgeschlossen

```
.git/                → Versionskontrolle, nie ausliefern
supabase/             → DB-Migrationen/Schema (39 SQL-Dateien), reine Backend-Konfiguration
__pycache__/          → Build-Artefakte der Karten-Pipelines
storybooks/           → geparkte Produktlinie (Strang 6: "keine neue Storybook-Produktlinie"),
                         kein Bestandteil des aktuellen Angebots
```

## Bewusst NICHT ausgeschlossen, aber als Folgeaufgabe notiert

`KLARTEXT_Trainerhandbuch.html` und `KLARTEXT_Systemanleitung.html` sind funktional
Supabase-frei (keine echten API-Aufrufe), enthalten aber Prosa-Verweise auf
Firebase-Funktionen, die es im Shop-Produkt nicht gibt (Kind-Barometer-Sync, Chat).
Bleiben vorerst im Paket (überwiegend gültiger Trainings-Content), sollten aber vor dem
Verkauf inhaltlich an die Lite-Version angepasst werden (die 1–2 betroffenen Absätze
entfernen/umschreiben) — eigener kleiner Content-Task, kein Blocker für die
Paket-Erstellung selbst.

## Ergebnis

33 Einzeldateien + 4 Ordner ausgeschlossen. Alle 344 Content-Seiten, die den
`klartext_login`-sessionStorage-Check nutzen (Kartendecks, Fachbuch, Workbook,
Lernpfad, Module M0–M8, Lernmaterialien etc.), sind Supabase-frei und bleiben
vollständig im Paket.

## 4. manifest.json (PWA-Startseite)

Das Root-`manifest.json` zeigt in der Live-Version über `start_url` auf
`KLARTEXT_Login.html` (Supabase) — diese Datei existiert im Shop-Paket nicht mehr.
`build_shop_package.sh` ersetzt `manifest.json` im Zielordner deshalb automatisch
durch `manifest_shop.json` (`start_url` → `KLARTEXT_Login_Shop.html`), damit eine
installierte Shop-PWA korrekt startet. `manifest_shop.json` selbst wird nicht als
eigene Datei mitkopiert, nur inhaltlich als `manifest.json` übernommen.

`pwa/manifest.json` (Kartendeck-Viewer) und `sw.js`/`pwa/service-worker.js`
brauchten keine Anpassung: Sie sind bereits Supabase-frei bzw. enthalten keine
feste Precache-Liste mit Login/Dashboard-Referenzen.
