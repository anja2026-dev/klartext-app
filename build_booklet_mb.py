#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Anleitung + Quellenverzeichnis fürs Mobbing-Interventionsdeck (15 Karten). Helfer von
build_booklet_werkzeug.py übernommen."""
from PIL import Image, ImageDraw, ImageFont
Image.init()

DPI = 300
MM = DPI / 25.4
def mm(v): return int(round(v * MM))

MB = (216, 27, 96)
MB_LIGHT = (253, 232, 241)
KT_INK = (45, 45, 45)
KT_MUTED = (122, 112, 96)
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
    d.rectangle((0, 0, W, kopf_h), fill=MB)
    d.text((MARGIN, mm(10)), kicker, font=f_kicker, fill=(255, 220, 235))
    ty = mm(17)
    for ln in lines:
        d.text((MARGIN, ty), ln, font=f_titel, fill=(255, 255, 255))
        ty += mm(size * 1.35)
    return img, d, kopf_h + mm(14)

def footer(d, page_label):
    f = ImageFont.truetype(F_SANS_REG, mm(4))
    d.text((MARGIN, H - mm(14)), "KLARTEXT-Mentoring · Mobbing-Intervention · © 2026 Anja Jolk", font=f, fill=KT_MUTED)
    w = d.textlength(page_label, font=f)
    d.text((W - MARGIN - w, H - mm(14)), page_label, font=f, fill=KT_MUTED)

def draw_h2(d, y, text):
    f = ImageFont.truetype(F_SERIF_BOLD, mm(6.5))
    d.text((MARGIN, y), text, font=f, fill=MB)
    return y + mm(9)

def draw_para(d, y, text, size=4.6, color=KT_INK, font_path=F_SANS_REG):
    f = ImageFont.truetype(font_path, mm(size))
    lh = mm(size * 1.55)
    for ln in wrap(d, text, f, CONTENT_W):
        d.text((MARGIN, y), ln, font=f, fill=color)
        y += lh
    return y

def draw_bullet(d, y, text, size=4.6):
    f = ImageFont.truetype(F_SANS_REG, mm(size))
    d.ellipse((MARGIN, y + mm(1.6), MARGIN + mm(1.6), y + mm(3.2)), fill=MB)
    lh = mm(size * 1.55)
    for ln in wrap(d, text, f, CONTENT_W - mm(7)):
        d.text((MARGIN + mm(6), y), ln, font=f, fill=KT_INK)
        y += lh
    return y + mm(1.5)

def anleitung_seite():
    img, d, y = new_page("GEBRAUCHSANWEISUNG", "Anleitung: Mobbing-Interventionsdeck")

    y = draw_h2(d, y, "Was ist dieses Deck?")
    y = draw_para(d, y, "15 Karten mit sofort abrufbarer Handlungssicherheit rund um Mobbing – für "
                        "Schulbegleitung und Teamkoordination. Deckt den gesamten Bogen ab: Erkennen, "
                        "Sofortmaßnahmen, Cybermobbing, Gruppendynamik, Zusammenarbeit mit Lehrkraft "
                        "und Eltern, Prävention, koordinierte Gruppenintervention und Nachsorge. "
                        "Direkt aus den 15 fachlich geprüften App-Modulseiten M6-01 bis M6-15 "
                        "kondensiert – diese bleiben zusätzlich als ausführliches Nachschlagewerk "
                        "in der App verfügbar.")
    y += mm(5)

    y = draw_h2(d, y, "Die 15 Karten")
    y = draw_para(d, y, "SOFORTMASSNAHMEN & ERKENNEN", size=4.0, color=MB, font_path=F_SANS_BOLD)
    y = draw_bullet(d, y, "MB-01 · Was tun bei Mobbing? – 8 Sofortschritte bei akuter Situation.")
    y = draw_bullet(d, y, "MB-02 · Mobbing erkennen – 8 Anzeichen zur frühzeitigen Einschätzung.")
    y = draw_bullet(d, y, "MB-03 · Digitale Spuren sichern – 10 Schritte bei Cybermobbing.")
    y = draw_bullet(d, y, "MB-04 · Cybermobbing – was digitale Gewalt besonders macht.")
    y += mm(2)
    y = draw_para(d, y, "GRUPPENDYNAMIK VERSTEHEN", size=4.0, color=MB, font_path=F_SANS_BOLD)
    y = draw_bullet(d, y, "MB-05 · Die Rollen im Mobbing-System – Täter, Mitläufer, Verteidiger & Co.")
    y = draw_bullet(d, y, "MB-06 · Täter-Opfer-Umkehr erkennen – die gefährlichste Fehleinschätzung.")
    y += mm(2)
    y = draw_para(d, y, "ZUSAMMENARBEIT", size=4.0, color=MB, font_path=F_SANS_BOLD)
    y = draw_bullet(d, y, "MB-07 · Mobbing und Lehrkraft – klare Aufgabenteilung.")
    y = draw_bullet(d, y, "MB-08 · Elterngespräch bei Mobbing – Rolle und Grenzen von INGRA.")
    y = draw_bullet(d, y, "MB-09 · Wenn INGRA selbst betroffen ist – Selbstschutz und Grenzen.")
    y += mm(2)
    y = draw_para(d, y, "PRÄVENTION & INTERVENTION", size=4.0, color=MB, font_path=F_SANS_BOLD)
    y = draw_bullet(d, y, "MB-10 · Prävention im Klassenzimmer – täglich mögliche Schritte.")
    y = draw_bullet(d, y, "MB-11 · Gruppenintervention Step by Step – 5 koordinierte Phasen.")
    y = draw_bullet(d, y, "MB-12 · No-Blame-Approach – die Methode kennen und einordnen.")
    y = draw_bullet(d, y, "MB-13 · Verteidiger stärken – die wirksamste Prävention über die Gruppe.")
    y += mm(2)
    y = draw_para(d, y, "NACHHALTIGKEIT", size=4.0, color=MB, font_path=F_SANS_BOLD)
    y = draw_bullet(d, y, "MB-14 · Eltern informieren & einbeziehen – aktive Zusammenarbeit gestalten.")
    y = draw_bullet(d, y, "MB-15 · Nachsorge nach dem Mobbing – Rückfälle verhindern.")

    footer(d, "Anleitung")
    return img

def herkunft_seite():
    img, d, y = new_page("QUELLEN & HERKUNFT", "Herkunft der Inhalte & Quellenverzeichnis")

    y = draw_h2(d, y, "Herkunft der Inhalte")
    y = draw_para(d, y, "MB-01 bis MB-03 sind unverändert aus den bereits bestehenden, geprüften "
                        "App-Vorlagen übernommen (Mini-Krisenkarte, Mini-Checkliste Erkennen, "
                        "Digitale Spuren sichern). MB-04 bis MB-15 sind aus den fachlich geprüften "
                        "App-Modulseiten M6-03 bis M6-15 kondensiert: Kernaussagen, Reihenfolge und "
                        "Zitate wurden inhaltlich unverändert übernommen, nur auf Kartenformat "
                        "gekürzt (Content-Treuepflicht) – es wurden keine neuen fachlichen Aussagen "
                        "hinzuerfunden. Die vollständigen Modulseiten bleiben als Nachschlagewerk in "
                        "der App verfügbar.")
    y += mm(6)

    y = draw_h2(d, y, "Quellenverzeichnis")
    quellen = [
        "Olweus, D. (1993). Bullying at School: What We Know and What We Can Do. Blackwell.",
        "Schäfer, M. (2010). Bullying im Schulkontext. Beltz.",
        "Rose, C. A., Monda-Amaya, L. E. & Espelage, D. L. (2011). Bullying Perpetration and "
        "Victimization in Special Education: A Review of the Literature. Exceptional Children.",
        "Salmivalli, C., Lagerspetz, K., Björkqvist, K., Österman, K. & Kaukiainen, A. (1996). "
        "Bullying as a Group Process: Participant Roles and Their Relations to Social Status "
        "within the Group. Aggressive Behavior.",
        "Salmivalli, C. (2010). Bullying and the Peer Group: A Review. Aggression and Violent "
        "Behavior.",
        "Salmivalli, C., Kärnä, A. & Poskiparta, E. (2011). Counteracting Bullying in Finland: "
        "The KiVa Program and Its Effects on Different Forms of Being Bullied. International "
        "Journal of Behavioral Development.",
        "Maines, B. & Robinson, G. (1992). The No Blame Approach. Lucky Duck Publishing.",
        "Bundesministerium für Bildung und Forschung – BMBF (2022). Mobbing an Schulen.",
    ]
    for q in quellen:
        y = draw_bullet(d, y, q, size=4.3)

    footer(d, "Quellen")
    return img

if __name__ == "__main__":
    img1 = anleitung_seite()
    img1.save("/sessions/kind-beautiful-ptolemy/mnt/outputs/booklet_mb_anleitung.png")
    img2 = herkunft_seite()
    img2.save("/sessions/kind-beautiful-ptolemy/mnt/outputs/booklet_mb_quellen.png")
    print("mb_anleitung + mb_quellen ok")
