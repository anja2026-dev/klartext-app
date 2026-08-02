#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Anleitung + Quellen fürs TK-Deck (Handlungskarten Teamkoordination) – adaptiert von build_booklet_lk.py.
Erstes Deck im neuen Handlungskarten-Format. Anleitung erklärt zusätzlich Brainy (TK begegnet Brainy
anders als INGRA) und die Tischwerkzeug-Markierung."""
from PIL import Image, ImageDraw, ImageFont
Image.init()

DPI = 300
MM = DPI / 25.4
def mm(v): return int(round(v * MM))

TK = (74, 20, 140)           # #4A148C
TK_LIGHT = (243, 229, 255)
TK_BORDER = (206, 169, 226)
KT_INK = (45, 45, 45)
KT_MUTED = (122, 112, 96)
KT_PAPER = (245, 240, 232)
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
    d.rectangle((0, 0, W, kopf_h), fill=TK)
    d.text((MARGIN, mm(10)), kicker, font=f_kicker, fill=(230, 210, 245))
    ty = mm(17)
    for ln in lines:
        d.text((MARGIN, ty), ln, font=f_titel, fill=(255, 255, 255))
        ty += mm(size * 1.35)
    return img, d, kopf_h + mm(14)

def footer(d, page_label):
    f = ImageFont.truetype(F_SANS_REG, mm(4))
    d.text((MARGIN, H - mm(14)), "KLARTEXT-Mentoring · TK-Handlungskarten · © 2026 Anja Jolk", font=f, fill=KT_MUTED)
    w = d.textlength(page_label, font=f)
    d.text((W - MARGIN - w, H - mm(14)), page_label, font=f, fill=KT_MUTED)

def draw_h2(d, y, text):
    f = ImageFont.truetype(F_SERIF_BOLD, mm(6.5))
    d.text((MARGIN, y), text, font=f, fill=TK)
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
    d.ellipse((MARGIN, y + mm(1.6), MARGIN + mm(1.6), y + mm(3.2)), fill=TK)
    lh = mm(size * 1.55)
    lines = wrap(d, text, f, CONTENT_W - mm(7))
    for ln in lines:
        d.text((MARGIN + mm(6), y), ln, font=f, fill=KT_INK)
        y += lh
    return y + mm(1.5)

def draw_numbered(d, y, num, titel, text, size=4.8):
    f_num = ImageFont.truetype(F_SERIF_BOLD, mm(7))
    d.ellipse((MARGIN, y, MARGIN + mm(9), y + mm(9)), fill=TK)
    d.text((MARGIN + mm(4.5), y + mm(4.5)), str(num), font=f_num, anchor="mm", fill=(255, 255, 255))
    f_titel = ImageFont.truetype(F_SANS_BOLD, mm(5.2))
    d.text((MARGIN + mm(13), y + mm(0.5)), titel, font=f_titel, fill=TK)
    f_text = ImageFont.truetype(F_SANS_REG, mm(size))
    ty = y + mm(7)
    lh = mm(size * 1.55)
    for ln in wrap(d, text, f_text, CONTENT_W - mm(13)):
        d.text((MARGIN + mm(13), ty), ln, font=f_text, fill=KT_INK)
        ty += lh
    return max(ty, y + mm(11)) + mm(4)

# ═══════════════════════════════════ ANLEITUNG ═══════════════════════════════════
def anleitung_seite1():
    img, d, y = new_page("GEBRAUCHSANWEISUNG", "Anleitung: So funktionieren die TK-Handlungskarten")

    y = draw_h2(d, y, "Was ist das TK-Deck?")
    y = draw_para(d, y, "19 Karten für die Teamkoordination/Trägerebene – aus der bereits bestehenden "
                        "digitalen TK-Handlungskarten-Galerie der App, jetzt zusätzlich als physisches "
                        "Deck. Anders als bei den Reflexionskarten (LK/EL) sind das Technik-Karten: "
                        'Situation, vier konkrete Schritte, eine Abgrenzungs-Box "Jetzt tun / Jetzt '
                        'nicht", eine Kurzquelle.')
    y += mm(6)

    y = draw_h2(d, y, "Drei Kategorien")
    y = draw_bullet(d, y, "Team & Koordination – Zusammenarbeit im INGRA-Team selbst.")
    y = draw_bullet(d, y, "Kind & Familie – Fallbezogene Themen: Hilfeplan, § 8a, Elternkontakt.")
    y = draw_bullet(d, y, "System & Schnittstellen – Qualitätssicherung, Schule, Selbstorganisation.")
    y += mm(4)

    y = draw_h2(d, y, "Die Tischwerkzeug-Markierung")
    y = draw_para(d, y, "Sechs Karten tragen zusätzlich ein kleines Zeichen: TISCHWERKZEUG. Das sind die "
                        "Karten, die sich für den gemeinsamen Einsatz in einer laufenden Besprechung "
                        "eignen – man legt sie in die Runde, statt nur nachzuschlagen (Fallbesprechung, "
                        "Teamentwicklung, Konflikt im Team, Abschlussgespräch INGRA, Meetingstruktur, "
                        "Feedback geben). Die übrigen 13 Karten sind für die Vorbereitung am Schreibtisch "
                        "gedacht.")

    footer(d, "Anleitung · 1/2")
    return img

def anleitung_seite2():
    img, d, y = new_page("GEBRAUCHSANWEISUNG", "Brainy im TK-Deck & Grenzen")

    y = draw_h2(d, y, "Wo ist Brainy?")
    y = draw_para(d, y, "Brainy ist die durchgängige Begleitfigur, der Kinder auf den anderen KLARTEXT-"
                        "Materialien begegnen (Kartendecks, App-Barometer, Geschichtenkarten). TK "
                        "arbeitet nicht täglich direkt am Kind – deshalb taucht Brainy hier bewusst "
                        "gezielter auf: klein in der Bildecke, nur auf den Karten mit direktem Fall-, "
                        "Kind- oder Beziehungsbezug (z. B. Hilfeplangespräch, § 8a, Elternkontakt, "
                        "Feedback geben). Auf den reinen Verwaltungskarten (z. B. Dokumentationsprüfung, "
                        "Zeitmanagement) erscheint Brainy nicht – dort geht es um Prozess und "
                        "Organisation, nicht um die Beziehung zum Kind. Wer Brainy von den anderen "
                        "KLARTEXT-Materialien kennt, erkennt die Marke wieder; wer TK-Karten zuerst in "
                        "die Hand bekommt, versteht mit dieser Erklärung, warum die Figur nicht auf jeder "
                        "Karte erscheint.")
    y += mm(6)

    box_y = y
    warn_text = ("Die TK-Handlungskarten ersetzen keine Rechtsberatung, keine Supervision und kein "
                 "Kinderschutzverfahren. Bei akuter Gefahr für ein Kind: sofort die Feuerwehrkarten in "
                 "der App nutzen und die schulinternen bzw. trägerinternen Kinderschutz-Vorgaben greifen "
                 "lassen. Die Karten sind für die alltägliche Team- und Fallkoordination gedacht, nicht "
                 "für akute Notlagen.")
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

    y = draw_h2(d, y, "Trägeroffen")
    y = draw_para(d, y, "Die TK-Handlungskarten sind bewusst neutral gehalten – unabhängig vom "
                        "jeweiligen Träger einsetzbar, konsistent mit der digitalen Fassung in der App.")

    footer(d, "Anleitung · 2/2")
    return img

# ═══════════════════════════════════ QUELLEN ═══════════════════════════════════
QUELLEN_BESTAETIGT = [
    "SGB VIII § 36 (Hilfeplan).",
    "SGB VIII § 8a (Schutzauftrag bei Kindeswohlgefährdung).",
    "DSGVO, Art. 5 Abs. 1 lit. c (Grundsatz der Datenminimierung).",
    "DIN EN ISO 9001:2015 – Qualitätsmanagement-Norm, in der Jugendhilfe verbreitet zur "
    "Trägerzertifizierung genutzt.",
    "Tuckman, B. W. (1965). Developmental sequence in small groups. Psychological Bulletin, 63(6), "
    "384–399.",
    "Doran, G. T. (1981). There's a S.M.A.R.T. way to write management's goals and objectives. "
    "Management Review, 70(11), 35–36.",
    "Maslach, C., & Jackson, S. E. (1981). The measurement of experienced burnout. Journal of "
    "Organizational Behavior, 2(2), 99–113.",
]

QUELLEN_VORGESCHLAGEN = [
    "Katzenbach, J. R., & Smith, D. K. (1993). The wisdom of teams. Harvard Business School Press. — "
    "Rollenklarheit-Konzept, TK-01.",
    "Schlee, J. (2019). Kollegiale Beratung und Supervision für pädagogische Berufe. Kohlhammer. — "
    "Kollegiale Fallberatung, TK-02.",
    "Glasl, F. Konfliktmanagement: Ein Handbuch für Führungskräfte, Beraterinnen und Berater. — "
    "9-Stufen-Eskalationsmodell, TK-08.",
    "Eisenhower-Matrix (Dringlichkeit/Wichtigkeit-Prinzip) – verbreitetes Zeitmanagement-Werkzeug, "
    "TK-17.",
    "Center for Creative Leadership – SBI-Modell (Situation-Behavior-Impact), TK-19.",
    "Rosenberg, M. B. (2003). Nonviolent communication: A language of life. PuddleDancer Press. — "
    "TK-19.",
]

QUELLEN_PRAXIS_HINWEIS = ("Fünf Karten (TK-07, TK-10, TK-11, TK-13, TK-15, TK-18) stützen sich auf "
    "KLARTEXT-interne Praxiserfahrung statt auf eine einzelne externe Quelle – dort, wo es primär um "
    "trägerspezifische Organisation statt um ein publiziertes Modell geht.")

def quellen_seite1():
    img, d, y = new_page("METHODISCHE GRUNDLAGE", "Quellen")
    y = draw_para(d, y, "Etablierte, bereits verifizierte Quellen bzw. Rechtsgrundlagen:",
                  size=4.6, color=KT_MUTED)
    y += mm(6)

    f_q = ImageFont.truetype(F_SANS_REG, mm(4.4))
    for q in QUELLEN_BESTAETIGT:
        for ln in wrap(d, q, f_q, CONTENT_W - mm(6)):
            d.text((MARGIN + mm(6), y), ln, font=f_q, fill=KT_INK)
            y += mm(6.8)
        y += mm(2)
    y += mm(4)

    y = draw_para(d, y, "Vorgeschlagen, bitte fachlich gegenprüfen – noch nicht im KLARTEXT-"
                        "Quellenregister bestätigt:",
                  size=4.2, color=GOLD)
    y += mm(3)
    for q in QUELLEN_VORGESCHLAGEN:
        for ln in wrap(d, q, f_q, CONTENT_W - mm(6)):
            d.text((MARGIN + mm(6), y), ln, font=f_q, fill=KT_INK)
            y += mm(6.8)
        y += mm(2)

    footer(d, "Quellen · 1/2")
    return img

def quellen_seite2():
    img, d, y = new_page("METHODISCHE GRUNDLAGE", "Praxisbasierte Karten")
    y = draw_para(d, y, QUELLEN_PRAXIS_HINWEIS, size=4.6)
    y += mm(8)
    y = draw_h2(d, y, "Anschluss an die App")
    y = draw_para(d, y, "TK-09 (Krisenprotokoll) verweist auf die Feuerwehrkarten FK-01–08 in der App "
                        "(akute Gefahr, Barometer Rot). TK-15 (Vertretungsorganisation) knüpft an "
                        "TK_Vertretungsassistent, TK-10 (Schulkommunikation) an das LK-Basis-Deck an – "
                        "die physischen Karten stehen bewusst nicht isoliert, sondern verweisen auf die "
                        "bestehenden digitalen Werkzeuge.")
    y += mm(6)
    y = draw_h2(d, y, "Barometer-Farbmarkierung in der Handlungskarten-Serie")
    y = draw_para(d, y, "TK ist das erste Deck einer wachsenden Handlungskarten-Serie (als nächstes: ein "
                        "Krisendeck zu den Feuerwehrkarten, danach ein Werkzeugkarten-Deck). Künftige "
                        "Decks der Serie tragen eine kleine Barometer-Farbmarkierung, damit man von der "
                        "aktuellen Barometer-Farbe direkt zum passenden Deck findet. Grau taucht dabei "
                        "bewusst auf keiner Handlungskarte auf: Grau bedeutet erschöpft oder "
                        "orientierungslos – das Kind weiß selbst nicht, was es braucht – und verlangt "
                        "kein Werkzeug, sondern Beobachten und TK informieren. Das deckt TK-Deck ohnehin "
                        "bereits ab.")

    footer(d, "Quellen · 2/2")
    return img

if __name__ == "__main__":
    pages = {
        "tk_anleitung1": anleitung_seite1(),
        "tk_anleitung2": anleitung_seite2(),
        "tk_quellen1": quellen_seite1(),
        "tk_quellen2": quellen_seite2(),
    }
    for name, img in pages.items():
        img.save(f"/sessions/kind-beautiful-ptolemy/mnt/outputs/booklet_{name}.png")
        print(name, "ok")
