# KD-Deck – Brainy-Vereinheitlichung: Charakterbogen + Bild-Prompts
Stand: 25.07.2026

## Werkzeug-Empfehlung

- **Gemini (weiter benutzen):** Genau das Tool, mit dem die bisherigen 31 Bilder schon entstanden sind – trifft den weichen Aquarell-Kinderbuch-Stil bereits gut. Aktuelle Gemini-Bildmodelle ("Nano Banana"-Familie) sind speziell dafür gut, eine Figur aus einem Referenzbild über mehrere neue Szenen hinweg konsistent zu halten. Das ist der praktikabelste Weg.
- **Claude Design (Anthropic, seit April 2026 verfügbar):** Echtes Produkt, aber für UI-Prototypen, Mockups, Slides und Landingpages gebaut – nicht für erzählerische Kinderbuch-Illustration mit Charakterkonsistenz über Szenen hinweg. Für dieses Set vermutlich nicht die richtige Wahl.
- **Claude Code:** Kein Bildgenerierungswerkzeug, hier nicht einsetzbar.

## Praktischer Ablauf

1. Charakterbogen-Prompt (unten) einmal in Gemini generieren lassen → mehrere Ansichten/Posen von Brainy im Szenen-Stil.
2. Für jedes der 30 Bilder: das beste Charakterbogen-Bild als Referenz mitgeben + den jeweiligen Szenen-Prompt unten verwenden ("gleiche Figur wie im Referenzbild, in dieser neuen Szene").
3. KD-06 und KD-08 zusätzlich inhaltlich geschärft (siehe unten) – die Gesichtsausdrücke/Symbole waren im Original zu ähnlich (beide liefen auf eine Regenwolke + neutralen Ausdruck hinaus).

## Brainy – Charakterbeschreibung (abgeleitet vom bestehenden Brainy-Icon)

Rundliche, wolkig-fluffige Gehirnform in cremeweißer Farbe mit sanften, klar gezeichneten Hirnwindungs-Linien; kleine runde Brille (helles Grau/Blau); geschlossene, friedliche Augen mit warmem, sanftem Lächeln; kurze, einfache Arme/Hände, oft mit einem kleinen roten Herz; keine Ohren, keine weiteren Merkmale außer der Windungstextur. Wichtig: Das bestehende Brainy-Icon ist flacher Vektor-Stil – in den Kartenbildern muss Brainy im selben weichen Aquarell-Stil wie die Szene selbst gemalt werden, nicht als Icon eingefügt.

### Charakterbogen-Prompt (einmalig generieren)
```
character reference sheet, three-quarter view and front view and side view of the same character: Brainy, a friendly round cream-white cloud-shaped brain character with soft rounded brain-fold texture drawn in gentle black outlines, small round grey-blue glasses, closed peaceful eyes with a warm gentle smile, short simple stubby arms, sometimes holding a small red heart, no ears, no other features, modern children's book illustration, confident linework, smooth shading, vibrant warm colors, expressive detailed faces, realistic proportions, high resolution, no grain, no texture, no text, no watermark
```

### Brainy-Kurzbeschreibung (für jeden Szenen-Prompt einsetzen)
`Brainy (a friendly round cream-white cloud-shaped brain character, soft brain-fold texture, small round grey-blue glasses, closed peaceful eyes, warm gentle smile, short stubby arms)`

---

## 30 aktualisierte Szenen-Prompts (Brainy statt generischer "mascot character")

Stil-Zusatz bleibt für alle: `modern children's book illustration, confident linework, smooth shading, vibrant warm colors, expressive detailed faces, realistic proportions, high resolution, no grain, no texture, no text, no watermark`

**KD-01 (korrigiert 25.07.2026 – falsche Barometer-Farben im ersten Ergebnis)** Das erste generierte Bild zeigte von sich aus 5 Farbkärtchen (schöne Idee!), aber in falschen Farben (Rot/Gelb/Grün/Blau/Lila statt dem echten KLARTEXT-Barometer). Neu generieren mit explizit benannten Farben:
`illustration of a child and Brainy sitting together on the floor, child pointing at five small mood cards laid out in a row, the cards colored in this exact order and these exact colors: green, yellow, orange, red, grey, [Stil-Zusatz]`

**KD-02** `illustration of a child with a gentle glowing spot on their tummy area, curious expression, Brainy sitting nearby, [Stil-Zusatz]`

**KD-03** `illustration of a child holding two small colorful cloud shapes, one in each hand, Brainy watching supportively, [Stil-Zusatz]`

**KD-04** `illustration of a child looking at a rainbow of simple colorful shapes, all treated equally, Brainy smiling encouragingly, [Stil-Zusatz]`

**KD-05** `illustration of a child looking thoughtfully at a simple blank cloud shape, Brainy sitting patiently beside them, [Stil-Zusatz]`

**KD-06 (geschärft – Wut statt Trauer erkennbar machen)** `illustration of a child with furrowed brows, flushed cheeks and crossed arms, a small soft storm cloud with a tiny lightning bolt above their head, Brainy sitting calmly beside them with one open supportive hand gesture, [Stil-Zusatz]`
Ergebnis vom 25.07. geprüft (Bild in bilder/kd/): Gewitterwolke+Blitz kommt gut rüber, Gesichtsausdruck des Kindes wirkt aber eher besorgt als eindeutig wütend – Anja hat entschieden, auch dieses Bild nochmal zu korrigieren. Für den nächsten Versuch Ausdruck expliziter machen, z. B.: `child with a scrunched angry frown, eyebrows pulled tightly down and together, mouth in a tight angry line, red flushed cheeks, arms crossed tightly` statt nur "furrowed brows".

**KD-07** `illustration of a child holding Brainy's hand while looking toward something unfamiliar in the distance, [Stil-Zusatz]`

**KD-08 (geschärft – klar von KD-06 unterscheidbar)** `illustration of a child sitting quietly with downturned mouth, low shoulders and one small teardrop, a plain gentle raincloud nearby (no lightning), Brainy sitting close in comforting silence, [Stil-Zusatz]`

**KD-09** `illustration of a child doing a calming activity like deep breathing with a pinwheel, Brainy breathing along, [Stil-Zusatz]`

**KD-10** `illustration of a small child standing confidently tall with Brainy cheering supportively beside them, [Stil-Zusatz]`

**KD-11** `illustration of two children standing slightly apart looking upset, Brainy standing calmly between them, [Stil-Zusatz]`

**KD-12** `illustration of a child offering a small flower or object to another child as a gesture of apology, Brainy smiling nearby, [Stil-Zusatz]`

**KD-13** `illustration of a child standing calmly and confidently while looking at a small conflict scene from a distance, Brainy standing supportively beside them, [Stil-Zusatz]`

**KD-14** `illustration of two children building or fixing something small together, cooperative calm scene, Brainy watching happily, [Stil-Zusatz]`

**KD-15** `illustration of a child watching two other children in a small disagreement from a calm distance, Brainy nearby, [Stil-Zusatz]`

**KD-16** `illustration of a child standing at a new doorway looking curious rather than scared, Brainy encouraging from beside them, [Stil-Zusatz]`

**KD-17** `illustration of a child reaching out toward a new activity or toy with curious excitement, Brainy cheering them on, [Stil-Zusatz]`

**KD-18** `illustration of a child hesitating at the edge of a playground activity, Brainy offering a gentle supportive hand, [Stil-Zusatz]`

**KD-19** `illustration of a child taking one small step forward while still holding Brainy's hand tightly, [Stil-Zusatz]`

**KD-20** `illustration of a child raising a hand calmly to ask for help, Brainy nodding supportively beside them, [Stil-Zusatz]`

**KD-21** `illustration of two children playing together happily, Brainy watching warmly from nearby, [Stil-Zusatz]`

**KD-22** `illustration of a child standing at the edge of a group of playing children, Brainy standing beside them supportively, [Stil-Zusatz]`

**KD-23** `illustration of a child sitting alone on a bench during a school break, Brainy sitting down calmly next to them, [Stil-Zusatz]`

**KD-24** `illustration of a child walking calmly toward another child playing alone, small approachable gesture, Brainy encouraging from behind, [Stil-Zusatz]`

**KD-25** `illustration of a child standing calmly while another child walks away, Brainy standing protectively but calmly beside them, [Stil-Zusatz]`

**KD-26** `illustration of a child with a gentle glowing signal near their stomach, curious attentive expression, Brainy pointing gently, [Stil-Zusatz]`

**KD-27** `illustration of a child pausing calmly mid-activity with a small clear stop gesture, Brainy nodding supportively, [Stil-Zusatz]`

**KD-28** `illustration of a child doing something comforting like stretching or hugging a soft object, Brainy relaxing alongside them, [Stil-Zusatz]`

**KD-29** `illustration of a child standing confidently with arms gently at their sides, calm assured posture, Brainy standing supportively beside them, [Stil-Zusatz]`

**KD-30** `illustration of a child sitting peacefully with eyes closed, Brainy sitting calmly beside them in the same relaxed pose, [Stil-Zusatz]`

---

## 30 fertige Copy-Prompts für Bing (27.07.2026)

Die Kurzform oben (mit `[Stil-Zusatz]`-Platzhalter und bloßer Namensnennung "Brainy") war für
Gemini + Referenzbild gedacht, wo ein Textzusatz für die Figur nicht nötig ist. Bing hat keinen
Referenzbild-Mechanismus – deshalb hier jeder Prompt komplett ausformuliert, inkl. Brainys
charakteristischem roten Herz (das bei der ersten FS-Deck-Fassung versehentlich verloren ging,
siehe FS_Bildprompts.md – hier von Anfang an mitgeführt und geprüft). Bei KD-07 und KD-19 hält das
Kind Brainys Hand, deshalb dort die besitzanzeigende Form „Brainy's (...)". Alle 30 Prompts einzeln
auf die 480-Zeichen-Grenze von Bing geprüft (Maximum: 485 Zeichen vor der letzten Kürzung bei
KD-06, jetzt 468 Zeichen – dafür wurde nur die Szenenbeschreibung gekürzt, nicht Brainys
Beschreibung).

**Hinweis zur Charakterkonsistenz:** wie bei FS/DaZ-GS/DaZ-Sek1 kann Brainys Aussehen bei Bing
(kein Referenzbild-Mechanismus) leicht von Bild zu Bild variieren. Stichprobenartig prüfen und
Ausreißer notfalls neu generieren.

Zielordner: `bilder/kd/` (bestehende Dateien mit Titel im Namen, z. B. `KD-01 Wie geht es mir
heute.jpg`, bleiben unangetastet liegen – neue Bilder bitte als `KD-01.jpg` usw. ablegen, das
Pipeline-Skript findet beide Varianten).

---

**Dateiname: KD-01.jpg**
```
A child and Brainy (cream cloud-shaped brain character, grey-blue glasses, peaceful closed eyes, gentle smile, holding a small red heart) sitting together, child pointing at five mood cards in a row: green, yellow, orange, red, grey. modern children's book illustration, confident linework, smooth shading, vibrant warm colors, expressive detailed faces, realistic proportions, high resolution, no grain, no texture, no text, no watermark
```

**Dateiname: KD-02.jpg**
```
A child with a gentle glowing spot on their tummy, curious expression, Brainy (cream cloud-shaped brain character, grey-blue glasses, peaceful closed eyes, gentle smile, holding a small red heart) sitting nearby. modern children's book illustration, confident linework, smooth shading, vibrant warm colors, expressive detailed faces, realistic proportions, high resolution, no grain, no texture, no text, no watermark
```

**Dateiname: KD-03.jpg**
```
A child holding two small colorful cloud shapes, one in each hand, Brainy (cream cloud-shaped brain character, grey-blue glasses, peaceful closed eyes, gentle smile, holding a small red heart) watching supportively. modern children's book illustration, confident linework, smooth shading, vibrant warm colors, expressive detailed faces, realistic proportions, high resolution, no grain, no texture, no text, no watermark
```

**Dateiname: KD-04.jpg**
```
A child looking at a rainbow of simple colorful shapes, all treated equally, Brainy (cream cloud-shaped brain character, grey-blue glasses, peaceful closed eyes, gentle smile, holding a small red heart) smiling encouragingly. modern children's book illustration, confident linework, smooth shading, vibrant warm colors, expressive detailed faces, realistic proportions, high resolution, no grain, no texture, no text, no watermark
```

**Dateiname: KD-05.jpg**
```
A child looking thoughtfully at a simple blank cloud shape, Brainy (cream cloud-shaped brain character, grey-blue glasses, peaceful closed eyes, gentle smile, holding a small red heart) sitting patiently beside them. modern children's book illustration, confident linework, smooth shading, vibrant warm colors, expressive detailed faces, realistic proportions, high resolution, no grain, no texture, no text, no watermark
```

**Dateiname: KD-06.jpg**
```
A child frowning, eyebrows down, tight angry mouth, red cheeks, arms crossed, a storm cloud with lightning above their head, Brainy (cream cloud-shaped brain character, grey-blue glasses, peaceful closed eyes, gentle smile, holding a small red heart) beside them. modern children's book illustration, confident linework, smooth shading, vibrant warm colors, expressive detailed faces, realistic proportions, high resolution, no grain, no texture, no text, no watermark
```

**Dateiname: KD-07.jpg**
```
A child holding Brainy's (cream cloud-shaped brain character, grey-blue glasses, peaceful closed eyes, gentle smile, holding a small red heart in his other hand) hand while looking toward something unfamiliar in the distance. modern children's book illustration, confident linework, smooth shading, vibrant warm colors, expressive detailed faces, realistic proportions, high resolution, no grain, no texture, no text, no watermark
```

**Dateiname: KD-08.jpg**
```
A child sitting quietly, downturned mouth, low shoulders, one small teardrop, a gentle raincloud nearby, Brainy (cream cloud-shaped brain character, grey-blue glasses, peaceful closed eyes, gentle smile, holding a small red heart) sitting close in comforting silence. modern children's book illustration, confident linework, smooth shading, vibrant warm colors, expressive detailed faces, realistic proportions, high resolution, no grain, no texture, no text, no watermark
```

**Dateiname: KD-09.jpg**
```
A child doing a calming activity like deep breathing with a pinwheel, Brainy (cream cloud-shaped brain character, grey-blue glasses, peaceful closed eyes, gentle smile, holding a small red heart) breathing along. modern children's book illustration, confident linework, smooth shading, vibrant warm colors, expressive detailed faces, realistic proportions, high resolution, no grain, no texture, no text, no watermark
```

**Dateiname: KD-10.jpg**
```
A small child standing confidently tall with Brainy (cream cloud-shaped brain character, grey-blue glasses, peaceful closed eyes, gentle smile, holding a small red heart) cheering supportively beside them. modern children's book illustration, confident linework, smooth shading, vibrant warm colors, expressive detailed faces, realistic proportions, high resolution, no grain, no texture, no text, no watermark
```

**Dateiname: KD-11.jpg**
```
Two children standing slightly apart looking upset, Brainy (cream cloud-shaped brain character, grey-blue glasses, peaceful closed eyes, gentle smile, holding a small red heart) standing calmly between them. modern children's book illustration, confident linework, smooth shading, vibrant warm colors, expressive detailed faces, realistic proportions, high resolution, no grain, no texture, no text, no watermark
```

**Dateiname: KD-12.jpg**
```
A child offering a small flower or object to another child as a gesture of apology, Brainy (cream cloud-shaped brain character, grey-blue glasses, peaceful closed eyes, gentle smile, holding a small red heart) smiling nearby. modern children's book illustration, confident linework, smooth shading, vibrant warm colors, expressive detailed faces, realistic proportions, high resolution, no grain, no texture, no text, no watermark
```

**Dateiname: KD-13.jpg**
```
A child standing calmly and confidently while looking at a small conflict scene from a distance, Brainy (cream cloud-shaped brain character, grey-blue glasses, peaceful closed eyes, gentle smile, holding a small red heart) standing supportively beside them. modern children's book illustration, confident linework, smooth shading, vibrant warm colors, expressive detailed faces, realistic proportions, high resolution, no grain, no texture, no text, no watermark
```

**Dateiname: KD-14.jpg**
```
Two children building or fixing something small together, cooperative calm scene, Brainy (cream cloud-shaped brain character, grey-blue glasses, peaceful closed eyes, gentle smile, holding a small red heart) watching happily. modern children's book illustration, confident linework, smooth shading, vibrant warm colors, expressive detailed faces, realistic proportions, high resolution, no grain, no texture, no text, no watermark
```

**Dateiname: KD-15.jpg**
```
A child watching two other children in a small disagreement from a calm distance, Brainy (cream cloud-shaped brain character, grey-blue glasses, peaceful closed eyes, gentle smile, holding a small red heart) nearby. modern children's book illustration, confident linework, smooth shading, vibrant warm colors, expressive detailed faces, realistic proportions, high resolution, no grain, no texture, no text, no watermark
```

**Dateiname: KD-16.jpg**
```
A child standing at a new doorway looking curious rather than scared, Brainy (cream cloud-shaped brain character, grey-blue glasses, peaceful closed eyes, gentle smile, holding a small red heart) encouraging from beside them. modern children's book illustration, confident linework, smooth shading, vibrant warm colors, expressive detailed faces, realistic proportions, high resolution, no grain, no texture, no text, no watermark
```

**Dateiname: KD-17.jpg**
```
A child reaching out toward a new activity or toy with curious excitement, Brainy (cream cloud-shaped brain character, grey-blue glasses, peaceful closed eyes, gentle smile, holding a small red heart) cheering them on. modern children's book illustration, confident linework, smooth shading, vibrant warm colors, expressive detailed faces, realistic proportions, high resolution, no grain, no texture, no text, no watermark
```

**Dateiname: KD-18.jpg**
```
A child hesitating at the edge of a playground activity, Brainy (cream cloud-shaped brain character, grey-blue glasses, peaceful closed eyes, gentle smile, holding a small red heart) offering a gentle supportive hand. modern children's book illustration, confident linework, smooth shading, vibrant warm colors, expressive detailed faces, realistic proportions, high resolution, no grain, no texture, no text, no watermark
```

**Dateiname: KD-19.jpg**
```
A child taking one small step forward while still holding Brainy's (cream cloud-shaped brain character, grey-blue glasses, peaceful closed eyes, gentle smile, holding a small red heart in his other hand) hand tightly. modern children's book illustration, confident linework, smooth shading, vibrant warm colors, expressive detailed faces, realistic proportions, high resolution, no grain, no texture, no text, no watermark
```

**Dateiname: KD-20.jpg**
```
A child raising a hand calmly to ask for help, Brainy (cream cloud-shaped brain character, grey-blue glasses, peaceful closed eyes, gentle smile, holding a small red heart) nodding supportively beside them. modern children's book illustration, confident linework, smooth shading, vibrant warm colors, expressive detailed faces, realistic proportions, high resolution, no grain, no texture, no text, no watermark
```

**Dateiname: KD-21.jpg**
```
Two children playing together happily, Brainy (cream cloud-shaped brain character, grey-blue glasses, peaceful closed eyes, gentle smile, holding a small red heart) watching warmly from nearby. modern children's book illustration, confident linework, smooth shading, vibrant warm colors, expressive detailed faces, realistic proportions, high resolution, no grain, no texture, no text, no watermark
```

**Dateiname: KD-22.jpg**
```
A child standing at the edge of a group of playing children, Brainy (cream cloud-shaped brain character, grey-blue glasses, peaceful closed eyes, gentle smile, holding a small red heart) standing beside them supportively. modern children's book illustration, confident linework, smooth shading, vibrant warm colors, expressive detailed faces, realistic proportions, high resolution, no grain, no texture, no text, no watermark
```

**Dateiname: KD-23.jpg**
```
A child sitting alone on a bench during a school break, Brainy (cream cloud-shaped brain character, grey-blue glasses, peaceful closed eyes, gentle smile, holding a small red heart) sitting down calmly next to them. modern children's book illustration, confident linework, smooth shading, vibrant warm colors, expressive detailed faces, realistic proportions, high resolution, no grain, no texture, no text, no watermark
```

**Dateiname: KD-24.jpg**
```
A child walking calmly toward another child playing alone, small approachable gesture, Brainy (cream cloud-shaped brain character, grey-blue glasses, peaceful closed eyes, gentle smile, holding a small red heart) encouraging from behind. modern children's book illustration, confident linework, smooth shading, vibrant warm colors, expressive detailed faces, realistic proportions, high resolution, no grain, no texture, no text, no watermark
```

**Dateiname: KD-25.jpg**
```
A child standing calmly while another child walks away, Brainy (cream cloud-shaped brain character, grey-blue glasses, peaceful closed eyes, gentle smile, holding a small red heart) standing protectively but calmly beside them. modern children's book illustration, confident linework, smooth shading, vibrant warm colors, expressive detailed faces, realistic proportions, high resolution, no grain, no texture, no text, no watermark
```

**Dateiname: KD-26.jpg**
```
A child with a gentle glowing signal near their stomach, curious attentive expression, Brainy (cream cloud-shaped brain character, grey-blue glasses, peaceful closed eyes, gentle smile, holding a small red heart) pointing gently. modern children's book illustration, confident linework, smooth shading, vibrant warm colors, expressive detailed faces, realistic proportions, high resolution, no grain, no texture, no text, no watermark
```

**Dateiname: KD-27.jpg**
```
A child pausing calmly mid-activity with a small clear stop gesture, Brainy (cream cloud-shaped brain character, grey-blue glasses, peaceful closed eyes, gentle smile, holding a small red heart) nodding supportively. modern children's book illustration, confident linework, smooth shading, vibrant warm colors, expressive detailed faces, realistic proportions, high resolution, no grain, no texture, no text, no watermark
```

**Dateiname: KD-28.jpg**
```
A child doing something comforting like stretching or hugging a soft object, Brainy (cream cloud-shaped brain character, grey-blue glasses, peaceful closed eyes, gentle smile, holding a small red heart) relaxing alongside them. modern children's book illustration, confident linework, smooth shading, vibrant warm colors, expressive detailed faces, realistic proportions, high resolution, no grain, no texture, no text, no watermark
```

**Dateiname: KD-29.jpg**
```
A child standing confidently with arms gently at their sides, calm assured posture, Brainy (cream cloud-shaped brain character, grey-blue glasses, peaceful closed eyes, gentle smile, holding a small red heart) standing supportively beside them. modern children's book illustration, confident linework, smooth shading, vibrant warm colors, expressive detailed faces, realistic proportions, high resolution, no grain, no texture, no text, no watermark
```

**Dateiname: KD-30.jpg**
```
A child sitting peacefully with eyes closed, Brainy (cream cloud-shaped brain character, grey-blue glasses, peaceful closed eyes, gentle smile, holding a small red heart) sitting calmly beside them in the same relaxed pose. modern children's book illustration, confident linework, smooth shading, vibrant warm colors, expressive detailed faces, realistic proportions, high resolution, no grain, no texture, no text, no watermark
```

---

## KD-31 bis KD-35 (Block 7 – Familie & neue Situationen, NEU, 30.07.2026)
Gleiches Format wie oben (Bing-fertig, Brainy-Kurzbeschreibung inkl. rotem Herz, alle ≤480
Zeichen). Zielordner weiterhin `bilder/kd/`. 1 Bild mit Diversitätsmerkmal (KD-33).

**Dateiname: KD-31.jpg**
```
A child sitting on a moving box in a half-packed room, calm but pensive expression, Brainy (cream cloud-shaped brain character, grey-blue glasses, peaceful closed eyes, gentle smile, holding a small red heart) sitting close beside them. modern children's book illustration, confident linework, smooth shading, vibrant warm colors, expressive detailed faces, realistic proportions, high resolution, no grain, no texture, no text, no watermark
```

**Dateiname: KD-32.jpg**
```
A child with a small backpack standing between two different front doors in the distance, curious expression, Brainy (cream cloud-shaped brain character, grey-blue glasses, peaceful closed eyes, gentle smile, holding a small red heart) walking alongside. modern children's book illustration, confident linework, smooth shading, vibrant warm colors, expressive detailed faces, realistic proportions, high resolution, no grain, no texture, no text, no watermark
```

**Dateiname: KD-33.jpg**
```
A child with Middle Eastern features sitting slightly apart at a family table with unfamiliar new faces, Brainy (cream cloud-shaped brain character, grey-blue glasses, peaceful closed eyes, gentle smile, holding a small red heart) sitting close for reassurance. modern children's book illustration, confident linework, smooth shading, vibrant warm colors, expressive detailed faces, realistic proportions, high resolution, no grain, no texture, no text, no watermark
```

**Dateiname: KD-34.jpg**
```
A child looking up at a large new school building, backpack on, mixed excited and nervous expression, Brainy (cream cloud-shaped brain character, grey-blue glasses, peaceful closed eyes, gentle smile, holding a small red heart) floating encouragingly beside them. modern children's book illustration, confident linework, smooth shading, vibrant warm colors, expressive detailed faces, realistic proportions, high resolution, no grain, no texture, no text, no watermark
```

**Dateiname: KD-35.jpg**
```
A child holding a tablet slightly away from their body with a startled expression, Brainy (cream cloud-shaped brain character, grey-blue glasses, peaceful closed eyes, gentle smile, holding a small red heart) gently placing a hand on their shoulder. modern children's book illustration, confident linework, smooth shading, vibrant warm colors, expressive detailed faces, realistic proportions, high resolution, no grain, no texture, no text, no watermark
```
