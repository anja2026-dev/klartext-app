# KLARTEXT – Merkliste
Stand: 18.08.2026 (Strang 94 ergänzt)

**Hinweis:** Abgeschlossene Stränge 1–31 (23.07.–02.08.2026) liegen jetzt in
`KLARTEXT_Merkliste_Archiv.md`, um diese Datei schlank zu halten. Diese Datei enthält alles ab
Strang 32 (Claude-Free-Übergabe, 02.08.2026) sowie die folgenden noch offenen Themen aus dem
archivierten Bereich, die sonst verloren gegangen wären:

- **App-Aufspaltung (Supabase-Auskopplung, Task #233):** reine INGRA-App ohne Supabase/
  Weiterleitungen + separate Trainer-App geplant, Stand weiterhin "noch nicht begonnen". Details:
  Archiv, Strang 3.
- **Zusatzvermarktung, später (Strang 2):** Workbook einzeln vermarkten, Unterrichtsmaterialien
  passend zu den Decks, ggf. weitere App-Bausteine einzeln vermarktbar — alles noch nicht geprüft/
  begonnen.
- **Ideensammlung Ergänzungssets (Strang 1c), nichts priorisiert:** Pflegefamilien/Pflegekinder-Set
  (~12–15 Karten, Fachprüfungs-Vorbehalt bereits aufgehoben, kann direkt entworfen werden),
  Geschwisterkinder-Set (~12–15 Karten, unproblematisch), Verlust-eines-Menschen-Set (braucht
  fachliche Begleitung, nur Themenliste bisher), Haustier-Verlust (unproblematisch, als Themenblock
  in KD/JD integrierbar). Außerdem Methoden-Tools ohne Zielgruppenbindung: Familienbrett,
  Genogramm-Set, Fragetechniken-Set (Kandidat fürs TR-Deck), Werte-Kartenset. Assoziatives
  Bildercoaching-Set (Strang 1b) ebenfalls vorgemerkt, nicht konzipiert.
- **Übergang Schule-Beruf (besprochen 18.08.2026), bewusst nicht als eigenes Fachdeck:** Anjas Idee, für
  Jugendliche noch "Übergang Schule-Beruf" zu ergänzen — auf Nachfrage abgeglichen: Anja hat dafür
  nur ihr systemisches Coaching-Kartenmaterial, keine praktische Erfahrung und keine
  Arbeitsmarktkenntnisse (Ausbildungswege, Bewerbungsprozesse, Förderprogramme). Ein vollwertiges
  Fachdeck dazu würde genau die Sorgfalt unterlaufen, die die anderen Materialien auszeichnet
  (verifizierte Fachlichkeit). Stattdessen vorgemerkt: **kein eigenständiges Deck**, sondern
  höchstens ein schmalerer Zusatzblock im JD-Deck (analog EL-Zusatzblöcke) zur *emotionalen* Seite
  des Übergangs (Zukunftsängste, Entscheidungsdruck, Erwartungsdruck, Prokrastination) — klar als
  "emotionale Begleitung, keine Berufsberatung" positioniert, mit Verweis auf Arbeitsagentur/BerEb
  für die inhaltliche Beratung. Anknüpfungspunkte, die schon existieren: AJ-Tool "Toolbox für den
  Berufseinstieg" (bisher nur für Jugendliche mit ADHS) und JD-Deck ("inkl. Berufsvorbereitung").
  Nicht priorisiert, nur vorgemerkt.

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

## Strang 52: Produkt-Fahrplan (Ideensammlung, noch nicht umgesetzt)

Brainstorming-Runde mit Anja zu "was ist mit unseren Materialien noch alles möglich" — hier
dokumentiert zur Priorisierung, noch keine der Ideen umgesetzt.

**1. Gestufte Pakete pro Zielgruppe (Eltern, Lehrkräfte, Schulbegleiter/INGRA, Trainer — Träger
vorerst nicht):** 3-Stufen-Idee pro Gruppe — Kartendeck allein (Einstieg) → Kartendeck + Ratgeber
(Mitte) → Vollzugang App (Komplett). Bausteine existieren größtenteils schon: EL-Deck +
`KLARTEXT_Elternkurs.html` (6 Kapitel), LK-Deck + `KLARTEXT_Lehrerkurs.html` (16 Kapitel, mehr als
die veraltete "5 Kapitel"-Angabe auf der Shop-Startseite), TR-Deck + Trainerhandbuch. Technischer
Hinweis: Elternkurs/Lehrerkurs hängen aktuell am selben Login wie die ganze App — für manuellen
Versand (aktueller Stand) kein Problem, erst bei automatisiertem Sofort-Zugang bräuchte es echte
Zugriffstrennung pro Produkt.

**2. "Kurs" vs. "Ratgeber" — Umbenennung geplant:** Anja ist unsicher, ob Eltern/Lehrkräfte
tatsächlich einen Kurs (mit Fortschritt/Modulen wie beim INGRA-System) wollen oder eher schnelles
Nachschlagen im Bedarfsfall. Einschätzung: eher Ratgeber — anders als INGRAs haben Eltern/Lehrkräfte
keinen beruflichen Auftrag, ein Programm durchzuarbeiten. Vorschlag: `KLARTEXT_Elternkurs.html` /
`KLARTEXT_Lehrerkurs.html` konzeptionell zu "Eltern-Ratgeber" / "Lehrkräfte-Ratgeber" umbenennen,
vorne einen Schnellzugriff/FAQ ergänzen ("Mein Kind hat XY — was tue ich?"), nicht in Richtung
Kurs-Struktur mit Wissenscheck/Fortschrittsanzeige ausbauen (das bleibt dem INGRA-System vorbehalten).
Noch nicht umgesetzt.

**3. Insel-Set / Zonen-Set gehören nicht in die Kartendeck-Kategorie:** Anjas Einschätzung bestätigt
sich — beides sind PDF-Raummarkierungs-/Token-Material-Bundles (je 3 Zielgruppen-Varianten:
Eltern/Zuhause, Schule-INGRA, Schule-LK), keine Gesprächskarten-Decks wie der Rest. Aktuell stehen
sie trotzdem in `KLARTEXT_Shop_Uebersicht.html` zwischen den echten Kartendecks. Vorschlag: eigene
Kategorie "Material-Pakete" bzw. Verschiebung in den Downloads-Bereich, aufgeteilt nach Altersgruppe
(Insel-Set = Kinder, Zonen-Set = Jugendliche, wie Anja vorgeschlagen hat). Noch nicht umgesetzt.

**4. Kostenloses Material für Social Media (TikTok/Instagram, ggf. Videos):** Einzelne Musterkarten
aus den Decks als Karussell-Posts (Idee stand schon in Strang 34: "1-2 Musterkarten pro Deck als
Einzeldatei"), Barometer-Grafik als Erklär-Post, "Was tue ich jetzt"-Tipps als Swipe-Karussell,
Brainy als wiederkehrende Erkennungsfigur, kurze Erklär-Reels (Barometer, kLAR-Modell, einzelne
Karte). Zusätzliche Idee: "Schnupper-Paket" — 3-5 kostenlose Karten gegen E-Mail-Adresse als
Einstieg in eine Mailingliste. Noch nicht umgesetzt, keine konkrete Priorität festgelegt.

**5. Brainy-Kinderserie ("Brainy-Welt"):** Bestehende Bausteine bereits vorhanden, aber verstreut:
KD-Deck (35 Karten), Zauberfächer (Digital + Streifen, siehe unten), die elf Kinder-Downloads
(Geheimschüler-Ausweis, Joker-Gutscheine, Sterntaler, Lob-Armband, Lob-Kärtchen, Mini-Fitness,
Himmel&Hölle, Mutmach-Kärtchen, Lesezeichen, Barometer). Vorschlag: eigene Sammelseite "Brainy-Welt",
die mit neuem Material mitwächst (Anja plant, hier laufend weiteres Material zu erstellen), statt
alles in der allgemeinen Downloads-Seite zu verstecken. Noch nicht umgesetzt.

**6. Neue Kartenserie "Brainy muss mal kurz…" (Signalkarten):** Umbenennung/Erweiterung der
"Klo-Kärtchen" (`KD-02_Klokarten.html`) zu einer kleinen Serie: Brainy hält die passende Bildkarte
hoch, je nach Bedarf des Kindes (Toilette, Bewegungspause am Platz, zur Insel/Zone gehen falls die
Klasse eine hat, Trinkpause usw.). Titel bewusst ohne "raus" (Anjas Korrektur), weil nicht alle
Optionen ein Verlassen des Raums bedeuten — Synergie zu Insel-/Zonen-Sets möglich (eine Bildoption
könnte auf "geh zu deiner Insel" zeigen). Konzept steht, Kartentexte/Bilder noch nicht erstellt.

**Update 06.08.2026 — umgesetzt:** Konzept + Bildprompts in `Brainy_Signalkarten_Konzept.md`
festgehalten, zwei Prompts nach Anjas Rückmeldung noch angepasst (Bewegung jetzt am
Schultisch, frische Luft jetzt auf dem Pausenhof statt am Fenster — beides realistischer).
Anja hat alle 6 Bilder generiert und unter `bilder/signalkarten/` abgelegt, Sichtprüfung
bestanden — durchgängig stilkonsistent mit dem bestehenden Brainy-Charakter.
`KD-02_Klokarten.html` komplett umgebaut: Titel/Header auf "Brainy muss mal kurz…", die 12
fast identischen Chips mit demselben 🚽-Emoji (unabhängig vom jeweiligen Text — z. B. auch
bei "Pause gebraucht" oder "Kurze Auszeit") ersetzt durch 6 Karten mit je eigenem Foto
(120px Kreis, farbige Umrandung wie vorher), Hinweis ergänzt dass die Insel-Karte nur für
Klassen mit Insel-/Zonen-Set gilt. Referenzen in `KLARTEXT_Downloads.html`,
`DL_Allgemein.html`, `DASHBOARD.html`, `DASHBOARD_Lite.html` von "Klo-Kärtchen" auf "Brainy
muss mal kurz…" umbenannt (Icon 🚽→🙋). Dateiname `KD-02_Klokarten.html` unverändert
gelassen, um Links nicht zu brechen.

**Update 06.08.2026 (2) — Brainy-Welt-Sammelseite umgesetzt:** Neue öffentliche Seite
`BRAINY_WELT.html` in klartext-shop gebaut (kein Login, bewusst extern verlinkbar — z. B. von
Lehrer-Online oder ähnlichen Portalen). Struktur: Brainy-Charaktervorstellung, Materialübersicht
(KD-Deck als einziges aktuell eigenständig kaufbares Produkt, Signalkarten/Zauberfächer/
Druckvorlagen/Kinder-Barometer als "Teil der KLARTEXT-App" gekennzeichnet, um nichts zu
versprechen was noch nicht einzeln erhältlich ist), Zielgruppen-Grid, Bildergalerie (echtes
KD-Kartenmuster + 3 Signalkarten-Motive, dafür `brainy.png` und 4 Signalkarten-Bilder aus
klartext-app nach `klartext-shop/vorschau/brainy/` kopiert), FAQ inkl. expliziter
"Darf ich diese Seite verlinken?"-Frage, und zwei CTAs (KD-Deck vormerken /
Benachrichtigungs-Mailto für künftige Materialien — fungiert als Lead-Magnet-Sammelpunkt).
In `index.html` (Header-Nav + Footer) und `KLARTEXT_Shop_Uebersicht.html` (Nav) verlinkt.

**Update 06.08.2026 (3) — Zauberfächer-Downloads-Bug behoben:** Ursache geklärt: Der
Zauberfächer war nie "verschwunden" — die Streifen-Druckvorlage (`KLARTEXT_Zauberfaecher_
Streifen.html`, voll ausgebaut, 1394 Zeilen, alle M0–M8-Module) existierte die ganze Zeit
und war sogar technisch verlinkt, aber nur ganz unten auf dem Farbwahl-Screen der
interaktiven Digital-Version — nirgends in Downloads oder Dashboard gelistet wie jedes
andere Kindermaterial. Fix: Zauberfächer (Digital + Streifen) jetzt regulär eingetragen in
`KLARTEXT_Downloads.html` (Kinder-Sektion, zwei Buttons: Öffnen + 🖨️ Druckvorlage),
`DL_Allgemein.html` (Interaktive Tools + Druckvorlagen, Kinder-Zähler 14→16) sowie als
eigene Kachel in `DASHBOARD.html` und `DASHBOARD_Lite.html` (Modul „kd", 🔮-Icon).

**Update 06.08.2026 (4) — Barometer-Erklär-Karussell (Social Media) umgesetzt:** Erstes
kostenloses Lead-Material gebaut, unabhängig von Gewerbeanmeldung (reine Werbung/
Content, kein Verkauf — Erstellung jederzeit zulässig, Posten sobald gewünscht).
7-teiliges Instagram/TikTok-Karussell (1080×1350, JPG) im bestehenden KLARTEXT-Look:
Cover ("Woran erkennst du, wie es einem Kind gerade wirklich geht?"), je eine Folie pro
Barometer-Farbe (Grün/Gelb/Orange/Rot/Grau, Text 1:1 aus `KLARTEXT_Barometer_kLAR_
Erklaerung.html` übernommen), Outro mit CTA "Link in Bio". Rendering-Skript
`build_barometer_karussell.py` adaptiert aus der bestehenden PIL-Kartenpipeline
(`build_card_kd.py`-Muster: gleiche Fonts/Farben/300-DPI-Logik). Dateien liegen in
`klartext-shop/social/barometer-karussell/` (7 Bilder + `caption.txt` mit fertigem
Insta-Text inkl. Hashtags). Bewusste Entscheidung: mit dem neutralsten, am wenigsten
verkäuflichen Format starten (reine Aufklärung, kein Produkt-Pitch), um Vertrauen/
Reichweite aufzubauen, bevor Lead-Magnet- oder Produkt-Posts folgen.

**Offen mit Anja:** von den ursprünglich sechs Fahrplan-Themen (Strang 52) sind jetzt alle
sechs angestoßen (Insel/Zonen, Ratgeber-Framing, Signalkarten, Brainy-Welt-Sammelseite,
Zauberfächer-Bug, Social-Media-Material — erstes Stück fertig). Nächster Schritt beim
Social-Media-Strang: "Was tue ich jetzt?"-Karussell (kLAR-Modell + Feuerwehr-Protokoll)
als Folgepost, danach ggf. Schnupper-Paket-Lead-Magnet.

**Update 06.08.2026 (5) — PWA-Kartendecks-Übersicht neu sortiert:** Ursache für "wirkt
unsortiert" gefunden: `pwa/index.html` (aufrufbar über DASHBOARD.html → "Alle Kartendecks
öffnen" bzw. direkt unter klartext-app-8kl.pages.dev/pwa/) rendert die Deck-Kacheln
clientseitig per `app.js` aus `pwa/data/decks.json` — bisher als eine einzige flache Liste
in Datei-Reihenfolge, ohne Kategorien, ohne den Kachel-Look der Verkaufsseiten (nur
Vollfarbfläche statt Farbbalken + Code-Badge). Fix: `decks.json` um Felder `kategorie` und
`code` je Deck ergänzt (alle 24 Decks einsortiert: 13× "Kartendecks nach Zielgruppe", 7×
"Handlungskarten & Spezialdecks", 4× "Material-Pakete für Zuhause & Klassenzimmer" — exakt
dieselbe Dreiteilung wie auf `klartext-shop/KLARTEXT_Shop_Uebersicht.html`, plus sinnvoll
eingeordnet: LRS/Dyskalkulie zu Zielgruppe, SMI + SP zu Handlungskarten, die dort noch
fehlten). `app.js` (`loadDecks()`) baut jetzt pro Kategorie einen eigenen Abschnitt mit
Überschrift + Unterzeile, `style.css` neu für Kachel-Kopf (Farbbalken + Code-Badge) und
Kachel-Body (Titel/Untertitel) im selben Look wie die Shop-`deck-karte`. Service-Worker-
Cache-Version von v10 auf v11 gebumpt, damit Bestandsnutzer die neue Version bekommen statt
den alten Cache-Stand zu behalten. `index.html` (Grid-Container) entsprechend angepasst
(`#deckGrid` → `#deckCategories`).

**Update 06.08.2026 (6) — Raummarkierungen für Insel-/Zonen-Set sichtbar gemacht:** Anjas
Beobachtung war berechtigt: die Insel-/Zonen-Sets liefen in der App bisher nur als
Flip-Karten (Begleitkarten-Inhalt mit Regeln/Nutzen), obwohl das eigentliche Kernprodukt
großformatige Wandschilder zum Aufhängen sind. Recherche ergab: die Schilder existierten
bereits fertig gebaut — `build_marker_insel.py` erzeugt 8 DIN-A4-Raummarkierungen pro Set
(`KLARTEXT_Insel-Set_Raummarkierungen_Schule.pdf` / `_Eltern.pdf`, je 8 Seiten, verifiziert)
— waren aber nirgends verlinkt: nicht in `KLARTEXT_Downloads.html`, nicht auf der
`IS_Verkaufsseite.html`. Beim Zonen-Set war die Situation anders: dort sind die (bewusst
kleinen, unauffälligen A6-)Markierungen für Jugendliche von Anfang an ins Haupt-PDF
eingebaut (`build_pdf_zonen.py`) und auf `ZS_Verkaufsseite.html` korrekt beworben — kein
Fix nötig. Behoben: neue Sektion "Raum-Material · Insel- & Zonen-Set" in
`KLARTEXT_Downloads.html` mit allen 8 zugehörigen PDFs (2× Raummarkierungen, 3×
Insel-Handbücher Schule-INGRA/Schule-LK/Eltern, 2× Zonen-Komplettpakete, 1×
Zonen-Token-Karten). `IS_Verkaufsseite.html` korrigiert: Copy sprach bisher nur von
"Badge-Druckvorlage" statt der tatsächlichen 8 großformatigen Raummarkierungen — in
Leistungs-Kacheln und allen drei Preis-Paketen (Digital, Bundle, Träger-Lizenz)
richtiggestellt. Die PWA-Flip-Karten bleiben zusätzlich bestehen (digitale Fassung der
kleinen Begleitkarten für die Fachkraft) — sie ersetzen die Schilder nicht, sondern
ergänzen sie, wie von Anja gewünscht.

**Update 06.08.2026 (7) — PWA: fehlender Rückweg zur App behoben:** Anja meldete "die App ist
weg, ich seh nur die Kartendecks, kein Button zum Dashboard" — echter Bug, nicht nur
gefühlt: `pwa/index.html` läuft als eigenständige PWA (`manifest.json`: `display: standalone`,
eigener Service Worker, eigenes Scope `./`), hatte aber nirgends einen Link zurück zu
`DASHBOARD.html`. Der vorhandene `backBtn` navigiert nur innerhalb der PWA (Karten-Ansicht →
Deck-Liste), nicht aus der PWA heraus. Im Standalone-Modus (v. a. nach "Zum Home-Bildschirm
hinzufügen") fehlt zusätzlich die Browser-Zurück-Taste — Nutzer waren dort wirklich gefangen.
Fix: 🏠-Button rechts in der Topbar ergänzt (`<a href="../DASHBOARD.html" class="iconbtn"
id="homeBtn">`), auf der Deck-Übersicht wie in der Karten-Ansicht durchgehend sichtbar.
`style.css`: `.iconbtn` für `<a>`-Elemente lauffähig gemacht (display:flex, text-decoration:
none). Service-Worker-Cache-Version v11 → v12 gebumpt.

**Update 06.08.2026 (8) — Zauberfächer: Beschreibung korrigiert + fehlende Streifen-PDF
gebaut:** Zwei getrennte Punkte. (1) Die Beschreibung "Farbe wählen, Karte ziehen, Gespräch
öffnen" war sachlich falsch — der Zauberfächer zieht keine Gesprächskarte, sondern eine
Mini-Übungskarte aus 6 Themen (Brainy-Flow, Spaß & Quatsch, Atem & Ruhe, Miteinander,
Denken & Entdecken, Selbstfürsorge; Quellcode `KLARTEXT_Zauberfaecher_Digital.html`,
`KARTEN`-Objekt). Korrigiert auf "Thema wählen, Karte ziehen, Mini-Übung machen" in
`DASHBOARD.html`, `DASHBOARD_Lite.html`, `DL_Allgemein.html`, `KLARTEXT_Downloads.html`.
(2) Die Streifen-Druckvorlage existierte nur als HTML (`KLARTEXT_Zauberfaecher_Streifen.
html`), nie als PDF. Neues Skript `build_pdf_zauberfaecher_streifen.py`: parst Texte, Farben
und Brainy-Farbfilter direkt aus der HTML-Datei (per Regex, garantiert Textgleichheit mit
der Web-Version statt manueller Abschrift), rendert alle 45 Streifen (6 Module) im
Original-Format 20×3 cm als Vorder-/Rückseite, verteilt auf A4-Bögen (6 Vorderseiten- +
6 Rückseiten-Seiten). CSS-`hue-rotate`/`saturate`-Filter der Brainy-Grafik per HSV-Shift
nachgebaut. `KLARTEXT_Zauberfaecher_Streifen.pdf` liegt jetzt in `klartext-app/` und ist
verlinkt: neuer 📄-PDF-Button in `KLARTEXT_Downloads.html` (zusätzlich zur HTML-Druckvorlage),
`DL_Allgemein.html`-Kachel zeigt jetzt direkt auf die PDF, Druckvorlage-Link in
`KLARTEXT_Zauberfaecher_Digital.html` ebenfalls auf die PDF umgestellt.

**Update 07.08.2026 (9) — Gewerbe angemeldet + Plattform-/Preisstrategie erarbeitet:**
Anja hat ihr Gewerbe angemeldet (Tätigkeitsbeschreibung: Konzeption/Erstellung/Vertrieb von
pädagogischem Material + Trainings/Coachings/Fortbildungen). Damit fallen die Gründe weg,
warum Checkout/Preise bisher bewusst offen gelassen wurden (#213, #220). Auf Wunsch geprüft:
was gibt es zu verkaufen, auf welchen Plattformen (Etsy, Pinterest, eduki/lehrermarktplatz.de),
was kostet das, welche Preise. Ergebnis in neuer Datei **`KLARTEXT_Plattform_Preisstrategie.md`**:

- **Inventar-Lücke gefunden:** 22 fertige Produkte, aber nur 19 haben eine Verkaufsseite — SMI,
  LRS-Sek1 und SP existieren bereits als fertiges PDF, sind aber nirgends gelistet.
- **Plattform-Rechercheergebnis:** Pinterest = kostenlos, aber kein Marktplatz (nur Trafficbringer
  zum eigenen Shop). Etsy = echter Marktplatz, ~10,5–17 % Gesamtgebühren, braucht Gewerbe (jetzt
  vorhanden). eduki (ehemals lehrermarktplatz.de, gleiche Firma, 2023 umbenannt — vermutlich das,
  was Anja mit "lehreronline" meinte, nicht das redaktionelle `lehrer-online.de`) = Lehrkräfte-
  Zielgruppe, aber 50 % Provision unter 20 Materialien (sinkt auf 30 % ab 100 Materialien), kein
  Gewerbe nötig. Eigener Shop bleibt mit ~1,5–3 % Zahlungsanbieter-Gebühr die margenstärkste Basis.
- **Preisvorschlag:** bestehende Preis-Spannen (z. B. "15–18 €") auf oberes Ende fixiert, als
  Tabelle für alle 22 Produkte inkl. der 3 noch unlistierten. Offene Frage an Anja: EL (58 Karten)
  und LK (71 Karten) sind die größten Decks im Sortiment, kosten aber wie die kleineren 30–50er
  Decks — bewusst nicht eigenmächtig angehoben, sondern zur Entscheidung vorgelegt.
- **Free-vs-Paid:** Barometer-Karussell, externe Barometer-Erklärseite und Vorschaubilder bleiben
  kostenloses Marketing; alle 22 Decks/Sets bleiben kostenpflichtig. "Brainy muss mal kurz…" als
  möglicher Freebie fürs Lead-Sammeln identifiziert, aber noch nicht umgesetzt/entschieden.

Vier offene Entscheidungen liegen jetzt bei Anja (siehe Dokument): EL/LK-Preis anheben oder nicht,
SMI/LRS/SP zuerst listen oder direkt mit auf die neuen Plattformen, Reihenfolge Etsy vs. eduki,
"Brainy muss mal kurz…" als offizielles Freebie einrichten oder nicht.

## Strang 53: Zwei der vier Preisstrategie-Entscheidungen umgesetzt (07.08.2026)

**EL/LK-Preis:** auf Anjas Rückfrage "was ist am professionellsten?" empfohlen und umgesetzt:
wertbasierte Preisgestaltung statt reiner Konsistenz — Umfang (58/71 Karten, größte Decks im
Sortiment) und höhere Zahlungsbereitschaft der Fachkräfte-Zielgruppe rechtfertigen einen Aufschlag.
Auf 22 €/34 € angehoben (Anzeige als Spanne 19–22 €/31–34 € in `EL_Verkaufsseite.html`/
`LK_Verkaufsseite.html`, konsistent mit dem Range-Stil der übrigen Seiten). Die unverlinkten,
veralteten Duplikate `el.html`/`lk.html` im klartext-shop-Repo wurden dabei bewusst nicht
angefasst (toter Code, nirgends verlinkt) — bei Bedarf aufräumbar.

**SMI/LRS-Sek1/SP-Verkaufsseiten gebaut:** Wichtiger Befund vorab — `KLARTEXT_Plattform_
Preisstrategie.md` hatte SMI und SP mit falschen Themen beschrieben ("Sinnesbeeinträchtigungen"
bzw. "Selektiver Mutismus/Sprache"). Gegen den echten Code (`pwa/data/smi.json`, `sp.json`)
geprüft: SMI = Systemische Mobbing-Intervention (10 Karten, Ergänzung zum bestehenden
MB-Handlungskartendeck auf Klassen-/Systemebene), SP = Springer-INGRAs (7 Karten, für
Schulbegleitung im flexiblen Klassenwechsel-Einsatz). LRS-Sek1-Beschreibung war korrekt.
Preisstrategie-Dokument entsprechend korrigiert.

Alle drei Karten-Sets komplett neu gerendert (`build_all_cards_smi/sp/lrs_sek1.py`), je 3 Karten
pro Deck (Vorder-/Rückseite) als Muster-JPGs nach `klartext-shop/vorschau/{smi,sp,lrs-sek1}/`
exportiert. Drei neue Verkaufsseiten nach dem HB/MB-Templatemuster gebaut: `SMI_Verkaufsseite.html`,
`SP_Verkaufsseite.html`, `LRS_Verkaufsseite.html` — Quellen direkt aus den Karten-JSONs übernommen
und gegenrecherchiert (Salmivalli 1996, de Shazer 1988 per Websuche verifiziert). Beim SP-Deck
bewusst *keine* Quellen erzwungen, wo keine echte Forschung zum Springer-Einsatz vorliegt — Sektion
heißt dort "Praxis & Fachbezug" statt "Wissenschaftliche Basis", mit explizitem Hinweis, dass 6 von
7 Karten auf strukturierter Praxiserfahrung statt Studien beruhen.

In `KLARTEXT_Shop_Uebersicht.html` verlinkt: SMI/SP unter "Handlungskarten & Spezialdecks", LRS
unter "Kartendecks nach Zielgruppe" (konsistent mit `pwa/data/decks.json`-Kategorisierung aus
Strang 52). Hero-Zahlen dort (12→13 Zielgruppen-Decks, 5→7 Spezialdecks) und in `index.html`
(19→22 Kartendecks) korrigiert. Struktur-Check (div/section-Balance) für alle drei neuen Seiten
sauber.

**Weiterhin offen (auf Anjas Wunsch zurückgestellt):** Reihenfolge Etsy vs. eduki, "Brainy muss mal
kurz…" als offizielles Freebie.

## Strang 54: Ursprungsgeschichte geklärt — warum es Admin-App, Shop und Shop-Lite nebeneinander gibt

Anja hat auf Rückfrage die Entstehungsgeschichte eingeordnet (wichtig fürs Verständnis, warum die
Architektur so verzweigt ist):

1. **Ursprünglich** war nur EINE App geplant — Supabase-frei, im Wesentlichen das, was heute als
   "Shop-Lite" bezeichnet wird.
2. **Durch die Testphase bei der Partnerorganisation** (jetzt beendet) wurde daraus "auf einmal"
   eine waschechte Supabase-App mit Case-Management/Fallmanagement (Barometer Kind, Chat,
   Zeitkonto etc.) — nicht der ursprüngliche Plan, sondern durch die Pilot-Anforderungen
   entstanden.
3. **Die Supabase-Linie ist wegen DSGVO bewusst zurückgestellt** (deckt sich mit Task #233 "App-
   Aufspaltung" — unverändert geparkt, keine neue Entscheidung, nur jetzt mit Begründung
   dokumentiert).
4. **Separat davon** entstand die Idee, Unterrichtsmaterialien auf Lehrkräfte-Plattformen (eduki
   u. a., siehe Strang 52) anzubieten — daraus wiederum die Idee der eigenständig verkaufbaren
   Kartendecks, und daraus wiederum die Idee, diese zusätzlich als digitale Flip-Cards anzubieten.

**Ergänzender technischer Befund (heute):** Die Flip-Card-Ansicht (`pwa/`) liegt aktuell im
klartext-app-Repo und wird unter `klartext-app-8kl.pages.dev/pwa/` mit ausgeliefert — technisch
zwar schon Supabase-frei (eigenes Manifest, eigener Service Worker), aber architektonisch nicht
getrennt von der Admin-App, wie es Anjas ursprünglicher Idee entspräche.

**Empfehlung (als Experte auf Anjas Bitte, siehe Chat vom 07.08.2026):** Nicht das komplette,
bereits gebaute Shop-Lite/DASHBOARD_Lite (kompletter INGRA-Kurs ohne Supabase) live schalten,
sondern zuerst eine schlankere, eigenständige Kartendecks-App (nur Flip-Cards + Suche über alle
22 Decks) als drittes, eigenes Deployment aufsetzen — passend zum aktuellen kommerziellen Fokus
(Kartendecks-Verkauf über eigenen Shop/Etsy/eduki). Details siehe
`KLARTEXT_Konzept_Kartendecks-App.md`. Shop-Lite/Gesamt-App-Idee bleibt als späteres,
nachgelagertes Produkt bestehen — kein Widerspruch, nur zeitlich hinten angestellt.

## Strang 55: Kartendecks-App gebaut — neues Repo `klartext-karten`

Anja hat der Empfehlung aus Strang 54 zugestimmt. Neues Repo `klartext-karten` angelegt (Anja,
lokal geklont neben klartext-app/klartext-shop), `pwa/`-Code aus klartext-app komplett übernommen
(Kartendaten aller 22 Decks, Bilder, Flip-Logik, Manifest, Service Worker — bereits Supabase-frei,
keine Migration nötig). Ergänzt:

- **Suchleiste**: `data/search-index.json` neu gebaut (572 Karten, alle Decks, Volltext aus Titel/
  Anleitung/Fragen/Schritte/Hinweis/Tipp/Merksatz/Verweis/Nutzen/Systemfrage), client-seitige
  Suche in `app.js` (umlauttolerant, debounced, öffnet das Deck direkt bei der passenden Karte
  statt bei Karte 1). Stichproben-Test der Suchlogik gegen echte Daten: "Wut" → 10 Treffer,
  "Mobbing" → 22 Treffer, "Elterngespräch" → 6 Treffer — sinnvolle Ergebnisse.
- `homeBtn` von `../DASHBOARD.html` (Admin-App) auf `https://klartext-mentoring.de` (Shop)
  umgestellt, Barometer-Link ebenfalls auf die Shop-Domain umgestellt (vorher relative Pfade, die
  außerhalb der Admin-App ins Leere gezeigt hätten).
- `README.md` komplett neu geschrieben (alte Version beschrieb einen 1-Deck-Prototyp innerhalb
  von klartext-app, nicht mehr zutreffend).
- Service-Worker-Cache-Version v12→v13 gebumpt (search-index.json neu im Precache).

**Getestet:** JSON-Validität, JS-Syntax-Check, HTML-Struktur-Balance, lokaler Serverlauf (alle
Kern-Dateien liefern HTTP 200), Suchlogik gegen echte Kartendaten — alles unauffällig. Kein
Headless-Browser im Sandbox verfügbar, daher kein echter Klick-/Flip-Test im Browser; bei Bedarf
über Claude in Chrome nachholbar.

**Deployment (07.08.2026):** Anja hat Cloudflare Pages Projekt + Subdomain
`karten.klartext-mentoring.de` bereits selbst eingerichtet (aktiv, SSL läuft) — schneller als
erwartet, kein Anleitungsbedarf.

**Verlinkung im Shop ergänzt (07.08.2026):** Alle 22 Verkaufsseiten bekommen einen Deep-Link-
Button "📱 Als Flip-Card ausprobieren" im Hero-Bereich, der direkt zum passenden Deck in der neuen
App springt (`karten.klartext-mentoring.de/?deck=<id>`), z. B. SMI-Verkaufsseite → öffnet direkt
das SMI-Deck statt der allgemeinen Deck-Übersicht. Ausnahme: Insel-Set/Zonen-Set (IS/ZS) verlinken
ohne Deck-Parameter, da beide zwei App-interne Varianten (Schule/Eltern) haben und keine
eindeutige Zuordnung möglich ist. Zusätzlich allgemeine Links ergänzt: Hauptnavigation
(`index.html`, neuer Menüpunkt "Flip-Card-App"), Kartendecks-Teaser auf der Startseite, Hero-
Bereich der `KLARTEXT_Shop_Uebersicht.html`. Alle Links öffnen in neuem Tab, damit die
Verkaufsseite nicht verloren geht. Struktur-Check (div/section-Balance) für alle geänderten
Dateien sauber.

**Damit ist Task #7 (Deployment + Verlinkung) abgeschlossen.**

**Nachtrag (07.08.2026) — Passwort-Sperre ergänzt:** Anja war bei der Live-App durch die offene
Zugänglichkeit alarmiert (alle 22 Decks ohne Kauf voll sichtbar) und wollte das sofort schließen,
während die parallel laufende Digistore24-Anmeldung durch ein 2FA-Problem blockiert war. Einfache
Client-seitige Passwort-Sperre ergänzt (`index.html`: neuer `lockScreen`, restlicher Inhalt in
`appShell` gewrappt und initial versteckt; `app.js`: Startlogik in `initApp()` verschoben, nur nach
korrektem Passwort oder bestehendem `localStorage`-Flag aufgerufen). Passwort aktuell
`brainy-lernt-2026`, im Quelltext hinterlegt — wie bei `KLARTEXT_Login_Shop.html` (Strang 44)
bewusst keine echte Zugriffskontrolle, nur ein Riegel gegen zufälligen Vollzugriff. Deep-Links von
den Verkaufsseiten (`?deck=<id>`) funktionieren nach Entsperrung weiterhin korrekt. Service-Worker
v13→v14 gebumpt. Getestet: JS-Syntax, HTML-Balance, lokaler Serverlauf mit sichtbarem
`lockScreen`/`appShell`.

**Noch offen:** Sobald Digistore24 läuft, Passwort-Weitergabe an Kund:innen einrichten (z. B. über
die Dankeseite/Bestellbestätigung) — aktuell nur ein Platzhalter-Passwort ohne Verteilmechanismus.

## Strang 56: Digistore24-Einrichtung begonnen, KD-Deck als Pilotprodukt

Anja hat sich bei Digistore24 als Verkäuferin registriert und mit Anja zusammen das erste Produkt
(KD-Deck) durchs Formular begleitet (Produktname/-typ, Verkaufsseite-URL, Rechnung/Logo,
Verkaufseinschränkungen — Details siehe Chat). Unterbrochen durch ein 2FA-Problem, Support-Anfrage
läuft.

**Vorbereitet für die Wartezeit:** `KLARTEXT_Digistore24_Produktliste.md` — alle 22 Decks mit
fertigen Digistore24-Produktdaten (Produktname intern/für Käufer, Kurzbeschreibung, Preis,
Verkaufsseite-URL, PDF-Dateiname), damit das Anlegen der restlichen 21 Produkte nur noch
Copy-Paste ist. Drei offene Bündelungsfragen markiert statt geraten: EL/LK-Zusatzblöcke (7 PDFs),
MB-Bonusmaterial, Insel-/Zonen-Set-Dateikombination.

**Nachtrag (07.08.2026) — Bündelungsfragen entschieden:** Anja hat (in Rücksprache mit
NotebookLM, mit dem sie parallel arbeitet) entschieden:
- **EL/LK:** Zusatzblöcke (7 PDFs) werden immer mitgeliefert statt einzeln verkauft — als ZIP mit
  dem Basis-PDF.
- **MB:** wird als "Mobbing-Intervention-Kit" mit allen Arbeitsmaterialien
  (`KLARTEXT_AntiMobbing_Arbeitsmaterialien.pdf`) gebündelt.
- **JD:** der Einheitlichkeit halber ebenfalls auf 22 €/34 € angehoben (gleiche Preisstufe wie
  EL/LK — die drei größten Decks im Sortiment). `JD_Verkaufsseite.html` und
  `KLARTEXT_Plattform_Preisstrategie.md` entsprechend aktualisiert.
- **Insel-/Zonen-Set:** Zielgruppen-Trennung (Schule/Zuhause/Jugendliche) grundsätzlich
  freigegeben, aber technisch zurückgestellt — die aktuellen Verkaufsseiten bieten eine "ein Set
  nach Wahl bei Bestellung"-Logik, die sich nicht 1:1 in ein Digistore24-Produkt mit festem Inhalt
  übersetzen lässt. Bräuchte erst einen Umbau der beiden Verkaufsseiten (echte Einzelprodukt-
  Kacheln statt Wahlmöglichkeit) — kein Blocker für die anderen 20 Produkte.
- Kurzer Zwischenfall: Anja hatte versehentlich einen Textabschnitt mit einem unpassenden Verweis
  auf ein anderes Projekt ("alfatraining"-Lebenslauf) reinkopiert — nach Rückfrage aufgeklärt,
  nichts übernommen.

`KLARTEXT_Digistore24_Produktliste.md` entsprechend aktualisiert: 20 von 22 Produkten jetzt
vollständig entscheidungsfertig, 2 (Insel-/Zonen-Set) als "Phase 2" markiert.

## Strang 57: Abgleich neue JD-Jugendlichen-Module gegen Bücher/Workbook/Lernpfad/Trainerbuch/Systemdateien (10.08.2026)

Anjas Auftrag: erstmal nur prüfen und auf die Merkliste setzen, nicht umsetzen — Umfang zu groß für eine
Session. Geprüft wurden sechs in der laufenden Session neu gebaute bzw. erweiterte Jugendlichen-Tools
gegen alle großen Referenz-/Systemdokumente. Per Subagenten-Recherche, jeder Treffer gegen Fehlalarme
geprüft (nicht blind auf Grep-Zahlen verlassen — gleiche Methodik wie Strang 50).

**Die sechs geprüften Module:**
A. Skill-Matrix — "Superpower-Profil" + neue Sektion "Bewerbungs-Profi 2.0" (Anschreiben/Interview-
   Textbausteine, Mut-Sektion mit JD-37-Bezug)
B. Perspektiv-Wechsler — komplett neu gebautes 8-Themen-Brückensystem (vorher: einfacher
   Karten-Mechanismus)
C. **Was hilft mir gerade?** (`KLARTEXT_Spiel_WasHilftMir.html`) — komplett neues Krisenmoment-zu-Tool
   Action-Center, verlinkt JD-Karten + Insel-Set
D. **Ressourcen-Bericht** (`KLARTEXT_Ressourcenbericht.html`) — komplett neue Export-Seite fürs Eltern-/
   Lehrergespräch
E. **Moderations-Leitfaden INGRA** (`KLARTEXT_Moderationsleitfaden_INGRA.html`) — komplett neu
F. **Feedbackbogen LK** (`KLARTEXT_Feedbackbogen_LK.html`) — komplett neu
Zusätzlich: Reizfilter-Regler (`KLARTEXT_Spiel_Reizfilter.html`) hat jetzt echte Tages-Verlaufsspeicherung
(vorher rein momentan, ohne Speicherung).

### Befund 1 — `M0-00_Systemelemente.html` (die zentrale Systemdatei)

Listet exakt **9 nummerierte Bausteine**: 01 Barometer, 02 kLAR-Modell, 03 Joker, 04 Brainy,
05 Feuerwehr, 06 Rollen & Haltung, 07 Humor & Leichtigkeit, 08 Abgrenzung, 09 Systemübersicht.

- ❌ **Insel-Set fehlt komplett** — obwohl `INSEL-Set_Konzept_und_Barometer-Integration.md` selbst
  vorschlägt, es "als Element 10" aufzunehmen (Zeile 76-78 dort). Bisher nicht umgesetzt.
- ❌ Keines der 6 neuen/erweiterten Module (A–F) wird dort erwähnt.
- kLAR-Modell dort korrekt dokumentiert (K-Kontakt & Körperliche Sicherheit / L-Leise & Langsam /
  A-Anerkennung & Atmen / R-Reizreduktion & Rückzug) — deckt sich mit dem, was im neuen
  Moderationsleitfaden korrekt referenziert wurde (Strang zu dieser Session, kein Widerspruch).

### Befund 2 — `KLARTEXT_Anleitungen_Tools.html` ("Trainer-Handreichung: Die interaktiven Tools")

Enthält nur 6 Modul-Einträge insgesamt (Brainy-Wort-Würfel, Werte-Poker, Skill-Matrix,
Perspektiv-Wechsler, ADHS-Toolbox, Online-Identity-Lab):

- **Skill-Matrix:** ⚠️ nur veralteter Stand dokumentiert (alter "Hobby-Check → Stärken-Liste"-Ablauf,
  Bewerbungs-Profi 2.0/Mut-Sektion/JD-37 fehlen).
- **Perspektiv-Wechsler:** ⚠️ nur veralteter Stand dokumentiert (alter Einzelkarten-Mechanismus,
  8-Themen-Brückensystem + Barometer-Check-in fehlen).
- **Was hilft mir gerade?, Ressourcen-Bericht, Moderations-Leitfaden, Feedbackbogen:** ❌ alle vier
  komplett nicht dokumentiert (kein Eintrag, auch kein alter Stand, da komplett neu).
- Reizfilter-Regler: hatte ohnehin nie einen eigenen Eintrag (weder alt noch neu).

### Befund 3 — WICHTIG: Zonen-Set für Jugendliche existiert bereits fertig gebaut

Beim Insel-Set/Zonen-Set-Vergleich kam ein Fund hoch, der über die eigentliche Prüfung hinausgeht und
eine Entscheidung aus dieser Session betrifft: Das Konzeptpapier `INSEL-Set_Konzept_und_Barometer-
Integration.md` behauptet (Zeile 80-86), das Zonen-Set für Jugendliche (Sek I/II) sei "noch nicht im
Detail ausgearbeitet". **Das stimmt nicht mehr** — es existiert bereits fertig:

- `Jugend-Zonen-Set_Konzept_und_Prompts.md` (vollständiges Konzeptpapier)
- Drei fertige PDFs, live verlinkt in `KLARTEXT_Downloads.html` (Zeile 477, 507–518):
  `KLARTEXT_Zonen-Set_Schule.pdf`, `_Eltern.pdf`, `_Token-Karten.pdf`
- Laut `KLARTEXT_Merkliste_Archiv.md` (Strang 9) bereits am 30.07.2026 fertiggestellt — das
  Konzeptpapier wurde seitdem nicht aktualisiert.

**Konsequenz für diese Session:** Bei „Was hilft mir gerade?" (Modul C) wurde in Rücksprache mit Anja
bewusst das **Kinder**-Insel-Set referenziert, mit zurückhaltender Sprache, *weil* das Konzeptpapier ein
eigenes Jugendlichen-Set als "noch nicht gebaut" auswies. Jetzt zeigt sich: ein echtes, speziell für
Jugendliche entworfenes Zonen-Set (neutrale statt niedliche Symbole, "Zone" statt "Insel" — genau die
Sprache, die dort extra für die Jugendlichen-Zielgruppe entwickelt wurde) lag die ganze Zeit bereits
fertig vor. Das ist wahrscheinlich die bessere Grundlage für Was-hilft-mir-gerade als das Kinder-Insel-Set
— **eigener Folge-Task, noch nicht umgesetzt**, da das erst mit Anja abzustimmen ist (Zonen-Namen/
-Regeln aus dem Zonen-Set-PDF müssten gegen den echten Inhalt geprüft werden, bevor etwas ausgetauscht
wird — gleiche Sorgfaltspflicht wie beim ursprünglichen Insel-Set-Check).

### Befund 4 — Große Referenzdokumente (Fachbuch, Workbook, Lernpfad, Trainerhandbuch, Lernhandbuch,
Curriculum, Systemanleitung, Glossar)

Alle acht per Grep + Fehlalarm-Kontrolle geprüft (u. a. gegen "Perspektivwechsel" ohne "-er", das an
mehreren Stellen als generischer Empathie-Begriff für andere, ältere Karten/Konzepte vorkommt — kein
echter Treffer). Ergebnis: **keines der 6 neuen/erweiterten Module ist in irgendeinem der acht Dokumente
erwähnt.** kLAR ist überall dort ausschließlich als Deeskalations-Werkzeug dokumentiert (nie als
Gesprächsmoderations-Baustein) — deckt sich mit der bewussten Entscheidung dieser Session, kLAR im neuen
Moderationsleitfaden nur als Eskalations-Fallback zu nutzen, nicht als Hauptstruktur. Kein Widerspruch,
aber auch keine Vorarbeit, auf die aufgebaut werden könnte.

### Zusammenfassung / Noch offen

- Kein Dokument wurde in dieser Runde verändert — reine Bestandsaufnahme, wie von Anja gewünscht.
- **Kandidaten für die nächste inhaltliche Angleichungsrunde** (nach demselben "Deck für Deck"-Muster
  wie Hochbegabung/Mobbing, Strang 39–42): `M0-00_Systemelemente.html` (Insel-Set als Element 10 + evtl.
  Verweis auf die neuen Jugendlichen-Tools), `KLARTEXT_Anleitungen_Tools.html` (Skill-Matrix/
  Perspektiv-Wechsler-Einträge aktualisieren, 4 neue Einträge ergänzen), danach ggf. Fachbuch/Lernpfad/
  Trainerhandbuch — aber erst nachdem mit Anja priorisiert ist, ob/wie tief das gehen soll.
- **Offene Entscheidung mit Anja:** Zonen-Set statt Insel-Set in Was-hilft-mir-gerade verwenden (Befund 3).
- Kein Zeitdruck-Hinweis von Anja — Priorisierung mit ihr noch offen, analog zu Strang 50.

## Strang 58: System-Erweiterung TO (Tourette) & DS (Trisomie 21) — Fact-Check + Decks/Module gebaut (11.08.2026)

**Kontext:** NotebookLM-Prompt "System-Erweiterung (TO & DS)" wollte zwei neue Zielgruppen-Kartendecks
(Tourette-Syndrom "Lila", Trisomie 21/Down-Syndrom "Hellblau/Gelb"), zwei neue M2-Module (M2-43, M2-44)
und eine Action-Hub-2.0-Verknüpfung (Reizfilter↔Tics, Sterntaler/Joker-Karten/Wochenplan↔DS). Vor
Umsetzung wie üblich gegen den echten Systemstand geprüft.

**Fact-Check-Befunde (echte `pwa/data/decks.json` als Quelle, nicht `KLARTEXT_Konzept_Kartendecks-App.md`
— letztere Datei ist nur ein Deployment-Memo für eine geplante Kartendecks-App, kein Farbschema-Dokument
und erwähnt TO/DS/Farben gar nicht):

- ❌ **Farbkollision:** "Lila" für TO ist bereits vergeben — TK-Deck nutzt `#4A148C` (dunkles Violett),
  SMI-Deck `#592D59` (dunkles Pflaume) liegt ebenfalls im Lila-Bereich. Neue Farbe gewählt: `#B08FD1`
  (helles Flieder/Lavendel, RGB-Distanz ≥135 zu allen 26 bestehenden Deck-Farben).
- ❌ **FK-Deck hat 8 Karten, nicht 7** (FK-01 bis FK-08 existieren) — das 7-Karten-Deck ist tatsächlich SP.
- ⚠️ **Sterntaler und Wochenplan existieren wirklich**, sind aber generische Tools (Lob-Druckvorlage
  bzw. Aufgaben-Wochenplan-Baukasten für alle Kinder), keine DS-spezifischen — Verknüpfung wäre
  Zweitnutzung, kein neu entdecktes Matching.
- ❌ **"Joker-Karten" (Plural, ein Kartendeck) existiert nicht.** Der echte Joker ist ein einzelnes,
  individuell vereinbartes Notfallsignal (Geste/Wort/Karte) — bestätigt in Glossar und `M3-Joker.html`.
  Nebenfund dabei: Glossar-Link zeigt auf `M3-03.html` ("Kind eskaliert — Wutausbruch"), nicht auf die
  echte Joker-Seite `M3-Joker.html` — noch nicht korrigiert, kleiner offener Punkt.
- ❌ **"Stress-Tic-Korrelation" wäre komplett neue Funktion:** Der digitale Reizfilter trackt aktuell nur
  einen täglichen Stresswert (0–4, ein Eintrag/Tag, `klartext_reizfilter_verlauf`) — kein Tic-Tracking
  existiert. Eine Korrelation bräuchte ein neues Datenmodell (Tic-Häufigkeit/-Typ) plus Korrelationslogik
  plus neue UI.
- ✅ Kern-Prämisse stimmt: Tourette und Trisomie 21/Down-Syndrom haben aktuell **kein eigenes Modul** —
  nur Randerwähnungen (Tourette ein Wort im Neurodivergenz-Glossareintrag → M2-07; Down-Syndrom ein
  Absatz in `KLARTEXT_Fachbuch_System_Paedagogik.html`). M2-43/44 waren wirklich frei (höchste Nummer
  M2-42).
- ✅ Recherchiert (nicht im Prompt behauptet, aber zur Farbwahl relevant): Die reale
  Tourette-Awareness-Farbe ist Teal/Türkis-Grün — im System aber schon zweimal vergeben (JD, IS-Schule),
  deshalb bewusst Lavendel statt Teal für TO gewählt. Die reale World-Down-Syndrome-Day-Farbkombination
  ist tatsächlich Blau + Gelb (worlddownsyndromeday.org) — passt zur ursprünglichen Idee, DS-Farbe
  entsprechend als `#5AC4D0` (Türkis-Hellblau) + `#F0C64A` (Gelb-Akzent) gewählt, RGB-Distanz ≥71/≥93
  zu den nächstgelegenen Bestandsfarben.

**Mit Anja abgestimmt (3 Scope-Fragen, alle Empfehlungen bestätigt):**
1. Farben: neue, kollisionsfreie Farben statt Lila (s.&nbsp;o.)
2. Umfang dieser Runde: nur Decks + M2-Module, Action-Hub-2.0-Verknüpfung (inkl. der komplett neuen
   Reizfilter-Funktion) als eigener, späterer Schritt
3. DS-Verknüpfung zu bestehenden Tools: falls später umgesetzt, echte Tools (Sterntaler, Wochenplan,
   singularer Joker) klar als Zweitnutzung kennzeichnen, keine "Joker-Karten"-Fiktion

**Umgesetzt:**
- `pwa/data/decks.json`: 2 neue Einträge TO (`#B08FD1`, 3 Karten) und DS (`#5AC4D0`, 3 Karten) —
  22 → 26 Decks insgesamt
- `pwa/data/to.json`, `pwa/data/ds.json`: je 3 echte Karten im etablierten Schema
  (nr/titel/anleitung/fragen/hinweis/bild), inhaltlich an AT-Deck-Tonalität angelehnt (Tic-Neutralität
  bzw. "Langsamer – nicht weniger"/Autonomie)
- `M2-43_Tourette_Tics.html`, `M2-44_Trisomie21_Inklusion.html`: neu, nach Vorlage `M2-42` (komplett
  inline-CSS, kein externes Stylesheet nötig), mit verifizierten Quellen (Leckman/Walker/Cohen 1993 zum
  Vorboten-Gefühl, DSM-5-Kriterien, Non-Disjunction/Meiose-Mechanismus für Trisomie 21 >95&nbsp;%,
  Personen-first-Sprache mit Verweis auf den bestehenden Fachbuch-Absatz), Cross-Referenzen zu M2-07
  (Neurodivergenz) und M2-29 (Entwicklungsverzögerungen)
- Nav-Kette aktualisiert: `M2-42` zeigt jetzt vorwärts auf `M2-43` statt auf Dashboard (war vorher Ende
  der Kette), `M2-43` ↔ `M2-44` verlinkt, Fußzeilen-Zähler von "42/42" auf "42/44", "43/44", "44/44"

**Bewusst NICHT umgesetzt (Scope-Entscheidung, s.&nbsp;o.):** Action-Hub-2.0-Verknüpfung
(Stress-Tic-Korrelation im Reizfilter, DS-Tool-Verlinkung) — eigener Folge-Task.

**Nebenbefund mit Tragweite:** 22 → 26 Decks ist keine reine Content-Frage — `KLARTEXT_Digistore24_
Produktliste.md` und die Preisstrategie-Datei referenzieren aktuell "22 Decks" als Produktumfang. Noch
nicht angepasst, eigene Preisstrategie-Entscheidung mit Anja nötig, bevor das nach außen kommuniziert wird.

### Noch offen (erweitert Strang 57 um TO/DS)

- **Punkt aus dem NotebookLM-Prompt (Punkt 4), wie von Anja gewünscht auf die Merkliste gesetzt:**
  Vollständige Überarbeitung von Fachbuch, Trainerhandbuch, Lernpfaden und Curriculum zur Integration
  der 6 Action-Hub-Module (Strang 57) **sowie** der neuen TO- und DS-Inhalte (Strang 58) — deckt sich
  mit dem bereits in Strang 57 offenen "Kandidaten für die nächste inhaltliche Angleichungsrunde"-Punkt,
  jetzt um TO/DS erweitert. Umfang/Priorisierung noch nicht mit Anja abgestimmt.
- Action-Hub-2.0-Verknüpfung TO↔Reizfilter (neue Stress-Tic-Korrelation-Funktion) und DS↔bestehende
  Tools (Sterntaler/Wochenplan/Joker) — noch nicht gebaut.
- Produktkonsequenz 22→26 Decks in `KLARTEXT_Digistore24_Produktliste.md`/Preisstrategie — noch nicht
  angepasst.
- Kleiner Nebenfund: Glossar-Link "Joker" zeigt auf `M3-03.html` statt `M3-Joker.html` — noch nicht
  korrigiert.

## Strang 59: Reizfilter INGRA-Overlay + Tic-Dokumentation (TO), Körper-Kompass-Persistenz,
M2-43-Verlinkung (11.08.2026)

Umsetzung des dritten NotebookLM-Prompts ("Präzisierung der Logik für den Reizfilter"), der die
Schwellenwert-Logik (kLAR-Modell/Shortcuts/Feuerwehrkarten je nach Barometer-Stufe), die
Tic-Dokumentation für TO sowie eine Daten-Brücke zwischen Reizfilter, Körper-Kompass und
Ressourcen-Bericht forderte. Vorab per AskUserQuestion geklärt: **getrennte Ansicht per
URL-Parameter**, damit die private, wertungsfreie Jugendlichen-Ansicht des Reizfilters unverändert
bleibt und die INGRA-Zusatzinfos nur bei explizitem Kontext-Aufruf erscheinen.

**Umgesetzt:**
- `KLARTEXT_Spiel_Reizfilter.html`: neue URL-Parameter `?kontext=ingra` (blendet INGRA-Box mit
  kLAR-Modell/Shortcuts/Feuerwehrkarten-Button ein) und `&herkunft=to` (blendet zusätzlich die
  optionale Tic-Zähler-Box ein). Schwellenwert-Mapping der 5 Reglerstufen auf Barometer-Farben:
  Gelb/Orange → kLAR-Kurzanleitung, Orange/Rot → Shortcuts zu Zonen-Set (Rückzugs-Zone) und
  Körper-Kompass, Rot (Maximum) → direkter Button zu den Feuerwehrkarten (`DASHBOARD.html#sek-fk`).
  Ohne `kontext=ingra` bleibt die Jugendlichen-Ansicht exakt wie vorher — kein Verhaltensunterschied,
  keine Kontrollelemente sichtbar.
- Tic-Zähler (`ticAendern()`) speichert additiv in `klartext_reizfilter_verlauf`: bestehendes Schema
  `{datum, stufe}` um optionales Feld `tics` erweitert, rückwärtskompatibel zu allen alten Einträgen.
  Regler-Änderungen überschreiben einen bereits erfassten Tic-Wert für den Tag nicht.
- `KLARTEXT_Spiel_Koerperkompass.html`: hatte bisher **keinerlei** Persistenz (reiner In-Memory-Zustand,
  bei jedem Neuladen verloren) — für die geforderte Daten-Brücke nachgerüstet. Neuer Key
  `klartext_koerperkompass_verlauf`, ein Tages-Snapshot der markierten Körperregionen
  (Intensität + Wörter), analog zum Reizfilter-Muster einmal pro Tag überschrieben. Leere Tage
  (nichts markiert bzw. alles zurückgesetzt) erzeugen keinen Eintrag. Beim Neuladen am selben Tag
  werden bereits gesetzte Markierungen wiederhergestellt.
- `M2-43_Tourette_Tics.html`: neuer Link im Abschnitt "Was hilft?" zu
  `KLARTEXT_Spiel_Reizfilter.html?kontext=ingra&herkunft=to`.

**Bewusst nicht umgesetzt:** Eine Verlauf-Zusammenführung der drei Datenquellen (Reizfilter-Stufe,
Tics, Körper-Kompass) *innerhalb* von `KLARTEXT_Ressourcenbericht.html` selbst — die drei
localStorage-Keys liegen jetzt kompatibel nebeneinander vor (Daten-Brücke ist gebaut), aber der
Ressourcen-Bericht liest sie noch nicht gemeinsam aus. Nicht Teil dieses Prompts; eigener Folge-Task,
falls gewünscht.

**Getestet:** jsdom-Simulation aller Parameter-Kombinationen (kein Kontext / `kontext=ingra` /
`kontext=ingra&herkunft=to` / nur `herkunft=to`), Schwellenwert-Übergänge Gelb→Orange→Rot→Grün mit
Prüfung von Show/Hide-Zuständen aller vier Overlay-Elemente, Tic-Zähler-Increment/Decrement mit
localStorage-Persistenz und Erhalt bei Regler-Änderung, Körper-Kompass-Markierung/-Löschung/-Reset
mit Persistenz- und Wiederherstellungs-Check über einen simulierten Reload.

### Noch offen

- Ressourcen-Bericht liest die drei neuen/erweiterten localStorage-Quellen (Reizfilter-Verlauf inkl.
  Tics, Körper-Kompass-Verlauf) noch nicht zusammengeführt aus — s.&nbsp;o.
- Alle Punkte aus Strang 57/58 (Fachbuch/Trainerhandbuch-Überarbeitung, DS↔bestehende-Tools-Verknüpfung,
  Produktkonsequenz 22→26 Decks, Glossar-Link-Fix "Joker") bleiben unverändert offen.

## Strang 60: Ressourcen-Bericht liest Tic-Korrelation + Körper-Fokus ein (11.08.2026)

Vierter NotebookLM-Prompt schloss die in Strang 59 bewusst offen gelassene Lücke: der
Ressourcen-Bericht sollte die in Strang 59 gebaute Daten-Brücke (Reizfilter-`tics`-Feld,
Körper-Kompass-Verlauf) tatsächlich auslesen und anzeigen. Zwei Ungenauigkeiten im Prompt vorab
korrigiert: (1) Datei heißt `KLARTEXT_Ressourcenbericht.html` im Repo-Root, nicht
`pwa/ressourcenbericht.html` — gleicher Fehlertyp wie schon beim Reizfilter-Prompt in Strang 59;
(2) Punkt 4 des Prompts war mittenabgeschnitten und nicht lesbar — Punkte 1–3 waren eigenständig
umsetzbar, daher umgesetzt und Punkt 4 in der Antwort an Anja zurückgemeldet statt geraten.

**Umgesetzt (`KLARTEXT_Ressourcenbericht.html`):**
- Neue Karte „🌀 Tic-Korrelation": liest alle Einträge mit Feld `tics` aus
  `klartext_reizfilter_verlauf`, gruppiert nach Barometer-Farbe (Grün/Gelb/Orange/Rot, gleiches
  Mapping wie im Reizfilter selbst), zeigt je Farbe Summe/Tage/Tagesschnitt tabellarisch. Bewusst als
  reine Deskription formuliert ("kein Beleg für eine Ursache, aber ein möglicher Gesprächsansatz"),
  keine kausale Überinterpretation der kleinen Stichprobe.
- Neue Karte „🧍 Körper-Fokus": liest den jeweils letzten Tages-Snapshot aus
  `klartext_koerperkompass_verlauf`, zeigt markierte Regionen mit Intensität und optionalen Wörtern
  als Text + Chip-Reihe. Hinweis: der Prompt nannte als Beispieltext „Druck im Bauch, Spannung im
  Kopf" — diese Wörter existieren nicht im echten Körper-Kompass-Vokabular (kribbelig/eng/schwer/
  zittrig/warm), der Bericht zeigt daher die tatsächlich erfassten Begriffe, nicht die Beispielformulierung.
- Beide Karten bleiben vollständig ausgeblendet (`display:none`, kein Leer-Hinweis-Text), wenn keine
  passenden Daten vorliegen — anders als Profil-/Trend-/Zonen-Karte, die immer eine Anleitung zeigen.
  Begründung: Tic-Tracking/Körper-Kompass sind spezialisierte Werkzeuge, ein "du hast das noch nicht
  benutzt"-Hinweis wäre für die meisten Jugendlichen irrelevanter Ballast im Bericht. Da `display:none`
  inline gesetzt wird, gilt das automatisch auch für die Druckansicht (Punkt 3 des Prompts).

**Getestet:** jsdom mit 5 Szenarien (keine Daten, nur Tics, nur Körper-Kompass mit mehreren
Tagen/nur letzter Tag wird gezeigt, beide gleichzeitig, Körper-Kompass-Eintrag ohne Regionen als
Edge-Case) — Sichtbarkeit und Inhalt in allen Fällen korrekt.

### Noch offen

- **Punkt 4 des Prompts fehlte** (Nachricht endete mit „4." ohne Inhalt) — bei Anja nachgefragt,
  war ein Versehen, kein weiterer Punkt.
- Alle Punkte aus Strang 57–59 bleiben unverändert offen.

## Strang 61: Bug-Fix — Login-Redirect-Schleife durch rel="noopener" auf internen Links (11.08.2026)

Anja meldete: "ich werde immer wieder zum login geleitet, z.B. bei feedbackbogen, oder von
weiterleitungen von den neuen tools". Ursache gefunden: Das Login-Gate auf jeder Seite prüft
`sessionStorage.getItem('klartext_login')`. `sessionStorage` wird beim Öffnen eines Links mit
`target="_blank"` nur dann in den neuen Tab übernommen, wenn der neue Tab eine "Opener"-Beziehung
zur ursprünglichen Seite hat. `rel="noopener"` kappt genau diese Beziehung — der neue Tab startet
mit leerem `sessionStorage`, das Gate-Skript hält das für "nicht eingeloggt" und leitet sofort auf
`KLARTEXT_Login.html` um. Betraf ausschließlich interne `target="_blank" rel="noopener"`-Links auf
andere KLARTEXT-Seiten (nicht PDF-Links — dort läuft kein Gate-Skript, daher kein Problem).

**Root-Cause-Suche:** Repo-weite Grep-Recherche über alle .html-Dateien nach der Kombination
`target="_blank" rel="noopener"` bei internen `.html`-Zielen.

**Fix:** `rel="noopener"` entfernt (nicht `target="_blank"` selbst — neue Tabs bleiben erwünscht),
da alle betroffenen Ziele interne, vertrauenswürdige KLARTEXT-Seiten sind — der
Sicherheitsgewinn von `noopener` (Schutz vor "Reverse Tabnabbing" durch fremde Seiten) ist hier
irrelevant, der Schaden (Session-Bruch) überwiegt deutlich. `sessionStorage` (nicht `localStorage`)
bleibt bewusst erhalten — Login endet weiterhin beim Schließen des Tabs/Browsers, wichtig für ein
Tool, das ggf. auf gemeinsam genutzten Schulgeräten läuft.

**Betroffene und korrigierte Dateien (11 Fundstellen):**
- `KLARTEXT_Ressourcenbericht.html` (2× — Moderationsleitfaden, **Feedbackbogen**, exakt Anjas
  gemeldetes Symptom)
- `KLARTEXT_Spiel_Reizfilter.html` (3× — Zonen-Set-, Körper-Kompass-, Feuerwehrkarten-Shortcuts aus
  der neuen INGRA-Overlay-Funktion, Strang 59)
- `M2-43_Tourette_Tics.html` (1× — Link zur Reizfilter-INGRA-Ansicht, Strang 59)
- `KLARTEXT_Spiel_SkillMatrix.html` (3× — Bericht-Link, 2× JD-Karten-Links ins pwa-Kartendeck)
- `KLARTEXT_Spiel_PerspektivWechsler.html`, `KLARTEXT_Spiel_Bewerbungsgespraech.html` (je 1× —
  JD-Karten-Links)
- `KLARTEXT_Spiel_WasHilftMir.html` (1×, im JS-Template `angebot-link` — betrifft *jeden* Link im
  zentralen "Angebote"-Panel dieser Seite, also alle 5 verlinkten Tools + pwa-Karten)

**Bewusst nicht angefasst:** `rel="noopener"` auf PDF-Downloads (`KLARTEXT_Downloads.html` u. a.) —
dort läuft kein Gate-Skript, kein Bug, `noopener` bleibt aus Best-Practice-Gründen.

**Nebenbefund (nicht behoben, da anderes Problem):** ca. 65 Seiten haben gar kein Login-Gate,
darunter `pwa/index.html`, die gesamte `LK-*`-Modulreihe und weitere. Für Landing/Login/Rechtstexte
plausibel gewollt, für `pwa/index.html` und die LK-Reihe eher ein Versehen — umgekehrtes Problem
(fehlender Schutz statt fälschlicher Umleitung), separat zu bewerten, noch nicht mit Anja
abgestimmt.

**Getestet:** Statischer Grep-Check, dass keine internen `.html`-Links mehr `target="_blank"` mit
`rel="noopener"` kombinieren (nur noch PDF-Links, wie beabsichtigt); `node --check` auf allen
betroffenen Dateien nach dem Edit.

### Noch offen

- Fehlendes Login-Gate auf ~65 Seiten (u. a. `pwa/index.html`, `LK-*`-Reihe) — noch nicht mit Anja
  abgestimmt, ob/wo das gewollt ist. Angesichts des Wochenlimits vertagt: ~26 eindeutige Fälle
  (gleiche Familie wie bereits gegatete Geschwister-Seiten) könnten in einer eigenen, günstigen
  Batch-Runde nachgezogen werden, die übrigen ~36 (Eltern-/Lehrkraft-/Admin-Bereich) brauchen erst
  eine Entscheidung von Anja, ob die einen eigenen Zugang haben sollen.
- Alle Punkte aus Strang 57–60 bleiben unverändert offen.

## Strang 62: Neues Tool — Bewerbungs-Generator (Anschreiben DIN 5008 + Lebenslauf) (11.08.2026)

Neuer Prompt (Format wie die vorherigen NotebookLM-Prompts) forderte ein neues Tool
`KLARTEXT_Bewerbungs_Generator.html`: Anschreiben nach DIN 5008 mit "Zauberstab" (Stärken-Sätze aus
der Skill-Matrix), tabellarischer Lebenslauf mit "KLARTEXT-Skills"-Bereich, DIN-5008-Druckansicht mit
Fensterposition, zwei ladbare Muster (klassisch/ressourcenorientiert). Vor dem Bauen Fact-Check
gemacht (eigener Recherche-Subagent) und mit Anja per Rückfrage kurz abgestimmt (Ergebnis: "Alles auf
einmal", trotz 65 %-Wochenlimit).

**Korrigierte Ungenauigkeiten im Prompt:**
- Font-Angabe "Playfair Display / Nunito" war falsch — das echte KLARTEXT-CSS nutzt durchgängig
  Playfair Display + DM Sans (Nunito kommt nur in einer einzigen Kinderseite vor, nicht im Standard).
  Mit der echten Kombination gebaut.
- "KLARTEXT-Skills" als Kategorie-Name existiert nirgends im System (0 Treffer) — nicht übernommen.
  Stattdessen die im System bereits etablierten Begriffe verwendet (Teamfähigkeit, Belastbarkeit
  usw., abgeleitet aus den echten Skill-Matrix-Clustern).
- "Analog zu Modul M2-42" für Muster B war eine gedehnte Analogie: M2-42 behandelt ADHS/
  Ausbildungsreife und würdigt Zwischenschritte (Berufskolleg/BVJ) explizit als "legitime Wege, keine
  Niederlage" — aber es behandelt keine Bewerbungsunterlagen. Diese Grundhaltung wurde für Muster B
  übernommen, ohne M2-42-Wortlaut zu kopieren oder eine engere inhaltliche Übereinstimmung zu
  behaupten, als tatsächlich besteht.

**DIN-5008-Positionsangaben recherchiert und mit echten Quellen belegt** (nicht geschätzt):
Anschriftenfeld Form B (heute die gängige Form für Geschäftsbriefe) beginnt 45 mm von oben, die
Anschriftzone bei 62,7 mm, Feldgröße 85×45 mm, 20 mm vom linken Rand, Beschriftung ab 25 mm (dieselbe
Linie wie der Fließtext); Falzmarken bei 105 mm und 210 mm, Lochmarke bei 148,5 mm — Quellen:
sekretaria.de ("Adressfeld im Geschäftsbrief nach DIN 5008") und federwerk.de ("Faltmarken und
Lochmarken auf Briefblättern nach DIN 5008"), beide unter Bezug auf die DIN-5008-Reform 03/2020.

**Umgesetzt (`KLARTEXT_Bewerbungs_Generator.html`, neu):**
- Zwei Tabs: Anschreiben (DIN-5008-Form-B-Layout, direkt beschreibbare Felder statt separater
  Vorschau) und Lebenslauf.
- Zauberstab: nutzt die echten `anschreiben`-Vorlagensätze aus den 6 Skill-Matrix-Clustern
  (`KLARTEXT_Spiel_SkillMatrix.html`, `CLUSTERS`-Array) statt neu erfundener Formulierungen —
  lokal in `CLUSTER_ANSCHREIBEN_VORLAGEN` gespiegelt, da das gespeicherte Profil selbst keine
  Vorlagen-Sätze enthält, nur titel/hobbys/felder.
- Lebenslauf: dynamische Werdegang-Tabelle (Typ/Von/Bis/Bezeichnung/Ort), sortiert sich automatisch
  antichronologisch (offenes „Bis" = „bis heute", steht oben); Stärken-Bereich mit Übernahme aus dem
  Skill-Matrix-Profil (Cluster-Titel in Bewerbungssprache übersetzt, z. B. "Team-Power" →
  "Teamfähigkeit") plus manuellem Hinzufügen.
- Muster A (klassisch/geradlinig) und Muster B (Berufskolleg-Zwischenschritt, ressourcenorientiert
  formuliert) füllen beide Tabs auf Knopfdruck.
- Entwurf wird laufend in `klartext_bewerbung_entwurf_v1` gespeichert (Muster für sitzungsübergreifende
  Persistenz wie an anderer Stelle im System etabliert).
- Login-Gate wie überall; interne Links ohne `rel="noopener"` (Lehre aus Strang 61).
- Verlinkt in `KLARTEXT_Downloads.html`, `KLARTEXT_Spiele.html` sowie zusätzlich direkt aus der
  Skill-Matrix heraus (im "Bausteine für Anschreiben & Gespräch"-Kasten, wo die Sätze ohnehin
  angezeigt werden).

**Im Test gefundener und behobener Bug:** Die Anrede-Automatik (Anschriftzone → Empfänger-Person →
Anrede-Vorschlag "Sehr geehrte/r …") erkannte fälschlich jede neue Empfänger-Eingabe als "manuell
überschrieben" und aktualisierte die Anrede danach nicht mehr korrekt (z. B. blieb bei einem
Wechsel von "Frau X" auf "Herr Y" die alte weibliche Anrede stehen). Ursache: eine verdrehte
Vergleichslogik. Behoben, per jsdom mit expliziten Frau/Herr-Wechseln nachgetestet.

**Getestet (jsdom, 11 Szenarien):** Tab-Wechsel, Absender→Rücksendeangabe/Gruß-Zeile, Anrede-Automatik
inkl. Bugfix-Nachweis, Zauberstab ohne/mit Profil (inkl. Satz-Rotation über mehrere Klicks),
Werdegang hinzufügen/sortieren/entfernen, Stärken übernehmen/hinzufügen/entfernen, Muster A/B laden,
Formular leeren, Entwurf-Persistenz über einen simulierten Reload.

### Noch offen

- Alle Punkte aus Strang 57–61 bleiben unverändert offen.

## Strang 63: Bewerbungs-Generator — Textbausteine ressourcenorientiert überarbeitet (11.08.2026)

Vierter NotebookLM-Prompt zu diesem Tool: Standardfloskeln in den Zauberstab-Vorlagen und in Muster B
durch einfache, systemische, ressourcenorientierte Sprache ersetzen. Vor dem Umsetzen eine
inhaltliche Rückfrage an Anja gestellt (nicht nur Fakten-Check): Der vorgeschlagene Hauptteil-Satz
nannte wörtlich "das KLARTEXT-System" — Text, der als Beispiel direkt in ein echtes Anschreiben an
eine echte Firma kopiert werden kann. Ein Ausbildungsbetrieb kennt "KLARTEXT" nicht und könnte den
Namen eines Mentoring-Programms eher als "braucht Unterstützung"-Signal lesen als als Stärke.
Entscheidung (Anja): Namen weglassen, Inhalt (Selbstkenntnis, Selbstregulation bei Stress) behalten.

**Weitere Korrektur:** Der Prompt nannte zwei Cluster mit erfundenen Namen ("Fokus-Held",
"Macher-Mut"), die es in der Skill-Matrix nicht gibt — die echten Titel sind "Fokus-Champion" und
"Mutig & Stressfest". Da der Zauberstab die Vorlagen über den echten Cluster-Titel aus dem
gespeicherten Profil nachschlägt, hätte die Übernahme der Fantasienamen als Schlüssel den Zauberstab
für diese zwei Cluster stumm geschaltet (kein Treffer, kein Satz). Mit den echten Titeln als
Schlüssel umgesetzt.

**Umgesetzt (`KLARTEXT_Bewerbungs_Generator.html`):**
- `CLUSTER_ANSCHREIBEN_VORLAGEN`: alle 6 Cluster auf die neue Sprache umgestellt — die 3 im Prompt
  explizit vorgegebenen (Team-Power, Fokus-Champion, Mutig & Stressfest, mit „Mut zur Lücke" bewusst
  zu „Dieser Mut" vereinfacht — das Idiom kann in einer echten Bewerbung leicht als „lässt Dinge
  unfertig" missverstanden werden) sowie 3 im gleichen Duktus ergänzte (Kreativ-Genie,
  Verantwortungs-Anker, Problem-Löser — im Prompt nicht vorgegeben, aus der Gesamtanweisung
  „Standardfloskeln ersetzen" plausibel abgeleitet, damit der Zauberstab nicht drei alte und drei
  neue Sätze mischt).
- Muster B: Einstieg/Hauptteil/Schluss auf die neue Sprache umgestellt (Hauptteil ohne
  Produktnamen, s. o.), an die bestehende Jonas-Berger-Geschichte angepasst statt roh eingefügt.
- Neues Feld `gruss` (vorher fest „Mit freundlichen Grüßen" im HTML) — jetzt Teil des Datenmodells
  und editierbar. Muster A bleibt bei „Mit freundlichen Grüßen", Muster B setzt „Klar. Warm.
  Menschlich." als bewusste Alternative, nicht als erzwungener Systemstandard.

**Getestet (jsdom, 5 Szenarien):** Standard-Gruß im Leerzustand, alle 6 Zauberstab-Cluster liefern
mit den echten Titeln korrekt einen Satz, Muster B enthält den neuen Text und nicht mehr "KLARTEXT",
Muster A behält den traditionellen Gruß, Gruß-Feld ist editierbar und wird persistiert.

### Noch offen

- Alle Punkte aus Strang 57–62 bleiben unverändert offen.

## Strang 64: Trainerhandbuch — Kapitel 9 "Bewerbungscoaching & Berufsvorbereitung" (11.08.2026)

Fünfter Prompt zum Bewerbungs-Themenkomplex, diesmal ein Trainerhandbuch-Kapitel statt Code. Vorab
kurz nach Aufwand gefragt (Wochenlimit 65 %) und ehrlich eingeschätzt: klein, weil (a) das
`KLARTEXT_Trainerhandbuch.html` bereits 8 Kapitel in einer wiederverwendbaren Struktur hat (Kapitel
einfach als Nr. 9 einsetzen) und (b) der im Prompt erwähnte „Bewerbungs-Simulator" kein fehlendes
Tool ist, sondern nur ein anderer Name für das längst existierende
`KLARTEXT_Spiel_Bewerbungsgespraech.html`.

**Fact-Check (kurz, da Aufwand gering sein sollte):** JD-3 „Meine Stärken sehen", JD-27 „Was mir
wichtig ist", JD-17 „Vor der Prüfung: was hilft wirklich?" und `M2-13_Selbstwirksamkeit.html`
existieren alle exakt wie im Prompt benannt — keine Korrektur nötig.

**Umgesetzt (`KLARTEXT_Trainerhandbuch.html`):** Kapitel 9 „Bewerbungscoaching &
Berufsvorbereitung" nach dem bestehenden Muster ergänzt (Inhaltsverzeichnis-Eintrag, Kapitel-Artikel
mit `.ab`-Blöcken, `.phasen-kette` für die 3-Phasen-Tool-Kette, `.box-tipp` am Ende) — fünf
Abschnitte: rechtlicher Rahmen (SGB IX/Eingliederungshilfe, DSGVO, DIN 5008 — ausdrücklich als
fachliche Orientierung, nicht als Rechtsberatung formuliert, mit Verweis auf Rücksprache bei der
Eingliederungshilfe-Fachstelle im Einzelfall), systemische Haltung, Tool-Kette (Selbsterkenntnis →
Dokumentenerstellung → Training & Simulation, mit den echten Datei-/Kartenverweisen), Umgang mit
Vermittlungshemmnissen (Neurodivergenz/M2-42, Prüfungsangst/JD-17), Dokumentation für Kostenträger
(Ressourcen-Bericht). Quellenverzeichnis um SGB IX, DSGVO und DIN 5008 (mit Verweis auf die in
Strang 62 recherchierten Positionsangaben) ergänzt.

**Getestet:** Struktur-Check (9 `<article class="kapitel">`-Elemente, TOC-Link vorhanden), alle im
Kapitel referenzierten Dateien existieren tatsächlich im Repo.

### Noch offen

- Alle Punkte aus Strang 57–63 bleiben unverändert offen.

## Strang 65: Trainerhandbuch — Checkliste "Erstgespräch mit dem Arbeitgeber" in Kapitel 9 (11.08.2026)

Sechster Prompt zum Themenkomplex: eine Netzwerkarbeit-Checkliste für Jobcoaches, in Kapitel 9
eingefügt (gleiche `.checkliste`-Vorlage wie Kapitel 4, kein neues Dokument — geringerer Aufwand,
gleicher Nutzen).

**Zwei Korrekturen:**
- Der Prompt schlug erneut "die Joker-Karten" (Plural) als Sicherheitsnetz vor — wie schon in
  Strang 58/59 festgestellt, existiert keine Joker-Kartendeck; der Joker ist ein einzelnes,
  individuell vereinbartes Signal (`M3-Joker.html`). Checkliste verweist auf den echten, singulären
  Joker plus den Reizfilter, nicht auf eine erfundene Kartensammlung.
- "M4-16" wurde als Quelle der "5-Schritte-Logik" (Zuhören → Validieren → Ressourcen benennen →
  Tool vorschlagen → Vereinbarung) genannt — geprüft: `M4-16_Migrantische_Eltern.html` behandelt
  Elterngespräche mit migrantischen Familien, hat nichts mit einer Argumentationslogik für
  Arbeitgebergespräche zu tun. Keine passende Quelle im System für dieses Vorgehen gefunden. Im
  Kapitel als eigenständige, an das Gespräch angepasste Anwendung der lösungsorientierten Haltung
  (im Geiste des kLAR-Modells) ausgewiesen, nicht fälschlich einem Modul zugeschrieben.

**Umgesetzt:** Neuer `.ab`-Block in Kapitel 9 mit den 5 Phasen (Vorbereitung, Einstieg,
Bedarfsanalyse, Transparenz &amp; Sicherheit, Abschluss) als `.checkliste`-Listen, plus
Tipp-Box mit der korrigierten 5-Schritte-Logik.

**Getestet:** div-Bilanz (121 auf/121 zu), keine „Joker-Karten"-Pluralfiktion im neuen Abschnitt.

### Noch offen

- Alle Punkte aus Strang 57–64 bleiben unverändert offen.

## Strang 66: KLARTEXT_ContextMapper.js — Jobcoach-Modus für erwachsene Klient:innen (11.08.2026)

Siebter Prompt: ein leichtgewichtiges Skript, das pädagogische Begriffe (Schüler, Kind, Lehrkraft,
Schultag, Hausaufgaben) im DOM durch Jobcoaching-taugliche Formulierungen ersetzt, aktiviert per
`?modus=jobcoach` oder localStorage-Flag. Der Auftrag war an einer Stelle technisch nicht wörtlich
umsetzbar und wurde entsprechend angepasst, nicht stillschweigend anders gebaut.

**Technische Korrektur (kein Fakten-, sondern ein Machbarkeits-Fehler):** "Kontextabhängig" zwischen
„Teilnehmer" und „Klient" wählen ist mit reiner Text-Ersetzung nicht sauber möglich — das würde
Satzverständnis brauchen, nicht nur Wortabgleich, und wäre kein „leichtgewichtiges JavaScript" mehr.
Umgesetzt: eine feste Zielformulierung pro Begriffsfamilie (Schüler/Kind → „Teilnehmer:in"), an
einer Stelle im Code leicht auf „Klient:in" umstellbar, falls gewünscht.

**Sicherheitsprinzipien der Umsetzung** (wichtig, weil das Skript live vor echten Arbeitgeber:innen
läuft — ein kaputtes DOM in dem Moment wäre schlimmer als gar keine Funktion):
- Nur echte Textknoten werden verändert (TreeWalker), nie `innerHTML` — kein Risiko, Event-Handler
  oder Attribute kaputtzumachen.
- Nur die Attribute `placeholder`/`aria-label`/`title` werden ersetzt, **nie** `value` — echte
  Nutzereingaben werden nie überschrieben.
- `<script>`/`<style>`/`<code>`/`<textarea>`-Inhalte werden ausgeschlossen.
- Wortgrenzen-sichere, längste-Muster-zuerst sortierte Ersetzung, damit z. B. „Lehrkraft reagiert"
  (Sonderfall Joker-Karte) vor der generischen „Lehrkraft"→„Coach"-Regel greift und „Schülerinnen"
  nicht falsch zerlegt wird.
- MutationObserver mit Disconnect/Reconnect um die eigenen Schreibvorgänge, damit keine Endlosschleife
  entsteht — deckt automatisch dynamisch nachgerenderten Inhalt ab (Skill-Matrix-Cluster,
  Bewerbungs-Generator-Werdegang), ohne dass die aufrufenden Seiten selbst etwas dafür tun müssen.
- Deckt die im Auftrag genannten Begriffsfamilien in ihren gängigen Flexionsformen ab
  (Singular/Plural/Genitiv/Dativ) — bewusst keine vollständige Grammatikabdeckung, neue Formen lassen
  sich leicht ergänzen.

**Eingebunden wie angefragt in:** `index.html`, `KLARTEXT_Spiel_SkillMatrix.html`,
`KLARTEXT_Bewerbungs_Generator.html`.

**Nebenbefund:** `index.html` ist die öffentliche Marketing-Landingpage ohne Login-Gate — sie enthält
aktuell keinen der Zielbegriffe (0 Treffer bei Schüler/Lehrkraft/Schultag/Hausaufgabe), das Skript
greift dort also derzeit ins Leere (harmlos, aber wirkungslos). `DASHBOARD.html`, der tatsächliche
Einstiegspunkt nach dem Login, enthält 12 Treffer — vermutlich die eigentlich relevante Seite für
den Praxisfall "Jobcoach zeigt einem/einer Klient:in das System". Nicht eigenmächtig ergänzt, da
außerhalb des angefragten Umfangs; auf Wunsch schnell nachrüstbar.

**Getestet (jsdom, 10 Szenarien):** inaktiv (Text unverändert), Aktivierung via URL-Parameter inkl.
localStorage-Persistenz, Aktivierung via localStorage, Sonderfall „Lehrkraft reagiert", alle
Flexionsformen der 5 Begriffsfamilien, Placeholder ersetzt/`value` unangetastet, Script-/Style-Inhalte
geschützt, MutationObserver erfasst dynamisch hinzugefügten Text, `?modus=schule` schaltet aktiv
zurück, öffentliche API (`aktivieren()`/`deaktivieren()`/`istAktiv()`).

### Noch offen (Status: **finalisiert und ausgerollt in Strang 67**, s. u.)

- Alle Punkte aus Strang 57–65 bleiben unverändert offen.

## Strang 67: ContextMapper — Rollout finalisiert (Dashboard, Reizfilter, Körper-Kompass) (11.08.2026)

Achter Prompt, angekündigt als "Strang 62b" mit der Bitte, "Strang 62 als finalisiert und ausgerollt"
zu markieren. Beides korrigiert: Strang 62 ist der Bewerbungs-Generator (DIN 5008), hat mit dem
ContextMapper nichts zu tun — die tatsächlich relevante Doku ist **Strang 66**. Nicht fälschlich
Strang 62 umbenannt, sondern hier als eigener Strang 67 die Fertigstellung von Strang 66 dokumentiert.

**Dateinamen im Prompt erneut falsch** (gleiches Muster wie schon mehrfach in diesem Themenkomplex):
`KLARTEXT_Skill_Matrix.html` → echt: `KLARTEXT_Spiel_SkillMatrix.html` (hatte den Mapper schon seit
Strang 66); `reizfilter.html` → echt: `KLARTEXT_Spiel_Reizfilter.html`; `koerperkompass.html` → echt:
`KLARTEXT_Spiel_Koerperkompass.html`. Mit den echten Dateinamen umgesetzt.

**Umgesetzt:**
- `<script src="KLARTEXT_ContextMapper.js">` ergänzt in `DASHBOARD.html` (die in Strang 66 als
  Nebenbefund identifizierte, tatsächlich relevante 12-Treffer-Seite), `KLARTEXT_Spiel_Reizfilter.html`
  und `KLARTEXT_Spiel_Koerperkompass.html`. Damit haben jetzt alle 5 vom Auftrag genannten Stellen
  (Dashboard + 4 Tools) den Mapper eingebunden.
- **Zustands-Sicherung (Punkt 3) war bereits durch die Architektur aus Strang 66 gelöst**, ohne
  weiteren Code: `?modus=jobcoach` wird beim ersten Aufruf in `localStorage` gespiegelt, und jede
  Seite mit eingebundenem Mapper prüft beim Laden zuerst den URL-Parameter, dann `localStorage`. Ein
  interner Link ganz ohne `?modus=jobcoach` in der URL aktiviert den Jobcoach-Modus auf der Zielseite
  trotzdem korrekt, solange dort ebenfalls der Mapper eingebunden ist — genau das war mit Punkt 2
  jetzt für alle 5 Seiten sichergestellt. Kein automatisches Anhängen des Parameters an interne Links
  gebaut (unnötig zusätzliche, invasivere Lösung für dasselbe Ergebnis, das der Prompt selbst als
  Alternative nennt: "oder dauerhafte Speicherung im localStorage").

**Getestet:** Gezielter Smoke-Test mit dem echten `DASHBOARD.html` (nicht nur synthetisches Test-HTML)
per jsdom — `?modus=jobcoach` aktiviert korrekt, `Schultag` → `Arbeitstag` bestätigt, „Geheimschüler-
Ausweis" (zusammengesetztes Wort, enthält „schüler" als Teilstring) bleibt korrekt unangetastet
(Wortgrenzen-Erkennung funktioniert auch an echtem, nicht konstruiertem Inhalt). Eine Einschränkung
ehrlich benannt: `DASHBOARD.html` lädt einen Teil seiner Kachel-Inhalte ("Mit Lehrkraft sprechen" u. ä.)
laut Code offenbar dynamisch über Firebase — das lässt sich in der netzwerklosen Test-Umgebung nicht
auslösen und daher nicht automatisiert verifizieren. Der gleiche MutationObserver-Mechanismus, der in
Strang 66 für dynamisch nachgeladenen Inhalt bereits erfolgreich getestet wurde, sollte auch hier
greifen — eine kurze manuelle Sichtprüfung im echten Browser mit `?modus=jobcoach` wäre trotzdem
sinnvoll, um diesen einen Pfad wirklich zu bestätigen.

### Noch offen

- Manuelle Sichtprüfung der Firebase-geladenen Dashboard-Kacheln im echten Browser (s. o.) — nicht
  automatisiert testbar in dieser Umgebung.
- Alle Punkte aus Strang 57–65 bleiben unverändert offen.

## Strang 68: QR-Code-Integration — Joker-Karte & Superpower-Card (11.08.2026)

Neunter Prompt in der QR-Code-Themenreihe. Anders als der vorherige Gesamtvorschlag (dort noch 4
Punkte inkl. Insel-Set und TK-Recruiting) beschränkte sich dieser konkrete Bauauftrag auf 2 der 4
Punkte — Joker-Karte und Superpower-Card — plus den ausdrücklichen Hinweis, das Insel-Set
wegzulassen. Genau in diesem Umfang umgesetzt; TK-Recruiting und Insel-Set bleiben unangetastet,
bis dafür ein eigener Auftrag kommt.

**Vorab fachlich geprüft/korrigiert:**
- `joker-karte.html` aus dem Prompt existiert nicht — echte Datei: `M3_DL_Joker-Karte.html` (8
  identische Karten, 2-spaltiges A4-Raster, Login-Gate vorhanden).
- Kritischer, nicht im Prompt erwähnter Punkt: Ein QR-Code, der nur auf einen **relativen** Pfad
  wie `KLARTEXT_Spiel_Reizfilter.html` zeigt, funktioniert nicht, wenn ein fremdes Gerät (z. B. das
  Handy der Lehrkraft) ihn scannt — es gibt keinen Browser-Kontext, der den relativen Pfad auflösen
  könnte. Die echte, im Repo mehrfach verwendete Produktions-Domain `https://klartext-mentoring.de/`
  wurde recherchiert (Fund: `KLARTEXT_Shop_Uebersicht.html`- und `*_Verkaufsseite.html`-Links) und für
  alle neuen QR-Ziele als absolute URL verwendet.
- Die im Prompt vorausgesetzte Zielseite `profil.html?data=XYZ` existierte nicht — neu angelegt als
  `KLARTEXT_Profil_Ansicht.html`, mit klarerem, KLARTEXT-konformem Dateinamen.
- Architektur-Punkt aus der letzten Rückfrage (Antwort erhalten: kompakte Profil-Zusammenfassung
  lokal in die URL kodieren, keine Dritt-API): umgesetzt — siehe unten.

**Umgesetzt:**
- **`KLARTEXT_QRCode.js`** (neu, vendored): enthält die Bibliothek `qrcode-generator` von Kazuhiko
  Arase (MIT-Lizenz, Version 2.0.4, https://github.com/kazuhikoarase/qrcode-generator) fast
  unverändert als lokale Datei — bewusst nicht per CDN geladen, damit keine Texte/Profildaten an
  einen fremden Server gehen und die Seite ohne Internetzugriff funktioniert. Am Dateiende ein
  kleiner KLARTEXT-Wrapper `window.KLARTEXT_QRCode.erzeugeSvg(text, opts)`, der ein fertiges,
  skalierbares `<svg>` liefert (Fehlerkorrektur-Level „M", automatische QR-Version je nach
  Textlänge, QR-Norm-Ruhezone von 4 Modulen unverändert gelassen statt hart auf einen festen Wert
  gesetzt).
- **`M3_DL_Joker-Karte.html`:** Auf allen 8 Karten ein 13×13 mm großes QR-Feld neben dem
  Merksatz ergänzt (Flex-Zeile `.jk-footer`, Merksatz bekommt `flex:1`, QR-Feld `flex:0 0 13mm`) —
  das 2-spaltige A4-Raster bleibt erhalten, Karten werden nur geringfügig höher, nichts überlappt
  oder verschiebt sich. Alle 8 QR-Codes zeigen auf denselben absoluten Link
  (`https://klartext-mentoring.de/KLARTEXT_Spiel_Reizfilter.html`), daher wird das SVG einmal
  erzeugt und in alle 8 Felder eingesetzt (kein 8-facher Rechenaufwand).
- **`KLARTEXT_Profil_Codec.js`** (neu, gemeinsam genutzt von Superpower-Card und Profil-Ansicht):
  Tabelle `CLUSTER_INFO` mit den 6 echten Cluster-IDs/Icons/Titeln aus
  `KLARTEXT_Spiel_SkillMatrix.html` (`team`, `fokus`, `kreativ`, `verantwortung`, `problem`,
  `mutig`) sowie denselben Berufssprache-Labels wie `CLUSTER_STAERKE_LABEL` im
  Bewerbungs-Generator (z. B. `fokus` → „Konzentrationsfähigkeit & Ausdauer"), damit alle drei Tools
  dieselbe Sprache sprechen. Funktionen `kodieren(name, clusterIds)` / `dekodieren(searchParams)`
  sowie `clusterAusLocalStorage()` (liest `klartext_skillmatrix_profil_v1` und mappt die
  gespeicherten Cluster-Titel zurück auf die kurzen IDs).
  **Bewusste Datensparsamkeit:** Im QR/Link stehen nur Name + bis zu 3 Cluster-IDs (kurz, z. B.
  `?n=Alex&c=team,fokus,mutig`) — keine Hobbys, Berufsfelder oder Beispielberufe aus dem
  Superpower-Profil. Das hält den QR-Code klein/gut scanbar UND gibt einer scannenden Arbeitgeberin
  /einem Arbeitgeber nicht mehr persönliche Details preis, als für eine Vorstellungs-Karte nötig
  sind — konsistent mit der bestehenden Privacy-Haltung der App (Sorgen-Kiste, sessionStorage-Login).
- **`KLARTEXT_Superpower_Card.html`** (neu): Login-gated Druckvorlage. Liest die Top-3-Cluster über
  `clusterAusLocalStorage()`; ist noch kein Superpower-Profil vorhanden, wird statt einer leeren
  Karte ein Hinweis mit direktem Link zum Skill-Matrix-Spiel gezeigt (keine kaputte/leere Karte).
  Name wird per Eingabefeld erfasst (eigener Speicherort `klartext_superpowercard_name_v1`, mit dem
  Hinweis, dass auch der Vorname allein reicht). Zwei identische Karten pro A4-Seite zum
  Ausschneiden (gleiches Muster wie die bestehende Joker-Karten-Vorlage), je Karte: Name, Top-3-
  Cluster mit Berufssprache-Label, sowie ein 18×18 mm QR-Code zur Profil-Ansicht. Zusätzlicher
  „Online-Ansicht testen"-Link (öffnet die Zielseite direkt im Browser), damit Teilnehmende/
  Trainer:innen vor dem Drucken selbst prüfen können, was Arbeitgeber:innen später sehen.
- **`KLARTEXT_Profil_Ansicht.html`** (neu): **Bewusst ohne Login-Gate** — das ist die Seite, die
  eine fremde Person (Arbeitgeber:in) über den QR-Code öffnet, die hat keinen KLARTEXT-Zugang und
  soll auch keinen brauchen. Liest zuerst `?n=`/`?c=` aus der URL (der Regelfall beim Scan durch
  Dritte); ist kein `c`-Parameter vorhanden, greift ein Fallback auf `klartext_skillmatrix_profil_v1`
  im lokalen Speicher (Vorschau auf dem eigenen Gerät ohne Parameter). Ist gar kein Profil auffindbar,
  erscheint ein freundlicher Leer-Zustand statt einer leeren/kaputten Seite. `<meta name="robots"
  content="noindex">` gesetzt, damit diese Profil-Seiten nicht in Suchmaschinen landen.
- Verlinkung: neuer Eintrag „Superpower-Card" in `KLARTEXT_Downloads.html` (direkt nach dem
  Bewerbungs-Generator) sowie ein zusätzlicher Link im „Bausteine für Anschreiben & Gespräch"-Kasten
  in `KLARTEXT_Spiel_SkillMatrix.html`, analog zum bestehenden Bewerbungs-Generator-Link — beide ohne
  `rel="noopener"` bzw. serverseitige Navigation, gemäß der in Strang 61 festgelegten Regel.

**Getestet (jsdom, gegen die echten Dateien):**
- `M3_DL_Joker-Karte.html`: alle 8 `.jk-qr`-Felder korrekt mit SVG befüllt, Kartenanzahl unverändert
  bei 8.
- `KLARTEXT_Superpower_Card.html`: mit gespeichertem Profil → 2 Karten, je 3 Cluster in korrekter
  Stärke-Reihenfolge, QR vorhanden, Vorschau-Link enthält die absolute Domain und korrekt kodierte
  Umlaute/ß (`Alex Müßig` → `Alex+M%C3%BCßig`-artige, korrekt decodierbare Kodierung); ohne Profil →
  Hinweis-Box sichtbar, keine leeren Karten gerendert.
- `KLARTEXT_Profil_Ansicht.html`: mit `?n=&c=`-Parametern → Name inkl. Umlaut/ß und alle 3 Cluster in
  korrekter Reihenfolge gerendert; ganz ohne Parameter und ohne lokalen Speicher → Leer-Zustand; ohne
  Parameter, aber mit lokal gespeichertem Profil → Fallback-Karte korrekt aus `localStorage` gefüllt.
- Struktur-Check (`<div>`-Balance) für alle 5 geänderten/neuen Dateien: durchweg ausgeglichen.
- `KLARTEXT_QRCode.js` und `KLARTEXT_Profil_Codec.js`: Syntax-Check (`node --check`) fehlerfrei.

### Noch offen

- **TK-Recruiting.html** (Punkt 4 des ursprünglichen Gesamtvorschlags) und **Insel-Set/Python-
  Pipeline** (Punkt 2) waren nicht Teil dieses konkreten Auftrags und wurden entsprechend nicht
  angefasst.
- Kein echter QR-Scan-Test mit einem physischen Smartphone durchgeführt (in dieser Umgebung nicht
  möglich) — die generierten SVGs sind nach QR-Norm aufgebaut (Standard-Ruhezone, Fehlerkorrektur
  „M"), ein kurzer Praxis-Scan-Test nach dem Ausdrucken wird trotzdem empfohlen.
- Alle Punkte aus Strang 57–67 bleiben unverändert offen.

## Strang 69: DASHBOARD.html — sichtbarer Schule/Jobcoach-Umschalter (12.08.2026)

Bug-Meldung: "ich kann nicht switchen zwischen Kind und Jobcoach App....es überschreibt automatisch,
ich muss über den Login und dann kommt immer die Kind-Variante....wie können wir es ändern?
möglichst einfach...."

**Ursache gefunden (Code-Lesen, kein spekulativer Fix):** Der Jobcoach-Modus ließ sich seit Strang 66
ausschließlich über den URL-Parameter `?modus=jobcoach` aktivieren. Zwei Stellen im bestehenden
Login-Ablauf leiten aber immer auf eine URL **ohne** diesen Parameter weiter: `DASHBOARD.html` leitet
bei abgelaufener Session (sessionStorage — läuft laut Design beim Schließen des Tabs ab) auf
`KLARTEXT_Login.html` ohne jeden Query-String um; `weiterleiten()` in `KLARTEXT_Login.html` leitet nach
erfolgreichem Login ebenso immer auf eine "nackte" `ZIELE[rolle]`-URL um. Der Jobcoach-Modus wird zwar
zusätzlich in `localStorage` gespiegelt (sollte einen Login-Umweg technisch überstehen), aber es gab
bislang **keinerlei sichtbaren Hinweis oder Schalter**, um den aktuellen Modus zu erkennen oder gezielt
zu wechseln — die einzige Möglichkeit war, den Parameter von Hand in die Adresszeile zu tippen. Das
erklärt "möglichst einfach" am treffendsten: nicht als komplexer technischer Defekt, sondern als
fehlende Bedienoberfläche für einen im Hintergrund eigentlich funktionierenden Mechanismus.

**Umgesetzt:**
- Neuer Button „🎓 Schule" / „💼 Jobcoach" im Desktop-Header von `DASHBOARD.html` (neben Login/Logout)
  und ein entsprechender Eintrag „🎓 Modus: Schule" / „💼 Modus: Jobcoach" im mobilen Menü.
- Funktion `modusUmschalten()`: nutzt die bereits vorhandene, öffentliche
  `KLARTEXT_CONTEXT_MAPPER`-API (`aktivieren()`/`deaktivieren()`) — kein neuer Speicherort, weiterhin
  derselbe `localStorage`-Schlüssel `klartext_modus` wie seit Strang 66. Nach dem Umschalten wird die
  Seite neu geladen, weil der ContextMapper Text nur einseitig ersetzt und bereits ersetzten Text ohne
  Neuladen nicht zurückverwandeln kann (das war schon in `deaktivieren()` selbst per `console.info` so
  dokumentiert).
- Button-Beschriftung zeigt beim Laden automatisch den tatsächlich aktiven Modus (`istAktiv()`), nicht
  nur eine feste Beschriftung.
- Bewusst nur auf `DASHBOARD.html` beschränkt (die Seite, auf der laut Bug-Meldung jedes Mal nach dem
  Login gelandet wird) — nicht auf Reizfilter/Körper-Kompass/Skill-Matrix/Bewerbungs-Generator
  ausgeweitet, um die Änderung klein und schnell nachvollziehbar zu halten. Bei Bedarf leicht auf
  weitere Seiten übertragbar (gleiches Muster, 3 Codeblöcke).

**Getestet:** jsdom gegen die echte Datei — Button zeigt „Schule" ohne gesetzten Modus, „Jobcoach" mit
`klartext_modus=jobcoach` in `localStorage` (inkl. bereits ersetztem Text auf der Seite); ein Klick auf
den Button setzt bzw. löscht den `localStorage`-Schlüssel korrekt, unabhängig vom Ausgangszustand.
div-Balance-Check und isolierter Syntax-Check des neuen Inline-Scripts fehlerfrei.

### Noch offen

- Umschalter bisher nur auf `DASHBOARD.html` — falls gewünscht, gleiches Muster auf
  `KLARTEXT_Spiel_Reizfilter.html`, `KLARTEXT_Spiel_Koerperkompass.html`,
  `KLARTEXT_Spiel_SkillMatrix.html` und `KLARTEXT_Bewerbungs_Generator.html` übertragen.
- Kein echter Login-Rundlauf-Test im echten Browser (Login → Session-Ablauf → erneuter Login)
  durchgeführt, nur die zugrundeliegende Logik isoliert per jsdom geprüft.
- Alle Punkte aus Strang 57–68 bleiben unverändert offen.

## Strang 70: BAROMETER_KIND.html — professionelle Selbsteinschätzung im Jobcoach-Modus (12.08.2026)

Auftrag: im Jobcoach-Modus die bunten Barometer-Buttons durch einen 0–10-Status-Slider ersetzen,
inkl. anonymer Teilnehmer-ID-Verwaltung. Ursprünglich als Frage zur Speicherung des 0–10-Werts gestellt
(Bucket-Mapping vs. echte neue Datenbank-Spalte) — die Antwort kam als vollständig ausformulierte,
deutlich größere Spezifikation zurück (inkl. neuer Teilnehmer-ID-Verwaltung, DSGVO-Anonymisierung,
eigenem Mapping-Schema, Rückwärts-Mapping). In diesem erweiterten Umfang umgesetzt.

**Fundort korrigiert (wie schon bei Strang 69):** Die eigentliche Barometer-Oberfläche liegt nicht im
Dashboard, sondern in `BAROMETER_KIND.html` — dort auch bereits richtig vermutet.

**Wichtiger, vorab geprüfter Architektur-Fakt:** Die Supabase-Spalte `barometer_kind.farbe` hat eine
feste Datenbank-Regel (`check farbe in ('gruen','gelb','orange','rot','grau')`, siehe
`supabase/migrations/0007_barometer.sql`) — ein roher 0–10-Wert kann dort technisch nicht ankommen.
Exakt mit dem im Prompt selbst vorgegebenen Mapping umgesetzt: 0–2→gruen, 3–4→gelb, 5–6→orange,
7–8→rot, 9–10→grau. Der exakte Zahlenwert geht dabei nicht verloren — er wird zusätzlich lesbar vor
die Notiz gestellt (z. B. „[Status 7/10] …") sowie als eigenes, schemaloses Feld zusätzlich nach
Firebase geschrieben.

**Zweiter, vorab geprüfter Architektur-Fakt (nicht im Prompt erwähnt, aber entscheidend für die
Teilnehmer-ID-Verwaltung):** Die RLS-Regeln auf der Tabelle `kinder` (`supabase/migrations/
0002_kinder_stammdaten.sql`) verlangen für **jeden** Zugriff — auch nur Lesen — eine eingeloggte
tk/admin-Session (`auth.uid()` muss zu einem `profiles`-Eintrag mit passender `traeger_id` und
`rolle in ('tk','admin')` gehören). Es gibt keine anonyme Lese- oder Schreib-Policy auf `kinder`.
Das bedeutet: Anlegen/Löschen von Teilnehmer-IDs **muss** eingeloggt passieren — das war technisch nicht
verhandelbar, keine gewählte Option, sondern eine Konsequenz der bestehenden Datenbank-Sicherheit.
Nebenbefund dabei: Der bestehende Code-Kommentar in `BAROMETER_KIND.html` („bewusst ohne Login/
INGRA-Filter, Kind-Self-Service-Gerät") dürfte nach den echten RLS-Regeln nie ganz zugetroffen haben —
nicht repariert (außerhalb dieses Auftrags), aber im neuen Jobcoach-Teil korrekt berücksichtigt.

**Umgesetzt (alles in `BAROMETER_KIND.html`, keine neue Datei):**
- **Moduserkennung:** eigene, schlanke Kopie der `klartext_modus`-Logik aus `KLARTEXT_ContextMapper.js`
  (nicht per `<script src>` eingebunden, weil hier mehr als Text-Ersetzung nötig ist — ganze
  UI-Abschnitte werden ein-/ausgeblendet, nicht nur einzelne Wörter ersetzt).
- **Teilnehmer-ID-Verwaltung** (`.jc-only`, nur Jobcoach-Modus): Anlegen/Entfernen anonymer Kürzel
  (z. B. „TN-DO-01"). Bewusst **keine neue Tabelle/Migration** — anonyme IDs werden als ganz normale
  Zeilen in der bestehenden Tabelle `kinder` angelegt (`name` = die anonyme ID, keine weiteren Felder
  befüllt), markiert über `bedarfsart='jobcoach-anonym'` (Freitextfeld als Marker zweckentfremdet,
  statt eine eigene Spalte per Migration anzulegen — bewusste „möglichst einfach"-Entscheidung, bei
  Bedarf später sauber nachrüstbar). Dadurch bleiben `barometer_kind` (Fremdschlüssel `kind_id`),
  bestehende RLS-Policies und die TK-Weiterleitung unverändert nutzbar. „Löschen" ist technisch ein
  Soft-Delete (`aktiv=false`, `ausgetreten_am=heute` — dieselben Felder, die für echte Kinder bereits
  existieren), kein echtes `DELETE`: `barometer_kind.kind_id` verweist ohne `on delete cascade` auf
  `kinder.id`, ein echtes Löschen würde an bereits gespeicherten Verlaufsdaten mit einem
  Fremdschlüssel-Fehler scheitern.
- **Teilnehmer-Auswahl im Jobcoach-Modus gefiltert** (`bedarfsart='jobcoach-anonym'`): Es werden
  ausschließlich die anonymen IDs angezeigt, nie echte Kindernamen aus dem Schul-Kontext — das war der
  DSGVO-Kern des Auftrags („Es dürfen keine Klarnamen gespeichert werden").
- **Status-Slider (0–10):** ersetzt die bunten Barometer-Buttons (inkl. dem grauen Vollbreite-Button)
  vollständig im Jobcoach-Modus. Endpunkt-Beschriftung exakt wie gefordert: „0 – Alles entspannt" /
  „10 – Maximale Belastung". Beim Bewegen wird sofort dieselbe `speichereKind()`-Logik vorbereitet, die
  auch die Farb-Buttons nutzen (ein Datenpfad für beide Modi, kein Duplikat).
- **Rückwärts-Mapping:** Beim Wechsel/Wiederherstellen einer Teilnehmer-ID springt der Slider auf die
  zuletzt gespeicherte Farbe (obere Grenze je Bereich verwendet, z. B. „gelb" → Slider auf 4 — exakt das
  Beispiel aus dem Auftrag).
- **Textanpassungen:** „Zeig wie du dich gerade fühlst." → „Aktueller Status-Check"; „Wer bist du?" →
  „Teilnehmer-ID wählen"; „Einschätzung der INGRA" → „💼 Coach-Einschätzung", inkl. angepasster
  Unter-/Hinweistexte und des Vergleichstexts bei abweichender Einschätzung (Kind/INGRA →
  Teilnehmer:in/Coach).
- **Sachlichere Rückmeldung:** im Jobcoach-Modus kein Konfetti und kein Brainy-Emoji im
  „Gespeichert"-Button (nur bei den Kind-Farbbuttons weiterhin wie bisher) — passend zum Ziel „sachliche,
  erwachsenengerechte Oberfläche".

**Getestet:**
- Syntax-Check (`node --check`) des extrahierten Moduls fehlerfrei.
- Reine Mapping-Logik isoliert geprüft: alle 11 Slider-Werte (0–10) ergeben die im Auftrag vorgegebene
  Farbe; Rückwärts-Mapping-Werte (2/4/6/8/10) transformieren konsistent wieder auf dieselbe Farbe
  zurück; Beispiel aus dem Auftrag „gelb → 4" exakt bestätigt.
- jsdom-Test gegen die echte Datei (Supabase-Client testweise durch einen Mock ersetzt, da das reale
  Modul von einer externen CDN/einem Live-Projekt importiert und in dieser Sandbox nicht ausgeführt
  werden kann/soll): Schule-Modus zeigt weiterhin unverändert Buttons/Original-Texte; Jobcoach-Modus
  ohne Login zeigt Slider + Login-Hinweis, Verwaltung ausgeblendet; Jobcoach-Modus eingeloggt zeigt
  Verwaltungsliste + gefilterte, ausschließlich anonyme Teilnehmer-Auswahl (kein Klarname im Dropdown
  bestätigt); Slider-Bewegung auf 7 färbt den Speichern-Button korrekt rot; Wiederherstellung mit
  Verlaufseintrag „gelb" setzt den Slider korrekt auf 4.
- Struktur-Check: `<div>`-Balance ausgeglichen (88/88), keine doppelten `id`-Attribute.

### Noch offen

- Kein echter Test gegen die echte Supabase-Datenbank (Login, `profiles.traeger_id`-Auflösung, echtes
  Anlegen/Soft-Löschen einer Teilnehmer-ID) — nur gegen einen Mock geprüft. Ein kurzer manueller
  Rundlauf im echten Browser (einloggen → Teilnehmer-ID anlegen → Status speichern → Verlauf prüfen)
  wird empfohlen, bevor das im echten Coaching-Alltag genutzt wird.
- Vorbestehender, bei diesem Fact-Check entdeckter (aber nicht behobener) Befund: Der Kommentar „Kind-
  Auswahl bewusst ohne Login" in `BAROMETER_KIND.html` dürfte nach den tatsächlichen RLS-Regeln auf
  `kinder` nie vollständig zugetroffen haben — außerhalb dieses Auftrags, nicht repariert.
- `bedarfsart='jobcoach-anonym'` als Marker ist eine Zweckentfremdung eines bestehenden Freitextfelds,
  keine "saubere" Lösung — falls die Jobcoach-Funktion wächst, wäre eine eigene boolesche Spalte
  (eigene Migration) der sauberere nächste Schritt.
- Alle Punkte aus Strang 57–69 bleiben unverändert offen.

## Strang 71: Teilnehmer-ID-Verwaltung — automatische ID-Generierung (12.08.2026)

**Korrektur ggü. Prompt (Punkt 3):** Der Auftrag ging davon aus, die Anonymisierung liefe über ein
Text-Präfix `jobcoach-anonym:` im Namensfeld, „wie bereits implementiert". Das trifft nicht zu — bereits
seit Strang 70 läuft die Anonymisierung über ein eigenes Datenbankfeld (`bedarfsart='jobcoach-anonym'`),
nicht über einen Text-Zusatz im Namen. Bewusst NICHT auf das Präfix-Muster umgestellt: `name` wird an
mehreren Stellen direkt anzeigt (Dropdown, Begrüßung „Hallo …", Verwaltungsliste) — ein Präfix dort
hätte die ID überall mit technischem Beiwerk verunstaltet, ohne einen Vorteil gegenüber der bereits
funktionierenden Feld-Trennung zu bringen. Die bestehende, sauberere Lösung beibehalten; im Code an der
Stelle `teilnehmerIdAnlegen()` mit einem Kommentar erklärt, damit diese Diskrepanz zum Prompt bei einer
künftigen Anfrage nicht erneut Verwirrung stiftet.

**Umgesetzt:**
- Neuer Button „🎲" neben dem Eingabefeld für neue Teilnehmer-IDs (`teilnehmerIdWuerfeln()`).
- ID-Muster exakt wie gefordert: `KT-` + 4 zufällige alphanumerische Zeichen (z. B. `KT-X8R2`). Eine
  Ergänzung ggü. der wörtlichen Vorgabe: Zeichensatz bewusst ohne leicht verwechselbare Zeichen (0/O,
  1/I/L) — passend zum vom Auftrag selbst verlangten Hinweistext, dass die ID von Hand auf eine
  physische Liste übertragen wird, soll dabei nichts kippen/verwechselt werden können.
- Kollisionsvermeidung: eine gewürfelte ID wird gegen die aktuell geladene Verwaltungsliste geprüft und
  bei einem Treffer neu gewürfelt (max. 20 Versuche).
- Hinweistext exakt wie vorgegeben ergänzt: „Notiere dir diese ID und den Namen deines Klienten in
  deiner physischen Liste. In der App werden keine Klarnamen gespeichert."
- Würfeln befüllt nur das Eingabefeld — Speichern bleibt ein bewusster zweiter Schritt (kein
  Auto-Anlegen beim Würfeln), damit die/der Coach die ID vor dem Anlegen noch sehen/prüfen kann.

**Getestet:** Syntax-Check fehlerfrei; isolierte Musterprüfung von 2000 generierten IDs (alle passend
auf `KT-` + 4 Zeichen ohne 0/O/1/I/L); jsdom-Test gegen die echte Datei mit gemocktem Supabase-Client —
Würfel-Button und Hinweistext vorhanden, generierte ID passt aufs Muster, Kollision mit einer bereits
in der (gemockten) Liste vorhandenen ID über 300 Versuche zuverlässig vermieden. div-Balance weiterhin
ausgeglichen (89/89 nach der Ergänzung).

### Noch offen

- Alle Punkte aus Strang 57–70 bleiben unverändert offen.

## Strang 72: BAROMETER_KIND.html — geführter Workflow & Status-Kacheln (12.08.2026)

Finalisierung des Jobcoach-Modus: Slider → 11 Status-Kacheln, ID-Verwaltung dezenter, Coach-Bereich
öffnet sich erst nach explizitem Klick statt automatisch, Wording konsequent zu Ende gezogen.

**Korrektur ggü. Prompt (Punkt 3):** Der Auftrag behauptete, „INGRA" solle „sobald der Jobcoach-Modus
aktiv ist" durch „Coach/Mentor:in" ersetzt werden — das war inhaltlich schon Ziel von Strang 70/71 und
größtenteils bereits umgesetzt (Titel, Hinweistexte). Hier vervollständigt um die noch verbliebenen
Stellen (Header-Untertitel „Kind" → „Teilnehmer:in", Status-Meldungen „Kind ausgewählt"/"Kind wählen",
Vergleichstext-Begriff „Coach" → „Coach/Mentor:in"). Bewusst NICHT angefasst: interne Bezeichner/
Kommentare/Variablennamen (`kind-select`, `aktuellesKindId`, `waehleKind()` usw.) sowie der externe Link
„INGRA-Barometer" unten rechts (echter, korrekter Name einer anderen, eigenständigen Seite
`BAROMETER_INGRA.html` — kein Fall von „INGRA" als Rollen-Label in dieser Seite selbst).

**Umgesetzt:**
- **Layout:** Teilnehmer-ID-Verwaltung jetzt als `<details>`/`<summary>` — im geschlossenen
  Ausgangszustand nur eine schmale, blasse Zeile („🗂️ Teilnehmer-IDs verwalten ▸"), statt der
  auffälligen gestrichelten Box aus Strang 70. Direkt darunter weiterhin die Teilnehmer-Auswahl, dann
  als klar erkennbarer Hauptbereich die neue Überschrift „Selbsteinschätzung Teilnehmer:in" über den
  Status-Kacheln.
- **11 Status-Kacheln statt Slider** (`statusKachelnRendern()`, `statusWertWaehlen()`): neutral
  (hellgrau) im Ausgangszustand, erst bei Auswahl dezent in die Bereichsfarbe eingefärbt (sanftes Grün/
  Gelb/Orange/Rot/Grau je nach Bereich) — exakt wie gefordert. Anders als der bisherige Slider ist beim
  Laden **keine** Kachel vorausgewählt (bewusste Verbesserung: eine echte Selbsteinschätzung sollte
  nicht durch einen stillen Default-Wert vorweggenommen werden — entspricht jetzt genau dem Verhalten
  der Farb-Buttons im Schul-Modus, die ebenfalls erst durch Klick aktiv werden).
- **Caption exakt wie vorgegeben:** „0 – Alles entspannt bis 10 – Maximale Belastung" als ein
  zusammenhängender Satz unter dem Kachel-Raster (vorher zwei getrennte Enden links/rechts am Slider).
- **Geführter Workflow:** Der Coach/Mentor:in-Bereich ist beim Laden unsichtbar. Erst nach Speichern
  erscheint der Button „🧭 Perspektive des Coaches ergänzen"; erst ein Klick darauf öffnet den Bereich
  (`coachEinschaetzungOeffnen()`). Zusätzliche, nicht explizit angefragte, aber naheliegende Ergänzung:
  Beim Wechsel zu einer anderen Teilnehmer-ID wird dieser Workflow zurückgesetzt (Coach-Bereich und
  Button wieder verborgen) — sonst bliebe die Einschätzung einer vorherigen Person fälschlich offen
  stehen, wenn zu einer neuen Person gewechselt wird.
- Schul-Modus unverändert: dort öffnet sich die INGRA-Einschätzung weiterhin automatisch nach dem
  Speichern (wie vor Strang 72), der neue „Perspektive ergänzen"-Button erscheint dort nie.

**Datenmapping (Punkt 4) unverändert beibehalten:** dieselbe 0–10→Farbe-Logik aus Strang 70/71
(`sliderWertZuFarbe`, `FARBE_ZU_SLIDER`) wird jetzt von den Kacheln statt vom Slider aufgerufen — keine
Änderung an der Übersetzung selbst, nur an der Bedienoberfläche, die sie auslöst.

**Getestet:** Syntax-Check fehlerfrei; div- und `<details>`-Balance ausgeglichen; jsdom-Test gegen die
echte Datei mit gemocktem Supabase-Client — Header-Untertitel, Kachel-Anzahl (11), Kachel-Überschrift,
Caption-Wortlaut, `<details>` geschlossen im Ausgangszustand, Coach-Bereich + Button beim Laden
unsichtbar, keine vorausgewählte Kachel, Kachel-Klick färbt korrekt (`rgb(250, 218, 215)` für Rot-Bereich
bestätigt), nach Speichern erscheint der Button statt dem Bereich selbst, Klick auf den Button öffnet
den Bereich und blendet den Button wieder aus, Teilnehmer-Wechsel setzt beides zurück. Zusätzlicher
Schule-Modus-Regressionstest bestätigt: Farb-Buttons, Original-Texte, Klarname+Klasse im Dropdown und
das automatische Öffnen der INGRA-Einschätzung nach dem Speichern funktionieren unverändert wie vor
diesem Strang.

### Noch offen

- Alle Punkte aus Strang 57–71 bleiben unverändert offen.

## Strang 73: Honorar-Flyer (Familienzentren/Migrationszentren) + neue Seite KLARTEXT_Antraege_Links.html (17.08.2026)

Anja plant Honorartätigkeit für Familienzentren und Migrationszentren (Kleingewerbe angemeldet) unter
dem Namen „Alltagsbegleitung für Familien" — niedrigschwellig, aufsuchend, mit drei Säulen: 1)
Struktur-Coaching vor Ort (Insel-Set · Zuhause), 2) Emotionale Stabilisierung (Barometer, Joker-Signale),
3) Ausfüllhilfe & Strukturgeberin bei Behördenpost (ausdrücklich **keine Rechtsberatung**).

**Fact-Checks/Korrekturen ggü. Prompt:**
- Kein `Anja_Jolk_Projektprofil_KLARTEXT.pdf` in den Ordnern gefunden — reales Vorlage-Dokument war
  `projektprofil.html`/`projektprofil.pdf` (EuBiA-Fokus, aus früherem Session-Abschnitt).
- Skill-Matrix-Cluster heißt „Team-Power", nicht „Team-Power-Experte" wie im Prompt behauptet.
- Das System nutzt seit Strang 72 Status-**Kacheln**, keinen Slider mehr — Formulierung entsprechend
  auf „0–10-Status-Skala" korrigiert statt „Slider".
- „11 Jahre Leitungserfahrung" und Pflegekasse-Erfahrung waren zunächst unbelegt (nicht in
  `KLARTEXT_Ueber_Anja_Jolk.html`, keine Lebenslauf-Datei in den Ordnern gefunden) — auf Rückfrage von
  Anja bestätigt/präzisiert: **11 Jahre Studienkreis-Leitung** (Abrechnung Bildung und Teilhabe,
  Elternberatung). Pflegekassen-Erfahrung laut Anja „nicht direkt, nur indirekt" (Promedica-Franchise-
  Zeit, private Pflegeerfahrung) — deshalb **nicht** als eigene Leistung auf den Flyern, sondern nur
  SGB IX/BuT als Beispiele für die Ausfüllhilfe-Säule.
- Pflegekassen-Anträge sind **nicht kommunal**, sondern kassenabhängig (AOK, TK, Barmer, …) — auf der
  neuen App-Seite entsprechend als eigener, städteunabhängiger Hinweisblock statt als Direktlink-Liste
  dargestellt (recherchiert: formloser Antrag direkt bei der eigenen Pflegekasse, 25-Werktage-Frist für
  den Bescheid).
- SGB IX/Eingliederungshilfe: Recherche bestätigt, dass trotz Träger-Wechsel zum LWL im Zuge des BTHG
  die Erstanträge für Kinder (Schulbegleitung u. Ä.) in der Praxis weiterhin bei den Sozialämtern der
  Städte bzw. beim Kreis gestellt werden (Dortmund-Seite bestätigt dies explizit) — Städte-Direktlinks
  daher wie ursprünglich geplant sinnvoll.

**Umgesetzt:**
- Zwei einseitige PDF-Flyer (`Anja_Jolk_Flyer_Familienzentren.pdf`, `Anja_Jolk_Flyer_Migrationszentren.pdf`,
  aus je einer HTML-Quelle mit weasyprint gerendert): drei Säulen, Nutzen-Box, Kontakt/Honorar-auf-
  Anfrage-Footer. Migrationszentren-Variante zusätzlich mit DAZ-Goethe-Unterricht, Trauma-Fortbildung
  und Hinweis auf sprachunabhängige, bildbasierte Tools.
- Säule 3 auf beiden Flyern umbenannt zu „Ausfüllhilfe & Strukturgeberin (keine Rechtsberatung)" mit
  drei konkreten Teilaufgaben (Sichten & Sortieren, Fristenmanagement, Vorbereitung der Unterlagen) plus
  SGB-IX-Beispiel (formloser Erstantrag zur Fristwahrung).
- Neue App-Seite `KLARTEXT_Antraege_Links.html`: Direktlinks zu echten, recherchierten offiziellen
  Antragsseiten für Bildung und Teilhabe (Dortmund, Schwerte/Kreis Unna, Unna, Hagen) und SGB IX/
  Eingliederungshilfe (Dortmund, Kreis Unna, Hagen), jeweils mit `target="_blank" rel="noopener"`.
  Eigener Pflegekasse-Infoblock (kein Direktlink-Raster, da nicht städtespezifisch) mit Link zum
  Bundesgesundheitsministerium. Deutlicher Disclaimer-Banner oben („keine Rechtsberatung", Links können
  sich ändern, Zuständigkeit im Zweifel telefonisch bestätigen). In `KLARTEXT_Downloads.html` unter
  „Teamkoordination" verlinkt.

**Getestet:** jsdom-Strukturtest für `KLARTEXT_Antraege_Links.html` (7 Direktlinks korrekt, Disclaimer
und Pflege-Sektion vorhanden, kein Parse-Fehler) und für `KLARTEXT_Downloads.html` nach Verlinkung (neuer
Link vorhanden, 82 Download-Items insgesamt, kein Parse-Fehler). Beide PDFs per Textextraktion geprüft:
je 1 Seite, kein „Pflegekasse" als fälschlich impliziter Städte-Service, „Rechtsberatung"/
„Fristenmanagement" korrekt enthalten.

### Noch offen

- Alle Punkte aus Strang 57–71 bleiben unverändert offen.
- Honorarsatz für die Flyer noch nicht festgelegt (Anja: „weiß ich selbst noch nicht genau") — Flyer
  zeigen „Honorar auf Anfrage".
- SGB-IX-Zuständigkeit beim Kreis Unna für Kinder/Schulbegleitung online nicht eindeutig als eigene
  Seite auffindbar (anders als Dortmund/Hagen) — App-Seite verlinkt bewusst nur die allgemeine
  Behinderung/Soziales-Kontaktseite des Kreises mit Hinweis, die genaue Zuständigkeit telefonisch zu
  klären.
- Direktlinks können sich ändern (kommunale Websites werden regelmäßig umstrukturiert) — kein
  automatischer Link-Check eingerichtet, sollte gelegentlich manuell geprüft werden.

## Strang 74: Ressourcen-Bericht 2.0 — vier Fachbereich-Varianten für Jobcoach-Kontext (17.08.2026)

Neue Seite `KLARTEXT_Ressourcenbericht_Jobcoach.html`: einseitiger, anonymisierter Bericht mit
umschaltbaren Fachbereich-Varianten (Struktur & Familie / Neurodivergenz / Sprache & Integration /
Admin-Support), gebaut nach Anjas Vorgabe, ergänzt um ein konkretes Textbeispiel (Struktur-&-Familie-
Variante), das Anja vorab bestätigt hat.

**Fact-Checks/Korrekturen ggü. Prompt:**
- Der Prompt nannte als Beispiel für Skill-Matrix-Superkräfte „Energie-Bündel" — das ist **kein**
  echter Cluster. Die sechs echten Cluster (`KLARTEXT_Spiel_SkillMatrix.html`) sind Team-Power,
  Fokus-Champion, Kreativ-Genie, Verantwortungs-Anker, Problem-Löser, Mutig & Stressfest — diese sechs
  wurden als Auswahl-Chips verwendet.
- Die „Brainy-Karten" für individuelle Notfall-Strategien sind ein reales, sechsteiliges Konzept
  (`Brainy_Signalkarten_Konzept.md`: Toilette, Trinkpause, Bewegung am Platz, Zu meiner Insel, Frische
  Luft, Kurz für mich) — als Auswahl-Chips übernommen statt frei erfunden.
- **Wichtige Architektur-Einschränkung, die im Prompt nicht bedacht war:** Nur der Barometer-Verlauf
  ist zentral in Supabase gespeichert und über die KT-ID geräteübergreifend abrufbar (Tabelle
  `barometer_kind`, Spalten `farbe`/`notiz`/`created_at`, exakter 0–10-Wert aus dem `[Status X/10]`-
  Präfix im `notiz`-Feld geparst — Muster aus Strang 70/72 übernommen). Reizfilter-Verlauf und
  Skill-Matrix-Profil liegen dagegen nur lokal auf dem Gerät des jeweiligen Teilnehmenden
  (`localStorage`, nicht Supabase-synchronisiert) und sind vom Coach-Gerät aus **nicht** abrufbar. Die
  Seite täuscht das nicht vor: Barometer-Verlauf wird automatisch geladen, alle anderen Kerninhalte
  (Reizfilter-Zusammenfassung, Superkräfte-Auswahl, Sprachstand, Admin-Status usw.) sind bewusst
  manuelle Eingabefelder des Coaches, gespeichert je Teilnehmer-ID + Variante in `localStorage`
  (Schlüssel-Präfix `klartext_ressourcenbericht_`).

**Umgesetzt:**
- Kopfbereich: Teilnehmer-ID-Auswahl (identische Supabase-Abfrage wie in `BAROMETER_KIND.html`:
  `Kinder`-Tabelle, `aktiv=true`, `bedarfsart='jobcoach-anonym'`), Berichtszeitraum (7/14/30 Tage),
  Datum automatisch, Motto „Klar. Warm. Menschlich." im Hero.
- Barometer-Verlauf-Karte: automatische Zusammenfassung (Ø-Wert, Anzahl Einträge, farbige Tages-Chips)
  aus der echten `barometer_kind`-Historie der gewählten Teilnehmer-ID im gewählten Zeitraum.
- Vier Fachbereich-Tabs, je mit eigenen, an Anjas Vorgabe angelehnten Kerninhalte-Feldern:
  - **Struktur & Familie:** Checkliste der acht echten Insel-Set-Zuhause-Zonen (Ruhe-/Emotions-/
    Arbeits-/Bewegungs-/Familien-Regel-/Eltern-Kind-Gesprächs-/Übergangs-/Geschwister-Konflikt-Insel)
    mit optionaler Notiz je Zone, Freitext für Regulations-Tools, Freitext für wertfreie Rückmeldung.
  - **Neurodivergenz:** Freitext Reizfilter-Zusammenfassung, Superkräfte-Auswahl (6 echte Cluster),
    Brainy-Karten-Auswahl (6 echte Karten) + Notiz.
  - **Sprache & Integration:** Sprachniveau-Auswahl (GER A1–C2), Freitext kulturelle Kompetenzen,
    Freitext Übersetzung informeller Kompetenzen, Freitext Teilhabe-Fortschritte.
  - **Admin-Support:** Status-Tabelle (BuT/SGB IX/Pflegekasse, je 6-stufiger Status), Freitext
    Sortier-Status Unterlagen, Freitext nächste Termine — mit Verweis auf `KLARTEXT_Antraege_Links.html`
    und explizitem „keine Rechtsberatung"-Hinweis (konsistent mit Strang 73).
  - Jede Variante endet mit einem eigenen Ausblick-Feld („nächste kleine Schritte").
- Speichern-Button (localStorage je Teilnehmer-ID+Variante+Feld) und Drucken/PDF-Button
  (`window.print()`, gleiches Druck-Layout-Muster wie `KLARTEXT_Ressourcenbericht.html`).
- Privacy-by-Design-Hinweis fest im Footer-Bereich: ausschließlich KT-ID, nirgends ein Klarname.
- In `KLARTEXT_Downloads.html` unter „Teamkoordination" verlinkt.

**Getestet:** jsdom mit gemocktem Supabase-Client (Muster aus Strang 70–72 übernommen) — Teilnehmer-ID-
Dropdown korrekt befüllt (2 Testeinträge), alle vier Auswahl-Grids in korrekter Anzahl (8 Zonen/6
Superkräfte/6 Brainy-Karten/3 Admin-Themen), Barometer-Ø-Berechnung aus drei Test-Einträgen exakt
korrekt (4/6/2 → Ø 4.0), Tages-Chip-Anzahl korrekt. Separater Test für Speichern/Laden: Freitext-Felder,
Zonen-Checkbox und Zonen-Notiz überleben Varianten-Wechsel und erneutes Laden aus `localStorage`
korrekt. `KLARTEXT_Downloads.html` nach Verlinkung erneut geprüft (neuer Link vorhanden, 83
Download-Items insgesamt, kein Parse-Fehler).

### Noch offen

- Alle Punkte aus Strang 57–73 bleiben unverändert offen.
- Reizfilter-Verlauf und Skill-Matrix-Profil sind aktuell nicht Supabase-synchronisiert — falls Anja
  will, dass auch diese Werte künftig automatisch im Bericht erscheinen, müsste zuerst eine
  geräteübergreifende Speicherung dieser beiden Datenquellen gebaut werden (bisher nicht beauftragt).
- Kein automatischer PDF-Export ohne Browser-Druckdialog (wie beim bestehenden `KLARTEXT_Ressourcenbericht.html`
  auch) — Export läuft über „Drucken → Als PDF speichern".
- Noch keine echte End-to-End-Prüfung mit realer Supabase-Instanz durchgeführt (nur Mock-Test).

## Strang 75: Ressourcen-Bericht — Supabase komplett entfernt, reine Offline-Nutzung (17.08.2026)

Anjas Korrektur: Sie nutzt die App vorerst nur selbst, direkt beim Klienten vor Ort — kein Login, keine
Cloud, keine Geräteübergreifung nötig. Berichte sollen alles Ausgefüllte zusammenfassen, damit sie per
E-Mail an den Klienten/die Einrichtung geschickt werden können.

**Abgrenzung geklärt (Rückfrage vor dem Umbau):** Nur `KLARTEXT_Ressourcenbericht_Jobcoach.html` wird
umgebaut. `BAROMETER_KIND.html` (Strang 70–72) bleibt unverändert auf Supabase, da dort weiterhin ein
geräteübergreifender Verlauf gewünscht ist.

**Umgesetzt (kompletter Umbau der Datenschicht, Oberfläche/Varianten inhaltlich unverändert):**
- `<script type="module"> import { supabase } ...` entfernt — keine Supabase-Referenz mehr in der Datei
  (verifiziert: `grep -c supabase` → 0 Treffer).
- Login-Gate entfernt: Der bisherige `sessionStorage.klartext_login`-Check hätte über
  `KLARTEXT_Login.html` indirekt wieder Supabase vorausgesetzt (dort läuft der eigentliche Login via
  `supabase.auth.signInWithPassword`) — daher komplett gestrichen, die Seite ist jetzt ohne Anmeldung
  direkt nutzbar.
- Teilnehmer-ID-Verwaltung neu als rein lokale Liste: eigene `<details>`-Box zum Anlegen/Würfeln/
  Entfernen von KT-IDs, gespeichert unter `klartext_rb_teilnehmer_liste` (localStorage, JSON-Array).
  ID-Generierung identisch zum bewährten Muster aus `BAROMETER_KIND.html` (`KT-` + 4 Zeichen aus dem
  verwechslungsarmen Zeichensatz, Kollisionsprüfung gegen die aktuelle Liste).
- Barometer-Verlauf kommt nicht mehr aus Supabase, sondern aus einem neuen lokalen Log: 11
  Status-Kacheln (0–10, gleiche Bereichsfarben-Logik wie `BAROMETER_KIND.html`) direkt auf der Seite —
  Klick + „Eintrag hinzufügen" schreibt `{wert, datum}` in `klartext_rb_barometer_<KT-ID>`
  (localStorage). Die Verlaufs-Zusammenfassung (Ø-Wert, Tages-Chips) wird aus diesem lokalen Log
  berechnet statt aus einer Datenbank-Abfrage — fachlich identische Logik, andere Datenquelle.
- Neuer Abschnitt „Bericht zusammenfassen & versenden": eine Funktion sammelt für die aktuell gewählte
  KT-ID alle vier Fachbereich-Varianten ein (nicht nur die gerade offene) und baut daraus einen
  Klartext-Bericht — Kopfzeile, Barometer-Zusammenfassung, dann nur die Bereiche, in denen tatsächlich
  etwas ausgefüllt wurde. Drei Aktionen: Text im Vorschaufeld anzeigen, „📋 Text kopieren"
  (Zwischenablage), „✉️ E-Mail vorbereiten" (öffnet `mailto:` mit Betreff und Text vorausgefüllt, mit
  Warnhinweis bei sehr langen Berichten wegen mailto-Längenbegrenzung in manchen E-Mail-Programmen).
  Drucken/PDF-Button bleibt zusätzlich bestehen (für ein optisch schöneres Anhängsel).
- Hinweis-Badge im Hero „🔒 Läuft komplett lokal auf diesem Gerät — kein Login, keine Cloud" ergänzt.

**Bewusste Einschränkung, offen kommuniziert:** Weil alles jetzt lokal in `localStorage` liegt, sind
Teilnehmer-IDs, Barometer-Log und Berichts-Inhalte **an das jeweils genutzte Gerät gebunden** — bei
Gerätewechsel oder Browser-Daten-Löschung gehen sie verloren, und es gibt keine Synchronisation mit
`BAROMETER_KIND.html` (dort angelegte KT-IDs erscheinen hier nicht automatisch, und umgekehrt). Das
passt zu Anjas aktuellem Nutzungsmuster (ein Gerät, direkt beim Klienten), sollte aber vor produktivem
Dauereinsatz mit ihr abgeglichen werden, falls sich das ändert.

**Getestet:** jsdom ohne jeden Mock (kein Supabase mehr nötig) — 8/6/6/3/11-Elemente-Zähler weiterhin
korrekt, Teilnehmer-ID anlegen funktioniert, drei Status-Kacheln-Einträge ergeben korrekt Ø 4.0,
Struktur-Variante speichern/laden funktioniert, `berichtErzeugen()` liefert einen korrekten Text mit
KT-ID, Barometer-Ø und nur den tatsächlich ausgefüllten Bereichen (leere Bereiche fehlen wie
vorgesehen, keine leeren Überschriften im Bericht).

### Noch offen

- Alle Punkte aus Strang 57–74 bleiben unverändert offen (der Supabase-Rückbau betrifft nur diese eine
  Datei, `BAROMETER_KIND.html` bleibt wie in Strang 70–72 beschrieben).
- Keine Synchronisation zwischen den lokalen Teilnehmer-IDs dieser Seite und den Supabase-Teilnehmer-IDs
  aus `BAROMETER_KIND.html` — falls beide Systeme später zusammengeführt werden sollen, wäre das ein
  eigenständiges, größeres Vorhaben.
- `mailto:`-Link kann bei sehr langen Berichten (viele ausgefüllte Bereiche) in manchen E-Mail-Programmen
  abgeschnitten werden — der Hinweistext macht darauf aufmerksam, „Text kopieren" ist der robustere Weg.

## Strang 76: Honorar-Dokument „Leistungsübersicht für Pflegedienste" (17.08.2026)

Anja hat einen von Copilot vorformulierten Text „A4 – Leistungsübersicht für Pflegedienste" eingereicht
(Zielgruppe: ambulante Pflegedienste als Kooperationspartner, nicht Familien direkt) und um Einschätzung
gebeten.

**Fact-Check vor der Übernahme:**
- Preise (40 €/45 €/55 € pro Stunde, 5-Std.-Paket 185 €, 10-Std.-Paket 360 €, Fahrtkosten 0,40 €/km ab
  10 km) stimmen mit den von Anja selbst recherchierten und bereits bestätigten Sätzen überein —
  unverändert übernommen.
- „MDK-Termine" ist veraltet: Der Medizinische Dienst der Krankenversicherung (MDK) wurde zum 1. Januar
  2020 durch das MDK-Reformgesetz in „Medizinischer Dienst (MD)" umbenannt (Quellen:
  medizinischer-dienst.de, pflege.de). Korrigiert zu „Begutachtungstermine des Medizinischen Dienstes
  (MD)".
- „Belastungs-Barometer" → echtes Tool heißt „Barometer" (Status-Check 0–10, ohne den Zusatz
  „Belastungs-"). „Insel-Modell" → echtes Tool heißt „Insel-Set" (Insel-Set · Zuhause). Beide korrigiert.
- Es fehlte ein Hinweis „keine Rechtsberatung" (im Unterschied zu den Familienzentren-/
  Migrationszentren-Flyern aus Strang 73 und `KLARTEXT_Antraege_Links.html` aus Strang 73, die diese
  Abgrenzung bereits konsequent führen). Ergänzt als eigener Hinweis-Kasten direkt unter dem Profiltext.
- Motto „Klar. Warm. Menschlich." fehlte, obwohl es auf allen anderen Anja-Dokumenten dieser Session
  steht — ergänzt.

**Rückfrage zur Pflegekassen-Prominenz:** Anjas Erfahrung mit Pflegekassen-Anträgen ist laut ihrer
eigenen Aussage in Strang 73 „nicht direkt, nur indirekt, aus privater Pflegeerfahrung". Im
Copilot-Text stand die Pflegekassen-Antragshilfe ganz oben als erster Aufzählungspunkt unter
„Administrativer Support". Rückfrage gestellt und mit „etwas zurückhaltender formulieren" beantwortet.
Umgesetzt durch zwei Maßnahmen: (1) der Punkt wurde ans Ende der Aufzählung verschoben (jetzt nach
BuT- und SGB-IX-Ausfüllhilfe), (2) ergänzt um den Zusatz „— in Abstimmung mit Ihrem Pflegedienst", der
klarstellt, dass Anja hier unterstützend und nicht als eigenständige Fachstelle auftritt.

**Gebaut:** `Anja_Jolk_Leistungsuebersicht_Pflegedienste.docx` (docx-js, KLARTEXT-Marken-Farben Navy
`#1A2E44`/Grün `#6EC6A0`, gleiche Gestaltungssprache wie die Honorar-Flyer aus Strang 73) und daraus
`Anja_Jolk_Leistungsuebersicht_Pflegedienste.pdf` (LibreOffice-Konvertierung). Aufbau: Kopfzeile mit
Motto, Profiltext, Hinweis-Kasten „keine Rechtsberatung", drei nummerierte Leistungsblöcke
(Administrativer Support/Alltagsbegleitung/Familienentlastung) mit Preisen, Fahrtkosten, dunkler
Nutzen-Kasten, Kontaktzeile.

**Getestet:** `pypdf`-Textextraktion bestätigt 1 Seite; enthält „keine Rechtsberatung",
„Medizinischen Dienstes (MD)", „Insel-Set", „Barometer", „Klar. Warm. Menschlich.", alle drei
Stundensätze und „0,40 € / km"; enthält kein „MDK" mehr. Layout visuell per Screenshot geprüft
(kein Umbruch, keine abgeschnittenen Boxen).

### Noch offen

- Telefonnummer im Kontaktblock ist als Platzhalter `[einfügen]` stehen geblieben — Anja muss sie noch
  ergänzen, bevor das Dokument verschickt wird.
- Wie bei den Strang-73-Flyern kein automatischer Soll-Ist-Abgleich, falls sich Preise oder Tool-Namen
  künftig ändern — Dokument müsste dann manuell erneut geprüft werden.

## Strang 77: Drei B2B-Landingpages für Kooperationspartner in klartext-shop (17.08.2026)

Anja wollte laut Übergabe-Prompt "eine Landing-Page überarbeiten" — auf Rückfrage stellte sich heraus,
dass sie eigentlich unsicher war, ob die App-Struktur ("alles in einer App") sinnvoll ist und wie sich
daraus eine Landing-Page für die neuen Familienzentren-/Migrationszentren-/Pflegedienste-Angebote bauen
lässt. Kein Umbau nötig — Architektur-Einschätzung + neue Verkaufsseiten im bestehenden Shop-Repo.

**Architektur-Einschätzung (mit Anja abgestimmt):** `klartext-app` (437 HTML-Dateien) ist zu Recht eine
zusammenhängende Mentoring-App für INGRA/Lehrkraft/Eltern/Teamkoordination — kein Aufräumfall.
`klartext-shop` ist bereits sauber für Marketing/Verkauf getrennt (Muster: eine Übersichtsseite +
eine `*_Verkaufsseite.html` pro Produkt). Zwei Nebenbefunde notiert, nicht akut: (1) Namenskollision
"TK" — in klartext-app Teamkoordination-Modul, in klartext-shop ein Kartendeck-Produktkürzel; (2)
`KLARTEXT_Traeger_Angebot.html` (Träger von Schulbegleitung) sitzt hinter Login, was für eine
Akquise-Seite unpassend ist — betrifft aber eine andere Zielgruppe, nicht Teil dieses Strangs.

**Entscheidung Seitenstruktur (mit Anja abgestimmt):** Drei getrennte Landingpages statt einer
gemeinsamen Seite, analog zum bestehenden Shop-Muster — damit Anja z. B. einem Familienzentrum gezielt
nur den passenden Link schicken kann, ohne Pflegedienst-Preise mitzuliefern.

**Preismodell-Klärung (wichtiger Fakten-Konflikt, mit Anja aufgelöst):** Anja lieferte eine zweite
Preisliste (aus einer NotebookLM-Recherche) mit zwei Tarif-Ebenen — niedrigschwellige Direktvermittlung
(40–55 €) vs. institutionelle Fachberatung (75–110 €/h) für Träger mit eigenem Budget. Das stand im
Widerspruch zur bereits committeten Pflegedienste-Übersicht aus Strang 76 (40/45/55 €/h). Klärung: Die
Pflegedienste-Übersicht ist bereits korrekt, weil dort laut eigenem Text die Familie/Senior:in privat
zahlt, nicht der Pflegedienst — das ist der Direktvermittlungs-Tarif, keine Korrektur nötig. Für alle
drei neuen Seiten hat sich Anja für ausschließlich die niedrigschwellige Direktvermittlung entschieden
(kein institutioneller Fachberatungs-Tarif, keine Workshop-Pauschalen — "ich muss mich erst einarbeiten
mit niedrigen Schwellen").

**Fact-Check DaZ (Migrationszentren):** Anja bestätigte, dass sie DaZ zwar unterrichten darf, aber
keine BAMF-Zulassung hat — DaZ läuft also im Sinne von privater "Nachhilfe", nicht als anerkannter
Integrationskurs. Auf der neuen Seite entsprechend explizit als "kein BAMF-anerkannter Integrationskurs"
gekennzeichnet und in den niedrigschwelligen Gesamtpreis (50 €/Termin) integriert statt als eigene
Institutionen-Pauschale. Der bestehende PDF-Flyer aus Strang 73 nennt "Deutschunterricht nach
DAZ-Goethe-Standard" bereits ohne BAMF-Bezug — laut Anja unkritisch, keine Korrektur am Flyer nötig.

**Marktrecherche zur Preis-Plausibilisierung (WebSearch):** Freiberufliche systemische Beratung liegt
je nach Region/Zielgruppe bei 60–220 €/h (Beispiel Familienberatung 130 €/60 Min., Quellen:
institut-bildung-coaching.de, systemische-beratung-mfr.de); Fachleistungsstunden in der ambulanten
Erziehungshilfe NRW werden kommunal verhandelt, keine landesweite Festlegung (lwl-landesjugendamt.de).
Damit sind sowohl die niedrigschwelligen 40–55 €/h als auch die (aktuell nicht genutzten) 75–110 €/h
markt-plausibel — die 40–55 €/h sind bewusst niedrigschwellig unter dem Marktdurchschnitt angesetzt.

**Gebaut (klartext-shop):**
- `Familienzentren_Verkaufsseite.html` — 3 Säulen (Struktur-Coaching vor Ort, Emotionale
  Stabilisierung, Ausfüllhilfe & Strukturgeberin), Preise 55 €/Termin (4/8 Termine 210 €/400 €) und
  40 €/h (5/10 h 185 €/360 €).
- `Migrationszentren_Verkaufsseite.html` — 3 Säulen inkl. sprach- und traumasensibler Begleitung,
  DaZ-Nachhilfe explizit als "kein BAMF-Integrationskurs" gekennzeichnet, ein Gesamtpreis 50 €/Termin
  inkl. DaZ (5/10 Termine 235 €/450 €).
- `Pflegedienste_Verkaufsseite.html` — HTML-Fassung der Strang-76-Leistungsübersicht, gleiche drei
  Preiskategorien (40/45/55 €/h) und Fahrtkosten.
- Alle drei im bestehenden Shop-Design (Playfair Display/DM Sans, Navy `#1B3A4B`/Grün `#6EC6A0`),
  ohne Login/Supabase, mit § 19 UStG-Hinweis (Kleinunternehmerregelung) und durchgängigem
  "keine Rechtsberatung"-Disclaimer.
- Die drei zugehörigen PDFs (zwei Flyer aus Strang 73, Pflegedienste-Übersicht aus Strang 76) wurden
  zusätzlich von `klartext-app` nach `klartext-shop` kopiert, damit die Download-Links auf den neuen
  Seiten funktionieren (Cloudflare Pages von klartext-shop kann nicht auf Dateien im
  klartext-app-Repo zugreifen, die beiden Deployments sind bewusst getrennt).
- `KLARTEXT_Shop_Uebersicht.html`: neue Sektion "Für Institutionen & Kooperationspartner"
  (`#kooperation`) mit drei Karten im bestehenden `deck-grid`-Stil, verlinkt auf die drei neuen Seiten,
  plus Nav-Link "Für Institutionen".

**Getestet:** `tidy` (keine HTML-Fehler in allen vier geänderten/neuen Dateien), jsdom-Smoketest
(Struktur-Zähler je Seite: 1 `<h1>`, korrekte Anzahl Preis-Karten je Preismodell — 2/1/3 —, je 4
FAQ-Einträge), BeautifulSoup-Linkcheck (alle internen `href`/`src` — Impressum, Datenschutz, `anja.jpg`,
die drei PDFs, `KLARTEXT_Shop_Uebersicht.html` — lösen auf existierende Dateien auf, keine toten Links).

### Noch offen

- **Git-Commit in `klartext-shop` konnte nicht abgeschlossen werden:** Alle sieben Dateien sind
  `git add`-gestaged (verifiziert per `git status`), aber `git commit` ist an einer verwaisten
  `.git/index.lock`-Datei hängen geblieben, die sich über das Sandbox-Dateisystem nicht löschen lässt
  (Berechtigungsfehler beim Mount, reproduziert auch mit einer frisch angelegten Testdatei — kein
  git-spezifisches Problem, sondern eine Mount-Einschränkung dieser Session). **Anja muss einmal
  manuell** `klartext-shop/.git/index.lock` löschen (Terminal: `rm klartext-shop/.git/index.lock`,
  oder einfach im Finder löschen), danach kann der Commit nachgeholt werden. Eine harmlose Testdatei
  `klartext-shop/_test_remove_me.txt` (leer) ist aus dem gleichen Grund ebenfalls stehen geblieben und
  kann mitgelöscht werden.
- Telefonnummer fehlt weiterhin im Kontaktblock der Pflegedienste-Materialien (siehe Strang 76) — auch
  auf der neuen `Pflegedienste_Verkaufsseite.html` nicht ergänzt, da bisher nur E-Mail als Kontaktweg
  über die bestehenden Seiten läuft.
- Auf `KLARTEXT_Shop_Uebersicht.html` verlinkt jetzt auch die neue Sektion — nicht geprüft: ob Anja die
  drei neuen Seiten zusätzlich von `index.html` (Landing-Einstieg) aus verlinkt haben möchte.
- Institutioneller Fachberatungs-Tarif (75–110 €/h) und Workshop-Pauschalen aus der NotebookLM-Recherche
  sind bewusst nicht auf den Seiten – falls Anja sich später eingearbeitet hat und höhere Sätze für
  Träger mit eigenem Budget anbieten möchte, wäre das eine spätere Ergänzung der drei Seiten.

## Strang 79: Zusatzqualifikationen aus `10_Weiterbildung` auf die drei Seiten (17.08.2026)

Anja hat den privaten Ordner `/Users/anjajolk/Beruf/Bewerbungen/10_Weiterbildung` freigegeben, um zu
prüfen, welche ihrer vielen Fortbildungen sich zusätzlich für die drei B2B-Seiten eignen.

**Vorgehen (wichtig für Verlässlichkeit):** Der Ordner enthält weit überwiegend reines Lern-/
Referenzmaterial (E-Books, Worksheets, Artikel-PDFs von Blogs), das keinen Abschluss belegt. Nur
Funde mit Name+Institution+Datum im PDF-Inhalt (nicht nur Dateiname) wurden als "echtes Zertifikat"
gewertet und vorgeschlagen — alles andere ausdrücklich als "kein belastbarer Nachweis" verworfen, damit
keine unbelegte Qualifikation auf einer öffentlichen Verkaufsseite landet.

**Rückfrage zur Positionierung (mit Anja abgestimmt):** Die Familienzentren-Seite grenzt sich bisher
rein ab ("kein Ersatz für ... Frühe Hilfen"). Anja ist aber selbst beim Nationalen Zentrum Frühe Hilfen
(BZgA) fortgebildet (6 Module, 26./27.10.2022, Köln). Entscheidung: aktiv erwähnen — die Abgrenzung
bleibt bestehen, zusätzlich aber als eigene Kompetenz sichtbar gemacht ("kenne die Ansätze der Frühen
Hilfen und ergänze sie praxisnah"). Umfang: bewusst knapp, 2–3 stärkste Zusatz-Qualifikationen je Seite
statt aller gefundenen Treffer.

**Gebaut:**
- `Familienzentren_Verkaufsseite.html`: Hero-Sub und ein Check-Item um die Frühe-Hilfen-Fortbildung
  ergänzt (Positionierung von reiner Abgrenzung zu "kennt die Ansätze, ergänzt praxisnah"). Drei neue
  Badges: Frühe Hilfen (Nationales Zentrum Frühe Hilfen, BZgA, 2022), Gesundheitsmanager*in
  Kindertagesbetreuung (Stiftung Kindergesundheit, 24 LE + Prüfung, 25.04.2025), Kindeswohlgefährdung
  & Schutzkonzept (Kita-Campus, 2019).
- `Migrationszentren_Verkaufsseite.html`: Zwei neue Badges neben der bestehenden Trauma-Qualifikation:
  Geflüchtete Kinder & Jugendliche (AUGEO Academy, NL, 10.10.2019), Flucht & Trauma (Johanniter,
  25.04.2025).
- `Pflegedienste_Verkaufsseite.html`: Referentin-Absatz und zwei neue Badges ergänzt: § 45 SGB
  XI-Pflegekurse (Demenz, Schlaganfallvorsorge, Sicherheit im Pflegealltag — mehrere Anbieter:
  Gesundheit von Morgen GmbH, curendo, Pflege-Betreuer, 2024–2026) sowie Pflegebedürftige Kinder:
  ADHS & ASS (Pflege-Betreuer, 26.02.2026).

**Nicht übernommen, geprüft und bewusst verworfen:**
- GFK/Knotenlösen GmbH (10.08.2019) — echt, aber expliziter "Gratis"-Einsteigerkurs, nicht als
  Qualifikation beworben.
- DICS/DICIS-Institut ISO-9001-Zertifikat (21.12.2025) — echt, aber kein inhaltlicher Bezug zu den drei
  Zielgruppen.
- IndiPaed-Module und Nifbe "Individuelle Begabungsförderung" — echte, aber sehr kurze (1–2h)
  Kinderschutz-/Begabungs-Module; nicht mit aufgenommen, um die Badge-Listen nicht zu überladen
  (Vorgabe: 2–3 stärkste je Seite). Bei Bedarf nachrüstbar.
- Uni-Ulm-Shelter-Material, sowie IU-Akademie/OPEN_HPI/openSAP-Kurse (außer dem einen DaZ-Kurs)/
  ONCAMPUS/LECTURIO/fobizz/Siemens/iMOOX/BNE_hoch3/Städel/utb/UDEMY/badges — größtenteils reines
  Kursmaterial ohne zugehöriges Zertifikat oder thematisch ohne Bezug zu den drei Zielgruppen.

**Wichtige Korrektur (nicht Live-relevant, nur für künftige Genauigkeit):** IFLW-Abschluss "Integrative
Lerntherapie" war laut Studiennachweis bereits am 20.07.2013, nicht wie zuvor angenommen 2021 — die
2021er-Rechnung im Ordner war nur ein separater Buchkauf (Praxisbuch, 29 €), keine neue Ausbildung.
Betrifft keine der Live-Seiten (dort steht nur "Integrative Lerntherapie (IFLW)" ohne Jahreszahl).

**Getestet:** `tidy` (keine HTML-Fehler auf allen drei Seiten nach der Änderung), jsdom-Smoketest
(Badge-Anzahl: Familienzentren 9, Migrationszentren 8, Pflegedienste 6).

### Noch offen

- Git-Commit für Strang 77, 78 **und** 79 steht weiterhin aus (gleiches Lock-Problem wie in Strang 77
  beschrieben) — Anja committet aktuell direkt selbst über die von Claude bereitgestellten
  Terminal-Befehle.
- IndiPaed-, Nifbe- und weitere kurze Kinderschutz-Module wurden bewusst nicht aufgenommen (siehe oben)
  — falls Anja die Badge-Listen doch umfangreicher haben möchte, sind die Fakten bereits recherchiert
  und einsatzbereit.

## Strang 80: Wichtige Korrektur "Systemische Beraterin (IHK)" + zwei weitere Zeugnis-Funde (17.08.2026)

Anja hat zusätzlich die Ordner `/Users/anjajolk/Beruf/Bewerbungen/05_Abschlüsse/Zeugnisse` und
`/Users/anjajolk/Beruf/Bewerbungen` freigegeben, um die auf allen drei B2B-Seiten (und im
Original-Flyer aus Strang 73) verwendete Kernqualifikation "Systemische Beraterin (IHK)" gegen echte
Zeugnisse zu prüfen.

**Kritischer Fund:** Im Zeugnisse-Ordner existiert **kein** Beleg für "Systemische Beraterin (IHK)".
Die einzige dort vorhandene IHK-Urkunde ist das Prüfungszeugnis Bürokauffrau von 1992 (unter Anjas
Mädchennamen "Anja Kersten", IHK Dortmund) — vier Kopien geprüft (OCR, da Scans ohne Text-Layer),
alle identisch. Auch Anjas eigene Bewerbungsübersicht (`Bewerbungen/.../BBA/BBA_Trainer Kopie.pdf`)
listet unter "Ausbildung & Zertifikate" nur "IHK - Abschluss Bürokauffrau (1992)", keine systemische
Beratungs-Qualifikation von der IHK. Rückfrage gestellt statt stillschweigend zu korrigieren oder zu
übernehmen.

**Auflösung:** Anja hat das Zertifikat nachgereicht, es lag im Ordner `Bewerbungen` (nicht
`Bewerbungen/05_Abschlüsse/Zeugnisse`): `IHK_Systemische Beratung-Coaching Kopie.pdf`. Per OCR
geprüft — das Zertifikat existiert wirklich, war aber unvollständig zitiert. Korrekter, vollständiger
Titel lt. Original: **"Systemische Beraterin und Coachin (IHK)"** (nicht nur "Systemische
Beraterin (IHK)"). Ausgestellt von der IHK-Projektgesellschaft mbH, Frankfurt (Oder),
Zertifikats-Nr. 01652/0108A, Onlinelehrgang 14.04.–22.05.2026, 163 Unterrichtsstunden (Systemische
Grundhaltung, Genogramm, Systembrett, Skulpturarbeit, kollegiale Fallberatung u. a.). Damit ist das
Zertifikat noch sehr jung (Mai 2026) und thematisch sauber belegt.

**Korrektur umgesetzt:** "Systemische Beraterin (IHK)" auf allen drei Seiten (Titel-Zeile unter dem
Namen + Badge, je 2 Stellen) zu "Systemische Beraterin und Coachin (IHK)" ergänzt (`replace_all`,
verifiziert: 0 Treffer alter Text, je 2 Treffer neuer Text pro Datei).

**Zwei weitere echte, starke Funde aus dem Zeugnisse-Ordner ergänzt:**
- `FAPS.pdf/Integrationspädagogik.pdf` + `FAPS.pdf/Sprachentwicklung.pdf` (beide OCR-geprüft, echte
  benotete Zeugnisse der Fernakademie für Pädagogik und Sozialberufe, Juni–August 2019): "Fachkraft für
  Integrationspädagogik" (Note sehr gut) und "Sprachentwicklungsexpertin" (Note gut) — auf
  Familienzentren- **und** Migrationszentren-Seite als Badges ergänzt.
- Goethe-Zertifikat präzisiert: OCR bestätigt exakten Titel "DaZ in der Grundschule" (Gesamtnote sehr
  gut/1,00, 14.10.2019) statt der bisherigen generischen Badge-Bezeichnung "DAZ Goethe-Institut" — Badge
  auf Migrationszentren-Seite zu "DaZ in der Grundschule (Goethe-Institut)" präzisiert.
- Body'n'Brain-Trainerin®-Zertifikat (2021–2022, aus Anjas eigener Bewerbungsübersicht bestätigt) als
  Badge auf der Pflegedienste-Seite ergänzt — der Begriff "Body'n'Brain-Methoden" wurde dort bereits in
  Strang 76 verwendet, jetzt mit echtem Zertifikatsnachweis unterlegt statt nur als Technik-Name.

**Getestet:** `tidy` (keine HTML-Fehler auf allen drei Seiten nach der Korrektur), gezielte
`grep -c`-Prüfung, dass der alte unvollständige Titel überall ersetzt wurde (0 Treffer) und der neue
vollständige Titel korrekt zweimal je Datei steht (Titel-Zeile + Badge).

### Noch offen

- Git-Commit für Strang 77–80 steht weiterhin aus (Anja committet selbst über die bereitgestellten
  Terminal-Befehle; der Korrektur-Commit für Strang 80 muss noch ergänzt werden, siehe unten).
- Weitere Funde aus dem Bewerbungen-Ordner nicht erschöpfend geprüft (nur gezielt nach "Systemische
  Beratung" gesucht) — falls Anja möchte, könnte dort noch weiter nach zusätzlichen Qualifikationen
  gesucht werden.
- PromedicaPlus-Tätigkeitsprofil ("Selbstständige Beratung & Koordination") und Arbeitszeugnisse
  VeBu/AWL (Lebenshilfe) aus Anjas eigener Bewerbungsübersicht bisher nicht in die Seiten eingearbeitet
  — das ist echte Berufserfahrung (kein Kurszertifikat), könnte aber die Pflegedienste-Seite inhaltlich
  stärken, falls gewünscht.

## Strang 81: VHS/Erwachsenenbildung als mögliche vierte Zielgruppe — zurückgestellt (17.08.2026)

Anja fragte, ob die IU-Zertifikate zur Erwachsenenbildung berücksichtigt wurden und ob sich daraus ein
Angebot für Volkshochschulen (VHS) ergeben könnte.

**Fakten geprüft (echte Zeugnisse, `Zeugnisse/IU/`):** Anja hat einen kompletten Einzelmodullehrgang aus
dem IU-Bachelor "Erwachsenenbildung, Beratung und Personalentwicklung" abgeschlossen (ZFU-Zulassungsnummer
1100419c, also offiziell anerkannter Fernunterricht), 06.06.–02.10.2025, IU Akademie/Erfurt,
Prüfungsausschuss-Vorsitz Prof. Dr. Tobias Brückmann. Vier Einzelmodule mit je eigenem Zeugnis:
"Lernen von Erwachsenen", "Veranstaltungsplanung und -durchführung von Lehr-Lern-Prozessen", "Planung
von Bildungsprozessen bei Erwachsenen", "Grundlagen von Beratung". Damit hat Anja ein fachlich
passendes Profil für eine VHS-Kursleiterinnen-Tätigkeit (Andragogik/Erwachsenenbildungsmethodik direkt
belegt).

**Entscheidung (mit Anja abgestimmt):** Zurückgestellt, nicht bauen. Passt zu Anjas bereits in Strang
77 getroffener Entscheidung, sich bei den B2B-Angeboten erst einzuarbeiten und niedrigschwellig zu
bleiben (keine Workshops/institutionellen Formate vorerst). VHS wäre zudem ein anderes Geschäftsmodell
als die drei bestehenden Seiten (Vergütung pro Unterrichtseinheit durch die VHS für öffentliche
Gruppenkurse statt 1:1-Honorartätigkeit mit Familien) — bewusst als eigenständige, spätere Option
behandelt statt in die bestehenden drei Seiten gepresst.

### Noch offen

- Vierte Landingpage für VHS/Erwachsenenbildungseinrichtungen ist geprüft und vorbereitet (Fakten oben
  vollständig), aber nicht gebaut — bei Bedarf jederzeit nachholbar.
- Keine Badge-Ergänzung auf den drei bestehenden Seiten für die IU-Erwachsenenbildungs-Quali — bewusst
  draußen gelassen, da sie zu dem 1:1-Honorartätigkeit-Modell der drei Seiten nicht passt.

## Strang 82: Site-Überblick + Impressum-Korrektur (17.08.2026)

Anja war überfragt, wie klartext-shop insgesamt aufgebaut ist, und hatte Sorge, dass die Digistore24-
Kontosperrung (2FA-Problem, siehe Strang 56) den laufenden Verkauf blockiert. Klargestellt: Die
"Kaufen"-Buttons auf allen Verkaufsseiten öffnen aktuell eine `mailto:`-Anfrage, nicht Digistore24 —
der Verkauf läuft unabhängig von der Kontosperrung normal weiter. Digistore24 ist nur für die geplante
Automatisierung vorbereitet (`KLARTEXT_Digistore24_Produktliste.md` liegt fertig).

**Fact-Check Impressum (echter Widerspruch gefunden, Rückfrage statt Annahme):**
`SHOP_KLARTEXT_Impressum.html` behauptete "Anja Jolk betreibt aktuell noch kein angemeldetes Gewerbe
(Anmeldung gemäß § 14 GewO steht noch aus)" — im Widerspruch zu den B2B-Flyern (Strang 73) und allen
drei neuen Landingpages (Strang 77), die durchgängig "Kleingewerbe angemeldet" sagen. Rückfrage
gestellt statt geraten. Anja bestätigt: Kleingewerbe **ist** angemeldet, das Impressum war veraltet.

**Korrigiert:** Veralteter Hinweis-Kasten ("kein angemeldetes Gewerbe") komplett entfernt. Im Block
"Verantwortlich für den Inhalt" ergänzt: "Kleingewerbe angemeldet. Kleinunternehmerin gemäß § 19 UStG
— es wird keine Umsatzsteuer ausgewiesen." Getestet: `tidy` (keine HTML-Fehler), Grep bestätigt keine
weiteren Fundstellen des alten Wortlauts im Repo.

### Noch offen

- Genaues Anmeldedatum des Kleingewerbes nicht erfragt/im Impressum genannt — falls Anja das für
  Formvollständigkeit ergänzt haben möchte, wäre das ein kleiner Nachtrag.
- Digistore24-Kontosperrung selbst liegt außerhalb dieser Session (Support-Ticket bei Digistore24) —
  keine Aktion von Claude-Seite möglich oder nötig.

## Strang 83: "Begleitung zu Terminen" überall entfernt — Personenbeförderungsschein vermeiden (17.08.2026)

Anja wollte "Begleitung zu Terminen" (Arzt, Apotheke, Einkauf) aus dem Pflegedienste-Angebot streichen,
da eine Fahrgastbeförderung von Klient:innen sonst einen Fahrgastbeförderungsschein ("Personenschein",
§ 48 FeV) erfordern würde. Geprüft: Betraf ausschließlich die Pflegedienste-Materialien — Grep über
beide Repos nach "Begleitung zu"/"zu Arzt"/"Fahrdienst" ergab sonst nur zwei unrelated Treffer in
INGRA-Krisenkarten (De-Eskalations-Vokabular "Begleitung zurück", kein Bezug zu Anjas eigenem Angebot).

**Geändert (Web, `klartext-shop/Pflegedienste_Verkaufsseite.html`):**
- Hero-Text: "administrative Entlastung und Begleitung zu Terminen" → "administrative Entlastung"
- Bullet "Begleitung zu Arzt, Apotheke, Einkauf" ersatzlos gestrichen
- Bullet "Entlastung bei Terminen, Papierkramhilfe" → "Terminorganisation, Papierkramhilfe"
- Preiskarten-Kurzbeschreibung "Begleitung, digitale Assistenz..." → "Gespräche & Struktur, digitale
  Assistenz..."
- "Terminorganisation (Arzt, Therapie, Schule, Amt)" und "Begleitung bei Telefonaten mit Kassen/Ämtern"
  bewusst unverändert gelassen — beides sind organisatorische/telefonische Leistungen ohne
  Personenbeförderung, kein Personenschein-Bezug.

**Geändert (Dokument):** `Anja_Jolk_Leistungsuebersicht_Pflegedienste.docx` direkt in der XML bearbeitet
(unzip → `document.xml` patchen → Python `zipfile` statt `zip`-CLI, da `zip` in dieser Session am
gleichen Mount-Rename-Problem wie die Git-Locks scheiterte — Workaround dokumentiert für künftige
Sessions). Dieselben drei Korrekturen wie auf der Webseite übernommen, mit `scripts/office/validate.py`
gegen das Original geprüft (nur 1 Absatz weniger, sonst strukturell identisch) und per LibreOffice neu
als PDF gerendert, Rendering per Screenshot visuell geprüft (sauberes Layout, keine verwaisten
Aufzählungspunkte). Aktualisiertes docx **und** PDF in `klartext-app` ersetzt, aktualisiertes PDF auch
in die Kopie in `klartext-shop` (Download-Link auf der Verkaufsseite) übernommen.

**Getestet:** `tidy` (keine HTML-Fehler auf der Verkaufsseite), pypdf-Textprüfung bestätigt "Begleitung
zu Arzt" nicht mehr enthalten und "Terminorganisation" korrekt vorhanden in der neuen PDF.

### Noch offen

- Die ursprünglichen Honorar-Flyer aus Strang 73 (Familienzentren/Migrationszentren) enthielten laut
  Grep keine "Begleitung zu"-Formulierung — keine Änderung nötig, aber nicht noch einmal einzeln
  gegengelesen über den Grep hinaus.
- Workaround "Python zipfile statt zip-CLI beim Neupacken von docx" sollte für künftige
  Dokument-Bearbeitungen in dieser Umgebung übernommen werden, falls das Mount-Problem weiterhin
  besteht.

## Strang 84: Transparenzhinweis KI-Unterstützung im Impressum (17.08.2026)

Anja fragte, ob irgendwo vermerkt ist, dass Inhalte teilweise KI-generiert sind — Stichwort
Kennzeichnungspflicht.

**Recherche (WebSearch, aktuelle Quellen):** Die Transparenzpflichten aus Art. 50 EU AI Act gelten erst
seit 02.08.2026 (Leitlinien der EU-Kommission vom 20.07.2026). Es gibt **keine pauschale
Kennzeichnungspflicht** für jeden KI-unterstützten Text. Relevant wäre die Pflicht nur für KI-generierte
Texte, die der Information der Öffentlichkeit zu Angelegenheiten von öffentlichem Interesse dienen — und
sie entfällt ausdrücklich, wenn der Inhalt menschlich überprüft wurde und eine Person die redaktionelle
Verantwortung trägt. Beides spricht bei Anjas kommerziellen Verkaufsseiten eher gegen eine Pflicht (keine
"Angelegenheit von öffentlichem Interesse", durchgängige Fakten-Prüfung durch Anja mit Namensnennung im
Impressum). Ausdrücklich keine Rechtsberatung, nur Einschätzung anhand öffentlicher Leitlinien.

**Entscheidung (mit Anja abgestimmt):** Trotz wahrscheinlich nicht bestehender Pflicht auf Nummer sicher
gehen — Transparenzhinweis ergänzt statt auf die Ausnahme zu vertrauen.

**Umgesetzt:** Neuer Block "Transparenzhinweis" in `SHOP_KLARTEXT_Impressum.html` (zwischen Rechtliches
und Datenschutz-Block): "Bei der Erstellung von Texten auf dieser Website wurde teilweise KI-gestützt
gearbeitet. Alle Inhalte wurden von Anja Jolk fachlich geprüft, redaktionell verantwortet und
freigegeben." Gilt website-weit, da das Impressum von jeder Seite verlinkt ist. Getestet: `tidy` (keine
HTML-Fehler).

### Noch offen

- Kein gesonderter Hinweis auf den einzelnen Verkaufsseiten selbst (nur zentral im Impressum) — falls
  Anja das prominenter/pro Seite haben möchte, wäre das ein kleiner Nachtrag.
- Einschätzung zur Art.-50-Ausnahme ist keine Rechtsberatung — bei Unsicherheit weiterhin eine
  Rechtsberatung/Datenschutzbeauftragte empfehlenswert.

## Strang 85: Launch-Readiness-Check + Telefonnummer ergänzt (17.08.2026)

Anja fragte, ob sie jetzt tatsächlich Träger anschreiben kann. Live-Check aller drei Seiten auf
klartext-mentoring.de per `web_fetch` (nicht nur Repo-Stand): Familienzentren- und
Migrationszentren-Seite liefen bereits vollständig aktuell. Die Pflegedienste-Seite, ihre PDF und das
Impressum zeigten dagegen noch den **alten** Stand — die letzten drei Commit-Blöcke aus Strang 82-84
(Impressum-Korrektur, Begleitung-Entfernung, KI-Transparenzhinweis) waren lokal zwar geändert, aber nie
committet/gepusht (`git status` zeigte sie noch als `M`, `origin/main` stand auf dem Stand vor Strang
81). Klar benannt statt anzunehmen, alles sei schon live.

**Telefonnummer ergänzt:** Anja hat `+49 176 62311567` durchgegeben (deckt sich mit der Nummer aus ihrer
eigenen Bewerbungsübersicht, Strang 79/BBA-Dokument — konsistent). "Telefon: [einfügen]" in
`Anja_Jolk_Leistungsuebersicht_Pflegedienste.docx` ersetzt (gleicher XML-Patch-Workflow wie Strang 83),
PDF neu gerendert und Nummer per pypdf-Textprüfung in beiden Kopien (klartext-app, klartext-shop)
bestätigt.

### Noch offen

- Anja muss den finalen, zusammengefassten Commit-Block (Pflegedienste-Seite+PDF+Telefonnummer,
  Impressum-Korrektur+Transparenzhinweis, Merkliste) noch pushen — erst danach sind wirklich alle drei
  Seiten und das Impressum live korrekt. Bis dahin: Familienzentren/Migrationszentren-Seite sind bereits
  verschickbar, Pflegedienste-Seite noch nicht.

## Strang 78: LRS-Nachhilfe auf Familienzentren- und Migrationszentren-Seite ergänzt (17.08.2026)

Anja wollte LRS-Training mit aufnehmen ("dort hab ich auch einige Fortbildungen und auch bereits selbst
unterrichtet") und DaZ + LRS gemeinsam als "Nachhilfe" rahmen. Auf Rückfrage: Weiterbildung bei IFLW
zur Lerntherapie und bei alphaPROF, auf beiden Seiten ergänzen (Familienzentren + Migrationszentren,
nicht nur Migrationszentren, da LRS nicht migrationsspezifisch ist).

**Fact-Check der beiden Fortbildungen (WebSearch):**
- **IFLW** = Institut für integrative Lerntherapie und Weiterbildung, seit 2003, Fernstudien-Institut mit
  Zertifizierung "Integrative Lerntherapeutin (IFLW)" — Kernkompetenzen Lerntherapie, Nachhilfe, Bildung,
  Beratung (Quelle: iflw.de, bildungsserver.de). Korrekt zitiert als "Integrative Lerntherapie (IFLW)".
- **alphaPROF** = kostenfreies Online-Fortbildungsprojekt der LegaKids-Stiftung zu LRS/Legasthenie für
  Lehr- und Förderkräfte, Ziel: Diagnostik- und Förderkompetenz bei Lese-Rechtschreib-Schwierigkeiten
  (Quelle: alphaprof.de, legakids.net). Korrekte Schreibweise "alphaPROF" (nicht "Alpha-Prof"), zitiert
  als "alphaPROF (LegaKids-Stiftung)". Hinweis: Neuanmeldung endete zum 30.09.2025 — betrifft nur neue
  Teilnehmer:innen, nicht Anjas bereits abgeschlossene Fortbildung.

**Bewusste Abgrenzung (Disclaimer ergänzt, analog zum bestehenden "keine Rechtsberatung"-Muster):**
LRS-Nachhilfe ist als ergänzende Lernbegleitung positioniert, ausdrücklich **kein Ersatz für eine
schulische LRS-Feststellung oder -Diagnostik** — IFLW-Zertifizierung und alphaPROF-Fortbildung sind
keine schulpsychologische Diagnostik-Berechtigung. Disclaimer auf beiden Seiten ergänzt.

**Gebaut:**
- `Familienzentren_Verkaufsseite.html`: neue Säule 4 "LRS-Nachhilfe", neue Preiskarte 55 €/Termin
  (4/8 Termine 210 €/400 €, gleicher Satz wie Struktur-Coaching), zwei neue Badges (Integrative
  Lerntherapie IFLW, LRS-Fortbildung alphaPROF), neue FAQ, Disclaimer erweitert. `.preis-grid`
  max-width von 800px auf 1000px angepasst (jetzt 3 statt 2 Preiskarten).
- `Migrationszentren_Verkaufsseite.html`: Säule 3 von "Sprachliche & administrative Begleitung" zu
  "Sprachliche, lernbezogene & administrative Begleitung" erweitert (DaZ- und LRS-Nachhilfe gemeinsam
  als "Nachhilfe" gerahmt), Preiskarte umbenannt zu "Alltagsbegleitung inkl. DaZ- & LRS-Nachhilfe"
  (weiterhin 50 €/Termin, kein separater Preis — LRS wird wie DaZ in den bestehenden Gesamtpreis
  integriert statt eigene Preiszeile), zwei neue Badges, neue FAQ, Check-Item und Disclaimer erweitert.

**Getestet:** `tidy` (keine HTML-Fehler auf beiden Seiten nach der Änderung), jsdom-Smoketest
(Familienzentren jetzt 3 Preiskarten/5 FAQ/6 Badges, Migrationszentren weiterhin 1 Preiskarte/jetzt
5 FAQ/6 Badges — Preiskarten-Anzahl bei Migrationszentren bewusst unverändert, da LRS dort in den
bestehenden Gesamtpreis integriert wurde statt eine neue Karte zu bekommen).

### Noch offen

- Git-Commit für Strang 77 **und** 78 steht weiterhin aus — beide hängen an derselben verwaisten
  `.git/index.lock` in `klartext-shop` und `klartext-app` (siehe Strang 77, "Noch offen"). Anja muss
  die drei Dateien manuell löschen, danach werden beide Stränge in einem gemeinsamen Commit-Durchgang
  nachgeholt.
- Kein separater Preis für LRS-Nachhilfe auf der Migrationszentren-Seite (anders als bei Familienzentren
  mit eigener 55€-Karte) — falls Anja das lieber als eigene Preiszeile sehen möchte statt im
  Pauschalpreis, wäre das eine kleine Nachbesserung.
- Keine Aussage dazu, ob IFLW-Zertifizierung/alphaPROF-Fortbildung eine formale Berechtigung zur
  amtlichen LRS-Feststellung beinhalten (z. B. für Nachteilsausgleich in der Schule) — bewusst nicht
  behauptet, Disclaimer schließt das aus. Falls Anja hierzu weitere Qualifikationen hat, könnte das
  präzisiert werden.

## Strang 86: Live-Check Familienzentren/Migrationszentren + Anschreiben-Vorlagen (17.08.2026)

Anja ist freigegeben, Träger aktiv anzuschreiben. Zwei Schritte in dieser Session:

**Live-Check per web_fetch** (Cache-Busting `?v=2`): `Familienzentren_Verkaufsseite.html` und
`Migrationszentren_Verkaufsseite.html` erneut abgerufen und mit dem dokumentierten Stand
abgeglichen — Preise (Familienzentren: 55 €/Termin Struktur-Coaching+Stabilisierung, 40 €/h
Administrativer Support, 55 €/Termin LRS-Nachhilfe; Migrationszentren: 50 €/Termin
Alltagsbegleitung inkl. DaZ- & LRS-Nachhilfe), Badges, Qualifikationstitel ("Systemische Beraterin
und Coachin (IHK)") und alle Disclaimer (kein Ersatz für Jugendamt/Frühe Hilfen, keine
Rechtsberatung, DaZ kein BAMF-Integrationskurs, keine schulische LRS-Diagnostik) stimmen mit dem
letzten Stand überein. Beide Seiten sind live korrekt.

**Zwei Anschreiben-Vorlagen erstellt** (E-Mail, ca. 180–200 Wörter, formelle Anrede, niedrigschwelliger
CTA für ein kurzes Telefonat): eine für Familienzentren, eine für Migrationszentren. Datei: außerhalb
des Repos bei Anja (`Anschreiben_Vorlagen_Familienzentren_Migrationszentren.md`, aus dem
Cowork-Output-Ordner übernommen — kein Repo-Artefakt, da reine Text-Vorlage ohne Website-Bezug).

**Nachtrag (auf Anjas Hinweis):** Flyer werden nicht nur verlinkt, sondern als PDF-Anhang mitgeschickt
(`Anja_Jolk_Flyer_Familienzentren.pdf`, `Anja_Jolk_Flyer_Migrationszentren.pdf`, beide bereits in
`klartext-app` vorhanden) — bei institutionellen Empfängern üblicher, da die Leitung den Flyer ohne
Klick öffnen und intern weiterleiten kann. Website-Link bleibt zusätzlich in der Mail für
Preise/FAQ, die nicht auf dem Flyer stehen. Vorlagen entsprechend angepasst (PS-Zeile).

**Zweiter Nachtrag — Flyer waren veraltet, jetzt neu gebaut:** Auf Anjas Rückfrage ("die Flyer haben
gar keine Preise?") geprüft: Beide PDFs hatten nur "Honorar auf Anfrage", keine Preise. Zusätzlich
entdeckt: beide waren generell veraltet gegenüber dem Live-Stand der Seiten — Familienzentren-Flyer
hatte nur 3 statt 4 Säulen (LRS-Nachhilfe aus Strang 78 fehlte), Migrationszentren-Flyer erwähnte in
Säule 3 nur DaZ, nicht die LRS-Ergänzung; beide trugen noch den alten Titel "Systemische Beraterin
(IHK)" statt der korrigierten Fassung "und Coachin" (Strang 80) und hatten keine Telefonnummer.

Auf Anjas Entscheidung ("voll aktualisieren + Preise ergänzen") beide Flyer komplett neu gebaut
(HTML/CSS → WeasyPrint, Farben/Struktur am Design-System orientiert: Navy #1B3A4B, Grün #6EC6A0,
Orange #C47A00, Beige #F5F0E8). Jetzt enthalten: alle Säulen inkl. LRS, korrigierter Titel,
Telefonnummer, vollständige Preistabellen 1:1 aus den Landingpages übernommen (Familienzentren:
55 €/Termin Struktur-Coaching+Stabilisierung, 40 €/h Administrativer Support, 55 €/Termin
LRS-Nachhilfe; Migrationszentren: 50 €/Termin Alltagsbegleitung inkl. DaZ- & LRS-Nachhilfe).
Beide je 1 Seite, in `klartext-app` UND `klartext-shop` aktualisiert (identische Dateien).

**Dritter Nachtrag — echte Schrift + Klarstellung zur Bezahlung:** Anja bestand zurecht auf der
korrekten Schrift ("die schrift müssen wir unbedingt nachbessern"). Da die Sandbox keinen
Netzwerkzugriff auf Google Fonts hat, hat Anja `Playfair Display` und `DM Sans` selbst von
fonts.google.com heruntergeladen (Downloads-Ordner freigegeben), ich habe die TTF-Dateien
lokal installiert und beide Flyer mit den echten Schriften neu gerendert — jetzt schriftidentisch
mit der Website.

Zweite Rückfrage von Anja: Was, wenn der Träger nicht zahlt, sondern nur empfiehlt, und die Familie
selbst zahlt? Antwort: Genau das ist das vorgesehene Modell (Direktvermittlung, kein Vertrag mit dem
Träger, kein Ausfallrisiko über den Träger) — stand aber im Flyer nicht deutlich genug direkt bei der
Preisliste. Ergänzt: hervorgehobener Kasten direkt im Honorar-Block auf beiden Flyern: "Für Ihre
Einrichtung entstehen keine Kosten. Die Familie bucht und bezahlt direkt und privat bei mir – Sie
vermitteln lediglich den Kontakt, kein Vertrag, keine Rechnung an Sie."

Beide PDFs final in `klartext-app` UND `klartext-shop` aktualisiert, je 1 Seite, Playfair
Display/DM Sans korrekt eingebettet.

**Bekanntes Sandbox-Problem erneut aufgetreten:** `.git/index.lock` in beiden Repos ließ sich beim
`git status` nicht automatisch aufräumen ("Operation not permitted") — betrifft nur die Sandbox, die
Dateiänderungen selbst sind unabhängig davon korrekt geschrieben. Anja muss vor dem Commit einmal
manuell aufräumen (siehe Merkliste-Kopfbereich, Abschnitt "Bekanntes Sandbox-Problem").

**Vierter Nachtrag — Pflegedienste-Flyer + dritte Anschreiben-Vorlage, plus Teilzeitanstellung als
zusätzliche Frage in allen drei Vorlagen:** Kontext: Malteser Hausnotruf hat Anja zum 31.08. gekündigt
(nur 3 Monate Beschäftigung, ALG-I-Anwartschaftszeit von 12/30 Monaten damit nicht erfüllt — Bürgergeld
droht ohne neue Anstellung). Homeoffice-Jobsuche lief ins Leere (nur Kreditvertrieb/zu spezifisch).
Idee: bei den ohnehin angeschriebenen Trägern zusätzlich nach einer Teilzeitanstellung fragen, nicht
nur Honorar-Kooperation — sinnvoll, da diese Einrichtungen oft echte Teilzeitstellen passend zu Anjas
Qualifikation haben. Umsetzung: **ein** Anschreiben mit **zwei** Angeboten (nicht zwei getrennte
Kontakte), Homeoffice ist jetzt kein Muss mehr (Präsenzstellen ausdrücklich ok). Ergänzt in allen drei
Vorlagen (Familienzentren, Migrationszentren, jetzt auch Pflegedienste): "Ergänzend: Da ich meine
Selbstständigkeit gerade aufbaue, bin ich aktuell auch offen für eine sozialversicherungspflichtige
Teilzeitanstellung bei Ihnen..." Datei: `Anschreiben_Vorlagen_Familienzentren_Migrationszentren.md`
(jetzt mit drei statt zwei Vorlagen, Dateiname bewusst nicht geändert).

Zusätzlich Pflegedienste-Flyer (`Anja_Jolk_Leistungsuebersicht_Pflegedienste.pdf`) geprüft und neu
gebaut (bisher LibreOffice-Erstellung ohne HTML-Quelle, jetzt wie die anderen zwei per HTML/CSS +
WeasyPrint mit Playfair Display/DM Sans): fehlende Kredential-Kopfzeile ("Systemische Beraterin und
Coachin (IHK)") ergänzt, "Für Ihren Pflegedienst entstehen keine Kosten"-Hinweis direkt im
Honorar-Block ergänzt (gleiches Muster wie bei den anderen zwei Flyern), Inhalte 1:1 mit
Pflegedienste_Verkaufsseite.html abgeglichen (drei Leistungsbereiche, Preise 40/45/55 €/Std.,
Pflegekurse § 45 SGB XI erwähnt). In `klartext-app` UND `klartext-shop` aktualisiert, 1 Seite.

**Offen:** Anja beantragt parallel keine ALG I (Anwartschaftszeit nicht erfüllt) — Bürgergeld bleibt
als Rückfalloption im Raum, falls bis 31.08. keine neue Anstellung/Teilzeitstelle zustande kommt.
Nächster Schritt bei Anja: Anschreiben an alle drei Zielgruppen verschicken, ggf. weitere Träger
(Kitas, Wohlfahrtsverbände) einbeziehen, falls die Zeit bis 31.08. knapp wird.

**Fünfter Nachtrag — vierter Flyer für Schulbegleitungs-Träger (Anjas "eigentliches Projekt"):**
Bisher komplett unberücksichtigt. Wichtige Klärung im Gespräch:

- **Positionierung korrigiert:** Anjas erster Impuls war "Einarbeitung + Betreuung/Supervision"
  anbieten. Zwei Korrekturen nötig: (1) Träger leisten die organisatorische Einarbeitung bereits
  selbst — Anja kann dort nicht "reingrätschen", sondern muss fachlich ergänzen, nicht ersetzen.
  (2) Anja hat noch nie Fallmanagement-Supervision geleitet und keine Supervisions-Zertifizierung
  — "Supervision" als Begriff bewusst vermieden (in Deutschland oft an eigene Ausbildung geknüpft),
  stattdessen ehrlich als "Begleitung & erste Ansprechpartnerin bei Redebedarf" positioniert.
- **Zwei Bausteine:** Fachlicher Vertiefungs-Workshop (Barometer, kLAR-Modell, Krisenintervention
  anhand der Feuerwehrkarten — Ergänzung zur bestehenden Einarbeitung) + Begleitung/Ansprechpartnerin
  (kollegiale fachliche Begleitung, keine formale Supervision).
- **Preisvorschlag (Expertenvorschlag auf Anjas Wunsch, Marktrecherche zu Supervisions-/
  Dozentenhonoraren):** Workshop 320 € Pauschale (Halbtag, bis 10 Teilnehmende, entspricht
  hochgerechnet ca. 640 €/Tag — bewusst über dem kritisierten "unter 500 €/Tag" öffentlicher
  Träger). Begleitung 80 €/Termin (60 Min.), Monatspauschale 150 € (bis 2 Termine) — bewusst
  niedriger als ursprünglich vorgeschlagene 120 €/Sitzung für "Supervision", da geringerer
  Formalitätsgrad ehrlich abgebildet werden soll.
- **Wichtiger Unterschied zu den ersten drei Flyern:** Hier zahlt der Träger selbst (kein
  "Direktvermittlung, keine Kosten für die Einrichtung"-Modell) — im Anschreiben (Vorlage 4)
  entsprechend vermerkt.
- **Klärung "eigentliche Website":** `https://klartext-mentoring.de/` (Root-Domain) ist die
  eigentliche Hauptseite — zeigt das komplette KLARTEXT-System für INGRA/Schulbegleitung inkl.
  12-Wochen-Präsenzkurs mit Zertifikat (6 Seminare, Supervision, Praxisbegleitung durch Anja als
  Trainerin), nicht nur Kartendecks. `KLARTEXT_Shop_Uebersicht.html` ist der reine
  Kartendecks-Katalog, eine Unterseite davon.
- **Sicherheitscheck "Kartendecks frei verfügbar":** Auf Anjas Sorge hin geprüft — Flip-Card-App
  (`karten.klartext-mentoring.de`) ist passwortgeschützt ("Zugang nach Kauf"), direkte
  PDF-Dateinamen der kompletten Decks (z. B. `KLARTEXT_KD-Deck_komplett.pdf`) sind auf dem Server
  nicht erreichbar (fallen auf die Startseite zurück), Verkaufsseiten zeigen nur
  wasserzeichenversehene Musterkarten. Kein Leak gefunden — falls Anja trotzdem etwas Konkretes
  gesehen hat, steht eine gezielte Nachprüfung mit Screenshot/Link noch aus.

**Gebaut:** `Anja_Jolk_Flyer_Schulbegleitung_Traeger.pdf` (HTML/CSS + WeasyPrint, gleiches
Design-System, 1 Seite), in `klartext-app` UND `klartext-shop`. Vierte Anschreiben-Vorlage in
`Anschreiben_Vorlagen_Familienzentren_Migrationszentren.md` ergänzt (Teilzeitanstellungs-Zusatz
hier explizit NICHT als Schulbegleitung, sondern Koordination/Einarbeitung/Verwaltung formuliert
— Anja möchte nicht selbst als Schulbegleitung eingesetzt werden).

### Noch offen
- Digistore24 (Anja ist wieder freigeschaltet) und Instagram/TikTok-Aufbau stehen noch aus,
  bewusst zurückgestellt zugunsten dieses vierten Flyers — nächste Priorität laut Anja.
- Die "Träger-Lizenz fürs ganze Team" (digitaler Zugang zum Kartensystem) ist weiterhin ungeklärt,
  bewusst nicht in diesem Flyer bepreist.
- Screenshot/Link von Anja zur "frei verfügbar"-Sorge steht noch aus, falls das Problem doch real
  ist.

### Noch offen

- Spot-Check der Pflegedienste-Seite/PDF war in Strang 85 bereits erledigt; für Familienzentren/
  Migrationszentren war es bisher nur die Text-Zusammenfassung aus der Vorsession — jetzt mit
  echtem `web_fetch` nachgeholt und bestätigt.
- Anschreiben-Vorlagen enthalten Platzhalter `[Ihre geschäftliche E-Mail-Adresse]` — Anja muss die
  reale Absender-E-Mail vor dem ersten Versand ergänzen.
- Git-Commit-Rückstand aus Strang 77/78 (`.git/index.lock`) weiterhin unverändert offen.

## Strang 87 (18.08.2026) — Digistore24: alle 20 Kartendeck-Produkte angelegt

Träger-Kontaktliste (`Traeger_Kontaktliste_Schwerte_Dortmund_Hagen.md`, recherchiert per
Websuche, mit Quellen) für alle vier Zielgruppen fertiggestellt. Danach Digistore24-Produkte
über Claude-in-Chrome-Browsersteuerung angelegt (Anja selbst eingeloggt, ich habe nur das
Formular ausgefüllt, keine Zugangsdaten gesehen/eingegeben).

**Wichtiger technischer Befund:** Das Datei-Upload-Werkzeug im Browser-Tool funktioniert aktuell
nicht (Bug, unabhängig von Dateigröße — mehrfach mit unterschiedlichen Parametern getestet).
Deshalb konnte ich die eigentlichen PDF-Dateien nicht selbst hochladen. Alles andere habe ich
komplett automatisch erledigt:

- Für alle 20 Produkte (KD, JD, AT, LRS, TK, FK, M3, HB, SMI, SP, MB, EL, LK, TR, ADHS, FS,
  DaZ-GS, DaZ-Sek1, OGS, GK): Produktname, Produktname für Käufer, Produkttyp "Downloads",
  Verkaufsseite-URL, Affiliate-Provision 0 % (Auto-Akzeptieren auf "Nein" gesetzt, sonst
  Validierungsfehler), Preis lt. `KLARTEXT_Digistore24_Produktliste.md` gesetzt.
- KD-PDF (Pilotprodukt, ID 719673) war schon angelegt, aber noch mit Alt-Preis 37 € — auf 18 €
  korrigiert.
- Pro Produkt ein leeres "Datei-Paket" im Download-Tresor angelegt und mit dem Produkt
  verknüpft (Ausliefern-Tab). Bei MB/EL/LK ist im Paketnamen vermerkt, dass mehrere Dateien
  zusammengehören (kein ZIP nötig — Digistore24 erlaubt mehrere Dateien pro Paket).
- Datei `Digistore24_Upload_Anleitung.md` für Anja erstellt: Tabelle mit allen 20 Produkten,
  Paket-Namen und genauen Dateinamen aus `klartext-app`, plus Schritt-für-Schritt-Anleitung für
  den letzten Klick (Datei(en) hochladen → Mein Gerät → Datei(en) auswählen).

### Noch offen
- ~~Anja muss pro Produkt die passende(n) PDF-Datei(en) selbst hochladen~~ erledigt (Anja hat
  alle 20 Dateien hochgeladen).
- ~~Genehmigung bei Digistore24 beantragen~~ erledigt für alle 20 Produkte (siehe Strang 88).
- Produktgruppe "Kartendecks" noch nicht angelegt (nur "(Ohne Gruppe)" verfügbar), nicht
  blockierend.
- Insel-Set/Zonen-Set weiterhin bewusst zurückgestellt (Phase 2).
- Instagram/TikTok-Aufbau weiterhin offen.
- **Offener Verdacht, noch nicht bestätigt:** MB-PDF-Datei-Paket (ID 138548) zeigt im
  Download-Tresor weiterhin nur 1 Datei/4 MB, erwartet werden aber 2 Dateien (~6,2 MB:
  `KLARTEXT_Mobbing-Intervention_komplett.pdf` + `KLARTEXT_AntiMobbing_Arbeitsmaterialien.pdf`,
  siehe Kit-Entscheidung 07.08.2026). Vermutlich hat Anja nur eine der zwei Dateien hochgeladen —
  mit ihr klären und ggf. zweite Datei ergänzen.

## Strang 88 (18.08.2026) — Digistore24-Genehmigung für alle 20 Produkte + Flip-Card-App-Leck geschlossen

**Genehmigung beantragt (technischer Befund):** Der erste Versuch, die Genehmigung für KD-PDF zu
beantragen, zeigte auch nach korrekt ausgefüllter Checkliste (7 Häkchen) + Speichern weiterhin
"Genehmigung beantragen" statt "Warte...", mit neuer Inline-Warnung "Bitte führen Sie einen
Testkauf durch!". Vermutung: Digistore24 verlangt serverseitig einen tatsächlichen (Test-)Kauf,
bevor ein Genehmigungsantrag angenommen wird — unabhängig vom Checkliste-Häkchen "Testkauf
gemacht". Anja hat das für GK-PDF (723461) über die kostenlose TEST-PAY-Zahlungsart verifiziert:
nach ihrem Testkauf wurde der erneute Genehmigungsantrag sofort zu "Warte..." — Hypothese
bestätigt. Anja hat danach selbstständig für alle 20 Produkte Testkäufe gemacht und die
Genehmigung beantragt; Produktliste zeigt jetzt für alle 20 Produkte "Warte... - Antrag
zurückziehen". Damit ist der komplette Digistore24-Rollout (Anlage, Preise, Dateien, Genehmigung)
für alle 20 Kartendeck-PDFs abgeschlossen, es fehlt nur noch die Prüfung durch Digistore24 selbst.

**Flip-Card-App war öffentlich frei zugänglich, ohne dass das so gedacht war:** Anja fiel beim
Blick auf die Verkaufsseiten auf, dass der Button "📱 Als Flip-Card ausprobieren" nicht zu einer
begrenzten Vorschau führt, sondern zur kompletten Flip-Card-Web-App
(`karten.klartext-mentoring.de`) — dort sind alle 26 Decks komplett und ohne jede Zugriffssperre
durchsuchbar. Klärung mit Anja: Diese App war ursprünglich **nur als privates Werkzeug für sie
selbst** gedacht (um alle Karten durchzusehen), nicht als Kundenprodukt — das deckt sich mit der
bewussten Entscheidung aus `KLARTEXT_Konzept_Kartendecks-App.md` ("Zugriffssteuerung pro
gekauftem Deck bewusst noch nicht gelöst, alle Decks vorerst frei zugänglich, Zugriffsschutz erst
mit echtem Checkout nachziehen"). Die echte Kunden-Vorschau sind die Wasserzeichen-Bildmuster in
der `vorschau/`-Galerie auf jeder Verkaufsseite — die bleiben unverändert.

Mit Anjas Bestätigung alle 25 öffentlichen Links zur Flip-Card-App entfernt (22 Verkaufsseiten +
2 Links auf `index.html` + 1 Link auf `KLARTEXT_Shop_Uebersicht.html`, alle im
`klartext-shop`-Repo). Zusätzlich eine dadurch falsch gewordene Werbeaussage auf `index.html`
entfernt ("Jedes Deck zusätzlich als digitale Flip-Card-App zum Ausprobieren"). Die App selbst
läuft technisch unverändert weiter (z. B. per Lesezeichen für Anja privat erreichbar), ist aber
nirgendwo mehr im Shop verlinkt.

### Noch offen
- ~~MB-PDF-Datei-Paket-Diskrepanz~~ erledigt: Anja hat die fehlende zweite Datei
  (`KLARTEXT_AntiMobbing_Arbeitsmaterialien.pdf`) nachgeladen, Paket zeigt jetzt korrekt 2
  Dateien/6 MB.
- Digistore24-Prüfergebnis für alle 20 Produkte abwarten.
- Produktgruppe "Kartendecks" weiterhin nicht angelegt, nicht blockierend.

## Strang 89 (18.08.2026) — Flip-Card-App als echter Bonus: Passwortschutz + Dankeseiten

Anja erinnerte sich an den ursprünglichen Plan aus `KLARTEXT_Konzept_Kartendecks-App.md`: PDF und
Flip-Card sollten irgendwann zusammen angeboten werden, Zugriffsschutz war bewusst auf "sobald
echter Checkout da ist" verschoben — der Checkout ist jetzt da. Auf Nachfrage, wie genau
(PDF/Flip/Bundle als drei Preisstufen vs. Flip als Bonus zum bestehenden Preis) meine Empfehlung
gegeben: **Flip-Card als kostenloser Bonus zu jedem PDF-Kauf**, keine neue Preisstruktur bei
Digistore24 (hätte 60 statt 20 Produkte oder unsichere Preisplan-Logik bedeutet, unnötiger
Aufwand vor dem ersten echten Verkauf). Anja hat zugestimmt.

**Umgesetzt:**
- **Passwortschutz in der Flip-Card-App** (`klartext-app/pwa/`): pro Deck ein zufälliger
  6-stelliger Code (Kleinbuchstaben/Ziffern, ohne verwechselbare Zeichen), als SHA-256-Hash in
  neuer `pwa/data/access.json` hinterlegt (nicht der Klartext-Code selbst im Code). Beim Öffnen
  eines Decks (Kachel-Klick oder `?deck=`-Link) fragt die App den Code ab, merkt sich freigeschaltete
  Decks danach per `localStorage` auf dem Gerät. Wichtig zu wissen: das ist eine reine
  Client-Schranke (kein Backend/Login), kein Schutz gegen technisch versierte Nutzer, die im
  Quelltext nachsehen — aber ausreichend, um zufälliges/beiläufiges Mitlesen fremder Decks zu
  verhindern, was der eigentliche Anlass war. `service-worker.js` Cache-Version v12→v13 erhöht.
- **20 einzelne Dankeseiten** (`klartext-shop/<CODE>_Dankeseite.html`, eine pro verkauftem
  Produkt) statt einer gemeinsamen Seite mit `?deck=`-Parameter — bewusst so, damit niemand durch
  Ändern eines Parameters an fremde Passwörter kommt (jede Datei enthält nur ihren eigenen Code).
  Jede Seite zeigt: Bestätigung des Kaufs, Pflichtsatz "Die Abbuchung erfolgt durch
  Digistore24.com", den Zugangscode fürs jeweilige Deck, und einen Button direkt zur Flip-Card-App.
- **Dankeseite-Feld in allen 20 Digistore24-Produkten gesetzt** (Eigenschaften-Tab), z. B. KD-PDF
  → `https://klartext-mentoring.de/KD_Dankeseite.html`, per Browser-Automation gesetzt und
  einzeln nach dem Speichern verifiziert.
- Passwörter auch für die 6 noch nicht verkauften Decks (Insel-Set × 2, Zonen-Set × 2, TO, DS)
  vorsorglich mit angelegt, damit `access.json` vollständig ist — werden aber erst verteilt, wenn
  diese Produkte live gehen (Phase 2).

**Zugangscodes (nur intern, nicht weitergeben):**

| Deck | Code | Zugangscode |
|---|---|---|
| KD-Deck | KD | `7e555w` |
| JD-Deck | JD | `u7fm8b` |
| AT-Deck | AT | `hmmae4` |
| LRS/Dyskalkulie-Deck | LRS | `xnfnwj` |
| TK-Deck | TK | `uebfrk` |
| Krisendeck | FK | `jvx3qq` |
| Werkzeugkarten | M3 | `z45wmk` |
| Hochbegabung | HB | `692n67` |
| SMI-Deck | SMI | `d6f35x` |
| SP-Deck | SP | `3nkhhs` |
| Mobbing-Intervention (MB-Kit) | MB | `hd3mt9` |
| EL-Deck | EL | `kd3th7` |
| LK-Deck | LK | `bts8p6` |
| TR-Deck | TR | `4s3q3m` |
| ADHS-Deck | ADHS | `4f3c49` |
| FS-Deck | FS | `y7xmg2` |
| DaZ-GS-Deck | DaZ-GS | `52q7ck` |
| DaZ-Sek-I-Deck | DaZ-Sek I | `c9p5qp` |
| OGS-Deck | OGS | `tcqrs2` |
| Geschichtenkarten | GK | `hjtxz2` |

### Noch offen
- **Wichtig, blockiert die Funktion:** `klartext-app` (pwa-Ordner) und `klartext-shop`
  (Dankeseiten + entfernte Flip-Card-Links) müssen erst committet und gepusht werden, sonst
  laufen weder Passwortschutz noch Dankeseiten live. Git-Befehle unten.
- ~~Danach einmal selbst testen~~ erledigt, siehe Strang 90 — Fund: falsches Repo bearbeitet.
- Digistore24-Prüfergebnis für alle 20 Produkte weiterhin abwarten.
- Produktgruppe "Kartendecks" weiterhin nicht angelegt, nicht blockierend.

## Strang 90 (18.08.2026) — Passwortschutz war im falschen Repo, jetzt im echten Live-Repo korrigiert

Anjas Test ("ohne Passwort reingekommen") deckte auf: `karten.klartext-mentoring.de` wird gar
nicht aus `klartext-app/pwa/` ausgeliefert (dort hatte ich Strang 89 gebaut), sondern aus einem
eigenen, dritten Repo `klartext-karten` (Cloudflare-Pages-Projekt `klartext-karten`,
GitHub `anja2026-dev/klartext-karten`) — steht auch schon in Strang 55 (07.08.2026): Anja hatte
den `pwa/`-Code damals komplett dorthin ausgelagert (inkl. eigener Suchleiste, die `klartext-app/
pwa/` nie bekommen hat) und **zusätzlich am selben Tag eine einfache seitenweite Passwortsperre**
eingebaut (ein Passwort `brainy-lernt-2026` für alle 24 Decks, Klartext im Code), weil sie durch
die offene Zugänglichkeit alarmiert war, während Digistore24 an einem 2FA-Problem hing. Das war
schon damals als Übergangslösung markiert, mit der offenen Notiz "Passwort-Weitergabe an
Kund:innen einrichten, sobald Digistore24 läuft" — genau die Aufgabe aus Strang 89, nur eben im
falschen Repo umgesetzt. `klartext-app/pwa/` ist seit 07.08. nur noch die (jetzt veraltete)
Ursprungskopie, nicht mehr live.

**Korrektur:** Zugriff auf `klartext-karten` (liegt lokal neben `klartext-app`/`klartext-shop`)
angefordert und erhalten. Dort die alte seitenweite Sperre (`lockScreen`/`appShell`-Wrapper,
`LOCK_PASSWORD`) entfernt und durch das Strang-89-System ersetzt (Passwort pro Deck, SHA-256-Hash
in neuer `data/access.json`, Abfrage beim Öffnen eines Decks über `openDeck()` — greift damit
automatisch auch bei Deep-Links und Sucher-Treffern, da beide über dieselbe Funktion laufen).
Die 22-Decks-Suchleiste aus Strang 55 unverändert erhalten. `service-worker.js` Cache-Version
v14→v15. `access.json` ist identisch mit der Version in `klartext-app/pwa/data/` — die 20 schon
gebauten Dankeseiten bleiben also gültig, keine neuen Zugangscodes nötig.

**Randnotiz:** `klartext-karten/data/decks.json` hat nur 24 Decks (kein TO-/DS-Deck) — die
System-Erweiterung um Tourette/Trisomie-21 aus einer späteren `klartext-app`-Änderung wurde nie
nach `klartext-karten` übertragen. Nicht Teil dieser Korrektur, aber als Lücke vermerkt: die
beiden Decks sind über die Live-App aktuell nicht erreichbar.

### Noch offen
- **Wichtig:** `klartext-karten` muss noch committet und gepusht werden (Befehle unten), sonst
  bleibt die alte Sperre live.
- Nach dem Push: einmal in einem privaten/Inkognito-Fenster `karten.klartext-mentoring.de`
  öffnen, ein Deck antippen, prüfen dass jetzt der deckeigene Code (nicht mehr
  `brainy-lernt-2026`) abgefragt wird.
- TO-/DS-Deck-Lücke zwischen `klartext-app` und `klartext-karten` — später einmal synchronisieren,
  nicht dringend.
- Digistore24-Prüfergebnis für alle 20 Produkte weiterhin abwarten.
- Produktgruppe "Kartendecks" weiterhin nicht angelegt, nicht blockierend.

## Strang 91 (18.08.2026) — Shop-Kaufbuttons von "Vormerken" auf echten Digistore24-Checkout umgestellt

Anja fiel auf: Trotz der 20 live geschalteten Digistore24-Produkte zeigten alle Verkaufsseiten im
`klartext-shop`-Repo weiterhin "Vormerken"-Buttons statt echter Kaufmöglichkeit — Rest vom
Vorbestellungs-Stand vor dem Digistore24-Rollout. Betroffen war der komplette Shop, nicht nur
einzelne Buttons.

**Umgesetzt, für alle 20 Produkte mit fertigem Digistore24-Produkt (nicht für Insel-Set/
Zonen-Set, die noch keins haben):**
- "🛒 Jetzt kaufen"-Button (Digital/PDF) auf jeder Verkaufsseite: bisher ein Popup
  ("Online-Kauf in Vorbereitung... per E-Mail bestellen"), jetzt ein direkter Link zur echten
  Digistore24-Kasse (`https://www.checkout-ds24.com/product/<Produkt-ID>`, neuer Tab). Print- und
  Träger-Lizenz-Buttons bewusst unverändert gelassen (dafür gibt es keine Digistore24-Produkte,
  bleiben "Vormerken" per E-Mail).
- Hero-Button "Jetzt vormerken" → "Jetzt kaufen" (Anker bleibt `#preise`).
- Abschnitts-Überschrift "„Code" vormerken" → "„Code" kaufen".
- Finale CTA am Seitenende: Text + Button ebenfalls auf echten Checkout-Link umgestellt, Text von
  "Trag dich unverbindlich für die Vorbestellung ein" auf "Einmalig zahlen — direkt als
  PDF-Download erhältlich" geändert.
- **Wichtiger Zusatzfund:** Auf allen 20 Seiten stand im Preise-Bereich noch ein Hinweiskasten
  ("Wir bereiten gerade Druck und Verkaufsstart vor. Trag dich jetzt schon unverbindlich ein...")
  der dem neuen Kaufen-Button direkt widersprochen hätte. Auf "Als PDF-Download sofort erhältlich,
  die Druckversion bereiten wir gerade vor." geändert (Kartenzahl-Bestätigung im ersten Satz
  unverändert gelassen, die ist weiter korrekt).
- Auf der JD-Seite zusätzlich einen ganzen Absatz entfernt, der noch behauptete "JD erscheint in
  Kürze, Kartentexte werden gerade fertiggestellt" — obwohl JD-PDF längst live ist.
- `KLARTEXT_Shop_Uebersicht.html`: Badge "Verfügbar zum Vormerken" → "Jetzt erhältlich" bei genau
  den 20 echten Produkten (per Deck-Code-Zuordnung, nicht pauschal), Hinweistext am Seitenende
  ergänzt ("20 Kartendecks sind als PDF-Download direkt käuflich").
- Alle Änderungen automatisiert per Skript umgesetzt (Regex mit Vorher/Nachher-Zählung pro Datei,
  keine stille Fehlanpassung), danach Div-Balance und Produkt-ID-Zuordnung stichprobenartig
  geprüft — sauber.

**Nachtrag (gleicher Tag): JD-Preisspanne geprüft und Kartenzahl korrigiert.** Anja bat, den oben
genannten Fund vollständig zu klären. Ergebnis: Die "X–Y €"-Preisspannen auf allen 20
Verkaufsseiten sind kein Fehler — bei allen 20 Produkten entspricht der obere Wert der Spanne
exakt dem echten, fest in Digistore24 hinterlegten Preis (geprüft über den Tab "Zahlungspläne" je
Produkt, z. B. JD: Spanne 19–22 €, echter Preis 22,00 €; KD: Spanne 15–18 €, echter Preis
18,00 €; usw. — alle 20 stimmen exakt überein). Keine Änderung nötig.

Die Kartenzahl bei JD war dagegen tatsächlich veraltet (40 statt 52, laut `decks.json`) und wurde
an allen vier Stellen auf der Seite korrigiert: Hero-Text, Hero-Statistik, Leistungs-Kachel,
beide Preis-Listen (PDF und Print). Dabei zusätzlich zwei weitere Reste aus der
Vorbereitungsphase gefunden und mitkorrigiert, die ausschließlich auf JD noch vorhanden waren
(alle anderen 19 Seiten hatten das schon richtig): die dritte Hero-Statistik zeigte noch
"24/40 Karten in Gestaltung" (jetzt: "fertig / Karten & PDF stehen", wie bei allen anderen
Decks), und die finale CTA-Überschrift hieß noch "JD erscheint in Kürze" (jetzt: "JD ist
startklar", wie bei KD/EL/LK/TR). Alle Änderungen nur in `JD_Verkaufsseite.html`, Div-Balance
geprüft (117/117), keine Auswirkung auf die anderen 19 Dateien.

### Noch offen
- `klartext-shop`-Änderungen (Kaufbuttons, Hinweistexte, JD-Korrektur) noch nicht committet/gepusht.

## Strang 92 (18.08.2026) — Kostenloses "KLARTEXT-Schnupperpaket" als Lead-Magnet aufgesetzt

Anja erinnerte sich an eine alte Idee: neben den 20 bezahlten Decks auch etwas Kostenloses anbieten.
Auf Nachfrage keine konkrete Erinnerung mehr an Details — gemeinsam neu entschieden.

**Verworfene Optionen, mit Begründung:**
- FK-Krisendeck komplett gratis: verworfen, weil die Verkaufsseite selbst "nur für qualifizierte
  Fachkräfte" sagt und ausdrücklich kein Kinderschutz-/Rechtsberatungs-Ersatz ist — ein offener
  Gratis-Download hätte genau diese bewusste Zielgruppen-Eingrenzung unterlaufen.
- SP-Deck komplett gratis: von Anja abgelehnt.
- Reiner Karten-Querschnitt (3-5 Einzelkarten aus verschiedenen Decks): erster Vorschlag, von Anja
  zu Recht hinterfragt ("nicht querbeet") — zu wenig echter Nutzwert.
- Ein komplettes größeres Deck (KD/JD/GK/M3) gratis: verworfen wegen zu hohem Umsatzverlust.

**Entschieden:** Ein neues, eigenständiges 8-Karten-PDF ("KLARTEXT-Schnupperpaket") aus drei
allgemeinen, nicht diagnose-gebundenen Decks — 4 Karten aus M3 (Werkzeugkarten: "Kind kommt
aufgewühlt an", "Übergang zwischen Situationen", "Mini-Pause", "Lob-Sandwich"), 2 aus KD ("Wie geht
es mir heute?", "Was ist ein guter Freund?"), 2 aus JD ("Meine Stärken sehen", "Nein sagen
können"). Bewusst nur alltagsnahe, nicht-krisenhafte Karten gewählt.

**Umgesetzt:**
- Neues PDF gebaut (`KLARTEXT_Schnupperpaket.pdf`, 18 Seiten: Cover + 8×2 Kartenseiten +
  Cross-Sell-Schlussseite), mit den bestehenden Karten-Renderern (`build_card_kd.py`,
  `build_card_jd.py`, `build_card_werkzeug.py`) und echten Kartenbildern/-texten aus den
  bestehenden Datenquellen — keine neuen Inhalte erfunden. Skript:
  `build_schnupperpaket.py` (im Repo-Root abgelegt, analog zu den bestehenden `build_pdf_*.py`).
- Neues Digistore24-Produkt "Schnupperpaket-PDF" (ID 723604) angelegt: Produkttyp Downloads,
  Zahlungsplan auf 0,00 € gesetzt (ein versehentlich mitangelegter 37-€-Plan wieder gelöscht),
  Datei im Download-Tresor hinterlegt (Anja hat den Datei-Upload selbst gemacht, da der
  automatische Upload über den Browser-Agent technisch nicht ging).
- `Schnupperpaket_Verkaufsseite.html` und `Schnupperpaket_Dankeseite.html` neu gebaut (Stil wie
  die 20 bestehenden Seiten), Dankeseite mit Cross-Sell-Hinweis auf alle 20 kostenpflichtigen
  Decks statt Flip-Card-Bonus (der Bonus gilt nur für echte Käufe, siehe Strang 89/90).
- Digistore24-Eigenschaften: Verkaufsseite/Dankeseite-URLs eingetragen.
- **Genehmigung beantragt:** Der übliche Weg (Testkauf über den Kaufen-Button vor Antragstellung)
  ging nicht, weil der öffentliche Checkout-Link vor Genehmigung generell "nicht verfügbar" zeigt —
  auch für eingeloggte Vendors. Anja hat das Produkt stattdessen direkt über den echten
  Kaufen-Button gekauft (0 €, kein Testkauf-Modus nötig) und selbst die Genehmigung beantragt.
  Status jetzt "Warte..." wie bei den anderen 20 Produkten.
- `KLARTEXT_Shop_Uebersicht.html`: neue Kachel ganz oben im Grid, grün hervorgehoben, Status
  "Kostenlos" statt "Jetzt erhältlich".

**Randnotiz:** Beim ersten Speichern der Verkaufsseite/Dankeseite-URLs gingen die Werte verloren
(vermutlich weil der Genehmigungs-Checkliste-Dialog den Eigenschaften-Save abgefangen hat) —
beim zweiten Versuch, getrennt von der Genehmigungs-Anfrage, hat es funktioniert. Beide Felder
vor dem Commit noch einmal geprüft und bestätigt korrekt gespeichert.

### Noch offen
- `klartext-shop`-Änderungen aus Strang 92 (2 neue Dateien + Shop-Übersicht-Kachel) noch nicht
  committet/gepusht.
- `KLARTEXT_Schnupperpaket.pdf` und `build_schnupperpaket.py` in `klartext-app` noch nicht
  committet/gepusht.
- Digistore24-Prüfergebnis fürs Schnupperpaket (wie bei den anderen 20) abwarten.

## Strang 93 (18.08.2026) — Google-Indexierung: sitemap.xml erstellt

**Auslöser:** Anja hat bei Google gesucht und "Die Domain klartext-mentoring.de ist derzeit nicht
als aktive Website mit spezifischem Inhalt verzeichnet" gefunden.

**Befund:** Die Seite selbst ist technisch in Ordnung — lädt normal, hat echten Inhalt, kein
"noindex"-Tag, robots.txt erlaubt Crawling ausdrücklich (`Content-Signal: search=yes`,
`Allow: /`). Eine `site:klartext-mentoring.de`-Suche liefert 0 Treffer — Google kennt die
Domain schlicht noch nicht. Ursache: keine `sitemap.xml` vorhanden (Aufruf lieferte bisher
die Startseite als Fallback zurück) und vermutlich keine Google Search Console eingerichtet,
über die man neue Seiten aktiv zur Indexierung anmelden kann. Bei einer neuen Domain ohne
eingehende Links ist das normal, kein technischer Fehler.

**Umgesetzt:**
- `klartext-shop/sitemap.xml` neu angelegt — 37 URLs (Startseite, Shop-Übersicht, App-Verkaufsseite,
  Brainy-Welt, Barometer-Erklärung, alle 26 Kartendeck-Verkaufsseiten inkl. Schnupperpaket, 6
  Rechts-Seiten). Dankeseiten und alte verwaiste Kurz-URL-Seiten (z. B. `adhs.html`, `kd.html`) bewusst
  **nicht** aufgenommen — Dankeseiten sind nur für Käufer:innen relevant, nicht für Google, und die
  Kurz-URL-Seiten sind nirgends mehr verlinkt (vermutlich alte Vorgänger-Seiten).
- `klartext-shop/robots.txt`: Zeile `Sitemap: https://klartext-mentoring.de/sitemap.xml` ergänzt,
  damit Google die Sitemap auch automatisch beim Crawlen findet.

**Noch offen (nächster Schritt, außerhalb meines Zugriffs):** Google Search Console ist der
eigentliche Hebel, damit die Indexierung schnell passiert (Tage statt Wochen) — dafür braucht Anja
ein Google-Konto und muss die Domain per DNS-Eintrag bei Cloudflare bestätigen. Das kann ich ihr
Schritt für Schritt anleiten bzw. per Bildschirm-Zusammenarbeit begleiten, sobald sie will.

**Update:** Erledigt. Anja hat die Search-Console-Property angelegt, die HTML-Bestätigungsdatei
(`googleb9a0d075d0a91e86.html`) heruntergeladen — ich habe sie in `klartext-shop` kopiert, gepusht
und live geprüft (Cloudflare-Deploy hat innerhalb weniger Minuten funktioniert). Inhaberschaft
bestätigt, Sitemap in der Search Console eingereicht. Domain ist jetzt offiziell bei Google
angemeldet, Indexierung läuft (dauert erfahrungsgemäß einige Tage).

## Strang 94 (18.08.2026) — Website-Rundum-Check auf Anjas Bitte

**Auslöser:** Anja fand beim Durchklicken mehrere mögliche Probleme und bat um eine
Gesamtprüfung: Navigationsstruktur, doppelte "Über mich"-Seiten inkl. einer "peinlichen" Note
"1,7" irgendwo, Insel-/Zonen-Set (Flip-Cards nicht auffindbar), Status "Vormerken" bei den
interaktiven Tools.

**Befund 1 — Navigation:** Kein Fehler, sondern Standard-Struktur (Startseite = Teaser, Klick auf
"Kartendecks entdecken" führt zum Katalog mit allen 5 Kategorien: Zielgruppen, Spezialdecks,
Institutionen, Interaktive Tools, Material-Pakete). Anja informiert, keine Änderung ohne
ausdrücklichen Wunsch vorgenommen.

**Befund 2 — Die "1,7":** Gefunden und behoben. Es war keine einzelne Stelle, sondern ein
Referenz-Badge ("Fortbildung Transitionspsychiatrie (1.7, Prof. Dr. Fegert, Uniklinikum Ulm)"),
das identisch auf **40 Dateien** stand (alle 24 aktuellen `*_Verkaufsseite.html` + 16 alte,
unverlinkte Kurz-URL-Duplikate wie `adhs.html`, `kd.html` usw.). Per `sed` in einem Rutsch über
alle Dateien entfernt — jetzt überall nur noch "Fortbildung Transitionspsychiatrie (Prof. Dr.
Fegert, Uniklinikum Ulm)" ohne Zahl. Nebenbefund (noch offen, s. u.): Auf
`SHOP_KLARTEXT_Ueber_Anja_Jolk.html` zeigt der Kontakt-Link den Text "anja.jolk@gmx.de" an,
verlinkt aber tatsächlich auf "info@klartext-mentoring.de" — Anja gefragt, welche Adresse richtig
ist, Antwort steht noch aus.

**Befund 3 — Insel-/Zonen-Set:** Alle Materialien (PDFs, Raummarkierungen, Booklets) und sogar die
Flip-Card-Version (Zugangscodes bereits in `klartext-karten/data/access.json` vorhanden) existieren
komplett fertig — nur die Digistore24-Anbindung fehlt. Aktuell nur Vorbestellung per E-Mail, kein
echter Checkout, keine Dankeseite (die den Flip-Card-Code ausliefern würde). Auf Anjas Wunsch:
Umbau zu echten Digistore24-Produkten. Bereits umgesetzt: IS/ZS zusätzlich im Abschnitt
"Interaktive Coaching-Tools" der Shop-Übersicht verlinkt (vorher nur unter "Material-Pakete" zu
finden), inklusive Hinweis auf die Flip-Card-Version im Kartentext. **Noch offen:** Bevor ich
echte Digistore24-Produkte mit Preis anlege, muss ich von Anja wissen (a) welchen konkreten Preis
sie je Deck fest einstellen möchte — Seite zeigt Spannen (IS: 18–22 €, ZS: 15–18 €), kein fixer
Preis bisher hinterlegt, und (b) welche der beiden Schule-PDF-Varianten für IS als Standard-
Verkaufsdatei dienen soll (`KLARTEXT_Insel-Set_Schule_INGRA.pdf` vs.
`KLARTEXT_Insel-Set_Schule_LK.pdf` — inhaltlich vermutlich fast gleich, aber unterschiedlich
zugeschnitten) sowie ob die "Raummarkierungen"-PDF (separate 8-Seiten-Datei) mit der Karten-PDF zu
einer einzigen Verkaufsdatei zusammengeführt werden soll (wie bei allen anderen 20 Decks üblich).

**Befund 4 — Interaktive Tools "Vormerken":** Kein Fehler, die 6 Tools sind schlicht noch nicht
gebaut. Anja fragte nach meiner Einschätzung, ob sie kostenlos angeboten werden sollten. Meine
Empfehlung (gegeben, noch keine Entscheidung/Umsetzung nötig): nicht alle 6 kostenlos machen,
bevor überhaupt eins existiert — das nimmt die Monetarisierungsmöglichkeit vorweg. Stattdessen
erst eins bauen, als bezahltes Produkt testen, und höchstens später eins davon als Lead-Magnet
kostenlos anbieten (analog zum Schnupperpaket-Modell aus Strang 92).

**Update:** Beide Anja-Antworten liegen vor. E-Mail auf beiden "Über mich"-Seiten (öffentlich +
intern) korrigiert auf "info@klartext-mentoring.de" (Text und Link stimmen jetzt überein). Für
IS: Anja möchte beide Schule-Varianten (INGRA + LK) anbieten, weil sie das Set auch auf
Lehrer-Material-Seiten vermarkten will — Preis 22 € (oberes Ende der Spanne, wie bei den anderen
Decks) unwidersprochen übernommen.

**Umgesetzt (vorbereitend, ohne Digistore24-Zugriff):**
- Neue Flip-Card-Zugangscodes generiert und in `access.json` (klartext-karten UND klartext-app/pwa)
  eingetragen: Insel-Set Schule = `h1qf9m`, Zonen-Set Schule = `qj874v` (die alten, nie
  ausgegebenen Hash-Platzhalter waren nicht mehr rekonstruierbar, da SHA-256 nicht umkehrbar ist —
  unkritisch, da noch nie an eine:n Käufer:in ausgegeben).
- `KLARTEXT_Insel-Set_Digital.zip` (Raummarkierungen Schule + Begleitkarten INGRA + Begleitkarten
  LK, 3 PDFs, 5,5 MB) und `KLARTEXT_Zonen-Set_Digital.zip` (Begleitkarten Schule + Token-Karten,
  2 PDFs, 4,2 MB) gebaut — beide unter dem 10-MB-Limit für automatischen Upload.
- `IS_Dankeseite.html` und `ZS_Dankeseite.html` neu gebaut, nach demselben Muster wie bei den
  anderen Decks (Flip-Card-Bonus-Box mit Zugangscode und Link zu `karten.klartext-mentoring.de`).

**Blockiert (zunächst):** Beim ersten Versuch war die Vendor-Session abgelaufen. Login übernehme
ich nicht selbst (Passwort-Eingabe ist mir grundsätzlich nicht erlaubt) — Anja hat sich neu
eingeloggt, danach ging es automatisch weiter.

**Update — beide Digistore24-Produkte vollständig angelegt:**
- **Insel-Set-PDF**, Produkt-ID **723777**, Produktname für Käufer "KLARTEXT-Insel-Set ·
  Raumzonen für Kinder (Schule und Lehrkräfte)", Preis **22,00 €** (oberes Ende der Spanne, wie
  besprochen), Verkaufsseite/Dankeseite eingetragen (`IS_Verkaufsseite.html` /
  `IS_Dankeseite.html`), Datei-Paket 138668 (`KLARTEXT_Insel-Set_Digital.zip`, 5 MB) verknüpft.
  Checkout: `https://www.checkout-ds24.com/product/723777`.
- **Zonen-Set-PDF**, Produkt-ID **723781**, Produktname für Käufer "KLARTEXT-Zonen-Set ·
  Raumzonen für Jugendliche", Preis **18,00 €**, Verkaufsseite/Dankeseite eingetragen
  (`ZS_Verkaufsseite.html` / `ZS_Dankeseite.html`), Datei-Paket 138669
  (`KLARTEXT_Zonen-Set_Digital.zip`, 4 MB) verknüpft. Checkout:
  `https://www.checkout-ds24.com/product/723781`.
- Bei beiden Produkten wieder der bekannte Zahlungsplan-Bug aufgetreten (automatisch ein
  zusätzlicher 37 €-Plan erzeugt) — jeweils gelöscht, nur der korrekte Plan (22 €/18 €) blieb aktiv.
- Datei-Upload (Filestack-Widget) erneut vom bekannten `file_upload`-Tool-Bug betroffen — beide
  ZIPs hat Anja manuell hochgeladen, ich habe sie danach jeweils vom "Ungenutzte Dateien"-Bereich
  ins Paket gezogen und gespeichert.
- `IS_Verkaufsseite.html` / `ZS_Verkaufsseite.html`: "Jetzt kaufen"-Button bei der Digital/PDF-
  Variante von der Vorbestell-E-Mail-Modal auf echten Checkout-Link umgestellt, Überschrift
  "IS/ZS vormerken" → "IS/ZS kaufen", Hinweisbox-Text an echten Kaufstatus angepasst. Bundle/
  Print/Träger-Lizenz-Kacheln bleiben bewusst bei "Vormerken" (nicht Teil dieses Rollouts).
- `KLARTEXT_Shop_Uebersicht.html`: Status für IS/ZS an beiden Stellen (Material-Pakete UND
  Interaktive Tools) von "Verfügbar zum Vormerken" auf "Jetzt erhältlich" aktualisiert.

**Noch offen — Genehmigung:** Wie bei allen anderen Produkten verlangt Digistore24 vor der
Genehmigungs-Anfrage einen bestätigten Testkauf über den echten "Kaufen"-Button. Da IS/ZS diesmal
echte Preise haben (22 €/18 €, nicht 0 € wie das Schnupperpaket), braucht es dafür die kostenlose
**TEST-PAY-Zahlungsart** (dieselbe, die Anja laut Strang-Notiz schon für GK-PDF genutzt hat) —
einen echten Kauf mit echtem Geld habe ich bewusst nicht ausgelöst, das ist mir ohnehin nicht
erlaubt. Anja muss für beide Produkte je einmal: über den Checkout-Link mit TEST-PAY „kaufen",
danach auf der Eigenschaften-Seite unter „Genehmigung durch Digistore24" → „Genehmigung jetzt
beantragen" wählen und speichern (Checkliste erscheint automatisch mit angehaktem Testkauf-Punkt).

### Noch offen
**Update:** Alle drei Repos committet/gepusht (`klartext-shop` caa944e, `klartext-app` 1501323,
`klartext-karten` 1e74268) — unterwegs kam zweimal die bekannte `.git/index.lock`-Blockade in
`klartext-app`/`klartext-karten` vor (vermutlich durch ein im Hintergrund laufendes Programm, das
kurz auf die Ordner zugreift), jeweils per manuellem `rm .git/index.lock` durch Anja behoben.
Zugangscodes sind jetzt live in der echten Flip-Card-App.

**Update — Genehmigung:** Anja hat für beide Produkte den TEST-PAY-Testkauf gemacht und die
Genehmigung beantragt. Status jetzt "Warte..." wie bei den anderen 20 Produkten + Schnupperpaket —
Strang 94 ist damit inhaltlich abgeschlossen, es fehlt nur noch Digistore24s eigene Prüfung.

### Noch offen
- Digistore24-Prüfergebnis für IS (723777) und ZS (723781) abwarten (wie bei allen anderen 22
  Produkten).
- Alle offenen Punkte aus Strang 91–93 (siehe oben) weiterhin gültig.
