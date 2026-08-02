#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baut die druckfertige PDF aus allen 30 Geschichtenkarten + Stoppschild-Bonuskarte. Wird VOR der
Bildgenerierung testweise mit Platzhaltern gebaut (Textlayout-Prüfung), nach Bildgenerierung erneut
mit build_all_cards_geschichtenkarten.py neu gerendert."""
from PIL import Image, ImageDraw, ImageFont
import os, sys
Image.init()
sys.path.insert(0, os.path.dirname(__file__))
from build_booklet_geschichtenkarten import anleitung_seite1, anleitung_seite2

KARTEN_DIR = "/sessions/kind-beautiful-ptolemy/mnt/outputs/geschichtenkarten_komplett/"
STOPPSCHILD_DIR = "/sessions/kind-beautiful-ptolemy/mnt/outputs/stoppschild_bonuskarte/"
OUT_PDF = "/sessions/kind-beautiful-ptolemy/mnt/outputs/KLARTEXT_Geschichtenkarten-Deck_komplett.pdf"
# (Entwurfsname KLARTEXT_Geschichtenkarten-Deck_ENTWURF_ohne_Bilder.pdf entfaellt jetzt, da alle
# 30 Illustrationen vorliegen)

DPI = 300
MM = DPI / 25.4
def mm(v): return int(round(v * MM))

NAVY = (27, 58, 75)
KT_MUTED = (122, 112, 96)
KT_INK = (45, 45, 45)

F_SERIF_BOLD = "/usr/share/fonts/truetype/crosextra/Caladea-Bold.ttf"
F_SANS_REG = "/usr/share/fonts/truetype/lato/Lato-Regular.ttf"
F_SANS_BOLD = "/usr/share/fonts/truetype/lato/Lato-Bold.ttf"

def build_cover():
    W, H = mm(210), mm(297)
    img = Image.new("RGB", (W, H), (255, 255, 255))
    d = ImageDraw.Draw(img)

    kopf_h = mm(60)
    d.rectangle((0, 0, W, kopf_h), fill=NAVY)
    logo_s = mm(20)
    logo_y = (kopf_h - logo_s) // 2
    d.rounded_rectangle((mm(20), logo_y, mm(20) + logo_s, logo_y + logo_s), radius=mm(4),
                         fill=(27, 58, 75), outline=(110, 198, 160), width=mm(1.2))
    f_logo = ImageFont.truetype(F_SERIF_BOLD, mm(11))
    d.text((mm(20) + logo_s / 2, logo_y + logo_s / 2), "K", font=f_logo, anchor="mm", fill=(255, 255, 255))

    f_titel = ImageFont.truetype(F_SERIF_BOLD, mm(11))
    d.text((mm(48), mm(21)), "KLARTEXT-Mentoring", font=f_titel, fill=(255, 255, 255))
    f_sub = ImageFont.truetype(F_SANS_REG, mm(5.5))
    d.text((mm(48), mm(34)), "Handlungskarten · Geschichtenkarten", font=f_sub, fill=(210, 225, 220))

    haupt_text = "Geschichtenkarten-Deck"
    haupt_size = 19.0
    f_haupt = ImageFont.truetype(F_SERIF_BOLD, mm(haupt_size))
    while d.textlength(haupt_text, font=f_haupt) > W - mm(40) and haupt_size > 8:
        haupt_size -= 0.5
        f_haupt = ImageFont.truetype(F_SERIF_BOLD, mm(haupt_size))
    d.text((mm(20), mm(88)), haupt_text, font=f_haupt, fill=NAVY)

    f_haupt2 = ImageFont.truetype(F_SANS_BOLD, mm(7))
    d.text((mm(20), mm(122)), "30 Karten + Bonuskarte · Brainy und das Thema Mobbing", font=f_haupt2, fill=KT_INK)

    f_label = ImageFont.truetype(F_SANS_BOLD, mm(5.5))
    d.text((mm(20), mm(140)), "DIE 3 SETS", font=f_label, fill=NAVY)
    sets = ["Set A · Brainy erlebt Mobbing (A1–A10)", "Set B · Brainy hilft anderen (B1–B10)",
            "Set C · Brainy lernt Strategien (C1–C10)", "+ Bonuskarte: Stoppschild"]
    f_thema = ImageFont.truetype(F_SANS_REG, mm(5.6))
    row_h = mm(9.4)
    for i, t in enumerate(sets):
        x = mm(20)
        y = mm(150) + i * row_h
        d.ellipse((x, y + mm(2.0), x + mm(2.6), y + mm(4.6)), fill=NAVY)
        d.text((x + mm(6), y), t, font=f_thema, fill=KT_INK)

    box_y = mm(240)
    box_h = mm(22)
    d.rounded_rectangle((mm(20), box_y, W - mm(20), box_y + box_h), radius=mm(3), fill=(232, 241, 238))
    f_status_l = ImageFont.truetype(F_SANS_BOLD, mm(6))
    f_status = ImageFont.truetype(F_SANS_REG, mm(5.6))
    d.text((mm(28), box_y + mm(6)), "STAND DIESER AUSGABE", font=f_status_l, fill=NAVY)
    d.text((mm(28), box_y + mm(13)), "30 Karten + Bonuskarte vollständig, inkl. Illustrationen.",
           font=f_status, fill=KT_INK)

    f_foot = ImageFont.truetype(F_SANS_REG, mm(5))
    d.text((mm(20), H - mm(18)), "KLARTEXT-Mentoring · © 2026 Anja Jolk", font=f_foot, fill=KT_MUTED)
    return img

def run():
    pages = [build_cover(), anleitung_seite1(), anleitung_seite2()]

    fehlt = []
    ids = [f"A{n}" for n in range(1, 11)] + [f"B{n}" for n in range(1, 11)] + [f"C{n}" for n in range(1, 11)]
    for id_text in ids:
        vorn = os.path.join(KARTEN_DIR, f"{id_text}_Vorderseite.png")
        hinten = os.path.join(KARTEN_DIR, f"{id_text}_Rueckseite.png")
        if os.path.exists(vorn) and os.path.exists(hinten):
            pages.append(Image.open(vorn).convert("RGB"))
            pages.append(Image.open(hinten).convert("RGB"))
        else:
            fehlt.append(id_text)

    stopp_vorn = os.path.join(STOPPSCHILD_DIR, "Stoppschild_Vorderseite.png")
    stopp_hinten = os.path.join(STOPPSCHILD_DIR, "Stoppschild_Rueckseite.png")
    if os.path.exists(stopp_vorn) and os.path.exists(stopp_hinten):
        pages.append(Image.open(stopp_vorn).convert("RGB"))
        pages.append(Image.open(stopp_hinten).convert("RGB"))
    else:
        fehlt.append("Stoppschild")

    first, rest = pages[0], pages[1:]
    first.save(OUT_PDF, save_all=True, append_images=rest, resolution=DPI)
    print(f"PDF fertig: {OUT_PDF} ({len(pages)} Seiten)")
    if fehlt:
        print(f"Fehlt: {fehlt}")

if __name__ == "__main__":
    run()
