#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baut die druckfertige PDF-Version von KLARTEXT_Zauberfaecher_Streifen.html: 45 Streifen
(6 Module) im 1:1-Layout der Druckvorlage (20 cm x 3 cm je Streifen, Vorderseite mit Text +
Rueckseite mit Brainy). Daten werden direkt aus der bestehenden HTML-Datei geparst, damit
Text/Farben garantiert mit der Web-Version uebereinstimmen.

Seite 1..n: alle Vorderseiten (Modul fuer Modul). Seite n+1..: alle Rueckseiten in exakt
derselben Reihenfolge, damit beidseitiger Druck (Papier wenden) aufgeht.
"""
import re, json, html as htmlmod, os, colorsys
from PIL import Image, ImageDraw, ImageFont
Image.init()

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = "/sessions/kind-beautiful-ptolemy/mnt/outputs/zauberfaecher_streifen"
os.makedirs(OUT_DIR, exist_ok=True)

DPI = 300
MM = DPI / 25.4
def mm(v): return int(round(v * MM))

PAGE_W, PAGE_H = mm(210), mm(297)  # A4
MARGIN = mm(8)
STRIP_W, STRIP_H = mm(200), mm(30)  # 20cm x 3cm, wie im Original
GAP = mm(1.5)

WHITE = (255, 255, 255)
INK = (45, 45, 45)
MUTED = (150, 150, 150)

F_SERIF_BOLD = "/usr/share/fonts/truetype/crosextra/Caladea-Bold.ttf"
F_SANS_REG = "/usr/share/fonts/truetype/lato/Lato-Regular.ttf"
F_SANS_BOLD = "/usr/share/fonts/truetype/lato/Lato-Bold.ttf"
F_SANS_BLACK = "/usr/share/fonts/truetype/lato/Lato-Black.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def parse_hue_rotate(filt):
    """CSS 'hue-rotate(Xdeg) saturate(Y)' -> (deg, sat). 'none' -> (0, 1.0)."""
    if not filt or filt == "none":
        return 0.0, 1.0
    m_deg = re.search(r'hue-rotate\((-?\d+(?:\.\d+)?)deg\)', filt)
    m_sat = re.search(r'saturate\((\d+(?:\.\d+)?)\)', filt)
    deg = float(m_deg.group(1)) if m_deg else 0.0
    sat = float(m_sat.group(1)) if m_sat else 1.0
    return deg, sat

def apply_hue_rotate(img_rgb, deg, sat):
    """Naeherung von CSS filter:hue-rotate()+saturate() via HSV-Shift (visuell nah genug fuer
    ein dekoratives Hintergrund-Icon, keine farbkritische Anwendung)."""
    if deg == 0 and sat == 1.0:
        return img_rgb
    img = img_rgb.convert("RGB")
    px = img.load()
    w, h = img.size
    out = Image.new("RGB", (w, h))
    opx = out.load()
    hue_shift = deg / 360.0
    # Downsample-Trick fuer Performance: HSV pro Pixel ist bei 600x600 ok (~360k Pixel)
    for y in range(h):
        for x in range(w):
            r, g, b = px[x, y]
            hh, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
            hh = (hh + hue_shift) % 1.0
            s = min(1.0, s * sat)
            r2, g2, b2 = colorsys.hsv_to_rgb(hh, s, v)
            opx[x, y] = (int(r2*255), int(g2*255), int(b2*255))
    return out

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

# ---------------------------------------------------------------------------
# Daten aus der HTML-Datei parsen
# ---------------------------------------------------------------------------
def parse_streifen_html():
    src = os.path.join(ROOT, "KLARTEXT_Zauberfaecher_Streifen.html")
    html_txt = open(src, encoding="utf-8").read()
    blocks = html_txt.split('<div class="modul-gruppe">')[1:]
    module = []
    for b in blocks:
        farbe = re.search(r'modul-farb" style="background:(#[0-9a-fA-F]+);"', b).group(1)
        name = re.search(r'modul-name" style="color:#[0-9a-fA-F]+;">([^<]+)</span>', b).group(1)
        karten = re.findall(
            r'<div class="streifen">.*?<div class="streifen-name" style="color:#[0-9a-fA-F]+;">([^<]+)</div>\s*'
            r'<div class="streifen-text">(.*?)</div>\s*</div>\s*<div class="streifen-brainy">\s*'
            r'<img src="brainy\.png" style="filter:([^"]*);" alt="Brainy">',
            b, re.S
        )
        karten_clean = [(htmlmod.unescape(t.strip()), htmlmod.unescape(txt.strip()), filt.strip())
                         for t, txt, filt in karten]
        module.append({"farbe": hex_to_rgb(farbe), "name": htmlmod.unescape(name), "karten": karten_clean})
    return module

MODULE = parse_streifen_html()
BRAINY = Image.open(os.path.join(ROOT, "brainy.png")).convert("RGB")

# Brainy-Varianten je (deg, sat) vorab rendern (Performance: nur 1x pro Modul statt pro Karte)
_brainy_cache = {}
def get_brainy(deg, sat):
    key = (deg, sat)
    if key not in _brainy_cache:
        _brainy_cache[key] = apply_hue_rotate(BRAINY, deg, sat)
    return _brainy_cache[key]

# ---------------------------------------------------------------------------
# Einzel-Streifen rendern
# ---------------------------------------------------------------------------
def render_front_strip(name, text, farbe_rgb, brainy_img):
    img = Image.new("RGB", (STRIP_W, STRIP_H), WHITE)
    d = ImageDraw.Draw(img)

    loch_w = mm(12)
    farb_w = mm(3.3)
    brainy_w = mm(30)

    # Loch-Bereich (Modulfarbe)
    d.rectangle((0, 0, loch_w, STRIP_H), fill=farbe_rgb)
    r = mm(3)
    cx, cy = loch_w // 2, STRIP_H // 2
    d.ellipse((cx-r, cy-r, cx+r, cy+r), outline=WHITE, width=mm(0.6))

    # Duenner Farbstreifen
    d.rectangle((loch_w, 0, loch_w + farb_w, STRIP_H), fill=farbe_rgb)

    # Inhalt (weiss)
    content_x0 = loch_w + farb_w + mm(4)
    content_x1 = STRIP_W - brainy_w
    content_w = content_x1 - content_x0

    f_name = font(F_SERIF_BOLD, mm(5.3))
    d.text((content_x0, mm(4.5)), name, font=f_name, fill=farbe_rgb)

    f_text = font(F_SANS_REG, mm(3.6))
    lines = wrap_text(d, text, f_text, content_w)[:3]
    ty = mm(12.5)
    for ln in lines:
        d.text((content_x0, ty), ln, font=f_text, fill=INK)
        ty += mm(4.3)

    # Brainy rechts, leicht transparent wirkend -> auf hellgrauem Grund gemischt
    bsize = mm(24)
    b = brainy_img.resize((bsize, bsize), Image.LANCZOS)
    # leichte Aufhellung simuliert CSS opacity:0.55 auf weissem Grund
    b = Image.blend(Image.new("RGB", b.size, WHITE), b, 0.55)
    bx = STRIP_W - brainy_w + (brainy_w - bsize)//2
    by = (STRIP_H - bsize)//2
    img.paste(b, (bx, by))

    return img

def render_back_strip(module_name, farbe_rgb, brainy_img):
    img = Image.new("RGB", (STRIP_W, STRIP_H), WHITE)
    d = ImageDraw.Draw(img)

    loch_w = mm(12)
    farb_w = mm(2.6)

    d.rectangle((0, 0, loch_w, STRIP_H), fill=WHITE)
    d.line((loch_w, 0, loch_w, STRIP_H), fill=(230, 228, 223), width=mm(0.4))
    r = mm(3)
    cx, cy = loch_w // 2, STRIP_H // 2
    d.ellipse((cx-r, cy-r, cx+r, cy+r), outline=(200, 200, 200), width=mm(0.6))

    d.rectangle((loch_w, 0, loch_w + farb_w, STRIP_H), fill=farbe_rgb)

    bsize = mm(24)
    b = brainy_img.resize((bsize, bsize), Image.LANCZOS)
    b = Image.blend(Image.new("RGB", b.size, WHITE), b, 0.85)

    gap = mm(6)
    total_w = bsize + gap + mm(60)
    start_x = loch_w + farb_w + (STRIP_W - loch_w - farb_w - total_w)//2
    by = (STRIP_H - bsize)//2
    img.paste(b, (start_x, by))

    tx = start_x + bsize + gap
    f_name = font(F_SERIF_BOLD, mm(4.6))
    ty = STRIP_H//2 - mm(4.5)
    d.text((tx, ty), module_name, font=f_name, fill=farbe_rgb)
    f_copy = font(F_SANS_BOLD, mm(2.3))
    d.text((tx, ty + mm(6)), "KLARTEXT-MENTORING", font=f_copy, fill=(200, 200, 200))

    return img

# ---------------------------------------------------------------------------
# Seiten zusammensetzen
# ---------------------------------------------------------------------------
def build_pages(strip_images):
    """strip_images: Liste von PIL-Images (STRIP_W x STRIP_H). Gibt Liste fertiger A4-Seiten
    zurueck, mehrere Streifen pro Seite gestapelt."""
    per_page = (PAGE_H - 2*MARGIN) // (STRIP_H + GAP)
    pages = []
    i = 0
    while i < len(strip_images):
        page = Image.new("RGB", (PAGE_W, PAGE_H), WHITE)
        d = ImageDraw.Draw(page)
        x0 = (PAGE_W - STRIP_W)//2
        y = MARGIN
        for _ in range(per_page):
            if i >= len(strip_images):
                break
            page.paste(strip_images[i], (x0, y))
            d.rectangle((x0, y, x0+STRIP_W, y+STRIP_H), outline=(210,210,210), width=1)
            y += STRIP_H + GAP
            i += 1
        pages.append(page)
    return pages

def main():
    front_strips = []
    back_strips = []
    for mod in MODULE:
        deg0, sat0 = parse_hue_rotate(mod["karten"][0][2]) if mod["karten"] else (0, 1.0)
        brainy_mod = get_brainy(deg0, sat0)
        for name, text, filt in mod["karten"]:
            deg, sat = parse_hue_rotate(filt)
            b = get_brainy(deg, sat)
            front_strips.append(render_front_strip(name, text, mod["farbe"], b))
            back_strips.append(render_back_strip(mod["name"], mod["farbe"], brainy_mod))

    print(f"Streifen gesamt: {len(front_strips)}")

    front_pages = build_pages(front_strips)
    back_pages = build_pages(back_strips)
    all_pages = front_pages + back_pages

    out_path = os.path.join(OUT_DIR, "KLARTEXT_Zauberfaecher_Streifen.pdf")
    all_pages[0].save(out_path, save_all=True, append_images=all_pages[1:],
                       resolution=DPI)
    print(f"PDF gespeichert: {out_path} ({len(all_pages)} Seiten: {len(front_pages)} Vorder- + {len(back_pages)} Rueckseiten)")

if __name__ == "__main__":
    main()
