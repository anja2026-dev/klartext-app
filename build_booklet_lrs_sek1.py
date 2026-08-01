#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Anleitung + Quellen fürs LRS/Dyskalkulie-Sek1-Deck – kompakte 3-Seiten-Variante."""
from PIL import Image, ImageDraw, ImageFont
Image.init()

DPI = 300
MM = DPI / 25.4
def mm(v): return int(round(v * MM))

LRS = (191, 147, 105)          # #BF9369
LRS_BORDER = (224, 203, 168)
KT_INK = (45, 45, 45)
KT_MUTED = (122, 112, 96)
GOLD = (150, 120, 50)

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
    f_titel = ImageFont.truetype(F_SERIF_BOLD, mm(10.5))
    kopf_h = mm(38)
    d.rectangle((0, 0, W, kopf_h), fill=LRS)
    d.text((MARGIN, mm(10)), kicker, font=f_kicker, fill=(70, 55, 35))
    d.text((MARGIN, mm(17)), titel, font=f_titel, fill=(50, 35, 20))
    return img, d, kopf_h + mm(14)

def footer(d, page_label):
    f = ImageFont.truetype(F_SANS_REG, mm(4))
    d.text((MARGIN, H - mm(14)), "KLARTEXT-Mentoring · LRS/Dyskalkulie-Deck · © 2026 Anja Jolk", font=f, fill=KT_MUTED)
    w = d.textlength(page_label, font=f)
    d.text((W - MARGIN - w, H - mm(14)), page_label, font=f, fill=KT_MUTED)

def draw_h2(d, y, text):
    f = ImageFont.truetype(F_SERIF_BOLD, mm(6.5))
    d.text((MARGIN, y), text, font=f, fill=(140, 100, 60))
    return y + mm(9)

def draw_para(d, y, text, size=4.6, color=KT_INK, font_path=F_SANS_REG):
    f = ImageFont.truetype(font_path, mm(size))
    lh = mm(size * 1.55)
    for ln in wrap(d, text, f, CONTENT_W):
        d.text((MARGIN, y), ln, font=f, fill=color)
        y += lh
    return y

def draw_numbered(d, y, num, titel, text, size=4.8):
    f_num = ImageFont.truetype(F_SERIF_BOLD, mm(7))
    d.ellipse((MARGIN, y, MARGIN + mm(9), y + mm(9)), fill=(140, 100, 60))
    d.text((MARGIN + mm(4.5), y + mm(4.5)), str(num), font=f_num, anchor="mm", fill=(255, 255, 255))
    f_titel = ImageFont.truetype(F_SANS_BOLD, mm(5.2))
    d.text((MARGIN + mm(13), y + mm(0.5)), titel, font=f_titel, fill=(140, 100, 60))
    f_text = ImageFont.truetype(F_SANS_REG, mm(size))
    ty = y + mm(7)
    lh = mm(size * 1.55)
    for ln in wrap(d, text, f_text, CONTENT_W - mm(13)):
        d.text((MARGIN + mm(13), ty), ln, font=f_text, fill=KT_INK)
        ty += lh
    return max(ty, y + mm(11)) + mm(4)

def anleitung_seite1():
    img, d, y = new_page("GEBRAUCHSANWEISUNG", "Anleitung: LRS/Dyskalkulie-Deck Sek I")
    y = draw_h2(d, y, "Was ist dieses Deck?")
    y = draw_para(d, y, "10 Karten für Jugendliche mit LRS (L-01–07) und Dyskalkulie (D-01–03) in der "
                        "weiterführenden Schule. Kernhaltung: Entlastung von Scham, Trennung von Fehler "
                        "und Werturteil. Jede Karte trägt zusätzlich im Hinweis-Feld eine "
                        "fächerübergreifende Lehrkraft-Strategie – die Karte ist also gleichzeitig "
                        "Impuls für den/die Jugendliche/n und Mini-Handreichung für die mitlesende "
                        "Lehrkraft.")
    y += mm(6)
    y = draw_h2(d, y, "Für wen ist es gedacht?")
    y = draw_para(d, y, "Für Jugendliche selbst (Karte vorlesen oder gemeinsam lesen) sowie für "
                        "Lehrkräfte, die die Lehrkraft-Strategie im Hinweis-Feld direkt im Fachunterricht "
                        "umsetzen wollen – unabhängig vom Fach (außer Deutsch für die Rechtschreib-Regel).")
    y += mm(8)
    y = draw_h2(d, y, "In drei Schritten")
    y += mm(2)
    y = draw_numbered(d, y, 1, "Karte auswählen",
        "Passend zur aktuellen Situation – Scham beim Schreiben, Fremdsprachenfrust, Zukunftsängste "
        "oder eine konkrete Rechenherausforderung.")
    y = draw_numbered(d, y, 2, "Anleitung und Fragen lesen",
        "Die Anleitung ordnet die Situation ein, die zwei Fragen öffnen das Gespräch mit dem/der "
        "Jugendlichen.")
    y = draw_numbered(d, y, 3, "Lehrkraft-Strategie umsetzen",
        "Der zweite Teil der Hinweis-Box gibt eine konkrete didaktische Anpassung für den Fachunterricht "
        "vor, oft mit Verweis auf ein passendes M3-Werkzeug.")
    footer(d, "Anleitung")
    return img

QUELLEN_VORGESCHLAGEN = [
    "Schulte-Körne, G. & Galuschka, K. Lese-Rechtschreibstörung (LRS). Hogrefe. — Grundlage L-01, 03, "
    "04, 06, 07.",
    "Bundesverband Legasthenie und Dyskalkulie e.V. (BVL) – Nachteilsausgleich, rechtliche Grundlage "
    "nach KMK-Beschlüssen der Länder. — Grundlage L-02, 05.",
    "von Aster, M. & Shalev, R. S. (2007). Number development and developmental dyscalculia. "
    "Developmental Medicine & Child Neurology, 49(11), 868–873. — Grundlage D-01, 02, 03.",
]

def quellen_seite1():
    img, d, y = new_page("METHODISCHE GRUNDLAGE", "Quellen")
    y = draw_para(d, y, "Alle drei Quellen sind neu für dieses Deck recherchiert und noch nicht im "
                        "KLARTEXT-Quellenregister bestätigt – hier als „vorgeschlagen, bitte fachlich "
                        "gegenprüfen“ markiert (wie bei EL/LK üblich).",
                  size=4.2, color=GOLD)
    y += mm(4)
    f_q = ImageFont.truetype(F_SANS_REG, mm(4.6))
    for q in QUELLEN_VORGESCHLAGEN:
        for ln in wrap(d, q, f_q, CONTENT_W - mm(6)):
            d.text((MARGIN + mm(6), y), ln, font=f_q, fill=KT_INK)
            y += mm(7.2)
        y += mm(2)
    footer(d, "Quellen · 1/2")
    return img

def quellen_seite2():
    img, d, y = new_page("METHODISCHE GRUNDLAGE", "Lehrkraft-Strategien im Überblick")
    y = draw_para(d, y, "Die vier fächerübergreifenden Strategien, die sich durch die L-Karten ziehen:",
                  size=4.6, color=KT_MUTED)
    y += mm(6)
    for titel, text in [
        ("Mündlich vor Schriftlich", "Wissen zählt, nicht die Rechtschreibung – in allen Fächern außer Deutsch."),
        ("Struktur-Hilfen", "Verweis auf M3-15 (Schritt-Plan) für komplexe Schreib-/Rechenaufgaben."),
        ("Multisensorik", "Visualisierung (M3-17) und Audio-Medien statt reinem Lesen/Schreiben."),
        ("Zeit-Management", "Sichtbare Zeit (M3-21) zur Druckreduktion statt reiner Zeitzuteilung."),
    ]:
        f_t = ImageFont.truetype(F_SANS_BOLD, mm(5))
        d.text((MARGIN, y), titel, font=f_t, fill=(140, 100, 60))
        y += mm(6.5)
        y = draw_para(d, y, text, size=4.4)
        y += mm(4)
    footer(d, "Quellen · 2/2")
    return img

if __name__ == "__main__":
    pages = {
        "lrs-sek1_anleitung1": anleitung_seite1(),
        "lrs-sek1_quellen1": quellen_seite1(),
        "lrs-sek1_quellen2": quellen_seite2(),
    }
    for name, img in pages.items():
        img.save(f"/sessions/kind-beautiful-ptolemy/mnt/outputs/booklet_{name}.png")
        print(name, "ok")
