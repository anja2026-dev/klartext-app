#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baut alle KD-Karten (01-30) als Vorder-/Rückseite PNG. Neu aufgebaut 27.07.2026 mit den
aktualisierten, modernen Bildern (plain benannt KD-NN.jpg) für alle 30 Karten."""
import os, re, glob, sys
sys.path.insert(0, os.path.dirname(__file__))
from build_card_kd import build_front, build_back, CARD_W, CARD_H

BILDER = "/sessions/kind-beautiful-ptolemy/mnt/klartext-app/bilder/kd/"
OUT = "/sessions/kind-beautiful-ptolemy/mnt/outputs/kd_karten_komplett/"
os.makedirs(OUT, exist_ok=True)

def find_image(nr):
    for pattern in (f"KD-{nr:02d}.jpg", f"KD-{nr:02d} *.jpg", f"KD-{nr:02d}.jpeg", f"KD-{nr:02d}.png"):
        files = sorted(glob.glob(os.path.join(BILDER, pattern)))
        if files:
            return files[0]
    return None

# nr: (titel, anleitung, [frage1, frage2], hinweis)
CARDS = {
    1: ("Wie geht es mir heute?",
        "Guter Einstieg in ein Gespräch, auch als fester Ritual-Start nutzbar.",
        ["Welche Farbe passt gerade zu dir?", "Magst du erzählen, warum?"],
        "Am besten als festen, wiederkehrenden Einstieg nutzen (z. B. jede Woche), nicht nur wenn etwas Schwieriges ansteht – sonst verknüpft das Kind die Karte mit „jetzt kommt Ärger“."),
    2: ("Mein Bauchgefühl",
        "Für sehr junge Kinder, die „Gefühl“ noch schwer benennen können. Körperbezug nutzen.",
        ["Was spürst du gerade in deinem Bauch?", "Ist es ein gutes oder ein komisches Gefühl?"],
        "Wenn ein Kind auch körperlich nichts benennen kann: nicht nachbohren, stattdessen zu KD-05 wechseln."),
    3: ("Viele Gefühle auf einmal",
        "Wenn ein Kind widersprüchliche Gefühle gleichzeitig zeigt (z. B. aufgeregt und ängstlich).",
        ["Kannst du zwei Gefühle gleichzeitig haben?", "Welche zwei fühlst du gerade?"],
        "Beide Gefühle stehen lassen, das Kind muss sich nicht für eins entscheiden."),
    4: ("Gefühle haben keine Farbe, die falsch ist",
        "Entlastend einsetzen, wenn ein Kind sich für ein Gefühl schämt.",
        ["Gibt es ein Gefühl, das du dir nicht erlaubst?", "Was würde Brainy dazu sagen?"],
        "Gut geeignet, wenn Scham wegen eines Gefühls sichtbar wird (z. B. Wut auf ein Geschwisterkind). Gefühl und Verhalten bleiben getrennt: das Gefühl ist immer okay, nicht jedes Verhalten."),
    5: ("Wenn ich nicht weiß, was ich fühle",
        "Entlastung: Nicht-Wissen ist in Ordnung, kein Druck zur sofortigen Antwort.",
        ["Ist 'ich weiß es nicht' gerade okay für dich?", "Möchtest du später nochmal schauen?"],
        "„Ich weiß es nicht“ ist ein vollständiges, legitimes Ergebnis – kein Gespräch erzwingen."),
    6: ("Wenn ich wütend bin",
        "Einsetzen, wenn Kind sichtbar aufgebracht, aber ansprechbar ist. Ruhige Stimme, keine Bewertung.",
        ["Wo im Körper spürst du die Wut?", "Was hilft dir jetzt: reden, Pause oder bewegen?"],
        "Nur einsetzen, wenn das Kind schon ansprechbar ist. Mitten in der akuten Wutreaktion hilft die Karte nicht – dort das kLAR-Modell nutzen (siehe Anleitung)."),
    7: ("Wenn ich Angst habe",
        "Bei sichtbarer Ängstlichkeit vor einer konkreten Situation einsetzen.",
        ["Wovor hast du gerade Angst?", "Was würde dir jetzt helfen, dich sicherer zu fühlen?"],
        "Bei akuter Angst direkt vor einer konkreten Situation eher kurzfristig beruhigen als mit der Karte vertiefen."),
    8: ("Wenn ich traurig bin",
        "Raum für Traurigkeit geben, nicht schnell trösten wollen.",
        ["Möchtest du erzählen, was dich traurig macht?", "Was tut dir gut, wenn du traurig bist?"],
        "Raum geben, nicht schnell trösten oder ablenken wollen – Traurigkeit darf da sein."),
    9: ("Was mich beruhigt",
        "Gemeinsam eine persönliche Liste an Beruhigungsstrategien erarbeiten.",
        ["Was hilft dir, wenn du dich aufgeregt fühlst?", "Was davon können wir hier gerade machen?"],
        "Gut geeignet, um gemeinsam eine persönliche „Werkzeugkiste“ aufzubauen, die auch außerhalb des Karten-Gesprächs nutzbar ist."),
    10: ("Groß fühlen, obwohl ich klein bin",
         "Bei Ohnmachtsgefühlen in Konfliktsituationen (z. B. gegenüber älteren Kindern) einsetzen.",
         ["Wann fühlst du dich stark?", "Was könnte dir helfen, dich größer zu fühlen?"],
         "Besonders hilfreich nach Erfahrungen mit älteren oder stärkeren Kindern. Wie klein sich das Kind gefühlt hat, nicht kleinreden."),
    11: ("Streit mit einem Freund",
         "Nach einem frischen Konflikt einsetzen, wenn das Kind ansprechbar ist.",
         ["Was ist passiert?", "Was wünschst du dir jetzt?"],
         "Erst einsetzen, wenn sich die akute Situation schon beruhigt hat."),
    12: ("Sorry sagen",
         "Entschuldigung als aktive Fähigkeit üben, nicht erzwingen.",
         ["Was möchtest du sagen?", "Wie könntest du es sagen?"],
         "Nicht zur Entschuldigung drängen – die Karte öffnet den Raum, erzwingt aber nichts."),
    13: ("Wenn ich nicht schuld bin",
         "Wichtig, um Kinder zu bestärken, sich nicht automatisch schuldig zu fühlen.",
         ["Was war deine Rolle im Streit — und was war die des anderen?", "Musst du dich entschuldigen, wenn du nichts falsch gemacht hast?"],
         "Wichtig für Kinder, die schnell die volle Verantwortung übernehmen wollen. Bewusst bestärkend einsetzen, nicht relativierend."),
    14: ("Wieder gut werden",
         "Fokus auf konkrete, kindgerechte Wiedergutmachung (nicht nur Worte).",
         ["Was könntest du tun, damit es wieder gut wird?", "Was würde dir helfen, wenn du der andere wärst?"],
         "Konkrete, machbare Handlung ist wichtiger als bloße Worte."),
    15: ("Wenn zwei Freunde streiten",
         "Für Situationen, in denen das begleitete Kind Zeuge eines fremden Streits ist.",
         ["Was machst du, wenn zwei andere streiten?", "Musst du dich einmischen?"],
         "Kind nicht zur Vermittlung drängen. Es geht um den eigenen Umgang mit der Situation, nicht um Konfliktlösung für andere."),
    16: ("Der erste Tag",
         "Vor neuen Situationen (neue Klasse, neue Gruppe) einsetzen.",
         ["Was macht dir am meisten Sorge?", "Was würde dir helfen, dich sicherer zu fühlen?"],
         "Vorbereitend vor der neuen Situation einsetzen, nicht erst wenn die Angst schon akut ist."),
    17: ("Etwas Neues ausprobieren",
         "Bei Zurückhaltung vor neuen Aktivitäten.",
         ["Was würdest du gern ausprobieren?", "Was ist der kleinste erste Schritt?"],
         "Kleine, machbare erste Schritte betonen statt große Veränderung auf einmal."),
    18: ("Wenn ich mich nicht traue",
         "Entlastend einsetzen, Mut nicht einfordern, sondern begleiten.",
         ["Was macht es gerade schwer?", "Was würde es ein bisschen leichter machen?"],
         "Mut nicht einfordern – Tempo des Kindes akzeptieren."),
    19: ("Mutig sein, auch mit Angst",
         "Vermitteln: Mut heißt nicht keine Angst haben, sondern trotzdem handeln.",
         ["Wann warst du mutig, obwohl du Angst hattest?", "Wie hat sich das angefühlt?"],
         "Vermitteln: Angst und Mut dürfen gleichzeitig da sein."),
    20: ("Hilfe holen ist okay",
         "Hilfeholen als Stärke framen, nicht als Versagen.",
         ["Wer könnte dir gerade helfen?", "Was würdest du sagen, wenn du um Hilfe bittest?"],
         "Immer als Stärke rahmen, nie als letzten Ausweg."),
    21: ("Was ist ein guter Freund?",
         "Gemeinsam Eigenschaften von Freundschaft sammeln, konkret statt abstrakt.",
         ["Was macht jemanden zu einem guten Freund?", "Bist du das auch für andere?"],
         "Konkrete Beispiele aus dem Kinderalltag sammeln, nicht abstrakt bleiben."),
    22: ("Wenn ich nicht mitspielen darf",
         "Bei Ausschluss-Erfahrungen einsetzen, ohne die anderen Kinder vorschnell zu verurteilen.",
         ["Was ist passiert?", "Was würdest du dir wünschen, was stattdessen passiert wäre?"],
         "Andere Kinder nicht vorschnell verurteilen. Das Erleben des begleiteten Kindes ernst nehmen."),
    23: ("Alleine in der Pause",
         "Bei wiederkehrender Einsamkeit in der Pause einsetzen.",
         ["Wie fühlt sich das Alleinsein für dich an?", "Was könnte dir helfen, jemanden zu finden?"],
         "Bei wiederkehrendem Muster zusätzlich Rücksprache mit der Schule halten – die Karte allein löst kein strukturelles Problem."),
    24: ("Neue Freunde finden",
         "Konkrete, machbare erste Schritte erarbeiten, nicht nur ermutigen.",
         ["Wie könntest du auf jemanden zugehen?", "Was könntest du fragen oder sagen?"],
         "Konkrete, kleine erste Schritte erarbeiten statt allgemein zu ermutigen."),
    25: ("Wenn jemand gemein zu mir ist",
         "Wichtig: nicht bagatellisieren, ernst nehmen, klären ob es Einzelfall oder wiederkehrend ist.",
         ["Was genau ist passiert?", "Ist das schon öfter passiert?"],
         "Ernst nehmen, klären ob Einzelfall oder wiederkehrend. Bei Hinweis auf Mobbing: Schule/Fachkraft einbeziehen, die Karte ersetzt das nicht."),
    26: ("Mein Bauch spürt mit",
         "Körperwahrnehmung als Frühwarnsystem einführen.",
         ["Merkst du manchmal im Bauch, wenn etwas nicht stimmt?", "Wie fühlt sich das an?"],
         "Körperwahrnehmung altersgerecht als Frühwarnsystem einführen, keine Diagnostik."),
    27: ("Wenn mein Körper „Stopp“ sagt",
         "Körperliche Grenzsignale (Müdigkeit, Überforderung) ernst nehmen lernen.",
         ["Woran merkst du, dass es genug ist?", "Was machst du, wenn dein Körper Stopp sagt?"],
         "Grenzsignale ernst nehmen, nicht als Trotz oder Unwilligkeit werten."),
    28: ("Was mir gut tut",
         "Positive Ressourcen sammeln, für ruhige Momente außerhalb akuter Belastung.",
         ["Was tut deinem Körper richtig gut?", "Wie oft machst du das?"],
         "Für ruhige Momente gedacht, nicht in akuter Belastung."),
    29: ("Mein Körper gehört mir",
         "Grundlegende Selbstbestimmung über den eigenen Körper vermitteln, altersgerecht.",
         ["Wer darf entscheiden, was mit deinem Körper passiert?", "Was, wenn dir etwas nicht gefällt?"],
         "Sensibles Thema, altersgerecht ohne Verunsicherung behandeln. Bei Hinweisen auf eine Grenzverletzung sofort die trägerinternen Kinderschutz-Vorgaben greifen lassen – die Karte ersetzt kein Schutzverfahren."),
    30: ("Zur Ruhe kommen",
         "Guter Abschluss-Impuls fürs Deck — eine Ruhe-/Entspannungsübung anbieten.",
         ["Was hilft dir, ruhig zu werden?", "Möchten wir das jetzt gemeinsam ausprobieren?"],
         "Guter Abschluss-Impuls, auch als letzte Karte einer Einheit gut einsetzbar."),
    31: ("Wenn sich zu Hause etwas ändert",
         "Sehr behutsam einsetzen, bei Trennung oder neuer Familiensituation. Kein Drängen, Tempo des Kindes respektieren.",
         ["Was ist bei dir zu Hause gerade anders?", "Was ist gleich geblieben, auch wenn sich viel verändert?"],
         "Besonders vorsichtig, Tempo des Kindes überlassen. Bei akuter Belastung eher nicht vertiefen."),
    32: ("Zwischen zwei Zuhause",
         "Für Kinder im Wechselmodell. Beide Zuhause wertfrei nebeneinander stehen lassen, keins besser oder schlechter dastehen lassen.",
         ["Was magst du an jedem deiner beiden Zuhause?", "Was nimmst du dir von einem zum anderen mit?"],
         "Beide Zuhause wertfrei nebeneinander stehen lassen."),
    33: ("Neue Menschen in der Familie",
         "Bei Patchwork/neuen Bezugspersonen der Eltern. Zeit als legitimen Faktor zulassen, Akzeptanz nicht erzwingen.",
         ["Was ist an der neuen Situation für dich noch ungewohnt?", "Was würde dir helfen, dich wohler zu fühlen?"],
         "Zeit als legitimen Faktor anerkennen, Akzeptanz darf sich nicht erzwingen lassen."),
    34: ("Die große Schule kommt",
         "Vor dem Übergang zur weiterführenden Schule. Vorfreude und Sorge dürfen gleichzeitig da sein.",
         ["Worauf freust du dich an der neuen Schule?", "Was macht dir dabei auch ein bisschen Sorge?"],
         "Gut einige Wochen vor dem eigentlichen Wechsel einsetzbar, nicht erst am letzten Schultag."),
    35: ("Wenn im Internet etwas gruselig war",
         "Nach belastenden Online-Erlebnissen (Bilder/Videos). Nicht bewerten, nur auffangen.",
         ["Was hast du gesehen, das dich erschreckt hat?", "Wer ist da, mit dem du darüber reden kannst?"],
         "Zeitnah nach dem Erlebnis einsetzen, wenn möglich. Bei wiederholten belastenden Erlebnissen: Eltern informieren, Mediennutzung gemeinsam anschauen."),
}

def run(nur=None, ueberspringen=()):
    ok, fehler, uebersprungen = [], [], []
    numbers = nur if nur else sorted(CARDS)
    for nr in numbers:
        if nr in ueberspringen:
            uebersprungen.append(nr)
            continue
        titel, anleitung, fragen, hinweis = CARDS[nr]
        image_path = find_image(nr)
        if not image_path:
            fehler.append((nr, "Bild nicht gefunden"))
            continue
        card = {"nr": nr, "titel": titel, "anleitung": anleitung, "fragen": fragen, "hinweis": hinweis,
                "total": 35}
        vorn = os.path.join(OUT, f"KD-{nr:02d}_Vorderseite.png")
        hinten = os.path.join(OUT, f"KD-{nr:02d}_Rueckseite.png")
        try:
            build_front(card, image_path, vorn)
            build_back(card, hinten)
            ok.append(nr)
        except Exception as e:
            fehler.append((nr, str(e)))
    print(f"Fertig: {len(ok)} Karten gebaut.")
    if uebersprungen:
        print("Übersprungen (Bild wird noch korrigiert):", uebersprungen)
    if fehler:
        print("Fehler bei:", fehler)

if __name__ == "__main__":
    run()
