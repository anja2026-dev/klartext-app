#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baut 3 druckfertige PDFs: Insel-Set Eltern, Insel-Set INGRA, Insel-Set LK. Cover + 2-seitiges
Handbuch + 8 Begleitkarten (Schul-Kartensatz für INGRA/LK, Eltern-Kartensatz fürs Eltern-PDF)."""
from PIL import Image, ImageDraw, ImageFont
import os, sys
Image.init()
sys.path.insert(0, os.path.dirname(__file__))
from build_booklet_insel import (eltern_seite1, eltern_seite2, ingra_seite1, ingra_seite2,
                                  lk_seite1, lk_seite2)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
KARTEN_SCHULE = os.path.join(BASE_DIR, "karten/insel_schule/")
KARTEN_ELTERN = os.path.join(BASE_DIR, "karten/insel_eltern/")
OUT_DIR = BASE_DIR

DPI = 300
MM = DPI / 25.4
def mm(v): return int(round(v * MM))

KT_PRIMARY = (27, 58, 75)
KT_ACCENT = (110, 198, 160)
KT_MUTED = (122, 112, 96)
KT_INK = (45, 45, 45)

F_SERIF_BOLD = "/usr/share/fonts/truetype/crosextra/Caladea-Bold.ttf"
F_SANS_REG = "/usr/share/fonts/truetype/lato/Lato-Regular.ttf"
F_SANS_BOLD = "/usr/share/fonts/truetype/lato/Lato-Bold.ttf"

def build_cover(untertitel, zielgruppe_text, farbe=KT_PRIMARY):
    W, H = mm(210), mm(297)
    img = Image.new("RGB", (W, H), (255, 255, 255))
    d = ImageDraw.Draw(img)

    kopf_h = mm(60)
    d.rectangle((0, 0, W, kopf_h), fill=farbe)
    logo_s = mm(20)
    logo_y = (kopf_h - logo_s) // 2
    d.rounded_rectangle((mm(20), logo_y, mm(20) + logo_s, logo_y + logo_s), radius=mm(4),
                         fill=(255, 255, 255), outline=KT_ACCENT, width=mm(1.2))
    f_logo = ImageFont.truetype(F_SERIF_BOLD, mm(11))
    d.text((mm(20) + logo_s / 2, logo_y + logo_s / 2), "K", font=f_logo, anchor="mm", fill=farbe)

    f_titel = ImageFont.truetype(F_SERIF_BOLD, mm(11))
    d.text((mm(48), mm(21)), "KLARTEXT-Mentoring", font=f_titel, fill=(255, 255, 255))
    f_sub = ImageFont.truetype(F_SANS_REG, mm(5.5))
    d.text((mm(48), mm(34)), "Insel-Set · Raumstrukturierung", font=f_sub, fill=(220, 230, 225))

    haupt_text = "Insel-Set"
    size = 22.0
    f_haupt = ImageFont.truetype(F_SERIF_BOLD, mm(size))
    d.text((mm(20), mm(90)), haupt_text, font=f_haupt, fill=farbe)

    f_haupt2 = ImageFont.truetype(F_SANS_BOLD, mm(7))
    d.text((mm(20), mm(128)), untertitel, font=f_haupt2, fill=KT_INK)

    f_zg_label = ImageFont.truetype(F_SANS_BOLD, mm(5.5))
    d.text((mm(20), mm(146)), "FÜR WEN", font=f_zg_label, fill=farbe)
    f_zg = ImageFont.truetype(F_SANS_REG, mm(6.2))
    words = zielgruppe_text.split()
    lines, cur = [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if d.textlength(t, font=f_zg) <= W - mm(40):
            cur = t
        else:
            lines.append(cur); cur = w_
    if cur: lines.append(cur)
    ty = mm(156)
    for ln in lines:
        d.text((mm(20), ty), ln, font=f_zg, fill=KT_INK)
        ty += mm(8.5)

    box_y = mm(240)
    box_h = mm(22)
    d.rounded_rectangle((mm(20), box_y, W - mm(20), box_y + box_h), radius=mm(3), fill=(235, 240, 238))
    f_status_l = ImageFont.truetype(F_SANS_BOLD, mm(6))
    f_status = ImageFont.truetype(F_SANS_REG, mm(5.6))
    d.text((mm(28), box_y + mm(6)), "INHALT", font=f_status_l, fill=farbe)
    d.text((mm(28), box_y + mm(13)), "8 Begleitkarten + Handbuch, final.", font=f_status, fill=KT_INK)

    f_foot = ImageFont.truetype(F_SANS_REG, mm(5))
    d.text((mm(20), H - mm(18)), "KLARTEXT-Mentoring · © 2026 Anja Jolk", font=f_foot, fill=KT_MUTED)
    return img

def karten_seiten(karten_dir, prefix, anzahl):
    pages = []
    for nr in range(1, anzahl + 1):
        vorn = os.path.join(karten_dir, f"{prefix}-{nr:02d}_front.png")
        hinten = os.path.join(karten_dir, f"{prefix}-{nr:02d}_back.png")
        if os.path.exists(vorn) and os.path.exists(hinten):
            pages.append(Image.open(vorn).convert("RGB"))
            pages.append(Image.open(hinten).convert("RGB"))
    return pages

def run():
    # 1) Eltern
    eltern_pages = [build_cover("Für Zuhause", "Eltern und Familien"),
                     eltern_seite1(), eltern_seite2()]
    eltern_pages += karten_seiten(KARTEN_ELTERN, "ELTERN", 8)
    out = os.path.join(OUT_DIR, "KLARTEXT_Insel-Set_Eltern.pdf")
    eltern_pages[0].save(out, save_all=True, append_images=eltern_pages[1:], resolution=DPI)
    print(f"PDF fertig: {out} ({len(eltern_pages)} Seiten)")

    # 2) INGRA
    ingra_pages = [build_cover("Für Schule & OGS", "Pädagogische Fachkräfte (INGRA)"),
                    ingra_seite1(), ingra_seite2()]
    ingra_pages += karten_seiten(KARTEN_SCHULE, "SCHULE", 8)
    out = os.path.join(OUT_DIR, "KLARTEXT_Insel-Set_Schule_INGRA.pdf")
    ingra_pages[0].save(out, save_all=True, append_images=ingra_pages[1:], resolution=DPI)
    print(f"PDF fertig: {out} ({len(ingra_pages)} Seiten)")

    # 3) LK
    lk_pages = [build_cover("Für den Klassenraum", "Lehrkräfte"),
                lk_seite1(), lk_seite2()]
    lk_pages += karten_seiten(KARTEN_SCHULE, "SCHULE", 8)
    out = os.path.join(OUT_DIR, "KLARTEXT_Insel-Set_Schule_LK.pdf")
    lk_pages[0].save(out, save_all=True, append_images=lk_pages[1:], resolution=DPI)
    print(f"PDF fertig: {out} ({len(lk_pages)} Seiten)")

if __name__ == "__main__":
    run()
