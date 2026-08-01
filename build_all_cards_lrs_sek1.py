#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baut alle 10 LRS/Dyskalkulie-Sek1-Karten (Vorder-/Rückseite PNG).
Nummerierung: nr 1-7 = L-01..L-07 (LRS), nr 8-10 = D-01..D-03 (Dyskalkulie)."""
import os, glob, sys
sys.path.insert(0, os.path.dirname(__file__))
from build_card_lrs_sek1 import build_front, build_back

BILDER = "/sessions/kind-beautiful-ptolemy/mnt/klartext-app/bilder/lrs-sek1/"
OUT = "/sessions/kind-beautiful-ptolemy/mnt/outputs/lrs-sek1_karten_komplett/"
os.makedirs(OUT, exist_ok=True)

def id_text_for(nr):
    return f"L-{nr:02d}" if nr <= 7 else f"D-{nr-7:02d}"

def find_image(nr):
    idt = id_text_for(nr)
    for pattern in (f"{idt}.jpg", f"{idt} *.jpg", f"{idt}.jpeg", f"{idt}.png"):
        files = sorted(glob.glob(os.path.join(BILDER, pattern)))
        if files:
            return files[0]
    return None

# nr: (id_text, titel, anleitung, [frage1, frage2], hinweis)
CARDS = {
    1: ("L-01", "Buchstaben-Salat umdeuten",
        "Für Jugendliche, die sich für ihre Rechtschreibung schämen. Es geht darum, den Fehler vom Werturteil zu trennen.",
        ["Was denkst du über dich, wenn ein Wort falsch geschrieben ist?", "Was würdest du einem Freund/einer Freundin sagen, dem/der das passiert?"],
        "Mündlich vor Schriftlich: Bewerte in allen Fächern außer Deutsch das Wissen, nicht die Rechtschreibung. Ein Referat mit Fehlern in der PowerPoint ist trotzdem inhaltlich richtig."),
    2: ("L-02", "Nachteilsausgleich verstehen",
        "Viele Jugendliche empfinden Nachteilsausgleich als Stigma statt als Recht. Es hilft, ihn als das zu benennen, was er ist: ein Ausgleich, kein Vorteil.",
        ["Was denkst du, wenn du an deinen Nachteilsausgleich denkst – Erleichterung oder Scham?", "Wer sollte wissen, dass du einen Nachteilsausgleich hast – und wer nicht?"],
        "Struktur-Hilfen: Bei komplexen Schreibaufgaben auf einen Schritt-Plan verweisen (M3-15) – das entlastet zusätzlich zum formalen Ausgleich."),
    3: ("L-03", "Fremdsprachen-Frust",
        "Eine zweite Fremdsprache kann für Jugendliche mit LRS besonders belastend sein – zwei Schriftsysteme gleichzeitig zu meistern, verschärft die Schwierigkeit.",
        ["Was genau macht die Fremdsprache schwerer als Deutsch für dich?", "Was würde dir helfen, ohne dass du \"weniger\" machst als andere?"],
        "Multisensorik: Wissensvermittlung über Visualisierung (M3-17) und Audio-Medien anbieten – Vokabeln hören statt nur lesen entlastet spürbar."),
    4: ("L-04", "Wissen zeigen, nicht nur schreiben",
        "Schriftliche Leistungsnachweise messen oft mehr die Rechtschreibung als das Fachwissen. Andere Ausdrucksformen können echtes Wissen sichtbar machen.",
        ["In welcher Form könntest du dein Wissen zeigen, wenn Schreiben nicht das einzige Mittel wäre (mündlich, Skizze, Audio)?", "Welches Fach würde davon am meisten profitieren?"],
        "Mündlich vor Schriftlich gilt für alle Fächer außer Deutsch – das Fachwissen zählt, nicht die Rechtschreibleistung."),
    5: ("L-05", "Laptop als Werkzeug, nicht als Sonderweg",
        "Digitale Hilfsmittel (Rechtschreibkorrektur, Sprachausgabe) werden von Mitschüler:innen manchmal als \"Extrawurst\" wahrgenommen – dabei sind sie ein Werkzeug wie eine Brille.",
        ["Wie fühlt es sich an, den Laptop zu nutzen, wenn andere mit der Hand schreiben?", "Was würde helfen, damit sich das nicht wie ein Sonderweg anfühlt?"],
        "Eine kurze, sachliche Erklärung in der Klasse (\"so wie eine Brille\") nimmt oft mehr Druck als Schweigen darüber."),
    6: ("L-06", "Schreib-Tempo",
        "Unter Zeitdruck steigt die Fehlerquote oft zusätzlich. Zeitverlängerung ist keine Erleichterung der Aufgabe, sondern ein Ausgleich der Bearbeitungsgeschwindigkeit.",
        ["Was passiert mit deiner Konzentration, wenn die Zeit knapp wird?", "Wie viel zusätzliche Zeit würde wirklich helfen – und wofür genau?"],
        "Zeit-Management: Sichtbare Zeit (M3-21) nutzen, um Druck zu reduzieren, statt Zeit nur zuzuteilen ohne Transparenz für den Jugendlichen."),
    7: ("L-07", "Zukunftsdruck",
        "Jugendliche mit LRS sorgen sich oft besonders um Ausbildung, Noten und Zukunftschancen – die Sorge kann größer wirken als das eigentliche Problem.",
        ["Was genau befürchtest du für deine Zukunft wegen der LRS?", "Was weißt du über Menschen mit LRS, die trotzdem ihren Weg gemacht haben?"],
        "LRS betrifft die Rechtschreibung, nicht die Intelligenz oder die beruflichen Chancen – das explizit benennen hilft gegen Katastrophisieren."),
    8: ("D-01", "Mengen-Rätsel",
        "Für Jugendliche mit Dyskalkulie ist oft nicht das Rechnen selbst das Problem, sondern das Verständnis von Mengen und ihrer Beziehung zueinander.",
        ["Wann merkst du, dass Zahlen für dich \"nicht wie Bilder\" funktionieren, sondern nur wie Symbole?", "Was hilft dir, dir eine Menge wirklich vorzustellen?"],
        "Visualisierung (M3-17) einsetzen – Mengen als Bilder statt nur als Ziffern zeigen, entlastet das Zahlenverständnis direkt."),
    9: ("D-02", "Stress mit Zeit und Geld",
        "Uhrzeiten lesen, Geld zählen, Prozentrechnung im Alltag – diese alltäglichen Rechenanforderungen können bei Dyskalkulie besonders belasten, weil sie ständig vorkommen.",
        ["In welcher Alltagssituation macht dir das Rechnen am meisten Stress?", "Welches Hilfsmittel (Taschenrechner, App, Uhr mit Zahlen) würde diesen Stress konkret senken?"],
        "Der Einsatz von Hilfsmitteln im Alltag ist keine Ausrede, sondern ein Ausgleich – genau wie eine Brille beim Sehen."),
    10: ("D-03", "Der eigene Rechenweg",
        "Es gibt oft mehrere richtige Wege zu einem Rechenergebnis. Der eigene, vielleicht ungewöhnliche Weg zählt genauso, wenn er zum richtigen Ergebnis führt.",
        ["Wie rechnest du – auf welchem Weg kommst du meistens zum richtigen Ergebnis?", "Wann hat dir jemand gesagt, dein Weg sei \"falsch\", obwohl das Ergebnis stimmte?"],
        "Struktur-Hilfen: Bei mehrschrittigen Rechenaufgaben auf den Schritt-Plan (M3-15) verweisen – der eigene Weg darf dabei erhalten bleiben."),
}

def run(nur=None, ueberspringen=()):
    ok, fehler, uebersprungen = [], [], []
    numbers = nur if nur else sorted(CARDS)
    for nr in numbers:
        if nr in ueberspringen:
            uebersprungen.append(nr)
            continue
        idt, titel, anleitung, fragen, tipp = CARDS[nr]
        image_path = find_image(nr)
        if not image_path:
            fehler.append((nr, "Bild nicht gefunden"))
            continue
        card = {"nr": nr, "id_text": idt, "titel": titel, "anleitung": anleitung, "fragen": fragen, "hinweis": tipp, "total": len(CARDS)}
        vorn = os.path.join(OUT, f"{idt}_Vorderseite.png")
        hinten = os.path.join(OUT, f"{idt}_Rueckseite.png")
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