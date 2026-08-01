# KLARTEXT-Mentoring Karten – PWA (Prototyp)

Digitale Flashcard-App für die KLARTEXT-Kartendecks. Vorderseite antippen → dreht sich zur
Rückseite mit Anleitung, Impulsfragen und Tipp. Kein Framework, kein Build-Schritt – reines
HTML/CSS/JS, offline-fähig als installierbare PWA.

## Aktueller Stand

Enthält bisher **1 Deck als Prototyp: KD-Deck (35 Karten)**. Die restlichen 18 Decks folgen nach
Freigabe – Aufwand pro Deck ist gering (siehe unten), da Engine und Datenformat schon stehen.

## Lokal testen

Service Worker brauchen `http://`, nicht `file://` – deshalb einen kleinen lokalen Server starten.
**Bitte `serve.py` verwenden, nicht `python3 -m http.server`** – der eingebaute Server setzt keine
Cache-Control-Header, wodurch Safari geänderte Dateien oft trotz Neuladen aus dem eigenen Cache
zeigt (nicht dem Service-Worker-Cache – dem ganz normalen Browser-Cache):

```bash
cd pwa
python3 serve.py
```

Dann im Browser (Handy im selben WLAN funktioniert auch über die lokale IP) öffnen:
`http://localhost:8080`

Falls in Safari trotzdem noch eine alte Version erscheint: Safari → Einstellungen →
Datenschutz → „Website-Daten verwalten" → „localhost" suchen → entfernen. Das löscht sowohl den
Browser-Cache als auch den Service-Worker-Cache für die App komplett.

Zum "Installieren" (Add to Home Screen) auf dem Handy: im Browser-Menü "Zum Startbildschirm
hinzufügen" – danach läuft die App wie eine native App, auch offline (einmal geöffnete Decks
bleiben gespeichert).

**Ein einzelnes Deck aufs Home-Bildschirm legen** (eigenes farbiges Icon + eigener Name, damit
es sich von anderen Decks/Apps unterscheidet): zuerst das gewünschte Deck in der App öffnen
(nicht auf der Übersichtsseite bleiben!), erst dann "Zum Home-Bildschirm hinzufügen" antippen.
Der Home-Bildschirm-Eintrag springt danach direkt in dieses Deck.

## Dauerhaft deployen (kostenlos, ohne Server)

Da `klartext-app` schon ein GitHub-Repo ist, bietet sich **GitHub Pages** an:
1. Repo-Einstellungen → Pages → Branch `main`, Ordner `/pwa` auswählen.
2. Die App ist dann unter `https://<dein-github-name>.github.io/klartext-app/` erreichbar –
   funktioniert auf jedem Gerät, kein eigener Server nötig, HTTPS ist automatisch dabei (Pflicht
   für Service Worker).

## Ein weiteres Deck ergänzen

Alle Kartentexte stehen schon in `build_all_cards_<deck>.py` – das Skript `pwa_export_deck.py`
(im Hauptordner) liest sie direkt aus, erzeugt kein neues Textmaterial:

```bash
python3 pwa_export_deck.py build_all_cards_el el "#BF5B3E" "#F5E5DE" "#E0BEA9" \
    "EL-Deck" "Reflexionskarten Eltern" EL
```

Erzeugt `pwa/data/el.json`, komprimierte Bilder in `pwa/images/el/`, trägt das Deck automatisch
in `pwa/data/decks.json` (Deck-Übersicht) ein, und erzeugt gleich noch ein eigenes farbiges
Home-Bildschirm-Icon dafür (`pwa/icons/deck-el.png`, via `pwa_generate_deck_icon.py`). Kein
Server-Neustart nötig, nur die Seite neu laden.

## Struktur

```
pwa/
  index.html         Deck-Übersicht + Karten-Ansicht (eine Seite, kein Reload)
  style.css           Alle Styles, Deckfarbe wird pro Deck per CSS-Variable gesetzt
  app.js              Lade-/Flip-/Navigations-Logik
  manifest.json        PWA-Metadaten (Name, Icons, Startfarbe)
  service-worker.js    Offline-Caching (App-Hülle + einmal geöffnete Decks)
  icons/                App-Icons (192px, 512px)
  data/decks.json       Register aller verfügbaren Decks
  data/<id>.json         Ein JSON pro Deck (Kartentexte + Bildpfade)
  images/<id>/            Komprimierte Kartenbilder (Web-Größe, ~55 KB statt ~500 KB–1 MB im Original)
```
