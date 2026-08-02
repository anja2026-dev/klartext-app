#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baut alle 33 TR-Deck-Karten (Vorder-/Rückseite PNG) aus TR_Kartenkonzept_Entwurf.md."""
import os, glob, sys
sys.path.insert(0, os.path.dirname(__file__))
from build_card_tr import build_front, build_back

BILDER = "/sessions/kind-beautiful-ptolemy/mnt/klartext-app/bilder/tr/"
OUT = "/sessions/kind-beautiful-ptolemy/mnt/outputs/tr_karten_komplett/"
os.makedirs(OUT, exist_ok=True)

def find_image(nr):
    for pattern in (f"TR-{nr:02d}.jpg", f"TR-{nr:02d} *.jpg", f"TR-{nr:02d}.jpeg", f"TR-{nr:02d}.png"):
        files = sorted(glob.glob(os.path.join(BILDER, pattern)))
        if files:
            return files[0]
    return None

# nr: (titel, anleitung, [frage1, frage2], tipp_fuer_dich)
CARDS = {
    1: ("Prozessbegleiter:in, nicht Vortragende:r",
        "Die Teilnehmenden bringen eigene Praxiserfahrung mit – die Aufgabe ist, sie mit dem System zu verknüpfen, nicht sie zu ersetzen.",
        ["Wo verfalle ich eher in den Vortrags-Modus als ins Prozessbegleiten?", "Was verändert sich, wenn ich eine Frage zurück in die Gruppe gebe statt sie selbst zu beantworten?"],
        "Du musst nicht jede Frage beantworten. Manchmal ist „Was denkt ihr dazu?“ die bessere Antwort."),
    2: ("Nicht bewerten – auch nicht implizit",
        "Weder Erziehungsstile noch Familien noch Kolleg:innen bewerten, auch nicht durch Tonfall oder Mimik.",
        ["Wann ist mir zuletzt eine Bewertung „rausgerutscht“, ohne dass ich es geplant hatte?", "Woran erkenne ich bei mir selbst, dass ich gerade werte statt beschreibe?"],
        "Ein wertfreier Tonfall ist trainierbar wie jede andere Fertigkeit – nicht Charaktersache."),
    3: ("Autorität über das System, nicht über „richtig“ und „falsch“",
        "Bei Unsicherheit, ob eine Frage noch „System“ oder schon „Supervision“ ist: „Was würde das KLAR-Modell hier vorschlagen?“ holt die Gruppe zurück zur Systemebene.",
        ["Wo verwische ich die Grenze zwischen System erklären und Praxis bewerten?", "Welche Rückfrage hilft mir, wieder auf die Systemebene zu wechseln?"],
        "Diese eine Rückfrage ist erlaubt, immer zur Hand zu haben – sie muss nicht spontan erfunden werden."),
    4: ("Erfahrungsbezug: An Vorhandenes andocken",
        "Erwachsene lernen am besten, wenn neues Wissen an vorhandene Erfahrung andockt – deshalb starten Einheiten mit einer Praxissituation, nicht mit Theorie.",
        ["Starte ich meine Einheiten wirklich mit einer Situation – oder rutsche ich doch in die Theorie zuerst?", "Welche Praxissituation aus meinem eigenen Alltag passt zum nächsten Modul?"],
        "Zwei aktuelle eigene Fallbeispiele parat zu haben ersetzt jede Theorie-Folie."),
    5: ("Relevanzbedürfnis: Nutzen vor Werkzeug",
        "Erwachsene wollen wissen, warum sie etwas lernen, bevor sie es lernen – den Nutzen erklären, bevor das Werkzeug erklärt wird.",
        ["Erkläre ich den Nutzen zuerst – oder springe ich zu schnell zum „Wie“?", "Wie würde ich den Nutzen dieses Werkzeugs in einem Satz erklären?"],
        "Ein Satz reicht. Wenn er nicht in einen Satz passt, ist er noch nicht klar genug."),
    6: ("Selbststeuerung: Wahlmöglichkeiten geben",
        "Erwachsene wollen als Mitgestaltende behandelt werden, nicht als Empfangende – Wahl anbieten, z. B. welches Fallbeispiel vertieft wird.",
        ["Wo könnte ich der Gruppe echte Wahl anbieten, wo tue ich es noch nicht?", "Was passiert mit der Energie im Raum, wenn ich eine Wahl anbiete statt vorzugeben?"],
        "Schon eine kleine Wahl reicht, um aus Empfangenden Mitgestaltende zu machen."),
    7: ("Der Lernzyklus nach Kolb",
        "Erleben → Reflektieren → Verallgemeinern → Anwenden. Jede Einheit sollte diesen Zyklus mindestens einmal durchlaufen.",
        ["Welche der vier Phasen überspringe ich am ehesten?", "Wie sieht der Zyklus in meiner letzten Einheit konkret aus – wo hakt er?"],
        "Fehlt eine Phase meist die Reflexion („Was ist aufgefallen?“) – das ist der Schritt, der am leichtesten unter Zeitdruck wegfällt."),
    8: ("Forming: Struktur und Sicherheit geben",
        "Die Gruppe ist zurückhaltend, abwartend – klare Struktur und Sicherheit sind jetzt die Aufgabe.",
        ["Woran erkenne ich Forming im Raum?", "Was gibt mir selbst in dieser Phase Sicherheit?"],
        "Zurückhaltung am Anfang ist kein schlechtes Zeichen – sie gehört zur Phase."),
    9: ("Storming: Kritik einordnen statt verteidigen",
        "Erste Widersprüche, Kritik am System („bei uns geht das nicht“) – normal und produktiv, nicht persönlich nehmen.",
        ["Wie reagiere ich innerlich auf Systemkritik – verteidige ich reflexhaft?", "Welche Gegenfrage hilft mir, von genereller Ablehnung zu einem konkreten Detail zu kommen?"],
        "Storming ist ein Zeichen, dass die Gruppe sich ernsthaft mit dem System auseinandersetzt – nicht, dass etwas schiefläuft."),
    10: ("Norming: Gemeinsame Arbeitsweise entstehen lassen",
         "Die Gruppe einigt sich auf gemeinsame Arbeitsweisen – hier entsteht echtes Systemverständnis.",
         ["Woran merke ich, dass die Gruppe in Norming übergeht?", "Wo kann ich jetzt bewusst Raum lassen, statt weiter zu strukturieren?"],
         "Norming ist der Moment, in dem weniger Eingreifen oft mehr bringt."),
    11: ("Performing: Zurücknehmen können",
         "Die Gruppe arbeitet eigenständig mit dem Material – hier kann sich die Trainer:in stärker zurücknehmen.",
         ["Fällt es mir leicht, mich zurückzunehmen, wenn die Gruppe eigenständig arbeitet?", "Was hindert mich daran, loszulassen?"],
         "Zurücknehmen ist eine aktive Entscheidung, kein Kontrollverlust."),
    12: ("Format und Zielgruppe klären",
         "Teilnehmerzahl und Vorerfahrung vorab klären (Erstschulung vs. Auffrischung), passendes Format wählen.",
         ["Kenne ich die Vorerfahrung meiner Gruppe wirklich, bevor ich plane?", "Passt das gewählte Format tatsächlich zur Gruppengröße und zum Vorwissen?"],
         "Eine kurze Vorab-Nachfrage bei der Anmeldung spart am Schulungstag viel Zeit."),
    13: ("Raum und Technik vorbereiten",
         "Gruppentische statt Reihenbestuhlung, genug Platz für Rollenspiele, Zugänge und Logins vorab geprüft.",
         ["Wie oft scheitert bei mir eine gute Übung an einem ungeeigneten Raum statt am Inhalt?", "Was prüfe ich inzwischen routinemäßig, was ich früher vergessen habe?"],
         "15 Minuten vorher Technik testen ist keine Formalität – es ist die günstigste Investition des ganzen Tages."),
    14: ("Eigene Praxisbeispiele parat haben",
         "Mindestens zwei aktuelle Fallbeispiele aus der eigenen Praxis, passend zur Zielgruppe, vorbereitet mitbringen.",
         ["Wie aktuell sind meine Standard-Fallbeispiele wirklich noch?", "Welches neue Beispiel könnte ich beim nächsten Mal ergänzen?"],
         "Fallbeispiele altern schneller, als man denkt – regelmäßig auffrischen."),
    15: ("Am Tag selbst: die letzten 15 Minuten",
         "Technik testen, Namensschilder/Vorstellungsrunde bei größeren Gruppen, Pausenzeiten sichtbar ankündigen.",
         ["Was von diesen letzten 15 Minuten überspringe ich am ehesten, wenn ich selbst gestresst bin?", "Wie merkt die Gruppe, dass ich gut vorbereitet bin, bevor ich ein Wort gesagt habe?"],
         "Sichtbare Pausenzeiten reduzieren Unruhe – ein kleiner Aufwand mit großer Wirkung."),
    16: ("Rollenspiel mit Kartenwechsel",
         "Zwei TN spielen eine M3-Situation nach. Nach 2 Minuten Stopp, Karte tauschen, gleiche Szene mit anderem Werkzeug fortsetzen – zeigt die Wirkung von Werkzeugwahl konkret.",
         ["Bei welchem Thema würde diese Methode besonders viel zeigen?", "Was mache ich, wenn sich niemand freiwillig meldet?"],
         "Freiwillige finden sich leichter, wenn du selbst die erste Rolle kurz vorspielst."),
    17: ("Karten-Sortieraufgabe",
         "Gedruckte Kartenausschnitte in Kleingruppen nach Barometer-Farbe sortieren lassen – macht das Farbmodell greifbar, bevor es digital genutzt wird.",
         ["Für welche Gruppe wäre die haptische Version hilfreicher als die digitale?", "Wie viel Zeit brauche ich realistisch für diese Übung?"],
         "Ausgedruckte Kartenausschnitte griffbereit zu haben lohnt sich – nicht erst am Schulungstag improvisieren."),
    18: ("Fishbowl-Diskussion",
         "Innenkreis diskutiert eine Grauzone, Außenkreis hört zu und schreibt Fragen auf Karten – gut für Recht-/Grenzfragen-Themen.",
         ["Welche Grauzone aus meiner eigenen Praxis würde eine gute Fishbowl-Frage abgeben?", "Wie moderiere ich, ohne selbst zu viel Raum einzunehmen?"],
         "Die Außenkreis-Fragen am Ende laut vorlesen zu lassen bindet auch die Zuhörenden aktiv ein."),
    19: ("Stiller Galeriegang",
         "Ausgedruckte Fallbeispiele an den Wänden, Teilnehmende gehen still herum und schreiben Post-its mit „Welches Modul passt?“ – aktiviert vor der Theorie-Einheit.",
         ["Wann in meinem Ablauf würde stille Einzelarbeit der Gruppe mehr bringen als Plenumsdiskussion?", "Wie gehe ich mit der ungewohnten Stille im Raum um?"],
         "Stille ist bei dieser Methode gewollt – nicht vorschnell auflösen."),
    20: ("„Das funktioniert bei uns nicht“ – Systemkritik auffangen",
         "Häufig in der Storming-Phase. Nicht verteidigen, sondern konkretisieren: „Welcher Teil kostet dir konkret Zeit?“",
         ["Wie reagiere ich im ersten Moment auf pauschale Kritik?", "Welche Rückfrage funktioniert bei mir zuverlässig, um zu konkretisieren?"],
         "Die Gegenfrage muss nicht klug sein, nur konkret – „Was genau kostet dich Zeit?“ reicht meistens."),
    21: ("Dominante Teilnehmende einbinden",
         "Direkt, aber wertschätzend würdigen und gleichzeitig Raum für andere öffnen; strukturell vorbeugen mit Kleingruppenarbeit statt offenem Plenum.",
         ["Kenne ich meine Gruppe vorab gut genug, um das strukturell vorzubeugen?", "Wie formuliere ich Anerkennung, ohne die Person zu beschämen?"],
         "„Danke, das ist ein wichtiger Punkt – ich möchte gern auch hören, wie es bei anderen aussieht“ funktioniert fast immer."),
    22: ("Emotional belastende Fallbeispiele auffangen",
         "Bei Trauma-/Missbrauchs-/Mobbing-Themen kann eigene Betroffenheit hochkommen. Du bist Trainer:in, nicht Therapeut:in.",
         ["Wo ist für mich persönlich die Grenze zwischen Auffangen und Therapieren?", "Wie merke ich rechtzeitig, dass ich selbst emotional mitgehe?"],
         "„Das klingt schwer – möchtest du in der Pause kurz mit mir sprechen?“ reicht als Sofortreaktion völlig aus."),
    23: ("Technische Probleme: Offline-Alternative",
         "Immer eine Offline-Alternative vorbereitet haben; nie länger als 3–4 Minuten live vor der Gruppe debuggen.",
         ["Habe ich für die wichtigsten Module wirklich eine Offline-Version griffbereit?", "Wie gehe ich mit dem eigenen Stress um, wenn Technik ausfällt?"],
         "Die 3–4-Minuten-Regel schützt vor allem die Gruppe vor Leerlauf – nicht dich vor Frustration."),
    24: ("Feedback während der Übung, nicht nur danach",
         "Feedback ist einer der stärksten Hebel für Lernerfolg – vorausgesetzt, es beschreibt konkret die Lücke zwischen aktuellem Stand und Ziel.",
         ["Gebe ich laufend kurzes Feedback, oder sammle ich es bis zum Schluss?", "Wie konkret ist mein Feedback wirklich – beschreibt es die Lücke oder nur „gut/nicht gut“?"],
         "Ein Satz während der Übung wirkt oft mehr als eine ausführliche Rückmeldung am Ende."),
    25: ("Konkret fragen statt „Wie fandet ihr's?“",
         "Statt allgemeiner Fragen konkret fragen: „Welches Werkzeug nimmst du morgen als Erstes mit in die Praxis?“",
         ["Welche Frage stelle ich standardmäßig – ist sie konkret genug?", "Was würde sich ändern, wenn ich nach dem ersten Schritt morgen statt nach der Zufriedenheit fragen würde?"],
         "Eine konkrete Abschlussfrage liefert dir gleichzeitig ein besseres Bild vom Lernerfolg als jede Zufriedenheitsfrage."),
    26: ("Schriftlich und anonym ermöglichen",
         "Mündliches Feedback in der Gruppe ist oft sozial erwünscht gefärbt – schriftliche, anonyme Feedbackbögen zusätzlich anbieten.",
         ["Wie unterscheidet sich das mündliche vom schriftlichen Feedback, das ich bekomme?", "Nutze ich die anonymen Rückmeldungen tatsächlich aus, oder sammeln sie sich nur an?"],
         "Schon ein kurzer anonymer Zettel am Ende bringt oft ehrlichere Rückmeldungen als die Plenumsrunde."),
    27: ("Checkliste nach der Schulung",
         "Feedbackbögen auswerten und dokumentieren, Zertifikate ausstellen, offene Fragen der Gruppe an die TK-Koordination weiterleiten.",
         ["Wie zügig nach der Schulung erledige ich diese Punkte üblicherweise?", "Was bleibt bei mir am ehesten liegen?"],
         "Direkt am selben Tag noch 10 Minuten für die Nachbereitung einplanen, bevor der Alltag wieder übernimmt."),
    28: ("Muster über mehrere Durchführungen erkennen",
         "Eine kurze private Notiz pro Durchführung – nach 3–4 Durchführungen zeichnen sich Muster ab, welche Kapitel überarbeitet werden sollten.",
         ["Führe ich diese Notizen bereits, oder verlasse ich mich auf mein Gedächtnis?", "Welches Muster ist mir in den letzten Schulungen schon aufgefallen?"],
         "Drei Stichpunkte pro Durchführung reichen – das muss kein aufwendiges Protokoll sein."),
    29: ("Offene Fragen weiterleiten",
         "Fragen der Gruppe, die über die Schulung hinausgehen, gehören an die TK-Koordination weitergeleitet, nicht spontan selbst beantwortet.",
         ["Wo beantworte ich eine Frage lieber selbst, obwohl sie eigentlich weitergeleitet gehört?", "Was hindert mich daran, „Das kläre ich und melde mich“ zu sagen?"],
         "„Das kläre ich und melde mich“ ist eine vollständige, professionelle Antwort – auch ohne sofortige Lösung."),

    # Block I – Moderne Fortbildungslandschaft (4 Karten, ergänzt 30.07.2026)
    30: ("Energie vor dem Bildschirm halten",
         "Für Online- oder Hybrid-Schulungen, in denen die übliche Raum-Energie fehlt.",
         ["Wie merke ich online, dass die Gruppe müde oder abwesend wird – anders als im Raum?",
          "Welche eine Methode aus meinem Methodenkoffer funktioniert auch am Bildschirm?"],
         "Kurze, bewusste Sprechpausen wirken online noch stärker als im Raum – Stille ist kein totes Zeichen der Technik."),
    31: ("Skepsis auf Trägerebene ernst nehmen",
         "Für Situationen, in denen der Widerstand nicht von den Kursteilnehmenden kommt, sondern von der Leitungsebene des Trägers, der KLARTEXT gerade erst einführt.",
         ["Wessen Skepsis begegnet mir hier eigentlich – die der Gruppe oder die der Organisation dahinter?",
          "Was würde diese Leitungsebene brauchen, um Vertrauen in das System aufzubauen?"],
         "Institutionelle Skepsis ist selten gegen dich persönlich gerichtet – meist geht es um Kontrollverlust über einen neuen Prozess."),
    32: ("Nach dem Workshop wieder auftanken",
         "Für die Zeit nach einem intensiven 1- oder 2-Tages-Workshop, wenn belastende Fallbeispiele nachwirken. Erweitert TR-22 um die Phase danach.",
         ["Was von diesem Workshop trägst du noch mit dir herum, obwohl er vorbei ist?",
          "Was hilft dir persönlich, nach einem intensiven Trainingstag wirklich abzuschalten?"],
         "Psychohygiene nach belastenden Fallbeispielen ist kein Luxus, sondern Voraussetzung für die nächste gute Schulung."),
    33: ("Heterogene Vorbildung als Ausgangspunkt",
         "Für Trainingsgruppen mit sehr unterschiedlichen Vorerfahrungen, Ausbildungswegen oder kulturellen Hintergründen innerhalb der INGRA-Teams.",
         ["Wie unterschiedlich ist die Vorbildung in meiner aktuellen Gruppe wirklich?",
          "Wo passe ich mein Beispiel oder meine Sprache noch nicht an diese Unterschiede an?"],
         "Heterogenität ist kein Störfaktor, der ausgeglichen werden muss – sie ist der Ausgangspunkt guter Erwachsenenbildung."),
}

SYSTEMFRAGEN = {
    2: ("SKALIERUNGSFRAGE", "Auf einer Skala von 1–10 – wie bewertungsfrei war meine letzte Schulung wirklich?"),
    6: ("HANDLUNGSFRAGE", "Welche eine Entscheidung überlasse ich beim nächsten Training bewusst der Gruppe?"),
    9: ("ZIRKULÄRE FRAGE", "Was würde eine skeptische Teilnehmerin sagen, was sie an diesem Widerstand eigentlich schützen will?"),
    16: ("HANDLUNGSFRAGE", "Wann setze ich diese Methode das nächste Mal konkret ein?"),
    22: ("HANDLUNGSFRAGE", "Welchen einen Satz halte ich mir für diese Situation griffbereit?"),
    28: ("SKALIERUNGSFRAGE", "Auf einer Skala von 1–10 – wie systematisch werte ich meine eigenen Schulungen bisher aus?"),
    30: ("HANDLUNGSFRAGE", "Welche Online-Moderationstechnik nehme ich mir für die nächste Hybrid-Schulung konkret vor?"),
    31: ("ZIRKULÄRE FRAGE", "Was würde eine skeptische Trägerleitung sagen, was sie mit ihrer Zurückhaltung eigentlich schützen will?"),
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
                "systemfrage": SYSTEMFRAGEN.get(nr), "total": len(CARDS)}
        vorn = os.path.join(OUT, f"TR-{nr:02d}_Vorderseite.png")
        hinten = os.path.join(OUT, f"TR-{nr:02d}_Rueckseite.png")
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
