#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KLARTEXT Werkzeugkarten-Deck – Kartengenerator (3. Deck der Handlungskarten-Serie, nach TK & Krisendeck).
20 Karten aus dem bestehenden App-Modul "M3 · Werkzeugkasten": 8 Situationskarten (M3-01–08,
5-Schritte-Reaktion + Werkzeug-Verweis) + 12 Werkzeugkarten (M3-09–20, Was-ist-das + So-geht's).
Farbe/Icon-Sprache wie Krisendeck: Font-Awesome statt Foto, App-eigene Farbe (Amber-Gold) übernommen.
Kein Brainy-Bild (TK hat nie eines bekommen, hier ebenfalls bewusst nur Text-Zeile statt neuer Grafik –
kein zusätzlicher Bildaufwand nötig).
"""
from PIL import Image, ImageDraw, ImageFont
import os

DPI = 300
MM = DPI / 25.4
def mm(v): return int(round(v * MM))

CARD_W = mm(105)
CARD_H = mm(148)

# ── Farbe: identisch mit bestehender App-M3-Farbe (Werkzeugkasten), kollisionsgeprüft.
# Nächste Nachbarfarbe EL-Terracotta #BF5B3E, RGB-Distanz ~42 (Minimum ~40-70) – knapp aber
# unterschiedliche Farbfamilie (gelblich vs. rötlich) und andere Produktkategorie, an Anja
# rückgemeldet, auf Wunsch beibehalten. ──
M3          = (176, 125, 42)      # #B07D2A
M3_DARK     = (122, 83, 24)       # #7A5318
M3_LIGHT    = (251, 244, 232)     # #FBF4E8
M3_BORDER   = (224, 200, 138)     # #E0C88A
KT_PRIMARY  = (27, 58, 75)        # #1B3A4B
KT_ACCENT   = (110, 198, 160)     # #6EC6A0
KT_INK      = (45, 45, 45)        # #2D2D2D
KT_MUTED    = (122, 112, 96)      # #7A7060
WHITE       = (255, 255, 255)

F_SERIF_BOLD   = "/usr/share/fonts/truetype/crosextra/Caladea-Bold.ttf"
F_SERIF_ITALIC = "/usr/share/fonts/truetype/crosextra/Caladea-Italic.ttf"
F_SANS_REG     = "/usr/share/fonts/truetype/lato/Lato-Regular.ttf"
F_SANS_MED     = "/usr/share/fonts/truetype/lato/Lato-Medium.ttf"
F_SANS_BOLD    = "/usr/share/fonts/truetype/lato/Lato-Bold.ttf"
F_ICONS        = "/usr/share/fonts/truetype/font-awesome/fontawesome-webfont.ttf"

ICON_CODEPOINTS = {
    "sun":            0xf185,  # M3-01 Tagesbeginn
    "ban":            0xf05e,  # M3-02 Verweigert Arbeit
    "bolt":           0xf0e7,  # M3-03 Wutausbruch
    "snowflake":      0xf2dc,  # M3-04 Freeze
    "exchange":       0xf0ec,  # M3-05 Übergang
    "users":          0xf0c0,  # M3-06 Konflikt
    "tint":           0xf043,  # M3-07 Weint
    "bell":           0xf0f3,  # M3-08 Krise/Feuerwehr
    "circle-notch":   0xf1ce,  # M3-09 Atemanker
    "refresh":        0xf021,  # M3-10 Liegende Acht
    "eye":            0xf06e,  # M3-11 5-Dinge-Grounding
    "headphones":     0xf025,  # M3-12 Reizfilter
    "flag":           0xf024,  # M3-13 Joker
    "pause":          0xf04c,  # M3-14 Mini-Pause
    "list-ol":        0xf0cb,  # M3-15 Schritt-Plan
    "dot-circle":     0xf192,  # M3-16 Igel-Ball
    "map":            0xf278,  # M3-17 Visualisierung
    "thumbs-up":      0xf087,  # M3-18 Lob-Sandwich
    "sitemap":        0xf0e8,  # M3-19 Brainy-Flow
    "leaf":           0xf06c,  # M3-20 Selbst-Regulation
    "hourglass-half": 0xf252,  # M3-21 Sichtbare Zeit
    "hand-paper-o":   0xf256,  # M3-22 Stopp-Hand-Signal
    "home":           0xf015,  # M3-23 Sicherer Ort
    "heartbeat":      0xf21e,  # M3-24 Körper-Check-In
    "handshake-o":    0xf2b5,  # M3-26 No-Blame-Approach
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
    d.rectangle((0, 0, CARD_W, kopf_h), fill=M3)
    logo = logo_mark(7)
    img.paste(logo, (mm(5), (kopf_h - logo.height) // 2), logo)
    f_badge = font(F_SANS_BOLD, 2.5)
    typ_label = "SITUATION" if card["typ"] == "situation" else "WERKZEUG"
    d.text((mm(5) + logo.width + mm(2.5), kopf_h / 2), typ_label, font=f_badge, fill=WHITE, anchor="lm")
    f_nr = font(F_SANS_BOLD, 2.6)
    nr_text = f"{card['id_text']} / {card.get('total', 26)}"
    nr_w = d.textlength(nr_text, font=f_nr)
    d.text((CARD_W - mm(5) - nr_w, kopf_h / 2), nr_text, font=f_nr, fill=WHITE)

    feld_h = mm(58)
    feld_top = kopf_h
    d.rectangle((0, feld_top, CARD_W, feld_top + feld_h), fill=M3)
    draw_icon(d, CARD_W / 2, feld_top + feld_h / 2, mm(26), card["icon"])

    titel_top = feld_top + feld_h
    titel_h = mm(22)
    d.rectangle((0, titel_top, CARD_W, titel_top + titel_h), fill=M3_LIGHT)
    d.line((0, titel_top, CARD_W, titel_top), fill=M3_BORDER, width=mm(0.5))
    f_titel = font(F_SERIF_BOLD, 4.9)
    lines = wrap_text(d, card["titel"], f_titel, CARD_W - mm(10))
    ly = titel_top + mm(3.5)
    for ln in lines[:2]:
        d.text((mm(5), ly), ln, font=f_titel, fill=M3_DARK, anchor="la")
        ly += mm(6.0)

    kontext_top = titel_top + titel_h
    d.rectangle((0, kontext_top, CARD_W, CARD_H), fill=WHITE)
    f_lab = font(F_SANS_BOLD, 2.4)
    label = "BAROMETER" if card["typ"] == "situation" else "WANN EINSETZEN"
    d.text((mm(5), kontext_top + mm(3)), label, font=f_lab, fill=M3)
    f_kontext = font(F_SANS_REG, 3.1)
    ky = kontext_top + mm(8)
    for ln in wrap_text(d, card["front_kontext"], f_kontext, CARD_W - mm(10)):
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
        d.text((pad, ty), ln, font=f_rstitel, fill=M3)
        ty += mm(5.3)
    d.text((pad, ty), card["id_text"], font=f_rsnr, fill=KT_MUTED)
    y = ty + mm(4.2)
    d.line((pad, y, CARD_W - pad, y), fill=M3_BORDER, width=mm(0.4))
    y += mm(2.6)

    f_label = font(F_SANS_BOLD, 2.3)
    f_lead = font(F_SERIF_ITALIC, 2.9)

    if card["typ"] == "situation":
        d.text((pad, y), "SITUATION", font=f_label, fill=M3)
        y += mm(3.7)
        for ln in wrap_text(d, card["lead"], f_lead, CARD_W - 2 * pad):
            d.text((pad, y), ln, font=f_lead, fill=KT_INK)
            y += mm(3.8)
        y += mm(2.2)
        schritt_label = "SCHRITTE"
    else:
        d.text((pad, y), "WAS IST DAS", font=f_label, fill=M3)
        y += mm(3.7)
        for ln in wrap_text(d, card["lead"], f_lead, CARD_W - 2 * pad):
            d.text((pad, y), ln, font=f_lead, fill=KT_INK)
            y += mm(3.8)
        y += mm(2.2)
        schritt_label = "SO GEHT'S"

    d.text((pad, y), schritt_label, font=f_label, fill=M3)
    y += mm(3.7)
    f_schritt = font(F_SANS_REG, 2.75)
    for i, schritt in enumerate(card["schritte"], 1):
        nr_w2 = mm(4.2)
        lines = wrap_text(d, schritt, f_schritt, CARD_W - 2 * pad - nr_w2)
        d.ellipse((pad, y, pad + mm(3.5), y + mm(3.5)), fill=M3)
        d.text((pad + mm(1.75), y + mm(1.75)), str(i), font=font(F_SANS_BOLD, 2.05), fill=WHITE, anchor="mm")
        ty2 = y
        for ln in lines:
            d.text((pad + nr_w2, ty2), ln, font=f_schritt, fill=KT_INK)
            ty2 += mm(3.35)
        y = max(ty2, y + mm(3.8)) + mm(0.8)
    y += mm(1.2)

    f_tipp_lab = font(F_SANS_BOLD, 2.3)
    f_tipp = font(F_SANS_REG, 2.55)
    tipp_lines = wrap_text(d, card["tipp"], f_tipp, CARD_W - 2 * pad - mm(3))
    box_h = mm(5.5) + len(tipp_lines) * mm(3.3)
    rounded_rect(d, (pad, y, CARD_W - pad, y + box_h), radius=mm(1.5), fill=M3_LIGHT)
    d.text((pad + mm(2), y + mm(1.6)), "TIPP", font=f_tipp_lab, fill=M3_DARK)
    ty3 = y + mm(5.2)
    for ln in tipp_lines:
        d.text((pad + mm(2), ty3), ln, font=f_tipp, fill=KT_INK)
        ty3 += mm(3.3)
    y += box_h + mm(2.0)

    if card["typ"] == "situation" and card.get("werkzeuge"):
        f_wz_lab = font(F_SANS_BOLD, 2.2)
        f_wz = font(F_SANS_REG, 2.5)
        d.text((pad, y), "WERKZEUGE", font=f_wz_lab, fill=M3)
        y += mm(3.4)
        for ln in wrap_text(d, card["werkzeuge"], f_wz, CARD_W - 2 * pad):
            d.text((pad, y), ln, font=f_wz, fill=KT_MUTED)
            y += mm(3.4)
        y += mm(1.0)

    foot_y = CARD_H - mm(13.5)
    if y > foot_y - mm(1):
        print(f"WARNUNG: Karte {card['id_text']} läuft in den Footer über "
              f"(Inhalt endet bei {y}px, Footer beginnt bei {foot_y}px)")
    f_brainy = font(F_SANS_REG, 2.15)
    for ln in wrap_text(d, "Brainy: " + card["brainy"], f_brainy, CARD_W - 2 * pad):
        d.text((pad, y), ln, font=f_brainy, fill=KT_MUTED)
        y += mm(2.9)

    d.line((pad, foot_y, CARD_W - pad, foot_y), fill=M3_BORDER, width=mm(0.4))
    logo = logo_mark(5.2)
    img.paste(logo, (pad, foot_y + mm(1.8)), logo)
    f_foot = font(F_SANS_REG, 2.15)
    d.text((pad + logo.width + mm(2), foot_y + mm(2.7)),
           "KLARTEXT-Mentoring · Werkzeugkarten · © 2026 Anja Jolk", font=f_foot, fill=KT_MUTED)

    img.save(out_path, dpi=(DPI, DPI))
    return img
