#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_eduki_material.py
===========================================================================
KLARTEXT-Mentoring · Automatisierte QR-Code- & PDF-Generierung
für haptisch-digitale eduki-Materialien
===========================================================================

Was macht dieses Skript?
  1. Erzeugt für ein Material einen hochauflösenden, reizarmen QR-Code
     (PNG), der auf das passende Tool in der KLARTEXT-PWA
     (https://klartext-app-8kl.pages.dev) verlinkt.
  2. Baut daraus ein druckfertiges DIN-A4-Arbeitsblatt (PDF) im
     KLARTEXT-Look (Farben/Struktur wie in der App), inkl. einer
     "Dein digitaler KLARTEXT-Bonus"-Box mit dem QR-Code.
  3. Speichert alles in /eduki_outputs/, fertig zum Hochladen auf eduki.

Installation (einmalig, lokal):
    pip install reportlab qrcode[pil] pillow

Ausführen:
    python3 generate_eduki_material.py

Struktur:
  - Die Marken-Farben/-Fonts stammen 1:1 aus dem bestehenden
    KLARTEXT-System (style-karten.css, BAROMETER_KIND.html), damit jedes
    eduki-PDF wie ein natürlicher Teil der App aussieht.
  - PRODUCTS: eine Liste von Materialien. Für "tagesjournal" ist der
    komplette Inhalt bereits fertig ausgearbeitet (Schritt 2 des
    Master-Prompts). Für die drei weiteren, in eduki-master-strategie-
    prompt.md skizzierten Bausteine (OGS-Übergabe-Ticket, ADHS-Toolbox,
    Brainy-Wort-Würfel) stehen Platzhalter-Einträge bereit – sobald ihr
    Feininhalt ausgearbeitet ist, braucht es nur eine neue build_*
    Funktion nach demselben Muster wie build_tagesjournal_content().
===========================================================================
"""

import os
import textwrap

import qrcode
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

MM = 72.0 / 25.4  # 1 mm in PDF-Punkten (72 dpi Basis von reportlab)


def mm(v):
    return v * MM


# ---------------------------------------------------------------------------
# 1. KLARTEXT-Marke: Farben & Schriften (übernommen aus style-karten.css /
#    BAROMETER_KIND.html, damit eduki-Material und App optisch identisch
#    wirken)
# ---------------------------------------------------------------------------
KT_PRIMARY = HexColor("#1B3A4B")   # Dunkelblau (Header, Logo)
KT_ACCENT = HexColor("#6EC6A0")    # Mint (Akzentlinie, Claim)
KT_PAPER = HexColor("#F5F0E8")     # Warmes Off-White (Seitenhintergrund)
KT_INK = HexColor("#2D2D2D")       # Fließtext
KT_MUTED = HexColor("#7A7060")     # Sekundärtext / Footer
KT_BORDER = HexColor("#DDD8CE")    # Rahmen / Trennlinien
WHITE = HexColor("#FFFFFF")

# Das 5-Stufen-Barometer – exakt wie in BAROMETER_KIND.html (FARBEN_K /
# STATUS_TEXTE), inklusive "Grau" als eigenständige, gleichwertige Stufe.
BAROMETER = [
    {"id": "gruen",  "label": "Grün",   "text": "Ich bin gut drauf!",
     "farbe": HexColor("#2E9E5A"), "hell": HexColor("#DCF3E4")},
    {"id": "gelb",   "label": "Gelb",   "text": "Ein bisschen schwierig",
     "farbe": HexColor("#D4A800"), "hell": HexColor("#FCF0C8")},
    {"id": "orange", "label": "Orange", "text": "Ich brauche Hilfe",
     "farbe": HexColor("#D4651A"), "hell": HexColor("#FBE1CB")},
    {"id": "rot",    "label": "Rot",    "text": "Ich bin in einer Krise",
     "farbe": HexColor("#C0392B"), "hell": HexColor("#FADAD7")},
    {"id": "grau",   "label": "Grau",   "text": "Ich bin sehr müde \u2014 ich mag gerade nicht reden",
     "farbe": HexColor("#757575"), "hell": HexColor("#E7E7E7")},
]

# Schriften: Die App nutzt "Playfair Display" (Überschriften) und "Nunito"
# (Fließtext). Beide sind für PDFs nicht garantiert lokal installiert –
# das Skript versucht sie zu registrieren, fällt aber sauber auf die in
# reportlab immer verfügbaren Basisschriften zurück, damit es auf JEDEM
# Rechner ohne Fehler läuft.
FONT_SERIF = "Times-Bold"
FONT_SANS = "Helvetica"
FONT_SANS_BOLD = "Helvetica-Bold"

_CANDIDATE_FONTS = [
    # (Registrierter Name, mögliche Dateipfade auf macOS/Windows/Linux)
    ("PlayfairDisplay-Bold", [
        os.path.expanduser("~/Library/Fonts/PlayfairDisplay-Bold.ttf"),
        "/Library/Fonts/PlayfairDisplay-Bold.ttf",
        "/usr/share/fonts/truetype/playfair-display/PlayfairDisplay-Bold.ttf",
        "C:\\Windows\\Fonts\\PlayfairDisplay-Bold.ttf",
    ]),
    ("Nunito-Regular", [
        os.path.expanduser("~/Library/Fonts/Nunito-Regular.ttf"),
        "/Library/Fonts/Nunito-Regular.ttf",
        "/usr/share/fonts/truetype/nunito/Nunito-Regular.ttf",
        "C:\\Windows\\Fonts\\Nunito-Regular.ttf",
    ]),
    ("Nunito-Bold", [
        os.path.expanduser("~/Library/Fonts/Nunito-Bold.ttf"),
        "/Library/Fonts/Nunito-Bold.ttf",
        "/usr/share/fonts/truetype/nunito/Nunito-Bold.ttf",
        "C:\\Windows\\Fonts\\Nunito-Bold.ttf",
    ]),
]


def register_brand_fonts():
    """Registriert Playfair Display / Nunito, falls lokal vorhanden.
    Andernfalls bleiben die robusten reportlab-Basisschriften aktiv –
    das Skript bricht dadurch NIE wegen fehlender Schriftdateien ab."""
    global FONT_SERIF, FONT_SANS, FONT_SANS_BOLD
    for name, paths in _CANDIDATE_FONTS:
        for p in paths:
            if os.path.isfile(p):
                try:
                    pdfmetrics.registerFont(TTFont(name, p))
                    if "Playfair" in name:
                        FONT_SERIF = name
                    elif name == "Nunito-Regular":
                        FONT_SANS = name
                    elif name == "Nunito-Bold":
                        FONT_SANS_BOLD = name
                except Exception:
                    pass
                break


# ---------------------------------------------------------------------------
# 2. Generische Zeichen-Helfer
# ---------------------------------------------------------------------------
def wrap_to_width(c, text, font_name, font_size, max_width_pt):
    """Bricht Text hart auf eine gegebene Breite um (in PDF-Punkten)."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        test = (cur + " " + w).strip()
        if c.stringWidth(test, font_name, font_size) <= max_width_pt:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def rounded_box(c, x, y, w, h, r, fill=None, stroke=None, line_width=0.9):
    c.saveState()
    if fill is not None:
        c.setFillColor(fill)
    if stroke is not None:
        c.setStrokeColor(stroke)
        c.setLineWidth(line_width)
    c.roundRect(x, y, w, h, r, fill=1 if fill is not None else 0,
                stroke=1 if stroke is not None else 0)
    c.restoreState()


def checkbox(c, x, y, size, color=KT_INK, line_width=1.1):
    c.saveState()
    c.setStrokeColor(color)
    c.setLineWidth(line_width)
    c.roundRect(x, y, size, size, size * 0.22, fill=0, stroke=1)
    c.restoreState()


def logo_mark(c, x, y, size):
    """Kleines quadratisches 'K'-Logo, wie im Header der App."""
    rounded_box(c, x, y, size, size, size * 0.18, fill=KT_PRIMARY,
                stroke=KT_ACCENT, line_width=1.4)
    c.saveState()
    c.setFillColor(WHITE)
    c.setFont(FONT_SERIF, size * 0.55)
    c.drawCentredString(x + size / 2, y + size * 0.28, "K")
    c.restoreState()


def section_header(c, x, y, content_w, number, titel, hinweis=None):
    """Nummerierter Abschnitts-Titel (Kreis-Chip + Serif-Titel), ersetzt
    Emoji-Icons bewusst durch Vektor-Grafik: Emoji-Glyphen sind in den
    PDF-Basisschriften nicht enthalten und würden als schwarze Kästchen
    erscheinen. Gibt die neue y-Position zurück."""
    d = mm(6.2)
    c.setFillColor(KT_PRIMARY)
    c.circle(x + d / 2, y - d / 2 + mm(1.1), d / 2, fill=1, stroke=0)
    c.setFillColor(WHITE)
    c.setFont(FONT_SANS_BOLD, 9.5)
    c.drawCentredString(x + d / 2, y - d / 2 + mm(1.1) - mm(1.6), str(number))

    c.setFillColor(KT_PRIMARY)
    c.setFont(FONT_SERIF, 12.5)
    c.drawString(x + d + mm(3.5), y - mm(1.2), titel)
    y -= mm(7.8)

    if hinweis:
        c.setFillColor(KT_MUTED)
        c.setFont(FONT_SANS, 8.6)
        c.drawString(x, y, hinweis)
        y -= mm(6.5)

    return y


# ---------------------------------------------------------------------------
# 3. Wiederkehrende Seitenbausteine (Header, Footer, QR-Bonus-Box)
# ---------------------------------------------------------------------------
def draw_header(c, page_w, page_h, kicker, titel, untertitel):
    header_h = mm(32)
    top = page_h

    # Kopfleiste
    c.setFillColor(KT_PRIMARY)
    c.rect(0, top - header_h, page_w, header_h, fill=1, stroke=0)
    c.setFillColor(KT_ACCENT)
    c.rect(0, top - header_h - mm(1.3), page_w, mm(1.3), fill=1, stroke=0)

    logo_mark(c, mm(15), top - header_h + mm(7), mm(15))

    c.setFillColor(WHITE)
    c.setFont(FONT_SERIF, 15)
    c.drawString(mm(34), top - header_h + mm(17), "KLARTEXT")
    c.setFillColor(KT_ACCENT)
    c.setFont(FONT_SANS_BOLD, 7.3)
    c.drawString(mm(34), top - header_h + mm(9.5), kicker.upper())

    c.setFillColor(WHITE)
    c.setFont(FONT_SANS_BOLD, 8)
    c.drawRightString(page_w - mm(15), top - header_h + mm(17), "Mentoring-System")
    c.setFillColor(KT_ACCENT)
    c.setFont(FONT_SANS, 6.6)
    c.drawRightString(page_w - mm(15), top - header_h + mm(9.5), "\u201eKlar. Warm. Menschlich.\u201c")

    # Titelblock
    y = top - header_h - mm(14)
    c.setFillColor(KT_PRIMARY)
    c.setFont(FONT_SERIF, 20)
    c.drawString(mm(15), y, titel)
    y -= mm(7.5)
    c.setFillColor(KT_MUTED)
    c.setFont(FONT_SANS, 10.5)
    c.drawString(mm(15), y, untertitel)

    return y - mm(6)  # y-Position, ab der der Seiteninhalt beginnt


def draw_footer(c, page_w, seiten_hinweis=""):
    c.saveState()
    c.setStrokeColor(KT_BORDER)
    c.setLineWidth(0.8)
    c.line(mm(15), mm(14), page_w - mm(15), mm(14))
    c.setFillColor(KT_MUTED)
    c.setFont(FONT_SANS, 7.3)
    c.drawString(mm(15), mm(9.5),
                 "KLARTEXT-Mentoring \u00b7 Anja Jolk \u00a9 2026 \u00b7 klartext-app-8kl.pages.dev")
    if seiten_hinweis:
        c.drawRightString(page_w - mm(15), mm(9.5), seiten_hinweis)
    c.restoreState()


def generate_qr_png(link, out_path, box_size=10, border=3):
    """Erzeugt einen hochauflösenden, reizarmen (reinen Schwarz/Weiß-)
    QR-Code als PNG. box_size/border in QR-'Modulen', nicht mm – box_size=10
    ergibt bei Standardgröße ein sehr scharfes, druckfähiges PNG (>800px)."""
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=box_size,
        border=border,
    )
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#1B3A4B", back_color="white")
    img.save(out_path)
    return out_path


def draw_qr_bonus_box(c, x, y, w, h, qr_png_path, link_text):
    """Die wiederkehrende 'Dein digitaler KLARTEXT-Bonus'-Box mit QR-Code,
    die jedes eduki-PDF mit der PWA verknüpft."""
    rounded_box(c, x, y, w, h, mm(3.5), fill=KT_PAPER, stroke=KT_BORDER, line_width=1)

    qr_size = h - mm(6)
    qr_x = x + mm(5)
    qr_y = y + (h - qr_size) / 2
    c.drawImage(qr_png_path, qr_x, qr_y, width=qr_size, height=qr_size,
                preserveAspectRatio=True, mask="auto")

    text_x = qr_x + qr_size + mm(6)
    text_w = x + w - mm(5) - text_x

    c.setFillColor(KT_PRIMARY)
    c.setFont(FONT_SANS_BOLD, 11)
    c.drawString(text_x, y + h - mm(9), "Dein digitaler KLARTEXT-Bonus")

    body = ("Scanne den Code mit deinem Handy und f\u00fchre dein "
            "Tagesjournal auch digital weiter \u2013 mit Erinnerung, "
            "Barometer-Verlauf und Brainy als Begleiter.")
    lines = wrap_to_width(c, body, FONT_SANS, 8.6, text_w)
    ty = y + h - mm(15.5)
    c.setFillColor(KT_INK)
    c.setFont(FONT_SANS, 8.6)
    for ln in lines:
        c.drawString(text_x, ty, ln)
        ty -= mm(4.2)

    c.setFillColor(KT_MUTED)
    c.setFont(FONT_SANS, 7.4)
    c.drawString(text_x, y + mm(4), link_text)


# ---------------------------------------------------------------------------
# 4. Produkt 1: "Mein 5-Sekunden-Tagesjournal mit dem 5-Stufen-Barometer"
# ---------------------------------------------------------------------------
def build_tagesjournal_pdf(out_path, qr_png_path, qr_link):
    page_w, page_h = A4
    c = canvas.Canvas(out_path, pagesize=A4)

    content_top = draw_header(
        c, page_w, page_h,
        kicker="Eduki-Material \u00b7 Baustein 1 von 4",
        titel="Mein 5-Sekunden-Tagesjournal",
        untertitel="mit dem 5-Stufen-Barometer \u2014 f\u00fcr Grundschule & F\u00f6rderschule",
    )

    left = mm(15)
    right = page_w - mm(15)
    content_w = right - left
    y = content_top

    # Name/Datum-Zeile
    c.setFillColor(KT_INK)
    c.setFont(FONT_SANS_BOLD, 9.5)
    c.drawString(left, y, "Name:")
    c.setStrokeColor(KT_BORDER)
    c.setLineWidth(1)
    c.line(left + mm(16), y - mm(0.8), left + mm(78), y - mm(0.8))
    c.drawString(left + mm(86), y, "Datum:")
    c.line(left + mm(102), y - mm(0.8), right, y - mm(0.8))
    y -= mm(11)

    # ---- Abschnitt 1: Morgens \u2013 das Barometer ----
    y = section_header(c, left, y, content_w, 1, "Guten Morgen! Wie f\u00fchle ich mich gerade?",
                        hinweis="Kreuze dein Feld an \u2014 jede Farbe ist okay, jede Farbe darf sein.")

    row_h = mm(24)
    gap = mm(2.4)
    box_w = (content_w - gap * (len(BAROMETER) - 1)) / len(BAROMETER)
    row_top = y
    for i, stufe in enumerate(BAROMETER):
        bx = left + i * (box_w + gap)
        rounded_box(c, bx, row_top - row_h, box_w, row_h, mm(2.4),
                    fill=stufe["hell"], stroke=stufe["farbe"], line_width=1.3)
        # Farbpunkt
        r = mm(3.1)
        cx, cy = bx + box_w / 2, row_top - mm(4.8)
        c.setFillColor(stufe["farbe"])
        c.circle(cx, cy, r, fill=1, stroke=0)
        # Label
        c.setFillColor(KT_INK)
        c.setFont(FONT_SANS_BOLD, 8.3)
        c.drawCentredString(cx, row_top - mm(9.8), stufe["label"])
        # Kurztext (max. 2 Zeilen, danach folgt mit Abstand das Ankreuzfeld)
        c.setFont(FONT_SANS, 6.1)
        txt_lines = wrap_to_width(c, stufe["text"], FONT_SANS, 6.1, box_w - mm(3))
        ty = row_top - mm(12.8)
        for ln in txt_lines[:2]:
            c.drawCentredString(cx, ty, ln)
            ty -= mm(3.1)
        # Ankreuzfeld \u2013 mit fixem Abstand vom Boxboden, unabh\u00e4ngig von der
        # Textl\u00e4nge, damit es nie mit dem Text kollidiert
        checkbox(c, cx - mm(2.1), row_top - row_h + mm(3), mm(4.2), color=stufe["farbe"])
    y = row_top - row_h - mm(11)

    # ---- Abschnitt 2: Zum Feierabend \u2013 Reflexion ----
    y = section_header(c, left, y, content_w, 2, "Zum Feierabend: Was hat mir heute geholfen?")

    optionen = [
        "Bewegung oder eine Pause",
        "Ein Gespr\u00e4ch mit jemandem",
        "Mich kurz zur\u00fcckziehen",
        "Laut sein oder lachen d\u00fcrfen",
        "Musik h\u00f6ren",
        "Etwas anderes:",
    ]
    cols = 2
    cell_gap_x = mm(4)
    cell_gap_y = mm(3.2)
    cell_w = (content_w - cell_gap_x * (cols - 1)) / cols
    cell_h = mm(11.5)
    for idx, label in enumerate(optionen):
        col = idx % cols
        row = idx // cols
        cx0 = left + col * (cell_w + cell_gap_x)
        cy0 = y - row * (cell_h + cell_gap_y)
        rounded_box(c, cx0, cy0 - cell_h, cell_w, cell_h, mm(2.2),
                    fill=WHITE, stroke=KT_BORDER, line_width=1)
        checkbox(c, cx0 + mm(3.2), cy0 - cell_h / 2 - mm(2.1), mm(4.2), color=KT_PRIMARY)
        c.setFillColor(KT_INK)
        c.setFont(FONT_SANS, 9.3)
        c.drawString(cx0 + mm(10.5), cy0 - cell_h / 2 - mm(1.6), label)
        if label.endswith(":"):
            c.setStrokeColor(KT_BORDER)
            c.setLineWidth(0.8)
            c.line(cx0 + mm(35), cy0 - cell_h / 2 - mm(1.9),
                   cx0 + cell_w - mm(3), cy0 - cell_h / 2 - mm(1.9))

    rows_used = (len(optionen) + cols - 1) // cols
    y = y - rows_used * (cell_h + cell_gap_y) - mm(6.5)

    # ---- Abschnitt 3: Vorsatz f\u00fcr morgen ----
    c.setFillColor(KT_PRIMARY)
    c.setFont(FONT_SERIF, 11.5)
    c.drawString(left, y, "Das nehme ich mir f\u00fcr morgen vor:")
    y -= mm(6)
    c.setStrokeColor(KT_BORDER)
    c.setLineWidth(0.9)
    c.line(left, y, right, y)
    y -= mm(11)

    # ---- QR-Bonus-Box ----
    qr_box_h = mm(28)
    draw_qr_bonus_box(c, left, y - qr_box_h, content_w, qr_box_h,
                       qr_png_path, link_text=qr_link)

    draw_footer(c, page_w, "Reizarm gestaltet f\u00fcr Kinder mit besonderem Regulationsbedarf")
    c.showPage()
    c.save()
    return out_path


# ---------------------------------------------------------------------------
# 5. Produkt-Konfiguration (aus eduki-master-strategie-prompt.md, Schritt 2)
#    -> Für "tagesjournal" ist der Inhalt vollständig ausgearbeitet.
#    -> Die drei weiteren Bausteine sind als Platzhalter hinterlegt, damit
#       das Skript strukturell für die ganze Produktreihe vorbereitet ist.
#       Sobald ihr Feininhalt feststeht, braucht jeder nur eine eigene
#       build_*_pdf()-Funktion nach dem Vorbild von build_tagesjournal_pdf().
# ---------------------------------------------------------------------------
BASE_URL = "https://klartext-app-8kl.pages.dev"

PRODUCTS = [
    {
        "id": "tagesjournal",
        "titel": "Mein 5-Sekunden-Tagesjournal",
        "preis": "2,90 \u20ac",
        # ?ref=eduki&produkt=... hilft, eduki-Traffic in der App später
        # von anderen Quellen zu unterscheiden (Trichter-Tracking).
        "qr_link": f"{BASE_URL}/BAROMETER_KIND.html?guest=true",
        "builder": build_tagesjournal_pdf,
    },
    {
        "id": "ogs-uebergabeticket",
        "titel": "Das OGS-\u00dcbergabe-Ticket & kLAR-Deeskalations-Formel",
        "preis": "3,50 \u20ac",
        "qr_link": f"{BASE_URL}/KLARTEXT_OGS_Workspace.html?ref=eduki&produkt=ogs-ticket",
        "builder": None,  # TODO: eigene build_*_pdf()-Funktion, DIN A6, 2-seitig
    },
    {
        "id": "adhs-toolbox",
        "titel": "ADHS-Klassenzimmer-Toolbox (Mein Wunschzettel an die Lehrkraft)",
        "preis": "2,90 \u20ac",
        "qr_link": f"{BASE_URL}/KLARTEXT_ADHS_Tool.html?ref=eduki&produkt=adhs-toolbox",
        "builder": None,  # TODO: eigene build_*_pdf()-Funktion
    },
    {
        "id": "brainy-wortwuerfel",
        "titel": "Der Brainy-Wort-W\u00fcrfel (Spielerische Sprachf\u00f6rderung DaZ)",
        "preis": "2,90 \u20ac",
        "qr_link": f"{BASE_URL}/KLARTEXT_Wortwuerfel.html?ref=eduki&produkt=brainy-wortwuerfel",
        "builder": None,  # TODO: eigene build_*_pdf()-Funktion, W\u00fcrfelnetz-Vorlage
    },
]


# ---------------------------------------------------------------------------
# 6. Hauptprogramm
# ---------------------------------------------------------------------------
def main():
    register_brand_fonts()

    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "eduki_outputs")
    os.makedirs(out_dir, exist_ok=True)

    for produkt in PRODUCTS:
        if produkt["builder"] is None:
            print(f"\u23ed\ufe0f  {produkt['titel']} \u2014 \u00fcbersprungen (noch keine PDF-Vorlage hinterlegt)")
            continue

        qr_path = os.path.join(out_dir, f"{produkt['id']}_qrcode.png")
        pdf_path = os.path.join(out_dir, f"KLARTEXT_{produkt['id']}.pdf")

        generate_qr_png(produkt["qr_link"], qr_path)
        produkt["builder"](pdf_path, qr_path, produkt["qr_link"])

        print(f"\u2705 {produkt['titel']} ({produkt['preis']})")
        print(f"   QR-Ziel: {produkt['qr_link']}")
        print(f"   PDF:     {pdf_path}")

    print(f"\nFertig. Alle Dateien liegen in: {out_dir}")


if __name__ == "__main__":
    main()
