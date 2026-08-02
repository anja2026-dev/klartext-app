#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baut großformatige Raummarkierungen (DIN A4, volle Seite) fürs Insel-Set – zum Ausdrucken,
Laminieren und an Wand/Boden anbringen. Getrennt von der kleinen A6-Begleitkarte (Regeln/Nutzen):
die Raummarkierung ist bewusst reduziert auf Symbol + Name, damit Kinder sie auf einen Blick im
Raum erkennen, nicht lesen müssen."""
from PIL import Image, ImageDraw, ImageFont
import os
Image.init()

DPI = 300
MM = DPI / 25.4
def mm(v): return int(round(v * MM))

W, H = mm(210), mm(297)  # DIN A4

WHITE = (255, 255, 255)
KT_MUTED = (255, 255, 255)

F_SERIF_BOLD = "/usr/share/fonts/truetype/crosextra/Caladea-Bold.ttf"
F_SANS_REG = "/usr/share/fonts/truetype/lato/Lato-Regular.ttf"
F_SANS_BOLD = "/usr/share/fonts/truetype/lato/Lato-Bold.ttf"

def build_marker(name, badge_image_path, farbe, out_path):
    # Textfarbe je nach Helligkeit des Hintergrunds wählen (Kontrast/Lesbarkeit auf großer Fläche)
    luminanz = 0.299 * farbe[0] + 0.587 * farbe[1] + 0.114 * farbe[2]
    text_farbe = WHITE if luminanz < 165 else (35, 35, 35)

    img = Image.new("RGB", (W, H), farbe)
    d = ImageDraw.Draw(img)

    # Weißer Rahmen-Streifen oben/unten für Schnittkante beim Laminieren
    rand = mm(8)
    d.rectangle((0, 0, W, rand), fill=WHITE)
    d.rectangle((0, H - rand, W, H), fill=WHITE)
    d.rectangle((0, 0, rand, H), fill=WHITE)
    d.rectangle((W - rand, 0, W, H), fill=WHITE)
    d.rounded_rectangle((rand, rand, W - rand, H - rand), radius=mm(6), fill=farbe)

    # Großes Badge-Symbol, zentriert, füllt fast die ganze Breite
    badge_size = mm(150)
    if os.path.exists(badge_image_path):
        raw = Image.open(badge_image_path).convert("RGB")
        src_ratio = raw.width / raw.height
        if src_ratio > 1:
            new_h = badge_size
            new_w = int(new_h * src_ratio)
        else:
            new_w = badge_size
            new_h = int(new_w / src_ratio)
        raw = raw.resize((new_w, new_h), Image.LANCZOS)
        left = (new_w - badge_size) // 2
        top = (new_h - badge_size) // 2
        raw = raw.crop((left, top, left + badge_size, top + badge_size))
        mask = Image.new("L", (badge_size, badge_size), 0)
        ImageDraw.Draw(mask).ellipse((0, 0, badge_size, badge_size), fill=255)
        px = (W - badge_size) // 2
        py = mm(30)
        # Weißer Ring hinter dem Badge für Kontrast
        ring = mm(6)
        d.ellipse((px - ring, py - ring, px + badge_size + ring, py + badge_size + ring), fill=WHITE)
        img.paste(raw, (px, py), mask)

    # Name, riesig, unten
    f_name = font_fit(d, name, W - mm(30))
    tw = d.textlength(name, font=f_name)
    ny = mm(30) + badge_size + mm(18)
    d.text(((W - tw) / 2, ny), name, font=f_name, fill=text_farbe)

    # Kleiner KLARTEXT-Schriftzug ganz unten, dezent
    f_foot = ImageFont.truetype(F_SANS_REG, mm(4.5))
    foot_text = "KLARTEXT-Mentoring · Insel-Set"
    fw = d.textlength(foot_text, font=f_foot)
    d.text(((W - fw) / 2, H - mm(16)), foot_text, font=f_foot, fill=text_farbe)

    img.save(out_path, dpi=(DPI, DPI))
    return img

def font_fit(draw, text, max_w, start=18.0, min_size=8.0):
    size = start
    f = ImageFont.truetype(F_SERIF_BOLD, mm(size))
    while draw.textlength(text, font=f) > max_w and size > min_size:
        size -= 0.5
        f = ImageFont.truetype(F_SERIF_BOLD, mm(size))
    return f
