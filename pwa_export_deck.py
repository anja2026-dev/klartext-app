#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exportiert ein KLARTEXT-Kartendeck aus einer bestehenden build_all_cards_*.py-Datei als JSON +
komprimierte Web-Bilder für die PWA (pwa/data/<id>.json, pwa/images/<id>/...). Wiederverwendbar
für jedes Deck der Serie – liest nur die bereits vorhandenen CARDS-Dicts, erzeugt keine neuen
Texte. Deckt beide bestehenden Kartenformate ab:
  Pattern A (4-Tupel): (titel, anleitung, [frage1, frage2], hinweis)               – z.B. KD, JD, FS
  Pattern B (6-Tupel):  (titel, anleitung, [frage1, frage2], systemfrage, hinweis, quelle) – z.B. OGS
  Pattern C (4-Tupel) + separates SYSTEMFRAGEN-Dict {nr: (label, text)}            – z.B. EL, LK, TR

Aufruf:
  python3 pwa_export_deck.py <modul> <deck_id> <farbe_hex> <farbe_hell_hex> <farbe_rand_hex> \
      "<Titel>" "<Untertitel>" [bild_prefix]

Beispiel:
  python3 pwa_export_deck.py build_all_cards_el el "#BF5B3E" "#F5E5DE" "#E0BEA9" \
      "EL-Deck" "Reflexionskarten Eltern" EL
"""
import sys, os, json, importlib
from PIL import Image

REPO = "/sessions/kind-beautiful-ptolemy/mnt/klartext-app"
PWA_OUT = os.path.join(REPO, "pwa")
sys.path.insert(0, REPO)

import pwa_generate_deck_icon


def compress_image(src_path, dst_path, target_w=700, quality=76):
    im = Image.open(src_path).convert("RGB")
    w, h = im.size
    if w > target_w:
        im = im.resize((target_w, int(h * target_w / w)), Image.LANCZOS)
    im.save(dst_path, "JPEG", quality=quality, optimize=True)


def unpack(card_tuple):
    """Gibt (titel, anleitung, fragen, systemfrage_text_oder_None, hinweis, quelle_oder_None) zurück."""
    if len(card_tuple) == 4:
        titel, anleitung, fragen, hinweis = card_tuple
        return titel, anleitung, fragen, None, hinweis, None
    elif len(card_tuple) == 6:
        titel, anleitung, fragen, systemfrage, hinweis, quelle = card_tuple
        return titel, anleitung, fragen, systemfrage, hinweis, quelle
    else:
        raise ValueError(f"Unbekanntes Kartenformat mit {len(card_tuple)} Feldern: {card_tuple[:1]}")


def run(modulname, deck_id, farbe, farbe_hell, farbe_rand, titel, untertitel, prefix=None):
    mod = importlib.import_module(modulname)
    CARDS = mod.CARDS
    find_image = getattr(mod, "find_image", None)
    SYSTEMFRAGEN = getattr(mod, "SYSTEMFRAGEN", {})
    prefix = prefix or deck_id.upper()

    img_out_dir = os.path.join(PWA_OUT, "images", deck_id)
    os.makedirs(img_out_dir, exist_ok=True)

    deck = {
        "id": deck_id, "titel": titel, "untertitel": untertitel,
        "farbe": farbe, "farbe_hell": farbe_hell, "farbe_rand": farbe_rand,
        "karten": [],
    }

    fehlend = []
    for nr in sorted(CARDS):
        t, anleitung, fragen, systemfrage, hinweis, quelle = unpack(CARDS[nr])
        systemfrage_label = None
        if not systemfrage and nr in SYSTEMFRAGEN:
            sf = SYSTEMFRAGEN[nr]
            if isinstance(sf, tuple):
                systemfrage_label, systemfrage = sf
            else:
                systemfrage = sf

        img_path = find_image(nr) if find_image else None
        img_name = f"{prefix}-{nr:02d}.jpg"
        if img_path and os.path.exists(img_path):
            compress_image(img_path, os.path.join(img_out_dir, img_name))
        else:
            fehlend.append(nr)
            img_name = None

        eintrag = {
            "nr": nr, "titel": t, "anleitung": anleitung, "fragen": fragen, "hinweis": hinweis,
            "bild": f"images/{deck_id}/{img_name}" if img_name else None,
        }
        if systemfrage:
            eintrag["systemfrage"] = systemfrage
            eintrag["systemfrage_label"] = systemfrage_label or "SYSTEMISCH GEDACHT"
        deck["karten"].append(eintrag)

    out_json = os.path.join(PWA_OUT, "data", f"{deck_id}.json")
    os.makedirs(os.path.dirname(out_json), exist_ok=True)
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(deck, f, ensure_ascii=False, indent=2)

    print(f"{deck_id}: {len(deck['karten'])} Karten exportiert, {len(fehlend)} ohne Bild: {fehlend}")
    print("->", out_json)

    # Registry (data/decks.json) aktualisieren/ergänzen
    registry_path = os.path.join(PWA_OUT, "data", "decks.json")
    registry = json.load(open(registry_path)) if os.path.exists(registry_path) else []
    registry = [d for d in registry if d["id"] != deck_id]
    registry.append({"id": deck_id, "titel": titel, "untertitel": untertitel, "farbe": farbe,
                      "anzahl": len(deck["karten"])})
    with open(registry_path, "w", encoding="utf-8") as f:
        json.dump(registry, f, ensure_ascii=False, indent=2)
    print("Registry aktualisiert:", registry_path)

    # Eigenes Home-Bildschirm-Icon für dieses Deck (für "Zum Home-Bildschirm hinzufügen" pro Deck)
    code = prefix if len(prefix) <= 3 else prefix[:2]
    pwa_generate_deck_icon.generate(deck_id, farbe, farbe_rand, code)


if __name__ == "__main__":
    if len(sys.argv) < 8:
        print(__doc__)
        sys.exit(1)
    run(*sys.argv[1:8], prefix=(sys.argv[8] if len(sys.argv) > 8 else None))
