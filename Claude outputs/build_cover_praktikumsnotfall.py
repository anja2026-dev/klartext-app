#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Erzeugt das eduki-Deckblatt fuer die Praktikums-Notfall-Kaertchen &
Kuehlschrank-Superpower im bestehenden KLARTEXT-Cover-Template (identische
Massen/Logik wie build_eduki_covers.py / build_cover_kd15.py).
"""

import os
import subprocess
from reportlab.lib import colors
from reportlab.pdfgen import canvas as pdfcanvas
from reportlab.pdfbase.pdfmetrics import stringWidth

PT_W, PT_H = 850, 1190
SCALE = 2

BAND_H = 230
BADGE_X, BADGE_Y_TOP, BADGE_SIZE = 44, 83, 64
BADGE_RADIUS = 11
WORDMARK_X = 128
WORDMARK_BASELINE_TOP = 118
TAGLINE_BASELINE_TOP = 142
TITLE_X = 50
TITLE_BASELINE_1_TOP = 335
TITLE_LINE_HEIGHT = 76
LABEL_Y_TOP = 433
BOX_X, BOX_W, BOX_H = 50, 750, 97
BOX_Y_TOP = 517
BOX_RADIUS = 9
BRAINY_X0, BRAINY_SIZE = 572, 236
BRAINY_Y_TOP = 894
FOOTER_BASELINE_FROM_BOTTOM = 41

NAVY = colors.HexColor("#1B3A4B")
CREAM = colors.HexColor("#F5F0E8")
WHITE = colors.white
GREY_TEXT = colors.HexColor("#3A3A3A")
GREY_LIGHT = colors.HexColor("#969696")
DARK = colors.HexColor("#141414")

ACCENT_KUPFER = colors.HexColor("#A6643A")  # wiederverwendet vom Eltern-Set Berufsvorbereitung

ASSETS_DIR = os.path.dirname(os.path.abspath(__file__))
BRAINY_MAIN = os.path.join(ASSETS_DIR, "brainy.png")

SERIF = "Times-Bold"
SANS_BOLD = "Helvetica-Bold"
SANS = "Helvetica"
SANS_ITALIC = "Helvetica-Oblique"


def draw_tracked(c, x, y, text, font_name, size, fill, tracking=0.5):
    c.setFillColor(fill)
    c.setFont(font_name, size)
    for ch in text:
        c.drawString(x, y, ch)
        x += stringWidth(ch, font_name, size) + tracking


def wrap_text(text, font_name, size, max_width):
    words = text.split()
    lines, current = [], ""
    for word in words:
        candidate = f"{current} {word}".strip()
        if stringWidth(candidate, font_name, size) <= max_width or not current:
            current = candidate
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def build_cover_pdf(pdf_path, accent_color, tagline, title_lines, label_text,
                     description_text, box_label, box_text, footer_pages, show_brainy):
    c = pdfcanvas.Canvas(pdf_path, pagesize=(PT_W, PT_H))
    top = PT_H

    c.setFillColor(accent_color)
    c.rect(0, top - BAND_H, PT_W, BAND_H, fill=1, stroke=0)

    badge_y = top - BADGE_Y_TOP - BADGE_SIZE
    c.setFillColor(CREAM)
    c.roundRect(BADGE_X, badge_y, BADGE_SIZE, BADGE_SIZE, BADGE_RADIUS, fill=1, stroke=0)
    c.setFillColor(NAVY)
    c.setFont(SERIF, BADGE_SIZE * 0.62)
    c.drawCentredString(BADGE_X + BADGE_SIZE / 2, badge_y + BADGE_SIZE * 0.30, "K")

    c.setFillColor(WHITE)
    c.setFont(SANS_BOLD, 27)
    c.drawString(WORDMARK_X, top - WORDMARK_BASELINE_TOP, "KLARTEXT-Mentoring")
    c.setFont(SANS_ITALIC, 16)
    c.drawString(WORDMARK_X, top - TAGLINE_BASELINE_TOP, tagline)

    c.setFillColor(accent_color)
    c.setFont(SERIF, 40)
    for i, line in enumerate(title_lines):
        c.drawString(TITLE_X, top - TITLE_BASELINE_1_TOP - i * TITLE_LINE_HEIGHT, line)

    draw_tracked(c, TITLE_X, top - LABEL_Y_TOP, label_text.upper(), SANS_BOLD, 12, accent_color, tracking=1)

    c.setFillColor(GREY_TEXT)
    c.setFont(SANS, 18)
    c.drawString(TITLE_X, top - LABEL_Y_TOP - 24, description_text)

    box_y = top - BOX_Y_TOP - BOX_H
    c.setFillColor(CREAM)
    c.roundRect(BOX_X, box_y, BOX_W, BOX_H, BOX_RADIUS, fill=1, stroke=0)
    draw_tracked(c, BOX_X + 23, box_y + BOX_H - 26, box_label.upper(), SANS_BOLD, 11, accent_color, tracking=1)
    c.setFillColor(DARK)
    c.setFont(SANS, 15)
    wrapped = wrap_text(box_text, SANS, 15, BOX_W - 46)
    for i, line in enumerate(wrapped[:2]):
        c.drawString(BOX_X + 23, box_y + BOX_H - 62 - i * 21, line)

    if show_brainy and os.path.exists(BRAINY_MAIN):
        brainy_y = top - BRAINY_Y_TOP - BRAINY_SIZE
        c.drawImage(BRAINY_MAIN, BRAINY_X0, brainy_y, width=BRAINY_SIZE, height=BRAINY_SIZE,
                    preserveAspectRatio=True, mask="auto")

    c.setFillColor(GREY_LIGHT)
    c.setFont(SANS_BOLD, 15)
    c.drawString(TITLE_X - 10, FOOTER_BASELINE_FROM_BOTTOM, "KLARTEXT-Mentoring")
    c.setFillColor(DARK)
    c.setFont(SANS_BOLD, 20)
    c.drawRightString(PT_W - 50, FOOTER_BASELINE_FROM_BOTTOM, footer_pages)

    c.showPage()
    c.save()
    print(f"erstellt: {pdf_path}")


def render_png_from_pdf(pdf_path, png_path):
    dpi = int(72 * SCALE)
    subprocess.run(["pdftoppm", "-png", "-r", str(dpi), "-singlefile", pdf_path, png_path[:-4]], check=True)
    print(f"erstellt: {png_path}")


def build_cover(out_dir, name, **kwargs):
    pdf_path = os.path.join(out_dir, f"{name}.pdf")
    png_path = os.path.join(out_dir, f"{name}.png")
    build_cover_pdf(pdf_path, **kwargs)
    render_png_from_pdf(pdf_path, png_path)


def main():
    out_dir = os.path.dirname(os.path.abspath(__file__))
    build_cover(
        out_dir,
        "KLARTEXT_Cover_PraktikumsNotfallkaertchen",
        accent_color=ACCENT_KUPFER,
        tagline="1,99 € · Arbeitslehre",
        title_lines=["Praktikums-", "Notfall-Kärtchen"],
        label_text="Für wen",
        description_text="Jugendliche Sek I · Berufsvorbereitung, ohne Maskottchen",
        box_label="Inhalt",
        box_text=(
            "Superpower-Card für den Kühlschrank (A5) + 2 Notfallkarten im "
            "Scheckkartenformat zum Ausschneiden & Laminieren."
        ),
        footer_pages="1 Seite",
        show_brainy=False,
    )


if __name__ == "__main__":
    main()
