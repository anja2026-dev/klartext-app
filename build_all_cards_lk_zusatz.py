#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baut alle 21 LK-Zusatzblock-Karten (Autismus, ADHS, Pflegekinder) als Vorder-/Rückseite PNG.
Aus LK_Zusatzbloecke_Entwurf.md."""
import os, glob, sys
sys.path.insert(0, os.path.dirname(__file__))
from build_card_lk import build_front, build_back

BILDER = "/sessions/kind-beautiful-ptolemy/mnt/klartext-app/bilder/lk/"
OUT = "/sessions/kind-beautiful-ptolemy/mnt/outputs/lk_zusatz_karten_komplett/"
os.makedirs(OUT, exist_ok=True)

def find_image(code, nr):
    for pattern in (f"{code}-{nr:02d}.jpg", f"{code}-{nr:02d}.*jpg", f"{code}-{nr:02d}*.jpg",
                    f"{code}-{nr:02d}.jpeg", f"{code}-{nr:02d}.png"):
        files = sorted(glob.glob(os.path.join(BILDER, pattern)))
        if files:
            return files[0]
    return None

SYSTEMFRAGEN = {
    "LK-R-AT": {
        1: ("HANDLUNGSFRAGE", "Was wäre ein kleiner Schritt, um ein altes Bild bewusst loszulassen?"),
        2: ("SKALIERUNGSFRAGE", "Auf einer Skala von 1–10 – wie nah bist du gerade an deiner Grenze?"),
        3: ("SKALIERUNGSFRAGE", "Auf einer Skala von 1–10 – wie sicher fühlst du dich gerade im Umgang mit der Diagnose?"),
        4: ("ZIRKULÄRE FRAGE", "Was würde eine Kollegin/ein Kollege, die/der dich gut kennt, zu deinen häufigen Erklärungen sagen?"),
        5: ("SKALIERUNGSFRAGE", "Auf einer Skala von 1–10 – wie erschöpft bist du gerade wirklich?"),
        6: ("HANDLUNGSFRAGE", "Was wäre ein kleiner, konkreter Moment für die Klasse als Ganzes diese Woche?"),
        7: ("ZIRKULÄRE FRAGE", "Was würde jemand, der eure Entwicklung begleitet hat, an dir hervorheben?"),
    },
    "LK-R-ADHS": {
        1: ("SKALIERUNGSFRAGE", "Auf einer Skala von 1–10 – wie viel Kraft kostet dich die Energie dieses Kindes gerade?"),
        2: ("HANDLUNGSFRAGE", "Was wäre ein kleiner Schritt, um dir das Wiederholen leichter zu machen?"),
        3: ("SKALIERUNGSFRAGE", "Auf einer Skala von 1–10 – wie sehr überwiegt gerade die Erleichterung gegenüber der zusätzlichen Verantwortung?"),
        4: ("ZIRKULÄRE FRAGE", "Was würde jemand sagen, der die Situation in deiner Klasse wirklich kennt?"),
        5: ("SKALIERUNGSFRAGE", "Auf einer Skala von 1–10 – wie viel Geduld hast du gerade noch übrig?"),
        6: ("ZIRKULÄRE FRAGE", "Was würden die Eltern zu dieser Zusammenarbeit gerade sagen?"),
        7: ("HANDLUNGSFRAGE", "Was wäre eine kleine Geste, mit der du dir selbst diesen Fortschritt anerkennst?"),
    },
    "LK-R-PF": {
        1: ("SKALIERUNGSFRAGE", "Auf einer Skala von 1–10 – wie klar fühlt sich deine Rolle für dieses Kind gerade an?"),
        2: ("HANDLUNGSFRAGE", "Was wäre ein kleiner, geduldiger nächster Schritt im Vertrauensaufbau?"),
        3: ("ZIRKULÄRE FRAGE", "Was würde eine Person, die die Situation gut kennt, zu deinem Umgang mit diesem Wissen sagen?"),
        4: ("SKALIERUNGSFRAGE", "Auf einer Skala von 1–10 – wie leicht fällt es dir gerade, das Verhalten nicht persönlich zu nehmen?"),
        5: ("HANDLUNGSFRAGE", "Was wäre ein kleiner Schritt, um die Kommunikation mit den Pflegeeltern zu vereinfachen?"),
        6: ("SKALIERUNGSFRAGE", "Auf einer Skala von 1–10 – wie verlässlich fühlt sich der Schulalltag für dieses Kind gerade an?"),
        7: ("ZIRKULÄRE FRAGE", "Was würde das Kind wohl sagen, wenn es beschreiben müsste, was sich durch dich verändert hat?"),
    },
}

# code: (badge, footer_deck, {nr: (titel, anleitung, [frage1, frage2], tipp)})
BLOECKE = {
    "LK-R-AT": (
        "LK-R-AT · ZUSATZBLOCK AUTISMUS",
        "LK-Zusatzblock Autismus",
        {
            1: ("Das Bild vom \"normalen\" Unterricht loslassen",
                "Für die Phase, in der klassische Unterrichtserwartungen nicht mehr passen.",
                ["Welches Bild von einem 'guten Unterrichtstag' hattest du, bevor du wusstest, was dieses Kind braucht?",
                 "Was davon war eigentlich nie realistisch?"],
                "Ein anderer Unterrichtstag ist nicht automatisch ein schlechterer."),
            2: ("Wenn die eigene Kapazität an Grenzen kommt",
                "Für Momente extremer Anforderung (z. B. bei sensorischer Überlastung/Meltdown im Unterricht).",
                ["Was kostet dich in solchen Momenten am meisten Kraft?",
                 "Was hilft dir selbst, wenn es gerade zu viel wird?"],
                "Grenzen zu spüren heißt nicht, dass du zu wenig gibst."),
            3: ("Die Diagnose und was sie für meinen Unterricht bedeutet",
                "Nicht für die erste Zeit nach Bekanntwerden gedacht, eher für die praktische Umsetzung danach.",
                ["Was hat sich für deinen Unterricht durch das Wissen um die Diagnose verändert?",
                 "Was ist gleich geblieben?"],
                "Es ist normal, wenn sich der praktische Umgang mit einer Diagnose mit der Zeit einspielt."),
            4: ("Erklären, ohne dich zu rechtfertigen",
                "Für Situationen, in denen Kolleg:innen oder Eltern anderer Kinder das Vorgehen infrage stellen.",
                ["Wo erklärst du dich gerade eigentlich zu oft?",
                 "Was würdest du sagen, wenn du dich nicht rechtfertigen müsstest?"],
                "Eine Erklärung ist keine Rechtfertigung, auch wenn sie sich manchmal so anfühlt."),
            5: ("Die eigene Erschöpfung ernst nehmen",
                "Entlastend, besonders wenn Mehraufwand lange als \"normal\" hingenommen wurde.",
                ["Woran merkst du, dass du erschöpft bist?",
                 "Wer weiß eigentlich, wie viel Kraft das gerade kostet?"],
                "Erschöpfung, die lange andauert, ist kein Charakterzug, sondern ein Signal."),
            6: ("Die anderen Kinder der Klasse nicht aus dem Blick verlieren",
                "Für die Balance zwischen individueller Unterstützung und der ganzen Klasse.",
                ["Wie geht es der Klasse gerade wirklich?",
                 "Was bräuchte die Gruppe von dir, das gerade zu kurz kommt?"],
                "Auch kleine, bewusste Momente für die ganze Klasse zählen."),
            7: ("Stolz auf die eigenen Fortschritte",
                "Guter Abschluss-Impuls, bewusst auf dich als Lehrkraft bezogen.",
                ["Worauf bist du bei dir selbst stolz, wenn du auf die letzten Monate schaust?",
                 "Was hast du gelernt, das dir vorher niemand hätte beibringen können?"],
                "Dein eigener Lernweg zählt genauso wie der des Kindes."),
        }),
    "LK-R-ADHS": (
        "LK-R-ADHS · ZUSATZBLOCK ADHS",
        "LK-Zusatzblock ADHS",
        {
            1: ("Unterrichten mit einem hohen Energielevel im Raum",
                "Für den Unterricht mit viel Bewegung, Impulsivität, wechselnder Aufmerksamkeit.",
                ["Was an der Energie dieses Kindes kostet dich am meisten Kraft – und was bewunderst du eigentlich daran?",
                 "Wann hast du zuletzt bewusst beides gleichzeitig gesehen?"],
                "Viel Energie ist anstrengend und eine echte Stärke – beides gleichzeitig."),
            2: ("Wenn Regeln immer wieder neu durchgesetzt werden müssen",
                "Für die Erfahrung, dass eine einmal erklärte Regel nicht \"einfach hält\".",
                ["Welche Regel musst du am häufigsten neu durchsetzen?",
                 "Was würde dir helfen, das als normal statt als Scheitern zu sehen?"],
                "Wiederholen müssen ist kein Zeichen, dass die Regel falsch war."),
            3: ("Die Diagnose – zwischen Erleichterung und zusätzlicher Verantwortung",
                "Für die Zeit, in der beide Gefühle gleichzeitig da sind.",
                ["Was hat sich durch die Diagnose für deinen Unterricht erleichtert?",
                 "Welche zusätzliche Verantwortung ist neu dazugekommen?"],
                "Beide Gefühle dürfen gleichzeitig da sein, das eine widerlegt das andere nicht."),
            4: ("Wenn andere „schlechtes Classroom-Management“ vermuten",
                "Bei Kommentaren von Kolleg:innen oder Eltern.",
                ["In welcher Situation triffst du solche Kommentare am meisten?",
                 "Was würdest du der Person sagen, wenn es keine Konsequenzen hätte?"],
                "Fremde Kommentare kennen selten die ganze Geschichte."),
            5: ("Die eigene Geduld an ihre Grenzen bringen",
                "Entlastend – auch sehr geduldige Lehrkräfte kommen an einen Punkt.",
                ["Wann war deine Geduld zuletzt komplett aufgebraucht?",
                 "Was hättest du in dem Moment gebraucht?"],
                "Geduld ist endlich, auch bei sehr engagierten Lehrkräften."),
            6: ("Zusammenarbeit mit Eltern und Fachpersonen",
                "Für die Abstimmung rund um Unterstützung, Nachteilsausgleich oder Behandlung.",
                ["Was läuft in der Zusammenarbeit gerade gut?",
                 "Was würde die Abstimmung leichter machen?"],
                "Gute Abstimmung entsteht selten auf einmal, sondern über viele kleine Gespräche."),
            7: ("Stolz auf die eigenen Fortschritte",
                "Guter Abschluss-Impuls, bewusst auf dich selbst bezogen.",
                ["Worauf bist du bei dir selbst stolz, wenn du auf die letzten Monate schaust?",
                 "Was würdest du einer Kollegin/einem Kollegen in deiner Situation gerne sagen?"],
                "Fortschritt zeigt sich oft leiser, als man erwartet."),
        }),
    "LK-R-PF": (
        "LK-R-PF · ZUSATZBLOCK PFLEGEKINDER",
        "LK-Zusatzblock Pflegekinder",
        {
            1: ("Die eigene Rolle für dieses Kind finden",
                "Für die Auseinandersetzung mit einer Rolle, die mehr sein kann als \"nur Unterricht\".",
                ["Wie würdest du deine Rolle für dieses Kind gerade beschreiben?",
                 "Was daran fühlt sich noch ungewohnt an?"],
                "Diese Rolle darf sich mit der Zeit entwickeln, sie muss nicht von Anfang an klar sein."),
            2: ("Vertrauen aufbauen, ohne zu drängen",
                "Für die oft längere Zeit des Vertrauensaufbaus im Klassenzimmer.",
                ["Woran merkst du kleine Fortschritte im Vertrauen, auch wenn sie klein sind?",
                 "Was hilft dir, geduldig zu bleiben?"],
                "Vertrauen, das sich Zeit nimmt, ist nicht weniger echt."),
            3: ("Umgang mit Informationen über die Vorgeschichte",
                "Für den sensiblen Umgang mit dem Wissen über die Situation des Kindes.",
                ["Wie viel von der Vorgeschichte beeinflusst gerade deinen Blick auf das Kind?",
                 "Was brauchst du, um fair zu bleiben?"],
                "Wissen um die Vorgeschichte darf informieren, ohne den Blick festzulegen."),
            4: ("Wenn Verhalten aus der Vorgeschichte kommt",
                "Hilft, schwieriges Verhalten im Unterricht als Folge früherer Erfahrungen statt als aktuellen Regelverstoß zu verstehen.",
                ["Welches Verhalten fällt dir am schwersten, nicht persönlich zu nehmen?",
                 "Was könnte es mit der Geschichte des Kindes zu tun haben, nicht mit dir oder der Klasse?"],
                "Nicht jede Reaktion des Kindes ist eine Reaktion auf dich oder die Klasse."),
            5: ("Zusammenarbeit mit Pflegeeltern und Fachstellen",
                "Für die oft komplexere Kommunikation als bei anderen Elternhäusern.",
                ["Was läuft in der Zusammenarbeit gerade gut?",
                 "Was würde sie erleichtern?"],
                "Gute Zusammenarbeit entsteht oft über kurze, regelmäßige statt seltene, lange Kontakte."),
            6: ("Stabilität bieten trotz Unsicherheiten",
                "Für die besondere Bedeutung von Verlässlichkeit bei einem Kind mit instabiler Vorgeschichte.",
                ["Was kannst du diesem Kind an Verlässlichkeit ganz konkret bieten?",
                 "Was davon tust du bereits, ohne es zu merken?"],
                "Verlässlichkeit im Kleinen zählt oft mehr als große Gesten."),
            7: ("Stolz auf das, was schon gelungen ist",
                "Guter Abschluss-Impuls, bewusst auf das Erreichte statt auf das noch Fehlende schauen.",
                ["Worauf bist du stolz, wenn du auf die gemeinsame Zeit zurückblickst?",
                 "Was hat sich für das Kind durch dich bereits zum Besseren verändert?"],
                "Auch kleine Veränderungen sind oft ein großer Schritt für das Kind."),
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
