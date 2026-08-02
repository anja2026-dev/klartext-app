#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KLARTEXT TR-Deck – Kartengenerator (adaptiert von build_card_lk.py).
Baut Vorder- und Rückseite einer Karte als druckfertiges PNG (300 dpi, A6 105x148mm).
Rückseiten-Hinweisbox "TIPP FÜR DICH" wie bei EL/LK, dritte systemische Frage wie bei EL/LK.
"""
from PIL import Image, ImageDraw, ImageFont
import os

DPI = 300
MM = DPI / 25.4
def mm(v): return int(round(v * MM))

CARD_W = mm(105)
CARD_H = mm(148)

# ── Farben (TR-Deckfarbe: Slate-Blau #3E5C76 – kollisionsgeprüft gegen bestehende
# App-Modulfarben: TR-App-Modul=Braun/Gold #7A4C00, LK-App-Modul=Blau #1565C0,
# KD-App-Modul=Teal #00838F/#4FC3C7, Elternkurs(App)=Magenta #AD1457, sowie gegen die
# bestehenden Deckfarben JD-Petrol #2F6B6E, KD-Grün #2E9E5A, EL-Terracotta #BF5B3E,
# LK-Pflaume #6B4E71. Slate-Blau bewusst nicht die App-TR-Farbe (Braun/Gold), um
# Verwechslung mit dem bestehenden TR-App-Modul zu vermeiden – gleiches Muster wie bei EL/LK.) ──
TR          = (62, 92, 118)       # #3E5C76
TR_LIGHT    = (233, 238, 242)     # #E9EEF2
TR_BORDER   = (185, 199, 209)     # #B9C7D1
KT_PRIMARY  = (27, 58, 75)        # #1B3A4B
KT_ACCENT   = (110, 198, 160)     # #6EC6A0
KT_INK      = (45, 45, 45)        # #2D2D2D
KT_MUTED    = (122, 112, 96)      # #7A7060
WHITE       = (255, 255, 255)
KT_PAPER    = (245, 240, 232)     # #F5F0E8
HINWEIS_BORDER = (196, 176, 120)

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
    img = Image.new("RGB", (CARD_W, CARD_H), WHITE)
    d = ImageDraw.Draw(img)

    kopf_h = mm(11)
    d.rectangle((0, 0, CARD_W, kopf_h), fill=TR)
    logo = logo_mark(7)
    img.paste(logo, (mm(5), (kopf_h - logo.height) // 2), logo)
    f_badge = font(F_SANS_BOLD, 2.6)
    badge_text = card.get("badge", "TR · TRAINER-DECK")
    d.text((mm(5) + logo.width + mm(2.5), kopf_h / 2), badge_text,
           font=f_badge, fill=(255, 255, 255, 217), anchor="lm")
    f_nr = font(F_SANS_BOLD, 2.6)
    total = card.get("total", 29)
    nr_text = f"{card['nr']:02d} / {total}"
    nr_w = d.textlength(nr_text, font=f_nr)
    d.text((CARD_W - mm(5) - nr_w, kopf_h / 2), nr_text, font=f_nr, fill=(255, 255, 255))

    titel_h = mm(20)
    bild_h = CARD_H - kopf_h - titel_h
    bild_top = kopf_h
    if os.path.exists(image_path):
        raw = Image.open(image_path).convert("RGB")
        cropped = cover_crop(raw, CARD_W, bild_h)
        img.paste(cropped, (0, bild_top))
    else:
        d.rectangle((0, bild_top, CARD_W, bild_top + bild_h), fill=(224, 229, 234))

    tf_top = bild_top + bild_h
    d.rectangle((0, tf_top, CARD_W, CARD_H), fill=TR_LIGHT)
    d.line((0, tf_top, CARD_W, tf_top), fill=TR_BORDER, width=mm(0.5))
    f_titel = font(F_SERIF_BOLD, 5)
    lines = wrap_text(d, card["titel"], f_titel, CARD_W - mm(10))
    ly = tf_top + mm(4)
    for ln in lines[:2]:
        d.text((mm(5), ly), ln, font=f_titel, fill=TR)
        ly += mm(6.2)

    img.save(out_path, dpi=(DPI, DPI))
    return img

def build_back(card, out_path):
    img = Image.new("RGB", (CARD_W, CARD_H), WHITE)
    d = ImageDraw.Draw(img)
    pad = mm(5.5)
    y = pad

    f_rstitel = font(F_SERIF_BOLD, 4.4)
    f_rsnr = font(F_SANS_REG, 2.5)
    nr_text = card.get("id_text", f"TR-{card['nr']:02d}")
    nr_w = d.textlength(nr_text, font=f_rsnr)
    titel_lines = wrap_text(d, card["titel"], f_rstitel, CARD_W - 2 * pad - nr_w - mm(3))
    if len(titel_lines) > 2:
        titel_lines = wrap_text(d, card["titel"], f_rstitel, CARD_W - 2 * pad)
        ty = y
        for ln in titel_lines[:2]:
            d.text((pad, ty), ln, font=f_rstitel, fill=TR)
            ty += mm(5.6)
        d.text((pad, ty), nr_text, font=f_rsnr, fill=KT_MUTED)
        y = ty + mm(4.5)
    else:
        ty = y
        for ln in titel_lines:
            d.text((pad, ty), ln, font=f_rstitel, fill=TR)
            ty += mm(5.6)
        d.text((CARD_W - pad - nr_w, y + mm(1.8)), nr_text, font=f_rsnr, fill=KT_MUTED)
        y = max(ty, y + mm(9))
    d.line((pad, y, CARD_W - pad, y), fill=TR_BORDER, width=mm(0.4))
    y += mm(3.3)

    f_label = font(F_SANS_BOLD, 2.4)
    f_anleitung = font(F_SERIF_ITALIC, 3.1)
    d.text((pad, y), "ANLEITUNG", font=f_label, fill=TR)
    y += mm(4.3)
    for ln in wrap_text(d, card["anleitung"], f_anleitung, CARD_W - 2 * pad):
        d.text((pad, y), ln, font=f_anleitung, fill=KT_MUTED)
        y += mm(4.4)
    y += mm(3.3)

    d.text((pad, y), "IMPULSFRAGEN", font=f_label, fill=TR)
    y += mm(4.6)
    f_frage = font(F_SANS_MED, 3.5)
    box_pad_x, box_pad_y = mm(3.2), mm(2.6)
    for frage in card["fragen"]:
        lines = wrap_text(d, frage, f_frage, CARD_W - 2 * pad - 2 * box_pad_x - mm(1))
        line_h = mm(4.5)
        box_h = 2 * box_pad_y + len(lines) * line_h
        rounded_rect(d, (pad, y, CARD_W - pad, y + box_h), radius=mm(2), fill=TR_LIGHT)
        d.rectangle((pad, y, pad + mm(1), y + box_h), fill=TR)
        ty = y + box_pad_y
        for ln in lines:
            d.text((pad + mm(1) + box_pad_x, ty), ln, font=f_frage, fill=KT_INK)
            ty += line_h
        y += box_h + mm(2.6)

    if card.get("systemfrage"):
        sf_label, sf_text = card["systemfrage"]
        f_sf_label = font(F_SANS_BOLD, 2.3)
        f_sf = font(F_SANS_MED, 3.5)
        sf_pad_x, sf_pad_y = mm(3.2), mm(2.4)
        sf_label_h = mm(3.4)
        lines = wrap_text(d, sf_text, f_sf, CARD_W - 2 * pad - 2 * sf_pad_x - mm(1))
        line_h = mm(4.5)
        box_h = sf_label_h + 2 * sf_pad_y + len(lines) * line_h
        SYS = (27, 58, 75)
        SYS_LIGHT = (223, 231, 236)
        rounded_rect(d, (pad, y, CARD_W - pad, y + box_h), radius=mm(2), fill=SYS_LIGHT)
        d.rectangle((pad, y, pad + mm(1), y + box_h), fill=SYS)
        ty = y + sf_pad_y
        d.text((pad + mm(1) + sf_pad_x, ty), sf_label, font=f_sf_label, fill=SYS)
        ty += sf_label_h
        for ln in lines:
            d.text((pad + mm(1) + sf_pad_x, ty), ln, font=f_sf, fill=KT_INK)
            ty += line_h
        y += box_h + mm(2.6)

    if card.get("hinweis"):
        y += mm(3)
        f_hint_label = font(F_SANS_BOLD, 2.3)
        f_hint = font(F_SANS_REG, 2.9)
        hint_pad_x, hint_pad_y = mm(3.2), mm(2.6)
        label_h = mm(3.8)
        lines = wrap_text(d, card["hinweis"], f_hint, CARD_W - 2 * pad - 2 * hint_pad_x)
        line_h = mm(4)
        box_h = label_h + 2 * hint_pad_y + len(lines) * line_h - mm(1)
        rounded_rect(d, (pad, y, CARD_W - pad, y + box_h), radius=mm(2), fill=KT_PAPER)
        d.rounded_rectangle((pad, y, CARD_W - pad, y + box_h), radius=mm(2),
                             outline=HINWEIS_BORDER, width=mm(0.4))
        ty = y + hint_pad_y
        d.text((pad + hint_pad_x, ty), "TIPP FÜR DICH", font=f_hint_label, fill=(150, 120, 50))
        ty += label_h
        for ln in lines:
            d.text((pad + hint_pad_x, ty), ln, font=f_hint, fill=KT_INK)
            ty += line_h
        y += box_h

    foot_y = CARD_H - mm(15)
    if y > foot_y - mm(1):
        print(f"WARNUNG: Karte {card.get('id_text', card.get('nr'))} läuft in den Footer über "
              f"(Inhalt endet bei {y}px, Footer beginnt bei {foot_y}px)")
    d.line((pad, foot_y, CARD_W - pad, foot_y), fill=TR_BORDER, width=mm(0.4))
    logo = logo_mark(5.5)
    img.paste(logo, (pad, foot_y + mm(2)), logo)
    f_foot = font(F_SANS_REG, 2.3)
    footer_deck = card.get("footer_deck", "TR-Deck")
    d.text((pad + logo.width + mm(2), foot_y + mm(3)),
           f"KLARTEXT-Mentoring · {footer_deck} · © 2026 Anja Jolk", font=f_foot, fill=KT_MUTED)

    img.save(out_path, dpi=(DPI, DPI))
    return img
