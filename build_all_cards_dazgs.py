#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baut alle 25 DaZ-GS-Deck-Karten (Vorder-/Rückseite PNG) aus DAZ-GS_Kartenkonzept_Entwurf.md.
Kein Fachprüfungs-Vorbehalt (Anjas eigene Qualifikation deckt das ab)."""
import os, glob, sys
sys.path.insert(0, os.path.dirname(__file__))
from build_card_dazgs import build_front, build_back

BILDER = "/sessions/kind-beautiful-ptolemy/mnt/klartext-app/bilder/dazgs/"
OUT = "/sessions/kind-beautiful-ptolemy/mnt/outputs/dazgs_karten_komplett/"
os.makedirs(OUT, exist_ok=True)

def find_image(nr):
    for pattern in (f"DAZ-GS-{nr:02d}.jpg", f"DAZ-GS-{nr:02d} *.jpg", f"DAZ-GS-{nr:02d}.jpeg", f"DAZ-GS-{nr:02d}.png"):
        files = sorted(glob.glob(os.path.join(BILDER, pattern)))
        if files:
            return files[0]
    return None

# nr: (titel, anleitung, [frage1, frage2], tipp_fuer_die_ingra)
CARDS = {
    1: ("Der erste Tag in der neuen Schule",
        "Für den Einstieg nach der Ankunft in einer neuen Schule.",
        ["Was war heute anders, als du dachtest?", "Was hat dir geholfen, dich ein bisschen sicherer zu fühlen?"],
        "Ein Rundgang oder eine feste Bezugsperson am ersten Tag hilft mehr als viele Erklärungen auf einmal."),
    2: ("Wenn ich am Anfang nichts verstehe",
        "Für Momente akuter Sprachüberforderung, entlastend statt fordernd.",
        ["Was hilft dir, wenn du etwas nicht verstehst?", "Traust du dich zu fragen, wenn etwas unklar ist?"],
        "Nicht verstehen ist am Anfang normal – nicht als fehlende Anstrengung werten."),
    3: ("Ein neuer Ort",
        "Für die ersten Eindrücke von einem neuen Ort.",
        ["Was ist hier anders, als du es kanntest?", "Gibt es etwas, das dir hier schon gefällt?"],
        "Beides darf gleichzeitig da sein – Fremdheit und erste positive Momente."),
    4: ("Meine Klasse kennenlernen",
        "Für die ersten Kontakte in der neuen Klasse.",
        ["Wer in der Klasse ist dir schon aufgefallen?", "Was würdest du gern über sie wissen?"],
        "Kleine, konkrete Beobachtungen sind ein besserer erster Schritt als die große Erwartung, sofort Freunde zu finden."),
    5: ("Wenn mir die Wörter fehlen",
        "Bei sichtbarer Frustration über fehlende Wörter.",
        ["Wann fehlen dir die Wörter am meisten?", "Was machst du, wenn dir ein Wort fehlt?"],
        "Zeigen, Zeichnen oder die Muttersprache nutzen sind gute Übergangslösungen, kein Umweg."),
    6: ("Zwei Sprachen im Kopf",
        "Für das Erleben, zwischen zwei Sprachen zu wechseln oder sie zu mischen.",
        ["Passiert es dir, dass sich zwei Sprachen in deinem Kopf mischen?", "Welche Sprache kommt dir in welchen Momenten zuerst?"],
        "Sprachen mischen ist ein normaler Teil des Zweisprachig-Werdens, kein Fehler."),
    7: ("Wenn jemand über meine Aussprache lacht",
        "Bei erlebtem Spott wegen Akzent oder Fehlern.",
        ["Was ist passiert?", "Was würdest du der Person gern sagen?"],
        "Ernst nehmen, nicht bagatellisieren – ein Fehler beim Deutschlernen ist kein Grund zum Auslachen."),
    8: ("Ein Wort, das ich neu gelernt habe",
        "Positiver Fortschritts-Impuls.",
        ["Welches neue Wort hast du zuletzt gelernt?", "Wo hast du es benutzt?"],
        "Fortschritt sichtbar machen – auch kleine Schritte zählen."),
    9: ("Zu Hause anders sprechen als in der Schule",
        "Für das Erleben von zwei Sprachwelten (Familie vs. Schule).",
        ["Welche Sprache sprichst du zu Hause?", "Ist das für dich zwei verschiedene Welten oder eine?"],
        "Beide Sprachen sind wertvoll – die Familiensprache ist kein Hindernis für Deutsch."),
    10: ("Für meine Eltern übersetzen",
         "Für Kinder, die als Sprachmittler für Eltern einspringen.",
         ["Musst du manchmal für deine Eltern übersetzen?", "Wie fühlt sich das für dich an?"],
         "Übersetzen kann stolz machen, aber auch belasten – beides ernst nehmen. Bei viel Verantwortung Rücksprache mit der Schule halten."),
    11: ("Was ich von zu Hause mitgebracht habe",
         "Für Traditionen, Gewohnheiten, Gegenstände von „zu Hause“.",
         ["Was von zu Hause ist dir hier besonders wichtig?", "Möchtest du davon erzählen?"],
         "Echtes Interesse an der Herkunft zeigen, ohne auszufragen."),
    12: ("Weder das eine noch das andere – oder beides?",
         "Für ältere Grundschulkinder, die anfangen, über Zugehörigkeit nachzudenken.",
         ["Fühlst du dich manchmal zwischen zwei Welten?", "Was magst du an beiden?"],
         "Zwei Zugehörigkeiten gleichzeitig sind kein Widerspruch."),
    13: ("Spielen ohne viele Worte",
         "Zeigt, dass Kontakt auch ohne perfekte Sprache möglich ist.",
         ["Welches Spiel geht auch ohne viele Worte?", "Mit wem hast du das schon ausprobiert?"],
         "Bewegungsspiele/Sport sind oft die ersten erfolgreichen Kontaktbrücken."),
    14: ("Mein erster Freund hier",
         "Positiver Rückblick auf eine erste gelungene Freundschaft.",
         ["Wer war der oder die Erste, mit dem/der du dich hier angefreundet hast?", "Was hat den Anfang leicht gemacht?"],
         "Die Geschichte des ersten Kontakts hilft, das eigene Können als Ressource zu sehen."),
    15: ("Wenn ich nicht mitreden kann",
         "Bei Ausschlusserleben wegen Sprache.",
         ["Wann fühlst du dich außen vor, weil du nicht alles verstehst?", "Was würde dir helfen, mehr dazuzugehören?"],
         "Ernst nehmen, ggf. mit der ganzen Klasse an Einbindung arbeiten – liegt nicht allein am Kind."),
    16: ("Jemandem Neuem helfen",
         "Für Kinder, die schon länger da sind und nun anderen neu Ankommenden helfen können.",
         ["Was könntest du einem neuen Kind zeigen?", "Wie hättest du dir das am Anfang gewünscht?"],
         "Die eigene Erfahrung als Stärke nutzen – stärkt Selbstwirksamkeit."),
    17: ("Was ich vermisse",
         "Vorsichtig, ohne zu drängen – Raum für Heimweh geben. Nicht nach Fluchtdetails fragen.",
         ["Was vermisst du manchmal?", "Was hilft dir, wenn du das Vermissen spürst?"],
         "Es geht um das Gefühl, nicht um die Details – bei belastenden Erinnerungen nicht nachbohren, ggf. Fachkraft einbeziehen."),
    18: ("Menschen, die ich vermisse",
         "Für vermisste Familie/Freunde an einem anderen Ort.",
         ["An wen denkst du oft?", "Gibt es eine Art, wie du in Kontakt bleibst?"],
         "Kontakt halten (Fotos, Anrufe) ist eine wertvolle Ressource, wenn möglich unterstützen."),
    19: ("Essen, das mich an zu Hause erinnert",
         "Niedrigschwelliger, positiver Zugang zum Thema Herkunft.",
         ["Welches Essen erinnert dich an zu Hause?", "Isst du das noch manchmal hier?"],
         "Ein einfacher, positiv besetzter Einstieg ins Thema Herkunft."),
    20: ("Wenn das Vermissen groß wird",
         "Für Momente akuten Heimwehs.",
         ["Was tust du, wenn das Vermissen besonders groß ist?", "Wer kann dich dann trösten?"],
         "Trösten, nicht ablenken wollen – das Gefühl darf da sein."),
    21: ("Das erste Mal Deutsch gesprochen",
         "Rückblick auf einen konkreten Sprach-Meilenstein.",
         ["Erinnerst du dich an das erste Mal, als du auf Deutsch etwas gesagt hast?", "Wie hat sich das angefühlt?"],
         "Diesen Moment bewusst würdigen, auch wenn er schon lange her ist."),
    22: ("Ein Wort in meiner Sprache",
         "Positiver Rollentausch – das Kind bringt anderen etwas bei.",
         ["Welches Wort in deiner Sprache möchtest du der Klasse beibringen?", "Was bedeutet es?"],
         "Macht die Herkunftssprache als Können sichtbar, nicht als Defizit."),
    23: ("Was ich schon alles kann",
         "Ressourcenorientierter Rückblick auf den bisherigen Weg.",
         ["Was kannst du heute, das du am Anfang noch nicht konntest?", "Was hat dir dabei am meisten geholfen?"],
         "Fortschritt konkret benennen – motiviert mehr als allgemeines Lob."),
    24: ("Worauf ich stolz bin",
         "Guter Abschluss-Impuls.",
         ["Worauf bist du stolz, wenn du an deinen Weg hier denkst?", "Was möchtest du dir selbst dafür sagen?"],
         "Guter Abschluss – bewusst als Rückblick lesen, nicht als Bewertung."),
    25: ("Von der Sprachförderung in die neue Klasse",
         "Für den Übergang aus der DaZ-/Vorbereitungsklasse in die Regelklasse, wenn die vertraute Kleingruppe und Unterstützung wegfällt.",
         ["Was wird in der neuen Klasse anders sein als in der DaZ-Gruppe?", "Was von der DaZ-Zeit hilft dir dabei weiter?"],
         "Der Wechsel bedeutet oft auch den Verlust der vertrauten Kleingruppe – das aktiv ansprechen, nicht nur als Fortschritt feiern."),
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
        card = {"nr": nr, "titel": titel, "anleitung": anleitung, "fragen": fragen, "hinweis": tipp,
                "total": len(CARDS)}
        vorn = os.path.join(OUT, f"DAZ-GS-{nr:02d}_Vorderseite.png")
        hinten = os.path.join(OUT, f"DAZ-GS-{nr:02d}_Rueckseite.png")
        try:
            build_front(card, image_path, vorn)
            build_back(card, hinten)
            ok.append(nr)
        except Exception as e:
            fehler.append((nr, str(e)))
    print(f"Fertig: {len(ok)} Karten gebaut.")
    if uebersprungen:
        print("Übersprungen:", uebersprungen)
    if fehler:
        print("Fehler bei (fehlende Bilder):", fehler)

if __name__ == "__main__":
    run()
