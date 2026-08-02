#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""KD-Deck – Bonus-Barometer-Karte (physische Zeigekarte fürs Kind), gleiches A6-Format wie die Karten."""
from PIL import Image, ImageDraw, ImageFont
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from build_card_kd import (CARD_W, CARD_H, mm, KD, KD_LIGHT, KD_BORDER, KT_PRIMARY, KT_ACCENT,
                            KT_INK, KT_MUTED, WHITE, KT_PAPER, HINWEIS_BORDER,
                            F_SERIF_BOLD, F_SERIF_ITALIC, F_SANS_REG, F_SANS_MED, F_SANS_BOLD,
                            font, wrap_text, rounded_rect, logo_mark, DPI)

BAROMETER = [
    ((76, 175, 80), "GRÜN", "Alles gut"),
    ((249, 168, 37), "GELB", "Angespannt"),
    ((239, 108, 0), "ORANGE", "Ganz schön viel"),
    ((198, 40, 40), "ROT", "Zu viel!"),
    ((120, 120, 120), "GRAU", "Weiß nicht"),
]

def build_front(out_path):
    img = Image.new("RGB", (CARD_W, CARD_H), WHITE)
    d = ImageDraw.Draw(img)

    kopf_h = mm(11)
    d.rectangle((0, 0, CARD_W, kopf_h), fill=KD)
    logo = logo_mark(7)
    img.paste(logo, (mm(5), (kopf_h - logo.height) // 2), logo)
    f_badge = font(F_SANS_BOLD, 2.6)
    d.text((mm(5) + logo.width + mm(2.5), kopf_h / 2), "KD · BONUS-KARTE",
           font=f_badge, fill=(255, 255, 255), anchor="lm")

    f_titel = font(F_SERIF_BOLD, 6.2)
    ty = kopf_h + mm(8)
    d.text((mm(6), ty), "Wie fühle ich", font=f_titel, fill=KD)
    ty += mm(8.5)
    d.text((mm(6), ty), "mich gerade?", font=f_titel, fill=KD)
    ty += mm(12)

    bar_top = ty
    bar_h = (CARD_H - mm(6) - bar_top) // len(BAROMETER)
    f_lab = font(F_SANS_BOLD, 4.2)
    f_desc = font(F_SANS_REG, 3.4)
    for color, label, desc in BAROMETER:
        y0 = bar_top
        y1 = y0 + bar_h - mm(1.5)
        rounded_rect(d, (mm(6), y0, CARD_W - mm(6), y1), radius=mm(2), fill=color)
        d.text((mm(9), (y0 + y1) / 2), label, font=f_lab, fill=WHITE, anchor="lm")
        lw = d.textlength(label, font=f_lab)
        d.text((mm(9) + lw + mm(4), (y0 + y1) / 2), desc, font=f_desc, fill=(255, 255, 255, 230), anchor="lm")
        bar_top += bar_h

    img.save(out_path, dpi=(DPI, DPI))
    return img

def build_back(out_path):
    img = Image.new("RGB", (CARD_W, CARD_H), WHITE)
    d = ImageDraw.Draw(img)
    pad = mm(5.5)
    y = pad

    f_rstitel = font(F_SERIF_BOLD, 4.4)
    d.text((pad, y), "Wie fühle ich mich gerade?", font=f_rstitel, fill=KD)
    y += mm(9)
    d.line((pad, y, CARD_W - pad, y), fill=KD_BORDER, width=mm(0.4))
    y += mm(4.5)

    f_label = font(F_SANS_BOLD, 2.5)
    f_anleitung = font(F_SERIF_ITALIC, 3.3)
    d.text((pad, y), "ANLEITUNG", font=f_label, fill=KD)
    y += mm(4.8)
    anleitung = ("Karte griffbereit halten, wenn Worte gerade schwerfallen. Einfach fragen: "
                 "„Auf welche Farbe zeigst du gerade?“ Keine Bewertung, kein Nachfragen erzwingen.")
    for ln in wrap_text(d, anleitung, f_anleitung, CARD_W - 2 * pad):
        d.text((pad, y), ln, font=f_anleitung, fill=KT_MUTED)
        y += mm(5)
    y += mm(6)

    f_hint_label = font(F_SANS_BOLD, 2.5)
    f_hint = font(F_SANS_REG, 3.1)
    hint_pad_x, hint_pad_y = mm(3.6), mm(3.2)
    label_h = mm(4.3)
    hinweis = ("Zeigt das Kind wiederholt auf Orange oder Rot: die vier kLAR-Schritte nutzen "
               "(siehe „Die KLARTEXT-Methodik“ in der Anleitung). Ab Rot zusätzlich eine "
               "Fachperson einbeziehen.")
    lines = wrap_text(d, hinweis, f_hint, CARD_W - 2 * pad - 2 * hint_pad_x)
    line_h = mm(4.5)
    box_h = label_h + 2 * hint_pad_y + len(lines) * line_h - mm(1)
    rounded_rect(d, (pad, y, CARD_W - pad, y + box_h), radius=mm(2), fill=KT_PAPER)
    d.rounded_rectangle((pad, y, CARD_W - pad, y + box_h), radius=mm(2),
                         outline=HINWEIS_BORDER, width=mm(0.4))
    ty = y + hint_pad_y
    d.text((pad + hint_pad_x, ty), "TIPP FÜR DIE INGRA", font=f_hint_label, fill=(150, 120, 50))
    ty += label_h
    for ln in lines:
        d.text((pad + hint_pad_x, ty), ln, font=f_hint, fill=KT_INK)
        ty += line_h
    y += box_h

    foot_y = CARD_H - mm(15)
    d.line((pad, foot_y, CARD_W - pad, foot_y), fill=KD_BORDER, width=mm(0.4))
    logo = logo_mark(5.5)
    img.paste(logo, (pad, foot_y + mm(2)), logo)
    f_foot = font(F_SANS_REG, 2.3)
    d.text((pad + logo.width + mm(2), foot_y + mm(3)),
           "KLARTEXT-Mentoring · KD-Deck · © 2026 Anja Jolk", font=f_foot, fill=KT_MUTED)

    img.save(out_path, dpi=(DPI, DPI))
    return img

if __name__ == "__main__":
    out = "/sessions/kind-beautiful-ptolemy/mnt/outputs/kd_karten_komplett/"
    os.makedirs(out, exist_ok=True)
    build_front(out + "KD-Bonus_Vorderseite.png")
    build_back(out + "KD-Bonus_Rueckseite.png")
    print("fertig")
