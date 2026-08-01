#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baut die druckfertige PDF aus allen 20 Werkzeugkarten-Deck-Karten. Icon-Vorderseiten, kein Foto-
Wartezustand nötig. Struktur analog build_pdf_krisendeck.py."""
from PIL import Image, ImageDraw, ImageFont
import os, sys
Image.init()
sys.path.insert(0, os.path.dirname(__file__))
from build_booklet_werkzeug import (anleitung_seite1, anleitung_seite2, barometer_klar_seite,
                                     quellen_seite, quellen_seite2)

KARTEN_DIR = "/sessions/kind-beautiful-ptolemy/mnt/outputs/werkzeug_karten_komplett/"
OUT_PDF = "/sessions/kind-beautiful-ptolemy/mnt/outputs/KLARTEXT_Werkzeugkarten-Deck_komplett.pdf"

DPI = 300
MM = DPI / 25.4
def mm(v): return int(round(v * MM))

M3 = (176, 125, 42)
KT_MUTED = (122, 112, 96)
KT_INK = (45, 45, 45)

F_SERIF_BOLD = "/usr/share/fonts/truetype/crosextra/Caladea-Bold.ttf"
F_SANS_REG = "/usr/share/fonts/truetype/lato/Lato-Regular.ttf"
F_SANS_BOLD = "/usr/share/fonts/truetype/lato/Lato-Bold.ttf"

SITUATIONEN = ["M3-01 Kind kommt aufgewühlt an", "M3-02 Kind verweigert Arbeit", "M3-03 Kind eskaliert – Wutausbruch",
               "M3-04 Kind zieht sich zurück – Freeze", "M3-05 Übergang zwischen Situationen", "M3-06 Konflikt mit Mitschüler:innen",
               "M3-07 Kind ist überwältigt – weint", "M3-08 Krise – Rot/Grau – Feuerwehr"]
WERKZEUGE = ["M3-09 Atemanker", "M3-10 Liegende Acht", "M3-11 5-Dinge-Grounding", "M3-12 Reizfilter",
             "M3-13 Joker", "M3-14 Mini-Pause", "M3-15 Schritt-Plan", "M3-16 Igel-Ball",
             "M3-17 Visualisierung", "M3-18 Lob-Sandwich", "M3-19 Brainy-Flow", "M3-20 Selbst-Regulation stärken",
             "M3-21 Sichtbare Zeit", "M3-22 Stopp-Hand-Signal", "M3-23 Sicherer Ort",
             "M3-24 Körper-Check-In", "M3-25 Die Kraft der Pause", "M3-26 No-Blame-Approach"]

def build_cover():
    W, H = mm(210), mm(297)
    img = Image.new("RGB", (W, H), (255, 255, 255))
    d = ImageDraw.Draw(img)

    kopf_h = mm(60)
    d.rectangle((0, 0, W, kopf_h), fill=M3)
    logo_s = mm(20)
    logo_y = (kopf_h - logo_s) // 2
    d.rounded_rectangle((mm(20), logo_y, mm(20) + logo_s, logo_y + logo_s), radius=mm(4),
                         fill=(27, 58, 75), outline=(110, 198, 160), width=mm(1.2))
    f_logo = ImageFont.truetype(F_SERIF_BOLD, mm(11))
    d.text((mm(20) + logo_s / 2, logo_y + logo_s / 2), "K", font=f_logo, anchor="mm", fill=(255, 255, 255))

    f_titel = ImageFont.truetype(F_SERIF_BOLD, mm(11))
    d.text((mm(48), mm(21)), "KLARTEXT-Mentoring", font=f_titel, fill=(255, 255, 255))
    f_sub = ImageFont.truetype(F_SANS_REG, mm(5.5))
    d.text((mm(48), mm(34)), "Handlungskarten · Werkzeugkasten", font=f_sub, fill=(255, 240, 215))

    f_haupt = ImageFont.truetype(F_SERIF_BOLD, mm(15.5))
    d.text((mm(20), mm(90)), "Werkzeugkarten-Deck", font=f_haupt, fill=M3)

    f_haupt2 = ImageFont.truetype(F_SANS_BOLD, mm(7))
    d.text((mm(20), mm(122)), "26 Karten für den Alltag · Barometer Gelb bis Orange", font=f_haupt2, fill=KT_INK)

    f_label = ImageFont.truetype(F_SANS_BOLD, mm(5.5))
    d.text((mm(20), mm(138)), "8 SITUATIONEN", font=f_label, fill=M3)
    f_thema = ImageFont.truetype(F_SANS_REG, mm(4.5))
    row_h = mm(6.2)
    for i, t in enumerate(SITUATIONEN):
        x = mm(20)
        y = mm(147) + i * row_h
        d.ellipse((x, y + mm(1.7), x + mm(2.2), y + mm(3.9)), fill=M3)
        d.text((x + mm(5), y), t, font=f_thema, fill=KT_INK)

    # 18 Werkzeuge passen textbreitenmäßig nicht mehr neben die Situationen-Spalte (zu lange
    # Bezeichnungen). Deshalb eigener Block unterhalb, auf zwei volle Spalten aufgeteilt (9+9).
    werkzeuge_label_y = mm(206)
    d.text((mm(20), werkzeuge_label_y), "18 WERKZEUGE", font=f_label, fill=M3)
    f_werkzeug = ImageFont.truetype(F_SANS_REG, mm(4.3))
    wz_row_h = mm(4.6)
    wz_start_y = mm(213)
    colA_x = mm(20)
    colB_x = mm(105)
    werkzeuge_colA = WERKZEUGE[:9]
    werkzeuge_colB = WERKZEUGE[9:]
    for i, t in enumerate(werkzeuge_colA):
        y = wz_start_y + i * wz_row_h
        d.ellipse((colA_x, y + mm(1.5), colA_x + mm(2.0), y + mm(3.5)), fill=M3)
        d.text((colA_x + mm(4.5), y), t, font=f_werkzeug, fill=KT_INK)
    for i, t in enumerate(werkzeuge_colB):
        y = wz_start_y + i * wz_row_h
        d.ellipse((colB_x, y + mm(1.5), colB_x + mm(2.0), y + mm(3.5)), fill=M3)
        d.text((colB_x + mm(4.5), y), t, font=f_werkzeug, fill=KT_INK)

    box_y = mm(257)
    box_h = mm(18)
    d.rounded_rectangle((mm(20), box_y, W - mm(20), box_y + box_h), radius=mm(3), fill=(251, 244, 232))
    f_status_l = ImageFont.truetype(F_SANS_BOLD, mm(6))
    f_status = ImageFont.truetype(F_SANS_REG, mm(5.6))
    d.text((mm(28), box_y + mm(6)), "STAND DIESER AUSGABE", font=f_status_l, fill=M3)
    d.text((mm(28), box_y + mm(13)), "26 Karten vollständig — M3-21–26 neu ergänzt (01.08.2026).",
           font=f_status, fill=KT_INK)

    f_foot = ImageFont.truetype(F_SANS_REG, mm(5))
    d.text((mm(20), H - mm(18)), "KLARTEXT-Mentoring · © 2026 Anja Jolk", font=f_foot, fill=KT_MUTED)
    return img

def run():
    pages = [build_cover(), anleitung_seite1(), anleitung_seite2(), barometer_klar_seite(),
             quellen_seite(), quellen_seite2()]

    fehlt = []
    for id_text in [f"M3-{n:02d}" for n in range(1, 27)]:
        vorn = os.path.join(KARTEN_DIR, f"{id_text}_Vorderseite.png")
        hinten = os.path.join(KARTEN_DIR, f"{id_text}_Rueckseite.png")
        if os.path.exists(vorn) and os.path.exists(hinten):
            pages.append(Image.open(vorn).convert("RGB"))
            pages.append(Image.open(hinten).convert("RGB"))
        else:
            fehlt.append(id_text)

    first, rest = pages[0], pages[1:]
    first.save(OUT_PDF, save_all=True, append_images=rest, resolution=DPI)
    print(f"PDF fertig: {OUT_PDF} ({len(pages)} Seiten)")
    if fehlt:
        print(f"Fehlt: {fehlt}")

if __name__ == "__main__":
    run()
