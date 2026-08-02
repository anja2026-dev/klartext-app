#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baut die Token-Karten fürs Zonen-Set (Scheckkartenformat, CR80/85.6x54mm). Kernstück der
unauffälligen Selbstwahl: Jede/r Jugendliche bekommt ein Set von 4 Token-Karten (eine pro Zone)
und legt die passende Karte verdeckt/offen auf eine vereinbarte Ablage, statt sichtbar quer durch
den Raum zur Zone zu laufen. Bewusst reduziert: nur Symbol + Name, keine Regeln/Nutzen-Text."""
from PIL import Image, ImageDraw, ImageFont
import os

DPI = 300
MM = DPI / 25.4
def mm(v): return int(round(v * MM))

CARD_W, CARD_H = mm(85.6), mm(54)  # CR80-Format
WHITE = (255, 255, 255)

F_SERIF_BOLD = "/usr/share/fonts/truetype/crosextra/Caladea-Bold.ttf"
F_SANS_REG = "/usr/share/fonts/truetype/lato/Lato-Regular.ttf"

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

def build_token(name, badge_image_path, farbe):
    img = Image.new("RGB", (CARD_W, CARD_H), farbe)
    d = ImageDraw.Draw(img)

    rand = mm(2)
    d.rounded_rectangle((rand, rand, CARD_W - rand, CARD_H - rand), radius=mm(3),
                         outline=WHITE, width=mm(0.8))

    badge_size = mm(26)
    px = mm(6)
    py = (CARD_H - badge_size) // 2
    if os.path.exists(badge_image_path):
        raw = Image.open(badge_image_path).convert("RGB")
        raw_fit = cover_crop(raw, badge_size, badge_size)
        mask = Image.new("L", (badge_size, badge_size), 0)
        ImageDraw.Draw(mask).ellipse((0, 0, badge_size, badge_size), fill=255)
        img.paste(raw_fit, (px, py), mask)
        d.ellipse((px, py, px + badge_size, py + badge_size), outline=WHITE, width=mm(1))

    f_name = font_fit(d, name, CARD_W - px - badge_size - mm(12))
    tx = px + badge_size + mm(4)
    bbox = d.textbbox((0, 0), name, font=f_name)
    th = bbox[3] - bbox[1]
    d.text((tx, (CARD_H - th) / 2 - bbox[1]), name, font=f_name, fill=WHITE)

    f_foot = ImageFont.truetype(F_SANS_REG, mm(2.2))
    d.text((mm(6), CARD_H - mm(6)), "KLARTEXT · Zonen-Set", font=f_foot, fill=WHITE)

    return img

def font_fit(draw, text, max_w, start=5.5, min_size=3.0):
    size = start
    f = ImageFont.truetype(F_SERIF_BOLD, mm(size))
    while draw.textlength(text, font=f) > max_w and size > min_size:
        size -= 0.3
        f = ImageFont.truetype(F_SERIF_BOLD, mm(size))
    return f
