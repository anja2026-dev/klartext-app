# "Brainy muss mal kurz…" — Signalkarten-Serie (Konzept)

Stand: 06.08.2026 · Nachfolger von `KD-02_Klokarten.html` ("Klo-Kärtchen")

## Idee

Statt eines einzelnen Kärtchen-Typs (bisher: 12 fast identische runde Chips, alle mit
demselben 🚽-Emoji, auch wenn der Text "Pause gebraucht" oder "Kurze Auszeit" sagt — das
Symbol passte nicht zum Text) eine kleine Serie mit klar unterscheidbaren Bedürfnissen.
Serientitel bewusst offen, ohne "raus" (Anjas Korrektur): **"Brainy muss mal kurz…"** — das
Bild auf jeder Karte vervollständigt den Satz.

Kind zeigt die Karte → INGRA/Lehrkraft nickt → keine Unterbrechung, keine lange Erklärung
nötig. Bisheriger Mechanismus bleibt, nur die Bildsprache wird differenziert.

## Die 6 Karten

1. **Toilette** — Brainy zeigt auf eine Toilettentür / hält ein WC-Symbol
2. **Trinkpause** — Brainy hält ein Glas Wasser
3. **Bewegung am Platz** — Brainy macht eine kleine Dehnübung (bleibt im Raum)
4. **Zu meiner Insel** — Brainy zeigt auf eine kleine Insel-/Zonen-Markierung (nur relevant
   wenn die Klasse ein Insel-/Zonen-Set hat, siehe `KLARTEXT_Insel-Set_*.pdf`)
5. **Frische Luft** — Brainy steht an einer offenen Tür/einem Fenster, atmet sichtbar
6. **Kurz für mich** — Brainy sitzt ruhig mit geschlossenen Augen (Moment zum Runterkommen,
   Bezug zum Barometer Gelb/Orange)

Jede Karte: kurzes 1-2-Wort-Label unter dem Bild (Toilette · Trinken · Bewegung · Insel ·
Luft · Für mich), keine langen Sätze — Konsistenz mit dem Rest der Kinder-Downloads.

## Bildprompts (copy-ready, Gemini)

Charakterbogen + Stil identisch zu `KD_Brainy_Prompts.md` — falls der Referenzbogen noch
nicht vorliegt, zuerst dort den Charakterbogen-Prompt generieren.

**Brainy-Kurzbeschreibung** (in jeden Prompt einsetzen):
`Brainy (a friendly round cream-white cloud-shaped brain character, soft brain-fold texture, small round grey-blue glasses, closed peaceful eyes, warm gentle smile, short stubby arms)`

**Stil-Zusatz** (an jeden Prompt anhängen):
`modern children's book illustration, confident linework, smooth shading, vibrant warm colors, expressive detailed faces, realistic proportions, high resolution, no grain, no texture, no text, no watermark`

1. **Toilette:** `illustration of Brainy pointing cheerfully at a simple toilet door icon with a small figure symbol, friendly and matter-of-fact expression, [Stil-Zusatz]`
2. **Trinkpause:** `illustration of Brainy happily holding up a small glass of water with both stubby arms, [Stil-Zusatz]`
3. **Bewegung am Platz:** `illustration of Brainy mid-stretch with arms raised playfully, small motion lines around it, [Stil-Zusatz]`
4. **Zu meiner Insel:** `illustration of Brainy standing on a small round cushion or floor marker like a tiny island, gesturing invitingly toward it, [Stil-Zusatz]`
5. **Frische Luft:** `illustration of Brainy standing beside an open window with a gentle breeze, eyes closed, taking a deep calm breath, [Stil-Zusatz]`
6. **Kurz für mich:** `illustration of Brainy sitting cross-legged with eyes closed and a small peaceful smile, hands resting calmly, [Stil-Zusatz]`

## Technisch

`KD-02_Klokarten.html` bleibt als Dateiname bestehen (verlinkt von `KLARTEXT_Downloads.html`
und weiteren Downloads-Seiten) — nur Inhalt/Titel wird beim Umbau ersetzt, keine
Linkbrüche. Layout-Vorlage: dieselben runden Chips (110×110px) wie bisher, aber pro Karte
eigenes Bild statt Emoji, plus Brainy jetzt als Hauptmotiv statt kleines Wasserzeichen.

**Nächster Schritt:** Anja generiert die 6 Bilder, dann baue ich die Karte neu (Titel,
Layout, Downloads-Verlinkung inkl. Umbenennung von "Klo-Kärtchen" auf "Brainy muss mal
kurz…" in `KLARTEXT_Downloads.html`).
