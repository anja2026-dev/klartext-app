# KLARTEXT – Einstieg für neue Chats

Diese Datei IMMER zuerst lesen, bevor an KLARTEXT gearbeitet wird. Danach `KLARTEXT_Merkliste.md`
lesen für den aktuellen Stand (bei Bedarf `KLARTEXT_Merkliste_Archiv.md` für ältere Details vor
dem 02.08.2026).

## Was ist KLARTEXT?
Trainingssystem + Kartendeck-Serie für Schulbegleiter (Anjas eigener Begriff dafür: **INGRA**),
entwickelt von Anja Jolk (Trainerin, Systemische Beraterin/Coach, Lerntherapeutin). Basiert auf
dem **kLAR-Modell** und dem **Barometer** (5-Farben-Emotionsregulations-System). Maskottchen:
**Brainy**.

## Zwei getrennte Repos — nicht verwechseln

**`klartext-app`** — Pfad: `/Users/anjajolk/Documents/GitHub/klartext-app`
Die interne Case-Management- und Trainings-App für Träger/Fachkräfte (aktuell in Pilotphase bei
den Maltesern). Hat Login, Supabase-Backend, M0–M8-Lernmodule, Barometer-Tracking pro Kind. Live
unter `klartext-app-8kl.pages.dev`. Hier liegen auch: alle Karten-PDFs/Booklets, die Build-Skripte
(`build_card_*.py` etc.), die PWA (`pwa/`-Unterordner, siehe unten), und alle `KLARTEXT_*`-
Referenzdokumente (Merkliste, Preisstrategie, Qualifikationsnachweise …).

**`klartext-shop`** — Pfad: `/Users/anjajolk/Documents/GitHub/klartext-shop`
Die öffentliche Marketing-/Verkaufsseite, live unter `klartext-mentoring.de`. Kein Login, kein
Supabase. Enthält die Verkaufsseiten pro Deck (`*_Verkaufsseite.html`), AGB, Widerrufsbelehrung,
`BRAINY_WELT.html`, Social-Media-Material (`social/`). Verkauf läuft aktuell nur über
"Vormerken per E-Mail" (`mailto:info@klartext-mentoring.de`), noch kein echter Checkout.

**Faustregel:** Geht es um Fachkräfte/Träger/Login/Case-Management/Kartenproduktion → `klartext-app`.
Geht es um Kund:innen, die etwas kaufen sollen, Werbetexte, Preise, Social Media → `klartext-shop`.
Bei Unklarheit: nachfragen statt raten.

## PWA / Flip-Cards / "Shop-Lite" — häufigste Verwechslung

- **PWA** (`klartext-app/pwa/`): digitale Flip-Karten-Ansicht für alle 22 Decks, Teil der internen
  App, aktuell nur dort nutzbar (braucht die App drumherum).
- **"Shop-Lite"**: die geplante *abgespeckte* Version davon — ohne Supabase/Login, gedacht für
  Kund:innen, die im Shop ein Deck gekauft haben und die digitale Flip-Card-Version dazu bekommen
  sollen. Bisher **teilweise gebaut, nicht fertig/live**: Login-freie Login-Seite und
  DASHBOARD-Lite existieren, Rest siehe Merkliste (Suche nach "Shop-Lite" oder "Strang 38/39/44").
  Das ist technisch ein dritter Baustein, weder `klartext-app` noch `klartext-shop` im bisherigen
  Sinn — bei Fragen dazu erst in der Merkliste nachlesen, welcher Teil schon existiert.

## Wichtige Referenzdateien (alle in `klartext-app/`)
- `KLARTEXT_Merkliste.md` — aktueller Stand, IMMER zuerst lesen.
- `KLARTEXT_Merkliste_Archiv.md` — abgeschlossene Stränge vor 02.08.2026.
- `KLARTEXT_Plattform_Preisstrategie.md` — Preise, Etsy/Pinterest/eduki-Recherche.
- `pwa/data/decks.json` — vollständige Produktliste (22 Decks/Sets, Kartenzahl, Kategorie).
- `KLARTEXT_Qualifikationsnachweise.md` — Anjas Fortbildungen/Zertifikate (für Marketing/Fachtexte).

## Standing Rules
- Nie selbst `git push` ausführen — immer den Befehl zum Copy-Pasten geben, für beide Repos wenn
  beide Änderungen haben.
- Bei Gender-Sprache: bestätigte Grundsatzentscheidung siehe Merkliste — vor Änderungen nachlesen.
- Inklusions-Kalibrierung ist eine Standing-Regel — vor inhaltlichen Kartentexten relevant, siehe
  Merkliste.
