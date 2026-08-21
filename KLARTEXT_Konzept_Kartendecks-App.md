# KLARTEXT · Konzept Kartendecks-App (eigenständige Flip-Card-App)

Stand: 07.08.2026. Empfehlung nach Anjas Bitte um eine klare Vorgehensweise, da die Architektur
(Admin-App, Shop, Shop-Lite) unübersichtlich geworden war.

## Ausgangslage in einem Satz

Drei Bausteine existieren nebeneinander, aus unterschiedlichen historischen Gründen entstanden
(siehe Merkliste Strang 54) — die Frage ist nicht "was ist richtig", sondern "was bauen wir
zuerst, und wo läuft es".

| Baustein | Was | Läuft wo | Status |
|---|---|---|---|
| Admin-App | Case-Management/Fallmanagement, Supabase, Barometer Kind, Chat | `klartext-app-8kl.pages.dev` | Live, Pilot beendet, Supabase-Linie wegen DSGVO zurückgestellt (#233) |
| Shop | Marketing/Verkaufsseiten pro Deck, statisch | `klartext-mentoring.de` | Live |
| Shop-Lite (bisher gebaut) | Kompletter INGRA-Kurs (M0–M8, Fachbuch, Workbook) + Kartendecks, ohne Supabase | Nirgends deployed, nur Code im klartext-app-Repo | Fertig gebaut, nicht live |
| **Kartendecks-App (neu, hier empfohlen)** | **Nur die 22 Kartendecks, Flip-Cards + Suche** | **Neu aufzusetzen** | **Zu entscheiden** |

## Empfehlung

**Zuerst die schlanke Kartendecks-App bauen, nicht das komplette Shop-Lite live schalten.**

Begründung:
- Dein aktueller kommerzieller Fokus (dieser Chat, letzte Wochen) ist eindeutig der
  Kartendecks-Verkauf — eigener Shop, Etsy, eduki, gerade erst 3 neue Verkaufsseiten gebaut. Eine
  passende digitale Ergänzung dazu ist die Kartendecks-App, nicht der ganze INGRA-Kurs.
- Das komplette Shop-Lite (INGRA-Kurs + Module + Workbook) ist ein größeres, eigenständiges
  Produkt ("Gesamt-App", Strang 39) mit eigener Preis-/Vermarktungslogik — das lenkt jetzt nur ab
  und verzögert den kleineren, schneller fertigstellbaren Baustein.
- Technischer Vorsprung: Die Basis existiert bereits (`pwa/` in klartext-app) — Flip-Cards,
  Kartendaten für alle 22 Decks, kein Supabase. Muss nur ausgelagert, nicht neu entwickelt werden.
- Die Shop-Lite-Idee geht dabei nicht verloren, sie wird nur zeitlich nachgelagert.

## Deployment: eigenes, drittes Cloudflare-Pages-Projekt

**Empfehlung: neues, separates Repo + eigene Subdomain, z. B. `karten.klartext-mentoring.de`.**

Begründung (aus Professionalitäts-Sicht, wie gefragt):
- Gleiche Logik, die du schon bei der Trennung klartext-app/klartext-shop bewusst angewendet hast
  (siehe `README_klartextshop.md`: "damit sie nicht versehentlich auf derselben Cloudflare-Pages-
  Umgebung sichtbar werden"). Eine Kunden-App mit eigenem Datenzugriff (auch wenn nur
  Kartendaten) verdient dieselbe saubere Trennung von der Admin-App.
- Eigene Subdomain unter deiner Marke wirkt professioneller als eine nackte `*.pages.dev`-URL und
  lässt sich leicht von den Verkaufsseiten aus verlinken ("Jetzt als Flip-Card öffnen").
- Kein Mehraufwand gegenüber "unter klartext-mentoring.de einhängen": Cloudflare Pages
  unterstützt beliebig viele Projekte pro Konto kostenlos, die Subdomain-Einrichtung ist ein
  einmaliger DNS-Eintrag.

## Technischer Fahrplan (grob, zur Abstimmung — noch nicht umgesetzt)

1. Neues Repo `klartext-karten` (oder ähnlich) anlegen — du legst es an (GitHub), ich bekomme
   Zugriff wie bei den beiden bestehenden Repos.
2. `pwa/`-Ordner aus klartext-app als Ausgangspunkt kopieren (Kartendaten, Bilder, Flip-Logik,
   Manifest, Service Worker) — bereits Supabase-frei, keine Migration nötig.
3. Such-Leiste ergänzen: Volltextsuche über Titel/Fragen/Hinweise aller 22 Decks (technisch
   unkompliziert, reine Client-Suche über die bereits vorhandenen JSON-Kartendaten).
4. `homeBtn`-Link (aktuell `../DASHBOARD.html`, führt zurück in die Admin-App) entfernen bzw. auf
   den Shop umstellen.
5. Cloudflare Pages Projekt verbinden, Subdomain `karten.klartext-mentoring.de` einrichten (DNS-
   Schritt machst du im Cloudflare-Dashboard, ich gebe dir die genaue Anleitung).
6. Verlinkung von den Verkaufsseiten im Shop aus ergänzen.

## Bewusst noch NICHT Teil dieser Entscheidung

**Zugriffssteuerung pro gekauftem Deck** (wer sieht welches Deck als Flip-Card) wird hier bewusst
nicht mitgelöst. Empfehlung: für den Start alle 22 Decks frei zugänglich lassen (wie aktuell die
Vorschau-Karten auf den Verkaufsseiten), volle Kunden-Freischaltung erst mit echtem Checkout
(Elopage/Digistore24, siehe Strang 39) — sonst bauen wir jetzt ein Lizenzsystem, das beim
Checkout-Anbieter-Wechsel eventuell wieder angepasst werden muss. Diese Reihenfolge vermeidet
Doppelarbeit.

## Offene Entscheidung bei Anja

Passt diese Reihenfolge (zuerst schlanke Kartendecks-App, Shop-Lite/Gesamt-App später), und soll
ich mit Schritt 1 (Repo-Anlage) starten?
