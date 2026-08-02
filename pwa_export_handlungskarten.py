#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exportiert die vier Handlungskarten-Decks (TK, Krisendeck, Werkzeugkarten, mb) fuer die PWA.
Eigenes Skript statt pwa_export_deck.py, weil diese Decks eine andere Kartenstruktur haben
(Schritte + Tun/Nicht-tun-Tabelle statt Impulsfragen) - siehe neuer Kartentyp "Handlungskarte"
in app.js/index.html/style.css. Icon-Namen werden von den internen Kurzcodes der Quelldateien
(z.B. "blitz", "puls") auf echte Font-Awesome-6-Klassennamen gemappt, weil die PWA FA6 per
CDN laedt statt der lokalen TTF-Codepoints, die die PDF-Pipeline benutzt.

Nur deterministische Datenumformung, kein LLM-Aufruf noetig - liest CARDS direkt aus den
bestehenden build_all_cards_*.py-Modulen.
"""
import sys, os, json
sys.path.insert(0, "/sessions/kind-beautiful-ptolemy/mnt/klartext-app")
from pwa_export_deck import compress_image, PWA_OUT
import pwa_generate_deck_icon


def export_registry(deck_id, titel, untertitel, farbe, anzahl):
    registry_path = os.path.join(PWA_OUT, "data", "decks.json")
    registry = json.load(open(registry_path)) if os.path.exists(registry_path) else []
    registry = [d for d in registry if d["id"] != deck_id]
    registry.append({"id": deck_id, "titel": titel, "untertitel": untertitel,
                      "farbe": farbe, "anzahl": anzahl})
    with open(registry_path, "w", encoding="utf-8") as f:
        json.dump(registry, f, ensure_ascii=False, indent=2)


def write_deck(deck):
    out_json = os.path.join(PWA_OUT, "data", f"{deck['id']}.json")
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(deck, f, ensure_ascii=False, indent=2)


def abgrenzung_dict(paare):
    """Wandelt die Liste von (tun, nicht_tun)-Tupeln der Quelldateien in das von der PWA
    erwartete {tun: [...], nicht_tun: [...]}-Format um."""
    if not paare:
        return None
    return {"tun": [p[0] for p in paare], "nicht_tun": [p[1] for p in paare]}


# ---------------------------------------------------------------- TK-Deck (Fotos, 19 Karten)
def export_tk():
    import build_all_cards_tk as m
    DECK_ID = "tk"
    FARBE, FARBE_HELL, FARBE_RAND = "#4A148C", "#F3E5FF", "#CEA9E2"
    img_out_dir = os.path.join(PWA_OUT, "images", DECK_ID)
    os.makedirs(img_out_dir, exist_ok=True)

    deck = {"id": DECK_ID, "titel": "TK-Deck", "untertitel": "Handlungskarten für die Teamkoordination",
            "farbe": FARBE, "farbe_hell": FARBE_HELL, "farbe_rand": FARBE_RAND, "karten": []}

    fehlend = []
    for card in m.CARDS:
        img_path = m.find_image(card["nr"])
        img_name = f"{card['id_text']}.jpg"
        if img_path and os.path.exists(img_path):
            compress_image(img_path, os.path.join(img_out_dir, img_name))
        else:
            fehlend.append(card["id_text"])
            img_name = None

        deck["karten"].append({
            "nr": card["nr"], "titel": card["titel"],
            "situation": card["situation"], "schritte": card["schritte"],
            "abgrenzung": abgrenzung_dict(card.get("abgrenzung")),
            "quelle": card.get("quelle"),
            "bild": f"images/{DECK_ID}/{img_name}" if img_name else None,
        })

    write_deck(deck)
    export_registry(DECK_ID, deck["titel"], deck["untertitel"], FARBE, len(deck["karten"]))
    pwa_generate_deck_icon.generate(DECK_ID, FARBE, FARBE_RAND, "TK")
    print(f"{DECK_ID}: {len(deck['karten'])} Karten exportiert, {len(fehlend)} ohne Bild: {fehlend}")


# ------------------------------------------------------- Krisendeck (Icons, 8 Karten, akut)
KRISEN_ICON_MAP = {
    "blitz": "bolt", "mute": "volume-off", "puls": "heart-pulse",
    "warndreieck": "triangle-exclamation", "pflaster": "suitcase-medical",
    "laufen": "person-running", "nebel": "cloud", "vulkan": "fire",
}

def export_krisendeck():
    import build_all_cards_krisendeck as m
    DECK_ID = "krisendeck"
    FARBE, FARBE_HELL, FARBE_RAND = "#C62828", "#FDEAEA", "#F4A0A0"

    deck = {"id": DECK_ID, "titel": "Krisendeck", "untertitel": "Akute Krisensituationen – Barometer Rot",
            "farbe": FARBE, "farbe_hell": FARBE_HELL, "farbe_rand": FARBE_RAND, "karten": []}

    for nr, card in enumerate(m.CARDS, start=1):
        signale = " · ".join(card.get("front_signale") or [])
        situation = card["situation"]
        if signale:
            situation = f"Erkennungssignale: {signale}. {situation}"

        deck["karten"].append({
            "nr": nr, "titel": card["titel"],
            "icon": KRISEN_ICON_MAP.get(card["icon"], "circle-exclamation"),
            "situation": situation, "schritte": card["schritte"],
            "abgrenzung": abgrenzung_dict(card.get("abgrenzung")),
            "verweis": card.get("verweis"),
            "badge": f"AKUT · {card['id_text']}",
        })

    write_deck(deck)
    export_registry(DECK_ID, deck["titel"], deck["untertitel"], FARBE, len(deck["karten"]))
    pwa_generate_deck_icon.generate(DECK_ID, FARBE, FARBE_RAND, "FK")
    print(f"{DECK_ID}: {len(deck['karten'])} Karten exportiert")


# -------------------------------------------------- Werkzeugkarten (Icons, 26 Karten, WZ)
WERKZEUG_ICON_MAP = {
    "sun": "sun", "ban": "ban", "bolt": "bolt", "snowflake": "snowflake",
    "exchange": "right-left", "users": "users", "tint": "droplet", "bell": "bell",
    "circle-notch": "circle-notch", "refresh": "arrows-rotate", "eye": "eye",
    "headphones": "headphones", "flag": "flag", "pause": "pause", "list-ol": "list-ol",
    "dot-circle": "circle-dot", "map": "map", "thumbs-up": "thumbs-up",
    "sitemap": "sitemap", "leaf": "leaf",
}

def export_werkzeug():
    import build_all_cards_werkzeug as m
    DECK_ID = "werkzeug"
    FARBE, FARBE_HELL, FARBE_RAND = "#B07D2A", "#FBF4E8", "#E0C88A"

    deck = {"id": DECK_ID, "titel": "Werkzeugkarten", "untertitel": "26 Mini-Interventionen für den Alltag",
            "farbe": FARBE, "farbe_hell": FARBE_HELL, "farbe_rand": FARBE_RAND, "karten": []}

    for nr, card in enumerate(m.CARDS, start=1):
        tipp = card.get("tipp") or ""
        werkzeuge = card.get("werkzeuge")
        if werkzeuge:
            tipp = f"{tipp} Passende Werkzeuge: {werkzeuge}." if tipp else f"Passende Werkzeuge: {werkzeuge}."

        deck["karten"].append({
            "nr": nr, "titel": card["titel"],
            "icon": WERKZEUG_ICON_MAP.get(card["icon"], "circle"),
            "situation": card["lead"],
            "intro_label": "SITUATION" if card.get("typ") == "situation" else "WAS IST DAS",
            "schritte": card["schritte"],
            "tipp": tipp or None,
            "badge": card["id_text"],
        })

    write_deck(deck)
    export_registry(DECK_ID, deck["titel"], deck["untertitel"], FARBE, len(deck["karten"]))
    pwa_generate_deck_icon.generate(DECK_ID, FARBE, FARBE_RAND, "WZ")
    print(f"{DECK_ID}: {len(deck['karten'])} Karten exportiert")


# --------------------------------------------------------- mb (Mobbing-Intervention, 15 Karten)
MB_ICON_MAP = {
    "warndreieck": "triangle-exclamation", "suche": "magnifying-glass", "mobil": "mobile-screen",
    "cyber": "laptop", "gruppe": "user-group", "wechsel": "arrows-rotate", "schule": "school",
    "dialog": "comments", "schutz": "shield-halved", "auge": "eye", "ablauf": "list-check",
    "handschlag": "handshake", "herz": "heart", "familie": "people-roof", "wachstum": "seedling",
}

def export_mb():
    import build_all_cards_mb as m
    DECK_ID = "mb"
    FARBE, FARBE_HELL, FARBE_RAND = "#D81B60", "#FDE8F1", "#F0B2CD"

    deck = {"id": DECK_ID, "titel": "Mobbing-Intervention", "untertitel": "Vom ersten Anzeichen bis zur Nachsorge",
            "farbe": FARBE, "farbe_hell": FARBE_HELL, "farbe_rand": FARBE_RAND, "karten": []}

    for nr, card in enumerate(m.CARDS, start=1):
        deck["karten"].append({
            "nr": nr, "titel": card["titel"],
            "icon": MB_ICON_MAP.get(card["icon"], "circle"),
            "situation": card["lead"],
            "schritte": card["schritte"],
            "merksatz": card.get("merksatz"),
            "badge": f"{card['id_text']} · {card.get('fuer', '')}".strip(" ·"),
        })

    write_deck(deck)
    export_registry(DECK_ID, deck["titel"], deck["untertitel"], FARBE, len(deck["karten"]))
    pwa_generate_deck_icon.generate(DECK_ID, FARBE, FARBE_RAND, "MB")
    print(f"{DECK_ID}: {len(deck['karten'])} Karten exportiert")


# --------------------------------------------------------- hb (Hochbegabung, 12 Karten)
HB_ICON_MAP = {
    "idee": "lightbulb", "suche": "magnifying-glass", "asynchron": "shuffle",
    "abwaerts": "arrow-trend-down", "achtung": "circle-exclamation", "gruppe": "user-group",
    "doppel": "clone", "uhr": "clock", "rakete": "rocket", "liste": "list-check",
    "handschlag": "handshake", "dialog": "comments",
}

def export_hb():
    import build_all_cards_hb as m
    DECK_ID = "hb"
    FARBE, FARBE_HELL, FARBE_RAND = "#2024C4", "#E3E4FA", "#B2B5ED"

    deck = {"id": DECK_ID, "titel": "Hochbegabung", "untertitel": "Erkennen, Herausforderungen, Handeln",
            "farbe": FARBE, "farbe_hell": FARBE_HELL, "farbe_rand": FARBE_RAND, "karten": []}

    for nr, card in enumerate(m.CARDS, start=1):
        deck["karten"].append({
            "nr": nr, "titel": card["titel"],
            "icon": HB_ICON_MAP.get(card["icon"], "circle"),
            "situation": card["lead"],
            "schritte": card["schritte"],
            "merksatz": card.get("merksatz"),
            "badge": f"{card['id_text']} · {card.get('fuer', '')}".strip(" ·"),
        })

    write_deck(deck)
    export_registry(DECK_ID, deck["titel"], deck["untertitel"], FARBE, len(deck["karten"]))
    pwa_generate_deck_icon.generate(DECK_ID, FARBE, FARBE_RAND, "HB")
    print(f"{DECK_ID}: {len(deck['karten'])} Karten exportiert")


if __name__ == "__main__":
    export_tk()
    export_krisendeck()
    export_werkzeug()
    export_mb()
    export_hb()
