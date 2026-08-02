#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baut drei kompakte PDFs für die LK-Zusatzblöcke (Autismus, ADHS, Pflegekinder).
Analog zu build_pdf_el_zusatz.py."""
from PIL import Image, ImageDraw, ImageFont
import os
Image.init()

KARTEN_DIR = "/sessions/kind-beautiful-ptolemy/mnt/outputs/lk_zusatz_karten_komplett/"
OUT_DIR = "/sessions/kind-beautiful-ptolemy/mnt/outputs/"

DPI = 300
MM = DPI / 25.4
def mm(v): return int(round(v * MM))

LK = (107, 78, 113)
LK_LIGHT = (238, 231, 239)
KT_INK = (45, 45, 45)
KT_MUTED = (122, 112, 96)

F_SERIF_BOLD = "/usr/share/fonts/truetype/crosextra/Caladea-Bold.ttf"
F_SANS_REG = "/usr/share/fonts/truetype/lato/Lato-Regular.ttf"
F_SANS_BOLD = "/usr/share/fonts/truetype/lato/Lato-Bold.ttf"

W, H = mm(210), mm(297)
MARGIN = mm(20)
CONTENT_W = W - 2 * MARGIN

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

def build_cover(titel, andockt_an, hinweis_text, stand_text):
    img = Image.new("RGB", (W, H), (255, 255, 255))
    d = ImageDraw.Draw(img)

    kopf_h = mm(55)
    d.rectangle((0, 0, W, kopf_h), fill=LK)
    logo_s = mm(18)
    logo_y = mm(18)
    d.rounded_rectangle((mm(20), logo_y, mm(20) + logo_s, logo_y + logo_s), radius=mm(4),
                         fill=(27, 58, 75), outline=(110, 198, 160), width=mm(1.2))
    f_logo = ImageFont.truetype(F_SERIF_BOLD, mm(9.5))
    d.text((mm(20) + logo_s / 2, logo_y + logo_s / 2), "K", font=f_logo, anchor="mm", fill=(255, 255, 255))
    f_titel = ImageFont.truetype(F_SERIF_BOLD, mm(9))
    d.text((mm(46), mm(20)), "KLARTEXT-Mentoring", font=f_titel, fill=(255, 255, 255))
    f_sub = ImageFont.truetype(F_SANS_REG, mm(4.8))
    d.text((mm(46), mm(31)), "LK-Deck · Ergänzungsset", font=f_sub, fill=(232, 222, 234))

    y = mm(75)
    f_haupt = ImageFont.truetype(F_SERIF_BOLD, mm(15))
    for ln in wrap(d, titel, f_haupt, CONTENT_W):
        d.text((mm(20), y), ln, font=f_haupt, fill=LK)
        y += mm(18)
    y += mm(6)

    f_body = ImageFont.truetype(F_SANS_REG, mm(5))
    y = draw_para(d, y, andockt_an, f_body)
    y += mm(10)

    box_h_lines = wrap(d, hinweis_text, ImageFont.truetype(F_SANS_REG, mm(4.6)), CONTENT_W - mm(16))
    line_h = mm(4.6 * 1.55)
    box_h = mm(15) + len(box_h_lines) * line_h + mm(6)
    d.rounded_rectangle((MARGIN, y, W - MARGIN, y + box_h), radius=mm(3),
                         fill=(253, 245, 245), outline=(210, 160, 160), width=mm(0.4))
    f_warn_l = ImageFont.truetype(F_SANS_BOLD, mm(5.2))
    d.text((MARGIN + mm(8), y + mm(7)), "HINWEIS", font=f_warn_l, fill=(160, 60, 60))
    wy = y + mm(15)
    f_warn_text = ImageFont.truetype(F_SANS_REG, mm(4.6))
    for ln in box_h_lines:
        d.text((MARGIN + mm(8), wy), ln, font=f_warn_text, fill=KT_INK)
        wy += line_h
    y = y + box_h + mm(10)

    box_y = mm(255)
    box_h2 = mm(20)
    d.rounded_rectangle((mm(20), box_y, W - mm(20), box_y + box_h2), radius=mm(3), fill=LK_LIGHT)
    f_status_l = ImageFont.truetype(F_SANS_BOLD, mm(5.5))
    f_status = ImageFont.truetype(F_SANS_REG, mm(5))
    d.text((mm(28), box_y + mm(5)), "STAND DIESER AUSGABE", font=f_status_l, fill=LK)
    d.text((mm(28), box_y + mm(12)), stand_text, font=f_status, fill=KT_INK)

    f_foot = ImageFont.truetype(F_SANS_REG, mm(4.5))
    d.text((mm(20), H - mm(15)), "KLARTEXT-Mentoring · © 2026 Anja Jolk", font=f_foot, fill=KT_MUTED)
    return img

def draw_para(d, y, text, font, color=KT_INK):
    lh = mm(5 * 1.55)
    for ln in wrap(d, text, font, CONTENT_W):
        d.text((MARGIN, y), ln, font=font, fill=color)
        y += lh
    return y

SETS = [
    ("LK-R-AT", "KLARTEXT_LK-Zusatzblock_Autismus.pdf",
     "LK-Zusatzblock: Lehrkräfte autistischer Kinder",
     "7 Ergänzungskarten zur LK-Basis. Andockt an das AT-Kind-Deck – gedacht für Lehrkräfte, "
     "die ein Kind unterrichten, das mit dem AT-Deck begleitet wird.",
     "Diese Karten fokussieren bewusst auf die emotionale/praktische Erfahrung der Lehrkraft, "
     "nicht auf Diagnostik oder Interventionsempfehlungen. Vor Veröffentlichung fachlich "
     "gegenlesen lassen.",
     "7 Karten vollständig. Fachliches Gegenlesen vor Veröffentlichung noch ausstehend."),
    ("LK-R-ADHS", "KLARTEXT_LK-Zusatzblock_ADHS.pdf",
     "LK-Zusatzblock: Lehrkräfte von Kindern mit ADHS",
     "7 Ergänzungskarten zur LK-Basis. Andockt an das geplante ADHS-Kind-Deck.",
     "Fokus auf die emotionale/praktische Erfahrung der Lehrkraft. Vor Veröffentlichung "
     "fachlich gegenlesen lassen.",
     "7 Karten vollständig. Fachliches Gegenlesen vor Veröffentlichung noch ausstehend."),
    ("LK-R-PF", "KLARTEXT_LK-Zusatzblock_Pflegekinder.pdf",
     "LK-Zusatzblock: Lehrkräfte von Pflegekindern",
     "7 Ergänzungskarten zur LK-Basis. Andockt an das geplante Pflegekinder-Ergänzungsset.",
     "Anders als bei Autismus/ADHS kein externer Fachprüfungs-Vorbehalt nötig – basiert auf "
     "mehrjähriger Praxiserfahrung (Förderschule Sprache/Lernen mit Wohngruppen- und "
     "Pflegekindern).",
     "7 Karten vollständig, kein Gegenlesen-Vorbehalt."),
]

def run():
    for code, filename, titel, andockt, hinweis, stand in SETS:
        pages = [build_cover(titel, andockt, hinweis, stand)]
        for nr in range(1, 8):
            vorn = os.path.join(KARTEN_DIR, f"{code}-{nr:02d}_Vorderseite.png")
            hinten = os.path.join(KARTEN_DIR, f"{code}-{nr:02d}_Rueckseite.png")
            if os.path.exists(vorn) and os.path.exists(hinten):
                pages.append(Image.open(vorn).convert("RGB"))
                pages.append(Image.open(hinten).convert("RGB"))
            else:
                print(f"Fehlt: {code}-{nr:02d}")
        out_path = os.path.join(OUT_DIR, filename)
        first, rest = pages[0], pages[1:]
        first.save(out_path, save_all=True, append_images=rest, resolution=DPI)
        print(f"PDF fertig: {out_path} ({len(pages)} Seiten)")

if __name__ == "__main__":
    run()
