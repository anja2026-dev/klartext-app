#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baut 4 A4-Drucksheets (eine pro Zone, 10 Token-Karten je Sheet, 2x5-Raster zum Ausschneiden).
Zusammen ergeben die 4 Sheets komplette Token-Sets für bis zu 10 Jugendliche (je 1 Karte pro Zone
zusammenstellen). Gleiche Bilder/Farben wie die Begleitkarten (build_all_cards_zonen.py)."""
import os, sys
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, os.path.dirname(__file__))
from build_token_zonen import build_token, CARD_W, CARD_H, mm
from build_all_cards_zonen import SCHUL_CARDS, BILDER

OUT_DIR = "/sessions/kind-beautiful-ptolemy/mnt/outputs/zonen_token_sheets/"
os.makedirs(OUT_DIR, exist_ok=True)

F_SANS_BOLD = "/usr/share/fonts/truetype/lato/Lato-Bold.ttf"
F_SANS_REG = "/usr/share/fonts/truetype/lato/Lato-Regular.ttf"

A4_W, A4_H = mm(210), mm(297)
COLS, ROWS = 2, 5
GAP = mm(4)

def build_sheet(name, badge_datei, farbe, out_path):
    token = build_token(name, os.path.join(BILDER, badge_datei), farbe)

    total_w = COLS * CARD_W + (COLS - 1) * GAP
    total_h = ROWS * CARD_H + (ROWS - 1) * GAP
    left0 = (A4_W - total_w) // 2
    top0 = mm(28)

    sheet = Image.new("RGB", (A4_W, A4_H), (255, 255, 255))
    d = ImageDraw.Draw(sheet)

    f_head = ImageFont.truetype(F_SANS_BOLD, mm(6))
    d.text((mm(15), mm(12)), f"Zonen-Set · Token-Karten · {name}", font=f_head, fill=(35, 35, 35))
    f_sub = ImageFont.truetype(F_SANS_REG, mm(3.5))
    d.text((mm(15), mm(20)), "Ausschneiden, laminieren. Pro Person 1 Karte je Zonen-Sheet sammeln.",
           font=f_sub, fill=(100, 100, 100))

    for r in range(ROWS):
        for c in range(COLS):
            x = left0 + c * (CARD_W + GAP)
            y = top0 + r * (CARD_H + GAP)
            sheet.paste(token, (x, y))
            d.rectangle((x, y, x + CARD_W, y + CARD_H), outline=(200, 200, 200), width=2)

    sheet.save(out_path, dpi=(300, 300))
    return sheet

def run():
    pages = []
    for nr, name, badge_datei, (farbe, farbe_light), *_ in SCHUL_CARDS:
        out_path = os.path.join(OUT_DIR, f"TOKEN-{name.replace(' ', '_')}.png")
        pages.append(build_sheet(name, badge_datei, farbe, out_path))
        print(f"Sheet fertig: {name}")
    out_pdf = "/sessions/kind-beautiful-ptolemy/mnt/outputs/KLARTEXT_Zonen-Set_Token-Karten.pdf"
    pages[0].save(out_pdf, save_all=True, append_images=pages[1:], resolution=300)
    print(f"PDF fertig: {out_pdf} ({len(pages)} Seiten)")

if __name__ == "__main__":
    run()
