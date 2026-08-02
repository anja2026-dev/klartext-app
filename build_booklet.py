#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Anleitung, Glossar, Quellen fürs JD-Deck – als A4-Seiten im bestehenden Look (siehe build_pdf.py Cover)."""
from PIL import Image, ImageDraw, ImageFont
Image.init()

DPI = 300
MM = DPI / 25.4
def mm(v): return int(round(v * MM))

JD = (47, 107, 110)
JD_LIGHT = (234, 243, 243)
JD_BORDER = (195, 220, 220)
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
    # Titelschrift automatisch verkleinern, bis sie in die Breite passt
    size = 11.0
    f_titel = ImageFont.truetype(F_SERIF_BOLD, mm(size))
    while d.textlength(titel, font=f_titel) > CONTENT_W and size > 6:
        size -= 0.5
        f_titel = ImageFont.truetype(F_SERIF_BOLD, mm(size))
    lines = wrap(d, titel, f_titel, CONTENT_W)
    kopf_h = mm(24) + len(lines) * mm(size * 1.35)
    d.rectangle((0, 0, W, kopf_h), fill=JD)
    d.text((MARGIN, mm(10)), kicker, font=f_kicker, fill=(200, 225, 220))
    ty = mm(17)
    for ln in lines:
        d.text((MARGIN, ty), ln, font=f_titel, fill=(255, 255, 255))
        ty += mm(size * 1.35)
    return img, d, kopf_h + mm(14)

def footer(d, page_label):
    f = ImageFont.truetype(F_SANS_REG, mm(4))
    d.text((MARGIN, H - mm(14)), "KLARTEXT-Mentoring · JD-Deck · © 2026 Anja Jolk", font=f, fill=KT_MUTED)
    w = d.textlength(page_label, font=f)
    d.text((W - MARGIN - w, H - mm(14)), page_label, font=f, fill=KT_MUTED)

def draw_h2(d, y, text):
    f = ImageFont.truetype(F_SERIF_BOLD, mm(6.5))
    d.text((MARGIN, y), text, font=f, fill=JD)
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
    fb = ImageFont.truetype(F_SANS_BOLD, mm(size))
    d.ellipse((MARGIN, y + mm(1.6), MARGIN + mm(1.6), y + mm(3.2)), fill=JD)
    lh = mm(size * 1.55)
    lines = wrap(d, text, f, CONTENT_W - mm(7))
    for i, ln in enumerate(lines):
        d.text((MARGIN + mm(6), y), ln, font=f, fill=KT_INK)
        y += lh
    return y + mm(1.5)

def draw_numbered(d, y, num, titel, text, size=4.8):
    f_num = ImageFont.truetype(F_SERIF_BOLD, mm(7))
    d.ellipse((MARGIN, y, MARGIN + mm(9), y + mm(9)), fill=JD)
    d.text((MARGIN + mm(4.5), y + mm(4.5)), str(num), font=f_num, anchor="mm", fill=(255, 255, 255))
    f_titel = ImageFont.truetype(F_SANS_BOLD, mm(5.2))
    d.text((MARGIN + mm(13), y + mm(0.5)), titel, font=f_titel, fill=JD)
    f_text = ImageFont.truetype(F_SANS_REG, mm(size))
    ty = y + mm(7)
    lh = mm(size * 1.55)
    for ln in wrap(d, text, f_text, CONTENT_W - mm(13)):
        d.text((MARGIN + mm(13), ty), ln, font=f_text, fill=KT_INK)
        ty += lh
    return max(ty, y + mm(11)) + mm(4)

# ═══════════════════════════════════ ANLEITUNG Seite 1 ═══════════════════════════════════
def anleitung_seite1():
    img, d, y = new_page("GEBRAUCHSANWEISUNG", "Anleitung: So funktioniert das JD-Deck")

    y = draw_h2(d, y, "Was ist das JD-Deck?")
    y = draw_para(d, y, "Das JD-Deck enthält 52 Coaching-Impulskarten für Jugendliche im weiterführenden "
                        "Schulalter. Jede Karte greift ein Thema auf, mit dem Jugendliche im Alltag häufig "
                        "ringen – von Selbstwert über Zukunftsdruck bis zu digitaler Balance. Die Karten sind "
                        "kein Test und keine Diagnostik, sondern ein Gesprächsanlass: ein Bild, ein Titel und "
                        "zwei offene Fragen, die einen Raum zum Nachdenken öffnen.")
    y += mm(6)

    y = draw_h2(d, y, "Für wen ist es gedacht?")
    y = draw_para(d, y, "In erster Linie für INGRA (Schulbegleitung) im direkten Kontakt mit Jugendlichen. "
                        "Genauso einsetzbar für Eltern, Lehrkräfte und Referent:innen – einzeln oder in kleinen "
                        "Gruppen, etwa im Rahmen von Workshops.")
    y += mm(8)

    y = draw_h2(d, y, "In drei Schritten")
    y += mm(2)
    y = draw_numbered(d, y, 1, "Karte auswählen",
        "Passt ein Thema gerade zur Situation? Die dreizehn Themenblöcke (siehe Rückseite dieser Seite) "
        "helfen bei der Auswahl.")
    y = draw_numbered(d, y, 2, "Vorderseite zeigen",
        "Bild und Titel wirken lassen, bevor gesprochen wird. Kein Erklären, kein Vorwegnehmen.")
    y = draw_numbered(d, y, 3, "Rückseite nutzen",
        "Anleitung lesen, eine der beiden Impulsfragen stellen, dem Gespräch folgen statt es zu lenken. "
        "Es muss nicht immer beide Fragen geben – eine reicht oft.")

    footer(d, "Anleitung · 1/2")
    return img

def anleitung_seite2():
    img, d, y = new_page("GEBRAUCHSANWEISUNG", "Haltung, Grenzen & praktische Tipps")

    y = draw_h2(d, y, "Haltung")
    y = draw_para(d, y, "Die Karten funktionieren nur mit einer bestimmten Grundhaltung: nicht bewerten, "
                        "nicht korrigieren, nicht sofort lösen wollen. Die Fragen sind offen formuliert – es "
                        "gibt keine richtige Antwort. Wenn eine Karte nicht passt oder der oder die "
                        "Jugendliche nicht möchte: die Karte weglegen, kein Druck aufbauen.")
    y += mm(8)

    box_y = y
    warn_text = ("Das JD-Deck ersetzt keine Diagnostik, keine Therapie und keine akute "
                 "Krisenintervention. Bei Anzeichen von Selbstgefährdung, akuter psychischer Krise "
                 "oder Gewalt: Karte weglegen und eine Fachperson einbeziehen – schulpsychologischer "
                 "Dienst, Beratungsstelle oder Kinder- und Jugendpsychiatrie. Die Karten sind für "
                 "ruhige, reflektierende Momente gedacht, nicht für akute Situationen.")
    f_warn_text = ImageFont.truetype(F_SANS_REG, mm(4.6))
    warn_lines = wrap(d, warn_text, f_warn_text, CONTENT_W - mm(16))
    line_h = mm(4.6 * 1.55)
    box_h = mm(15) + len(warn_lines) * line_h + mm(6)
    d.rounded_rectangle((MARGIN, box_y, W - MARGIN, box_y + box_h), radius=mm(3),
                         fill=(253, 245, 245), outline=(210, 160, 160), width=mm(0.4))
    f_warn_l = ImageFont.truetype(F_SANS_BOLD, mm(5.5))
    d.text((MARGIN + mm(8), box_y + mm(7)), "GRENZEN – WICHTIG", font=f_warn_l, fill=(160, 60, 60))
    wy = box_y + mm(15)
    for ln in warn_lines:
        d.text((MARGIN + mm(8), wy), ln, font=f_warn_text, fill=KT_INK)
        wy += line_h
    y = box_y + box_h + mm(10)

    y = draw_h2(d, y, "Praktische Tipps")
    y = draw_bullet(d, y, "Ruhiger Ort, ungestörte Zeit – keine Karte zwischen Tür und Angel.")
    y = draw_bullet(d, y, "Freiwillige Teilnahme: kein Zwang, eine Karte zu bearbeiten.")
    y = draw_bullet(d, y, "Kein Zeitdruck – eine Karte darf auch nur kurz angeschaut und dann "
                          "liegen gelassen werden.")
    y = draw_bullet(d, y, "Jede Rückseite enthält einen kurzen „Tipp für die INGRA“ mit Hinweisen "
                          "zur passenden Einsatzsituation – der lohnt sich vor dem Gespräch zu lesen.")

    footer(d, "Anleitung · 2/2")
    return img

# ═══════════════════════════════════ GLOSSAR ═══════════════════════════════════
GLOSSAR = [
    ("Care-Aufgaben", "Sorge- und Verantwortungsaufgaben für andere Familienmitglieder, zum Beispiel "
     "jüngere Geschwister, die über altersgerechte Mithilfe hinausgehen. Bei Jugendlichen häufig "
     "unsichtbar, weil sie zu Hause selbstverständlich wirken."),
    ("Impulsfrage", "Eine offen formulierte Frage ohne vorgegebene richtige Antwort. Ziel ist nicht die "
     "schnelle Lösung, sondern das Öffnen eines Gedankens. Methodisch verwandt mit der lösungsorientierten "
     "und systemischen Fragetechnik (siehe Quellen)."),
    ("INGRA", "Bezeichnung für die pädagogischen Fachkräfte des KLARTEXT-Systems (früher: "
     "Schulbegleiter:in). INGRA begleitet Jugendliche im Schulalltag – auf Grundlage des Hilfeplans und "
     "im Rahmen der Eingliederungshilfe."),
    ("Patchwork-Familie", "Familienform, in der mindestens ein Elternteil Kinder aus einer früheren "
     "Beziehung mit in eine neue Partnerschaft bringt. Stiefgeschwister und neue Bezugspersonen gehören "
     "zur neuen Familienkonstellation."),
    ("Systemisches Coaching", "Beratungsansatz, der Menschen nicht isoliert, sondern in ihren Beziehungen "
     "und Kontexten betrachtet. Fragt nicht „was ist falsch“, sondern „was würde helfen“ – "
     "lösungsorientiert statt problemorientiert."),
    ("Wechselmodell", "Betreuungsform nach Trennung der Eltern, bei der die Jugendlichen zu etwa gleichen "
     "Teilen bei beiden Elternteilen leben – im Unterschied zum Residenzmodell mit einem hauptsächlichen "
     "Wohnort."),
]

def glossar_seite(begriffe, seiten_label, intro=None):
    img, d, y = new_page("BEGRIFFE AUS DEM JD-DECK", "Glossar")
    if intro:
        y = draw_para(d, y, intro, size=4.6, color=KT_MUTED)
        y += mm(8)

    for begriff, definition in begriffe:
        f_term = ImageFont.truetype(F_SERIF_BOLD, mm(6))
        d.text((MARGIN, y), begriff, font=f_term, fill=JD)
        y += mm(9)
        y = draw_para(d, y, definition, size=4.6)
        y += mm(4)
        d.line((MARGIN, y, W - MARGIN, y), fill=JD_BORDER, width=mm(0.3))
        y += mm(8)

    footer(d, seiten_label)
    return img

# ═══════════════════════════════════ QUELLEN ═══════════════════════════════════
QUELLEN_BESTAETIGT = [
    "Schulz von Thun, F. (1981). Miteinander reden 1: Störungen und Klärungen. Rowohlt.",
    "Rosenberg, M. B. (2003). Nonviolent communication: A language of life (2nd ed.). PuddleDancer Press.",
    "Satir, V. (1990). Kommunikation, Selbstwert, Kongruenz: Konzepte und Perspektiven "
    "familientherapeutischer Praxis. Junfermann.",
    "Watzlawick, P., Beavin, J. H., & Jackson, D. D. (1967). Pragmatics of human communication: A study "
    "of interactional patterns, pathologies and paradoxes. Norton.",
]
QUELLEN_VORSCHLAG = [
    "de Shazer, S. (1988). Clues: Investigating solutions in brief therapy. Norton.",
    "Selvini Palazzoli, M., Boscolo, L., Cecchin, G., & Prata, G. (1980). Hypothesizing–circular "
    "questioning–neutrality: Three guidelines for the conductor of the session. Family Process, 19(1), 3–12.",
    "von Schlippe, A., & Schweitzer, J. (2012). Lehrbuch der systemischen Therapie und Beratung I: Das "
    "Grundlagenwissen (11. Aufl.). Vandenhoeck & Ruprecht.",
]
QUELLEN_EINORDNUNG = [
    "Dweck, C. S. (2006). Mindset: The new psychology of success. Random House.",
    "Fröhlich-Gildhoff, K., & Rönnau-Böse, M. (2022). Resilienz (6. Aufl.). Ernst Reinhardt/UTB.",
]

def quellen_seite1():
    img, d, y = new_page("METHODISCHE GRUNDLAGE", "Quellen")
    y = draw_para(d, y, "Die Impulsfragen der JD-Karten folgen der offenen, nicht wertenden Fragetechnik "
                        "systemischer und lösungsorientierter Beratung.", size=4.6, color=KT_MUTED)
    y += mm(9)

    y = draw_h2(d, y, "Aus dem KLARTEXT-Quellenregister")
    f_q = ImageFont.truetype(F_SANS_REG, mm(4.6))
    for q in QUELLEN_BESTAETIGT:
        for ln in wrap(d, q, f_q, CONTENT_W - mm(6)):
            d.text((MARGIN + mm(6), y), ln, font=f_q, fill=KT_INK)
            y += mm(7.2)
        y += mm(2)
    y += mm(6)

    y = draw_h2(d, y, "Ergänzend vorgeschlagen (bitte gegenprüfen)")
    y = draw_para(d, y, "Diese drei Quellen begründen die zirkuläre und lösungsorientierte Fragetechnik "
                        "direkt, sind aber noch nicht im KLARTEXT-Quellenregister – vor Veröffentlichung "
                        "bitte einmal selbst verifizieren.", size=4.2, color=GOLD)
    y += mm(4)
    for q in QUELLEN_VORSCHLAG:
        for ln in wrap(d, q, f_q, CONTENT_W - mm(6)):
            d.text((MARGIN + mm(6), y), ln, font=f_q, fill=KT_INK)
            y += mm(7.2)
        y += mm(2)

    footer(d, "Quellen · 1/2")
    return img

def quellen_seite2():
    img, d, y = new_page("METHODISCHE GRUNDLAGE", "Ergänzende theoretische Einordnung")
    y = draw_para(d, y, "Diese Karten wurden nicht anhand dieser Modelle entwickelt – die Modelle passen "
                        "aber inhaltlich zu einzelnen Karten und können die fachliche Einordnung vertiefen, "
                        "wenn gewünscht.", size=4.6, color=KT_MUTED)
    y += mm(9)
    f_q = ImageFont.truetype(F_SANS_REG, mm(4.6))
    for q in QUELLEN_EINORDNUNG:
        for ln in wrap(d, q, f_q, CONTENT_W - mm(6)):
            d.text((MARGIN + mm(6), y), ln, font=f_q, fill=KT_INK)
            y += mm(7.2)
        y += mm(2)
    y += mm(6)

    y = draw_h2(d, y, "Beispielhafte Passung")
    y = draw_bullet(d, y, "JD-07 (Angst vorm Scheitern) – Growth Mindset: Scheitern als Lernprozess statt "
                          "als feste Eigenschaft.")
    y = draw_bullet(d, y, "JD-04 (Ein schlechter Tag ist kein schlechtes Ich) – Resilienz: Trennung von "
                          "Ereignis und Identität.")
    y = draw_bullet(d, y, "JD-03 (Meine Stärken sehen) – Resilienz: Ressourcenorientierung als "
                          "Schutzfaktor.")

    footer(d, "Quellen · 2/2")
    return img

if __name__ == "__main__":
    pages = {
        "anleitung1": anleitung_seite1(),
        "anleitung2": anleitung_seite2(),
        "glossar1": glossar_seite(GLOSSAR[:3], "Glossar · 1/2",
            intro="Kurz erklärt: Begriffe, die auf den Karten oder in dieser Anleitung vorkommen "
                  "und nicht selbsterklärend sind."),
        "glossar2": glossar_seite(GLOSSAR[3:], "Glossar · 2/2"),
        "quellen1": quellen_seite1(),
        "quellen2": quellen_seite2(),
    }
    for name, img in pages.items():
        img.save(f"/sessions/kind-beautiful-ptolemy/mnt/outputs/booklet_{name}.png")
        print(name, "ok")
