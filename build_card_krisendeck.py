#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KLARTEXT Krisendeck – Kartengenerator (2. Deck der Handlungskarten-Serie, nach TK).
Adaptiert von build_card_tk.py: Rückseite (Situation/Schritte/Abgrenzung/Quelle) fast 1:1
übernommen. Vorderseite komplett neu – bewusst OHNE Foto (Themen wie Selbstverletzung/
Fremdgefährdung verbieten illustrative Szenen), stattdessen kleines Linien-Icon je Karte
(angelehnt an die in der App bereits verwendeten Emoji-Symbole) + kurze Erkennungssignale
als Schnellindex.
Baut Vorder- und Rückseite einer Karte als druckfertiges PNG (300 dpi, A6 105x148mm).
"""
from PIL import Image, ImageDraw, ImageFont
import os

DPI = 300
MM = DPI / 25.4
def mm(v): return int(round(v * MM))

CARD_W = mm(105)
CARD_H = mm(148)

# ── Farbe: identisch mit bestehender App-Feuerwehr-Farbe (Barometer Rot), kollisionsgeprüft
# gegen alle Deck-Farben (u.a. DaZ-Sek1 Bordeaux #6E1438 – RGB-Distanz ≈ 92, unkritisch).
# Kein Kollisionsrisiko erwartet, da Rot bislang von keinem anderen Deck als Markenfarbe
# genutzt wird und hier bewusst "ist" die Barometer-Rot-Antwort, nicht nur eine Produktfarbe. ──
FK          = (198, 40, 40)       # #C62828
FK_DARK     = (127, 0, 0)         # #7F0000
FK_LIGHT    = (253, 234, 234)     # #FDEAEA
FK_BORDER   = (244, 160, 160)     # #F4A0A0
KT_PRIMARY  = (27, 58, 75)        # #1B3A4B
KT_ACCENT   = (110, 198, 160)     # #6EC6A0
KT_INK      = (45, 45, 45)        # #2D2D2D
KT_MUTED    = (122, 112, 96)      # #7A7060
WHITE       = (255, 255, 255)
TUN_GREEN   = (46, 125, 50)       # #2E7D32
NICHT_RED   = (127, 0, 0)         # #7F0000 (dunkler als FK, damit auf FK_BG lesbar/abgesetzt)
TUN_BG      = (232, 245, 233)     # #E8F5E9
NICHT_BG    = (253, 235, 235)     # #FDEBEB

F_SERIF_BOLD   = "/usr/share/fonts/truetype/crosextra/Caladea-Bold.ttf"
F_SERIF_ITALIC = "/usr/share/fonts/truetype/crosextra/Caladea-Italic.ttf"
F_SANS_REG     = "/usr/share/fonts/truetype/lato/Lato-Regular.ttf"
F_SANS_MED     = "/usr/share/fonts/truetype/lato/Lato-Medium.ttf"
F_SANS_BOLD    = "/usr/share/fonts/truetype/lato/Lato-Bold.ttf"
F_ICONS        = "/usr/share/fonts/truetype/font-awesome/fontawesome-webfont.ttf"

# Font-Awesome-Icons statt handgezeichneter Formen – sauberer, professioneller lesbar.
# Ausgewählt passend zu den bereits in der App vergebenen Emoji-Symbolen je FK-Karte.
ICON_CODEPOINTS = {
    "blitz":        0xf0e7,  # fa-bolt (FK-01 Akute Eskalation)
    "mute":         0xf026,  # fa-volume-off (FK-02 Shutdown)
    "puls":         0xf21e,  # fa-heartbeat (FK-03 Panikattacke)
    "warndreieck":  0xf071,  # fa-exclamation-triangle (FK-04 Fremdgefährdung)
    "pflaster":     0xf0fa,  # fa-medkit (FK-05 Selbstverletzung)
    "laufen":       0xf08b,  # fa-sign-out (FK-06 Weglaufen/Flucht)
    "nebel":        0xf0c2,  # fa-cloud (FK-07 Dissoziation)
    "vulkan":       0xf06d,  # fa-fire (FK-08 Meltdown)
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

# ═══════════════════════════════════════════════════════════
# Icons: saubere Font-Awesome-Glyphen statt handgezeichneter Formen (deutlich besser lesbar).
def draw_icon(d, cx, cy, s, kind):
    """s = Icon-Größe in Pixel (Kantenhöhe). Zentriert auf (cx,cy), Farbe WHITE."""
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
    d.rectangle((0, 0, CARD_W, kopf_h), fill=FK)
    logo = logo_mark(7)
    img.paste(logo, (mm(5), (kopf_h - logo.height) // 2), logo)
    f_badge = font(F_SANS_BOLD, 2.5)
    d.text((mm(5) + logo.width + mm(2.5), kopf_h / 2), "AKUT · BAROMETER ROT",
           font=f_badge, fill=WHITE, anchor="lm")
    f_nr = font(F_SANS_BOLD, 2.6)
    nr_text = f"{card['id_text']} / 8"
    nr_w = d.textlength(nr_text, font=f_nr)
    d.text((CARD_W - mm(5) - nr_w, kopf_h / 2), nr_text, font=f_nr, fill=WHITE)

    # Rot-Feld mit zentriertem Icon statt Foto
    feld_h = mm(58)
    feld_top = kopf_h
    d.rectangle((0, feld_top, CARD_W, feld_top + feld_h), fill=FK)
    icon_cx, icon_cy = CARD_W / 2, feld_top + feld_h / 2
    draw_icon(d, icon_cx, icon_cy, mm(26), card["icon"])

    # Titel-Feld
    titel_top = feld_top + feld_h
    titel_h = mm(20)
    d.rectangle((0, titel_top, CARD_W, titel_top + titel_h), fill=FK_LIGHT)
    d.line((0, titel_top, CARD_W, titel_top), fill=FK_BORDER, width=mm(0.5))
    f_titel = font(F_SERIF_BOLD, 5.2)
    lines = wrap_text(d, card["titel"], f_titel, CARD_W - mm(10))
    ly = titel_top + mm(3.5)
    for ln in lines[:2]:
        d.text((mm(5), ly), ln, font=f_titel, fill=FK_DARK, anchor="la")
        ly += mm(6.2)

    # Erkennungssignale als Schnellindex
    sig_top = titel_top + titel_h
    d.rectangle((0, sig_top, CARD_W, CARD_H), fill=WHITE)
    f_lab = font(F_SANS_BOLD, 2.4)
    d.text((mm(5), sig_top + mm(3)), "ERKENNUNGSSIGNALE", font=f_lab, fill=FK)
    f_sig = font(F_SANS_REG, 2.9)
    sy = sig_top + mm(8)
    for sig in card["front_signale"]:
        d.ellipse((mm(5), sy + mm(1.1), mm(5) + mm(1.6), sy + mm(1.1) + mm(1.6)), fill=FK)
        for i, ln in enumerate(wrap_text(d, sig, f_sig, CARD_W - mm(13))):
            d.text((mm(8.5), sy + i * mm(3.6)), ln, font=f_sig, fill=KT_INK)
        sy += max(mm(4.4), len(wrap_text(d, sig, f_sig, CARD_W - mm(13))) * mm(3.6) + mm(1.2))

    img.save(out_path, dpi=(DPI, DPI))
    return img

def build_back(card, out_path):
    img = Image.new("RGB", (CARD_W, CARD_H), WHITE)
    d = ImageDraw.Draw(img)
    pad = mm(5.2)
    y = pad

    f_rstitel = font(F_SERIF_BOLD, 4.2)
    f_rsnr = font(F_SANS_REG, 2.4)
    nr_text = card["id_text"]
    titel_lines = wrap_text(d, card["titel"], f_rstitel, CARD_W - 2 * pad)
    ty = y
    for ln in titel_lines[:2]:
        d.text((pad, ty), ln, font=f_rstitel, fill=FK)
        ty += mm(5.3)
    d.text((pad, ty), nr_text, font=f_rsnr, fill=KT_MUTED)
    y = ty + mm(4.2)
    d.line((pad, y, CARD_W - pad, y), fill=FK_BORDER, width=mm(0.4))
    y += mm(2.8)

    f_label = font(F_SANS_BOLD, 2.3)
    f_situation = font(F_SERIF_ITALIC, 3.0)
    d.text((pad, y), "SITUATION", font=f_label, fill=FK)
    y += mm(3.9)
    for ln in wrap_text(d, card["situation"], f_situation, CARD_W - 2 * pad):
        d.text((pad, y), ln, font=f_situation, fill=KT_INK)
        y += mm(4.0)
    y += mm(2.6)

    d.text((pad, y), "SOFORTMASSNAHMEN", font=f_label, fill=FK)
    y += mm(3.9)
    f_schritt = font(F_SANS_REG, 2.8)
    for i, schritt in enumerate(card["schritte"], 1):
        nr_str = f"{i}"
        nr_w2 = mm(4.2)
        lines = wrap_text(d, schritt, f_schritt, CARD_W - 2 * pad - nr_w2)
        d.ellipse((pad, y, pad + mm(3.6), y + mm(3.6)), fill=FK)
        d.text((pad + mm(1.8), y + mm(1.8)), nr_str, font=font(F_SANS_BOLD, 2.1), fill=WHITE, anchor="mm")
        ty2 = y
        for ln in lines:
            d.text((pad + nr_w2, ty2), ln, font=f_schritt, fill=KT_INK)
            ty2 += mm(3.45)
        y = max(ty2, y + mm(4)) + mm(0.9)
    y += mm(1.4)

    f_ab_label = font(F_SANS_BOLD, 2.4)
    ab_rows = card["abgrenzung"]
    col_gap = mm(1.6)
    col_w = (CARD_W - 2 * pad - col_gap) / 2
    header_h = mm(4.2)
    rounded_rect(d, (pad, y, pad + col_w, y + header_h), radius=mm(1), fill=TUN_GREEN)
    rounded_rect(d, (pad + col_w + col_gap, y, CARD_W - pad, y + header_h), radius=mm(1), fill=NICHT_RED)
    f_ab_head = font(F_SANS_BOLD, 2.3)
    d.text((pad + col_w / 2, y + header_h / 2), "JETZT TUN", font=f_ab_head, fill=WHITE, anchor="mm")
    d.text((pad + col_w + col_gap + col_w / 2, y + header_h / 2), "JETZT NICHT", font=f_ab_head, fill=WHITE, anchor="mm")
    y += header_h + mm(1.2)

    f_ab_text = font(F_SANS_REG, 2.5)
    for tun, nicht in ab_rows:
        tun_lines = wrap_text(d, tun, f_ab_text, col_w - mm(3.5))
        nicht_lines = wrap_text(d, nicht, f_ab_text, col_w - mm(3.5))
        n_lines = max(len(tun_lines), len(nicht_lines))
        line_h = mm(3.3)
        row_h = n_lines * line_h + mm(1.8)
        rounded_rect(d, (pad, y, pad + col_w, y + row_h), radius=mm(1), fill=TUN_BG)
        rounded_rect(d, (pad + col_w + col_gap, y, CARD_W - pad, y + row_h), radius=mm(1), fill=NICHT_BG)
        ty3 = y + mm(0.9)
        for ln in tun_lines:
            d.text((pad + mm(1.8), ty3), ln, font=f_ab_text, fill=(30, 70, 32))
            ty3 += line_h
        ty3 = y + mm(0.9)
        for ln in nicht_lines:
            d.text((pad + col_w + col_gap + mm(1.8), ty3), ln, font=f_ab_text, fill=(90, 20, 20))
            ty3 += line_h
        y += row_h + mm(1.0)

    y += mm(1.0)
    foot_y = CARD_H - mm(13.5)
    if y > foot_y - mm(1):
        print(f"WARNUNG: Karte {card['id_text']} läuft in den Footer über "
              f"(Inhalt endet bei {y}px, Footer beginnt bei {foot_y}px)")
    f_verweis = font(F_SANS_REG, 2.15)
    for ln in wrap_text(d, "Verweis: " + card["verweis"], f_verweis, CARD_W - 2 * pad):
        d.text((pad, y), ln, font=f_verweis, fill=KT_MUTED)
        y += mm(2.9)

    d.line((pad, foot_y, CARD_W - pad, foot_y), fill=FK_BORDER, width=mm(0.4))
    logo = logo_mark(5.2)
    img.paste(logo, (pad, foot_y + mm(1.8)), logo)
    f_foot = font(F_SANS_REG, 2.15)
    d.text((pad + logo.width + mm(2), foot_y + mm(2.7)),
           "KLARTEXT-Mentoring · Krisendeck · © 2026 Anja Jolk", font=f_foot, fill=KT_MUTED)

    img.save(out_path, dpi=(DPI, DPI))
    return img
