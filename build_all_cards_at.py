#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baut alle 24 AT-Deck-Karten (Vorder-/Rückseite PNG) aus AT_Kartenkonzept_Entwurf.md.
ENTWURF – Fachprüfung durch Autismus-Fachperson vor produktivem Einsatz weiterhin nötig."""
import os, glob, sys
sys.path.insert(0, os.path.dirname(__file__))
from build_card_at import build_front, build_back

BILDER = "/sessions/kind-beautiful-ptolemy/mnt/klartext-app/bilder/at/"
OUT = "/sessions/kind-beautiful-ptolemy/mnt/outputs/at_karten_komplett/"
os.makedirs(OUT, exist_ok=True)

def find_image(nr):
    for pattern in (f"AT-{nr:02d}.jpg", f"AT-{nr:02d} *.jpg", f"AT-{nr:02d}.jpeg", f"AT-{nr:02d}.png"):
        files = sorted(glob.glob(os.path.join(BILDER, pattern)))
        if files:
            return files[0]
    return None

# nr: (titel, anleitung, [frage1, frage2], tipp_fuer_die_ingra)
CARDS = {
    1: ("Was als Nächstes passiert",
        "Für den Einsatz vor einem Tagesablauf oder vor einem anstehenden Wechsel.",
        ["Was ist der nächste Schritt heute?", "Weißt du schon, was danach kommt, oder soll ich es dir zeigen?"],
        "Der nächste Schritt reicht oft aus – nicht den ganzen Tag auf einmal erklären."),
    2: ("Wenn sich der Plan ändert",
        "Wenn ein angekündigter Ablauf sich kurzfristig ändert.",
        ["Was ist heute anders als geplant?", "Was bleibt trotzdem gleich?"],
        "Zuerst sagen, was sich ändert, danach, was gleich bleibt – das gibt Halt."),
    3: ("Ein neuer Ort",
        "Vor dem ersten Besuch an einem neuen Ort (neues Klassenzimmer, neue Praxis).",
        ["Was weißt du schon über den neuen Ort?", "Was möchtest du vorher noch wissen?"],
        "Wenn möglich, den Ort vorher zeigen (Foto oder kurzer Besuch), nicht nur beschreiben."),
    4: ("Der Wechsel zwischen zwei Aktivitäten",
        "Für den Moment zwischen zwei Tätigkeiten, wenn der Wechsel schwerfällt.",
        ["Was machst du gerade?", "Was kommt als Nächstes, und wie viel Zeit bleibt dafür?"],
        "Eine klare Ankündigung („Noch 2 Minuten, dann...\") erleichtert den Wechsel mehr als eine plötzliche Aufforderung."),
    5: ("Was ist gerade zu laut",
        "Wenn Geräusche im Raum belastend wirken könnten.",
        ["Welches Geräusch stört dich gerade am meisten?", "Auf einer Skala von 1 bis 5 – wie laut ist es für dich gerade?"],
        "Die Zahl ernst nehmen, auch wenn der Raum objektiv leise wirkt."),
    6: ("Was ist gerade zu hell",
        "Bei möglicher Lichtempfindlichkeit (grelles Licht, Bildschirme, Sonne).",
        ["Ist das Licht hier gerade angenehm oder zu viel?", "Was würde helfen: weniger Licht, ein anderer Platz, oder etwas anderes?"],
        "Auch kleine Änderungen (Jalousie, Sitzplatz) können viel bewirken."),
    7: ("Zu viele Menschen auf einmal",
        "In vollen, lauten Räumen (Pausenhof, Kantine, Gruppenraum) einsetzbar.",
        ["Wie viele Menschen sind gerade zu viel für dich?", "Gibt es einen Platz hier, der weniger voll ist?"],
        "Die Anzahl an Menschen zu benennen macht das Gefühl greifbarer als „das ist mir zu viel\"."),
    8: ("Ein ruhiger Ort für mich",
        "Zur Vorbereitung eines Rückzugsorts, bevor er tatsächlich gebraucht wird.",
        ["Welcher Ort hier ist für dich am ruhigsten?", "Was müsste dort sein, damit du dich wohlfühlst?"],
        "Diesen Ort im Vorfeld gemeinsam festlegen, nicht erst in der akuten Überforderung suchen."),
    9: ("Was „Hallo sagen\" konkret bedeutet",
        "Zur expliziten Erklärung ungeschriebener sozialer Regeln, wörtlich statt vorausgesetzt.",
        ["Was machst du normalerweise, wenn du jemanden triffst?", "Was, denkst du, erwartet die andere Person?"],
        "Die Regel konkret benennen („Hallo sagen heißt: den Namen sagen oder winken\"), nicht als selbstverständlich voraussetzen."),
    10: ("Wenn jemand weiterredet, obwohl ich fertig bin",
         "Bei Gesprächssituationen, in denen das Gesprächsende schwer zu erkennen ist.",
         ["Woran erkennst du sonst, dass ein Gespräch zu Ende ist?", "Welcher Satz könnte dir helfen, das zu sagen?"],
         "Einen konkreten Satz gemeinsam üben (z. B. „Ich muss jetzt los\") statt nur „sei höflich\" zu sagen."),
    11: ("Was Blickkontakt für mich bedeutet",
         "Bei Druck, „in die Augen schauen\" zu müssen – ohne das einzufordern.",
         ["Ist Blickkontakt für dich angenehm oder anstrengend?", "Wie zeigst du stattdessen, dass du zuhörst?"],
         "Zuhören zeigt sich auch ohne Blickkontakt – das nicht einfordern, sondern anerkennen."),
    12: ("Eine Regel, die ich nicht verstehe",
         "Wenn eine soziale Regel unklar oder willkürlich wirkt.",
         ["Welche Regel ergibt für dich gerade keinen Sinn?", "Was würde dir helfen, sie zu verstehen?"],
         "Regeln konkret begründen können („Das ist so, weil...\") statt nur „das macht man so\" zu sagen."),
    13: ("Worüber ich am liebsten spreche",
         "Positiver Einstieg, macht das Spezialinteresse als Ressource sichtbar.",
         ["Worüber könntest du am längsten erzählen?", "Was macht dieses Thema für dich so gut?"],
         "Echtes Interesse zeigen, statt das Thema als Ablenkung zu behandeln."),
    14: ("Wenn andere mein Thema nicht mögen",
         "Bei Rückmeldungen anderer Kinder, die das Spezialinteresse als „zu viel\" empfinden.",
         ["Was sagen andere über dein Thema?", "Gibt es Momente, in denen du es lieber für dich behältst?"],
         "Nicht das Interesse infrage stellen, nur gemeinsam den passenden Moment dafür finden."),
    15: ("Was ich durch mein Thema gut kann",
         "Um Fähigkeiten sichtbar zu machen, die aus dem Spezialinteresse entstehen.",
         ["Was hast du durch dein Thema gelernt, das du sonst nicht könntest?", "Wo könnte dir das noch nützen?"],
         "Spezialinteressen bringen oft echtes Fachwissen und Ausdauer mit – das benennen."),
    16: ("Zeit für mein Thema bekommen",
         "Zur konkreten Planung von Zeiten für das Spezialinteresse im Alltag.",
         ["Wann im Tag hast du gerade Zeit für dein Thema?", "Wie viel Zeit wäre für dich genug?"],
         "Feste, verlässliche Zeiten wirken beruhigender als „irgendwann mal\"."),
    17: ("Woran ich merke, dass ich wütend bin",
         "Körperliche, konkrete Anzeichen von Wut erkennen lernen, statt abstrakt über „Wut\" zu sprechen.",
         ["Was macht dein Körper, wenn du wütend wirst? (z. B. Fäuste, heiß, laut)", "Wann hast du das zuletzt gemerkt?"],
         "Konkrete Körpersignale sind oft leichter zu erkennen als das Gefühlswort selbst."),
    18: ("Woran ich merke, dass ich müde oder überfordert bin",
         "Frühe, konkrete Anzeichen von Überforderung erkennen, bevor sie zu groß wird.",
         ["Was ist bei dir anders, wenn du überfordert bist? (z. B. Reden weniger, Bewegen mehr)", "Wer merkt das noch außer dir?"],
         "Diese Anzeichen gemeinsam aufschreiben – dann kann früher reagiert werden."),
    19: ("Was mir hilft, wenn ich aufgeregt bin",
         "Konkrete, bereits erprobte Strategien sammeln, statt neue vorzuschlagen.",
         ["Was hat dir letztes Mal geholfen, ruhiger zu werden?", "Was davon könntest du auch hier benutzen?"],
         "Auf bekannte, bereits funktionierende Strategien zurückgreifen, nicht in dem Moment etwas Neues ausprobieren."),
    20: ("Mein Platz auf dem Barometer gerade",
         "Direkte Verbindung zum Kind-Barometer (Grün/Gelb/Orange/Rot/Grau) – die Karte fragt konkret nach der aktuellen Farbe.",
         ["Welche Farbe passt gerade zu dir?", "Was müsste passieren, damit du eine Farbe weiter Richtung Grün kommst?"],
         "Das Barometer bewusst nutzen – es ist bereits ein konkretes, nicht-metaphorisches System."),
    21: ("Wie ich sage, dass ich eine Pause brauche",
         "Ein konkretes Signal/Wort für den Pausenbedarf einüben.",
         ["Welches Wort oder welche Geste könntest du benutzen, um eine Pause zu zeigen?", "Wer sollte dieses Signal kennen?"],
         "Ein einziges, immer gleiches Signal vereinbaren – zuverlässiger als wechselnde Formulierungen."),
    22: ("Was mir in der Pause hilft",
         "Konkrete Aktivitäten für die Pause sammeln, die tatsächlich beruhigen.",
         ["Was tust du in einer guten Pause?", "Was brauchst du dafür (Ort, Gegenstand, Zeit)?"],
         "Die benötigten Gegenstände (Kopfhörer, Kuscheltier, Buch) griffbereit halten."),
    23: ("Zurückkommen nach der Pause",
         "Den Übergang zurück in die Gruppe/Aktivität konkret vorbereiten.",
         ["Was hilft dir, wieder zurückzukommen?", "Wie viel Vorwarnung brauchst du, bevor die Pause endet?"],
         "Eine klare Ankündigung vor Ende der Pause erleichtert den Rückweg genauso wie den Rückzug."),
    24: ("Was ich über mich weiß, das mir hilft",
         "Guter Abschluss-Impuls – eigene Stärken/Strategien zusammenfassen.",
         ["Was weißt du inzwischen über dich, das dir im Alltag hilft?", "Wem könntest du das mal erklären?"],
         "Dieses Wissen ist wertvoll – auch für neue Bezugspersonen, die das Kind noch nicht kennen."),
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
        vorn = os.path.join(OUT, f"AT-{nr:02d}_Vorderseite.png")
        hinten = os.path.join(OUT, f"AT-{nr:02d}_Rueckseite.png")
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
