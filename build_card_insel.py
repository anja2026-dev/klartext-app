#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KLARTEXT Insel-Set – Begleitkarten-Generator (Badge-Format statt Reflexionsformat).
Baut Vorder- und Rückseite einer Karte als druckfertiges PNG (300 dpi, A6 105x148mm).
Vorderseite: großes Badge-Symbol + Name. Rückseite: Zweck/Ort + Regeln + Nutzen.
Eine Karte pro Insel, Farbe wird pro Karte übergeben (siehe INSEL-Set_Konzept_und_Barometer-Integration.md).
"""
from PIL import Image, ImageDraw, ImageFont
import os

DPI = 300
MM = DPI / 25.4
def mm(v): return int(round(v * MM))

CARD_W = mm(105)
CARD_H = mm(148)

KT_PRIMARY  = (27, 58, 75)
KT_ACCENT   = (110, 198, 160)
KT_INK      = (45, 45, 45)
KT_MUTED    = (122, 112, 96)
WHITE       = (255, 255, 255)

F_SERIF_BOLD   = "/usr/share/fonts/truetype/crosextra/Caladea-Bold.ttf"
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

def rounded_rect(draw, box, radius, fill):
    draw.rounded_rectangle(box, radius=radius, fill=fill)

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
    """card: dict mit name, farbe (RGB), farbe_light (RGB), set_label, nr, total, badge_datei"""
    farbe = card["farbe"]
    farbe_light = card["farbe_light"]
    img = Image.new("RGB", (CARD_W, CARD_H), WHITE)
    d = ImageDraw.Draw(img)

    kopf_h = mm(11)
    d.rectangle((0, 0, CARD_W, kopf_h), fill=farbe)
    logo = logo_mark(7)
    img.paste(logo, (mm(5), (kopf_h - logo.height) // 2), logo)
    f_badge = font(F_SANS_BOLD, 2.6)
    d.text((mm(5) + logo.width + mm(2.5), kopf_h / 2), card["set_label"],
           font=f_badge, fill=(255, 255, 255))
    f_nr = font(F_SANS_BOLD, 2.6)
    nr_text = f"{card['nr']:02d} / {card['total']}"
    nr_w = d.textlength(nr_text, font=f_nr)
    d.text((CARD_W - mm(5) - nr_w, kopf_h / 2), nr_text, font=f_nr, fill=(255, 255, 255))

    bild_h = mm(95)
    bild_top = kopf_h
    d.rectangle((0, bild_top, CARD_W, bild_top + bild_h), fill=farbe_light)
    if os.path.exists(image_path):
        raw = Image.open(image_path).convert("RGB")
        badge_size = mm(70)
        raw_fit = cover_crop(raw, badge_size, badge_size)
        mask = Image.new("L", (badge_size, badge_size), 0)
        ImageDraw.Draw(mask).ellipse((0, 0, badge_size, badge_size), fill=255)
        px = (CARD_W - badge_size) // 2
        py = bild_top + (bild_h - badge_size) // 2
        img.paste(raw_fit, (px, py), mask)
        d.ellipse((px, py, px + badge_size, py + badge_size), outline=farbe, width=mm(0.8))

    tf_top = bild_top + bild_h
    d.rectangle((0, tf_top, CARD_W, CARD_H), fill=farbe_light)
    f_titel = font(F_SERIF_BOLD, 6)
    lines = wrap_text(d, card["name"], f_titel, CARD_W - mm(10))
    total_h = len(lines) * mm(7.2)
    ly = tf_top + (CARD_H - tf_top - total_h) / 2
    for ln in lines:
        tw = d.textlength(ln, font=f_titel)
        d.text(((CARD_W - tw) / 2, ly), ln, font=f_titel, fill=farbe)
        ly += mm(7.2)

    img.save(out_path, dpi=(DPI, DPI))
    return img

def build_back(card, out_path):
    farbe = card["farbe"]
    farbe_light = card["farbe_light"]
    img = Image.new("RGB", (CARD_W, CARD_H), WHITE)
    d = ImageDraw.Draw(img)
    pad = mm(5.5)
    y = pad

    f_rstitel = font(F_SERIF_BOLD, 5)
    d.text((pad, y), card["name"], font=f_rstitel, fill=farbe)
    y += mm(8)
    d.line((pad, y, CARD_W - pad, y), fill=farbe_light, width=mm(0.6))
    y += mm(4)

    f_label = font(F_SANS_BOLD, 2.4)
    f_text = font(F_SANS_REG, 3.3)
    d.text((pad, y), "ZWECK / ORT", font=f_label, fill=farbe)
    y += mm(4.3)
    for ln in wrap_text(d, card["zweck"], f_text, CARD_W - 2 * pad):
        d.text((pad, y), ln, font=f_text, fill=KT_INK)
        y += mm(4.6)
    y += mm(4)

    d.text((pad, y), "REGELN", font=f_label, fill=farbe)
    y += mm(4.6)
    f_regel = font(F_SANS_MED, 3.3)
    for regel in card["regeln"]:
        d.ellipse((pad, y + mm(1.2), pad + mm(1.8), y + mm(3)), fill=farbe)
        lines = wrap_text(d, regel, f_regel, CARD_W - 2 * pad - mm(6))
        for i, ln in enumerate(lines):
            d.text((pad + mm(5), y + i * mm(4.4)), ln, font=f_regel, fill=KT_INK)
        y += len(lines) * mm(4.4) + mm(2)
    y += mm(3)

    rounded_rect(d, (pad, y, CARD_W - pad, CARD_H - mm(18)), radius=mm(2), fill=farbe_light)
    ny = y + mm(3)
    d.text((pad + mm(3), ny), "NUTZEN", font=f_label, fill=farbe)
    ny += mm(4.6)
    f_nutzen = font(F_SANS_REG, 3.1)
    for nutzen in card["nutzen"]:
        lines = wrap_text(d, "· " + nutzen, f_nutzen, CARD_W - 2 * pad - mm(6))
        for ln in lines:
            d.text((pad + mm(3), ny), ln, font=f_nutzen, fill=KT_INK)
            ny += mm(4.2)
        ny += mm(1)

    foot_y = CARD_H - mm(15)
    d.line((pad, foot_y, CARD_W - pad, foot_y), fill=farbe_light, width=mm(0.4))
    logo = logo_mark(5.5)
    img.paste(logo, (pad, foot_y + mm(2)), logo)
    f_foot = font(F_SANS_REG, 2.3)
    d.text((pad + logo.width + mm(2), foot_y + mm(3)),
           f"KLARTEXT-Mentoring · {card['set_label']} · © 2026 Anja Jolk", font=f_foot, fill=KT_MUTED)

    img.save(out_path, dpi=(DPI, DPI))
    return img
