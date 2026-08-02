#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Anleitung, Methodik, Glossar, Quellen fürs LK-Deck (Basis, 50 Karten/zehn Blöcke) – adaptiert von
build_booklet_el.py. Wie EL: kein Barometer/kLAR-Modell (INGRA-Werkzeug), Dual-Use-Prinzip (allein oder
mit Begleitung, hier: Kollegium/INGRA statt Partner:in), dritte systemische Frage. Erweitert 30.07.2026
um Block 7-10 (Klassengemeinschaft, Abgrenzung & Feierabend, Interkulturelle Kompetenz, KI & Digitalität)."""
from PIL import Image, ImageDraw, ImageFont
Image.init()

DPI = 300
MM = DPI / 25.4
def mm(v): return int(round(v * MM))

LK = (107, 78, 113)          # #6B4E71
LK_LIGHT = (238, 231, 239)
LK_BORDER = (206, 189, 208)
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
    d.rectangle((0, 0, W, kopf_h), fill=LK)
    d.text((MARGIN, mm(10)), kicker, font=f_kicker, fill=(232, 222, 234))
    ty = mm(17)
    for ln in lines:
        d.text((MARGIN, ty), ln, font=f_titel, fill=(255, 255, 255))
        ty += mm(size * 1.35)
    return img, d, kopf_h + mm(14)

def footer(d, page_label):
    f = ImageFont.truetype(F_SANS_REG, mm(4))
    d.text((MARGIN, H - mm(14)), "KLARTEXT-Mentoring · LK-Deck · © 2026 Anja Jolk", font=f, fill=KT_MUTED)
    w = d.textlength(page_label, font=f)
    d.text((W - MARGIN - w, H - mm(14)), page_label, font=f, fill=KT_MUTED)

def draw_h2(d, y, text):
    f = ImageFont.truetype(F_SERIF_BOLD, mm(6.5))
    d.text((MARGIN, y), text, font=f, fill=LK)
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
    d.ellipse((MARGIN, y + mm(1.6), MARGIN + mm(1.6), y + mm(3.2)), fill=LK)
    lh = mm(size * 1.55)
    lines = wrap(d, text, f, CONTENT_W - mm(7))
    for ln in lines:
        d.text((MARGIN + mm(6), y), ln, font=f, fill=KT_INK)
        y += lh
    return y + mm(1.5)

def draw_numbered(d, y, num, titel, text, size=4.8):
    f_num = ImageFont.truetype(F_SERIF_BOLD, mm(7))
    d.ellipse((MARGIN, y, MARGIN + mm(9), y + mm(9)), fill=LK)
    d.text((MARGIN + mm(4.5), y + mm(4.5)), str(num), font=f_num, anchor="mm", fill=(255, 255, 255))
    f_titel = ImageFont.truetype(F_SANS_BOLD, mm(5.2))
    d.text((MARGIN + mm(13), y + mm(0.5)), titel, font=f_titel, fill=LK)
    f_text = ImageFont.truetype(F_SANS_REG, mm(size))
    ty = y + mm(7)
    lh = mm(size * 1.55)
    for ln in wrap(d, text, f_text, CONTENT_W - mm(13)):
        d.text((MARGIN + mm(13), ty), ln, font=f_text, fill=KT_INK)
        ty += lh
    return max(ty, y + mm(11)) + mm(4)

# ═══════════════════════════════════ ANLEITUNG ═══════════════════════════════════
def anleitung_seite1():
    img, d, y = new_page("GEBRAUCHSANWEISUNG", "Anleitung: So funktioniert das LK-Deck")

    y = draw_h2(d, y, "Was ist das LK-Deck?")
    y = draw_para(d, y, "Das LK-Deck richtet sich direkt an Lehrkräfte – nicht an das Kind. Die 50 Karten "
                        "der LK-Basis laden zur Reflexion der eigenen Rolle im Schulalltag ein: die eigene "
                        "Haltung, die Beziehung zu einzelnen Kindern und zur Klasse als Ganzes, die "
                        "Zusammenarbeit mit Eltern und Kollegium, Abgrenzung und der Umgang mit digitalem "
                        "Wandel. Ergänzend gibt es Zusatzblöcke für bestimmte Situationen (z. B. Autismus, "
                        "ADHS, Pflegekinder in der Klasse), die an die jeweiligen Kind-Decks andocken.")
    y += mm(6)

    y = draw_h2(d, y, "Für wen ist es gedacht?")
    y = draw_para(d, y, "Für Lehrkräfte selbst – allein nutzbar oder gemeinsam mit einer begleitenden "
                        "Person (INGRA, Kolleg:in, Schulleitung). Beides ist ausdrücklich vorgesehen "
                        "(siehe „Zwei Nutzungsarten“, nächste Seite).")
    y += mm(8)

    y = draw_h2(d, y, "In drei Schritten")
    y += mm(2)
    y = draw_numbered(d, y, 1, "Karte auswählen",
        "Passt ein Thema gerade zur eigenen Situation? Die zehn Themenblöcke (siehe Cover) helfen bei "
        "der Auswahl.")
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
        "Eine begleitende Person (INGRA, Kolleg:in, Schulleitung) liest Anleitung und Fragen vor und "
        "lässt Raum zum Antworten. Die Rolle der Begleitung ist zuhören, nicht bewerten oder lösen.")
    y += mm(4)

    box_y = y
    warn_text = ("Das LK-Deck ersetzt keine Supervision, keine dienstliche Beurteilung und kein "
                 "Kinderschutzverfahren. Bei Hinweisen auf eine Kindeswohlgefährdung: sofort die "
                 "schulinternen Kinderschutz-Vorgaben greifen lassen. Bei eigener akuter Überforderung "
                 "oder Krise: eine Beratungsstelle oder das Personalratsangebot der Schule kontaktieren – "
                 "die Karten sind für ruhige Reflexionsmomente gedacht, nicht für akute Notlagen.")
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
    y = draw_bullet(d, y, "Im Idealfall ein ruhiger Moment statt zwischen Tür und Angel – aber auch fünf "
                          "Minuten in Ruhe sind besser als gar keine Reflexion.")
    y = draw_bullet(d, y, "Die Zusatzblöcke passend zur eigenen Klassensituation dazu nutzen, nicht alle "
                          "auf einmal.")

    footer(d, "Anleitung · 2/2")
    return img

# ═══════════════════════════════════ METHODIK ═══════════════════════════════════
def methodik_seite():
    img, d, y = new_page("HINTERGRUND", "Warum „Tipp für dich“ und eine dritte Frage?")
    y = draw_para(d, y, "Wie beim EL-Deck richtet sich die Hinweisbox direkt an die lesende Person selbst "
                        "– die Lehrkraft ist hier zugleich Zielperson und (meistens) Nutzer:in der Karte.",
                  size=4.6, color=KT_MUTED)
    y += mm(8)

    y = draw_h2(d, y, "Der Unterschied zu JD/KD")
    y = draw_para(d, y, "JD- und KD-Deck werden von einer Fachkraft mit einem Kind oder Jugendlichen "
                        "genutzt. Beim LK-Deck gibt es diese Rollenteilung nicht zwingend: Die Karte kann "
                        "direkt bei der Person ankommen, die auch die Antwort gibt. „Tipp für dich“ "
                        "funktioniert in beiden Nutzungsarten – ob die Karte allein gelesen oder von einer "
                        "Begleitung vorgelesen wird.")
    y += mm(8)

    y = draw_h2(d, y, "Die dritte Frage")
    y = draw_para(d, y, "Da Erwachsene mehr Tragfähigkeit haben als Kinder, ergänzt jede LK-Karte zu den "
                        "zwei Impulsfragen eine dritte, optisch abgesetzte Frage aus der systemischen "
                        "Beratung: eine Skalierungsfrage, eine zirkuläre Frage oder eine Handlungsfrage "
                        "(siehe Glossar). Bewusst nur eine dritte Frage, nicht mehr – die Karte soll ein "
                        "Impuls bleiben, kein Arbeitsblatt.")
    y += mm(6)

    y = draw_h2(d, y, "Kein Barometer, kein kLAR-Modell im LK-Deck")
    y = draw_para(d, y, "Barometer und kLAR-Modell (siehe JD-/KD-Deck) sind Werkzeuge für die Fachkraft, "
                        "um ein akut angespanntes Kind zu ko-regulieren – nicht für die Selbstreflexion der "
                        "Lehrkraft, deshalb bewusst nicht ins LK-Deck übernommen.")
    y += mm(4)
    y = draw_para(d, y, "Ein Hinweis bleibt trotzdem wichtig: Auch Lehrkräfte können selbst in einen roten "
                        "Zustand geraten (akute Überforderung, Erschöpfung). Bevor du in so einem Moment "
                        "eine Karte ziehst, lohnt sich ein kurzer Blick auf dich selbst – erst dich "
                        "regulieren, dann reflektieren. Die Karten sind für ruhige Momente gedacht, nicht "
                        "für akute rote Zustände (siehe auch „GRENZEN – WICHTIG“, vorherige Seite).",
                  size=4.4)
    y += mm(4)

    y = draw_para(d, y, "Hinweis zur Abgrenzung: Diese neuen Reflexionskarten tragen die Kennung „LK-R-“, "
                        "um sie von den bestehenden Karten LK-01–17 (INGRA-Lehrkraft-Zusammenarbeit, "
                        "anderer Inhalt) klar zu unterscheiden.", size=4.2, color=GOLD)

    footer(d, "Methodik")
    return img

# ═══════════════════════════════════ GLOSSAR ═══════════════════════════════════
GLOSSAR = [
    ("LK-Basis", "Die 50 universellen Karten des LK-Decks, thematisch in zehn Blöcke gegliedert – von "
     "der eigenen Rolle bis zu KI & Digitalität. Für alle Lehrkräfte gedacht, unabhängig von einer "
     "bestimmten Situation eines Kindes."),
    ("Zusatzblock", "Ein kleiner Satz von ca. 7 zusätzlichen Karten für eine bestimmte Klassensituation "
     "(z. B. Autismus, ADHS, ein Pflegekind in der Klasse), der an die LK-Basis und an das jeweilige "
     "Kind-Deck andockt."),
    ("Tipp für dich", "Die persönlich formulierte Hinweisbox auf jeder Kartenrückseite – direkt an die "
     "lesende Person selbst gerichtet."),
    ("INGRA", "Bezeichnung für die pädagogischen Fachkräfte des KLARTEXT-Systems (früher: "
     "Schulbegleiter:in). Kann im LK-Deck als begleitende Person in der Nutzungsart „Mit Begleitung“ "
     "auftreten."),
    ("Impulsfrage", "Eine offen formulierte Frage ohne vorgegebene richtige Antwort. Ziel ist nicht die "
     "schnelle Lösung, sondern das Öffnen eines Gedankens."),
    ("Systemisches Coaching", "Beratungsansatz, der eine Person nicht isoliert, sondern in ihren "
     "Beziehungen und Kontexten betrachtet. Fragt nicht „was ist falsch“, sondern „was würde helfen“."),
    ("Dritte Frage (Skalierung / Zirkulär / Handlung)", "Jede LK-Karte hat neben den zwei "
     "Impulsfragen eine optisch abgesetzte dritte Frage aus der systemischen Beratung: eine "
     "Skalierungsfrage („Auf einer Skala von 1–10 …“, lösungsorientierte Kurztherapie), eine "
     "zirkuläre Frage (Perspektive einer anderen Person, Mailänder Modell) oder eine Handlungsfrage "
     "(kleiner nächster Schritt)."),
]

def glossar_seite(begriffe, seiten_label, intro=None):
    img, d, y = new_page("BEGRIFFE AUS DEM LK-DECK", "Glossar")
    if intro:
        y = draw_para(d, y, intro, size=4.6, color=KT_MUTED)
        y += mm(8)

    for begriff, definition in begriffe:
        f_term = ImageFont.truetype(F_SERIF_BOLD, mm(6))
        d.text((MARGIN, y), begriff, font=f_term, fill=LK)
        y += mm(9)
        y = draw_para(d, y, definition, size=4.4)
        y += mm(4)
        d.line((MARGIN, y, W - MARGIN, y), fill=LK_BORDER, width=mm(0.3))
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

QUELLEN_VORGESCHLAGEN_NEUE_BLOECKE = [
    "Kounin, J. S. (1970). Discipline and group management in classrooms. Holt, Rinehart and Winston. "
    "— Grundlage für Block 7 (Klassengemeinschaft als System): Prävention und Gruppenführung wirken "
    "stärker auf das Klassenklima als reaktive Einzelinterventionen.",
    "Sonnentag, S., & Fritz, C. (2007). The Recovery Experience Questionnaire: Development and "
    "validation of a measure for assessing recuperation and unwinding from work. Journal of "
    "Occupational Health Psychology, 12(3), 204–221. — Grundlage für Block 8 (Abgrenzung & "
    "Feierabend): psychologische Distanzierung als zentraler Erholungsfaktor.",
    "Gogolin, I. (1994, 2. Aufl. 2008). Der monolinguale Habitus der multilingualen Schule. Waxmann. "
    "— Grundlage für Block 9 (Interkulturelle Kompetenz), bereits bei DaZ-GS/DaZ-Sek1 verwendet.",
    "Zhai, X. (2024). Transforming teachers' roles and agencies in the era of generative AI: "
    "Perceptions, acceptance, knowledge, and practices. Journal of Science Education and Technology. "
    "https://doi.org/10.1007/s10956-024-10174-0 — Grundlage für Block 10 (KI & Digitalität).",
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

    footer(d, "Quellen · 1/3")
    return img

def quellen_seite1b():
    img, d, y = new_page("METHODISCHE GRUNDLAGE", "Quellen: Themenblöcke 7–10")
    y = draw_para(d, y, "Grundlage der neuen Themenblöcke (ergänzt 30.07.2026) – vorgeschlagen, bitte "
                        "fachlich gegenprüfen, noch nicht im Quellenregister bestätigt:",
                  size=4.2, color=GOLD)
    y += mm(5)

    f_q = ImageFont.truetype(F_SANS_REG, mm(4.6))
    for q in QUELLEN_VORGESCHLAGEN_NEUE_BLOECKE:
        for ln in wrap(d, q, f_q, CONTENT_W - mm(6)):
            d.text((MARGIN + mm(6), y), ln, font=f_q, fill=KT_INK)
            y += mm(7.2)
        y += mm(4)

    footer(d, "Quellen · 2/3")
    return img

def quellen_seite2():
    img, d, y = new_page("METHODISCHE GRUNDLAGE", "Beispielhafte Passung")
    y = draw_bullet(d, y, "LK-R-01 / LK-R-05 / LK-R-26 (eigene Rolle & Grenzen) – Bowlby / Ainsworth: "
                          "sichere Bindung setzt eine ausreichend regulierte Bezugsperson voraus, nicht "
                          "Selbstaufgabe.")
    y = draw_bullet(d, y, "LK-R-06 / LK-R-07 / LK-R-08 (Kind verstehen) – Siegel: kindliches Verhalten als "
                          "Ausdruck innerer Zustände statt als bloßes „Fehlverhalten“ lesen.")
    y = draw_bullet(d, y, "LK-R-11 / LK-R-12 / LK-R-15 (Kommunikation) – Gottman / Rosenberg: gelingende "
                          "Kommunikation und gewaltfreie Sprache in belasteten Gesprächsmomenten.")
    y = draw_bullet(d, y, "LK-R-17 / LK-R-29 / LK-R-30 (Selbstfürsorge) – Bandura: Selbstwirksamkeit auch "
                          "für die eigene Lehrrolle, nicht nur für die Schüler:innen.")
    y = draw_bullet(d, y, "LK-R-31–35 (Klassengemeinschaft) – Kounin: Gruppenführung und Prävention "
                          "wirken stärker auf das Klassenklima als reaktive Einzelinterventionen.")
    y = draw_bullet(d, y, "LK-R-36–40 (Abgrenzung & Feierabend) – Sonnentag & Fritz: psychologische "
                          "Distanzierung von der Arbeit als zentraler Erholungsfaktor.")
    y = draw_bullet(d, y, "LK-R-41–45 (Interkulturelle Kompetenz) – Gogolin: der „monolinguale Habitus“ "
                          "macht sprachlich-kulturelle Vielfalt im Schulsystem sichtbar, statt sie zu "
                          "übergehen.")
    y = draw_bullet(d, y, "LK-R-46–50 (KI & Digitalität) – Zhai: Wandel der Lehrkraft-Rolle durch "
                          "generative KI, von reiner Skepsis zu aktiver Mitgestaltung.")
    y += mm(6)
    y = draw_h2(d, y, "Zur dritten Frage")
    y = draw_para(d, y, "Skalierungs-, zirkuläre und Handlungsfragen sind über alle LK-Karten verteilt "
                        "eingesetzt, passend zum jeweiligen Kartenthema gewählt (siehe Glossar: „Dritte "
                        "Frage“) – keine kartenweise Einzelauflistung hier, um die Seite nicht zu "
                        "überladen.")

    footer(d, "Quellen · 3/3")
    return img

if __name__ == "__main__":
    pages = {
        "lk_anleitung1": anleitung_seite1(),
        "lk_anleitung2": anleitung_seite2(),
        "lk_methodik": methodik_seite(),
        "lk_glossar1": glossar_seite(GLOSSAR[:3], "Glossar · 1/2",
            intro="Kurz erklärt: Begriffe, die auf den Karten oder in dieser Anleitung vorkommen und "
                  "nicht selbsterklärend sind."),
        "lk_glossar2": glossar_seite(GLOSSAR[3:], "Glossar · 2/2"),
        "lk_quellen1": quellen_seite1(),
        "lk_quellen2": quellen_seite2(),
    }
    for name, img in pages.items():
        img.save(f"/sessions/kind-beautiful-ptolemy/mnt/outputs/booklet_{name}.png")
        print(name, "ok")
