#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Haengt Zusatzblock-Karten an ein bereits mit pwa_export_deck.py exportiertes Deck an.
Fuer Module wie build_all_cards_el_zusatz.py / build_all_cards_lk_zusatz.py, die NICHT das
CARDS-Dict-Format nutzen, sondern BLOECKE = {code: (badge, footer_deck, {nr: (titel,
anleitung, [frage1, frage2], tipp)})} + optional SYSTEMFRAGEN = {code: {nr: (label, text)}}.
Liest nur die bereits vorhandenen Texte, erzeugt kein neues Textmaterial. Nummeriert die
Zusatzkarten fortlaufend nach der hoechsten bereits vorhandenen Kartennummer im Ziel-Deck.

Aufruf:
  python3 pwa_export_zusatz.py build_all_cards_el_zusatz el
  python3 pwa_export_zusatz.py build_all_cards_lk_zusatz lk
"""
import sys, os, json, importlib

REPO = "/sessions/kind-beautiful-ptolemy/mnt/klartext-app"
sys.path.insert(0, REPO)
from pwa_export_deck import compress_image, PWA_OUT


def run(modulname, deck_id):
    mod = importlib.import_module(modulname)
    BLOECKE = mod.BLOECKE
    SYSTEMFRAGEN = getattr(mod, "SYSTEMFRAGEN", {})
    find_image = mod.find_image

    deck_path = os.path.join(PWA_OUT, "data", f"{deck_id}.json")
    with open(deck_path, encoding="utf-8") as f:
        deck = json.load(f)
    next_nr = max(k["nr"] for k in deck["karten"]) + 1

    img_out_dir = os.path.join(PWA_OUT, "images", deck_id)
    os.makedirs(img_out_dir, exist_ok=True)

    fehlend = []
    hinzugefuegt = 0
    for code, (badge, footer_deck, cards) in BLOECKE.items():
        for local_nr, (titel, anleitung, fragen, tipp) in cards.items():
            img_path = find_image(code, local_nr)
            img_name = f"{deck_id.upper()}-Z-{next_nr:02d}.jpg"
            if img_path and os.path.exists(img_path):
                compress_image(img_path, os.path.join(img_out_dir, img_name))
            else:
                fehlend.append((code, local_nr))
                img_name = None

            sf = SYSTEMFRAGEN.get(code, {}).get(local_nr)
            if isinstance(sf, tuple):
                systemfrage_label, systemfrage = sf
            else:
                systemfrage_label, systemfrage = None, sf

            eintrag = {
                "nr": next_nr, "titel": titel, "anleitung": anleitung, "fragen": fragen,
                "hinweis": tipp, "bild": f"images/{deck_id}/{img_name}" if img_name else None,
                "badge": badge,
            }
            if systemfrage:
                eintrag["systemfrage"] = systemfrage
                eintrag["systemfrage_label"] = systemfrage_label or "SYSTEMISCH GEDACHT"
            deck["karten"].append(eintrag)
            next_nr += 1
            hinzugefuegt += 1

    with open(deck_path, "w", encoding="utf-8") as f:
        json.dump(deck, f, ensure_ascii=False, indent=2)

    reg_path = os.path.join(PWA_OUT, "data", "decks.json")
    with open(reg_path, encoding="utf-8") as f:
        registry = json.load(f)
    for d in registry:
        if d["id"] == deck_id:
            d["anzahl"] = len(deck["karten"])
    with open(reg_path, "w", encoding="utf-8") as f:
        json.dump(registry, f, ensure_ascii=False, indent=2)

    print(f"{deck_id}: {hinzugefuegt} Zusatzblock-Karten angehängt (jetzt {len(deck['karten'])} "
          f"gesamt), {len(fehlend)} ohne Bild: {fehlend}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    run(sys.argv[1], sys.argv[2])
