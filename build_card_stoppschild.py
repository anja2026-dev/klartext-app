#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Stoppschild-Bonuskarte – einzige der 4 AM_DL-Vorlagen, die strukturell schon eine Karte ist
(App-Original hat bereits Vorder-/Rueckseite im Mini-Kartenformat). Aufbereitet im A6-Serienformat,
reserviert als Bonuskarte fuers spaetere Geschichtenkarten-Deck (Set A "Brainy erlebt Mobbing" nutzt
zufaellig dieselbe Rot-Farbfamilie #C62828 wie die App-eigene Anti-Mobbing-Identitaet – passt farblich
schon zusammen). Text unveraendert aus AM_DL_Stoppschild.html uebernommen."""
from PIL import Image, ImageDraw, ImageFont

DPI = 300
MM = DPI / 25.4
def mm(v): return int(round(v * MM))

CARD_W = mm(105)
CARD_H = mm(148)

AM          = (198, 40, 40)       # #C62828 (App Anti-Mobbing-Rot, = Set-A-Farbe Geschichtenkarten)
AM_DARK     = (139, 0, 0)         # #8B0000
AM_LIGHT    = (255, 235, 238)     # #FFEBEE
AM_BORDER   = (255, 205, 210)     # #FFCDD2
KT_PRIMARY  = (27, 58, 75)
KT_ACCENT   = (110, 198, 160)
KT_INK      = (45, 45, 45)
KT_MUTED    = (122, 112, 96)
WHITE       = (255, 255, 255)

F_SERIF_BOLD   = "/usr/share/fonts/truetype/crosextra/Caladea-Bold.ttf"
F_SANS_REG     = "/usr/share/fonts/truetype/lato/Lato-Regular.ttf"
F_SANS_BOLD    = "/usr/share/fonts/truetype/lato/Lato-Bold.ttf"
F_ICONS        = "/usr/share/fonts/truetype/font-awesome/fontawesome-webfont.ttf"
ICON_BAN = 0xf05e

def font(path, size_mm):
    return ImageFont.truetype(path, mm(size_mm))

def wrap_text(draw, text, fnt, max_width):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        test = (cur + " " + w).strip()
        if draw.textlength(test, font=fnt) <= max_width:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def rounded_rect(draw, box, radius, fill=None, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)

def draw_icon(d, cx, cy, s):
    f = ImageFont.truetype(F_ICONS, int(s))
    ch = chr(ICON_BAN)
    bbox = d.textbbox((0, 0), ch, font=f)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    d.text((cx - tw / 2 - bbox[0], cy - th / 2 - bbox[1]), ch, font=f, fill=WHITE)

def logo_mark(size_mm, bg=KT_PRIMARY, border=KT_ACCENT, letter="K"):
    s = mm(size_mm)
    im = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    bw = max(2, mm(size_mm * 0.07))
    rounded_rect(d, (0, 0, s - 1, s - 1), radius=mm(size_mm * 0.17), fill=bg)
    d.rounded_rectangle((bw // 2, bw // 2, s - 1 - bw // 2, s - 1 - bw // 2),
                         radius=mm(size_mm * 0.17), outline=border, width=bw)
    f = font(F_SERIF_BOLD, size_mm * 0.55)
    bbox = d.textbbox((0, 0), letter, font=f)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    d.text(((s - tw) / 2 - bbox[0], (s - th) / 2 - bbox[1]), letter, font=f, fill=WHITE)
    return im

def build_front(out_path):
    img = Image.new("RGB", (CARD_W, CARD_H), WHITE)
    d = ImageDraw.Draw(img)

    kopf_h = mm(11)
    d.rectangle((0, 0, CARD_W, kopf_h), fill=AM)
    logo = logo_mark(7)
    img.paste(logo, (mm(5), (kopf_h - logo.height) // 2), logo)
    f_badge = font(F_SANS_BOLD, 2.5)
    d.text((mm(5) + logo.width + mm(2.5), kopf_h / 2), "ANTI-MOBBING · BONUSKARTE", font=f_badge, fill=WHITE, anchor="lm")

    feld_h = mm(70)
    feld_top = kopf_h
    d.rectangle((0, feld_top, CARD_W, feld_top + feld_h), fill=AM)
    draw_icon(d, CARD_W / 2, feld_top + feld_h / 2, mm(32))

    titel_top = feld_top + feld_h
    titel_h = mm(30)
    d.rectangle((0, titel_top, CARD_W, titel_top + titel_h), fill=AM_LIGHT)
    d.line((0, titel_top, CARD_W, titel_top), fill=AM_BORDER, width=mm(0.5))
    f_titel = font(F_SERIF_BOLD, 8.5)
    d.text((CARD_W / 2, titel_top + mm(9)), "STOPP!", font=f_titel, fill=AM_DARK, anchor="ma")
    f_sub = font(F_SANS_REG, 3.6)
    ly = titel_top + mm(19)
    for ln in ["Das ist nicht okay.", "Ich will das nicht."]:
        w = d.textlength(ln, font=f_sub)
        d.text(((CARD_W - w) / 2, ly), ln, font=f_sub, fill=KT_INK)
        ly += mm(5)

    img.save(out_path, dpi=(DPI, DPI))
    return img

def build_back(out_path):
    img = Image.new("RGB", (CARD_W, CARD_H), WHITE)
    d = ImageDraw.Draw(img)
    pad = mm(5.2)
    y = pad

    f_titel = font(F_SERIF_BOLD, 4.4)
    d.text((pad, y), "Mein Stoppschild", font=f_titel, fill=AM)
    y += mm(6.5)
    d.line((pad, y, CARD_W - pad, y), fill=AM_BORDER, width=mm(0.4))
    y += mm(3.5)

    f_lab = font(F_SANS_BOLD, 2.5)
    f_text = font(F_SANS_REG, 3.1)
    d.text((pad, y), "WENN ICH DAS SCHILD ZEIGE, HEISST DAS:", font=f_lab, fill=AM)
    y += mm(5)
    for zeile in ["Ich fühle mich nicht wohl", "Ich will, dass es aufhört", "Ich brauche Hilfe"]:
        d.ellipse((pad, y + mm(0.6), pad + mm(2.6), y + mm(3.2)), fill=AM)
        for ln in wrap_text(d, zeile, f_text, CARD_W - 2 * pad - mm(5)):
            d.text((pad + mm(4.5), y), ln, font=f_text, fill=KT_INK)
            y += mm(4.6)
        y += mm(1)
    y += mm(2)

    box_h = mm(14)
    rounded_rect(d, (pad, y, CARD_W - pad, y + box_h), radius=mm(1.5), fill=AM_LIGHT, outline=AM_BORDER, width=mm(0.4))
    f_box_lab = font(F_SANS_BOLD, 2.6)
    f_box_line = font(F_SANS_REG, 3.0)
    d.text((pad + mm(3), y + mm(2.2)), "MEINE ANSPRECHPERSON:", font=f_box_lab, fill=AM_DARK)
    d.line((pad + mm(3), y + mm(10.5), CARD_W - pad - mm(3), y + mm(10.5)), fill=AM_BORDER, width=mm(0.4))
    y += box_h + mm(4)

    d.text((pad, y), "Reserviert als Bonuskarte für das", font=font(F_SANS_REG, 2.3), fill=KT_MUTED)
    y += mm(3.2)
    d.text((pad, y), "Geschichtenkarten-Deck (Set A).", font=font(F_SANS_REG, 2.3), fill=KT_MUTED)

    foot_y = CARD_H - mm(13.5)
    d.line((pad, foot_y, CARD_W - pad, foot_y), fill=AM_BORDER, width=mm(0.4))
    logo = logo_mark(5.2)
    img.paste(logo, (pad, foot_y + mm(1.8)), logo)
    f_foot = font(F_SANS_REG, 2.15)
    d.text((pad + logo.width + mm(2), foot_y + mm(2.7)),
           "KLARTEXT-Mentoring · Anti-Mobbing-Training · © 2026 Anja Jolk", font=f_foot, fill=KT_MUTED)

    img.save(out_path, dpi=(DPI, DPI))
    return img

if __name__ == "__main__":
    import os
    out_dir = "/sessions/kind-beautiful-ptolemy/mnt/outputs/stoppschild_bonuskarte/"
    os.makedirs(out_dir, exist_ok=True)
    build_front(os.path.join(out_dir, "Stoppschild_Vorderseite.png"))
    build_back(os.path.join(out_dir, "Stoppschild_Rueckseite.png"))
    print("Stoppschild fertig")
