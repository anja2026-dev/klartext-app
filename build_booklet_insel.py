#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kondensierte 2-Seiten-Handbuch-Booklets fürs Insel-Set (Eltern/INGRA/LK), Inhalt aus
Eltern-Insel-Mini-Handbuch.md / INGRA-Insel-Mini-Handbuch.md / LK-Insel-Mini-Handbuch.md."""
from PIL import Image, ImageDraw, ImageFont
import qrcode
Image.init()

DPI = 300
MM = DPI / 25.4
def mm(v): return int(round(v * MM))

KT_PRIMARY = (27, 58, 75)
KT_ACCENT = (110, 198, 160)
KT_INK = (45, 45, 45)
KT_MUTED = (122, 112, 96)

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
    size = 10.0
    f_titel = ImageFont.truetype(F_SERIF_BOLD, mm(size))
    while d.textlength(titel, font=f_titel) > CONTENT_W and size > 6:
        size -= 0.5
        f_titel = ImageFont.truetype(F_SERIF_BOLD, mm(size))
    lines = wrap(d, titel, f_titel, CONTENT_W)
    kopf_h = mm(22) + len(lines) * mm(size * 1.35)
    d.rectangle((0, 0, W, kopf_h), fill=KT_PRIMARY)
    d.text((MARGIN, mm(9)), kicker, font=f_kicker, fill=KT_ACCENT)
    ty = mm(16)
    for ln in lines:
        d.text((MARGIN, ty), ln, font=f_titel, fill=(255, 255, 255))
        ty += mm(size * 1.35)
    return img, d, kopf_h + mm(12)

def footer(d, deckname, page_label):
    f = ImageFont.truetype(F_SANS_REG, mm(4))
    d.text((MARGIN, H - mm(14)), f"KLARTEXT-Mentoring · {deckname} · © 2026 Anja Jolk", font=f, fill=KT_MUTED)
    w = d.textlength(page_label, font=f)
    d.text((W - MARGIN - w, H - mm(14)), page_label, font=f, fill=KT_MUTED)

def draw_h2(d, y, text):
    f = ImageFont.truetype(F_SERIF_BOLD, mm(6))
    d.text((MARGIN, y), text, font=f, fill=KT_PRIMARY)
    return y + mm(8.5)

def draw_para(d, y, text, size=4.4, color=KT_INK):
    f = ImageFont.truetype(F_SANS_REG, mm(size))
    lh = mm(size * 1.5)
    for ln in wrap(d, text, f, CONTENT_W):
        d.text((MARGIN, y), ln, font=f, fill=color)
        y += lh
    return y

def draw_bullet(d, y, text, size=4.3):
    f = ImageFont.truetype(F_SANS_REG, mm(size))
    d.ellipse((MARGIN, y + mm(1.5), MARGIN + mm(1.6), y + mm(3.1)), fill=KT_PRIMARY)
    lh = mm(size * 1.5)
    lines = wrap(d, text, f, CONTENT_W - mm(7))
    for ln in lines:
        d.text((MARGIN + mm(6), y), ln, font=f, fill=KT_INK)
        y += lh
    return y + mm(1.2)

def draw_numbered_short(d, y, num, text, size=4.3):
    f_num = ImageFont.truetype(F_SANS_BOLD, mm(4.6))
    d.ellipse((MARGIN, y, MARGIN + mm(6.5), y + mm(6.5)), fill=KT_ACCENT)
    d.text((MARGIN + mm(3.25), y + mm(3.25)), str(num), font=f_num, anchor="mm", fill=KT_PRIMARY)
    f_text = ImageFont.truetype(F_SANS_REG, mm(size))
    lines = wrap(d, text, f_text, CONTENT_W - mm(10))
    ty = y + mm(0.3)
    for ln in lines:
        d.text((MARGIN + mm(10), ty), ln, font=f_text, fill=KT_INK)
        ty += mm(size * 1.5)
    return max(ty, y + mm(8)) + mm(2.5)

def draw_digitalzugang(img, d, y, url, code):
    f_h2 = ImageFont.truetype(F_SERIF_BOLD, mm(5))
    d.text((MARGIN, y), "Digitaler Zugang", font=f_h2, fill=KT_PRIMARY)
    y += mm(6.5)
    qr_px = mm(18)
    qr = qrcode.QRCode(border=1, box_size=10, error_correction=qrcode.constants.ERROR_CORRECT_M)
    qr.add_data(url)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color=KT_PRIMARY, back_color="white").convert("RGB").resize((qr_px, qr_px))
    img.paste(qr_img, (MARGIN, y))
    tx = MARGIN + qr_px + mm(5)
    f1 = ImageFont.truetype(F_SANS_REG, mm(3.9))
    ty = y
    for ln in wrap(d, "QR-Code = digitale Flip-Card-Version. Freischaltcode:", f1, W - tx - MARGIN):
        d.text((tx, ty), ln, font=f1, fill=KT_INK)
        ty += mm(5.6)
    f_code = ImageFont.truetype(F_SERIF_BOLD, mm(5.5))
    d.text((tx, ty), code, font=f_code, fill=KT_PRIMARY)
    ty += mm(7.5)
    f2 = ImageFont.truetype(F_SANS_REG, mm(3.5))
    for ln in wrap(d, "Kein Login noetig - Code beim ersten Oeffnen des Decks eingeben.", f2, W - tx - MARGIN):
        d.text((tx, ty), ln, font=f2, fill=KT_MUTED)
        ty += mm(4.8)
    return max(ty, y + qr_px) + mm(3)

MINI_ANLEITUNG = [
    "Badge-Vorlage ausdrucken (zuhause, Copyshop oder – für INGRA/LK – über den Schuldrucker)",
    "Laminieren – schützt vor Abnutzung an Boden oder Wand",
    "Befestigen: doppelseitiges Klebeband (Wand/Boden) ODER lochen und aufhängen (Haken/Kordel)",
    "Fertige Vinyl-Aufkleber gibt es optional auf Anfrage, kein Standard-Bestandteil des Sets",
]

INSELN_8 = ["Regel-Insel", "Ruhe-Insel", "Arbeits-Insel", "Bewegungs-Insel", "Kreativ-Insel",
            "Gesprächs-Insel", "Emotions-Insel", "Material-Insel"]
INSELN_ELTERN = ["Ruhe-Insel", "Emotions-Insel", "Arbeits-Insel (Hausaufgaben)", "Bewegungs-Insel",
                 "Familien-Regel-Insel", "Übergangs-Insel", "Geschwister-Konflikt-Insel",
                 "Eltern-Kind-Gesprächs-Insel"]

def _seite1(deckname, ziel_text, inseln_liste, extra_h2=None, extra_text=None):
    img, d, y = new_page("GEBRAUCHSANWEISUNG", f"Insel-Set – {deckname}")
    y = draw_h2(d, y, "Ziel")
    y = draw_para(d, y, ziel_text)
    y += mm(6)
    y = draw_h2(d, y, "Prinzipien")
    for p in ["Visuelle Strukturierung statt wiederholter Ansagen", "Klare, wenige, immer gleiche Regeln",
              "Wiederkehrende Rituale", "Selbstständige Nutzung", "Entlastung im Alltag"]:
        y = draw_bullet(d, y, p)
    y += mm(4)
    y = draw_h2(d, y, "Die 8 Inseln")
    y = draw_para(d, y, " · ".join(inseln_liste), size=4.2, color=KT_MUTED)
    if extra_h2:
        y += mm(6)
        y = draw_h2(d, y, extra_h2)
        y = draw_para(d, y, extra_text)
    footer(d, deckname, "Handbuch · 1/2")
    return img

def _seite2(deckname, umsetzung_schritte, quellen, quellen_hinweis, qr_url=None, qr_code=None):
    img, d, y = new_page("GEBRAUCHSANWEISUNG", "Umsetzung, Anleitung & Quellen")
    y = draw_h2(d, y, "Umsetzung")
    for i, s in enumerate(umsetzung_schritte, 1):
        y = draw_numbered_short(d, y, i, s)
    y += mm(4)
    y = draw_h2(d, y, "Mini-Anleitung: Insel-Badge anbringen")
    for i, s in enumerate(MINI_ANLEITUNG, 1):
        y = draw_numbered_short(d, y, i, s)
    y += mm(4)
    y = draw_h2(d, y, "Quellen")
    f_q = ImageFont.truetype(F_SANS_REG, mm(4.1))
    for q in quellen:
        for ln in wrap(d, q, f_q, CONTENT_W - mm(4)):
            d.text((MARGIN + mm(4), y), ln, font=f_q, fill=KT_INK)
            y += mm(6.3)
        y += mm(1.5)
    y += mm(2)
    y = draw_para(d, y, quellen_hinweis, size=3.9, color=(150, 120, 50))
    if qr_url:
        y += mm(2)
        y = draw_digitalzugang(img, d, y, qr_url, qr_code)
    footer(d, deckname, "Handbuch · 2/2")
    return img

def eltern_seite1():
    return _seite1("Zuhause (Eltern)",
        "Kinder brauchen klare, visuelle und räumliche Orientierung, um sich selbstständig regulieren, "
        "Konflikte lösen und Übergänge bewältigen zu können. Das Insel-System bietet einfache, "
        "kindgerechte Strukturen für den Familienalltag.",
        INSELN_ELTERN)

def eltern_seite2():
    return _seite2("Zuhause (Eltern)",
        ["Inseln markieren (Symbol + Farbe) – Vorlage ausdrucken, siehe Mini-Anleitung",
         "Regeln kurz erklären – nicht mehr als 2–3 Sätze pro Insel",
         "Nutzung ritualisieren, z. B. an einem ruhigen Wochenende einführen",
         "Regelmäßig reflektieren – was funktioniert, was nicht"],
        ["Mesibov, Shea & Schopler (2005). The TEACCH Approach to Autism Spectrum Disorders.",
         "Hodgdon, L. (1995). Visual Strategies for Improving Communication.",
         "Dunn, W. (1997). The impact of sensory processing abilities on daily life. Infants & Young Children.",
         "Fiese, B. et al. (2002). 50 years of research on family routines and rituals. J. of Family Psychology.",
         "Brackett, M. & Rivers, S. (2014). Transforming students' lives with social and emotional learning."],
        "5 von 6 Quellen geprüft und zitierfähig. Zimmer (2010) „Selbstregulation im Kindesalter“ – "
        "exakter Titel nicht bestätigt, vor Druck gegenprüfen.",
        qr_url="https://karten.klartext-mentoring.de/?deck=insel-eltern",
        qr_code="hc7msv")

def ingra_seite1():
    return _seite1("INGRA",
        "Für INGRA ist das Insel-Set die physische Ebene zu Barometer und kLAR-Modell: ein konkreter "
        "Ort für das, was sonst nur als Zustand (Barometer) und Skript (kLAR) existiert.",
        INSELN_8, extra_h2="Einbindung in Barometer & kLAR",
        extra_text="Grün: alle Inseln frei. Gelb: Regel-/Ruhe-Insel selbstständig (Joker-Mechanismus). "
                   "Orange: Ruhe-Insel = kLAR-Schritt R, Emotions-Insel = kLAR-Schritt A, INGRA begleitet "
                   "aktiv. Rot: keine freie Wahl, Feuerwehr-Protokoll gilt. Grau: erschöpft oder "
                   "orientierungslos – weiß selbst nicht, was es braucht. Ruhe-Insel, nicht drängen.")

def ingra_seite2():
    return _seite2("INGRA",
        ["Inseln markieren (Symbol + Farbe) – Vorlage über Schuldrucker ausdrucken",
         "Regeln kurz erklären, im Ritual verankern (z. B. Morgenkreis)",
         "Bei Gelb/Orange aktiv auf die passende Insel verweisen",
         "Regelmäßig reflektieren, ob die Zuordnung fürs jeweilige Kind noch passt"],
        ["Porges, S. (2011). Polyvagal-Theorie – bereits im KLARTEXT-Register bestätigt.",
         "Mesibov, Shea & Schopler (2005). The TEACCH Approach to Autism Spectrum Disorders.",
         "Siegel, D. (1999). Window of Tolerance.",
         "Kuypers, L. (2011). Zones of Regulation.",
         "Calming Corners – PBIS-/traumainformierte Forschung, 29.07.2026 recherchiert."],
        "Porges 2011 bestätigt. Mesibov/Shea/Schopler, Siegel als „vorgeschlagen, bitte gegenprüfen“ "
        "markiert. Kuypers/Calming Corners eigenständig recherchiert und belegt.",
        qr_url="https://karten.klartext-mentoring.de/?deck=insel-schule",
        qr_code="h1qf9m")

def lk_seite1():
    return _seite1("Lehrkräfte",
        "Für die Lehrkraft ist das Insel-Set ein Klassenraum-Management-Element: es reduziert die Zahl "
        "der Situationen, in denen die ganze Klasse für ein einzelnes Kind unterbrochen werden muss.",
        INSELN_8, extra_h2="Einbindung in den Unterrichtsalltag",
        extra_text="Kernprinzip „Withitness“ (Kounin): früh bemerken, kurz und gezielt lenken, ohne den "
                   "Unterricht zu stoppen. Übergänge sind die naheliegendsten Momente für Insel-Nutzung. "
                   "Insel-Nutzung positiv erwähnen (CHAMPS/PBIS), nicht nur bei Problemen ansprechen.")

def lk_seite2():
    return _seite2("Lehrkräfte",
        ["Inseln markieren, Platz im Klassenraum fest einplanen",
         "Regeln einmal für die ganze Klasse einführen",
         "Bei Unruhe kurz und gezielt auf die passende Insel verweisen",
         "Regelmäßig reflektieren, ob die Klasse die Inseln wie vorgesehen nutzt"],
        ["Marzano, R. & Pickering, D. (2003). Classroom Management That Works.",
         "Kounin, J. (1970). Discipline and Group Management in Classrooms.",
         "Sprick, R. – CHAMPS: A Proactive and Positive Approach to Classroom Management.",
         "PBIS-Rahmenwerk (Positive Behavioral Interventions and Supports, OSEP)."],
        "Alle vier Quellen im bestehenden LK-Classroom-Management-Konzept bereits als „vorgeschlagen, "
        "bitte gegenprüfen“ markiert – gleicher Status hier übernommen.",
        qr_url="https://karten.klartext-mentoring.de/?deck=insel-schule",
        qr_code="h1qf9m")

if __name__ == "__main__":
    pages = {
        "insel_eltern1": eltern_seite1(), "insel_eltern2": eltern_seite2(),
        "insel_ingra1": ingra_seite1(), "insel_ingra2": ingra_seite2(),
        "insel_lk1": lk_seite1(), "insel_lk2": lk_seite2(),
    }
    for name, img in pages.items():
        img.save(f"/sessions/kind-beautiful-ptolemy/mnt/outputs/booklet_{name}.png")
        print(name, "ok")
