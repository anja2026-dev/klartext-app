#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Anleitung fürs Geschichtenkarten-Deck. Struktur/Helfer von build_booklet_werkzeug.py übernommen."""
from PIL import Image, ImageDraw, ImageFont
Image.init()

DPI = 300
MM = DPI / 25.4
def mm(v): return int(round(v * MM))

NAVY = (27, 58, 75)
SET_A = (150, 30, 35)
SET_B = (21, 101, 192)
SET_C = (46, 110, 60)
KT_INK = (45, 45, 45)
KT_MUTED = (122, 112, 96)

F_SERIF_BOLD = "/usr/share/fonts/truetype/crosextra/Caladea-Bold.ttf"
F_SANS_REG = "/usr/share/fonts/truetype/lato/Lato-Regular.ttf"
F_SANS_BOLD = "/usr/share/fonts/truetype/lato/Lato-Bold.ttf"

W, H = mm(210), mm(297)
MARGIN = mm(20)
CONTENT_W = W - 2 * MARGIN

def wrap(draw, text, font, max_width):
    words = text.split()
    lines, cur = [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if draw.textlength(t, font=font) <= max_width:
            cur = t
        else:
            if cur: lines.append(cur)
            cur = w_
    if cur: lines.append(cur)
    return lines

def new_page(kicker, titel):
    img = Image.new("RGB", (W, H), (255, 255, 255))
    d = ImageDraw.Draw(img)
    f_kicker = ImageFont.truetype(F_SANS_BOLD, mm(4.5))
    size = 11.0
    f_titel = ImageFont.truetype(F_SERIF_BOLD, mm(size))
    while d.textlength(titel, font=f_titel) > CONTENT_W and size > 6:
        size -= 0.5
        f_titel = ImageFont.truetype(F_SERIF_BOLD, mm(size))
    lines = wrap(d, titel, f_titel, CONTENT_W)
    kopf_h = mm(24) + len(lines) * mm(size * 1.35)
    d.rectangle((0, 0, W, kopf_h), fill=NAVY)
    d.text((MARGIN, mm(10)), kicker, font=f_kicker, fill=(210, 225, 220))
    ty = mm(17)
    for ln in lines:
        d.text((MARGIN, ty), ln, font=f_titel, fill=(255, 255, 255))
        ty += mm(size * 1.35)
    return img, d, kopf_h + mm(14)

def footer(d, page_label):
    f = ImageFont.truetype(F_SANS_REG, mm(4))
    d.text((MARGIN, H - mm(14)), "KLARTEXT-Mentoring · Geschichtenkarten · © 2026 Anja Jolk", font=f, fill=KT_MUTED)
    w = d.textlength(page_label, font=f)
    d.text((W - MARGIN - w, H - mm(14)), page_label, font=f, fill=KT_MUTED)

def draw_h2(d, y, text, color=NAVY):
    f = ImageFont.truetype(F_SERIF_BOLD, mm(6.5))
    d.text((MARGIN, y), text, font=f, fill=color)
    return y + mm(9)

def draw_para(d, y, text, size=4.6, color=KT_INK, font_path=F_SANS_REG):
    f = ImageFont.truetype(font_path, mm(size))
    lh = mm(size * 1.55)
    for ln in wrap(d, text, f, CONTENT_W):
        d.text((MARGIN, y), ln, font=f, fill=color)
        y += lh
    return y

def draw_bullet(d, y, text, color, size=4.6):
    f = ImageFont.truetype(F_SANS_REG, mm(size))
    d.ellipse((MARGIN, y + mm(1.6), MARGIN + mm(1.6), y + mm(3.2)), fill=color)
    lh = mm(size * 1.55)
    for ln in wrap(d, text, f, CONTENT_W - mm(7)):
        d.text((MARGIN + mm(6), y), ln, font=f, fill=KT_INK)
        y += lh
    return y + mm(1.5)

def anleitung_seite1():
    img, d, y = new_page("GEBRAUCHSANWEISUNG", "Anleitung: Geschichtenkarten-Deck")

    y = draw_h2(d, y, "Was ist das Geschichtenkarten-Deck?")
    y = draw_para(d, y, "30 Karten mit kurzen Geschichten rund um Brainy – zum gemeinsamen Anschauen "
                        "und Besprechen mit dem Kind. Direkt aus der bestehenden App-Galerie "
                        "übernommen, jetzt zusätzlich physisch griffbereit. Vierter Baustein der "
                        "Handlungskarten-Serie, aber anders als TK/Krisendeck/Werkzeugkarten nicht "
                        "für INGRA selbst, sondern zum gemeinsamen Betrachten mit dem Kind gedacht.")
    y += mm(6)

    y = draw_h2(d, y, "Drei Sets")
    y = draw_bullet(d, y, "Set A · Brainy erlebt Mobbing (A1–A10) – Opferperspektive, hilft dem Kind, "
                          "eigene Erfahrungen wiederzuerkennen und Gefühle zu benennen.", SET_A)
    y = draw_bullet(d, y, "Set B · Brainy hilft anderen (B1–B10) – Verteidiger-Perspektive, zeigt "
                          "konkrete, mutige Handlungsmöglichkeiten.", SET_B)
    y = draw_bullet(d, y, "Set C · Brainy lernt Strategien (C1–C10) – Übungskarten für konkrete "
                          "Techniken wie Ich-Botschaften, Grenzen setzen, Hilfe holen.", SET_C)
    y += mm(4)

    y = draw_h2(d, y, "So wird eine Karte genutzt")
    y = draw_para(d, y, "Karte gemeinsam anschauen, Situation vorlesen, die 3 Fragen zum Gespräch "
                        "als Einstieg nutzen. Der Impuls zeigt eine mögliche Reaktion – kein Muss, "
                        "sondern ein Gesprächsanstoß. Kein festes Set vorgeschrieben: je nach "
                        "Situation des Kindes mit A, B oder C beginnen.")

    footer(d, "Anleitung · 1/2")
    return img

def anleitung_seite2():
    img, d, y = new_page("GEBRAUCHSANWEISUNG", "Bonuskarte & Herkunft")

    y = draw_h2(d, y, "Bonuskarte: Stoppschild")
    y = draw_para(d, y, "Zusätzlich zu den 30 Geschichtenkarten liegt eine Stoppschild-Bonuskarte "
                        "bei (aus dem Anti-Mobbing-Training der App, dort schon im Mini-Kartenformat "
                        "angelegt) – passend zu Set A, gleiche Rot-Familie. Kann als 31. Karte im "
                        "Deck oder separat als Erinnerungskarte genutzt werden.")
    y += mm(6)

    y = draw_h2(d, y, "Herkunft der Inhalte")
    y = draw_para(d, y, "Text unverändert aus der bestehenden, geprüften App-Galerie übernommen "
                        "(M6_Geschichtenkarten_Galerie.html) – keine neuen Geschichten erfunden. "
                        "Die Illustrationen sind neu gemalt, im selben Aquarell-Kinderbuch-Stil wie "
                        "die übrigen Bilderdecks (KD/EL/LK/JD), mit derselben Brainy-Figur.")
    y += mm(6)

    y = draw_h2(d, y, "Kein Ersatz für die App")
    y = draw_para(d, y, "Die App-Module M6-01 bis M6-15 bleiben die ausführliche fachliche "
                        "Grundlage für INGRA. Dieses Deck ist ein ergänzendes Gesprächswerkzeug "
                        "für den Moment mit dem Kind, kein Lehrmaterial für Erwachsene.")

    footer(d, "Anleitung · 2/2")
    return img

if __name__ == "__main__":
    pages = {
        "geschichtenkarten_anleitung1": anleitung_seite1(),
        "geschichtenkarten_anleitung2": anleitung_seite2(),
    }
    for name, img in pages.items():
        img.save(f"/sessions/kind-beautiful-ptolemy/mnt/outputs/booklet_{name}.png")
        print(name, "ok")
