#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Anleitung, Methodik, Glossar, Quellen fürs KD-Deck – adaptiert von build_booklet.py (JD)."""
from PIL import Image, ImageDraw, ImageFont
Image.init()

DPI = 300
MM = DPI / 25.4
def mm(v): return int(round(v * MM))

KD = (46, 158, 90)          # #2E9E5A
KD_LIGHT = (231, 245, 236)
KD_BORDER = (188, 222, 200)
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
    d.rectangle((0, 0, W, kopf_h), fill=KD)
    d.text((MARGIN, mm(10)), kicker, font=f_kicker, fill=(225, 240, 230))
    ty = mm(17)
    for ln in lines:
        d.text((MARGIN, ty), ln, font=f_titel, fill=(255, 255, 255))
        ty += mm(size * 1.35)
    return img, d, kopf_h + mm(14)

def footer(d, page_label):
    f = ImageFont.truetype(F_SANS_REG, mm(4))
    d.text((MARGIN, H - mm(14)), "KLARTEXT-Mentoring · KD-Deck · © 2026 Anja Jolk", font=f, fill=KT_MUTED)
    w = d.textlength(page_label, font=f)
    d.text((W - MARGIN - w, H - mm(14)), page_label, font=f, fill=KT_MUTED)

def draw_h2(d, y, text):
    f = ImageFont.truetype(F_SERIF_BOLD, mm(6.5))
    d.text((MARGIN, y), text, font=f, fill=KD)
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
    d.ellipse((MARGIN, y + mm(1.6), MARGIN + mm(1.6), y + mm(3.2)), fill=KD)
    lh = mm(size * 1.55)
    lines = wrap(d, text, f, CONTENT_W - mm(7))
    for ln in lines:
        d.text((MARGIN + mm(6), y), ln, font=f, fill=KT_INK)
        y += lh
    return y + mm(1.5)

def draw_numbered(d, y, num, titel, text, size=4.8):
    f_num = ImageFont.truetype(F_SERIF_BOLD, mm(7))
    d.ellipse((MARGIN, y, MARGIN + mm(9), y + mm(9)), fill=KD)
    d.text((MARGIN + mm(4.5), y + mm(4.5)), str(num), font=f_num, anchor="mm", fill=(255, 255, 255))
    f_titel = ImageFont.truetype(F_SANS_BOLD, mm(5.2))
    d.text((MARGIN + mm(13), y + mm(0.5)), titel, font=f_titel, fill=KD)
    f_text = ImageFont.truetype(F_SANS_REG, mm(size))
    ty = y + mm(7)
    lh = mm(size * 1.55)
    for ln in wrap(d, text, f_text, CONTENT_W - mm(13)):
        d.text((MARGIN + mm(13), ty), ln, font=f_text, fill=KT_INK)
        ty += lh
    return max(ty, y + mm(11)) + mm(4)

# ═══════════════════════════════════ ANLEITUNG ═══════════════════════════════════
def anleitung_seite1():
    img, d, y = new_page("GEBRAUCHSANWEISUNG", "Anleitung: So funktioniert das KD-Deck")

    y = draw_h2(d, y, "Was ist das KD-Deck?")
    y = draw_para(d, y, "Das KD-Deck enthält 35 Coaching-Impulskarten für Grundschulkinder. Anders als bei "
                        "den älteren Decks erscheint Brainy direkt im Bild, gemeinsam mit dem Kind – die Karten "
                        "sind so gestaltet, dass sie mit dem Kind zusammen angeschaut werden. Jede Karte greift "
                        "ein Gefühl oder eine Alltagssituation auf, mit kurzer Anleitung und zwei einfachen, "
                        "kindgerechten Fragen.")
    y += mm(6)

    y = draw_h2(d, y, "Für wen ist es gedacht?")
    y = draw_para(d, y, "In erster Linie für INGRA (Schulbegleitung) im direkten Kontakt mit Grundschulkindern. "
                        "Genauso einsetzbar für Eltern und Lehrkräfte, einzeln oder in kleinen Gruppen.")
    y += mm(8)

    y = draw_h2(d, y, "In drei Schritten")
    y += mm(2)
    y = draw_numbered(d, y, 1, "Karte auswählen",
        "Passt ein Thema gerade zur Situation? Die sieben Themenblöcke (siehe Rückseite dieser Seite) "
        "helfen bei der Auswahl.")
    y = draw_numbered(d, y, 2, "Gemeinsam anschauen",
        "Bild und Titel gemeinsam mit dem Kind anschauen. Brainy im Bild hilft, sich mit der Situation "
        "zu identifizieren.")
    y = draw_numbered(d, y, 3, "Rückseite nutzen",
        "Anleitung lesen, eine der beiden Fragen stellen, dem Kind Zeit zum Antworten geben. Es muss "
        "nicht immer beide Fragen geben – eine reicht oft.")

    footer(d, "Anleitung · 1/2")
    return img

def anleitung_seite2():
    img, d, y = new_page("GEBRAUCHSANWEISUNG", "Haltung, Grenzen & praktische Tipps")

    y = draw_h2(d, y, "Haltung")
    y = draw_para(d, y, "Kinder brauchen noch mehr Sicherheit und Tempo als Jugendliche: nicht bewerten, "
                        "nicht korrigieren, keine Antwort einfordern. Wenn ein Kind nicht antworten möchte "
                        "oder eine Karte nicht passt: die Karte weglegen, kein Druck aufbauen.")
    y += mm(8)

    box_y = y
    warn_text = ("Das KD-Deck ersetzt keine Diagnostik, keine Therapie und kein Kinderschutzverfahren. "
                 "Wird ein Kind während eines Karten-Gesprächs sichtbar stark aufgebracht: Kartenarbeit "
                 "unterbrechen und die vier kLAR-Schritte nutzen (siehe „Die KLARTEXT-Methodik“, nächste "
                 "Seite). Bei Hinweisen auf eine Kindeswohlgefährdung oder Grenzverletzung (insbesondere "
                 "bei KD-29): sofort die trägerinternen Kinderschutz-Vorgaben greifen lassen – die Karte "
                 "ersetzt kein Schutzverfahren.")
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
    y = draw_bullet(d, y, "Die Bonus-Barometer-Karte griffbereit halten – Kinder zeigen oft lieber auf "
                          "eine Farbe, als ein Gefühl in Worte zu fassen.")
    y = draw_bullet(d, y, "Ruhiger Ort, ungestörte Zeit – keine Karte zwischen Tür und Angel.")
    y = draw_bullet(d, y, "Freiwillige Teilnahme: kein Zwang, eine Karte zu bearbeiten.")
    y = draw_bullet(d, y, "Jede Rückseite enthält einen kurzen „Tipp für die INGRA“ mit Hinweisen "
                          "zur passenden Einsatzsituation – der lohnt sich vor dem Gespräch zu lesen.")

    footer(d, "Anleitung · 2/2")
    return img

# ═══════════════════════════════════ METHODIK (Barometer & kLAR) ═══════════════════════════════════
BAROMETER = [
    ((76, 175, 80), "GRÜN", "Stabil, lernbereit."),
    ((249, 168, 37), "GELB", "Angespannt, aufmerksam."),
    ((239, 108, 0), "ORANGE", "Dysreguliert, braucht Unterstützung – hier greift das kLAR-Modell."),
    ((198, 40, 40), "ROT", "Akute Krise – kLAR reicht nicht mehr, sofort eine Fachperson einbeziehen."),
    ((120, 120, 120), "GRAU", "Erschöpft oder orientierungslos – weiß selbst nicht, was es braucht. Erst beobachten, nicht vorschnell einordnen."),
]

KLAR_STEPS = [
    ("K", "Kontakt & Sicherheit",
     "Auf Augenhöhe gehen. Ruhige Stimme, körperliche und räumliche Sicherheit zuerst herstellen."),
    ("L", "Leise & Langsam",
     "Stimme senken, Tempo herausnehmen. Kurze Sätze, Pausen aushalten statt füllen."),
    ("A", "Anerkennung & Atmen",
     "Das Erleben anerkennen – „Ich sehe, das ist gerade viel.“ Gemeinsam bewusst durchatmen."),
    ("R", "Reizreduktion & Rückzug",
     "Reize reduzieren, Rückzug ermöglichen. Raum geben, nicht drängen."),
]

def methodik_seite():
    img, d, y = new_page("HINTERGRUND", "Die KLARTEXT-Methodik")
    y = draw_para(d, y, "Barometer und kLAR-Modell sind die Grundbegriffe hinter KLARTEXT. Beim KD-Deck "
                        "steht das Barometer zusätzlich als eigene Bonus-Karte griffbereit für das Kind – "
                        "hier der Hintergrund für die Fachkraft.", size=4.6, color=KT_MUTED)
    y += mm(8)

    y = draw_h2(d, y, "Das Barometer – 5 Zustände")
    f_lab = ImageFont.truetype(F_SANS_BOLD, mm(4.8))
    f_desc = ImageFont.truetype(F_SANS_REG, mm(4.4))
    lab_w = mm(30)
    for color, label, desc in BAROMETER:
        d.ellipse((MARGIN, y + mm(0.9), MARGIN + mm(3.6), y + mm(4.5)), fill=color)
        d.text((MARGIN + mm(6), y), label, font=f_lab, fill=KT_INK)
        lines = wrap(d, desc, f_desc, CONTENT_W - lab_w - mm(6))
        ly = y
        for ln in lines:
            d.text((MARGIN + lab_w, ly), ln, font=f_desc, fill=KT_MUTED)
            ly += mm(6.2)
        y = max(ly, y + mm(7.5)) + mm(1.5)
    y += mm(5)

    y = draw_h2(d, y, "Das kLAR-Modell – 4 Schritte bei Anspannung")
    y += mm(2)
    for letter, titel, text in KLAR_STEPS:
        y = draw_numbered(d, y, letter, titel, text)

    y = draw_para(d, y, "kLAR gilt für Gelb und Orange. Ab Rot reicht kLAR nicht mehr – dann sofort eine "
                        "Fachperson einbeziehen (siehe „Grenzen“ in der Anleitung).", size=4.2, color=GOLD)

    footer(d, "Methodik")
    return img

# ═══════════════════════════════════ GLOSSAR ═══════════════════════════════════
GLOSSAR = [
    ("Brainy", "Die Coach-Figur, die auf den KD-Bildern gemeinsam mit dem Kind zu sehen ist. Steht für "
     "ruhige, wertfreie Begleitung – Brainy bewertet nicht, sondern hört zu."),
    ("Kind-Barometer", "Eine kindgerechte Farbskala mit 5 Zuständen (Grün, Gelb, Orange, Rot, Grau), mit der "
     "Kinder zeigen können, wie es ihnen gerade geht – auch wenn Worte dafür noch fehlen. Als eigene "
     "Bonus-Karte im Deck enthalten."),
    ("kLAR-Modell", "Vierstufiges Vorgehen für die Fachkraft, wenn ein Kind sichtbar angespannt oder "
     "aufgebracht ist: Kontakt & Sicherheit, Leise & Langsam, Anerkennung & Atmen, Reizreduktion & Rückzug "
     "(siehe „Die KLARTEXT-Methodik“)."),
    ("INGRA", "Bezeichnung für die pädagogischen Fachkräfte des KLARTEXT-Systems (früher: "
     "Schulbegleiter:in). INGRA begleitet Kinder im Schulalltag – auf Grundlage des Hilfeplans und im "
     "Rahmen der Eingliederungshilfe."),
    ("Impulsfrage", "Eine offen formulierte Frage ohne vorgegebene richtige Antwort. Ziel ist nicht die "
     "schnelle Lösung, sondern das Öffnen eines Gedankens – bei Kindern besonders einfach und konkret "
     "gehalten."),
    ("Systemisches Coaching", "Beratungsansatz, der Kinder nicht isoliert, sondern in ihren Beziehungen "
     "und Kontexten betrachtet. Fragt nicht „was ist falsch“, sondern „was würde helfen“."),
]

def glossar_seite(begriffe, seiten_label, intro=None):
    img, d, y = new_page("BEGRIFFE AUS DEM KD-DECK", "Glossar")
    if intro:
        y = draw_para(d, y, intro, size=4.6, color=KT_MUTED)
        y += mm(8)

    for begriff, definition in begriffe:
        f_term = ImageFont.truetype(F_SERIF_BOLD, mm(6))
        d.text((MARGIN, y), begriff, font=f_term, fill=KD)
        y += mm(9)
        y = draw_para(d, y, definition, size=4.4)
        y += mm(4)
        d.line((MARGIN, y, W - MARGIN, y), fill=KD_BORDER, width=mm(0.3))
        y += mm(7)

    footer(d, seiten_label)
    return img

# ═══════════════════════════════════ QUELLEN ═══════════════════════════════════
QUELLEN_BESTAETIGT = [
    "Oerter, R., & Montada, L. (Hrsg.). (2008). Entwicklungspsychologie (6. Aufl.). Beltz Psychologie "
    "Verlags Union.",
    "Bandura, A. (1977). Self-efficacy: Toward a unifying theory of behavioral change. Psychological "
    "Review, 84(2), 191–215.",
    "Rosenberg, M. B. (2003). Nonviolent communication: A language of life (2nd ed.). PuddleDancer Press.",
    "Olweus, D. (1993). Bullying at school: What we know and what we can do. Blackwell.",
    "Salmivalli, C. (2010). Bullying and the peer group: A review. Aggression and Violent Behavior, 15(2), "
    "112–120.",
    "Porges, S. W. (2011). The polyvagal theory: Neurophysiological foundations of emotions, attachment, "
    "communication, and self-regulation. Norton.",
]

def quellen_seite():
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

    y = draw_h2(d, y, "Beispielhafte Passung")
    y = draw_bullet(d, y, "KD-17 / KD-19 (Mut) – Bandura: Selbstwirksamkeit entsteht durch kleine, "
                          "machbare Erfolgserlebnisse.")
    y = draw_bullet(d, y, "KD-22 / KD-23 / KD-25 (Ausgrenzung) – Olweus / Salmivalli: Gruppendynamik bei "
                          "Ausgrenzung und Mobbing unter Kindern.")
    y = draw_bullet(d, y, "KD-09 / KD-26 / KD-27 (Körper & Beruhigen) – Porges: Körperbasierte Regulation "
                          "als Zugang zu Emotionen bei jungen Kindern.")

    footer(d, "Quellen")
    return img

if __name__ == "__main__":
    pages = {
        "kd_anleitung1": anleitung_seite1(),
        "kd_anleitung2": anleitung_seite2(),
        "kd_methodik": methodik_seite(),
        "kd_glossar1": glossar_seite(GLOSSAR[:3], "Glossar · 1/2",
            intro="Kurz erklärt: Begriffe, die auf den Karten oder in dieser Anleitung vorkommen und "
                  "nicht selbsterklärend sind."),
        "kd_glossar2": glossar_seite(GLOSSAR[3:], "Glossar · 2/2"),
        "kd_quellen": quellen_seite(),
    }
    for name, img in pages.items():
        img.save(f"/sessions/kind-beautiful-ptolemy/mnt/outputs/booklet_{name}.png")
        print(name, "ok")
