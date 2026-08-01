#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Werkzeugkarten-Deck – rendert alle 20 Karten (8 Situationen + 12 Werkzeuge) aus den
gekürzten, aus M3-01–20 (App) abgeleiteten Inhalten."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from build_card_werkzeug import build_front, build_back

OUT_DIR = "/sessions/kind-beautiful-ptolemy/mnt/outputs/werkzeug_karten_komplett/"
os.makedirs(OUT_DIR, exist_ok=True)

CARDS = [
    # ═══════════════ SITUATIONEN (M3-01–08) ═══════════════
    dict(id_text="WZ-01", typ="situation", icon="sun", titel="Kind kommt aufgewühlt an",
         front_kontext="Gelb bis Orange – typischer Bereich",
         lead="Kind kommt morgens sichtlich aufgewühlt an – noch bevor der Tag beginnt.",
         schritte=[
             "Kontakt herstellen – ruhig, ohne Druck, kein „Hallo-Hallo“",
             "Barometer abfragen – ohne Worte, Farbe zeigen lassen",
             "Ankommen ermöglichen – 5 Minuten, bei Orange keine Aufgaben",
             "Übergabeinfo an Lehrkraft – kurzes Signal, LK hält den Unterricht",
             "Regulationstool wählen – was heute passt, nicht was immer passt",
         ],
         tipp="Kein Kind kommt absichtlich aufgewühlt. Was draußen passiert ist, landet im "
              "Körper – und braucht Zeit.",
         werkzeuge="Atemanker (M3-09) · Mini-Pause (M3-14)",
         brainy="In dieser Situation zuerst regulieren – dann alles andere."),

    dict(id_text="WZ-02", typ="situation", icon="ban", titel="Kind verweigert Arbeit",
         front_kontext="Gelb bis Orange – typischer Bereich",
         lead="Kind verweigert eine Aufgabe – meist steckt mehr dahinter als Trotz.",
         schritte=[
             "Nicht sofort einfordern – 10-15 Sekunden ruhig daneben sein",
             "Barometer checken – Angst, Überforderung, Stress oder Hunger statt Trotz",
             "Aufgabe verkleinern – nur den ersten Satz, nur den Namen schreiben",
             "Anderen Zugang anbieten – mündlich statt schriftlich, gemeinsam statt allein",
             "Bei anhaltendem Rot: Aufgabe beenden – „Das machen wir später“, LK/TK informieren",
         ],
         tipp="Nie „Warum machst du das nicht?“ – sondern „Was macht es gerade schwer?“",
         werkzeuge="Schritt-Plan (M3-15)",
         brainy="In dieser Situation zuerst regulieren – dann alles andere."),

    dict(id_text="WZ-03", typ="situation", icon="bolt", titel="Kind eskaliert – Wutausbruch",
         front_kontext="Orange bis Rot – typischer Bereich",
         lead="Kind ist im vollen Wutausbruch – schreiend, werfend, außer sich.",
         schritte=[
             "Sofort Ruhe ausstrahlen – nicht spiegeln, Stimme tief und langsam",
             "Anderen Kindern Sicherheit geben – Abstand schaffen, ggf. rausschicken",
             "Abstand halten, präsent bleiben – 1-2 Meter, „Ich bin hier“, mehr nicht",
             "Kein Gespräch, keine Erklärungen – das Gehirn ist jetzt nicht zugänglich",
             "Nach dem Sturm: kLAR einleiten – Rückzugsort, Atemübung, dann kurzes Gespräch",
         ],
         tipp="Ein explodierendes Kind beruhigst du nicht mit Worten – nur mit deiner eigenen Ruhe.",
         werkzeuge="kLAR-Modell · Feuerwehrkarten (bei Eskalation)",
         brainy="In dieser Situation zuerst regulieren – dann alles andere."),

    dict(id_text="WZ-04", typ="situation", icon="snowflake", titel="Kind zieht sich zurück – Freeze",
         front_kontext="Grau bis Orange – typischer Bereich",
         lead="Kind wirkt wie abwesend, reagiert nicht – das ist maximaler Stress, kein Desinteresse.",
         schritte=[
             "Erkennen, nicht verwechseln – Freeze wirkt wie Sturheit, ist aber Notbetrieb",
             "Keine Anforderungen, kein Reden – kein „Was ist los?“",
             "Einfach da sein – sanfte Präsenz, ruhig atmen",
             "Orientierungsanker anbieten – „Wir sitzen hier. Du bist sicher.“ Kurze Sätze",
             "Langsam auftauen mit Tool – Igel-Ball, Wasser, Kopfhörer",
         ],
         tipp="Freeze ist kein Widerstand – das Nervensystem schaltet auf Notbetrieb.",
         werkzeuge="Selbst-Regulation stärken (M3-20)",
         brainy="In dieser Situation zuerst regulieren – dann alles andere."),

    dict(id_text="WZ-05", typ="situation", icon="exchange", titel="Übergang zwischen Situationen",
         front_kontext="Gelb – erhöhte Aufmerksamkeit",
         lead="Wechsel von einer Situation/einem Fach zur nächsten – für viele Kinder der schwierigste Moment.",
         schritte=[
             "Ankündigen, immer vorher – mind. 2-3 Minuten vorher, keine Überraschungen",
             "Visuell zeigen, wenn möglich – Tagesplan, nächsten Schritt auf Karte",
             "Übergangsritual nutzen – immer dasselbe Signal (Klopfen, Wort)",
             "Bei Widerstand: nicht sofort – kleiner Puffer, kein Kampf",
             "Ankommen bestätigen – kurzer Check, Barometer, dann erst Inhalt",
         ],
         tipp="Übergänge sind für viele Kinder die schwierigsten Momente des Schultags – weil "
              "das Gehirn umschalten muss.",
         werkzeuge="Atemanker (M3-09) · Visualisierung (M3-17)",
         brainy="In dieser Situation zuerst regulieren – dann alles andere."),

    dict(id_text="WZ-06", typ="situation", icon="users", titel="Konflikt mit Mitschüler:innen",
         front_kontext="Orange – typischer Bereich",
         lead="Zwei Kinder geraten aneinander – Sicherheit geht vor Klärung.",
         schritte=[
             "Stoppen, Sicherheit herstellen – dazwischen gehen, „Stopp“, ohne Gewalt trennen",
             "Beide beruhigen, getrennt – kein Schuld-Zuweisen jetzt",
             "Beiden zuhören, nacheinander – sachlich zusammenfassen, ohne zu werten",
             "Klären was passiert ist – „Was ist passiert? Was hast du gefühlt? Was hättest du gebraucht?“",
             "Lösung von beiden tragen lassen – keine Lösung von oben, konkrete Schritte",
         ],
         tipp="Konflikte sind Lernchancen, wenn sie begleitet werden. Schuld verteilen lernt nichts.",
         werkzeuge="Selbst-Regulation stärken (M3-20)",
         brainy="In dieser Situation zuerst regulieren – dann alles andere."),

    dict(id_text="WZ-07", typ="situation", icon="tint", titel="Kind ist überwältigt – weint",
         front_kontext="Orange bis Grau – typischer Bereich",
         lead="Kind weint, ist überwältigt – der Körper verarbeitet gerade etwas Großes.",
         schritte=[
             "Zuerst da sein, nicht reden – neben das Kind setzen, keine Fragen",
             "Gefühl anerkennen, ohne Relativieren – „Ich sehe, das ist gerade sehr schwer“",
             "Rückzugsmöglichkeit anbieten – ruhiger Ort, Kind entscheidet",
             "Keine sofortige Problemlösung – erst Gefühl anerkennen, dann fragen",
             "Übergang zurück vorbereiten – kleines Erfolgserlebnis, sanft zurück",
         ],
         tipp="Weinen ist kein Problem – der Körper verarbeitet. Deine Aufgabe ist Sicherheit, "
              "nicht Stoppen.",
         werkzeuge="Atemanker (M3-09)",
         brainy="In dieser Situation zuerst regulieren – dann alles andere."),

    dict(id_text="WZ-08", typ="situation", icon="bell", titel="Krise – Rot oder Grau – Feuerwehr",
         front_kontext="Rot / Grau – typischer Bereich",
         lead="Akute Krise – hier greift ausschließlich das Feuerwehr-Protokoll, kein normaler Unterricht mehr.",
         schritte=[
             "Sofort Feuerwehr-Protokoll aktivieren – TK sofort informieren",
             "Andere Kinder schützen – LK schickt raus oder gibt Aufgabe",
             "kLAR einleiten – Kontakt&Sicherheit, Leise&Langsam, Anerkennung&Atmen, "
             "Reizreduktion&Rückzug",
             "Eltern informieren – durch TK oder LK, nicht durch INGRA allein",
             "Dokumentieren, noch heute – sachlich, ohne Interpretation",
         ],
         tipp="Bei Rot gilt: erst Sicherheit, dann alles andere. Keine Inhalte, keine Gespräche, "
              "keine Konsequenzen.",
         werkzeuge="kLAR-Modell · Krisendeck (Feuerwehrkarten)",
         brainy="In dieser Situation zuerst regulieren – dann alles andere."),

    # ═══════════════ WERKZEUGE (M3-09–20) ═══════════════
    dict(id_text="WZ-09", typ="werkzeug", icon="circle-notch", titel="Atemanker",
         front_kontext="Gelb · Orange · vor Übergängen · nach Pause",
         lead="Einfache Atemübung, beruhigt das Nervensystem sofort. 4 Sek ein – 4 halten – "
              "6 aus. Wirkt bei Gelb, Orange, als Einstieg nach Rot.",
         schritte=[
             "Ruhig neben das Kind setzen, kein Druck",
             "Kurz zeigen: Hand auf Bauch legen",
             "Gemeinsam 4 Sekunden einatmen",
             "4 Sekunden halten",
             "6 Sekunden ausatmen",
             "2-3 Runden, dann kurz warten",
         ],
         tipp="Nie erzwingen. „Sollen wir kurz zusammen atmen?“ Wenn nein – ok.",
         brainy="Kein Werkzeug passt immer – wähle was heute zum Kind passt."),

    dict(id_text="WZ-10", typ="werkzeug", icon="refresh", titel="Liegende Acht",
         front_kontext="Gelb · Konzentrationsprobleme · nach Übergängen · morgens",
         lead="Bewegungsübung aus der Edu-Kinestetik, verbindet beide Gehirnhälften, hilft bei "
              "Konzentrationsproblemen und Blockaden.",
         schritte=[
             "Blatt Papier quer hinlegen",
             "Finger in die Mitte setzen",
             "Liegende 8 (∞) in einem Zug malen, immer wieder",
             "Erst groß, dann kleiner",
             "Mit beiden Händen abwechselnd oder zusammen",
         ],
         tipp="Auch in der Luft möglich, kein Material nötig. 30 Sekunden reichen.",
         brainy="Kein Werkzeug passt immer – wähle was heute zum Kind passt."),

    dict(id_text="WZ-11", typ="werkzeug", icon="eye", titel="5-Dinge-Grounding",
         front_kontext="Orange · Angst · Überwältigung · Dissoziation · Freeze",
         lead="Bringt das Kind zurück in den Moment, weg von Gedanken, Angst oder Überwältigung. "
              "Nutzt alle 5 Sinne.",
         schritte=[
             "Ruhig fragen: „Können wir kurz ein Spiel machen?“",
             "5 Dinge die ich sehe – benennen",
             "4 Dinge die ich fühlen kann",
             "3 Dinge die ich höre",
             "2 Dinge die ich rieche",
             "1 Ding das ich schmecke",
         ],
         tipp="Langsam sprechen, Pausen lassen. Das Kind darf flüstern oder nicken.",
         brainy="Kein Werkzeug passt immer – wähle was heute zum Kind passt."),

    dict(id_text="WZ-12", typ="werkzeug", icon="headphones", titel="Reizfilter",
         front_kontext="Orange · Rot · Überreizung · laute Klasse · Stress",
         lead="Reduziert sensorische Überstimulation. Kopfhörer, Sichtschutz, ruhiger Platz – "
              "einfache Mittel, große Wirkung.",
         schritte=[
             "Signal erkennen: Kind wirkt überreizt, zieht sich zurück",
             "Ruhig anbieten: „Möchtest du Kopfhörer?“",
             "Ruhigen Platz aufsuchen, wenn möglich",
             "Reize reduzieren – Licht dimmen, Geräusche minimieren",
             "Keine Anforderungen während Reizreduktion",
             "Erst wenn beruhigt: langsam zurück",
         ],
         tipp="Kopfhörer sind kein Privileg, sondern Regulation. Andere Kinder müssen das nicht "
              "kommentieren.",
         brainy="Kein Werkzeug passt immer – wähle was heute zum Kind passt."),

    dict(id_text="WZ-13", typ="werkzeug", icon="flag", titel="Joker",
         front_kontext="Gelb · Orange · wenn Kind nicht sprechen kann · Krise droht",
         lead="Notfallsignal, das das Kind selbst einsetzt – ohne Worte, ohne Erklärung. Eine "
              "Karte, ein Zeichen, ein stilles Signal.",
         schritte=[
             "Joker-Karte beim Kind lassen (laminiert)",
             "Vorab vereinbaren: „Wenn du die Karte zeigst, komme ich sofort“",
             "Kind zeigt Karte oder legt sie hin",
             "INGRA reagiert sofort und ruhig",
             "Keine Fragen, keine Erklärung nötig",
             "Kind entscheidet, was als nächstes passiert",
         ],
         tipp="Der Joker funktioniert nur, wenn er vorab erklärt und geübt wurde.",
         brainy="Kein Werkzeug passt immer – wähle was heute zum Kind passt."),

    dict(id_text="WZ-14", typ="werkzeug", icon="pause", titel="Mini-Pause",
         front_kontext="Gelb · Orange · vor Tests · bei Überforderung",
         lead="2-5 Minuten Pause außerhalb des Klassenraums, kann Eskalationen verhindern. "
              "Strukturiert, kurz, wiederkehrend.",
         schritte=[
             "Signal vereinbaren (Joker oder Geste)",
             "Ruhig und unauffällig rausgehen",
             "Kurze Bewegung: Flur, Treppe, Schulhof",
             "INGRA begleitet, kein Gespräch nötig",
             "Nach 2-5 Minuten: „Bereit?“",
             "Zurück, wenn Kind nickt",
         ],
         tipp="Mini-Pause ist keine Belohnung und keine Strafe – sie ist Regulation.",
         brainy="Kein Werkzeug passt immer – wähle was heute zum Kind passt."),

    dict(id_text="WZ-15", typ="werkzeug", icon="list-ol", titel="Schritt-Plan",
         front_kontext="Gelb · Verweigerung · Überforderung · komplexe Aufgaben",
         lead="Bricht eine überwältigende Aufgabe in kleine machbare Schritte. Reduziert "
              "Verweigerung, stärkt Selbstwirksamkeit.",
         schritte=[
             "Aufgabe zusammen anschauen",
             "Fragen: „Was ist der allererste kleine Schritt?“",
             "Nur diesen einen Schritt aufschreiben",
             "Kind macht nur diesen einen Schritt",
             "Abhaken, kurz loben",
             "Nächsten Schritt erst dann",
         ],
         tipp="Ein Schritt, nicht fünf. Der erste soll so klein sein, dass er unmöglich "
              "schiefgehen kann.",
         brainy="Kein Werkzeug passt immer – wähle was heute zum Kind passt."),

    dict(id_text="WZ-16", typ="werkzeug", icon="dot-circle", titel="Igel-Ball",
         front_kontext="Gelb · Unruhe · Zappeln · Konzentration · sensorisches Bedürfnis",
         lead="Sensorisches Tool, reguliert Überreizung, fördert Fokus. Einfach, unauffällig, "
              "effektiv.",
         schritte=[
             "Igel-Ball unauffällig anbieten",
             "Kind kann damit kneten, rollen, drücken",
             "Keine Erklärung nötig",
             "Ball bleibt auf dem Tisch oder in der Hand",
             "Anforderungen bleiben gleich, Tool unterstützt",
         ],
         tipp="Auch Knete, Stressball oder Fidget-Spinner wirken ähnlich. Was das Kind mag, das "
              "nimmt man.",
         brainy="Kein Werkzeug passt immer – wähle was heute zum Kind passt."),

    dict(id_text="WZ-17", typ="werkzeug", icon="map", titel="Visualisierung",
         front_kontext="täglich · Übergänge · neue Situationen · Pflegekinder · ADHS",
         lead="Visuelle Pläne und Tages-Übersichten geben Struktur und Vorhersehbarkeit. "
              "Hilfreich bei Pflegekindern und ADHS.",
         schritte=[
             "Tagesplan morgens zeigen",
             "Jede Einheit als Bild oder Symbol",
             "Abgehaktes durchstreichen oder umdrehen",
             "Bei Änderungen: frühzeitig zeigen und besprechen",
             "Plan sichtbar lassen, nicht wegsperren",
         ],
         tipp="Ein Plan muss nicht schön sein. Eine handgezeichnete Liste reicht.",
         brainy="Kein Werkzeug passt immer – wähle was heute zum Kind passt."),

    dict(id_text="WZ-18", typ="werkzeug", icon="thumbs-up", titel="Lob-Sandwich",
         front_kontext="nach Aufgaben · bei Verhalten · Rückmeldung geben · täglich",
         lead="Feedback-Technik: Positiv – Verbesserung – Positiv. Kritik wird aufgenommen, ohne "
              "das Selbstbild zu beschädigen.",
         schritte=[
             "Erst etwas Konkretes loben",
             "Dann einen konkreten Hinweis",
             "Zuletzt wieder positiv",
             "Immer konkret, nie pauschal",
         ],
         tipp="Lob muss verdient sein. „Super“ ohne Inhalt wirkt nicht – „Du hast alle 5 Zeilen "
              "fertig“ wirkt.",
         brainy="Kein Werkzeug passt immer – wähle was heute zum Kind passt."),

    dict(id_text="WZ-19", typ="werkzeug", icon="sitemap", titel="Brainy-Flow",
         front_kontext="systemisch · als Orientierung · wenn unklar welches Tool",
         lead="Die im KLARTEXT-System empfohlene Werkzeug-Abfolge – je nach Barometer-Farbe.",
         schritte=[
             "Barometer-Farbe bestimmen",
             "Grün: normal weiter",
             "Gelb: Atemanker oder Igel-Ball",
             "Orange: Reizfilter + Mini-Pause + kLAR",
             "Rot: kLAR komplett, TK informieren",
             "Grau: ruhige Präsenz, keine Anforderungen",
         ],
         tipp="Der Brainy-Flow ist kein Muss, sondern Orientierung. Intuition und Kenntnis des "
              "Kindes gehen vor.",
         brainy="Kein Werkzeug passt immer – wähle was heute zum Kind passt."),

    dict(id_text="WZ-20", typ="werkzeug", icon="leaf", titel="Selbst-Regulation stärken",
         front_kontext="langfristig · nach stabilen Phasen · als Entwicklungsziel",
         lead="Langfristiges Ziel aller Werkzeuge: Das Kind lernt, sich selbst zu regulieren – "
              "braucht INGRA immer weniger.",
         schritte=[
             "Werkzeuge benennen: „Das nennt sich Atemanker“",
             "Kind einbeziehen: „Was hat dir heute geholfen?“",
             "Kind entscheiden lassen: „Was brauchst du gerade?“",
             "Erfolge sichtbar machen, Barometer zeigen",
             "Rückschritte normal nehmen, kein Druck",
         ],
         tipp="Das Ziel ist nicht Abhängigkeit von INGRA, sondern ein Kind, das weiß, was ihm hilft.",
         brainy="Kein Werkzeug passt immer – wähle was heute zum Kind passt."),

    # ═══════════════ M3-ERWEITERUNG (M3-21–26, ergänzt 01.08.2026) ═══════════════
    dict(id_text="WZ-21", typ="werkzeug", icon="hourglass-half", titel="Sichtbare Zeit",
         front_kontext="vor Aufgaben · vor Übergängen · bei Prüfungsangst",
         lead="Visueller Timer (z. B. Time-Timer) zeigt verbleibende Zeit als Fläche statt nur als "
              "Zahl – reduziert Angst vor dem Unbekannten.",
         schritte=[
             "Visuellen Timer sichtbar aufstellen",
             "Verbleibende Zeit als Fläche/Farbe zeigen, nicht nur als Zahl",
             "Vor Beginn kurz erklären, was passiert, wenn die Zeit abgelaufen ist",
             "Bei Bedarf 1x zwischendurch auf den Timer hinweisen, nicht mehrfach mahnen",
         ],
         tipp="Sichtbare Zeit reduziert Angst vor dem Unbekannten – das Kind sieht die Zeit "
              "schrumpfen, statt sich auf eine abstrakte Zahl verlassen zu müssen.",
         brainy="Kein Werkzeug passt immer – wähle was heute zum Kind passt."),

    dict(id_text="WZ-22", typ="werkzeug", icon="hand-paper-o", titel="Stopp-Hand-Signal",
         front_kontext="Gelb · Orange · verbale Eskalation",
         lead="Klares, nonverbales Stopp-Signal, bevor Worte nicht mehr ankommen.",
         schritte=[
             "Flache Hand ruhig heben, auf Augenhöhe, kein Anschreien",
             "Blickkontakt halten, wenn möglich, ohne zu starren",
             "Kurz warten – nicht sofort weiterreden",
             "Erst wenn Ruhe da ist, in 1-2 Sätzen erklären, was als Nächstes passiert",
         ],
         tipp="Das Stopp-Hand-Signal wirkt am besten, wenn es vorher eingeführt und geübt wurde – "
              "in der akuten Situation ist es zu spät für Erklärungen.",
         brainy="Kein Werkzeug passt immer – wähle was heute zum Kind passt."),

    dict(id_text="WZ-23", typ="werkzeug", icon="home", titel="Sicherer Ort",
         front_kontext="vorbeugend · Orange · als fester Rückzugsort",
         lead="Fester, bekannter Rückzugsort, bevor eine Situation weiter eskaliert – nicht erst, "
              "wenn es schon zu spät ist.",
         schritte=[
             "Sicheren Ort im Vorfeld gemeinsam festlegen, nicht erst im Akutfall",
             "Ort so gestalten, dass er reizarm und vorhersehbar ist",
             "Zugang niedrigschwellig ermöglichen (kein Antrag, keine Erlaubnis nötig)",
             "Rückkehr aus dem sicheren Ort nicht erzwingen, Zeit lassen",
         ],
         tipp="Ein sicherer Ort funktioniert nur, wenn er wirklich jederzeit zugänglich ist – ein "
              "\"sicherer Ort\" mit Hürden ist keiner.",
         brainy="Kein Werkzeug passt immer – wähle was heute zum Kind passt."),

    dict(id_text="WZ-24", typ="werkzeug", icon="heartbeat", titel="Körper-Check-In",
         front_kontext="vor Gesprächen · vor Aufgaben · als Routine",
         lead="Kurzer Check, wie reguliert der Körper gerade ist – Worte allein zeigen das oft "
              "nicht.",
         schritte=[
             "Kurze, konkrete Frage stellen: „Wie fühlt sich dein Körper gerade an?“",
             "Bei Bedarf Körperskala nutzen (ruhig – angespannt – sehr angespannt)",
             "Je nach Antwort: erst regulieren, dann inhaltlich weitermachen",
             "Keine Bewertung der Antwort – jeder Zustand ist erstmal nur Information",
         ],
         tipp="Der Körper reagiert oft schneller und ehrlicher als Worte – ein Körper-Check-In "
              "holt Informationen, die ein „Wie geht's?“ nicht liefert.",
         brainy="Kein Werkzeug passt immer – wähle was heute zum Kind passt."),

    dict(id_text="WZ-25", typ="werkzeug", icon="pause", titel="Die Kraft der Pause",
         front_kontext="in jeder angespannten Situation",
         lead="Eine kurze Pause vor der eigenen Reaktion ist selbst schon eine Intervention.",
         schritte=[
             "Bewusst 3–5 Sekunden nichts sagen, bevor reagiert wird",
             "Eigene Atmung kurz wahrnehmen",
             "Erst dann entscheiden, was als Nächstes gebraucht wird",
             "Bei Bedarf die Pause auch dem Kind laut ankündigen („Ich brauch kurz einen Moment“)",
         ],
         tipp="Eine Pause wirkt nicht als Schwäche, sondern als Signal von Ruhe – sie gibt auch "
              "dem Kind einen Moment zum Ankommen.",
         brainy="Kein Werkzeug passt immer – wähle was heute zum Kind passt."),

    dict(id_text="WZ-26", typ="werkzeug", icon="handshake-o", titel="No-Blame-Approach",
         front_kontext="nach Mobbingvorfall · Gruppenaufarbeitung",
         lead="Weg, die Gruppe nach einem Mobbingvorfall einzubeziehen, ohne Schuldzuweisung in den "
              "Mittelpunkt zu stellen.",
         schritte=[
             "Kleine Gruppe (Beteiligte + Umstehende) zusammenbringen, ohne Vorwurf",
             "Situation des betroffenen Kindes schildern (mit dessen Einverständnis), ohne "
             "anzuklagen",
             "Gruppe nach eigenen Ideen fragen, was helfen könnte",
             "Nach ca. 1 Woche kurze Nachbesprechung, was sich verändert hat",
         ],
         tipp="Der No-Blame-Approach funktioniert, weil er Verantwortung statt Schuld anspricht – "
              "das öffnet Kinder eher für echte Veränderung als eine Bestrafung.",
         brainy="Kein Werkzeug passt immer – wähle was heute zum Kind passt."),
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
