#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baut alle 16 großformatigen A4-Raummarkierungen (8 Schule + 8 Eltern) und fügt sie zu 2 PDFs
zusammen. Nutzt dieselben Karten-Definitionen wie build_all_cards_insel.py (SCHUL_CARDS/ELTERN_CARDS),
damit Name/Farbe/Badge konsistent bleiben."""
import os, sys
from PIL import Image
sys.path.insert(0, os.path.dirname(__file__))
from build_marker_insel import build_marker
from build_all_cards_insel import SCHUL_CARDS, ELTERN_CARDS, BILDER

OUT_SCHULE = "/sessions/kind-beautiful-ptolemy/mnt/outputs/insel_marker_schule/"
OUT_ELTERN = "/sessions/kind-beautiful-ptolemy/mnt/outputs/insel_marker_eltern/"
os.makedirs(OUT_SCHULE, exist_ok=True)
os.makedirs(OUT_ELTERN, exist_ok=True)

def build_set(cards, out_dir, prefix):
    pages = []
    for nr, name, badge_datei, (farbe, farbe_light), zweck, regeln, nutzen in cards:
        image_path = os.path.join(BILDER, badge_datei)
        out_path = os.path.join(out_dir, f"{prefix}-{nr:02d}_marker.png")
        img = build_marker(name, image_path, farbe, out_path)
        pages.append(img)
        print(f"{prefix}-{nr:02d} Markierung: {name}")
    return pages

def run():
    print("=== Schul-Set ===")
    schule_pages = build_set(SCHUL_CARDS, OUT_SCHULE, "SCHULE")
    out = "/sessions/kind-beautiful-ptolemy/mnt/outputs/KLARTEXT_Insel-Set_Raummarkierungen_Schule.pdf"
    schule_pages[0].save(out, save_all=True, append_images=schule_pages[1:], resolution=300)
    print(f"PDF fertig: {out} ({len(schule_pages)} Seiten)")

    print("=== Eltern-Set ===")
    eltern_pages = build_set(ELTERN_CARDS, OUT_ELTERN, "ELTERN")
    out = "/sessions/kind-beautiful-ptolemy/mnt/outputs/KLARTEXT_Insel-Set_Raummarkierungen_Eltern.pdf"
    eltern_pages[0].save(out, save_all=True, append_images=eltern_pages[1:], resolution=300)
    print(f"PDF fertig: {out} ({len(eltern_pages)} Seiten)")

if __name__ == "__main__":
    run()
