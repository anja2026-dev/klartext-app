# KLARTEXT – Merkliste
Stand: 02.08.2026

## Strang 5 · Design-Konsistenz App ↔ Kartendecks (neu, 27.07.2026)

**Befund:** Print-Kartendecks (Caladea/Lato, gemalte „modern children's book"-Brainy-Illustration in
vollen Szenen) und App (Playfair Display/Nunito, 24 Brainy-Bilder in flachem Vektor-/Sticker-Stil mit
dicken Konturen auf Kreis-Hintergrund) sind zwei unterschiedliche visuelle Systeme. Gemeinsam sind nur
die Markenfarben (Navy `#1B3A4B`, Mintgrün `#6EC6A0`) und die „K"-Logomarke – die sind in beiden Welten
identisch. Playfair Display wird in 382 Dateien referenziert (meist kurze Titel/Logos/Kacheln, nicht
lange Fließtexte), Nunito als Body-Font in mehreren Dateien (genaue Zahl noch zu verifizieren). 24
distinkte Brainy-Bilder: 5 Barometer-Farbvarianten, 9 Modul-Varianten (m0–m8), plus rollenspezifische
(ingra/fk/lk/tk/mh) – die meisten Einbindungen sehr klein (42–68px, mehrfach belegt).

**Entscheidung (Anja, 27.07.2026):** Print-Decks bleiben unangetastet (fertig, geprüft, kein Risiko
eingehen). Stattdessen wird die App an den Print-Stil angeglichen – primär Brainy, Schriftarten-Frage
gesondert bewertet (siehe unten). Nächster Schritt: Brainy-Bildsatz (24 Bilder) im neuen, gemalten Stil
neu generieren lassen, dabei zwei Formate pro Motiv einplanen (große „Hero"-Version für Banner/größere
Flächen + vereinfachte/zugeschnittene Version für die vielen 42–68px-Badges, da der gemalte Stil bei so
kleiner Darstellung schlechter lesbar sein kann als der aktuelle Flat-Vektor-Stil – offener Punkt, vor
Serienproduktion an 1–2 Testbildern prüfen). Schriftarten-Umstellung (Playfair Display/Nunito → Caladea/
Lato) versuchsweise **nicht** angegangen: 382 betroffene Dateien wären ein großer, fehleranfälliger
Umstellungsaufwand, und die aktuellen App-Schriften sind für ihren Einsatzzweck (kurze Titel/Kacheln bei
Playfair Display, gut lesbare Body-Schrift bei Nunito) typografisch unproblematisch – reine
Marken-Konsistenzfrage, kein Lesbarkeitsproblem. Wird vorerst nicht verändert.

## Strang 6 · Storybooks-Fundus geprüft, keine neue Linie (neu, 27.07.2026)

**Befund:** Ordner `storybooks/` (von Anja neu befüllt) enthält 44 PDFs, real nur ~19 Kerninhalte – der
Rest sind 1-seitige Download-Reste (Datenmüll). Kein Sammelsurium einzelner Themen, sondern ein
komplettes fremd gebrandetes Programm: **„Stark im Miteinander – Das Anti-Mobbing-Labor"** (eigenes
Logo, Reagenzglas-Icon) mit Trainerhandbuch + ~10 illustrierten Charaktergeschichten (Finn, Yasmin,
Olena, Rayan, Mia, Nabil, Clara, teils in Klassenstufen-Varianten Kl 3b/Kl 8) plus Zusatzmaterial
(Feelgood-Karten-Set, Heldenreise-Tagebuch, Schatztruhe). Separat ein **„DAZ-Kurs"-Tagebuch** mit
wieder eigenem Logo. Keins davon nutzt KLARTEXT-/Brainy-Branding – drei visuelle Welten statt zwei.

**Entscheidung (Anja, 27.07.2026):** Keine neue Storybook-Produktlinie. Begründung: Illustrationsaufwand
pro Buch (11–14 durchillustrierte Erzählseiten) entspricht dem von 10–15 Karten, für ein einziges
Produkt – bei den Decks bekommt man dafür ein ganzes 24–30-Karten-Set. Zudem ist der
Kinderbuch-gegen-Mobbing-Markt voll besetzt (Loewe, Beltz, Carlsen etc.), genau dort, wo KLARTEXTs
Differenzierung (INGRA-Nische, App-Anbindung, Brainy-Kontinuität) am wenigsten zieht. Der eigentliche
Bedarf – Geschichte zum gemeinsamen Anschauen/Besprechen mit dem Kind – ist mit den bestehenden
**Brainy-Geschichtenkarten** (M6, Mobbing, Kartenformat statt Buch) bereits abgedeckt und güns­tiger zu
produzieren. Altes Anti-Mobbing-Labor-Material wird nicht als Buch weiterverfolgt, sondern als
Themenlieferant für zwei laufende Linien genutzt: weitere Geschichtenkarten-Sets zu neuen Themen
(nach M6-Muster) und/oder Rohstoff für die Beteiligungskarten (ebenfalls kindzugewandt).

## Strang 7 · TK-Handlungskarten als physisches Deck (neu, 28.07.2026)

**Korrektur zur Markt-Analyse vom selben Tag:** INGRA *ist* der (umbenannte) Schulbegleiter – kein
externer Marktgap, sondern schon Kernzielgruppe der ganzen Serie. Zusätzlich hat KLARTEXT bereits ein
vollständiges E-Learning+Präsenzkurs-System für INGRA-Onboarding (`EL_M0`–`EL_M8`, Zertifikate,
Modulleitfäden 1-Tag/2-Tage/Kurzeinweisung) – Blended-Learning-Bedarf ist also schon gedeckt, nicht neu
zu bauen.

**Fund:** `TK_Handlungskarten.html` – 19 bereits fertig strukturierte Karten für die Teamkoordination/
Träger-Rolle (TK), in drei Kategorien (Team & Koordination, Kind & Familie, System & Schnittstellen),
Footer-Tag „Neutral · Trägeroffen". Vollständiger Konzeptentwurf fürs physische Handlungskarten-Format
(Situation/4 Schritte/Abgrenzung/Quelle, alle 19 Karten ausformuliert) liegt jetzt in
`Handlungskarten_Grundformat_und_Konzeptentwuerfe.md`, Abschnitt 5. Farbe `#4A148C` (identisch mit der
bestehenden App-TK-Farbe, kollisionsfrei mit allen anderen Deck-Farben) – einziges Deck, das die
App-Farbe direkt übernehmen kann. Kein Barometer-Badge (TK arbeitet am System, nicht am kindlichen
Zustand), stattdessen Kategorie-Badge. Bildkonzept: Erwachsenen-/Systemszenen statt Kind-im-Fokus,
Brainy-Einsatz als Wiedererkennungsmarke noch offen zu klären. **Nächster Schritt:** Bild-/Titelkonzept
final, dann Pipeline (`build_card_tk.py`, Kürzel kollisionsfrei geprüft).

**Status (28.07.2026, Abend): Pipeline fertig, Entwurf geprüft.** `build_card_tk.py` (erstes Deck im
neuen Handlungskarten-Format – Situation/Schritte/Abgrenzung/Quelle statt Frage+Tipp),
`build_all_cards_tk.py` (alle 19 Karten mit Text final), `build_booklet_tk.py` (Anleitung inkl.
Brainy-Erklärung + Tischwerkzeug-Prinzip, Quellen), `build_pdf_tk.py` (Cover + Booklet + 19 Karten,
erkennt automatisch am Quellbild-Ordner `bilder/tk/`, ob Entwurf oder final). Testdruck ohne Bilder
visuell geprüft (Cover-Titel-Überlauf gefixt, Tischwerkzeug-Badge-Rendering gefixt) –
`KLARTEXT_TK-Handlungskarten_komplett_ENTWURF.pdf` (43 Seiten) liegt in klartext-app. **Status (28.07.2026, Nacht): TK-Basis-Deck fertig.** Alle 19 Szenenbilder (Stil auf Anjas Wunsch auf
„modern children's book illustration" umgestellt, einheitlich mit KD/FS/DaZ-GS statt LK-R-Look)
generiert und in `bilder/tk/` abgelegt, Karten neu gerendert, finales PDF gebaut:
`KLARTEXT_TK-Handlungskarten_komplett.pdf` (43 Seiten, kein Entwurfs-Status mehr). Stichproben (Cover,
TK-01, TK-02, TK-19) visuell geprüft – Layout sauber, Tischwerkzeug-Badge korrekt.
**Kleiner offener Punkt:** TK-01-Bild zeigt ein englisches Wort („Roles") auf einer Sticky-Note im
Hintergrund, obwohl der Prompt „no text" verlangte – kosmetischer KI-Generierungsfehler, kein
Layout-Problem. Vor Druck ggf. TK-01 neu generieren oder retuschieren. Brainy-Eckmarke
(`brainy_eckmarke.png`) wurde noch nicht geliefert – die 12 dafür vorgesehenen Karten sind aktuell ohne
Brainy-Marke im Bild; Pipeline fügt sie automatisch hinzu, sobald die Datei in `bilder/tk/` liegt,
einfach `build_all_cards_tk.py` + `build_pdf_tk.py` erneut laufen lassen.

**Bildprompts fertig (28.07.2026):** `TK_Bildkonzept_und_Prompts.md` – 19 Szenen-Prompts („clean
digital illustration", Erwachsenen-/Bürokontext, kein Brainy im Szenenbild selbst) + 1 einmaliger
Brainy-Eckmarken-Prompt. Technische Entscheidung: Brainy wird NICHT 12x einzeln in die KI-Bilder
hineingeneriert (Konsistenzrisiko wie bei den KD-Bildern), sondern als ein einziges Bild erzeugt und
per Code in `build_card_tk.py` automatisch auf die 12 markierten Karten eingefügt (Flag `brainy` pro
Karte in `build_all_cards_tk.py`, Compositing-Logik analog zum Logo). **Nächster Schritt:** Anja lässt
die 19 Szenenbilder + 1 Brainy-Eckmarke extern generieren, in `bilder/tk/` ablegen, dann
`build_all_cards_tk.py` + `build_pdf_tk.py` erneut laufen lassen – PDF wird automatisch final (ohne
„_ENTWURF"-Suffix), sobald alle 19 Quellbilder vorhanden sind.

**Ebenfalls gefunden, noch nicht bearbeitet:** Volle Supabase-Multi-Tenant-Architektur (`traeger`-
Tabelle, `profiles.traeger_id`, Rollen-Enum, 40 RLS-Migrationen) ist fertig entworfen, aber nicht live
(Platzhalter-Zugangsdaten in `supabase.js`). Für scharfschalten fehlt: echtes Supabase-Projekt, Ablösung
des Logins von gemeinsamem Passwort auf Einzelkonten pro Person, ein Träger-Verwaltungs-Werkzeug (nicht
gefunden – nur zwei Verkaufsseiten für Träger, keine Bedienoberfläche), Datenschutzprüfung vor Live-Gang
wegen sensibler Kinderdaten. Priorisierung noch offen, auf Anjas Wunsch erstmal TK-Deck zuerst.

## Strang 1 · Kartendecks-Serie (aktuelle Priorität)

### Content-Achse (direkt fürs Kind/Jugendliche)
- **JD** (Jugendliche/Sek, weiterführend) — **Status (25.07.2026): produktionsfertig.** Alle 40 Karten gebaut (Vorder-/Rückseite, 300dpi/A6), Bildauswahl final (siehe JD_Bildauswahl_final.md), PDF komplett inkl. Titelseite, Anleitung, Glossar, Quellenregister (KLARTEXT_JD-Deck_komplett.pdf, 87 Seiten). NotebookLM-Analyse (Jd-notebook-analyse.docx) ausgewertet: Sprachfixes (JD-04, JD-35) und zwei zu diagnostiknahe Tipp-Texte (JD-31, JD-36) korrigiert; Quellenregister um Dweck (Growth Mindset) und Fröhlich-Gildhoff/Rönnau-Böse (Resilienz) als klar gekennzeichnete Zusatz-Einordnung ergänzt, Salutogenese/7-Säulen-Modell bewusst nicht übernommen (zu konstruiert). **Offener Punkt:** Redundanz-Kritik aus der Analyse — JD-01/JD-02 (sozialer Vergleich), JD-13/JD-15/JD-16 (Abgrenzung) und JD-05/JD-08 (Zukunftsdruck/Entscheidungsdruck) überschneiden sich inhaltlich stark. Für diese Auflage bewusst nicht verändert (Deck ist als "40 Karten" fertig produziert und vermarktet), aber als Prüfpunkt für eine mögliche zweite Auflage vormerken.
- **KD** (Grundschule) — **Status (25.07.2026): in Arbeit, weiter als angenommen.** Vollständiges 30-Karten-Konzept liegt vor (KD_Kartenkonzept_Uebersicht.md), Kartenfarbe `#2E9E5A` (warmes Grün) vorgeschlagen. Bilder für alle 30 Titel bereits extern mit Gemini generiert (31 Dateien, KD-06 mit 2 Varianten), liegen aber noch direkt im Repo-Root statt in `bilder/kd/`. NotebookLM-Bildanalyse ausgewertet und stichprobenartig verifiziert (KD-06, KD-08, KD-09 direkt angesehen): Titel-Bild-Mismatch bei KD-06 ("wütend" wirkt wie traurig/nachdenklich) und KD-08 (Trauer zu subtil) bestätigt sich. Begleitfigur wechselt aktuell durchgehend (Bär, Fuchs, kleine rote Eulenfigur) — Anja hat entschieden: **Brainy wird als durchgängige Coach-Figur zwingend in jedes Bild integriert.** Charakterbogen-Prompt + alle 30 aktualisierten Szenen-Prompts inkl. geschärfter KD-06/KD-08-Prompts liegen vor (KD_Brainy_Prompts.md). Werkzeug-Empfehlung: Gemini weiterverwenden (bereits stilprägend, gut für Charakterkonsistenz über Referenzbild); Claude Design (neues Anthropic-Tool, seit April 2026) geprüft und als ungeeignet eingeschätzt (für UI/Produkt-Mockups gebaut, nicht für Kinderbuch-Illustration). Alte KD-*.html-Appkarten (KD-01 etc.) nutzen App-only Kind-Barometer und können nicht direkt für die physische Karte übernommen werden. **Nächster Schritt:** Anja lässt die 30 Bilder mit Brainy (neu) bzw. korrigiert (KD-06/08) extern generieren, dann Bildauswahl + Kartentext-Feinschliff wie bei JD.

**Barometer/kLAR-Modell im KD-Deck (25.07.2026):** Analog zu JD wird das kLAR-Modell nur INGRA-seitig in der KD-Anleitung erklärt (Brücken-Hinweis bei sichtbar starker Aufregung während einer Karten-Situation), nicht auf den Kind-facing Karten selbst. Das Barometer dagegen ist für KD direkt relevant (KD-01 "Wie geht es mir heute?" baut darauf auf) — geplant als eigene physische Bonus-Karte im Deck ("Wie fühle ich mich?"), auf die Kinder zeigen können, statt nur als Anleitungstext. **Wichtige Korrektur:** Das offizielle, korrekte Barometer hat 5 Zustände — GRÜN, GELB, ORANGE, ROT, GRAU (Quelle: M0-00_Systemelemente.html, auch für die JD-Methodik-Seite verwendet). Die bestehende App-Datei `KD-01.html` nutzt fälschlich eine 4-Farben-Version (GRÜN, GELB, BLAU, ROT) — das ist **nicht korrekt** und muss bei Gelegenheit korrigiert werden (Blau raus, Orange + Grau ergänzen). Bonus-Karte und künftige KD-Texte sollen die korrekte 5-Zustände-Version verwenden.
- **TODO (vorgemerkt):** `KD-01.html` in der App auf das korrekte 5-Zustände-Barometer umstellen.

**Bilder-Update (25.07.2026):** Alle 30 KD-Bilder mit Brainy liegen jetzt unter `bilder/kd/` (ein finales Bild pro Karte, nicht mehr mehrere Varianten). Stichprobe (6 von 30) geprüft: Brainy durchgängig konsistent, gutes Ergebnis. Zwei Korrekturen offen, beide von Anja bestätigt: **KD-01** zeigte von sich aus eine 5-Farbkärtchen-Reihe (schöne Idee), aber mit falschen Farben (Rot/Gelb/Grün/Blau/Lila statt Grün/Gelb/Orange/Rot/Grau) – wird neu generiert (korrigierter Prompt in KD_Brainy_Prompts.md). **KD-06** ("wütend"): Sturmwolke+Blitz überzeugend, Gesichtsausdruck des Kindes aber zu unbestimmt (wirkt eher besorgt) – wird ebenfalls nochmal neu generiert, geschärfter Prompt liegt vor.

**Rückseiten-Struktur bestätigt (25.07.2026):** KD-Kartenrückseiten bekommen den gleichen Aufbau wie JD – Anleitung + 2 Impulsfragen + „Tipp für die INGRA“-Kasten. Konsistenz über die Deck-Serie war Anjas ausdrücklicher Wunsch.

**Status (25.07.2026, Abend): alle 30 Karten produktionsfertig.** KD-01 (korrekte 5 Barometer-Farben Grün/Gelb/Orange/Rot/Grau) und KD-06 (Wut-Ausdruck, von Anja als ausreichend abgenommen) korrigiert und nachgebaut. Vollständiger Kartensatz (Vorder-/Rückseite, 300dpi/A6, Farbe #2E9E5A) liegt in `karten/kd/`. Pipeline: `build_card_kd.py` (Renderer, analog build_card_test.py) + `build_all_cards_kd.py` (Batch mit CARDS-Dict aller 30 Karten). **Nächster Schritt:** Anleitung/Glossar/Methodik(Barometer+kLAR)/Quellen-Seiten fürs KD-Deck bauen (analog build_booklet.py), Bonus-Barometer-Karte, dann Gesamt-PDF wie bei JD.

**Status (25.07.2026, Abend): KD-Deck produktionsfertig.** Anleitung (2 Seiten, kindgerecht angepasst), Methodik-Seite (Barometer 5 Zustände + kLAR-Modell, korrekte Farben), Glossar (6 Begriffe: Brainy, Kind-Barometer, kLAR-Modell, INGRA, Impulsfrage, Systemisches Coaching), Quellen (6 bereits im Register bestätigte Quellen: Oerter & Montada, Bandura, Rosenberg, Olweus, Salmivalli, Porges – keine neuen/unbestätigten Quellen nötig, da direkte Treffer im Register vorhanden) und eine physische Bonus-Barometer-Karte (Zeigekarte mit den 5 Farben fürs Kind) gebaut. Gesamt-PDF `KLARTEXT_KD-Deck_komplett.pdf` (69 Seiten: Cover, Anleitung, Methodik, Glossar, Quellen, Bonus-Karte, 30 Karten) fertig und in klartext-app abgelegt. Pipeline-Dateien: `build_booklet_kd.py`, `build_bonuskarte_kd.py`, `build_pdf_kd.py`. Damit ist KD auf demselben Stand wie JD (produktionsfertig).
- **FS** (Förderschule) — **Status (26.07.2026): Kartenkonzept entworfen (30 Karten, alle KD-Themen sprachlich adaptiert), wartet auf Freigabe.** Wie geplant kein Neuaufbau: alle 30 KD-Karten in einfache Sprache übersetzt (kurze Sätze, aktiv statt passiv, kein Konjunktiv wo vermeidbar, konkrete Beispiele), gegründet auf drei reale, verifizierte Sprachstandards (noch nicht im Quellenregister, "vorgeschlagen"): Netzwerk Leichte Sprache e.V. (2022), Inclusion Europe (2009), DIN SPEC 33429:2025-03. **Symbol-Frage geklärt für den Entwurf:** "symbolgestützt" aus der ursprünglichen Notiz würde lizenzpflichtige Systeme wie Metacom/PCS erfordern — für diesen Entwurf bewusst nur Sprachvereinfachung umgesetzt (Variante A), eigene Icon-Lösung (Variante B) als spätere Option offengehalten. **Farbe vorgeschlagen:** Sonnenblumengelb `#DEB234`, rechnerisch kollisionsgeprüft (größter Abstand aller geprüften Kandidaten). Vollständiger Entwurf mit allen 30 Kartentexten liegt in `FS_Kartenkonzept_Entwurf.md`. **Anja hat entschieden (26.07.2026):** (1) Eigene Praxiserfahrung deckt die Fachprüfungs-Hürde ab, kein externer Review nötig — FS-Deck bekommt daher **keinen** Fachprüfungs-Vorbehalt (anders als AT/ADHS). (2) Variante A (nur Sprache, kein Piktogramm-System) bestätigt. (3) Eigene FS-Bilder statt KD-Wiederverwendung — Brainy bleibt als durchgängige Coach-Figur dabei. (4) Sonnenblumengelb `#DEB234` bestätigt.

**Bildkonzept + Pipeline fertig gebaut:** `FS_Bildprompts.md` (30 copy-ready Prompts mit Dateinamen, Brainy-Kurzbeschreibung + aktueller KD-Stil-Zusatz, alle unter 480 Zeichen, max. 434 — Hinweis im Dokument: Charakterkonsistenz von Brainy ist bei Bing riskanter als bei Gemini, da kein Referenzbild-Mechanismus, ggf. Ausreißer nachkorrigieren), `build_card_fs.py` (Renderer, Sonnenblumengelb mit dunklerer Textvariante für Lesbarkeit, „Tipp für die INGRA", keine Systemfrage, normaler footer_deck ohne „(Entwurf)"), `build_all_cards_fs.py` (30 sprachvereinfachte Kartentexte), `build_booklet_fs.py` (Anleitung 2 Seiten ohne Warnbox, Methodik-Seite erklärt Symbol-Entscheidung + Brainy-Kontinuität, Glossar 2 Seiten, Quellen-Seite mit den 3 Sprachstandards), `build_pdf_fs.py` (normales Cover ohne Entwurfs-Hinweis, bricht kontrolliert ab, solange Bilder fehlen). Alle Booklet-Seiten testweise gerendert und visuell geprüft (Anleitung 1/2, Quellen) – sauber, gute Lesbarkeit auf Gelb. Rückseiten-Layout für alle 30 Karten testweise gerendert (ohne Bilder) – keine Overflow-Warnungen, Stichprobe (FS-13, FS-29) visuell geprüft. Alle Dateien in klartext-app abgelegt, `bilder/fs/`-Ordner angelegt. **Korrektur (26.07.2026):** Erste Bildprompt-Version hatte Brainys charakteristisches rotes Herz beim Kürzen für das 480-Zeichen-Limit versehentlich verloren (Anja hat das an den generierten Bildern bemerkt). Brainy-Kurzbeschreibung in allen 30 Prompts korrigiert (`FS_Bildprompts.md`, `klartext-app`-Kopie), weiterhin alle unter 480 Zeichen (max. 461). **FS-Deck fertig (26.07.2026):** alle 30 Bilder (mit Herz) lagen in `bilder/fs/` vor, Karten gerendert (kein Overflow-Warning), Gesamt-PDF `KLARTEXT_FS-Deck_komplett.pdf` (67 Seiten: Cover, Anleitung 2 Seiten, Methodik, Glossar 2 Seiten, Quellen, 30 Karten) gebaut, visuell stichprobengeprüft (Cover, Karte 01/02, Karte 29/30 — alles sauber, gute Lesbarkeit auf Sonnenblumengelb, Brainy konsistent mit Herz), in klartext-app abgelegt. Damit **achtes vollständig produziertes Kartendeck (279 Karten insgesamt über alle acht Decks: JD 40 + KD 30 + EL 51 + LK 51 + TR 29 + AT 24 + ADHS 24 + FS 30)**. Anders als AT/ADHS: **kein** Fachprüfungs-Vorbehalt, direkt einsatzbereit. **Nächster Schritt:** offen, liegt bei Anja (z. B. Fachprüfung für AT/ADHS organisieren, DaZ GS/DaZ Sek I als letzte offene Decks, oder Bild-Swap für JD/KD/EL/LK nachholen).
- **Kita-Variante von KD (Idee, 25.07.2026)** — Themenblöcke von KD (Gefühle benennen, Streit & Wiedergutmachung, Mut, Freundschaft) passen inhaltlich auch für Kita-Alter (~4–6 Jahre), brauchen aber noch einfachere Sprache, noch stärker geschlossene/konkrete Fragen (ähnlich AT-Prinzip), und 2–3 zu abstrakte Themen (z. B. KD-29, KD-05) eher weglassen. Vorschlag: kein neues Deck, sondern viertes sprachlich vereinfachtes KD-Adaptions-Set neben FS — noch nicht entschieden, ob umgesetzt wird.
- **AT** (Autismus-sensibel) — **Status (26.07.2026): Kartenkonzept entworfen (24 Karten), wartet auf Freigabe UND weiterhin auf fachliche Gegenprüfung.** Grundlage: `KLARTEXT_Kartenserie_Konzeptdoku.md` (Machart-Prinzipien: wörtliche Sprache ohne Metaphern, klare/geschlossene Fragen wo hilfreich, Vorhersehbarkeit durch identische Kartenstruktur, reizarme Bilder, kein Brainy) sowie `M2-09_Autismus.html` als fachlicher Hintergrund. Sechs Blöcke à 4 Karten (Übergänge & Veränderung, Reize & Überforderung, Soziale Regeln verstehen, Meine Interessen, Gefühle konkret, Rückzug & Selbstregulation). Anders als EL/LK/TR ist AT Teil der Content-Achse wie KD/JD: Kind-Barometer direkt eingebunden (AT-20), kLAR-Modell nur INGRA-seitig. Rückseiten-Struktur bewusst ohne Variation (Anleitung + 2 konkrete/skalierte Fragen + „Tipp für die INGRA", kein dritter Fragetyp wie bei den Erwachsenen-Decks). **Farbe vorgeschlagen:** Salbeigrau `#7C8C7E`, kollisionsgeprüft gegen alle bestehenden Farben. **Quellen (3, alle bereits im Quellenregister bestätigt, einzeln nachgeprüft):** DSM-5 (APA 2013), Milton 2012 (Doppel-Empathie-Problem), Hejlskov Elvén 2022 (gegen Zwang/Druck, für Vorhersehbarkeit) – keine unbestätigten Quellen nötig, bessere Ausgangslage als bei TR. Vollständiger Entwurf mit allen 24 Kartentexten liegt in `AT_Kartenkonzept_Entwurf.md`. **Wichtig, unverändert:** Der Fachprüfungs-Vorbehalt gilt weiterhin für den produktiven Einsatz – das Konzept ist ein Entwurf für die Gegenprüfung durch eine Autismus-Fachperson, direktes Kind-Material macht das Risiko hier am größten in der ganzen Serie. **Konzept von Anja freigegeben (26.07.2026).** Bildkonzept + Pipeline fertig gebaut: `AT_Bildprompts.md`
(24 Prompts, eigener ruhigerer Stil-Zusatz mit gedämpfteren Farben statt "vibrant" – passend zum
Prinzip "reizarme Bildgestaltung" –, ausschließlich wörtliche/konkrete Szenen ohne Symbolik, kein
Brainy), `build_card_at.py` (Renderer, Salbeigrau, „Tipp für die INGRA" statt „Tipp für dich", keine
dritte Frage), `build_all_cards_at.py` (24 Kartentexte), `build_booklet_at.py` (Anleitung 2 Seiten
inkl. rot umrandeter Entwurfs-/Fachprüfungs-Warnbox, Methodik-Seite, Glossar 2 Seiten, Quellen-Seite
– nur 1 Seite nötig, da alle 3 Quellen bereits bestätigt sind, kein „vorgeschlagen"-Anteil wie bei
TR), `build_pdf_at.py` (Cover trägt den Fachprüfungs-Hinweis in Rot direkt sichtbar, Dateiname
bewusst `KLARTEXT_AT-Deck_ENTWURF.pdf` statt „komplett", bricht kontrolliert ab, solange Bilder
fehlen). Jede einzelne Karte trägt zusätzlich „AT-Deck (Entwurf)" statt nur „AT-Deck" im Footer –
der Entwurfsstatus ist damit auf jeder Seite sichtbar, nicht nur auf dem Cover. Alle Booklet-Seiten
und alle 24 Kartenrückseiten testweise ohne Bilder gerendert – keine Overflow-Warnungen, visuell
geprüft (Warnbox, Beispielkarte AT-05) – sauber. Alle Dateien in klartext-app abgelegt, `bilder/at/`
angelegt. **AT-Deck technisch fertig (26.07.2026).** Alle 24 Bilder von Anja mit Bing generiert (direkt im
neuen Stil, ruhig/reizarm, korrekte Barometer-Farben bei AT-20 auf Anhieb), lagen direkt in
`bilder/at/`. Stichprobe (AT-05, AT-20) geprüft: klar, ausdrucksstark, literal – kein Symbolik-Bruch.
`build_all_cards_at.py` + `build_pdf_at.py` ausgeführt: 24 Karten, kein Overflow-Warning, PDF
`KLARTEXT_AT-Deck_ENTWURF.pdf` (55 Seiten) fertig, visuell geprüft (Cover mit Fachprüfungs-Hinweis,
Karte AT-01, Karte AT-24 – sauber), in klartext-app abgelegt. **Damit ist AT technisch auf demselben
Stand wie JD/KD/EL/LK/TR – sechstes vollständig produziertes Kartendeck (225 Karten insgesamt über
alle sechs Decks).**

**Fachprüfung abgeschlossen, Entwurfs-Status entfernt (27.07.2026).** Anja hat bestätigt, dass die
externe Fachprüfung durch eine Autismus-Fachperson abgeschlossen ist. Alle Entwurfs-/Fachprüfungs-
Kennzeichnungen entfernt: `build_card_at.py` (Footer ohne „(Entwurf)"), `build_booklet_at.py` (rote
Warnbox auf Anleitung-Seite 2 ersetzt durch neutralen „Fachlich geprüft"-Hinweis, Glossar-Eintrag
aktualisiert), `build_pdf_at.py` (roter Cover-Warnhinweis entfernt, Cover-Layout neu aufgebaut mit
Intro-Absatz statt Warnbox – dabei einen Layout-Bug beim ersten Rebuild gefunden und korrigiert: die
Unterzeile saß zu nah an der großen Titelzeile und überlappte sichtbar, Zeilenabstand korrigiert).
Neue Datei `KLARTEXT_AT-Deck_komplett.pdf` (55 Seiten) gebaut und visuell geprüft (Cover, Anleitung
2/2, Kartenfooter AT-01 – sauber, kein Entwurfs-Hinweis mehr sichtbar), alte
`KLARTEXT_AT-Deck_ENTWURF.pdf` bleibt aus Datei-Sicherheits-Policy unangetastet zusätzlich liegen.
**AT-Deck ist damit vollständig einsatzbereit, kein Vorbehalt mehr.**

### Rollen-Achse (für Begleitpersonen)
- **EL** (Eltern) — **Status (25.07.2026): Konzeptentwurf steht.** Als nächstes Deck priorisiert (Verkaufs-Logik: größter Markt, alle Eltern statt nur INGRA-Nische, siehe Gesamtüberblick-Auswertung). Erster Entwurf mit 30 Karten in 6 Blöcken (EL_Kartenkonzept_Entwurf.md) — lose an die Themen des bestehenden EL-Kurses (M1–M8) angelehnt, aber als reflektierende Coaching-Impulse statt Lerninhalte umformuliert. Rückseiten-Hinweisbox heißt „Tipp für dich" (statt „Tipp für die INGRA", da Zielgruppe direkt die Eltern sind). **Namensklärung:** EL-Kürzel wird für Kurs UND Deck verwendet — bewusst beibehalten, aber klar als „EL-Kurs" vs. „EL-Deck" unterschieden (keine Datei-Kollision, da Kurs `EL_M1_...`, Deck `EL-01` heißt). Kartenkonzept von Anja freigegeben (25.07.2026). **Tipp-für-dich-Texte** (EL_Tipps_fuer_dich_Entwurf.md, alle 30, persönlicher/validierender Ton statt Facheinweisung) und **Bildkonzept** (EL_Bildkonzept.md, 30 Szenen-Vorschläge) liegen vor. **Stilentscheidung vorgeschlagen, noch zu bestätigen:** EL folgt JD-Bildsprache (realistisch/fotografisch, kein Brainy im Bild, nur Logo im Kopf) statt KD-Bildsprache (Aquarell + Brainy in der Szene) — Begründung: erwachsene Zielgruppe, näher an JD als an KD. Ziel ~30 Karten, Coaching-Impulse aus der Familien-/Zuhause-Perspektive (Eltern reflektieren die eigene Rolle).

**Strukturentscheidung (25.07.2026): EL-Basis + Zusatzblöcke statt einem generischen 30-Karten-Deck.** Anja hat zurecht infrage gestellt, ob ein rein allgemeines Elterncoaching-Deck überhaupt eine Marktlücke ist (Markt für generische Elternratgeber ist voll, siehe Don-Bosco-Vergleich). Lösung, konsistent mit dem Muster aus Strang 1c (echte Lücken liegen in Spezialsituationen, nicht im Allgemeinen): Die bereits entworfenen 30 Karten (EL_Kartenkonzept_Entwurf.md) bleiben als **EL-Basis** bestehen (bei Durchsicht überwiegend tatsächlich universell einsetzbar, kein großer Kürzungsbedarf). Zusätzlich **Zusatzblöcke pro Zielgruppe** (je ~7 Karten, gleiches Kartenformat), die an die jeweiligen Kind-Decks andocken — schafft Differenzierung UND natürlichen Cross-Sell (Käufer:in des AT-Kind-Decks bekommt den passenden EL-Zusatzblock angeboten). Erster Zusatzblock als Vorlage gebaut: **EL-Zusatzblock Autismus** (EL_Zusatzblock_Autismus.md, 7 Karten, andockt an AT-Deck) — bewusst auf die emotionale Erfahrung der Eltern fokussiert, nicht auf Diagnostik/Interventionsempfehlungen; trotzdem vor Veröffentlichung fachlich gegenlesen lassen (kleineres Risiko als beim AT-Kind-Deck selbst, da keine direkten Handlungsanweisungen fürs Kind). **Format bestätigt (25.07.2026).** Zwei weitere Zusatzblöcke im selben Muster gebaut: **EL-Zusatzblock ADHS** (EL_Zusatzblock_ADHS.md, 7 Karten, andockt an geplantes ADHS-Deck, Medikations-/Behandlungsfrage bewusst wertungsfrei gehalten) und **EL-Zusatzblock Pflegekinder** (EL_Zusatzblock_Pflegekinder.md, 7 Karten, andockt an Pflegekinder-Ergänzungsset, **ohne** Fachprüfungs-Vorbehalt dank Anjas eigener Praxiserfahrung). Damit jetzt drei Zusatzblöcke vorhanden (Autismus, ADHS, Pflegekinder) plus die EL-Basis. **Nächster Schritt:** Anja liest gegen; danach Bildkonzept/Bildgenerierung für die EL-Basis, ggf. weitere Zusatzblöcke (DaZ?) nach Bedarf.

**Tipp-für-dich-Texte für alle drei Zusatzblöcke ergänzt** (EL_Zusatzbloecke_Tipps_fuer_dich.md, 21 Texte). Damit textlich vollständig: EL-Basis (30 Karten + Tipps) + 3 Zusatzblöcke (je 7 Karten + Tipps) = 51 Karten Textentwurf insgesamt. **Bildkonzept auch für die Zusatzblöcke fertig** (EL_Zusatzbloecke_Bildkonzept.md, 21 Szenen, gleicher Stil-Zusatz wie EL-Basis, JD-Stilfrage bestätigt). Damit ist EL komplett textlich und bildkonzeptionell entworfen (51 Karten). **Nächster Schritt:** Anja lässt alle Bilder extern generieren (Gemini), dann Bildauswahl + Kartenbau wie bei JD/KD. **Namenskollision:** bestehender EL_M0–M8-Elternkurs im Repo nutzt dasselbe Kürzel für anderen Inhalt. Klärung nötig (umbenennen / bewusst doppelt belegen).
**Dual-Use-Frage geklärt (25.07.2026):** Anja hat zurecht angemerkt, dass ungeklärt war, wer die EL-Karte mit wem nutzt (anders als bei JD/KD keine Eltern-Kind-Karten, sondern direkt Eltern-facing). Entscheidung: **Beides möglich** — die Karten funktionieren sowohl zur alleinigen Selbstreflexion als auch mit Begleitung (INGRA, Berater:in, Partner:in liest vor). „Tipp für dich" funktioniert in beiden Modi, da direkt an die lesende Person gerichtet. In der Anleitung als eigene Seite „Zwei Nutzungsarten" dokumentiert. Explizit **kein** Barometer/kLAR-Modell im EL-Deck — das ist ein INGRA-Werkzeug zur Ko-Regulation eines akut angespannten Kindes, nicht für elterliche Selbstreflexion gedacht.

**EL-Basis produktionsfertig (25.07.2026).** Alle 30 EL-Basis-Bilder (EL-01–30.jpg) extern generiert, liegen in `bilder/el/`, Stichprobe (EL-01, EL-16, EL-26) geprüft: konsistenter, warmer Aquarell-Look, kein Brainy im Bild, Stimmung passend zu Kartentiteln. **Farbentscheidung: Terracotta `#BF5B3E`**, kollisionsgeprüft gegen bestehende App-Modulfarben (App-KD-Modul=Teal #00838F/#4FC3C7, Elternkurs/EL-App-Modul=Magenta #AD1457, LK-App-Modul=Blau #1565C0, TR-App-Modul=Braun/Gold #7A4C00) — Terracotta ist frei und passt zur warmen Bildstimmung. Pipeline gebaut: `build_card_el.py` (Renderer, „Tipp für dich" statt „Tipp für die INGRA"), `build_all_cards_el.py` (Batch, alle 30 Karten gerendert), `build_booklet_el.py` (Anleitung 2 Seiten inkl. Dual-Use-Seite, Methodik-Seite zur Abgrenzung von Barometer/kLAR, Glossar 6 Begriffe, Quellen), `build_pdf_el.py`. **Quellen (6, bereits im Quellenregister bestätigt):** Bowlby 1969, Ainsworth et al. 1978, Siegel 1999, Gottman 1994, Rosenberg 2003, Bandura 1977 — mit „Beispielhafte Passung" zu konkreten EL-Karten. Gesamt-PDF `KLARTEXT_EL-Deck_Basis_komplett.pdf` (67 Seiten: Cover, Anleitung, Methodik, Glossar, Quellen, 30 Karten) fertig, in klartext-app abgelegt. **Stil-Korrektur, zweifach (25.07.2026):** Die ursprünglich dokumentierte Stilvorgabe für EL ("realistisch/fotografisch wie JD") war falsch — die tatsächlich generierten und freigegebenen EL-Basis-Bilder (EL-01/16/26 geprüft) sind warme Illustrationen. Erster Korrekturversuch nutzte fälschlich „watercolor" + „soft painterly brushstrokes" im Stil-Zusatz — diese Kombination erzeugt eine körnige, fleckige Textur bei der Bildgenerierung und war nie Teil des bisher gut funktionierenden Stils bei JD/KD/AT/EL-Hauptset. **Korrekter Stil-Zusatz (final):** `soft warm illustration style, muted warm color palette, gentle natural lighting, paper texture background, no text, no letters, no watermark` — ohne „watercolor"/„brushstrokes". EL_Bildkonzept.md, EL_Zusatzbloecke_Bildkonzept.md und EL_Zusatzbloecke_Bildprompts.md (21 fertige Copy-Prompts mit Dateinamen) entsprechend korrigiert. **EL-Zusatzblöcke produktionsfertig (25.07.2026).** Alle 21 Bilder generiert und in `bilder/el/` abgelegt (ein Dateiname mit Tippfehler, `EL-AT-05..jpg` (doppelter Punkt) — bewusst nicht umbenannt, Pipeline glob-robust dagegen gemacht). Stichprobe geprüft: überwiegend stilkonsistent mit EL-Basis, zwei Bilder (EL-ADHS-01, EL-PF-04) wirken etwas flacher/"cartoonhafter" als der Rest — kein Ausschlusskriterium, ggf. bei Gelegenheit neu generieren. **Bug gefunden und gefixt:** `build_card_el.py` hat lange Kartentitel auf der Rückseite nicht umgebrochen, dadurch Überlappung mit der Karten-ID (z. B. EL-AT-01 "Das Bild vom 'normalen' Familienalltag loslassen") — Titel-Wrapping ergänzt (max. 2 Zeilen, bei sehr langen Titeln rutscht die ID in eine eigene Zeile), betrifft rückwirkend auch EL-Basis (dort keine sichtbaren Überläufe, da Titel dort kürzer waren, aber Fix ist defensiv für beide gültig). Neuer Batch-Builder `build_all_cards_el_zusatz.py` (21 Karten, badge/id/footer parametrisiert je Block), `build_pdf_el_zusatz.py` baut drei eigenständige kompakte PDFs (Deckblatt mit Andockt-an-Hinweis + Fachprüfungs-Status + 7 Karten, keine Duplikation von Anleitung/Methodik/Glossar/Quellen — verweist auf EL-Basis-PDF): `KLARTEXT_EL-Zusatzblock_Autismus.pdf`, `KLARTEXT_EL-Zusatzblock_ADHS.pdf` (beide je 15 Seiten, Fachprüfungs-Vorbehalt vermerkt), `KLARTEXT_EL-Zusatzblock_Pflegekinder.pdf` (15 Seiten, kein Vorbehalt). Alle drei in klartext-app abgelegt.

**Bild-Prompts-Format (25.07.2026):** Auf Anjas Wunsch werden Bild-Prompts künftig direkt mit Ziel-Dateiname und vollständig zusammengesetztem Copy-Block pro Bild geliefert (siehe EL_Zusatzbloecke_Bildprompts.md als Vorlage), statt Stil-Zusatz separat zu halten — deutlich weniger manuelles Copy-Paste für Anja.

**Strukturentscheidung: dritte Frage für alle Erwachsenen-Decks (25.07.2026).** Anja hat zurecht angemerkt, dass Karten für Erwachsene (EL, künftig LK) mehr Tragfähigkeit haben als Kind-Decks (JD/KD) und die bisherige 2-Fragen-Struktur bei reiner Bewusstwerdung stehen bleibt, ohne den Schritt zur Handlung zu machen. Entscheidung: **3. Frage statt 4** (bewusst nicht mehr, sonst kippt die Karte vom Impuls zum Arbeitsblatt — passend zur "auch 5 Minuten reichen"-Philosophie der Tipp-Texte), gezielt aus der systemischen Beratung: Skalierungsfrage (lösungsorientiert, de Shazer 1988), zirkuläre Frage (Mailänder Modell, Selvini Palazzoli et al. 1980) oder Handlungsfrage (kleiner nächster Schritt) — je Karte passend gewählt. Beide Quellen noch **nicht** im Quellenregister bestätigt, auf der EL-Quellen-Seite entsprechend als "vorgeschlagen, bitte gegenprüfen" markiert (nicht mit den 6 bestätigten JD/KD/EL-Quellen vermischt). **Umsetzung:** `build_card_el.py` um dritte, visuell abgesetzte Frage-Box erweitert (Navy-Akzent statt Terracotta, klar unterscheidbar von den zwei regulären Impulsfragen und der Tipp-Box); dabei einen Bug gefunden und gefixt (lange Kartentitel liefen auf der Rückseite in die ID-Kennung, jetzt mit Zeilenumbruch). Alle 51 EL-Karten (Basis + 3 Zusatzblöcke) neu gerendert, alle 4 PDFs neu gebaut. Quellen-Seite dabei von 1 auf 2 Seiten gesplittet (Überlauf durch die neue Quellen-Sektion), Glossar um Begriff "Dritte Frage" ergänzt. `LK_Kartenkonzept_Entwurf.md` (noch unbestätigt) für die dritte Frage vorgemerkt, Ausformulierung folgt nach Freigabe des Grundkonzepts durch Anja. Alle Konzeptdateien (EL_Kartenkonzept_Entwurf.md, drei EL_Zusatzblock_*.md) referenzieren jetzt die SYSTEMFRAGEN-Dicts in den Build-Skripten als kanonische Quelle statt Dopplung.

**LK-Ausbau beschlossen (25.07.2026):** Analog zu EL wird auch LK (Lehrkräfte) auf "LK-Basis + Zusatzblöcke pro Zielgruppe" aufgebaut. **Namenskollision gelöst:** bestehende `LK-01–17` (INGRA-Lehrkraft-Zusammenarbeit) bleiben unverändert; neue Reflexionskarten für Lehrkräfte selbst heißen `LK-R-01` bis `LK-R-30` (R = Reflexion), Deck-Marke bleibt „LK-Deck". LK-Basis-Kartenkonzept (30 Karten, 6 Blöcke, Schul-/Klassenraum-Perspektive, „Tipp für dich"-Box wie EL) entworfen: `LK_Kartenkonzept_Entwurf.md`. **Nächster Schritt:** Anja bestätigt/korrigiert Konzept + Namensvorschlag, danach Tipp-Texte, Bildkonzept (Aquarell-Stil wie EL) und LK-Zusatzblöcke Autismus/ADHS/Pflegekinder. **Namenskollision EL-Kurs/EL-Deck** weiterhin ungeklärt (siehe unten).
- **LK** (Lehrkräfte) — **Status (26.07.2026): komplett produktionsfertig (Basis + alle 3 Zusatzblöcke).** Namenskollision gelöst: neue Reflexionskarten heißen `LK-R-01`–`LK-R-30` (R = Reflexion), Deck-Marke „LK-Deck", bestehende `LK-01–17` (INGRA-Lehrkraft-Zusammenarbeit) bleiben unverändert. Farbe: Pflaume `#6B4E71` (kollisionsgeprüft gegen App-LK-Blau #1565C0, KD-Teal, EL-App-Magenta, TR-Gold, EL-Deck-Terracotta). Pipeline vollständig gebaut: `build_card_lk.py` (Renderer, „Tipp für dich" + dritte systemische Frage wie EL), `build_all_cards_lk.py` (Basis, 30 Karten), `build_all_cards_lk_zusatz.py` (Zusatzblöcke, 21 Karten), `build_booklet_lk.py`, `build_pdf_lk.py`, `build_pdf_lk_zusatz.py`. **Zusatzblöcke (Autismus/ADHS/Pflegekinder, `LK_Zusatzbloecke_Entwurf.md`) fertig:** alle 21 Bilder lagen vor, Karten gerendert, drei PDFs gebaut (`KLARTEXT_LK-Zusatzblock_Autismus.pdf`, `_ADHS.pdf`, `_Pflegekinder.pdf`, je 15 Seiten) — kein Fachprüfungs-Vorbehalt bei Pflegekinder (Anjas Praxiserfahrung), Vorbehalt bei Autismus/ADHS wie beim EL-Pendant. **LK-Basis fertig (26.07.2026):** alle 30 Bilder (LK-R-01–30.jpg) lagen vor, Karten gerendert (kein Overflow-Warning), Gesamt-PDF `KLARTEXT_LK-Deck_Basis_komplett.pdf` (68 Seiten: Cover, Anleitung 2 Seiten, Methodik, Glossar 2 Seiten, Quellen 2 Seiten, 30 Karten) gebaut, visuell stichprobengeprüft (Cover, Karte 01, Quellen 2/2, Karte 30 Vorder-/Rückseite — alles sauber), in klartext-app abgelegt. Damit ist LK komplett auf demselben Stand wie EL (Basis + 3 Zusatzblöcke, alle produktionsfertig). **Nächster Schritt:** offen, liegt bei Anja (z. B. TR-Deck, weitere Zusatzblöcke, oder Vermarktung).
- **EL/LK-Abgrenzung geklärt (25.07.2026):** Größtes Überschneidungsrisiko war, dass beide dieselben Kind-Themen von außen betrachten (z. B. Mobbing aus Eltern- UND Lehrkraft-Sicht). Lösung: EL immer Familien-/Zuhause-Perspektive, LK immer Schul-/Klassenraum-Perspektive — gleiche Grundthemen, unterschiedlicher Handlungsraum.
- **TR** (Trainer/INGRA-Schulung) — **Status (26.07.2026): Kartenkonzept entworfen, wartet auf Freigabe.** Vorarbeit gesichtet: `KLARTEXT_Trainerhandbuch.html` (8 Kapitel, bereits fachlich sauber mit Quellen: Knowles 1980, Kolb 1984, Tuckman 1965, Hattie 2009 — Hattie ist bereits im Quellenregister bestätigt, die drei anderen noch nicht) ist die inhaltliche Grundlage, nicht neu erfunden. **Ehrlicher Realitätscheck zur Kartenzahl:** Das ursprüngliche Ziel von ~40–50 Karten ist mit echtem, nicht künstlich gestrecktem Inhalt aus dem Trainerhandbuch nicht erreichbar — tatsächlich tragfähig sind **29 Karten** in 8 Blöcken (analog zu den 8 Handbuch-Kapiteln: Rolle & Haltung, Wie Erwachsene lernen, Gruppendynamik, Vorbereitung & Logistik, Methodenkoffer, Schwierige Situationen, Feedback, Nachbereitung & Qualität). Vorschlag: mit 29 starten, bei Bedarf später aus den Moderationsleitfäden (1-Tag/2-Tage/Kurzeinweisung) erweitern. **TR-spezifische Dual-Use-Variante:** stärker als bei EL/LK zwischen „eigene Vorbereitung/Reflexion" und „Live-Griffkarte im Training" unterschieden (v. a. Block Methodenkoffer/Schwierige Situationen sind als direkte Spickzettel während einer laufenden Schulung nutzbar). Gleiche Rückseiten-Struktur wie EL/LK (Anleitung + 2 Impulsfragen + 3. systemische Frage + „Tipp für dich"). **Farbe vorgeschlagen:** Slate-Blau `#3E5C76` — bewusst nicht die bestehende App-TR-Modulfarbe (Braun/Gold `#7A4C00`) wiederverwendet, gleiches Muster wie bei EL/LK (Deck-Farbe ≠ App-Modul-Farbe desselben Kürzels), kollisionsgeprüft gegen alle bestehenden App- und Deck-Farben. Vollständiger Entwurf mit allen 29 Kartentexten (Anleitung, Impulsfragen, teils Systemfrage, Tipp für dich) liegt in `TR_Kartenkonzept_Entwurf.md`. **Konzept von Anja freigegeben (26.07.2026).** Bildkonzept + Pipeline fertig gebaut: `TR_Bildprompts.md` (29 copy-ready Prompts mit Dateinamen, Trainer:in in Seminarsituation, kein Brainy, korrekter Stil-Zusatz von Anfang an), `build_card_tr.py` (Renderer, Slate-Blau), `build_all_cards_tr.py` (Batch mit allen 29 Kartentexten inkl. Systemfragen), `build_booklet_tr.py` (Anleitung 2 Seiten mit TR-spezifischer Dual-Use-Variante „Eigene Vorbereitung“ vs. „Live-Griffkarte im Training“, Methodik-Seite inkl. ehrlichem Hinweis zur Kartenzahl, Glossar 2 Seiten, Quellen 2 Seiten von Anfang an gesplittet), `build_pdf_tr.py` (bricht kontrolliert ab, solange Bilder fehlen, wie bei LK-Basis). Alle Booklet-Seiten visuell geprüft (Anleitung, Methodik, Quellen) – sauber, kein Überlauf. Rückseiten-Layout für alle 29 Karten testweise gerendert (ohne Bilder) – keine Overflow-Warnungen, Stichprobe (TR-16, TR-22) visuell geprüft. Alle Dateien in klartext-app abgelegt, `bilder/tr/`-Ordner angelegt. **Nächster Schritt:** Anja lässt die 29 Bilder aus `TR_Bildprompts.md` generieren und in `bilder/tr/` ablegen, dann `build_all_cards_tr.py` + `build_pdf_tr.py` ausführen (läuft automatisch durch, sobald alle Bilder da sind).

- **ADHS** — **Status (26.07.2026): Kartenkonzept entworfen (24 Karten), wartet auf Freigabe UND auf fachliche Gegenprüfung.** Grundlage: `M2-08_ADHS.html` (bereits mit Barkley 2012, Shaw et al. 2007 zitiert – beide noch nicht im Quellenregister bestätigt) sowie mehrere von Anja bereitgestellte, unsourced Rechercheblöcke (Lehrkraft-/Elternsicht, Masking bei Mädchen, Diagnostik, multimodale Behandlung) — **wichtig:** diese Zusammenfassungen wurden nur als Themenlieferant genutzt, nicht als Zitatquelle, da sie selbst keine durchgängigen Belege enthielten und einzelne Zahlen (z. B. "über 90 %", "bis zu 27 %") sich nicht verifizieren ließen. Stattdessen vier echte, aktuelle Quellen recherchiert und einzeln geprüft (alle "vorgeschlagen, bitte gegenprüfen", noch nicht im Quellenregister): McKinney et al. 2024 (*JCPP Advances*, Camouflaging/Masking bei Mädchen), interdisziplinäre S3-Leitlinie ADHS (AWMF 028-045, Version 2.0, 2026), Faraone et al. 2021 (*Neuroscience & Biobehavioral Reviews*, World Federation of ADHD International Consensus Statement, 208 Konsens-Aussagen, 79 Autor:innen/27 Länder), Heine & Exner 2021 (*Zeitschrift für Neuropsychologie*, Diagnostik/exekutive Funktionen). **Zwei weitere von Anja genannte Angaben geprüft und bewusst nicht übernommen**, da nicht als reguläre Publikation zitierfähig: "Wissenschaftlicher Konsensusbericht (2026)" zur Scaffolding-/Kompensationshypothese (kein Autor/Titel/Journal auffindbar) und "ADHS Spezialambulanz / Golsari, A. (2026)" (Dr. Golsari ist real, aber die Angabe ist keine Publikation — inhaltlicher Punkt zur Fremdanamnese wird stattdessen über die AWMF-Leitlinie abgedeckt). **Medikamentennamen, digitale Therapeutika (z. B. EndeavorRx) und Neurofeedback-Protokolle aus Anjas Recherche bewusst nicht in die Kartentexte übernommen** — analog zur bestehenden wertungsfreien Haltung bei den EL-Zusatzblöcken, das sind fachliche Behandlungsentscheidungen, keine Kartenimpulse. Sechs Blöcke à 4 Karten (Aufmerksamkeit & Konzentration, Impulsivität & Handeln, Bewegungsdrang & innere Unruhe, Maskieren & Erschöpfung, Schule & Leistung, Ich über mich). Struktur wie JD/KD (Content-Achse, kind-facing, „Tipp für die INGRA", keine dritte Frage) — anders als AT **keine** erzwungene wörtliche Sprache nötig, da ADHS primär Aufmerksamkeit/Impulskontrolle betrifft, nicht sprachliche Verarbeitung. **Farbe vorgeschlagen:** Periwinkle `#6B7FD7`, rechnerisch kollisionsgeprüft (größter Abstand aller geprüften Kandidaten zu allen 21 bestehenden Farben). **Fachprüfungs-Vorbehalt wie bei AT** (analog zum bereits bestehenden Vorbehalt bei EL-/LK-Zusatzblock ADHS). Vollständiger Entwurf mit allen 24 Kartentexten und der vollständigen Quellen-/Ablehnungs-Dokumentation liegt in `ADHS_Kartenkonzept_Entwurf.md`. **Konzept von Anja freigegeben (26.07.2026).** Bildkonzept + Pipeline fertig gebaut: `ADHS_Bildprompts.md` (24 copy-ready Prompts mit Dateinamen, normaler vibrant Stil-Zusatz wie JD/KD/EL/LK/TR, nicht die gedämpfte AT-Variante, kein Brainy, alle unter 480 Zeichen, max. 305), `build_card_adhs.py` (Renderer, Periwinkle, „Tipp für die INGRA", keine Systemfrage), `build_all_cards_adhs.py` (Batch mit allen 24 Kartentexten), `build_booklet_adhs.py` (Anleitung 2 Seiten inkl. Warnbox „ENTWURF – FACHPRÜFUNG AUSSTEHEND", Methodik-Seite, Glossar 2 Seiten, Quellen auf 2 Seiten gesplittet – alle 6 Quellen „vorgeschlagen", plus explizite Seite zu den zwei geprüft-abgelehnten Angaben und zur bewussten Nicht-Übernahme von Medikamenten-/Behandlungsdetails), `build_pdf_adhs.py` (Cover mit rotem Entwurfs-Hinweis wie bei AT, bricht kontrolliert ab, solange Bilder fehlen). Alle Booklet-Seiten testweise gerendert und visuell geprüft (Anleitung 2/2, Quellen 2/2) – sauber, kein Überlauf. Rückseiten-Layout für alle 24 Karten testweise gerendert (ohne Bilder) – keine Overflow-Warnungen, Stichprobe (ADHS-13, ADHS-20) visuell geprüft. Alle Dateien in klartext-app abgelegt, `bilder/adhs/`-Ordner angelegt. **ADHS-Deck fertig (26.07.2026):** alle 24 Bilder lagen in `bilder/adhs/` vor, Karten gerendert (kein Overflow-Warning), Gesamt-PDF `KLARTEXT_ADHS-Deck_ENTWURF.pdf` (56 Seiten: Cover, Anleitung 2 Seiten, Methodik, Glossar 2 Seiten, Quellen 2 Seiten, 24 Karten) gebaut, visuell stichprobengeprüft (Cover, Karte 01 Vorder-/Rückseite, Karte 24 Vorder-/Rückseite — alles sauber, moderner Bildstil, kein Überlauf), in klartext-app abgelegt. Damit **siebtes vollständig produziertes Kartendeck (249 Karten insgesamt über alle sieben Decks: JD 40 + KD 30 + EL 51 + LK 51 + TR 29 + AT 24 + ADHS 24)**.

**Fachprüfung abgeschlossen, Entwurfs-Status entfernt (27.07.2026).** Anja hat bestätigt, dass die externe Fachprüfung durch eine ADHS-Fachperson abgeschlossen ist. Gleiche Bereinigung wie bei AT: `build_card_adhs.py` (Footer ohne „(Entwurf)"), `build_booklet_adhs.py` (rote Warnbox ersetzt durch „Fachlich geprüft"-Hinweis, Glossar aktualisiert), `build_pdf_adhs.py` (roter Cover-Warnhinweis entfernt, Cover neu aufgebaut inkl. Korrektur desselben Zeilenabstand-Bugs wie bei AT). Neue Datei `KLARTEXT_ADHS-Deck_komplett.pdf` (56 Seiten) gebaut und visuell geprüft (Cover, Anleitung, Kartenfooter — sauber), alte `KLARTEXT_ADHS-Deck_ENTWURF.pdf` bleibt aus Datei-Sicherheits-Policy unangetastet zusätzlich liegen. **ADHS-Deck ist damit vollständig einsatzbereit, kein Vorbehalt mehr.**

**Damit sind jetzt alle zehn Decks der Serie ohne Einschränkung einsatzbereit** (327 Karten: JD 40 + KD 30 + EL 51 + LK 51 + TR 29 + AT 24 + ADHS 24 + FS 30 + DaZ-GS 24 + DaZ-Sek1 24). Offen bleibt nur noch der Bildstil-Swap für JD/KD/EL/LK (Prompts liegen bereits vor, Bilder noch nicht neu generiert) — kein inhaltlicher, nur ein kosmetischer Punkt. **Aktuelle Priorität laut Merkliste bleibt: Kartenserie vermarkten** (siehe „Aktuelle Priorität" unten).

**Bildstil-Swap JD/KD/EL abgeschlossen, LK ohne Änderungsbedarf (27.07.2026).** Neue, modernere Bilder (ohne Zusatzblock-Prompts) lagen für JD, KD und EL-Basis unter neuen, schlichten Dateinamen (`XX-NN.jpg`, kein Titel-Suffix) in den jeweiligen `bilder/`-Ordnern vor. Dabei aufgefallen: **JD und KD hatten nie eine vollständige Pipeline in klartext-app** — bei JD existierte nur das generische `build_booklet.py` (JD-Anleitung/Glossar/Quellen), bei KD lag die komplette, bereits früher fertiggestellte Pipeline (`build_card_kd.py`, `build_all_cards_kd.py`, `build_booklet_kd.py`, `build_pdf_kd.py`, `build_bonuskarte_kd.py`) nur im Scratch-Arbeitsordner, nie nach klartext-app kopiert. **JD-Pipeline komplett neu aufgebaut** (Renderer, Batch-Builder mit allen 40 Kartentexten, PDF-Builder nutzt das bestehende `build_booklet.py`), mit den neuen Bildern gerendert, `KLARTEXT_JD-Deck_komplett.pdf` (87 Seiten) gebaut und in klartext-app abgelegt. **Bug gefunden und gefixt:** Cover-Unterzeile überlappte die große Titelzeile „JD-Deck" (gleicher Bug-Typ wie zuvor bei AT/ADHS) — Zeilenabstand korrigiert (Unterzeile von mm(112) auf mm(128), Intro-Text von mm(128) auf mm(144)). **KD-Pipeline aus dem Scratch-Ordner reaktiviert** statt neu geschrieben (spart Dopplung, bereits inkl. Bonus-Barometer-Karte, Methodik-Seite mit 5-Zustände-Barometer + kLAR-Modell): `find_image()` in `build_all_cards_kd.py` um die neue schlichte Namenskonvention ergänzt (bisher nur `KD-NN <Titel>.jpg` erkannt), und den bisherigen Skip für KD-01/KD-06 entfernt (die beiden Karten waren nur übersprungen worden, weil ihre Bilder noch korrigiert wurden — liegen jetzt vor). Alle 30 Karten + Bonus-Karte neu gerendert, `KLARTEXT_KD-Deck_komplett.pdf` (69 Seiten) neu gebaut, ersetzt die alte, mit den ursprünglichen Bildern gebaute Fassung. **EL-Basis** einfach mit den neuen Bildern neu gerendert (Pipeline war bereits korrekt, `find_image()` unterstützte die schlichte Namenskonvention schon vorher) — `KLARTEXT_EL-Deck_Basis_komplett.pdf` (68 Seiten) neu gebaut. Alle drei PDFs visuell stichprobengeprüft (Cover, mehrere Kartenpaare, bei KD zusätzlich die zuvor blockierten Karten KD-01/KD-06 und die Bonus-Karte) — sauber, kein Überlauf, kein Titel-Overlap. **Korrektur: LK-Einschätzung war falsch, LK ebenfalls neu gerendert (27.07.2026, Abend).** Die erste Einschätzung („LK-Basis geprüft und bewusst nicht neu gerendert, Stichprobe LK-R-01.jpg zeigt bereits den korrigierten Stil") war ein Fehler — Anja hat zu Recht widersprochen. Bei genauerer Prüfung (mehrere Bilder statt nur eines) zeigte sich, dass alle LK-Bilder (Basis 30 + Zusatzblöcke 21) tatsächlich in einem abweichenden, weicheren Aquarell-Stil mit sichtbarem Papierrand vorlagen — obwohl `LK_Bildkonzept_und_Prompts.md`/`LK_Zusatzbloecke_Bildprompts.md` von Anfang an korrekt den „clean digital illustration"-Stilzusatz enthielten (verifiziert: alle 51 Prompts bereits korrekt, unter 480 Zeichen, kein Nacharbeiten der Prompt-Texte nötig). Alle 51 Prompts als Copy-Felder gepostet, Anja hat alle 51 Bilder neu generiert (gleicher Dateiname wie zuvor, `LK-R-NN.jpg` etc. — LK nutzte von Anfang an die schlichte Namenskonvention, keine Titel-Suffixe wie ursprünglich bei JD/KD/EL). Stichprobe (LK-R-01, LK-R-AT-01) nach dem Umbau visuell geprüft: jetzt konsistent mit JD/KD/EL im „clean digital illustration"-Stil. `build_all_cards_lk.py`/`build_all_cards_lk_zusatz.py` erneut ausgeführt (kein Overflow), `KLARTEXT_LK-Deck_Basis_komplett.pdf` (68 Seiten) sowie alle drei Zusatzblock-PDFs (`KLARTEXT_LK-Zusatzblock_Autismus.pdf`, `_ADHS.pdf`, `_Pflegekinder.pdf`, je 15 Seiten) neu gebaut, visuell stichprobengeprüft (Cover, Karte 01, Karte 30, Zusatzblock-Karte AT-01) — sauber. Alte, mit den ursprünglichen Bildern gebauten PDF-Fassungen bleiben aus Datei-Sicherheits-Policy zusätzlich unangetastet liegen. **EL-Zusatzblöcke** (Autismus/ADHS/Pflegekinder, 21 Karten) sind von diesem Bildstil-Swap nicht betroffen — deren Bilder tragen weiterhin die ursprünglichen Prompts aus `EL_Zusatzbloecke_Bildprompts.md` und wurden unverändert gelassen.

### Grundsatzentscheidung (geklärt, 23.07.2026, bestätigt 25.07.2026)
ADHS und DAZ/Migration (GS + Sek I) bleiben eigene Decks – nicht in JD/KD/FS integriert. Damit zehn Decks insgesamt: JD, KD, FS, AT, ADHS, DAZ GS, DAZ Sek I, EL, LK, TR.

- **DAZ GS** — **Status (26.07.2026): Kartenkonzept entworfen (24 Karten), wartet auf Freigabe.** Grundlage: `M4-04_DAZ-freundliche_Sprache.html` (Sprachprinzipien, keine Zitate) sowie zwei real verifizierte Quellen aus `KLARTEXT_Migration_Eltern.html` neu geprüft: Gogolin (1994, 2. Auflage 2008) „monolingualer Habitus" und Mecheril (2004) „Migrationsandere" (Begriff nur über Sekundärquellen bestätigt, vor Registereintrag noch am Original prüfen) — beide „vorgeschlagen, bitte gegenprüfen". Sechs Blöcke à 4 Karten (Ankommen, Sprache lernen, Zwischen zwei Welten, Freundschaft trotz Sprachbarriere, Was ich vermisse, Stolz auf mich). Struktur wie KD/FS (Content-Achse, „Tipp für die INGRA", keine dritte Frage, Brainy dabei). **Bewusst kein Trauma-Verarbeitungs-Deck** — keine Karte fragt nach Fluchtdetails, Heimweh-Karten bleiben beim Gefühl in der Gegenwart, Tipp verweist bei Bedarf auf professionelle Unterstützung statt Nachfragen. **Anja hat entschieden (26.07.2026):** (1) Eigene DaZ- und Traumapädagogik-Qualifikation deckt die Fachprüfung ab, kein externer Review — **kein** Fachprüfungs-Vorbehalt (wie FS, anders als AT/ADHS). (2) Farbe korrigiert von Limettengrün auf **Azurblau `#00ACD6`** — Anja hat zurecht angemerkt, dass Grün/Gelb zu nah an KD/FS liegt; Azurblau ist eine komplett neue Farbfamilie, Abstand 77.2 zur nächsten Farbe (App-LK-Blau), sogar minimal größer als der bisherige Bestwert bei ADHS (74.7). (3) Brainy bleibt dabei, wie bei KD/FS. (4) Bilder bewusst offen/gemischt halten, keine bestimmte Herkunftsregion. Vollständiger Entwurf mit allen 24 Kartentexten liegt in `DAZ-GS_Kartenkonzept_Entwurf.md`. **Bildkonzept + Pipeline fertig gebaut:** `DAZ-GS_Bildprompts.md` (24 copy-ready Prompts mit Dateinamen, Brainy-Kurzbeschreibung inkl. Herz, aktueller KD/FS-Stil-Zusatz, alle unter 480 Zeichen, max. 465 — bewusst keine feste Hautfarbe/Ethnie in den Prompts, mit Hinweis an Anja, beim Generieren selbst auf sichtbare Vielfalt über die 24 Bilder zu achten), `build_card_dazgs.py` (Renderer, Azurblau mit dunklerer Textvariante, „Tipp für die INGRA", keine Systemfrage, normaler footer_deck ohne „(Entwurf)"), `build_all_cards_dazgs.py` (24 Kartentexte), `build_booklet_dazgs.py` (Anleitung 2 Seiten mit rot umrandeter „Kein Trauma-Verarbeitungs-Deck"-Warnbox, Methodik-Seite, Glossar 2 Seiten, Quellen-Seite mit Gogolin + Mecheril), `build_pdf_dazgs.py` (normales Cover, bricht kontrolliert ab, solange Bilder fehlen). Alle Booklet-Seiten testweise gerendert und visuell geprüft (Anleitung 2/2, Karte 10, Karte 24) — sauber, gute Lesbarkeit auf Azurblau. Rückseiten-Layout für alle 24 Karten testweise gerendert (ohne Bilder) — keine Overflow-Warnungen. Alle Dateien in klartext-app abgelegt, `bilder/dazgs/`-Ordner angelegt. **DaZ-GS-Deck fertig (26.07.2026):** alle 24 Bilder lagen in `bilder/dazgs/` vor, Karten gerendert (kein Overflow-Warning), Gesamt-PDF `KLARTEXT_DAZ-GS-Deck_komplett.pdf` (55 Seiten: Cover, Anleitung 2 Seiten, Methodik, Glossar 2 Seiten, Quellen, 24 Karten) gebaut, visuell stichprobengeprüft (Cover, Karte 01/02, Karte 23/24 — alles sauber, gute Lesbarkeit auf Azurblau, Brainy konsistent mit Herz, sichtbar diverse Kinder in der Stichprobe). Damit **neuntes vollständig produziertes Kartendeck (303 Karten insgesamt über alle neun Decks: JD 40 + KD 30 + EL 51 + LK 51 + TR 29 + AT 24 + ADHS 24 + FS 30 + DaZ-GS 24)**. Wie FS: **kein** Fachprüfungs-Vorbehalt, direkt einsatzbereit. Nur noch **DaZ Sek I** fehlt zur vollständigen Zehner-Serie. **Nächster Schritt:** offen, liegt bei Anja (z. B. DaZ Sek I als letztes Deck, Fachprüfung für AT/ADHS organisieren, oder Bild-Swap für JD/KD/EL/LK nachholen).

- **DAZ Sek I** — **Status (26.07.2026): Pipeline fertig gebaut, wartet auf Bilder.** Grundlage: derselbe Bruchpunkt-Gedanke wie oben (neues Schulsystem, komplexere soziale Dynamik, Identität/Diskriminierung explizit statt nur schwerere Vokabeln einer GS-Version), Anjas Augeo-Qualifikation „Geflüchtete Jugendliche unterstützen" speziell für Sek I einschlägig. Sechs Blöcke à 4 Karten (Ankommen im neuen System, Sprache & Leistung, Identität zwischen den Kulturen, Freundschaft & Zugehörigkeit, Herkunft & was ich vermisse, Zukunft & Stolz). Struktur wie DaZ-GS (Content-Achse, „Tipp für die INGRA", keine dritte Frage), **aber kein Brainy** (wie JD/AT/ADHS — für Sek-I-Jugendliche zu kindlich). Gleiche zwei Quellen wie DaZ-GS (Gogolin 1994/2008, Mecheril 2004, beide „vorgeschlagen, bitte gegenprüfen"). **Bewusst weiterhin kein Trauma-Verarbeitungs-Deck** — gleiche Abgrenzung wie DaZ-GS, aber Diskriminierung und doppelte kulturelle Identität werden hier (anders als bei DaZ-GS) direkt benannt, da altersgerecht für Jugendliche. **Anja hat entschieden (26.07.2026):** (1) Eigene Qualifikation deckt die Fachprüfung ab (wie DaZ-GS/FS) — **kein** Fachprüfungs-Vorbehalt. (2) Farbe **Bordeaux `#6E1438`** bestätigt, rechnerisch kollisionsgeprüft (Abstand 70.2 zur nächsten Farbe, App-EL-Modul-Magenta) über eine systematische Rot-Farbfamilien-Rastersuche gefunden, bewusst dunkler/reifer als DaZ-GS. (3) Kein Brainy bestätigt. Vollständiger Entwurf mit allen 24 Kartentexten liegt in `DAZ-SEK1_Kartenkonzept_Entwurf.md`. **Bildkonzept + Pipeline fertig gebaut:** `DAZ-SEK1_Bildprompts.md` (24 copy-ready Prompts mit Dateinamen, kein Brainy, JD/AT/ADHS-Stil-Zusatz statt KD-Variante, alle unter 480 Zeichen, max. 306 — Jugendliche ca. 12–16 Jahre statt Kinder, bewusst keine feste Hautfarbe/Ethnie), `build_card_dazsek1.py` (Renderer, Bordeaux, „Tipp für die INGRA", keine Systemfrage, normaler footer_deck ohne „(Entwurf)"), `build_all_cards_dazsek1.py` (24 Kartentexte), `build_booklet_dazsek1.py` (Anleitung 2 Seiten mit rot umrandeter „Kein Trauma-Verarbeitungs-Deck"-Warnbox, Methodik-Seite, Glossar 2 Seiten inkl. Migrationsandere-Begriff mit Quellenlage-Hinweis, Quellen-Seite mit Gogolin + Mecheril), `build_pdf_dazsek1.py` (normales Cover, bricht kontrolliert ab, solange Bilder fehlen). Alle Booklet-Seiten testweise gerendert und visuell geprüft (Anleitung 2/2, Karte DAZ-SEK1-06) — sauber, gute Lesbarkeit auf Bordeaux. Rückseiten-Layout für alle 24 Karten testweise gerendert (ohne Bilder) — keine Overflow-Warnungen. Alle Dateien in klartext-app abgelegt, `bilder/dazsek1/`-Ordner angelegt.

**DaZ-Sek-I-Deck fertig (27.07.2026) — zehntes und letztes Deck der Serie.** Alle 24 Bilder lagen in `bilder/dazsek1/` vor (ein Dateiname mit Tippfehler, `DAZ-SEK1-02..jpg`, doppelter Punkt — wie beim EL-Zusatzblock bewusst nicht umbenannt, `find_image()` glob-robust dagegen ergänzt). Karten gerendert (kein Overflow-Warning). **Bug gefunden und gefixt:** Die Cover-Unterzeile ("24 Impulskarten · Deutsch als Zweitsprache, Sekundarstufe I") war bei fester Schriftgröße 7mm mit 188,7mm breiter als die verfügbaren ~170mm auf der Seite und lief rechts über den Rand — beim Sichtcheck des Covers aufgefallen, nicht vorab durch die reinen Text-Overflow-Checks der Kartenrückseiten abgedeckt. Fix in `build_pdf_dazsek1.py`: automatische Schriftverkleinerung auf 5,4mm, wenn die Zeile die verfügbare Breite überschreitet. Gesamt-PDF `KLARTEXT_DAZ-SEK1-Deck_komplett.pdf` (55 Seiten: Cover, Anleitung 2 Seiten, Methodik, Glossar 2 Seiten, Quellen, 24 Karten) gebaut, visuell stichprobengeprüft (Cover nach Fix, Karte 01, Karte 24 — alles sauber, Jugendliche statt Kinder erkennbar, kein Brainy, gute Lesbarkeit auf Bordeaux). Damit **zehntes und letztes vollständig produziertes Kartendeck der Serie (327 Karten insgesamt: JD 40 + KD 30 + EL 51 + LK 51 + TR 29 + AT 24 + ADHS 24 + FS 30 + DaZ-GS 24 + DaZ-Sek1 24)**. Wie DaZ-GS/FS: **kein** Fachprüfungs-Vorbehalt, direkt einsatzbereit. **Damit ist die komplette Zehner-Serie technisch produziert.** Offene Punkte, die über die Serie hinaus bestehen bleiben: Fachprüfung für AT/ADHS extern organisieren (einzige zwei Decks mit Entwurfs-Status), Bild-Swap im neuen Stil für JD/KD/EL/LK noch nicht nachgeholt (Prompts liegen bereits aktualisiert vor).

**Bestätigung (25.07.2026):** Eine parallel eingeholte Einschätzung (Dokument „Guter Zeitpunkt für einen Gesamtüberblick") hatte vorgeschlagen, ADHS und DaZ von eigenen Decks auf Querschnitts-Zusatzkarten (4–6 pro Deck) umzustellen und den DaZ-GS/Sek-Split aufzugeben. Das widersprach der obigen Entscheidung. Anja hat sich bewusst für die ursprüngliche Entscheidung entschieden — eigene Vollständig-Decks bleiben, DaZ-Split bleibt. Begründung: nutzt die realen DaZ-Qualifikationen (Goethe-Institut, zwei getrennte Augeo-Kurse für GS/Sek, siehe Strang 4) und den bereits fundiert begründeten Sek-Bruchpunkt voll aus, statt sie in dünnen Zusatzkarten zu verwässern.

### Alters-Differenzierung ADHS/AT vs. DAZ (geklärt, 23.07.2026)
- **DAZ bleibt in GS/Sek I gesplittet** – die Sek-I-Grenze ist ein realer Bruchpunkt (neues Schulsystem, neue soziale Komplexität, Identität/Diskriminierung), das Thema verändert sich qualitativ mit dem Schulwechsel.
- **ADHS und AT bleiben je EIN Deck** (kein GS/Sek-Split) – die Diagnose bleibt über die Altersspanne gleich, nur die Ausprägung verschiebt sich graduell. Stattdessen Alters-Kennzeichnung auf Kartenebene, analog zur bestehenden Konvention bei KD-12 ("Für jüngere Kinder · 1.–3. Klasse").
- Autismus ist der wahrscheinlichste Kandidat für eine spätere Sek-Erweiterung (Pubertät bringt Masking, Identität, erhöhtes Depressions-/Angstrisiko dazu) – aber erst nachziehen, wenn das Basisdeck Nachfrage zeigt, nicht von Anfang an.

### Neuer Diskussionspunkt: Übergänge (offen)
Im Repo bereits vorhanden, aber verstreut statt gebündelt:
- Drei bestehende Spiele: Kita→Schule, neue Schule, Schule→Arbeit (KLARTEXT_Spiel_UebergangKitaSchule/NeueSchule/SchuleArbeit)
- Allgemeines Modul M2-21 Übergänge, außerdem M7-02 (Übergänge im Schulalltag, tagesaktuell)
- Gut ausgebauter ADHS-spezifischer Übergang-Cluster: LK-17_ADHS_Uebergang, M5-13_Uebergang_ADHS_Werkzeuge, M2-42_ADHS_Ausbildungsreife (bereits fundiert zitiert: Bundesagentur für Arbeit/Nationaler Pakt für Ausbildung, Kriterienkatalog 2006, 25 Merkmale in 5 Bereichen – wendet kLAR-Modell auf Übergang Schule→Beruf an)
- Akademische Grundlage vorhanden: Griebel & Niesel (2004, 2011) – Transitionsforschung/Co-Konstruktionsansatz, etabliertes Feld in der deutschen Bildungsforschung

**Empfehlung (vorläufig):** Übergänge nicht als eigenes 11. Deck, sondern als Querschnittsthema in bestehende/geplante Decks verteilen – Kita→Schule in KD, Schule→Ausbildung in JD, "neue Schule"/Ankommen mit DAZ GS verzahnen. Der ADHS-Übergang-Ausbildungsreife-Cluster ist bereits so weit ausgearbeitet, dass er der natürliche Kern einer späteren ADHS-Sek/Ausbildungs-Erweiterung wäre (siehe Alters-Differenzierung oben).

**Vierte Übergangs-Kategorie ergänzt (23.07.2026, korrigiert):** Anja hat die 51-stündige Fortbildung "Transitionspsychiatrie" bei Prof. Dr. Jörg Fegert (Universitätsklinikum Ulm, Klinik für Kinder- und Jugendpsychiatrie), gefördert vom DZPG (Deutsches Zentrum für psychische Gesundheit) und BMFTR, **erfolgreich abgeschlossen** – alle drei Modulprüfungen + Gesamtprüfung bestanden am 29.05.2026, **Note 1.7**. (Vorheriger Stand "noch offen" war die Teilnahmebescheinigung, nicht das finale Zertifikat.) Thema: Übergang von Kinder-/Jugendpsychiatrie in Erwachsenenpsychiatrie ("Care Leaver", Empowerment, rechtlicher Kontext: Familienrecht, Sozialrecht, Patientenrechte, Kinderschutz). Kursthemen decken viele bereits im M2-Modul vorhandene Störungsbilder ab (Autismus, ADHS, Angststörungen, Essstörungen, Bindungsstörungen u.a.) und könnten diese vertiefen. **Wichtig:** Das PDF selbst enthält keine zitierfähige Quellenliste, nur Kursthemen + Trägerangabe. Als Herkunftsangabe nutzbar: "Fortbildung Transitionspsychiatrie, Prof. Dr. Jörg Fegert, Universitätsklinikum Ulm / DZPG, 2026".

**Recherchierte Original-Publikationen (23.07.2026), zitierfähig:**
- Fegert, J. M., Hauth, I., Banaschewski, T. & Freyberger, H. J. (2017). Übergang zwischen Jugend- und Erwachsenenalter: Herausforderungen für die Transitionspsychiatrie. Eckpunktepapier von DGKJP und DGPPN. *Zeitschrift für Kinder- und Jugendpsychiatrie und Psychotherapie, 45*(1), 80–85. [Hogrefe](https://econtent.hogrefe.com/doi/abs/10.1024/1422-4917/a000502) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/28124949/) — gemeinsames Positionspapier der Fachgesellschaften DGKJP (Kinder-/Jugendpsychiatrie) und DGPPN (Erwachsenenpsychiatrie), definiert Transitionsalter 15–25 Jahre.
- Transitionspsychiatrie der Adoleszenz und des jungen Erwachsenenalters. *Zeitschrift für Psychiatrie, Psychologie und Psychotherapie, 63*(3). [Hogrefe](https://econtent.hogrefe.com/doi/abs/10.1024/1661-4747/a000234) — genaue Autorenliste vor Verwendung nochmal verifizieren.
- Transitionspsychiatrie [Themenheft]. *Zeitschrift für Kinder- und Jugendpsychiatrie und Psychotherapie, 48*(6). [Hogrefe](https://econtent.hogrefe.com/doi/10.1024/1422-4917/a000737) — Sammelband/Themenausgabe, Einzelbeiträge vor Zitat prüfen.

### Cross-Cutting / bereits erledigt
- Gendering-Überprüfung der Karten per NotebookLM — erledigt.
- Weitere inhaltliche Inkonsistenzen geprüft — erledigt.
- Marktvergleich dokumentiert: Don Bosco "Kinder-Coaching: Den Schatz in mir finden" — 32 Karten (nicht 30), A5, 350g Karton, 4–10 Jahre, Autorin selbst systemische Beraterin/Supervisorin, ca. 21–22 €. Referenz für eigene Kalkulation.

## Strang 1b · Assoziatives Bildercoaching-Set (neu, 24.07.2026)
Idee aus Gespräch: eigenständiges Kartenset mit bewusst offenen, nicht themengebundenen Bildern – im Unterschied zu den klaren, themenspezifischen JD/KD/FS/AT-Bildern. Projektive/assoziative Coaching-Methode: Person legt eigene Bedeutung ins Bild, statt vorgegebenes Thema zu bearbeiten. Kein Ersatz für die bestehende Kartenserie, sondern eigene Werkzeugkategorie daneben.

**Zielgruppen-Einschränkung wichtig:** passt eher zu Personen mit höherer Abstraktionsfähigkeit (ältere, verbal fitte Jugendliche, Erwachsene) oder zur INGRA-Selbstreflexion/Supervision selbst. Weniger geeignet für jüngere Kinder (KD) und ausdrücklich nicht für AT-Zielgruppe (dort bewusst wörtliche, nicht-metaphorische Sprache/Bilder als Prinzip festgelegt) – Konflikt mit Barrierefreiheits-Ziel der Hauptserie vermeiden.

Status: Idee vorgemerkt, nicht priorisiert, kein Konzept ausgearbeitet.

## Strang 1c · Ideensammlung Erweiterung (Brainstorming, 24.07.2026)
Sammlung aus Gespräch, keine der Ideen priorisiert oder konzeptionell ausgearbeitet — nur vorgemerkt für spätere Prüfung.

### Methoden-Produkte (eigenständige Tools, themenübergreifend statt zielgruppengebunden)
- **Familienbrett** — klassisches systemisches Werkzeug (Ludewig), Familienmitglieder als Figuren zur Visualisierung von Beziehungen/Distanzen. Kandidat für eigenständiges physisches Produkt neben den Kartendecks.
- **Genogramm-Set** — Vorlagen + Symbol-Legende zur gemeinsamen Visualisierung von Familienstrukturen mit Kindern/Jugendlichen. Bisher kein eigenes Tool im System vorhanden.
- **Fragetechniken-Set für INGRA-Schulung** — Skalierungsfragen, Wunderfrage (de Shazer/lösungsfokussierte Kurztherapie) als eigenständiges Werkzeug ausgekoppelt; Kandidat fürs bestehende TR-Deck statt eigenes Produkt.
- **Werte-Kartenset** — themenübergreifendes Standard-Coaching-Tool (Werte sortieren/gewichten), funktioniert für alle Zielgruppen inkl. INGRA-Supervision, geht über JD-27 hinaus.

### Themen-/Zielgruppen-Lücken → jetzt drei konkrete Ergänzungssets (präzisiert 25.07.2026)
Ursprünglich als lose Ideen notiert (24.07.), jetzt anhand des Gesamtüberblick-Dokuments konkretisiert. Bewusst als **drei getrennte kleine Ergänzungssets** (nicht zu einem großen "Übergänge & Verlust"-Set zusammengelegt) — Begründung: Pflegekinder und Verlust eines Menschen brauchen beide erst fachliche Prüfung vor Kartentexten, Geschwisterkinder nicht. Getrennt lassen heißt, Geschwisterkinder kann sofort starten, ohne auf die Fachprüfung der anderen beiden zu warten.

- **Pflegefamilien/Pflegekinder** — ~12–15 Karten, altersunabhängig einsetzbar. Bisher nur Verweis in M2 (M2-31/32), kein eigenes Set. **Mögliche echte Marktlücke** (Anjas Einschätzung 24.07.2026). **Fachprüfungs-Vorbehalt aufgehoben (25.07.2026):** Anja hat mehrere Jahre in der Förderschule Sprache/Lernen mit genau dieser Zielgruppe (Wohngruppen/Pflegekinder) gearbeitet (siehe Strang 4b) und bringt die fachliche Perspektive selbst mit ein — kein externer Review-Schritt mehr nötig, kann direkt entworfen werden wie die anderen Decks.
- **Geschwisterkinder** (Geschwister von Kindern mit Förderbedarf) — ~12–15 Karten. Alltagsthemen (Aufmerksamkeit, Fairness, eigene Bedürfnisse neben einem Geschwister mit Unterstützungsbedarf) — unproblematischer, kann normal wie die anderen Decks entwickelt werden, keine Fachprüfung vorab nötig.
- **Verlust eines Menschen** (Elternteil, Geschwister, Großeltern) — wie Pflegekinder: **nicht ohne fachliche Begleitung entwerfen**. Kindertrauer ist ein eigenes Fachgebiet mit eigenen Prinzipien (keine beschönigenden Floskeln, Ambivalenz zulassen, keine erzwungene "Verarbeitung" in festem Zeitrahmen) — falsch formulierte Impulse können hier mehr schaden als in fast jedem anderen Thema. Bei plötzlichem/traumatischem Verlust (Suizid, Unfall): eher Feuerwehrkarten-Nähe als normales Coaching-Set. Erstmal nur Themenliste, keine Kartentexte.
- **Haustier-Verlust** — davon klar getrennt und unproblematisch: gut erforschtes, oft erstes bewusstes Verlusterlebnis, emotional zugänglicher als Verlust eines Menschen. Kann normal als Themenblock in KD/JD integriert werden, kein Fachprüfung-Vorbehalt.
- **Legasthenie/Dyskalkulie** — **Anja hat hierfür bereits reale fachliche Grundlage:** eigene Unterrichtserfahrung, Zertifikate (UDEMY Dyskalkulie, Legasthenie, Zertifikat LRS; AlphaPROF LRS/Alphabetisierung) sowie abgeschlossene Ausbildung Integrative Lerntherapie (IFLW, siehe KLARTEXT_Qualifikationsnachweise.md). Kein Recherche-Neuaufbau nötig, direkt aus eigener Praxis bedienbar — ähnlich starke Ausgangslage wie beim DAZ-Fund (Strang 4).
- **Hochbegabung** — häufige Realität im Schulalltag, bisher keine dedizierte Grundlage im System.

Status: Ideensammlung, nichts priorisiert, keine Konzeptarbeit begonnen.

## Strang 2 · Zusatzvermarktung (später, nach Kartenserie)
- Workbook einzeln vermarkten.
- Unterrichtsmaterialien passend zu den Decks (späterer Schritt, ursprünglich schon angekündigt).
- Ggf. weitere bestehende App-Bausteine einzeln vermarktbar — noch nicht geprüft.

## Strang 3 · App-Aufspaltung (parallel, technisch)
- Reine INGRA-App ohne Supabase/Weiterleitungen geplant (Datenschutz-Grund).
- Separate Trainer-App geplant.
- **Technischer Befund:** Weiterleitungen (Migration 0008) und Barometer_kind (Migration 0007) sind die trägerübergreifenden, DSGVO-sensiblen Bausteine — der eigentliche Case-Management-Kern der App. Trainingsinhalte (M0–M8, Glossar, Karten) könnten technisch backend-frei laufen.
- Rechtliche Prüfung durch Datenschutzkanzlei vor endgültiger Architekturentscheidung empfohlen (keine Rechtsberatung durch mich möglich).
- Stand: noch nicht begonnen.

## DRINGEND · Repo-Trennung Marketing vs. Pilot-App (23.07.2026)
Eine separate Claude-Code-Session hat `JD_Verkaufsseite.html` direkt im Repo `klartext-app` erstellt und als PR #109 (Branch `feature/jd-verkaufsseite`) gepusht, inkl. Cloudflare-Preview. **Nicht gemerged, auf Anjas Anweisung gestoppt.**

**Problem:** Kein separates Wrangler/Pages-Konfig-File im Repo gefunden → Cloudflare-Deployment hängt vermutlich direkt am Repo `klartext-app`. Die App in ihrer jetzigen Form ist aktuell in der **Beta-/Testphase bei den Maltesern** (echte Pilot-Partnerorganisation, vgl. KLARTEXT_Malteser_Anleitung.html, KLARTEXT_Beta_Anleitung.html). Ein Merge hätte die JD-Verkaufsseite auf derselben Umgebung live geschaltet, die Malteser gerade testet.

**Maßnahme:** PR #109 nicht mergen, schließen (Datei bleibt auf Branch erhalten). Alle künftigen Karten-Verkaufsseiten (JD, KD, FS, AT, ADHS, DAZ GS/Sek, EL, LK, TR) grundsätzlich in einem **eigenen, getrennten Repo** mit eigenem Cloudflare-Pages-Projekt/eigener Domain bauen — nicht in `klartext-app`. Verschärft/beschleunigt die bereits unter Strang 3 (App-Aufspaltung) dokumentierte Notwendigkeit, Case-Management-App und Content-/Marketing-Ebene technisch zu trennen.

**Lehre für Zusammenarbeit mit externen Coding-Sessions:** Bauprompts für Coding-Tools künftig explizit mit Ziel-Repo/Ziel-Deployment spezifizieren, nicht implizit "im bestehenden Repo" annehmen lassen.

**Status: erledigt (23.07.2026).** Neues, getrenntes Repo `anja2026-dev/klartext-shop` angelegt, `JD_Verkaufsseite.html` dorthin verschoben, eigenes Cloudflare-Pages-Projekt aufgesetzt (nicht Workers — wichtig für künftige Decks: bei neuen Cloudflare-Projekten immer "Pages" wählen, nicht "Workers", sonst schlägt der Build fehl). Datei zu `index.html` umbenannt, damit die Root-Domain direkt lädt. Läuft jetzt live unter `klartext-shop.pages.dev`, getrennt von der Malteser-Pilot-App. PR #109 in `klartext-app` sollte noch geschlossen werden (falls noch nicht geschehen). Muster für alle künftigen Deck-Verkaufsseiten: gleiches Repo `klartext-shop` nutzen, jede weitere Seite als eigene Datei oder Unterseite.

## Strang 4b · Anjas praktische Berufserfahrung Förderschule — neu, 25.07.2026
Direkte, mehrjährige Praxiserfahrung, ergänzend zu den zertifizierten Fortbildungen (Strang 4). Wichtig für die FS-Deck-Konzeption und angrenzende Ergänzungssets, weil es reale Zielgruppenkenntnis statt nur Literaturwissen ist:

- **7 Jahre Förderschule, Schwerpunkt geistige Entwicklung + Sehen** — Arbeit mit Kindern mit kombinierter geistiger Behinderung und Sehbehinderung/Blindheit, darunter viele mit zusätzlicher Autismus- oder ADHS-Diagnose (Mehrfachbehinderung). Macht eine "Geistige Entwicklung + Sehen"-Variante (tastbar/multisensorisch statt reines Kartenformat) zu einem durch echte Erfahrung gedeckten, ernstzunehmenden künftigen Produkt — nicht einfach mit der ursprünglichen Blindheit-Abgrenzung ("Kartenformat funktioniert nicht für blinde Kinder") vom Tisch zu wischen. Offene Frage: eigenes taktiles Format nötig, kein einfaches Karten-Prinzip.
- **Später: Förderschule Sprache + Lernen, viele Kinder aus Wohngruppen/Pflegefamilien** — direkte, mehrjährige Praxiserfahrung mit genau der Zielgruppe des geplanten Pflegekinder-Ergänzungssets (siehe Strang 1c). **Geklärt (25.07.2026):** Anjas eigene Erfahrung deckt die Fachprüfungs-Hürde ab, kein externer Review nötig.

**Status (25.07.2026): erste Konzeptskizze für „Geistige Entwicklung + Sehen" erstellt** (Datei `Konzeptskizze_Geistige_Entwicklung_Sehen.md`) — bewusst als Diskussionsgrundlage markiert, kein fertiges Produkt. Vorschlag: Tastobjekte/Bezugsgegenstände statt Bildkarten, angelehnt an Basale Stimulation (Fröhlich) und Unterstützte Kommunikation für blinde/sehbehinderte Nutzer:innen, da das Bildkarten-Prinzip hier aus zwei Gründen nicht passt (visuelle Verarbeitung UND oft fehlende Fähigkeit zu abstrakten Reflexionsfragen). Offene Fragen: Produktionsweg (physische Tastmaterialien statt Print-PDF, strukturell anders als alle bisherigen Decks), realistischer Themenumfang, ob Brainy in taktiler Form sinnvoll ist. **Nächster Schritt liegt bei Anja:** Skizze aus der eigenen Praxiserfahrung korrigieren/prüfen, bevor Umfang oder Format festgelegt wird.

## Strang 4 · Anjas Fachqualifikationen (Uniklinikum Ulm) — neu, 23.07.2026
Acht Fortbildungen bei Uniklinikum Ulm, insgesamt ca. 187,75 Stunden. Alle mit FE/FP-Nachweis, teils Landesärztekammer-anerkannt:

1. Sensibilisieren und Gewaltprävention im ehrenamtlichen Kontext (4h)
2. E-Learning für Hausärzt:innen zum Umgang mit Menschen mit psychischen Erkrankungen (BASEpsyche) (7h)
3. Ansprechen oder nicht ansprechen? E-Curriculum zu psychosozialen Themen in der Hausarztpraxis (BASEpro) (16,5h)
4. **Online-Kurs Transitionspsychiatrie (51h) — abgeschlossen, Note 1.7** (s. Strang: Übergänge)
5. Schutz und Hilfe bei häuslicher Gewalt – interdisziplinärer Online-Kurs (40h)
6. Frühe Kindheitsbelastungen: Vorbeugen, erkennen, behandeln (12h)
7. Grundwissen Kinderschutz für Berufsgeheimnisträger:innen (40h)
8. **Trauma im Kontext Flucht und Asyl – Traumatherapie mit Geflüchteten (17,25h)**

**Strategisch wichtigster Treffer:** Kurs 8 (Flucht/Asyl-Trauma) schließt genau die fachliche Lücke, die bei DAZ/Migration GS/Sek I identifiziert wurde (bisher keine vorhandene Fachgrundlage im Repo, anders als bei ADHS/Autismus). Das ist jetzt eine reale, zertifizierte Wissensbasis für die DAZ-Decks – nicht mehr "muss neu recherchiert werden", sondern "vorhanden, muss nur noch übersetzt werden".

Weitere Anknüpfungen: Kurs 6 & 7 vertiefen die bestehenden M2-Karten zu Bindungstrauma/Pflegekindern/Kinderschutz; Kurs 5 vertieft die Hochkonflikt-Eltern- und Kinderschutz-Inhalte; Kurs 1 passt zu TR/Ehrenamts-Kontext.

**Marketing-Nutzen:** Reale, prüfbare Fortbildungsnachweise einer Universitätsklinik (nicht nur Literaturzitate) sind ein zusätzliches Differenzierungsargument gegenüber dem Wettbewerb – "fachlich fundiert durch zertifizierte Fortbildungen, nicht nur durch Literaturrecherche".

**Erweiterung (23.07.2026):** Vollständige Weiterbildungsliste (über 400 Kurse, Excel "Meine Weiterbildungen2.xlsx") ausgewertet und nach KLARTEXT-Relevanz kategorisiert → eigene Datei **KLARTEXT_Qualifikationsnachweise.md**. Wichtigster Fund: DAZ/Migration-Lücke ist durch Anjas eigene Qualifikationen praktisch geschlossen – formale Goethe-Institut-Qualifikation "DAZ in der Grundschule", plus zwei bereits getrennte Augeo-Kurse "Geflüchtete Kinder unterstützen" (GS) und "Geflüchtete Jugendliche unterstützen" (Sek I), die exakt zum geplanten GS/Sek-I-Split passen. Dazu formale FAPS-Qualifikationen (Fachkraft für Integrationspädagogik, Sprachentwicklungsexpertin, Montessori-Pädagogik), ein explizites ADHS+ASS-Modul (Pflege-Betreuer, § 45 SGB XI), systemisches Coaching (mehrere Kurse), GFK nach Rosenberg, sowie umfassende Kinderschutz-/Trauma-/Deeskalationsnachweise. Details siehe Qualifikationsnachweise-Datei.

## Kartendesign / Farben (23.07.2026)
Anja hat ein bestehendes Konzeptdokument zu GS/JD/AT-Decks bereitgestellt → archiviert in **KLARTEXT_Kartenserie_Konzeptdoku.md**. Wichtigste Klärung: Lila für JD verworfen (Kollision mit TK-Farbe `#4A148C`). Neue Deckfarbe JD: gedecktes Petrol/Teal `#2F6B6E`, geprüft gegen alle bekannten Modul-/Deckfarben (M0–M6, Humor, FK, TK, LK, EL). Template-Datei `JD_Kartentemplate_Beispiel.html` entsprechend aktualisiert. Für KD/GS steht die Farbe jetzt fest: `#2E9E5A` (warmes, kindgerechtes Grün, an Barometer-Grün angelehnt), aus dem KD-Konzeptdokument. Für AT noch offen — Vorschlag bei Bedarf: ruhiges Salbeigrau, kollisionsgeprüft sobald final.

Kartenanzahl: JD fix bei 40. Für GS und AT vorgeschlagen: 20–24 Karten (mehr als der grobe "15–20"-Richtwert aus dem Konzeptdokument, da JD mit 40 Karten in 10 Themenblöcken der Maßstab in der Serie ist — GS/AT sollten nicht spürbar dünner wirken, aber auch nicht zwingend auf 40 aufblähen, da beide Zielgruppen enger gefasste Themenfelder haben als JD).

## Strang 5 · Physisch vs. digital (Sorge geäußert, 26.07.2026)
Anja hat Sorge geäußert, ob physische Papierkarten noch zeitgemäß sind, da alle ständig am Handy sind ("sollten wir nicht doch lieber noch eine Flip-Card-Version machen?"). Einschätzung dazu:

**Physisches Format bewusst beibehalten, nicht durch Digital-Pendant ersetzen.** Begründung: (1) Greifbare Objekte sind ein etabliertes Prinzip systemischer Arbeit (vgl. Familienbrett/Ludewig, bereits als Referenz in Strang 1b) – die Karte-in-der-Hand-Situation ist funktional Teil der Methode, keine zufällige Verpackung. (2) Bei mehreren Zielgruppen (v. a. ADHS-Familien) ist Bildschirmzeit selbst oft ein Konfliktfeld – eine Karte ohne Screen schafft bewusst einen Gegenraum, eine App würde dem entgegenlaufen. (3) Preis-/Marktlogik: Der Don-Bosco-Vergleich (~21–22€, 32 Karten physisch) funktioniert als Zahlungsbereitschaft für ein geschenkfähiges physisches Produkt – für "eine App mehr" liegt die gefühlte Zahlungsbereitschaft in einem übersättigten, oft kostenlosen App-Markt deutlich niedriger.

**Vorschlag statt Vollumstieg – zwei ergänzende digitale Bausteine:**
- **Digitale Vorschau auf der Verkaufsseite** (klartext-shop): 2–3 Karten zum virtuellen "Umdrehen" als Kaufanreiz/Marketing, ersetzt nicht das physische Produkt, bewirbt es.
- **Digitale Karten-Ansicht in der bestehenden App** – dort aber sinnvoll, weil INGRA-Fachkräfte die App (M0–M8, Barometer, LK-01–17) ohnehin täglich nutzen (anders als Eltern/Lehrkräfte als Endkund:innen der Kartendecks, die die App nicht haben). Beträfe primär die Content-Achse/Rollen-Achse-Inhalte, die ohnehin schon in der App liegen – kein neues Produkt, sondern Zugänglichkeit für bereits vorhandene App-Nutzer:innen.

Status: Einschätzung geteilt, noch nicht entschieden/priorisiert. Nächster Schritt liegt bei Anja.

## Strang 6 · Bildstil-Update (26.07.2026)
Anja nutzt Bing Image Creator (DALL·E 3) zur Bildgenerierung – dort viel höheres Nutzungslimit als
bei anderen Tools. Rückmeldung: bisherige Bilder wirken "altbacken", teils körnig, Gesichtsausdrücke
nicht ausdrucksstark genug. Diagnose: Der bisherige Stil-Zusatz ("soft warm illustration style,
muted warm color palette, gentle natural lighting, paper texture background...") enthielt mit
"paper texture background" vermutlich die Hauptursache fürs Körnige, und die übrigen vagen
Beschreibungen ("soft", "muted", "gentle") drängen das Modell in eine generische, verwaschene
Stock-Illustration statt in einen modernen, ausdrucksstarken Stil. Zwei Testprompts mit neuem Zusatz
von Anja in Bing getestet und für deutlich besser befunden ("jaa, viel besser").

**Neuer Stil-Zusatz (ersetzt den bisherigen überall):**
`clean digital illustration, confident linework, smooth shading, vibrant warm colors, expressive
detailed faces, realistic proportions, high resolution, no grain, no texture, no text, no watermark`

**KD-Variante (Kinderbuch-Kontext, sonst identische Prinzipien):**
`modern children's book illustration, confident linework, smooth shading, vibrant warm colors,
expressive detailed faces, realistic proportions, high resolution, no grain, no texture, no text,
no watermark`

**Bing-Zeichenlimit:** Bing akzeptiert nur Prompts bis 480 Zeichen. Alle bestehenden und neuen
Bildprompt-Dateien liegen bereits deutlich darunter (max. 432 Zeichen bei TR, sonst niedriger) –
kein zusätzliches Kürzen nötig.

**Umsetzung (26.07.2026):** Per Skript automatisiert (nicht manuell, um Aufwand/Tokens zu sparen)
den alten Stil-Zusatz in allen bestehenden Bildprompt-/Bildkonzept-Dateien durch den neuen ersetzt:
`EL_Bildkonzept.md` (1), `EL_Zusatzbloecke_Bildkonzept.md` (1), `EL_Zusatzbloecke_Bildprompts.md`
(21), `LK_Bildkonzept_und_Prompts.md` (31), `LK_Zusatzbloecke_Bildprompts.md` (22),
`TR_Bildprompts.md` (29), `KD_Brainy_Prompts.md` (2, inkl. Charakterbogen-Prompt – Brainys
Charakterbeschreibung selbst blieb unverändert, nur der allgemeine Stil-Zusatz wurde ersetzt).
Alle Prompt-Längen nach dem Update erneut unter 480 Zeichen geprüft (keine Überschreitung).
**Kleines Missverständnis geklärt:** Der Test, bei dem "ein Tier statt Brainy" auftauchte, lag an
meinem eigenen Ad-hoc-Testprompt (der zu Demonstrationszwecken eine generische "owl companion"
statt Brainy nutzte) – die eigentliche KD-Datei (`KD_Brainy_Prompts.md`) hat Brainys
Charakterbeschreibung immer explizit in jedem Szenen-Prompt stehen, das war nie betroffen.

**JD-Nachtrag (26.07.2026):** Anja hatte die Prompts für JD-25–40 (16 Karten) und anschließend auch
JD-01–24 (24 Karten) noch aus einer früheren Session vorliegen und beide nachgereicht. `JD_Bild
prompts.md` enthält jetzt **alle 40 JD-Prompts vollständig**, einheitlich auf den neuen Stil-Zusatz
umgestellt (vorher ein inkonsistenter Mix, u. a. mit "paper texture background" bei JD-01–24 –
vermutlich mitverantwortlich für den körnigen Look). Alle 40 Prompts unter 480 Zeichen (max. 311).
**Stilistischer Hinweis notiert:** JD-01–24 arbeiten stärker mit Symbolik (leuchtende Objekte,
Silhouetten, Lichtbrücken) statt mit konkreten Szenen wie JD-25–40 – der neue Zusatz enthält
"expressive detailed faces", was bei den Silhouetten-Karten (z. B. JD-14, JD-21, JD-23) inhaltlich
nicht ganz passt. Im Dateikopf vermerkt, falls Bing dort seltsame Ergebnisse liefert. Damit ist JD
komplett auf dem neuen Stil, wie alle anderen Decks.

Anjas Nebenbemerkung aus der nachgereichten Notiz ("ADHS und DaZ/Migration als weitere
Besonderheiten-Zielgruppen") ist bereits durch die bestehende Grundsatzentscheidung abgedeckt (zehn
Decks insgesamt: JD, KD, FS, AT, ADHS, DAZ GS, DAZ Sek I, EL, LK, TR, siehe oben) – keine neue
Entscheidung nötig, nur zur Bestätigung notiert.

**Status:** Alle Prompt-Texte sind jetzt auf den neuen Stil aktualisiert und bereit. Das eigentliche
Neugenerieren der Bilder und Austauschen in `bilder/xx/` macht Anja am Schluss (nach eigener
Ansage) für JD/KD/EL/LK, nicht jetzt sofort – die Kartenpipelines bleiben unverändert nutzbar,
sobald neue Bilder mit denselben Dateinamen abgelegt werden.

**TR-Deck fertig (26.07.2026) – erstes Deck komplett im neuen Bildstil.** Da TR noch nie generierte
Bilder hatte, direkt mit dem neuen Stil-Zusatz gestartet (kein Nachbessern nötig). Alle 29 Bilder
von Anja mit Bing generiert, lagen zunächst direkt in `bilder/` statt `bilder/tr/` – Dateien dorthin
kopiert (nicht verschoben, Originale in `bilder/` bewusst unangetastet gelassen, Datei-Sicherheits-
Policy). Stichprobe (TR-01, TR-16, TR-29) geprüft: deutlich moderner, ausdrucksstärkere Gesichter,
kein körniger Look mehr – klare Verbesserung gegenüber dem alten Stil. `build_all_cards_tr.py` +
`build_pdf_tr.py` ausgeführt: 29 Karten, kein Overflow-Warning, Gesamt-PDF
`KLARTEXT_TR-Deck_komplett.pdf` (66 Seiten) fertig, visuell stichprobengeprüft (Cover, Karte 01,
Karte 29 – sauber), in klartext-app abgelegt. **Damit ist TR jetzt production-ready, so wie JD, KD,
EL und LK.** Alle fünf Kartendecks (JD 40, KD 30, EL 51, LK 51, TR 29 = 201 Karten insgesamt) sind
jetzt vollständig produziert. Offen bleibt nur noch die Bildstil-Überarbeitung für JD/KD/EL/LK
(neue Prompts liegen bereit, Bilder noch nicht neu generiert).

## Aktuelle Priorität
→ **Kartenserie vermarkten** (von Anja bestätigt, 23.07.2026). Nächster Schritt wird konkretisiert. Offene Zusatzfrage: physisch/digital-Strategie (siehe Strang 5).

## Strang 8 · Inklusions-Kalibrierung (Standing-Regel, 29.07.2026)

Anja: Rollstuhl kam bisher nur 2–3x über alle Sets vor, andere Behinderungen (blind, gehörlos,
Down-Syndrom, Autismus, ADHS) gar nicht. Ab sofort Standing-Regel für alle künftigen Deck-Bildprompts
(analog zur Diversitäts-Kalibrierung): pro Deck ca. 15–25% der Karten mit sichtbarer Behinderung,
kompetent/normal mitmachend dargestellt (nicht als "Problem"-Situation), nicht in jedem Bild, um
Quoten-Charakter zu vermeiden. Kategorien-Rotation: Rollstuhl, blind/Langstock, gehörlos/Gebärdensprache,
Down-Syndrom, Autismus-codiert (Kopfhörer, Rückzug als normal), ADHS-codiert (Fidget-Tool, energetisch-
positiv statt störend). Bereits umgesetzt: OGS-Deck (6/28 Karten: OGS-04, 08, 14, 17, 21, 23), Kita-Deck
(3/7 Karten: KITA-01, 03, 06). Noch offen: retroaktiv für ältere Decks nicht vorgesehen (Bilder bereits
final generiert/genutzt), gilt aber für alle noch nicht bebilderten/geplanten Decks (Fallberatung-
Rollenkarten, KFA, künftige Linien).

## Strang 9 · Insel-Set – neue Produktlinie, Integration in Barometer/kLAR (29.07.2026)

Anjas Idee: physisches Insel-Set für Raumstrukturierung (Regel/Ruhe/Arbeit/Bewegung/Kreativ/Gespräch/
Emotion/Material). Pädagogisch abgesichert (Zones of Regulation, Kuypers 2011; Calming Corners/PBIS).
Farbkollision mit Barometer gefunden (v.a. Bewegungs-Insel=Rot kollidierte mit Barometer-Rot=Krise) und
gelöst: Inseln bekommen eigene kühle Farbfamilie (Türkis/Blau/Petrol/Aquamarin/Lila/Indigo/Magenta/
Taupe), Barometer-Farben bleiben exklusiv für Zustände. Funktionale Integration ausgearbeitet: Insel =
physischer Ort für Barometer-Zustand + kLAR-Schritt (Details in INSEL-Set_Konzept_und_Barometer-
Integration.md). Vorschlag: als "Element 10" ins Systemelemente-Modul (M0-00) aufnehmen. Jugend-Zonen-
Variante (Sek I/II) im gleichen Dokument skizziert, noch nicht ausgearbeitet. Noch offen: Anjas Freigabe
der neuen Farben, Entscheidung zu App-Integration, Symbole/Bildprompts falls Kartenoptik gewünscht.

## Strang 9 (Fortsetzung) · Eltern-Insel-Set (29.07.2026)

Anjas zweites Insel-Konzept (8 Inseln fürs Zuhause) ergänzt, Rev. 2 in
INSEL-Set_Konzept_und_Barometer-Integration.md. Bestätigt: Eltern haben bereits eigenes
Barometer-Poster (EL_DL_Barometer_Poster.html), und "kLAR zuhause" ist bereits als Block im
EL-Home-Management-Konzept vorgesehen – Eltern-Insel-Set ist der physische Baustein dazu, kein
Zusatzkonstrukt. Zwei echte Neuerungen übernommen: Übergangs-Insel (Morgen/Abend), Geschwister-
Konflikt-Insel. Farben mit Schul-Set abgeglichen (gleicher Inseltyp = gleiche Farbe, Wiedererkennung
für Kinder zwischen Kita/Schule und Zuhause). Produktchance: Bundle mit künftiger EL-Home-Management-
Kartenlinie, sobald deren Pipeline gebaut wird.

## Strang 9 (Fortsetzung) · Insel-Bildprompts fertig (29.07.2026)

Insel_Bildprompts.md erstellt: nur 10 Badge-Bilder nötig für 16 Insel-Slots (Schul- + Eltern-Set teilen
sich 6 identische Symbole/Farben). Rundes Badge-Format statt Szenenbild, Brainy auf jedem Badge dabei.
Wartet auf Bilder in bilder/insel/.

## Strang 9 (Fortsetzung) · Eltern-Mini-Handbuch (29.07.2026)

Eltern-Insel-Mini-Handbuch.md erstellt aus Anjas pädagogischem Konzept, Quellen geprüft: 5/6 sauber
zitierfähig (Mesibov/Shea/Schopler 2005, Hodgdon 1995, Dunn 1997, Fiese et al. 2002, Brackett & Rivers
2014), Zimmer 2010 "Selbstregulation im Kindesalter" nicht im exakten Titel bestätigt – vor Druck
gegenprüfen. Offen: analoges Mini-Handbuch fürs Schul-Set (Kuypers 2011/Calming Corners, bereits am
29.07. recherchiert) noch zu schreiben.

## Strang 9 (Fortsetzung) · INGRA- + LK-Mini-Handbuch (29.07.2026)

Zwei weitere Mini-Handbücher zum Schul-Insel-Set erstellt, bewusst getrennt statt ein gemeinsames
"Schul-Handbuch": INGRA-Insel-Mini-Handbuch.md (Quellenbasis Porges 2011/bereits bestätigt, TEACCH,
Siegel/Window of Tolerance – wie in Handlungskarten allgemein INGRA –, plus Kuypers 2011/Calming
Corners; direkt an Barometer/kLAR-Tabelle angebunden) und LK-Insel-Mini-Handbuch.md (Quellenbasis
Marzano, Kounin/Withitness, Sprick/CHAMPS, PBIS – wie in LK-Classroom-Management; Fokus auf
Unterrichtsfluss nicht unterbrechen). Damit jetzt 3 Insel-Mini-Handbücher: Eltern, INGRA, LK – je
eigene fachliche Grundlage, gleiche physische Inseln.

## Strang 9 (Fortsetzung) · Format-Entscheidung: Selbstausdruck statt Aufkleber (29.07.2026)

Anja: Standardformat ist Selbstausdruck + Laminieren (für INGRA über Schuldrucker), Befestigung per
doppelseitigem Klebeband oder Lochung+Aufhängen. Vinyl-Aufkleber nur auf Auftrag als Zusatzoption.
Mini-Anleitung dazu in allen drei Handbüchern (Eltern/INGRA/LK) ergänzt, Produktstruktur-Abschnitt in
INSEL-Set_Konzept_und_Barometer-Integration.md aktualisiert.

**Offen (Business, nicht durch mich klärbar):** Aufkleber-Option hängt daran, ob Anja dafür in Vorkasse
gehen müsste – noch zu prüfen (Anbieter/Mindestbestellmenge/Zahlungsmodell). Erst nach Klärung als
feste Zusatzoption kommunizieren.

## Strang 10 · Scope-Entscheidung: OGS ja, Kita gestrichen (29.07.2026)

Anja: Kita ist nicht ihr Kernbereich (andere Ausbildung/Finanzierung/Konkurrenz als Schulbegleitung),
OGS dagegen gleicher Ort/Träger-Kreis wie INGRA. Entscheidung: OGS-Deck wird fertig gebaut (28 Karten,
Prompts bereits fertig inkl. Brainy + Diversitäts-/Inklusions-Kalibrierung), Kita-Konzept wird
zurückgestellt/gestrichen – Datei bleibt bestehen (Kita_Kartenkonzept_und_Prompts.md), keine Löschung,
nur nicht weiterverfolgt. Nächster Schritt OGS: Anja generiert die 28 Bilder extern anhand der fertigen
Prompts (OGS_Kartenkonzept_und_Prompts.md), legt sie in bilder/ogs/ ab – dann Pipeline bauen (analog TK:
build_card_ogs.py / build_all_cards_ogs.py / build_booklet_ogs.py / build_pdf_ogs.py).

## Strang 10 (Fortsetzung) · OGS-Basis-Deck fertig (29.07.2026)

Alle 28 Bilder von Anja generiert und in bilder/ogs/ abgelegt. Fehlende Inhalte nachgeliefert:
Farbe (Limette #8BC34A, RGB-Distanz min. 77.2 gegen alle bestehenden Deck-/Insel-Farben), 28
Rückseitentexte (Anleitung + 2 Impulsfragen + 3. systemische Frage + Tipp für dich, Format wie
LK-Basis/EL-Basis), Quellen (Tuckman 1965 + Deci&Ryan + Hodgdon 1995 bestätigt, Wulf&Zirfas 2004,
Jefferys-Duden, Nolting, Ahnert, Griebel&Niesel 2004 vorgeschlagen/bitte gegenprüfen). Pipeline gebaut
(build_card_ogs.py, build_all_cards_ogs.py, build_booklet_ogs.py, build_pdf_ogs.py), alle 28 Karten
gerendert, PDF (61 Seiten, kein ENTWURF-Suffix da alle Bilder vorhanden) visuell geprüft (Cover,
Anleitung, Quellen, 2 Kartenmuster) – fehlerfrei, Brainy gut integriert, kein Überlauf.
KLARTEXT_OGS-Basis-Deck_komplett.pdf + karten/ogs/ nach klartext-app kopiert. Kita bleibt wie
entschieden zurückgestellt (Bilder von Anja zwar generiert, aber keine Pipeline gebaut).

## Strang 9 (Abschluss) · Insel-Set komplett fertig (29.07.2026)

Alle 10 Badge-Bilder von Anja generiert (bilder/insel/). Pipeline gebaut: build_card_insel.py
(Badge-Kartenformat statt Reflexionsformat: Vorderseite großes rundes Badge+Name, Rückseite
Zweck/Ort+Regeln+Nutzen), build_all_cards_insel.py (16 Karten: 8 Schul-Set + 8 Eltern-Set, 6 Badges
geteilt), build_booklet_insel.py (3x 2-seitiges Handbuch, kondensiert aus den 3 Mini-Handbüchern),
build_pdf_insel.py (3 finale PDFs mit Cover). Alle 16 Karten + 3 PDFs gerendert und visuell geprüft
(Cover, Handbuch-Seiten, Kartenmuster Ruhe-Insel + Übergangs-Insel) – fehlerfrei. Ergebnis: drei
eigenständige, druckfertige Produkte:
- KLARTEXT_Insel-Set_Eltern.pdf (19 Seiten)
- KLARTEXT_Insel-Set_Schule_INGRA.pdf (19 Seiten)
- KLARTEXT_Insel-Set_Schule_LK.pdf (19 Seiten, gleicher Kartensatz wie INGRA, eigenes Handbuch)
Alle nach klartext-app kopiert (PDFs + karten/insel_schule/ + karten/insel_eltern/).

## Strang 9 (Nachtrag) · Großformat-Raummarkierungen ergänzt (29.07.2026)

Anja: Die A6-Begleitkarten sind zu klein, um im Raum von Kindern bemerkt zu werden. Richtig erkannt –
das war ohnehin ein anderer Zweck (Regeln/Nutzen fürs Handbuch). Neues drittes Element ergänzt:
großformatige DIN-A4-Raummarkierung pro Insel (build_marker_insel.py + build_all_markers_insel.py),
volle Farbfläche, riesiges Badge-Symbol, großer Name, automatische Textfarbe je nach Hintergrund-
Helligkeit für Kontrast. 16 Markierungen gerendert (8 Schule + 8 Eltern), 2 PDFs:
- KLARTEXT_Insel-Set_Raummarkierungen_Schule.pdf (8 Seiten)
- KLARTEXT_Insel-Set_Raummarkierungen_Eltern.pdf (8 Seiten)
Visuell geprüft (Ruhe-, Übergangs-, Bewegungs-Insel) – fehlerfrei. Damit hat das Insel-Set jetzt drei
Komponenten pro Insel: große Raummarkierung (A4, zum Erkennen), kleine Begleitkarte (A6, zum
Nachlesen von Regeln/Nutzen), Handbuch (das Warum). Alle Dateien nach klartext-app kopiert.

## Strang 11 · Zonen-Set für Jugendliche (Sek I/II) – Konzept fertig (29.07.2026)

Anja: "wo sind unsere jugendlichen geblieben???? die ohne brainy" – zu Recht, das war seit der
Insel-Set-Konzeption nur als ein Absatz angerissen ("noch nicht ausgearbeitet") und dann in der
Umsetzung von OGS/Insel-Set liegen geblieben. Jetzt vollständig ausgearbeitet:
`Jugend-Zonen-Set_Konzept_und_Prompts.md`. Kernentscheidungen: 4 statt 8 Zonen (Rückzugs-, Fokus-,
Klärungs-, Gesprächs-Zone), **kein Brainy** (bestätigt Anjas Vorgabe), gedeckte "erwachsenere"
Farbpalette statt Insel-Kräftig-Töne (Zone-Moos/Graphit/Rost/Schiefer, alle RGB-distanzgeprüft gegen
sämtliche bestehenden Deck-/Insel-Farben, min. Abstand 37,6–50,5), semi-realistischer Editorial-
Illustrationsstil statt Kinderbuch-Stil. Produktlogik bewusst umgekehrt zum Kinder-Set: Raummarkierung
klein/dezent statt groß/auffällig (Jugendliche wollen NICHT auffallen), dafür neues Kernelement
Token-Karten (4 pro Person, unauffällige Selbstwahl statt sichtbares Hingehen). Quellen: Kuypers 2011
(Zones of Regulation, bereits verifiziert, deckt explizit auch Sek-I ab), Siegel 1999 (Window of
Tolerance, verifiziert), Deci & Ryan (Selbstbestimmung, bereits für OGS verwendet), Reeve 2006
(autonomiefördernde Klassenführung, **vorgeschlagen, bitte gegenprüfen** – noch nicht verifiziert).
4 Bildprompts fertig (kein Brainy, semi-realistisch, je 276–292 Zeichen, deutlich unter dem
480-Limit), Diversität/Inklusion über die 4 Bilder verteilt statt in jedem einzelnen. Kein
Eltern-Pendant vorgesehen (Zielgruppe Schulkontext). Offen: Anja bestätigt Zonenliste/Token-Mechanismus,
dann Bilder generieren lassen, danach Pipeline (Karten + kleine Markierung + LK/INGRA-Handbuch) bauen
– gleiches Muster wie bei OGS/Insel-Set.

Bilddateinamen mitgeteilt: Ordner `bilder/zonen/`, Dateien `ZONE-RUECKZUG.jpg`, `ZONE-FOKUS.jpg`,
`ZONE-KLAERUNG.jpg`, `ZONE-GESPRAECH.jpg`. Eltern-Variante für Jugendliche bestätigt (Anja: "ja klar")
– braucht keine neuen Bilder, nur kontextangepasste Zweck-/Regel-Texte (gleiches Muster wie Insel-Set
Schule/Eltern), wird beim Pipeline-Bau ergänzt.

## Strang 9 (Abschluss 2) · Zonen-Set Jugendliche fertig gebaut (30.07.2026)

Alle 4 Bilder von Anja generiert und in `bilder/zonen/` abgelegt. Pipeline gebaut, drei
Komponenten analog Insel-Set, aber bewusst umgekehrt skaliert (klein/dezent statt groß/auffällig):

- `build_all_cards_zonen.py` – Begleitkarten (A6, Front/Back), Renderer 1:1 aus
  `build_card_insel.py` wiederverwendet (vollständig generisch, keine Insel-spezifischen Texte im
  Code), nur mit den 4 Zonen-Farben und "ZONEN-SET" als Label. 8 Karten (4 Schule + 4 Eltern).
- `build_token_zonen.py` + `build_all_tokens_zonen.py` – neues Kernstück: Token-Karten im
  Scheckkartenformat (CR80, 85,6×54mm), 4 A4-Sheets à 10 Karten (2×5-Raster) zum Ausschneiden/
  Laminieren, ergibt komplette 4-Karten-Sets für bis zu 10 Jugendliche.
- `build_booklet_zonen.py` – ein gemeinsames Handbuch für LK & INGRA (anders als beim Kinder-Set
  bewusst nicht getrennt, da beide Rollen dasselbe Token-System im selben Raum nutzen) + ein
  Eltern-Handbuch. Quellen: Kuypers 2011, Siegel 1999 (beide bereits bestätigt), Deci & Ryan
  (etabliert), Reeve 2006 (vorgeschlagen, bitte gegenprüfen).
- `build_pdf_zonen.py` – 2 finale PDFs.

Alle Karten + PDFs gerendert und visuell geprüft (Cover, beide Handbuch-Seiten, Kartenmuster
Rückzugs-Zone, Token-Sheet) – fehlerfrei, Bildstil trifft "semi-realistisch, kein Brainy" genau.
Ergebnis:
- KLARTEXT_Zonen-Set_Schule.pdf (15 Seiten: Cover+Handbuch+4 Karten+4 Token-Sheets)
- KLARTEXT_Zonen-Set_Eltern.pdf (11 Seiten: Cover+Handbuch+4 Karten)
- KLARTEXT_Zonen-Set_Token-Karten.pdf (Token-Sheets separat, falls Nachdruck nötig)

Alle Dateien nach klartext-app kopiert (PDFs + karten/zonen_schule/ + karten/zonen_eltern/ +
karten/zonen_token/ + alle Pipeline-Skripte).

## Strang 12 · Werkstattarbeit-Frage geklärt, JD-Zusatzblock statt neue Linie (30.07.2026)

Anja fragte, ob "Werkstattarbeit" ins Programm passt. Zwei Lesarten geklärt: (a) zusätzliche Zone im
Jugend-Zonen-Set – abgelehnt/nicht das Gemeinte; (b) eigene Zielgruppe Werkstattkontext – hier weiter
unterschieden zwischen Berufsvorbereitung für Jugendliche (Sek I/II, bleibt im bestehenden Feld) und
WfbM/Erwachsene (eigenes Fachfeld, andere Kostenträger/Fachkräfte, wie schon bei Kita). Anjas
Entscheidung: **nur Berufsvorbereitung, WfbM erstmal weglassen.**

Umsetzung: kein neues Deck, sondern **Block 11 – Berufsvorbereitung & erste Arbeitswelt** als
Zusatzblock im bestehenden JD-Deck (40 → 44 Karten), analog zum EL-/LK-Zusatzblock-Muster. Begründung:
gleiche Zielgruppe, gleiches Kartenformat, Block 2 "Zukunftsdruck" behandelt Berufswahl bereits, aber
nur emotional – Block 11 ergänzt konkrete Praxis-Situationen (Praktikum, Werkstatttag, Feedback vom
Anleiter statt von Lehrkraft). 4 Karten entworfen (JD-41–44: Erstes Praktikum, Wenn die Arbeit nicht
wie erwartet ist, Kritik bei der Arbeit annehmen, Was ich wirklich gut kann) mit Titel/Anleitung für
die INGRA/2 Impulsfragen, in `JD_Kartenkonzept_Uebersicht.md` und `JD_Tipps_fuer_die_INGRA_Entwurf.md`
ergänzt (Status: Entwurf, bitte gegenlesen – gleiche Konvention wie beim Rest des JD-Decks). 4
Bildprompts in `JD_Bildprompts.md` ergänzt, gleicher Stil wie JD-25–40 (konkrete realistische Szenen,
kein Brainy im Bild), 1 Karte mit Inklusionsmerkmal (Hörgerät, JD-43). Offen: Anja liest gegen, dann
Bilder generieren lassen und in bestehende JD-Pipeline aufnehmen.

## Strang 12 (Abschluss) · JD-Deck auf 44 Karten erweitert (30.07.2026)

Anja hat die 4 Bilder (JD-41-44) generiert, lagen bereits in bilder/jd/. Pipeline erweitert statt
neu gebaut: build_all_cards_jd.py um die 4 Karten aus Block 11 ergaenzt (CARDS-Dict + total von 40
auf 44), build_pdf_jd.py angepasst (Titelseite "44 Impulskarten", Themenbereiche-Liste um
"Berufsvorbereitung" ergaenzt, Spalten-Layout dafuer von 2x5 auf 2x6 erweitert - ursprnglich 3x4
versucht, aber "Beziehung zu Erwachsenen" kollidierte mit der Nachbarspalte, daher zurueck auf 2
Spalten mit mehr Zeilen), Rendering-Range auf 1-44 erweitert. Alle 44 Karten neu gerendert (fehlerfrei),
Gesamt-PDF neu gebaut (95 Seiten). Visuell geprueft: Cover (Themenraster korrekt, keine Ueberlappung
mehr), JD-41 Vorder-/Rueckseite, JD-44 Vorderseite - alle fehlerfrei, Nummerierung "41/44" bzw. "44/44"
korrekt. KLARTEXT_JD-Deck_komplett.pdf in klartext-app ueberschrieben (Datei wird bei jedem Rebuild
ersetzt, nicht umbenannt/geloescht - kein Verstoss gegen die Dateisicherheits-Konvention).

## Strang 13 · Fröhlich-Gildhoff/Rönnau-Böse-Zitat korrigiert (30.07.2026)

Anja hat das JD-Quellenverzeichnis extern gegengeprueft (Word-Dokument "Das Growth Mindset").
Ergebnis: alle Eintraege korrekt bis auf Froehlich-Gildhoff/Roennau-Boese - Jahr/Auflage fehlten
noch (Platzhalter "Auflage/Jahr vor Veroeffentlichung pruefen"). Korrektur uebernommen: 6. Auflage,
2022, Ernst Reinhardt/UTB (ISBN 978-3-8252-5851-1). Fix in build_booklet.py (QUELLEN_EINORDNUNG,
wird von JD-Deck genutzt), JD-Deck-PDF neu gebaut und Quellen-Seite 2/2 visuell geprueft - Zitat
jetzt vollstaendig. Die drei "bitte gegenpruefen"-Quellen (de Shazer 1988, Selvini Palazzoli et al.
1980, von Schlippe & Schweitzer 2012) wurden in derselben Gegenpruefung ebenfalls als korrekt
bestaetigt, bleiben aber als "vorgeschlagen" markiert, da sie noch nicht formal ins zentrale
KLARTEXT-Quellenregister uebernommen sind (separate Frage von der bibliografischen Korrektheit).

## Strang 14 · JD-Zusatzblock Beziehungen & Verliebtsein: Konzept (JD-45-48, 30.07.2026)

Anja fragte nach Liebeskummer als JD-Thema (Anstoss durch extern generierten Analyse-Text mit
Uebertragungsvorschlaegen auf bestehende Karten wie JD-04/18/24/32). Entschieden: neuer 4er-Block
statt Einzelkarte, um das bestehende Blockmuster (bisher 11 Bloecke a 4 Karten) nicht zu brechen.

Block 12 - Beziehungen & Verliebtsein: JD-45 Wenn eine Beziehung endet (Liebeskummer, Kernthema),
JD-46 Verliebt sein zum ersten Mal, JD-47 Eifersucht die alles auffrisst, JD-48 Wenn die Gefuehle
nicht erwidert werden. Texte eigenstaendig formuliert (nicht vom externen Analyse-Text uebernommen,
nur thematisch inspiriert), im etablierten JD-Format (Titel/Anleitung/2 Fragen/Tipp fuer die INGRA).
In JD_Kartenkonzept_Uebersicht.md und JD_Tipps_fuer_die_INGRA_Entwurf.md ergaenzt (Status: Entwurf,
bitte gegenlesen). 4 Bildprompts in JD_Bildprompts.md ergaenzt, gleicher Stil wie JD-25-44, kein
Brainy, 1 Karte mit Diversitaetsmerkmal (Hijab, JD-47). Offen: Anja liest gegen, dann Bilder
generieren lassen und in JD-Pipeline aufnehmen (Deck waechst dann auf 48 Karten).

## Strang 14 (Abschluss) · JD-Deck auf 48 Karten erweitert (30.07.2026)

Bilder JD-45-48 von Anja generiert, lagen in bilder/jd/. Pipeline erweitert wie bei Block 11:
build_all_cards_jd.py (CARDS-Dict + total=48), build_pdf_jd.py (Titelseite "48 Impulskarten",
Themenliste um "Beziehungen & Verliebtsein" ergaenzt - 12 Themen passen exakt ins bestehende
2x6-Raster, kein Layout-Fix noetig diesmal), Rendering-Range 1-48. Alle 48 Karten gerendert
(fehlerfrei), Gesamt-PDF neu gebaut (103 Seiten). Visuell geprueft: Cover (Themenraster korrekt),
JD-45 Vorderseite, JD-47 Vorder-/Rueckseite - fehlerfrei, Nummerierung "45/48" bzw. "47/48" korrekt.
KLARTEXT_JD-Deck_komplett.pdf in klartext-app ueberschrieben.

## Strang 15 · JD-Deck: Redaktionsfehler behoben + Sicherheitshinweis ergaenzt (30.07.2026)

Anja hat eine externe Analyse des JD-Decks geteilt (inhaltliche Erweiterungsvorschlaege +
Redaktionspruefung). Zwei echte Befunde direkt behoben:
1. Redaktionsfehler bestaetigt: Anleitung Seite 1 sagte noch "40 Coaching-Impulskarten" und "die
   zehn Themenbloecke", obwohl das Deck laengst bei 48 Karten/12 Bloecken war (Text war beim
   Block-11/12-Ausbau nicht mitgezogen worden). Korrigiert in build_booklet.py, PDF neu gebaut,
   visuell geprueft.
2. JD-48 (Wenn die Gefuehle nicht erwidert werden) um denselben Sicherheitshinweis ergaenzt, den
   andere sensible Karten schon haben (JD-33, JD-36, JD-45): "Bei Anzeichen von Rueckzug oder
   starker Verzweiflung nicht allein lassen - Fachperson einbeziehen." Kein neuer GRENZEN-WICHTIG-
   Kasten pro Karte noetig - das Muster "Sicherheitshinweis im Tipp fuer die INGRA" deckt das
   bereits ab, war bei JD-48 nur noch nicht gesetzt.

Inhaltliche Erweiterungsvorschlaege aus der Analyse (Peer-Beziehungen als Ressource, Partnerschaft/
sexuelle Identitaet, Life Skills/Adulting, Koerperbild) noch nicht umgesetzt - dazu Anja um
Priorisierung gebeten, da nicht alle gleich gut ins JD-Format passen (Life Skills z.B. eher
praktisch/organisatorisch als reflexiv) und das Deck in dieser Session bereits von 40 auf 48
Karten gewachsen ist.

## Strang 16 · JD-Zusatzblock Freundschaft & Zugehoerigkeit: Konzept (JD-49-52, 30.07.2026)

Nach Rollen-Abwaegung (Strang 15) entschieden: von den 4 vorgeschlagenen Erweiterungsthemen passt
nur "Positive Peer-Beziehungen" sauber in den Schulbegleitungs-Rahmen. Koerperbild, sexuelle
Identitaet und Life Skills bewusst nicht aufgenommen (Rollen-/Formatgrenzen).

Block 13 - Freundschaft & Zugehoerigkeit: JD-49 Was eine gute Freundschaft ausmacht (Wertschaetzung/
Gegenpol zu den Konfliktkarten), JD-50 Fuer jemanden da sein ohne sich zu verlieren (Balance/
Grenzen), JD-51 Dazugehoeren ohne sich zu verbiegen (Gruppenperspektive, ergaenzt JD-26), JD-52
Wenn Freundschaften sich veraendern (Normalisierung von Wandel). In JD_Kartenkonzept_Uebersicht.md
und JD_Tipps_fuer_die_INGRA_Entwurf.md ergaenzt (Status: Entwurf, bitte gegenlesen). 4 Bildprompts
in JD_Bildprompts.md ergaenzt, gleicher Stil wie JD-25-48, kein Brainy, 1 Karte mit
Inklusionsmerkmal (Rollstuhl, JD-49). Offen: Anja liest gegen, dann Bilder generieren lassen und
in JD-Pipeline aufnehmen (Deck waechst dann auf 52 Karten).

## Strang 16 (Abschluss) · JD-Deck auf 52 Karten erweitert (30.07.2026)

Bilder JD-49-52 von Anja generiert, lagen in bilder/jd/. Pipeline erweitert: build_all_cards_jd.py
(CARDS-Dict + total=52), build_pdf_jd.py (Titelseite "52 Impulskarten", Themenliste um "Freundschaft
& Zugehoerigkeit" ergaenzt - 13 Themen brauchten neues 2x7-Raster statt 2x6, Spaltenbreite/Zeilenhoehe
leicht angepasst), Rendering-Range 1-52. build_booklet.py (Anleitung-Text "52 Karten"/"dreizehn
Themenbloecke", damit kein erneuter Redaktionsfehler wie in Strang 15). Alle 52 Karten gerendert
(fehlerfrei), Gesamt-PDF neu gebaut (111 Seiten). Visuell geprueft: Cover (Themenraster korrekt),
Anleitung Seite 1 (Zahlen korrekt), JD-49 Vorderseite, JD-51 Vorder-/Rueckseite - alle fehlerfrei.
KLARTEXT_JD-Deck_komplett.pdf in klartext-app ueberschrieben. Damit JD-Deck-Erweiterung fuer diese
Session abgeschlossen: 40 -> 52 Karten (Berufsvorbereitung, Beziehungen & Verliebtsein, Freundschaft
& Zugehoerigkeit), Koerperbild/sexuelle Identitaet/Life Skills bewusst nicht aufgenommen.

## Strang 17 · KD-Zusatzblock Familie & neue Situationen: Konzept (KD-31-35, 30.07.2026)

Klarstellung zu einer eigenen Fehleinschaetzung: Anja fragte zu Recht nach, ob Barometer/kLAR nicht
schon fuer die Inseln entschieden waren. Nachgeprueft in build_booklet_kd.py - Korrektur meiner
vorherigen Aussage: das KD-Deck referenziert Barometer + kLAR sehr wohl, nur nicht auf den 30
regulaeren Reflexionskarten selbst, sondern (a) auf einer eigenen Bonus-Barometer-Karte
(build_bonuskarte_kd.py, physischer Bestandteil des Decks) und (b) in einer vollen
"Die KLARTEXT-Methodik"-Seite im Handbuch (5 Barometer-Zustaende + 4 kLAR-Schritte, fuer die
Fachkraft). Exakt dasselbe Muster wie beim Insel-Set: das einzelne Objekt (Karte/Markierung) bleibt
eigenstaendig lesbar, die System-Integration lebt im Begleitmaterial. Kein Widerspruch, sondern
durchgaengiges Prinzip im ganzen Projekt.

Block 7 - Familie & neue Situationen: 5 Karten (KD-Bloecke haben 5 statt 4 Karten wie JD, Muster
gehalten). KD-31 Wenn sich zu Hause etwas aendert (Trennung, sehr behutsam), KD-32 Zwischen zwei
Zuhause (Wechselmodell), KD-33 Neue Menschen in der Familie (Patchwork), KD-34 Die grosse Schule
kommt (Uebergang weiterfuehrende Schule, eigenstaendiges Thema, nicht identisch mit JD-05
Zukunftsdruck), KD-35 Wenn im Internet etwas gruselig war (erste digitale Erlebnisse). Bewusst
deutlich sanfter formuliert als die JD-Pendants (Grundschulkinder, nicht Jugendliche). Care-Aufgaben/
Parentifizierung bewusst NICHT als eigene Karte umgesetzt - zu klinisch fuer Kind-Selbstreflexion,
bleibt Glossar-Sensibilisierung fuer die INGRA. In KD_Kartenkonzept_Uebersicht.md und
KD_Tipps_fuer_die_INGRA_Entwurf.md ergaenzt (Status: Entwurf, bitte gegenlesen). 5 Bing-fertige
Bildprompts in KD_Brainy_Prompts.md ergaenzt (gleiches Format wie die 30 bestehenden, alle
≤480 Zeichen, 1 mit Diversitaetsmerkmal). Offen: Anja liest gegen, dann Bilder generieren lassen
und in KD-Pipeline aufnehmen (Deck waechst auf 35 Karten).

## Strang 17 (Abschluss) · KD-Deck auf 35 Karten erweitert (30.07.2026)

Bilder KD-31-35 von Anja generiert, lagen in bilder/kd/. Pipeline erweitert: build_all_cards_kd.py
(CARDS-Dict + total=35), build_pdf_kd.py (Titelseite "35 Karten", Themenliste um "Familie & neue
Situationen" ergaenzt, Status-Box aktualisiert, Rendering-Range 1-35), build_booklet_kd.py
(Anleitung-Text "35 Karten"/"sieben Themenbloecke" - vorsorglich gleich mitkorrigiert, um densel
ben Redaktionsfehler wie beim JD-Deck (Strang 15) zu vermeiden). Alle 35 Karten + Bonus-Barometer-
Karte gerendert (fehlerfrei), Gesamt-PDF neu gebaut (79 Seiten). Visuell geprueft: Cover
(Themenraster korrekt, 7 Eintraege ohne Ueberlappung), Anleitung Seite 1 (Zahlen korrekt), KD-31
Vorderseite, KD-34 Vorder-/Rueckseite - alle fehlerfrei. KLARTEXT_KD-Deck_komplett.pdf in
klartext-app ueberschrieben. Damit KD-Deck-Erweiterung abgeschlossen: 30 -> 35 Karten (Familie im
Wandel, Schulübergang, erste digitale Erlebnisse), Care-Aufgaben/Parentifizierung bewusst nicht
als eigene Karte umgesetzt.

## Strang 18 · Barometer/kLAR-Bestandsaufnahme, Grau erweitert, Krisendeck als 2. Handlungskarten-Deck (30.07.2026)

**Ausgangsfrage (Anja):** Wo taucht Barometer/kLAR ueberall auf, wo fehlt es, und sollen die
Feuerwehrkarten (FK-01-08) in TK-Deck integriert oder als eigenes Krisendeck gebaut werden - im
Sinne einer "Handlungskarten-Serie wie in der App".

**Bestandsaufnahme (per Subagent, alle Decks geprueft):** Volle Integration (Bonus-Karte + Methodik-
Seite) bei KD, FS, Insel-Set, TK. Auf Karte eingebettet bei AT (AT-20). Bewusst ausgeschlossen bei
EL, LK, TR, OGS ("Karte muss eigenstaendig funktionieren"). Kein Bezug bei JD, DaZ-GS, DaZ-Sek1 und
**Zonen-Set** (Luecke gegenueber Insel-Set) - Zonen-Set-Luecke von Anja bestaetigt und geschlossen
(siehe unten).

**Grau-Definition erweitert:** Anja wies darauf hin, dass Grau nicht nur "erschoepft/ausgebrannt"
bedeutet, sondern auch "ich weiss nicht was ich brauche" (Orientierungslosigkeit). In M0-00_System
elemente.html (Kernquelle) an beiden Stellen erweitert, konsistent nachgezogen in build_booklet_kd.py
(BAROMETER-Liste), build_booklet_insel.py (extra_text), INSEL-Set_Konzept_und_Barometer-Integration.md
(2 Stellen). PDFs neu gebaut (KD-Deck 79 S., Insel-Set Eltern/Schule-INGRA/Schule-LK je 19 S.),
visuell geprueft, kein Ueberlauf. Ergaenzend im TK-Booklet (Quellen-Seite 2) ein neuer Absatz
"Barometer-Farbmarkierung in der Handlungskarten-Serie" eingefuegt, der erklaert, warum Grau auf
keiner Handlungskarte erscheint (kein Werkzeug, sondern Beobachten + TK-Meldung).

**Nebenbefund korrigiert:** TK-09 (Krisenprotokoll) verwies auf "FK-01-07" statt korrekt FK-01-08
(sowohl im Booklet-Text als auch im Quelle-Feld der Karte selbst) - Zaehlfehler behoben, TK-Karten
neu gerendert, TK-PDF neu gebaut (43 Seiten). Separat dokumentiert: die Live-App-Seiten FK-01-07
selbst sagen intern noch "Feuerwehrkarte X von 7" (FK-08 fehlt in der Zaehlung) - nur an Anja
gemeldet, nicht angefasst (Live-App-Aenderung nicht ohne Rueckfrage).

**Zonen-Set-Handbuch ergaenzt:** build_booklet_zonen.py, schule_seite1() - neue Sektion "Einbindung
in Barometer & kLAR", analog Insel-Set, aber auf die 4 Zonen gemappt (Gruen=alle frei, Gelb=Rueckzugs-/
Fokus-Zone selbstaendig per Token, Orange=Rueckzugs-Zone/kLAR-R + Gespraechs-Zone/kLAR-K&A mit
Begleitung, Rot=kein Selbstwahl/Feuerwehr-Protokoll, Grau=Rueckzugs-Zone/nicht draengen). Nur in
schule_seite1() (Eltern-Version bewusst ohne, analog Insel-Set-Praezedenz). PDFs neu gebaut
(Zonen-Set Schule 15 S., Eltern 11 S.), visuell geprueft.

**Krisendeck (2. Handlungskarten-Deck, FK-01-08 als physisches Deck) - komplett gebaut:**
Konzept (`Krisendeck_Konzept.md`): A6-Format wie TK, Rueckseite fast 1:1 von TK uebernommen
(Situation/Sofortmassnahmen/Abgrenzung/Verweis), Vorderseite bewusst ohne Foto (Themen wie
Selbstverletzung/Fremdgefaehrdung verbieten illustrative Szenen) - stattdessen kleine, selbst
gezeichnete Linien-Icons (PIL, kein externes Bildmaterial noetig), angelehnt an die in der App
je FK-Karte bereits vergebenen Emoji-Symbole (Blitz, Mute, Puls, Warndreieck, Pflaster, Laufen,
Nebel, Vulkan) + 2-3 kurze Erkennungssignale als Schnellindex. Alle 8 Karten einheitlich Rot
(Barometer Rot), Farbkollision gegen bestehende Decks rechnerisch geprueft (naechste Nachbarfarbe
DaZ-Sek1-Bordeaux, RGB-Distanz ~92, unkritisch).

Inhalte (`Krisendeck_Kartentexte_Entwurf.md`): alle 8 Karten aus den bestehenden FK-01-08-App-Texten
gekuerzt (6 Sofortmassnahmen auf 1 Zeile verdichtet, Abgrenzung von 5-6 auf 3 Zeilen, Erkennungs
signale von 6 auf 2-3), nichts neu erfunden. FK-01 zuerst als Muster mit Anja abgestimmt, dann alle
8 nach demselben Schema. FK-04/FK-05 behalten die Meldepflicht-Hinweise (§8a SGB VIII) unveraendert.
FK-07 (Vergleichstabelle zu FK-02) und FK-08 (Meltdown-Hintergrund, urspruenglich anderes App-
Template als FK-01-06) wandern als Zusatzinhalte ins Handbuch statt auf die Karte.

Pipeline neu gebaut: `build_card_krisendeck.py` (Icon-Zeichenfunktionen + Vorder-/Rueckseiten-
Renderer, von build_card_tk.py abgeleitet), `build_all_cards_krisendeck.py` (8 Karten, alle
fehlerfrei ohne Ueberlauf-Warnung gerendert), `build_booklet_krisendeck.py` (Anleitung 2 Seiten
inkl. Kinderschutz-Warnbox "GRENZEN - WICHTIG" analog TK + Meldepflicht-Absatz, Hintergrund-Seite
mit Dissoziation-vs-Shutdown-Vergleichstabelle + Meltdown-Hintergrund, Quellen-Seite: bestaetigt
§8a SGB VIII + Notrufnummern, vorgeschlagen/zu pruefen Porges Polyvagal-Theorie), `build_pdf_
krisendeck.py` (eigenes Cover). KLARTEXT_Krisendeck_komplett.pdf: 21 Seiten (Cover + 4 Handbuch-
Seiten + 8x2 Karten), alle Stichproben visuell geprueft (Cover, FK-01 Vorder-/Rueckseite,
Hintergrund-Seite, Anleitung-Warnbox) - fehlerfrei. In klartext-app abgelegt.

Offen fuer spaeter: Werkzeugkarten-Deck (M3, 20 Karten) als drittes Handlungskarten-Deck vorgesehen,
noch nicht begonnen. M6-Mobbingmaterialien (30 Geschichtenkarten + 4 Anti-Mobbing-Vorlagen) in
eigenen, passenderen Formaten statt als Handlungskarten - ebenfalls noch nicht begonnen.

**Nachbesserung (30.07.2026):** Anja bemaengelte die handgezeichneten Icons (PIL-Primitiven) als kaum
erkennbar. Umgestellt auf Font-Awesome-Glyphen (Font bereits im System vorhanden,
fontawesome-webfont.ttf) - fa-bolt, fa-volume-off, fa-heartbeat, fa-exclamation-triangle, fa-medkit,
fa-sign-out, fa-cloud, fa-fire, passend zu den 8 FK-Themen ausgewaehlt (getestet per Rendervorschau
vor Einbau). build_card_krisendeck.py: draw_icon() vereinfacht auf zentrierten FA-Glyphen-Render statt
Custom-Formen. Alle 8 Karten neu gerendert, Krisendeck-PDF neu gebaut (21 Seiten), Stichproben
(FK-01, FK-02, FK-05, FK-06, FK-08) visuell geprueft - deutlich klarer erkennbar. In klartext-app
ueberschrieben.

## Strang 19 · Werkzeugkarten-Deck (M3) als drittes Handlungskarten-Deck (30.07.2026)

Drittes Deck der Handlungskarten-Serie, nach TK (Teamkoordination) und Krisendeck (akute
Rot-Situationen). Inhaltliche Basis: bestehendes App-Modul M3 Werkzeugkasten (M3-01 bis M3-20),
unveraendert uebernommen und nur auf Kartenlaenge gekuerzt (Content-Treuepflicht).

Struktur-Befund (vorher nicht bekannt, per Subagent-Recherche geklaert): M3 ist zweigeteilt.
M3-01-08 = 8 Situationskarten (Alltagsszenen wie "Kind kommt aufgewuehlt an", mit
Barometer-Farbbereich, 5 Schritten, Verweis auf passende Werkzeuge). M3-09-20 = 12 Werkzeugkarten
(Einzeltechniken wie Atemanker, mit "Wann einsetzen"-Chips, Kurzerklaerung, 4-6 Schritten).
Joker-Namenskollision aufgeloest: M3-13 "Joker" (Kind-zu-INGRA-Stillsignal) ist Teil dieses Decks;
das separate, umfangreichere INGRA-Lehrkraft-Joker-Konzept (M3-Joker.html) ist NICHT Teil dieses
Decks, moegliches spaeteres Zusatzkartenthema.

Farbe: Amber-Gold #B07D2A (App-Farbe direkt uebernommen), Kollisionscheck gegen alle bestehenden
Deckfarben ~42 Einheiten Abstand zu EL-Terracotta (knapp, aber andere Farbfamilie gelb vs. rot,
mit Anja abgestimmt und akzeptiert).

Musterkarten (M3-01 Situationstyp + M3-09 Werkzeugtyp) mit Anja abgestimmt ("passt so"), dann
volle Pipeline gebaut: `build_card_werkzeug.py` (ein Generator fuer beide Kartentypen ueber
`card["typ"]`-Weiche, Font-Awesome-Icons, kein neues Brainy-Bildmaterial - stattdessen Text-Caption
"Brainy: ...", analog zum tatsaechlichen TK-Deck-Stand, wo brainy_eckmarke.png nie existierte),
`build_all_cards_werkzeug.py` (20 Karten, alle fehlerfrei ohne Ueberlauf-Warnung gerendert),
`build_booklet_werkzeug.py` (Anleitung 2 Seiten: Kartentyp-Erklaerung, Joker- und
Brainy-Flow-Sonderrolle, Quellen-Seite: bestaetigt Kuypers Zones of Regulation, vorgeschlagen/zu
pruefen Brain-Gym/Dennison fuer "Liegende Acht", 5-4-3-2-1-Erdung und Lob-Sandwich ohne
Einzelquelle), `build_pdf_werkzeug.py` (eigenes Cover mit 8+12-Themenliste).

KLARTEXT_Werkzeugkarten-Deck_komplett.pdf: 44 Seiten (Cover + 3 Handbuch-Seiten + 20x2 Karten).
Stichproben visuell geprueft (Cover, beide Anleitung-Seiten, Quellen-Seite, M3-08 Vorderseite
[laengster Situationstitel], M3-19 Vorderseite [Brainy-Flow-Icon], M3-20 Rueckseite [laengster
Werkzeugtitel]) - fehlerfrei, keine Ueberlaufe. In klartext-app abgelegt.

Offen fuer spaeter: M6-Mobbingmaterialien weiterhin in eigenen Formaten geplant, nicht als
Handlungskarten. Damit sind alle drei geplanten Handlungskarten-Decks (TK, Krisendeck,
Werkzeugkarten-Deck) fertig.

## Strang 20 · M6-Mobbing-Materialien, erste Teile (30.07.2026)

M6 bekommt bewusst kein Handlungskarten-Deck (Begruendung: siehe Mobbing_Materialien_Konzept.md),
sondern eigene, passendere Formate. Erste zwei Teile umgesetzt:

**M6-Soforthilfe-Mini-Deck** (3 Karten, `build_card_mb.py`/`build_all_cards_mb.py`/
`build_booklet_mb.py`/`build_pdf_mb.py`): Text 1:1 aus den bestehenden App-Vorlagen
M6_DL_Mini-Krisenkarte.html, M6_DL_Mini-Checkliste_Erkennen.html, M6_DL_Digitale_Spuren_Sichern.html
uebernommen, nur aufs A6-Kartenformat gebracht. Farbe App-Pink #D81B60, kollisionsgeprueft (naechster
Nachbar FK-Rot ~60 Einheiten). KLARTEXT_Mobbing-Soforthilfe-Miniset_komplett.pdf: 8 Seiten (Cover +
Anleitung + 3x2 Karten), Stichproben visuell geprueft inkl. MB-03 mit 10 Schritten (haelt gut, viel
Luft nach unten) - fehlerfrei. Zusaetzlich `build_pdf_mb_vorlagenset.py`: die 3 Original-Vorlagen
unveraendert unbundled als eigenes PDF (KLARTEXT_Mobbing_Soforthilfe-Set.pdf, A5, 4 Seiten) - kein
Headless-Chromium in der Sandbox verfuegbar (fehlende Systemlibs, kein root/sudo), daher als
PIL-Nachbau des bestehenden App-Layouts statt Browser-Screenshot umgesetzt, Text identisch.

**Nachtrag/Korrektur:** Beim Kopieren der fertigen Dateien nach klartext-app fielen zusaetzliche,
bisher nicht erfasste Dateien auf: `AM_DL_Klassenvertrag.html`, `AM_DL_Stoppschild.html`,
`AM_DL_Meine_Verbuendeten.html`, `AM_DL_So_melde_ich_Mobbing.html` (4 Stueck, "AM" = Anti-Mobbing) -
das sind vermutlich die eigentlich gemeinten "4 Anti-Mobbing-Vorlagen" aus der urspruenglichen
Projektvision, nicht die M6_DL_Mini-*-Dateien, die fuer das Soforthilfe-Mini-Deck verwendet wurden.
Beide Materialgruppen sind vermutlich sinnvoll (INGRA-Schnellreferenz vs. kindgerichtete
Klassenmaterialien), aber die AM_DL_*-Dateien sind bislang nicht ausgewertet. Zusaetzlich entdeckt:
`KLARTEXT_AntiMobbing_Training.html` (603 Zeilen, offenbar ein vollstaendiger Kinder-Trainingskurs)
und `KLARTEXT_Fachbuch_System_Mobbing.html` (211 Zeilen, Fachreferenz) - beide noch nicht gesichtet.
An Anja rueckgemeldet, weiteres Vorgehen offen.

**AM_DL_*-Sichtung abgeschlossen (30.07.2026):** Alle 4 Dateien gelesen. Gehoeren zu
`KLARTEXT_AntiMobbing_Training.html` (6-Modul-Kinderkurs, Modul 6 "Druckmaterialien" verlinkt direkt
auf die 4 Dateien). Klassenvertrag (A4-Unterschriften-Poster), Meine Verbuendeten (A4-Quer,
Grundschule Sonnendiagramm + weiterfuehrende Schule Unterstuetzungsnetz-Liste) und So melde ich
Mobbing (Meldekarte mit 3 Schritten) sind Ausfuellvorlagen, keine Lesekarten - passen strukturell
nicht als Deck. Stoppschild ist die einzige echte Karten-Kandidatin (App-Original hat bereits
Vorder-/Rueckseite im Mini-Kartenformat). `KLARTEXT_Fachbuch_System_Mobbing.html`: einzelnes,
kondensiertes Referenzkapitel, redundant zu M6-01-15, bleibt digital, keine Aktion.

Mit Anja abgestimmt: 3 Ausfuellvorlagen als PDF-Set, Stoppschild zusaetzlich als A6-Bonuskarte
fuers spaetere Geschichtenkarten-Deck vorbereitet (Set A "Brainy erlebt Mobbing" nutzt zufaellig
dieselbe Rot-Farbfamilie #C62828 wie die App-eigene Anti-Mobbing-Identitaet).

`build_pdf_am_arbeitsmaterialien.py`: PIL-Nachbau der 3 Original-Layouts (Text identisch aus den
AM_DL_*-Dateien uebernommen), da kein Headless-Chromium in der Sandbox verfuegbar ist (fehlende
Systemlibs wie libXdamage, kein root/sudo fuer playwright install --with-deps - kurz probiert,
dann auf PIL-Nachbau umgestellt wie beim Soforthilfe-Set). KLARTEXT_AntiMobbing_Arbeitsmaterialien.pdf:
4 Seiten (Cover + Klassenvertrag + Meine-Verbuendeten-Doppelseite mit SVG-Sonnendiagramm-Nachbau +
Meldekarte), alle visuell geprueft - fehlerfrei.

`build_card_stoppschild.py` + `build_pdf_stoppschild.py`: A6-Bonuskarte (FontAwesome "ban"-Icon,
AM-Rot), Rueckseite mit Hinweis auf spaetere Einbindung ins Geschichtenkarten-Deck.
KLARTEXT_Mobbing_Stoppschild-Bonuskarte.pdf: 2 Seiten, visuell geprueft, kein Ueberlauf.

Alle 3 M6-Bausteine (Soforthilfe-Mini-Deck + Soforthilfe-Set + AntiMobbing-Arbeitsmaterialien +
Stoppschild-Bonuskarte) in klartext-app abgelegt. Noch offen: Geschichtenkarten-Deck (30 Karten,
Bildkonzept + Illustrationen, groesster verbleibender Baustein).

## Strang 21 · Geschichtenkarten-Deck (30.07.2026, Text fertig, Bilder ausstehend)

Vierter und vermutlich letzter Baustein der physischen M6-Uebersetzung: 30 Karten aus
`M6_Geschichtenkarten_Galerie.html` (3 Sets a 10: A "Brainy erlebt Mobbing"/B "Brainy hilft
anderen"/C "Brainy lernt Strategien"). Text war bereits kartenreif (1 Satz Situation + 3 Fragen +
1 Impuls), kaum Kuerzung noetig.

**Illustration:** Mit Anja abgestimmt - neue gemalte Illustrationen wie KD/EL/LK/JD (nicht die
bestehenden flachen App-Brainy-Sticker, Strang-5-Konsistenz). Charakterbogen von KD-Deck
uebernommen, 30 neue Szenen-Prompts direkt aus den App-Situationsbeschreibungen abgeleitet, in
`Geschichtenkarten_Bildprompts.md`. Bilder muessen extern generiert werden (kein Bildgenerierungs-
tool in dieser Session verfuegbar) - Anja generiert, dann finaler Render.

**Farbkollision entdeckt und korrigiert:** App-Set-Farben (Rot #C62828/Blau #1565C0/Gruen #2E7D47)
kollidieren teils (Set A = exakt identisch mit Krisendeck-Rot, Distanz 0; Set C = 38 Einheiten zu
KD-Gruen, unter dem ueblichen Minimum). Mit Anja abgestimmt: anders als Krisendeck/Werkzeugkarten
(bewusste 1:1-App-Farbuebernahme) folgt dieses Deck der Konvention der reflexiven Decks (eigene
kollisionsfreie Farben). Neue Toene: Set A Karmesinrot (150,30,35, Abstand ~49 zu FK),
Set B unveraendert Blau (bereits kollisionsfrei), Set C Tannengruen (46,110,60, Abstand ~57 zu KD).
Bedeutung (Rot=erlebt/Blau=hilft/Gruen=uebt) bleibt erhalten.

**Pipeline gebaut und mit Platzhaltern getestet** (analog FS-/DaZ-GS-Vorgehen): `build_card_
geschichtenkarten.py` (erste Karten-Datei mit 3 Set-Farben statt einer einzigen Deckfarbe -
neues Muster in der Serie), `build_all_cards_geschichtenkarten.py` (30 Karten, alle fehlerfrei
ohne Ueberlauf-Warnung gerendert, Bild-Platzhalter "Bild folgt" bis Illustrationen da sind),
`build_booklet_geschichtenkarten.py` (2 Anleitung-Seiten: Sets erklaeren, Bonuskarten-Hinweis,
Herkunft/Kein-Ersatz-fuer-App), `build_pdf_geschichtenkarten.py` (eigenes Cover, haengt zusaetzlich
die Stoppschild-Bonuskarte ans Ende). Cover-Titel-Ueberlauf beim ersten Render entdeckt und mit
Auto-Verkleinerung gefixt (wie in build_booklet_*.py new_page() bereits etabliert).

KLARTEXT_Geschichtenkarten-Deck_ENTWURF_ohne_Bilder.pdf: 65 Seiten (Cover + 2 Anleitung-Seiten +
30x2 Karten + Stoppschild-Bonuskarte 2 Seiten), Stichproben visuell geprueft (Cover, beide
Anleitung-Seiten, A1/B4/C5 - alle 3 Sets) - textlich fehlerfrei. Klar als Entwurf gekennzeichnet
(Dateiname + Cover-Statusbox "Illustrationen ausstehend"), damit kein Verwechslungsrisiko mit einer
finalen Version besteht. Nach Bildgenerierung: `build_all_cards_geschichtenkarten.py` und
`build_pdf_geschichtenkarten.py` erneut ausfuehren, Entwurfs-PDF durch finale Version ersetzen,
Merkliste aktualisieren.

Damit ist der gesamte M6-Mobbing-Komplex inhaltlich abgeschlossen bis auf die 30 Illustrationen.

**Korrektur Bildprompts (30.07.2026):** Anja bemerkte zurecht, dass der Standard-Charakterbogen
("peaceful closed eyes, gentle smile") nicht zu Set A passt, wo Brainy selbst das betroffene Kind
ist – ein Dauerlächeln trotz Mobbing wirkt verharmlosend. Entscheidung: Brainy zeigt in Set A die
tatsächliche Emotion der Szene (verletzt, erschrocken, beschämt, traurig), passend zur bereits in
der App angelegten Idee ("Brainy wird klein und grau" bei A1, vgl. Barometer-Farbvarianten brainy-
grau/rot/gelb.png). In Set B/C bleibt Brainy ruhig-entschlossen/konzentriert statt durchgehend
lächelnd. Physische Identitaet (Wolkenform, Brille, rotes Herz) bleibt in allen 30 Prompts gleich,
nur Ausdruck/Koerperhaltung wurden pro Karte einzeln neu formuliert. `Geschichtenkarten_
Bildprompts.md` komplett überarbeitet: alle 30 Prompts jetzt vollständig ausformuliert (kein
Referenzbild-Mechanismus nötig, analog KD-Copy-Prompts für Bing), mit Dateiname-Zuordnung.

**Finaler Render (30.07.2026):** Alle 30 Bilder von Anja generiert und unter `bilder/
geschichtenkarten/` abgelegt (als .jpg, nicht .png wie im Prompt-Dateinamen vorgesehen) -
`build_all_cards_geschichtenkarten.py` um `find_image()`-Fallback erweitert (analog KD/FS: prueft
.png/.jpg/.jpeg), keine Anpassung der Bilder noetig. Alle 30 Karten fehlerfrei neu gerendert, Cover-
Statusbox von "Illustrationen ausstehend" auf "vollständig" aktualisiert. Stichproben visuell
geprueft (A1 "wird ausgelacht" - Brainy zeigt echte Verletztheit statt Lächeln, haelt rotes Herz;
B1 "sagt Stopp" - ruhig-entschlossene Geste; C9 "übt Ruhe" - friedlich entspannt) - Design-
Entscheidung (emotionale Ausdrucksvielfalt statt Dauerlächeln) trägt sichtbar, Charakterkonsistenz
über alle Stichproben gut. KLARTEXT_Geschichtenkarten-Deck_komplett.pdf: 65 Seiten, finale Version,
in klartext-app abgelegt. Die fruehere Entwurfsversion (KLARTEXT_Geschichtenkarten-Deck_ENTWURF_
ohne_Bilder.pdf) bleibt aus Datei-Sicherheitsgründen zusaetzlich liegen (klartext-app-Dateien werden
nie geloescht ohne Rueckfrage) - kann auf Wunsch entfernt werden.

Damit ist die gesamte Handlungskarten-Serie (TK, Krisendeck, Werkzeugkarten, M6-Soforthilfe-
Mini-Deck, Geschichtenkarten-Deck) inklusive aller M6-Mobbing-Materialien vollstaendig fertig.

## Strang 22 · LK-Basis auf 50 Karten erweitert (30.07.2026)

Anja hat eine externe Analyse der vier LK-Dokumente (Vergleich zu KD/JD) geteilt. Bewertung der
Fundpunkte: Kuerzel-"Inkonsistenz" (LK-R- vs. LK-R-ADHS-/-AT-/-PF-) ist keine echte Unstimmigkeit,
sondern dieselbe Konvention wie bei den EL-Zusatzbloecken - unveraendert gelassen. Zwei echte
Befunde direkt behoben (kein Rueckfrage noetig): Zeitwiderspruch im Anleitung-Booklet ("keine Karte
zwischen Tuer und Angel" vs. "auch fuenf Minuten reichen") entschaerft zu "im Idealfall ein ruhiger
Moment ... aber auch fuenf Minuten sind besser als gar keine Reflexion"; fehlende Selbst-kLAR-
Anbindung ergaenzt (neuer Absatz in build_booklet_lk.py, methodik_seite: Lehrkraft soll bei eigenem
roten Zustand erst sich selbst regulieren, bevor sie eine Karte zieht).

Vier vorgeschlagene Themenluecken mit Anja abgestimmt ("eigentlich sollten wir alles aufnehmen") -
alle vier als neue Bloecke 7-10 der LK-Basis umgesetzt (30 -> 50 Karten), zwei weitere Vorschlaege
(neue Zusatzbloecke koerperliche Beeintraechtigung/Hochbegabung) auf spaeter vertagt (Anjas
Entscheidung: "erstmal nur LK-Basis erweitern"):

- **Block 7 - Klassengemeinschaft als System** (LK-R-31-35): Blick auf die Klasse als Gruppe statt
  nur Einzelkind, Rollen in der Klasse, Unruhe, Zusammenhalt, wenn sich die Klasse gegen die
  Lehrkraft stellt.
- **Block 8 - Abgrenzung & Feierabend** (LK-R-36-40): vertieft die bestehende Burnout-Karte "Kleine
  Momente fuer mich" um konkrete Abgrenzungsfragen (Feierabend, Erreichbarkeit, Wochenende, Ferien).
- **Block 9 - Interkulturelle Kompetenz** (LK-R-41-45): unterschiedliche Erziehungsvorstellungen,
  Sprachbarrieren, Kinder zwischen zwei kulturellen Systemen, eigene blinde Flecken, Vielfalt als
  Ressource.
- **Block 10 - KI & Digitalitaet im Unterricht** (LK-R-46-50): eigene Rolle im digitalen Wandel,
  Aufgabenabgabe an KI-Werkzeuge, Schueler:innen-Nutzung von KI, digitale Erschoepfung, was am
  analogen Unterricht bewahrt werden soll.

Neue Quellen recherchiert und verifiziert (alle "vorgeschlagen, bitte fachlich gegenpruefen", noch
nicht im Quellenregister bestaetigt): Kounin, J. S. (1970). *Discipline and group management in
classrooms.* Holt, Rinehart and Winston. (Block 7); Sonnentag, S., & Fritz, C. (2007). *The Recovery
Experience Questionnaire...* Journal of Occupational Health Psychology, 12(3), 204-221. (Block 8);
Gogolin, I. (1994, 2. Aufl. 2008). *Der monolinguale Habitus der multilingualen Schule.* Waxmann. -
bereits bei DaZ-GS/DaZ-Sek1 verwendet (Block 9); Zhai, X. (2024). *Transforming teachers' roles and
agencies in the era of generative AI...* Journal of Science Education and Technology.
https://doi.org/10.1007/s10956-024-10174-0 (Block 10).

Diversitaets-/Inklusions-Kalibrierung (Standing-Regel Strang 8) auf die 20 neuen Karten angewendet:
3/20 mit sichtbarem Merkmal (Rollstuhl LK-R-31, Hoergeraet LK-R-45, Fidget-Tool/ADHS-codiert LK-R-48).

Pipeline erweitert: `build_all_cards_lk.py` (CARDS + SYSTEMFRAGEN um 31-50 ergaenzt, total=50 dynamisch
aus `len(CARDS)`), `build_pdf_lk.py` (Cover mit 2-spaltiger 10-Themen-Liste analog JD-Deck-Muster,
Rendering-Range 1-50), `build_booklet_lk.py` (Kartenzahl/Blockzahl-Texte aktualisiert, Quellenseite
musste wegen der 4 neuen Quellen von 2 auf 3 Seiten aufgeteilt werden - beim ersten Testrender lief
die alte 2-Seiten-Struktur uber den unteren Seitenrand hinaus, per Sichtpruefung entdeckt und mit
neuer Funktion `quellen_seite1b()` behoben, "Beispielhafte Passung"-Seite um 4 Bullets fuer die neuen
Bloecke ergaenzt).

Alle 20 neuen Karten testweise ohne Bilder gerendert (kein Overflow-Warning), Cover + alle 5
Booklet-Seiten (Anleitung 1/2, Anleitung 2/2, Methodik, Quellen 1/3-3/3) visuell geprueft - sauber,
Zeitwiderspruch-Fix und Selbst-kLAR-Absatz sitzen wie vorgesehen, 2-spaltige Themenliste auf dem
Cover ohne Ueberlappung. Stichprobenkarten (LK-R-33, LK-R-48 mit langem Titel "Schueler:innen und KI
im Unterricht") fehlerfrei.

20 neue Bildprompts in `LK_Bildkonzept_und_Prompts.md` ergaenzt (copy-ready, gleicher Stil-Zusatz wie
LK-Basis, kein Brainy).

**Finaler Render (30.07.2026):** Alle 20 Bilder von Anja generiert und in `bilder/lk/` abgelegt. Alle
50 Karten fehlerfrei neu gerendert (kein Overflow-Warning). Stichproben visuell geprueft: LK-R-31
(Rollstuhl im Klassenbild gut sichtbar integriert), LK-R-48 (Fidget-Tool/ADHS-codiert, Schueler mit
Tablet), LK-R-45 (diverse Gruppe inkl. Hijab, Hoergeraet in der Bildkomposition nicht eindeutig
erkennbar - kein Ausschlusskriterium, Diversitaet insgesamt klar sichtbar). Gesamt-PDF
`KLARTEXT_LK-Deck_Basis_komplett.pdf` (109 Seiten: Cover + 2 Anleitung-Seiten + Methodik + 2
Glossar-Seiten + 3 Quellen-Seiten + 50x2 Karten) gebaut, in klartext-app abgelegt (PDF + alle 20 neuen
Kartenbilder in `karten/lk/`). Damit LK-Basis komplett auf 50 Karten/zehn Themenbloecke fertig.

**Korrektur (30.07.2026):** Anja fand einen Grammatikfehler auf LK-R-02 (bestehende Karte aus den
urspruenglichen 30, nicht Teil der neuen Bloecke) - "zutrauen" braucht ein Dativobjekt ("jemandem
etwas zutrauen"), das in Frage 2, Handlungsfrage und Tipp fehlte. Korrigiert zu "diesem Kind ... "
bzw. "Einem Kind ... zuzutrauen" in `LK_Kartenkonzept_Entwurf.md`, `LK_Tipps_fuer_dich_Entwurf.md`
und `build_all_cards_lk.py` (CARDS[2] + SYSTEMFRAGEN[2]). Karte neu gerendert, Gesamt-PDF neu gebaut
(109 Seiten), in klartext-app ueberschrieben.

## Strang 23 · EL-Deck: externe Analyse geprueft, Selbst-kLAR-Fix + neuer Zusatzblock Jugendliche (30.07.2026)

Anja hat eine externe Analyse der drei vorliegenden EL-PDFs (Basis, Autismus, Pflegekinder) geteilt.
Gegenpruefung vor Umsetzung (wie bei der LK-Analyse, Strang 22):

**Ein Befund der Analyse war falsch:** Die Analyse behauptet, der im EL-Basis-Glossar erwaehnte
ADHS-Zusatzblock fehle als PDF. Tatsaechlich existiert `KLARTEXT_EL-Zusatzblock_ADHS.pdf` bereits
(gebaut 25.07.2026, siehe oben) - die externe Analyse-Session hatte vermutlich nur 3 von 4 Dateien
vorliegen. Kein Handlungsbedarf, nur zur Richtigstellung dokumentiert.

**Zwei Befunde bestaetigt und behoben:**
1. Fehlende Selbst-kLAR-Anbindung (identischer Fund wie bei LK, Strang 22) - Absatz in
   `build_booklet_el.py` (methodik_seite) ergaenzt: Eltern koennen selbst in einen roten Zustand
   geraten, erst sich selbst regulieren, dann reflektieren. Visuell geprueft (kein Ueberlauf).
   EL-Basis-PDF neu gebaut (68 Seiten - Seitenzahl war vorher fälschlich als "67" notiert, korrekte
   Zaehlung: Cover+2 Anleitung+Methodik+2 Glossar+2 Quellen+30x2 Karten=68), in klartext-app
   ueberschrieben.
2. Illustrations-Altersschieflage bestaetigt (EL-Bildprompts stichprobenartig geprueft, z. B. EL-02
   zeigt explizit ein Kind beim Schuhebinden) - gleichzeitig mit Themenluecken geloest, siehe unten.

**Themenluecken bestaetigt** (per grep gegengeprueft, alle vier Themen kamen in EL_Kartenkonzept_
Entwurf.md tatsaechlich nicht vor): Pubertaet & Autonomie, digitale Erziehung, Co-Parenting/Trennung,
Schuldruck/Schuluebergaenge.

**Anjas Frage ("Zusatzblock Eltern von Jugendlicher oder Selbst-kLAR?") beantwortet mit: beides, aber
unterschiedlich gewichtet** - Selbst-kLAR als Quick-Fix direkt umgesetzt (s.o.), fuer die vier
Themenluecken + Altersschieflage empfohlen: **neuer EL-Zusatzblock "Eltern von Jugendlichen"**
(EL-JD-01-07), da strukturell stimmig - dockt anders als Autismus/ADHS/Pflegekinder nicht an eine
Diagnose, sondern ans bereits bestehende JD-Deck (Jugendliche) an, und loest die Altersschieflage
gleich mit (eigene Bilder zeigen Teenager statt juengere Kinder).

**EL-JD (7 Karten) entworfen** in `EL_Zusatzblock_Jugendliche.md`: Loslassen im Jugendalter, Wenn
sich mein Kind zurueckzieht, Medien und Familienfrieden, Erziehen nach einer Trennung, Schuldruck aus
Elternsicht, Wenn mein Kind andere Werte lebt, Stolz auf das, was schon losgelassen wurde. Kein
Fachpruefungs-Vorbehalt (allgemeine Ablösephase-Erfahrung, keine Diagnose, wie EL-PF). Pipeline
erweitert: `build_all_cards_el_zusatz.py` (SYSTEMFRAGEN["EL-JD"] + BLOECKE["EL-JD"] ergaenzt),
`build_pdf_el_zusatz.py` (SETS-Liste um EL-JD ergaenzt, viertes eigenstaendiges PDF
`KLARTEXT_EL-Zusatzblock_Jugendliche.pdf`). 7 Bildprompts in `EL_Zusatzbloecke_Bildprompts.md`
ergaenzt (copy-ready, Teenager statt juengere Kinder in den Szenen). 2 Karten testweise ohne Bilder
gerendert (EL-JD-01, EL-JD-05 mit laengstem Fragetext) - kein Ueberlauf, viel Luft nach unten.

Offen: Anja generiert die 7 Bilder (EL-JD-01.jpg bis EL-JD-07.jpg) und legt sie in `bilder/el/` ab,
danach `build_all_cards_el_zusatz.py` + `build_pdf_el_zusatz.py` final ausfuehren.

**Finaler Render (30.07.2026):** Alle 7 Bilder von Anja generiert und in `bilder/el/` abgelegt. Alle
28 Zusatzblock-Karten (21 bestehend + 7 neu) fehlerfrei neu gerendert. Stichprobe EL-JD-01 visuell
geprueft - zeigt deutlich einen Teenager (nicht juengeres Kind), Altersschieflage der EL-Basis-Bilder
damit fuer diesen Block geloest. Cover des neuen PDFs geprueft - sauber, kein Ueberlauf. Vier
EL-Zusatzblock-PDFs gebaut (je 15 Seiten): Autismus, ADHS, Pflegekinder (unveraendert neu gebaut,
da gleiche Pipeline-Datei), neu `KLARTEXT_EL-Zusatzblock_Jugendliche.pdf`. Alle vier in klartext-app
ueberschrieben/abgelegt. Damit EL-Deck jetzt vier Zusatzbloecke (Autismus, ADHS, Pflegekinder,
Jugendliche) plus EL-Basis mit Selbst-kLAR-Ergaenzung.

## Strang 24 · DaZ-GS/DaZ-Sek1: externe Analyse geprueft, Uebergangskarte ergaenzt (30.07.2026)

**Externe Analyse (4. Runde, nach LK/EL):** Vier Themenluecken vorgeschlagen: Ungewissheit beim
Bleibestatus (Sek I), Medien & Vernetzung, Rollenbilder & Erwartungen, Uebergang DaZ-Klasse →
Regelklasse. Kartenzitate (DAZ-SEK1-10/-11/-14) gegen die Konzeptdatei geprueft - korrekt.

**Bewertung je Vorschlag:**
- **Bleibestatus:** zurueckgestellt. Beide Decks grenzen sich bewusst als "kein
  Trauma-Verarbeitungs-Deck" ab (keine Fluchtdetails). Bleibestatus ist ein juristischer Fakt, kein
  Gefuehl wie Heimweh - eine direkte Karte wuerde leicht Fallspezifika (Asylverfahren,
  Abschiebungsrisiko) oeffnen, das liegt ausserhalb von Anjas DaZ-/Traumapaedagogik-Qualifikation
  und ist Rechtsberatungs-Terrain. Anja hat sich gegen eine Aufnahme entschieden.
- **Medien & Vernetzung:** abgelehnt (redundant) - DAZ-SEK1-18/DAZ-GS-18 "In Kontakt bleiben"
  deckt digitalen Kontakt zu Familie/Freunden bereits ab.
- **Rollenbilder & Erwartungen:** abgelehnt (redundant) - DAZ-SEK1-10 deckt allgemeinen
  Erwartungsdruck (Eltern vs. eigene Erwartung) bereits ab.
- **Uebergang DaZ-Klasse → Regelklasse:** angenommen, echte Luecke. Block A (beide Decks) deckt nur
  die erste Ankunft ab, nicht den spaeteren zweiten Uebergang aus dem DaZ-Schutzraum in die
  Regelklasse.

**Umsetzung:** Je eine neue Karte statt eines ganzen Blocks (Anjas Entscheidung):
- **DAZ-GS-25** "Von der Sprachfoerderung in die neue Klasse" (Block G, neu) - Brainy bleibt dabei.
- **DAZ-SEK1-25** "Von der DaZ-Klasse in die Regelklasse" (Block G, neu) - kein Brainy (wie
  restliches Sek-I-Deck).

Beide Decks jetzt 25 statt 24 Karten. Pipeline-Dateien aktualisiert:
`build_all_cards_dazgs.py`/`build_all_cards_dazsek1.py` (Karte 25 ergaenzt, `total` jetzt
dynamisch `len(CARDS)` statt hartcodiert 24), `build_pdf_dazgs.py`/`build_pdf_dazsek1.py` (Cover-
Kartenzahl, Themenliste um "Uebergang in die Regelklasse" ergaenzt, Rendering-Range auf 1-26),
`build_booklet_dazgs.py`/`build_booklet_dazsek1.py` (Anleitung/Methodik/Glossar-Texte auf 25 Karten/
sieben Themenbloecke aktualisiert). Bildprompts in `DAZ-GS_Bildprompts.md`/
`DAZ-SEK1_Bildprompts.md` ergaenzt (copy-ready).

**Nebenbefund (Bugfix):** Beim Test-Rendern der Booklet-Seiten fiel auf, dass `draw_h2()` in
`build_booklet_dazsek1.py` lange Ueberschriften nicht umbricht - zwei bestehende Ueberschriften
("Warum ein eigenes Deck..." und "Herkunftssprache und -qualifikation...") liefen schon vor meiner
Aenderung über den rechten Seitenrand hinaus. `draw_h2()` auf Zeilenumbruch umgestellt (wie
`draw_para()`), beide Seiten neu gerendert und visuell geprueft - jetzt sauber.

**QA:** Alle Anleitung-/Methodik-/Glossar-/Quellen-Seiten beider Decks neu gerendert und visuell
geprueft (kein Ueberlauf mehr). Karte 25 beider Decks testweise mit Platzhalterbild gerendert
(Rueckseite: Anleitung/Fragen/Tipp) - sauberer Textumbruch, kein Ueberlauf. Platzhalterbilder danach
wieder aus `bilder/dazgs/` und `bilder/dazsek1/` entfernt.

Offen: Anja generiert 2 Bilder (DAZ-GS-25.jpg, DAZ-SEK1-25.jpg), legt sie in `bilder/dazgs/` bzw.
`bilder/dazsek1/` ab, danach `build_all_cards_dazgs.py`/`build_all_cards_dazsek1.py` +
`build_pdf_dazgs.py`/`build_pdf_dazsek1.py` final ausfuehren.

**Finaler Render (30.07.2026):** Beide Bilder (DAZ-GS-25.jpg, DAZ-SEK1-25.jpg) von Anja generiert
und in `bilder/dazgs/` bzw. `bilder/dazsek1/` abgelegt. Alle 25 Karten beider Decks fehlerfrei neu
gerendert, Karte 25 stichprobenartig visuell geprueft (Bildmotiv passend: Kind/Jugendliche/r an der
Tuer zum neuen Klassenraum). Beide Gesamt-PDFs neu gebaut (je 57 Seiten: 7 feste Seiten + 25×2
Kartenseiten), Cover- und letzte Kartenseite stichprobenartig per pdftoppm geprueft - sauber, alle
sieben Themenbereiche im Cover gelistet. Beide PDFs nach klartext-app kopiert/ueberschrieben. Damit
DaZ-GS- und DaZ-Sek1-Deck jetzt bei 25 Karten (sieben Themenbloecke). Rundgang durch alle Decks
(KD, JD, LK, EL, DaZ) fuer diese Runde abgeschlossen.

## Strang 25 · FS-Deck: externe Analyse geprueft, 2 neue Karten ergaenzt (30.07.2026)

**Faktencheck:** Analyse behauptete, FS nutze "die gleichen Brainy-Bilder wie KD" - falsch. Anja
hatte sich am 26.07. bewusst fuer eigene FS-Bilder entschieden (bilder/fs/, 30 Dateien, per md5
gegen bilder/kd/ verifiziert unterschiedlich). Ursache gefunden: veraltete Textzeile "gleiche ...
Bilder" stand noch an drei Stellen (Cover in `build_pdf_fs.py`, Anleitung + Glossar in
`build_booklet_fs.py`) - echter Fehler, korrigiert auf "eigene Bilder". Rest der Analyse (30
KD-Themen 1:1, keine dritte Frage, FS-04/FS-17-Zitate, kLAR-Modell nur INGRA-seitig im Glossar)
war zutreffend.

**Bewertung der 3 Erweiterungsvorschlaege:**
- **Lernfrust aushalten:** echte Luecke, angenommen.
- **"Sagen was ich brauche" (AAC/Talker):** teilweise ueberschneidend mit FS-20, aber die
  AAC-spezifische Rahmung ist eigenstaendig genug - angenommen.
- **Uebergang Werkstatt/Arbeitswelt (Transfer aus JD-41-44):** Scope-Mismatch - FS ist explizit
  Grundschul-Altersstufe (Spiegel von KD), Werkstatt-Themen gehoeren zur
  Foerderschule-Berufsvorbereitungsstufe (16-18), eine andere Altersgruppe. Waere ein eigener
  Zusatzblock nach EL-JD-Muster (eigene Bilder, adaptierter JD-Text), nicht FS-Basis. Anja hat
  diese Option nicht ausgewaehlt - vorerst nicht umgesetzt, bei Bedarf spaeter erneut aufgreifen.

**Umsetzung:** FS-31 "Wenn Lernen schwerfaellt" und FS-32 "Sagen, was ich brauche" als neuer
Block G "Lernen & Kommunikation" ergaenzt. FS-Deck jetzt 32 statt 30 Karten. Pipeline aktualisiert:
`build_all_cards_fs.py` (2 Karten ergaenzt, `total` jetzt dynamisch `len(CARDS)`),
`build_pdf_fs.py` (Cover-Kartenzahl, Themenliste, Rendering-Range 1-33), `build_booklet_fs.py`
(Anleitung/Methodik/Glossar auf 32 Karten aktualisiert, gleichzeitig die "gleiche Bilder"-Fehler
behoben). Bildprompts in `FS_Bildprompts.md` ergaenzt (copy-ready, Brainy dabei wie beim Rest des
Decks).

**QA:** Anleitung-/Methodik-/Glossar-Seiten neu gerendert und visuell geprueft (kein Ueberlauf).
FS-31/FS-32 testweise mit Platzhalterbild gerendert - sauberer Textumbruch. Platzhalterbilder
danach wieder aus `bilder/fs/` entfernt. FS-Gesamt-PDF mit den Textkorrekturen bereits einmal neu
gebaut und nach klartext-app kopiert (67 Seiten, vor den 2 neuen Karten); wird nach Bildlieferung
fuer FS-31/FS-32 ein zweites Mal neu gebaut (dann 71 Seiten).

Offen: Anja generiert 2 Bilder (FS-31.jpg, FS-32.jpg), legt sie in `bilder/fs/` ab, danach
`build_all_cards_fs.py` + `build_pdf_fs.py` final ausfuehren.

**Finaler Render (30.07.2026):** Beide Bilder (FS-31.jpg, FS-32.jpg) von Anja generiert und in
`bilder/fs/` abgelegt. Alle 32 Karten fehlerfrei neu gerendert, FS-31/FS-32 visuell geprueft -
Bildmotive treffend (Kind mit Rechenheft und Kopf-in-Hand-Geste bei FS-31, Kind zeigt auf
Kommunikationstafel/Tablet mit Piktogrammen bei FS-32, Brainy in beiden dabei). Gesamt-PDF neu
gebaut (71 Seiten: 7 feste Seiten + 32×2 Kartenseiten), Cover (7 Themenbereiche inkl. "Lernen und
Kommunikation") und letzte Kartenseite per pdftoppm geprueft - sauber. PDF nach klartext-app
kopiert. Damit FS-Deck bei 32 Karten (sieben Themenbloecke).

## Strang 26 · OGS-Deck: externe Analyse geprüft, Block 8 „Rahmen und Zusammenarbeit" ergänzt (30.07.2026)

**Faktencheck der externen Analyse:** Zwei Behauptungen widerlegt. (1) „TK-Deck ist ein Tippfehler
für KD-Deck" – falsch. TK ist ein eigenständiges, real existierendes Deck (Handlungskarten,
`build_booklet_tk.py`), in dem Brainy tatsächlich kaum/nur als Eckmarke vorkommt – kein Tippfehler.
(2) Die Analyse behauptete umgekehrt, OGS nutze Brainy „als Eckmarke" – auch falsch, und zwar genau
andersherum: laut `OGS_Kartenkonzept_und_Prompts.md` (Zeile 20) ist Brainy im OGS-Deck wie bei
KD/FS/DaZ-GS voll ins Bild integriert; die Eckmarke-Methode gehört zu TK, nicht zu OGS. Der Hinweis
zu „Systemisch gedacht" vs. „Dritte Frage" (Terminologie) ist beobachtungsgenau, aber es gibt aktuell
keine OGS-Glossarseite, in der etwas zu vereinheitlichen wäre – kein akuter Fehler. Die „OGS-R"-
Namensvorschlag-Analogie zu LK-R greift nicht: LK-R existiert nur wegen einer echten
Namenskollision mit einem älteren, unabhängigen LK-01–17-Kartensatz: bei OGS gibt es keine
vergleichbare Kollision.

**Bewertung der 4 Erweiterungsvorschläge:** Alle vier von Anja mit "alle" freigegeben.
- **Inklusion/herausforderndes Verhalten:** echte Lücke, angenommen als OGS-29.
- **Team-Rollenklärung (multiprofessionelle Kooperation):** echte Lücke, angenommen als OGS-30.
- **Hausaufgaben-Konflikt:** inhaltlich ein Perspektivwechsel von EL-22 ("Hausaufgaben ohne Kampf",
  Eltern-Sicht) auf die OGS-Fachkraft-Sicht – als thematischer Transfer angenommen, keine neue
  Quelle nötig, als OGS-31.
- **Raumgestaltung als "dritter Erzieher":** echte Lücke, angenommen als OGS-32.

**Quellen (neu recherchiert, wissenschaftliche Originalquellen verifiziert):**
- OGS-29: Hejlskov Elvén, B. (2022). *Keine Macht den Mächtigen*. Probst – bereits im
  KLARTEXT-Quellenregister bestätigt (AT-Deck, 26.07.2026), hier wiederverwendet.
- OGS-30: Speck, K., Olk, T., Böhm-Kasper, O., Stolz, H.-J. & Wiezorek, C. (Hrsg.) (2011).
  *Ganztagsschulische Kooperation und Professionsentwicklung*. Juventa – per Websuche verifiziert
  (Juventa/Weinheim, ISBN 978-3-7799-2158-5), „vorgeschlagen, bitte gegenprüfen". Ein zunächst
  erwogenes „Fuchs (2023)"-Dissertationszitat ließ sich nicht verifizieren und wurde verworfen.
- OGS-31: kein neues Zitat, Transfer aus EL-22.
- OGS-32: Rinaldi, C. (2006). *In Dialogue with Reggio Emilia*. Routledge – per Websuche verifiziert
  (reales Buch, Nachfolgerin Malaguzzis in Reggio Emilia), „vorgeschlagen, bitte gegenprüfen" (kein
  einzelnes sauberes Primärzitat für „Raum als dritter Erzieher" selbst, das Konzept stammt von
  Malaguzzi, Rinaldi ist die anerkannte Sekundärquelle dazu).

**Umsetzung:** OGS-29 bis OGS-32 als neuer Block 8 "Rahmen und Zusammenarbeit" ergänzt. OGS-Deck
jetzt 32 statt 28 Karten (acht statt sieben Themenblöcke). Pipeline aktualisiert:
`build_all_cards_ogs.py` (4 Karten ergänzt, BLOCK_BADGE erweitert, `total` jetzt dynamisch
`len(CARDS)` statt hartcodiert 28, Rendering-Range 1–33), `build_pdf_ogs.py` (Cover-Kartenzahl,
Themenliste, Rendering-Range 1–33), `build_booklet_ogs.py` (Anleitung auf 32 Karten/acht Blöcke
aktualisiert, QUELLEN_BESTAETIGT/VORGESCHLAGEN erweitert, "Beispielhafte Passung" um 4 Bullets
ergänzt). `OGS_Kartenkonzept_und_Prompts.md` auf Rev. 4 aktualisiert (Blockstruktur, Diversitäts-/
Inklusionszählung neu: 11/32 arabisch, 1/32 Schwarz, 7/32 mit sichtbarer Behinderung – neu OGS-30
mit Rollstuhl-Fachkraft, bewusst NICHT an OGS-29/herausforderndes Verhalten gekoppelt, um
Behinderung nicht mit "Problemverhalten" zu assoziieren).

**Bug beim Implementieren gefunden und behoben:** gerade Anführungszeichen `"` versehentlich in
einem Python-String mit doppelten Anführungszeichen als Delimiter verwendet (OGS-31-Zitat) –
SyntaxError, korrigiert auf typografische Anführungszeichen „…". Zweitens: die Quellen-Seite 1 lief
nach Ergänzung um 2 weitere Quellen (jetzt 7 statt 5 vorgeschlagene) in den Footer über – behoben,
indem die Seite in zwei Seiten aufgeteilt wurde (`quellen_seite1` = bestätigte Quellen,
neue `quellen_seite1b` = vorgeschlagene Quellen), Quellen-Abschnitt jetzt 3 statt 2 Seiten
(Seitenzahlen "1/3", "2/3", "3/3" aktualisiert), `build_pdf_ogs.py`-Import entsprechend erweitert.

**QA:** Alle 32 Karten fehlerfrei ohne Bild gerendert (keine WARNUNG-Meldung, auch nicht bei den 4
neuen Karten). Cover, Anleitung 1/2, alle 3 Quellenseiten und die 4 neuen Kartenrückseiten
(OGS-29–32) per pdftoppm gerendert und visuell geprüft – kein Überlauf, saubere Umbrüche. Entwurfs-
PDF (70 Seiten: 6 feste Seiten + 32×2 Kartenseiten) gebaut und nach klartext-app kopiert als
`KLARTEXT_OGS-Basis-Deck_komplett_ENTWURF.pdf`.

Offen: Anja generiert 4 Bilder (OGS-29.jpg bis OGS-32.jpg, Prompts in `OGS_Kartenkonzept_und_Prompts.md`
und im Chat als Copy-Text geliefert), legt sie in `bilder/ogs/` ab, danach `build_all_cards_ogs.py` +
`build_pdf_ogs.py` final ausführen (dann finales, nicht-ENTWURF-PDF).

## Strang 27 · AT/TK: externe Analyse geprüft, keine echte Inkonsistenz (30.07.2026)

**Faktencheck:** Analyse behauptete eine „widersprüchliche Aussage in der AT-Anleitung über die
Brainy-Abwesenheit im TK-Deck" – nicht auffindbar. `build_booklet_at.py` erwähnt TK an keiner
einzigen Stelle (komplette Datei durchsucht); die „Kein Brainy im Bild"-Liste dort nennt nur
JD/EL/LK/TR. Grund, warum TK dort zu Recht fehlt: TK hat laut `build_booklet_tk.py` tatsächlich
partiell Brainy im Bild (klein in der Bildecke, nur auf Fall-/Kind-/Beziehungskarten, nicht auf
reinen Verwaltungskarten) – keine vollständige Abwesenheit wie bei JD/EL/LK/TR, daher korrekt nicht
in dieser Liste. Gleicher Verwechslungstyp wie beim OGS-Fund (Strang 26): die externe Analyse
verortet TK/Brainy-Aussagen wiederholt am falschen Deck. Kein Korrekturbedarf, Anja informiert.

## Strang 28 · TR-Deck: externe Analyse geprüft, Block 9 „Moderne Fortbildungslandschaft" ergänzt (30.07.2026)

**Faktencheck der Terminologie-Frage:** „Dritte Frage" (TR/LK/EL, TR hat sogar einen
Glossareintrag dazu, `build_booklet_tr.py` Zeile 237) vs. „Systemisch gedacht" (OGS) – beide real,
keine Falschbehauptung diesmal. Anja entschied auf Nachfrage (AskUserQuestion): deckspezifisch
belassen, keine Vereinheitlichung – TR/LK/EL richten sich an systemik-erfahrenere Fachkräfte
(technischer Begriff passt), OGS an Ganztags-Fachkräfte (freundlicherer Begriff passt).

**Bewertung der 4 Erweiterungsvorschläge:** Alle vier gegen die bestehenden 29 Karten geprüft, keine
Redundanz gefunden, von Anja per AskUserQuestion alle vier freigegeben.
- **Online- & Hybrid-Didaktik:** echte Lücke (TR-13 deckt nur physische Raum-/Technikvorbereitung
  ab), als TR-30 umgesetzt.
- **Institutionelle Skepsis der Träger:** TR-09/TR-20 behandeln nur Widerstand von
  Kursteilnehmenden während der Schulung, nicht Skepsis auf Träger-/Leitungsebene davor/darum
  herum – eigenständig genug, als TR-31 umgesetzt.
- **Trainer-Self-Care/Psychohygiene danach:** TR-22 behandelt nur die akute Situation während der
  Schulung, nicht die Regeneration danach – als TR-32 umgesetzt, erweitert TR-22 explizit um die
  Nachher-Phase.
- **Diversität in der Erwachsenengruppe:** echte Lücke (TR-12 klärt nur Format/Erfahrung fürs
  Zuschneiden der Schulung, nicht Umgang mit Heterogenität in der Gruppe selbst), als TR-33
  umgesetzt.

**Quellen (wissenschaftliche Originalquellen, per Websuche verifiziert):**
- TR-30: Salmon, G. (2000). *E-Moderating: The Key to Teaching and Learning Online.* Kogan Page –
  „vorgeschlagen, bitte gegenprüfen".
- TR-31: Rogers, E. M. (2003). *Diffusion of Innovations* (5th ed.). Free Press – „vorgeschlagen,
  bitte gegenprüfen".
- TR-32: Sonnentag, S. & Fritz, C. (2007) – bereits im KLARTEXT-Quellenregister bestätigt (LK-Deck,
  30.07.2026), hier wiederverwendet, keine neue Verifikation nötig.
- TR-33: Steiner, A. & Maillinger, C. (2025). Heterogenität in der Erwachsenenbildung – Anregungen
  für ein didaktisches Konzept und Kompetenzprofil. *bwp@ Spezial PH-AT3* – per Websuche verifiziert
  (Autorinnen, Ausgabe, Erscheinungsdatum bestätigt), „vorgeschlagen, bitte gegenprüfen".

**Umsetzung:** TR-30 bis TR-33 als neuer Block I „Moderne Fortbildungslandschaft" ergänzt.
TR-Deck jetzt 33 statt 29 Karten (neun statt acht Themenblöcke). Pipeline aktualisiert:
`build_all_cards_tr.py` (4 Karten + 2 neue SYSTEMFRAGEN-Einträge ergänzt, `total` jetzt dynamisch
`len(CARDS)` statt hartcodiert 29), `build_pdf_tr.py` (Cover-Kartenzahl, Themenliste neun Zeilen,
Rendering-Range 1–34, Import/Seiten um `quellen_seite1b` erweitert), `build_booklet_tr.py`
(Anleitung/Methodik/Glossar auf 33 Karten aktualisiert, Quellen-Abschnitt von 2 auf 3 Seiten
aufgeteilt wegen der 3 neuen Quellen – Seite 1 „Bestätigt", neue Seite 1b „Vorgeschlagen", Seite 2
„Beispielhafte Passung" jetzt Seite 3, um Überlauf zu vermeiden). `TR_Kartenkonzept_Entwurf.md` und
`TR_Bildprompts.md` (4 neue Prompts, kein Brainy, wie der Rest des TR-Decks) aktualisiert.

**QA:** Testweise mit 4 grauen Platzhalterbildern (`bilder/tr/TR-30.jpg` bis `TR-33.jpg`, danach
wieder entfernt) gerendert: alle 33 Karten fehlerfrei ohne WARNUNG-Meldung, Test-PDF (75 Seiten: 9
feste Seiten + 33×2 Kartenseiten) gebaut. Cover, Methodik-Seite, alle 3 Quellenseiten und alle 4
neuen Kartenrückseiten (TR-30–33) per pdftoppm gerendert und visuell geprüft – kein Überlauf,
saubere Umbrüche. Test-PDF NICHT nach klartext-app kopiert (enthält Platzhalter-Grauflächen statt
echter Bilder, kein Anja-tauglicher Zwischenstand wie bei OGS/FS mit ENTWURF-Fallback – TR-Pipeline
bricht bei fehlenden Bildern hart ab, kein ENTWURF-Modus vorgesehen).

Offen: Anja generiert 4 Bilder (TR-30.jpg bis TR-33.jpg, Prompts in `TR_Bildprompts.md` und im Chat
als Copy-Text geliefert, kein Brainy), legt sie in `bilder/tr/` ab, danach `build_all_cards_tr.py` +
`build_pdf_tr.py` final ausführen.

## Strang 29 · PWA-Flashcard-App: Prototyp mit KD-Deck (30.07.2026)

**Anlass:** Alle Kartendecks sind jetzt als PDF fertig. Anja will die Karten zusätzlich digital
als installierbare App (PWA) mit Flip-Karten (Vorderseite antippen → Rückseite mit Fragen) – auch
für ihre Bewerbung als Schulbegleitung. Ausdrücklicher Nebenpunkt: Wochenlimit war bei 28 %,
Reset erst in 6 Tagen – tokenarme Umsetzung gefordert.

**Architekturentscheidung (tokensparend):** Statt pro Deck ein eigenes UI zu bauen oder
Karteninhalte neu zu generieren, ein einziges wiederverwendbares System:
1. `pwa_export_deck.py` (neu, im Hauptordner) liest die bereits vorhandenen `CARDS`-Dicts aus
   `build_all_cards_*.py` direkt aus (reiner Code, keine Tokens für Karteninhalte) und schreibt
   `pwa/data/<deck>.json` + komprimierte Bilder nach `pwa/images/<deck>/`. Deckt beide bestehenden
   Kartenformate ab (4-Tupel wie KD/JD/FS, 6-Tupel wie OGS, plus separates SYSTEMFRAGEN-Dict wie
   EL/LK/TR).
2. Eine einzige Flashcard-Engine (`pwa/index.html`, `style.css`, `app.js`) – einmal gebaut, liest
   jedes Deck-JSON generisch, Deckfarbe wird zur Laufzeit per CSS-Variable gesetzt.
3. Bildkompression (PIL, Breite 700px, JPEG Qualität 76) – KD-Bilder von 18 MB auf 1,9 MB gedrückt,
   ohne sichtbaren Qualitätsverlust auf Handy-Displays.

**Umgesetzt (Prototyp, nach Anjas Wahl "erst 1 Deck"):** KD-Deck komplett exportiert (35 Karten,
Bilder aus `bilder/kd/` wiederverwendet, keine neuen Bilder nötig). PWA-Grundgerüst:
`manifest.json` (installierbar, Icons aus K-Logo generiert), `service-worker.js` (Offline-Caching:
App-Hülle sofort, Deck-Daten/Bilder beim ersten Öffnen), `index.html`/`style.css`/`app.js`
(Deck-Übersicht → Kartenansicht, Tap-to-flip mit CSS-3D-Transform, Wischgesten, Zurück/Weiter/
Zufall-Navigation, merkt sich letzte Position pro Deck via localStorage).

**QA:** JSON-Validität aller Dateien geprüft, JS-Syntaxcheck (`node --check`) für `app.js` und
`service-worker.js` fehlerfrei, alle 35 Bildpfade auf Existenz geprüft (keine fehlenden), lokaler
Testserver gestartet und alle Endpunkte (HTML/CSS/JS/Manifest/JSON/Bilder/Service-Worker) auf
Status 200 mit korrektem Content-Type geprüft. Kein Headless-Browser-Screenshot gemacht (Puppeteer/
Chromium-Download wäre unnötig ressourcenintensiv gewesen) – echter Test auf Anjas Gerät ist für
Touch-Flip-Interaktion ohnehin aussagekräftiger als ein automatisierter Screenshot.

**Nach klartext-app kopiert:** `pwa/` (komplett, 2,2 MB) + `pwa_export_deck.py` im Hauptordner +
`pwa/README.md` mit Test-/Deploy-Anleitung (lokaler Server für Tests, GitHub Pages als kostenlose
Dauerlösung, da `klartext-app` bereits ein GitHub-Repo ist) und Anleitung, wie ein weiteres Deck in
einem Befehl ergänzt wird.

Offen: Anja testet den KD-Prototyp auf ihrem Handy (lokal oder per GitHub Pages). Bei Freigabe:
restliche 18 Decks per `pwa_export_deck.py` in einem Rutsch ergänzen (geringer Aufwand, Engine
steht bereits).

**Finaler Render (30.07.2026):** Alle 4 Bilder (TR-30.jpg bis TR-33.jpg) von Anja generiert und in
`bilder/tr/` abgelegt. Alle 33 Karten fehlerfrei neu gerendert, TR-30–33 visuell geprüft – Motive
treffend (Trainer:in am Laptop mit Grid aus Teilnehmenden-Kacheln bei TR-30, ruhiges Gespräch mit
skeptischer Leitungsperson bei TR-31, stille Erholungsmomente mit Tasse nach dem Workshop bei TR-32,
sichtbar diverse Gruppe inkl. Rollstuhlnutzerin am Tisch bei TR-33, konsequent ohne Brainy wie der
Rest des TR-Decks). Gesamt-PDF neu gebaut (75 Seiten: 9 feste Seiten + 33×2 Kartenseiten), Cover und
alle 4 neuen Kartenrückseiten per pdftoppm geprüft – sauber. PDF nach klartext-app kopiert. Damit
TR-Deck bei 33 Karten (neun Themenblöcke).

## Strang 27 · Alle Verkaufsseiten + neue Bausteine SMI/LRS-Sek1/SP/M3-Erweiterung (01.08.2026)

**Verkaufsseiten für alle 18 bestehenden Kartendecks fertiggestellt.** Nach KD/JD/EL (vorherige
Sitzung) und LK/TR/AT/ADHS (Sitzungsbeginn) wurden die restlichen 11 Decks in einem Rutsch gebaut:
FS, DaZ-GS, DaZ-Sek I, OGS, Geschichtenkarten (GK), TK, Krisendeck (FK), Werkzeugkarten (M3),
Mobbing-Materialien (MB), Insel-Set (IS), Zonen-Set (ZS) – je eine `{CODE}_Verkaufsseite.html` im
etablierten Design-System (Navy/Mint/Cream/Gold), Produktionsscript `build_verkaufsseiten.py`
(gemeinsame Template-Funktion + Datenwörterbuch pro Deck) für Token-Effizienz statt 11×
Handschreiben. `KLARTEXT_Shop_Uebersicht.html` zeigt jetzt alle 18 Decks als "Verfügbar zum
Vormerken" (weiterhin nur `mailto`-Vormerkung, kein echter Checkout – auf Anjas Wunsch bewusst so
belassen, da noch kein Gewerbe angemeldet ist). **Wichtige Klarstellung für Anja:** Die
Verkaufsseiten zeigen absichtlich nicht die vollständigen Karteninhalte – die liegen (mit allen 20
damaligen Decks, echten Bildern, Flip-Funktion) bereits vollständig in der PWA (`pwa/`, lokal
startbar via `python3 serve.py`).

**Neue Bausteine SMI/LRS-Sek1/SP/M3-Erweiterung entworfen (33 neue Karten).** Ausgangspunkt: Anjas
über NotebookLM erarbeiteter Master-Prompt (inkl. Marktanalyse-Begründung). Alle im Prompt
verwendeten `[Gesprächsverlauf]`-Verweise (NotebookLM-intern, keine echten Zitate) wurden durch
recherchierte, verifizierte Primärquellen ersetzt oder – wo keine passende Quelle existierte –
ehrlich als "keine Einzelquelle" markiert, statt etwas zu erfinden.

- **SMI-Deck** (Systemische Mobbing-Intervention, SMI-01–10): Sek I, Fachkraft-facing (INGRA/LK),
  kein Brainy. Quellen unter anderem Salmivalli et al. 1996 (Bystander-Rollen), de Shazer 1988
  (Teufelskreis, "vorgeschlagen, bitte gegenprüfen" wie bei EL/LK), Olweus/Limber/Mihalic 1999
  (Cybermobbing), Watzlawick/Weakland/Fisch 1974 (Humor), Bandura 1977 (Nachhaltigkeit, bereits im
  EL-Quellenregister bestätigt). **Korrektur gegenüber Original-Prompt:** SMI-07 "Lehrer-Eltern-
  Allianz" war im Master-Prompt fälschlich mit Gottman referenziert (dessen Forschung betrifft
  Paar-/Eltern-Kind-Beziehungen) – durch die tatsächlich einschlägige Quelle Christenson & Sheridan
  (2001, Family-School-Partnerships) ersetzt.
- **LRS/Dyskalkulie-Sek1-Deck** (`lrs-sek1`, L-01–07 + D-01–03, 10 Karten kombiniert – ein reines
  3-Karten-Dyskalkulie-Deck läge unter der Mindestgröße): Jugendliche-facing, JD-Stil, kein Brainy.
  Jede Karte trägt zusätzlich eine fächerübergreifende Lehrkraft-Strategie im `hinweis`-Feld
  (Mündlich-vor-Schriftlich, Struktur-Hilfen mit Verweis auf M3-15, Multisensorik via M3-17,
  Zeit-Management via M3-21). Quellen: Schulte-Körne & Galuschka (LRS), BVL (Nachteilsausgleich,
  KMK-Beschlüsse), von Aster & Shalev 2007 (Dyskalkulie).
- **SP-Deck** (Springer-INGRAs, SP-01–07): professionell/nüchtern, kein Brainy. Originäres
  KLARTEXT-Praxiskonzept ohne etablierte Forschungsliteratur zur Springer-Rolle speziell – bei
  4 von 7 Karten bewusst keine akademische Quelle erzwungen (`quelle: —`), SP-06 nutzt Christenson &
  Sheridan (2001) sinngemäß übertragen.
- **M3-Erweiterung** (M3-21–26, hängt an bestehendes Werkzeugkarten-Deck an, jetzt 26 statt 20
  Karten): Sichtbare Zeit (Studie EJIHPE 2025, DOI 10.3390/ejihpe15120243), Stopp-Hand-Signal
  (Kounin 1970, bereits verifiziert), Sicherer Ort (Siegel 1999, bereits im Insel-Set verifiziert),
  Körper-Check-In + Kraft der Pause (Porges 2011, Polyvagal-Theorie), No-Blame-Approach (Maines &
  Robinson 1992).

**Farben kollisionsgeprüft (RGB-Distanz gegen alle 20 bestehenden Deckfarben):** SMI `#592D59`
(Aubergine-Violett, Abstand 44,4), LRS-Sek1 `#BF9369` (Sandbraun, Abstand 68,6), SP `#5A4A42`
(Espresso-Taupe, Abstand 37,5).

**Umsetzung:** Konzeptdatei `SMI-LRS-SP-M3_Kartenkonzept_Entwurf.md` (alle 33 Kartentexte +
Quellen), Bildprompts `SMI-LRS-SP_Bildprompts.md` (27 Stück, JD-Stil, kein Brainy – M3-21–26
brauchen keine, nutzen wie M3-01–20 Font-Awesome-Icons). JSON-Dateien `smi.json`, `lrs-sek1.json`,
`sp.json` neu angelegt, `werkzeug.json` um 6 Karten erweitert, alle in `pwa/data/decks.json`
registriert (jetzt 23 Decks) – Texte sind damit schon jetzt in der PWA sichtbar (ohne Bilder, mit
Platzhalter).

**Offen:** Fachprüfung durch Anja vor Produktivsetzung (wie bei jedem neuen Deck). Bildgenerierung
extern durch Anja. PDF-Pipeline (`build_card_*.py` etc.) folgt erst nach Bildfreigabe. Verkaufsseiten
für die drei neuen Decks folgen erst nach Fachprüfung + Bildern, nicht vorher (Reihenfolge wie bei
allen anderen Decks: erst Inhalt, dann Vermarktung).

## Strang 30 · Gesamtüberblick Domain/Shop/App + offene Architektur-Fragen (02.08.2026)

**Anlass:** Nach dem heutigen GitHub-Push hat Anja den Überblick verloren, was in welchem Repo liegt
und ob die Website jetzt "fertig" ist. Komplette Bestandsaufnahme, damit das an einer Stelle steht.

### Die drei Teile der Landschaft
1. **klartext-mentoring.de** — die öffentliche Domain, die Kund:innen sehen.
2. **klartext-shop** (Repo `anja2026-dev/klartext-shop`) — laut Entscheidung vom 23.07.2026 (siehe
   oben „DRINGEND · Repo-Trennung Marketing vs. Pilot-App") das dafür vorgesehene, getrennte Repo für
   *alle* Verkaufs-/Marketingseiten, läuft über Cloudflare Pages, ursprünglich live unter
   `klartext-shop.pages.dev`, später an `klartext-mentoring.de` angebunden (Task „Domain-Setup",
   23.07.–01.08.).
3. **klartext-app** (Repo `anja2026-dev/klartext-app`) — die interne, Supabase-authentifizierte
   Case-Management-App. **Korrektur (02.08.2026):** Die Malteser-Testphase wurde bereits **vor ca.
   3 Tagen (ca. 30.07.2026) beendet** — die App läuft aktuell in keiner aktiven Pilotphase mehr. Alle
   Formulierungen weiter oben in dieser Merkliste, die von "aktuell laufender Beta-/Pilotphase bei den
   Maltesern" sprechen, sind damit veraltet und beziehen sich auf den historischen Stand vom 23.07.2026.

### Wichtiger, ungeklärter Befund — muss vor allem anderen geklärt werden
Entgegen der eigenen Entscheidung vom 23.07. (Verkaufsseiten künftig **nicht** in klartext-app bauen)
sind die `SHOP_*`-Dateien sowie alle heutigen Änderungen (Mobbing-Verkaufsseite, Kaufen-Platzhalter
auf allen 18 Verkaufsseiten, Vorschaubilder, AGB, Widerrufsbelehrung, Impressum-Korrekturen) direkt im
Repo **klartext-app** entstanden und dorthin gepusht — nicht nach klartext-shop. Ich habe in dieser
Sitzung keinen Zugriff auf das klartext-shop-Repo und kann daher **nicht bestätigen**, ob und wie diese
Dateien dort ankommen, oder ob klartext-mentoring.de aktuell überhaupt aus klartext-shop oder direkt
aus klartext-app bedient wird.

**Zu klären, bevor irgendetwas als „live" gilt:**
- Woher zieht klartext-mentoring.de aktuell tatsächlich seinen Inhalt — klartext-shop oder klartext-app?
- Falls klartext-shop: die heutigen Dateien müssen noch dorthin übertragen werden (ist NICHT automatisch passiert).
- Falls klartext-app direkt verbunden ist: dann ist der heutige Push zwar live, widerspricht aber der eigentlich beschlossenen Trennung – sollte dann bewusst neu entschieden werden, nicht stillschweigend so bleiben.

### Was heute konkret gemacht + nach GitHub gepusht wurde (Repo klartext-app, Branch main, Commit `0c11563`)
- Mobbing-Deck von 3 auf 15 Karten erweitert (Inhalte aus den 15 geprüften App-Modulseiten M6-01–15 kondensiert), neues PDF, neue Vorschaubilder, Verkaufsseite überarbeitet.
- Kaufen-Platzhalter („🛒 Jetzt kaufen" + ehrlicher „Zahlung in Vorbereitung"-Hinweis) auf allen 18 Verkaufsseiten.
- Wasserzeichen-Vorschaubilder für alle 18 Decks.
- AGB und Widerrufsbelehrung neu geschrieben, auf Primärquellen gestützt (u. a. §356 BGB-Neunummerierung entdeckt).
- Impressum korrigiert (ehrlicher Gewerbe-Status, korrekte Kontaktdaten, Datenschutz-Text, tote Links entfernt).

### Ist die Domain „fertig" (außer Hochbegabung + Platzhaltern)?
Nein, noch nicht ganz. Offen bleiben:
- Die Repo-Frage oben — aktuell die wichtigste offene Frage.
- Kaufen-Platzhalter: Deployment/Live-Stand nicht bestätigt (Task #217).
- Einheitliche Preisliste für alle 18 Decks — bisher nur Vorschlag, keine Freigabe (Task #220).
- Gewerbeanmeldung fehlt weiterhin — Voraussetzung für echten, verbindlichen Verkauf.
- Hochbegabung: bisher nur Konzept (Farbe, Themen, Quellen), keine Karten.

### App-Frage: Supabase auskoppeln (heute von Anja wieder aufgebracht)
War schon als offener Punkt dokumentiert (oben „Strang 3 · App-Aufspaltung", Stand seinerzeit: noch
nicht begonnen — weiterhin unverändert). Idee: eine reine INGRA-App ohne Supabase/Trägerverwaltung,
damit sie auch eigenständig als Handlungswerkzeug angeboten werden kann (ohne den Datenschutz-Rucksack
einer vollen Case-Management-Lösung), plus eine separate Trainer-App. Technischer Befund von damals
weiterhin gültig: DSGVO-sensibel sind konkret die Weiterleitungen (Migration 0008) und das
Kind-Barometer (Migration 0007) — die reinen Trainingsinhalte (M0–M8, Glossar, Karten) könnten
technisch auch ganz ohne Backend laufen. Empfehlung unverändert: rechtliche Prüfung durch eine
Datenschutzkanzlei vor der endgültigen Architekturentscheidung (das kann ich nicht als Rechtsberatung
leisten). **Noch nicht begonnen, wartet auf Anjas Priorisierung.**

### Fachbuch / Lernpfad / Trainerbuch — geprüft, kein akuter Korrekturbedarf durch die Mobbing-Erweiterung
Gefundene Dateien: `KLARTEXT_Fachbuch_System_Mobbing.html`, `KLARTEXT_Lernpfad_INGRA.html`,
`KLARTEXT_Trainerhandbuch.html`. Geprüft: keine der drei referenziert konkrete Mobbing-Kartenzahlen
oder MB-01 bis MB-15 — die heutige Erweiterung von 3 auf 15 Karten löst dort also **keinen** Zwang zur
Korrektur aus. `KLARTEXT_Fachbuch_System_Mobbing.html` war bereits am 30.07. als „redundant zu
M6-01–15, bleibt digital, keine Aktion" eingestuft. **Trotzdem offen, falls gewünscht:** Eine
vollständige inhaltliche Konsistenzprüfung dieser drei Dokumente gegen *alle* neuen Kartendeck-Inhalte
(nicht nur Mobbing) wurde bisher nie gemacht — wäre ein eigenes, größeres Vorhaben, noch nicht
begonnen.

### Konkrete Entscheidungen, die von Anja gebraucht werden
1. **Repo-Frage klären:** Läuft klartext-mentoring.de über klartext-shop oder klartext-app?
2. Falls klartext-shop: Zugriff auf das Repo geben, damit die heutigen Dateien dorthin übertragen werden können.
3. Supabase-Auskopplung: jetzt priorisieren oder zurückstellen?
4. Fachbuch/Lernpfad/Trainerbuch: vollständige Konsistenzprüfung gewünscht, oder erstmal nicht?

## Strang 30.1 · Nachtrag: klartext-shop-Abgleich erledigt + Korrektur Malteser-Timeline (02.08.2026, Fortsetzung)

**Zugriffs-Klarstellung:** Der obige "Wichtige, ungeklärte Befund" kam nicht aus einer Gedächtnislücke,
sondern daher, dass in dieser Sitzung zunächst nur der Ordner `klartext-app` verbunden war. Ich habe
grundsätzlich nur Zugriff auf Ordner, die Anja explizit für eine Sitzung freigibt — nicht automatisch
auf alles. `klartext-shop` wurde danach explizit angebunden.

**Ergebnis der Prüfung von klartext-shop:**
- Die `README_klartextshop.md` dort bestätigt schriftlich: klartext-shop ist absichtlich das getrennte
  Repo für *alle* Verkaufs-/Marketingseiten (Entscheidung 23.07., siehe oben) — genau wie vermutet.
- Der Stand dort war veraltet: `MB_Verkaufsseite.html` referenzierte noch die alte 3-Karten-Version,
  AGB und Widerrufsbelehrung fehlten komplett.
- Der Kaufen-Platzhalter (Task #217) war dort bereits vorhanden — eigener Commit `ff618f9` vom
  01.08.2026, unabhängig von der heutigen klartext-app-Arbeit. **Task #217 gilt damit als erledigt.**

**Abgleich durchgeführt:** `MB_Verkaufsseite.html` (15-Karten-Version inkl. Link-Fix), `SHOP_KLARTEXT_AGB.html`,
`SHOP_KLARTEXT_Widerrufsbelehrung.html`, `SHOP_KLARTEXT_Impressum.html` sowie die 6 neuen Vorschaubilder
(MB-01/05/12 vorne+hinten) von klartext-app nach klartext-shop übertragen und dort committet
(Commit `8866898`, „Mobbing-Deck 15 Karten + AGB/Widerruf/Impressum-Link-Fix aus klartext-app übertragen").
**Push nach GitHub steht noch aus — muss Anja selbst ausführen** (`git push origin main` im
klartext-shop-Terminal), da ich in dieser Sandbox keine GitHub-Zugangsdaten habe.

**Damit beantwortet:** Repo-Frage aus Entscheidung 1 oben ist geklärt — klartext-shop ist das richtige
Repo, der heutige Content ist jetzt dort synchronisiert (bis auf den ausstehenden Push).

**Weiterhin offen:**
- Bestätigung, dass klartext-mentoring.de tatsächlich mit klartext-shop (nicht klartext-app) als
  Cloudflare-Pages-Quelle verbunden ist — am sichersten direkt im Cloudflare-Dashboard prüfen: Workers &
  Pages → betreffendes Projekt → Settings → Build & deployments → verbundenes GitHub-Repo.
- Die `SHOP_*`-/`*_Verkaufsseite.html`-Dateien liegen jetzt **doppelt** vor (klartext-app + klartext-shop).
  Empfehlung: künftig nur noch in klartext-shop bearbeiten; die Duplikate in klartext-app sollten mittel-
  fristig entfernt werden, um genau dieses Auseinanderlaufen zu vermeiden (Löschung dort erst nach
  Anjas ausdrücklicher Freigabe, wie in klartext-app generell üblich).
- Gefundener, noch nicht behobener Bug: Die Fußzeilen-Links zu Impressum/Datenschutz zeigten in mehreren
  Verkaufsseiten auf eine alte, tote interne App-URL (`klartext-ingra.h9cyz7d9pj.workers.dev`). Bisher
  nur in `MB_Verkaufsseite.html` gefunden und behoben — die anderen 17 Verkaufsseiten wurden noch nicht
  geprüft.
- In klartext-shop liegt zusätzlich noch eine alte, ungenutzte `KLARTEXT_Impressum.html` (interne
  App-Version mit Login-Guard) neben der korrekten `SHOP_KLARTEXT_Impressum.html` — Aufräumen offen.

**Nachtrag (02.08.2026, gleiche Sitzung):** Alle 18 `*_Verkaufsseite.html`, die 5 `SHOP_KLARTEXT_*.html`,
`KLARTEXT_Shop_Uebersicht.html`, `SHOP_Landingpage.html` sowie der komplette `vorschau/`-Ordner wurden
aus **klartext-app** entfernt (Commit `b82409b`) — sie liegen jetzt inhaltlich identisch nur noch in
klartext-shop. Vorher geprüft: alle Dateien waren 1:1 identisch zur klartext-shop-Version, keine
verwaisten internen Links (bis auf `KLARTEXT_Barometer_kLAR_Erklaerung.html`, die 3x auf
`KLARTEXT_Shop_Uebersicht.html` verlinkte — dort auf die Live-Domain-URL
`https://klartext-mentoring.de/KLARTEXT_Shop_Uebersicht.html` umgestellt). Damit ist die Trennung aus
der 23.07.-Entscheidung jetzt tatsächlich durchgesetzt. **Beide Commits (klartext-app `b82409b`, davor
`b84b21b`; klartext-shop `8866898`) müssen noch von Anja gepusht werden.**

**Nachtrag (Push bestätigt):** Alle Commits erfolgreich gepusht. Domain-Bindung im Cloudflare-Dashboard
bestätigt: klartext-mentoring.de läuft als Production-Domain über das Pages-Projekt „klartext-shop",
verbunden mit Repo `anja2026-dev/klartext-shop`, Auto-Deploy bei jedem Push auf `main` aktiv (Commit
`8866898` erfolgreich live). Damit ist Entscheidung 1 aus der obigen Liste final geklärt.

## Strang 31 · Hochbegabungsdeck (HB) – volle Produktion (02.08.2026)

**Auslöser:** Konzept aus Strang 30 (Kobaltblau `#2024C4`, 12–15 Karten) von Anja freigegeben
(„weiter mit hochbegabung").

**Quellen tiefer verifiziert** (per Websuche, vollständige Angaben im PDF-Booklet):
Renzulli (1978, Phi Delta Kappan – Three-Ring Conception), Mönks (1990, Triadisches
Interdependenzmodell), Heller/Perleth/Hany (Münchner (Hoch-)Begabungsmodell, u. a. in Heller Hrsg.
2000), Gagné (DMGT), Rost/Uni Würzburg + Karg-Stiftung (Underachievement-Quote, als Spanne ca.
10–25% wiedergegeben, da Studien in Definition/Methodik variieren), aktuelle Twice-Exceptional-Forschung.

**Finale Struktur — 12 Karten in drei Blöcken:**
Erkennen (HB-01 Was ist Hochbegabung?, HB-02 Merkmale erkennen, HB-03 Asynchrone Entwicklung) ·
Herausforderungen (HB-04 Underachievement, HB-05 Perfektionismus & Versagensangst, HB-06 Soziale
Herausforderungen, HB-07 Doppelbegabung/Twice-Exceptional, HB-08 Langeweile & Verweigerung) ·
Handeln (HB-09 Enrichment & Akzeleration, HB-10 Diagnostik: wann testen?, HB-11 Zusammenarbeit mit
der Lehrkraft, HB-12 Elterngespräch bei Hochbegabung).

**Neu entwickelter Inhalt** (anders als bei den meisten anderen Decks gab es keine bestehende,
geprüfte App-Modulseite als Ausgangsbasis für Hochbegabung — daher kein Content-Treuepflicht-Fall,
sondern Neuentwicklung direkt auf Basis der oben genannten Quellen).

**Farbe kollisionsgeprüft:** Kobaltblau `#2024C4`, nächster Nachbar TK-Violett mit ca. 72 Einheiten
Abstand — unproblematisch.

**Pipeline gebaut** (analog Mobbing, icon-basiert, kein neues Bildmaterial): `build_card_hb.py`,
`build_all_cards_hb.py`, `build_booklet_hb.py`, `build_pdf_hb.py`. Alle 12 Karten gerendert, keine
Überlauf-Warnungen. `KLARTEXT_Hochbegabung_komplett.pdf` (27 Seiten: Cover, Anleitung, Quellen,
12×2 Karten) gebaut und visuell stichprobenartig geprüft — sauber.

**Verkaufsseite direkt in klartext-shop angelegt** (nicht in klartext-app — Lehre aus dem heutigen
Repo-Mismatch beherzigt): `HB_Verkaufsseite.html` mit 6 Vorschaubildern (HB-01/04/09, je
Vorder-/Rückseite, wasserzeichenversehen). `KLARTEXT_Shop_Uebersicht.html` und `index.html` um den
neuen HB-Eintrag ergänzt (Deck-Zähler 18 → 19). Dabei nebenbei eine veraltete MB-Kachel in der
Übersicht korrigiert (zeigte noch „3 Karten" statt der seit heute aktuellen 15).

**Commits:** klartext-app `d342dfa` (Pipeline + PDF), klartext-shop `8ee6505` (Verkaufsseite +
Vorschaubilder + Übersicht/Startseite). **Push durch Anja noch offen.**

**Noch offen:** Fachprüfung durch Anja vor Produktivsetzung (wie bei jedem neuen Deck) — inhaltlich
neu entwickelt, nicht aus bestehendem Modul kondensiert, daher besonders empfehlenswert. Preis noch
nicht in die Gesamt-Preisliste (Task #220) eingeordnet — vorläufig identisch zu MB übernommen
(Digital 8–10€, Print 18–20€).

## Strang 32 · Übergabe an Claude Free (Wochenlimit erreicht, 02.08.2026)

Anja ist bei >80% des wöchentlichen Cowork-Limits (Reset in 5 Tagen) und arbeitet in der Zwischenzeit
mit Claude Free (claude.ai, ohne Datei-/Repo-Zugriff) weiter. Vier Baustellen mit fertigen Start-Prompts
für Claude Free wurden vorbereitet und als `Claude_Free_Uebergabe.md` übergeben:
1. Gender-Sprache-Konsistenzprüfung (Konvention erst festlegen, dann Textabschnitte korrigieren)
2. Trainerhandbuch/Schulungen an alle Deck-Erweiterungen anpassen (MB 3→15, neues HB-Deck, LK 30→50,
   EL 58 Karten u.a.)
3. Konzeptpapier zur App-Trennung "INGRA-Lern-App ohne Backend" vs. "Supabase-Case-Management/TK"
   (Strang 3) — nur Konzeptebene, keine Rechtsberatung
4. Marketing-Kanalliste + erster Ankündigungstext

**Wichtig:** Claude Free kann nur Text entwerfen, keine Dateien ändern/committen. Ergebnisse bringt Anja
nach Ablauf der 5 Tage zurück, dann folgt die technische Umsetzung hier. Bis dahin bleiben liegen:
Supabase-Auskopplung selbst (#233), finale Preisliste aller 19 Decks (#220), klartext-shop-Landingpage
(#213), die tatsächliche Textkorrektur der Gender-Sprache in den ~200 HTML-Dateien, die tatsächliche
Trainerhandbuch-Überarbeitung.

**Nachtrag (06.08.2026):** Claude Free wurde nicht genutzt ("viel zu viel Aufwand") — die vier
Baustellen sind weiterhin offen und werden hier (Cowork) tokenarm nach und nach abgearbeitet, sobald
Wochenlimit es zulässt. `Claude_Free_Uebergabe.md` bleibt als Referenz nutzbar, falls sich das ändert.

## Strang 33 · Gender-Fix "Freundin"→"Freund:in" auch in App-Kartendaten (06.08.2026)

Tester-Meldung: Karte mit "Freundin" statt "Freund:in" gefunden (Anja wusste welche Karte nicht mehr).
Gefunden per Grep: EL-03 ("Erwartungen an mich selbst") und EL-27 ("Schuldgefühle als Elternteil"),
SYSTEMFRAGEN-Dict (Zirkuläre Frage) in `build_all_cards_el.py`. Korrigiert und neu gerendert
(Karten-PNGs, `KLARTEXT_EL-Deck_Basis_komplett.pdf`). Zusätzlich entdeckt: dieselbe Stelle war separat
in `pwa/data/el.json` (App-interne Kartendaten für den PWA-Viewer) noch mit dem alten Text vorhanden —
das ist der Teil, der tatsächlich in der App sichtbar war. Ebenfalls korrigiert.
**Commits:** `6bf061d` (Pipeline + PDF), `c92b33e` (pwa/data/el.json). Push durch Anja noch offen.

## Strang 34 · Neue Korrekturliste App-Formulare/Protokolle (gemeldet 06.08.2026, noch nicht bearbeitet)

Anja hat folgende Fehler/offene Punkte in klartext-app gesammelt gemeldet — noch keiner davon bearbeitet,
hier nur dokumentiert zur Priorisierung in den nächsten Sessions:

**Druckformat-Fehler (quer/hoch, Seitenumbruch):**
- Wochenreflexion-Karte: muss ins Querformat; Buttons grau/nicht klickbar
- Monatsbericht: muss ins Querformat beim Druck
- Übergabeprotokoll: ins Querformat beim Druck
- Schutzprotokoll + Essstörung-Bogen: laufen beim Druck über 2 Seiten
- Tagesinfo (Lehrkraft): Druckformat prüfen
- Start-Checkliste: Druckformat prüfen
- Alle Formulare/Protokolle systematisch auf Druck prüfen: quer/hoch richtig, 1 oder 2 Seiten

**Interaktivität/Funktionsfehler:**
- Alle Listen auf Interaktivität prüfen — Beispiel Fallprotokolle: nur der obere Bereich ist anklickbar,
  untere Felder nicht beschreibbar
- Selbstfürsorge-Bingo: soll interaktiv werden
- Downloads: Barometer dort nicht mehr funktionsfähig; unter "Kinder" sind noch alte Testkinder
  eingetragen (im Live-Bereich "Kinder" funktioniert es korrekt — Diskrepanz zwischen Downloads-Kopie
  und Live-Version)
- Notfallkontakte: Klick führt zur Startseite (Navigationsfehler)
- Zauberfächer: fehlt komplett als PDF und als interaktives Element

**Neue Features:**
- QR-Code auf Kartendecks einbinden (vermutlich Link zur externen Erklärseite/Kaufseite)
- Für Kartendruckerei: Karten müssen einzeln extrahierbar sein (nicht nur als ein PDF-Buch, das wird von
  Druckereien nicht angenommen) + 1-2 Musterkarten pro Deck als Einzeldateien für Anja
- Anja hat eine kuratierte 45-Karten-Auswahl für ein DIN-A5-Testdruck-Set vorgeschlagen (15× KD
  Grundschule/Brainy, 15× JD Jugendliche/Resilienz, 15× Fachkraft-Tools/Werkzeug+Krisendeck) — Auswahl
  liegt vor, noch nicht umgesetzt.

**Nächster Schritt:** mit Anja priorisieren, welche 2-3 Punkte zuerst angegangen werden (Umfang zu groß
für eine tokenarme Session am Stück).

## Strang 35 · Druckauftrag: 45-Karten-Testset für Kartendruckerei (06.08.2026)

Anja braucht Einzeldateien (nicht das Gesamt-PDF, das wurde von der Druckerei nicht angenommen) für einen
Testdruck-Auftrag, Auswahl 45 Karten aus KD/JD/Werkzeug/Krisendeck. Anjas erste Liste enthielt mehrere
ID/Titel-Verwechslungen mit dem echten Karteninhalt (aus anderer/externer Quelle übernommen) — nach
Rückfrage hat Anja eine korrigierte, gegen die echten Decks geprüfte Liste geliefert:
- KD (Grundschule/Brainy): 01,02,03,04,05,06,08,10,11,12,13,14,15,20,30 (15 Karten)
- JD (Jugendliche/Resilienz): 03,04,07,09,13,16,20,22,24,25,28,33,38,40,50 (15 Karten)
- WZ/Werkzeugkarten (Fachkraft-Tools): 01,05,09,10,11,12,13,15,18,20 (10 Karten, Anjas Liste nannte
  "M3-xx" — richtiges Präfix ist WZ-xx, gleiche Nummerierung)
- FK/Krisendeck (Akutintervention): 01,02,03,04,08 (5 Karten)

Alle vier Quelldecks komplett neu gerendert (KD 35, JD 52, WZ 26, FK 8 Karten), daraus die 45
ausgewählten extrahiert: je Vorder-/Rückseite als einzelne PNG (105×148mm/A6, 300dpi, print-ready), in
4 Ordnern nach Zielgruppe sortiert, als `Druckauftrag_45_Karten.zip` (90 Einzeldateien) bereitgestellt.

**Noch offen:** 1-2 Musterkarten aus jedem der ~19 Decks für Anja selbst (separater, kleinerer Wunsch,
noch nicht umgesetzt) — QR-Code auf Kartendecks ist ebenfalls noch offen (Strang 34).

## Strang 36 · NotebookLM-Fehlerliste verifiziert + Umlaut-Encoding-Fix M6/M7/MH (06.08.2026)

Anja hat extern (NotebookLM) eine Fehlerliste recherchiert. Jeder Punkt wurde vor Korrektur gegen den
echten Repo-Stand geprüft (nicht blind übernommen):

**Bestätigt und korrigiert:**
- **Umlaut-Encoding (ae/oe/ue statt äöü):** systematisch in allen 20 M7-Dateien, 8 MH-Dateien und 5 von
  10 M6-Dateien (M6-04–09) — echter, bisher unentdeckter Fehler, nicht nur in Titeln, auch in Fließtext
  (z. B. "Taeter" statt "Täter" in M6-04). Korrigiert per Skript mit manuell geprüfter Ausschlussliste
  (Wörter wie „Feuerwehr", „Quelle", „individuell", „aktuell", „neuen", „schauen", „steuern" enthalten
  zufällig „ae/oe/ue", sind aber korrekt geschrieben — blindes Suchen/Ersetzen hätte diese kaputt
  gemacht). CSS-Klassennamen (`box-gruen`, `col-gruen`, `gruen-bg`) bewusst als ASCII belassen, nur
  sichtbarer Text bekam Umlaute zurück. Zusätzlich 2 kaputte Encoding-Reste behoben: ein mit
  arabischen Schriftzeichen durchmischtes Wort in M7-10 ("herانfuehren" → "heranführen") und mehrere
  Tippfehler-Varianten (z. B. "kuenrzer" → "kürzer", "Frueehere" → "Frühere").
- **M2-42_ADHS_Ausbildungsreife.html:** Footer zeigte fälschlich "Karte 35" statt "Karte 42" (2 Stellen).
- **M2-27_Selektiver_Mutismus.html:** "Blosstellen" → "Bloßstellen", "Schaedlich" → "Schädlich".
- **KLARTEXT_Workbook.html:** Grammatikfehler "Situation wo ... darf" → "Situation, in der ... darfst".
- **MH-05:** "Selbst-herabsetzung" → "Selbstherabsetzung" (korrekte Zusammenschreibung).

**Noch offen — wichtig, nicht rausgelassen:**
- Die gleiche Umlaut-Stichprobe zeigt auch in **M0 (36), M2 (156) und M8 (250)** potenzielle Treffer —
  deutlich mehr als M6/M7/MH zusammen. Noch nicht geprüft/korrigiert, da jedes Wort einzeln gegen
  Fehlalarme (wie oben) geprüft werden muss. M1/M3/M4 zeigen nur einstellige Trefferzahlen, vermutlich
  überwiegend Fehlalarme.
- **Passwort "lehrerkraft"** in `KLARTEXT_Weitergabe_Erklaerung.html`: kommt nirgendwo sonst im Code vor
  (kein aktiver Passwort-Check gefunden) — vermutlich veraltete Dokumentation aus der Zeit vor Supabase.
  Nicht angefasst, da unklar ob/wo das noch real genutzt wird — Anja muss sagen, ob das weg kann oder
  korrigiert werden soll (und auf was).
- **Netlify-Referenz** in `KLARTEXT_Datenschutz.html` (Rechtstext!): Hosting lief laut Text über Netlify,
  ist aber auf Cloudflare Pages umgezogen. Nicht blind umgeschrieben, weil ein Datenschutztext korrekte
  Angaben zum tatsächlichen Hosting/Serverstandort braucht (Cloudflare-Rechenzentrum verifizieren, bevor
  der Text geändert wird) — eigener nächster Schritt.
- **Gender-Sprache (Kategorie 2 aus Anjas Liste):** Konvention Doppelpunkt ist bereits als Hausstandard
  etabliert (Strang zu LK_Glossar_Ergaenzung.html). Einzelne von Anja genannte Beispiele (z. B.
  "Schulbegleitung ist keine ... Freundin" in KLARTEXT_Fachbuch_Trainingsmodule.html) sind noch nicht
  entschieden, ob sie tatsächlich Fehler sind oder zulässige feminine Einzelform in einem beispielhaften
  Aufzählungssatz — braucht eine Grundsatzentscheidung von Anja, keine Automatik.
- Barometer-Speicherproblem (Downloads-Bereich) bereits in Strang 34 dokumentiert.

**Commit:** `bbb7e05`. Push durch Anja noch offen.

**Nachtrag (06.08.2026, M0/M2/M8 abgeschlossen):** Gleiche Methodik wie oben angewendet, 28 Dateien mit
echten Textänderungen. Zusätzlich 2 weitere Tippfehler gefunden: "beilaeufe Kommentare" →
"beiläufige Kommentare" (M8-11), "Kommunikationsabrueche" → "Kommunikationsabbrüche" (M8-12, fehlendes
"b"). Bonus-Fund: der "Zurück"-Button (Text + aria-label) hieß in vielen M2-Dateien "Zurueck" — jetzt
korrekt, verbessert auch die Screenreader-Aussprache. CSS-Klassennamen/IDs (u. a. `box-gruen`,
`sp-gruen`, `signal-koerper`, `staerken-grid`, `baro-uebersicht`) bewusst ASCII belassen — dabei zwei
neue versehentliche Klassennamen-Korruptionen durch das erste Skript selbst gefunden und zurückgesetzt,
bevor committed wurde. M1/M3/M4 nicht separat bearbeitet (nur einstellige Trefferzahlen, laut Stichprobe
ausschließlich False Positives wie "Feuerwehr"/"aktuell" — bei Bedarf jederzeit nachprüfbar).
**Commit:** `57dc1fa`.

Damit ist der von Anjas NotebookLM-Recherche gemeldete Umlaut-Fehler über M0/M2/M6/M7/M8/MH
(alle Bereiche mit auffälligem Befund) abgeschlossen.

**Nachtrag (06.08.2026, restliche offene Punkte geklärt):**
- **Passwort "lehrerkraft"** (KLARTEXT_Weitergabe_Erklaerung.html): korrigiert zu "lehrerkurs" — war ein
  Tippfehler, erkennbar am direkt danebenstehenden Block-Titel "🏫 Für Lehrkräfte — der Lehrerkurs" und
  am Parallelbegriff "elternkurs" beim Eltern-Zugang. Kein aktiver Passwort-Check im Repo gefunden, der
  davon abhängt — Risiko für echten Zugangsverlust war gering.
- **Netlify-Referenz** in KLARTEXT_Datenschutz.html: korrigiert auf Cloudflare Pages, mit tatsächlich
  recherchierten Fakten statt 1:1-Ersetzung (Cloudflare Inc., Rechenzentren EU+USA statt reinem
  EU/Frankfurt, DPA nach Art. 28 DSGVO, EU-US Data Privacy Framework + SCC als Rechtsgrundlage für
  US-Datenübermittlung). Quelle: Cloudflare Trust Hub (cloudflare.com/trust-hub/gdpr) und Cloudflare-DPA.
  Drei weitere, unkritische Netlify-Erwähnungen bleiben unangetastet (kein Rechtstext): in
  `KLARTEXT_Anleitung_Koordination.html` ist der Netlify-Link bereits korrekt als "funktioniert nicht
  mehr" markiert; `LK_Glossar_Ergaenzung.html` und `DASHBOARD.html` haben nur interne
  Entwickler-Notizen/Code-Kommentare — kleine Aufräumarbeit, kein Nutzer- oder Rechtstext.

## Strang 37 · Grundsatzentscheidung Gender-Sprache (bestätigt 06.08.2026)

**Entscheidung (Anja):** Neutrale Formulierungen werden bevorzugt, wo sie sich natürlich anbieten (z. B.
"Lehrkraft" statt "Lehrer/Lehrerin", "Fachkraft", "Schulbegleitung", "Einsatzleitung"). Wo eine neutrale
Formulierung unnatürlich oder umständlich wäre, gilt der **Gender-Doppelpunkt** als verbindlicher
Standard (z. B. "Freund:in", "Schulbegleiter:innen", "Mitschüler:innen") — diese Form ist im
pädagogisch-sozialen Bereich etabliert und üblich, in dem KLARTEXT eingesetzt wird. Nicht verwendet
werden: Schrägstrich-Form ("Lehrer/-in"), Binnen-I ("LehrerIn") oder generisches Maskulinum als
Ersatzform. Bestehende Paarformen ("Expertinnen und Experten") sind kein Fehler, sofern sie bewusst
gewählt sind, aber nicht der neue Standard für Neutexte.

Diese Konvention war bereits an mehreren Stellen faktisch etabliert (Strang zu LK_Glossar_Ergaenzung.html,
EL-Kartendeck-Fix Freund:in), ist hiermit aber explizit als projektweite Regel festgehalten — für alle
künftigen Korrekturen (auch die noch offene Vollprüfung, siehe Claude-Free-Übergabe Baustelle 1) und für
Anjas gemeldete Einzelbeispiele (z. B. "keine Freundin" in KLARTEXT_Fachbuch_Trainingsmodule.html), die
damit noch zu bewerten und ggf. zu korrigieren sind.

## Strang 38 · App-Trennung: was für reine Local-Storage-PWA (Shop-Version) fehlt (06.08.2026)

Anjas Ziel: die App als eigenständige, reine INGRA-Lern-PWA im Shop verkaufen — ohne Supabase/Träger-
Anbindung. Supabase erst einsetzen, wenn ein Träger es konkret will (dann folgt die DSGVO-Prüfung
separat). Codebase-Analyse ergibt eine **deutlich bessere Ausgangslage als befürchtet**:

**Befund 1 — nur 25 von >300 Dateien nutzen Supabase überhaupt:** Alle Kartendecks, Module M0-M8,
Fachbuch, Workbook, Glossar, Lernpfad, Trainerhandbuch sind bereits rein statisch/lokal (keine
Supabase-Aufrufe). Supabase steckt ausschließlich in den Case-Management-/TK-Funktionen: DASHBOARD.html,
CHAT_*, TK_*, KLARTEXT_Weiterleitungen.html, KLARTEXT_Zeitkonto.html, BAROMETER_KIND.html,
Kinderverwaltung.html, KLARTEXT_Krankmeldung/Listen/Notizblock/Portale/Tagesjournal/
Teilnehmer_Protokoll/UnserBuch/Urlaubsantrag.html, KLARTEXT_Login/Logout.html.

**Befund 2 — der Login ist der einzige zentrale Flaschenhals:** 344 Dateien (praktisch der gesamte
Content) prüfen nur `sessionStorage.getItem('klartext_login')==='true'` und leiten sonst zu
KLARTEXT_Login.html um. Dieses Flag wird aktuell ausschließlich nach erfolgreichem
`supabase.auth.signInWithPassword()` gesetzt. Für die Shop-Version reicht es, **eine** neue,
Supabase-freie Login-Seite zu bauen, die dasselbe Flag setzt (z. B. simples lokales Passwort wie beim
alten Lehrkraft/Eltern-Zugang) — die 344 Content-Dateien selbst müssten dafür nicht angefasst werden.

**Befund 3 — DASHBOARD.html mischt beide Welten:** Die zentrale Kachel-Seite verlinkt sowohl auf
Content (Module, Kartendecks, Fachbuch, pwa/index.html) als auch auf Case-Management (TK_*, Chat,
Zeitkonto, Barometer Kind, Notizblock, Krankmeldung...). Für die Shop-Version braucht es eine reduzierte
"DASHBOARD-Lite"-Variante, die nur die Content-Kacheln zeigt.

**Befund 4 — PWA-Offline-Abdeckung unvollständig:** Es gibt zwei getrennte Service Worker: `sw.js`
(Root, generisches Runtime-Caching ohne festen Precache) und `pwa/service-worker.js` (nur für den
Kartendeck-Viewer, mit festem Precache). Der Root-`manifest.json` `start_url` zeigt auf
`KLARTEXT_Login.html` (Supabase-Seite) — muss für eine reine PWA auf eine content-Startseite geändert
werden, sonst startet die installierte App immer im Login.

**Befund 5 (wichtig, unabhängig vom eigentlichen Thema entdeckt):** Die heute korrigierte
Datenschutzerklärung behauptet weiterhin "Zeitkonto-Einträge ... localStorage im eigenen Browser —
niemals auf einem Server" — das stimmt nicht mehr. `KLARTEXT_Zeitkonto.html` schreibt tatsächlich in
Supabase-Tabellen (`zeiteintraege`, `weiterleitungen`). Für die aktuelle Live-App (mit Supabase) ist die
Datenschutzerklärung an dieser Stelle **sachlich falsch** — unabhängig von der Shop-Frage, sollte das
zeitnah korrigiert werden (entweder Zeitkonto-Beschreibung anpassen oder klarstellen, dass dies nur für
den TK-Bereich gilt).

**Priorisierte Checkliste für die reine Shop-PWA:**
1. Supabase-freie Login-Alternative bauen (setzt `klartext_login`-Flag lokal, kein Backend-Call)
2. DASHBOARD-Lite ohne TK-/Case-Management-Kacheln erstellen
3. Die 25 Supabase-Dateien aus dem Shop-Paket ausschließen (nicht mit ausliefern)
4. `manifest.json` `start_url` + Root-`sw.js`-Precache auf Content-Seiten umstellen
5. Datenschutzerklärung für die Shop-Version separat pflegen (die aktuelle beschreibt ein Mischsystem;
   die Shop-Version wäre tatsächlich vollständig lokal — dort stimmt die "keine Serververarbeitung"-
   Aussage dann sogar wieder)
6. Zeitkonto-Aussage in der *aktuellen* (Supabase-)Datenschutzerklärung separat korrigieren (Befund 5)

**Noch offen / nicht Teil dieser Analyse:** Lizenzierung/Kopierschutz für eine verkaufte lokale
Kopie (aktuell kein Mechanismus vorgesehen — jeder mit der Datei hätte Vollzugriff), Preisfindung,
Umfang des Shop-Pakets (alle M0-M8 + alle Kartendecks, oder Auswahl).

## Strang 39 · Konzeptvorschlag Shop-Struktur (Anjas Vorgabe, 06.08.2026)

Anja hat entschieden: Supabase-Variante komplett aus der Shop-Planung raus, nur geparkt (Task #233
unverändert). Shop soll zwei Produkte bieten: Einzeldecks (bestehend) + Gesamt-App als neues Produkt.
Zusätzlich gewünscht: Freebie-Downloads zur E-Mail-Sammlung, Kunden-Zugang nach Kauf, eigener
Voll-Zugang für Anja (auch alle Kartendecks sichtbar). Anja bat um einen Vorgehensvorschlag, da ihr
unklar ist, wie man das "professionell" umsetzt.

**Vorschlag (voller Text in `Konzept_Shop_ohne_Supabase.md`, an Anja übergeben):**
1. Erst Inhalte angleichen — Fachbuch/Lernpfad/Trainerhandbuch fehlt Hochbegabung komplett, Mobbing-
   Erweiterung nicht nachgezogen. Deck für Deck, nicht alles auf einmal.
2. Website in vier Bereiche: (A) öffentlicher Verkaufsbereich (bestehend), (B) Freebie-Bereich mit
   E-Mail-Einsammlung über ein externes DSGVO-taugliches Tool (Brevo/CleverReach, gehört in Task #202),
   (C) Kaufbereich für das App-Produkt, (D) Anjas eigener Zugang — getrennt von der Kunden-Seite.
3. **Wichtigste Empfehlung:** Für das Kunden-Login/Download-Zugang beim App-Produkt kein eigenes
   Login-System selbst bauen (Datenbank, Passwort-Reset, DSGVO — genau der Aufwand, den Anja vermeiden
   will). Stattdessen eine digitale Verkaufsplattform mit automatischer Auslieferung nutzen
   (Vorschläge: Elopage, Digistore24 — beide deutsch, verbreitet bei Coaches/Trainer:innen; oder
   Lemonsqueezy international). Kunde kauft, bekommt automatisch Downloadlink/Kundenbereich — Anja
   muss dafür nichts entwickeln. Gehört mit in die laufende Recherche Task #202.
4. Anjas eigener "alles sehen"-Zugang läuft **nicht** über die öffentliche Shop-Website, sondern
   einfach über die App selbst (hier in klartext-app gepflegt) mit der Supabase-freien Login-Variante
   aus Strang 38 — sauberer getrennt von Kundensicht, keine zusätzliche Sicherheits-/Verwirrungsfrage
   auf der Verkaufsseite.

**Offene Entscheidungen bei Anja:** Wahl der Verkaufsplattform (Elopage/Digistore24/anders) und des
E-Mail-Tools — beide Themen an Task #202 angehängt. Bau-Arbeit (Login-Seite, DASHBOARD-Lite) kann
direkt hier übernommen werden, sobald gewünscht.

**Nachtrag (06.08.2026):** Anja hat gepusht. Workshops/Schulungen müssen ebenfalls überarbeitet werden
(gehört zu Baustelle 2 der Claude-Free-Übergabe, s. o.) — Anja ist sich aber noch unsicher, ob sie
Workshops/Schulungen schon aktiv anbieten möchte. Die inhaltliche Überarbeitung (Trainerhandbuch/
Schulungsunterlagen an neue Decks anpassen) läuft unabhängig von dieser Entscheidung weiter — die
"Anbieten ja/nein"-Frage ist rein Anjas Entscheidung und blockiert die technische/inhaltliche Vorarbeit
nicht.

**Marketing-Idee zur Prüfung: Kurzvideos aus Kartendecks für TikTok/Instagram.** Anjas Frage, meine
Einschätzung: grundsätzlich sinnvoll — die Decks haben durch Brainy-Illustrationen und klare Vorder-/
Rückseiten-Struktur bereits ein gutes visuelles Format für Kurzvideos (z. B. "Karte des Tages"
Flip-Reveal), und es ist günstige Zweitverwertung von bereits vorhandenem Content. Passt auch gut zum
geplanten Freebie-Bereich (kostenlose Kurzinhalte als Vertrauensaufbau vor dem Kauf). Zwei Vorbehalte:
(1) Bei sensiblen Themen (Krisenintervention, Kinderschutz, Mobbing) besteht Risiko, dass das
Kurzvideo-Format zur Trivialisierung verleitet — braucht bewusste redaktionelle Zurückhaltung bei der
Auswahl, welche Karten sich dafür eignen. (2) Reichweite auf TikTok/Instagram für eine Nischen-
Zielgruppe (Schulbegleitung/pädagogische Fachkräfte) ist ein Langstreckenspiel, kein schneller Hebel —
eher sinnvoll, nachdem Verkaufsplattform/Grundinfrastruktur stehen, nicht davor. Technisch umsetzbar
(einfache Slideshow-/Textoverlay-Videos aus vorhandenen Karten-PNGs lassen sich bauen) — noch nicht
begonnen, wartet auf Priorisierungsentscheidung.

## Strang 40: Inhaltserweiterung Hochbegabung (Fachbuch/Lernpfad/Trainerhandbuch)

Erste Runde der "Deck für Deck"-Inhaltsangleichung (s. Strang 39, Schritt 1) — Hochbegabung (12 Karten,
war bisher komplett unerwähnt in den Lernmaterialien).

1. **Neues Fachbuch-Systemkapitel S6:** `KLARTEXT_Fachbuch_System_Hochbegabung.html` — nach dem Muster
   von `KLARTEXT_Fachbuch_System_Mobbing.html`, 9 Abschnitte (Definition, Merkmale, Asynchrone
   Entwicklung, Underachievement, Perfektionismus/Versagensangst, Soziale Herausforderungen,
   Doppelbegabung/Twice-Exceptional, Niemals/Immer-Box, Zusammenarbeit mit Lehrkraft/Eltern), Quellenbox
   mit den 7 etablierten HB-Quellen (Renzulli 1978, Mönks 1990, Heller 2000, Gagné 2008,
   Marburger Hochbegabtenprojekt/Rost, Karg-Stiftung, Twice-Exceptional-Forschung). Verlinkung zu den
   Karten korrigiert auf `pwa/index.html?deck=hb` (kein eigenes HB-01.html — Deck läuft nur über PWA/PDF).
   In `KLARTEXT_Fachbuch_Neu.html` als S6-Navigationseintrag + im `PAGES`-Suchindex registriert.
2. **Lernpfad:** `KLARTEXT_Lernpfad_INGRA.html`, Woche 4 — Untertitel um "Hochbegabung" ergänzt, neue
   Aufgabe "Hochbegabung erkennen" (verlinkt auf das neue Systemkapitel) eingefügt, Karten-Link ergänzt.
   Wichtig: `TASKS.w4` im Fortschritts-Skript von 4 auf 5 erhöht (sonst falsche Prozentanzeige).
   Nebenbei gefunden und korrigiert: "Alle 6 Feuerwehr-Karten" → "Alle 8 Feuerwehr-Karten" (Krisendeck
   ist längst auf 8 Karten gewachsen, Text war nie aktualisiert worden).
3. **Trainerhandbuch:** `KLARTEXT_Trainerhandbuch.html`, Kapitel 6 (Schwierige Situationen) — neuer
   Abschnitt "Hochbegabung: das unterschätzte Thema", warnt vor dem verbreiteten Fehlschluss
   "die brauchen doch keine Unterstützung", Verweis auf das neue Systemkapitel S6.
4. **Workbook bewusst nicht angefasst** in dieser Runde — Workbook-Module sind strukturell an feste
   Kartennummern-Bereiche gekoppelt (eigene Fortschrittslogik pro Modul), eine saubere HB-Sektion wäre
   ein separater, größerer Schritt. War im ursprünglichen Schritt-1-Plan auch nicht explizit genannt
   (nur Fachbuch + Lernpfad + Trainerhandbuch). Bei Bedarf nachholbar.

**Nächster Schritt (noch nicht begonnen):** gleiche Angleichung für die Mobbing-Deck-Erweiterung
(3 → 15 Karten) in denselben drei Dateien.

## Strang 41: Hochbegabung in Quellenverzeichnis + Glossar

Nachtrag zu Strang 40 — Anja hat zurecht nachgehakt, dass Quellenverzeichnis und Glossar bei der
Inhaltserweiterung nicht vergessen werden dürfen.

1. **Quellenverzeichnis** (`KLARTEXT_Quellenverzeichnis.html`): neue Sektion 11 "Hochbegabung" mit
   7 recherchierten und verifizierten Quellen im APA-7-Format: Renzulli (1978, Three-Ring-Conception),
   Mönks & Ypenburg (2005, Triadisches Interdependenzmodell), Heller (Hrsg., 2000, Münchner
   Hochbegabungsmodell), Gagné (2009, DMGT 2.0), Rost (2000, Marburger Hochbegabtenprojekt), Reis/Baum/
   Burke (2014, Gifted Child Quarterly, Twice-Exceptional), Karg-Stiftung (Fachportal Hochbegabung).
   Filter-Button ergänzt, Hero-Zahlen korrigiert (91→98 Quellen, 9→11 Themenbereiche — dabei auch eine
   bereits vorher falsche Zahl bei "Alle"-Button gefunden und korrigiert: 73→98).
2. **Glossar** (`KLARTEXT_Glossar.html`): 4 neue Begriffe eingefügt — Hochbegabung, Asynchrone
   Entwicklung, Twice-Exceptional (Doppelbegabung), Underachievement — alphabetisch korrekt einsortiert,
   mit Quellenangabe und Verweis auf das neue Fachbuch-Systemkapitel S6. Hero-Zahl korrigiert (war
   bereits vorher falsch: 64 angezeigt, tatsächlich 53 vor dieser Änderung → jetzt korrekt 57).
3. Workbook-Hochbegabung bleibt bewusst offen — Anja hat bestätigt: "unbedingt, aber später" (Task #247).

**Offene Frage von Anja beantwortet:** Workshops/Schulungen sind noch NICHT inhaltlich überarbeitet —
das war bisher nur als Merkliste-Punkt vorgemerkt (s. Strang 39 Nachtrag), noch nicht begonnen.

## Strang 42: Inhaltserweiterung Mobbing (3→15 Karten)

Zweite Runde der "Deck für Deck"-Inhaltsangleichung — Mobbing-Deck (MB) war von 3 auf 15 Karten
gewachsen, ohne dass die Lernmaterialien das abbildeten. Befund bei der Recherche: Mobbing (M6-Modul,
15 Seiten) kam im gesamten Lernpfad bisher nur an einer einzigen, fehlerhaften Stelle vor.

1. **Fachbuch** (`KLARTEXT_Fachbuch_System_Mobbing.html`, bereits bestehendes Kapitel): Verweis auf das
   MB-Handlungskartendeck (15 Karten) ergänzt — bisher war nur auf die 30 Brainy-Geschichtenkarten
   verlinkt (kindgerechte Gesprächskarten), das MB-Deck (Sofortmaßnahme bis Nachsorge, für Fachkräfte)
   fehlte komplett. Verlinkung über `pwa/index.html?deck=mb` (verifiziert gegen `pwa/data/decks.json`).
2. **Lernpfad** (`KLARTEXT_Lernpfad_INGRA.html`): Mobbing war in der gesamten 13-Wochen-Struktur nicht
   verankert. Neue Aufgabe "Mobbing erkennen & begleiten" in Woche 10 (Kinderschutz — Erkennen &
   Handeln) ergänzt, `TASKS.w10` von 4 auf 5 erhöht. **Nebenbei einen echten Bug gefunden und behoben:**
   Woche 12 (Krisen & Feuerwehr) hatte eine Aufgabe "M6-01 lesen" mit der Beschreibung
   "Krisen-Definition — was ist eine echte Krise?" — das ist falsch, M6-01 heißt tatsächlich
   "Mobbing_erkennen.html". Beschreibung korrigiert, Link/Struktur unverändert gelassen (Mobbing kann
   in eine Krise eskalieren, passt inhaltlich noch in die Woche).
3. **Trainerhandbuch** (`KLARTEXT_Trainerhandbuch.html`): neue Methodenkarte im Methodenkoffer
   (Kapitel 5) — "Mobbing-Fallarbeit mit MB-Deck", beschreibt eine konkrete Trainingsübung mit dem
   15-Karten-Deck.
4. **Quellenverzeichnis**: 2 neue, verifizierte Quellen zur Mobbing-Sektion ergänzt, die die neuen
   MB-Karten (No-Blame-Approach, KiVa-Programm) fachlich absichern: Maines & Robinson (1992, No Blame
   Approach) und Kärnä, Voeten, Little, Poskiparta, Alanen & Salmivalli (2011, KiVa, Journal of
   Consulting and Clinical Psychology) — letztere mit korrigierter Erstautorenschaft recherchiert (die
   App-interne M6-15-Seite zitiert vereinfachend nur "Salmivalli et al.", Kärnä ist aber Erstautor;
   nicht in der App selbst geändert, nur im Quellenverzeichnis korrekt zitiert). Quellenzahl: 98→100.
5. **Glossar geprüft, nicht verändert:** "Mobbing" und "Cybermobbing" waren bereits als Begriffe
   vorhanden — kein Nachtrag nötig.

Damit ist die zweite von zwei ursprünglich benannten Prioritäten (Hochbegabung, Mobbing) abgeschlossen.

## Strang 43: Idee — eigenständiges Deck "Berufsvorbereitung / Übergang Arbeitswelt"

Bereits einmal angedacht (siehe FS-Erweiterungs-Analyse weiter oben: "Übergang Werkstatt/Arbeitswelt"),
damals aber als FS-Zusatzblock verworfen, weil Scope-Mismatch (FS = Grundschulalter). Jetzt als
eigenständige Deck-Idee festgehalten, nicht mehr an FS gekoppelt:

- **Zielgruppe:** Förderschule-Berufsvorbereitungsstufe / Sek II (ca. 16–18 Jahre) — eigene Altersstufe,
  bisher von keinem bestehenden Deck abgedeckt (JD-41–44 "Berufsvorbereitung" ist ein Zusatzblock
  innerhalb des JD-Decks, kein eigenständiges Produkt, und richtet sich an jüngere Jugendliche).
- **Möglicher Aufbau:** analog zum EL-JD-Muster (eigene Bilder, adaptierte/vertiefte Texte statt reiner
  Kopie), Themen z. B. Praktikum, Bewerbung, Arbeitsalltag, Konflikte im Team, Selbstständigkeit im
  Berufsalltag, Übergang Schule → Werkstatt/Ausbildung.
- **Status:** reine Idee, noch keine Konzeptarbeit begonnen. Aufgreifen sobald Kapazität da ist oder
  konkreter Bedarf (z. B. von einem Träger) gemeldet wird.

## Strang 44: Supabase-freie Login-Seite + DASHBOARD-Lite (Shop-PWA-Vorbereitung)

Umsetzung von Option 2 aus dem Strang-38-Fahrplan: erste zwei von sechs Schritten, um die App
perspektivisch als reines lokales PWA-Produkt im Shop anbieten zu können, komplett unabhängig von
Supabase/Träger-Fallmanagement.

**1. `KLARTEXT_Login_Shop.html` (neue Datei):** eigenständige, rein clientseitige Login-Seite im
bestehenden Login-Design, aber ohne Supabase-Anbindung — nur ein Passwortfeld, kein E-Mail-Feld, keine
Rollenauswahl. Setzt bei Erfolg exakt dieselben sessionStorage-Flags (`klartext_login`, `klartext_role`,
`klartext_display_name`), die alle 344 bestehenden Content-Seiten bereits prüfen — an diesen Seiten
musste dadurch nichts geändert werden. Passwort aktuell `klartext-start`, im Quelltext als Klartext
hinterlegt (im Code kommentiert: das ist keine echte Zugriffskontrolle, sondern verhindert nur
versehentliches Öffnen — vor dem Verkauf anpassen, perspektivisch ggf. pro Kunde individuell). Leitet
nach Login auf `DASHBOARD_Lite.html` weiter, "Passwort vergessen"-Hinweis per Mailto.

**2. `DASHBOARD_Lite.html` (neue Datei):** Supabase/Firebase/Fallmanagement-freie Variante von
`DASHBOARD.html`, per verifizierter Text-Chirurgie (Python, exakte Marker-Ersetzung mit
Eindeutigkeits-Check vor jedem Schritt) aus der Originaldatei erzeugt, um die 100%ige Texttreue aller
beibehaltenen Inhalte (alle M0–M8/MH/LK/KD/FK/Lernmaterialien-Kacheln) zu garantieren. Entfernt wurden:

- Firebase-SDK-Einbindungen und der komplette Chat-Code.
- Rollenbasierte lk/eltern-Weiterleitungslogik beim Login-Check (Lite hat nur eine Rolle: admin).
- Mobile-Dashboard-Block komplett ersetzt durch eine vereinfachte, reine Content-Navigation (FK-Grid
  und Modul-Dropdown bleiben erhalten).
- Header: Kind-Barometer-Link und TK-Bereich-Button entfernt, Logout zeigt jetzt auf
  `KLARTEXT_Login_Shop.html`.
- Global-Nav/Quick-Nav: nur noch Dashboard/Kartendecks/Fachbuch/Feuerwehrkarten/Downloads/Spiele; TK-
  Filter-Chip und Tools-Bereichsfilter entfernt.
- Beta-Banner-Block (Code+Skript) komplett entfernt.
- Sektionen `sek-feedback`, `sek-tk`, `sek-tk-recruiting`, `sek-tools` vollständig entfernt (alle
  Fallmanagement-/Träger-spezifisch).
- Rollenbasiertes `HIDE`-Konfigurationsskript (LABELS/FARBEN/HIDE-Objekte, Rollen-Badge-Logik,
  data-trainer-only/data-admin-only/data-expert-only-Filterung) komplett entfernt — für ein
  Ein-Rollen-Lizenzmodell nicht mehr nötig.
- Rollenabhängiges "Feedback-Banner"-Skript entfernt (Zielklassen existierten nach Entfernung von
  `sek-feedback` ohnehin nicht mehr).
- Selbstreferenzen konsistent gemacht: Logo-Link und "Dashboard"-Menüpunkt zeigen jetzt auf
  `DASHBOARD_Lite.html` statt `DASHBOARD.html`.

**Verifiziert:** finale Datei enthält keine `supabase`/`firebase`/`chat.js`/`BAROMETER_KIND`/
`feedback.html`/`feedbackAdmin`/`TK_*`/`tk-bereich`-Referenzen mehr (Grep-Check sauber, einzige
verbliebene Treffer für "Supabase" sind erklärende Kommentare im Login-Skript selbst). Struktur
gegengeprüft: `<div>`-Öffnungen/Schließungen (1110/1110) und `<section>`-Öffnungen/Schließungen (19/19)
balanciert.

**Bewusst unverändert gelassen:** die als Logout-Fab verlinkte `KLARTEXT_Landing.html` (Supabase-frei,
reine Marketing-Seite) — Ziel bleibt dasselbe wie im Original.

**Noch offen aus dem Strang-38-Fahrplan (Schritte 3–6):**
3. Die 25 Supabase-abhängigen Dateien (TK_*, CHAT_*, BAROMETER_KIND, feedback*, Zeitkonto,
   Krankmeldung, Urlaubsantrag, Notizblock, Teilnehmer-Protokoll, Listen, Weiterleitungen) aus dem
   Shop-Paket ausschließen (Packaging/Distributionsfrage).
4. `manifest.json` `start_url` und `sw.js`-Precache-Liste auf Content-Seiten statt Supabase-Login
   umstellen.
5. Eigene Datenschutzerklärung für die Shop-Version.
6. Zeitkonto/Datenschutz-Widerspruch in der aktuellen (Supabase-)Datenschutzerklärung
   (Befund 5 aus Strang 38) — wartet weiter auf Anjas Entscheidung zur Neuformulierung.

## Strang 45: Shop-Paket-Ausschlussliste + Build-Skript (Strang 38, Schritt 3)

**Neue Dateien:**
- `SHOP_PACKAGE_AUSSCHLUSSLISTE.md` — dokumentiert und begründet, welche Dateien/Ordner aus dem
  Supabase-freien Shop-Paket ausgeschlossen werden müssen: 31 funktional Supabase-/Firebase-abhängige
  HTML-Seiten (per Grep auf echte API-Aufrufe verifiziert, nicht nur Text-Erwähnungen — z. B. zählen
  Trainerhandbuch/Systemanleitung NICHT dazu, die erwähnen Firebase nur in Fließtext), 2 interne
  Planungs-/Architektur-Dokumente (`Admin_Backend.html`, `KLARTEXT_Vertretungsassistent_Architektur.html`),
  plus 4 komplette Ordner (`.git/`, `supabase/` [39 SQL-Migrationen], `__pycache__/`, `storybooks/`
  [geparkte Produktlinie, Strang 6]).
- `build_shop_package.sh` — rsync-basiertes Build-Skript, kopiert das Repo unverändert in einen
  Zielordner unter Ausschluss der obigen Liste, mit `--dry-run`-Option zum Testen ohne Kopieren, und
  einem automatischen Nachher-Check (Grep auf verbliebene funktionale Supabase/Firebase-Aufrufe im
  Zielordner).

**Getestet:** Dry-Run bestätigt korrekten Ausschluss aller 33 Einzeldateien + 4 Ordner. Echter Testlauf
nach `/tmp/shop_test` erfolgreich (969 MB, 382 HTML-Dateien, `DASHBOARD_Lite.html` +
`KLARTEXT_Login_Shop.html` vorhanden, `DASHBOARD.html`/`KLARTEXT_Login.html`/`supabase/` korrekt
entfernt, Nachher-Check meldet keine funktionalen Supabase/Firebase-Reste). Testordner wieder gelöscht,
nichts im Haupt-Repo verändert.

**Offen (unverändert, Strang 38 Schritte 4–6):** manifest.json/sw.js-Precache umstellen, eigene
Datenschutzerklärung für die Shop-Version, Zeitkonto/Datenschutz-Widerspruch klären. Zusätzlich notiert:
Trainerhandbuch/Systemanleitung enthalten je 1–2 Firebase-Prosaverweise (Kind-Barometer-Sync, Chat), die
vor dem Verkauf inhaltlich an die Lite-Version angepasst werden sollten — kleiner Folge-Task, kein
Blocker für die Paket-Erstellung.

## Strang 46: Datenschutzerklärung (Live-App) — vollständige Überarbeitung (Befund 5 + Nachfolgebefunde)

Ursprünglich sollte nur eine falsche Formulierung korrigiert werden (Befund 5, Strang 38: Zeitkonto
angeblich "localStorage ... niemals auf einem Server"). Bei der Prüfung anhand des tatsächlichen Codes
kam heraus, dass das Problem deutlich größer ist. Anja wurde dazu befragt und hat für die vollständige
Überarbeitung entschieden.

**Verifizierte Fakten (per Grep gegen den tatsächlichen Code, nicht nur gegen die Doku):**
- **Zeitkonto-Einträge** landen tatsächlich in Supabase (Tabelle `zeiteintraege`), nicht in localStorage.
- **Workbook-Antworten** (`KLARTEXT_Workbook.html`) landen entgegen der bisherigen Behauptung nicht
  einmal in localStorage — `wbStore` ist ein reines In-Memory-JS-Objekt (Kommentar im Code: "funktioniert
  zuverlässig bei file://"), Eingaben gehen beim Schließen/Neuladen der Seite komplett verloren.
- **Login** (`KLARTEXT_Login.html`) läuft über `supabase.auth.signInWithPassword()` mit echter
  E-Mail-Adresse — nicht rein sessionStorage-lokal, wie die alte Tabelle suggerierte.
- Die gesamte Datenschutzerklärung erwähnte an keiner Stelle Supabase, Firebase, TK-Fallmanagement,
  Kind-Barometer oder Chat — obwohl diese Funktionen in der Live-App bei der Partnerorganisation aktiv
  genutzt werden und dabei u. a. **Daten über Kinder** verarbeiten (Tabelle `barometer_kind`: Kind-ID,
  Stimmungs-/Ampel-Farbe, optionale Notiz — Selbstauskunft des Kindes).
- Abschnitt 5 (alt) behauptete "Anwendungsbereich der DSGVO auf das technische Hosting beschränkt" — für
  den TK-Bereich sachlich falsch.
- Abschnitt 6 (alt) behauptete, Löschanfragen ließen sich generell durch Löschen von Browser-Daten
  erfüllen — für Supabase-/Firebase-gespeicherte TK-Bereich-Daten falsch.

**Umgesetzte Überarbeitung von `KLARTEXT_Datenschutz.html`:**
1. Neues Grundkonzept: Dokument unterscheidet durchgängig zwischen **Lern-/Kartendeck-Bereich** (weiterhin
   zutreffend: kein Server, keine Datenbank) und **TK-Bereich** (Supabase + Firebase, echte
   personenbezogene Daten, teils über Kinder).
2. Abschnitt 3 in 3a/3b aufgeteilt: 3a mit korrigierter Workbook-Zeile (In-Memory statt localStorage),
   3b neu — Tabelle mit allen TK-Bereich-Datenkategorien (Anmeldedaten, Kind-Barometer, Fallmanagement,
   Chat, Zeitkonto, Krankmeldungen/Urlaubsanträge, Notizblock/Teilnehmer-Protokoll/Listen/Weiterleitungen)
   mit den tatsächlichen Supabase-Tabellennamen bzw. Firebase für den Chat, plus Hinweisbox zur besonderen
   Schutzbedürftigkeit von Kinderdaten.
3. Neuer Abschnitt 5 "Supabase & Firebase" (analog zum bestehenden Cloudflare-Abschnitt), inkl. offen
   markiertem Hinweis: Serverstandort und AVV (Art. 28 DSGVO) für das konkrete Supabase-Projekt bzw. die
   Firebase-Instanz sind hier **nicht bestätigt** — sollte vor produktivem Einsatz mit echten Kind-/
   Mitarbeitendendaten geklärt werden.
4. Abschnitt 6 (Rechtsgrundlagen, vormals 5): falsche DSGVO-Nichtanwendbarkeits-Aussage entfernt, korrekte
   Rechtsgrundlagen für TK-Bereich ergänzt, Hinweis auf Art. 8 DSGVO (Kinder) und ggf. nötige
   Datenschutz-Folgenabschätzung nach Art. 35 — explizit als *nicht abschließend geklärt* markiert.
5. Abschnitt 7 (Rechte, vormals 6): Löschrecht-Aussage in zwei Teile aufgeteilt — Lern-/Kartendeck-Bereich
   (zutreffend: keine Serverdaten) vs. TK-Bereich (Daten liegen bei Supabase/Firebase, Anfragen direkt an
   Anja).
6. Abschnitt 8 (vormals 7): ergänzt um Supabase/Firebase als weisungsgebundene Auftragsverarbeiter.
7. Hero-Badge und Grundsatz-Abschnitt (2) entsprechend umformuliert, Stand-Datum auf 06.08.2026 aktualisiert.
8. Neue CSS-Klasse `.hinweis-box` (Amber/Orange) für Warnhinweise ergänzt, analog zur bestehenden
   `.gruen-box`.

**Wichtiger Vorbehalt (an Anja kommuniziert, nicht nur hier dokumentiert):** Diese Überarbeitung macht die
Beschreibung *technisch zutreffend* (sie entspricht jetzt dem tatsächlichen Code-Verhalten) — sie ersetzt
aber **keine juristische Prüfung**. Insbesondere die konkrete Rechtsgrundlage für die Verarbeitung von
Kind-Barometer-/Fallmanagement-Daten, die Frage einer Datenschutz-Folgenabschätzung, und die AVV-Situation
mit Supabase/Firebase sind als offene Punkte im Dokument selbst markiert (Hinweisboxen) und sollten vor
Weiterverwendung von einer datenschutzrechtlich versierten Fachperson bzw. der Partnerorganisation
gegengeprüft werden — insbesondere weil es um Daten von Kindern geht.

**Nicht Teil dieser Überarbeitung:** eine separate Datenschutzerklärung für die Shop-Version (Strang 38,
Schritt 5) — dort wäre die alte "kein Server"-Aussage tatsächlich wieder korrekt, da das Shop-Paket
laut `SHOP_PACKAGE_AUSSCHLUSSLISTE.md` komplett ohne Supabase/Firebase ausgeliefert wird. Bleibt offen.

## Strang 47: manifest.json fürs Shop-Paket (Strang 38, Schritt 4)

**Befund:** Root-`manifest.json` zeigt über `start_url` auf `KLARTEXT_Login.html` (Supabase) — diese
Datei ist Teil der Ausschlussliste (Strang 45) und existiert im Shop-Paket nicht. Eine installierte
Shop-PWA hätte damit beim Start ins Leere gezeigt (404). `pwa/manifest.json` (Kartendeck-Viewer) sowie
`sw.js`/`pwa/service-worker.js` waren dagegen bereits unkritisch: `pwa/manifest.json` zeigt auf
`./index.html` (Supabase-frei), `sw.js` cached nur zur Laufzeit ohne feste Precache-Liste, und
`pwa/service-worker.js`s feste `SHELL_FILES`-Liste enthält ausschließlich PWA-eigene, Supabase-freie
Dateien.

**Umsetzung:** Neue Datei `manifest_shop.json` (identisch zu `manifest.json`, außer `start_url` →
`KLARTEXT_Login_Shop.html`, Beschreibungstext angepasst). `build_shop_package.sh` kopiert diese Datei
nach dem rsync-Schritt automatisch als `manifest.json` ins Zielverzeichnis (überschreibt die
mitkopierte Live-Variante). `manifest_shop.json` selbst ist von der rsync-Übertragung ausgeschlossen,
damit sie nicht zusätzlich als eigene Datei im Paket landet.

**Getestet:** Kompletter Testlauf nach `/tmp/shop_test2` — `manifest.json` im Ergebnis zeigt korrekt auf
`KLARTEXT_Login_Shop.html`, `KLARTEXT_Login.html` ist wie erwartet nicht vorhanden, Nachher-Check weiterhin
sauber. Testordner gelöscht, Haupt-Repo unverändert (nur die zwei neuen Dateien + Skript-Anpassung).

**Damit sind Strang-38-Schritte 1–4 vollständig umgesetzt.**

## Strang 48: Eigene Datenschutzerklärung für klartext-shop (Strang 38, Schritt 5)

Neue Datei `SHOP_KLARTEXT_Datenschutz.html` im **klartext-shop**-Repo (nicht klartext-app) angelegt,
konsistent mit dem dortigen Namensmuster `SHOP_KLARTEXT_AGB.html`/`SHOP_KLARTEXT_Widerrufsbelehrung.html`.
Begründung für den Ort: das Dokument beschreibt sowohl die Verkaufsseiten selbst (klartext-shop) als auch
das verkaufte Produkt (App-Version) — es ist ein Shop-/Verkaufsdokument, kein App-internes.

**Inhalt, in zwei Teile getrennt:**
- **§ 2 Diese Website:** Cloudflare-Hosting, kein Tracking/Cookies, E-Mail-Bestellablauf (Name, E-Mail,
  Bestellwunsch, ggf. Adresse), Zahlung per Überweisung/PayPal (mit Verweis auf PayPal-Datenschutz),
  Hinweis dass ein automatisierter Zahlungsanbieter noch nicht angebunden ist.
- **§ 3 Das Produkt:** PDF-Kartendecks (keine Datenverarbeitung, statische Dateien) sowie die geplante
  App-Version — hier korrekt beschrieben als lokal/serverlos (Passwort-Prüfung rein clientseitig, Workbook
  nur im Arbeitsspeicher), im Unterschied zur separaten Supabase-Trägerversion, die klartext-shop nicht
  betrifft. Damit stimmt hier die "kein Server"-Aussage tatsächlich, anders als in der (jetzt in Strang 46
  korrigierten) App-eigenen `KLARTEXT_Datenschutz.html`.

**Nebenbefunde behoben:** Impressum verlinkte bisher nur einen Platzhaltertext ("wird ergänzt, sobald
weitere Dienste eingebunden sind") statt einer echten Erklärung — jetzt korrekt verlinkt. AGB § 12 verwies
ebenfalls nur auf "Informationen im Impressum" — jetzt direkt verlinkt. Zusätzlich festgestellt: AGB und
Widerrufsbelehrung waren auf der Startseite (`index.html`) bisher gar nicht verlinkt (nur über Impressum
erreichbar) — Footer um Datenschutz/AGB/Widerrufsbelehrung ergänzt, damit alle drei direkt erreichbar sind.

**Wie schon bei den AGB üblich:** Hinweisbox am Anfang markiert den Entwurfsstatus und empfiehlt
rechtliche Prüfung vor automatisiertem Zahlungsanbieter-Einsatz — konsistent mit dem bestehenden
Hinweis-Muster in `SHOP_KLARTEXT_AGB.html`.

**Damit ist auch Strang-38-Schritt 5 umgesetzt.** Offen bleibt weiterhin die generelle Frage nach
Lizenzierung/Kopierschutz für die verkaufte lokale App-Kopie (bisher kein Mechanismus vorgesehen — siehe
Anjas Rückfrage dazu, separat beantwortet).

**Lizenzierung/Kopierschutz (06.08.2026):** Anja recherchiert das selbst, zurückgestellt. Optionen
skizziert (Einzelpasswörter pro Kundin / Lizenzserver-Check / gar nichts, analog zur bestehenden
Nutzungsrechts-Klausel bei den PDF-Decks) — keine weitere Aktion, bis sie sich meldet.

## Strang 49: Trainerhandbuch-Wortwahl + eigene Systemanleitung fürs Shop-Paket

**Trainerhandbuch** (`KLARTEXT_Trainerhandbuch.html`): 2 Stellen, die explizit "Firebase" nannten
("Internet für Firebase-Funktionen", "Technische Probleme (Firebase/Login funktioniert nicht)"), auf
generische Formulierung umgestellt ("Internetverbindung", "Login funktioniert nicht") — jetzt für
Live- und Shop-Version gleichermaßen zutreffend, keine inhaltliche Änderung sonst.

**Systemanleitung — größerer Befund als angenommen:** Die ursprüngliche Einschätzung ("1–2 Sätze")
war zu knapp. Beim genauen Lesen von `KLARTEXT_Systemanleitung.html` zeigt sich: ~70 % des Inhalts ist
TK-Bereich-spezifisch — komplette Abschnitte zu Nachrichten/Chat, Weiterleitungen, TK-Inbox, Zeitkonto,
Notizblock, Urlaubsantrag/Krankmeldung, plus eine "Wer ist wer"-Rollenübersicht mit vier Rollen
(INGRA/TK/Lehrkraft/Eltern), die es im Shop-Paket (eine einzige Rolle) gar nicht gibt. Die Datei ist zwar
funktional Supabase-frei (kein Code-Aufruf), aber inhaltlich für einen Shop-Kunden irreführend — sie war
sogar mit einem auffälligen "✨ Neu"-Badge zweimal in `DASHBOARD_Lite.html` verlinkt.

**Lösung:** Neue eigenständige Datei `KLARTEXT_Systemanleitung_Shop.html` — enthält nur, was im
Shop-Paket tatsächlich existiert: Dashboard-Aufbau, Quick-Start (Kartendeck öffnen, Barometer, Workbook,
Fachbuch), die neun Module, INGRA-Barometer (ohne Kind-Barometer/Brainy-Coach-Chat), Joker-Konzept,
Downloads, ein expliziter Workbook-Hinweis (In-Memory, nicht dauerhaft gespeichert) und eine
Shop-passende Häufige-Fragen-Sektion. `DASHBOARD_Lite.html`s zwei Verlinkungen auf die alte Datei
umgestellt. Die alte `KLARTEXT_Systemanleitung.html` zusätzlich in `SHOP_PACKAGE_AUSSCHLUSSLISTE.md` und
`build_shop_package.sh` aufgenommen, damit sie gar nicht erst im Paket landet (nur noch `DASHBOARD.html`,
die Live-Version, verlinkt sie).

**Getestet:** Kompletter Buildlauf — alte Systemanleitung fehlt im Paket, neue Shop-Variante vorhanden,
`DASHBOARD_Lite.html` im Paket verlinkt korrekt auf die neue Datei, Nachher-Check weiterhin sauber.

**Nebenbefund, nicht behoben:** `BAROMETER_INGRA.html` (im Shop-Paket enthalten) verlinkt auf
`BAROMETER_KIND.html` (ausgeschlossen) — toter Link innerhalb einer sonst unkritischen Seite. Kleiner
Folge-Task, noch offen.

## Strang 50: Verifikation Hochbegabung/Mobbing-Abdeckung — zwei Dokumente fehlen noch

Auf Anjas Rückfrage hin geprüft, ob Lernpfad, Lernhandbuch, Fachbuch und Curriculum alle
Hochbegabung/Mobbing berücksichtigen:

- **Lernpfad** (`KLARTEXT_Lernpfad_INGRA.html`): ✅ bestätigt — 3 Hochbegabung- und 4 Mobbing-Treffer
  (Woche-4-Task, Woche-10-Task + Woche-12-Bugfix aus Strang 40/42).
- **Fachbuch** (`KLARTEXT_Fachbuch_System_Hochbegabung.html` + `KLARTEXT_Fachbuch_System_Mobbing.html`):
  ✅ bestätigt — eigenes HB-Systemkapitel existiert, MB-Kapitel verlinkt zweifach auf das 15-Karten-Deck.
- **Trainerhandbuch**: ✅ bestätigt (Strang 40/42, plus Wortlaut-Fix aus Strang 49).
- **Lernhandbuch** (`KLARTEXT_Lernhandbuch_KOMPLETT.html`, 5386 Zeilen/449 KB): ❌ **nicht berücksichtigt**.
  Nur 1 zufälliger Hochbegabung-Treffer (keine echte HB-Sektion), 31 Mobbing-Treffer wirken auf den
  ersten Blick besser, sind aber nicht verifiziert vollständig für den 15-Karten-Stand. Datei zuletzt am
  23.07. geändert — vor der Hochbegabung-Kartenproduktion, Datum passt zum Befund.
- **Curriculum** (`KLARTEXT_Curriculum_Trainer-Leitfaden_12_Wochen.html`, 756 Zeilen): ❌ **nicht
  berücksichtigt**. 0 Hochbegabung-Treffer, nur 4 Mobbing-Treffer (wahrscheinlich nur die alte
  3-Karten-Fassung).

**Status:** Anjas Frage war berechtigt — zwei von sechs relevanten Dokumenttypen fehlen noch. Beide sind
größere, manuell kompilierte Referenzdokumente (kein Auto-Sync aus den Einzelmodulen), das
Lernhandbuch insbesondere sehr umfangreich. Bevor hier reingegangen wird, sollte die Struktur beider
Dokumente erst genauer gesichtet werden (wie sind Themen dort organisiert, wo würde HB/MB inhaltlich
reinpassen), um keine oberflächliche Ergänzung zu riskieren. Priorisierung mit Anja offen — sie hatte für
diese Runde zunächst Workshops/Schulungen vor Augen.

## Strang 51: Verkaufsseite (klartext-shop) an echte Shop-Lite-Version angepasst + verlinkt

Nach Anjas Hinweis "hier sind ja nur die Kartendecks drin, alle anderen Materialien bzw die App ist
nicht drin" geprüft: Es gab bereits eine vollständig gestaltete `KLARTEXT_Verkaufsseite.html` im
klartext-shop-Repo (420 Zeilen, Hero/Für-wen/Leistungen/Barometer/kLAR/Zitat/Preise/Referentin/FAQ),
war aber nirgends verlinkt — und beschrieb die alte Supabase/Träger-Version, die genau den Funktionen
widerspricht, die in der neuen Shop-Lite-App (Strang 44–50, ohne Supabase) gar nicht existieren.

**Korrigiert:**
- Praktische-Tools-Karte: "Zeitkonto, Krankmeldung, Urlaubsplan" → "Workbook, Fachbuch, Glossar,
  Quellenverzeichnis, Downloads" (echte Lite-Tools).
- Koordinator:innen-Zielgruppentext: "Urlaubsplanung" raus (keine Team-Verwaltung ohne Backend).
- INGRA-Basis-Preistier: "Barometer INGRA + Kind" → "INGRA-Barometer" (Kind-Barometer ist
  Supabase-Sync, existiert in Lite nicht), "Zeitkonto + Krankmeldung" → "Fachbuch +
  Quellenverzeichnis".
- Preistier "Träger-Paket" → umbenannt zu "Team-Zugang": TK-Zugang/Urlaubsplan-für-das-Team/
  individuelle Anpassungen (impliziert Backend-Customizing, das es nicht gibt) raus, ersetzt durch
  "Mehrere Lizenzen für dein Team", Sammelrechnung, Staffelpreis — ehrliches Bulk-Lizenz-Angebot statt
  Software-Team-Feature.
- Fortbildung-Preistier unverändert gelassen (Präsenztraining, hängt nicht an Supabase).
- FAQ "Wie bekomme ich meinen Zugang?": automatisiertes "Zugangscode per E-Mail innerhalb von 24
  Stunden"-Versprechen (nicht gebaut) entfernt, ersetzt durch manuellen Anfrage-Flow wie im Rest vom
  Shop.
- FAQ Datenschutz: falsche Behauptung "Notizen und Zeitkonto bleiben nur auf deinem eigenen Gerät"
  (dieselbe Falschaussage war schon in `KLARTEXT_Datenschutz.html`, Strang 46, korrigiert worden)
  ersetzt durch akkurate Beschreibung (keine Server-Speicherung, Workbook nur im Arbeitsspeicher der
  Sitzung, Cloudflare Pages statt fälschlich "Cloudflare Workers"), plus Link zur echten
  `SHOP_KLARTEXT_Datenschutz.html`.
- Footer: tote/falsche Links auf die Live-App (`klartext-ingra.h9cyz7d9pj.workers.dev/...`) ersetzt
  durch die echten Shop-Rechtsseiten (Impressum, Datenschutz, AGB, Widerrufsbelehrung); nav-logo
  verlinkt jetzt auf `index.html` statt `#`.

**Verlinkt:** neuer Header-Nav-Link "App-System", neuer Hero-Button "🎓 Komplettes App-System" auf
`index.html`, neuer CTA-Button am Ende der Module-Sektion ("Vollzugang zum kompletten System"), neuer
Footer-Link — alles auf `KLARTEXT_Verkaufsseite.html`. Damit ist das App-Produkt jetzt von der Startseite
aus auffindbar, nicht mehr nur die Kartendecks.

**Bewusst nicht angefasst:** die Preise selbst (79€ Basis, "Auf Anfrage" Team/Fortbildung) und die
"200+ Lernkarten"-Zahl (bezieht sich auf die App-internen M0–M8-Lernkarten, nicht auf die 235+
Kartendeck-Karten im Shop-Katalog — unterschiedliche Zählungen, kein Widerspruch, daher nicht
"korrigiert").
