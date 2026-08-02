#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baut alle 25 DaZ-Sek-I-Deck-Karten (Vorder-/Rückseite PNG) aus DAZ-SEK1_Kartenkonzept_Entwurf.md.
Kein Fachprüfungs-Vorbehalt (Anjas eigene Qualifikation deckt das ab). Letztes Deck der Zehner-Serie."""
import os, glob, sys
sys.path.insert(0, os.path.dirname(__file__))
from build_card_dazsek1 import build_front, build_back

BILDER = "/sessions/kind-beautiful-ptolemy/mnt/klartext-app/bilder/dazsek1/"
OUT = "/sessions/kind-beautiful-ptolemy/mnt/outputs/dazsek1_karten_komplett/"
os.makedirs(OUT, exist_ok=True)

def find_image(nr):
    for pattern in (f"DAZ-SEK1-{nr:02d}.jpg", f"DAZ-SEK1-{nr:02d}.*.jpg", f"DAZ-SEK1-{nr:02d} *.jpg", f"DAZ-SEK1-{nr:02d}.jpeg", f"DAZ-SEK1-{nr:02d}.png"):
        files = sorted(glob.glob(os.path.join(BILDER, pattern)))
        if files:
            return files[0]
    return None

# nr: (titel, anleitung, [frage1, frage2], tipp_fuer_die_ingra)
CARDS = {
    1: ("Der erste Tag in der neuen Schule",
        "Für den Einstieg nach der Ankunft in einer neuen Sek-I-Schule.",
        ["Was war heute anders, als du dachtest?", "Was hat dir geholfen, dich ein bisschen sicherer zu fühlen?"],
        "Ein Überblick über das Schulsystem (Fächer, Noten, Ablauf) entlastet mehr, als man denkt – Sek I ist oft ein komplett anderes System als im Herkunftsland."),
    2: ("Das neue Schulsystem verstehen",
        "Für Verwirrung über ein unbekanntes Schulsystem (Fächerwahl, Notensystem, Struktur).",
        ["Was am Schulsystem hier verstehst du noch nicht ganz?", "Wen könntest du das fragen?"],
        "Nicht alles auf einmal erklären – konkrete offene Fragen sammeln und nacheinander klären."),
    3: ("Eine neue Stadt, ein neues Leben",
        "Für die ersten Eindrücke von einem neuen Ort im Jugendalter.",
        ["Was ist hier anders, als du es kanntest?", "Was hast du hier schon für dich entdeckt?"],
        "Jugendliche orientieren sich oft eigenständiger als jüngere Kinder – eigene Entdeckungen ernst nehmen."),
    4: ("Meine neue Klasse",
        "Für die ersten Kontakte in einer komplexeren, distanzierteren Klassengemeinschaft.",
        ["Wie ist die Stimmung in deiner neuen Klasse?", "Wo fühlst du dich schon ein bisschen zugehörig?"],
        "Sek-I-Klassen sind oft weniger offen als Grundschulklassen – realistische Erwartungen helfen."),
    5: ("Wenn ich mehr weiß, als ich zeigen kann",
        "Für die Erfahrung, durch die Sprachbarriere unterschätzt zu werden.",
        ["In welchem Fach kannst du mehr, als du auf Deutsch zeigen kannst?", "Was würde dir helfen, das zu zeigen?"],
        "Sprachbarriere ist kein Leistungsproblem – ggf. Nachteilsausgleich oder andere Ausdrucksformen prüfen."),
    6: ("Für meine Eltern übersetzen",
        "Für Jugendliche, die offizielle Dokumente oder Behördentermine für ihre Eltern übersetzen.",
        ["Musst du manchmal bei wichtigen Terminen übersetzen?", "Wie fühlt sich diese Verantwortung für dich an?"],
        "Diese Verantwortung ist größer als bei jüngeren Kindern (Behördensprache!) – explizit würdigen und bei Bedarf entlasten."),
    7: ("Wenn jemand über meinen Akzent urteilt",
        "Bei erlebtem Spott oder Vorurteil wegen Akzent, in diesem Alter oft subtiler und verletzender.",
        ["Was ist passiert?", "Was würdest du der Person gern sagen?"],
        "In diesem Alter wird Sprachspott oft mit Ausgrenzung verknüpft – ernst nehmen, nicht als „Kinderkram“ abtun."),
    8: ("Was ich auf Deutsch schon richtig gut kann",
        "Positiver Fortschritts-Impuls, altersgerecht konkret.",
        ["Worin bist du auf Deutsch inzwischen richtig gut?", "Wo hast du das zuletzt gemerkt?"],
        "Konkrete Fortschritte benennen wirkt bei Jugendlichen glaubwürdiger als allgemeines Lob."),
    9: ("Wer ich hier bin und wer ich zu Hause bin",
        "Für beginnende Identitätsfragen im Jugendalter, verstärkt durch Migration.",
        ["Fühlst du dich hier anders als zu Hause?", "Welche Seite von dir zeigst du wo?"],
        "Unterschiedliche Rollen in unterschiedlichen Kontexten sind normal – kein Widerspruch."),
    10: ("Erwartungen von zu Hause und von hier",
         "Für den Druck zwischen familiären Erwartungen und Erwartungen der neuen Umgebung.",
         ["Was erwarten deine Eltern von dir?", "Was erwartest du von dir selbst?"],
         "Beide Erwartungen dürfen benannt werden, auch wenn sie sich widersprechen – kein Entweder-oder erzwingen."),
    11: ("Wenn ich wegen meiner Herkunft anders behandelt werde",
         "Für Diskriminierungserfahrungen, direkter benannt als im GS-Deck.",
         ["Was ist passiert?", "Wer könnte dich dabei unterstützen?"],
         "Ernst nehmen, nicht relativieren. Bei wiederholten Vorfällen die Schule/Fachkraft aktiv einbeziehen."),
    12: ("Beides sein dürfen",
         "Positiver Reframing-Impuls zur doppelten kulturellen Zugehörigkeit.",
         ["Was magst du an beiden Kulturen, die zu dir gehören?", "Musst du dich für eine entscheiden?"],
         "Zwei Zugehörigkeiten gleichzeitig sind eine Stärke, kein Entweder-oder."),
    13: ("Meine Freundesgruppe hier",
         "Für die komplexere soziale Struktur im Jugendalter (Gruppen, Cliquen).",
         ["Wo findest du dich in den Gruppen hier wieder?", "Was würde dir helfen, mehr dazuzugehören?"],
         "Jugendliche Gruppenbildung ist komplex – Geduld einplanen, kein schneller Anschluss erwartbar."),
    14: ("Wenn Sprüche kommen",
         "Für abwertende Kommentare oder Mikroaggressionen im Schulalltag.",
         ["Welche Sprüche hörst du manchmal?", "Was hilft dir, damit umzugehen?"],
         "Konkrete Handlungsoptionen (Kontern, Ignorieren, Melden) gemeinsam durchgehen, statt nur „das ist nicht schlimm“ zu sagen."),
    15: ("Jemandem Neuem helfen",
         "Für ältere Schüler:innen, die anderen neu Ankommenden Orientierung geben können.",
         ["Was könntest du einem neuen Mitschüler/einer neuen Mitschülerin zeigen?", "Wie hättest du dir das am Anfang gewünscht?"],
         "Die eigene Erfahrung als Ressource nutzen – stärkt Selbstwirksamkeit besonders in diesem Alter."),
    16: ("Eine Freundschaft, die die Sprache überbrückt hat",
         "Positiver Rückblick auf eine gelungene Freundschaft trotz anfänglicher Sprachbarriere.",
         ["Wer hat dir geholfen, hier anzukommen?", "Was hat diese Freundschaft möglich gemacht?"],
         "Konkrete positive Erfahrungen stärken das Vertrauen in weitere Kontakte."),
    17: ("Was ich vermisse",
         "Vorsichtig, ohne zu drängen – Raum für Heimweh geben. Nicht nach Fluchtdetails fragen.",
         ["Was vermisst du manchmal?", "Was hilft dir, wenn du das Vermissen spürst?"],
         "Es geht um das Gefühl, nicht um die Details – bei belastenden Erinnerungen nicht nachbohren, ggf. Fachkraft einbeziehen."),
    18: ("In Kontakt bleiben",
         "Für vermisste Familie/Freunde an einem anderen Ort, altersgerecht eigenständiger als bei DaZ-GS.",
         ["Wie hältst du Kontakt zu Menschen, die dir wichtig sind?", "Reicht dir das, oder fehlt noch was?"],
         "Jugendliche pflegen oft eigenständig digitalen Kontakt – das als reale Ressource anerkennen, nicht kleinreden."),
    19: ("Zwei Orte, die zu mir gehören",
         "Reflektierter Zugang zu Herkunft und neuem Zuhause gleichzeitig.",
         ["Was verbindet dich noch mit deinem Herkunftsort?", "Was verbindet dich schon mit hier?"],
         "Beide Verbindungen dürfen nebeneinander bestehen."),
    20: ("Wenn das Vermissen groß wird",
         "Für Momente akuten Heimwehs, altersgerecht ernst genommen.",
         ["Was tust du, wenn das Vermissen besonders groß wird?", "Wer oder was hilft dir dann?"],
         "Trösten, nicht bagatellisieren – auch Jugendliche brauchen sichtbaren Raum für dieses Gefühl."),
    21: ("Was ich mir für die Zukunft vorstelle",
         "Für erste Zukunfts-/Berufsvorstellungen, ggf. durch Sprachbarriere erschwert.",
         ["Was möchtest du später mal machen?", "Was brauchst du dafür noch?"],
         "Sprachbarriere ist ein Hindernis, kein Grund, Ziele kleiner zu stecken."),
    22: ("Eine Ausbildung oder ein Weg, der zu mir passt",
         "Für die konkrete Ausbildungs-/Berufswahl-Phase, migrationsspezifische Hürden mitdenken.",
         ["Welcher Weg nach der Schule interessiert dich?", "Wer könnte dir bei der Orientierung helfen?"],
         "Anerkennung von Vorerfahrungen/Qualifikationen aus dem Herkunftsland aktiv mitdenken, nicht bei null anfangen lassen."),
    23: ("Was ich schon alles geschafft habe",
         "Ressourcenorientierter Rückblick auf den bisherigen Weg, altersgerecht mit größerer Perspektive.",
         ["Was hast du seit deiner Ankunft schon alles geschafft?", "Was hat dir dabei am meisten geholfen?"],
         "Den ganzen Weg würdigen, nicht nur die Schulleistung."),
    24: ("Worauf ich stolz bin",
         "Guter Abschluss-Impuls.",
         ["Worauf bist du stolz, wenn du an deinen Weg hier denkst?", "Was möchtest du dir selbst dafür sagen?"],
         "Guter Abschluss – bewusst als Rückblick lesen, nicht als Bewertung."),
    25: ("Von der DaZ-Klasse in die Regelklasse",
         "Für den zweiten großen Übergang nach der Ankunft: aus dem DaZ-Schutzraum ins reguläre Klassentempo.",
         ["Was macht dir am Wechsel in die Regelklasse am meisten Sorgen?", "Was von der DaZ-Zeit nimmst du mit?"],
         "Tempo und Erwartungen steigen spürbar – realistische Übergangszeit einplanen, nicht abrupt „schwimmen lassen“."),
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
        vorn = os.path.join(OUT, f"DAZ-SEK1-{nr:02d}_Vorderseite.png")
        hinten = os.path.join(OUT, f"DAZ-SEK1-{nr:02d}_Rueckseite.png")
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
