#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baut die PDF aus allen fertigen JD-Deck-Karten (40 von 40). Nutzt das bereits bestehende
build_booklet.py (Anleitung/Glossar/Quellen, war schon in klartext-app vorhanden). Neu aufgebaut
27.07.2026 zusammen mit build_card_jd.py/build_all_cards_jd.py, mit den aktualisierten Bildern im
neuen Stil."""
from PIL import Image, ImageDraw, ImageFont
import os, sys
Image.init()
sys.path.insert(0, os.path.dirname(__file__))
from build_booklet import (anleitung_seite1, anleitung_seite2, glossar_seite,
                            quellen_seite1, quellen_seite2, GLOSSAR)

KARTEN_DIR = "/sessions/kind-beautiful-ptolemy/mnt/outputs/jd_karten_komplett/"
OUT_PDF = "/sessions/kind-beautiful-ptolemy/mnt/outputs/KLARTEXT_JD-Deck_komplett.pdf"

DPI = 300
MM = DPI / 25.4
def mm(v): return int(round(v * MM))

JD = (47, 107, 110)
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
    d.rectangle((0, 0, W, kopf_h), fill=JD)
    logo_s = mm(20)
    logo_y = (kopf_h - logo_s) // 2
    d.rounded_rectangle((mm(20), logo_y, mm(20) + logo_s, logo_y + logo_s), radius=mm(4),
                         fill=(27, 58, 75), outline=(110, 198, 160), width=mm(1.2))
    f_logo = ImageFont.truetype(F_SERIF_BOLD, mm(11))
    d.text((mm(20) + logo_s / 2, logo_y + logo_s / 2), "K", font=f_logo, anchor="mm", fill=(255, 255, 255))

    f_titel = ImageFont.truetype(F_SERIF_BOLD, mm(11))
    d.text((mm(48), mm(21)), "KLARTEXT-Mentoring", font=f_titel, fill=(255, 255, 255))
    f_sub = ImageFont.truetype(F_SANS_REG, mm(5.5))
    d.text((mm(48), mm(34)), "Systemische Coaching-Impulskarten", font=f_sub, fill=(220, 240, 238))

    f_haupt = ImageFont.truetype(F_SERIF_BOLD, mm(28))
    d.text((mm(20), mm(84)), "JD-Deck", font=f_haupt, fill=JD)
    f_haupt2 = ImageFont.truetype(F_SANS_BOLD, mm(6))
    sub_text = "52 Impulskarten · Jugendliche im weiterführenden Schulalter"
    sub_max_w = W - mm(40)
    if d.textlength(sub_text, font=f_haupt2) > sub_max_w:
        f_haupt2 = ImageFont.truetype(F_SANS_BOLD, mm(5.2))
    d.text((mm(20), mm(128)), sub_text, font=f_haupt2, fill=KT_INK)

    f_intro = ImageFont.truetype(F_SANS_REG, mm(4.8))
    intro_text = ("Für Jugendliche im weiterführenden Schulalter. Themen: Selbstwert, Zukunftsdruck, "
                  "Konflikt, Grenzen, Stress, Beziehung zu Erwachsenen, Identität, digitale Balance, "
                  "Familie im Wandel, Mut, Berufsvorbereitung, Beziehungen & Verliebtsein, Freundschaft. "
                  "Kein Test, keine Diagnostik – ein Gesprächsanlass.")
    intro_lines = wrap(d, intro_text, f_intro, W - mm(48))
    iy = mm(144)
    for ln in intro_lines:
        d.text((mm(20), iy), ln, font=f_intro, fill=KT_INK)
        iy += mm(7.2)

    f_themen_label = ImageFont.truetype(F_SANS_BOLD, mm(5.5))
    themen_y = iy + mm(10)
    d.text((mm(20), themen_y), "THEMENBEREICHE", font=f_themen_label, fill=JD)

    themen = ["Selbstwert & Vergleich", "Zukunftsdruck", "Konflikt auf Augenhöhe",
              "Grenzen setzen", "Stress & Leistungsdruck", "Beziehung zu Erwachsenen",
              "Identität & Selbstfindung", "Digitale Balance", "Familie im Wandel",
              "Mut & Umgang mit Fehlern", "Berufsvorbereitung", "Beziehungen & Verliebtsein",
              "Freundschaft & Zugehörigkeit"]
    f_thema = ImageFont.truetype(F_SANS_REG, mm(4.8))
    row_h = mm(6.8)
    col_w = mm(85)
    for i, t in enumerate(themen):
        col = i // 7
        row = i % 7
        x = mm(20) + col * col_w
        y = themen_y + mm(10) + row * row_h
        d.ellipse((x, y + mm(1.6), x + mm(2.2), y + mm(3.8)), fill=JD)
        d.text((x + mm(5), y), t, font=f_thema, fill=KT_INK)

    f_foot = ImageFont.truetype(F_SANS_REG, mm(5))
    d.text((mm(20), H - mm(18)), "KLARTEXT-Mentoring · © 2026 Anja Jolk", font=f_foot, fill=KT_MUTED)
    return img

def run():
    pages = [build_cover(), anleitung_seite1(), anleitung_seite2(),
             glossar_seite(GLOSSAR[:3], "Glossar · 1/2",
                 intro="Kurz erklärt: Begriffe, die auf den Karten oder in dieser Anleitung vorkommen "
                       "und nicht selbsterklärend sind."),
             glossar_seite(GLOSSAR[3:], "Glossar · 2/2"),
             quellen_seite1(), quellen_seite2()]

    fehlt = []
    for nr in range(1, 53):
        vorn = os.path.join(KARTEN_DIR, f"JD-{nr:02d}_Vorderseite.png")
        hinten = os.path.join(KARTEN_DIR, f"JD-{nr:02d}_Rueckseite.png")
        if os.path.exists(vorn) and os.path.exists(hinten):
            pages.append(Image.open(vorn).convert("RGB"))
            pages.append(Image.open(hinten).convert("RGB"))
        else:
            fehlt.append(nr)

    if fehlt:
        print(f"Abgebrochen: {len(fehlt)} Karten fehlen noch (Bilder nicht vorhanden): {fehlt}")
        print("PDF wird erst gebaut, wenn alle 52 Karten vorliegen. Erst build_all_cards_jd.py "
              "erneut laufen lassen, sobald die Bilder da sind.")
        return

    first, rest = pages[0], pages[1:]
    first.save(OUT_PDF, save_all=True, append_images=rest, resolution=DPI)
    print(f"PDF fertig: {OUT_PDF} ({len(pages)} Seiten)")

if __name__ == "__main__":
    run()
