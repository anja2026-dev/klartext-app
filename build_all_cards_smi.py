#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baut alle 10 SMI-Deck-Karten (Vorder-/Rückseite PNG)."""
import os, glob, sys
sys.path.insert(0, os.path.dirname(__file__))
from build_card_smi import build_front, build_back

BILDER = "/sessions/kind-beautiful-ptolemy/mnt/klartext-app/bilder/smi/"
OUT = "/sessions/kind-beautiful-ptolemy/mnt/outputs/smi_karten_komplett/"
os.makedirs(OUT, exist_ok=True)

def find_image(nr):
    for pattern in (f"SMI-{nr:02d}.jpg", f"SMI-{nr:02d} *.jpg", f"SMI-{nr:02d}.jpeg", f"SMI-{nr:02d}.png"):
        files = sorted(glob.glob(os.path.join(BILDER, pattern)))
        if files:
            return files[0]
    return None

# nr: (titel, anleitung, [frage1, frage2], hinweis, quelle)
CARDS = {
    1: ("Rollen im Schatten",
        "Bei Mobbing gibt es selten nur Täter:in und Opfer. Salmivalli u. a. identifizierten weitere Rollen: Assistent:in, Verstärker:in, Verteidiger:in, Außenstehende. Wer diese Rollen erkennt, kann gezielter ansetzen als nur bei den zwei Hauptfiguren.",
        ["Welche Rolle nimmt welches Kind in dieser Klasse tatsächlich ein – nicht nur Täter:in/Opfer?", "Wen könnte ich gezielt als Verteidiger:in stärken?"],
        "Verstärker:innen (die lachen, zuschauen, Aufmerksamkeit geben) tragen die Dynamik oft mehr als der/die Täter:in selbst – dort anzusetzen wirkt oft schneller."),
    2: ("Die stille Mehrheit",
        "Die meisten Kinder in einer Klasse sind weder Täter:in noch Opfer – sie sehen zu, sagen nichts. Diese stille Mehrheit ist der größte Hebel, den eine Klasse hat.",
        ["Was würde die stille Mehrheit brauchen, um nicht mehr still zu bleiben?", "Gibt es schon ein sicheres, anonymes Meldesystem – kennt die Klasse es wirklich?"],
        "Schweigen ist selten Zustimmung. Oft ist es Angst, selbst zur Zielscheibe zu werden – das ernst nehmen, nicht als Gleichgültigkeit werten."),
    3: ("Den Teufelskreis durchbrechen",
        "Mobbing-Dynamiken laufen oft in sich verstärkenden Mustern. Lösungsfokussiert bedeutet: nicht die Ursache suchen, sondern den Kreislauf an einer Stelle unterbrechen.",
        ["An welcher Stelle im Kreislauf könnte eine kleine Veränderung die größte Wirkung haben?", "Was ist die eine Ausnahme – eine Situation, in der der Kreislauf schon mal nicht wie erwartet lief?"],
        "Nicht \"wer hat angefangen\" fragen. Fragen, was beim letzten Mal anders war, als es besser lief."),
    4: ("Transparenz schaffen",
        "Geheimhaltung schützt selten das betroffene Kind – sie schützt oft nur die Dynamik. Offenheit im Klassenrahmen (ohne Bloßstellung) nimmt dem Verhalten die Bühne.",
        ["Was würde sich verändern, wenn das Thema offen im Klassenrat besprochen würde – ohne Namen zu nennen?", "Wie kann ich Transparenz schaffen, ohne das betroffene Kind zusätzlich zu exponieren?"],
        "Transparenz heißt nicht Bloßstellung. Es geht ums Verhalten als Klassenthema, nicht um eine Anklage einzelner Namen vor der Gruppe."),
    5: ("Ressourcen der Klasse",
        "Jede Klasse hat schon Stärken im Umgang miteinander – Fairness-Regeln, positive Rituale, einzelne starke Verteidiger:innen. Diese Ressourcen aktivieren, statt nur Defizite zu bearbeiten.",
        ["Welche Stärke hat diese Klasse im Umgang miteinander schon gezeigt – auch wenn es nur einmal war?", "Wer in der Klasse könnte diese Stärke sichtbar vorleben?"],
        "Ressourcenorientierung heißt nicht, das Problem kleinzureden – es heißt, mit dem zu arbeiten, was schon da ist."),
    6: ("Cybermobbing erkennen",
        "Cybermobbing läuft oft unsichtbar für Erwachsene weiter, auch wenn die Situation in der Schule scheinbar beruhigt ist. Es braucht eigene Aufmerksamkeit, eigene Fragen.",
        ["Welche Hinweise auf digitale Fortsetzung habe ich bisher übersehen (Gruppenchats, Ausschluss aus Gruppen)?", "Wer könnte als Vertrauensperson für digitale Vorfälle benannt werden?"],
        "Cybermobbing endet nicht am Schultor. Nachfragen, ob \"es online weitergeht\" gehört mit dazu."),
    7: ("Die Eltern-Schule-Allianz",
        "Eltern erfahren oft spät oder gefiltert von Vorfällen. Eine funktionierende Allianz zwischen Schule und Elternhaus verhindert, dass Fronten statt Zusammenarbeit entstehen.",
        ["Wie informiere ich die Eltern so, dass sie Partner:in werden statt Gegner:in?", "Welche gemeinsamen nächsten Schritte kann ich konkret vorschlagen?"],
        "Eltern brauchen zuerst das Gefühl, ernst genommen zu werden – erst danach sind sie offen für gemeinsames Handeln."),
    8: ("Status-Check",
        "Sozialer Status in der Gruppe verschiebt sich ständig. Ein regelmäßiger, kurzer Status-Check verhindert, dass sich Dynamiken unbemerkt verfestigen.",
        ["Wie hat sich der soziale Status der beteiligten Kinder in den letzten Wochen verändert?", "Gibt es ein einfaches, wiederholbares Format für diesen Check (z. B. Soziogramm, kurze Einzelgespräche)?"],
        "Ein Status-Check muss nicht aufwendig sein – ein kurzes „Wie läuft's gerade mit …?\" alle paar Wochen reicht oft."),
    9: ("Humor als Werkzeug",
        "Humor kann Spannung lösen, aber auch verletzen. Der Unterschied liegt darin, ob er sich gegen jemanden richtet oder eine Situation gemeinsam entschärft.",
        ["Wann hilft ein humorvoller Kommentar, die Situation zu entspannen – und wann verstärkt er sie?", "Wie unterscheide ich \"mit jemandem lachen\" von \"über jemanden lachen\" im konkreten Moment?"],
        "Humor, der auf Kosten eines Kindes geht, ist kein Humor, sondern eine mildere Form der gleichen Dynamik."),
    10: ("Nachhaltigkeit sichern",
        "Eine Intervention, die einmal wirkt, reicht selten. Nachhaltige Veränderung entsteht, wenn die Klasse selbst erlebt, dass sie etwas bewirken kann.",
        ["Was hat die Klasse in dieser Situation selbst bewirkt – und wie mache ich das sichtbar?", "Wie halte ich die Wirkung über die akute Situation hinaus im Blick (Wiedervorlage, Nachfrage in 4 Wochen)?"],
        "Selbstwirksamkeitserleben trägt weiter als jede externe Ermahnung – die Klasse soll merken: \"Wir haben das verändert.\""),
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
        card = {"nr": nr, "titel": titel, "anleitung": anleitung, "fragen": fragen, "hinweis": tipp, "total": len(CARDS)}
        vorn = os.path.join(OUT, f"SMI-{nr:02d}_Vorderseite.png")
        hinten = os.path.join(OUT, f"SMI-{nr:02d}_Rueckseite.png")
        try:
            build_front(card, image_path, vorn)
            build_back(card, hinten)
            ok.append(nr)
        except Exception as e:
            fehler.append((nr, str(e)))
    print(f"Fertig: {len(ok)} Karten gebaut.")
    if uebersprungen: print("Übersprungen:", uebersprungen)
    if fehler: print("Fehler:", fehler)

if __name__ == "__main__":
    run()