#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baut alle 21 EL-Zusatzblock-Karten (Autismus, ADHS, Pflegekinder) als Vorder-/Rückseite PNG.
Aus EL_Zusatzblock_Autismus.md, EL_Zusatzblock_ADHS.md, EL_Zusatzblock_Pflegekinder.md +
EL_Zusatzbloecke_Tipps_fuer_dich.md."""
import os, glob, sys
sys.path.insert(0, os.path.dirname(__file__))
from build_card_el import build_front, build_back, CARD_W, CARD_H

BILDER = "/sessions/kind-beautiful-ptolemy/mnt/klartext-app/bilder/el/"
OUT = "/sessions/kind-beautiful-ptolemy/mnt/outputs/el_zusatz_karten_komplett/"
os.makedirs(OUT, exist_ok=True)

def find_image(code, nr):
    # robust gegen Tippfehler im Dateinamen (z.B. "EL-AT-05..jpg"): Präfix-Glob statt exaktem Match
    for pattern in (f"{code}-{nr:02d}.jpg", f"{code}-{nr:02d}.*jpg", f"{code}-{nr:02d}*.jpg",
                    f"{code}-{nr:02d}.jpeg", f"{code}-{nr:02d}.png"):
        files = sorted(glob.glob(os.path.join(BILDER, pattern)))
        if files:
            return files[0]
    return None

# code: (systemfrage-label, systemfrage-text) je nr – dritte Frage, gleiche Systematik wie EL-Basis
SYSTEMFRAGEN = {
    "EL-AT": {
        1: ("HANDLUNGSFRAGE", "Was wäre ein kleiner Schritt, um ein altes Bild bewusst loszulassen?"),
        2: ("SKALIERUNGSFRAGE", "Auf einer Skala von 1–10 – wie nah bist du gerade an deiner Grenze?"),
        3: ("SKALIERUNGSFRAGE", "Auf einer Skala von 1–10 – wie weit bist du in der Verarbeitung der Diagnose?"),
        4: ("ZIRKULÄRE FRAGE", "Was würde eine Person, die dich gut kennt, zu deinen häufigen Erklärungen sagen?"),
        5: ("SKALIERUNGSFRAGE", "Auf einer Skala von 1–10 – wie erschöpft bist du gerade wirklich?"),
        6: ("HANDLUNGSFRAGE", "Was wäre ein kleiner, konkreter Moment für das andere Kind diese Woche?"),
        7: ("ZIRKULÄRE FRAGE", "Was würde jemand, der eure Entwicklung begleitet hat, an dir hervorheben?"),
    },
    "EL-ADHS": {
        1: ("SKALIERUNGSFRAGE", "Auf einer Skala von 1–10 – wie viel Kraft kostet dich die Energie deines Kindes gerade?"),
        2: ("HANDLUNGSFRAGE", "Was wäre ein kleiner Schritt, um dir das Wiederholen leichter zu machen?"),
        3: ("SKALIERUNGSFRAGE", "Auf einer Skala von 1–10 – welches Gefühl überwiegt gerade, Erleichterung oder Sorge?"),
        4: ("ZIRKULÄRE FRAGE", "Was würde jemand sagen, der eure Situation wirklich kennt?"),
        5: ("SKALIERUNGSFRAGE", "Auf einer Skala von 1–10 – wie viel Geduld hast du gerade noch übrig?"),
        6: ("ZIRKULÄRE FRAGE", "Was würde eine Person, die euch gut kennt, zu dieser Entscheidung sagen?"),
        7: ("HANDLUNGSFRAGE", "Was wäre eine kleine Geste, mit der du dir selbst diesen Fortschritt anerkennst?"),
    },
    "EL-PF": {
        1: ("SKALIERUNGSFRAGE", "Auf einer Skala von 1–10 – wie klar fühlt sich deine Rolle gerade an?"),
        2: ("HANDLUNGSFRAGE", "Was wäre ein kleiner, geduldiger nächster Schritt im Vertrauensaufbau?"),
        3: ("ZIRKULÄRE FRAGE", "Was würde eine Person, die eure Situation gut kennt, zu deinen Gefühlen gegenüber der Herkunftsfamilie sagen?"),
        4: ("SKALIERUNGSFRAGE", "Auf einer Skala von 1–10 – wie leicht fällt es dir gerade, das Verhalten nicht persönlich zu nehmen?"),
        5: ("SKALIERUNGSFRAGE", "Auf einer Skala von 1–10 – wie stark sind die Zweifel gerade?"),
        6: ("HANDLUNGSFRAGE", "Was kannst du trotz der Unsicherheit heute ganz konkret für das Kind tun?"),
        7: ("ZIRKULÄRE FRAGE", "Was würde das Kind wohl sagen, wenn es beschreiben müsste, was sich durch dich verändert hat?"),
    },
    "EL-JD": {
        1: ("HANDLUNGSFRAGE", "Was wäre ein kleiner, konkreter Schritt, um deinem Kind diese Woche mehr Eigenverantwortung zuzutrauen?"),
        2: ("ZIRKULÄRE FRAGE", "Was würde dein Kind sagen, wenn es erklären müsste, warum es sich gerade zurückzieht?"),
        3: ("SKALIERUNGSFRAGE", "Auf einer Skala von 1–10 – wie sehr ist Mediennutzung gerade ein Machtkampf statt ein Thema?"),
        4: ("HANDLUNGSFRAGE", "Was wäre ein kleiner nächster Schritt, um die Absprache mit dem anderen Elternteil zu verbessern?"),
        5: ("ZIRKULÄRE FRAGE", "Was würde dein Kind sagen, wenn es beschreiben müsste, wie viel Druck es von dir spürt?"),
        6: ("SKALIERUNGSFRAGE", "Auf einer Skala von 1–10 – wie sehr kannst du diese Andersartigkeit gerade akzeptieren, ohne sie zu bewerten?"),
        7: ("HANDLUNGSFRAGE", "Was möchtest du deinem Kind bei nächster Gelegenheit ausdrücklich zutrauen?"),
    },
}

# code: (kategorie_label, footer_label, {nr: (titel, anleitung, [frage1, frage2], tipp)})
BLOECKE = {
    "EL-AT": (
        "EL-AT · ZUSATZBLOCK AUTISMUS",
        "EL-Zusatzblock Autismus",
        {
            1: ("Das Bild vom \"normalen\" Familienalltag loslassen",
                "Für die Phase, in der alte Vorstellungen von Familienalltag nicht mehr passen.",
                ["Welches Bild von Familienalltag hattest du, bevor ihr wusstet, was euer Kind braucht?",
                 "Was davon vermisst du – und was war eigentlich nie realistisch?"],
                "Ein anderer Alltag ist nicht automatisch ein schlechterer."),
            2: ("Wenn die eigene Fürsorge an Grenzen kommt",
                "Für Momente extremer Anforderung (z. B. rund um sensorische Überlastung oder Meltdowns).",
                ["Was kostet dich in solchen Momenten am meisten Kraft?",
                 "Was hilft dir selbst, wenn es gerade zu viel wird?"],
                "Grenzen zu spüren heißt nicht, dass du zu wenig gibst."),
            3: ("Die Diagnose und was sie für mich bedeutet",
                "Nicht für die erste Zeit nach der Diagnose gedacht, eher für die Verarbeitung danach.",
                ["Was hat sich für dich selbst durch die Diagnose verändert?",
                 "Was ist gleich geblieben, auch wenn es sich anders anfühlt?"],
                "Es ist normal, wenn sich das Verhältnis zur Diagnose mit der Zeit verändert."),
            4: ("Erklären, ohne dich zu entschuldigen",
                "Für Situationen, in denen Umfeld/Familie das Verhalten des Kindes infrage stellt.",
                ["Wo erklärst du dich gerade eigentlich zu oft?",
                 "Was würdest du sagen, wenn du dich nicht rechtfertigen müsstest?"],
                "Eine Erklärung ist keine Entschuldigung, auch wenn sie sich manchmal so anfühlt."),
            5: ("Die eigene Erschöpfung ernst nehmen",
                "Entlastend, besonders wenn Erschöpfung lange als \"normal\" hingenommen wurde.",
                ["Woran merkst du, dass du erschöpft bist – nicht dein Kind, sondern du selbst?",
                 "Wer weiß eigentlich, wie erschöpft du gerade bist?"],
                "Erschöpfung, die lange andauert, ist kein Charakterzug, sondern ein Signal."),
            6: ("Geschwisterkinder nicht aus dem Blick verlieren",
                "Für Familien mit weiteren Kindern, die neben dem autistischen Kind manchmal zurückstehen.",
                ["Wie geht es deinem anderen Kind gerade wirklich?",
                 "Was bräuchte es von dir, das gerade zu kurz kommt?"],
                "Auch kleine, bewusste Momente zu zweit zählen."),
            7: ("Stolz auf die eigenen Fortschritte",
                "Guter Abschluss-Impuls, bewusst auf die Eltern selbst bezogen, nicht nur auf das Kind.",
                ["Worauf bist du bei dir selbst stolz, wenn du auf die letzten Monate schaust?",
                 "Was hast du gelernt, das dir vorher niemand hätte beibringen können?"],
                "Dein eigener Lernweg zählt genauso wie der deines Kindes."),
        }),
    "EL-ADHS": (
        "EL-ADHS · ZUSATZBLOCK ADHS",
        "EL-Zusatzblock ADHS",
        {
            1: ("Leben mit einem hohen Energielevel",
                "Für den Alltag mit viel Bewegung, Impulsivität, wechselnder Aufmerksamkeit.",
                ["Was an der Energie deines Kindes kostet dich am meisten Kraft – und was bewunderst du eigentlich daran?",
                 "Wann hast du zuletzt bewusst beides gleichzeitig gesehen?"],
                "Viel Energie ist anstrengend und eine echte Stärke – beides gleichzeitig."),
            2: ("Wenn Grenzen immer wieder neu verhandelt werden",
                "Für die Erfahrung, dass eine einmal gesetzte Grenze nicht \"einfach hält\".",
                ["Welche Grenze musst du am häufigsten neu durchsetzen?",
                 "Was würde dir helfen, das als normal statt als Scheitern zu sehen?"],
                "Wiederholen müssen ist kein Zeichen, dass die Grenze falsch war."),
            3: ("Die Diagnose – zwischen Erleichterung und Sorge",
                "Für die Zeit nach der Diagnose, wenn beide Gefühle gleichzeitig da sind.",
                ["Was hat sich durch die Diagnose erleichtert?",
                 "Welche Sorge ist neu dazugekommen?"],
                "Beide Gefühle dürfen gleichzeitig da sein, das eine widerlegt das andere nicht."),
            4: ("Wenn andere „schlechte Erziehung“ vermuten",
                "Bei Blicken/Kommentaren von außen, besonders in der Öffentlichkeit.",
                ["In welcher Situation triffst du solche Blicke am meisten?",
                 "Was würdest du der Person sagen, wenn es keine Konsequenzen hätte?"],
                "Fremde Blicke kennen selten die ganze Geschichte."),
            5: ("Die eigene Geduld an ihre Grenzen bringen",
                "Entlastend – auch sehr geduldige Eltern kommen an einen Punkt.",
                ["Wann war deine Geduld zuletzt komplett aufgebraucht?",
                 "Was hättest du in dem Moment gebraucht, nicht dein Kind?"],
                "Geduld ist endlich, auch bei liebevollen Eltern."),
            6: ("Entscheidungen rund um Unterstützung und Behandlung",
                "Für die Auseinandersetzung mit Therapie-, Förder- oder Behandlungsfragen – ohne Bewertung einer bestimmten Richtung.",
                ["Was beschäftigt dich an der aktuellen Entscheidung am meisten?",
                 "Wessen Meinung fehlt dir noch, um dich sicherer zu fühlen?"],
                "Es gibt hier keine einzig richtige Entscheidung, nur die für eure Familie stimmige."),
            7: ("Stolz auf die eigenen Fortschritte",
                "Guter Abschluss-Impuls, bewusst auf die Eltern selbst bezogen.",
                ["Worauf bist du bei dir selbst stolz, wenn du auf die letzten Monate schaust?",
                 "Was würdest du einem anderen Elternteil in deiner Situation gerne sagen?"],
                "Fortschritt zeigt sich oft leiser, als man erwartet."),
        }),
    "EL-PF": (
        "EL-PF · ZUSATZBLOCK PFLEGEKINDER",
        "EL-Zusatzblock Pflegekinder",
        {
            1: ("Die eigene Rolle als Pflegeeltern finden",
                "Für die Auseinandersetzung mit einer Rolle, die weder \"Elternteil\" im klassischen Sinn noch \"nur Betreuung\" ist.",
                ["Wie würdest du deine Rolle für dieses Kind gerade beschreiben?",
                 "Was daran fühlt sich noch ungewohnt an?"],
                "Diese Rolle darf sich mit der Zeit entwickeln, sie muss nicht von Anfang an klar sein."),
            2: ("Bindung aufbauen, ohne zu drängen",
                "Für die oft längere, nicht linear verlaufende Zeit des Vertrauensaufbaus.",
                ["Woran merkst du kleine Fortschritte in der Bindung, auch wenn sie klein sind?",
                 "Was hilft dir, geduldig zu bleiben, wenn es gerade nicht vorangeht?"],
                "Bindung, die sich Zeit nimmt, ist nicht weniger echt."),
            3: ("Umgang mit der Herkunftsfamilie",
                "Für die oft komplexen Gefühle gegenüber leiblichen Eltern des Kindes.",
                ["Welches Gefühl gegenüber der Herkunftsfamilie beschäftigt dich gerade am meisten?",
                 "Muss dieses Gefühl aufgelöst werden, oder darf es einfach da sein?"],
                "Widersprüchliche Gefühle gegenüber der Herkunftsfamilie sind keine Illoyalität dem Kind gegenüber."),
            4: ("Wenn Verhalten aus der Vorgeschichte kommt",
                "Hilft, schwieriges Verhalten als Folge früherer Erfahrungen statt als aktuelle Ablehnung zu verstehen.",
                ["Welches Verhalten fällt dir am schwersten, nicht persönlich zu nehmen?",
                 "Was könnte es mit der Geschichte des Kindes zu tun haben, nicht mit dir?"],
                "Nicht jede Reaktion des Kindes ist eine Reaktion auf dich."),
            5: ("Die eigene Erschöpfung und eigene Zweifel ernst nehmen",
                "Entlastend – Zweifel an der eigenen Entscheidung gehören dazu, auch bei guter Pflegeelternschaft.",
                ["Wann hattest du zuletzt ernsthafte Zweifel?",
                 "Was hat dir geholfen, trotzdem weiterzumachen?"],
                "Zweifel zu haben bedeutet nicht, die falsche Entscheidung getroffen zu haben."),
            6: ("Unsicherheit über Zukunft und Dauer",
                "Für die besondere Belastung durch offene oder ungewisse Zukunftsperspektiven.",
                ["Welcher ungewisse Punkt beschäftigt dich gerade am meisten?",
                 "Was kannst du trotz der Unsicherheit heute schon für das Kind da sein lassen?"],
                "Für das Kind da zu sein muss nicht von einer geklärten Zukunft abhängen."),
            7: ("Stolz auf das, was schon gelungen ist",
                "Guter Abschluss-Impuls, bewusst auf das Erreichte statt auf das noch Fehlende schauen.",
                ["Worauf bist du stolz, wenn du auf die gemeinsame Zeit zurückblickst?",
                 "Was hat sich für das Kind durch dich bereits zum Besseren verändert?"],
                "Auch kleine Veränderungen beim Kind sind oft ein großer Schritt für es."),
        }),
    "EL-JD": (
        "EL-JD · ZUSATZBLOCK ELTERN VON JUGENDLICHEN",
        "EL-Zusatzblock Eltern von Jugendlichen",
        {
            1: ("Loslassen im Jugendalter",
                "Für die Phase, in der aus Fürsorge zunehmend Vertrauen werden darf.",
                ["Wo fällt dir Loslassen bei deinem jugendlichen Kind besonders schwer?",
                 "Was würde sich ändern, wenn du an dieser Stelle einen Schritt zurücktrittst?"],
                "Loslassen in der Pubertät ist ein Prozess in kleinen Schritten, kein einmaliger Sprung."),
            2: ("Wenn sich mein Kind zurückzieht",
                "Für die oft verunsichernde Erfahrung, dass ein jugendliches Kind plötzlich weniger erzählt.",
                ["Wie fühlt sich der Rückzug deines Kindes für dich an?",
                 "Woran erkennst du, dass die Tür trotzdem noch offen ist?"],
                "Rückzug in der Pubertät ist meistens Entwicklung, nicht Ablehnung."),
            3: ("Medien und Familienfrieden",
                "Für wiederkehrenden Streit um Handy- und Bildschirmzeit.",
                ["Worum geht es beim Medienstreit eigentlich wirklich – um die Zeit oder um etwas anderes?",
                 "Wie ist dein eigener Umgang mit Medien gerade als Vorbild?"],
                "Kinder orientieren sich mehr am eigenen Medienverhalten der Eltern als an deren Regeln."),
            4: ("Erziehen nach einer Trennung",
                "Für Eltern, die getrennt und trotzdem gemeinsam erziehen.",
                ["Wo gelingt die Abstimmung mit dem anderen Elternteil gerade gut, wo nicht?",
                 "Was bräuchte dein Kind gerade am meisten von euch beiden gemeinsam?"],
                "Ein Kind muss die Eltern nicht einig erleben, aber sicher, dass es nicht zwischen ihnen steht."),
            5: ("Schuldruck aus Elternsicht",
                "Für die eigene Anspannung rund um Noten, Schulwahl und Zukunftssorgen.",
                ["Wessen Erwartung an die schulische Leistung deines Kindes spürst du gerade am meisten – deine eigene oder von außen?",
                 "Was würdest du dir wünschen, wenn Noten nicht so im Zentrum stünden?"],
                "Deine eigene Sorge um die Zukunft ist verständlich – sie muss trotzdem nicht beim Kind landen."),
            6: ("Wenn mein Kind andere Werte lebt",
                "Für Momente, in denen die Identität des jugendlichen Kindes von den eigenen Vorstellungen abweicht.",
                ["Was genau an den Werten oder der Identität deines Kindes fühlt sich fremd für dich an?",
                 "Was davon ist wirklich ein Problem, was nur ungewohnt?"],
                "Andere Werte als deine eigenen sind kein Zeichen, dass etwas schiefgelaufen ist."),
            7: ("Stolz auf das, was schon losgelassen wurde",
                "Guter Abschluss-Impuls, bewusst wertschätzend statt bewertend.",
                ["Worauf bist du stolz, wenn du siehst, wie selbstständig dein Kind schon ist?",
                 "Was hast du selbst über Loslassen gelernt, das du vorher nicht wusstest?"],
                "Jeder losgelassene Schritt ist ein Beweis, dass dein Kind auf einem guten Weg ist – und du auch."),
        }),
}

def run():
    ok, fehler = [], []
    for code, (badge, footer_deck, cards) in BLOECKE.items():
        for nr, (titel, anleitung, fragen, tipp) in cards.items():
            image_path = find_image(code, nr)
            if not image_path:
                fehler.append((code, nr, "Bild nicht gefunden"))
                continue
            card = {
                "nr": nr, "titel": titel, "anleitung": anleitung, "fragen": fragen,
                "hinweis": tipp, "badge": badge, "total": 7,
                "id_text": f"{code}-{nr:02d}", "footer_deck": footer_deck,
                "systemfrage": SYSTEMFRAGEN.get(code, {}).get(nr),
            }
            vorn = os.path.join(OUT, f"{code}-{nr:02d}_Vorderseite.png")
            hinten = os.path.join(OUT, f"{code}-{nr:02d}_Rueckseite.png")
            try:
                build_front(card, image_path, vorn)
                build_back(card, hinten)
                ok.append(f"{code}-{nr:02d}")
            except Exception as e:
                fehler.append((code, nr, str(e)))
    print(f"Fertig: {len(ok)} Karten gebaut.")
    if fehler:
        print("Fehler bei:", fehler)

if __name__ == "__main__":
    run()
