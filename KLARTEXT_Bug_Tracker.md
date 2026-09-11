# KLARTEXT-App · Bug-Tracker

Stand: 11.09.2026. Von Anja gemeldete Fundstellen, nach Modul sortiert. Severity ist mein Vorschlag zur Priorisierung (🔴 App-Funktion blockiert / 🟡 funktioniert, aber fehlerhaft oder eingeschränkt / ⚪ kosmetisch bzw. Verbesserungswunsch) — noch keine Fixes vorgenommen.

## Live-Status auf eduki.com (Stand: 11.09.2026, 32 veröffentlichte Materialien geprüft)

**Bestätigt live + Bug gemeldet:**
- 🟢live **Liegende Acht** ("Liegende Acht – Edu-Kinestetik-Übung...") — Bug: ⚪ Schnell-/Zeitlupe-Variante fehlt (kosmetisch)
- 🟢live **Zivilcourage-Trainer** ("Zivilcourage-Trainer gegen Mobbing (Sek I/II)" — die 46-Zeichen-Titelvariante wurde verwendet) — Bug: ⚪ nur vage "überarbeitungsbedürftig" gemeldet, konkrete Rückmeldung noch offen

- 🟢live **Toolbox-Berufseinstieg** (Datei `KLARTEXT_Spiel_ADHS_Toolbox.html`, intern betitelt "Toolbox für den Berufseinstieg" / "Toolbox für meinen Chef / Ausbilder") — bestätigt identisch mit dem live-Material "KLARTEXT · ADHS-Wunschzettel für den Berufseinstieg". Bug: ⚪ nur vage "überarbeiten" gemeldet, konkrete Rückmeldung noch offen

**Klargestellt — KEIN Live-Match:**
- **Was hilft mir gerade** (Datei `KLARTEXT_Spiel_WasHilftMir.html`) ist eine eigenständige Datei, NICHT identisch mit dem live gelisteten "Umgebungs-Anker für Jugendliche" (das ist `KLARTEXT_Spiel_UmgebungsAnker.html`, ein separates Tool). "Was hilft mir gerade" ist also weiterhin App-only, kein Marktplatz-Impact aktuell.

**Noch nicht live auf eduki (nur in der App, kein Marktplatz-Impact aktuell):**
Mutmachtier, Wochenplan & Mein Tag, Neue Schule, Schulalltag-Wörterbuch, Brainy-Wort-Würfel, Brainy-Zauberfächer, Reizfilter, Körperkompass, Mini-Fitness, OGS-Brücke, Unser Buch, Assoziationsblitz, Bewerbungsgespräch, Richtig oder Komisch, Bewerbungsgenerator, Werte-Poker, Interessen-Check, Perspektiv-Wechsler (Anzeigentext fertig, Upload steht noch aus), Online-Identity-Lab, Was hilft mir gerade, Übergangs-Timer, Teile-Mischer, Vokabel-Kino, Nacht-Sucher, Resilienz-Jojo.

→ **Priorität nach Live-Status:** 3 bestätigte live-Materialien mit gemeldeten Bugs (Liegende Acht, Zivilcourage-Trainer, Toolbox-Berufseinstieg) — alle davon aktuell nur ⚪/vage, kein 🔴 darunter. Der 🔴-Fall "Was hilft mir gerade" (Login-Umleitung) betrifft aktuell keine zahlenden Kund*innen, da App-only.

## Architektur-Baustelle: Firebase/Supabase-Migration (übergeordnet, kein Einzel-Bug)

Kontext (von Anja): App startete mit Firebase, wechselte während der Malteser-Testphase zu Supabase, ging wegen DSGVO-Problemen und der Entscheidung, die App nicht mehr als Ganzes anzubieten, wieder zurück zu Firebase (stattdessen einzelne HTML-Tools + Kartendecks, wie bei eduki/Shop). Migration ist derzeit unvollständig — Code-Bestand geprüft (11.09.2026):

- **14 Dateien nur mit Supabase** (kein Firebase-Bezug, potenziell noch nicht zurückmigriert): `KLARTEXT_Krankmeldung.html`, `KLARTEXT_Listen.html`, `KLARTEXT_Login.html`, `KLARTEXT_Login_Shop.html`, `KLARTEXT_Logout.html`, `KLARTEXT_Notizblock.html`, `KLARTEXT_Ressourcenbericht_Jobcoach.html`, `KLARTEXT_Tagesjournal.html`, `KLARTEXT_Teilnehmer_Protokoll.html`, `KLARTEXT_UnserBuch.html`, `KLARTEXT_Zeitkonto.html`, `TK_Fallmanagement.html`, `TK_Kinderzuordnung.html`, `TK_Landing.html`
- **14 Dateien nur mit Firebase:** `Admin_Backend.html`, `KLARTEXT_Feedback_INGRA.html`, `KLARTEXT_Feedback_TK.html`, `KLARTEXT_Forward_Read.html`, `KLARTEXT_Setup_Demo_Kinder.html`, `KLARTEXT_Vertretungsassistent_Architektur.html`, `KLARTEXT_Weiterleiten.html`, `TK_Uebergaben.html`, `chat.js`, `feedback.html`, `feedback.js`, `feedbackAdmin.html`, `feedbackAdmin.js`, `firebase.js`
- **8 Dateien mit BEIDEN Backends gleichzeitig** (mitten in der Migration, Risiko für Doppelaufwand/halbfertigen Zustand): `BAROMETER_KIND.html`, `DASHBOARD.html`, `DASHBOARD_Lite.html`, `KLARTEXT_Datenschutz.html`, `KLARTEXT_TK_Inbox.html`, `KLARTEXT_Weiterleitungen.html`, `Kinderverwaltung.html`, `TK_Vertretungsassistent.html`

**Konkreter Zusammenhang mit einem gemeldeten Bug:** `KLARTEXT_UnserBuch.html` speichert ausschließlich über Supabase (`supabase.from('kind_buch_eintraege')`, Zeilen 288-518). Das erklärt sehr wahrscheinlich den Bug "Unser Buch – Wechsel und Speicherung nicht möglich": Falls der Supabase-Zugang im Zuge der DSGVO-Entscheidung abgeschaltet/geändert wurde, scheitert das Speichern still, ohne Fehlermeldung. Zum Vergleich: **Nacht-Sucher** (anderer "speichert nicht"-Bug) hat KEINEN Firebase-/Supabase-Bezug — dessen Ursache liegt vermutlich rein im lokalen Speicher (anderes Problem).

→ Empfehlung: Vor Einzel-Fixes an den 14 reinen Supabase-Dateien und den 8 Misch-Dateien klären, welches Backend aktuell tatsächlich aktiv/erreichbar ist — sonst werden Symptome (wie bei Unser Buch) einzeln geflickt, während die Ursache (falsches/totes Backend) bestehen bleibt.

## Bereits verifiziert (Root Cause bekannt)

- 🔴 **Übergangs-Timer** – kein Ton/keine Vibration: `AudioContext` wird erst beim Timer-Ende erzeugt (in der setInterval-Callback), nicht beim Start-Klick. Browser sperren neu erzeugte AudioContexts ohne direkte Nutzer-Interaktion → Ton bleibt stumm ohne Fehlermeldung. Fix: AudioContext beim Start-Klick erzeugen/aufwecken. Vibration ist korrekt implementiert, funktioniert aber grundsätzlich nicht auf iPhone/Safari (Plattform-Einschränkung, kein Bug).
- 🟡 **Hilfewege-Planer vs. "Meine Verbündeten"** (AM_DL_Meine_Verbuendeten.html, Anti-Mobbing-Training): inhaltliche Überschneidung (beide "Wer hilft mir?"-Vertrauensnetz), aber unterschiedliches Format/Zielgruppe — "Meine Verbündeten" ist reines Ausdruck-Arbeitsblatt, mobbing-spezifisch; Hilfewege-Planer ist die neue interaktive App, allgemein. Vor eduki-Launch des Hilfewege-Planers klären, wie beide voneinander abgegrenzt kommuniziert werden.

## Grundschule

**Mutmachtier**
- ✅ **Gefixt (11.09.2026, Folgesession):** Die drei Schreibfelder waren bisher nur dekorative Linien ohne Funktion (kein input/textarea). Jetzt echte Formularfelder, die pro Tier gemeinsam mit dem Ausmalbild in localStorage gespeichert werden (mutmachtier_text_<tierId>). Zurücksetzen-Button löscht jetzt Text+Bild gemeinsam. Commit 928aec1.
- ✅ **Gefixt (11.09.2026, 3. Anlauf):** Erste beide Anläufe (Deko-Brainy, dann selbst gezeichnete SVG-Tiere) waren beide nicht professionell genug — von Anja zurecht bemängelt. 3. Anlauf: komplett umgebaut auf Anjas eigene Gemini-generierte Ausmalbilder (mt_loewe.jpg, mt_elefant.jpg, mt_drache.jpg, mt_schildkroete.jpg, mt_schmetterling.jpg, mt_fuchs.jpg, mt_eule.jpg, mt_baer.jpg, mt_adler.jpg, mt_brainy.jpg — alle aus Downloads ins Repo kopiert, auf 700px Breite optimiert). Antipp-Mechanik von SVG-Bereichen auf echten Fülleimer/Flood-Fill auf Canvas umgestellt (Klick in eine Fläche → Farbe läuft bis zur nächsten schwarzen Linie), funktioniert mit echten Rasterbildern statt Vektor-Regionen. Speicherung pro Tier als Canvas-Snapshot in localStorage (übersteht Tier-Wechsel und Reload, per Playwright verifiziert), Zurücksetzen-Button lädt Originalbild neu. **Igel fehlt** — kein Gemini-Bild dafür vorhanden, aktuell 10 statt 11 Tiere; Anja gefragt ob sie eins nachliefert oder Igel raus bleibt (Antwort steht aus).
- 🟡 Kein Zurück (Navigation)

**Wochenplan & Mein Tag**
- 🟡 Funktion "Aktivität löschen" fehlt

**Neue Schule**
- 🟡 Stundenplan-Simulator: Platzaufteilung nicht realistisch
- 🟡 Funktion Fächer hinzufügen/löschen fehlt
- 🔴 Fach Religion/Ethik lässt sich nicht einzeln aus dem Stundenplan entfernen (Kreuz/Löschen fehlt)

**Schulalltag-Wörterbuch**
- ✅ **Gefixt (11.09.2026, Folgesession):** Root Cause war kein falscher Sprachcode im Code (utterance.lang war korrekt gesetzt), sondern ein lautloser Browser-Fallback: fehlt auf dem Gerät eine installierte Stimme für die Zielsprache (z.B. Arabisch/Ukrainisch/Türkisch/Russisch), springt der Browser ohne Fehlermeldung auf die Standardstimme (meist Deutsch) und liest die Fremdsprache falsch aus. Fix sucht jetzt aktiv nach einer passenden installierten Stimme; ohne Treffer wird nicht gesprochen, sondern ein Hinweis eingeblendet statt falscher Aussprache. Behebt die falsche Sprache zuverlässig — ersetzt aber keine fehlende Stimme auf dem Gerät selbst (Betriebssystem-Einstellung). Commit 410efe4.
- 🟡 Sprachen inhaltlich gegenprüfen (Richtigkeit) — weiterhin offen, braucht muttersprachliche Prüfung (nicht durch Code lösbar)

**Brainy-Wort-Würfel**
- ✅ **Gefixt (11.09.2026, Folgesession):** Druckvorlage (KLARTEXT_Spiel_Wortwuerfel_Basteln.html) hatte 4 von 7 Klebelaschen falsch positioniert — die seitlichen Laschen über/unter SIGNALE und NOMEN saßen eine volle Zeilenhöhe (5,5cm) zu weit oben/unten am Blattrand, komplett losgelöst vom Netz statt direkt an der Feldkante. Jetzt korrekt platziert. Commit 72da2d1.
- ✅ **Geklärt:** Wortkarten & Aktions-Set (KLARTEXT_Spiel_Wortwuerfel_Karten.html) ist keine Verwechslung, sondern ein eigenständiges, separates Druckprodukt (18 Karten: Aktions- + Wortkarten) zusätzlich zur Bastelvorlage — keine Änderung nötig.

**Brainy-Zauberfächer**
- ⚪ Rechtschreibfehler: "liegende AchtER" (Gelb), "der Affe" Knie DICH hin (Gelb)
- 🟡 Zurücktaste fehlt

**Reizfilter**
- 🟡 Muss unter "Jugendliche" einsortiert werden (falsche Rollen-/Altersgruppen-Zuordnung)

**Liegende Acht**
- ⚪ Soll in Schnell- und Zeitlupe-Variante angeboten werden

**Körperkompass**
- ⚪ Als generell überarbeitungsbedürftig gemeldet ("doof") — konkretere Rückmeldung nötig, was genau stört

**Mini-Fitness**
- 🟡 Start-, Pause-, Ende-Knopf fehlt/fehlerhaft

**OGS-Brücke**
- 🟡 "Jugendlicher" muss raus (falsche Zielgruppen-Option)
- ⚪ Brainy statt Smileys verwenden

**Unser Buch**
- ⚠️ **Umklassifiziert (11.09.2026): kein Einzelnutzer-Bug, sondern Träger-Feature ohne Rollen-Schutz.** Code fragt aktiv die `ingra`-Tabelle (Supabase) nach der eingeloggten Person ab und lädt zugeordnete Kinder inkl. Vertretungslogik (`zuteilungen`, `vertretKinder`) — dieselbe Organisations-Infrastruktur wie Kinderverwaltung/TK-Inbox, NICHT das anonyme Einzelnutzer-Muster. Eigentlicher Fehler: die Kachel in KLARTEXT_Spiele.html hat kein `data-roles`-Attribut, ist also für JEDE Rolle sichtbar/nutzbar, obwohl es nur mit echtem INGRA-Account + zugewiesenen Kindern in der (noch nicht buchbaren) Träger-Datenbank funktionieren kann — für alle anderen läuft die Abfrage ins Leere, Speichern scheitert still. Entscheidung von Anja offen: (a) Kachel auf Träger-Rolle beschränken (`data-roles="tk admin"` o.ä.), oder (b) falls als Einzelnutzer-Tool gedacht: komplett neu auf Firebase/localStorage bauen. Kein dringender Fix nötig, solange das Träger-Szenario nicht live/gebucht ist.

**Assoziationsblitz**
- 🟡 Erkennung falscher Wörter, Rechtschreibung & Buchstabenzugehörigkeit fehlerhaft/fehlt

## Jugendliche

**Bewerbungsgespräch**
- ⚪ Drucken der Startseite ist sinnlos (falscher Druckinhalt)

**Richtig oder Komisch**
- ✅ **Gefixt (11.09.2026, Folgesession):** Root Cause für "Antworten teilweise inhaltlich falsch" war nicht die Klassifizierung der 12 Situationen (die war korrekt), sondern die Feedback-Logik: Text/Farbe richteten sich bisher nur nach der tatsächlichen Einordnung, nicht nach der Antwort der Person — z.B. "Genau!" auch bei falscher Antwort. Jetzt 4 Feedback-Varianten je nach Nutzer-Antwort × echte Einordnung. Gleichzeitig den Timer-Bug mitgefixt: automatischer Kartenwechsel nach 1,5s ersetzt durch manuellen "Weiter"-Button. Commit 58e6584.

**Bewerbungsgenerator**
- ✅ **Gefixt (11.09.2026, Folgesession):** Root Cause: der Zurück-Button war fest auf KLARTEXT_Downloads.html verdrahtet. Das Tool wird aber auch von Spiele-Übersicht, Interessen-Check und Skill-Matrix aus verlinkt — von dort kam man beim Zurück-Klick an der falschen Stelle an statt dort, wo man hergekommen ist. Jetzt echte Browser-Historie (history.back()) mit Fallback auf Downloads. Commit 61651af.

**Werte-Poker**
- ⚪ Beschreibung ändern: Klicken statt Ziehen (Interaktionsart)
- ⚪ Druckvorlagen (Karten) optisch aufhübschen

**Interessen-Check**
- ⚪ Drucken statt Kopieren (Funktion prüfen)

**Perspektiv-Wechsler**
- 🟡 Hervorhebung als Empfehlung nur bei "Überfordert" und "Alarmiert" (fehlt bei anderen Zuständen?)

**Toolbox-Berufseinstieg** — ⚪ überarbeiten (generell gemeldet)
**Online-Identity-Lab** — ⚪ überarbeiten (generell gemeldet)

**Was hilft mir gerade**
- 🔴 Leitet komplett zum Login um — **Root Cause gefunden:** betrifft nur die Vorschlags-Links INNERHALB des Tools (Perspektiv-Wechsler, Reizfilter, Interessen-Check, Bewerbungsgespräch), nicht den Einstieg über die Kachel in "Interaktive Tools" selbst. Alle Vorschlags-Links öffnen mit `target="_blank"` in einem neuen Tab (Code-Zeile 276); der Login-Status wird dorthin nicht zuverlässig übernommen (v. a. Safari), zusätzlich läuft jede Zieladresse noch durch eine automatische Cloudflare-Weiterleitung (.html → ohne Endung), was die Übergabe zusätzlich stören kann. Verschärfend: 2 der 4 Ziel-Tools (Interessen-Check, Bewerbungsgespräch) haben im eigenen Code gar keine Gast-Zugriffs-Ausnahme; die anderen 2 (Perspektiv-Wechsler, Reizfilter) unterstützen zwar `?guest=true`, aber der Link aus "Was hilft mir gerade" nutzt diesen Parameter nicht. "Was tun bei…?" funktioniert nur deshalb, weil diese eine Datei gar keine Login-Prüfung eingebaut hat (eigener Punkt, siehe unten). Fix-Ansatz (noch nicht umgesetzt): Vorschlags-Links ohne `target="_blank"` im selben Tab öffnen + fehlende Gast-Ausnahme bei Interessen-Check/Bewerbungsgespräch ergänzen.
- 🟡 Zurück-Navigation bei den Karten kaputt — Folgefehler desselben Root Cause: da die Vorschlags-Links in neuem Tab öffnen, gibt es dort keine Verlaufs-Historie zurück zu "Was hilft mir gerade"; der Zurück-Button landet stattdessen auf der kompletten Kartendeck-Übersicht. Löst sich mit demselben Fix.
- 🟡 Ressourcenbericht-Link zeigt fälschlich auch OGS-Option — "Was hilft mir gerade" (Jugendliche-Tool) verlinkt auf `KLARTEXT_Ressourcenbericht.html`, das ist aber eine allgemeine Auswahlseite ("Ressourcen-Bericht wählen") mit zwei Kacheln: OGS-Entwicklungsbericht (Grundschule) UND Ressourcenbericht für Jugendliche. Es gibt bereits eine passende, direkte Datei `KLARTEXT_Ressourcenbericht_Jugendliche.html` — der Link sollte dorthin zeigen statt auf die Auswahlseite, dann verschwindet die unpassende OGS-Option.

**"Was tun bei…?" — ohne Login-Schutz (eigener Punkt, kein von Anja gemeldeter Bug, aber auffällig):**
- ⚪/🟡 Diese Datei hat als einzige der genannten Jugendliche-Tools GAR KEINE Login-Prüfung — frei zugänglich für jeden mit dem Link, ohne Account. Zur Konsistenz mit den anderen Tools prüfen, ob das beabsichtigt ist.

**Zivilcourage-Trainer**
- ⚪ Als generell überarbeitungsbedürftig gemeldet ("doof") — konkretere Rückmeldung nötig

**Übergangs-Timer** → siehe oben, bereits verifiziert

**Teile-Mischer**
- 🟡 Keine Auswertung am Ende

**Vokabel-Kino**
- ⚪ Beispiele in den Sprachen und Ideen für Brückenwörter ausbauen

**Nacht-Sucher**
- ✅ **Gefixt (11.09.2026):** Playwright-Test bestätigt, dass die eigentliche Speicherlogik (localStorage, Abend→Morgen→Tagebuch) korrekt funktioniert und Daten über Reloads hinweg erhalten bleiben — der Code selbst war nicht kaputt. Wahrscheinlichste reale Ursache des gemeldeten "speichert nicht": ein eingebetteter Browser (z. B. WhatsApp/Mail-Vorschau) oder private Browser-Einstellungen, in denen `localStorage.setItem` entweder wirft oder den Wert wieder verwirft, ohne dass die App das bisher bemerkt hat. Fix: `datenSchreiben()` prüft jetzt per Read-back, ob der Wert wirklich gespeichert wurde, und zeigt bei Fehlschlag eine sichtbare Warnung ("⚠️ Deine Antworten werden gerade NICHT gespeichert...") statt still zu scheitern; zusätzlicher Storage-Check direkt beim Laden der Seite. Falls das Problem weiterhin auftritt, bitte beim nächsten Mal notieren: welches Gerät/Browser, und ob der Link aus einer anderen App (WhatsApp/Notizen) heraus geöffnet wurde — das würde die Ursache endgültig bestätigen.

**Resilienz-Jojo**
- 🟡 Im Frei-Modus markiert sich die Seite (Text-Selektion statt Drag — CSS `user-select` fehlt vermutlich)

## Download-Bereich

- 🔴 Komplett überprüfen (von Anja als eigener dringender Punkt markiert) — **erste systematische Prüfung durchgeführt (alle Links gegen vorhandene Dateien geprüft):**
  - ✅ `KLARTEXT_Downloads.html` (regulärer Download-Bereich): alle Links funktionieren, keine toten Verweise.
  - 🔴 `KLARTEXT_Downloads_Premium.html`: 15 tote Links, vermutlich Folge einer Umbenennungs-Aktion, die auf dieser Seite nicht nachgezogen wurde:
    - `FK-01_Meltdown.html` … `FK-05_Selbstverletzung.html` → jetzt vermutlich `FK-01.html` … `FK-05.html`
    - `KD-ADHS.html` → vermutlich `M2-08_ADHS.html`
    - `KD-GL-01_Grundlagen.html` / `KD-GL-02_Praxis.html` → vermutlich `M2-40_Gehoerlosigkeit_Grundlagen.html` / `M2-41_Gehoerlosigkeit_Praxis.html`
    - `KD-SB-01_Grundlagen.html` / `KD-SB-02_Praxis.html` → vermutlich `M2-38_Sehbehinderung_Blindheit_Grundlagen.html` / `M2-39_Sehbehinderung_Praxis.html`
    - `KD-SM-01_Erkennen.html` / `-02_Handeln.html` / `-03_Schutz.html` → vermutlich `M2-35_Sexueller_Missbrauch_Grundlagen.html` / `M2-36_..._Handeln.html` / `M2-37_..._Schutz_INGRA.html`
    - `KLARTEXT_Urlaubsantrag.html` → unklar: `KLARTEXT_Urlaubsantrag_INGRA.html` oder `KLARTEXT_Urlaubsplan.html`? Anja muss entscheiden.
    - `TK_Rollenlogik.html` → kein ähnlicher Dateiname gefunden — evtl. wirklich fehlender/nie gebauter Inhalt statt nur umbenannt.
  - ⚪ Zusatzfund: Keine andere Datei in der App verlinkt aktuell auf `KLARTEXT_Downloads_Premium.html` — die Seite ist aus der App-Navigation ausgehängt (nur per direktem Aufruf erreichbar). Klären: soll sie wieder eingebunden oder ist sie ein Überbleibsel?

---

## Nächster Schritt

Anja entscheidet die Reihenfolge/Priorität für die Bearbeitung. Vorschlag: zuerst die 🔴-Punkte (App-Funktion blockiert oder Kernfunktion kaputt), danach 🟡, zuletzt ⚪.
