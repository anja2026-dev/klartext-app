#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baut die druckfertige PDF aus allen 32 OGS-Basis-Karten. Erlaubt Testrender ohne Bilder
(Platzhalter) – druckt Warnung statt abzubrechen."""
from PIL import Image, ImageDraw, ImageFont
import os, sys
Image.init()
sys.path.insert(0, os.path.dirname(__file__))
from build_booklet_ogs import (anleitung_seite1, anleitung_seite2, quellen_seite1, quellen_seite1b,
                                quellen_seite2)

KARTEN_DIR = "/sessions/kind-beautiful-ptolemy/mnt/outputs/ogs_karten_komplett/"
BILD_DIR = "/sessions/kind-beautiful-ptolemy/mnt/klartext-app/bilder/ogs/"
OUT_PDF = "/sessions/kind-beautiful-ptolemy/mnt/outputs/KLARTEXT_OGS-Basis-Deck_komplett.pdf"

DPI = 300
MM = DPI / 25.4
def mm(v): return int(round(v * MM))

OGS = (139, 195, 74)
KT_MUTED = (122, 112, 96)
KT_INK = (45, 45, 45)

F_SERIF_BOLD = "/usr/share/fonts/truetype/crosextra/Caladea-Bold.ttf"
F_SANS_REG = "/usr/share/fonts/truetype/lato/Lato-Regular.ttf"
F_SANS_BOLD = "/usr/share/fonts/truetype/lato/Lato-Bold.ttf"

def build_cover(entwurf=False):
    W, H = mm(210), mm(297)
    img = Image.new("RGB", (W, H), (255, 255, 255))
    d = ImageDraw.Draw(img)

    kopf_h = mm(60)
    d.rectangle((0, 0, W, kopf_h), fill=OGS)
    logo_s = mm(20)
    logo_y = (kopf_h - logo_s) // 2
    d.rounded_rectangle((mm(20), logo_y, mm(20) + logo_s, logo_y + logo_s), radius=mm(4),
                         fill=(27, 58, 75), outline=(110, 198, 160), width=mm(1.2))
    f_logo = ImageFont.truetype(F_SERIF_BOLD, mm(11))
    d.text((mm(20) + logo_s / 2, logo_y + logo_s / 2), "K", font=f_logo, anchor="mm", fill=(255, 255, 255))

    f_titel = ImageFont.truetype(F_SERIF_BOLD, mm(11))
    d.text((mm(48), mm(21)), "KLARTEXT-Mentoring", font=f_titel, fill=(255, 255, 255))
    f_sub = ImageFont.truetype(F_SANS_REG, mm(5.5))
    d.text((mm(48), mm(34)), "Reflexionskarten · Offener Ganztag", font=f_sub, fill=(240, 248, 230))

    haupt_text = "OGS-Basis-Deck"
    haupt_max_w = W - mm(40)
    size = 22.0
    f_haupt = ImageFont.truetype(F_SERIF_BOLD, mm(size))
    while d.textlength(haupt_text, font=f_haupt) > haupt_max_w and size > 10:
        size -= 0.5
        f_haupt = ImageFont.truetype(F_SERIF_BOLD, mm(size))
    d.text((mm(20), mm(90)), haupt_text, font=f_haupt, fill=OGS)

    f_haupt2 = ImageFont.truetype(F_SANS_BOLD, mm(7))
    d.text((mm(20), mm(128)), "32 Karten für pädagogische Fachkräfte im Ganztag", font=f_haupt2, fill=KT_INK)

    f_themen_label = ImageFont.truetype(F_SANS_BOLD, mm(5.5))
    d.text((mm(20), mm(146)), "THEMENBLÖCKE", font=f_themen_label, fill=OGS)

    themen = ["Gruppendynamik verstehen (4)", "Rituale nutzen (4)", "Konflikte begleiten (4)",
              "Regeln vermitteln (4)", "Beziehungsarbeit im OGS (4)", "Selbstständigkeit fördern (4)",
              "Übergänge gestalten (4)", "Rahmen und Zusammenarbeit (4)"]
    f_thema = ImageFont.truetype(F_SANS_REG, mm(5.6))
    row_h = mm(8.4)
    for i, t in enumerate(themen):
        x = mm(20)
        y = mm(155) + i * row_h
        d.ellipse((x, y + mm(1.9), x + mm(2.4), y + mm(4.3)), fill=OGS)
        d.text((x + mm(6), y), t, font=f_thema, fill=KT_INK)

    box_y = mm(240)
    box_h = mm(22)
    d.rounded_rectangle((mm(20), box_y, W - mm(20), box_y + box_h), radius=mm(3), fill=(238, 246, 227))
    f_status_l = ImageFont.truetype(F_SANS_BOLD, mm(6))
    f_status = ImageFont.truetype(F_SANS_REG, mm(5.6))
    d.text((mm(28), box_y + mm(6)), "STAND DIESER AUSGABE", font=f_status_l, fill=OGS)
    status_text = ("ENTWURF – Layout-Testdruck ohne Bilder, Texte final." if entwurf else
                   "32 Karten vollständig, Bilder final.")
    d.text((mm(28), box_y + mm(13)), status_text, font=f_status, fill=KT_INK)

    f_foot = ImageFont.truetype(F_SANS_REG, mm(5))
    d.text((mm(20), H - mm(18)), "KLARTEXT-Mentoring · © 2026 Anja Jolk", font=f_foot, fill=KT_MUTED)
    return img

def run():
    bilder_fehlen = []
    for nr in range(1, 33):
        hat_bild = any(os.path.exists(os.path.join(BILD_DIR, f"OGS-{nr:02d}{ext}"))
                       for ext in (".jpg", ".png", ".jpeg"))
        if not hat_bild:
            bilder_fehlen.append(nr)

    entwurf = len(bilder_fehlen) > 0
    pages = [build_cover(entwurf=entwurf), anleitung_seite1(), anleitung_seite2(),
             quellen_seite1(), quellen_seite1b(), quellen_seite2()]

    for nr in range(1, 33):
        vorn = os.path.join(KARTEN_DIR, f"OGS-{nr:02d}_front.png")
        hinten = os.path.join(KARTEN_DIR, f"OGS-{nr:02d}_back.png")
        if os.path.exists(vorn) and os.path.exists(hinten):
            pages.append(Image.open(vorn).convert("RGB"))
            pages.append(Image.open(hinten).convert("RGB"))

    out_path = OUT_PDF.replace(".pdf", "_ENTWURF.pdf") if entwurf else OUT_PDF
    first, rest = pages[0], pages[1:]
    first.save(out_path, save_all=True, append_images=rest, resolution=DPI)
    print(f"PDF fertig: {out_path} ({len(pages)} Seiten)")
    if bilder_fehlen:
        print(f"Hinweis: {len(bilder_fehlen)} Karten noch ohne Quellbild (Platzhalter-Fläche): {bilder_fehlen}")

if __name__ == "__main__":
    run()
