#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Erzeugt ein 192x192-Home-Bildschirm-Icon fuer ein einzelnes KLARTEXT-Deck: randloses,
voll deckendes Quadrat in der Deckfarbe mit Kurzcode (z.B. "KD") in der Mitte. Bewusst
KEINE eigene Abrundung und KEINE Transparenz am Rand - macOS/iOS legen sonst beim
"Zum Dock/Home-Bildschirm hinzufuegen" eine weisse Flaeche hinter transparente Bereiche,
was wie ein weisser Rahmen aussieht. Das Betriebssystem rundet die Ecken selbst ab.

Wird von pwa_export_deck.py automatisch mitaufgerufen. Einzelaufruf:
  python3 pwa_generate_deck_icon.py kd "#2E9E5A" "#C3E1CD" "KD"
"""
import sys
import os
from PIL import Image, ImageDraw, ImageFont

REPO = "/sessions/kind-beautiful-ptolemy/mnt/klartext-app"
ICONS_DIR = os.path.join(REPO, "pwa", "icons")

FONT_CANDIDATES = [
    "/usr/share/fonts/truetype/liberation2/LiberationSerif-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf",
]


def _font(size):
    for path in FONT_CANDIDATES:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def generate(deck_id, farbe_hex, rand_hex, code, size=192):
    os.makedirs(ICONS_DIR, exist_ok=True)
    # Voll deckendes, randloses Quadrat (kein Alpha-Kanal) - Betriebssystem maskiert/rundet selbst.
    img = Image.new("RGB", (size, size), farbe_hex)
    draw = ImageDraw.Draw(img)

    font_size = int(size * 0.40) if len(code) <= 2 else int(size * 0.30)
    font = _font(font_size)
    bbox = draw.textbbox((0, 0), code, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text(
        ((size - tw) / 2 - bbox[0], (size - th) / 2 - bbox[1]),
        code,
        fill="#FFFFFF",
        font=font,
    )

    out_path = os.path.join(ICONS_DIR, f"deck-{deck_id}.png")
    img.save(out_path)
    print(f"Icon gespeichert: {out_path}")
    return out_path


if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Aufruf: python3 pwa_generate_deck_icon.py <deck_id> <farbe_hex> <rand_hex> <code>")
        sys.exit(1)
    generate(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
