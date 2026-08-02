#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Anleitung, Methodik, Glossar, Quellen fürs TR-Deck – adaptiert von build_booklet_lk.py.
TR-spezifisch: Zwei Nutzungsarten sind "eigene Vorbereitung/Reflexion" und "Live-Griffkarte im
Training" (statt "allein"/"mit Begleitung" bei EL/LK). Kein Barometer/kLAR-Modell. Inhalt basiert
auf dem bestehenden KLARTEXT_Trainerhandbuch.html (Knowles 1980, Kolb 1984, Tuckman 1965 – noch
nicht im Quellenregister bestätigt; Hattie 2009 – bereits bestätigt)."""
from PIL import Image, ImageDraw, ImageFont
Image.init()

DPI = 300
MM = DPI / 25.4
def mm(v): return int(round(v * MM))

TR = (62, 92, 118)          # #3E5C76
TR_LIGHT = (233, 238, 242)
TR_BORDER = (185, 199, 209)
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
    d.rectangle((0, 0, W, kopf_h), fill=TR)
    d.text((MARGIN, mm(10)), kicker, font=f_kicker, fill=(226, 232, 237))
    ty = mm(17)
    for ln in lines:
        d.text((MARGIN, ty), ln, font=f_titel, fill=(255, 255, 255))
        ty += mm(size * 1.35)
    return img, d, kopf_h + mm(14)

def footer(d, page_label):
    f = ImageFont.truetype(F_SANS_REG, mm(4))
    d.text((MARGIN, H - mm(14)), "KLARTEXT-Mentoring · TR-Deck · © 2026 Anja Jolk", font=f, fill=KT_MUTED)
    w = d.textlength(page_label, font=f)
    d.text((W - MARGIN - w, H - mm(14)), page_label, font=f, fill=KT_MUTED)

def draw_h2(d, y, text):
    f = ImageFont.truetype(F_SERIF_BOLD, mm(6.5))
    d.text((MARGIN, y), text, font=f, fill=TR)
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
    d.ellipse((MARGIN, y + mm(1.6), MARGIN + mm(1.6), y + mm(3.2)), fill=TR)
    lh = mm(size * 1.55)
    lines = wrap(d, text, f, CONTENT_W - mm(7))
    for ln in lines:
        d.text((MARGIN + mm(6), y), ln, font=f, fill=KT_INK)
        y += lh
    return y + mm(1.5)

def draw_numbered(d, y, num, titel, text, size=4.8):
    f_num = ImageFont.truetype(F_SERIF_BOLD, mm(7))
    d.ellipse((MARGIN, y, MARGIN + mm(9), y + mm(9)), fill=TR)
    d.text((MARGIN + mm(4.5), y + mm(4.5)), str(num), font=f_num, anchor="mm", fill=(255, 255, 255))
    f_titel = ImageFont.truetype(F_SANS_BOLD, mm(5.2))
    d.text((MARGIN + mm(13), y + mm(0.5)), titel, font=f_titel, fill=TR)
    f_text = ImageFont.truetype(F_SANS_REG, mm(size))
    ty = y + mm(7)
    lh = mm(size * 1.55)
    for ln in wrap(d, text, f_text, CONTENT_W - mm(13)):
        d.text((MARGIN + mm(13), ty), ln, font=f_text, fill=KT_INK)
        ty += lh
    return max(ty, y + mm(11)) + mm(4)

# ═══════════════════════════════════ ANLEITUNG ═══════════════════════════════════
def anleitung_seite1():
    img, d, y = new_page("GEBRAUCHSANWEISUNG", "Anleitung: So funktioniert das TR-Deck")

    y = draw_h2(d, y, "Was ist das TR-Deck?")
    y = draw_para(d, y, "Das TR-Deck richtet sich an Trainer:innen, die KLARTEXT-Schulungen für INGRAs/"
                        "TK-Kolleg:innen durchführen. Anders als EL/LK (Reflexion über die eigene Eltern- "
                        "oder Lehrkraft-Rolle) geht es hier um die eigene Trainer-Rolle: Haltung, Didaktik, "
                        "Umgang mit der Gruppe. Der Großteil stammt aus dem bestehenden Trainerhandbuch, "
                        "ergänzt um einen neunten Block zur modernen Fortbildungslandschaft – neun "
                        "Themenblöcke, 33 Karten.")
    y += mm(6)

    y = draw_h2(d, y, "Für wen ist es gedacht?")
    y = draw_para(d, y, "Für angehende und erfahrene KLARTEXT-Trainer:innen. Die Karten funktionieren "
                        "sowohl zur eigenen Vorbereitung vor einer Schulung als auch als Griffkarte "
                        "während einer laufenden Schulung (siehe „Zwei Nutzungsarten“, nächste Seite).")
    y += mm(8)

    y = draw_h2(d, y, "In drei Schritten")
    y += mm(2)
    y = draw_numbered(d, y, 1, "Karte auswählen",
        "Passt ein Thema gerade zur eigenen Vorbereitung oder zur aktuellen Situation im Training? Die "
        "neun Themenblöcke (Rolle & Haltung, Erwachsenenlernen, Gruppendynamik, Vorbereitung & Logistik, "
        "Methodenkoffer, Schwierige Situationen, Feedback, Nachbereitung, Moderne Fortbildungslandschaft) "
        "helfen bei der Auswahl.")
    y = draw_numbered(d, y, 2, "Anleitung und Fragen lesen",
        "Die Anleitung zeigt, wofür die Karte gedacht ist. Die beiden Impulsfragen müssen nicht beide "
        "beantwortet werden – eine reicht oft.")
    y = draw_numbered(d, y, 3, "„Tipp für dich“ nutzen",
        "Ein kurzer, direkt anwendbarer Gedanke auf jeder Rückseite – zum Mitnehmen in die nächste "
        "Schulung.")

    footer(d, "Anleitung · 1/2")
    return img

def anleitung_seite2():
    img, d, y = new_page("GEBRAUCHSANWEISUNG", "Zwei Nutzungsarten & Grenzen")

    y = draw_h2(d, y, "Zwei Nutzungsarten – beides ist vorgesehen")
    y = draw_numbered(d, y, 1, "Eigene Vorbereitung/Reflexion",
        "Vor einer Schulung durch die Karten blättern, die zur eigenen Weiterentwicklung passen – z. B. "
        "Block „Schwierige Situationen“ vor einer Gruppe, die man noch nicht kennt.")
    y = draw_numbered(d, y, 2, "Live-Griffkarte im Training",
        "Vor allem Block „Methodenkoffer“ und „Schwierige Situationen“ sind so konkret formuliert, dass "
        "die Karte während der laufenden Schulung als Spickzettel gezogen werden kann.")
    y += mm(4)

    box_y = y
    warn_text = ("Das TR-Deck ersetzt keine Trainer-Ausbildung, keine Supervision und kein Curriculum. "
                 "Bei grundsätzlicher Unsicherheit über die eigene Trainer-Rolle: KLARTEXT_Trainer_"
                 "Ausbildung.html und die Moderationsleitfäden (1-Tag/2-Tage/Kurzeinweisung) bleiben die "
                 "vollständige Grundlage – die Karten sind eine Verdichtung daraus, kein Ersatz dafür.")
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
    y = draw_bullet(d, y, "Vor jeder Schulung 2–3 passende Karten herauslegen statt das ganze Deck "
                          "mitzunehmen.")
    y = draw_bullet(d, y, "Die Methodenkoffer-Karten laminiert oder als Kopie griffbereit halten – sie "
                          "sind für den Live-Einsatz gedacht.")
    y = draw_bullet(d, y, "Nach der Schulung kurz notieren, welche Karte geholfen hat – das erleichtert "
                          "die Auswahl beim nächsten Mal.")

    footer(d, "Anleitung · 2/2")
    return img

# ═══════════════════════════════════ METHODIK ═══════════════════════════════════
def methodik_seite():
    img, d, y = new_page("HINTERGRUND", "Warum „Tipp für dich“ und eine dritte Frage?")
    y = draw_para(d, y, "Wie bei EL/LK richtet sich die Hinweisbox direkt an die lesende Person selbst – "
                        "die Trainer:in ist hier zugleich Zielperson und Nutzer:in der Karte.",
                  size=4.6, color=KT_MUTED)
    y += mm(8)

    y = draw_h2(d, y, "Woher der Inhalt stammt")
    y = draw_para(d, y, "29 der 33 Karten sind keine neu erfundenen Inhalte, sondern eine Verdichtung des "
                        "bestehenden KLARTEXT_Trainerhandbuch.html (acht Kapitel: Rolle & Haltung, Wie "
                        "Erwachsene lernen, Gruppendynamik, Vorbereitung & Logistik, Methodenkoffer, "
                        "Schwierige Situationen, Feedback, Nachbereitung & Qualität) in Kartenform. Ein "
                        "neunter Block „Moderne Fortbildungslandschaft“ (TR-30–33) wurde am 30.07.2026 "
                        "ergänzt – Online-/Hybrid-Didaktik, institutionelle Skepsis der Träger, "
                        "Trainer-Self-Care und Diversität in der Erwachsenengruppe, alle mit eigenen "
                        "Quellen belegt (siehe Quellen-Seite).")
    y += mm(8)

    y = draw_h2(d, y, "Die dritte Frage")
    y = draw_para(d, y, "Wie bei EL/LK ergänzt ein Teil der TR-Karten zu den zwei Impulsfragen eine dritte, "
                        "optisch abgesetzte Frage aus der systemischen Beratung: eine Skalierungsfrage, "
                        "eine zirkuläre Frage oder eine Handlungsfrage (siehe Glossar). Nicht jede Karte "
                        "bekommt eine dritte Frage – nur dort, wo sie inhaltlich wirklich etwas ergänzt.")
    y += mm(6)

    y = draw_h2(d, y, "Kein Barometer, kein kLAR-Modell im TR-Deck")
    y = draw_para(d, y, "Barometer und kLAR-Modell (siehe JD-/KD-Deck) sind Werkzeuge für die Fachkraft, "
                        "um ein akut angespanntes Kind zu ko-regulieren – für die Reflexion der eigenen "
                        "Trainer-Rolle nicht einschlägig, deshalb bewusst nicht ins TR-Deck übernommen.")
    y += mm(4)

    y = draw_para(d, y, "Hinweis zur Kartenzahl: Ursprünglich waren 40–50 Karten angedacht. Tatsächlich "
                        "tragfähig mit echtem, nicht künstlich gestrecktem Inhalt aus dem Trainerhandbuch "
                        "waren 29 Karten. Block 9 (TR-30–33, 30.07.2026) ergänzt vier Themen, die im "
                        "bestehenden Handbuch fehlten, aber echte Lücken in der modernen "
                        "Fortbildungslandschaft schließen – damit jetzt 33 Karten. Eine weitere Erweiterung "
                        "aus den Moderationsleitfäden (1-Tag/2-Tage/Kurzeinweisung) bleibt möglich, wurde "
                        "aber bewusst nicht vorgenommen, um den Einzelkarteninhalt nicht zu verdünnen.",
                  size=4.2, color=GOLD)

    footer(d, "Methodik")
    return img

# ═══════════════════════════════════ GLOSSAR ═══════════════════════════════════
GLOSSAR = [
    ("TR-Deck", "Die 33 Karten für Trainer:innen, in neun Themenblöcken gegliedert – von der eigenen "
     "Rolle bis zur modernen Fortbildungslandschaft. 29 Karten sind eine Verdichtung des bestehenden "
     "Trainerhandbuchs, 4 Karten (Block 9) wurden am 30.07.2026 ergänzt."),
    ("Methodenkoffer", "Block mit vier konkreten Trainingsmethoden (Rollenspiel mit Kartenwechsel, "
     "Karten-Sortieraufgabe, Fishbowl-Diskussion, Stiller Galeriegang), die auch live während einer "
     "Schulung als Griffkarte genutzt werden können."),
    ("Tipp für dich", "Die persönlich formulierte Hinweisbox auf jeder Kartenrückseite – direkt an die "
     "lesende Person selbst gerichtet."),
    ("INGRA", "Bezeichnung für die pädagogischen Fachkräfte des KLARTEXT-Systems (früher: "
     "Schulbegleiter:in). Die Zielgruppe, die TR-Trainer:innen in ihren Schulungen ausbilden."),
    ("Impulsfrage", "Eine offen formulierte Frage ohne vorgegebene richtige Antwort. Ziel ist nicht die "
     "schnelle Lösung, sondern das Öffnen eines Gedankens."),
    ("Systemisches Coaching", "Beratungsansatz, der eine Person nicht isoliert, sondern in ihren "
     "Beziehungen und Kontexten betrachtet. Fragt nicht „was ist falsch“, sondern „was würde helfen“."),
    ("Dritte Frage (Skalierung / Zirkulär / Handlung)", "Bei einem Teil der TR-Karten ergänzt eine "
     "optisch abgesetzte dritte Frage aus der systemischen Beratung die zwei Impulsfragen: eine "
     "Skalierungsfrage („Auf einer Skala von 1–10 …“, lösungsorientierte Kurztherapie), eine zirkuläre "
     "Frage (Perspektive einer anderen Person, Mailänder Modell) oder eine Handlungsfrage (kleiner "
     "nächster Schritt)."),
]

def glossar_seite(begriffe, seiten_label, intro=None):
    img, d, y = new_page("BEGRIFFE AUS DEM TR-DECK", "Glossar")
    if intro:
        y = draw_para(d, y, intro, size=4.6, color=KT_MUTED)
        y += mm(8)

    for begriff, definition in begriffe:
        f_term = ImageFont.truetype(F_SERIF_BOLD, mm(6))
        d.text((MARGIN, y), begriff, font=f_term, fill=TR)
        y += mm(9)
        y = draw_para(d, y, definition, size=4.4)
        y += mm(4)
        d.line((MARGIN, y, W - MARGIN, y), fill=TR_BORDER, width=mm(0.3))
        y += mm(7)

    footer(d, seiten_label)
    return img

# ═══════════════════════════════════ QUELLEN ═══════════════════════════════════
QUELLEN_BESTAETIGT = [
    "Hattie, J. (2009). Visible learning: A synthesis of over 800 meta-analyses relating to "
    "achievement. Routledge.",
    "Sonnentag, S., & Fritz, C. (2007). The Recovery Experience Questionnaire: Development and "
    "validation of a measure for assessing recuperation and unwinding from work. Journal of "
    "Occupational Health Psychology, 12(3), 204–221. — bereits im KLARTEXT-Quellenregister bestätigt "
    "(LK-Deck, 30.07.2026), hier für TR-32 wiederverwendet.",
]

QUELLEN_VORGESCHLAGEN = [
    "Knowles, M. S. (1980). The modern practice of adult education: From pedagogy to andragogy. "
    "Cambridge Adult Education. — Grundlage von Block B (Wie Erwachsene lernen).",
    "Kolb, D. A. (1984). Experiential learning: Experience as the source of learning and "
    "development. Prentice-Hall. — Grundlage des Lernzyklus (TR-07).",
    "Tuckman, B. W. (1965). Developmental sequence in small groups. Psychological Bulletin, 63(6), "
    "384–399. — Grundlage von Block C (Gruppendynamik, Forming/Storming/Norming/Performing).",
    "Salmon, G. (2000). E-moderating: The key to teaching and learning online. Kogan Page. — "
    "Grundlage TR-30 (Online- & Hybrid-Didaktik).",
    "Rogers, E. M. (2003). Diffusion of innovations (5th ed.). Free Press. — Grundlage TR-31 "
    "(institutionelle Skepsis der Träger).",
    "Steiner, A. & Maillinger, C. (2025). Heterogenität in der Erwachsenenbildung – Anregungen für "
    "ein didaktisches Konzept und Kompetenzprofil. bwp@ Spezial PH-AT3. — Grundlage TR-33 (Diversität "
    "in der Erwachsenengruppe).",
]

def quellen_seite1():
    img, d, y = new_page("METHODISCHE GRUNDLAGE", "Quellen · Bestätigt")
    y = draw_para(d, y, "Diese Quellen sind bereits im KLARTEXT-Quellenregister bestätigt.",
                  size=4.6, color=KT_MUTED)
    y += mm(9)

    f_q = ImageFont.truetype(F_SANS_REG, mm(4.6))
    for q in QUELLEN_BESTAETIGT:
        for ln in wrap(d, q, f_q, CONTENT_W - mm(6)):
            d.text((MARGIN + mm(6), y), ln, font=f_q, fill=KT_INK)
            y += mm(7.2)
        y += mm(2)

    footer(d, "Quellen · 1/3")
    return img

def quellen_seite1b():
    img, d, y = new_page("METHODISCHE GRUNDLAGE", "Quellen · Vorgeschlagen")
    y = draw_para(d, y, "Weitere Quellen – teils bereits im bestehenden Trainerhandbuch korrekt zitiert, "
                        "teils neu für Block 9 recherchiert, hier als „vorgeschlagen, bitte fachlich "
                        "gegenprüfen“ markiert, da noch nicht im Quellenregister selbst bestätigt:",
                  size=4.2, color=GOLD)
    y += mm(3)
    f_q = ImageFont.truetype(F_SANS_REG, mm(4.6))
    for q in QUELLEN_VORGESCHLAGEN:
        for ln in wrap(d, q, f_q, CONTENT_W - mm(6)):
            d.text((MARGIN + mm(6), y), ln, font=f_q, fill=KT_INK)
            y += mm(7.2)
        y += mm(2)

    footer(d, "Quellen · 2/3")
    return img

def quellen_seite2():
    img, d, y = new_page("METHODISCHE GRUNDLAGE", "Beispielhafte Passung")
    y = draw_bullet(d, y, "TR-04 / TR-05 / TR-06 (Wie Erwachsene lernen) – Knowles: Andragogik statt "
                          "Pädagogik, Erfahrungsbezug/Relevanzbedürfnis/Selbststeuerung als Grundprinzipien.")
    y = draw_bullet(d, y, "TR-07 (Lernzyklus) – Kolb: Erleben – Reflektieren – Verallgemeinern – Anwenden "
                          "als wiederkehrender Aufbau jeder Trainingseinheit.")
    y = draw_bullet(d, y, "TR-08 / TR-09 / TR-10 / TR-11 (Gruppendynamik) – Tuckman: Forming, Storming, "
                          "Norming, Performing als typische Entwicklungsphasen jeder Trainingsgruppe.")
    y = draw_bullet(d, y, "TR-24 / TR-25 / TR-26 (Feedback) – Hattie: konkretes, laufendes Feedback als "
                          "einer der stärksten Hebel für Lernerfolg.")
    y = draw_bullet(d, y, "TR-30 (Online- & Hybrid-Didaktik) – Salmon: Stufenmodell für Moderation und "
                          "Aktivierung im digitalen Lernraum.")
    y = draw_bullet(d, y, "TR-31 (Institutionelle Skepsis) – Rogers: Widerstand gegen Neuerungen als "
                          "normaler Teil jedes Diffusions-/Einführungsprozesses, nicht als persönliche "
                          "Ablehnung.")
    y = draw_bullet(d, y, "TR-32 (Trainer-Self-Care) – Sonnentag & Fritz: psychologische Distanzierung "
                          "und Erholung nach belastenden Arbeitsphasen.")
    y = draw_bullet(d, y, "TR-33 (Diversität in der Erwachsenengruppe) – Steiner & Maillinger: "
                          "Kompetenzprofil für Erwachsenenbildner:innen im Umgang mit heterogenen "
                          "Lerngruppen.")
    y += mm(6)
    y = draw_h2(d, y, "Zur dritten Frage")
    y = draw_para(d, y, "Skalierungs-, zirkuläre und Handlungsfragen sind bei einem Teil der TR-Karten "
                        "eingesetzt, passend zum jeweiligen Kartenthema gewählt (siehe Glossar: „Dritte "
                        "Frage“) – keine kartenweise Einzelauflistung hier, um die Seite nicht zu "
                        "überladen.")

    footer(d, "Quellen · 3/3")
    return img

if __name__ == "__main__":
    pages = {
        "tr_anleitung1": anleitung_seite1(),
        "tr_anleitung2": anleitung_seite2(),
        "tr_methodik": methodik_seite(),
        "tr_glossar1": glossar_seite(GLOSSAR[:4], "Glossar · 1/2",
            intro="Kurz erklärt: Begriffe, die auf den Karten oder in dieser Anleitung vorkommen und "
                  "nicht selbsterklärend sind."),
        "tr_glossar2": glossar_seite(GLOSSAR[4:], "Glossar · 2/2"),
        "tr_quellen1": quellen_seite1(),
        "tr_quellen1b": quellen_seite1b(),
        "tr_quellen2": quellen_seite2(),
    }
    for name, img in pages.items():
        img.save(f"/sessions/kind-beautiful-ptolemy/mnt/outputs/booklet_{name}.png")
        print(name, "ok")
