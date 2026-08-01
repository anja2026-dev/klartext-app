#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Anleitung, Methodik, Glossar, Quellen fürs AT-Deck. Fachprüfung durch externe Autismus-Fachperson
abgeschlossen (27.07.2026) – kein Entwurfs-Status mehr. Kind-facing wie JD/KD (nicht Erwachsenen-
Selbstreflexion wie EL/LK/TR): "Tipp für die INGRA", Kind-Barometer direkt eingebunden, kLAR-Modell
nur INGRA-seitig, KEINE dritte systemische Frage."""
from PIL import Image, ImageDraw, ImageFont
Image.init()

DPI = 300
MM = DPI / 25.4
def mm(v): return int(round(v * MM))

AT = (124, 140, 126)          # #7C8C7E
AT_LIGHT = (237, 241, 236)
AT_BORDER = (201, 211, 201)
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
    d.rectangle((0, 0, W, kopf_h), fill=AT)
    d.text((MARGIN, mm(10)), kicker, font=f_kicker, fill=(240, 244, 239))
    ty = mm(17)
    for ln in lines:
        d.text((MARGIN, ty), ln, font=f_titel, fill=(255, 255, 255))
        ty += mm(size * 1.35)
    return img, d, kopf_h + mm(14)

def footer(d, page_label):
    f = ImageFont.truetype(F_SANS_REG, mm(4))
    d.text((MARGIN, H - mm(14)), "KLARTEXT-Mentoring · AT-Deck · © 2026 Anja Jolk",
           font=f, fill=KT_MUTED)
    w = d.textlength(page_label, font=f)
    d.text((W - MARGIN - w, H - mm(14)), page_label, font=f, fill=KT_MUTED)

def draw_h2(d, y, text):
    f = ImageFont.truetype(F_SERIF_BOLD, mm(6.5))
    d.text((MARGIN, y), text, font=f, fill=AT)
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
    d.ellipse((MARGIN, y + mm(1.6), MARGIN + mm(1.6), y + mm(3.2)), fill=AT)
    lh = mm(size * 1.55)
    lines = wrap(d, text, f, CONTENT_W - mm(7))
    for ln in lines:
        d.text((MARGIN + mm(6), y), ln, font=f, fill=KT_INK)
        y += lh
    return y + mm(1.5)

def draw_numbered(d, y, num, titel, text, size=4.8):
    f_num = ImageFont.truetype(F_SERIF_BOLD, mm(7))
    d.ellipse((MARGIN, y, MARGIN + mm(9), y + mm(9)), fill=AT)
    d.text((MARGIN + mm(4.5), y + mm(4.5)), str(num), font=f_num, anchor="mm", fill=(255, 255, 255))
    f_titel = ImageFont.truetype(F_SANS_BOLD, mm(5.2))
    d.text((MARGIN + mm(13), y + mm(0.5)), titel, font=f_titel, fill=AT)
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
    img, d, y = new_page("GEBRAUCHSANWEISUNG", "Anleitung: So funktioniert das AT-Deck")

    y = draw_h2(d, y, "Was ist das AT-Deck?")
    y = draw_para(d, y, "Das AT-Deck ist eine autismus-sensible Version der Content-Achse (wie JD/KD) "
                        "– dieselben Grundthemen (Gefühle, soziale Situationen, Alltag), aber in einer "
                        "angepassten Machart: wörtlich gemeinte Sprache statt Metaphern, klare oder "
                        "skalierte Fragen statt ausschließlich offener Fragen, und eine bei jeder Karte "
                        "identische, vorhersehbare Struktur.")
    y += mm(6)

    y = draw_h2(d, y, "Für wen ist es gedacht?")
    y = draw_para(d, y, "Für autistische Kinder und Jugendliche, gemeinsam mit einer INGRA-Fachkraft "
                        "oder einer anderen Begleitperson – die Anleitung auf der Rückseite richtet "
                        "sich an die begleitende Person, nicht an das Kind direkt.")
    y += mm(8)

    y = draw_h2(d, y, "In drei Schritten")
    y += mm(2)
    y = draw_numbered(d, y, 1, "Karte auswählen",
        "Passend zur aktuellen Situation oder zum Thema, das gerade ansteht. Die sechs Themenblöcke "
        "(siehe Rückseite dieser Seite) helfen bei der Auswahl.")
    y = draw_numbered(d, y, 2, "Anleitung lesen, dann Fragen stellen",
        "Beide Fragen sind bewusst konkret formuliert. Es ist in Ordnung, wenn nur eine Frage "
        "beantwortet wird oder die Antwort sehr kurz ausfällt.")
    y = draw_numbered(d, y, 3, "„Tipp für die INGRA“ nutzen",
        "Ein kurzer, direkt umsetzbarer Hinweis auf jeder Rückseite – zur eigenen Vorbereitung, nicht "
        "zum Vorlesen.")

    footer(d, "Anleitung · 1/2")
    return img

def anleitung_seite2():
    img, d, y = new_page("GEBRAUCHSANWEISUNG", "Fachlich geprüft")

    y = draw_para(d, y, "Kartentexte, Bilder und Anleitung wurden von einer externen "
                        "Autismus-Fachperson gegengelesen (Fachprüfung abgeschlossen). Das Deck ist "
                        "damit für den produktiven Einsatz mit Kindern freigegeben.",
                  size=4.8, color=KT_INK)
    y += mm(10)

    y = draw_h2(d, y, "Vier Grundprinzipien dieses Decks")
    y = draw_bullet(d, y, "Wörtlich gemeinte Sprache – keine Metaphern, keine bildhaften Umschreibungen.")
    y = draw_bullet(d, y, "Klare, oft geschlossene oder skalierte Fragen (Zahl, Ja/Nein, konkrete "
                          "Beobachtung), wo das hilfreicher ist als eine offene Frage.")
    y = draw_bullet(d, y, "Vorhersehbarkeit – jede Karte hat exakt denselben Aufbau, keine Überraschungen "
                          "im Format.")
    y = draw_bullet(d, y, "Reizarme Bildgestaltung – ruhige, unaufgeräumte Bilder ohne Symbolik.")

    footer(d, "Anleitung · 2/2")
    return img

# ═══════════════════════════════════ METHODIK ═══════════════════════════════════
def methodik_seite():
    img, d, y = new_page("HINTERGRUND", "Warum eine eigene Machart statt eines eigenen Themas?")
    y = draw_para(d, y, "Das AT-Deck erfindet keine neuen Themen – dieselben Grundthemen wie bei JD/KD "
                        "(Gefühle, soziale Situationen, Alltag) werden nur anders aufbereitet.",
                  size=4.6, color=KT_MUTED)
    y += mm(8)

    y = draw_h2(d, y, "Kind-Barometer statt neuer Begriffe")
    y = draw_para(d, y, "Anders als bei EL/LK/TR (dort bewusst ausgeschlossen) ist das Kind-Barometer "
                        "(Grün/Gelb/Orange/Rot/Grau) hier direkt eingebunden (AT-20) – es ist bereits "
                        "ein konkretes, nicht-metaphorisches System und passt damit gut zum "
                        "Grundprinzip dieses Decks. Das kLAR-Modell bleibt wie bei JD/KD nur "
                        "INGRA-seitig in der Anleitung erklärt.")
    y += mm(8)

    y = draw_h2(d, y, "Warum keine dritte Frage wie bei EL/LK/TR?")
    y = draw_para(d, y, "Die Erwachsenen-Decks bekommen bewusst eine dritte, variierende Frage aus der "
                        "systemischen Beratung. Beim AT-Deck gilt das Gegenteil: Vorhersehbarkeit hat "
                        "Vorrang vor zusätzlicher Tiefe – jede Karte folgt exakt derselben Struktur, "
                        "ohne Variation.")
    y += mm(6)

    y = draw_h2(d, y, "Kein Brainy im Bild")
    y = draw_para(d, y, "Da das AT-Deck auch ältere Kinder und Jugendliche anspricht, wurde bewusst auf "
                        "Brainy als Bildfigur verzichtet (wie bei JD/EL/LK/TR) – nur das K-Logo im "
                        "Kartenkopf, um nicht kindisch zu wirken.")

    footer(d, "Methodik")
    return img

# ═══════════════════════════════════ BAROMETER & kLAR ═══════════════════════════════════
BAROMETER = [
    ((76, 175, 80), "GRÜN", "Stabil, lernbereit."),
    ((249, 168, 37), "GELB", "Angespannt, aufmerksam."),
    ((239, 108, 0), "ORANGE", "Dysreguliert, braucht Unterstützung – hier greift das kLAR-Modell."),
    ((198, 40, 40), "ROT", "Akute Krise – kLAR reicht nicht mehr, sofort eine Fachperson einbeziehen."),
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
                        "KLARTEXT arbeitest: Hier die beiden Grundbegriffe, auf die AT-20 sich bezieht.",
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

    y = draw_para(d, y, "kLAR gilt für Gelb und Orange. Ab Rot reicht kLAR nicht mehr – dann sofort eine "
                        "Fachperson einbeziehen.", size=4.2, color=GOLD)

    footer(d, "Barometer & kLAR")
    return img

# ═══════════════════════════════════ GLOSSAR ═══════════════════════════════════
GLOSSAR = [
    ("AT-Deck", "Die 24 Karten dieses Decks, in sechs Themenblöcken – autismus-sensible Machart "
     "bestehender Content-Achse-Themen. Fachlich geprüft, einsatzbereit."),
    ("Spezialinteresse", "Ein Thema, mit dem sich eine Person besonders intensiv und ausdauernd "
     "beschäftigt. Im AT-Deck bewusst als Ressource behandelt, nicht als Ablenkung."),
    ("Kind-Barometer", "Das 5-Zustände-System (Grün/Gelb/Orange/Rot/Grau) aus JD/KD, im AT-Deck "
     "direkt als konkretes, nicht-metaphorisches Werkzeug genutzt (siehe AT-20)."),
    ("INGRA", "Bezeichnung für die pädagogischen Fachkräfte des KLARTEXT-Systems (früher: "
     "Schulbegleiter:in). Begleitet die Nutzung der AT-Karten gemeinsam mit dem Kind."),
    ("Wörtliche Sprache", "Sprache ohne Metaphern oder bildhafte Umschreibungen (z. B. nicht "
     "„Schmetterlinge im Bauch“, sondern konkrete Körpersignale benennen)."),
    ("Vorhersehbarkeit", "Grundprinzip des AT-Decks: jede Karte hat exakt denselben Aufbau (Anleitung "
     "+ 2 Fragen + Tipp für die INGRA), keine Überraschungen im Format."),
]

def glossar_seite(begriffe, seiten_label, intro=None):
    img, d, y = new_page("BEGRIFFE AUS DEM AT-DECK", "Glossar")
    if intro:
        y = draw_para(d, y, intro, size=4.6, color=KT_MUTED)
        y += mm(8)

    for begriff, definition in begriffe:
        f_term = ImageFont.truetype(F_SERIF_BOLD, mm(6))
        d.text((MARGIN, y), begriff, font=f_term, fill=AT)
        y += mm(9)
        y = draw_para(d, y, definition, size=4.4)
        y += mm(4)
        d.line((MARGIN, y, W - MARGIN, y), fill=AT_BORDER, width=mm(0.3))
        y += mm(7)

    footer(d, seiten_label)
    return img

# ═══════════════════════════════════ QUELLEN ═══════════════════════════════════
QUELLEN_BESTAETIGT = [
    "American Psychiatric Association. (2013). Diagnostic and statistical manual of mental "
    "disorders (5th ed.). APA Publishing. — Diagnostische Grundlage.",
    "Milton, D. E. M. (2012). On the ontological status of autism: The 'double empathy problem'. "
    "Disability & Society, 27(6), 883–887. — Autismus als anderer Wahrnehmungsstil, nicht Defizit; "
    "Missverständnisse entstehen auf beiden Seiten.",
    "Hejlskov Elvén, B. (2022). Keine Macht den Mächtigen: Warum Zwang und Druck in der Erziehung "
    "scheitern. Probst. — Grundlage für Vorhersehbarkeit und konkrete Unterstützung statt Druck.",
]

def quellen_seite():
    img, d, y = new_page("METHODISCHE GRUNDLAGE", "Quellen")
    y = draw_para(d, y, "Alle drei Quellen sind bereits im KLARTEXT-Quellenregister bestätigt (einzeln "
                        "nachgeprüft, 26.07.2026) – keine unbestätigten Quellen in diesem Deck.",
                  size=4.6, color=KT_MUTED)
    y += mm(9)

    f_q = ImageFont.truetype(F_SANS_REG, mm(4.6))
    for q in QUELLEN_BESTAETIGT:
        for ln in wrap(d, q, f_q, CONTENT_W - mm(6)):
            d.text((MARGIN + mm(6), y), ln, font=f_q, fill=KT_INK)
            y += mm(7.2)
        y += mm(3)
    y += mm(6)

    y = draw_h2(d, y, "Beispielhafte Passung")
    y = draw_bullet(d, y, "AT-01 bis AT-04 (Übergänge) – Hejlskov Elvén: Vorhersehbarkeit und "
                          "Ankündigung statt Druck bei Veränderungen.")
    y = draw_bullet(d, y, "AT-09 bis AT-12 (Soziale Regeln) – Milton: ungeschriebene Regeln explizit "
                          "machen statt vorauszusetzen, dass sie \"selbstverständlich\" verstanden werden.")
    y = draw_bullet(d, y, "AT-13 bis AT-16 (Spezialinteressen) – DSM-5-Einordnung als Merkmal, hier "
                          "bewusst als Ressource statt als Symptom behandelt.")

    footer(d, "Quellen")
    return img

if __name__ == "__main__":
    pages = {
        "at_anleitung1": anleitung_seite1(),
        "at_anleitung2": anleitung_seite2(),
        "at_methodik": methodik_seite(),
        "at_glossar1": glossar_seite(GLOSSAR[:3], "Glossar · 1/2",
            intro="Kurz erklärt: Begriffe, die auf den Karten oder in dieser Anleitung vorkommen und "
                  "nicht selbsterklärend sind."),
        "at_glossar2": glossar_seite(GLOSSAR[3:], "Glossar · 2/2"),
        "at_quellen": quellen_seite(),
    }
    for name, img in pages.items():
        img.save(f"/sessions/kind-beautiful-ptolemy/mnt/outputs/booklet_{name}.png")
        print(name, "ok")
