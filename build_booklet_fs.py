#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Anleitung, Methodik, Glossar, Quellen fürs FS-Deck (Förderschule). Sprachlich vereinfachte
KD-Adaption, kein Fachprüfungs-Vorbehalt (Anjas eigene 7 Jahre Förderschule-Praxiserfahrung deckt
das ab, analog zum Pflegekinder-Ergänzungsset) – daher normale Anleitung ohne Warnbox."""
from PIL import Image, ImageDraw, ImageFont
Image.init()

DPI = 300
MM = DPI / 25.4
def mm(v): return int(round(v * MM))

FS = (222, 178, 52)           # #DEB234
FS_TEXT = (150, 112, 20)      # dunklere Textvariante fuer Lesbarkeit auf Weiss
FS_LIGHT = (251, 243, 220)
FS_BORDER = (237, 219, 168)
KT_INK = (45, 45, 45)
KT_MUTED = (122, 112, 96)
KT_PAPER = (245, 240, 232)
GOLD = (150, 120, 50)

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
    d.rectangle((0, 0, W, kopf_h), fill=FS)
    d.text((MARGIN, mm(10)), kicker, font=f_kicker, fill=(90, 68, 12))
    ty = mm(17)
    for ln in lines:
        d.text((MARGIN, ty), ln, font=f_titel, fill=(60, 45, 8))
        ty += mm(size * 1.35)
    return img, d, kopf_h + mm(14)

def footer(d, page_label):
    f = ImageFont.truetype(F_SANS_REG, mm(4))
    d.text((MARGIN, H - mm(14)), "KLARTEXT-Mentoring · FS-Deck · © 2026 Anja Jolk",
           font=f, fill=KT_MUTED)
    w = d.textlength(page_label, font=f)
    d.text((W - MARGIN - w, H - mm(14)), page_label, font=f, fill=KT_MUTED)

def draw_h2(d, y, text):
    f = ImageFont.truetype(F_SERIF_BOLD, mm(6.5))
    d.text((MARGIN, y), text, font=f, fill=FS_TEXT)
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
    d.ellipse((MARGIN, y + mm(1.6), MARGIN + mm(1.6), y + mm(3.2)), fill=FS_TEXT)
    lh = mm(size * 1.55)
    lines = wrap(d, text, f, CONTENT_W - mm(7))
    for ln in lines:
        d.text((MARGIN + mm(6), y), ln, font=f, fill=KT_INK)
        y += lh
    return y + mm(1.5)

def draw_numbered(d, y, num, titel, text, size=4.8):
    f_num = ImageFont.truetype(F_SERIF_BOLD, mm(7))
    d.ellipse((MARGIN, y, MARGIN + mm(9), y + mm(9)), fill=FS_TEXT)
    d.text((MARGIN + mm(4.5), y + mm(4.5)), str(num), font=f_num, anchor="mm", fill=(255, 255, 255))
    f_titel = ImageFont.truetype(F_SANS_BOLD, mm(5.2))
    d.text((MARGIN + mm(13), y + mm(0.5)), titel, font=f_titel, fill=FS_TEXT)
    f_text = ImageFont.truetype(F_SANS_REG, mm(size))
    ty = y + mm(7)
    lh = mm(size * 1.55)
    for ln in wrap(d, text, f_text, CONTENT_W - mm(13)):
        d.text((MARGIN + mm(13), ty), ln, font=f_text, fill=KT_INK)
        ty += lh
    return max(ty, y + mm(11)) + mm(4)

# ═══════════════════════════════════ ANLEITUNG ═══════════════════════════════════
def anleitung_seite1():
    img, d, y = new_page("GEBRAUCHSANWEISUNG", "Anleitung: So funktioniert das FS-Deck")

    y = draw_h2(d, y, "Was ist das FS-Deck?")
    y = draw_para(d, y, "Das FS-Deck ist die sprachlich vereinfachte Version des KD-Decks "
                        "(Grundschule) – 30 Karten mit gleichen Themen, gleicher Aufbau, eigene "
                        "Bilder mit Brainy, alle Texte in einfacher Sprache, plus 2 FS-eigene "
                        "Ergänzungskarten zu Lernen und Kommunikation. Für Kinder, die der "
                        "Satzbau oder Umfang der KD-Texte überfordern würde.")
    y += mm(6)

    y = draw_h2(d, y, "Für wen ist es gedacht?")
    y = draw_para(d, y, "Für Kinder mit Sprach- oder Lernschwierigkeiten, insbesondere im Kontext "
                        "Förderschule, gemeinsam mit einer INGRA-Fachkraft oder einer anderen "
                        "Begleitperson – die Anleitung auf der Rückseite richtet sich an die "
                        "begleitende Person, nicht an das Kind direkt.")
    y += mm(8)

    y = draw_h2(d, y, "In drei Schritten")
    y += mm(2)
    y = draw_numbered(d, y, 1, "Karte auswählen",
        "Passend zum Thema, das gerade ansteht. Die Reihenfolge folgt den KD-Themenblöcken "
        "(Gefühle, Konflikte, Mut, Freundschaft, Körperwahrnehmung, Ruhe), plus dem FS-eigenen "
        "Block Lernen und Kommunikation.")
    y = draw_numbered(d, y, 2, "Anleitung lesen, dann Fragen stellen",
        "Beide Fragen sind bewusst kurz formuliert. Es ist in Ordnung, wenn nur eine Frage "
        "beantwortet wird oder die Antwort sehr kurz ausfällt.")
    y = draw_numbered(d, y, 3, "„Tipp für die INGRA“ nutzen",
        "Ein kurzer, direkt umsetzbarer Hinweis auf jeder Rückseite – zur eigenen Vorbereitung, "
        "nicht zum Vorlesen.")

    footer(d, "Anleitung · 1/2")
    return img

def anleitung_seite2():
    img, d, y = new_page("GEBRAUCHSANWEISUNG", "Was an diesem Deck anders ist als bei KD")

    y = draw_h2(d, y, "Sprachregeln in diesem Deck")
    y = draw_bullet(d, y, "Kurze Sätze – ein Gedanke pro Satz, keine verschachtelten Nebensätze.")
    y = draw_bullet(d, y, "Aktiv statt Passiv, kein Konjunktiv wo vermeidbar (\"kannst du\" statt "
                          "\"könntest du\").")
    y = draw_bullet(d, y, "Alltagswörter statt Fachbegriffe, konkrete Beispiele statt Abstraktion.")
    y = draw_bullet(d, y, "Direkte Anrede \"du\", wie bei KD.")
    y += mm(4)

    y = draw_h2(d, y, "Zur Einordnung")
    y = draw_para(d, y, "Diese Sprachvereinfachung folgt anerkannten Regeln für einfache Sprache "
                        "(siehe Quellen), ist aber kein Ersatz für eine formale "
                        "Leichte-Sprache-Prüfung durch eine zertifizierte Prüfgruppe mit "
                        "Betroffenen. Die fachliche Grundlage für dieses Deck stützt sich auf "
                        "mehrjährige Praxiserfahrung in der Förderschule (Schwerpunkt Sprache "
                        "und Lernen).")

    footer(d, "Anleitung · 2/2")
    return img

# ═══════════════════════════════════ METHODIK ═══════════════════════════════════
def methodik_seite():
    img, d, y = new_page("HINTERGRUND", "Warum eine Sprachvariante statt eines neuen Themas?")
    y = draw_para(d, y, "Das FS-Deck übernimmt für 30 Karten dieselben Themen wie KD und bereitet "
                        "sie nur sprachlich anders auf. 2 weitere Karten (Lernfrust, Sagen was ich "
                        "brauche) sind FS-eigene Ergänzungen zu Themen, die spezifisch für die "
                        "Zielgruppe Förderschule sind und keine KD-Entsprechung haben (ergänzt "
                        "30.07.2026).",
                  size=4.6, color=KT_MUTED)
    y += mm(8)

    y = draw_h2(d, y, "Kind-Barometer und kLAR-Modell wie bei KD")
    y = draw_para(d, y, "Genau wie bei KD ist das Kind-Barometer (Grün/Gelb/Orange/Rot/Grau) "
                        "direkt eingebunden (FS-01), das kLAR-Modell bleibt nur INGRA-seitig in "
                        "der Anleitung erklärt.")
    y += mm(8)

    y = draw_h2(d, y, "Warum keine Piktogramme in dieser Auflage?")
    y = draw_para(d, y, "Etablierte Symbolsysteme wie Metacom oder PCS/Boardmaker sind "
                        "lizenzpflichtig und wurden hier bewusst nicht verwendet. Diese Auflage "
                        "setzt auf reine Sprachvereinfachung. Eigene, selbst gezeichnete "
                        "Symbol-Icons sind als spätere Erweiterung denkbar.")
    y += mm(6)

    y = draw_h2(d, y, "Brainy bleibt dabei")
    y = draw_para(d, y, "Anders als bei AT/ADHS behält das FS-Deck Brainy als durchgängige "
                        "Coach-Figur – wie bei KD, für dieselbe Altersgruppe und zur "
                        "Wiedererkennbarkeit über die beiden Decks hinweg.")

    footer(d, "Methodik")
    return img

# ═══════════════════════════════════ GLOSSAR ═══════════════════════════════════
GLOSSAR = [
    ("FS-Deck", "Die 32 Karten dieses Decks – 30 als sprachlich vereinfachte Version von KD "
     "(gleiche Themen, eigene Bilder), plus 2 FS-eigene Karten zu Lernen und Kommunikation. "
     "Für Kinder mit Sprach- oder Lernschwierigkeiten."),
    ("Leichte Sprache", "Eine Sprachform mit kurzen Sätzen, einfachen Wörtern und klarem Aufbau, "
     "die Texte leichter verständlich macht. Grundlage für die Sprachvereinfachung in diesem Deck."),
    ("Brainy", "Die durchgängige Coach-Figur aus dem KD-Deck – ein freundlicher, wolkenförmiger "
     "Gehirn-Charakter, der auch im FS-Deck in jedem Bild dabei ist."),
    ("Kind-Barometer", "Das 5-Zustände-System (Grün/Gelb/Orange/Rot/Grau) aus KD, im FS-Deck auf "
     "FS-01 direkt genutzt."),
    ("INGRA", "Bezeichnung für die pädagogischen Fachkräfte des KLARTEXT-Systems (früher: "
     "Schulbegleiter:in). Begleitet die Nutzung der FS-Karten gemeinsam mit dem Kind."),
    ("kLAR-Modell", "Ein Vorgehen für akute Belastungsmomente, nur INGRA-seitig in der Anleitung "
     "erklärt, nicht auf den Karten selbst (wie bei KD)."),
]

def glossar_seite(begriffe, seiten_label, intro=None):
    img, d, y = new_page("BEGRIFFE AUS DEM FS-DECK", "Glossar")
    if intro:
        y = draw_para(d, y, intro, size=4.6, color=KT_MUTED)
        y += mm(8)

    for begriff, definition in begriffe:
        f_term = ImageFont.truetype(F_SERIF_BOLD, mm(6))
        d.text((MARGIN, y), begriff, font=f_term, fill=FS_TEXT)
        y += mm(9)
        y = draw_para(d, y, definition, size=4.4)
        y += mm(4)
        d.line((MARGIN, y, W - MARGIN, y), fill=FS_BORDER, width=mm(0.3))
        y += mm(7)

    footer(d, seiten_label)
    return img

# ═══════════════════════════════════ QUELLEN ═══════════════════════════════════
QUELLEN_VORGESCHLAGEN = [
    "Netzwerk Leichte Sprache e.V. (2022). Die Regeln für Leichte Sprache (Neuauflage). Berlin. "
    "— Grundlage für die Sprachregeln (kurze Sätze, aktiv statt passiv, Alltagswörter).",
    "Inclusion Europe (2009). Information for all: European standards for making information "
    "easy to read and understand. Brüssel. — Europäischer Referenzstandard für einfache Sprache.",
    "DIN SPEC 33429:2025-03. Empfehlungen für Deutsche Leichte Sprache. Berlin: DIN Media (im "
    "Auftrag des BMAS). — Aktuelle deutsche Norm, ergänzt die beiden älteren Standards.",
]

def quellen_seite():
    img, d, y = new_page("METHODISCHE GRUNDLAGE", "Quellen")
    y = draw_para(d, y, "Alle drei Quellen sind einzeln geprüft (26.07.2026), aber noch nicht im "
                        "KLARTEXT-Quellenregister bestätigt – „vorgeschlagen, bitte fachlich "
                        "gegenprüfen“. Die inhaltlichen Kartentexte selbst basieren auf den "
                        "bereits produktionsfertigen KD-Quellen (siehe KD-Deck-Anleitung).",
                  size=4.6, color=KT_MUTED)
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
        "fs_anleitung1": anleitung_seite1(),
        "fs_anleitung2": anleitung_seite2(),
        "fs_methodik": methodik_seite(),
        "fs_glossar1": glossar_seite(GLOSSAR[:3], "Glossar · 1/2",
            intro="Kurz erklärt: Begriffe, die auf den Karten oder in dieser Anleitung vorkommen "
                  "und nicht selbsterklärend sind."),
        "fs_glossar2": glossar_seite(GLOSSAR[3:], "Glossar · 2/2"),
        "fs_quellen": quellen_seite(),
    }
    for name, img in pages.items():
        img.save(f"/sessions/kind-beautiful-ptolemy/mnt/outputs/booklet_{name}.png")
        print(name, "ok")
