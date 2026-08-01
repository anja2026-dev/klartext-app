#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Anleitung, Methodik, Glossar, Quellen fürs ADHS-Deck. Fachprüfung durch externe ADHS-Fachperson
abgeschlossen (27.07.2026) – kein Entwurfs-Status mehr. Kind-facing wie JD/KD/AT: "Tipp für die
INGRA", KEINE dritte systemische Frage. Anders als AT: keine erzwungene wörtliche Sprache/
geschlossene Fragen, da ADHS primär Aufmerksamkeit/Impulskontrolle betrifft, nicht sprachliche
Verarbeitung im selben Sinn wie Autismus."""
from PIL import Image, ImageDraw, ImageFont
Image.init()

DPI = 300
MM = DPI / 25.4
def mm(v): return int(round(v * MM))

ADHS = (107, 127, 215)        # #6B7FD7
ADHS_LIGHT = (232, 234, 249)
ADHS_BORDER = (196, 203, 240)
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
    d.rectangle((0, 0, W, kopf_h), fill=ADHS)
    d.text((MARGIN, mm(10)), kicker, font=f_kicker, fill=(240, 241, 250))
    ty = mm(17)
    for ln in lines:
        d.text((MARGIN, ty), ln, font=f_titel, fill=(255, 255, 255))
        ty += mm(size * 1.35)
    return img, d, kopf_h + mm(14)

def footer(d, page_label):
    f = ImageFont.truetype(F_SANS_REG, mm(4))
    d.text((MARGIN, H - mm(14)), "KLARTEXT-Mentoring · ADHS-Deck · © 2026 Anja Jolk",
           font=f, fill=KT_MUTED)
    w = d.textlength(page_label, font=f)
    d.text((W - MARGIN - w, H - mm(14)), page_label, font=f, fill=KT_MUTED)

def draw_h2(d, y, text):
    f = ImageFont.truetype(F_SERIF_BOLD, mm(6.5))
    d.text((MARGIN, y), text, font=f, fill=ADHS)
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
    d.ellipse((MARGIN, y + mm(1.6), MARGIN + mm(1.6), y + mm(3.2)), fill=ADHS)
    lh = mm(size * 1.55)
    lines = wrap(d, text, f, CONTENT_W - mm(7))
    for ln in lines:
        d.text((MARGIN + mm(6), y), ln, font=f, fill=KT_INK)
        y += lh
    return y + mm(1.5)

def draw_numbered(d, y, num, titel, text, size=4.8):
    f_num = ImageFont.truetype(F_SERIF_BOLD, mm(7))
    d.ellipse((MARGIN, y, MARGIN + mm(9), y + mm(9)), fill=ADHS)
    d.text((MARGIN + mm(4.5), y + mm(4.5)), str(num), font=f_num, anchor="mm", fill=(255, 255, 255))
    f_titel = ImageFont.truetype(F_SANS_BOLD, mm(5.2))
    d.text((MARGIN + mm(13), y + mm(0.5)), titel, font=f_titel, fill=ADHS)
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
    img, d, y = new_page("GEBRAUCHSANWEISUNG", "Anleitung: So funktioniert das ADHS-Deck")

    y = draw_h2(d, y, "Was ist das ADHS-Deck?")
    y = draw_para(d, y, "Das ADHS-Deck ist eine Version der Content-Achse (wie JD/KD) für Kinder und "
                        "Jugendliche mit ADHS – dieselbe Grundhaltung (ressourcenorientiert, "
                        "entlastend statt bewertend), aber mit Themen, die für Aufmerksamkeit, "
                        "Impulsivität, Bewegungsdrang, Maskieren und Schule/Leistung besonders "
                        "relevant sind.")
    y += mm(6)

    y = draw_h2(d, y, "Für wen ist es gedacht?")
    y = draw_para(d, y, "Für Kinder und Jugendliche mit ADHS-Diagnose oder -Verdacht, gemeinsam mit "
                        "einer INGRA-Fachkraft oder einer anderen Begleitperson – die Anleitung auf "
                        "der Rückseite richtet sich an die begleitende Person, nicht an das Kind "
                        "direkt.")
    y += mm(8)

    y = draw_h2(d, y, "In drei Schritten")
    y += mm(2)
    y = draw_numbered(d, y, 1, "Karte auswählen",
        "Passend zur aktuellen Situation oder zum Thema, das gerade ansteht. Die sechs Themenblöcke "
        "(siehe Methodik-Seite) helfen bei der Auswahl.")
    y = draw_numbered(d, y, 2, "Anleitung lesen, dann Fragen stellen",
        "Beide Fragen sind offen formuliert. Es ist in Ordnung, wenn nur eine Frage beantwortet wird "
        "oder die Antwort sehr kurz ausfällt.")
    y = draw_numbered(d, y, 3, "„Tipp für die INGRA“ nutzen",
        "Ein kurzer, direkt umsetzbarer Hinweis auf jeder Rückseite – zur eigenen Vorbereitung, nicht "
        "zum Vorlesen.")

    footer(d, "Anleitung · 1/2")
    return img

def anleitung_seite2():
    img, d, y = new_page("GEBRAUCHSANWEISUNG", "Fachlich geprüft")

    y = draw_para(d, y, "Kartentexte, Bilder und Anleitung wurden von einer externen ADHS-Fachperson "
                        "(Kinder-/Jugendpsychiatrie bzw. entsprechend qualifizierte Fachkraft) "
                        "gegengelesen (Fachprüfung abgeschlossen). Das Deck ist damit für den "
                        "produktiven Einsatz mit Kindern freigegeben.",
                  size=4.8, color=KT_INK)
    y += mm(10)

    y = draw_h2(d, y, "Grundhaltung dieses Decks")
    y = draw_bullet(d, y, "Entlastend statt bewertend – ADHS-Verhalten wird neurobiologisch erklärt, "
                          "nicht als Charakter- oder Erziehungsfrage behandelt.")
    y = draw_bullet(d, y, "Ressourcenorientiert – mehrere Karten fragen gezielt nach bereits "
                          "funktionierenden Strategien statt nur nach Problemen.")
    y = draw_bullet(d, y, "Offene Fragen – anders als beim AT-Deck keine erzwungene wörtliche "
                          "Sprache oder geschlossenen Fragen nötig, da ADHS primär Aufmerksamkeit "
                          "und Impulskontrolle betrifft, nicht sprachliche Verarbeitung.")
    y = draw_bullet(d, y, "Masking wird explizit benannt (Block D) – gerade bei Mädchen oft "
                          "übersehen, weil die Anstrengung nach außen nicht sichtbar ist.")

    footer(d, "Anleitung · 2/2")
    return img

# ═══════════════════════════════════ METHODIK ═══════════════════════════════════
def methodik_seite():
    img, d, y = new_page("HINTERGRUND", "Sechs Themenblöcke, eine Haltung")
    y = draw_para(d, y, "24 Karten in sechs Blöcken à 4 Karten – Aufmerksamkeit & Konzentration, "
                        "Impulsivität & Handeln, Bewegungsdrang & innere Unruhe, Maskieren & "
                        "Erschöpfung, Schule & Leistung, Ich über mich.",
                  size=4.6, color=KT_MUTED)
    y += mm(8)

    y = draw_h2(d, y, "Warum keine dritte Frage wie bei EL/LK/TR?")
    y = draw_para(d, y, "Die Erwachsenen-Decks bekommen bewusst eine dritte, variierende Frage aus "
                        "der systemischen Beratung. Das ADHS-Deck folgt hier wie AT/JD/KD der "
                        "Content-Achse: Anleitung + 2 Impulsfragen + „Tipp für die INGRA“, keine "
                        "dritte Frage.")
    y += mm(8)

    y = draw_h2(d, y, "Kein GS/Sek-Split")
    y = draw_para(d, y, "Wie bei AT ein Deck über die gesamte Altersspanne – die Diagnose bleibt "
                        "gleich, nur die Ausprägung verschiebt sich graduell. Alters-Hinweise nur auf "
                        "Kartenebene, wo nötig (Konvention wie KD-12).")
    y += mm(6)

    y = draw_h2(d, y, "Kein Brainy im Bild")
    y = draw_para(d, y, "Da das ADHS-Deck auch ältere Jugendliche anspricht, wurde bewusst auf Brainy "
                        "als Bildfigur verzichtet (wie bei AT/JD/EL/LK/TR) – nur das K-Logo im "
                        "Kartenkopf, um nicht kindisch zu wirken.")

    footer(d, "Methodik")
    return img

# ═══════════════════════════════════ GLOSSAR ═══════════════════════════════════
GLOSSAR = [
    ("ADHS-Deck", "Die 24 Karten dieses Decks, in sechs Themenblöcken. Fachlich geprüft, "
     "einsatzbereit."),
    ("Masking / Camouflaging", "Das bewusste oder unbewusste Verbergen von ADHS-Symptomen, um nach "
     "außen „normal“ zu wirken – kostet Kraft, wird besonders bei Mädchen oft übersehen (Block D)."),
    ("Exekutive Funktionen", "Kognitive Steuerungsprozesse wie Arbeitsgedächtnis, Impulskontrolle und "
     "Planung – bei ADHS oft betroffen, Grundlage für Vergessen/Impulsivität-Themen."),
    ("INGRA", "Bezeichnung für die pädagogischen Fachkräfte des KLARTEXT-Systems (früher: "
     "Schulbegleiter:in). Begleitet die Nutzung der ADHS-Karten gemeinsam mit dem Kind."),
    ("Nachteilsausgleich", "Anpassung von Prüfungs-/Arbeitsbedingungen, um eine reale Hürde "
     "auszugleichen, nicht um einen Vorteil zu schaffen (siehe ADHS-20)."),
    ("Reframing", "Eine Situation oder ein Verhalten neu einordnen, ohne die Fakten zu ändern – z. B. "
     "„ADHS ist keine Charakterfrage“ (ADHS-21)."),
]

def glossar_seite(begriffe, seiten_label, intro=None):
    img, d, y = new_page("BEGRIFFE AUS DEM ADHS-DECK", "Glossar")
    if intro:
        y = draw_para(d, y, intro, size=4.6, color=KT_MUTED)
        y += mm(8)

    for begriff, definition in begriffe:
        f_term = ImageFont.truetype(F_SERIF_BOLD, mm(6))
        d.text((MARGIN, y), begriff, font=f_term, fill=ADHS)
        y += mm(9)
        y = draw_para(d, y, definition, size=4.4)
        y += mm(4)
        d.line((MARGIN, y, W - MARGIN, y), fill=ADHS_BORDER, width=mm(0.3))
        y += mm(7)

    footer(d, seiten_label)
    return img

# ═══════════════════════════════════ QUELLEN ═══════════════════════════════════
QUELLEN_VORGESCHLAGEN = [
    "Barkley, R. A. (2012). Executive Functions: What They Are, How They Work, and Why They "
    "Evolved. Guilford Press. — Grundlage für Arbeitsgedächtnis/Impulskontrolle-Themen (Block A, B).",
    "Shaw, P. et al. (2007). ADHD is characterized by a delay in cortical maturation. PNAS, 104, "
    "19649–19654. — Grundlage für „das Gehirn braucht länger, nicht weniger“ (Block F).",
    "McKinney, A. et al. (2024). Camouflaging in neurodivergent and neurotypical girls at the "
    "transition to adolescence and its relationship to mental health. JCPP Advances. — Studie zu "
    "Masking/Camouflaging bei Mädchen, Grundlage für Block D.",
    "Interdisziplinäre S3-Leitlinie ADHS (AWMF-Register-Nr. 028-045), Version 2.0, 2026 — betont "
    "funktionale Beeinträchtigung/Lebensqualität statt reiner Symptomzählung (Block E).",
    "Faraone, S. V. et al. (2021). The World Federation of ADHD International Consensus Statement: "
    "208 Evidence-based conclusions about the disorder. Neuroscience & Biobehavioral Reviews, 128, "
    "789–818. — internationales Konsenspapier, Grundlage für den neurobiologischen Rahmen (Block F).",
    "Heine, S. & Exner, C. (2021). Aufmerksamkeitsdefizit-/Hyperaktivitätsstörung (ADHS) im "
    "Erwachsenenalter. Zeitschrift für Neuropsychologie. — Übersicht zu Diagnostik/exekutiven "
    "Funktionen, ergänzt Barkley (Block A, B).",
]

def quellen_seite1():
    img, d, y = new_page("METHODISCHE GRUNDLAGE · 1/2", "Quellen")
    y = draw_para(d, y, "Alle sechs Quellen sind einzeln geprüft (26.07.2026), aber noch nicht im "
                        "KLARTEXT-Quellenregister bestätigt – „vorgeschlagen, bitte fachlich "
                        "gegenprüfen“.", size=4.6, color=KT_MUTED)
    y += mm(9)

    f_q = ImageFont.truetype(F_SANS_REG, mm(4.6))
    for q in QUELLEN_VORGESCHLAGEN[:3]:
        for ln in wrap(d, q, f_q, CONTENT_W - mm(6)):
            d.text((MARGIN + mm(6), y), ln, font=f_q, fill=KT_INK)
            y += mm(7.2)
        y += mm(3)

    footer(d, "Quellen · 1/2")
    return img

def quellen_seite2():
    img, d, y = new_page("METHODISCHE GRUNDLAGE · 2/2", "Quellen (Fortsetzung)")

    f_q = ImageFont.truetype(F_SANS_REG, mm(4.6))
    for q in QUELLEN_VORGESCHLAGEN[3:]:
        for ln in wrap(d, q, f_q, CONTENT_W - mm(6)):
            d.text((MARGIN + mm(6), y), ln, font=f_q, fill=KT_INK)
            y += mm(7.2)
        y += mm(3)
    y += mm(6)

    y = draw_h2(d, y, "Geprüft und nicht übernommen")
    y = draw_para(d, y, "Zwei ursprünglich vorgeschlagene Angaben („Wissenschaftlicher Konsensusbericht "
                        "2026“ zur Scaffolding-Hypothese, „ADHS Spezialambulanz / Golsari, A. 2026“) "
                        "ließen sich nicht als reguläre Publikation verifizieren und wurden nicht als "
                        "Quelle übernommen. Konkrete Medikamentennamen, digitale Therapeutika und "
                        "Behandlungsprotokolle fließen bewusst nicht in die Kartentexte ein – das sind "
                        "fachliche Behandlungsentscheidungen, keine Karteninhalte.", size=4.4)

    footer(d, "Quellen · 2/2")
    return img

if __name__ == "__main__":
    pages = {
        "adhs_anleitung1": anleitung_seite1(),
        "adhs_anleitung2": anleitung_seite2(),
        "adhs_methodik": methodik_seite(),
        "adhs_glossar1": glossar_seite(GLOSSAR[:3], "Glossar · 1/2",
            intro="Kurz erklärt: Begriffe, die auf den Karten oder in dieser Anleitung vorkommen und "
                  "nicht selbsterklärend sind."),
        "adhs_glossar2": glossar_seite(GLOSSAR[3:], "Glossar · 2/2"),
        "adhs_quellen1": quellen_seite1(),
        "adhs_quellen2": quellen_seite2(),
    }
    for name, img in pages.items():
        img.save(f"/sessions/kind-beautiful-ptolemy/mnt/outputs/booklet_{name}.png")
        print(name, "ok")
