#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Anleitung & Quellen fürs Werkzeugkarten-Deck (M3-01–20 als physisches Deck). Drittes Deck im
Handlungskarten-Format, nach TK & Krisendeck. Struktur/Helfer von build_booklet_krisendeck.py übernommen."""
from PIL import Image, ImageDraw, ImageFont
Image.init()

DPI = 300
MM = DPI / 25.4
def mm(v): return int(round(v * MM))

M3 = (176, 125, 42)         # #B07D2A
M3_LIGHT = (251, 244, 232)
M3_BORDER = (224, 200, 138)
KT_INK = (45, 45, 45)
KT_MUTED = (122, 112, 96)
GOLD = (150, 120, 50)

F_SERIF_BOLD = "/usr/share/fonts/truetype/crosextra/Caladea-Bold.ttf"
F_SERIF_IT = "/usr/share/fonts/truetype/crosextra/Caladea-Italic.ttf"
F_SANS_REG = "/usr/share/fonts/truetype/lato/Lato-Regular.ttf"
F_SANS_MED = "/usr/share/fonts/truetype/lato/Lato-Medium.ttf"
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
    d.rectangle((0, 0, W, kopf_h), fill=M3)
    d.text((MARGIN, mm(10)), kicker, font=f_kicker, fill=(255, 240, 215))
    ty = mm(17)
    for ln in lines:
        d.text((MARGIN, ty), ln, font=f_titel, fill=(255, 255, 255))
        ty += mm(size * 1.35)
    return img, d, kopf_h + mm(14)

def footer(d, page_label):
    f = ImageFont.truetype(F_SANS_REG, mm(4))
    d.text((MARGIN, H - mm(14)), "KLARTEXT-Mentoring · Werkzeugkarten · © 2026 Anja Jolk", font=f, fill=KT_MUTED)
    w = d.textlength(page_label, font=f)
    d.text((W - MARGIN - w, H - mm(14)), page_label, font=f, fill=KT_MUTED)

def draw_h2(d, y, text):
    f = ImageFont.truetype(F_SERIF_BOLD, mm(6.5))
    d.text((MARGIN, y), text, font=f, fill=M3)
    return y + mm(9)

def draw_para(d, y, text, size=4.6, color=KT_INK, font_path=F_SANS_REG, line_h=None, max_w=None):
    f = ImageFont.truetype(font_path, mm(size))
    lh = mm(line_h if line_h else size * 1.55)
    for ln in wrap(d, text, f, max_w or CONTENT_W):
        d.text((MARGIN, y), ln, font=f, fill=color)
        y += lh
    return y

def draw_bullet(d, y, text, size=4.6):
    f = ImageFont.truetype(F_SANS_REG, mm(size))
    d.ellipse((MARGIN, y + mm(1.6), MARGIN + mm(1.6), y + mm(3.2)), fill=M3)
    lh = mm(size * 1.55)
    lines = wrap(d, text, f, CONTENT_W - mm(7))
    for ln in lines:
        d.text((MARGIN + mm(6), y), ln, font=f, fill=KT_INK)
        y += lh
    return y + mm(1.5)

# ═══════════════════════════════════ ANLEITUNG ═══════════════════════════════════
def anleitung_seite1():
    img, d, y = new_page("GEBRAUCHSANWEISUNG", "Anleitung: So funktioniert das Werkzeugkarten-Deck")

    y = draw_h2(d, y, "Was ist das Werkzeugkarten-Deck?")
    y = draw_para(d, y, "26 Karten aus dem bereits bestehenden App-Modul „M3 · Werkzeugkasten“ – "
                        "gekürzt auf Kartenlänge und jetzt zusätzlich physisch griffbereit. Drittes "
                        "Deck der Handlungskarten-Serie, nach TK und Krisendeck. Anders als das "
                        "Krisendeck (nur akute Rot-Situationen) deckt dieses Deck den alltäglichen "
                        "Gelb-bis-Orange-Bereich ab – die Situationen, die jeden Schultag vorkommen. "
                        "M3-21–26 wurden am 01.08.2026 neu ergänzt.")
    y += mm(6)

    y = draw_h2(d, y, "Zwei Kartentypen")
    y = draw_bullet(d, y, "8 Situationskarten (M3-01–08) – konkrete Alltagsszenen (Kind kommt "
                          "aufgewühlt an, verweigert Arbeit, eskaliert …), mit Barometer-Einordnung, "
                          "5 Schritten und Verweis auf passende Werkzeugkarten.")
    y = draw_bullet(d, y, "18 Werkzeugkarten (M3-09–26) – einzelne Techniken (Atemanker, Igel-Ball, "
                          "Joker, Sichtbare Zeit, Stopp-Hand-Signal, Sicherer Ort, Körper-Check-In, "
                          "Die Kraft der Pause, No-Blame-Approach …), mit „Wann einsetzen“-Kurzliste, "
                          "Kurzerklärung und Schritt-für-Schritt-Anleitung.")
    y += mm(4)

    y = draw_h2(d, y, "Vorderseite ohne Foto")
    y = draw_para(d, y, "Wie beim Krisendeck bewusst kein Foto, sondern ein kleines Symbol-Icon je "
                        "Karte – schnell erkennbar beim Blättern, ohne Fotoproduktion.")

    footer(d, "Anleitung · 1/2")
    return img

def anleitung_seite2():
    img, d, y = new_page("GEBRAUCHSANWEISUNG", "Der Joker & Brainy-Flow")

    y = draw_h2(d, y, "Der Joker (M3-13)")
    y = draw_para(d, y, "Ein stilles Notfallsignal, das das Kind selbst einsetzt – ohne Worte. Der "
                        "Joker ist eines der sechs KLARTEXT-Systemelemente und taucht deshalb auch "
                        "an anderer Stelle auf: als „Joker-Mechanismus“ bereits im Insel-Set und "
                        "Zonen-Set bei Barometer Gelb. Wichtig: Es gibt daneben ein zweites, "
                        "eigenständiges Joker-Konzept in der App (INGRA ↔ Lehrkraft, ausführlichere "
                        "Vereinbarung) – das ist NICHT Teil dieses Decks und bleibt ein mögliches "
                        "Thema für eine spätere Zusatzkarte.")
    y += mm(6)

    y = draw_h2(d, y, "Brainy-Flow (M3-19)")
    y = draw_para(d, y, "Diese Karte ist die Landkarte des ganzen Decks: sie ordnet allen anderen "
                        "25 Karten eine Barometer-Farbe zu und hilft, in der Situation schnell die "
                        "richtige Karte zu finden. Bei Unsicherheit, welches Werkzeug passt, ist "
                        "M3-19 der Startpunkt. Hinweis: M3-21–26 sind nach Erstellung dieser Karte "
                        "hinzugekommen und dort noch nicht mit aufgeführt.")
    y += mm(6)

    y = draw_h2(d, y, "Kein neues Bildmaterial nötig")
    y = draw_para(d, y, "Anders als bei den bisherigen Reflexionsdecks wurden für dieses Deck keine "
                        "neuen Illustrationen erzeugt – die Symbol-Icons sind aus einer bestehenden "
                        "Icon-Bibliothek gesetzt, kein Fotoshooting oder Bildgenerierung nötig.")

    footer(d, "Anleitung · 2/2")
    return img

# ═══════════════════════════════════ QUELLEN ═══════════════════════════════════
QUELLEN_BESTAETIGT = [
    "Kuypers, L. (2011). The Zones of Regulation – Grundprinzip Barometer/Zustand-Regulierung, "
    "bereits im KLARTEXT-Register bestätigt.",
]

QUELLEN_VORGESCHLAGEN_1 = [
    "Dennison, P. E., & Dennison, G. E. – Brain Gym / Edu-Kinestetik, Grundlage der „Liegenden "
    "Acht“ (M3-10) – exakte Publikation/Auflage vor Druck prüfen.",
    "5-4-3-2-1-Erdungstechnik (M3-11) – etablierte Technik aus Trauma- und Achtsamkeitspraxis, "
    "keine einzelne Primärquelle zugeordnet (wie bereits im Krisendeck-Quellenregister vermerkt).",
    "„Lob-Sandwich“ / Feedback-Sandwich (M3-18) – verbreitete Feedback-Technik aus Pädagogik und "
    "Kommunikationstraining, keine einzelne Primärquelle zugeordnet.",
    "„Time on Their Side: How Visual Timers Affect Anticipatory Anxiety, Performance, and "
    "On-Task Behavior in Elementary Math Assessments.“ (2025). European Journal of Investigation "
    "in Health, Psychology and Education, 15(12). https://doi.org/10.3390/ejihpe15120243 – "
    "Grundlage von „Sichtbare Zeit“ (M3-21).",
]

QUELLEN_VORGESCHLAGEN_2 = [
    "Kounin, J. S. (1970). Discipline and Group Management in Classrooms. New York: Holt, "
    "Rinehart & Winston – Konzept der „Allgegenwärtigkeit“ ruhiger, klarer Signale, bereits im "
    "LK-Deck-Quellenregister verifiziert; inhaltlich verwandt mit „Stopp-Hand-Signal“ (M3-22), "
    "keine einzelne Primärquelle für das Signal selbst.",
    "Siegel, D. (1999). The Developing Mind. New York: Guilford Press – Window of Tolerance, "
    "bereits im Insel-Set-Konzept verifiziert, Grundlage von „Sicherer Ort“ (M3-23).",
    "Porges, S. W. (2011). The Polyvagal Theory: Neurophysiological Foundations of Emotions, "
    "Attachment, Communication, and Self-Regulation. New York: W. W. Norton – Grundlage von "
    "„Körper-Check-In“ (M3-24) und „Die Kraft der Pause“ (M3-25).",
    "Maines, B. & Robinson, G. (1992). The No Blame Approach. Bristol: Lame Duck Publishing – "
    "Grundlage von „No-Blame-Approach“ (M3-26).",
]

QUELLEN_HINWEIS = ("Die inhaltliche Grundlage für alle 26 Karten ist das bereits in der App bestehende, "
    "fachlich hinterlegte Modul M3 · Werkzeugkasten – das Deck kürzt und adaptiert diesen Text für "
    "die physische Karte, erfindet keine neuen Techniken. M3-21–26 wurden am 01.08.2026 ergänzt.")

def quellen_seite():
    img, d, y = new_page("METHODISCHE GRUNDLAGE", "Quellen · 1/2")
    y = draw_para(d, y, QUELLEN_HINWEIS, size=4.6, color=KT_MUTED)
    y += mm(6)

    y = draw_para(d, y, "Etablierte, bereits verifizierte Quelle:", size=4.6, color=KT_MUTED)
    y += mm(4)
    f_q = ImageFont.truetype(F_SANS_REG, mm(4.4))
    for q in QUELLEN_BESTAETIGT:
        for ln in wrap(d, q, f_q, CONTENT_W - mm(6)):
            d.text((MARGIN + mm(6), y), ln, font=f_q, fill=KT_INK)
            y += mm(6.8)
        y += mm(2)
    y += mm(4)

    y = draw_para(d, y, "Vorgeschlagen, bitte fachlich gegenprüfen – noch nicht im KLARTEXT-"
                        "Quellenregister bestätigt (1/2):",
                  size=4.2, color=GOLD)
    y += mm(3)
    for q in QUELLEN_VORGESCHLAGEN_1:
        for ln in wrap(d, q, f_q, CONTENT_W - mm(6)):
            d.text((MARGIN + mm(6), y), ln, font=f_q, fill=KT_INK)
            y += mm(6.8)
        y += mm(2)

    footer(d, "Quellen · 1/2")
    return img

def quellen_seite2():
    img, d, y = new_page("METHODISCHE GRUNDLAGE", "Quellen · 2/2")
    y = draw_para(d, y, "Vorgeschlagen, bitte fachlich gegenprüfen – noch nicht im KLARTEXT-"
                        "Quellenregister bestätigt (2/2):",
                  size=4.2, color=GOLD)
    y += mm(3)
    f_q = ImageFont.truetype(F_SANS_REG, mm(4.4))
    for q in QUELLEN_VORGESCHLAGEN_2:
        for ln in wrap(d, q, f_q, CONTENT_W - mm(6)):
            d.text((MARGIN + mm(6), y), ln, font=f_q, fill=KT_INK)
            y += mm(6.8)
        y += mm(2)

    footer(d, "Quellen · 2/2")
    return img

if __name__ == "__main__":
    pages = {
        "werkzeug_anleitung1": anleitung_seite1(),
        "werkzeug_anleitung2": anleitung_seite2(),
        "werkzeug_quellen": quellen_seite(),
        "werkzeug_quellen2": quellen_seite2(),
    }
    for name, img in pages.items():
        img.save(f"/sessions/kind-beautiful-ptolemy/mnt/outputs/booklet_{name}.png")
        print(name, "ok")
