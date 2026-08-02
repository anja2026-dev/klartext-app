#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exportiert Insel-Set + Zonen-Set fuer die PWA (4 Decks: insel-schule, insel-eltern,
zonen-schule, zonen-eltern). Vierte Kartenstruktur neben Impulskarte/Handlungskarte-mit-Foto/
Handlungskarte-mit-Icon: die "Raum-/Regelkarte" (name/zweck/regeln/nutzen, keine nummerierten
Handlungsschritte im engeren Sinn, keine Tun/Nicht-tun-Tabelle). Statt eines fuenften HTML/CSS/
JS-Kartentyps wird das bestehende Handlungskarte-Geruest wiederverwendet:
  - zweck  -> cardIntro (introLabel dynamisch "ZWECK")
  - regeln -> cardSchritte-Liste (schritteLabel dynamisch "REGELN" statt "SCHRITTE")
  - nutzen -> Notiz-Box unten (notizLabel "NUTZEN")
Kein LLM-Aufruf noetig - liest SCHUL_CARDS/ELTERN_CARDS direkt aus den bestehenden
build_all_cards_insel.py / build_all_cards_zonen.py Modulen.
"""
import sys, os, json
sys.path.insert(0, "/sessions/kind-beautiful-ptolemy/mnt/klartext-app")
from pwa_export_deck import compress_image, PWA_OUT
import pwa_generate_deck_icon


def to_hex(rgb):
    return "#{:02X}{:02X}{:02X}".format(*rgb)


def blend(rgb1, rgb2, t=0.5):
    return tuple(int(a + (b - a) * t) for a, b in zip(rgb1, rgb2))


def export_registry(deck_id, titel, untertitel, farbe, anzahl):
    registry_path = os.path.join(PWA_OUT, "data", "decks.json")
    registry = json.load(open(registry_path)) if os.path.exists(registry_path) else []
    registry = [d for d in registry if d["id"] != deck_id]
    registry.append({"id": deck_id, "titel": titel, "untertitel": untertitel,
                      "farbe": farbe, "anzahl": anzahl})
    with open(registry_path, "w", encoding="utf-8") as f:
        json.dump(registry, f, ensure_ascii=False, indent=2)


def export_set(cards, bilder_dir, deck_id, titel, untertitel, farbe_rgb, farbe_hell_rgb, icon_code, badge_label):
    farbe = to_hex(farbe_rgb)
    farbe_hell = to_hex(farbe_hell_rgb)
    farbe_rand = to_hex(blend(farbe_rgb, farbe_hell_rgb, 0.45))

    img_out_dir = os.path.join(PWA_OUT, "images", deck_id)
    os.makedirs(img_out_dir, exist_ok=True)

    deck = {"id": deck_id, "titel": titel, "untertitel": untertitel,
            "farbe": farbe, "farbe_hell": farbe_hell, "farbe_rand": farbe_rand, "karten": []}

    fehlend = []
    for nr, name, badge_datei, (_karten_farbe, _karten_farbe_light), zweck, regeln, nutzen in cards:
        img_path = os.path.join(bilder_dir, badge_datei)
        img_name = badge_datei
        if os.path.exists(img_path):
            compress_image(img_path, os.path.join(img_out_dir, img_name))
        else:
            fehlend.append(name)
            img_name = None

        deck["karten"].append({
            "nr": nr, "titel": name,
            "situation": zweck, "intro_label": "ZWECK",
            "schritte": regeln, "schritte_label": "REGELN",
            "nutzen": " ".join(nutzen),
            "bild": f"images/{deck_id}/{img_name}" if img_name else None,
            "badge": badge_label,
        })

    out_json = os.path.join(PWA_OUT, "data", f"{deck_id}.json")
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(deck, f, ensure_ascii=False, indent=2)
    export_registry(deck_id, titel, untertitel, farbe, len(deck["karten"]))
    pwa_generate_deck_icon.generate(deck_id, farbe, farbe_rand, icon_code)
    print(f"{deck_id}: {len(deck['karten'])} Karten exportiert, {len(fehlend)} ohne Bild: {fehlend}")


def export_insel():
    import build_all_cards_insel as m
    BILDER = "/sessions/kind-beautiful-ptolemy/mnt/klartext-app/bilder/insel/"
    TUERKIS = ((38, 166, 154), (224, 242, 239))
    INDIGO = ((63, 81, 181), (227, 229, 246))
    export_set(m.SCHUL_CARDS, BILDER, "insel-schule", "Insel-Set · Schule",
               "Raumzonen für pädagogische Strukturierung",
               *TUERKIS, "IS", "INSEL-SET · SCHULE")
    export_set(m.ELTERN_CARDS, BILDER, "insel-eltern", "Insel-Set · Zuhause",
               "Raumzonen für Familien",
               *INDIGO, "IE", "INSEL-SET · ZUHAUSE")


def export_zonen():
    import build_all_cards_zonen as m
    BILDER = "/sessions/kind-beautiful-ptolemy/mnt/klartext-app/bilder/zonen/"
    GRAPHIT = ((55, 71, 79), (222, 227, 229))
    SCHIEFER = ((91, 122, 128), (224, 233, 234))
    export_set(m.SCHUL_CARDS, BILDER, "zonen-schule", "Zonen-Set · Schule",
               "Raumzonen für Jugendliche in der Schule",
               *GRAPHIT, "ZS", "ZONEN-SET · SCHULE")
    export_set(m.ELTERN_CARDS, BILDER, "zonen-eltern", "Zonen-Set · Zuhause",
               "Raumzonen für Jugendliche zuhause",
               *SCHIEFER, "ZE", "ZONEN-SET · ZUHAUSE")


if __name__ == "__main__":
    export_insel()
    export_zonen()
