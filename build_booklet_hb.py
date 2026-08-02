#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Anleitung + Quellenverzeichnis fürs Hochbegabungsdeck (12 Karten). Helfer von
build_booklet_mb.py übernommen."""
from PIL import Image, ImageDraw, ImageFont
Image.init()

DPI = 300
MM = DPI / 25.4
def mm(v): return int(round(v * MM))

HB = (32, 36, 196)
HB_LIGHT = (227, 228, 250)
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
    size = 11.0
    f_titel = ImageFont.truetype(F_SERIF_BOLD, mm(size))
    while d.textlength(titel, font=f_titel) > CONTENT_W and size > 6:
        size -= 0.5
        f_titel = ImageFont.truetype(F_SERIF_BOLD, mm(size))
    lines = wrap(d, titel, f_titel, CONTENT_W)
    kopf_h = mm(24) + len(lines) * mm(size * 1.35)
    d.rectangle((0, 0, W, kopf_h), fill=HB)
    d.text((MARGIN, mm(10)), kicker, font=f_kicker, fill=(225, 226, 250))
    ty = mm(17)
    for ln in lines:
        d.text((MARGIN, ty), ln, font=f_titel, fill=(255, 255, 255))
        ty += mm(size * 1.35)
    return img, d, kopf_h + mm(14)

def footer(d, page_label):
    f = ImageFont.truetype(F_SANS_REG, mm(4))
    d.text((MARGIN, H - mm(14)), "KLARTEXT-Mentoring · Hochbegabung · © 2026 Anja Jolk", font=f, fill=KT_MUTED)
    w = d.textlength(page_label, font=f)
    d.text((W - MARGIN - w, H - mm(14)), page_label, font=f, fill=KT_MUTED)

def draw_h2(d, y, text):
    f = ImageFont.truetype(F_SERIF_BOLD, mm(6.5))
    d.text((MARGIN, y), text, font=f, fill=HB)
    return y + mm(9)

def draw_para(d, y, text, size=4.6, color=KT_INK, font_path=F_SANS_REG):
    f = ImageFont.truetype(font_path, mm(size))
    lh = mm(size * 1.55)
    for ln in wrap(d, text, f, CONTENT_W):
        d.text((MARGIN, y), ln, font=f, fill=color)
        y += lh
    return y

def draw_bullet(d, y, text, size=4.6):
    f = ImageFont.truetype(F_SANS_REG, mm(size))
    d.ellipse((MARGIN, y + mm(1.6), MARGIN + mm(1.6), y + mm(3.2)), fill=HB)
    lh = mm(size * 1.55)
    for ln in wrap(d, text, f, CONTENT_W - mm(7)):
        d.text((MARGIN + mm(6), y), ln, font=f, fill=KT_INK)
        y += lh
    return y + mm(1.5)

def anleitung_seite():
    img, d, y = new_page("GEBRAUCHSANWEISUNG", "Anleitung: Hochbegabungsdeck")

    y = draw_h2(d, y, "Was ist dieses Deck?")
    y = draw_para(d, y, "12 Karten für den Umgang mit Hochbegabung im Schulalltag – für "
                        "Schulbegleitung und Team. Deckt drei Bereiche ab: Merkmale und Modelle "
                        "erkennen, typische Herausforderungen einordnen (Underachievement, "
                        "Perfektionismus, soziale Schwierigkeiten, Doppelbegabung, Unterforderung) "
                        "und konkret handeln (Förderwege, Diagnostik, Zusammenarbeit mit Lehrkraft "
                        "und Eltern). Neu entwickelter Inhalt, gestützt auf anerkannte "
                        "Begabungsmodelle und aktuelle Forschung – keine bestehende App-Modulseite "
                        "als Quelle, da Hochbegabung bisher keine dedizierte Grundlage im System hatte.")
    y += mm(5)

    y = draw_h2(d, y, "Die 12 Karten")
    y = draw_para(d, y, "ERKENNEN", size=4.0, color=HB, font_path=F_SANS_BOLD)
    y = draw_bullet(d, y, "HB-01 · Was ist Hochbegabung? – Modelle und Grundbegriffe.")
    y = draw_bullet(d, y, "HB-02 · Merkmale erkennen – typische Anzeichen im Schulalltag.")
    y = draw_bullet(d, y, "HB-03 · Asynchrone Entwicklung – kognitiv voraus, emotional altersgemäß.")
    y += mm(2)
    y = draw_para(d, y, "HERAUSFORDERUNGEN", size=4.0, color=HB, font_path=F_SANS_BOLD)
    y = draw_bullet(d, y, "HB-04 · Underachievement – wenn Potenzial nicht sichtbar wird.")
    y = draw_bullet(d, y, "HB-05 · Perfektionismus & Versagensangst – hoher Anspruch als Blockade.")
    y = draw_bullet(d, y, "HB-06 · Soziale Herausforderungen – Anschluss an Gleichaltrige finden.")
    y = draw_bullet(d, y, "HB-07 · Doppelbegabung / Twice-Exceptional – wenn sich zwei Besonderheiten überdecken.")
    y = draw_bullet(d, y, "HB-08 · Langeweile & Verweigerung – Unterforderung sieht aus wie Verhaltensproblem.")
    y += mm(2)
    y = draw_para(d, y, "HANDELN", size=4.0, color=HB, font_path=F_SANS_BOLD)
    y = draw_bullet(d, y, "HB-09 · Enrichment & Akzeleration – zwei bewährte Förderwege.")
    y = draw_bullet(d, y, "HB-10 · Diagnostik: wann testen? – Einordnung, nicht Durchführung.")
    y = draw_bullet(d, y, "HB-11 · Zusammenarbeit mit der Lehrkraft – gemeinsam abstimmen.")
    y = draw_bullet(d, y, "HB-12 · Elterngespräch bei Hochbegabung – sensibel und ressourcenorientiert.")

    footer(d, "Anleitung")
    return img

def herkunft_seite():
    img, d, y = new_page("QUELLEN & HERKUNFT", "Herkunft der Inhalte & Quellenverzeichnis")

    y = draw_h2(d, y, "Herkunft der Inhalte")
    y = draw_para(d, y, "Anders als bei den meisten anderen KLARTEXT-Decks gab es für Hochbegabung "
                        "noch keine geprüfte App-Modulseite als Ausgangsbasis. Die 12 Karten wurden "
                        "daher neu entwickelt und direkt auf anerkannte, wissenschaftlich etablierte "
                        "Begabungsmodelle sowie aktuelle Forschung zu Underachievement, "
                        "Perfektionismus und Twice-Exceptional gestützt (vollständige Angaben unten). "
                        "Statistische Angaben (z. B. zur Häufigkeit von Underachievement) werden als "
                        "Spannen wiedergegeben, da sich Studien in Definition und Methodik "
                        "unterscheiden.")
    y += mm(6)

    y = draw_h2(d, y, "Quellenverzeichnis")
    quellen = [
        "Renzulli, J. S. (1978). What Makes Giftedness? Reexamining a Definition. Phi Delta "
        "Kappan, 60(3), 180–184.",
        "Mönks, F. J. (1990). Hochbegabung: Ein Handbuch für Studium und Praxis. Hogrefe "
        "(Triadisches Interdependenzmodell).",
        "Heller, K. A. (Hrsg.) (2000). Begabungsdiagnostik in der Schul- und Erziehungsberatung. "
        "Hans Huber (Münchner (Hoch-)Begabungsmodell, mit Perleth & Hany).",
        "Gagné, F. (2008). Building Gifts into Talents: Overview of the DMGT. Referenzmodell zur "
        "Unterscheidung von Begabung und Talent.",
        "Rost, D. H. Underachievement aus psychologischer und pädagogischer Sicht. "
        "Forschungsüberblick, Universität Würzburg.",
        "Karg-Stiftung. Einschätzung der Underachievement-Quote bei Hochbegabten (ca. 15–25%).",
        "Aktuelle Forschung zu Twice-Exceptional (2e) / Doppelbegabung, u. a. im Zusammenspiel "
        "von Hochbegabung mit ADHS, Autismus oder LRS – Übersicht in deutschsprachiger "
        "Fachliteratur seit den 2010er-Jahren, systematische Forschung in den USA seit den 1990ern.",
    ]
    for q in quellen:
        y = draw_bullet(d, y, q, size=4.3)

    footer(d, "Quellen")
    return img

if __name__ == "__main__":
    img1 = anleitung_seite()
    img1.save("/sessions/kind-beautiful-ptolemy/mnt/outputs/booklet_hb_anleitung.png")
    img2 = herkunft_seite()
    img2.save("/sessions/kind-beautiful-ptolemy/mnt/outputs/booklet_hb_quellen.png")
    print("hb_anleitung + hb_quellen ok")
