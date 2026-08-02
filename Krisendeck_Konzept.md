# Krisendeck – Konzept (Feuerwehrkarten FK-01–08 als physisches Deck)

## 1. Zweck & Einordnung

Zweites Deck der Handlungskarten-Serie (nach TK). Anders als TK (Reflexion/Koordination) ist das
Krisendeck ein Sekunden-Schnellgriff-Werkzeug für akute Situationen – Barometer Rot. Es ersetzt nicht
das Feuerwehr-Protokoll in der App, sondern macht die 8 dort bereits vorhandenen, fachlich hinterlegten
Karten physisch griffbereit (Laminat/Ringbuch, kein Bildschirm nötig, wenn's drauf ankommt).

Content-Treuepflicht: die App-Inhalte (FK-01–08) gelten als bereits inhaltlich geprüft. Die physischen
Karten adaptieren/kürzen diesen Text, erfinden aber keine neuen Handlungsanweisungen. Bei Kürzung im
Zweifel eher eine Zeile weglassen als medizinisch/pädagogisch relevante Aussagen umformulieren.

## 2. Bestandsaufnahme der App-Quelle

Die 8 FK-Karten sind NICHT einheitlich strukturiert:

- **FK-01–06** (Akute Eskalation, Shutdown, Panikattacke, Fremdgefährdung, Selbstverletzung,
  Weglaufen/Flucht): einheitliches Format – Lead-Satz, 6 Sofortmaßnahmen (nummeriert), 6
  Erkennungssignale (Grid), Abgrenzungstabelle "Jetzt tun / Jetzt nicht tun" (5–6 Zeilen).
- **FK-07 Dissoziation**: wie oben, aber zusätzlich eine zweite Vergleichstabelle
  ("Dissoziation vs. Shutdown FK-02") plus Abschnitt "Nach der Akutphase" – deutlich umfangreicher.
- **FK-08 Meltdown**: komplett anderes Template (andere CSS-Klassen/Struktur) – Erklärabschnitt
  "Was ist ein Meltdown?", Warn-/Nie-Kästen statt Abgrenzungstabelle, nummerierte Schritte in
  eigenem Format. Vermutlich später gebaut als FK-01–07, nie angeglichen.

Für ein einheitliches Kartendeck müssen alle 8 auf ein gemeinsames Format normalisiert werden.

## 3. Kartenformat (Vorschlag)

Gleiche physische Größe wie TK: A6, 105×148mm, 300dpi. Layout-Engine wird von `build_card_tk.py`
abgeleitet – die TK-Rückseite (Situation/Schritte/Abgrenzung/Quelle) deckt sich fast 1:1 mit
FK-01–06s Struktur.

**Vorderseite – bewusst ohne Foto/Szene, aber mit kleinem Symbol-Icon** (anders als TK/KD/JD, die
Fotos nutzen): Bei Themen wie Selbstverletzung oder Fremdgefährdung wäre eine illustrative Szene
unpassend bis geschmacklos – ein kleines, ruhiges Icon dagegen hilft beim schnellen Wiedererkennen
und passt zur bestehenden Symbolsprache der App. Die App hat pro FK-Karte bereits ein Emoji-Icon
festgelegt (FK-01 ⚡, FK-02 🔇, FK-03 😰, FK-04 ⚠️, FK-05 🩹, FK-06 🏃, FK-07 🌫️, FK-08 🌋) – Vorschlag:
diese Symbolik als Basis für ein sauberes, kleines Linien-Icon im KLARTEXT-Still übernehmen (kein
1:1-Emoji-Rendering, sondern eine ruhige, gezeichnete Version davon, ähnlich wie die kleine
Logo-Marke bei TK), statt neue Symbole zu erfinden. Layout: durchgehendes Rot-Farbband (Barometer
Rot), Icon zentriert, Titel, darunter die Erkennungssignale als kurze Stichpunktliste (3–4 statt 6,
gekürzt) – Vorderseite fungiert als Schnellindex zum Blättern ("welche Karte brauche ich gerade").

**Rückseite**: Situation (1 Satz) → Sofortmaßnahmen (nummeriert, gekürzt auf max. 5–6 kurze Schritte)
→ Abgrenzung "Jetzt tun / Jetzt nicht" (3–4 Zeilen statt 5–6) → Verweis auf App für Details
("Vollständige Fassung inkl. Hintergrund: FK-0X in der App").

**FK-07-Zusatzinhalte** (Vergleichstabelle, Nachsorge) und **FK-08-Erklärabschnitt** ("Was ist ein
Meltdown") wandern NICHT auf die Karte, sondern ins Krisendeck-Handbuch als Hintergrundwissen –
gleiches Prinzip wie bei KD (Karte bleibt schlank, Kontext lebt im Begleitmaterial).

## 4. Farbmarkierung

Alle 8 Karten einheitlich Rot (Barometer Rot / akute Krise) – im Gegensatz zum künftigen
Werkzeugkarten-Deck (Gelb/Orange, situativ unterschiedlich) macht hier eine einzige Farbe Sinn: das
ganze Deck IST die Rot-Antwort. Farbe noch gegen bestehende Decks kollisionsprüfen (FK-Rot #C62828
liegt nah an KD-Rot-Ton aus der Abgrenzungstabelle, aber das ist Interface-intern, keine Deckfarbe –
unkritisch; TK-Lila #4A148C ist ausreichend verschieden).

## 5. Struktur & Nummerierung

8 Karten, FK-01 bis FK-08, gleiche Reihenfolge und Titel wie in der App:
FK-01 Akute Eskalation · FK-02 Shutdown · FK-03 Panikattacke · FK-04 Fremdgefährdung ·
FK-05 Selbstverletzung · FK-06 Weglaufen/Flucht · FK-07 Dissoziation · FK-08 Meltdown.

Kein Bonus-/Zusatzblock geplant – die App-Quelle gibt exakt 8 Karten vor, keine Erweiterung ohne
neue App-Inhalte zuerst.

## 6. Bezug zu TK

TK-09 (Krisenprotokoll) verweist bereits auf "FK-01–08 in der App" (soeben korrigiert, vorher stand
fälschlich FK-01–07). Perspektivisch könnte TK-09s Rückseite auf das physische Krisendeck verweisen,
sobald es existiert – das aber erst nach Fertigstellung anpassen, nicht vorher.

## 7. Sensibilitätshinweis

FK-04 (Fremdgefährdung) und FK-05 (Selbstverletzung) berühren Kinderschutz-relevante Inhalte. Das
Handbuch sollte – wie bei TK bereits Standard – einen Warnhinweis tragen, dass die Karten keine
Rechtsberatung/kein Kinderschutzverfahren ersetzen, plus einen klaren Verweis auf trägerinterne
Meldewege (analog zum bestehenden TK-Warnkasten).

## 8. Offen / nächste Schritte

1. Bestätigung dieses Formats durch Anja, insbesondere: kein Foto auf der Vorderseite, Kürzung der
   Sofortmaßnahmen/Abgrenzung, FK-07/08-Zusatzinhalte ins Handbuch statt auf die Karte.
2. Alle 8 Karten adaptieren (Text kürzen, Rückseite befüllen) – Entwurf zur Gegenprüfung vorlegen,
   bevor gerendert wird.
3. `build_card_krisendeck.py` (abgeleitet von `build_card_tk.py`, Vorderseite neu ohne Foto-Slot).
4. Handbuch mit Sensibilitätshinweis, Vergleichstabelle (FK-07) und Meltdown-Hintergrund (FK-08).
5. Kein Bildprompt-Bedarf, da keine Fotos auf den Karten – reduziert Aufwand gegenüber allen bisherigen Decks.
