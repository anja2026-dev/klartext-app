#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Krisendeck – rendert alle 8 Karten (Vorder- und Rückseite) aus den in
Krisendeck_Kartentexte_Entwurf.md abgestimmten, aus FK-01–08 (App) gekürzten Inhalten."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from build_card_krisendeck import build_front, build_back

OUT_DIR = "/sessions/kind-beautiful-ptolemy/mnt/outputs/krisendeck_karten_komplett/"
os.makedirs(OUT_DIR, exist_ok=True)

CARDS = [
    dict(id_text="FK-01", icon="blitz", titel="Akute Eskalation",
         front_signale=["Schreien, Werfen, Schlagen/Treten",
                         "Totaler Kontrollverlust, keine Reaktion auf Ansprache"],
         situation="Kind im Ausnahmezustand – schreiend, werfend, schlagend. Fight-Modus, "
                    "rationale Kommunikation nicht möglich. Diese Karte gilt jetzt, nicht kLAR.",
         schritte=[
             "Sicherheitsabstand – 2 Armlängen, andere Kinder rausführen, seitwärts stehen",
             "Lehrkraft holen – „Ich brauche Unterstützung“, übernimmt Unterricht",
             "TK sofort informieren – parallel, nicht erst danach",
             "Ruhige Präsenz aus Distanz – Stimme senken, „Ich bin da, ich gehe nicht weg“",
             "Raum geben – nicht anfassen/festhalten (außer FK-04/FK-05 greift)",
             "Warten bis Sturm nachlässt – dann Angebot machen, keine sofortige Aufarbeitung",
         ],
         abgrenzung=[
             ("Sicherheitsdistanz halten", "Kind anfassen/festhalten"),
             ("TK sofort informieren", 'Warten bis "es vorbei ist"'),
             ("Ruhig, langsam sprechen", "Erklären, diskutieren, Fragen stellen"),
         ],
         verweis="Vollständige Fassung: FK-01 in der App."),

    dict(id_text="FK-02", icon="mute", titel="Shutdown",
         front_signale=["Kein Blickkontakt, leerer Blick",
                         "Keine Reaktion auf Ansprache, völlige Bewegungslosigkeit"],
         situation="Kind eingefroren, zieht sich zurück – kein Blickkontakt, keine Reaktion. "
                    "Freeze-Reaktion, kein Trotz. Das Kind „kann“ nicht antworten.",
         schritte=[
             "Ruhe herstellen – Reize reduzieren, Lärm/Blicke minimieren",
             "Keine Anforderungen, keine Fragen – ruhig in Abstand bleiben",
             "TK informieren – kurz und sachlich",
             "Anker anbieten – sanft, ohne Erwartung (Getränk hinstellen, ruhige Atmung)",
             "Warten – Geduld ist die Intervention, keine Zeitvorgaben",
             "Nach Rückkehr: leichte Orientierung geben – kurze Sätze",
         ],
         abgrenzung=[
             ("Reize minimieren, Ruhe schaffen", "Anfassen oder schütteln"),
             ("TK sofort informieren", "Auf Antwort bestehen"),
             ("Geduldig warten", "Humor/Ablenkung einsetzen"),
         ],
         verweis="Bei leerem Blick ohne jede Reaktion auf Namen → FK-07 Dissoziation prüfen. "
                 "Vollständige Fassung: FK-02 in der App."),

    dict(id_text="FK-03", icon="puls", titel="Panikattacke",
         front_signale=["Schnelle/flache Atmung, Herzrasen, Zittern",
                         "„Ich sterbe“ / „Ich kann nicht mehr“"],
         situation="Akute Angstreaktion – Herzrasen, Atemnot, Kontrollverlustgefühl. "
                    "Körperreaktion real, auch ohne objektive Gefahr. Geht von selbst vorbei.",
         schritte=[
             "Ruhige, sichere Umgebung schaffen – Sitzen lassen, Blicke anderer vermeiden",
             "Körperkontakt nur mit Einverständnis – fragen, nie erzwingen",
             "Orientierungssätze ruhig sprechen – „Du bist sicher, das geht vorbei“",
             "Atemführung anbieten – gemeinsam voratmen, Boxatmung",
             "TK informieren – vor allem bei erster/unbekannter Panikattacke",
             "5-4-3-2-1-Erdung anbieten, wenn ansprechbar",
         ],
         abgrenzung=[
             ("Ruhige Stimme, sichere Präsenz", '"Reiß dich zusammen"'),
             ("Gemeinsam atmen, voratmen", "In Tüte atmen lassen"),
             ("Orientierungssätze: „Du bist sicher“", "Nach Ursache fragen"),
         ],
         verweis="Vollständige Fassung: FK-03 in der App."),

    dict(id_text="FK-04", icon="warndreieck", titel="Fremdgefährdung",
         front_signale=["Schlagen/Kratzen/Beißen anderer, konkrete Drohungen",
                         "Gefährlicher Gegenstand in der Hand"],
         situation="Kind greift andere körperlich an oder bedroht konkret. Unmittelbare Gefahr "
                    "für Dritte – INGRA hat aktive Schutzpflicht.",
         schritte=[
             "Gefährdete Personen sofort schützen – aus Gefahrenbereich bringen",
             "Lehrkraft & Schulleitung sofort einschalten",
             "TK sofort informieren – parallel",
             "Eigene Sicherheit wahren – kein Eingreifen, das einen selbst gefährdet",
             "Bei Verletzungsgefahr: Notruf 112",
             "Deeskalation nur aus sicherem Abstand – kein Körperkontakt",
         ],
         abgrenzung=[
             ("Gefährdete Personen schützen", "Alleine eingreifen"),
             ("Schulleitung + TK sofort", "Intern regeln wollen"),
             ("Bei Verletzungsgefahr: Notruf 112", "Warten bis es schlimmer wird"),
         ],
         verweis="§ 8a SGB VIII prüfen, TK/Schulleitung entscheiden über weitere Schritte. "
                 "Vollständige Fassung: FK-04 in der App."),

    dict(id_text="FK-05", icon="pflaster", titel="Selbstverletzung",
         front_signale=["Sichtbare Kratzer/Wunden/Narben",
                         "Kind ritzt sich mit Gegenstand, schlägt Kopf gegen Wand"],
         situation="Kind verletzt sich selbst – Ritzen, Schlagen, Beißen. Zeichen für inneren "
                    "Schmerz, kein manipulatives Verhalten. Meldepflicht.",
         schritte=[
             "Ruhe bewahren – keine sichtbare Erschütterung zeigen",
             "Sicherheit schaffen – Gegenstände entfernen, ohne Aufhebens",
             "TK sofort informieren – Meldepflicht, keine Ausnahme",
             "Medizinische Versorgung bei Verletzungen, ggf. Notruf 112",
             "Würde wahren – kein Vorwurf, keine Warum-Fragen jetzt",
             "Ruhige Begleitung – bis TK/Eltern übernehmen",
         ],
         abgrenzung=[
             ("Ruhig, würdevoll reagieren", "Dramatisch reagieren/schimpfen"),
             ("TK sofort informieren", "Schweigen/intern lösen wollen"),
             ("Würde schützen", "Vor anderen Kindern ansprechen"),
         ],
         verweis="Meldepflicht gilt unabhängig von Bitte um Schweigen (§ 8a SGB VIII). "
                 "Vollständige Fassung: FK-05 in der App."),

    dict(id_text="FK-06", icon="laufen", titel="Weglaufen / Flucht",
         front_signale=["Kind bewegt sich schnell zur Tür",
                         "Taschen/Jacke packen im Unterricht, frühere Fluchtversuche"],
         situation="Kind verlässt unkontrolliert Schule/Klassenraum, nicht mehr beaufsichtigt. "
                    "Sicherheit hat Vorrang – ruhig und koordiniert handeln.",
         schritte=[
             "Lehrkraft sofort informieren – Klasse absichern",
             "Kind auf Sicht halten – ruhig folgen, nicht hetzen",
             "TK und Schulleitung sofort informieren",
             "Bei Verkehr/Gefahr: Sicherung hat Vorrang, ggf. Notruf 112",
             "Kind stoppen – wenn möglich durch ruhige Ansprache",
             "Rückkehr begleiten – ohne Vorwurf",
         ],
         abgrenzung=[
             ("Auf Sicht halten, ruhig folgen", "Schreien, hetzen, nachjagen"),
             ("Schulleitung + TK sofort", "Alleine suchen"),
             ("Ruhige Ansprache", "Sofortige Konsequenzen androhen"),
         ],
         verweis="Bei Nichtauffindbarkeit: Polizei 110. Vollständige Fassung: FK-06 in der App."),

    dict(id_text="FK-07", icon="nebel", titel="Dissoziation",
         front_signale=["Starrer, leerer Blick",
                         "Keine/verzögerte Reaktion, reagiert nicht auf eigenen Namen"],
         situation="Kind körperlich anwesend, innerlich abwesend – starrer Blick, keine "
                    "Reaktion. Automatische Schutzreaktion (Freeze), keine Absicht.",
         schritte=[
             "Ruhe bewahren, Umgebung sichern – reizarm, keine hektischen Bewegungen",
             "Ruhig ansprechen – sanft, repetitiv: „Ich bin hier, du bist sicher“",
             "TK unverzüglich informieren",
             "Sanfte Erdung anbieten – nicht erzwingen (Tischfläche fühlen)",
             "Präsenz halten – nicht alleine lassen, keine Personen wechseln",
             "Rückkehr langsam begleiten – keine sofortigen Fragen",
         ],
         abgrenzung=[
             ("Ruhige, konstante Präsenz", "Laut sprechen/schütteln"),
             ("TK sofort informieren", "Fragen/Erklärungen verlangen"),
             ("Reizarme Umgebung", "Viele Personen herbeirufen"),
         ],
         verweis="Abgrenzung zu Shutdown FK-02 und Hintergrund: siehe Handbuch. "
                 "Vollständige Fassung: FK-07 in der App."),

    dict(id_text="FK-08", icon="vulkan", titel="Meltdown",
         front_signale=["Schreien, Weinen, Zittern, Schlagen",
                         "Totaler Kontrollverlust ohne Ziel/Publikum"],
         situation="Totaler neurologischer Kontrollverlust durch Überlastung – kein Wutanfall, "
                    "kein Theater. Das Kind kann in diesem Moment nicht anders.",
         schritte=[
             "Sicherheit herstellen – andere Kinder raus, gefährliche Gegenstände weg",
             "Reize reduzieren – Licht dimmen, Lärm minimieren",
             "Abstand geben – nicht anfassen/festhalten (außer akute Gefahr)",
             "Ruhig bleiben – eigene Regulation zuerst",
             "Wenige Worte, keine Fragen/Erklärungen – „Ich bin da. Du bist sicher.“",
             "Recovery abwarten – kein Nachbesprechen in ersten 30–60 Minuten",
         ],
         abgrenzung=[
             ("Ruhig bleiben, wenige Worte", "Anfassen ohne Erlaubnis/erklären/bestrafen"),
             ("Selbstregulation zulassen (Schaukeln)", "Blickkontakt erzwingen"),
             ("Stille nach Meltdown ermöglichen", "Konsequenzen in der Situation ankündigen"),
         ],
         verweis="Neurologischer Notstand, häufig bei Autismus, aber nicht nur. Hintergrund: "
                 "siehe Handbuch. Vollständige Fassung: FK-08 in der App."),
]

def run():
    for card in CARDS:
        vorn = os.path.join(OUT_DIR, f"{card['id_text']}_Vorderseite.png")
        hinten = os.path.join(OUT_DIR, f"{card['id_text']}_Rueckseite.png")
        build_front(card, vorn)
        build_back(card, hinten)
        print(f"{card['id_text']} fertig")

if __name__ == "__main__":
    run()
