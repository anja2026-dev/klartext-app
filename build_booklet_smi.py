#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Anleitung + Quellen fürs SMI-Deck – adaptiert von build_booklet_tr.py, kompakte 3-Seiten-Variante
(wie Werkzeugkarten/Krisendeck), da 10 statt 33 Karten kein eigenes Glossar rechtfertigen."""
from PIL import Image, ImageDraw, ImageFont
Image.init()

DPI = 300
MM = DPI / 25.4
def mm(v): return int(round(v * MM))

SMI = (89, 45, 89)          # #592D59
SMI_LIGHT = (238, 227, 238)
SMI_BORDER = (211, 184, 211)
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
    d.rectangle((0, 0, W, kopf_h), fill=SMI)
    d.text((MARGIN, mm(10)), kicker, font=f_kicker, fill=(230, 220, 230))
    d.text((MARGIN, mm(17)), titel, font=f_titel, fill=(255, 255, 255))
    return img, d, kopf_h + mm(14)

def footer(d, page_label):
    f = ImageFont.truetype(F_SANS_REG, mm(4))
    d.text((MARGIN, H - mm(14)), "KLARTEXT-Mentoring · SMI-Deck · © 2026 Anja Jolk", font=f, fill=KT_MUTED)
    w = d.textlength(page_label, font=f)
    d.text((W - MARGIN - w, H - mm(14)), page_label, font=f, fill=KT_MUTED)

def draw_h2(d, y, text):
    f = ImageFont.truetype(F_SERIF_BOLD, mm(6.5))
    d.text((MARGIN, y), text, font=f, fill=SMI)
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
    d.ellipse((MARGIN, y, MARGIN + mm(9), y + mm(9)), fill=SMI)
    d.text((MARGIN + mm(4.5), y + mm(4.5)), str(num), font=f_num, anchor="mm", fill=(255, 255, 255))
    f_titel = ImageFont.truetype(F_SANS_BOLD, mm(5.2))
    d.text((MARGIN + mm(13), y + mm(0.5)), titel, font=f_titel, fill=SMI)
    f_text = ImageFont.truetype(F_SANS_REG, mm(size))
    ty = y + mm(7)
    lh = mm(size * 1.55)
    for ln in wrap(d, text, f_text, CONTENT_W - mm(13)):
        d.text((MARGIN + mm(13), ty), ln, font=f_text, fill=KT_INK)
        ty += lh
    return max(ty, y + mm(11)) + mm(4)

def anleitung_seite1():
    img, d, y = new_page("GEBRAUCHSANWEISUNG", "Anleitung: So funktioniert das SMI-Deck")
    y = draw_h2(d, y, "Was ist das SMI-Deck?")
    y = draw_para(d, y, "SMI steht für Systemische Mobbing-Intervention: 10 Reflexionskarten für INGRA und "
                        "Lehrkräfte in der Sek I. Die Grundhaltung: Mobbing ist ein Systemsymptom, nicht "
                        "das Fehlverhalten einer einzelnen Person – die Karten helfen, die ganze Gruppendynamik "
                        "in den Blick zu nehmen, statt nur Täter:in und Opfer zu sehen.")
    y += mm(6)
    y = draw_h2(d, y, "Für wen ist es gedacht?")
    y = draw_para(d, y, "Für INGRA-Fachkräfte und Lehrkräfte, die einen akuten oder schwelenden Mobbingfall "
                        "in einer Sek-I-Klasse begleiten – zur eigenen Reflexion vor oder während der "
                        "Intervention, nicht als Material für die betroffenen Kinder selbst.")
    y += mm(8)
    y = draw_h2(d, y, "In drei Schritten")
    y += mm(2)
    y = draw_numbered(d, y, 1, "Karte auswählen",
        "Passend zur aktuellen Phase der Intervention – von der ersten Einschätzung der Gruppendynamik "
        "(SMI-01/02) bis zur Nachhaltigkeitssicherung (SMI-10).")
    y = draw_numbered(d, y, 2, "Anleitung und Fragen lesen",
        "Die Anleitung ordnet die Situation ein, die zwei Impulsfragen öffnen die eigene Reflexion.")
    y = draw_numbered(d, y, 3, "Hinweis-Box nutzen",
        "Ein kurzer, direkt anwendbarer Gedanke auf jeder Rückseite.")
    footer(d, "Anleitung")
    return img

QUELLEN_BESTAETIGT = [
    "Bandura, A. (1977). Self-efficacy: Toward a unifying theory of behavioral change. Psychological "
    "Review, 84(2), 191–215. — bereits im EL-Deck-Quellenregister bestätigt, hier für SMI-10 "
    "wiederverwendet.",
]

QUELLEN_VORGESCHLAGEN = [
    "Salmivalli, C., Lagerspetz, K., Björkqvist, K., Österman, K. & Kaukiainen, A. (1996). Bullying as "
    "a group process: Participant roles and their relations to social status within the group. "
    "Aggressive Behavior, 22, 1–15. — Grundlage SMI-01, 02, 08.",
    "de Shazer, S. (1988). Clues: Investigating Solutions in Brief Therapy. W. W. Norton. — Grundlage "
    "SMI-03, 05 (wie bei EL/LK: vorgeschlagen, bitte gegenprüfen).",
    "Olweus, D., Limber, S. & Mihalic, S. F. (1999). Blueprints for Violence Prevention, Book Nine: "
    "Bullying Prevention Program. Center for the Study and Prevention of Violence. — Grundlage SMI-06.",
    "Christenson, S. L. & Sheridan, S. M. (2001). Schools and Families: Creating Essential Connections "
    "for Learning. Guilford Press. — Grundlage SMI-07.",
    "Watzlawick, P., Weakland, J. H. & Fisch, R. (1974). Change: Principles of Problem Formation and "
    "Problem Resolution. W. W. Norton. — Grundlage SMI-09.",
]

def quellen_seite1():
    img, d, y = new_page("METHODISCHE GRUNDLAGE", "Quellen · Bestätigt")
    y = draw_para(d, y, "Diese Quelle ist bereits im KLARTEXT-Quellenregister bestätigt.",
                  size=4.6, color=KT_MUTED)
    y += mm(9)
    f_q = ImageFont.truetype(F_SANS_REG, mm(4.6))
    for q in QUELLEN_BESTAETIGT:
        for ln in wrap(d, q, f_q, CONTENT_W - mm(6)):
            d.text((MARGIN + mm(6), y), ln, font=f_q, fill=KT_INK)
            y += mm(7.2)
        y += mm(2)
    footer(d, "Quellen · 1/2")
    return img

def quellen_seite2():
    img, d, y = new_page("METHODISCHE GRUNDLAGE", "Quellen · Vorgeschlagen")
    y = draw_para(d, y, "Neu recherchiert für das SMI-Deck, hier als „vorgeschlagen, bitte fachlich "
                        "gegenprüfen“ markiert, da noch nicht im Quellenregister selbst bestätigt. "
                        "Hinweis: Der ursprüngliche Entwurfs-Prompt zitierte SMI-07 fälschlich mit "
                        "Gottman (dessen Forschung betrifft Paar-/Eltern-Kind-Beziehungen) – korrigiert "
                        "zu Christenson & Sheridan, der tatsächlich einschlägigen Quelle zu "
                        "Family-School-Partnerships.",
                  size=4.2, color=GOLD)
    y += mm(3)
    f_q = ImageFont.truetype(F_SANS_REG, mm(4.6))
    for q in QUELLEN_VORGESCHLAGEN:
        for ln in wrap(d, q, f_q, CONTENT_W - mm(6)):
            d.text((MARGIN + mm(6), y), ln, font=f_q, fill=KT_INK)
            y += mm(7.2)
        y += mm(2)
    footer(d, "Quellen · 2/2")
    return img

if __name__ == "__main__":
    pages = {
        "smi_anleitung1": anleitung_seite1(),
        "smi_quellen1": quellen_seite1(),
        "smi_quellen2": quellen_seite2(),
    }
    for name, img in pages.items():
        img.save(f"/sessions/kind-beautiful-ptolemy/mnt/outputs/booklet_{name}.png")
        print(name, "ok")
