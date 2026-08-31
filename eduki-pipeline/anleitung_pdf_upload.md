# Schritt-für-Schritt: PDFs erstellen & bei eduki hochladen

## Wichtiger Hinweis vorab

Beim Einbau der QR-Codes ist mir aufgefallen, dass **3 Dateien einen Login-Schutz hatten**, der den QR-Code-Zugriff komplett blockiert hätte: `KLARTEXT_Spiel_OnlineIdentityLab.html`, `LK_DL_Beobachtungsbogen.html` und `LK_DL_Krisenprotokoll.html`. Wer eine gedruckte PDF kauft und den QR-Code scannt, wäre ohne Login sofort auf die Login-Seite umgeleitet worden. Ich habe dort denselben Gast-Zugang-Mechanismus ergänzt, den `BAROMETER_KIND.html` bereits nutzt (`?guest=true` in der URL) – analog zur bereits bestehenden Konvention in deiner App. Bei den anderen 6 Dateien war kein Login-Schutz vorhanden, daher war dort nichts zu reparieren.

Alle 9 Dateien liegen jetzt aktualisiert in deinem Repo-Ordner `klartext-app`.

---

## A) Freebie: ADHS-Wunschzettel (Datei bereits korrekt, keine Änderung nötig)

1. Öffne `KLARTEXT_Freebie_Wunschzettel.html` im Browser (Doppelklick oder per Live-Server).
2. Drucken → Ziel „Als PDF speichern" → Speichern unter `KLARTEXT_Freebie_Wunschzettel.pdf`.
3. Bei eduki: bestehendes Freebie-Angebot öffnen → alte PDF-Datei entfernen → neue PDF hochladen → Preis bleibt 0,00 €.

## B) Die 8 aktualisierten Dateien (mit neu eingebautem QR-Code)

Für jede der folgenden Dateien gilt derselbe Ablauf:

1. Datei im Browser öffnen (Chrome oder Safari empfohlen für sauberen PDF-Export).
2. Kurz warten (ca. 1 Sekunde), bis der QR-Code sichtbar ist – er wird per JavaScript nachgeladen.
3. Drucken (Cmd+P) → **Ziel: „Als PDF sichern"**.
4. Bei den Druckoptionen jeweils beachten (siehe Tabelle unten).
5. PDF unter dem eduki-Dateinamen speichern (siehe Tabelle).
6. Bei eduki: neues Produkt anlegen, Titel/Beschreibung/Tags aus `eduki_anzeigentexte.md` einfügen, Preis setzen, PDF hochladen, Kategorie zuordnen.

| # | Datei | Druckeinstellung | PDF-Dateiname | Preis |
|---|---|---|---|---|
| 2 | `LK_DL_Perspektiv_Wechsler_Ticket.html` | **Beidseitig drucken** (2 Seiten = Vorder-/Rückseite) | `LK_DL_Perspektiv_Wechsler_Ticket.pdf` | 2,90 € |
| 3 | `KLARTEXT_Spiel_OnlineIdentityLab.html` | Erst auf „🖨 Drucken/Ergebnis erzeugen"-Button in der Seite klicken, dann druckt sich automatisch die Ergebnisansicht mit QR-Code | `KLARTEXT_Spiel_OnlineIdentityLab.pdf` | 2,90 € |
| 4 | `LK_DL_Therapeuten_Ticket.html` | Einfacher einseitiger Druck (Ticket-Hälften liegen bereits nebeneinander) | `LK_DL_Therapeuten_Ticket.pdf` | 1,90 € |
| 5 | `LK_DL_Nachteilsausgleich.html` | Standard A4 Hochformat | `LK_DL_Nachteilsausgleich.pdf` | 2,50 € |
| 6 | `LK_DL_OGS_Uebergabe.html` | Standard (4 Karten sind bereits auf einer A4-Seite angeordnet) | `LK_DL_OGS_Uebergabe.pdf` | 1,90 € |
| 7 | `LK_DL_Reizfilter_Audit.html` | Standard A4 Hochformat | `LK_DL_Reizfilter_Audit.pdf` | 2,50 € |
| 8a | `LK_DL_Beobachtungsbogen.html` | Standard A4 Hochformat | `LK_DL_Beobachtungsbogen.pdf` | Teil des Kombi-Sets |
| 8b | `LK_DL_Krisenprotokoll.html` | Standard A4 Hochformat | `LK_DL_Krisenprotokoll.pdf` | Teil des Kombi-Sets |
| 9 | `M8-DL_Selbstfuersorge-Bingo.html` | Standard A4 Hochformat | `M8-DL_Selbstfuersorge-Bingo.pdf` | 0,00 € |

**Bei 8a/8b:** Beide PDFs beim Kombi-Set-Produkt gemeinsam hochladen (eduki erlaubt mehrere Dateien pro Angebot), Preis 1,90–2,50 € je nach gewählter Preisstufe.

## C) QR-Codes vor dem Hochladen kurz testen

Bevor du live gehst: Scanne jeden QR-Code einmal selbst mit dem Handy und prüfe, ob die Zielseite ohne Login-Aufforderung lädt. Ich habe das bereits technisch verifiziert (Rendering + Login-Bypass geprüft), eine kurze eigene Kontrolle schadet aber nie – besonders bei den drei zuvor login-geschützten Dateien.

## D) eduki-Produktanlage – Checkliste pro Angebot

- [ ] Titel aus `eduki_anzeigentexte.md` einfügen
- [ ] Beschreibung einfügen (Formatierung mit Absätzen/Fettung wo eduki das zulässt)
- [ ] Tags einfügen (eduki erlaubt meist 8–12 Schlagworte)
- [ ] Kategorie wählen: Elternarbeit / Regeln & Rituale / Inklusion / Spiele & Rätsel (siehe Übersichtstabelle)
- [ ] Klassenstufe/Schulform angeben (Sek I/II bzw. Grundschule je nach Produkt)
- [ ] Preis setzen
- [ ] Vorschaubild hochladen (Screenshot der ersten PDF-Seite, evtl. mit Wasserzeichen „Vorschau")
- [ ] PDF hochladen
- [ ] Veröffentlichen
