# KLARTEXT – Merkliste
Stand: 11.08.2026 (Strang 67 ergänzt)

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
