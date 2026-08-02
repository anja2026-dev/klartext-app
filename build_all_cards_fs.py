#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baut alle 32 FS-Deck-Karten (Vorder-/Rückseite PNG) aus FS_Kartenkonzept_Entwurf.md.
Sprachlich vereinfachte KD-Adaption, kein Fachprüfungs-Vorbehalt (Anjas eigene Praxiserfahrung)."""
import os, glob, sys
sys.path.insert(0, os.path.dirname(__file__))
from build_card_fs import build_front, build_back

BILDER = "/sessions/kind-beautiful-ptolemy/mnt/klartext-app/bilder/fs/"
OUT = "/sessions/kind-beautiful-ptolemy/mnt/outputs/fs_karten_komplett/"
os.makedirs(OUT, exist_ok=True)

def find_image(nr):
    for pattern in (f"FS-{nr:02d}.jpg", f"FS-{nr:02d} *.jpg", f"FS-{nr:02d}.jpeg", f"FS-{nr:02d}.png"):
        files = sorted(glob.glob(os.path.join(BILDER, pattern)))
        if files:
            return files[0]
    return None

# nr: (titel, anleitung, [frage1, frage2], tipp_fuer_die_ingra)
CARDS = {
    1: ("Wie geht es mir heute?",
        "Ein guter Anfang für ein Gespräch. Die Karte kann man oft benutzen.",
        ["Welche Farbe passt zu dir?", "Willst du erzählen, warum?"],
        "Benutze die Karte oft. Nicht nur bei Problemen."),
    2: ("Mein Bauchgefühl",
        "Für kleine Kinder. Manche Kinder kennen die Wörter für Gefühle noch nicht. Der Bauch hilft.",
        ["Was spürst du gerade in deinem Bauch?", "Ist das Gefühl gut oder komisch?"],
        "Spürt das Kind nichts? Dann frag nicht weiter. Nimm stattdessen Karte FS-05."),
    3: ("Viele Gefühle auf einmal",
        "Für Momente mit zwei Gefühlen gleichzeitig. Zum Beispiel aufgeregt und ängstlich.",
        ["Kannst du zwei Gefühle gleichzeitig haben?", "Welche zwei Gefühle sind das gerade?"],
        "Beide Gefühle dürfen da sein. Das Kind muss sich nicht entscheiden."),
    4: ("Kein Gefühl ist falsch",
        "Für Momente, in denen sich ein Kind für ein Gefühl schämt.",
        ["Gibt es ein Gefühl, das du dir nicht erlaubst?", "Was sagt Brainy dazu?"],
        "Das Gefühl ist immer okay. Nicht jedes Verhalten ist okay. Trenne diese zwei Dinge."),
    5: ("Wenn ich nicht weiß, was ich fühle",
        "Nicht wissen ist okay. Kein Druck für eine schnelle Antwort.",
        ["Ist 'Ich weiß es nicht' gerade okay für dich?", "Willst du später noch mal schauen?"],
        "'Ich weiß es nicht' ist eine gute Antwort. Zwinge das Kind nicht zum Reden."),
    6: ("Wenn ich wütend bin",
        "Nutze die Karte, wenn das Kind wütend, aber ansprechbar ist. Bleib ruhig. Bewerte nicht.",
        ["Wo im Körper spürst du die Wut?", "Was hilft dir jetzt: Reden, Pause oder Bewegung?"],
        "Nutze die Karte nur, wenn das Kind schon ansprechbar ist. Mitten in der Wut hilft das kLAR-Modell besser."),
    7: ("Wenn ich Angst habe",
        "Nutze die Karte bei sichtbarer Angst vor einer Situation.",
        ["Wovor hast du gerade Angst?", "Was hilft dir jetzt, dich sicherer zu fühlen?"],
        "Bei akuter Angst erst beruhigen. Die Karte kommt danach."),
    8: ("Wenn ich traurig bin",
        "Gib Raum für Traurigkeit. Tröste nicht zu schnell.",
        ["Willst du erzählen, was dich traurig macht?", "Was tut dir gut, wenn du traurig bist?"],
        "Traurigkeit darf da sein. Nicht ablenken."),
    9: ("Was mich beruhigt",
        "Sammelt gemeinsam Ideen, die beruhigen.",
        ["Was hilft dir, wenn du aufgeregt bist?", "Was davon können wir jetzt machen?"],
        "Baut gemeinsam eine Liste. Die Liste hilft auch später."),
    10: ("Groß fühlen, obwohl ich klein bin",
         "Nutze die Karte bei Ohnmacht in einem Streit. Zum Beispiel mit älteren Kindern.",
         ["Wann fühlst du dich stark?", "Was hilft dir, dich größer zu fühlen?"],
         "Rede das Gefühl nicht klein."),
    11: ("Streit mit einem Freund",
         "Nutze die Karte nach einem frischen Streit. Erst wenn das Kind ansprechbar ist.",
         ["Was ist passiert?", "Was wünschst du dir jetzt?"],
         "Warte, bis sich die Situation beruhigt hat."),
    12: ("Sorry sagen",
         "Übe Entschuldigung als Fähigkeit. Zwinge nicht dazu.",
         ["Was willst du sagen?", "Wie willst du es sagen?"],
         "Dräng nicht zur Entschuldigung. Die Karte öffnet nur den Raum."),
    13: ("Wenn ich nicht schuld bin",
         "Stärke Kinder, die sich zu schnell schuldig fühlen.",
         ["Was war deine Rolle im Streit? Was war die Rolle vom anderen Kind?", "Musst du dich entschuldigen, wenn du nichts falsch gemacht hast?"],
         "Stärke das Kind. Rede die Sache nicht klein."),
    14: ("Wieder gut werden",
         "Es geht um eine konkrete Wiedergutmachung. Nicht nur um Worte.",
         ["Was kannst du tun, damit es wieder gut wird?", "Was braucht das andere Kind jetzt?"],
         "Eine kleine Handlung ist wichtiger als viele Worte."),
    15: ("Wenn zwei Freunde streiten",
         "Für Kinder, die einen fremden Streit miterleben.",
         ["Was machst du, wenn zwei andere streiten?", "Musst du dich einmischen?"],
         "Dräng das Kind nicht zum Vermitteln. Es geht um sein eigenes Erleben."),
    16: ("Der erste Tag",
         "Nutze die Karte vor einer neuen Situation. Zum Beispiel eine neue Klasse.",
         ["Was macht dir am meisten Sorgen?", "Was hilft dir, dich sicherer zu fühlen?"],
         "Nutze die Karte vorher. Nicht erst, wenn die Angst schon groß ist."),
    17: ("Etwas Neues ausprobieren",
         "Für Zurückhaltung vor neuen Dingen.",
         ["Was möchtest du gern ausprobieren?", "Was ist der kleinste erste Schritt?"],
         "Kleine Schritte sind besser als ein großer Sprung."),
    18: ("Wenn ich mich nicht traue",
         "Begleite das Kind. Verlang keinen Mut.",
         ["Was macht es gerade schwer?", "Was macht es leichter?"],
         "Verlang keinen Mut. Akzeptiere das Tempo vom Kind."),
    19: ("Mutig sein, auch mit Angst",
         "Zeige: Mut heißt nicht, keine Angst zu haben.",
         ["Wann warst du mutig, obwohl du Angst hattest?", "Wie hat sich das angefühlt?"],
         "Angst und Mut dürfen gleichzeitig da sein."),
    20: ("Hilfe holen ist okay",
         "Zeige: Hilfe holen ist stark. Kein Versagen.",
         ["Wer kann dir gerade helfen?", "Was sagst du, wenn du um Hilfe bittest?"],
         "Hilfe holen ist immer eine Stärke."),
    21: ("Was ist ein guter Freund?",
         "Sammelt gemeinsam Eigenschaften von Freundschaft. Konkret, nicht abstrakt.",
         ["Was macht jemanden zu einem guten Freund?", "Bist du das auch für andere?"],
         "Sammelt Beispiele aus dem Alltag vom Kind."),
    22: ("Wenn ich nicht mitspielen darf",
         "Für Ausschluss-Erfahrungen. Verurteile andere Kinder nicht vorschnell.",
         ["Was ist passiert?", "Was wünschst du dir stattdessen?"],
         "Nimm das Erleben vom Kind ernst."),
    23: ("Alleine in der Pause",
         "Für wiederkehrende Einsamkeit in der Pause.",
         ["Wie fühlt sich das Alleinsein für dich an?", "Was hilft dir, jemanden zu finden?"],
         "Sprich bei einem Muster auch mit der Schule. Die Karte allein reicht nicht."),
    24: ("Neue Freunde finden",
         "Erarbeitet konkrete erste Schritte.",
         ["Wie kannst du auf jemanden zugehen?", "Was kannst du fragen oder sagen?"],
         "Kleine, machbare Schritte sind besser als nur Ermutigung."),
    25: ("Wenn jemand gemein zu mir ist",
         "Nimm das Kind ernst. Bagatellisiere nicht.",
         ["Was genau ist passiert?", "Ist das schon öfter passiert?"],
         "Bei Hinweisen auf Mobbing: Hol die Schule oder eine Fachkraft dazu."),
    26: ("Mein Bauch spürt mit",
         "Führe Körperwahrnehmung als Frühwarnsystem ein.",
         ["Merkst du manchmal im Bauch, wenn etwas nicht stimmt?", "Wie fühlt sich das an?"],
         "Das ist kein Test. Es geht nur um das Wahrnehmen."),
    27: ("Wenn mein Körper „Stopp“ sagt",
         "Nimm körperliche Grenzsignale ernst. Zum Beispiel Müdigkeit.",
         ["Woran merkst du, dass es genug ist?", "Was machst du, wenn dein Körper Stopp sagt?"],
         "Das ist kein Trotz. Nimm das Signal ernst."),
    28: ("Was mir gut tut",
         "Sammelt positive Dinge für ruhige Momente.",
         ["Was tut deinem Körper gut?", "Wie oft machst du das?"],
         "Nutze die Karte in ruhigen Momenten. Nicht in akutem Stress."),
    29: ("Mein Körper gehört mir",
         "Vermittle altersgerecht: Das Kind bestimmt über den eigenen Körper.",
         ["Wer darf entscheiden, was mit deinem Körper passiert?", "Was machst du, wenn dir etwas nicht gefällt?"],
         "Bei Hinweisen auf eine Grenzverletzung: Sofort die Kinderschutz-Regeln nutzen. Die Karte ersetzt das nicht."),
    30: ("Zur Ruhe kommen",
         "Ein guter Abschluss. Biete eine Ruheübung an.",
         ["Was hilft dir, ruhig zu werden?", "Wollen wir das jetzt zusammen probieren?"],
         "Eine gute letzte Karte für eine Einheit."),
    31: ("Wenn Lernen schwerfällt",
         "Für Momente, in denen eine Aufgabe trotz viel Anstrengung nicht klappt.",
         ["Was ist gerade schwer für dich?", "Was hilft dir, wenn etwas nicht auf Anhieb klappt?"],
         "Anstrengung darf sichtbar sein. Nicht zu schnell trösten oder die Aufgabe leichter machen."),
    32: ("Sagen, was ich brauche",
         "Für Kinder, die Talker, Bilder oder Gebärden nutzen. Anders als bei FS-20 geht es hier um den eigenen Weg, sich auszudrücken.",
         ["Wie sagst du, was du brauchst?", "Was hilft dir dabei am meisten?"],
         "Jeder Weg zu sagen, was man braucht, zählt. Auch ohne Worte."),
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
        vorn = os.path.join(OUT, f"FS-{nr:02d}_Vorderseite.png")
        hinten = os.path.join(OUT, f"FS-{nr:02d}_Rueckseite.png")
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
