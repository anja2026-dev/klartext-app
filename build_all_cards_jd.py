#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baut alle 40 JD-Deck-Karten (Vorder-/Rückseite PNG) aus JD_Kartenkonzept_Uebersicht.md +
JD_Tipps_fuer_die_INGRA_Entwurf.md. Neu aufgebaut 27.07.2026, da die ursprüngliche Pipeline nie
ins klartext-app-Repo kopiert wurde."""
import os, glob, sys
sys.path.insert(0, os.path.dirname(__file__))
from build_card_jd import build_front, build_back

BILDER = "/sessions/kind-beautiful-ptolemy/mnt/klartext-app/bilder/jd/"
OUT = "/sessions/kind-beautiful-ptolemy/mnt/outputs/jd_karten_komplett/"
os.makedirs(OUT, exist_ok=True)

def find_image(nr):
    for pattern in (f"JD-{nr:02d}.jpg", f"JD-{nr:02d} *.jpg", f"JD-{nr:02d}.jpeg", f"JD-{nr:02d}.png"):
        files = sorted(glob.glob(os.path.join(BILDER, pattern)))
        if files:
            return files[0]
    return None

# nr: (titel, anleitung, [frage1, frage2], tipp_fuer_die_ingra)
CARDS = {
    1: ("Ich und die anderen",
        "Einsetzen bei Vergleich mit anderen (online/live), nicht bewerten, nur öffnen.",
        ["Mit wem vergleichst du dich am meisten?", "Was übersiehst du dabei an dir selbst?"],
        "Nicht korrigierend eingreifen, wenn der Vergleich negativ ausfällt. Erst mal nur benennen lassen, was da ist."),
    2: ("Was andere von mir denken",
        "Bei „Die denken bestimmt...“ nutzen, Unterschied Annahme/Fakt zeigen.",
        ["Woher weißt du, was die anderen wirklich denken?", "Was würdest du dir wünschen, dass sie denken?"],
        "Gut geeignet, wenn viele Gedanken um andere Menschen kreisen. Bei akuter sozialer Angst eher beruhigen als hinterfragen."),
    3: ("Meine Stärken sehen",
        "Für ruhige Momente, nicht in akuter Krise.",
        ["Worauf bist du an dir selbst stolz, auch wenn es klein ist?", "Wer würde dir noch eine Stärke von dir nennen?"],
        "Nicht in akuten Krisenmomenten einsetzen – dann wirkt die Frage nach Stärken schnell deplatziert. Für ruhige Gesprächsmomente reservieren."),
    4: ("Ein schlechter Tag ist kein schlechtes Ich",
        "Nach Rückschlägen, Trennung Tag/Person betonen.",
        ["Was ist heute schiefgelaufen – und was sagt das über dich als Person?", "Was würdest du einer befreundeten Person an deiner Stelle sagen?"],
        "Direkt nach einem Rückschlag einsetzbar. Hilft, Tagesform und Selbstbild zu trennen, bevor sich Selbstkritik festsetzt."),
    5: ("Alle wissen schon, was sie wollen – nur ich nicht",
        "Bei Berufswahl-/Zukunftsangst, Druck rausnehmen.",
        ["Woher kommt das Gefühl, du müsstest es schon wissen?", "Was interessiert dich gerade, auch wenn es kein Plan ist?"],
        "Eignet sich gut mit Abstand zu konkreten Bewerbungs- oder Entscheidungsfristen – dann wirkt der Druck weniger akut."),
    6: ("Erwartungen von zu Hause",
        "Vorsichtig, nicht wertend gegenüber Eltern.",
        ["Welche Erwartung spürst du am stärksten?", "Ist das auch dein eigener Wunsch, oder eher ein fremder?"],
        "Neutral bleiben, nicht gegen die Eltern positionieren, auch wenn der/die Jugendliche das erwartet."),
    7: ("Angst vorm Scheitern",
        "Bei Prüfungs-/Entscheidungsangst, Scheitern als Teil des Lernens.",
        ["Was wäre das Schlimmste, wenn es nicht klappt?", "Was würdest du danach als Nächstes tun?"],
        "Nicht direkt vor der Prüfung einsetzen – dann hilft kurzfristige Beruhigung mehr als Reflexion. Gut geeignet in ruhigeren Momenten davor oder danach."),
    8: ("Was, wenn ich meine Meinung später ändere?",
        "Bei Entscheidungsdruck, Entscheidungen sind nicht endgültig.",
        ["Was macht dir am meisten Angst an der Entscheidung?", "Was würde passieren, wenn du sie später änderst?"],
        "Hilfreich vor größeren Entscheidungen. Nicht erst einsetzen, wenn die Entscheidung schon gefallen ist."),
    9: ("Streit ohne Verlierer",
        "Direkt nach Konflikt, wenn beide ansprechbar sind.",
        ["Was wolltest du eigentlich erreichen im Streit?", "Was hättest du anders sagen können, ohne nachzugeben?"],
        "Erst einsetzen, wenn sich die Situation beruhigt hat – mitten im akuten Streit wirkt die Karte eher wie ein Verhör."),
    10: ("Wenn ich wütend bin, sage ich...",
         "Bei wiederkehrenden verbalen Eskalationen, Fokus Formulierung statt Gefühl unterdrücken.",
         ["Was sagst du normalerweise, wenn du wütend bist?", "Wie könntest du dasselbe sagen, ohne zu verletzen?"],
         "Fokus liegt auf der Formulierung, nicht auf dem Gefühl selbst. Wut nicht kleinreden, nur die Ausdrucksform gemeinsam anschauen."),
    11: ("Missverständnisse klären",
         "Bei Konflikt durch Fehlinterpretation, Fokus Nachfragen statt Annehmen.",
         ["Was hast du gedacht, was der andere meint?", "Was könntest du stattdessen fragen?"],
         "Besonders wirksam bei wiederkehrenden Missverständnissen mit derselben Person – Muster sichtbar machen."),
    12: ("Sich entschuldigen, ohne sich klein zu machen",
         "Bei Widerstand gegen Entschuldigung, Entschuldigung ≠ Schwäche.",
         ["Was fällt dir schwer am Entschuldigen?", "Wie könntest du dich entschuldigen und trotzdem zu dir stehen?"],
         "Nicht einsetzen, um eine Entschuldigung zu erzwingen. Die Karte öffnet, drängt aber nicht."),
    13: ("Nein sagen können",
         "Bei wiederkehrendem Nachgeben trotz Widerwillen.",
         ["Wann fällt dir Nein sagen besonders schwer?", "Was könnte passieren, wenn du es trotzdem sagst?"],
         "Gut geeignet, um ein wiederkehrendes Muster zu benennen, statt nur eine einzelne Situation zu bearbeiten."),
    14: ("Gruppendruck erkennen",
         "Bei Mitläufer-Verhalten/Gruppenzwang.",
         ["Wann hast du zuletzt etwas gemacht, das du eigentlich nicht wolltest?", "Was hätte dir geholfen, anders zu handeln?"],
         "Nicht moralisierend einsetzen – Ziel ist Verstehen des eigenen Verhaltens, nicht Bewertung."),
    15: ("Meine Grenze ist okay, auch wenn andere sie nicht verstehen",
         "Nach Zurückweisung wegen einer Grenze, bestärkend nicht rechtfertigend.",
         ["Wessen Reaktion beschäftigt dich gerade am meisten?", "Was würdest du dir selbst sagen, wenn du dich verstehst?"],
         "Bestärkend einsetzen, nicht um die Grenze im Nachhinein zu rechtfertigen oder zu verhandeln."),
    16: ('Wann sage ich "Stopp"?',
         "Vorsorglich einsetzen, nicht in akuter Grenzverletzung – das ist ein Moment für sofortiges Handeln, nicht für Reflexion.",
         ["Woran merkst du, dass eine Grenze erreicht ist?", "Wie klingt dein Stopp – laut, leise, deutlich?"],
         "Nicht in einer akuten Grenzverletzung einsetzen – dann braucht es sofortiges Eingreifen, keine Reflexion. Diese Karte ist für ruhige Momente zur Vorbereitung gedacht."),
    17: ("Vor der Prüfung: was hilft wirklich?",
         "In Prüfungsvorbereitung, konkrete machbare Ideen statt Druck.",
         ["Was hilft dir wirklich, wenn du nervös bist?", "Was tust du stattdessen, obwohl es nicht hilft?"],
         "Am besten mit zeitlichem Abstand zur Prüfung nutzen, damit die Ideen auch umsetzbar sind."),
    18: ("Wenn der Kopf voll ist",
         "Bei Gedankenkarussell/Überforderung, kein Lösungsdruck.",
         ["Was drängt sich gerade am meisten in deinem Kopf?", "Was könntest du für einen Moment beiseitelegen?"],
         "Keinen Lösungsdruck aufbauen – reicht, wenn die Gedanken einmal ausgesprochen werden."),
    19: ("Perfekt ist nicht das Ziel",
         "Bei Perfektionismus/Selbstkritik nach Ergebnissen.",
         ["Wie gut muss etwas sein, damit es für dich okay ist?", "Was verpasst du, wenn du auf perfekt wartest?"],
         "Nicht direkt nach einem konkreten Misserfolg einsetzen, wenn die Selbstkritik noch frisch ist – dann eher validieren."),
    20: ("Pause ist keine Schwäche",
         "Bei Erschöpfung trotz Erfolgsdruck, Pause als Strategie framen.",
         ["Wann hast du dir zuletzt eine echte Pause erlaubt?", "Was hält dich davon ab, öfter zu pausieren?"],
         "Pause als Strategie framen, nicht als Belohnung fürs Funktionieren – sonst bleibt der Leistungsdruck im Hintergrund bestehen."),
    21: ("Ernst genommen werden wollen",
         "Bei „das verstehst du noch nicht“-Erfahrungen.",
         ["Wann hast du dich zuletzt nicht ernst genommen gefühlt?", "Was würde dir zeigen, dass man dich ernst nimmt?"],
         "Erst mal nur zuhören – die Erfahrung nicht relativieren, auch wenn sie aus Erwachsenensicht nachvollziehbar wirkt."),
    22: ("Wenn Erwachsene nicht zuhören",
         "Bei Kommunikationsabbruch mit Eltern/Lehrkräften.",
         ["Woran merkst du, dass jemand nicht wirklich zuhört?", "Was könntest du anders sagen, damit es ankommt?"],
         "Fokus auf die eigene Formulierung legen, nicht auf eine Verteidigung der Erwachsenen."),
    23: ("Vertrauen aufbauen",
         "Bei belastetem Verhältnis zu Bezugsperson, langsamer Prozess.",
         ["Was bräuchtest du, um wieder mehr zu vertrauen?", "Was hast du selbst schon getan, um Vertrauen aufzubauen?"],
         "Als langsamer Prozess verstehen – keine schnelle Lösung erwarten oder einfordern."),
    24: ("Wie ich Hilfe holen kann, ohne mich zu schämen",
         "Bei Hilfe-Vermeidung aus Scham, Hilfe holen als Stärke framen.",
         ["Was hält dich davon ab, Hilfe zu holen?", "Wer wäre eine Person, die du fragen könntest?"],
         "Hilfe holen konsequent als Stärke framen, nie als letzten Ausweg."),
    25: ("Wer bin ich, wenn ich allein bin?",
         "Bei Fragen nach Identität abseits von Gruppenzugehörigkeit.",
         ["Was machst du gern, wenn niemand zuschaut?", "Was davon zeigst du auch anderen?"],
         "Eignet sich gut in ruhigen, unbeobachteten Momenten – nicht in der Gruppe oder unter Zeitdruck stellen."),
    26: ("Anders sein dürfen",
         "Bei Anpassungsdruck/Scham über eigene Interessen.",
         ["Was an dir ist anders als bei den meisten anderen?", "Wann fühlt sich das gut an, wann schwer?"],
         "Unterschiede wertfrei stehen lassen – nicht vorschnell normalisieren oder erklären wollen."),
    27: ("Was mir wichtig ist",
         "Für Werteklärung, z. B. nach Konflikten über Prioritäten.",
         ["Was ist dir wichtiger als du zeigst?", "Wofür würdest du auch mal unbequem werden?"],
         "Gut nach Konflikten über Prioritäten einsetzbar – hilft, eigene Werte von übernommenen zu unterscheiden."),
    28: ("Vergleich mit dem, wer ich mal war",
         "Bei Veränderungswunsch/Rückblick.",
         ["Was ist heute anders an dir als vor einem Jahr?", "Was davon war deine Entscheidung, was ist einfach passiert?"],
         "Rückblick wertschätzend halten – auch unfreiwillige Veränderungen dürfen als Veränderung stehen bleiben."),
    29: ("Handy weglegen können",
         "Bei Kontrollverlust-Gefühl, nicht moralisierend.",
         ["Wann merkst du, dass du eigentlich aufhören wolltest?", "Was passiert kurz bevor du wieder zum Handy greifst?"],
         "Nicht moralisierend einsetzen – Ziel ist Selbstbeobachtung, nicht Handyverzicht als Ziel an sich."),
    30: ("Online anders sein als offline",
         "Bei Diskrepanz Online-Auftritt/echtes Erleben.",
         ["Was zeigst du online, was du offline nicht zeigst?", "Was würde passieren, wenn beides gleicher wäre?"],
         "Ohne Bewertung der Online-Selbstdarstellung einsetzen – Unterschied benennen reicht, muss nicht aufgelöst werden."),
    31: ("Nachts noch wach wegen dem Handy",
         "Bei Schlafproblemen durch Bildschirmzeit.",
         ["Was hält dich nachts am Handy fest?", "Was würdest du morgen gern anders machen?"],
         "Halten die Schlafprobleme über längere Zeit an, ist das ein Fall für Eltern oder eine Fachperson – nicht für weitere Nachfragen durch die INGRA."),
    32: ("Wenn ein Kommentar wehtut",
         "Nach negativer Online-Erfahrung.",
         ["Was genau hat dich an dem Kommentar getroffen?", "Was hättest du gebraucht, direkt danach?"],
         "Zeitnah nach dem Erlebnis einsetzen, wenn möglich – validieren geht vor Einordnen."),
    33: ("Wenn sich zu Hause etwas ändert",
         "Bei Trennung/Umzug/neuer Familienkonstellation, sehr vorsichtig.",
         ["Was ist für dich gerade am schwersten an der Veränderung?", "Was ist gleich geblieben, trotz allem?"],
         "Besonders vorsichtig einsetzen und Tempo der/des Jugendlichen überlassen – bei akuter Belastung eher nicht vertiefen."),
    34: ("Zwischen zwei Zuhause",
         "Für Jugendliche im Wechselmodell.",
         ["Was ist an jedem der beiden Zuhause gut?", "Was nimmst du dir von einem Ort zum anderen mit?"],
         "Beide Zuhause wertfrei nebeneinander stehen lassen – keinen Ort besser oder schlechter dastehen lassen."),
    35: ("Neue Familienmitglieder akzeptieren",
         "Bei Patchwork/Stiefgeschwistern/neuen Bezugspersonen der Eltern.",
         ["Was fällt dir an der neuen Situation schwer?", "Wobei bräuchtest du mehr Zeit?"],
         "Zeit als legitimen Faktor anerkennen – Akzeptanz darf sich nicht erzwingen lassen."),
    36: ("Verantwortung für jüngere Geschwister",
         "Bei Überforderung durch Care-Aufgaben.",
         ["Was übernimmst du zu Hause, das eigentlich viel für dich ist?", "Wer weiß, wie viel das gerade ist?"],
         "Aufmerksam sein, ob die Verantwortung altersgerecht ist. Bei deutlicher Überforderung reicht Reflexion allein nicht – dann Rücksprache mit der für den Hilfeplan zuständigen Fachkraft halten."),
    37: ("Etwas Neues ausprobieren",
         "Bei Zurückhaltung vor neuen Aktivitäten/Freundschaften.",
         ["Was würdest du gern ausprobieren, wenn nichts schiefgehen könnte?", "Was ist der kleinste erste Schritt?"],
         "Kleine, machbare erste Schritte betonen – große Veränderungen wirken eher abschreckend."),
    38: ("Einen Fehler zugeben",
         "Nach eigenem Fehlverhalten.",
         ["Was ist das Schlimmste, das passieren könnte, wenn du es zugibst?", "Was würde es leichter machen?"],
         "Nicht einsetzen, um ein Geständnis zu erzwingen – die Karte unterstützt, wenn der Wunsch zuzugeben schon da ist."),
    39: ("Feedback annehmen, ohne einzuknicken",
         "Nach kritischem Feedback von Lehrkraft/Trainer:in.",
         ["Welcher Teil des Feedbacks stimmt, auch wenn's wehtut?", "Welcher Teil gehört nicht dir?"],
         "Mit etwas zeitlichem Abstand zum Feedback einsetzen, wenn die erste Reaktion abgeklungen ist."),
    40: ("Stolz auf den eigenen Weg",
         "Möglicher Abschluss-Impuls, Rückblick auf Wachstum.",
         ["Worauf bist du stolz, wenn du auf die letzten Monate schaust?", "Was möchtest du dir selbst dafür sagen?"],
         "Gut als Abschlusskarte einer Begleitung oder eines Zeitraums geeignet – bewusst als Rückblick, nicht als Bewertung rahmen."),
    41: ("Erstes Praktikum – und dann?",
         "Einsetzen vor oder während des ersten Praktikums/Werkstatttags, wenn Unsicherheit vor der neuen Situation im Vordergrund steht.",
         ["Was macht dir am meisten Sorgen vor dem Praktikum?", "Was würde dir helfen, es trotzdem zu versuchen?"],
         "Angst nicht kleinreden, nur öffnen. Nicht einsetzen, um die Sorge wegzureden."),
    42: ("Wenn die Arbeit nicht wie erwartet ist",
         "Bei Enttäuschung während/nach einem Praktikum, wenn die Realität nicht dem Wunschberuf entspricht.",
         ["Was ist anders, als du es dir vorgestellt hast?", "Was nimmst du trotzdem für dich mit?"],
         "Enttäuschung nicht wegreden, aber auch nicht als endgültiges Urteil über den ganzen Berufsweg stehen lassen."),
    43: ("Kritik bei der Arbeit annehmen",
         "Rückmeldung von Anleiter:innen/Chef:innen in der echten Arbeitswelt, wo Fehler direkte Konsequenzen haben können.",
         ["Was war schwer an der Rückmeldung?", "Was machst du beim nächsten Mal anders?"],
         "Anders als bei JD-39 (Feedback von Lehrkraft/Trainer:in): hier zählt, dass Fehler in der Arbeitswelt andere Folgen haben als in der Schule. Nicht relativieren, aber auch nicht dramatisieren."),
    44: ("Was ich wirklich gut kann",
         "Für Selbstwirksamkeitserleben durch praktische/handwerkliche Tätigkeit, besonders wertvoll für Jugendliche mit wenig schulischen Erfolgserlebnissen.",
         ["Bei welcher Aufgabe hast du gemerkt: Das kann ich richtig gut?", "Wer hat das auch schon an dir bemerkt?"],
         "Gut direkt nach einem gelungenen praktischen Arbeitsschritt einsetzbar, um Erfolg bewusst zu machen."),
    45: ("Wenn eine Beziehung endet",
         "Bei akutem Trennungsschmerz, keine schnellen Lösungen anbieten, Trennung nicht bewerten, auch wenn sie kurz war.",
         ["Was tut gerade am meisten weh?", "Was ist gleich geblieben, obwohl sich gerade so viel verändert hat?"],
         "Nicht relativieren („war doch nur kurz zusammen“) – der Schmerz ist unabhängig von der Beziehungsdauer real. Bei anhaltender starker Belastung nicht allein mit Reflexion arbeiten, Fachperson einbeziehen."),
    46: ("Verliebt sein zum ersten Mal",
         "Bei erster Beziehung/Verliebtheit, Aufregung und Unsicherheit gleichermaßen Raum geben, nicht belächeln.",
         ["Was macht dich an der Situation gerade am meisten unsicher?", "Was würdest du gern jemanden fragen, der/die schon mehr Erfahrung hat?"],
         "Nicht ins Elternhafte kippen („das geht schon vorbei“) – ernst nehmen, ohne zu dramatisieren oder zu verharmlosen."),
    47: ("Eifersucht, die alles auffrisst",
         "Bei starker Eifersucht, Gefühl benennen ohne zu bewerten, Fokus auf eigenes Erleben statt Kontrolle der anderen Person.",
         ["Was genau macht dir am meisten Angst, wenn du eifersüchtig bist?", "Was würde dir helfen, dich sicherer zu fühlen, ohne die andere Person zu kontrollieren?"],
         "Gefühl nicht moralisch bewerten, aber auf kontrollierendes Verhalten (Nachrichten checken, Ausfragen) behutsam hinweisen, wenn es zur Sprache kommt."),
    48: ("Wenn die Gefühle nicht erwidert werden",
         "Bei unerwiderter Liebe/Zurückweisung, Gefühl der Ablehnung validieren, bevor irgendetwas eingeordnet wird.",
         ["Was war der schwerste Moment, als du gemerkt hast, dass die Gefühle nicht erwidert werden?", "Was hilft dir, trotzdem zu dir zu stehen?"],
         "Validieren geht vor Einordnen (wie bei JD-32). Nicht vorschnell trösten („es gibt so viele andere“) – erst das Gefühl anerkennen. Bei Anzeichen von Rückzug oder starker Verzweiflung nicht allein lassen – Fachperson einbeziehen."),
    49: ("Was eine gute Freundschaft ausmacht",
         "Für ruhige Reflexionsmomente, nicht nur in Konfliktsituationen einsetzbar.",
         ["Was schätzt du an deiner besten Freundschaft am meisten?", "Was gibst du selbst in diese Freundschaft?"],
         "Guter positiver Gegenpol zu den Konflikt-Karten (JD-09 bis JD-12) – nicht nur bei Problemen an Freundschaft erinnern."),
    50: ("Für jemanden da sein, ohne sich zu verlieren",
         "Bei Überforderung durch die Bedürfnisse von Freund:innen.",
         ["Wie viel gibst du gerade in dieser Freundschaft, und wie viel bekommst du zurück?", "Woran würdest du merken, dass es zu viel wird?"],
         "Nicht in Richtung „diese Freundschaft beenden“ lenken – Ziel ist Balance finden, nicht Bewertung der Freundschaft."),
    51: ("Dazugehören, ohne sich zu verbiegen",
         "Bei Unsicherheit, ob man in eine Gruppe passt, oder dem Gefühl, sich anpassen zu müssen.",
         ["Bei wem fühlst du dich am meisten du selbst?", "Was müsstest du an dir ändern, um noch mehr dazuzugehören – und willst du das?"],
         "Anschlussfähig an JD-26 (Anders sein dürfen) – hier der Fokus auf die Gruppe statt auf das Individuum."),
    52: ("Wenn Freundschaften sich verändern",
         "Bei auseinanderdriftenden Freundschaften, z. B. nach Schulwechsel oder unterschiedlicher Entwicklung.",
         ["Was hat sich zwischen euch verändert?", "Was bleibt trotzdem wertvoll, auch wenn es nicht mehr wie früher ist?"],
         "Nicht als Scheitern rahmen – Veränderung von Freundschaften ist normal, nicht automatisch ein Verlust."),
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
                "total": 52}
        vorn = os.path.join(OUT, f"JD-{nr:02d}_Vorderseite.png")
        hinten = os.path.join(OUT, f"JD-{nr:02d}_Rueckseite.png")
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
