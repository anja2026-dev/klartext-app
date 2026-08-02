#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exportiert das Geschichtenkarten-Deck (30 Karten, 3 Sets a 10) fuer die PWA. Eigenes Skript statt
pwa_export_deck.py, weil CARDS hier eine Liste von Dicts ist (id_text/set/titel/situation/
fragen/impuls), nicht das nr-indizierte Tupel-Dict der anderen Decks. Liest nur vorhandene Texte.
"""
import sys, os, json
sys.path.insert(0, "/sessions/kind-beautiful-ptolemy/mnt/klartext-app")
from pwa_export_deck import compress_image, PWA_OUT
import pwa_generate_deck_icon
import build_all_cards_geschichtenkarten as m

SET_BADGES = {
    "A": "SET A · BRAINY ERLEBT MOBBING",
    "B": "SET B · BRAINY HILFT ANDEREN",
    "C": "SET C · BRAINY LERNT STRATEGIEN",
}

DECK_ID = "geschichtenkarten"
FARBE, FARBE_HELL, FARBE_RAND = "#961E23", "#FCEAEA", "#E0B2B2"

img_out_dir = os.path.join(PWA_OUT, "images", DECK_ID)
os.makedirs(img_out_dir, exist_ok=True)

deck = {
    "id": DECK_ID, "titel": "Geschichtenkarten", "untertitel": "Brainy erlebt & lernt (3 Sets)",
    "farbe": FARBE, "farbe_hell": FARBE_HELL, "farbe_rand": FARBE_RAND,
    "karten": [],
}

fehlend = []
for nr, card in enumerate(m.CARDS, start=1):
    img_path = m.find_image(card["id_text"])
    img_name = f"GK-{card['id_text']}.jpg"
    if img_path and os.path.exists(img_path):
        compress_image(img_path, os.path.join(img_out_dir, img_name))
    else:
        fehlend.append(card["id_text"])
        img_name = None

    deck["karten"].append({
        "nr": nr, "titel": card["titel"], "anleitung": card["situation"],
        "fragen": card["fragen"], "hinweis": card.get("impuls"),
        "bild": f"images/{DECK_ID}/{img_name}" if img_name else None,
        "badge": SET_BADGES.get(card["set"], "GESCHICHTENKARTEN"),
    })

out_json = os.path.join(PWA_OUT, "data", f"{DECK_ID}.json")
with open(out_json, "w", encoding="utf-8") as f:
    json.dump(deck, f, ensure_ascii=False, indent=2)
print(f"{DECK_ID}: {len(deck['karten'])} Karten exportiert, {len(fehlend)} ohne Bild: {fehlend}")

registry_path = os.path.join(PWA_OUT, "data", "decks.json")
registry = json.load(open(registry_path)) if os.path.exists(registry_path) else []
registry = [d for d in registry if d["id"] != DECK_ID]
registry.append({"id": DECK_ID, "titel": deck["titel"], "untertitel": deck["untertitel"],
                  "farbe": FARBE, "anzahl": len(deck["karten"])})
with open(registry_path, "w", encoding="utf-8") as f:
    json.dump(registry, f, ensure_ascii=False, indent=2)
print("Registry aktualisiert:", registry_path)

pwa_generate_deck_icon.generate(DECK_ID, FARBE, FARBE_RAND, "GK")
