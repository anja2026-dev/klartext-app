# KLARTEXT · Plattform- und Preisstrategie

Stand: 07.08.2026, erstellt nach Gewerbeanmeldung. Grundlage: bestehende Verkaufsseiten in `klartext-shop`, Preisrecherche (Task #218) und aktuelle Plattform-Recherche (Etsy, Pinterest, eduki).

## 1. Angebots-Inventar: Was gibt es aktuell zu verkaufen?

**22 fertige Produkte** (Kartendecks + Sets), jetzt **alle 22 mit Verkaufsseite** (Stand 07.08.2026).

**Korrektur (07.08.2026):** Die drei zuvor fehlenden Verkaufsseiten waren mit falschen Themenbeschreibungen in diesem Dokument gelistet — vermutlich eine Verwechslung mit anderen Deck-Ideen. Gegen den echten Code (`pwa/data/*.json`) geprüft, korrekter Inhalt:

| Kürzel | Produkt (tatsächlicher Inhalt) | Karten | Verkaufsseite? |
|---|---|---|---|
| SMI | Systemische Mobbing-Intervention (nicht "Sinnesbeeinträchtigungen") | 10 | ✅ `SMI_Verkaufsseite.html` |
| LRS | LRS/Dyskalkulie Sek I (Beschreibung war korrekt) | 10 | ✅ `LRS_Verkaufsseite.html` |
| SP | Springer-INGRAs (nicht "Selektiver Mutismus/Sprache") | 7 | ✅ `SP_Verkaufsseite.html` |

Alle drei Seiten neu gebaut (Vorschaubilder aus den echten Kartendaten gerendert, Quellen gegen den tatsächlichen Karteninhalt geprüft — beim SP-Deck ehrlich als überwiegend praxisbasiert statt wissenschaftlich referenziert ausgewiesen, da es dafür keine 1:1-Forschung gibt). In `KLARTEXT_Shop_Uebersicht.html` verlinkt: SMI/SP unter "Handlungskarten & Spezialdecks", LRS unter "Kartendecks nach Zielgruppe" (konsistent mit der bestehenden Kategorisierung in `pwa/data/decks.json`). Hero-Zahlen der Übersichtsseite und `index.html` von 19 auf 22 Kartendecks korrigiert.

Die restlichen 19 Produkte (JD, KD, EL, LK, TR, AT, ADHS, FS, DaZ-GS, DaZ-Sek-I, OGS, Geschichtenkarten, TK, Krisendeck, Werkzeugkarten, Mobbing, Hochbegabung, Insel-Set, Zonen-Set) sind fertig und auf `klartext-mentoring.de` gelistet — aktuell aber nur mit "Vormerken per Mail" statt echtem Checkout, weil bisher kein Gewerbe vorlag. Das ist jetzt der nächste logische Schritt (siehe #213 in der Aufgabenliste).

## 2. Plattformvergleich

### Pinterest — kostenlos, kein Marktplatz
Pinterest ist **kein Verkaufsort**, sondern ein Trafficbringer. Ein Business-Konto ist komplett kostenlos, es fallen keine Gebühren an — außer du schaltest bezahlte Werbung, was optional ist. Pinterest verkauft nicht selbst, sondern verlinkt zu deinem eigenen Shop (`klartext-mentoring.de`). Für dich heißt das: null Kosten, aber auch kein eigenes Käufer-Publikum wie bei Etsy — du musst die Leute erst über Pins auf deine Seite holen. Gut geeignet, um z. B. das Barometer-Karussell oder einzelne Karten-Vorschauen als Pins zu posten und Leute zur eigentlichen Verkaufsseite zu leiten.

### Etsy — eigener Marktplatz, mittlere Gebühren
Etsy ist ein echter Marktplatz mit eigenem Käuferpublikum, passend sowohl für PDF-Downloads als auch für Print-on-Demand-Kartendecks (Etsy hat POD-Integrationen). Gebührenstruktur:
- 0,20 USD Einstellgebühr pro Listing
- 6,5 % Transaktionsgebühr auf Artikelpreis + Versand
- 4 % + 0,30 € Zahlungsbearbeitungsgebühr (Deutschland)
- Gesamtbelastung: **ca. 10,5–17 %** des Verkaufspreises, ohne bezahlte Anzeigen

Etsy setzt eine Gewerbeanmeldung voraus — die du jetzt hast, also kein Hindernis mehr. Startkosten liegen laut Recherche meist unter 100 € im ersten Jahr (Gewerbeanmeldung, IHK, Etsy-Gebühren zusammen).

### eduki (ehemals lehrermarktplatz.de) — Lehrkräfte-Marktplatz, hohe Anfangsgebühr
Das ist vermutlich das, was du mit "lehreronline" meintest — `lehrer-online.de` selbst ist keine Verkaufsplattform (redaktionelles Portal), sondern **eduki** ist der tatsächliche deutsche Marktplatz für Unterrichtsmaterial (2016 als lehrermarktplatz.de gestartet, 2023 zu eduki umbenannt, gleiche Firma). Zielgruppe trifft ziemlich genau auf deine LK-, OGS-, DaZ- und Werkzeugkarten-Decks.

Provisionsmodell (gestaffelt nach Anzahl hochgeladener Materialien):
- Unter 20 Materialien: **du bekommst nur 50 %** des Verkaufspreises (eduki behält 50 %)
- Ab 100 Materialien: du bekommst bis zu 70 % (eduki behält 30 %)
- Zusätzlich 0,30 € Transaktionsgebühr pro Verkauf
- **Kein Gewerbe nötig** — läuft rechtlich als Lizenzvergabe, nicht als Direktverkauf; Auszahlung ab 10 € monatlich

Wichtig: Bei nur 19–22 Produkten wirst du länger in der 50-%-Stufe bleiben, wenn du nicht zusätzlich einzelne Kartenblöcke oder Arbeitsblätter separat hochlädst, um über 20 bzw. 100 Materialien zu kommen.

### Eigener Shop (klartext-mentoring.de) — 0 % Provision
Zur Einordnung: Sobald du dort einen echten Checkout hast (z. B. über Stripe oder PayPal), zahlst du nur die üblichen Zahlungsanbieter-Gebühren (grob 1,5–3 %) — keine Marktplatz-Provision. Das ist langfristig die günstigste Variante, hat aber kein eingebautes Käuferpublikum wie Etsy/eduki.

### Empfehlung
Nicht "entweder-oder", sondern gestaffelt:
1. **Eigener Shop** bleibt die Basis (höchste Marge, du bestimmst alles).
2. **Pinterest** kostenlos parallel für Reichweite/Traffic auf den eigenen Shop.
3. **Etsy** für die Kartendecks (Print + PDF), weil dort ohnehin nach "Coaching-Karten"/"Therapiekarten" gesucht wird und die Gebühr mit ~10–17 % vertretbar ist.
4. **eduki** gezielt für die Decks mit klarem Schulbezug (LK, OGS, DaZ-GS/Sek-I, Werkzeugkarten, Geschichtenkarten) — die 50 % Anfangsprovision ist hoch, aber die Zielgruppe (Lehrkräfte, die aktiv nach Unterrichtsmaterial suchen) ist dort konzentrierter als sonst irgendwo.

## 3. Preisvorschlag (fixiert, bisher nur als Spanne markiert)

Die Verkaufsseiten zeigen aktuell Preisspannen (z. B. "15–18 €"). Für einen echten Checkout brauchst du feste Preise. Vorschlag: oberes Ende der bisherigen Spanne fixieren — das gibt dir Puffer für Marktplatz-Gebühren (Etsy/eduki), ohne dass du auf deinem eigenen Shop draufzahlst.

| Produkt | Karten | Digital/PDF | Print |
|---|---|---|---|
| Hochbegabung (HB) | 12 | 10 € | 20 € |
| Mobbing (MB) | 15 | 10 € | 20 € |
| Krisendeck (FK) | 8 | 15 € | 22 € |
| DaZ-GS | 25 | 15 € | 25 € |
| DaZ-Sek I | 25 | 15 € | 25 € |
| Werkzeugkarten (M3) | 26 | 15 € | 25 € |
| FS | 32 | 15 € | 27 € |
| OGS | 32 | 15 € | 27 € |
| TK | 19 | 18 € | 27 € |
| Zonen-Set (ZS) | – | 18 € | 27 € |
| JD | 52 | **22 €** | **34 €** |
| KD | 35 | 18 € | 29 € |
| EL | 58 | **22 €** | **34 €** |
| LK | 71 | **22 €** | **34 €** |
| TR | 33 | 18 € | 29 € |
| AT | 24 | 18 € | 29 € |
| ADHS | 24 | 18 € | 29 € |
| Geschichtenkarten (GK) | 30 | 18 € | 29 € |
| Insel-Set (IS) | 16 | 22 € | 36 € (beide Sets) |
| SMI | 10 | 13–15 € | 22–25 € |
| LRS-Sek1 | 10 | 13–15 € | 22–25 € |
| SP | 7 | 12–15 € | 19–22 € |

**Entschieden (07.08.2026):** EL/LK auf 22 €/34 € angehoben (wertbasierte Preisgestaltung — Umfang + höhere Zahlungsbereitschaft der Fachkräfte-Zielgruppe statt reiner Konsistenz mit den kleineren Decks). Auf den Verkaufsseiten (`EL_Verkaufsseite.html`, `LK_Verkaufsseite.html`) als Spanne 19–22 €/31–34 € dargestellt, konsistent mit dem Range-Stil der übrigen, noch nicht auf Festpreis umgestellten Seiten.

**Nachtrag (07.08.2026):** JD (52 Karten, zweitgrößtes Deck nach LK/EL) der Einheitlichkeit halber
in dieselbe Preisstufe gezogen — ebenfalls 22 €/34 € (Spanne 19–22 €/31–34 € auf
`JD_Verkaufsseite.html`). Damit bilden EL/LK/JD gemeinsam die "große Decks"-Preisstufe, klar
abgesetzt von den 18 €/29 €-Decks wie KD (35 Karten).

## 4. Was bleibt kostenlos?

Kostenlos = Werbung/Vertrauensaufbau, kein Verkaufsverlust, weil es nie verkauft werden sollte:

- **Barometer-Erklär-Karussell** (Social Media) — bereits als kostenloses Lead-Material konzipiert, bleibt frei zugänglich auf Instagram/TikTok/Pinterest.
- **Externe Barometer-Erklärseite** (ohne Login) — dient als Vertrauensaufbau/Vorschau, nicht als Produkt.
- **Musterkarten/Vorschaubilder** auf den Verkaufsseiten — bleiben Marketing, nicht Produkt.
- **"Brainy muss mal kurz…"-Kärtchen** — eignen sich gut als kostenloser Download/Freebie beim Newsletter-Eintrag oder Social-Media-Aktion, falls du Leads sammeln willst (aktuell nicht als Freebie verlinkt — Idee, keine Entscheidung).

Alles andere (die 22 Decks/Sets) bleibt kostenpflichtig — das ist dein eigentliches Geschäft, hier gibt es keinen Grund, etwas zu verschenken.

## Offene Entscheidungen für dich

1. ~~EL/LK höher bepreisen wegen Kartenzahl, oder Konsistenz behalten?~~ **Entschieden 07.08.2026: angehoben auf 22 €/34 €.**
2. ~~Sollen SMI/LRS-Sek1/SP zuerst eine Verkaufsseite bekommen?~~ **Erledigt 07.08.2026: alle drei Seiten gebaut und verlinkt.**
3. Auf welchen Marktplätzen willst du zuerst starten — alle drei gleichzeitig, oder erst Etsy, dann eduki? *(weiterhin offen, zurückgestellt)*
4. Soll "Brainy muss mal kurz…" als offizielles Freebie (z. B. gegen E-Mail-Adresse) eingerichtet werden? *(weiterhin offen, zurückgestellt)*
