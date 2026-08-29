# Spezifikation: KLARTEXT Werte-Poker 2.0 (Deep-Dive für Jugendliche)

Diese Spezifikation dient als direktes Umsetzungsdokument für das Entwicklungs- und Coaching-Team. Sie rüstet das bestehende Werte-Poker (`KLARTEXT_Spiel_WertePoker.html`) zu einem interaktiven, kognitiv entlasteten Coaching-Erlebnis für Jugendliche (ab Klasse 7) auf.

---

## 1. Die pädagogische UX-Herausforderung & Lösung

### Das Problem (Schreibblockade / „Head Freeze“)
Jugendliche im Übergang Schule-Beruf oder in Krisensituationen tun sich extrem schwer, eigene Werte abstrakt zu benennen oder lange Freitexte einzutippen. Ein leeres Eingabefeld erzeugt Frust und führt zu schnellen Abbrüchen.

### Die KLARTEXT-Lösung: „Klicken statt Grübeln – Ergänzen statt Erfinden“
Wir erweitern das Werte-Poker um ein dreistufiges Entlastungs-Modell:
1. **Themen-Sortierter Kartenpool:** Die klassischen 24 Werte werden in nahbare, jugendgerechte Themenwelten sortiert.
2. **Inspirations-Joker (Erweiterter Pool):** Einblendbare Zusatzkarten mit modernen Begriffen (z.B. „Grenzen setzen“, „Gaming-Crew“, „Echtheit“).
3. **Lückentext-Generator (Satzstarter):** Statt leerer Textfelder beantworten Jugendliche systemische Reflexionsfragen über anklickbare Antwort-Kacheln, die sie optional durch eigene Worte ergänzen können.

---

## 2. Der neue Spiel- & Reflexions-Flow (5 Phasen)

```
+-----------------------------------------------------------------------+
|  Phase 1: Karten wählen (Themenwelten, Zusatzkarten, Custom-Input)    |
+-----------------------------------------------------------------------+
                                  v
+-----------------------------------------------------------------------+
|  Phase 2: Werte-Treppe (Priorisierung 1 bis 5 per Drag & Drop)        |
+-----------------------------------------------------------------------+
                                  v
+-----------------------------------------------------------------------+
|  Phase 3: Barometer-Brücke (Wert mit Regulations-Farbe verknüpfen)    |
+-----------------------------------------------------------------------+
                                  v
+-----------------------------------------------------------------------+
|  Phase 4: Sinn-Reflexion (Anklickbare Satzstarter & Lückentexte)      |
+-----------------------------------------------------------------------+
                                  v
+-----------------------------------------------------------------------+
|  Phase 5: Live-Speicherung & Übergabe an den Ressourcen-Bericht      |
+-----------------------------------------------------------------------+
```

### Phase 1: Karten-Auswahl mit Entlastung

Der bestehende Kartenpool von 24 Werten bleibt als Basis erhalten, wird aber optisch in vier **„Themenwelten“** sortiert, um dem Gehirn Struktur zu geben:

*   **🏆 Leistung & Machen:** Erfolg, Wissen, Disziplin, Macht, Kreativität, Abenteuer
*   **❤️ Beziehungen & Team:** Freundschaft, Familie, Treue, Respekt, Loyalität, Toleranz
*   **🛡️ Sicherheit & Halt:** Sicherheit, Gesundheit, Vertrauen, Gerechtigkeit, Ehrlichkeit, Schönheit
*   **🌱 Mein Freiraum:** Freiheit, Unabhängigkeit, Ruhe, Anerkennung, Humor, Mut

#### ➕ Das Zusatzkarten-Karussell (Clickable Presets)
Falls Jugendliche im Standard-Pool nichts finden, können sie per Klick auf *„Mehr Ideen anzeigen“* moderne, alltagsnahe Zusatzkarten aktivieren:
*   *„Grenzen setzen“ (Selbstfürsorge)*
*   *„Echtheit“ (Real-Me vs. Online-Me)*
*   *„Digital-Life / Gaming“*
*   *„Klimaschutz / Zukunft“*
*   *„Gesehen werden“ (Anerkennung)*
*   *„Einfach Chillen“*

#### ✍️ Das geführte Custom-Eingabefeld (Eigener Wert)
Ein Eingabefeld *„Eigenen Wert erfinden“* ist vorhanden. Sobald der Cursor ins Feld springt, rotiert ein grauer, inspirierender Platzhalter-Text im Hintergrund:
*   *„z.B. Mein Hund, Zocken mit Freunden, Mein eigenes Zimmer, Musik hören...“*

---

### Phase 2: Die Werte-Treppe (Werte-Ranking)

Sobald exakt 5 Karten im Setz-Bereich liegen, wechselt die Ansicht zur **Werte-Treppe**. 
*   Die 5 Karten müssen per Drag & Drop oder simpler Klick-Reihenfolge auf die Treppenstufen **Platz 1 (Mein Fundament / Unverzichtbar)** bis **Platz 5 (Wichtig, aber verhandelbar)** verteilt werden.

---

### Phase 3: Die Barometer-Brücke (Selbstregulation)

Die App schlägt die Brücke zum zentralen Regulations-Werkzeug (Barometer):
*   **Frage:** *„Wenn dein Stimmungs-Barometer auf GELB (angespannt) oder ORANGE (belastet) steht – welcher deiner 5 Werte ist dein bester Rettungsanker, um wieder in den grünen Bereich zu kommen?“*
*   **Interaktion:** Der Jugendliche tippt einfach auf eine der 5 platzierten Wertekarten.
*   **Systemischer Effekt:** Verknüpfung von kognitiven Werten mit unmittelbarer emotionaler Körperregulation.

---

### Phase 4: Die Sinn-Reflexion (Lückentext-Prinzip)

Um herauszufinden, was der gewählte Top-Wert (Platz 1) für den Jugendlichen *konkret* bedeutet, nutzen wir einen spielerischen **Lückentext-Ablauf mit vordefinierten Antwort-Kacheln**:

#### Beispiel für gewählten Top-Wert: „Freiheit“
> *„Freiheit ist mein Platz 1. Das bedeutet für mich im Alltag vor allem...“*
*   [ ] ...dass ich mir meine Zeit selbst einteilen kann.
*   [ ] ...dass mir niemand ständig reinredet oder mich kontrolliert.
*   [ ] ...dass ich meine eigenen kreativen Ideen ausprobieren darf.
*   [ ] ...dass ich mich auch mal zurückziehen und meine Ruhe haben kann.
*   [ ] *[Freies Textfeld]* „Ich möchte es mit eigenen Worten beschreiben...“

#### Beispiel für gewählten Top-Wert: „Freundschaft“
> *„Freundschaft ist mein Platz 1. Das bedeutet für mich im Alltag vor allem...“*
*   [ ] ...dass wir absolut ehrlich zueinander sind und keine Geheimnisse haben.
*   [ ] ...dass wir einfach zusammen chillen können, ohne viel zu labern.
*   [ ] ...dass wir ein festes Team sind (z.B. in der Gaming-Gilde oder beim Sport).
*   [ ] ...dass mich der andere so akzeptiert, wie ich wirklich bin (mein Real-Me).
*   [ ] *[Freies Textfeld]* „Ich möchte es mit eigenen Worten beschreiben...“

---

### Phase 5: Speicher-Logik & Berichts-Schnittstelle

*   **localStorage-Key:** `klartext_werte_deepdive`
*   **Struktur:**
    ```json
    {
      "ranked_values": ["Freiheit", "Freundschaft", "Ruhe", "Humor", "Erfolg"],
      "barometer_anchor": "Ruhe",
      "top_value_meaning": "dass mir niemand ständig reinredet oder mich kontrolliert.",
      "timestamp": "2026-08-28T12:00:00Z"
    }
    ```
*   **Berichts-Integration:** Diese detaillierte Struktur wird direkt in den **Ressourcen-Bericht für Jugendliche** (Schiene B) eingelesen. Im Bericht steht dann ein hochprofessioneller, wertschätzender Absatz:
    > *„Im Werte-Poker hat der Jugendliche **Freiheit** als seinen wichtigsten Kernwert identifiziert. Für ihn bedeutet dies im praktischen Alltag: **'dass mir niemand ständig reinredet oder mich kontrolliert.'** Als emotionalen Rettungsanker in Stressmomenten (Barometer Gelb/Orange) nutzt er den Wert **Ruhe**.“*

---

## 3. Technische CSS/JS-Kompaktheiten für den Prototyp

*   **Drag-and-Drop:** Fallback auf Touch-freundliche Click-to-Rank-Mechanik für reibungslose mobile Nutzung auf schuleigenen Tablets.
*   **Ablauf-Sicherung:** Erst wenn Phase 4 (Lückentext) abgeschlossen ist, wird der Button „Ergebnisse speichern & zum Ressourcen-Bericht hinzufügen“ freigeschaltet.
*   **Reizarme Optik:** Dunkles, beruhigendes KLARTEXT-Hintergrunddesign mit farbigen Akzenten ausschließlich bei den Barometer-Referenzen, um ADHS- und autistische Jugendliche nicht visuell zu überfordern.
