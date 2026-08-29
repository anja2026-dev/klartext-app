#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baut 2 druckfertige PDFs: Zonen-Set Schule (LK & INGRA) + Zonen-Set Zuhause (Eltern).
Cover + 2-seitiges Handbuch + 4 Begleitkarten (=Raummarkierung, klein/dezent A6) + bei Schule
zusätzlich die 4 Token-Karten-Sheets."""
from PIL import Image, ImageDraw, ImageFont
import os, sys
Image.init()
sys.path.insert(0, os.path.dirname(__file__))
from build_booklet_zonen import schule_seite1, schule_seite2, eltern_seite1, eltern_seite2

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
KARTEN_SCHULE = os.path.join(BASE_DIR, "karten/zonen_schule/")
KARTEN_ELTERN = os.path.join(BASE_DIR, "karten/zonen_eltern/")
TOKEN_SHEETS = os.path.join(BASE_DIR, "karten/zonen_token/")
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

def build_cover(untertitel, zielgruppe_text, inhalt_text, farbe=KT_PRIMARY):
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
    d.text((mm(48), mm(34)), "Zonen-Set · Jugendliche Sek I/II", font=f_sub, fill=(220, 230, 225))

    haupt_text = "Zonen-Set"
    f_haupt = ImageFont.truetype(F_SERIF_BOLD, mm(22))
    d.text((mm(20), mm(90)), haupt_text, font=f_haupt, fill=farbe)

    f_haupt2 = ImageFont.truetype(F_SANS_BOLD, mm(7))
    d.text((mm(20), mm(128)), untertitel, font=f_haupt2, fill=KT_INK)

    f_zg_label = ImageFont.truetype(F_SANS_BOLD, mm(5.5))
    d.text((mm(20), mm(146)), "FÜR WEN", font=f_zg_label, fill=farbe)
    f_zg = ImageFont.truetype(F_SANS_REG, mm(6.2))
    ty = _draw_wrapped(d, zielgruppe_text, f_zg, mm(20), mm(156), W - mm(40))

    ty += mm(6)
    f_inh_label = ImageFont.truetype(F_SANS_BOLD, mm(5.5))
    d.text((mm(20), ty), "KEIN BRAINY", font=f_inh_label, fill=farbe)
    ty += mm(10)
    f_inh = ImageFont.truetype(F_SANS_REG, mm(5.6))
    _draw_wrapped(d, inhalt_text, f_inh, mm(20), ty, W - mm(40))

    box_y = mm(240)
    box_h = mm(22)
    d.rounded_rectangle((mm(20), box_y, W - mm(20), box_y + box_h), radius=mm(3), fill=(235, 240, 238))
    f_status_l = ImageFont.truetype(F_SANS_BOLD, mm(6))
    f_status = ImageFont.truetype(F_SANS_REG, mm(5.6))
    d.text((mm(28), box_y + mm(6)), "INHALT", font=f_status_l, fill=farbe)
    d.text((mm(28), box_y + mm(13)), "4 Begleitkarten + Handbuch, final.", font=f_status, fill=KT_INK)

    f_foot = ImageFont.truetype(F_SANS_REG, mm(5))
    d.text((mm(20), H - mm(18)), "KLARTEXT-Mentoring · © 2026 Anja Jolk", font=f_foot, fill=KT_MUTED)
    return img

def _draw_wrapped(d, text, f, x, y, max_w, lh=mm(8.5)):
    words = text.split()
    lines, cur = [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if d.textlength(t, font=f) <= max_w:
            cur = t
        else:
            lines.append(cur); cur = w_
    if cur: lines.append(cur)
    for ln in lines:
        d.text((x, y), ln, font=f, fill=KT_INK)
        y += lh
    return y

def karten_seiten(karten_dir, prefix, anzahl):
    pages = []
    for nr in range(1, anzahl + 1):
        vorn = os.path.join(karten_dir, f"{prefix}-{nr:02d}_front.png")
        hinten = os.path.join(karten_dir, f"{prefix}-{nr:02d}_back.png")
        if os.path.exists(vorn) and os.path.exists(hinten):
            pages.append(Image.open(vorn).convert("RGB"))
            pages.append(Image.open(hinten).convert("RGB"))
    return pages

def token_seiten():
    pages = []
    for name in ["Rückzugs-Zone", "Fokus-Zone", "Klärungs-Zone", "Gesprächs-Zone"]:
        p = os.path.join(TOKEN_SHEETS, f"TOKEN-{name.replace(' ', '_')}.png")
        if os.path.exists(p):
            pages.append(Image.open(p).convert("RGB"))
    return pages

def run():
    # 1) Schule (LK & INGRA)
    schule_pages = [build_cover("Für Schule (LK & INGRA)", "Lehrkräfte und INGRA in Sek I/II",
                                 "Bewusst ohne Maskottchen – altersangemessene, nüchterne Gestaltung "
                                 "für Jugendliche."),
                     schule_seite1(), schule_seite2()]
    schule_pages += karten_seiten(KARTEN_SCHULE, "SCHULE", 4)
    schule_pages += token_seiten()
    out = os.path.join(OUT_DIR, "KLARTEXT_Zonen-Set_Schule.pdf")
    schule_pages[0].save(out, save_all=True, append_images=schule_pages[1:], resolution=DPI)
    print(f"PDF fertig: {out} ({len(schule_pages)} Seiten)")

    # 2) Eltern (Zuhause)
    eltern_pages = [build_cover("Für Zuhause", "Eltern von Jugendlichen (Sek I/II)",
                                 "Bewusst ohne Maskottchen – altersangemessene, nüchterne Gestaltung "
                                 "für Jugendliche."),
                     eltern_seite1(), eltern_seite2()]
    eltern_pages += karten_seiten(KARTEN_ELTERN, "ELTERN", 4)
    out = os.path.join(OUT_DIR, "KLARTEXT_Zonen-Set_Eltern.pdf")
    eltern_pages[0].save(out, save_all=True, append_images=eltern_pages[1:], resolution=DPI)
    print(f"PDF fertig: {out} ({len(eltern_pages)} Seiten)")

if __name__ == "__main__":
    run()
