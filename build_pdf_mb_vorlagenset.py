#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Buendelt die 3 bereits bestehenden, unveraenderten App-Vorlagen (M6_DL_Mini-Krisenkarte.html,
M6_DL_Mini-Checkliste_Erkennen.html, M6_DL_Digitale_Spuren_Sichern.html) als eigenstaendiges PDF-Set –
Text 1:1 identisch aus den Original-HTML-Dateien uebernommen, nur als PIL-Nachbau des bestehenden
Layouts (Kopfzeile/Farbstreifen/Schritte/Merksatz), analog zur A5-Print-Vorlage, statt Browser-
Rendering (kein Headless-Chromium mit Systemabhaengigkeiten im Sandbox verfuegbar)."""
from PIL import Image, ImageDraw, ImageFont
Image.init()

DPI = 300
MM = DPI / 25.4
def mm(v): return int(round(v * MM))

W, H = mm(148), mm(210)  # A5

PINK = (216, 27, 96)
PINK_DARK = (168, 18, 74)
ACCENT = (110, 198, 160)
NAVY = (27, 58, 75)
INK = (45, 45, 45)
MUTED = (122, 96, 96)

F_SERIF_BOLD = "/usr/share/fonts/truetype/crosextra/Caladea-Bold.ttf"
F_SERIF_ITALIC = "/usr/share/fonts/truetype/crosextra/Caladea-Italic.ttf"
F_SANS_REG = "/usr/share/fonts/truetype/lato/Lato-Regular.ttf"
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

VORLAGEN = [
    dict(farbe=(198, 40, 40), titel="🟥 Was tun bei Mobbing?",
         sub="Sofortige Handlungssicherheit für Schulbegleitung & TK",
         schritte=[
             ("Ruhe bewahren", "nicht mitgehen, nicht eskalieren, klare ruhige Stimme"),
             ("Sicherheit herstellen", "betroffene Person aus der Situation holen, Abstand schaffen"),
             ("Betroffene Person schützen", "„Ich bin da.“ – nicht nach Details drängen"),
             ("Lehrkraft informieren", "sofort, nicht später, kurze sachliche Info"),
             ("TK informieren", "zeitnah, Fakten statt Bewertungen"),
             ("Dokumentieren", "Was? Wer? Wann? Wo? – wörtliche Zitate, keine Vermutungen"),
             ("Elternkontakt über TK", "SB informiert nicht selbst – TK übernimmt"),
             ("§8a prüfen", "bei körperlicher Gewalt, Drohungen, digitaler Gewalt, Selbstgefährdung"),
         ],
         merksatz="„Sicherheit zuerst. Fakten danach.“",
         brainy="Im Ernstfall zählt zuerst Schutz — alles andere kommt danach."),
    dict(farbe=(176, 125, 42), titel="🟧 Mobbing erkennen",
         sub="Frühzeitig erkennen, nicht erst im Akutfall",
         schritte=[
             ("Wiederholung", "Passiert es immer wieder?"),
             ("Absicht", "Ist es gezielt verletzend?"),
             ("Machtungleichgewicht", "Mehrere gegen eine Person – körperlich, sozial oder digital überlegen?"),
             ("Ausschluss", "Systematisches Ignorieren, „Du darfst nicht mitspielen“?"),
             ("Demütigung", "Lächerlich machen, Nachäffen, Bloßstellen"),
             ("Digitale Spuren", "Nachrichten, Screenshots, Gruppenchat-Druck"),
             ("Reaktion des Opfers", "Rückzug, Angst, Bauchschmerzen, Schweigen"),
             ("Umfeld", "Niemand greift ein, Verteidiger fehlen"),
         ],
         merksatz="„Mobbing ist ein Muster — kein Moment.“",
         brainy="Wenn ein Kind leidet und nicht mehr rauskommt — Muster prüfen, nicht nur Einzelsituationen."),
    dict(farbe=(21, 101, 192), titel="🟦 Digitale Spuren sichern",
         sub="Sofortige Handlungssicherheit bei Cybermobbing",
         schritte=[
             ("Screenshots machen", "gesamte Nachricht, Absender, Datum & Uhrzeit sichtbar"),
             ("Chatverläufe sichern", "nicht nur einzelne Nachrichten – als Bildreihe sichern"),
             ("Nichts löschen", "keine Nachrichten entfernen, keine Chats verlassen, keine Apps deinstallieren"),
             ("Nicht antworten", "keine Gegenreaktion, keine Rechtfertigung, nichts weiterleiten"),
             ("Gerät sichern", "Passwort nicht ändern, Gerät nicht aus der Hand geben, Akku laden"),
             ("TK informieren", "zeitnah, sachlich, ohne Interpretation"),
             ("Eltern informieren", "über TK – SB informiert nicht selbst"),
             ("Schule informieren", "Klassenleitung, ggf. Schulleitung"),
             ("§8a prüfen", "bei Drohungen, sexualisierten Inhalten, Erpressung"),
             ("Weiteres Vorgehen abstimmen", "TK + Lehrkraft + Eltern, ggf. Schulsozialarbeit oder Polizei"),
         ],
         merksatz="„Sichern — nicht reagieren.“",
         brainy="In der Hitze des Moments zählt: Beweise sichern, nicht selbst eingreifen."),
]

def build_seite(v):
    img = Image.new("RGB", (W, H), (255, 255, 255))
    d = ImageDraw.Draw(img)

    kopf_h = mm(20)
    d.rectangle((0, 0, W, kopf_h), fill=PINK)
    logo_s = mm(8)
    logo_y = (kopf_h - logo_s) // 2
    d.rounded_rectangle((mm(6), logo_y, mm(6) + logo_s, logo_y + logo_s), radius=mm(1.5),
                         fill=NAVY, outline=ACCENT, width=mm(0.6))
    f_logo = font(F_SERIF_BOLD, 4.2)
    d.text((mm(6) + logo_s / 2, logo_y + logo_s / 2), "K", font=f_logo, anchor="mm", fill=(255, 255, 255))
    f_name = font(F_SERIF_BOLD, 4.8)
    d.text((mm(6) + logo_s + mm(3), mm(5.5)), "KLARTEXT", font=f_name, fill=(255, 255, 255))
    f_sub = font(F_SANS_BOLD, 2.2)
    d.text((mm(6) + logo_s + mm(3), mm(11.5)), "MENTORING-SYSTEM", font=f_sub, fill=ACCENT)

    stripe_h = mm(1.4)
    d.rectangle((0, kopf_h, W, kopf_h + stripe_h), fill=v["farbe"])

    y = kopf_h + stripe_h + mm(5)
    pad = mm(7)
    f_titel = font(F_SERIF_BOLD, 6.2)
    d.text((pad, y), v["titel"], font=f_titel, fill=v["farbe"])
    y += mm(8.5)
    f_sub2 = font(F_SANS_REG, 3.4)
    for ln in wrap(d, v["sub"], f_sub2, W - 2 * pad):
        d.text((pad, y), ln, font=f_sub2, fill=MUTED)
        y += mm(4.6)
    y += mm(3)

    f_nr = font(F_SANS_BOLD, 3.0)
    f_label = font(F_SANS_BOLD, 3.5)
    f_text = font(F_SANS_REG, 3.5)
    circle_s = mm(6.5)
    for i, (label, text) in enumerate(v["schritte"], 1):
        d.ellipse((pad, y, pad + circle_s, y + circle_s), fill=v["farbe"])
        d.text((pad + circle_s / 2, y + circle_s / 2), str(i), font=f_nr, fill=(255, 255, 255), anchor="mm")
        tx = pad + circle_s + mm(3)
        full = f"{label} — {text}"
        lines = wrap(d, full, f_text, W - tx - pad)
        ty = y
        for j, ln in enumerate(lines):
            if j == 0 and " — " in ln:
                lab, rest = ln.split(" — ", 1)
                d.text((tx, ty), lab, font=f_label, fill=v["farbe"])
                lw = d.textlength(lab + " — ", font=f_label)
                d.text((tx + lw, ty), rest, font=f_text, fill=INK)
            else:
                d.text((tx, ty), ln, font=f_text, fill=INK)
            ty += mm(4.6)
        y = max(ty, y + circle_s + mm(1.5)) + mm(1.5)

    y += mm(2)
    f_merk = font(F_SERIF_ITALIC, 4.4)
    merk_lines = wrap(d, v["merksatz"], f_merk, W - 2 * pad - mm(6))
    box_h = mm(6) + len(merk_lines) * mm(5.6)
    d.rounded_rectangle((pad, y, W - pad, y + box_h), radius=mm(2), fill=(255, 240, 244), outline=v["farbe"], width=mm(0.6))
    ty = y + mm(3)
    for ln in merk_lines:
        lw = d.textlength(ln, font=f_merk)
        d.text(((W - lw) / 2, ty), ln, font=f_merk, fill=INK)
        ty += mm(5.6)
    y += box_h + mm(4)

    f_brainy_lab = font(F_SANS_BOLD, 3.0)
    f_brainy = font(F_SANS_REG, 3.0)
    d.text((pad, y), "Brainy erinnert:", font=f_brainy_lab, fill=v["farbe"])
    y += mm(4.4)
    for ln in wrap(d, v["brainy"], f_brainy, W - 2 * pad):
        d.text((pad, y), ln, font=f_brainy, fill=MUTED)
        y += mm(4.4)

    return img

def build_cover():
    img = Image.new("RGB", (W, H), (255, 255, 255))
    d = ImageDraw.Draw(img)
    kopf_h = mm(50)
    d.rectangle((0, 0, W, kopf_h), fill=PINK)
    logo_s = mm(14)
    logo_y = (kopf_h - logo_s) // 2
    d.rounded_rectangle((mm(10), logo_y, mm(10) + logo_s, logo_y + logo_s), radius=mm(3),
                         fill=NAVY, outline=ACCENT, width=mm(1))
    f_logo = font(F_SERIF_BOLD, 7.5)
    d.text((mm(10) + logo_s / 2, logo_y + logo_s / 2), "K", font=f_logo, anchor="mm", fill=(255, 255, 255))
    f_titel = font(F_SERIF_BOLD, 7.5)
    d.text((mm(28), mm(16)), "KLARTEXT-Mentoring", font=f_titel, fill=(255, 255, 255))
    f_sub = font(F_SANS_REG, 3.8)
    d.text((mm(28), mm(26)), "Mobbing · Soforthilfe-Set", font=f_sub, fill=(255, 220, 235))

    f_h = font(F_SERIF_BOLD, 8.5)
    d.text((mm(10), mm(65)), "Soforthilfe-Set", font=f_h, fill=PINK)
    f_p = font(F_SANS_REG, 3.6)
    para = ("Die 3 Sofort-Vorlagen aus der App, unverändert für den Druck gebündelt: "
            "Was tun bei Mobbing?, Mobbing erkennen, Digitale Spuren sichern. Ergänzt das "
            "Soforthilfe-Mini-Deck (3 Handlungskarten) als Klassenzimmer-/Ordner-Version zum "
            "Aushängen oder Abheften.")
    y = mm(78)
    for ln in wrap(d, para, f_p, W - mm(20)):
        d.text((mm(10), y), ln, font=f_p, fill=INK)
        y += mm(5)

    f_foot = font(F_SANS_REG, 3.0)
    d.text((mm(10), H - mm(12)), "KLARTEXT-Mentoring · © 2026 Anja Jolk", font=f_foot, fill=MUTED)
    return img

def run():
    out_pdf = "/sessions/kind-beautiful-ptolemy/mnt/outputs/KLARTEXT_Mobbing_Soforthilfe-Set.pdf"
    pages = [build_cover()] + [build_seite(v) for v in VORLAGEN]
    first, rest = pages[0], pages[1:]
    first.save(out_pdf, save_all=True, append_images=rest, resolution=DPI)
    print(f"PDF fertig: {out_pdf} ({len(pages)} Seiten)")

if __name__ == "__main__":
    run()
