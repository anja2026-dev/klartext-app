#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KLARTEXT TK-Handlungskarten – Kartengenerator.
Erstes Deck im neuen Handlungskarten-Format (Situation/Schritte/Abgrenzung/Quelle),
adaptiert vom Vorderseiten-Layout aus build_card_lk.py, Rückseite komplett neu.
Baut Vorder- und Rückseite einer Karte als druckfertiges PNG (300 dpi, A6 105x148mm).
"""
from PIL import Image, ImageDraw, ImageFont
import os

DPI = 300
MM = DPI / 25.4
def mm(v): return int(round(v * MM))

CARD_W = mm(105)
CARD_H = mm(148)

# ── Farbe: identisch mit bestehender App-TK-Farbe (Teamkoordination), kollisionsgeprüft
# gegen alle Deck-Farben (KD Grün, EL Terracotta, LK Pflaume, TR Blaugrau, AT Salbei,
# ADHS Periwinkle, FS Gold, DaZ-GS Cyan, DaZ-Sek1 Wein). ──
TK          = (74, 20, 140)       # #4A148C
TK_LIGHT    = (243, 229, 255)     # #F3E5FF (identisch App-TK-Light)
TK_BORDER   = (206, 169, 226)     # #CEA9E2
KT_PRIMARY  = (27, 58, 75)        # #1B3A4B
KT_ACCENT   = (110, 198, 160)     # #6EC6A0
KT_INK      = (45, 45, 45)        # #2D2D2D
KT_MUTED    = (122, 112, 96)      # #7A7060
WHITE       = (255, 255, 255)
KT_PAPER    = (245, 240, 232)     # #F5F0E8
TUN_GREEN   = (46, 125, 50)       # #2E7D32
NICHT_RED   = (183, 28, 28)       # #B71C1C
TUN_BG      = (232, 245, 233)     # #E8F5E9
NICHT_BG    = (253, 235, 235)     # #FDEBEB

F_SERIF_BOLD   = "/usr/share/fonts/truetype/crosextra/Caladea-Bold.ttf"
F_SERIF_ITALIC = "/usr/share/fonts/truetype/crosextra/Caladea-Italic.ttf"
F_SANS_REG     = "/usr/share/fonts/truetype/lato/Lato-Regular.ttf"
F_SANS_MED     = "/usr/share/fonts/truetype/lato/Lato-Medium.ttf"
F_SANS_BOLD    = "/usr/share/fonts/truetype/lato/Lato-Bold.ttf"

KATEGORIE_LABEL = {
    "team": "Team & Koordination",
    "kind": "Kind & Familie",
    "system": "System & Schnittstellen",
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

BRAINY_ECKMARKE_PATH = "/sessions/kind-beautiful-ptolemy/mnt/klartext-app/bilder/tk/brainy_eckmarke.png"

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
    d.rectangle((0, 0, CARD_W, kopf_h), fill=TK)
    logo = logo_mark(7)
    img.paste(logo, (mm(5), (kopf_h - logo.height) // 2), logo)
    f_badge = font(F_SANS_BOLD, 2.5)
    badge_text = KATEGORIE_LABEL.get(card["kategorie"], "TK-Handlungskarten")
    d.text((mm(5) + logo.width + mm(2.5), kopf_h / 2), badge_text.upper(),
           font=f_badge, fill=WHITE, anchor="lm")
    f_nr = font(F_SANS_BOLD, 2.6)
    nr_text = f"{card['nr']:02d} / 19"
    nr_w = d.textlength(nr_text, font=f_nr)
    d.text((CARD_W - mm(5) - nr_w, kopf_h / 2), nr_text, font=f_nr, fill=WHITE)

    titel_h = mm(20)
    bild_h = CARD_H - kopf_h - titel_h
    bild_top = kopf_h
    if image_path and os.path.exists(image_path):
        raw = Image.open(image_path).convert("RGB")
        cropped = cover_crop(raw, CARD_W, bild_h)
        img.paste(cropped, (0, bild_top))
    else:
        d.rectangle((0, bild_top, CARD_W, bild_top + bild_h), fill=TK_LIGHT)

    # Brainy-Wiedererkennungsmarke: EIN einmalig erzeugtes Bild, per Code in die Ecke
    # eingefügt (statt 12x separat KI-generiert – vermeidet Konsistenzprobleme über
    # mehrere Bilder hinweg). Nur auf Karten mit Fall-/Kind-/Beziehungsbezug (card["brainy"]).
    if card.get("brainy") and os.path.exists(BRAINY_ECKMARKE_PATH):
        bsize = mm(14)
        brainy_img = Image.open(BRAINY_ECKMARKE_PATH).convert("RGBA")
        brainy_img = brainy_img.resize((bsize, bsize), Image.LANCZOS)
        bx, by = mm(3), bild_top + bild_h - bsize - mm(3)
        img.paste(brainy_img, (bx, by), brainy_img)

    # Tischwerkzeug-Markierung: kleines Eckband oben rechts im Bild
    if card.get("tischwerkzeug"):
        f_tw = font(F_SANS_BOLD, 2.1)
        tw_text = "TISCHWERKZEUG"
        tw_w = d.textlength(tw_text, font=f_tw)
        band_w, band_h = tw_w + mm(7), mm(6.5)
        bx0, by0 = CARD_W - band_w - mm(3), bild_top + mm(3)
        rounded_rect(d, (bx0, by0, bx0 + band_w, by0 + band_h), radius=mm(1.2), fill=(255, 255, 255))
        d.rounded_rectangle((bx0, by0, bx0 + band_w, by0 + band_h), radius=mm(1.2), outline=TK, width=mm(0.35))
        dot_cx, dot_r = bx0 + mm(3), mm(1.1)
        d.ellipse((dot_cx - dot_r, by0 + band_h / 2 - dot_r, dot_cx + dot_r, by0 + band_h / 2 + dot_r), fill=TK)
        d.text((bx0 + mm(5.5), by0 + band_h / 2), tw_text, font=f_tw, fill=TK, anchor="lm")

    tf_top = bild_top + bild_h
    d.rectangle((0, tf_top, CARD_W, CARD_H), fill=TK_LIGHT)
    d.line((0, tf_top, CARD_W, tf_top), fill=TK_BORDER, width=mm(0.5))
    f_titel = font(F_SERIF_BOLD, 4.8)
    lines = wrap_text(d, card["titel"], f_titel, CARD_W - mm(10))
    ly = tf_top + mm(4)
    for ln in lines[:2]:
        d.text((mm(5), ly), ln, font=f_titel, fill=TK)
        ly += mm(6)

    img.save(out_path, dpi=(DPI, DPI))
    return img

def build_back(card, out_path):
    img = Image.new("RGB", (CARD_W, CARD_H), WHITE)
    d = ImageDraw.Draw(img)
    pad = mm(5.2)
    y = pad

    f_rstitel = font(F_SERIF_BOLD, 4.2)
    f_rsnr = font(F_SANS_REG, 2.4)
    nr_text = card.get("id_text", f"TK-{card['nr']:02d}")
    nr_w = d.textlength(nr_text, font=f_rsnr)
    titel_lines = wrap_text(d, card["titel"], f_rstitel, CARD_W - 2 * pad)
    ty = y
    for ln in titel_lines[:2]:
        d.text((pad, ty), ln, font=f_rstitel, fill=TK)
        ty += mm(5.3)
    d.text((pad, ty), nr_text, font=f_rsnr, fill=KT_MUTED)
    y = ty + mm(4.2)
    d.line((pad, y, CARD_W - pad, y), fill=TK_BORDER, width=mm(0.4))
    y += mm(2.8)

    f_label = font(F_SANS_BOLD, 2.3)
    f_situation = font(F_SERIF_ITALIC, 3.0)
    d.text((pad, y), "SITUATION", font=f_label, fill=TK)
    y += mm(3.9)
    for ln in wrap_text(d, card["situation"], f_situation, CARD_W - 2 * pad):
        d.text((pad, y), ln, font=f_situation, fill=KT_INK)
        y += mm(4.0)
    y += mm(2.6)

    d.text((pad, y), "SCHRITTE", font=f_label, fill=TK)
    y += mm(3.9)
    f_schritt = font(F_SANS_REG, 2.85)
    f_schrittnr = font(F_SANS_BOLD, 2.85)
    for i, schritt in enumerate(card["schritte"], 1):
        nr_str = f"{i}"
        nr_w2 = mm(4.2)
        lines = wrap_text(d, schritt, f_schritt, CARD_W - 2 * pad - nr_w2)
        d.ellipse((pad, y, pad + mm(3.6), y + mm(3.6)), fill=TK)
        d.text((pad + mm(1.8), y + mm(1.8)), nr_str, font=font(F_SANS_BOLD, 2.1), fill=WHITE, anchor="mm")
        ty2 = y
        for ln in lines:
            d.text((pad + nr_w2, ty2), ln, font=f_schritt, fill=KT_INK)
            ty2 += mm(3.55)
        y = max(ty2, y + mm(4)) + mm(1.1)
    y += mm(1.6)

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

    f_ab_text = font(F_SANS_REG, 2.55)
    for tun, nicht in ab_rows:
        tun_lines = wrap_text(d, tun, f_ab_text, col_w - mm(3.5))
        nicht_lines = wrap_text(d, nicht, f_ab_text, col_w - mm(3.5))
        n_lines = max(len(tun_lines), len(nicht_lines))
        line_h = mm(3.35)
        row_h = n_lines * line_h + mm(2)
        rounded_rect(d, (pad, y, pad + col_w, y + row_h), radius=mm(1), fill=TUN_BG)
        rounded_rect(d, (pad + col_w + col_gap, y, CARD_W - pad, y + row_h), radius=mm(1), fill=NICHT_BG)
        ty3 = y + mm(1)
        for ln in tun_lines:
            d.text((pad + mm(1.8), ty3), ln, font=f_ab_text, fill=(30, 70, 32))
            ty3 += line_h
        ty3 = y + mm(1)
        for ln in nicht_lines:
            d.text((pad + col_w + col_gap + mm(1.8), ty3), ln, font=f_ab_text, fill=(90, 20, 20))
            ty3 += line_h
        y += row_h + mm(1.1)

    y += mm(1.2)
    foot_y = CARD_H - mm(13.5)
    if y > foot_y - mm(1):
        print(f"WARNUNG: Karte {card.get('id_text', card.get('nr'))} läuft in den Footer über "
              f"(Inhalt endet bei {y}px, Footer beginnt bei {foot_y}px)")
    f_quelle = font(F_SANS_REG, 2.15)
    for ln in wrap_text(d, "Quelle: " + card["quelle"], f_quelle, CARD_W - 2 * pad):
        d.text((pad, y), ln, font=f_quelle, fill=KT_MUTED)
        y += mm(2.9)

    d.line((pad, foot_y, CARD_W - pad, foot_y), fill=TK_BORDER, width=mm(0.4))
    logo = logo_mark(5.2)
    img.paste(logo, (pad, foot_y + mm(1.8)), logo)
    f_foot = font(F_SANS_REG, 2.15)
    d.text((pad + logo.width + mm(2), foot_y + mm(2.7)),
           "KLARTEXT-Mentoring · TK-Handlungskarten · © 2026 Anja Jolk", font=f_foot, fill=KT_MUTED)

    img.save(out_path, dpi=(DPI, DPI))
    return img
