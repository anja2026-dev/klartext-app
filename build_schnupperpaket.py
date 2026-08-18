#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baut das KLARTEXT-Schnupperpaket: 8 Karten (4x M3-Werkzeugkarten, 2x KD, 2x JD) als
Gratis-PDF, Cover + Karten + Schluss-/Cross-Sell-Seite. Nutzt die bestehenden Karten-Renderer."""
from PIL import Image, ImageDraw, ImageFont
import os, sys
Image.init()

APP_DIR = "/sessions/tender-trusting-franklin/mnt/klartext-app"
sys.path.insert(0, APP_DIR)

# Bild-/Font-Pfade der bestehenden Skripte zeigen auf eine alte Session -> patchen wir hier
import build_card_kd, build_card_jd, build_card_werkzeug

OUT_DIR = "/sessions/tender-trusting-franklin/mnt/outputs/schnupper_karten/"
os.makedirs(OUT_DIR, exist_ok=True)
OUT_PDF = "/sessions/tender-trusting-franklin/mnt/outputs/KLARTEXT_Schnupperpaket.pdf"

DPI = 300
MM = DPI / 25.4
def mm(v): return int(round(v * MM))

KT_PRIMARY = (27, 58, 75)     # #1B3A4B
KT_ACCENT  = (110, 198, 160)  # #6EC6A0
KT_INK     = (45, 45, 45)
KT_MUTED   = (122, 112, 96)

F_SERIF_BOLD = "/usr/share/fonts/truetype/crosextra/Caladea-Bold.ttf"
F_SANS_REG   = "/usr/share/fonts/truetype/lato/Lato-Regular.ttf"
F_SANS_BOLD  = "/usr/share/fonts/truetype/lato/Lato-Bold.ttf"

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

# ═══════════════════════ COVER ═══════════════════════
def build_cover():
    W, H = mm(210), mm(297)
    img = Image.new("RGB", (W, H), (255, 255, 255))
    d = ImageDraw.Draw(img)

    kopf_h = mm(60)
    d.rectangle((0, 0, W, kopf_h), fill=KT_PRIMARY)
    logo_s = mm(20)
    logo_y = (kopf_h - logo_s) // 2
    d.rounded_rectangle((mm(20), logo_y, mm(20) + logo_s, logo_y + logo_s), radius=mm(4),
                         fill=KT_PRIMARY, outline=KT_ACCENT, width=mm(1.2))
    f_logo = ImageFont.truetype(F_SERIF_BOLD, mm(11))
    d.text((mm(20) + logo_s / 2, logo_y + logo_s / 2), "K", font=f_logo, anchor="mm", fill=(255, 255, 255))

    f_titel = ImageFont.truetype(F_SERIF_BOLD, mm(11))
    d.text((mm(48), mm(21)), "KLARTEXT-Mentoring", font=f_titel, fill=(255, 255, 255))
    f_sub = ImageFont.truetype(F_SANS_REG, mm(5.5))
    d.text((mm(48), mm(34)), "Kostenlose Kostprobe aus drei Kartendecks", font=f_sub, fill=(220, 240, 230))

    f_haupt = ImageFont.truetype(F_SERIF_BOLD, mm(18))
    for i, ln in enumerate(["KLARTEXT-", "Schnupperpaket"]):
        d.text((mm(20), mm(85) + i * mm(21)), ln, font=f_haupt, fill=KT_PRIMARY)

    f_haupt2 = ImageFont.truetype(F_SANS_BOLD, mm(6.5))
    d.text((mm(20), mm(133)), "8 Karten aus 3 Decks – zum Ausprobieren, kostenlos.", font=f_haupt2, fill=KT_INK)

    f_lab = ImageFont.truetype(F_SANS_BOLD, mm(5.5))
    d.text((mm(20), mm(150)), "DIESE KARTEN SIND DABEI", font=f_lab, fill=KT_ACCENT2 if False else (110,150,130))
    d.text((mm(20), mm(150)), "DIESE KARTEN SIND DABEI", font=f_lab, fill=(74, 134, 108))

    themen = [
        ("WERKZEUGKARTEN", ["Kind kommt aufgewühlt an", "Übergang zwischen Situationen",
                             "Mini-Pause", "Lob-Sandwich"]),
        ("KD · KINDERCOACHING", ["Wie geht es mir heute?", "Was ist ein guter Freund?"]),
        ("JD · JUGENDCOACHING", ["Meine Stärken sehen", "Nein sagen können"]),
    ]
    f_grp = ImageFont.truetype(F_SANS_BOLD, mm(4.6))
    f_item = ImageFont.truetype(F_SANS_REG, mm(5.0))
    y = mm(159)
    for grp, items in themen:
        d.text((mm(20), y), grp, font=f_grp, fill=KT_PRIMARY)
        y += mm(7)
        for t in items:
            d.ellipse((mm(20), y + mm(1.8), mm(20) + mm(2.4), y + mm(4.2)), fill=KT_ACCENT)
            d.text((mm(25), y), t, font=f_item, fill=KT_INK)
            y += mm(6.6)
        y += mm(3)

    box_y = mm(258)
    box_h = mm(22)
    d.rounded_rectangle((mm(20), box_y, W - mm(20), box_y + box_h), radius=mm(3), fill=(232, 245, 238))
    f_status_l = ImageFont.truetype(F_SANS_BOLD, mm(5.5))
    f_status = ImageFont.truetype(F_SANS_REG, mm(5.0))
    d.text((mm(28), box_y + mm(5.5)), "ALLE 20 KARTENDECKS", font=f_status_l, fill=(74, 134, 108))
    d.text((mm(28), box_y + mm(12.5)), "klartext-mentoring.de", font=f_status, fill=KT_INK)

    f_foot = ImageFont.truetype(F_SANS_REG, mm(4.4))
    d.text((mm(20), H - mm(15)), "KLARTEXT-Mentoring · © 2026 Anja Jolk", font=f_foot, fill=KT_MUTED)
    return img

# ═══════════════════════ SCHLUSS-/CROSS-SELL-SEITE ═══════════════════════
def build_schluss():
    W, H = mm(210), mm(297)
    img = Image.new("RGB", (W, H), (255, 255, 255))
    d = ImageDraw.Draw(img)
    MARGIN = mm(20)
    CONTENT_W = W - 2 * MARGIN

    kopf_h = mm(45)
    d.rectangle((0, 0, W, kopf_h), fill=KT_PRIMARY)
    f_kicker = ImageFont.truetype(F_SANS_BOLD, mm(4.5))
    d.text((MARGIN, mm(12)), "UND JETZT?", font=f_kicker, fill=(220, 240, 230))
    f_titel = ImageFont.truetype(F_SERIF_BOLD, mm(9.5))
    d.text((MARGIN, mm(20)), "Das war nur ein kleiner Ausschnitt", font=f_titel, fill=(255, 255, 255))

    y = kopf_h + mm(14)
    f_p = ImageFont.truetype(F_SANS_REG, mm(4.8))
    text = ("Diese 8 Karten stammen aus drei von insgesamt 20 KLARTEXT-Kartendecks – für "
            "Grundschule, weiterführende Schule, ADHS, Mobbing, LRS, Hochbegabung, akute "
            "Krisensituationen und viele weitere Themen. Jedes Deck einzeln als PDF-Download "
            "erhältlich, sofort nutzbar.")
    for ln in wrap(d, text, f_p, CONTENT_W):
        d.text((MARGIN, y), ln, font=f_p, fill=KT_INK)
        y += mm(7.4)
    y += mm(8)

    f_h2 = ImageFont.truetype(F_SERIF_BOLD, mm(6.2))
    d.text((MARGIN, y), "Diese Karten waren dabei", font=f_h2, fill=KT_PRIMARY)
    y += mm(10)

    f_grp = ImageFont.truetype(F_SANS_BOLD, mm(4.4))
    f_item = ImageFont.truetype(F_SANS_REG, mm(4.6))
    gruppen = [
        ("M3 · Werkzeugkarten (26 Karten insgesamt)", "Schnelle Handlungshilfen für den pädagogischen Alltag."),
        ("KD · Coaching-Impulskarten Grundschule (35 Karten insgesamt)", "Emotionscoaching für jüngere Kinder."),
        ("JD · Coaching-Impulskarten Jugendliche (52 Karten insgesamt)", "Gesprächsimpulse für die weiterführende Schule."),
    ]
    for titel, desc in gruppen:
        d.ellipse((MARGIN, y + mm(1.6), MARGIN + mm(3), y + mm(4.6)), fill=KT_ACCENT)
        d.text((MARGIN + mm(6), y), titel, font=f_grp, fill=KT_PRIMARY)
        y += mm(6.2)
        for ln in wrap(d, desc, f_item, CONTENT_W - mm(6)):
            d.text((MARGIN + mm(6), y), ln, font=f_item, fill=KT_MUTED)
            y += mm(5.8)
        y += mm(4)

    y += mm(6)
    box_h = mm(30)
    d.rounded_rectangle((MARGIN, y, W - MARGIN, y + box_h), radius=mm(3), fill=(232, 245, 238))
    f_cta_l = ImageFont.truetype(F_SANS_BOLD, mm(5.6))
    f_cta = ImageFont.truetype(F_SANS_REG, mm(4.8))
    d.text((MARGIN + mm(8), y + mm(7)), "Alle 20 Kartendecks entdecken", font=f_cta_l, fill=(74, 134, 108))
    d.text((MARGIN + mm(8), y + mm(16)), "klartext-mentoring.de", font=f_cta, fill=KT_INK)

    f_foot = ImageFont.truetype(F_SANS_REG, mm(4.2))
    d.text((MARGIN, H - mm(15)), "KLARTEXT-Mentoring · © 2026 Anja Jolk", font=f_foot, fill=KT_MUTED)
    return img

def run():
    pages = [build_cover()]

    # ── KD ──
    kd_cards = {
        1: ("Wie geht es mir heute?",
            "Guter Einstieg in ein Gespräch, auch als fester Ritual-Start nutzbar.",
            ["Welche Farbe passt gerade zu dir?", "Magst du erzählen, warum?"],
            "Am besten als festen, wiederkehrenden Einstieg nutzen (z. B. jede Woche), nicht nur wenn etwas Schwieriges ansteht – sonst verknüpft das Kind die Karte mit „jetzt kommt Ärger“."),
        21: ("Was ist ein guter Freund?",
             "Gemeinsam Eigenschaften von Freundschaft sammeln, konkret statt abstrakt.",
             ["Was macht jemanden zu einem guten Freund?", "Bist du das auch für andere?"],
             "Konkrete Beispiele aus dem Kinderalltag sammeln, nicht abstrakt bleiben."),
    }
    KD_BILDER = os.path.join(APP_DIR, "bilder/kd/")
    import glob
    def find_image(bilder_dir, prefix, nr):
        for pattern in (f"{prefix}-{nr:02d}.jpg", f"{prefix}-{nr:02d} *.jpg", f"{prefix}-{nr:02d}.jpeg", f"{prefix}-{nr:02d}.png"):
            files = sorted(glob.glob(os.path.join(bilder_dir, pattern)))
            if files:
                return files[0]
        return None

    for nr, (titel, anleitung, fragen, hinweis) in kd_cards.items():
        card = {"nr": nr, "titel": titel, "anleitung": anleitung, "fragen": fragen, "hinweis": hinweis, "total": 35}
        img_path = find_image(KD_BILDER, "KD", nr)
        vorn = os.path.join(OUT_DIR, f"KD-{nr:02d}_Vorderseite.png")
        hinten = os.path.join(OUT_DIR, f"KD-{nr:02d}_Rueckseite.png")
        build_card_kd.build_front(card, img_path, vorn)
        build_card_kd.build_back(card, hinten)
        pages.append(Image.open(vorn).convert("RGB"))
        pages.append(Image.open(hinten).convert("RGB"))
        print("KD", nr, "ok")

    # ── JD ──
    jd_cards = {
        3: ("Meine Stärken sehen",
            "Für ruhige Momente, nicht in akuter Krise.",
            ["Worauf bist du an dir selbst stolz, auch wenn es klein ist?", "Wer würde dir noch eine Stärke von dir nennen?"],
            "Nicht in akuten Krisenmomenten einsetzen – dann wirkt die Frage nach Stärken schnell deplatziert. Für ruhige Gesprächsmomente reservieren."),
        13: ("Nein sagen können",
             "Bei wiederkehrendem Nachgeben trotz Widerwillen.",
             ["Wann fällt dir Nein sagen besonders schwer?", "Was könnte passieren, wenn du es trotzdem sagst?"],
             "Gut geeignet, um ein wiederkehrendes Muster zu benennen, statt nur eine einzelne Situation zu bearbeiten."),
    }
    JD_BILDER = os.path.join(APP_DIR, "bilder/jd/")
    for nr, (titel, anleitung, fragen, hinweis) in jd_cards.items():
        card = {"nr": nr, "titel": titel, "anleitung": anleitung, "fragen": fragen, "hinweis": hinweis, "total": 52}
        img_path = find_image(JD_BILDER, "JD", nr)
        vorn = os.path.join(OUT_DIR, f"JD-{nr:02d}_Vorderseite.png")
        hinten = os.path.join(OUT_DIR, f"JD-{nr:02d}_Rueckseite.png")
        build_card_jd.build_front(card, img_path, vorn)
        build_card_jd.build_back(card, hinten)
        pages.append(Image.open(vorn).convert("RGB"))
        pages.append(Image.open(hinten).convert("RGB"))
        print("JD", nr, "ok")

    # ── M3 (Werkzeugkarten) ──
    m3_cards = {
        1: dict(id_text="WZ-01", typ="situation", icon="sun", titel="Kind kommt aufgewühlt an",
             front_kontext="Gelb bis Orange – typischer Bereich",
             lead="Kind kommt morgens sichtlich aufgewühlt an – noch bevor der Tag beginnt.",
             schritte=[
                 "Kontakt herstellen – ruhig, ohne Druck, kein „Hallo-Hallo“",
                 "Barometer abfragen – ohne Worte, Farbe zeigen lassen",
                 "Ankommen ermöglichen – 5 Minuten, bei Orange keine Aufgaben",
                 "Übergabeinfo an Lehrkraft – kurzes Signal, LK hält den Unterricht",
                 "Regulationstool wählen – was heute passt, nicht was immer passt",
             ],
             tipp="Kein Kind kommt absichtlich aufgewühlt. Was draußen passiert ist, landet im Körper – und braucht Zeit.",
             werkzeuge="Atemanker (M3-09) · Mini-Pause (M3-14)",
             brainy="In dieser Situation zuerst regulieren – dann alles andere.", total=26),
        5: dict(id_text="WZ-05", typ="situation", icon="exchange", titel="Übergang zwischen Situationen",
             front_kontext="Gelb – erhöhte Aufmerksamkeit",
             lead="Wechsel von einer Situation/einem Fach zur nächsten – für viele Kinder der schwierigste Moment.",
             schritte=[
                 "Ankündigen, immer vorher – mind. 2-3 Minuten vorher, keine Überraschungen",
                 "Visuell zeigen, wenn möglich – Tagesplan, nächsten Schritt auf Karte",
                 "Übergangsritual nutzen – immer dasselbe Signal (Klopfen, Wort)",
                 "Bei Widerstand: nicht sofort – kleiner Puffer, kein Kampf",
                 "Ankommen bestätigen – kurzer Check, Barometer, dann erst Inhalt",
             ],
             tipp="Übergänge sind für viele Kinder die schwierigsten Momente des Schultags – weil das Gehirn umschalten muss.",
             werkzeuge="Atemanker (M3-09) · Visualisierung (M3-17)",
             brainy="In dieser Situation zuerst regulieren – dann alles andere.", total=26),
        14: dict(id_text="WZ-14", typ="werkzeug", icon="pause", titel="Mini-Pause",
             front_kontext="Gelb · Orange · vor Tests · bei Überforderung",
             lead="2-5 Minuten Pause außerhalb des Klassenraums, kann Eskalationen verhindern. Strukturiert, kurz, wiederkehrend.",
             schritte=[
                 "Signal vereinbaren (Joker oder Geste)",
                 "Ruhig und unauffällig rausgehen",
                 "Kurze Bewegung: Flur, Treppe, Schulhof",
                 "INGRA begleitet, kein Gespräch nötig",
                 "Nach 2-5 Minuten: „Bereit?“",
                 "Zurück, wenn Kind nickt",
             ],
             tipp="Mini-Pause ist keine Belohnung und keine Strafe – sie ist Regulation.",
             brainy="Kein Werkzeug passt immer – wähle was heute zum Kind passt.", total=26),
        18: dict(id_text="WZ-18", typ="werkzeug", icon="thumbs-up", titel="Lob-Sandwich",
             front_kontext="nach Aufgaben · bei Verhalten · Rückmeldung geben · täglich",
             lead="Feedback-Technik: Positiv – Verbesserung – Positiv. Kritik wird aufgenommen, ohne das Selbstbild zu beschädigen.",
             schritte=[
                 "Erst etwas Konkretes loben",
                 "Dann einen konkreten Hinweis",
                 "Zuletzt wieder positiv",
                 "Immer konkret, nie pauschal",
             ],
             tipp="Lob muss verdient sein. „Super“ ohne Inhalt wirkt nicht – „Du hast alle 5 Zeilen fertig“ wirkt.",
             brainy="Kein Werkzeug passt immer – wähle was heute zum Kind passt.", total=26),
    }
    for nr, card in m3_cards.items():
        vorn = os.path.join(OUT_DIR, f"{card['id_text']}_Vorderseite.png")
        hinten = os.path.join(OUT_DIR, f"{card['id_text']}_Rueckseite.png")
        build_card_werkzeug.build_front(card, vorn)
        build_card_werkzeug.build_back(card, hinten)
        pages.append(Image.open(vorn).convert("RGB"))
        pages.append(Image.open(hinten).convert("RGB"))
        print("M3", card["id_text"], "ok")

    pages.append(build_schluss())

    first, rest = pages[0], pages[1:]
    first.save(OUT_PDF, save_all=True, append_images=rest, resolution=DPI)
    print(f"PDF fertig: {OUT_PDF} ({len(pages)} Seiten)")

if __name__ == "__main__":
    run()
