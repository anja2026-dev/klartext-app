#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_praktikums_notfallkarten.py
KLARTEXT – Praktikums-Notfall-Kärtchen & Kühlschrank-Superpower (Sek I)

Eine DIN-A4-Hochformat-Seite im KLARTEXT-Corporate-Design:
  Obere Hälfte: Superpower-Card (A5 quer, zum Ausschneiden, Kühlschrank)
  Untere Hälfte: 2x Notfallkarten im Scheckkartenformat (zum Ausschneiden
                 + laminieren)

Reizarm, jugendgerecht, KEIN Brainy-Maskottchen (bewusste Entscheidung fuer
die Zielgruppe Berufsvorbereitung/Sek I - erwachsener/cooler wirken lassen).
Akzentfarbe Kupfer (#A6643A) wiederverwendet vom Eltern-Set Berufsvorbereitung,
damit beide Materialien als erkennbares Paar wirken.
"""

import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.pdfgen import canvas as pdfcanvas
from reportlab.pdfbase.pdfmetrics import stringWidth

# ------------------------------------------------------------------
# CORPORATE DESIGN
# ------------------------------------------------------------------
PETROL = colors.HexColor("#005F73")
SAGE = colors.HexColor("#8FBC8F")
SAND = colors.HexColor("#FAF0ED")
WHITE = colors.white
GREY_TEXT = colors.HexColor("#3A3A3A")
GREY_LIGHT = colors.HexColor("#8A8A8A")
DARK = colors.HexColor("#141414")
ACCENT_KUPFER = colors.HexColor("#A6643A")  # wiederverwendet vom Eltern-Set Berufsvorbereitung

COPYRIGHT_FOOTER = "© 2026 KLARTEXT-Mentoring · Anja Jolk · info@klartext-mentoring.de"

PAGE_W, PAGE_H = A4
MARGIN = 1.0 * cm

SANS = "Helvetica"
SANS_BOLD = "Helvetica-Bold"
SANS_IT = "Helvetica-Oblique"
SERIF_BOLD = "Times-Bold"


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


def draw_k_badge(c, x, y, size, bg_color=PETROL, letter_color=WHITE, border_color=None):
    c.saveState()
    c.setFillColor(bg_color)
    c.roundRect(x, y, size, size, size * 0.16, fill=1, stroke=0)
    if border_color:
        c.setStrokeColor(border_color)
        c.setLineWidth(1.1)
        c.roundRect(x, y, size, size, size * 0.16, fill=0, stroke=1)
    c.setFillColor(letter_color)
    c.setFont(SERIF_BOLD, size * 0.62)
    c.drawCentredString(x + size / 2, y + size * 0.30, "K")
    c.restoreState()


def draw_kopfband(c, x, top_y, w, accent_color, tagline, height=1.7 * cm):
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
    c.setFont(SANS_BOLD, 13.5)
    c.drawString(badge_x + badge_size + 0.35 * cm, band_y + height * 0.58, "KLARTEXT-Mentoring")
    c.setFont(SANS_IT, 8.7)
    c.drawString(badge_x + badge_size + 0.35 * cm, band_y + height * 0.22, tagline)
    c.restoreState()
    return band_y


def draw_page_frame(c, page_num=1):
    c.saveState()
    c.setStrokeColor(PETROL)
    c.setLineWidth(1.1)
    c.rect(MARGIN, MARGIN, PAGE_W - 2 * MARGIN, PAGE_H - 2 * MARGIN)
    c.setStrokeColor(SAGE)
    c.setLineWidth(2.4)
    corner = 0.55 * cm
    c.line(MARGIN, PAGE_H - MARGIN, MARGIN + corner, PAGE_H - MARGIN)
    c.line(MARGIN, PAGE_H - MARGIN, MARGIN, PAGE_H - MARGIN - corner)
    c.setFont(SANS, 7.5)
    c.setFillColor(PETROL)
    c.drawString(MARGIN + 0.6 * cm, MARGIN + 0.2 * cm, COPYRIGHT_FOOTER)
    c.drawRightString(PAGE_W - MARGIN - 0.6 * cm, MARGIN + 0.2 * cm, f"Seite {page_num}")
    c.restoreState()


def dashed_cut_rect(c, x, y, w, h, color=GREY_LIGHT, radius=6):
    c.saveState()
    c.setStrokeColor(color)
    c.setLineWidth(0.9)
    c.setDash(3, 2.5)
    c.roundRect(x, y, w, h, radius, fill=0, stroke=1)
    c.restoreState()


def scissors_label(c, x, y, text, color=GREY_LIGHT, size=8.5):
    c.saveState()
    c.setFillColor(color)
    c.setFont(SANS_IT, size)
    c.drawCentredString(x, y, f"✂  {text}  ✂")
    c.restoreState()


# ------------------------------------------------------------------
# OBERE HÄLFTE: SUPERPOWER-CARD (A5 quer)
# ------------------------------------------------------------------

def draw_superpower_card(c, x, top_y, w, h):
    dashed_cut_rect(c, x, top_y - h, w, h)
    scissors_label(c, x + w / 2, top_y + 0.15 * cm, "hier ausschneiden – für den Kühlschrank")

    pad = 0.7 * cm
    inner_x = x + pad
    inner_top = top_y - pad
    inner_w = w - 2 * pad

    c.setFillColor(ACCENT_KUPFER)
    c.setFont(SANS_BOLD, 19)
    c.drawString(inner_x, inner_top - 0.55 * cm, "MEIN PROFIL: MEINE SUPERPOWERS")
    c.setStrokeColor(ACCENT_KUPFER)
    c.setLineWidth(1.3)
    c.line(inner_x, inner_top - 0.8 * cm, inner_x + inner_w, inner_top - 0.8 * cm)

    # Linke Spalte: 3 Tiles mit Schreiblinien
    left_w = inner_w * 0.56
    tile_h = 2.05 * cm
    tile_gap = 0.7 * cm
    tile_y0 = inner_top - 1.5 * cm
    for i in range(3):
        ty = tile_y0 - i * (tile_h + tile_gap) - tile_h
        c.setFillColor(SAND)
        c.roundRect(inner_x, ty, left_w, tile_h, 4, fill=1, stroke=0)
        c.setFillColor(ACCENT_KUPFER)
        c.setFont(SANS_BOLD, 11)
        c.drawString(inner_x + 0.35 * cm, ty + tile_h - 0.6 * cm, f"SUPERPOWER {i + 1}")
        c.setStrokeColor(GREY_LIGHT)
        c.setLineWidth(0.7)
        c.line(inner_x + 0.3 * cm, ty + 0.3 * cm, inner_x + left_w - 0.3 * cm, ty + 0.3 * cm)

    # Rechte Spalte: QR-Platzhalter + Text
    right_x = inner_x + left_w + 0.55 * cm
    right_w = inner_w - left_w - 0.55 * cm
    qr_size = min(right_w, 4.2 * cm)
    qr_x = right_x + (right_w - qr_size) / 2
    qr_y = inner_top - 1.5 * cm - qr_size
    qr_img_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "qr_interessencheck.png")
    if os.path.exists(qr_img_path):
        pad_qr = qr_size * 0.06
        c.drawImage(qr_img_path, qr_x + pad_qr, qr_y + pad_qr, width=qr_size - 2 * pad_qr,
                    height=qr_size - 2 * pad_qr, preserveAspectRatio=True, mask="auto")
        c.setStrokeColor(PETROL)
        c.setLineWidth(1.1)
        c.rect(qr_x, qr_y, qr_size, qr_size, fill=0, stroke=1)
    else:
        c.setStrokeColor(PETROL)
        c.setLineWidth(1.1)
        c.rect(qr_x, qr_y, qr_size, qr_size, fill=0, stroke=1)
        c.setFillColor(PETROL)
        c.setFont(SANS_BOLD, 11)
        c.drawCentredString(qr_x + qr_size / 2, qr_y + qr_size / 2 + 5, "QR-CODE")
        c.setFont(SANS, 9)
        c.drawCentredString(qr_x + qr_size / 2, qr_y + qr_size / 2 - 11, "Interessen-Check")

    text_y = qr_y - 0.55 * cm
    caption = ("Unsicher, was deine Stärken sind? Scanne den Code und mach den "
               "2-Minuten-Interessen-Check – kostenlos, ohne Anmeldung.")
    lines = wrap_text(caption, SANS, 9, right_w)
    c.setFillColor(GREY_TEXT)
    c.setFont(SANS, 9)
    for i, line in enumerate(lines[:4]):
        c.drawCentredString(right_x + right_w / 2, text_y - i * 0.38 * cm, line)


# ------------------------------------------------------------------
# UNTERE HÄLFTE: 2 SCHECKKARTEN-NOTFALLKARTEN
# ------------------------------------------------------------------

CARD1_LINES = [
    ("Bei Unklarheit:",
     "„Ich möchte das gerne ordentlich machen. Könnten Sie mir diesen "
     "Arbeitsschritt bitte noch einmal kurz zeigen?“"),
    ("Bei Überforderung:",
     "„Ich merke, dass ich gerade unkonzentriert werde. Darf ich kurz für "
     "5 Minuten an die frische Luft, um danach wieder voll durchzustarten?“"),
    ("Bei Kritik/Fehlern:",
     "„Entschuldigung, das war ein Missverständnis. Wie kann ich das jetzt "
     "am besten korrigieren?“"),
]


def draw_card1(c, x, y, w, h):
    dashed_cut_rect(c, x, y, w, h, radius=4)
    pad = 0.28 * cm
    ix, iw = x + pad, w - 2 * pad
    top = y + h - pad
    c.setFillColor(ACCENT_KUPFER)
    c.setFont(SANS_BOLD, 7.2)
    for line in wrap_text("KLARTEXT IM PRAKTIKUM — ERSTE HILFE BEI STRESS", SANS_BOLD, 7.2, iw):
        c.drawString(ix, top, line)
        top -= 0.28 * cm
    top -= 0.06 * cm
    for label, sentence in CARD1_LINES:
        c.setFillColor(PETROL)
        c.setFont(SANS_BOLD, 5.8)
        c.drawString(ix, top, label)
        top -= 0.23 * cm
        c.setFillColor(GREY_TEXT)
        c.setFont(SANS_IT, 5.7)
        for line in wrap_text(sentence, SANS_IT, 5.7, iw):
            c.drawString(ix, top, line)
            top -= 0.22 * cm
        top -= 0.08 * cm


def draw_card2(c, x, y, w, h):
    dashed_cut_rect(c, x, y, w, h, radius=4)
    pad = 0.28 * cm
    ix, iw = x + pad, w - 2 * pad
    top = y + h - pad
    c.setFillColor(ACCENT_KUPFER)
    c.setFont(SANS_BOLD, 7.2)
    for line in wrap_text("KLARTEXT IM PRAKTIKUM — MEIN SICHERHEITSNETZ", SANS_BOLD, 7.2, iw):
        c.drawString(ix, top, line)
        top -= 0.28 * cm
    top -= 0.05 * cm
    c.setFillColor(DARK)
    c.setFont(SANS_BOLD, 6.4)
    for line in wrap_text("„Du bist nicht allein. Jedes Problem lässt sich klären.“", SANS_BOLD, 6.4, iw):
        c.drawCentredString(ix + iw / 2, top, line)
        top -= 0.26 * cm
    top -= 0.14 * cm
    fields = ["Ansprechperson Betrieb:", "Meine INGRA / Begleitung:", "Notfallkontakt (Schule/Eltern):"]
    for field in fields:
        c.setFillColor(GREY_TEXT)
        c.setFont(SANS, 5.6)
        c.drawString(ix, top, field)
        top -= 0.2 * cm
        c.setStrokeColor(GREY_LIGHT)
        c.setLineWidth(0.5)
        c.line(ix, top, ix + iw, top)
        top -= 0.22 * cm


# ------------------------------------------------------------------
# HAUPTSEITE
# ------------------------------------------------------------------

def build_pdf(out_path):
    c = pdfcanvas.Canvas(out_path, pagesize=A4)
    draw_page_frame(c, page_num=1)

    content_x = MARGIN + 0.6 * cm
    content_w = PAGE_W - 2 * (MARGIN + 0.6 * cm)
    top = PAGE_H - MARGIN

    band_y = draw_kopfband(
        c, content_x, top, content_w, ACCENT_KUPFER,
        "Praktikums-Notfall-Kärtchen & Kühlschrank-Superpower",
    )

    subtitle_y = band_y - 0.55 * cm
    c.setFillColor(GREY_TEXT)
    c.setFont(SANS_IT, 9.5)
    c.drawCentredString(
        PAGE_W / 2, subtitle_y,
        "Dein Mitmach-Tool fürs Praktikum – ausschneiden, aufhängen, mitnehmen",
    )

    # Obere Hälfte: Superpower-Card (A5 quer)
    upper_top = subtitle_y - 0.5 * cm
    upper_h = 10.4 * cm
    superpower_x = content_x
    superpower_w = content_w
    draw_superpower_card(c, superpower_x, upper_top, superpower_w, upper_h)

    # Mitte: kurze "So geht's"-Zeile
    mid_y = upper_top - upper_h - 0.9 * cm
    c.setFillColor(ACCENT_KUPFER)
    c.setFont(SANS_BOLD, 10.5)
    c.drawCentredString(PAGE_W / 2, mid_y, "SO GEHT'S")
    c.setFillColor(GREY_TEXT)
    c.setFont(SANS, 9)
    steps = "1. Superpower-Card ausfüllen & an den Kühlschrank hängen   ·   2. Notfallkarten ausschneiden & laminieren   ·   3. Immer griffbereit fürs Portemonnaie"
    c.drawCentredString(PAGE_W / 2, mid_y - 0.42 * cm, steps if stringWidth(steps, SANS, 9) < content_w else "")
    if stringWidth(steps, SANS, 9) >= content_w:
        for i, line in enumerate(wrap_text(steps, SANS, 9, content_w)):
            c.drawCentredString(PAGE_W / 2, mid_y - 0.42 * cm - i * 0.32 * cm, line)

    # Untere Hälfte: 2 Scheckkarten nebeneinander, zentriert
    card_w, card_h = 8.5 * cm, 5.5 * cm
    gap = 0.6 * cm
    cards_top_label_y = mid_y - 1.5 * cm
    scissors_label(c, PAGE_W / 2, cards_top_label_y, "hier ausschneiden & laminieren")

    cards_y = cards_top_label_y - 0.6 * cm - card_h
    total_w = 2 * card_w + gap
    start_x = (PAGE_W - total_w) / 2
    draw_card1(c, start_x, cards_y, card_w, card_h)
    draw_card2(c, start_x + card_w + gap, cards_y, card_w, card_h)

    # Fusshinweis unter den Karten
    note_y = cards_y - 0.9 * cm
    c.setFillColor(GREY_LIGHT)
    c.setFont(SANS_IT, 7.5)
    c.drawCentredString(
        PAGE_W / 2, note_y,
        "Tipp: einmal laminieren – dann hält die Karte das ganze Praktikum lang durch.",
    )

    closing_y = note_y - 0.9 * cm
    c.setStrokeColor(SAGE)
    c.setLineWidth(1)
    c.line(PAGE_W / 2 - 2.5 * cm, closing_y + 0.35 * cm, PAGE_W / 2 + 2.5 * cm, closing_y + 0.35 * cm)
    c.setFillColor(ACCENT_KUPFER)
    c.setFont(SANS_IT, 8.5)
    c.drawCentredString(
        PAGE_W / 2, closing_y,
        "Teil des KLARTEXT-Berufsvorbereitungs-Sets – gemeinsam mit dem Eltern-Set „Berufs-Dschungel“.",
    )

    c.showPage()
    c.save()
    print(f"erstellt: {out_path}")


def main():
    out_dir = os.path.dirname(os.path.abspath(__file__))
    build_pdf(os.path.join(out_dir, "KLARTEXT_Praktikums_Notfallkaertchen.pdf"))


if __name__ == "__main__":
    main()
