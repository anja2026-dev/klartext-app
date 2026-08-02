#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baut die PDF aus allen fertigen DaZ-Sek-I-Deck-Karten (25 von 25). Kein Fachprüfungs-Vorbehalt
(Anjas eigene Qualifikation deckt das ab) – normales Cover ohne Warnhinweis. Letztes Deck der
Zehner-Serie (10/10)."""
from PIL import Image, ImageDraw, ImageFont
import os, sys
Image.init()
sys.path.insert(0, os.path.dirname(__file__))
from build_booklet_dazsek1 import (anleitung_seite1, anleitung_seite2, methodik_seite, glossar_seite,
                                    quellen_seite, GLOSSAR)

KARTEN_DIR = "/sessions/kind-beautiful-ptolemy/mnt/outputs/dazsek1_karten_komplett/"
OUT_PDF = "/sessions/kind-beautiful-ptolemy/mnt/outputs/KLARTEXT_DAZ-SEK1-Deck_komplett.pdf"

DPI = 300
MM = DPI / 25.4
def mm(v): return int(round(v * MM))

DAZSEK1 = (110, 20, 56)
DAZSEK1_TEXT = (110, 20, 56)
KT_MUTED = (122, 112, 96)
KT_INK = (45, 45, 45)

F_SERIF_BOLD = "/usr/share/fonts/truetype/crosextra/Caladea-Bold.ttf"
F_SANS_REG = "/usr/share/fonts/truetype/lato/Lato-Regular.ttf"
F_SANS_BOLD = "/usr/share/fonts/truetype/lato/Lato-Bold.ttf"

def wrap(draw, text, font, max_width):
    words = text.split()
    lines, cur = [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if draw.textlength(t, font=font) <= max_width:
            cur = t
        else:
            if cur: lines.append(cur)
            cur = w_
    if cur: lines.append(cur)
    return lines

def build_cover():
    W, H = mm(210), mm(297)
    img = Image.new("RGB", (W, H), (255, 255, 255))
    d = ImageDraw.Draw(img)

    kopf_h = mm(60)
    d.rectangle((0, 0, W, kopf_h), fill=DAZSEK1)
    logo_s = mm(20)
    logo_y = (kopf_h - logo_s) // 2
    d.rounded_rectangle((mm(20), logo_y, mm(20) + logo_s, logo_y + logo_s), radius=mm(4),
                         fill=(27, 58, 75), outline=(110, 198, 160), width=mm(1.2))
    f_logo = ImageFont.truetype(F_SERIF_BOLD, mm(11))
    d.text((mm(20) + logo_s / 2, logo_y + logo_s / 2), "K", font=f_logo, anchor="mm", fill=(255, 255, 255))

    f_titel = ImageFont.truetype(F_SERIF_BOLD, mm(11))
    d.text((mm(48), mm(21)), "KLARTEXT-Mentoring", font=f_titel, fill=(255, 255, 255))
    f_sub = ImageFont.truetype(F_SANS_REG, mm(5.5))
    d.text((mm(48), mm(34)), "Systemische Coaching-Impulskarten", font=f_sub, fill=(240, 220, 228))

    f_haupt = ImageFont.truetype(F_SERIF_BOLD, mm(24))
    d.text((mm(20), mm(84)), "DaZ-Sek-I-Deck", font=f_haupt, fill=DAZSEK1_TEXT)
    f_haupt2 = ImageFont.truetype(F_SANS_BOLD, mm(6))
    sub_text = "25 Impulskarten · Deutsch als Zweitsprache, Sekundarstufe I"
    sub_max_w = W - mm(40)
    if d.textlength(sub_text, font=f_haupt2) > sub_max_w:
        f_haupt2 = ImageFont.truetype(F_SANS_BOLD, mm(5.4))
    d.text((mm(20), mm(112)), sub_text, font=f_haupt2, fill=KT_INK)

    f_intro = ImageFont.truetype(F_SANS_REG, mm(4.8))
    intro_text = ("Für Jugendliche der Sekundarstufe I mit Deutsch als Zweitsprache und/oder "
                  "Migrations-/Fluchthintergrund. Themen: Ankommen im neuen System, Sprache und "
                  "Leistung, Identität zwischen den Kulturen, Freundschaft und Zugehörigkeit, "
                  "Herkunft und was fehlt, Zukunft und Stolz. Kein Trauma-Verarbeitungs-Deck "
                  "(siehe Anleitung).")
    intro_lines = wrap(d, intro_text, f_intro, W - mm(48))
    iy = mm(128)
    for ln in intro_lines:
        d.text((mm(20), iy), ln, font=f_intro, fill=KT_INK)
        iy += mm(7.2)

    f_themen_label = ImageFont.truetype(F_SANS_BOLD, mm(5.5))
    themen_y = iy + mm(10)
    d.text((mm(20), themen_y), "THEMENBEREICHE", font=f_themen_label, fill=DAZSEK1_TEXT)

    themen = ["Ankommen im neuen System", "Sprache & Leistung", "Identität zwischen den Kulturen",
              "Freundschaft & Zugehörigkeit", "Herkunft & was ich vermisse", "Zukunft & Stolz",
              "Übergang in die Regelklasse"]
    f_thema = ImageFont.truetype(F_SANS_REG, mm(5.6))
    row_h = mm(9)
    for i, t in enumerate(themen):
        x = mm(20)
        y = themen_y + mm(10) + i * row_h
        d.ellipse((x, y + mm(2), x + mm(2.4), y + mm(4.4)), fill=DAZSEK1)
        d.text((x + mm(5.5), y), t, font=f_thema, fill=KT_INK)

    f_foot = ImageFont.truetype(F_SANS_REG, mm(5))
    d.text((mm(20), H - mm(18)), "KLARTEXT-Mentoring · © 2026 Anja Jolk", font=f_foot, fill=KT_MUTED)
    return img

def run():
    pages = [build_cover(), anleitung_seite1(), anleitung_seite2(), methodik_seite(),
             glossar_seite(GLOSSAR[:3], "Glossar · 1/2",
                 intro="Kurz erklärt: Begriffe, die auf den Karten oder in dieser Anleitung vorkommen "
                       "und nicht selbsterklärend sind."),
             glossar_seite(GLOSSAR[3:], "Glossar · 2/2"),
             quellen_seite()]

    fehlt = []
    for nr in range(1, 26):
        vorn = os.path.join(KARTEN_DIR, f"DAZ-SEK1-{nr:02d}_Vorderseite.png")
        hinten = os.path.join(KARTEN_DIR, f"DAZ-SEK1-{nr:02d}_Rueckseite.png")
        if os.path.exists(vorn) and os.path.exists(hinten):
            pages.append(Image.open(vorn).convert("RGB"))
            pages.append(Image.open(hinten).convert("RGB"))
        else:
            fehlt.append(nr)

    if fehlt:
        print(f"Abgebrochen: {len(fehlt)} Karten fehlen noch (Bilder nicht vorhanden): {fehlt}")
        print("PDF wird erst gebaut, wenn alle 25 Karten vorliegen. Erst build_all_cards_dazsek1.py "
              "erneut laufen lassen, sobald die Bilder da sind.")
        return

    first, rest = pages[0], pages[1:]
    first.save(OUT_PDF, save_all=True, append_images=rest, resolution=DPI)
    print(f"PDF fertig: {OUT_PDF} ({len(pages)} Seiten)")

if __name__ == "__main__":
    run()
