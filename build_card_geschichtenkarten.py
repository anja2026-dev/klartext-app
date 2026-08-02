#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KLARTEXT Geschichtenkarten-Deck – Kartengenerator (30 Karten aus M6_Geschichtenkarten_Galerie.html).
Anders als alle bisherigen Decks: 3 farbige Sets innerhalb eines Decks (Set A Rot/B Blau/C Grün),
angepasste Töne gegenüber der App zur Kollisionsvermeidung (siehe Geschichtenkarten_Konzept.md).
Bild-Handling wie build_card_fs.py: Platzhalter-Fläche, falls Bild noch nicht generiert wurde
(Pipeline wird vor der Bildgenerierung testweise gerendert).
"""
from PIL import Image, ImageDraw, ImageFont
import os

DPI = 300
MM = DPI / 25.4
def mm(v): return int(round(v * MM))

CARD_W = mm(105)
CARD_H = mm(148)

SET_FARBEN = {
    "A": dict(farbe=(150, 30, 35), light=(252, 234, 234), border=(224, 178, 178), dark=(105, 18, 22), label="SET A · BRAINY ERLEBT MOBBING"),
    "B": dict(farbe=(21, 101, 192), light=(232, 241, 250), border=(178, 205, 232), dark=(14, 70, 133), label="SET B · BRAINY HILFT ANDEREN"),
    "C": dict(farbe=(46, 110, 60), light=(232, 245, 236), border=(178, 214, 188), dark=(28, 74, 40), label="SET C · BRAINY LERNT STRATEGIEN"),
}

KT_PRIMARY  = (27, 58, 75)
KT_ACCENT   = (110, 198, 160)
KT_INK      = (45, 45, 45)
KT_MUTED    = (122, 112, 96)
WHITE       = (255, 255, 255)

F_SERIF_BOLD   = "/usr/share/fonts/truetype/crosextra/Caladea-Bold.ttf"
F_SERIF_ITALIC = "/usr/share/fonts/truetype/crosextra/Caladea-Italic.ttf"
F_SANS_REG     = "/usr/share/fonts/truetype/lato/Lato-Regular.ttf"
F_SANS_MED     = "/usr/share/fonts/truetype/lato/Lato-Medium.ttf"
F_SANS_BOLD    = "/usr/share/fonts/truetype/lato/Lato-Bold.ttf"

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

def cover_crop(img, target_w, target_h):
    src_ratio = img.width / img.height
    tgt_ratio = target_w / target_h
    if src_ratio > tgt_ratio:
        new_h = target_h
        new_w = int(new_h * src_ratio)
    else:
        new_w = target_w
        new_h = int(new_w / src_ratio)
    img = img.resize((new_w, new_h), Image.LANCZOS)
    left = (new_w - target_w) // 2
    top = (new_h - target_h) // 2
    return img.crop((left, top, left + target_w, top + target_h))

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

# ═══════════════════════════════════════════════════════════
def build_front(card, image_path, out_path):
    sf = SET_FARBEN[card["set"]]
    img = Image.new("RGB", (CARD_W, CARD_H), WHITE)
    d = ImageDraw.Draw(img)

    kopf_h = mm(11)
    d.rectangle((0, 0, CARD_W, kopf_h), fill=sf["farbe"])
    logo = logo_mark(7)
    img.paste(logo, (mm(5), (kopf_h - logo.height) // 2), logo)
    f_badge = font(F_SANS_BOLD, 2.3)
    d.text((mm(5) + logo.width + mm(2.5), kopf_h / 2), sf["label"], font=f_badge, fill=WHITE, anchor="lm")
    f_nr = font(F_SANS_BOLD, 2.6)
    nr_text = f"{card['id_text']} / 30"
    nr_w = d.textlength(nr_text, font=f_nr)
    d.text((CARD_W - mm(5) - nr_w, kopf_h / 2), nr_text, font=f_nr, fill=WHITE)

    titel_h = mm(20)
    bild_h = CARD_H - kopf_h - titel_h
    bild_top = kopf_h
    if os.path.exists(image_path):
        raw = Image.open(image_path).convert("RGB")
        cropped = cover_crop(raw, CARD_W, bild_h)
        img.paste(cropped, (0, bild_top))
    else:
        d.rectangle((0, bild_top, CARD_W, bild_top + bild_h), fill=sf["light"])
        f_ph = font(F_SANS_REG, 3.2)
        ph_text = "Bild folgt"
        pw = d.textlength(ph_text, font=f_ph)
        d.text(((CARD_W - pw) / 2, bild_top + bild_h / 2), ph_text, font=f_ph, fill=sf["border"])

    tf_top = bild_top + bild_h
    d.rectangle((0, tf_top, CARD_W, CARD_H), fill=sf["light"])
    d.line((0, tf_top, CARD_W, tf_top), fill=sf["border"], width=mm(0.5))
    f_titel = font(F_SERIF_BOLD, 4.8)
    lines = wrap_text(d, card["titel"], f_titel, CARD_W - mm(10))
    ly = tf_top + mm(3.5)
    for ln in lines[:2]:
        d.text((mm(5), ly), ln, font=f_titel, fill=sf["dark"])
        ly += mm(5.8)

    img.save(out_path, dpi=(DPI, DPI))
    return img

def build_back(card, out_path):
    sf = SET_FARBEN[card["set"]]
    img = Image.new("RGB", (CARD_W, CARD_H), WHITE)
    d = ImageDraw.Draw(img)
    pad = mm(5.2)
    y = pad

    f_rstitel = font(F_SERIF_BOLD, 4.6)
    f_rsnr = font(F_SANS_REG, 2.4)
    titel_lines = wrap_text(d, card["titel"], f_rstitel, CARD_W - 2 * pad)
    ty = y
    for ln in titel_lines[:2]:
        d.text((pad, ty), ln, font=f_rstitel, fill=sf["farbe"])
        ty += mm(5.6)
    d.text((pad, ty), card["id_text"], font=f_rsnr, fill=KT_MUTED)
    y = ty + mm(4.4)
    d.line((pad, y, CARD_W - pad, y), fill=sf["border"], width=mm(0.4))
    y += mm(3)

    f_label = font(F_SANS_BOLD, 2.4)
    f_situation = font(F_SERIF_ITALIC, 3.4)
    d.text((pad, y), "SITUATION", font=f_label, fill=sf["farbe"])
    y += mm(4.2)
    for ln in wrap_text(d, card["situation"], f_situation, CARD_W - 2 * pad):
        d.text((pad, y), ln, font=f_situation, fill=KT_INK)
        y += mm(4.6)
    y += mm(3)

    d.text((pad, y), "FRAGEN ZUM GESPRÄCH", font=f_label, fill=sf["farbe"])
    y += mm(4.4)
    f_frage = font(F_SANS_REG, 3.1)
    for frage in card["fragen"]:
        for i, ln in enumerate(wrap_text(d, frage, f_frage, CARD_W - 2 * pad - mm(4))):
            prefix = "→ " if i == 0 else "   "
            d.text((pad, y), prefix + ln, font=f_frage, fill=KT_INK)
            y += mm(4.4)
        y += mm(0.8)
    y += mm(2)

    f_impuls_lab = font(F_SANS_BOLD, 2.3)
    f_impuls = font(F_SANS_REG, 2.9)
    impuls_lines = wrap_text(d, card["impuls"], f_impuls, CARD_W - 2 * pad - mm(3))
    box_h = mm(5.5) + len(impuls_lines) * mm(3.7)
    rounded_rect(d, (pad, y, CARD_W - pad, y + box_h), radius=mm(1.5), fill=sf["light"])
    d.text((pad + mm(2), y + mm(1.6)), "IMPULS", font=f_impuls_lab, fill=sf["dark"])
    ty3 = y + mm(5.2)
    for ln in impuls_lines:
        d.text((pad + mm(2), ty3), ln, font=f_impuls, fill=KT_INK)
        ty3 += mm(3.7)
    y += box_h + mm(2)

    foot_y = CARD_H - mm(13.5)
    if y > foot_y - mm(1):
        print(f"WARNUNG: Karte {card['id_text']} läuft in den Footer über "
              f"(Inhalt endet bei {y}px, Footer beginnt bei {foot_y}px)")

    d.line((pad, foot_y, CARD_W - pad, foot_y), fill=sf["border"], width=mm(0.4))
    logo = logo_mark(5.2)
    img.paste(logo, (pad, foot_y + mm(1.8)), logo)
    f_foot = font(F_SANS_REG, 2.15)
    d.text((pad + logo.width + mm(2), foot_y + mm(2.7)),
           "KLARTEXT-Mentoring · Geschichtenkarten · © 2026 Anja Jolk", font=f_foot, fill=KT_MUTED)

    img.save(out_path, dpi=(DPI, DPI))
    return img
