#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_mitgeb_sets.py
KLARTEXT – Eltern-Mitgabe-Sets (Grundschule & Berufsvorbereitung)

Erzeugt zwei DIN-A4-PDFs im KLARTEXT-Corporate-Design:
  1) KLARTEXT_ElternSet_Grundschule.pdf         (3 Seiten)
  2) KLARTEXT_ElternSet_Berufsvorbereitung.pdf  (2 Seiten)

Reizarmes Design: weißer Hintergrund, feiner Petrol-Rahmen, klare
Typografie, Brainy-Maskottchen (echtes PNG-Asset aus der klartext-app)
als wiederkehrendes Bindeglied zwischen Schule und Zuhause.
"""

import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Flowable,
    Paragraph, Spacer, Table, TableStyle, Image, KeepTogether, PageBreak
)
from reportlab.pdfgen import canvas as pdfcanvas
from reportlab.pdfbase.pdfmetrics import stringWidth


# ------------------------------------------------------------------
# 1. CORPORATE DESIGN — KLARTEXT
# ------------------------------------------------------------------

PETROL = colors.HexColor("#005F73")
SAGE = colors.HexColor("#8FBC8F")
SAND = colors.HexColor("#FAF0ED")
HEART_RED = colors.HexColor("#C0392B")
WHITE = colors.white
GREY_TEXT = colors.HexColor("#3A3A3A")

# Produktspezifische Akzentfarben (KLARTEXT-Branding-Pflicht: jedes Material
# bekommt eine eigene, bisher unbenutzte Akzentfarbe fuer das Kopfband)
ACCENT_GRUNDSCHULE = colors.HexColor("#D6A24C")  # Honig – warm, "Küchentisch"-Thema
ACCENT_BERUF = colors.HexColor("#A6643A")  # Kupfer – nuechtern-erwachsen, Berufskontext

# Pflicht-Footer laut KLARTEXT-Branding-Checkliste (siehe Merkliste)
COPYRIGHT_FOOTER = "© 2026 KLARTEXT-Mentoring · Anja Jolk · info@klartext-mentoring.de"

ASSETS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
BRAINY_MAIN = os.path.join(ASSETS_DIR, "brainy.png")
BRAINY_GRUEN = os.path.join(ASSETS_DIR, "brainy-ingra-gruen.png")
BRAINY_GELB = os.path.join(ASSETS_DIR, "brainy-ingra-gelb.png")
BRAINY_ORANGE = os.path.join(ASSETS_DIR, "brainy-ingra-orange.png")

PAGE_W, PAGE_H = A4
MARGIN = 1.0 * cm  # Rahmenabstand vom Rand
FRAME_PAD = 0.6 * cm  # Innenabstand des Rahmens zum Inhalt


# ------------------------------------------------------------------
# 2. PARAGRAPH-STYLES (reizarm: linksbündig, großzügiger Zeilenabstand)
# ------------------------------------------------------------------

STYLES = {
    "header": ParagraphStyle(
        "header", fontName="Helvetica-Bold", fontSize=10.5,
        textColor=PETROL, alignment=TA_LEFT, spaceAfter=2,
        leading=13, tracking=0.3,
    ),
    "title": ParagraphStyle(
        "title", fontName="Helvetica-Bold", fontSize=19,
        textColor=PETROL, alignment=TA_LEFT, spaceBefore=2, spaceAfter=10,
        leading=23,
    ),
    "subtitle": ParagraphStyle(
        "subtitle", fontName="Helvetica-Oblique", fontSize=11.5,
        textColor=GREY_TEXT, alignment=TA_LEFT, spaceAfter=14,
        leading=15,
    ),
    "sectionhead": ParagraphStyle(
        "sectionhead", fontName="Helvetica-Bold", fontSize=12.5,
        textColor=PETROL, alignment=TA_LEFT, spaceBefore=10, spaceAfter=6,
        leading=15,
    ),
    "body": ParagraphStyle(
        "body", fontName="Helvetica", fontSize=11, textColor=GREY_TEXT,
        alignment=TA_LEFT, leading=15.5, spaceAfter=6,
    ),
    "bodybold": ParagraphStyle(
        "bodybold", fontName="Helvetica-Bold", fontSize=11,
        textColor=PETROL, alignment=TA_LEFT, leading=15.5, spaceAfter=4,
    ),
    "small": ParagraphStyle(
        "small", fontName="Helvetica", fontSize=9, textColor=GREY_TEXT,
        alignment=TA_LEFT, leading=12,
    ),
    "ticket_head": ParagraphStyle(
        "ticket_head", fontName="Helvetica-Bold", fontSize=12,
        textColor=PETROL, alignment=TA_LEFT, leading=14, spaceAfter=6,
    ),
    "ticket_prompt": ParagraphStyle(
        "ticket_prompt", fontName="Helvetica-Bold", fontSize=9.5,
        textColor=PETROL, alignment=TA_LEFT, leading=12, spaceAfter=4,
    ),
    "ticket_option": ParagraphStyle(
        "ticket_option", fontName="Helvetica", fontSize=8.7,
        textColor=GREY_TEXT, alignment=TA_LEFT, leading=11.5,
    ),
    "footer": ParagraphStyle(
        "footer", fontName="Helvetica", fontSize=7.5,
        textColor=PETROL, alignment=TA_LEFT, leading=9,
    ),
}


# ------------------------------------------------------------------
# 3. BRAINY-FLOWABLE (nutzt reale PNG-Assets aus der klartext-app)
# ------------------------------------------------------------------

class BrainyLogo(Flowable):
    """Platziert das Brainy-Maskottchen (Standard-Version) unten rechts
    im Rahmen als wiederkehrendes Marken-Element."""

    def __init__(self, size=2.1 * cm, image_path=BRAINY_MAIN):
        Flowable.__init__(self)
        self.size = size
        self.image_path = image_path
        self.width = size
        self.height = size

    def draw(self):
        if os.path.exists(self.image_path):
            self.canv.drawImage(
                self.image_path, 0, 0, width=self.size, height=self.size,
                preserveAspectRatio=True, mask="auto",
            )


def brainy_icon_flowable(image_path, size=0.85 * cm):
    """Kleines Brainy-Icon (z. B. Barometer-Ampel-Gesichter) als Image-Flowable."""
    if os.path.exists(image_path):
        img = Image(image_path, width=size, height=size)
        img.hAlign = "CENTER"
        return img
    return Spacer(size, size)


def draw_k_badge(c, x, y, size, bg_color=PETROL, letter_color=WHITE, border_color=None):
    """Zeichnet das offizielle KLARTEXT-'K'-Monogramm (abgerundetes Quadrat,
    serifenbetontes K) – das bestehende, erwachsenere Markenzeichen aus
    Mentoring-Material & App-Icon. Ersetzt Brainy ab der Zielgruppe
    Jugendliche/Berufsvorbereitung."""
    c.saveState()
    c.setFillColor(bg_color)
    c.roundRect(x, y, size, size, size * 0.16, fill=1, stroke=0)
    if border_color:
        c.setStrokeColor(border_color)
        c.setLineWidth(1.1)
        c.roundRect(x, y, size, size, size * 0.16, fill=0, stroke=1)
    c.setFillColor(letter_color)
    c.setFont("Times-Bold", size * 0.62)
    # vertikal optisch zentrieren (Times-Bold hat Overshoot oben/unten)
    c.drawCentredString(x + size / 2, y + size * 0.30, "K")
    c.restoreState()


def draw_kopfband(c, x, top_y, w, accent_color, tagline, height=1.7 * cm):
    """Zeichnet das verbindliche Kopfband (KLARTEXT-Branding-Pflicht): K-Logo +
    Wortmarke 'KLARTEXT-Mentoring' auf einem Balken in der produktspezifischen
    Akzentfarbe. Gibt die y-Koordinate der Bandunterkante zurueck."""
    band_y = top_y - height
    c.saveState()
    c.setFillColor(accent_color)
    c.roundRect(x, band_y, w, height, 5, fill=1, stroke=0)
    c.restoreState()

    badge_size = height - 0.5 * cm
    badge_x = x + 0.35 * cm
    badge_y = band_y + (height - badge_size) / 2
    draw_k_badge(c, badge_x, badge_y, badge_size, bg_color=PETROL, letter_color=WHITE, border_color=SAGE)

    c.saveState()
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 13.5)
    c.drawString(badge_x + badge_size + 0.35 * cm, band_y + height * 0.58, "KLARTEXT-Mentoring")
    c.setFont("Helvetica-Oblique", 8.7)
    c.drawString(badge_x + badge_size + 0.35 * cm, band_y + height * 0.22, tagline)
    c.restoreState()
    return band_y


class KBadgeLogo(Flowable):
    """Flowable-Variante von draw_k_badge fuer den Einsatz in Tables/Story."""

    def __init__(self, size=1.5 * cm):
        Flowable.__init__(self)
        self.size = size
        self.width = size
        self.height = size

    def draw(self):
        draw_k_badge(self.canv, 0, 0, self.size)


# ------------------------------------------------------------------
# 4. SEITEN-RAHMEN + FUSSZEILE (Petrol-Rahmen ca. 1 cm vom Rand)
# ------------------------------------------------------------------

def draw_page_frame(c: pdfcanvas.Canvas, doc, footer_text=COPYRIGHT_FOOTER):
    c.saveState()
    # Weißer Hintergrund (tonersparend – kein Fill nötig, Seite ist bereits weiß)
    # feiner Petrol-Rahmen, ca. 1 cm vom Rand
    c.setStrokeColor(PETROL)
    c.setLineWidth(1.1)
    c.rect(MARGIN, MARGIN, PAGE_W - 2 * MARGIN, PAGE_H - 2 * MARGIN)

    # dezente Eckakzente (Sage) oben links
    c.setStrokeColor(SAGE)
    c.setLineWidth(2.4)
    corner = 0.55 * cm
    c.line(MARGIN, PAGE_H - MARGIN, MARGIN + corner, PAGE_H - MARGIN)
    c.line(MARGIN, PAGE_H - MARGIN, MARGIN, PAGE_H - MARGIN - corner)

    # Fusszeile
    c.setFont("Helvetica", 7.5)
    c.setFillColor(PETROL)
    c.drawString(MARGIN + FRAME_PAD, MARGIN - 0.05 * cm + 0.25 * cm, footer_text)
    c.drawRightString(
        PAGE_W - MARGIN - FRAME_PAD, MARGIN - 0.05 * cm + 0.25 * cm,
        f"Seite {doc.page}",
    )
    c.restoreState()


def build_frame():
    return Frame(
        MARGIN + FRAME_PAD, MARGIN + FRAME_PAD,
        PAGE_W - 2 * MARGIN - 2 * FRAME_PAD,
        PAGE_H - 2 * MARGIN - 2 * FRAME_PAD,
        id="main", showBoundary=0,
        leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0,
    )


def make_doc(filename, doc_title, mode):
    doc = BaseDocTemplate(
        filename, pagesize=A4,
        leftMargin=0, rightMargin=0, topMargin=0, bottomMargin=0,
        title=doc_title,
    )
    template = PageTemplate(
        id="klartext",
        frames=[build_frame()],
        onPage=lambda c, d: on_page_router(c, d, mode),
    )
    doc.addPageTemplates([template])
    return doc


# ------------------------------------------------------------------
# 5. WIEDERVERWENDBARE UI-BAUSTEINE
# ------------------------------------------------------------------

def header_block(kicker, title, subtitle=None):
    elems = [
        Paragraph(kicker.upper(), STYLES["header"]),
        Paragraph(title, STYLES["title"]),
    ]
    if subtitle:
        elems.append(Paragraph(subtitle, STYLES["subtitle"]))
    return elems


def sage_divider(width):
    t = Table([[""]], colWidths=[width], rowHeights=[0.06 * cm])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), SAGE)]))
    return t


def footer_brainy_row(content_width, note_text="", logo="brainy"):
    """Untere Zeile mit optionalem Hinweistext links und Marken-Logo unten rechts.
    logo='brainy' (Grundschule) oder logo='k' (Jugendliche/Berufsvorbereitung –
    das erwachsenere KLARTEXT-'K'-Monogramm statt Brainy)."""
    note = Paragraph(note_text, STYLES["footer"]) if note_text else Spacer(1, 1)
    mark = BrainyLogo(size=2.0 * cm) if logo == "brainy" else KBadgeLogo(size=1.5 * cm)
    t = Table(
        [[note, mark]],
        colWidths=[content_width - 2.3 * cm, 2.3 * cm],
    )
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "BOTTOM"),
        ("ALIGN", (1, 0), (1, 0), "RIGHT"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    return t


# ------------------------------------------------------------------
# 6. PDF 1 – SEITE 1: "kLAR am Küchentisch"
# ------------------------------------------------------------------

def page1_klar_kuechentisch(content_width):
    story = [Spacer(1, 1.95 * cm)]  # Platz fuer das Kopfband (K-Logo + Wortmarke)
    story += header_block(
        "KLARTEXT · Co-Regulation für zu Hause",
        "kLAR am Küchentisch",
        "Das kLAR-Modell – übersetzt für den Alltag zu Hause",
    )
    story.append(sage_divider(content_width))
    story.append(Spacer(1, 10))
    story.append(Paragraph(
        "Wenn es zu Hause turbulent wird, hilft die gleiche Struktur, die "
        "auch in der Schule Sicherheit gibt. So sprechen Schule und "
        "Zuhause dieselbe Sprache – das kLAR-Modell:",
        STYLES["body"],
    ))
    story.append(Spacer(1, 8))

    rows_data = [
        ("k", "Kontakt auf Augenhöhe",
         "Auf die Höhe deines Kindes gehen (hinknien, hinsetzen), ruhig "
         "zugewandt bleiben – nicht von oben herab und nicht aus der Distanz sprechen."),
        ("L", "Leise Stimme",
         "Lautstärke und Tempo bewusst senken. Eine leise, langsame Stimme "
         "wirkt beruhigend und signalisiert: Hier ist kein Streit nötig."),
        ("A", "Atem-Ballon nutzen",
         "Gemeinsam den 'Atem-Ballon' aufblasen: langsam durch die Nase "
         "einatmen, Bauch wölbt sich wie ein Ballon, durch den Mund ausatmen."),
        ("R", "Reizreduktion & Pause gewähren",
         "Reize reduzieren (Lautstärke, Licht, Menschen) und eine Pause ohne "
         "Druck ermöglichen, bevor weitergesprochen oder weitergemacht wird."),
    ]

    table_rows = []
    for letter, headline, text in rows_data:
        badge = Table([[letter]], colWidths=[1.05 * cm], rowHeights=[1.05 * cm])
        badge.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), SAGE),
            ("TEXTCOLOR", (0, 0), (-1, -1), WHITE),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, -1), 15),
            ("ROUNDEDCORNERS", [6, 6, 6, 6]),
        ]))
        text_cell = [
            Paragraph(headline, STYLES["bodybold"]),
            Paragraph(text, STYLES["body"]),
        ]
        table_rows.append([badge, text_cell])

    t = Table(table_rows, colWidths=[1.4 * cm, content_width - 1.4 * cm])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 9),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
        ("LINEBELOW", (0, 0), (-1, -2), 0.5, SAND),
    ]))
    story.append(t)

    story.append(Spacer(1, 12))
    tip = Table(
        [[Paragraph(
            "<b>Gut zu wissen:</b> Euer Kind erlebt kLAR bereits in der Schule. "
            "Wenn ihr zu Hause dieselben Wörter und Schritte nutzt, entsteht "
            "Wiedererkennung und Sicherheit – in beiden Welten.",
            STYLES["body"],
        )]],
        colWidths=[content_width],
    )
    tip.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), SAND),
        ("BOX", (0, 0), (-1, -1), 0.6, SAGE),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
    ]))
    story.append(tip)
    story.append(Spacer(1, 14))
    story.append(footer_brainy_row(
        content_width,
        "Brainy begleitet dein Kind auch in der Schule – dieselben Symbole, "
        "dieselbe Sprache.",
    ))
    return story


# ------------------------------------------------------------------
# 7. PDF 1 – SEITE 2: "Unser Hausaufgaben-Schrittplan"
# ------------------------------------------------------------------

def page2_hausaufgaben_schrittplan(content_width):
    story = []
    story += header_block(
        "KLARTEXT · Struktur für den Schreibtisch zu Hause",
        "Unser Hausaufgaben-Schrittplan",
        "Zum Ausfüllen, Ankreuzen und Aufhängen am Schreibtisch",
    )
    story.append(sage_divider(content_width))
    story.append(Spacer(1, 10))
    story.append(Paragraph(
        "Gemeinsam ausfüllen und danach griffbereit über dem Schreibtisch "
        "aufhängen. Jeder Schritt wird nach Erledigung abgehakt.",
        STYLES["body"],
    ))
    story.append(Spacer(1, 10))

    steps = [
        "Arbeitsplatz vorbereiten (Reize reduzieren, Material bereitlegen)",
        "Aufgabe anschauen und in eigenen Worten wiederholen",
        "In kleinen Etappen bearbeiten – nach jeder Etappe kurz innehalten",
        "Ergebnis überprüfen (allein oder gemeinsam)",
        "Erledigtes einpacken und sich selbst loben",
    ]

    rows = []
    for i, text in enumerate(steps, start=1):
        num = Table([[str(i)]], colWidths=[1.15 * cm], rowHeights=[1.15 * cm])
        num.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), PETROL),
            ("TEXTCOLOR", (0, 0), (-1, -1), WHITE),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, -1), 16),
            ("ROUNDEDCORNERS", [6, 6, 6, 6]),
        ]))
        label = Paragraph(f"<b>Schritt {i}:</b> {text}", STYLES["body"])
        checkbox = CheckboxFlowable(size=0.55 * cm)
        write_box = Table([[""]], colWidths=[content_width - 5.3 * cm], rowHeights=[1.3 * cm])
        write_box.setStyle(TableStyle([
            ("BOX", (0, 0), (-1, -1), 0.7, SAGE),
            ("BACKGROUND", (0, 0), (-1, -1), WHITE),
        ]))
        rows.append([num, [label, Spacer(1, 3), write_box], checkbox])

    t = Table(rows, colWidths=[1.5 * cm, content_width - 3.3 * cm, 1.8 * cm])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ALIGN", (2, 0), (2, -1), "CENTER"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("LINEBELOW", (0, 0), (-1, -2), 0.4, SAND),
    ]))
    story.append(t)
    story.append(Spacer(1, 10))
    story.append(footer_brainy_row(
        content_width,
        "Geschafft? Dann gemeinsam abhaken und feiern!",
    ))
    return story


class CheckboxFlowable(Flowable):
    """Zeichnet ein leeres, ankreuzbares Kästchen (Vektor, kein Unicode-Font-Risiko)."""

    def __init__(self, size=0.5 * cm, box_color=PETROL):
        Flowable.__init__(self)
        self.size = size
        self.width = size
        self.height = size
        self.box_color = box_color

    def draw(self):
        self.canv.saveState()
        self.canv.setStrokeColor(self.box_color)
        self.canv.setLineWidth(1.3)
        self.canv.rect(0, 0, self.size, self.size, fill=0, stroke=1)
        self.canv.restoreState()


# ------------------------------------------------------------------
# 8. PDF 1 – SEITE 3: "1-Minuten-Postmappen-Ticket" (A5 x 2 auf A4)
# ------------------------------------------------------------------

def draw_dashed_cut_line(c, x, y1, y2):
    c.saveState()
    c.setStrokeColor(PETROL)
    c.setLineWidth(0.7)
    c.setDash(3, 3)
    c.line(x, y1, x, y2)
    c.restoreState()
    # kleine Scheren-Andeutung (zwei kurze Diagonalen) oben
    c.saveState()
    c.setStrokeColor(SAGE)
    c.setLineWidth(1.2)
    c.line(x - 0.15 * cm, y2 + 0.15 * cm, x + 0.15 * cm, y2 - 0.15 * cm)
    c.line(x - 0.15 * cm, y2 - 0.15 * cm, x + 0.15 * cm, y2 + 0.15 * cm)
    c.restoreState()


def draw_checkbox_line(c, x, y, label, box_size=0.38 * cm, font_size=8.8):
    c.saveState()
    c.setStrokeColor(PETROL)
    c.setLineWidth(1.0)
    c.rect(x, y - box_size + 0.08 * cm, box_size, box_size, fill=0, stroke=1)
    c.setFont("Helvetica", font_size)
    c.setFillColor(GREY_TEXT)
    c.drawString(x + box_size + 0.22 * cm, y - box_size + 0.18 * cm, label)
    c.restoreState()


def draw_weather_barometer(c, x, y, label_prefix=""):
    """Zeichnet die drei Barometer-Ampel-Optionen mit Brainy-Ingra-Icons."""
    icons = [
        (BRAINY_GRUEN, "Grün", "#2E7D32"),
        (BRAINY_GELB, "Gelb", "#B8860B"),
        (BRAINY_ORANGE, "Orange", "#C46200"),
    ]
    icon_size = 1.05 * cm
    gap = 2.55 * cm
    for i, (path, name, hexcol) in enumerate(icons):
        cx = x + i * gap
        if os.path.exists(path):
            c.drawImage(
                path, cx, y, width=icon_size, height=icon_size,
                preserveAspectRatio=True, mask="auto",
            )
        c.setStrokeColor(PETROL)
        c.setLineWidth(1.0)
        box_y = y - 0.18 * cm
        box_size = 0.34 * cm
        c.rect(cx + icon_size / 2 - box_size / 2, box_y - box_size, box_size, box_size, fill=0, stroke=1)
        c.setFont("Helvetica", 7.8)
        c.setFillColor(colors.HexColor(hexcol))
        c.drawCentredString(cx + icon_size / 2, box_y - box_size - 0.32 * cm, name)


def draw_ticket_half(c, x0, y0, w, h, side):
    """Zeichnet eine A5-Ticket-Hälfte. side: 'lk' (links) oder 'eltern' (rechts)."""
    pad = 0.5 * cm
    x = x0 + pad
    y_top = y0 + h - pad
    inner_w = w - 2 * pad

    # Kopfbereich
    c.setFillColor(PETROL)
    c.setFont("Helvetica-Bold", 8.5)
    c.drawString(x, y_top, "KLARTEXT · 1-Minuten-Postmappen-Ticket")
    c.setStrokeColor(SAGE)
    c.setLineWidth(1.3)
    c.line(x, y_top - 0.22 * cm, x + inner_w, y_top - 0.22 * cm)

    cursor_y = y_top - 0.9 * cm

    if side == "lk":
        c.setFillColor(PETROL)
        c.setFont("Helvetica-Bold", 11.5)
        c.drawString(x, cursor_y, "Für die Postmappe – von der Schule")
        cursor_y -= 0.65 * cm

        c.setFont("Helvetica-Bold", 9.5)
        c.setFillColor(GREY_TEXT)
        c.drawString(x, cursor_y, "Das war heute dein Highlight-Erfolg:")
        cursor_y -= 0.55 * cm

        options = [
            "Einem Freund geholfen",
            "Fokussiert gearbeitet",
            "Stopp-Signal akzeptiert",
            "Etwas Neues ausprobiert",
        ]
        for opt in options:
            draw_checkbox_line(c, x, cursor_y, opt)
            cursor_y -= 0.62 * cm

        cursor_y -= 0.35 * cm
        c.setFont("Helvetica-Bold", 9.5)
        c.setFillColor(GREY_TEXT)
        c.drawString(x, cursor_y, "Barometer-Wetter heute:")
        cursor_y -= 1.55 * cm
        draw_weather_barometer(c, x, cursor_y)
        cursor_y -= 0.9 * cm

        c.setFont("Helvetica", 7.6)
        c.setFillColor(PETROL)
        c.drawString(x, y0 + pad * 0.3, "Handzeichen LK / Schulbegleitung: ______________________")

    else:  # eltern
        c.setFillColor(PETROL)
        c.setFont("Helvetica-Bold", 11.5)
        c.drawString(x, cursor_y, "Für die Postmappe – von zu Hause")
        cursor_y -= 0.65 * cm

        c.setFont("Helvetica-Bold", 9.5)
        c.setFillColor(GREY_TEXT)
        c.drawString(x, cursor_y, "So lief unser Nachmittag zu Hause:")
        cursor_y -= 0.55 * cm

        options1 = [
            "Brauchte erst mal Rückzug",
            "Direkt voller Energie",
            "Normaler Trubel",
        ]
        for opt in options1:
            draw_checkbox_line(c, x, cursor_y, opt)
            cursor_y -= 0.62 * cm

        cursor_y -= 0.3 * cm
        c.setFont("Helvetica-Bold", 9.5)
        c.setFillColor(GREY_TEXT)
        c.drawString(x, cursor_y, "Unser Entspannungs-Schritt für heute Abend:")
        cursor_y -= 0.55 * cm

        options2 = [
            "Atmen mit Brainys Atemballon",
            "Liegende Acht malen",
            "5 Minuten Quatsch-Zeit",
        ]
        for opt in options2:
            draw_checkbox_line(c, x, cursor_y, opt)
            cursor_y -= 0.62 * cm

        c.setFont("Helvetica", 7.6)
        c.setFillColor(PETROL)
        c.drawString(x, y0 + pad * 0.3, "Handzeichen Eltern: ______________________")

    # äußerer Rahmen der Ticket-Hälfte (Sand-Hintergrund-Karte)
    c.saveState()
    c.setStrokeColor(SAGE)
    c.setLineWidth(0.8)
    c.roundRect(x0 + 0.15 * cm, y0 + 0.15 * cm, w - 0.3 * cm, h - 0.3 * cm, 8, fill=0, stroke=1)
    c.restoreState()


def draw_ticket_page(c, doc):
    """Vollständige Seite 3 (Ticket) direkt auf dem Canvas – exakte A5-Positionierung."""
    draw_page_frame(c, doc)

    inner_x = MARGIN + FRAME_PAD
    inner_y = MARGIN + FRAME_PAD
    inner_w = PAGE_W - 2 * MARGIN - 2 * FRAME_PAD
    inner_h = PAGE_H - 2 * MARGIN - 2 * FRAME_PAD

    # Kopfzeile über den zwei Spalten
    c.setFont("Helvetica-Bold", 9.5)
    c.setFillColor(PETROL)
    c.drawString(inner_x, inner_y + inner_h - 0.35 * cm,
                 "KLARTEXT · Co-Regulation für zu Hause")
    c.setFont("Helvetica-Bold", 15)
    c.drawString(inner_x, inner_y + inner_h - 1.05 * cm,
                 "Das 1-Minuten-Postmappen-Ticket")
    c.setFont("Helvetica-Oblique", 9)
    c.setFillColor(GREY_TEXT)
    c.drawString(inner_x, inner_y + inner_h - 1.5 * cm,
                 "Bitte trennen, ausfüllen und in die Postmappe legen – so bleiben Schule und Zuhause im Austausch.")

    tickets_top = inner_y + inner_h - 2.1 * cm
    ticket_h = tickets_top - inner_y
    half_w = inner_w / 2.0

    draw_ticket_half(c, inner_x, inner_y, half_w, ticket_h, side="lk")
    draw_ticket_half(c, inner_x + half_w, inner_y, half_w, ticket_h, side="eltern")

    # gestrichelte Schneidelinie in der Mitte
    draw_dashed_cut_line(c, inner_x + half_w, inner_y + 0.1 * cm, tickets_top - 0.1 * cm)

    # Brainy-Logo mittig auf der Schneidelinie (im unteren, freien Bereich) als
    # verbindendes Bruecken-Symbol zwischen Schule und Zuhause
    if os.path.exists(BRAINY_MAIN):
        b_size = 2.0 * cm
        bx = inner_x + half_w - b_size / 2
        by = inner_y + ticket_h * 0.22
        c.saveState()
        c.setFillColor(WHITE)
        c.circle(bx + b_size / 2, by + b_size / 2, b_size / 2 + 0.06 * cm, fill=1, stroke=0)
        c.restoreState()
        c.drawImage(
            BRAINY_MAIN, bx, by,
            width=b_size, height=b_size, preserveAspectRatio=True, mask="auto",
        )


# ------------------------------------------------------------------
# 9. PDF 2 – SEITE 1: "Gemeinsam durch den Berufs-Dschungel"
# ------------------------------------------------------------------

def page1_berufsdschungel(content_width):
    story = [Spacer(1, 1.95 * cm)]  # Platz fuer das Kopfband (K-Logo + Wortmarke)
    story += header_block(
        "KLARTEXT · Begleitung beim Übergang Schule → Beruf",
        "Gemeinsam durch den Berufs-Dschungel",
        "Ein Leitfaden für Eltern von Jugendlichen in der Berufsorientierung",
    )
    story.append(sage_divider(content_width))
    story.append(Spacer(1, 10))
    story.append(Paragraph(
        "Die Berufsfindung ist für Jugendliche mit hohem Druck verbunden. "
        "Diese drei goldenen Regeln helfen euch, ohne zusätzlichen Druck "
        "zu unterstützen:",
        STYLES["body"],
    ))
    story.append(Spacer(1, 8))

    rules = [
        ("1", "Interesse zeigen statt Druck aufbauen",
         "Offene Fragen statt Forderungen: 'Was hat dir daran gefallen?' "
         "statt 'Hast du dich schon beworben?'. Druck erzeugt Rückzug, "
         "Interesse erzeugt Vertrauen."),
        ("2", "Kleine Schritte statt großer Entscheidungen",
         "Ein Praktikum, ein Schnuppertag, ein Gespräch reichen als nächster "
         "Schritt – die endgültige Berufsentscheidung muss nicht heute fallen."),
        ("3", "Stärken sichtbar machen statt Defizite betonen",
         "Auch außerschulische Fähigkeiten zählen: Ausdauer beim Sport, "
         "Sorgfalt beim Basteln, Verantwortung für ein Haustier – das sind "
         "berufsrelevante Stärken."),
    ]
    table_rows = []
    for num, headline, text in rules:
        badge = Table([[num]], colWidths=[1.05 * cm], rowHeights=[1.05 * cm])
        badge.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), PETROL),
            ("TEXTCOLOR", (0, 0), (-1, -1), WHITE),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, -1), 15),
            ("ROUNDEDCORNERS", [6, 6, 6, 6]),
        ]))
        text_cell = [
            Paragraph(headline, STYLES["bodybold"]),
            Paragraph(text, STYLES["body"]),
        ]
        table_rows.append([badge, text_cell])

    t = Table(table_rows, colWidths=[1.4 * cm, content_width - 1.4 * cm])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LINEBELOW", (0, 0), (-1, -2), 0.5, SAND),
    ]))
    story.append(t)
    story.append(Spacer(1, 12))

    story.append(Paragraph("Verborgene Stärken aus dem Hobby-Check", STYLES["sectionhead"]))
    story.append(Paragraph(
        "Aus der Schule kennt ihr bereits den Hobby-Check, der Freizeit-"
        "Interessen in Stärken übersetzt. Diese Übersetzung lohnt sich auch "
        "zu Hause im Gespräch:",
        STYLES["body"],
    ))

    hobby_table = Table(
        [
            [Paragraph("<b>Hobby / Interesse</b>", STYLES["small"]),
             Paragraph("<b>Mögliche berufliche Stärke</b>", STYLES["small"])],
            [Paragraph("Gaming / Strategiespiele", STYLES["body"]),
             Paragraph("Planvolles Vorgehen, Ausdauer, Problemlösung", STYLES["body"])],
            [Paragraph("Handwerkeln / Basteln", STYLES["body"]),
             Paragraph("Feinmotorik, Sorgfalt, praktisches Denken", STYLES["body"])],
            [Paragraph("Tiere versorgen", STYLES["body"]),
             Paragraph("Verantwortungsbewusstsein, Verlässlichkeit", STYLES["body"])],
            [Paragraph("Musik / Kreatives", STYLES["body"]),
             Paragraph("Ausdrucksfähigkeit, Durchhaltevermögen", STYLES["body"])],
        ],
        colWidths=[content_width * 0.42, content_width * 0.58],
    )
    hobby_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), SAGE),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, SAND]),
        ("BOX", (0, 0), (-1, -1), 0.6, SAGE),
        ("INNERGRID", (0, 0), (-1, -1), 0.4, SAND),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    story.append(hobby_table)

    story.append(Spacer(1, 14))
    story.append(footer_brainy_row(
        content_width,
        "Das KLARTEXT-Zeichen begleitet Jugendliche auch beim Hobby-Stärken-Profil "
        "in der Schule – vom Brainy der Grundschulzeit bis zum eigenen Übergang in den Beruf.",
        logo="k",
    ))
    return story


# ------------------------------------------------------------------
# 10. PDF 2 – SEITE 2: "1-Minuten-Zukunfts-Ticket" (Brücken-Ticket)
# ------------------------------------------------------------------

def wrap_text_lines(text, font_name, font_size, max_width):
    """Bricht Text an Wortgrenzen um, sodass jede Zeile in max_width passt."""
    words = text.split()
    lines, current = [], ""
    for word in words:
        candidate = f"{current} {word}".strip()
        if stringWidth(candidate, font_name, font_size) <= max_width or not current:
            current = candidate
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_bridge_column(c, x, y_top, w, title, prompt, options, is_signature_area=False):
    cursor_y = y_top
    c.setFillColor(PETROL)
    c.setFont("Helvetica-Bold", 11.5)
    c.drawString(x, cursor_y, title)
    cursor_y -= 0.5 * cm
    c.setStrokeColor(SAGE)
    c.setLineWidth(1.1)
    c.line(x, cursor_y, x + w, cursor_y)
    cursor_y -= 0.55 * cm

    c.setFont("Helvetica-Bold", 9.5)
    c.setFillColor(GREY_TEXT)
    for line in wrap_text_lines(prompt, "Helvetica-Bold", 9.5, w):
        c.drawString(x, cursor_y, line)
        cursor_y -= 0.42 * cm
    cursor_y -= 0.2 * cm

    for opt in options:
        draw_checkbox_line(c, x, cursor_y, opt, box_size=0.4 * cm, font_size=9.2)
        cursor_y -= 0.68 * cm

    return cursor_y


def page2_zukunftsticket(content_width):
    """Seite wird komplett im Canvas gezeichnet (siehe draw_zukunftsticket_page),
    damit Spalten, Brücken-Zone und K-Badge exakt positioniert werden können.
    Die Story bleibt bewusst leer, damit die Seite dennoch im Fluss existiert."""
    return [Spacer(1, 1)]


def draw_zukunftsticket_page(c, doc):
    draw_page_frame(c, doc)

    inner_x = MARGIN + FRAME_PAD
    inner_y = MARGIN + FRAME_PAD
    inner_w = PAGE_W - 2 * MARGIN - 2 * FRAME_PAD
    inner_h = PAGE_H - 2 * MARGIN - 2 * FRAME_PAD

    c.setFont("Helvetica-Bold", 9.5)
    c.setFillColor(PETROL)
    c.drawString(inner_x, inner_y + inner_h - 0.35 * cm,
                 "KLARTEXT · Begleitung beim Übergang Schule → Beruf")
    c.setFont("Helvetica-Bold", 16)
    c.drawString(inner_x, inner_y + inner_h - 1.05 * cm,
                 "Das 1-Minuten-Zukunfts-Ticket")
    c.setFont("Helvetica-Oblique", 9)
    c.setFillColor(GREY_TEXT)
    c.drawString(inner_x, inner_y + inner_h - 1.5 * cm,
                 "Das Brücken-Gesprächs-Ticket – 1 Minute für ein ehrliches Gespräch.")

    col_top = inner_y + inner_h - 2.2 * cm
    col_gap = 0.6 * cm
    col_w = (inner_w - col_gap) / 2.0

    # Brücken-Zone (unten, über beide Spalten) — grosszuegig bemessen, damit
    # kein toter Leerraum zwischen Ankreuz-Optionen und Vereinbarungsfeld entsteht
    bridge_zone_h = 9.4 * cm
    bridge_y_top = inner_y + bridge_zone_h

    # Mittlere Trennlinie (gestrichelt) zwischen den Spalten, oberhalb der Brücken-Zone
    draw_dashed_cut_line(
        c, inner_x + col_w + col_gap / 2,
        bridge_y_top + 0.3 * cm, col_top + 0.3 * cm,
    )

    # Spalte 1 – Jugendlicher
    draw_bridge_column(
        c, inner_x, col_top, col_w,
        title="Für dich – Jugendliche/r",
        prompt="Was wünschst du dir gerade von deinen Eltern am meisten?",
        options=[
            "Keine Fragen zum Job für 3 Tage",
            "Lass mich ausschlafen",
            "Hilf mir bei dieser einen Mail",
            "Lass uns ein Hobby-Stärken-Profil ausfüllen",
        ],
    )

    # Spalte 2 – Eltern
    draw_bridge_column(
        c, inner_x + col_w + col_gap, col_top, col_w,
        title="Für euch – Eltern",
        prompt="Was fällt mir gerade am schwersten?",
        options=[
            "Sorge um deine Zukunft",
            "Kommunikations-Kluft",
            "Hilflosigkeit",
        ],
    )

    # --- Brücken-Zone: Karte mit Vereinbarungstext, Schreibfeld, Unterschriften ---
    box_y0 = inner_y + 0.2 * cm
    box_h = bridge_zone_h - 0.2 * cm
    c.saveState()
    c.setFillColor(SAND)
    c.roundRect(inner_x, box_y0, inner_w, box_h, 9, fill=1, stroke=0)
    c.setStrokeColor(SAGE)
    c.setLineWidth(0.9)
    c.roundRect(inner_x, box_y0, inner_w, box_h, 9, fill=0, stroke=1)
    c.restoreState()

    pad_x = 0.55 * cm
    text_right_margin = 2.2 * cm  # Platz fuer K-Badge oben rechts freihalten

    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(PETROL)
    c.drawString(inner_x + pad_x, bridge_y_top - 0.75 * cm,
                 "Die Brücke: Unsere kleinste gemeinsame Vereinbarung für die Woche")
    c.setFont("Helvetica-Oblique", 8.7)
    c.setFillColor(GREY_TEXT)
    c.drawString(inner_x + pad_x, bridge_y_top - 1.2 * cm,
                 "Gemeinsam eine einzige, realistische Kleinigkeit festhalten – nicht mehr.")

    # gepunktete Schreiblinien (grosszuegiger Platz)
    c.saveState()
    c.setStrokeColor(PETROL)
    c.setLineWidth(0.8)
    c.setDash(1, 2)
    for i, offset in enumerate([1.95, 2.75, 3.55]):
        c.line(inner_x + pad_x, bridge_y_top - offset * cm,
               inner_x + inner_w - pad_x, bridge_y_top - offset * cm)
    c.restoreState()

    # Unterschriften-Felder
    sign_y = box_y0 + 1.0 * cm
    half_w2 = inner_w / 2.0
    c.setFont("Helvetica", 8.5)
    c.setFillColor(GREY_TEXT)
    c.setStrokeColor(PETROL)
    c.setLineWidth(0.7)
    c.line(inner_x + pad_x, sign_y, inner_x + half_w2 - 0.3 * cm, sign_y)
    c.drawString(inner_x + pad_x, sign_y - 0.38 * cm, "Unterschrift Jugendliche/r")
    c.line(inner_x + half_w2 + 0.3 * cm, sign_y, inner_x + inner_w - pad_x, sign_y)
    c.drawString(inner_x + half_w2 + 0.3 * cm, sign_y - 0.38 * cm, "Unterschrift Eltern")

    # KLARTEXT-'K'-Badge oben rechts in der Bruecken-Zone (statt Brainy –
    # Jugendliche bekommen das erwachsenere Markenzeichen), freigehalten von Text/Linien
    k_size = 1.35 * cm
    kx = inner_x + inner_w - k_size - 0.45 * cm
    ky = bridge_y_top - k_size - 0.4 * cm
    draw_k_badge(c, kx, ky, k_size)


# ------------------------------------------------------------------
# 11. SEITEN-ROUTER
# ------------------------------------------------------------------

def on_page_router(c, doc, mode):
    """Zeichnet je nach PDF und aktueller Seitenzahl den passenden
    Custom-Canvas-Inhalt (Frame + Ticket-Layout)."""
    page_num = doc.page
    inner_x = MARGIN + FRAME_PAD
    inner_w = PAGE_W - 2 * MARGIN - 2 * FRAME_PAD
    top_y = PAGE_H - MARGIN - FRAME_PAD

    if mode == "grundschule":
        if page_num == 1:
            draw_page_frame(c, doc)
            draw_kopfband(c, inner_x, top_y, inner_w, ACCENT_GRUNDSCHULE,
                          "Eltern-Mitgabe-Set · Grundschule")
        elif page_num == 2:
            draw_page_frame(c, doc)
        elif page_num == 3:
            draw_ticket_page(c, doc)
    elif mode == "beruf":
        if page_num == 1:
            draw_page_frame(c, doc)
            draw_kopfband(c, inner_x, top_y, inner_w, ACCENT_BERUF,
                          "Eltern-Mitgabe-Set · Berufsvorbereitung")
        elif page_num == 2:
            draw_zukunftsticket_page(c, doc)


# ------------------------------------------------------------------
# 12. HAUPTPROGRAMM
# ------------------------------------------------------------------

def main():
    out_dir = os.path.dirname(os.path.abspath(__file__))
    content_width = PAGE_W - 2 * MARGIN - 2 * FRAME_PAD

    # --- PDF 1: Grundschule (Seite 1 & 2 als Flowables, Seite 3 komplett per Canvas) ---
    grundschule_path = os.path.join(out_dir, "KLARTEXT_ElternSet_Grundschule.pdf")
    doc1 = make_doc(grundschule_path, "KLARTEXT · Eltern-Mitgabe-Set Grundschule", mode="grundschule")
    story1 = []
    story1 += page1_klar_kuechentisch(content_width)
    story1.append(PageBreak())
    story1 += page2_hausaufgaben_schrittplan(content_width)
    story1.append(PageBreak())
    story1.append(Spacer(1, 1))  # Seite 3: Inhalt komplett via onPage (Ticket-Layout)
    doc1.build(story1)
    print(f"✓ erstellt: {grundschule_path}")

    # --- PDF 2: Berufsvorbereitung (Seite 1 als Flowables, Seite 2 komplett per Canvas) ---
    beruf_path = os.path.join(out_dir, "KLARTEXT_ElternSet_Berufsvorbereitung.pdf")
    doc2 = make_doc(beruf_path, "KLARTEXT · Eltern-Mitgabe-Set Berufsvorbereitung", mode="beruf")
    story2 = []
    story2 += page1_berufsdschungel(content_width)
    story2.append(PageBreak())
    story2.append(Spacer(1, 1))  # Seite 2: Inhalt komplett via onPage (Zukunfts-Ticket)
    doc2.build(story2)
    print(f"✓ erstellt: {beruf_path}")


if __name__ == "__main__":
    main()
