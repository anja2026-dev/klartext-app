#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Anleitung, Methodik, Glossar, Quellen fürs EL-Deck (Basis) – adaptiert von build_booklet_kd.py.
Unterschied zu JD/KD: kein Barometer/kLAR-Modell (das ist ein INGRA-Werkzeug für die Ko-Regulation
eines Kindes, nicht für die elterliche Selbstreflexion gedacht). Stattdessen: Erklärung des
Dual-Use-Prinzips (allein oder mit Begleitung nutzbar) als Methodik-Seite."""
from PIL import Image, ImageDraw, ImageFont
Image.init()

DPI = 300
MM = DPI / 25.4
def mm(v): return int(round(v * MM))

EL = (191, 91, 62)          # #BF5B3E
EL_LIGHT = (250, 235, 227)
EL_BORDER = (232, 196, 176)
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
    d.rectangle((0, 0, W, kopf_h), fill=EL)
    d.text((MARGIN, mm(10)), kicker, font=f_kicker, fill=(250, 232, 224))
    ty = mm(17)
    for ln in lines:
        d.text((MARGIN, ty), ln, font=f_titel, fill=(255, 255, 255))
        ty += mm(size * 1.35)
    return img, d, kopf_h + mm(14)

def footer(d, page_label):
    f = ImageFont.truetype(F_SANS_REG, mm(4))
    d.text((MARGIN, H - mm(14)), "KLARTEXT-Mentoring · EL-Deck · © 2026 Anja Jolk", font=f, fill=KT_MUTED)
    w = d.textlength(page_label, font=f)
    d.text((W - MARGIN - w, H - mm(14)), page_label, font=f, fill=KT_MUTED)

def draw_h2(d, y, text):
    f = ImageFont.truetype(F_SERIF_BOLD, mm(6.5))
    d.text((MARGIN, y), text, font=f, fill=EL)
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
    d.ellipse((MARGIN, y + mm(1.6), MARGIN + mm(1.6), y + mm(3.2)), fill=EL)
    lh = mm(size * 1.55)
    lines = wrap(d, text, f, CONTENT_W - mm(7))
    for ln in lines:
        d.text((MARGIN + mm(6), y), ln, font=f, fill=KT_INK)
        y += lh
    return y + mm(1.5)

def draw_numbered(d, y, num, titel, text, size=4.8):
    f_num = ImageFont.truetype(F_SERIF_BOLD, mm(7))
    d.ellipse((MARGIN, y, MARGIN + mm(9), y + mm(9)), fill=EL)
    d.text((MARGIN + mm(4.5), y + mm(4.5)), str(num), font=f_num, anchor="mm", fill=(255, 255, 255))
    f_titel = ImageFont.truetype(F_SANS_BOLD, mm(5.2))
    d.text((MARGIN + mm(13), y + mm(0.5)), titel, font=f_titel, fill=EL)
    f_text = ImageFont.truetype(F_SANS_REG, mm(size))
    ty = y + mm(7)
    lh = mm(size * 1.55)
    for ln in wrap(d, text, f_text, CONTENT_W - mm(13)):
        d.text((MARGIN + mm(13), ty), ln, font=f_text, fill=KT_INK)
        ty += lh
    return max(ty, y + mm(11)) + mm(4)

# ═══════════════════════════════════ ANLEITUNG ═══════════════════════════════════
def anleitung_seite1():
    img, d, y = new_page("GEBRAUCHSANWEISUNG", "Anleitung: So funktioniert das EL-Deck")

    y = draw_h2(d, y, "Was ist das EL-Deck?")
    y = draw_para(d, y, "Das EL-Deck richtet sich direkt an Eltern – nicht an das Kind. Die 30 Karten der "
                        "EL-Basis laden zur Reflexion der eigenen Elternrolle ein: die eigenen Grenzen, die "
                        "Beziehung zum Kind, den Familienalltag. Ergänzend gibt es Zusatzblöcke für "
                        "bestimmte Situationen (z. B. Autismus, ADHS, Pflegeelternschaft), die an die "
                        "jeweiligen Kind-Decks andocken.")
    y += mm(6)

    y = draw_h2(d, y, "Für wen ist es gedacht?")
    y = draw_para(d, y, "Für Eltern selbst – allein nutzbar oder gemeinsam mit einer begleitenden Person "
                        "(INGRA, Berater:in, Partner:in). Beides ist ausdrücklich vorgesehen (siehe "
                        "„Zwei Nutzungsarten“, nächste Seite).")
    y += mm(8)

    y = draw_h2(d, y, "In drei Schritten")
    y += mm(2)
    y = draw_numbered(d, y, 1, "Karte auswählen",
        "Passt ein Thema gerade zur eigenen Situation? Die sechs Themenblöcke (siehe Rückseite dieser "
        "Seite) helfen bei der Auswahl.")
    y = draw_numbered(d, y, 2, "Anleitung und Fragen lesen",
        "Die Anleitung zeigt, für welche Situation die Karte gedacht ist. Die beiden Impulsfragen müssen "
        "nicht beide beantwortet werden – eine reicht oft.")
    y = draw_numbered(d, y, 3, "„Tipp für dich“ nutzen",
        "Ein kurzer, persönlich formulierter Gedanke auf jeder Rückseite – zum Nachwirken, nicht als "
        "Anweisung gemeint.")

    footer(d, "Anleitung · 1/2")
    return img

def anleitung_seite2():
    img, d, y = new_page("GEBRAUCHSANWEISUNG", "Zwei Nutzungsarten & Grenzen")

    y = draw_h2(d, y, "Zwei Nutzungsarten – beides ist vorgesehen")
    y = draw_numbered(d, y, 1, "Allein, zur Selbstreflexion",
        "Eine Karte ziehen, in Ruhe lesen, die Fragen für sich beantworten – laut, im Kopf oder "
        "schriftlich. Es gibt keine „richtige“ Antwort.")
    y = draw_numbered(d, y, 2, "Mit Begleitung",
        "Eine begleitende Person (INGRA, Berater:in, Partner:in) liest Anleitung und Fragen vor und lässt "
        "Raum zum Antworten. Die Rolle der Begleitung ist zuhören, nicht bewerten oder lösen.")
    y += mm(4)

    box_y = y
    warn_text = ("Das EL-Deck ersetzt keine Therapie, keine Erziehungs- oder Paarberatung und kein "
                 "Kinderschutzverfahren. Bei Hinweisen auf eine Kindeswohlgefährdung: sofort die zuständige "
                 "Beratungsstelle oder das Jugendamt einbeziehen. Bei eigener akuter Überforderung oder "
                 "Krise: eine Beratungsstelle oder die Telefonseelsorge kontaktieren – die Karten sind für "
                 "ruhige Reflexionsmomente gedacht, nicht für akute Notlagen.")
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
    y = draw_bullet(d, y, "Freiwilligkeit: keine Karte erzwingen, auch nicht sich selbst gegenüber.")
    y = draw_bullet(d, y, "Ruhiger Moment statt zwischen Tür und Angel – auch fünf Minuten reichen.")
    y = draw_bullet(d, y, "Die Zusatzblöcke passend zur eigenen Situation dazu nutzen, nicht alle auf "
                          "einmal.")

    footer(d, "Anleitung · 2/2")
    return img

# ═══════════════════════════════════ METHODIK (Dual-Use) ═══════════════════════════════════
def methodik_seite():
    img, d, y = new_page("HINTERGRUND", "Warum „Tipp für dich“ statt „Tipp für die INGRA“?")
    y = draw_para(d, y, "Bei JD- und KD-Deck richtet sich die Hinweisbox an die begleitende Fachkraft. Beim "
                        "EL-Deck ist die lesende Person selbst die Zielperson der Karte – deshalb ein "
                        "anderer, persönlicherer Ton.", size=4.6, color=KT_MUTED)
    y += mm(8)

    y = draw_h2(d, y, "Der Unterschied zu JD/KD")
    y = draw_para(d, y, "JD- und KD-Deck werden von einer Fachkraft mit einem Kind oder Jugendlichen "
                        "genutzt – die Fachkraft liest die Hinweisbox, um die Situation besser einzuschätzen. "
                        "Beim EL-Deck gibt es diese Rollenteilung nicht zwingend: Die Karte kann direkt bei "
                        "der Person ankommen, die auch die Antwort gibt. „Tipp für dich“ funktioniert in "
                        "beiden Nutzungsarten – ob die Karte allein gelesen oder von einer Begleitung "
                        "vorgelesen wird.")
    y += mm(8)

    y = draw_h2(d, y, "Kein Barometer, kein kLAR-Modell im EL-Deck")
    y = draw_para(d, y, "Barometer und kLAR-Modell (siehe JD-/KD-Deck) sind Werkzeuge für die Fachkraft, um "
                        "ein akut angespanntes Kind zu ko-regulieren – sie sind nicht für die elterliche "
                        "Selbstreflexion gedacht und wurden deshalb bewusst nicht ins EL-Deck übernommen. "
                        "Wer als Elternteil selbst regelmäßig an eigene Grenzen kommt, findet dazu Impulse "
                        "in Block 6 (Selbstfürsorge als Elternteil) sowie im Zusatzblock der jeweiligen "
                        "Zielgruppe.")
    y += mm(4)
    y = draw_para(d, y, "Ein Hinweis bleibt trotzdem wichtig: Auch Eltern können selbst in einen roten "
                        "Zustand geraten (akute Überforderung, Erschöpfung). Bevor du in so einem Moment "
                        "eine Karte ziehst, lohnt sich ein kurzer Blick auf dich selbst – erst dich "
                        "regulieren, dann reflektieren. Die Karten sind für ruhige Momente gedacht, nicht "
                        "für akute rote Zustände.", size=4.4)
    y += mm(4)

    y = draw_para(d, y, "Hinweis zur Abgrenzung: Das EL-Deck (Karten) ist ein eigenständiges Produkt, "
                        "getrennt vom bestehenden EL-Kurs (Online-Modulreihe M0–M8) im KLARTEXT-System – "
                        "beide ergänzen sich, sind aber unabhängig voneinander nutzbar.", size=4.2, color=GOLD)

    footer(d, "Methodik")
    return img

# ═══════════════════════════════════ GLOSSAR ═══════════════════════════════════
GLOSSAR = [
    ("EL-Basis", "Die 30 universellen Karten des EL-Decks, thematisch in sechs Blöcke gegliedert – von der "
     "eigenen Rolle bis zur Selbstfürsorge. Für alle Eltern gedacht, unabhängig von einer bestimmten "
     "Situation des Kindes."),
    ("Zusatzblock", "Ein kleiner Satz von ca. 7 zusätzlichen Karten für eine bestimmte Elternsituation "
     "(z. B. Autismus, ADHS, Pflegeelternschaft), der an die EL-Basis und an das jeweilige Kind-Deck "
     "andockt."),
    ("Tipp für dich", "Die persönlich formulierte Hinweisbox auf jeder Kartenrückseite – anders als „Tipp "
     "für die INGRA“ bei JD/KD direkt an die lesende Person selbst gerichtet."),
    ("INGRA", "Bezeichnung für die pädagogischen Fachkräfte des KLARTEXT-Systems (früher: "
     "Schulbegleiter:in). Kann im EL-Deck als begleitende Person in der Nutzungsart „Mit Begleitung“ "
     "auftreten."),
    ("Impulsfrage", "Eine offen formulierte Frage ohne vorgegebene richtige Antwort. Ziel ist nicht die "
     "schnelle Lösung, sondern das Öffnen eines Gedankens."),
    ("Systemisches Coaching", "Beratungsansatz, der eine Person nicht isoliert, sondern in ihren "
     "Beziehungen und Kontexten betrachtet. Fragt nicht „was ist falsch“, sondern „was würde helfen“."),
    ("Dritte Frage (Skalierung / Zirkulär / Handlung)", "Jede EL-Karte hat neben den zwei "
     "Impulsfragen eine optisch abgesetzte dritte Frage aus der systemischen Beratung: eine "
     "Skalierungsfrage („Auf einer Skala von 1–10 …“, lösungsorientierte Kurztherapie), eine "
     "zirkuläre Frage (Perspektive einer anderen Person, Mailänder Modell) oder eine Handlungsfrage "
     "(kleiner nächster Schritt). Bewusst nur eine dritte Frage, nicht mehr – die Karte soll ein "
     "Impuls bleiben, kein Arbeitsblatt."),
]

def glossar_seite(begriffe, seiten_label, intro=None):
    img, d, y = new_page("BEGRIFFE AUS DEM EL-DECK", "Glossar")
    if intro:
        y = draw_para(d, y, intro, size=4.6, color=KT_MUTED)
        y += mm(8)

    for begriff, definition in begriffe:
        f_term = ImageFont.truetype(F_SERIF_BOLD, mm(6))
        d.text((MARGIN, y), begriff, font=f_term, fill=EL)
        y += mm(9)
        y = draw_para(d, y, definition, size=4.4)
        y += mm(4)
        d.line((MARGIN, y, W - MARGIN, y), fill=EL_BORDER, width=mm(0.3))
        y += mm(7)

    footer(d, seiten_label)
    return img

# ═══════════════════════════════════ QUELLEN ═══════════════════════════════════
QUELLEN_BESTAETIGT = [
    "Bowlby, J. (1969). Attachment and loss: Vol. 1. Attachment. Basic Books.",
    "Ainsworth, M. D. S., Blehar, M. C., Waters, E., & Wall, S. (1978). Patterns of attachment: A "
    "psychological study of the strange situation. Erlbaum.",
    "Siegel, D. J. (1999). The developing mind: How relationships and the brain interact to shape who we "
    "are. Guilford Press.",
    "Gottman, J. M. (1994). Why marriages succeed or fail: And how you can make yours last. Simon & "
    "Schuster.",
    "Rosenberg, M. B. (2003). Nonviolent communication: A language of life (2nd ed.). PuddleDancer Press.",
    "Bandura, A. (1977). Self-efficacy: Toward a unifying theory of behavioral change. Psychological "
    "Review, 84(2), 191–215.",
]

QUELLEN_VORGESCHLAGEN = [
    "de Shazer, S. (1988). Clues: Investigating solutions in brief therapy. Norton. — Grundlage der "
    "Skalierungsfragen.",
    "Selvini Palazzoli, M., Boscolo, L., Cecchin, G., & Prata, G. (1980). Hypothesizing—circularity—"
    "neutrality: Three guidelines for the conductor of the session. Family Process, 19(1), 3–12. — "
    "Grundlage der zirkulären Fragen (Mailänder Modell).",
]

def quellen_seite1():
    img, d, y = new_page("METHODISCHE GRUNDLAGE", "Quellen")
    y = draw_para(d, y, "Alle folgenden Quellen sind bereits im KLARTEXT-Quellenregister bestätigt.",
                  size=4.6, color=KT_MUTED)
    y += mm(9)

    f_q = ImageFont.truetype(F_SANS_REG, mm(4.6))
    for q in QUELLEN_BESTAETIGT:
        for ln in wrap(d, q, f_q, CONTENT_W - mm(6)):
            d.text((MARGIN + mm(6), y), ln, font=f_q, fill=KT_INK)
            y += mm(7.2)
        y += mm(2)
    y += mm(6)

    y = draw_para(d, y, "Grundlage der dritten Frage (Skalierung / Zirkulär) – vorgeschlagen, bitte "
                        "fachlich gegenprüfen, noch nicht im Quellenregister bestätigt:",
                  size=4.2, color=GOLD)
    y += mm(3)
    for q in QUELLEN_VORGESCHLAGEN:
        for ln in wrap(d, q, f_q, CONTENT_W - mm(6)):
            d.text((MARGIN + mm(6), y), ln, font=f_q, fill=KT_INK)
            y += mm(7.2)
        y += mm(2)

    footer(d, "Quellen · 1/2")
    return img

def quellen_seite2():
    img, d, y = new_page("METHODISCHE GRUNDLAGE", "Beispielhafte Passung")
    y = draw_bullet(d, y, "EL-01 / EL-02 / EL-26 (eigene Rolle & Grenzen) – Bowlby / Ainsworth: sichere "
                          "Bindung setzt eine ausreichend regulierte Bezugsperson voraus, nicht "
                          "Selbstaufgabe.")
    y = draw_bullet(d, y, "EL-06 / EL-07 / EL-08 (Kind verstehen) – Siegel: kindliches Verhalten als "
                          "Ausdruck innerer Zustände statt als bloßes „Fehlverhalten“ lesen.")
    y = draw_bullet(d, y, "EL-11 / EL-12 / EL-13 (Kommunikation) – Gottman / Rosenberg: gelingende "
                          "Kommunikation und gewaltfreie Sprache in belasteten Gesprächsmomenten.")
    y = draw_bullet(d, y, "EL-17 / EL-29 / EL-30 (Selbstfürsorge) – Bandura: Selbstwirksamkeit auch für die "
                          "eigene Elternrolle, nicht nur für das Kind.")
    y += mm(6)
    y = draw_h2(d, y, "Zur dritten Frage")
    y = draw_para(d, y, "Skalierungs-, zirkuläre und Handlungsfragen sind über alle 51 EL-Karten verteilt "
                        "eingesetzt, passend zum jeweiligen Kartenthema gewählt (siehe Glossar: „Dritte "
                        "Frage“) – keine kartenweise Einzelauflistung hier, um die Seite nicht zu "
                        "überladen.")

    footer(d, "Quellen · 2/2")
    return img

if __name__ == "__main__":
    pages = {
        "el_anleitung1": anleitung_seite1(),
        "el_anleitung2": anleitung_seite2(),
        "el_methodik": methodik_seite(),
        "el_glossar1": glossar_seite(GLOSSAR[:3], "Glossar · 1/2",
            intro="Kurz erklärt: Begriffe, die auf den Karten oder in dieser Anleitung vorkommen und "
                  "nicht selbsterklärend sind."),
        "el_glossar2": glossar_seite(GLOSSAR[3:], "Glossar · 2/2"),
        "el_quellen1": quellen_seite1(),
        "el_quellen2": quellen_seite2(),
    }
    for name, img in pages.items():
        img.save(f"/sessions/kind-beautiful-ptolemy/mnt/outputs/booklet_{name}.png")
        print(name, "ok")
