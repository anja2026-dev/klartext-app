#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Anleitung + Quellen fürs SP-Deck (Springer-INGRAs) – kompakte 3-Seiten-Variante."""
from PIL import Image, ImageDraw, ImageFont
Image.init()

DPI = 300
MM = DPI / 25.4
def mm(v): return int(round(v * MM))

SP = (90, 74, 66)          # #5A4A42
SP_BORDER = (211, 196, 187)
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
    f_titel = ImageFont.truetype(F_SERIF_BOLD, mm(11))
    kopf_h = mm(38)
    d.rectangle((0, 0, W, kopf_h), fill=SP)
    d.text((MARGIN, mm(10)), kicker, font=f_kicker, fill=(220, 212, 206))
    d.text((MARGIN, mm(17)), titel, font=f_titel, fill=(255, 255, 255))
    return img, d, kopf_h + mm(14)

def footer(d, page_label):
    f = ImageFont.truetype(F_SANS_REG, mm(4))
    d.text((MARGIN, H - mm(14)), "KLARTEXT-Mentoring · SP-Deck · © 2026 Anja Jolk", font=f, fill=KT_MUTED)
    w = d.textlength(page_label, font=f)
    d.text((W - MARGIN - w, H - mm(14)), page_label, font=f, fill=KT_MUTED)

def draw_h2(d, y, text):
    f = ImageFont.truetype(F_SERIF_BOLD, mm(6.5))
    d.text((MARGIN, y), text, font=f, fill=SP)
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
    d.ellipse((MARGIN, y, MARGIN + mm(9), y + mm(9)), fill=SP)
    d.text((MARGIN + mm(4.5), y + mm(4.5)), str(num), font=f_num, anchor="mm", fill=(255, 255, 255))
    f_titel = ImageFont.truetype(F_SANS_BOLD, mm(5.2))
    d.text((MARGIN + mm(13), y + mm(0.5)), titel, font=f_titel, fill=SP)
    f_text = ImageFont.truetype(F_SANS_REG, mm(size))
    ty = y + mm(7)
    lh = mm(size * 1.55)
    for ln in wrap(d, text, f_text, CONTENT_W - mm(13)):
        d.text((MARGIN + mm(13), ty), ln, font=f_text, fill=KT_INK)
        ty += lh
    return max(ty, y + mm(11)) + mm(4)

def anleitung_seite1():
    img, d, y = new_page("GEBRAUCHSANWEISUNG", "Anleitung: So funktioniert das SP-Deck")
    y = draw_h2(d, y, "Was ist das SP-Deck?")
    y = draw_para(d, y, "7 Karten für Springer-INGRAs – Fachkräfte, die kurzfristig und wechselnd in "
                        "fremden Klassen/Systemen eingesetzt werden, ohne die übliche lange "
                        "Beziehungsaufbauzeit einer Stammkraft. Kernhaltung: Plug-and-Play-"
                        "Handlungssicherheit statt langem Beziehungsaufbau.")
    y += mm(6)
    y = draw_h2(d, y, "Für wen ist es gedacht?")
    y = draw_para(d, y, "Für INGRA-Fachkräfte im Springer-Einsatz – zur schnellen Orientierung vor, "
                        "während und nach einem Einsatz in einer neuen Klasse.")
    y += mm(8)
    y = draw_h2(d, y, "In drei Schritten")
    y += mm(2)
    y = draw_numbered(d, y, 1, "Karte auswählen",
        "Passend zur Phase des Einsatzes – vom Blitz-Check am Anfang (SP-01) bis zum Selbstschutz "
        "danach (SP-07).")
    y = draw_numbered(d, y, 2, "Anleitung und Fragen lesen",
        "Die Anleitung ordnet die typische Springer-Situation ein, die zwei Fragen öffnen die eigene "
        "Reflexion vor Ort.")
    y = draw_numbered(d, y, 3, "Hinweis-Box nutzen",
        "Ein kurzer, sofort anwendbarer Gedanke – für den Moment, in dem keine Zeit für lange "
        "Vorbereitung bleibt.")
    footer(d, "Anleitung")
    return img

def quellen_seite1():
    img, d, y = new_page("METHODISCHE GRUNDLAGE", "Quellen")
    y = draw_para(d, y, "Das SP-Deck ist ein originäres KLARTEXT-Praxiskonzept – es gibt keine "
                        "etablierte Forschungsliteratur speziell zur „Springer-INGRA“-Rolle. Statt eine "
                        "unpassende Quelle künstlich heranzuziehen, ist das hier offen benannt: 5 von 7 "
                        "Karten haben bewusst keine akademische Einzelquelle.",
                  size=4.4, color=GOLD)
    y += mm(8)
    y = draw_h2(d, y, "Wo es eine passende Quelle gibt")
    y = draw_para(d, y, "SP-06 (Eltern-Erwartungen): Christenson, S. L. & Sheridan, S. M. (2001). "
                        "Schools and Families: Creating Essential Connections for Learning. Guilford "
                        "Press. — Grundprinzip transparenter Kommunikation, sinngemäß auf die "
                        "Springer-Situation übertragen.")
    y += mm(6)
    y = draw_para(d, y, "SP-03 (Chance des Neuanfangs) ist inhaltlich verwandt mit de Shazers "
                        "Ausnahme-Fokus (1988), aber nicht erzwungen zitiert, da keine Karte über die "
                        "Springer-Rolle selbst in der Literatur existiert.", size=4.4, color=KT_MUTED)
    footer(d, "Quellen")
    return img

if __name__ == "__main__":
    pages = {
        "sp_anleitung1": anleitung_seite1(),
        "sp_quellen1": quellen_seite1(),
    }
    for name, img in pages.items():
        img.save(f"/sessions/kind-beautiful-ptolemy/mnt/outputs/booklet_{name}.png")
        print(name, "ok")
