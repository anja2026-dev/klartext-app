#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Buendelt die 3 Ausfuell-Arbeitsblaetter aus dem bestehenden Anti-Mobbing-Training
(AM_DL_Klassenvertrag.html, AM_DL_Meine_Verbuendeten.html, AM_DL_So_melde_ich_Mobbing.html) als
eigenstaendiges Druck-PDF – Text/Struktur 1:1 aus den Original-HTML-Dateien uebernommen (Content-
Treuepflicht), nur als PIL-Nachbau statt Browser-Rendering (kein Headless-Chromium mit
Systemabhaengigkeiten in der Sandbox verfuegbar). Bleiben bewusst Einzelblaetter zum Ausfuellen,
kein Kartendeck – anders als Geschichtenkarten/Handlungskarten sind das personalisierte
Ausfuellvorlagen (Namen, Unterschriften), kein Lesematerial."""
from PIL import Image, ImageDraw, ImageFont
Image.init()

DPI = 300
MM = DPI / 25.4
def mm(v): return int(round(v * MM))

AM = (198, 40, 40)         # #C62828
AM_LIGHT = (255, 235, 238)  # #FFEBEE
AM_BORDER = (255, 205, 210) # #FFCDD2
DARK_RED = (139, 0, 0)      # #8B0000
INK = (45, 45, 45)
MUTED2 = (122, 96, 96)      # #7A6060
GREY = (170, 170, 170)

F_SERIF_BOLD = "/usr/share/fonts/truetype/crosextra/Caladea-Bold.ttf"
F_SANS_REG = "/usr/share/fonts/truetype/lato/Lato-Regular.ttf"
F_SANS_MED = "/usr/share/fonts/truetype/lato/Lato-Medium.ttf"
F_SANS_BOLD = "/usr/share/fonts/truetype/lato/Lato-Bold.ttf"

def font(path, size_mm):
    return ImageFont.truetype(path, mm(size_mm))

def wrap(draw, text, fnt, max_width):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_width:
            cur = t
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines

def page_header(d, W, titel, sub, pad):
    f_lab = font(F_SANS_BOLD, 2.6)
    d.text((pad, mm(10)), "KLARTEXT · DRUCKMATERIAL", font=f_lab, fill=AM)
    f_titel = font(F_SERIF_BOLD, 7.5)
    d.text((pad, mm(14)), titel, font=f_titel, fill=AM)
    f_sub = font(F_SANS_REG, 3.6)
    d.text((pad, mm(24)), sub, font=f_sub, fill=MUTED2)
    return mm(32)

# ═══════════════════════════ Seite 1: Klassenvertrag (A4 Hochformat) ═══════════════════════════
def seite_klassenvertrag():
    W, H = mm(210), mm(297)
    img = Image.new("RGB", (W, H), (255, 255, 255))
    d = ImageDraw.Draw(img)
    pad = mm(20)
    y = page_header(d, W, "Unser Klassenvertrag gegen Mobbing", "Gemeinsam beschlossen · Von allen unterschrieben", pad)
    y += mm(4)

    box_x0, box_y0, box_x1 = pad, y, W - pad
    d.rounded_rectangle((box_x0, box_y0, box_x1, box_y0 + mm(4)), radius=0, fill=None)  # placeholder skip
    y += mm(2)

    f_h = font(F_SANS_BOLD, 3.6)
    d.text((pad, y), "IN UNSERER KLASSE GELTEN DIESE REGELN:", font=f_h, fill=AM)
    y += mm(9)

    regeln = [
        ("Wir sagen Stopp.", "Wenn jemand Stopp sagt — wir hören sofort auf. Kein „War doch nur Spaß.“"),
        ("Wir schließen niemanden aus.", "Jede Person in unserer Klasse hat das Recht dazuzugehören."),
        ("Wir holen Hilfe.", "Wenn wir etwas sehen das nicht okay ist — wir sagen es einer Erwachsenen. Das ist kein Petzen."),
        ("Online gilt dasselbe wie offline.", "Was in der Schule nicht okay ist, ist auch per Handy und im Internet nicht okay."),
    ]
    f_nr = font(F_SANS_BOLD, 3.6)
    f_lab = font(F_SANS_BOLD, 4.0)
    f_txt = font(F_SANS_REG, 3.6)
    circle_s = mm(8)
    for i, (label, text) in enumerate(regeln, 1):
        d.ellipse((pad, y, pad + circle_s, y + circle_s), fill=AM)
        d.text((pad + circle_s / 2, y + circle_s / 2), str(i), font=f_nr, fill=(255, 255, 255), anchor="mm")
        tx = pad + circle_s + mm(4)
        d.text((tx, y), label, font=f_lab, fill=DARK_RED)
        ty = y + mm(5.5)
        for ln in wrap(d, text, f_txt, W - tx - pad):
            d.text((tx, ty), ln, font=f_txt, fill=(90, 48, 48))
            ty += mm(5.2)
        y = max(ty, y + circle_s) + mm(4)

    d.ellipse((pad, y, pad + circle_s, y + circle_s), fill=AM)
    d.text((pad + circle_s / 2, y + circle_s / 2), "5", font=f_nr, fill=(255, 255, 255), anchor="mm")
    tx = pad + circle_s + mm(4)
    d.text((tx, y), "Unsere eigene Regel:", font=f_lab, fill=DARK_RED)
    line_y = y + mm(9)
    d.line((tx, line_y, W - pad, line_y), fill=AM_BORDER, width=mm(0.4))
    y = line_y + mm(10)

    f_h2 = font(F_SANS_BOLD, 3.6)
    d.text((pad, y), "UNTERSCHRIFTEN:", font=f_h2, fill=AM)
    y += mm(8)
    cols = 3
    col_w = (W - 2 * pad - mm(10)) / cols
    for row in range(3):
        for c in range(cols):
            lx = pad + c * (col_w + mm(5))
            ly = y + row * mm(12)
            d.line((lx, ly, lx + col_w, ly), fill=AM_BORDER, width=mm(0.35))
    y += 3 * mm(12) + mm(6)

    d.line((pad, y, W - pad, y), fill=AM_BORDER, width=mm(0.3))
    y += mm(4)
    f_foot = font(F_SANS_REG, 2.8)
    d.text((pad, y), "KLARTEXT Anti-Mobbing-Training", font=f_foot, fill=GREY)
    d.text((W - pad - mm(45), y), "Datum: _______________", font=f_foot, fill=GREY)

    return img

# ═══════════════════════════ Seite 2: Meine Verbündeten (A4 Querformat) ═══════════════════════════
def seite_verbuendete():
    W, H = mm(297), mm(210)  # Querformat
    img = Image.new("RGB", (W, H), (255, 255, 255))
    d = ImageDraw.Draw(img)
    pad = mm(15)
    y = page_header(d, W, "Meine Verbündeten", "Wer ist für mich da? · Ausfüllen und aufbewahren", pad)
    y += mm(6)

    col_w = (W - 2 * pad - mm(15)) / 2
    box_h = H - y - mm(15)

    # Linke Spalte: Grundschule Sonnen-Diagramm
    x0 = pad
    d.rounded_rectangle((x0, y, x0 + col_w, y + box_h), radius=mm(4), outline=AM, width=mm(0.8))
    f_t = font(F_SERIF_BOLD, 4.2)
    tw = d.textlength("Meine Verbündeten (Grundschule)", font=f_t)
    d.text((x0 + (col_w - tw) / 2, y + mm(6)), "Meine Verbündeten (Grundschule)", font=f_t, fill=AM)

    cx, cy = x0 + col_w / 2, y + box_h / 2 + mm(4)
    r_inner, r_outer = mm(20), mm(30)
    labels = ["Mama/Papa", "Geschwister", "Freund:in", "Lehrer:in", "INGRA", "Oma/Opa", "Freund:in", "________"]
    import math
    f_ray = font(F_SANS_MED, 2.6)
    for i, lab in enumerate(labels):
        ang = -math.pi / 2 + i * (2 * math.pi / len(labels))
        x1, y1 = cx + r_inner * math.cos(ang), cy + r_inner * math.sin(ang)
        x2, y2 = cx + r_outer * math.cos(ang), cy + r_outer * math.sin(ang)
        d.line((x1, y1, x2, y2), fill=AM_BORDER, width=mm(0.8))
        lx, ly = cx + (r_outer + mm(4)) * math.cos(ang), cy + (r_outer + mm(4)) * math.sin(ang)
        lw = d.textlength(lab, font=f_ray)
        d.text((lx - lw / 2, ly - mm(2)), lab, font=f_ray, fill=DARK_RED)
    d.ellipse((cx - r_inner, cy - r_inner, cx + r_inner, cy + r_inner), fill=AM_LIGHT, outline=AM, width=mm(0.5))
    f_mid = font(F_SANS_BOLD, 3.0)
    d.text((cx, cy - mm(2)), "Ich bin", font=f_mid, fill=AM, anchor="mm")
    d.text((cx, cy + mm(3)), "nicht allein", font=f_mid, fill=AM, anchor="mm")

    f_hint = font(F_SANS_REG, 2.8)
    hint = "Schreibe die Namen deiner Verbündeten in die Strahlen."
    hw = d.textlength(hint, font=f_hint)
    d.text((x0 + (col_w - hw) / 2, y + box_h - mm(8)), hint, font=f_hint, fill=GREY)

    # Rechte Spalte: weiterführende Schule Unterstützungsnetz
    x1 = pad + col_w + mm(15)
    d.rounded_rectangle((x1, y, x1 + col_w, y + box_h), radius=mm(4), outline=AM, width=mm(0.8))
    f_t2 = font(F_SERIF_BOLD, 4.2)
    tw2 = d.textlength("Mein Unterstützungsnetz (weiterführende Schule)", font=f_t2)
    if tw2 > col_w - mm(10):
        f_t2 = font(F_SERIF_BOLD, 3.6)
    tw2 = d.textlength("Mein Unterstützungsnetz (weiterführende Schule)", font=f_t2)
    d.text((x1 + (col_w - tw2) / 2, y + mm(6)), "Mein Unterstützungsnetz (weiterführende Schule)", font=f_t2, fill=AM)

    ry = y + mm(16)
    gruppen = [
        ("Zuhause", 2), ("In der Schule", 2), ("Freunde", 2),
    ]
    f_glab = font(F_SANS_BOLD, 3.0)
    f_gline = font(F_SANS_REG, 3.2)
    for name, n_lines in gruppen:
        gx, gw = x1 + mm(6), col_w - mm(12)
        gh = mm(6) + n_lines * mm(7)
        d.rounded_rectangle((gx, ry, gx + gw, ry + gh), radius=mm(2), fill=AM_LIGHT)
        d.text((gx + mm(4), ry + mm(2)), name.upper(), font=f_glab, fill=AM)
        ly = ry + mm(8)
        for _ in range(n_lines):
            d.line((gx + mm(10), ly + mm(4.5), gx + gw - mm(4), ly + mm(4.5)), fill=AM_BORDER, width=mm(0.35))
            ly += mm(7)
        ry += gh + mm(3)

    gh2 = mm(14)
    d.rounded_rectangle((x1 + mm(6), ry, x1 + col_w - mm(6), ry + gh2), radius=mm(2), fill=AM_LIGHT)
    d.text((x1 + mm(10), ry + mm(2)), "NOTFALL-NUMMERN", font=f_glab, fill=AM)
    d.text((x1 + mm(10), ry + mm(7)), "Nummer gegen Kummer: 116 111  ·  Notruf: 110 / 112", font=f_gline, fill=(90, 48, 48))

    return img

# ═══════════════════════════ Seite 3: So melde ich Mobbing (A4 Hochformat) ═══════════════════════════
def seite_meldekarte():
    W, H = mm(210), mm(297)
    img = Image.new("RGB", (W, H), (255, 255, 255))
    d = ImageDraw.Draw(img)
    pad = mm(20)
    y = page_header(d, W, "So melde ich Mobbing", "Meine persönliche Meldekarte · Ausfüllen und mitnehmen", pad)
    y += mm(6)

    f_lab = font(F_SANS_BOLD, 3.2)
    f_txt = font(F_SANS_REG, 3.5)

    # Schritt 1
    box_h1 = mm(30)
    d.rounded_rectangle((pad, y, W - pad, y + box_h1), radius=mm(3), fill=AM_LIGHT)
    d.text((pad + mm(5), y + mm(3)), "SCHRITT 1 · AN WEN WENDE ICH MICH?", font=f_lab, fill=AM)
    zeilen = ["Meine INGRA / Schulbegleitung", "Meine Lehrkraft", "Zuhause"]
    zy = y + mm(9)
    for z in zeilen:
        d.text((pad + mm(5), zy), z, font=f_txt, fill=DARK_RED)
        d.line((pad + mm(5), zy + mm(5.5), W - pad - mm(5), zy + mm(5.5)), fill=AM_BORDER, width=mm(0.35))
        zy += mm(7)
    y += box_h1 + mm(5)

    # Schritt 2
    box_h2 = mm(32)
    d.rounded_rectangle((pad, y, W - pad, y + box_h2), radius=mm(3), fill=AM_LIGHT)
    d.text((pad + mm(5), y + mm(3)), "SCHRITT 2 · WAS SAGE ICH?", font=f_lab, fill=AM)
    saetze = ["„Ich möchte dir etwas sagen. Es passiert mir schon öfter…“",
              "„Ich brauche Hilfe. Ich weiß nicht mehr weiter.“",
              "„Kann ich dir etwas zeigen? Es geht um Nachrichten…“"]
    zy = y + mm(9)
    f_zit = font(F_SANS_REG, 3.2)
    for s in saetze:
        d.rounded_rectangle((pad + mm(5), zy, W - pad - mm(5), zy + mm(7)), radius=mm(1.5), fill=(255, 255, 255), outline=AM_BORDER, width=mm(0.3))
        d.text((pad + mm(7), zy + mm(1.8)), s, font=f_zit, fill=(90, 48, 48))
        zy += mm(8)
    y += box_h2 + mm(5)

    # Schritt 3
    box_h3 = mm(26)
    d.rounded_rectangle((pad, y, W - pad, y + box_h3), radius=mm(3), fill=AM_LIGHT)
    d.text((pad + mm(5), y + mm(3)), "SCHRITT 3 · WAS PASSIERT DANN?", font=f_lab, fill=AM)
    schritte = ["Die Person hört dir zu", "Wir dokumentieren gemeinsam was passiert ist",
                "Wir informieren die richtigen Personen", "Es wird etwas unternommen"]
    zy = y + mm(9)
    for i, s in enumerate(schritte, 1):
        d.text((pad + mm(5), zy), f"{i}.", font=f_txt, fill=AM)
        d.text((pad + mm(11), zy), s, font=f_txt, fill=(90, 48, 48))
        zy += mm(4.6)
    y += box_h3 + mm(5)

    # Notfallbox
    box_h4 = mm(20)
    d.rounded_rectangle((pad, y, W - pad, y + box_h4), radius=mm(3), fill=AM)
    f_not_lab = font(F_SANS_BOLD, 3.4)
    f_not_num = font(F_SANS_BOLD, 5.5)
    f_not_sub = font(F_SANS_REG, 2.6)
    t1 = "Notfall: Nummer gegen Kummer"
    tw1 = d.textlength(t1, font=f_not_lab)
    d.text((pad + (W - 2 * pad - tw1) / 2, y + mm(3)), t1, font=f_not_lab, fill=(255, 255, 255))
    t2 = "116 111"
    tw2 = d.textlength(t2, font=f_not_num)
    d.text((pad + (W - 2 * pad - tw2) / 2, y + mm(8)), t2, font=f_not_num, fill=AM_BORDER)
    t3 = "Kostenlos · Anonym · Mo–Sa 14–20 Uhr"
    tw3 = d.textlength(t3, font=f_not_sub)
    d.text((pad + (W - 2 * pad - tw3) / 2, y + mm(16)), t3, font=f_not_sub, fill=(255, 255, 255, 180))

    return img

def build_cover():
    W, H = mm(210), mm(297)
    img = Image.new("RGB", (W, H), (255, 255, 255))
    d = ImageDraw.Draw(img)
    kopf_h = mm(60)
    d.rectangle((0, 0, W, kopf_h), fill=AM)
    logo_s = mm(20)
    logo_y = (kopf_h - logo_s) // 2
    d.rounded_rectangle((mm(20), logo_y, mm(20) + logo_s, logo_y + logo_s), radius=mm(4),
                         fill=(27, 58, 75), outline=(110, 198, 160), width=mm(1.2))
    f_logo = font(F_SERIF_BOLD, 11)
    d.text((mm(20) + logo_s / 2, logo_y + logo_s / 2), "K", font=f_logo, anchor="mm", fill=(255, 255, 255))
    f_titel = font(F_SERIF_BOLD, 11)
    d.text((mm(48), mm(21)), "KLARTEXT-Mentoring", font=f_titel, fill=(255, 255, 255))
    f_sub = font(F_SANS_REG, 5.5)
    d.text((mm(48), mm(34)), "Anti-Mobbing-Training · Arbeitsmaterialien", font=f_sub, fill=(255, 220, 220))

    f_haupt = font(F_SERIF_BOLD, 14)
    d.text((mm(20), mm(90)), "Arbeitsmaterialien-Set", font=f_haupt, fill=AM)
    f_haupt2 = font(F_SANS_BOLD, 7)
    d.text((mm(20), mm(115)), "3 Ausfüllvorlagen aus dem Anti-Mobbing-Training", font=f_haupt2, fill=INK)

    f_label = font(F_SANS_BOLD, 5.5)
    d.text((mm(20), mm(133)), "DIE 3 VORLAGEN", font=f_label, fill=AM)
    themen = ["Unser Klassenvertrag – zum gemeinsamen Unterschreiben",
              "Meine Verbündeten – Grundschule & weiterführende Schule",
              "So melde ich Mobbing – persönliche Meldekarte"]
    f_thema = font(F_SANS_REG, 5.0)
    row_h = mm(9.4)
    for i, t in enumerate(themen):
        x = mm(20)
        y = mm(143) + i * row_h
        d.ellipse((x, y + mm(2.0), x + mm(2.6), y + mm(4.6)), fill=AM)
        lines = wrap(d, t, f_thema, W - mm(46))
        d.text((x + mm(6), y), lines[0], font=f_thema, fill=INK)

    para = ("Ergänzt das Soforthilfe-Mini-Deck (INGRA-Schnellreferenz) um die kindgerichtete Seite: "
            "Vorlagen zum Ausfüllen, Unterschreiben und Mitnehmen. Text unverändert aus dem "
            "bestehenden Anti-Mobbing-Training übernommen.")
    y = mm(180)
    f_p = font(F_SANS_REG, 4.4)
    for ln in wrap(d, para, f_p, W - mm(40)):
        d.text((mm(20), y), ln, font=f_p, fill=INK)
        y += mm(6)

    box_y = mm(240)
    box_h = mm(22)
    d.rounded_rectangle((mm(20), box_y, W - mm(20), box_y + box_h), radius=mm(3), fill=AM_LIGHT)
    f_status_l = font(F_SANS_BOLD, 6)
    f_status = font(F_SANS_REG, 5.6)
    d.text((mm(28), box_y + mm(6)), "STAND DIESER AUSGABE", font=f_status_l, fill=AM)
    d.text((mm(28), box_y + mm(13)), "3 Vorlagen vollständig, unverändert aus der App übernommen.",
           font=f_status, fill=INK)

    f_foot = font(F_SANS_REG, 5)
    d.text((mm(20), H - mm(18)), "KLARTEXT-Mentoring · © 2026 Anja Jolk", font=f_foot, fill=MUTED2)
    return img

def run():
    out_pdf = "/sessions/kind-beautiful-ptolemy/mnt/outputs/KLARTEXT_AntiMobbing_Arbeitsmaterialien.pdf"
    pages = [build_cover(), seite_klassenvertrag(), seite_verbuendete(), seite_meldekarte()]
    first, rest = pages[0], pages[1:]
    first.save(out_pdf, save_all=True, append_images=rest, resolution=DPI)
    print(f"PDF fertig: {out_pdf} ({len(pages)} Seiten)")

if __name__ == "__main__":
    run()
