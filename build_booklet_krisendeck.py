#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Anleitung, Hintergrund & Quellen fürs Krisendeck (Feuerwehrkarten FK-01–08 als physisches Deck).
Zweites Deck im Handlungskarten-Format, nach TK. Struktur/Helfer von build_booklet_tk.py übernommen."""
from PIL import Image, ImageDraw, ImageFont
Image.init()

DPI = 300
MM = DPI / 25.4
def mm(v): return int(round(v * MM))

FK = (198, 40, 40)          # #C62828
FK_LIGHT = (253, 234, 234)
FK_BORDER = (244, 160, 160)
KT_INK = (45, 45, 45)
KT_MUTED = (122, 112, 96)
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
    d.rectangle((0, 0, W, kopf_h), fill=FK)
    d.text((MARGIN, mm(10)), kicker, font=f_kicker, fill=(255, 220, 220))
    ty = mm(17)
    for ln in lines:
        d.text((MARGIN, ty), ln, font=f_titel, fill=(255, 255, 255))
        ty += mm(size * 1.35)
    return img, d, kopf_h + mm(14)

def footer(d, page_label):
    f = ImageFont.truetype(F_SANS_REG, mm(4))
    d.text((MARGIN, H - mm(14)), "KLARTEXT-Mentoring · Krisendeck · © 2026 Anja Jolk", font=f, fill=KT_MUTED)
    w = d.textlength(page_label, font=f)
    d.text((W - MARGIN - w, H - mm(14)), page_label, font=f, fill=KT_MUTED)

def draw_h2(d, y, text):
    f = ImageFont.truetype(F_SERIF_BOLD, mm(6.5))
    d.text((MARGIN, y), text, font=f, fill=FK)
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
    d.ellipse((MARGIN, y + mm(1.6), MARGIN + mm(1.6), y + mm(3.2)), fill=FK)
    lh = mm(size * 1.55)
    lines = wrap(d, text, f, CONTENT_W - mm(7))
    for ln in lines:
        d.text((MARGIN + mm(6), y), ln, font=f, fill=KT_INK)
        y += lh
    return y + mm(1.5)

def draw_numbered(d, y, num, titel, text, size=4.8):
    f_num = ImageFont.truetype(F_SERIF_BOLD, mm(7))
    d.ellipse((MARGIN, y, MARGIN + mm(9), y + mm(9)), fill=FK)
    d.text((MARGIN + mm(4.5), y + mm(4.5)), str(num), font=f_num, anchor="mm", fill=(255, 255, 255))
    f_titel = ImageFont.truetype(F_SANS_BOLD, mm(5.2))
    d.text((MARGIN + mm(13), y + mm(0.5)), titel, font=f_titel, fill=FK)
    f_text = ImageFont.truetype(F_SANS_REG, mm(size))
    ty = y + mm(7)
    lh = mm(size * 1.55)
    for ln in wrap(d, text, f_text, CONTENT_W - mm(13)):
        d.text((MARGIN + mm(13), ty), ln, font=f_text, fill=KT_INK)
        ty += lh
    return max(ty, y + mm(11)) + mm(4)

# ═══════════════════════════════════ ANLEITUNG ═══════════════════════════════════
def anleitung_seite1():
    img, d, y = new_page("GEBRAUCHSANWEISUNG", "Anleitung: So funktioniert das Krisendeck")

    y = draw_h2(d, y, "Was ist das Krisendeck?")
    y = draw_para(d, y, "8 Karten für akute Krisensituationen (Barometer Rot) – aus den bereits "
                        "bestehenden, fachlich hinterlegten Feuerwehrkarten FK-01–08 der App, gekürzt "
                        "auf Kartenlänge und jetzt zusätzlich physisch griffbereit. Zweites Deck der "
                        "Handlungskarten-Serie, nach TK. Anders als TK (Team-/Fallkoordination) ist das "
                        "Krisendeck ein Sekunden-Schnellgriff-Werkzeug für den akuten Moment.")
    y += mm(6)

    y = draw_h2(d, y, "Aufbau jeder Karte")
    y = draw_bullet(d, y, "Vorderseite – bewusst ohne Foto: Icon, Titel, 2–3 kurze "
                          "Erkennungssignale zum schnellen Blättern und Wiedererkennen.")
    y = draw_bullet(d, y, "Rückseite – Situation (1 Satz), Sofortmaßnahmen (nummeriert), "
                          "Abgrenzung „Jetzt tun / Jetzt nicht“, Verweis auf die vollständige "
                          "Fassung in der App.")
    y += mm(4)

    y = draw_h2(d, y, "Die 8 Karten")
    y = draw_para(d, y, "FK-01 Akute Eskalation · FK-02 Shutdown · FK-03 Panikattacke · "
                        "FK-04 Fremdgefährdung · FK-05 Selbstverletzung · FK-06 Weglaufen/Flucht · "
                        "FK-07 Dissoziation · FK-08 Meltdown.", size=4.4, color=KT_MUTED)
    y += mm(4)

    y = draw_h2(d, y, "Alle Karten: Barometer Rot")
    y = draw_para(d, y, "Anders als ein Werkzeugkarten-Deck (situativ Gelb/Orange) ist dieses ganze "
                        "Deck die Rot-Antwort – deshalb einheitlich rot markiert, keine Farbdifferenzierung "
                        "innerhalb des Decks nötig.")

    footer(d, "Anleitung · 1/2")
    return img

def anleitung_seite2():
    img, d, y = new_page("GEBRAUCHSANWEISUNG", "Grenzen & Meldewege")

    box_y = y
    warn_text = ("Das Krisendeck ersetzt keine Rechtsberatung, keine Supervision und kein "
                 "Kinderschutzverfahren. Es ist eine Gedächtnisstütze für den akuten Moment – nicht "
                 "die vollständige fachliche Grundlage. Bei jeder Nutzung gilt: TK unverzüglich "
                 "informieren, trägerinterne Kinderschutz-Vorgaben greifen lassen, bei unmittelbarer "
                 "Gefahr Notruf 112 (Rettungsdienst/Polizei) bzw. 110 (Polizei) nicht zögern.")
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

    y = draw_h2(d, y, "Meldepflicht bei FK-04 und FK-05")
    y = draw_para(d, y, "Fremdgefährdung (FK-04) und Selbstverletzung (FK-05) berühren unmittelbar "
                        "den Kinderschutz (§ 8a SGB VIII). Bei beiden gilt: sofortige Information an TK "
                        "ist keine Option, sondern Pflicht – unabhängig davon, ob das Kind um Schweigen "
                        "bittet. TK und ggf. Schulleitung entscheiden über die weiteren, formellen "
                        "Schritte, nicht INGRA allein.")
    y += mm(4)

    y = draw_h2(d, y, "Kein Ersatz für die App")
    y = draw_para(d, y, "Jede Karte trägt einen Verweis auf die vollständige Fassung in der App – dort "
                        "stehen zusätzliche Hintergründe, Meldewege und (bei FK-07/FK-08) weiterführende "
                        "Abschnitte, die aus Platzgründen nicht auf der Karte stehen, aber wichtig für "
                        "das Verständnis sind (siehe nächste Seite).")

    footer(d, "Anleitung · 2/2")
    return img

# ═══════════════════════════════════ HINTERGRUND ═══════════════════════════════════
DISSOZIATION_VS_SHUTDOWN = [
    ("Dissoziation (FK-07)", "Shutdown (FK-02)"),
    ("Blick leer, durch INGRA hindurch", "Blick gesenkt, Kind zieht sich zurück"),
    ("Keine Reaktion auf Ansprechen", "Geringe, verzögerte Reaktion möglich"),
    ("Körper wirkt eingefroren, steif", "Körper wirkt zusammengesunken"),
    ("Danach oft: Verwirrung, keine Erinnerung", "Danach: Erschöpfung, aber Erinnerung"),
    ("Immer FK-07 + TK sofort", "FK-02, TK informieren"),
]

def hintergrund_seite():
    img, d, y = new_page("HINTERGRUND", "Dissoziation vs. Shutdown & Meltdown")

    y = draw_h2(d, y, "Abgrenzung: Dissoziation (FK-07) vs. Shutdown (FK-02)")
    y = draw_para(d, y, "Beide Zustände wirken auf den ersten Blick ähnlich – ruhig, reglos, "
                        "unerreichbar. Der Unterschied entscheidet, welche Karte gilt:", size=4.4)
    y += mm(4)

    f_head = ImageFont.truetype(F_SANS_BOLD, mm(4.3))
    f_cell = ImageFont.truetype(F_SANS_REG, mm(4.1))
    col_gap = mm(4)
    col_w = (CONTENT_W - col_gap) / 2
    header_h = mm(7)
    d.rounded_rectangle((MARGIN, y, MARGIN + col_w, y + header_h), radius=mm(1), fill=FK)
    d.rounded_rectangle((MARGIN + col_w + col_gap, y, MARGIN + col_w * 2 + col_gap, y + header_h),
                         radius=mm(1), fill=(90, 20, 20))
    d.text((MARGIN + col_w / 2, y + header_h / 2), DISSOZIATION_VS_SHUTDOWN[0][0],
           font=f_head, fill=(255, 255, 255), anchor="mm")
    d.text((MARGIN + col_w + col_gap + col_w / 2, y + header_h / 2), DISSOZIATION_VS_SHUTDOWN[0][1],
           font=f_head, fill=(255, 255, 255), anchor="mm")
    y += header_h + mm(1.5)
    for a, b in DISSOZIATION_VS_SHUTDOWN[1:]:
        a_lines = wrap(d, a, f_cell, col_w - mm(3))
        b_lines = wrap(d, b, f_cell, col_w - mm(3))
        n = max(len(a_lines), len(b_lines))
        row_h = n * mm(5.6) + mm(2)
        d.rounded_rectangle((MARGIN, y, MARGIN + col_w, y + row_h), radius=mm(1), fill=FK_LIGHT)
        d.rounded_rectangle((MARGIN + col_w + col_gap, y, MARGIN + col_w * 2 + col_gap, y + row_h),
                             radius=mm(1), fill=(245, 240, 240))
        ty = y + mm(1)
        for ln in a_lines:
            d.text((MARGIN + mm(1.5), ty), ln, font=f_cell, fill=KT_INK)
            ty += mm(5.6)
        ty = y + mm(1)
        for ln in b_lines:
            d.text((MARGIN + col_w + col_gap + mm(1.5), ty), ln, font=f_cell, fill=KT_INK)
            ty += mm(5.6)
        y += row_h + mm(1.2)

    y += mm(4)
    y = draw_h2(d, y, "Hintergrund: Was ist ein Meltdown? (FK-08)")
    y = draw_para(d, y, "Ein Meltdown ist kein Wutanfall und kein manipulatives Verhalten. Totaler "
                        "Kontrollverlust durch sensorische oder emotionale Überlastung – häufig bei "
                        "Autismus, aber nicht ausschließlich. Das Nervensystem ist vollständig "
                        "überwältigt, ein „Können“ ist nicht mehr möglich. Unterschied zum Wutanfall: "
                        "kein Ziel, keine Kontrolle, keine Publikum-Orientierung. Dauer: Minuten bis "
                        "Stunden – lässt sich nicht abkürzen, nur begleiten.", size=4.4)
    y += mm(3)
    y = draw_para(d, y, "Prävention – typische Auslöser: sensorische Überlastung (Lärm, Licht, Gerüche, "
                        "Berührung), Routinebrüche, soziale Überforderung, Erschöpfung. Auslöserprofil "
                        "des Kindes kennen und mit TK besprechen.", size=4.4, color=KT_MUTED)

    footer(d, "Hintergrund")
    return img

# ═══════════════════════════════════ BAROMETER & FEUERWEHR ═══════════════════════════════════
BAROMETER_KURZ = [
    ((76, 175, 80), "GRÜN", "Stabil, lernbereit."),
    ((249, 168, 37), "GELB", "Angespannt – Gespräch möglich."),
    ((239, 108, 0), "ORANGE", "Dysreguliert – hier greift das kLAR-Modell (siehe Werkzeugkarten-Deck)."),
    ((198, 40, 40), "ROT", "Akute Krise – hier setzt dieses Deck an."),
    ((120, 120, 120), "GRAU", "Erschöpft/orientierungslos – erst beobachten, nicht vorschnell einordnen."),
]

FEUERWEHR_SCHRITTE = [
    ("1", "Sicherheit herstellen", "Abstand zur Gruppe, ruhigen Ort aufsuchen, körperliche Sicherheit prüfen."),
    ("2", "Kontakt halten", "Ruhige Stimme, wenig Worte. „Ich bin hier. Du bist sicher.“"),
    ("3", "Regulieren lassen", "Kein Erklären, kein Diskutieren. Den Körper regulieren lassen."),
    ("4", "TK informieren", "Teamkoordination unverzüglich in Kenntnis setzen."),
    ("5", "Nachgespräch (viel später)", "Erst wenn das Kind vollständig reguliert ist."),
]

def barometer_feuerwehr_seite():
    img, d, y = new_page("KURZ ERKLÄRT", "Barometer & Feuerwehr-Protokoll")
    y = draw_para(d, y, "Auch ohne die KLARTEXT-App nutzbar. Hier kurz, wo Barometer Rot im Gesamtsystem "
                        "steht und warum hier NICHT das kLAR-Modell gilt.",
                  size=4.4, color=KT_MUTED)
    y += mm(4)

    y = draw_h2(d, y, "Das Barometer – 5 Zustände")
    f_lab = ImageFont.truetype(F_SANS_BOLD, mm(4.8))
    f_desc = ImageFont.truetype(F_SANS_REG, mm(4.4))
    lab_w = mm(30)
    for color, label, desc in BAROMETER_KURZ:
        d.ellipse((MARGIN, y + mm(0.9), MARGIN + mm(3.6), y + mm(4.5)), fill=color)
        d.text((MARGIN + mm(6), y), label, font=f_lab, fill=KT_INK)
        lines = wrap(d, desc, f_desc, CONTENT_W - lab_w - mm(6))
        ly = y
        for ln in lines:
            d.text((MARGIN + lab_w, ly), ln, font=f_desc, fill=KT_MUTED)
            ly += mm(6.2)
        y = max(ly, y + mm(6.5)) + mm(1)
    y += mm(2)

    y = draw_h2(d, y, "Warum kein kLAR-Modell bei Rot?")
    y = draw_para(d, y, "kLAR (Kontakt, Leise & Langsam, Anerkennung & Atmen, Reizreduktion) ist für "
                        "Gelb und Orange gedacht – wenn ein Gespräch noch möglich ist. Bei Rot reicht "
                        "das nicht mehr: hier gilt ausschließlich das Feuerwehr-Protokoll.", size=4.4)
    y += mm(3)

    y = draw_h2(d, y, "Das Feuerwehr-Protokoll – 5 Schritte")
    for num, titel, text in FEUERWEHR_SCHRITTE:
        y = draw_numbered(d, y, num, titel, text, size=4.4)

    footer(d, "Barometer & Feuerwehr")
    return img

# ═══════════════════════════════════ QUELLEN ═══════════════════════════════════
QUELLEN_BESTAETIGT = [
    "SGB VIII § 8a (Schutzauftrag bei Kindeswohlgefährdung) – Grundlage für die Meldepflicht bei "
    "FK-04 und FK-05.",
    "Notruf 112 (Rettungsdienst/Feuerwehr), Polizei-Notruf 110 – amtliche Notrufnummern Deutschland.",
]

QUELLEN_VORGESCHLAGEN = [
    "Porges, S. W. – Polyvagal-Theorie (Dorsal-Vagus-/Freeze-Reaktion), zitiert als Hintergrund zu "
    "FK-02 Shutdown in der App (dort Jahresangabe 1994) – exakte Publikation/Jahr vor Druck prüfen, "
    "vermutlich Porges (1995), Psychophysiology.",
    "5-4-3-2-1-Erdungstechnik und Boxatmung (4-4-4-4) – etablierte Techniken aus Trauma- und "
    "Achtsamkeitspraxis (FK-03), keine einzelne Primärquelle zugeordnet.",
]

QUELLEN_HINWEIS = ("Die inhaltliche Grundlage für alle 8 Karten sind die bereits in der App bestehenden, "
    "fachlich hinterlegten Feuerwehrkarten FK-01–08 – das Krisendeck kürzt und adaptiert diesen Text "
    "für die physische Karte, erfindet keine neuen Handlungsanweisungen.")

def quellen_seite():
    img, d, y = new_page("METHODISCHE GRUNDLAGE", "Quellen")
    y = draw_para(d, y, QUELLEN_HINWEIS, size=4.6, color=KT_MUTED)
    y += mm(6)

    y = draw_para(d, y, "Etablierte, bereits verifizierte Quellen bzw. Rechtsgrundlagen:",
                  size=4.6, color=KT_MUTED)
    y += mm(4)
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

    footer(d, "Quellen")
    return img

if __name__ == "__main__":
    pages = {
        "krisendeck_anleitung1": anleitung_seite1(),
        "krisendeck_anleitung2": anleitung_seite2(),
        "krisendeck_hintergrund": hintergrund_seite(),
        "krisendeck_quellen": quellen_seite(),
    }
    for name, img in pages.items():
        img.save(f"/sessions/kind-beautiful-ptolemy/mnt/outputs/booklet_{name}.png")
        print(name, "ok")
