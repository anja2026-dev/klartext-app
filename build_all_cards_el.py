#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baut alle 30 EL-Basis-Karten (Vorder-/Rückseite PNG) aus EL_Kartenkonzept_Entwurf.md
und EL_Tipps_fuer_dich_Entwurf.md."""
import os, glob, sys
sys.path.insert(0, os.path.dirname(__file__))
from build_card_el import build_front, build_back, CARD_W, CARD_H

BILDER = "/sessions/kind-beautiful-ptolemy/mnt/klartext-app/bilder/el/"
OUT = "/sessions/kind-beautiful-ptolemy/mnt/outputs/el_karten_komplett/"
os.makedirs(OUT, exist_ok=True)

def find_image(nr):
    for pattern in (f"EL-{nr:02d}.jpg", f"EL-{nr:02d} *.jpg", f"EL-{nr:02d}.jpeg", f"EL-{nr:02d}.png"):
        files = sorted(glob.glob(os.path.join(BILDER, pattern)))
        if files:
            return files[0]
    return None

# nr: (titel, anleitung, [frage1, frage2], tipp_fuer_dich)
CARDS = {
    1: ("Meine Rolle gerade",
        "Guter Einstieg, um den aktuellen Stand der eigenen Rolle bewusst zu machen.",
        ["Wie würdest du deine Rolle als Elternteil gerade in einem Satz beschreiben?", "Was hat sich daran in letzter Zeit verändert?"],
        "Es gibt keine falsche Antwort. Die Rolle darf sich auch von Woche zu Woche anders anfühlen."),
    2: ("Zwischen Kümmern und Loslassen",
        "Für Momente, in denen Fürsorge und Autonomie des Kindes in Spannung stehen.",
        ["Wo merkst du gerade, dass du besonders viel abnimmst?", "Was würde passieren, wenn du an einer Stelle bewusst loslässt?"],
        "Loslassen an einer Stelle heißt nicht, insgesamt weniger zu kümmern."),
    3: ("Erwartungen an mich selbst",
        "Eigene, oft unausgesprochene Ansprüche an die eigene Elternrolle sichtbar machen.",
        ["Was erwartest du eigentlich von dir selbst als Elternteil?", "Woher kommt dieser Anspruch?"],
        "Oft stammen die höchsten Ansprüche aus der eigenen Kindheit, nicht aus der aktuellen Situation."),
    4: ("Wenn andere meine Erziehung infrage stellen",
        "Bei Kritik von außen (Familie, Schule, Umfeld) einsetzbar.",
        ["Wessen Meinung trifft dich dabei am meisten?", "Was würdest du dir stattdessen wünschen zu hören?"],
        "Nicht jede Kritik verdient ein Nachdenken – manche darf auch einfach vorbeiziehen."),
    5: ("Verantwortung teilen können",
        "Für Situationen, in denen Verantwortung ungleich verteilt ist (Partnerschaft, Familie, Fachkräfte).",
        ["Was trägst du gerade allein, das eigentlich geteilt werden könnte?", "Wer könnte dir davon etwas abnehmen?"],
        "Um Hilfe bitten ist keine Schwäche, sondern oft der erste Schritt zu mehr Kraft für das Wesentliche."),
    6: ("Was mein Kind gerade wirklich braucht",
        "Für Momente, in denen das Verhalten des Kindes schwer zu deuten ist.",
        ["Was zeigt dein Kind dir gerade mit seinem Verhalten?", "Was könnte dahinterstecken, auch wenn es auf den ersten Blick nicht so wirkt?"],
        "Besonders hilfreich, wenn ein Verhalten des Kindes gerade unverständlich wirkt."),
    7: ("Verhalten hinter dem Verhalten",
        "Hilfreich, wenn ein Verhalten des Kindes provoziert statt Verständnis auslöst.",
        ["Welches Gefühl steckt vermutlich hinter diesem Verhalten?", "Wie würdest du reagieren, wenn du nur das Gefühl sehen würdest, nicht das Verhalten?"],
        "Schwieriges Verhalten ist fast immer ein Hinweis, kein Angriff."),
    8: ("Wenn ich mein Kind nicht verstehe",
        "Entlastend einsetzen – nicht jedes Verhalten muss sofort erklärbar sein.",
        ["Was an deinem Kind ist dir gerade ein Rätsel?", "Ist es okay, das gerade nicht zu verstehen?"],
        "Nicht-Verstehen ist kein Versagen als Elternteil, nur ein ehrlicher Zwischenstand."),
    9: ("Unterschiede zwischen meinen Kindern",
        "Für Familien mit mehreren Kindern, besonders wenn eines mehr Aufmerksamkeit braucht.",
        ["Wo fällt es dir schwer, deine Kinder gleich zu behandeln?", "Muss Gerechtigkeit eigentlich Gleichheit bedeuten?"],
        "Gerechtigkeit heißt oft, jedem Kind das zu geben, was es gerade braucht – nicht dasselbe."),
    10: ("Mein Kind mit anderen Augen sehen",
         "Guter Perspektivwechsel-Impuls, um eingefahrene Sichtweisen zu lockern.",
         ["Was würde eine Person, die dein Kind mag, an ihm hervorheben?", "Wann hast du das zuletzt selbst so gesehen?"],
         "Guter Impuls für Tage, an denen der Blick aufs Kind besonders kritisch geworden ist."),
    11: ("Zuhören, ohne gleich zu lösen",
         "Für Situationen, in denen das Kind eigentlich nur gehört werden will.",
         ["Wann hast du zuletzt zugehört, ohne gleich eine Lösung anzubieten?", "Was würde sich ändern, wenn du das öfter tust?"],
         "Manchmal ist die beste Hilfe, gar keine Lösung anzubieten."),
    12: ("Wenn Gespräche eskalieren",
         "Rückblickend nach einem eskalierten Gespräch einsetzbar, nicht mittendrin.",
         ["An welchem Punkt kippt ein Gespräch bei euch meistens?", "Was könntest du an diesem Punkt anders machen?"],
         "Am hilfreichsten mit etwas Abstand zum letzten Streit, nicht mittendrin."),
    13: ("Grenzen setzen, ohne die Beziehung zu belasten",
         "Für die Sorge, dass Grenzen die Beziehung zum Kind gefährden könnten.",
         ["Welche Grenze fällt dir besonders schwer zu setzen?", "Was befürchtest du, wenn du sie setzt?"],
         "Klare Grenzen und eine warme Beziehung schließen sich nicht aus."),
    14: ("Ehrlich sein, ohne zu überfordern",
         "Bei der Frage, wie viel ein Kind über schwierige Themen wissen sollte.",
         ["Wo hältst du dich gerade zurück, um dein Kind zu schützen?", "Was wäre eine altersgerechte Version der Wahrheit?"],
         "Ehrlichkeit lässt sich fast immer altersgerecht dosieren, ganz weglassen muss sie nicht."),
    15: ("Mit dem Partner/der Partnerin an einem Strang",
         "Für Paare mit unterschiedlichen Erziehungsansätzen, nicht als Schuldzuweisung gedacht.",
         ["Wo unterscheidet ihr euch am meisten in der Erziehung?", "Was habt ihr trotzdem gemeinsam?"],
         "Nicht als Schuldfrage lesen – unterschiedliche Ansätze sind normal, nicht falsch."),
    16: ("Wenn mein Kind gemobbt wird",
         "Bei akuten Ausgrenzungs-/Mobbingerfahrungen des Kindes.",
         ["Was brauchst du gerade selbst, um deinem Kind beistehen zu können?", "Wer kann dich dabei unterstützen?"],
         "Erst für dich selbst sorgen, bevor du für dein Kind da sein kannst – das ist keine falsche Reihenfolge."),
    17: ("Wenn ich mich hilflos fühle",
         "Entlastend für Momente, in denen keine Lösung greifbar scheint.",
         ["Wann fühlst du dich als Elternteil am hilflosesten?", "Was hilft dir, das auszuhalten, auch ohne Lösung?"],
         "Hilflosigkeit auszuhalten ist manchmal die eigentliche Aufgabe, nicht ein Zeichen, dass etwas fehlt."),
    18: ("Der erste Schock nach einer Diagnose oder einem Befund",
         "Für die erste Zeit nach einer belastenden fachlichen Rückmeldung zum Kind.",
         ["Was hat sich für dich durch diese Nachricht verändert?", "Was bleibt trotzdem gleich?"],
         "Gib dir Zeit – diese Karte eignet sich nicht für den ersten Tag, eher für die Wochen danach."),
    19: ("Umgang mit Schule und Fachkräften in schwierigen Momenten",
         "Bei Spannungen zwischen Elternhaus und Schule/Fachkräften.",
         ["Was wünschst du dir gerade am meisten von der Schule?", "Was könntest du selbst dazu beitragen, dass es besser läuft?"],
         "Auch berechtigte Anliegen dürfen ruhig und bestimmt vorgetragen werden, nicht nur laut."),
    20: ("Wenn eine Krise vorbei ist",
         "Rückblickend nach überstandenen schwierigen Phasen.",
         ["Was hat euch als Familie durch die letzte schwierige Zeit getragen?", "Was nimmst du daraus mit?"],
         "Guter Moment, um festzuhalten, was diesmal geholfen hat – für die nächste schwierige Phase."),
    21: ("Der Morgen, der nie stressfrei ist",
         "Für wiederkehrenden Alltagsstress, niedrigschwellig einsetzbar.",
         ["Was macht eure Morgen am meisten stressig?", "Was wäre ein kleiner, realistischer erster Schritt?"],
         "Kleine Veränderungen wirken hier oft mehr als ein kompletter Neustart."),
    22: ("Hausaufgaben ohne Kampf",
         "Bei wiederkehrenden Konflikten rund um Hausaufgaben/Schulaufgaben.",
         ["Wo genau entsteht der Streit bei den Hausaufgaben?", "Wessen Aufgabe ist es eigentlich gerade?"],
         "Nicht jede Hausaufgaben-Verantwortung muss bei dir liegen."),
    23: ("Geschwister im Streit",
         "Für den Umgang mit wiederkehrendem Geschwisterstreit.",
         ["Musst du wirklich jeden Streit schlichten?", "Was würde passieren, wenn du dich öfter raushältst?"],
         "Nicht jeder Streit braucht ein elterliches Urteil."),
    24: ("Termine, Anträge, Formulare – der bürokratische Alltag",
         "Entlastend für die organisatorische Seite der Elternschaft.",
         ["Was an der Bürokratie belastet dich gerade am meisten?", "Was könntest du abgeben oder vereinfachen?"],
         "Auch Verwaltung darf an einem entlasteten Tag bearbeitet werden, nicht nur unter Druck."),
    25: ("Wenn der Alltag einfach zu viel wird",
         "Für allgemeine Überforderung, nicht an eine konkrete Situation gebunden.",
         ["Was würdest du gerade als Erstes weglassen, wenn du dürftest?", "Wer könnte dir eine Aufgabe abnehmen?"],
         "Ein einzelner weggelassener Punkt macht selten den Unterschied, den du befürchtest."),
    26: ("Meine eigenen Grenzen erkennen",
         "Für Eltern, die sich selbst oft zuletzt sehen.",
         ["Woran merkst du, dass du an deine Grenze kommst?", "Was tust du normalerweise, kurz bevor es zu viel wird?"],
         "Deine Grenze zu kennen schützt am Ende auch dein Kind."),
    27: ("Schuldgefühle als Elternteil",
         "Sehr verbreitetes Thema, entlastend statt bewertend einsetzen.",
         ["Wofür machst du dir gerade am meisten Vorwürfe?", "Würdest du das auch einer anderen Person so vorwerfen?"],
         "Fast jedes Elternteil kennt dieses Gefühl – das macht es nicht automatisch berechtigt."),
    28: ("Der Vergleich mit anderen Familien",
         "Bei Selbstzweifeln durch Vergleiche (Social Media, Umfeld, andere Familien).",
         ["Mit wem vergleichst du dich am meisten?", "Was siehst du bei der anderen Familie nicht?"],
         "Was du bei anderen siehst, ist fast nie ihr ganzer Alltag."),
    29: ("Kleine Momente für mich",
         "Ressourcenorientiert, um eigene kleine Auszeiten sichtbar zu machen.",
         ["Wann hattest du zuletzt einen Moment nur für dich?", "Was wäre ein realistischer kleiner Moment diese Woche?"],
         "Auch fünf Minuten zählen – es muss keine große Auszeit sein."),
    30: ("Worauf ich stolz sein darf",
         "Guter Abschluss-Impuls, wertschätzender Rückblick statt Bewertung.",
         ["Worauf bist du als Elternteil stolz, wenn du zurückblickst?", "Was möchtest du dir selbst dafür sagen?"],
         "Guter Abschluss – bewusst als Rückblick lesen, nicht als Bewertung."),
}

# nr: (label, systemische Frage) – dritte Frage, gezielt aus der systemischen Beratung
# ergänzt (25.07.2026): Skalierungsfrage (lösungsorientiert, de Shazer), Zirkuläre Frage
# (Mailänder Modell, Selvini Palazzoli/Boscolo/Cecchin) oder Handlungsfrage (lösungsorientiert)
# – bewusst nur eine dritte Frage, nicht vier, um die Karte nicht zum Arbeitsblatt zu machen.
SYSTEMFRAGEN = {
    1: ("SKALIERUNGSFRAGE", "Auf einer Skala von 1–10 – wie stimmig fühlt sich deine Rolle gerade an?"),
    2: ("HANDLUNGSFRAGE", "Was wäre ein kleiner, konkreter Schritt, um an einer Stelle bewusst loszulassen?"),
    3: ("ZIRKULÄRE FRAGE", "Was würde eine gute Freund:in sagen, wenn sie deinen Anspruch an dich selbst hören würde?"),
    4: ("SKALIERUNGSFRAGE", "Auf einer Skala von 1–10 – wie sehr lässt du diese Kritik gerade an dich heran?"),
    5: ("HANDLUNGSFRAGE", "Was wäre ein erster, kleiner Schritt, um genau das abzugeben?"),
    6: ("ZIRKULÄRE FRAGE", "Was würde dein Kind sagen, wenn es erklären könnte, was hinter seinem Verhalten steckt?"),
    7: ("ZIRKULÄRE FRAGE", "Wie würde eine außenstehende Person dieses Verhalten wohl deuten?"),
    8: ("SKALIERUNGSFRAGE", "Auf einer Skala von 1–10 – wie dringend fühlt sich das Nicht-Verstehen gerade an?"),
    9: ("HANDLUNGSFRAGE", "Was wäre ein kleiner Schritt, um dem Kind, das gerade zu kurz kommt, etwas mehr zu geben?"),
    10: ("SKALIERUNGSFRAGE", "Auf einer Skala von 1–10 – wie wohlwollend ist dein Blick auf dein Kind gerade?"),
    11: ("HANDLUNGSFRAGE", "Was wäre ein kleiner Schritt, um beim nächsten Gespräch bewusst länger zuzuhören, bevor du antwortest?"),
    12: ("ZIRKULÄRE FRAGE", "Wie würde eine außenstehende Person den Punkt beschreiben, an dem das Gespräch kippt?"),
    13: ("SKALIERUNGSFRAGE", "Auf einer Skala von 1–10 – wie sicher fühlst du dich gerade beim Grenzensetzen?"),
    14: ("HANDLUNGSFRAGE", "Was wäre ein kleiner, altersgerechter erster Satz, den du sagen könntest?"),
    15: ("ZIRKULÄRE FRAGE", "Was würde dein Partner/deine Partnerin sagen, wenn er/sie eure gemeinsamen Punkte beschreiben müsste?"),
    16: ("HANDLUNGSFRAGE", "Was wäre ein kleiner erster Schritt, um selbst Unterstützung zu holen?"),
    17: ("SKALIERUNGSFRAGE", "Auf einer Skala von 1–10 – wie stark ist das Gefühl von Hilflosigkeit gerade?"),
    18: ("SKALIERUNGSFRAGE", "Auf einer Skala von 1–10 – wie weit bist du gerade in der Verarbeitung?"),
    19: ("ZIRKULÄRE FRAGE", "Was würde die Schule/Fachkraft wohl sagen, wenn sie eure Zusammenarbeit beschreiben müsste?"),
    20: ("HANDLUNGSFRAGE", "Was möchtest du konkret festhalten, damit es dir beim nächsten Mal zur Verfügung steht?"),
    21: ("HANDLUNGSFRAGE", "Was wäre eine kleine, realistische Änderung, die du diese Woche ausprobieren könntest?"),
    22: ("HANDLUNGSFRAGE", "Was wäre ein kleiner Schritt, um Verantwortung stärker beim Kind zu lassen?"),
    23: ("SKALIERUNGSFRAGE", "Auf einer Skala von 1–10 – wie sehr ist es gerade wirklich dein Streit?"),
    24: ("HANDLUNGSFRAGE", "Was wäre ein kleiner Schritt, um etwas davon abzugeben oder zu vereinfachen?"),
    25: ("SKALIERUNGSFRAGE", "Auf einer Skala von 1–10 – wie voll fühlt sich dein Alltag gerade an?"),
    26: ("SKALIERUNGSFRAGE", "Auf einer Skala von 1–10 – wie nah bist du gerade an deiner Grenze?"),
    27: ("ZIRKULÄRE FRAGE", "Was würde eine gute Freund:in zu diesem Vorwurf sagen, den du dir machst?"),
    28: ("ZIRKULÄRE FRAGE", "Was würde die andere Familie wohl über ihre eigenen schwierigen Momente sagen, die du nicht siehst?"),
    29: ("HANDLUNGSFRAGE", "Was wäre ein realistischer kleiner Moment, den du dir diese Woche konkret einplanst?"),
    30: ("SKALIERUNGSFRAGE", "Auf einer Skala von 1–10 – wie sehr erlaubst du dir gerade, stolz zu sein?"),
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
                "systemfrage": SYSTEMFRAGEN.get(nr)}
        vorn = os.path.join(OUT, f"EL-{nr:02d}_Vorderseite.png")
        hinten = os.path.join(OUT, f"EL-{nr:02d}_Rueckseite.png")
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
        print("Fehler bei:", fehler)

if __name__ == "__main__":
    run()
