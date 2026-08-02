#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baut alle 24 ADHS-Deck-Karten (Vorder-/Rückseite PNG) aus ADHS_Kartenkonzept_Entwurf.md.
ENTWURF – Fachprüfung durch ADHS-Fachperson vor produktivem Einsatz weiterhin nötig."""
import os, glob, sys
sys.path.insert(0, os.path.dirname(__file__))
from build_card_adhs import build_front, build_back

BILDER = "/sessions/kind-beautiful-ptolemy/mnt/klartext-app/bilder/adhs/"
OUT = "/sessions/kind-beautiful-ptolemy/mnt/outputs/adhs_karten_komplett/"
os.makedirs(OUT, exist_ok=True)

def find_image(nr):
    for pattern in (f"ADHS-{nr:02d}.jpg", f"ADHS-{nr:02d} *.jpg", f"ADHS-{nr:02d}.jpeg", f"ADHS-{nr:02d}.png"):
        files = sorted(glob.glob(os.path.join(BILDER, pattern)))
        if files:
            return files[0]
    return None

# nr: (titel, anleitung, [frage1, frage2], tipp_fuer_die_ingra)
CARDS = {
    1: ("Wenn die Gedanken wegwandern",
        "Für Momente, in denen Konzentration schwerfällt, ohne das als Versagen zu werten.",
        ["Wohin wandern deine Gedanken am häufigsten ab?", "Was holt dich manchmal wieder zurück?"],
        "Abschweifende Gedanken sind kein Zeichen von Desinteresse – oft ein Zeichen, dass das Gehirn Reize gerade anders verarbeitet."),
    2: ("Wenn ich etwas dreimal lesen muss",
        "Bei Frustration über wiederholtes Lesen/Erklären-Müssen.",
        ["Was passiert in deinem Kopf, wenn du etwas mehrmals lesen musst?", "Gibt es eine Art, wie es dir leichter fällt (laut lesen, kürzere Abschnitte)?"],
        "Mehrmaliges Lesen ist keine Intelligenzfrage – oft hilft eine andere Aufnahmeform mehr als noch mehr Wiederholung."),
    3: ("Was mir hilft, dranzubleiben",
        "Ressourcenorientiert, bereits funktionierende Strategien sammeln.",
        ["Wann ist es dir zuletzt gut gelungen, bei einer Sache zu bleiben?", "Was war damals anders?"],
        "Auf bereits funktionierende Strategien zurückgreifen, statt ständig neue auszuprobieren."),
    4: ("Wenn ich etwas vergesse, das mir wichtig war",
        "Entlastend bei Vergessen wichtiger Dinge, nicht vorwurfsvoll.",
        ["Was vergisst du am häufigsten, obwohl es dir wichtig ist?", "Was könnte dir helfen, es trotzdem nicht zu vergessen?"],
        "Vergessen ist bei ADHS ein Arbeitsgedächtnis-Thema, kein Charakterzug – äußere Hilfen sind kein Versagen."),
    5: ("Wenn ich handle, bevor ich nachdenke",
        "Nach einer impulsiven Handlung, entlastend statt vorwurfsvoll einsetzbar.",
        ["Was ist zuletzt passiert, bevor du wirklich darüber nachdenken konntest?", "Was hättest du im Nachhinein gebraucht, um kurz innezuhalten?"],
        "Der Impuls kommt oft schneller als der Gedanke – das ist neurologisch, kein böser Wille."),
    6: ("Warten können",
        "Für Situationen mit Wartezeit (Schlange, Gesprächspause).",
        ["Was ist an Warten für dich am schwersten?", "Was hilft dir, eine Wartezeit auszuhalten?"],
        "Eine kleine Beschäftigung während des Wartens hilft oft mehr als „einfach durchhalten\"."),
    7: ("Dazwischenreden",
        "Bei häufigem Unterbrechen im Gespräch, ohne das als Unhöflichkeit zu werten.",
        ["Was passiert kurz bevor du dazwischenredest?", "Welches Zeichen könntest du stattdessen geben?"],
        "Ein vereinbartes Handzeichen kann helfen, den Gedanken festzuhalten, ohne ihn sofort auszusprechen."),
    8: ("Der Moment vor einer spontanen Entscheidung",
        "Rückblickend nach einer spontanen Entscheidung mit unerwünschter Folge einsetzbar.",
        ["Welche spontane Entscheidung fällt dir dazu ein?", "Was war der Gedanke direkt davor?"],
        "Rückblick statt Vorwurf – das schafft Bewusstsein für den nächsten ähnlichen Moment."),
    9: ("Wenn mein Körper sich bewegen muss",
        "Für den Bewegungsdrang, positiv statt als Störung gerahmt.",
        ["Wann merkst du, dass dein Körper sich bewegen muss?", "Welche Bewegung tut dir dabei am meisten gut?"],
        "Bewegungspausen sind keine Ablenkung vom Lernen, sondern oft eine Voraussetzung dafür."),
    10: ("Stillsitzen, wenn es erwartet wird",
         "Bei Situationen, die langes Stillsitzen verlangen.",
         ["Wo fällt dir Stillsitzen am schwersten?", "Was hilft dir, es trotzdem eine Weile zu schaffen?"],
         "Kleine erlaubte Bewegungen können großes Stillsitzen erst möglich machen."),
    11: ("Die Unruhe, die man nicht sieht",
         "Für innere Unruhe ohne sichtbare Hyperaktivität – wichtig, damit sie nicht übersehen wird.",
         ["Fühlst du dich manchmal unruhig, auch wenn du ruhig aussiehst?", "Wie würdest du das jemandem beschreiben, der es nicht sieht?"],
         "Innere Unruhe ist genauso echt wie sichtbare – auch wenn sie von außen nicht auffällt."),
    12: ("Was meinem Körper hilft, wenn er zu viel Energie hat",
         "Konkrete, erprobte Bewegungsstrategien sammeln.",
         ["Was tust du normalerweise, wenn du zu viel Energie hast?", "Wo könntest du das auch in der Schule/zu Hause einbauen?"],
         "Regelmäßige, eingeplante Bewegung wirkt oft mehr als das Warten auf den nächsten Ausbruch von Energie."),
    13: ("Den ganzen Tag „normal\" wirken",
         "Für Kinder/Jugendliche, die ihre Symptome tagsüber stark unterdrücken (Masking).",
         ["Musst du dich manchmal anstrengen, damit niemand merkt, wie du dich fühlst?", "Wie fühlt sich das am Ende des Tages an?"],
         "Masking kostet echte Kraft – das darf benannt werden, auch wenn es von außen nicht sichtbar ist."),
    14: ("Der Moment, wenn zu Hause alles rauskommt",
         "Für den bekannten „Nachmittags-Crash\" nach einem angestrengten Schultag.",
         ["Wie fühlt sich der erste Moment zu Hause nach der Schule an?", "Was würde dir direkt danach helfen?"],
         "Der Crash zu Hause ist oft ein Zeichen, dass sich das Kind dort sicher genug fühlt, um loszulassen – kein Erziehungsproblem."),
    15: ("Wie viel Kraft es kostet, mitzuhalten",
         "Wertschätzend die Anstrengung hinter dem äußeren Funktionieren sichtbar machen.",
         ["Was tust du im Alltag, das andere gar nicht bemerken, weil es so gut klappt?", "Was würdest du dir dafür gern mal sagen hören?"],
         "Gut funktionieren heißt nicht, dass es leicht ist – diese Anstrengung verdient Anerkennung."),
    16: ("Wer sieht, wie anstrengend das ist",
         "Zur Identifikation unterstützender Personen im Umfeld.",
         ["Wer in deinem Umfeld weiß, wie anstrengend manche Tage für dich sind?", "Wem könntest du das noch erzählen?"],
         "Mehr Menschen einzuweihen entlastet oft mehr, als man vorher denkt."),
    17: ("„Könntest du dich mehr anstrengen?\"",
         "Bei Rückmeldungen, die Anstrengung infrage stellen, obwohl das Kind sich bereits anstrengt.",
         ["Wie fühlt sich dieser Satz für dich an?", "Was würdest du der Person stattdessen gern erklären?"],
         "Dieser Satz übersieht oft die bereits vorhandene Anstrengung."),
    18: ("Warum Hausaufgaben länger dauern",
         "Entlastend bei langsamem Arbeitstempo bei Hausaufgaben.",
         ["Was dauert bei den Hausaufgaben am längsten?", "Was würde dir helfen, schneller reinzukommen?"],
         "Längere Bearbeitungszeit ist ein bekanntes, erklärbares Muster – kein Zeichen von zu wenig Fleiß."),
    19: ("Was mir hilft, eine Aufgabe zu Ende zu bringen",
         "Ressourcenorientiert, bereits funktionierende Abschluss-Strategien sammeln.",
         ["Was hat dir zuletzt geholfen, eine Aufgabe wirklich fertig zu machen?", "Was davon könntest du öfter nutzen?"],
         "Aufgaben in kleinere, klar abgeschlossene Schritte zu teilen hilft oft mehr als ein langes „Durchziehen\"."),
    20: ("Was ich brauche, um zu zeigen, was ich kann",
         "Zur konkreten Formulierung von Unterstützungsbedarf (z. B. Nachteilsausgleich), ohne Diagnostik-Anspruch der Karte selbst.",
         ["Was würde dir helfen, in einer Prüfung wirklich zu zeigen, was du kannst?", "Wer könnte dir dabei helfen, das einzurichten?"],
         "Unterstützung einzufordern ist kein Vorteil gegenüber anderen, sondern gleicht eine reale Hürde aus."),
    21: ("ADHS ist keine Charakterfrage",
         "Zentraler Reframing-Impuls – neurobiologisch statt moralisch einordnen.",
         ["Was hast du schon über ADHS gehört, das nicht stimmt?", "Was würdest du jemandem erklären, der ADHS nicht versteht?"],
         "Das Gehirn arbeitet anders, nicht schlechter – neurologisch, nicht erzieherisch bedingt."),
    22: ("Was ich an mir mag, seit ich mich besser verstehe",
         "Positiver Impuls nach einer Diagnose oder wachsendem Selbstverständnis.",
         ["Was verstehst du heute besser an dir als früher?", "Was magst du an dir, seit du das weißt?"],
         "Eine Diagnose kann entlasten, wenn sie als Erklärung statt als Etikett verstanden wird."),
    23: ("Wenn andere mich mit jemand anderem vergleichen",
         "Bei belastenden Vergleichen mit Geschwistern/Mitschüler:innen.",
         ["Mit wem wirst du am häufigsten verglichen?", "Was ist an deinem Weg anders, das der Vergleich nicht zeigt?"],
         "Vergleiche übersehen fast immer die unterschiedlichen Ausgangsbedingungen."),
    24: ("Worauf ich stolz bin, auch wenn es nicht einfach war",
         "Guter Abschluss-Impuls, wertschätzender Rückblick.",
         ["Worauf bist du stolz, obwohl es dir schwerer fiel als anderen?", "Was möchtest du dir selbst dafür sagen?"],
         "Guter Abschluss – bewusst als Rückblick lesen, nicht als Bewertung."),
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
                "total": 24}
        vorn = os.path.join(OUT, f"ADHS-{nr:02d}_Vorderseite.png")
        hinten = os.path.join(OUT, f"ADHS-{nr:02d}_Rueckseite.png")
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
