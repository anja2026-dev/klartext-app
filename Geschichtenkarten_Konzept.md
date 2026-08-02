# Geschichtenkarten-Deck – Konzept (30.07.2026)

## Was es ist

30 Karten aus dem bestehenden App-Feature `M6_Geschichtenkarten_Galerie.html` – Kurzgeschichten mit
Brainy als Identifikationsfigur für Kinder, zum gemeinsamen Anschauen/Besprechen mit INGRA. Vierte
und vermutlich letzte physische Übersetzung eines konkreten App-Elements in dieser Session (nach TK,
Krisendeck, Werkzeugkarten-Deck) – ergänzt die Handlungskarten-Serie um die kindgerichtete Seite.

Inhalt ist bereits kartenreif (1 Satz Situation + 3 Fragen + 1 Impuls-Zitat je Karte) – kaum Kürzung
nötig, nur Layout-Übertragung.

## Struktur: 3 Sets à 10 Karten

- **Set A "Brainy erlebt Mobbing"** (A1–A10) – Opferperspektive
- **Set B "Brainy hilft anderen"** (B1–B10) – Verteidiger-/Helferperspektive
- **Set C "Brainy lernt Strategien"** (C1–C10) – Übungskarten

## Format

A6, Serienlook (Caladea/Lato). Vorderseite: neue gemalte Illustration (Entscheidung 30.07., wie
KD/EL/LK/JD) + Set-Label + ID. Rückseite: Titel, Situation, 3 Fragen zum Gespräch, Impuls-Zitat.

## Farben (angepasst gegenüber App-Original, 30.07.2026)

App nutzt für die 3 Sets Rot #C62828 / Blau #1565C0 / Grün #2E7D47 – Set A ist damit bit-identisch
mit Krisendeck-Rot, Set C liegt mit ~38 Einheiten unter dem üblichen Mindestabstand zu KD-Grün.
Anders als Krisendeck/Werkzeugkarten (direkte 1:1-App-Farbübernahme, dort bewusst so belassen) folgt
dieses Deck der Konvention der reflexiven Decks (KD/EL/LK/JD etc.), die bewusst eigene, kollisions-
freie Farben statt Modulfarben nutzen – Set-Bedeutung (Rot=erlebt/Blau=hilft/Grün=übt) bleibt erhalten,
nur die exakten Töne verschieben sich:

- Set A: Karmesinrot `(150, 30, 35)` statt `(198, 40, 40)` – Abstand zu FK-Rot ~49, zu DaZ-Sek1-Bordeaux ~49.
- Set B: Blau `(21, 101, 192)` unverändert – bereits kollisionsfrei (min. Abstand ~77).
- Set C: Tannengrün `(46, 110, 60)` statt `(46, 125, 71)` – Abstand zu KD-Grün ~57, zu JD ~50.

## Illustration

Brainy-Charakterbogen wird 1:1 vom KD-Deck übernommen (`KD_Brainy_Prompts.md`) – gleiche Figur,
gleicher Aquarell-Kinderbuch-Stil, für Konsistenz über die ganze Serie. 30 neue Szenen-Prompts in
`Geschichtenkarten_Bildprompts.md`, abgeleitet direkt aus den bestehenden App-Situationsbeschreibungen
(Content-Treuepflicht – keine neuen Szenen erfunden).

## Bonuskarte

Stoppschild-Karte (aus AM_DL-Sichtung, s. `Mobbing_Materialien_Konzept.md`) wird als 31. Karte /
Bonuskarte angehängt, an Set A (gleiche Rot-Familie, Thema passt).

## Nächste Schritte

1. Anja generiert die 30 Bilder extern (Prompts liegen bereit).
2. Pipeline (`build_card_geschichtenkarten.py` etc.) wird jetzt schon gebaut und ohne Bilder
   testweise gerendert (Textlayout-Prüfung), analog FS-/DaZ-GS-Deck-Vorgehen.
3. Sobald Bilder da sind: finaler Render + PDF + Merkliste-Update.
