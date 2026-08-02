#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KLARTEXT Hochbegabungsdeck – Kartengenerator. 12 Karten in drei Blöcken (Erkennen,
Herausforderungen, Handeln), gestützt auf Renzulli (1978), Mönks (1990), Heller/Perleth/Hany
(Münchner Begabungsmodell), Gagné (DMGT), Rost/Karg-Stiftung (Underachievement) sowie aktueller
Twice-Exceptional-Forschung. Neu entwickelter Inhalt (kein bestehendes App-Modul als Quelle),
wissenschaftlich fundiert, vollständige Angaben im Anleitungs-Booklet.
Icon-basiert wie Krisendeck/Werkzeugkarten/Mobbing, kein neues Bildmaterial.
Farbe: Kobaltblau #2024C4, kollisionsgeprüft gegen alle bestehenden Deckfarben
(nächster Nachbar TK-Violett, ~72 Einheiten Abstand, unproblematisch).
"""
from PIL import Image, ImageDraw, ImageFont
import os

DPI = 300
MM = DPI / 25.4
def mm(v): return int(round(v * MM))

CARD_W = mm(105)
CARD_H = mm(148)

HB          = (32, 36, 196)       # #2024C4 Kobaltblau
HB_DARK     = (22, 25, 140)       # #16198C
HB_LIGHT    = (227, 228, 250)     # #E3E4FA
HB_BORDER   = (178, 181, 237)
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
F_ICONS        = "/usr/share/fonts/truetype/font-awesome/fontawesome-webfont.ttf"

ICON_CODEPOINTS = {
    "idee":        0xf0eb,   # HB-01 Was ist Hochbegabung?
    "suche":       0xf002,   # HB-02 Merkmale erkennen
    "asynchron":   0xf074,   # HB-03 Asynchrone Entwicklung
    "abwaerts":    0xf149,   # HB-04 Underachievement
    "achtung":     0xf06a,   # HB-05 Perfektionismus & Versagensangst
    "gruppe":      0xf0c0,   # HB-06 Soziale Herausforderungen
    "doppel":      0xf0ec,   # HB-07 Doppelbegabung / Twice-Exceptional
    "uhr":         0xf017,   # HB-08 Langeweile & Verweigerung
    "rakete":      0xf135,   # HB-09 Enrichment & Akzeleration
    "liste":       0xf022,   # HB-10 Diagnostik: wann testen?
    "handschlag":  0xf2b5,   # HB-11 Zusammenarbeit mit der Lehrkraft
    "dialog":      0xf086,   # HB-12 Elterngespräch bei Hochbegabung
}

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

def draw_icon(d, cx, cy, s, kind):
    cp = ICON_CODEPOINTS[kind]
    f = ImageFont.truetype(F_ICONS, int(s))
    ch = chr(cp)
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

# ═══════════════════════════════════════════════════════════
def build_front(card, out_path):
    img = Image.new("RGB", (CARD_W, CARD_H), WHITE)
    d = ImageDraw.Draw(img)

    kopf_h = mm(11)
    d.rectangle((0, 0, CARD_W, kopf_h), fill=HB)
    logo = logo_mark(7)
    img.paste(logo, (mm(5), (kopf_h - logo.height) // 2), logo)
    f_badge = font(F_SANS_BOLD, 2.5)
    d.text((mm(5) + logo.width + mm(2.5), kopf_h / 2), "HOCHBEGABUNG", font=f_badge, fill=WHITE, anchor="lm")
    f_nr = font(F_SANS_BOLD, 2.6)
    nr_text = f"{card['id_text']} / 12"
    nr_w = d.textlength(nr_text, font=f_nr)
    d.text((CARD_W - mm(5) - nr_w, kopf_h / 2), nr_text, font=f_nr, fill=WHITE)

    feld_h = mm(58)
    feld_top = kopf_h
    d.rectangle((0, feld_top, CARD_W, feld_top + feld_h), fill=HB)
    draw_icon(d, CARD_W / 2, feld_top + feld_h / 2, mm(26), card["icon"])

    titel_top = feld_top + feld_h
    titel_h = mm(24)
    d.rectangle((0, titel_top, CARD_W, titel_top + titel_h), fill=HB_LIGHT)
    d.line((0, titel_top, CARD_W, titel_top), fill=HB_BORDER, width=mm(0.5))
    f_titel = font(F_SERIF_BOLD, 4.9)
    lines = wrap_text(d, card["titel"], f_titel, CARD_W - mm(10))
    ly = titel_top + mm(3.5)
    for ln in lines[:2]:
        d.text((mm(5), ly), ln, font=f_titel, fill=HB_DARK, anchor="la")
        ly += mm(6.0)

    kontext_top = titel_top + titel_h
    d.rectangle((0, kontext_top, CARD_W, CARD_H), fill=WHITE)
    f_lab = font(F_SANS_BOLD, 2.4)
    d.text((mm(5), kontext_top + mm(3)), "FÜR", font=f_lab, fill=HB)
    f_kontext = font(F_SANS_REG, 3.1)
    ky = kontext_top + mm(8)
    for ln in wrap_text(d, card["fuer"], f_kontext, CARD_W - mm(10)):
        d.text((mm(5), ky), ln, font=f_kontext, fill=KT_INK)
        ky += mm(4.4)

    img.save(out_path, dpi=(DPI, DPI))
    return img

def build_back(card, out_path):
    img = Image.new("RGB", (CARD_W, CARD_H), WHITE)
    d = ImageDraw.Draw(img)
    pad = mm(5.2)
    y = pad

    f_rstitel = font(F_SERIF_BOLD, 4.2)
    f_rsnr = font(F_SANS_REG, 2.4)
    titel_lines = wrap_text(d, card["titel"], f_rstitel, CARD_W - 2 * pad)
    ty = y
    for ln in titel_lines[:2]:
        d.text((pad, ty), ln, font=f_rstitel, fill=HB)
        ty += mm(5.3)
    d.text((pad, ty), card["id_text"], font=f_rsnr, fill=KT_MUTED)
    y = ty + mm(4.2)
    d.line((pad, y, CARD_W - pad, y), fill=HB_BORDER, width=mm(0.4))
    y += mm(2.4)

    f_label = font(F_SANS_BOLD, 2.3)
    f_lead = font(F_SERIF_ITALIC, 2.8)
    d.text((pad, y), "WORUM ES GEHT", font=f_label, fill=HB)
    y += mm(3.5)
    for ln in wrap_text(d, card["lead"], f_lead, CARD_W - 2 * pad):
        d.text((pad, y), ln, font=f_lead, fill=KT_INK)
        y += mm(3.6)
    y += mm(1.8)

    d.text((pad, y), "SCHRITTE", font=f_label, fill=HB)
    y += mm(3.4)
    f_schritt = font(F_SANS_REG, 2.55)
    for i, schritt in enumerate(card["schritte"], 1):
        nr_w2 = mm(4.0)
        lines = wrap_text(d, schritt, f_schritt, CARD_W - 2 * pad - nr_w2)
        d.ellipse((pad, y, pad + mm(3.2), y + mm(3.2)), fill=HB)
        d.text((pad + mm(1.6), y + mm(1.6)), str(i), font=font(F_SANS_BOLD, 1.9), fill=WHITE, anchor="mm")
        ty2 = y
        for ln in lines:
            d.text((pad + nr_w2, ty2), ln, font=f_schritt, fill=KT_INK)
            ty2 += mm(3.1)
        y = max(ty2, y + mm(3.5)) + mm(0.6)
    y += mm(0.8)

    f_merk_lab = font(F_SANS_BOLD, 2.2)
    f_merk = font(F_SERIF_ITALIC, 2.9)
    merk_lines = wrap_text(d, card["merksatz"], f_merk, CARD_W - 2 * pad - mm(3))
    box_h = mm(5.2) + len(merk_lines) * mm(3.4)
    rounded_rect(d, (pad, y, CARD_W - pad, y + box_h), radius=mm(1.5), fill=HB_LIGHT)
    d.text((pad + mm(2), y + mm(1.5)), "MERKSATZ", font=f_merk_lab, fill=HB_DARK)
    ty3 = y + mm(4.9)
    for ln in merk_lines:
        d.text((pad + mm(2), ty3), ln, font=f_merk, fill=KT_INK, anchor="la")
        ty3 += mm(3.4)
    y += box_h + mm(2.0)

    foot_y = CARD_H - mm(13.5)
    if y > foot_y - mm(1):
        print(f"WARNUNG: Karte {card['id_text']} läuft in den Footer über "
              f"(Inhalt endet bei {y}px, Footer beginnt bei {foot_y}px)")
    f_brainy = font(F_SANS_REG, 2.15)
    for ln in wrap_text(d, "Brainy: " + card["brainy"], f_brainy, CARD_W - 2 * pad):
        d.text((pad, y), ln, font=f_brainy, fill=KT_MUTED)
        y += mm(2.9)

    d.line((pad, foot_y, CARD_W - pad, foot_y), fill=HB_BORDER, width=mm(0.4))
    logo = logo_mark(5.2)
    img.paste(logo, (pad, foot_y + mm(1.8)), logo)
    f_foot = font(F_SANS_REG, 2.15)
    d.text((pad + logo.width + mm(2), foot_y + mm(2.7)),
           "KLARTEXT-Mentoring · Hochbegabung · © 2026 Anja Jolk", font=f_foot, fill=KT_MUTED)

    img.save(out_path, dpi=(DPI, DPI))
    return img
