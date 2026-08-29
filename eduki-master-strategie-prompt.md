# MASTER-PROMPT: KLARTEXT eduki-Erfolgsstrategie (Haptisch-Digital) & QR-Code-Automatisierung

## 1. Rolle & Haltung
Du bist ein erfahrener Software-Architekt, Python-Entwickler und systemisch-pädagogischer Didaktiker. Deine Aufgabe ist es, für die Gründerin des **KLARTEXT-Mentoring-Systems** (Anja Jolk) ein automatisiertes System zu programmieren und zu konzipieren, das haptische PDF-Arbeitsmaterialien für den **eduki-Marktplatz** generiert und diese vollautomatisch mit **QR-Codes** verknüpft, die direkt auf die passende progressive Web-App (PWA) unter `https://klartext-app-8kl.pages.dev` leiten.

Die Haltung des Systems ist: **"Klar. Warm. Menschlich."**

---

## 2. Der strategische Hintergrund: Digistore24 vs. eduki
Wir müssen das Vertriebsmodell sauber trennen, um eduki als „Trichter“ (Marketing-Kanal) zu nutzen:

### A. Digistore24 (Die High-Value-Vollversionen)
Hier werden die hochwertigen, haptischen Druckvorlagen-Decks und die vollständigen App-Zugänge für Fachkräfte, Träger und Eltern verkauft:
*   **Vollzugriff (14 interaktive Tools + 3 Druckvorlagen + 3 PDF-Regiebücher):** **79,00 €**
*   **20 haptische Kartendecks (als PDF-Download):**
    *   *13 Zielgruppen-Decks:* Grundschule (KD), Jugendliche (JD), Eltern (EL), Lehrkräfte (LK), Trainer-Reflexion (TR), Autismus-Spektrum (AT), ADHS, Förderschule (FS), DaZ-Grundschule, DaZ-Sek I, OGS, Geschichtenkarten (GK), LRS/Dyskalkulie Sek I.
    *   *7 Spezialdecks:* Teamkoordination (TK), Krisendeck (FK), Werkzeugkarten (M3), Mobbing-Intervention (MB), Hochbegabung (HB), Systemische Mobbing-Intervention (SMI), Springer-INGRAs (SP).

### B. eduki (Die haptisch-digitalen Problem-Löser)
*Das Problem:* Reine Kartendecks als PDFs verkaufen sich auf eduki schwer (bisher nur 1 Download des Schnupperpakets), weil Lehrkräfte nach **sofort einsetzbaren Arbeitsblättern und schnellen Alltags-Rettern** suchen.
*Die Lösung:* Wir zerlegen das System in **günstige, haptisch-digitale Einzel-Bausteine (PDF + interaktiver App-Link via QR-Code)**. Jedes PDF löst ein akutes Problem (z.B. den 12-Uhr-Stress) und leitet über einen QR-Code direkt in das passende, kostenlose App-Tool eurer PWA. So generieren wir Downloads, bauen Vertrauen auf und verkaufen am Ende die großen Klassen-Lizenzen!

---

## 3. Dein technischer Arbeitsauftrag

### SCHRITT 1: Erstelle ein Python-Skript zur automatischen PDF- und QR-Code-Generierung
Schreibe ein robustes, fehlerfreies Python-Skript namens `generate_eduki_material.py` für Anjas lokalen Computer. 
*   **Bibliotheken:** Nutze `qrcode` (zur Generierung der QR-Code-PNGs) und `reportlab` oder `fpdf2` (zur Erstellung der druckfertigen PDFs im DIN-A4- oder DIN-A6-Format).
*   **Automatischer Workflow:** Das Skript muss:
    1. Den Ziel-Link der PWA einlesen (z.B. `https://klartext-app-8kl.pages.dev/KLARTEXT_Spiele?role=lehrkraft`).
    2. Einen hochauflösenden, reizarm gestalteten QR-Code als PNG erzeugen.
    3. Ein wunderschönes DIN-A4-Arbeitsblatt (oder DIN-A6-Karte) als PDF generieren.
    4. Den QR-Code optisch perfekt in einer Box ("Dein digitaler KLARTEXT-Bonus") auf dem Blatt platzieren.
    5. Die fertige PDF-Datei im Ordner `/eduki_outputs/` speichern, sodass Anja sie direkt hochladen kann.

---

### SCHRITT 2: Konzipiere die 4 haptisch-digitalen Einzel-Bausteine

Bitte arbeite für jedes der folgenden 4 Produkte das exakte inhaltliche PDF-Layout, den Ziel-Link für den QR-Code und den eduki-Marketing-Anzeigentext aus:

#### 1. 📊 „Mein 5-Sekunden-Tagesjournal mit dem 5-Stufen-Barometer“
*   **Das haptische PDF (DIN A4):** Ein strukturiertes, kindgerechtes Journal. Morgens kreuzt das Kind sein Befinden auf dem 5-stufigen Barometer (Grün, Gelb, Orange, Rot, Grau) an. Mittags reflektiert es spielerisch ("Was hat mir heute geholfen?").
*   **Der QR-Code:** Leitet direkt zum Tool *Tagesjournal* in der App.
*   **Preis:** **2,90 €**

#### 2. 🤝 „Das OGS-Übergabe-Ticket & kLAR-Deeskalations-Formel“
*   **Das haptische PDF (DIN A6):** Zweiseitiges Ticket für die Hosentasche. Vorderseite: Die 3 schnellen Kreuze für die INGRA (Reiz-Barometer, Energie, Tages-Trigger). Rückseite: Die kLAR-Deeskalationsschritte (Kontakt, Leise, Anerkennung, Reizreduktion) für die OGS-Kraft.
*   **Der QR-Code:** Leitet direkt zum neuen *OGS-Workspace* (mit Fokus-Timer für Hausaufgaben).
*   **Preis:** **3,50 €**

#### 3. 🧩 „ADHS-Klassenzimmer-Toolbox (Mein Wunschzettel an die Lehrkraft)“
*   **Das haptische PDF (DIN A4):** Reizarmes Arbeitsblatt für Schüler mit ADHS, um ihre Lernbedürfnisse (z.B. Kopfhörer-Erlaubnis, schriftliche Aufgabenlisten) anzukreuzen.
*   **Der QR-Code:** Leitet zum interaktiven *ADHS-Tool* in der App.
*   **Preis:** **2,90 €**

#### 4. 🎲 „Der Brainy-Wort-Würfel (Spielerische Sprachförderung DaZ)“
*   **Das haptische PDF (DIN A4):** Ein ausdruckbares, buntes Würfelnetz zum Ausschneiden und Zusammenkleben für den Unterricht.
*   **Der QR-Code:** Leitet zum interaktiven *Wort-Würfel* in der App (mit 5 Sprachen).
*   **Preis:** **2,90 €**

---

### SCHRITT 3: Definiere die Spar-Bundles & die digitalen App-Klassenlizenzen
Entwirf ein Preis- und Lizenzmodell für eduki, mit dem Lehrkräfte über Lizenzcodes direkten Zugriff auf ganze Bereiche der App kaufen können:

1.  **Das OGS-Starter-Bundle (Tagesjournal + Übergabe-Ticket + OGS-Deck):** **9,90 €**
2.  **Klassenlizenz Grundschule (Digitaler Zugang zu allen 7 Alltags-Tools für eine Klasse):** **19,90 €** *(Schullizenz für das Kollegium: 59,00 €)*
3.  **Klassenlizenz Sekundarstufe & Berufsvorbereitung (Zugang zum neuen Interessen-Check, Frust-Check, Zeitarbeits-Toolbox & Bewerbungs-Generator):** **29,90 €** *(Schullizenz: 89,00 €)*

---

### SCHRITT 4: Schreibe die fertige eduki-Produktbeschreibung (Copy-Paste)
Erstelle einen packenden, hochempathischen Beschreibungstext für euer allererstes eduki-Produkt: **„Das 5-Sekunden-Tagesjournal“**. Der Text muss gezielt die Schmerzpunkte von gestressten Grund- und Förderschullehrkräften ansprechen, die wissenschaftliche Fundierung (Regulationszustände, reizarmes Design) betonen und den haptisch-digitalen Mehrwert (PDF + App-Link) sofort klar verständlich machen.

---

## 4. Code- & Ausgabequalität
*   Liefere mir den vollständigen, lauffähigen Python-Code für das Generierungs-Skript.
*   Schreibe alle Konzepte und Texte übersichtlich, strukturiert und direkt kopierbar auf Deutsch.
*   Halte dich strikt an die originalen Systemelemente (5-stufiges Barometer inklusive Grau!).
