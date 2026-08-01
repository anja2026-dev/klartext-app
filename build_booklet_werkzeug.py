#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Anleitung & Quellen fürs Werkzeugkarten-Deck (WZ-01–20 als physisches Deck). Drittes Deck im
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

def draw_numbered(d, y, num, titel, text, size=4.8):
    f_num = ImageFont.truetype(F_SERIF_BOLD, mm(7))
    d.ellipse((MARGIN, y, MARGIN + mm(9), y + mm(9)), fill=M3)
    d.text((MARGIN + mm(4.5), y + mm(4.5)), str(num), font=f_num, anchor="mm", fill=(255, 255, 255))
    f_titel = ImageFont.truetype(F_SANS_BOLD, mm(5.2))
    d.text((MARGIN + mm(13), y + mm(0.5)), titel, font=f_titel, fill=M3)
    f_text = ImageFont.truetype(F_SANS_REG, mm(size))
    ty = y + mm(7)
    lh = mm(size * 1.55)
    for ln in wrap(d, text, f_text, CONTENT_W - mm(13)):
        d.text((MARGIN + mm(13), ty), ln, font=f_text, fill=KT_INK)
        ty += lh
    return max(ty, y + mm(11)) + mm(4)

# ═══════════════════════════════════ ANLEITUNG ═══════════════════════════════════
def anleitung_seite1():
    img, d, y = new_page("GEBRAUCHSANWEISUNG", "Anleitung: So funktioniert das Werkzeugkarten-Deck")

    y = draw_h2(d, y, "Was ist das Werkzeugkarten-Deck?")
    y = draw_para(d, y, "26 Karten aus dem bereits bestehenden App-Modul „M3 · Werkzeugkasten“ – "
                        "gekürzt auf Kartenlänge und jetzt zusätzlich physisch griffbereit. Drittes "
                        "Deck der Handlungskarten-Serie, nach TK und Krisendeck. Anders als das "
                        "Krisendeck (nur akute Rot-Situationen) deckt dieses Deck den alltäglichen "
                        "Gelb-bis-Orange-Bereich ab – die Situationen, die jeden Schultag vorkommen. "
                        "WZ-21–26 wurden am 01.08.2026 neu ergänzt.")
    y += mm(6)

    y = draw_h2(d, y, "Zwei Kartentypen")
    y = draw_bullet(d, y, "8 Situationskarten (WZ-01–08) – konkrete Alltagsszenen (Kind kommt "
                          "aufgewühlt an, verweigert Arbeit, eskaliert …), mit Barometer-Einordnung, "
                          "5 Schritten und Verweis auf passende Werkzeugkarten.")
    y = draw_bullet(d, y, "18 Werkzeugkarten (WZ-09–26) – einzelne Techniken (Atemanker, Igel-Ball, "
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

    y = draw_h2(d, y, "Der Joker (WZ-13)")
    y = draw_para(d, y, "Ein stilles Notfallsignal, das das Kind selbst einsetzt – ohne Worte. Der "
                        "Joker ist eines der sechs KLARTEXT-Systemelemente und taucht deshalb auch "
                        "an anderer Stelle auf: als „Joker-Mechanismus“ bereits im Insel-Set und "
                        "Zonen-Set bei Barometer Gelb. Wichtig: Es gibt daneben ein zweites, "
                        "eigenständiges Joker-Konzept in der App (INGRA ↔ Lehrkraft, ausführlichere "
                        "Vereinbarung) – das ist NICHT Teil dieses Decks und bleibt ein mögliches "
                        "Thema für eine spätere Zusatzkarte.")
    y += mm(6)

    y = draw_h2(d, y, "Brainy-Flow (WZ-19)")
    y = draw_para(d, y, "Diese Karte ist die Landkarte des ganzen Decks: sie ordnet allen anderen "
                        "25 Karten eine Barometer-Farbe zu und hilft, in der Situation schnell die "
                        "richtige Karte zu finden. Bei Unsicherheit, welches Werkzeug passt, ist "
                        "WZ-19 der Startpunkt. Hinweis: WZ-21–26 sind nach Erstellung dieser Karte "
                        "hinzugekommen und dort noch nicht mit aufgeführt.")
    y += mm(6)

    y = draw_h2(d, y, "Kein neues Bildmaterial nötig")
    y = draw_para(d, y, "Anders als bei den bisherigen Reflexionsdecks wurden für dieses Deck keine "
                        "neuen Illustrationen erzeugt – die Symbol-Icons sind aus einer bestehenden "
                        "Icon-Bibliothek gesetzt, kein Fotoshooting oder Bildgenerierung nötig.")

    footer(d, "Anleitung · 2/2")
    return img

# ═══════════════════════════════════ BAROMETER & kLAR ═══════════════════════════════════
BAROMETER = [
    ((76, 175, 80), "GRÜN", "Stabil, lernbereit."),
    ((249, 168, 37), "GELB", "Angespannt, aufmerksam."),
    ((239, 108, 0), "ORANGE", "Dysreguliert, braucht Unterstützung – hier greift das kLAR-Modell."),
    ((198, 40, 40), "ROT", "Akute Krise – kLAR reicht nicht mehr, sofort eine Fachperson einbeziehen. "
                            "Für diesen Zustand gibt es das eigene Krisendeck."),
    ((120, 120, 120), "GRAU", "Erschöpft oder orientierungslos – weiß selbst nicht, was es braucht. Erst beobachten, nicht vorschnell einordnen."),
]

KLAR_STEPS = [
    ("K", "Kontakt & Sicherheit",
     "Auf Augenhöhe gehen. Ruhige Stimme, körperliche und räumliche Sicherheit zuerst herstellen."),
    ("L", "Leise & Langsam",
     "Stimme senken, Tempo herausnehmen. Kurze Sätze, Pausen aushalten statt füllen."),
    ("A", "Anerkennung & Atmen",
     "Das Erleben anerkennen – „Ich sehe, das ist gerade viel.“ Gemeinsam bewusst durchatmen."),
    ("R", "Reizreduktion & Rückzug",
     "Reize reduzieren, Rückzug ermöglichen. Raum geben, nicht drängen."),
]

def barometer_klar_seite():
    img, d, y = new_page("KURZ ERKLÄRT", "Barometer & kLAR-Modell")
    y = draw_para(d, y, "Dieses Deck ist auch ohne die KLARTEXT-App nutzbar. Falls du zum ersten Mal mit "
                        "KLARTEXT arbeitest: Hier die Grundlage für die Barometer-Einordnung auf den "
                        "Situationskarten und für WZ-19 (Brainy-Flow).",
                  size=4.6, color=KT_MUTED)
    y += mm(8)

    y = draw_h2(d, y, "Das Barometer – 5 Zustände")
    f_lab = ImageFont.truetype(F_SANS_BOLD, mm(4.8))
    f_desc = ImageFont.truetype(F_SANS_REG, mm(4.4))
    lab_w = mm(30)
    for color, label, desc in BAROMETER:
        d.ellipse((MARGIN, y + mm(0.9), MARGIN + mm(3.6), y + mm(4.5)), fill=color)
        d.text((MARGIN + mm(6), y), label, font=f_lab, fill=KT_INK)
        lines = wrap(d, desc, f_desc, CONTENT_W - lab_w - mm(6))
        ly = y
        for ln in lines:
            d.text((MARGIN + lab_w, ly), ln, font=f_desc, fill=KT_MUTED)
            ly += mm(6.2)
        y = max(ly, y + mm(7.5)) + mm(1.5)
    y += mm(5)

    y = draw_h2(d, y, "Das kLAR-Modell – 4 Schritte bei Anspannung")
    y += mm(2)
    for letter, titel, text in KLAR_STEPS:
        y = draw_numbered(d, y, letter, titel, text)

    y = draw_para(d, y, "kLAR gilt für Gelb und Orange – genau der Bereich, den dieses Deck abdeckt. "
                        "Ab Rot reicht kLAR nicht mehr – dann sofort eine Fachperson einbeziehen.",
                  size=4.2, color=GOLD)

    footer(d, "Barometer & kLAR")
    return img

# ═══════════════════════════════════ QUELLEN ═══════════════════════════════════
QUELLEN_BESTAETIGT = [
    "Kuypers, L. (2011). The Zones of Regulation – Grundprinzip Barometer/Zustand-Regulierung, "
    "bereits im KLARTEXT-Register bestätigt.",
]

QUELLEN_VORGESCHLAGEN_1 = [
    "Dennison, P. E., & Dennison, G. E. – Brain Gym / Edu-Kinestetik, Grundlage der „Liegenden "
    "Acht“ (WZ-10) – exakte Publikation/Auflage vor Druck prüfen.",
    "5-4-3-2-1-Erdungstechnik (WZ-11) – etablierte Technik aus Trauma- und Achtsamkeitspraxis, "
    "keine einzelne Primärquelle zugeordnet (wie bereits im Krisendeck-Quellenregister vermerkt).",
    "„Lob-Sandwich“ / Feedback-Sandwich (WZ-18) – verbreitete Feedback-Technik aus Pädagogik und "
    "Kommunikationstraining, keine einzelne Primärquelle zugeordnet.",
    "„Time on Their Side: How Visual Timers Affect Anticipatory Anxiety, Performance, and "
    "On-Task Behavior in Elementary Math Assessments.“ (2025). European Journal of Investigation "
    "in Health, Psychology and Education, 15(12). https://doi.org/10.3390/ejihpe15120243 – "
    "Grundlage von „Sichtbare Zeit“ (WZ-21).",
]

QUELLEN_VORGESCHLAGEN_2 = [
    "Kounin, J. S. (1970). Discipline and Group Management in Classrooms. New York: Holt, "
    "Rinehart & Winston – Konzept der „Allgegenwärtigkeit“ ruhiger, klarer Signale, bereits im "
    "LK-Deck-Quellenregister verifiziert; inhaltlich verwandt mit „Stopp-Hand-Signal“ (WZ-22), "
    "keine einzelne Primärquelle für das Signal selbst.",
    "Siegel, D. (1999). The Developing Mind. New York: Guilford Press – Window of Tolerance, "
    "bereits im Insel-Set-Konzept verifiziert, Grundlage von „Sicherer Ort“ (WZ-23).",
    "Porges, S. W. (2011). The Polyvagal Theory: Neurophysiological Foundations of Emotions, "
    "Attachment, Communication, and Self-Regulation. New York: W. W. Norton – Grundlage von "
    "„Körper-Check-In“ (WZ-24) und „Die Kraft der Pause“ (WZ-25).",
    "Maines, B. & Robinson, G. (1992). The No Blame Approach. Bristol: Lame Duck Publishing – "
    "Grundlage von „No-Blame-Approach“ (WZ-26).",
]

QUELLEN_HINWEIS = ("Die inhaltliche Grundlage für alle 26 Karten ist das bereits in der App bestehende, "
    "fachlich hinterlegte Modul M3 · Werkzeugkasten – das Deck kürzt und adaptiert diesen Text für "
    "die physische Karte, erfindet keine neuen Techniken. WZ-21–26 wurden am 01.08.2026 ergänzt.")

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
