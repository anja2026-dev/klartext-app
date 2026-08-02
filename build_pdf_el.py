#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baut die druckfertige PDF aus allen fertigen EL-Basis-Karten (30 von 30)."""
from PIL import Image, ImageDraw, ImageFont
import os, sys
Image.init()
sys.path.insert(0, os.path.dirname(__file__))
from build_booklet_el import (anleitung_seite1, anleitung_seite2, methodik_seite, glossar_seite,
                               quellen_seite1, quellen_seite2, GLOSSAR)

KARTEN_DIR = "/sessions/kind-beautiful-ptolemy/mnt/outputs/el_karten_komplett/"
OUT_PDF = "/sessions/kind-beautiful-ptolemy/mnt/outputs/KLARTEXT_EL-Deck_Basis_komplett.pdf"

DPI = 300
MM = DPI / 25.4
def mm(v): return int(round(v * MM))

EL = (191, 91, 62)
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
    d.rectangle((0, 0, W, kopf_h), fill=EL)
    logo_s = mm(20)
    logo_y = (kopf_h - logo_s) // 2
    d.rounded_rectangle((mm(20), logo_y, mm(20) + logo_s, logo_y + logo_s), radius=mm(4),
                         fill=(27, 58, 75), outline=(110, 198, 160), width=mm(1.2))
    f_logo = ImageFont.truetype(F_SERIF_BOLD, mm(11))
    d.text((mm(20) + logo_s / 2, logo_y + logo_s / 2), "K", font=f_logo, anchor="mm", fill=(255, 255, 255))

    f_titel = ImageFont.truetype(F_SERIF_BOLD, mm(11))
    d.text((mm(48), mm(21)), "KLARTEXT-Mentoring", font=f_titel, fill=(255, 255, 255))
    f_sub = ImageFont.truetype(F_SANS_REG, mm(5.5))
    d.text((mm(48), mm(34)), "Systemische Coaching-Impulskarten", font=f_sub, fill=(250, 232, 224))

    f_haupt = ImageFont.truetype(F_SERIF_BOLD, mm(34))
    d.text((mm(20), mm(90)), "EL-Deck", font=f_haupt, fill=EL)

    f_haupt2 = ImageFont.truetype(F_SANS_BOLD, mm(7))
    d.text((mm(20), mm(140)), "30 Coaching-Impulskarten für Eltern", font=f_haupt2, fill=KT_INK)

    f_themen_label = ImageFont.truetype(F_SANS_BOLD, mm(5.5))
    d.text((mm(20), mm(158)), "THEMENBEREICHE", font=f_themen_label, fill=EL)

    themen = ["Die eigene Rolle als Elternteil", "Mein Kind verstehen",
              "Kommunikation im Familienalltag", "Wenn es schwierig wird",
              "Alltag & Praxissituationen", "Selbstfürsorge als Elternteil"]
    f_thema = ImageFont.truetype(F_SANS_REG, mm(6.2))
    row_h = mm(11)
    for i, t in enumerate(themen):
        x = mm(20)
        y = mm(168) + i * row_h
        d.ellipse((x, y + mm(2.2), x + mm(2.6), y + mm(4.8)), fill=EL)
        d.text((x + mm(6), y), t, font=f_thema, fill=KT_INK)

    box_y = mm(240)
    box_h = mm(22)
    d.rounded_rectangle((mm(20), box_y, W - mm(20), box_y + box_h), radius=mm(3), fill=(250, 235, 227))
    f_status_l = ImageFont.truetype(F_SANS_BOLD, mm(6))
    f_status = ImageFont.truetype(F_SANS_REG, mm(5.6))
    d.text((mm(28), box_y + mm(6)), "STAND DIESER AUSGABE", font=f_status_l, fill=EL)
    d.text((mm(28), box_y + mm(13)), "EL-Basis vollständig (30 Karten). Zusatzblöcke folgen separat.",
           font=f_status, fill=KT_INK)

    f_foot = ImageFont.truetype(F_SANS_REG, mm(5))
    d.text((mm(20), H - mm(18)), "KLARTEXT-Mentoring · © 2026 Anja Jolk", font=f_foot, fill=KT_MUTED)
    return img

def run():
    pages = [build_cover(), anleitung_seite1(), anleitung_seite2(), methodik_seite(),
             glossar_seite(GLOSSAR[:3], "Glossar · 1/2",
                 intro="Kurz erklärt: Begriffe, die auf den Karten oder in dieser Anleitung vorkommen "
                       "und nicht selbsterklärend sind."),
             glossar_seite(GLOSSAR[3:], "Glossar · 2/2"),
             quellen_seite1(), quellen_seite2()]

    for nr in range(1, 31):
        vorn = os.path.join(KARTEN_DIR, f"EL-{nr:02d}_Vorderseite.png")
        hinten = os.path.join(KARTEN_DIR, f"EL-{nr:02d}_Rueckseite.png")
        if os.path.exists(vorn) and os.path.exists(hinten):
            pages.append(Image.open(vorn).convert("RGB"))
            pages.append(Image.open(hinten).convert("RGB"))
        else:
            print(f"Fehlt: EL-{nr:02d}")

    first, rest = pages[0], pages[1:]
    first.save(OUT_PDF, save_all=True, append_images=rest, resolution=DPI)
    print(f"PDF fertig: {OUT_PDF} ({len(pages)} Seiten)")

if __name__ == "__main__":
    run()
