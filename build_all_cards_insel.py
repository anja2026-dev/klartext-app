#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baut alle Insel-Begleitkarten: 8 fürs Schul-Set + 8 fürs Eltern-Set (6 Badges geteilt, 10 Bilder
insgesamt). Text aus Anjas Originalvorlagen (Insel-Set für pädagogische Raumstrukturierung /
Insel-Set für Eltern), Farben aus INSEL-Set_Konzept_und_Barometer-Integration.md Rev. 2."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from build_card_insel import build_front, build_back

BILDER = "/sessions/kind-beautiful-ptolemy/mnt/klartext-app/bilder/insel/"
OUT_SCHULE = "/sessions/kind-beautiful-ptolemy/mnt/outputs/insel_karten_schule/"
OUT_ELTERN = "/sessions/kind-beautiful-ptolemy/mnt/outputs/insel_karten_eltern/"
os.makedirs(OUT_SCHULE, exist_ok=True)
os.makedirs(OUT_ELTERN, exist_ok=True)

TUERKIS  = ((38, 166, 154), (224, 242, 239))
BLAU     = ((33, 150, 243), (227, 242, 253))
PETROL   = ((0, 96, 100),   (217, 232, 233))
AQUA     = ((77, 208, 225), (224, 247, 250))
LILA     = ((126, 87, 194), (237, 231, 246))
INDIGO   = ((63, 81, 181),  (227, 229, 246))
MAGENTA  = ((171, 71, 188), (243, 229, 246))
TAUPE    = ((120, 144, 156),(232, 237, 239))
FLIEDER  = ((179, 157, 219),(241, 237, 249))

# (nr, name, badge_datei, farbe, zweck, [regeln], [nutzen])
SCHUL_CARDS = [
    (1, "Regel-Insel", "INSEL-REGEL.jpg", TUERKIS,
     "Ort für kurze Klärungen, Mini-Regelgespräche und Orientierung.",
     ["Nur kurze Gespräche (1–2 Minuten)", "Keine Diskussionen", "Klärung → zurück zur Aktivität"],
     ["Kinder wissen, wo sie Unsicherheiten klären können.",
      "Verhindert, dass Regelgespräche den Raum blockieren."]),
    (2, "Ruhe-Insel", "INSEL-RUHE.jpg", BLAU,
     "Selbstregulation, Reizreduktion, Rückzug.",
     ["Leise sein", "Nicht sprechen", "Max. 5 Minuten",
      "Keine Medien oder Geräuschspielzeuge (Ausnahme: Noise-Cancelling-Kopfhörer)"],
     ["Kinder können sich selbstständig beruhigen.",
      "Unterstützt Emotionsregulation und Reizfilterung."]),
    (3, "Arbeits-Insel", "INSEL-ARBEIT.jpg", PETROL,
     "Fokus, Aufgabenbearbeitung, Lernzeit.",
     ["Konzentration", "Keine Gespräche", "Aufgaben sichtbar (Mini-Whiteboard)"],
     ["Klare Struktur für Kinder mit Fokus-Schwierigkeiten.",
      "Minimiert Ablenkung und Chaos."]),
    (4, "Bewegungs-Insel", "INSEL-BEWEGUNG.jpg", AQUA,
     "Motorische Pausen, Energieabbau.",
     ["30–60 Sekunden", "Nur definierte Bewegungen (z. B. 3 Sprünge, 5 Schritte)", "Kein Rennen"],
     ["Kinder können Energie regulieren, ohne den Raum zu stören.",
      "Unterstützt Impulskontrolle."]),
    (5, "Kreativ-Insel", "INSEL-KREATIV.jpg", LILA,
     "Zeichnen, Basteln, sensorische Materialien.",
     ["Materialien bleiben auf der Insel", "Kein Chaos mitnehmen", "5–10 Minuten"],
     ["Fördert Ausdruck, Feinmotorik und Selbstwirksamkeit."]),
    (6, "Gesprächs-Insel", "INSEL-GESPRAECH.jpg", INDIGO,
     "Kurze 1:1-Gespräche.",
     ["Max. 3 Minuten", "Keine Konfliktbearbeitung (dafür Regel-Insel)"],
     ["Strukturierte Gesprächsangebote ohne Raumstörung."]),
    (7, "Emotions-Insel", "INSEL-EMOTION.jpg", MAGENTA,
     "Gefühle benennen, Emotionskarten nutzen.",
     ["Gefühl benennen", "Passende Karte auswählen", "Kurze Reflexion"],
     ["Unterstützt Emotionskompetenz und Selbstwahrnehmung."]),
    (8, "Material-Insel", "INSEL-MATERIAL.jpg", TAUPE,
     "Ort für Materialien, die Kinder selbstständig holen dürfen.",
     ["Nur erlaubte Materialien", "Nach Nutzung zurückbringen"],
     ["Fördert Selbstständigkeit und Ordnung."]),
]

ELTERN_CARDS = [
    (1, "Ruhe-Insel", "INSEL-RUHE.jpg", BLAU,
     "Sofa-Ecke, Teppich oder ein kleines Kissen zuhause.",
     ["Leise sein", "3–5 Minuten", "Kein Bildschirm"],
     ["Kind kann sich selbst beruhigen.", "Verhindert Eskalationen."]),
    (2, "Emotions-Insel", "INSEL-EMOTION.jpg", MAGENTA,
     "Kleiner Tisch oder Wandbereich.",
     ["Gefühl benennen", "Passende Karte wählen", "Kurze Erklärung"],
     ["Fördert Emotionskompetenz.", "Entlastet Eltern bei Konflikten."]),
    (3, "Arbeits-Insel", "INSEL-ARBEIT.jpg", PETROL,
     "Fester Tischplatz für Hausaufgaben.",
     ["Nur Hausaufgaben", "10–15 Minuten Fokus", "Timer nutzen"],
     ["Weniger Streit bei Hausaufgaben.", "Klare Struktur."]),
    (4, "Bewegungs-Insel", "INSEL-BEWEGUNG.jpg", AQUA,
     "Flur, Teppich oder Balkon.",
     ["30–60 Sekunden Bewegung", "Keine Rennen"],
     ["Energieabbau ohne Chaos.", "Hilft bei ADHS/Unruhe."]),
    (5, "Familien-Regel-Insel", "INSEL-REGEL.jpg", TUERKIS,
     "Wandbereich mit Mini-Poster.",
     ["Kurze Klärungen", "Keine Diskussionen"],
     ["Weniger Streit.", "Klare Orientierung."]),
    (6, "Übergangs-Insel", "INSEL-UEBERGANG.jpg", FLIEDER,
     "Flur oder Kinderzimmer, für Morgen und Abend.",
     ["3 Schritte (z. B. Schuhe, Jacke, Tasche)"],
     ["Weniger Stress bei Übergängen."]),
    (7, "Geschwister-Konflikt-Insel", "INSEL-KONFLIKT.jpg", TAUPE,
     "Neutraler Platz.",
     ["Jeder spricht 1 Satz", "Lösung suchen"],
     ["Weniger Geschwisterstreit.", "Struktur statt Chaos."]),
    (8, "Eltern-Kind-Gesprächs-Insel", "INSEL-GESPRAECH.jpg", INDIGO,
     "Sofa oder Stuhl.",
     ["2 Minuten", "Nur ein Thema"],
     ["Klare Kommunikation.", "Weniger Überforderung."]),
]

def build_set(cards, out_dir, set_label, prefix):
    total = len(cards)
    for nr, name, badge_datei, (farbe, farbe_light), zweck, regeln, nutzen in cards:
        card = dict(nr=nr, total=total, name=name, set_label=set_label,
                    farbe=farbe, farbe_light=farbe_light, zweck=zweck, regeln=regeln, nutzen=nutzen)
        image_path = os.path.join(BILDER, badge_datei)
        front_out = os.path.join(out_dir, f"{prefix}-{nr:02d}_front.png")
        back_out = os.path.join(out_dir, f"{prefix}-{nr:02d}_back.png")
        build_front(card, image_path, front_out)
        build_back(card, back_out)
        status = "mit Bild" if os.path.exists(image_path) else "OHNE BILD"
        print(f"{prefix}-{nr:02d}: {status} – {name}")

def run():
    print("=== Schul-Set ===")
    build_set(SCHUL_CARDS, OUT_SCHULE, "INSEL-SET · SCHULE", "SCHULE")
    print("=== Eltern-Set ===")
    build_set(ELTERN_CARDS, OUT_ELTERN, "INSEL-SET · ZUHAUSE", "ELTERN")

if __name__ == "__main__":
    run()
