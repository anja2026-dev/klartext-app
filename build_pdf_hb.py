#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baut die druckfertige PDF aus allen 12 Karten des Hochbegabungsdecks. Struktur analog
build_pdf_mb.py: Cover, Anleitung, Quellenverzeichnis, dann 12 Karten (Vorder-/Rückseite)."""
from PIL import Image, ImageDraw, ImageFont
import os, sys
Image.init()
sys.path.insert(0, os.path.dirname(__file__))
from build_booklet_hb import anleitung_seite, herkunft_seite

KARTEN_DIR = "/sessions/kind-beautiful-ptolemy/mnt/outputs/hb_karten_komplett/"
OUT_PDF = "/sessions/kind-beautiful-ptolemy/mnt/outputs/KLARTEXT_Hochbegabung_komplett.pdf"

DPI = 300
MM = DPI / 25.4
def mm(v): return int(round(v * MM))

HB = (32, 36, 196)
KT_MUTED = (122, 112, 96)
KT_INK = (45, 45, 45)

F_SERIF_BOLD = "/usr/share/fonts/truetype/crosextra/Caladea-Bold.ttf"
F_SANS_REG = "/usr/share/fonts/truetype/lato/Lato-Regular.ttf"
F_SANS_BOLD = "/usr/share/fonts/truetype/lato/Lato-Bold.ttf"

def _wrap(d, text, font, max_width):
    words = text.split()
    lines, cur = [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if d.textlength(t, font=font) <= max_width:
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
    content_w = W - mm(40)

    kopf_h = mm(60)
    d.rectangle((0, 0, W, kopf_h), fill=HB)
    logo_s = mm(20)
    logo_y = (kopf_h - logo_s) // 2
    d.rounded_rectangle((mm(20), logo_y, mm(20) + logo_s, logo_y + logo_s), radius=mm(4),
                         fill=(27, 58, 75), outline=(110, 198, 160), width=mm(1.2))
    f_logo = ImageFont.truetype(F_SERIF_BOLD, mm(11))
    d.text((mm(20) + logo_s / 2, logo_y + logo_s / 2), "K", font=f_logo, anchor="mm", fill=(255, 255, 255))

    f_titel = ImageFont.truetype(F_SERIF_BOLD, mm(11))
    d.text((mm(48), mm(21)), "KLARTEXT-Mentoring", font=f_titel, fill=(255, 255, 255))
    f_sub = ImageFont.truetype(F_SANS_REG, mm(5.5))
    d.text((mm(48), mm(34)), "Hochbegabung", font=f_sub, fill=(225, 226, 250))

    haupt_size = 15.0
    f_haupt = ImageFont.truetype(F_SERIF_BOLD, mm(haupt_size))
    while d.textlength("Hochbegabungsdeck", font=f_haupt) > content_w and haupt_size > 8:
        haupt_size -= 0.5
        f_haupt = ImageFont.truetype(F_SERIF_BOLD, mm(haupt_size))
    d.text((mm(20), mm(88)), "Hochbegabungsdeck", font=f_haupt, fill=HB)

    f_haupt2 = ImageFont.truetype(F_SANS_BOLD, mm(6))
    sub_lines = _wrap(d, "12 Karten für Erkennen, Herausforderungen und Handeln", f_haupt2, content_w)
    sy = mm(108)
    for ln in sub_lines:
        d.text((mm(20), sy), ln, font=f_haupt2, fill=KT_INK)
        sy += mm(8.5)

    f_label = ImageFont.truetype(F_SANS_BOLD, mm(5.5))
    d.text((mm(20), mm(126)), "DIE 12 KARTEN", font=f_label, fill=HB)
    themen = ["HB-01 Was ist Hochbegabung?", "HB-02 Merkmale erkennen", "HB-03 Asynchrone Entwicklung",
              "HB-04 Underachievement", "HB-05 Perfektionismus & Versagensangst", "HB-06 Soziale Herausforderungen",
              "HB-07 Doppelbegabung / Twice-Exceptional", "HB-08 Langeweile & Verweigerung", "HB-09 Enrichment & Akzeleration",
              "HB-10 Diagnostik: wann testen?", "HB-11 Zusammenarbeit mit der Lehrkraft", "HB-12 Elterngespräch bei Hochbegabung"]
    f_thema = ImageFont.truetype(F_SANS_REG, mm(4.2))
    row_h = mm(6.4)
    col_w = mm(87)
    for i, t in enumerate(themen):
        col = i // 6
        row = i % 6
        x = mm(20) + col * col_w
        y = mm(136) + row * row_h
        d.ellipse((x, y + mm(1.6), x + mm(2.2), y + mm(3.8)), fill=HB)
        d.text((x + mm(5), y), t, font=f_thema, fill=KT_INK)

    box_y = mm(200)
    box_h = mm(26)
    d.rounded_rectangle((mm(20), box_y, W - mm(20), box_y + box_h), radius=mm(3), fill=(227, 228, 250))
    f_status_l = ImageFont.truetype(F_SANS_BOLD, mm(6))
    f_status = ImageFont.truetype(F_SANS_REG, mm(5.0))
    d.text((mm(28), box_y + mm(6)), "STAND DIESER AUSGABE", font=f_status_l, fill=HB)
    status_lines = _wrap(d, "12 Karten vollständig, neu entwickelt auf Basis anerkannter Begabungsmodelle "
                             "und aktueller Forschung (Renzulli, Mönks, Heller, Gagné u. a.).",
                          f_status, content_w - mm(16))
    stat_y = box_y + mm(13)
    for ln in status_lines:
        d.text((mm(28), stat_y), ln, font=f_status, fill=KT_INK)
        stat_y += mm(7)

    f_foot = ImageFont.truetype(F_SANS_REG, mm(5))
    d.text((mm(20), H - mm(18)), "KLARTEXT-Mentoring · © 2026 Anja Jolk", font=f_foot, fill=KT_MUTED)
    return img

def run():
    pages = [build_cover(), anleitung_seite(), herkunft_seite()]

    fehlt = []
    for id_text in [f"HB-{n:02d}" for n in range(1, 13)]:
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
