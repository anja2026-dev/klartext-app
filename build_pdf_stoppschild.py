#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kleine PDF fuer die Stoppschild-Bonuskarte, damit sie wie alle anderen Bausteine als eigenes
Dokument vorliegt, bis das Geschichtenkarten-Deck steht und sie dort eingebunden wird."""
from PIL import Image
Image.init()

KARTEN_DIR = "/sessions/kind-beautiful-ptolemy/mnt/outputs/stoppschild_bonuskarte/"
OUT_PDF = "/sessions/kind-beautiful-ptolemy/mnt/outputs/KLARTEXT_Mobbing_Stoppschild-Bonuskarte.pdf"
DPI = 300

def run():
    vorn = Image.open(KARTEN_DIR + "Stoppschild_Vorderseite.png").convert("RGB")
    hinten = Image.open(KARTEN_DIR + "Stoppschild_Rueckseite.png").convert("RGB")
    vorn.save(OUT_PDF, save_all=True, append_images=[hinten], resolution=DPI)
    print(f"PDF fertig: {OUT_PDF} (2 Seiten)")

if __name__ == "__main__":
    run()
