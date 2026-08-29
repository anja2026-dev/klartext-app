# 📋 Premium-Prompt für Claude: Saubere Trennung der Berichte (OGS vs. Jugendliche)

## 1. Hintergrund & Problemstellung
Wir müssen eine gravierende logische und pädagogische Inkonsistenz in der App bereinigen. Aktuell vermischt der `KLARTEXT · Ressourcen-Bericht` Elemente für Jugendliche (wie Discord-Server, Handy-Sog, Werte-Poker und Berufsvorbereitung) mit der OGS-Übergabe (die reine Grundschul-Struktur ist). 

Diese Vermischung macht den Bericht in der Praxis unbrauchbar:
- Ein Grundschul-OGS-Kind hat keinen Bezug zu Discord-Superpowers oder Handy-Sog.
- Ein Jugendlicher in der Berufsvorbereitung ist nicht mehr im Offenen Ganztag (OGS).

## 2. Dein Arbeitsauftrag: Berichte radikal trennen

Bitte überarbeite die Berichts-Logik und die Benutzeroberfläche in den betroffenen Dateien (`KLARTEXT_Ressourcenbericht.html` / `Ressourcenbericht`-Module) und trenne sie in zwei eigenständige, saubere Dokumente auf:

### 📄 Bericht A: Der "KLARTEXT · OGS-Entwicklungsbericht" (Für Grundschüler)
- **Zielgruppe:** Lehrkräfte, OGS-Kräfte, Integrationskräfte und Eltern von Grundschulkindern.
- **Inhalte (Fokus auf Alltag & Übergänge):**
  - **Stimmungs-Barometer:** Visualisierung des Barometer-Verlaufs (Vormittag vs. Nachmittag / OGS-Übergabe).
  - **Kindgerechte Regulation:** Welche beruhigenden Zonen (Insel-Set wie Ruhe-Insel, Toberaum) oder physische Joker-Signale wurden genutzt?
  - **Pädagogische Notiz:** Freitextfeld für die Übergabe oder Beobachtungen der Begleitperson (z.B. "Heute im Freispiel gut reguliert").
- **Verbotene Elemente:** KEIN Handy-Sog, KEINE Discord-Superpowers, KEIN Werte-Poker, KEINE Berufsvorbereitung.

### 📄 Bericht B: Der "KLARTEXT · Ressourcen-Bericht Jugendliche" (Für Sekundarstufe I & II)
- **Zielgruppe:** Jugendliche, INGRAs, Beratungslehrkräfte und Eltern.
- **Inhalte (Fokus auf Reflexion & Zukunft):**
  - **Superpower-Profil:** Stärken aus dem Interessen-Check (Hobbys, Gaming, Stärken-Cluster).
  - **Werte-Poker-Ergebnisse:** Die gewählten Top-5-Werte des Jugendlichen.
  - **Selbstregulation im Schulalltag:** Genutzte Zonen aus dem Zonen-Set (Fokus-Zone, Rückzugs-Zone bei z.B. Handy-Sog).
- **Verbotene Elemente:** KEINE OGS-Nachmittags-Übergabe, keine kindlichen Begrifflichkeiten.

## 3. Umsetzung im Code
1. Erstelle in der HTML-Sicht des Ressourcenberichts eine einfache, klare Weiche am Anfang (z.B. zwei große Kacheln: "Bericht für Grundschule/OGS erstellen" und "Ressourcenbericht für Jugendliche erstellen").
2. Je nach Auswahl wird die entsprechende, sauber gefilterte PDF-Druckvorlage gerendert.
3. Passe die localStorage-Keys so an, dass sie sauber zugeordnet werden können.

Passe die Dateien direkt fehlerfrei in meinem Projektordner an!
