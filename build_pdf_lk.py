#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baut die druckfertige PDF aus allen fertigen LK-Basis-Karten (50 von 50)."""
from PIL import Image, ImageDraw, ImageFont
import os, sys
Image.init()
sys.path.insert(0, os.path.dirname(__file__))
from build_booklet_lk import (anleitung_seite1, anleitung_seite2, methodik_seite, glossar_seite,
                               quellen_seite1, quellen_seite1b, quellen_seite2, GLOSSAR)

KARTEN_DIR = "/sessions/kind-beautiful-ptolemy/mnt/outputs/lk_karten_komplett/"
OUT_PDF = "/sessions/kind-beautiful-ptolemy/mnt/outputs/KLARTEXT_LK-Deck_Basis_komplett.pdf"

DPI = 300
MM = DPI / 25.4
def mm(v): return int(round(v * MM))

LK = (107, 78, 113)
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
    d.rectangle((0, 0, W, kopf_h), fill=LK)
    logo_s = mm(20)
    logo_y = (kopf_h - logo_s) // 2
    d.rounded_rectangle((mm(20), logo_y, mm(20) + logo_s, logo_y + logo_s), radius=mm(4),
                         fill=(27, 58, 75), outline=(110, 198, 160), width=mm(1.2))
    f_logo = ImageFont.truetype(F_SERIF_BOLD, mm(11))
    d.text((mm(20) + logo_s / 2, logo_y + logo_s / 2), "K", font=f_logo, anchor="mm", fill=(255, 255, 255))

    f_titel = ImageFont.truetype(F_SERIF_BOLD, mm(11))
    d.text((mm(48), mm(21)), "KLARTEXT-Mentoring", font=f_titel, fill=(255, 255, 255))
    f_sub = ImageFont.truetype(F_SANS_REG, mm(5.5))
    d.text((mm(48), mm(34)), "Systemische Coaching-Impulskarten", font=f_sub, fill=(232, 222, 234))

    f_haupt = ImageFont.truetype(F_SERIF_BOLD, mm(34))
    d.text((mm(20), mm(90)), "LK-Deck", font=f_haupt, fill=LK)

    f_haupt2 = ImageFont.truetype(F_SANS_BOLD, mm(7))
    d.text((mm(20), mm(140)), "50 Coaching-Impulskarten für Lehrkräfte", font=f_haupt2, fill=KT_INK)

    f_themen_label = ImageFont.truetype(F_SANS_BOLD, mm(5.5))
    d.text((mm(20), mm(158)), "THEMENBEREICHE", font=f_themen_label, fill=LK)

    themen = ["Die eigene Rolle als Lehrkraft", "Das Kind im Unterricht verstehen",
              "Kommunikation im Schulalltag", "Wenn es schwierig wird",
              "Alltag & Praxissituationen", "Selbstfürsorge als Lehrkraft",
              "Klassengemeinschaft als System", "Abgrenzung & Feierabend",
              "Interkulturelle Kompetenz", "KI & Digitalität im Unterricht"]
    f_thema = ImageFont.truetype(F_SANS_REG, mm(4.7))
    row_h = mm(8.6)
    col_w = mm(85)
    themen_y = mm(168)
    for i, t in enumerate(themen):
        col = i // 5
        row = i % 5
        x = mm(20) + col * col_w
        y = themen_y + row * row_h
        d.ellipse((x, y + mm(1.7), x + mm(2.3), y + mm(4.0)), fill=LK)
        d.text((x + mm(5), y), t, font=f_thema, fill=KT_INK)

    box_y = mm(240)
    box_h = mm(22)
    d.rounded_rectangle((mm(20), box_y, W - mm(20), box_y + box_h), radius=mm(3), fill=(238, 231, 239))
    f_status_l = ImageFont.truetype(F_SANS_BOLD, mm(6))
    f_status = ImageFont.truetype(F_SANS_REG, mm(5.6))
    d.text((mm(28), box_y + mm(6)), "STAND DIESER AUSGABE", font=f_status_l, fill=LK)
    d.text((mm(28), box_y + mm(13)), "LK-Basis vollständig (50 Karten). Zusatzblöcke folgen separat.",
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
             quellen_seite1(), quellen_seite1b(), quellen_seite2()]

    fehlt = []
    for nr in range(1, 51):
        vorn = os.path.join(KARTEN_DIR, f"LK-R-{nr:02d}_Vorderseite.png")
        hinten = os.path.join(KARTEN_DIR, f"LK-R-{nr:02d}_Rueckseite.png")
        if os.path.exists(vorn) and os.path.exists(hinten):
            pages.append(Image.open(vorn).convert("RGB"))
            pages.append(Image.open(hinten).convert("RGB"))
        else:
            fehlt.append(nr)

    if fehlt:
        print(f"Abgebrochen: {len(fehlt)} Karten fehlen noch (Bilder nicht vorhanden): {fehlt}")
        print("PDF wird erst gebaut, wenn alle 50 Karten vorliegen. Erst build_all_cards_lk.py erneut "
              "laufen lassen, sobald die Bilder da sind.")
        return

    first, rest = pages[0], pages[1:]
    first.save(OUT_PDF, save_all=True, append_images=rest, resolution=DPI)
    print(f"PDF fertig: {OUT_PDF} ({len(pages)} Seiten)")

if __name__ == "__main__":
    run()
