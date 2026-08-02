#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Anleitung + Quellen fürs OGS-Basis-Deck – adaptiert von build_booklet_tk.py (leichte Struktur,
4 Seiten statt 7: kein Barometer/kLAR im Reflexionsformat, siehe LK/EL-Vorbild)."""
from PIL import Image, ImageDraw, ImageFont
Image.init()

DPI = 300
MM = DPI / 25.4
def mm(v): return int(round(v * MM))

OGS = (139, 195, 74)          # #8BC34A
OGS_LIGHT = (238, 246, 227)
OGS_BORDER = (206, 227, 176)
KT_INK = (45, 45, 45)
KT_MUTED = (122, 112, 96)
KT_PAPER = (245, 240, 232)
GOLD = (150, 120, 50)

F_SERIF_BOLD = "/usr/share/fonts/truetype/crosextra/Caladea-Bold.ttf"
F_SANS_REG = "/usr/share/fonts/truetype/lato/Lato-Regular.ttf"
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
    d.rectangle((0, 0, W, kopf_h), fill=OGS)
    d.text((MARGIN, mm(10)), kicker, font=f_kicker, fill=(240, 248, 230))
    ty = mm(17)
    for ln in lines:
        d.text((MARGIN, ty), ln, font=f_titel, fill=(255, 255, 255))
        ty += mm(size * 1.35)
    return img, d, kopf_h + mm(14)

def footer(d, page_label):
    f = ImageFont.truetype(F_SANS_REG, mm(4))
    d.text((MARGIN, H - mm(14)), "KLARTEXT-Mentoring · OGS-Deck · © 2026 Anja Jolk", font=f, fill=KT_MUTED)
    w = d.textlength(page_label, font=f)
    d.text((W - MARGIN - w, H - mm(14)), page_label, font=f, fill=KT_MUTED)

def draw_h2(d, y, text):
    f = ImageFont.truetype(F_SERIF_BOLD, mm(6.5))
    d.text((MARGIN, y), text, font=f, fill=OGS)
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
    d.ellipse((MARGIN, y + mm(1.6), MARGIN + mm(1.6), y + mm(3.2)), fill=OGS)
    lh = mm(size * 1.55)
    lines = wrap(d, text, f, CONTENT_W - mm(7))
    for ln in lines:
        d.text((MARGIN + mm(6), y), ln, font=f, fill=KT_INK)
        y += lh
    return y + mm(1.5)

def draw_numbered(d, y, num, titel, text, size=4.8):
    f_num = ImageFont.truetype(F_SERIF_BOLD, mm(7))
    d.ellipse((MARGIN, y, MARGIN + mm(9), y + mm(9)), fill=OGS)
    d.text((MARGIN + mm(4.5), y + mm(4.5)), str(num), font=f_num, anchor="mm", fill=(255, 255, 255))
    f_titel = ImageFont.truetype(F_SANS_BOLD, mm(5.2))
    d.text((MARGIN + mm(13), y + mm(0.5)), titel, font=f_titel, fill=OGS)
    f_text = ImageFont.truetype(F_SANS_REG, mm(size))
    ty = y + mm(7)
    lh = mm(size * 1.55)
    for ln in wrap(d, text, f_text, CONTENT_W - mm(13)):
        d.text((MARGIN + mm(13), ty), ln, font=f_text, fill=KT_INK)
        ty += lh
    return max(ty, y + mm(11)) + mm(4)

# ═══════════════════════════════════ ANLEITUNG ═══════════════════════════════════
def anleitung_seite1():
    img, d, y = new_page("GEBRAUCHSANWEISUNG", "Anleitung: So funktioniert das OGS-Deck")

    y = draw_h2(d, y, "Was ist das OGS-Deck?")
    y = draw_para(d, y, "Das OGS-Deck richtet sich an pädagogische Fachkräfte im Offenen Ganztag. Die "
                        "32 Karten laden zur Reflexion des eigenen Alltags mit der Gruppe ein: "
                        "Gruppendynamik, Rituale, Konflikte, Regeln, Beziehungsarbeit, Selbstständigkeit, "
                        "Übergänge sowie Rahmen und Zusammenarbeit. Kein Handlungskarten-Format mit festen "
                        "Schritten, sondern Reflexionskarten wie bei LK-Basis und EL-Basis – zum "
                        "Nachdenken, nicht zum Abarbeiten.")
    y += mm(8)

    y = draw_h2(d, y, "Die acht Themenblöcke")
    y = draw_para(d, y, "Gruppendynamik verstehen (OGS-01–04) · Rituale nutzen (OGS-05–08) · Konflikte "
                        "begleiten (OGS-09–12) · Regeln vermitteln (OGS-13–16) · Beziehungsarbeit im OGS "
                        "(OGS-17–20) · Selbstständigkeit fördern (OGS-21–24) · Übergänge gestalten "
                        "(OGS-25–28) · Rahmen und Zusammenarbeit (OGS-29–32).", size=4.4, color=KT_MUTED)
    y += mm(8)

    y = draw_h2(d, y, "In drei Schritten")
    y += mm(2)
    y = draw_numbered(d, y, 1, "Karte auswählen",
        "Passt ein Thema gerade zur eigenen Situation? Die acht Themenblöcke helfen bei der Auswahl.")
    y = draw_numbered(d, y, 2, "Anleitung und Fragen lesen",
        "Die Anleitung zeigt, für welche Situation die Karte gedacht ist. Die beiden Impulsfragen müssen "
        "nicht beide beantwortet werden – eine reicht oft.")
    y = draw_numbered(d, y, 3, "„Tipp für dich“ nutzen",
        "Ein kurzer, persönlich formulierter Gedanke auf jeder Rückseite – zum Nachwirken, nicht als "
        "Anweisung gemeint.")

    footer(d, "Anleitung · 1/2")
    return img

def anleitung_seite2():
    img, d, y = new_page("GEBRAUCHSANWEISUNG", "Nutzung, Brainy & Grenzen")

    y = draw_h2(d, y, "Allein oder im Team")
    y = draw_para(d, y, "Eine Karte ziehen, in Ruhe lesen, die Fragen für sich beantworten – oder im "
                        "Team-Gespräch gemeinsam nutzen. Beides ist vorgesehen, es gibt keine „richtige“ "
                        "Antwort.")
    y += mm(6)

    y = draw_h2(d, y, "Wo ist Brainy?")
    y = draw_para(d, y, "Anders als beim TK-Deck ist Brainy auf jeder OGS-Bildkarte mit dabei, nicht nur "
                        "als Eckmarke – im OGS sind Kinder im Bild, Brainy passt organisch mit rein statt "
                        "nur am Rand zu stehen (gleiche Regel wie bei KD/FS/DaZ-GS).")
    y += mm(6)

    box_y = y
    warn_text = ("Das OGS-Deck ersetzt keine Supervision und kein Kinderschutzverfahren. Bei Hinweisen "
                 "auf eine mögliche Kindeswohlgefährdung: sofort die trägerinternen Kinderschutz-Vorgaben "
                 "greifen lassen (§ 8a SGB VIII). Die Karten sind für ruhige Reflexionsmomente gedacht, "
                 "nicht für akute Krisen.")
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
    y = draw_bullet(d, y, "Trägeroffen: keine bestimmte OGS-Konzeption vorausgesetzt.")

    footer(d, "Anleitung · 2/2")
    return img

# ═══════════════════════════════════ QUELLEN ═══════════════════════════════════
QUELLEN_BESTAETIGT = [
    "Tuckman, B. W. (1965). Developmental sequence in small groups. Psychological Bulletin, 63(6), "
    "384–399. — bereits im KLARTEXT-Quellenregister bestätigt.",
    "Deci, E. L. & Ryan, R. M. — Self-Determination Theory (Autonomieunterstützung, Kompetenzerleben) — "
    "breite, etablierte Publikationsbasis.",
    "Hodgdon, L. (1995). Visual strategies for improving communication. QuirkRoberts. — bereits im "
    "KLARTEXT-Quellenregister bestätigt.",
    "Hejlskov Elvén, B. (2022). Keine Macht den Mächtigen: Warum Zwang und Druck in der Erziehung "
    "scheitern. Probst. — bereits im KLARTEXT-Quellenregister bestätigt (AT-Deck, 26.07.2026).",
]

QUELLEN_VORGESCHLAGEN = [
    "Wulf, C. & Zirfas, J. (2004). Die Kultur des Rituals. Campus. — Grundlage Block „Rituale nutzen“.",
    "Jefferys-Duden, K. — Streitschlichter-Programm. — Grundlage Block „Konflikte begleiten“.",
    "Nolting, H.-P. — Störungen in der Schulklasse. Beltz. — Grundlage Block „Regeln vermitteln“.",
    "Ahnert, L. — Forschung zur Fachkraft-Kind-Bindung. — Grundlage Block „Beziehungsarbeit im OGS“.",
    "Griebel, W. & Niesel, R. (2004). Transitionen: Fähigkeit von Kindern in Tageseinrichtungen fördern, "
    "Veränderungen erfolgreich zu bewältigen. Beltz. — Grundlage Block „Übergänge gestalten“.",
    "Speck, K., Olk, T., Böhm-Kasper, O., Stolz, H.-J. & Wiezorek, C. (Hrsg.) (2011). Ganztagsschulische "
    "Kooperation und Professionsentwicklung. Juventa. — Grundlage OGS-30 „Wer ist wofür zuständig?“.",
    "Rinaldi, C. (2006). In Dialogue with Reggio Emilia: Listening, Researching and Learning. Routledge. "
    "— Grundlage OGS-32 „Der Raum als stille Fachkraft“ (Konzept „Raum als dritter Erzieher“, Malaguzzi).",
]

def quellen_seite1():
    img, d, y = new_page("METHODISCHE GRUNDLAGE", "Quellen · Bestätigt")
    y = draw_para(d, y, "Vier Quellen sind bereits im KLARTEXT-Quellenregister bestätigt.",
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
    y = draw_para(d, y, "Sieben weitere Quellen – vorgeschlagen, bitte fachlich gegenprüfen, noch nicht "
                        "im Quellenregister bestätigt:",
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
    y = draw_bullet(d, y, "OGS-01–04 (Gruppendynamik) – Tuckman: Gruppen durchlaufen wiederkehrende "
                          "Phasen, keine feste Endstufe.")
    y = draw_bullet(d, y, "OGS-05–08 (Rituale) – Wulf & Zirfas: wiederkehrende Rituale geben Struktur und "
                          "Sicherheit im Alltag.")
    y = draw_bullet(d, y, "OGS-09–12 (Konflikte) – Jefferys-Duden: Kinder als aktiv Beteiligte der eigenen "
                          "Konfliktlösung statt reiner Schlichtung von außen.")
    y = draw_bullet(d, y, "OGS-13–16 (Regeln) – Nolting: wenige, klare, konsequent geltende Regeln statt "
                          "vieler unklarer.")
    y = draw_bullet(d, y, "OGS-17–20 (Beziehungsarbeit) – Ahnert: Fachkraft-Kind-Bindung als eigenständige, "
                          "professionelle Bindungsform.")
    y = draw_bullet(d, y, "OGS-21–24 (Selbstständigkeit) – Deci & Ryan: Autonomie, Kompetenzerleben und "
                          "soziale Eingebundenheit als Grundbedürfnisse.")
    y = draw_bullet(d, y, "OGS-25–28 (Übergänge) – Griebel & Niesel: Übergänge als eigene, gestaltbare "
                          "Phasen, nicht als bloße Nebensache.")
    y = draw_bullet(d, y, "OGS-29 (Herausforderndes Verhalten) – Hejlskov Elvén: Verhalten als "
                          "Kommunikation verstehen statt mit Druck zu begegnen.")
    y = draw_bullet(d, y, "OGS-30 (Team-Rollenklärung) – Speck, Olk u. a.: klare Zuständigkeiten als "
                          "Voraussetzung gelingender multiprofessioneller Kooperation.")
    y = draw_bullet(d, y, "OGS-31 (Hausaufgaben-Konflikt) – thematischer Transfer aus EL-22, keine eigene "
                          "Quelle nötig.")
    y = draw_bullet(d, y, "OGS-32 (Raumgestaltung) – Rinaldi: der Raum als aktiver, mitwirkender Teil der "
                          "pädagogischen Arbeit.")

    footer(d, "Quellen · 3/3")
    return img

if __name__ == "__main__":
    pages = {
        "ogs_anleitung1": anleitung_seite1(),
        "ogs_anleitung2": anleitung_seite2(),
        "ogs_quellen1": quellen_seite1(),
        "ogs_quellen1b": quellen_seite1b(),
        "ogs_quellen2": quellen_seite2(),
    }
    for name, img in pages.items():
        img.save(f"/sessions/kind-beautiful-ptolemy/mnt/outputs/booklet_{name}.png")
        print(name, "ok")
