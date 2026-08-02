#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baut die Zonen-Begleitkarten (Schule + Eltern) für Jugendliche. Nutzt denselben Karten-
Renderer wie das Insel-Set (build_card_insel.py – vollständig generisch, keine Insel-spezifischen
Texte im Code), nur mit gedeckten Zonen-Farben statt Insel-Farben und "ZONEN-SET" als Label."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from build_card_insel import build_front, build_back

BILDER = "/sessions/kind-beautiful-ptolemy/mnt/klartext-app/bilder/zonen/"
OUT_SCHULE = "/sessions/kind-beautiful-ptolemy/mnt/outputs/zonen_karten_schule/"
OUT_ELTERN = "/sessions/kind-beautiful-ptolemy/mnt/outputs/zonen_karten_eltern/"
os.makedirs(OUT_SCHULE, exist_ok=True)
os.makedirs(OUT_ELTERN, exist_ok=True)

MOOS     = ((85, 107, 79),   (228, 233, 224))
GRAPHIT  = ((55, 71, 79),    (222, 227, 229))
ROST     = ((141, 85, 58),   (238, 226, 219))
SCHIEFER = ((91, 122, 128),  (224, 233, 234))

# (nr, name, badge_datei, farbe, zweck, [regeln], [nutzen])
SCHUL_CARDS = [
    (1, "Rückzugs-Zone", "ZONE-RUECKZUG.jpg", MOOS,
     "Reizreduktion – sich für einen Moment zurückziehen dürfen, ohne sich zu rechtfertigen.",
     ["Zeitlich begrenzt (z. B. 5–10 Minuten)", "Kein Gespräch erzwingen",
      "Danach freiwillige Rückmeldung, keine Pflicht"],
     ["Selbstregulation ohne Bloßstellung.", "Verhindert Eskalation durch Reizüberflutung."]),
    (2, "Fokus-Zone", "ZONE-FOKUS.jpg", GRAPHIT,
     "Ungestörtes konzentriertes Arbeiten, z. B. bei Prüfungsvorbereitung oder Reizempfindlichkeit.",
     ["Keine Gespräche", "Feste Arbeitszeit vereinbaren", "Ergebnis sichtbar machen (z. B. Checkliste)"],
     ["Weniger Ablenkung.", "Unterstützt bei ADHS/Konzentrationsschwierigkeiten."]),
    (3, "Klärungs-Zone", "ZONE-KLAERUNG.jpg", ROST,
     "Kurze, sachliche Klärung eines Konflikts oder einer Regelfrage, ohne Publikum.",
     ["Max. 5 Minuten", "Auf Augenhöhe sprechen, nicht von oben herab", "Lösung statt Bestrafung"],
     ["Deeskalation.", "Konfliktklärung wird als fair statt als Kontrolle erlebt."]),
    (4, "Gesprächs-Zone", "ZONE-GESPRAECH.jpg", SCHIEFER,
     "1:1-Gespräch mit Vertrauensperson (LK/INGRA), auf Wunsch der/des Jugendlichen.",
     ["Freiwillig, nie erzwungen", "Vertraulich, soweit rechtlich möglich", "Klar begrenzte Zeit"],
     ["Stärkt Vertrauen.", "Erwachsene werden als ansprechbar erlebt, nicht nur als Autorität."]),
]

ELTERN_CARDS = [
    (1, "Rückzugs-Zone", "ZONE-RUECKZUG.jpg", MOOS,
     "Ein Rückzugsort zuhause (Zimmer, ruhige Ecke), den der/die Jugendliche ohne Erklärung nutzen darf.",
     ["Kein „Was ist los?“ beim Reingehen", "Feste Zeit vereinbaren (z. B. 15 Minuten)",
      "Danach wieder ansprechbar"],
     ["Weniger Konflikte durch Überforderung.", "Jugendliche lernen, eigene Grenzen zu erkennen."]),
    (2, "Fokus-Zone", "ZONE-FOKUS.jpg", GRAPHIT,
     "Fester Arbeitsplatz für Hausaufgaben/Lernen, ohne Familienlärm.",
     ["Handy weglegen", "Timer nutzen (z. B. 25 Minuten)", "Klare Start- und Endzeit"],
     ["Weniger Streit ums Lernen.", "Stärkt Selbstständigkeit."]),
    (3, "Klärungs-Zone", "ZONE-KLAERUNG.jpg", ROST,
     "Neutraler Ort für Familienkonflikte, statt mitten im Wohnzimmer oder vor Geschwistern.",
     ["Jede Person spricht aus, ohne unterbrochen zu werden", "Ich-Botschaften statt Vorwürfe"],
     ["Weniger eskalierende Streits.", "Jugendliche fühlen sich ernst genommen."]),
    (4, "Gesprächs-Zone", "ZONE-GESPRAECH.jpg", SCHIEFER,
     "Ruhiger Moment für ein Gespräch zwischen Elternteil und Jugendlichem, ohne Ablenkung.",
     ["Ein Thema pro Gespräch", "Zuhören vor Bewerten", "Kein Handy nebenbei"],
     ["Bessere Kommunikation.", "Weniger „Wir reden nie“-Gefühl."]),
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
    build_set(SCHUL_CARDS, OUT_SCHULE, "ZONEN-SET · SCHULE", "SCHULE")
    print("=== Eltern-Set ===")
    build_set(ELTERN_CARDS, OUT_ELTERN, "ZONEN-SET · ZUHAUSE", "ELTERN")

if __name__ == "__main__":
    run()
