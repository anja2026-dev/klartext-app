# 📋 Premium-Prompt für Claude: Das "Klassenzimmer-Upgrade" (Multi-Profile, Gast-Bypass & Zauberfächer) - v3.0

## 1. Hintergrund & Problemstellung
Wir haben das "Mein 5-Sekunden-Tagesjournal" für den eduki-Verkauf optimiert. Lehrkräfte möchten dieses Journal ausdrucken und für **alle** Kinder einer Klasse (z.B. auf den Tisch oder in das Fach geklebt) verwenden. 
Aktuell stößt das digitale System dabei an zwei logische Grenzen:
1. **Der Login-Schutz:** Wenn ein Kind den QR-Code auf seinem gedruckten Journal scannt, landet es auf der Login-Seite (`KLARTEXT_Login.html`), weil es keinen aktiven Lizenzschlüssel hat.
2. **Das 1-Kind-Limit:** Die App speichert im `localStorage` aktuell nur die Daten für *ein* einzelnes Kind ab. Wenn mehrere Kinder denselben Klassen-Tablet-PC nutzen oder die Lehrkraft Berichte abrufen will, überschreiben sich die Daten gegenseitig.

## 2. Dein Arbeitsauftrag: Das Klassenzimmer-Upgrade umsetzen

Bitte überarbeite die App-Logik in den betroffenen Dateien (`KLARTEXT_Login.html`, `KLARTEXT_Spiele.html`, `KLARTEXT_Ressourcenbericht.html` und den betroffenen Spiel-Modulen) wie folgt:

### Säule 1: Der "Gast-Bypass" für Schüler-QR-Codes (No-Login-Modus)
- Wenn eine Datei mit dem URL-Parameter `?guest=true` aufgerufen wird (z.B. über den QR-Code auf dem gedruckten eduki-Blatt), wird der **Login-Schutz komplett umgangen**!
- Das Kind sieht direkt das Tool und kann damit interagieren.
- **Folgende Tools MÜSSEN den Bypass (?guest=true) unterstützen:**
  1. `BAROMETER_KIND.html` (Das 5-stufige Barometer für den Tisch) [37, 50, 77]
  2. `KLARTEXT_Spiel_Ruheballon.html` (Atemberuhigung bei Gelb/Orange) [35, 36]
  3. `KLARTEXT_Spiel_Zauberfaecher.html` (Der interaktive digitale Zauberfächer!) [38]
- **Wichtig für den Datenschutz (DSGVO):** Im Gast-Modus werden *keine* Daten dauerhaft im localStorage gespeichert und es wird kein Name abgefragt. Nach der kurzen Nutzung schließt sich das Tool einfach wieder. Dadurch gibt es an Schulen keinerlei Datenschutz-Bedenken!

### Sektion 2: Der "Lehrer-Klassen-Manager" für `lehrkraft24` & `sb-ingra26`
- Wenn sich eine Lehrkraft mit dem Code `lehrkraft24` oder eine Schulbegleitung mit `sb-ingra26` einloggt, sieht sie auf ihrem Dashboard ein neues Element: **"Klassenzimmer verwalten"**.
- Hier kann sie eine Liste von Vornamen ihrer Schüler anlegen (z.B. "Paul", "Emma", "Lina"). Diese Liste wird lokal im localStorage unter `klartext_class_list` gespeichert.
- Wenn die Lehrkraft nun ein Tool (wie das Tagesjournal, das Barometer, den Ressourcenbericht oder die unten freigeschalteten Spiele) öffnet, erscheint oben ein kleines, dezentes **Dropdown-Menü ("Aktives Kind wählen")**.
- Wählt sie "Paul", werden alle Eingaben und Berichte unter dem Key `klartext_data_Paul` gespeichert. Wechselt sie auf "Emma", sieht sie Emmas Daten.
- Dadurch kann die Lehrkraft ein einziges Klassen-Tablet herumgehen lassen, und jedes Kind kann nacheinander seine Stimmung eintragen oder seine Tools nutzen, ohne dass Daten überschrieben werden!

### Sektion 3: Freischaltung der Grundschul- & Regulations-Tools für Lehrkräfte
Stelle sicher, dass bei den Logins `lehrkraft24` und `sb-ingra26` die folgenden 5 elementaren Tools auf dem Dashboard voll sichtbar und nutzbar sind:
1. **Der digitale Zauberfächer** (`KLARTEXT_Spiel_Zauberfaecher.html`) 🌟 *NEU* [38]
2. **Das Mutmach-Tier** (Zum interaktiven Ausmalen & Kraft tanken) [35]
3. **Der Fokus-Trainer** (Der 25-Minuten-ADHS-Konzentrations-Timer) [35, 36]
4. **Mein Tag (Tagesplan)** (Für die visuelle Strukturierung des Schultags) [35, 36]
5. **Der Ruhe-Ballon** (Die Atemanleitung zur sofortigen Beruhigung bei Gelb/Orange) [35, 36]

## 3. Code-Qualität & Token-Sparvorgabe
- Bitte lies die betroffenen Dateien direkt von meiner lokalen Festplatte ein.
- Überschreibe nur die notwendigen Login-Abfragen und die localStorage-Keys (nutze dynamische Keys wie `klartext_data_` + `active_student_name`).
- Gib mir KEINEN unnötigen Code-Spam aus – passe die Dateien direkt im Projektordner an.
