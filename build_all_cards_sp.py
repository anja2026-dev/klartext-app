#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baut alle 7 SP-Deck-Karten (Vorder-/Rückseite PNG)."""
import os, glob, sys
sys.path.insert(0, os.path.dirname(__file__))
from build_card_sp import build_front, build_back

BILDER = "/sessions/kind-beautiful-ptolemy/mnt/klartext-app/bilder/sp/"
OUT = "/sessions/kind-beautiful-ptolemy/mnt/outputs/sp_karten_komplett/"
os.makedirs(OUT, exist_ok=True)

def find_image(nr):
    for pattern in (f"SP-{nr:02d}.jpg", f"SP-{nr:02d} *.jpg", f"SP-{nr:02d}.jpeg", f"SP-{nr:02d}.png"):
        files = sorted(glob.glob(os.path.join(BILDER, pattern)))
        if files:
            return files[0]
    return None

# nr: (titel, anleitung, [frage1, frage2], hinweis)
CARDS = {
    1: ("Blitz-Check",
        "Als Springer-INGRA hast du oft nur Minuten, um dich in einer neuen Klasse zu orientieren, bevor du handeln musst.",
        ["Welche 3 Informationen brauche ich in den ersten 5 Minuten wirklich (Barometer-Stand des Kindes, akute Trigger, Ansprechperson vor Ort)?", "Wo bekomme ich diese Informationen am schnellsten her?"],
        "Ein kurzer, standardisierter Blitz-Check (3 Fragen an die Lehrkraft) ersetzt keinen langen Übergabebericht, verschafft aber sofort Handlungssicherheit."),
    2: ("Gast in der Klasse",
        "In einer fremden Klasse bist du zu Gast im System der Stammlehrkraft – deine Autorität ist geliehen, nicht gegeben.",
        ["Wie kläre ich mit der Lehrkraft vorab, welche Regeln in dieser Klasse gelten?", "Was mache ich, wenn meine übliche Vorgehensweise nicht zur Klassenregel passt?"],
        "Vorab-Abstimmung mit der Lehrkraft (\"Wie handhabt ihr das hier normalerweise?\") verhindert Reibung in der akuten Situation."),
    3: ("Die Chance des Neuanfangs",
        "Anders als die Stammkraft hast du keine Vorgeschichte mit dem Kind – das kann ein Vorteil sein, wenn eine Beziehung festgefahren ist.",
        ["Was weiß ich noch nicht über dieses Kind – und was könnte ich dadurch unvoreingenommener sehen?", "Wie nutze ich diesen \"unbelasteten Blick\" bewusst?"],
        "Ein Kind reagiert manchmal anders auf eine neue Bezugsperson, gerade weil keine alte Dynamik mitschwingt – das ist keine Konkurrenz zur Stammkraft, sondern eine Chance für alle."),
    4: ("Der Nachmittags-Crash",
        "Springer-Einsätze finden oft nachmittags statt, wenn die Energie- und Regulationsreserven des Kindes schon aufgebraucht sind.",
        ["Wie erkenne ich den Unterschied zwischen \"normaler Nachmittagsmüdigkeit\" und echter Überlastung?", "Welches Regulationstool passt in dieser Tageszeit am besten (kurz, wenig Aufwand)?"],
        "Nachmittags weniger erwarten, nicht mehr – die Reserven sind oft schon am Limit, bevor du überhaupt ankommst."),
    5: ("Die Brücke zur Stammkraft",
        "Deine Übergabe an die Stammkraft entscheidet, ob dein Einsatz nachwirkt oder verpufft.",
        ["Was muss die Stammkraft unbedingt wissen, um morgen dort weiterzumachen, wo ich aufgehört habe?", "In welcher Form (schriftlich, kurzes Gespräch) kommt diese Information am zuverlässigsten an?"],
        "Eine knappe, konkrete Übergabe (3 Sätze) wird eher gelesen als ein langer Bericht – Qualität vor Vollständigkeit."),
    6: ("Eltern-Erwartungen",
        "Eltern kennen dich als Springer-INGRA oft nicht – Vertrauen musst du dir in kürzerer Zeit erarbeiten als eine Stammkraft.",
        ["Wie stelle ich mich und meine Rolle in einem ersten Kontakt klar und knapp vor?", "Was kann ich realistisch versprechen – und was nicht?"],
        "Transparenz über die eigene, zeitlich begrenzte Rolle schafft mehr Vertrauen als der Versuch, wie eine Dauerlösung zu wirken."),
    7: ("Selbstschutz",
        "Ständig wechselnde Systeme, ständig neue Beziehungsarbeit – Springer-Einsätze sind kognitiv und emotional besonders fordernd.",
        ["Wie merke ich, wenn die vielen Wechsel an meine eigene Substanz gehen?", "Welches Ritual hilft mir, zwischen zwei Einsätzen \"umzuschalten\"?"],
        "Ein kurzes Übergangsritual zwischen zwei Einsätzen (auch nur 2 Minuten) schützt vor Vermischung der Systeme – im Kopf und im Körper."),
}

def run(nur=None, ueberspringen=()):
    ok, fehler, uebersprungen = [], [], []
    numbers = nur if nur else sorted(CARDS)
    for nr in numbers:
        if nr in ueberspringen:
            uebersprungen.append(nr)
            continue
        titel, anleitung, fragen, tipp = CARDS[nr]
        image_path = find_image(nr)
        if not image_path:
            fehler.append((nr, "Bild nicht gefunden"))
            continue
        card = {"nr": nr, "titel": titel, "anleitung": anleitung, "fragen": fragen, "hinweis": tipp, "total": len(CARDS)}
        vorn = os.path.join(OUT, f"SP-{nr:02d}_Vorderseite.png")
        hinten = os.path.join(OUT, f"SP-{nr:02d}_Rueckseite.png")
        try:
            build_front(card, image_path, vorn)
            build_back(card, hinten)
            ok.append(nr)
        except Exception as e:
            fehler.append((nr, str(e)))
    print(f"Fertig: {len(ok)} Karten gebaut.")
    if uebersprungen: print("Übersprungen:", uebersprungen)
    if fehler: print("Fehler:", fehler)

if __name__ == "__main__":
    run()