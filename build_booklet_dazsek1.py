#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Anleitung, Methodik, Glossar, Quellen fürs DaZ-Sek-I-Deck (Deutsch als Zweitsprache, Sek I).
Kein Fachprüfungs-Vorbehalt (Anjas eigene DaZ-/Traumapädagogik-Qualifikation deckt das ab) – aber
mit explizitem Hinweis: kein Trauma-Verarbeitungs-Deck. Letztes Deck der Zehner-Serie."""
from PIL import Image, ImageDraw, ImageFont
Image.init()

DPI = 300
MM = DPI / 25.4
def mm(v): return int(round(v * MM))

DAZSEK1 = (110, 20, 56)          # #6E1438
DAZSEK1_TEXT = (110, 20, 56)     # gleiche Farbe, ausreichend dunkel für Fließtext-Überschriften
DAZSEK1_LIGHT = (240, 231, 235)
DAZSEK1_BORDER = (208, 179, 191)
KT_INK = (45, 45, 45)
KT_MUTED = (122, 112, 96)
KT_PAPER = (245, 240, 232)
GOLD = (150, 120, 50)
WARN_RED = (160, 60, 60)

F_SERIF_BOLD = "/usr/share/fonts/truetype/crosextra/Caladea-Bold.ttf"
F_SERIF_IT = "/usr/share/fonts/truetype/crosextra/Caladea-Italic.ttf"
F_SANS_REG = "/usr/share/fonts/truetype/lato/Lato-Regular.ttf"
F_SANS_MED = "/usr/share/fonts/truetype/lato/Lato-Medium.ttf"
F_SANS_BOLD = "/usr/share/fonts/truetype/lato/Lato-Bold.ttf"
F_SANS_IT = "/usr/share/fonts/truetype/lato/Lato-Italic.ttf"

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
    d.rectangle((0, 0, W, kopf_h), fill=DAZSEK1)
    d.text((MARGIN, mm(10)), kicker, font=f_kicker, fill=(240, 220, 228))
    ty = mm(17)
    for ln in lines:
        d.text((MARGIN, ty), ln, font=f_titel, fill=(255, 255, 255))
        ty += mm(size * 1.35)
    return img, d, kopf_h + mm(14)

def footer(d, page_label):
    f = ImageFont.truetype(F_SANS_REG, mm(4))
    d.text((MARGIN, H - mm(14)), "KLARTEXT-Mentoring · DaZ-Sek-I-Deck · © 2026 Anja Jolk",
           font=f, fill=KT_MUTED)
    w = d.textlength(page_label, font=f)
    d.text((W - MARGIN - w, H - mm(14)), page_label, font=f, fill=KT_MUTED)

def draw_h2(d, y, text):
    f = ImageFont.truetype(F_SERIF_BOLD, mm(6.5))
    lines = wrap(d, text, f, CONTENT_W)
    for ln in lines:
        d.text((MARGIN, y), ln, font=f, fill=DAZSEK1_TEXT)
        y += mm(9)
    return y

def draw_para(d, y, text, size=4.6, color=KT_INK, font_path=F_SANS_REG, line_h=None, max_w=None):
    f = ImageFont.truetype(font_path, mm(size))
    lh = mm(line_h if line_h else size * 1.55)
    for ln in wrap(d, text, f, max_w or CONTENT_W):
        d.text((MARGIN, y), ln, font=f, fill=color)
        y += lh
    return y

def draw_bullet(d, y, text, size=4.6):
    f = ImageFont.truetype(F_SANS_REG, mm(size))
    d.ellipse((MARGIN, y + mm(1.6), MARGIN + mm(1.6), y + mm(3.2)), fill=DAZSEK1_TEXT)
    lh = mm(size * 1.55)
    lines = wrap(d, text, f, CONTENT_W - mm(7))
    for ln in lines:
        d.text((MARGIN + mm(6), y), ln, font=f, fill=KT_INK)
        y += lh
    return y + mm(1.5)

def draw_numbered(d, y, num, titel, text, size=4.8):
    f_num = ImageFont.truetype(F_SERIF_BOLD, mm(7))
    d.ellipse((MARGIN, y, MARGIN + mm(9), y + mm(9)), fill=DAZSEK1_TEXT)
    d.text((MARGIN + mm(4.5), y + mm(4.5)), str(num), font=f_num, anchor="mm", fill=(255, 255, 255))
    f_titel = ImageFont.truetype(F_SANS_BOLD, mm(5.2))
    d.text((MARGIN + mm(13), y + mm(0.5)), titel, font=f_titel, fill=DAZSEK1_TEXT)
    f_text = ImageFont.truetype(F_SANS_REG, mm(size))
    ty = y + mm(7)
    lh = mm(size * 1.55)
    for ln in wrap(d, text, f_text, CONTENT_W - mm(13)):
        d.text((MARGIN + mm(13), ty), ln, font=f_text, fill=KT_INK)
        ty += lh
    return max(ty, y + mm(11)) + mm(4)

def draw_warnbox(d, y, label, text):
    f_warn_text = ImageFont.truetype(F_SANS_REG, mm(4.6))
    warn_lines = wrap(d, text, f_warn_text, CONTENT_W - mm(16))
    line_h = mm(4.6 * 1.55)
    box_h = mm(15) + len(warn_lines) * line_h + mm(6)
    d.rounded_rectangle((MARGIN, y, W - MARGIN, y + box_h), radius=mm(3),
                         fill=(253, 245, 245), outline=(210, 160, 160), width=mm(0.4))
    f_warn_l = ImageFont.truetype(F_SANS_BOLD, mm(5.5))
    d.text((MARGIN + mm(8), y + mm(7)), label, font=f_warn_l, fill=WARN_RED)
    wy = y + mm(15)
    for ln in warn_lines:
        d.text((MARGIN + mm(8), wy), ln, font=f_warn_text, fill=KT_INK)
        wy += line_h
    return y + box_h

# ═══════════════════════════════════ ANLEITUNG ═══════════════════════════════════
def anleitung_seite1():
    img, d, y = new_page("GEBRAUCHSANWEISUNG", "Anleitung: So funktioniert das DaZ-Sek-I-Deck")

    y = draw_h2(d, y, "Was ist das DaZ-Sek-I-Deck?")
    y = draw_para(d, y, "25 Impulskarten für Jugendliche der Sekundarstufe I mit Deutsch als "
                        "Zweitsprache und/oder Migrations-/Fluchthintergrund. Themen: Ankommen im "
                        "neuen System, Sprache und Leistung, Identität zwischen den Kulturen, "
                        "Freundschaft und Zugehörigkeit, Herkunft und was fehlt, Zukunft und "
                        "Stolz, sowie der Übergang in die Regelklasse.")
    y += mm(6)

    y = draw_h2(d, y, "Warum ein eigenes Deck und nicht einfach DaZ-GS mit schwereren Wörtern?")
    y = draw_para(d, y, "Sek I ist ein realer Bruchpunkt: neues Schulsystem, komplexere soziale "
                        "Dynamik, Diskriminierung und Identität werden explizit zum Thema – nicht "
                        "nur eine schwierigere Version der Grundschul-Themen.")
    y += mm(8)

    y = draw_h2(d, y, "In drei Schritten")
    y += mm(2)
    y = draw_numbered(d, y, 1, "Karte auswählen",
        "Passend zur aktuellen Situation. Die sieben Themenblöcke (Ankommen im neuen System, "
        "Sprache & Leistung, Identität zwischen den Kulturen, Freundschaft & Zugehörigkeit, "
        "Herkunft & was ich vermisse, Zukunft & Stolz, Übergang in die Regelklasse) helfen bei "
        "der Auswahl.")
    y = draw_numbered(d, y, 2, "Anleitung lesen, dann Fragen stellen",
        "Beide Fragen sind offen formuliert. Es ist in Ordnung, wenn nur eine Frage beantwortet "
        "wird oder die Antwort sehr kurz ausfällt.")
    y = draw_numbered(d, y, 3, "„Tipp für die INGRA“ nutzen",
        "Ein kurzer, direkt umsetzbarer Hinweis auf jeder Rückseite – zur eigenen Vorbereitung, "
        "nicht zum Vorlesen.")

    footer(d, "Anleitung · 1/2")
    return img

def anleitung_seite2():
    img, d, y = new_page("GEBRAUCHSANWEISUNG", "Wichtiger Hinweis: Kein Trauma-Verarbeitungs-Deck")

    y = draw_warnbox(d, y, "BEWUSSTE ABGRENZUNG",
        "Manche Jugendlichen in dieser Zielgruppe haben Fluchterfahrungen. Dieses Deck ist NICHT "
        "für die Verarbeitung von Fluchttraumata gedacht. Keine Karte fragt nach Fluchtdetails "
        "oder belastenden Ereignissen. Kommt trotzdem eine belastende Erzählung auf: nicht "
        "nachfragen, das Gefühl würdigen und bei Bedarf professionelle Unterstützung "
        "einbeziehen.")
    y += mm(10)

    y = draw_h2(d, y, "Wo Heimweh vorkommt (Block E)")
    y = draw_para(d, y, "Der Fokus bleibt bewusst beim Gefühl in der Gegenwart – was jemand "
                        "vermisst und was gerade hilft –, nicht bei der Vergangenheit oder den "
                        "Umständen des Weggehens. Jugendliche pflegen Kontakt oft eigenständiger "
                        "als jüngere Kinder – das wird als reale Ressource anerkannt.")
    y += mm(6)

    y = draw_h2(d, y, "Diskriminierung und Identität werden direkt benannt")
    y = draw_para(d, y, "Anders als bei DaZ-GS spricht dieses Deck Diskriminierungserfahrungen "
                        "und doppelte kulturelle Zugehörigkeit direkt an (Block C, D) – "
                        "altersgerecht für Jugendliche, die diese Themen bereits bewusst "
                        "erleben.")

    footer(d, "Anleitung · 2/2")
    return img

# ═══════════════════════════════════ METHODIK ═══════════════════════════════════
def methodik_seite():
    img, d, y = new_page("HINTERGRUND", "Sechs Themenblöcke, eine Haltung")
    y = draw_para(d, y, "25 Karten: sechs Blöcke à 4 Karten – Ankommen im neuen System, "
                        "Sprache & Leistung, Identität zwischen den Kulturen, Freundschaft & "
                        "Zugehörigkeit, Herkunft & was ich vermisse, Zukunft & Stolz – plus eine "
                        "Übergangskarte (Block G, ergänzt 30.07.2026).",
                  size=4.6, color=KT_MUTED)
    y += mm(8)

    y = draw_h2(d, y, "Warum keine dritte Frage wie bei EL/LK/TR?")
    y = draw_para(d, y, "Wie bei KD/FS/AT/ADHS/DaZ-GS folgt das DaZ-Sek-I-Deck der Content-Achse: "
                        "Anleitung + 2 Impulsfragen + „Tipp für die INGRA“, keine dritte Frage.")
    y += mm(8)

    y = draw_h2(d, y, "Herkunftssprache und -qualifikation als Ressource, nicht als Defizit")
    y = draw_para(d, y, "Mehrere Karten (z. B. DAZ-SEK1-06, DAZ-SEK1-22) kehren die übliche "
                        "Blickrichtung bewusst um: Sprachmittlung für die Eltern und "
                        "Vorqualifikationen aus dem Herkunftsland werden als eigenständiges "
                        "Können sichtbar gemacht, nicht übergangen (vgl. Gogolin 1994/2008 zum "
                        "„monolingualen Habitus“ der Schule).")
    y += mm(6)

    y = draw_h2(d, y, "Kein Brainy")
    y = draw_para(d, y, "Anders als bei KD/FS/DaZ-GS verzichtet das DaZ-Sek-I-Deck auf die "
                        "Coach-Figur Brainy – wie bei JD/AT/ADHS, da eine Maskottchen-Figur für "
                        "Sek-I-Jugendliche zu kindlich wirkt.")

    footer(d, "Methodik")
    return img

# ═══════════════════════════════════ GLOSSAR ═══════════════════════════════════
GLOSSAR = [
    ("DaZ-Sek-I-Deck", "Die 25 Karten dieses Decks für Jugendliche der Sekundarstufe I mit "
     "Deutsch als Zweitsprache und/oder Migrations-/Fluchthintergrund."),
    ("DaZ", "Deutsch als Zweitsprache – der Spracherwerb von Jugendlichen, deren Familiensprache "
     "nicht Deutsch ist."),
    ("Monolingualer Habitus", "Der Umstand, dass Schule oft so kommuniziert, als sei "
     "Einsprachigkeit die Norm (Gogolin 1994/2008) – Grundlage für die Haltung dieses Decks."),
    ("Migrationsandere", "Begriff nach Mecheril (2004) für die gesellschaftliche Zuschreibung "
     "„nicht von hier“ – der genaue Wortlaut im Primärtext von 2004 konnte nicht abschließend "
     "verifiziert werden, nur über Sekundärquellen belegt."),
    ("INGRA", "Bezeichnung für die pädagogischen Fachkräfte des KLARTEXT-Systems (früher: "
     "Schulbegleiter:in). Begleitet die Nutzung der Karten gemeinsam mit dem/der Jugendlichen."),
    ("Sprachmittlung", "Wenn ein Jugendlicher für seine Eltern zwischen zwei Sprachen übersetzt, "
     "oft bei Behördenterminen (siehe DAZ-SEK1-06) – kann stolz machen, aber auch belasten."),
]

def glossar_seite(begriffe, seiten_label, intro=None):
    img, d, y = new_page("BEGRIFFE AUS DEM DAZ-SEK-I-DECK", "Glossar")
    if intro:
        y = draw_para(d, y, intro, size=4.6, color=KT_MUTED)
        y += mm(8)

    for begriff, definition in begriffe:
        f_term = ImageFont.truetype(F_SERIF_BOLD, mm(6))
        d.text((MARGIN, y), begriff, font=f_term, fill=DAZSEK1_TEXT)
        y += mm(9)
        y = draw_para(d, y, definition, size=4.4)
        y += mm(4)
        d.line((MARGIN, y, W - MARGIN, y), fill=DAZSEK1_BORDER, width=mm(0.3))
        y += mm(7)

    footer(d, seiten_label)
    return img

# ═══════════════════════════════════ QUELLEN ═══════════════════════════════════
QUELLEN_VORGESCHLAGEN = [
    "Gogolin, I. (1994). Der monolinguale Habitus der multilingualen Schule. Münster: Waxmann "
    "(2., unveränderte Auflage 2008). — Schule kommuniziert oft, als sei Einsprachigkeit die "
    "Norm; Grundlage für Block B und die Wertschätzung der Herkunftssprache/-qualifikation.",
    "Mecheril, P. (2004). Einführung in die Migrationspädagogik. Weinheim/Basel: Beltz. — "
    "Konzept „Migrationsandere“; Grundlage für die Haltung des Decks (Zugehörigkeit stärken, "
    "nicht Differenz betonen). Der exakte Wortlaut im Primärtext von 2004 konnte nur über "
    "Sekundärquellen bestätigt werden.",
]

def quellen_seite():
    img, d, y = new_page("METHODISCHE GRUNDLAGE", "Quellen")
    y = draw_para(d, y, "Beide Quellen sind einzeln geprüft (26.07.2026), aber noch nicht im "
                        "KLARTEXT-Quellenregister bestätigt – „vorgeschlagen, bitte fachlich "
                        "gegenprüfen“. Dieselben Quellen wie beim DaZ-GS-Deck.", size=4.6, color=KT_MUTED)
    y += mm(9)

    f_q = ImageFont.truetype(F_SANS_REG, mm(4.6))
    for q in QUELLEN_VORGESCHLAGEN:
        for ln in wrap(d, q, f_q, CONTENT_W - mm(6)):
            d.text((MARGIN + mm(6), y), ln, font=f_q, fill=KT_INK)
            y += mm(7.2)
        y += mm(3)

    footer(d, "Quellen")
    return img

if __name__ == "__main__":
    pages = {
        "dazsek1_anleitung1": anleitung_seite1(),
        "dazsek1_anleitung2": anleitung_seite2(),
        "dazsek1_methodik": methodik_seite(),
        "dazsek1_glossar1": glossar_seite(GLOSSAR[:3], "Glossar · 1/2",
            intro="Kurz erklärt: Begriffe, die auf den Karten oder in dieser Anleitung vorkommen "
                  "und nicht selbsterklärend sind."),
        "dazsek1_glossar2": glossar_seite(GLOSSAR[3:], "Glossar · 2/2"),
        "dazsek1_quellen": quellen_seite(),
    }
    for name, img in pages.items():
        img.save(f"/sessions/kind-beautiful-ptolemy/mnt/outputs/booklet_{name}.png")
        print(name, "ok")
