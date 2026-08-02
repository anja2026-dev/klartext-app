#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Batch-Renderer für alle 19 TK-Handlungskarten (Vorder- + Rückseite)."""
import os
from build_card_tk import build_front, build_back

BILD_DIR = "/sessions/kind-beautiful-ptolemy/mnt/klartext-app/bilder/tk/"
OUT_DIR = "/sessions/kind-beautiful-ptolemy/mnt/outputs/tk_karten_komplett/"
os.makedirs(OUT_DIR, exist_ok=True)

def find_image(nr):
    for suffix in (".jpg", ".png", ".jpeg"):
        p = os.path.join(BILD_DIR, f"TK-{nr:02d}{suffix}")
        if os.path.exists(p):
            return p
    return None

CARDS = [
    dict(nr=1, id_text="TK-01", brainy=False, kategorie="team", tischwerkzeug=False,
         titel="Koordination im Team",
         situation="Mehrere INGRA betreuen dasselbe Kind oder Team, Zuständigkeiten sind unklar.",
         schritte=[
             "Rollen und Zuständigkeiten einmal schriftlich festhalten",
             "Wer entscheidet was, wer informiert wen",
             "Feste Übergabepunkte statt Zufallsgespräche",
             "Bei Unklarheit: TK fragen, nicht raten",
         ],
         abgrenzung=[
             ("Zuständigkeiten schriftlich fixieren", "Stillschweigend annehmen, wer zuständig ist"),
             ("Feste Übergabepunkte nutzen", "Nur zufällig auf dem Flur austauschen"),
             ("Bei Unklarheit früh nachfragen", "Aus Höflichkeit unklar lassen"),
         ],
         quelle="Rollenklarheit-Konzept (Katzenbach & Smith, The Wisdom of Teams, 1993) – vorgeschlagen, bitte gegenprüfen."),

    dict(nr=2, id_text="TK-02", brainy=True, kategorie="team", tischwerkzeug=True,
         titel="Fallbesprechung strukturieren",
         situation="Ein Fall soll im Team besprochen werden, Gefahr: unstrukturiert, zu lang, ohne Ergebnis.",
         schritte=[
             "Fall in 2–3 Sätzen einleiten (Fakten, kein Urteil)",
             "Fragerunde vor Meinungsrunde",
             "Erst wenn alle gehört wurden: Einschätzungen sammeln",
             "Konkretes Ergebnis + Verantwortliche festhalten",
         ],
         abgrenzung=[
             ("Fragen vor Bewerten", "Sofort Lösungen vorschlagen"),
             ("Alle zu Wort kommen lassen", "Nur die Lautesten hören"),
             ("Ergebnis schriftlich festhalten", "Ohne Ergebnis auseinandergehen"),
         ],
         quelle="Kollegiale Fallberatung (Schlee, J., 2019) – vorgeschlagen, bitte gegenprüfen."),

    dict(nr=3, id_text="TK-03", brainy=True, kategorie="kind", tischwerkzeug=False,
         titel="Hilfeplangespräch vorbereiten",
         situation="Ein Hilfeplangespräch (§ 36 SGB VIII) steht an, INGRA und TK müssen strukturiert vorbereitet reingehen.",
         schritte=[
             "Beobachtungszeitraum sichten, Kernpunkte auswählen",
             "Konkrete Beispiele statt allgemeiner Einschätzungen vorbereiten",
             "Eigene Zielvorschläge vorab klären",
             "Rollen im Gespräch kurz absprechen",
         ],
         abgrenzung=[
             ("Konkrete Beispiele mitbringen", "Nur vage Eindrücke schildern"),
             ("Rollen vorher klären", "Im Gespräch improvisieren, wer redet"),
             ("Zielvorschläge vorbereiten", "Unvorbereitet auf andere warten"),
         ],
         quelle="SGB VIII § 36 (Hilfeplan) – bereits im Quellenregister der Serie bestätigt."),

    dict(nr=4, id_text="TK-04", brainy=True, kategorie="kind", tischwerkzeug=False,
         titel="§ 8a – Schutzauftrag",
         situation="Anzeichen, die auf eine mögliche Kindeswohlgefährdung hindeuten könnten – Unsicherheit, wie einzuordnen.",
         schritte=[
             "Beobachtung konkret und zeitnah dokumentieren (Fakten, keine Bewertung)",
             "Insoweit erfahrene Fachkraft einbeziehen (§ 8a Abs. 4)",
             "TK sofort informieren, auch bei Unsicherheit",
             "Weiteres Vorgehen gemeinsam festlegen",
         ],
         abgrenzung=[
             ("Sofort dokumentieren und melden", 'Erst selbst "sicher sein" wollen'),
             ("Fachkraft einbeziehen", "Allein entscheiden"),
             ("TK informieren, auch im Zweifel", 'Abwarten, "wird schon nichts sein"'),
         ],
         quelle="SGB VIII § 8a (Schutzauftrag bei Kindeswohlgefährdung)."),

    dict(nr=5, id_text="TK-05", brainy=False, kategorie="system", tischwerkzeug=False,
         titel="Qualitätssicherung",
         situation="Regelmäßige Überprüfung, ob Standards in der Fallarbeit eingehalten werden.",
         schritte=[
             "Stichproben statt lückenloser Kontrolle",
             "Standards konkret und schriftlich vorher festlegen",
             'Rückmeldung wertschätzend, nicht als Kontrolle "von oben"',
             "Ergebnisse für Weiterentwicklung nutzen",
         ],
         abgrenzung=[
             ("Standards vorher klar kommunizieren", "Erst bei der Prüfung Maßstäbe erfinden"),
             ("Wertschätzend rückmelden", "Als reine Kontrolle auftreten"),
             ("Ergebnisse nutzen", "Nur dokumentieren, nichts verändern"),
         ],
         quelle="DIN EN ISO 9001:2015 – in der Jugendhilfe verbreitete Qualitätsmanagement-Norm."),

    dict(nr=6, id_text="TK-06", brainy=True, kategorie="team", tischwerkzeug=True,
         titel="Teamentwicklung",
         situation="Ein Team ist neu zusammengestellt oder durchläuft eine Veränderung.",
         schritte=[
             "Phase erkennen: Findung, Auseinandersetzung, Klärung oder eingespielt",
             "In Findung/Auseinandersetzung: mehr Struktur, nicht weniger",
             "Konflikte als Teil des Prozesses einordnen, nicht als Störung",
             "Erfolge im Team sichtbar machen",
         ],
         abgrenzung=[
             ("Phase benennen, Erwartungen anpassen", 'Von Tag eins "eingespieltes Team" erwarten'),
             ("Reibung als normal einordnen", "Reibung sofort persönlich nehmen"),
             ("Kleine Erfolge sichtbar machen", "Nur Probleme besprechen"),
         ],
         quelle="Tuckman, B. W. (1965). Developmental Sequence in Small Groups – etabliertes Modell."),

    dict(nr=7, id_text="TK-07", brainy=True, kategorie="team", tischwerkzeug=False,
         titel="Kultursensible Begleitung organisieren",
         situation="Familie spricht wenig/kein Deutsch, oder kulturelle Missverständnisse erschweren die Zusammenarbeit.",
         schritte=[
             "Sprachmittlung früh organisieren, nicht erst bei Problemen",
             "Nie Kinder als Dolmetscher einsetzen",
             "Kulturelle Erwartungen offen ansprechen, nicht annehmen",
             "Dolmetscher-Einsatz dokumentieren",
         ],
         abgrenzung=[
             ("Professionelle Sprachmittlung organisieren", "Kind als Dolmetscher nutzen"),
             ("Erwartungen offen ansprechen", "Kulturelle Annahmen ungeprüft übernehmen"),
             ("Einsatz dokumentieren", "Bei jedem Fall neu improvisieren"),
         ],
         quelle="KLARTEXT-Praxis, angelehnt an Standards zu Sprachmittlung in der Kinder- und Jugendhilfe."),

    dict(nr=8, id_text="TK-08", brainy=True, kategorie="team", tischwerkzeug=True,
         titel="Konflikt im Team",
         situation="Zwischen zwei Teammitgliedern (oder Team/Familie) hat sich Spannung aufgebaut, die die Arbeit beeinträchtigt.",
         schritte=[
             "Konflikt benennen, bevor er eskaliert",
             "Getrennte Gespräche vor gemeinsamem Gespräch, wenn nötig",
             "Sachebene und Beziehungsebene trennen",
             "Konkrete Vereinbarung statt vager Versöhnung",
         ],
         abgrenzung=[
             ("Früh ansprechen", "Aussitzen, bis es eskaliert"),
             ("Sach- und Beziehungsebene trennen", "Alles vermischen"),
             ("Konkrete Vereinbarung treffen", 'Bei "ist doch geklärt" stehen bleiben'),
         ],
         quelle="Glasl, F. Konfliktmanagement – 9-Stufen-Eskalationsmodell, etabliert in der Konfliktforschung."),

    dict(nr=9, id_text="TK-09", brainy=False, kategorie="system", tischwerkzeug=False,
         titel="Krisenprotokoll",
         situation="Eine Krisensituation ist eingetreten oder gemeldet worden, Sofortmaßnahmen und Meldewege sind gefragt.",
         schritte=[
             "Sicherheit zuerst – bei akuter Gefahr: siehe Feuerwehrkarten in der App",
             "Sofort dokumentieren: was, wann, wer war beteiligt",
             "Meldewege einhalten (TK, ggf. Jugendamt, ggf. § 8a)",
             "Nachbesprechung im Team terminieren, nicht auslassen",
         ],
         abgrenzung=[
             ("Meldewege einhalten", 'Selbst "regeln" und nicht melden'),
             ("Sofort dokumentieren", "Erst später aus dem Gedächtnis aufschreiben"),
             ("Nachbesprechung terminieren", "Nach der Akutphase nichts aufarbeiten"),
         ],
         quelle="KLARTEXT-System – Anschluss an Feuerwehrkarten FK-01–08 (App)."),

    dict(nr=10, id_text="TK-10", brainy=True, kategorie="system", tischwerkzeug=False,
         titel="Schulkommunikation",
         situation="Abstimmung mit Schule/Lehrkraft ist nötig, läuft aber unregelmäßig oder nur bei Problemen.",
         schritte=[
             "Feste, regelmäßige Kontaktpunkte statt nur Anlass-Kommunikation",
             "Beobachtungen konkret und wertfrei schildern",
             "Erwartungen beider Seiten offen klären",
             "Vereinbarungen schriftlich festhalten",
         ],
         abgrenzung=[
             ("Regelmäßige Kontaktpunkte einplanen", "Nur bei Problemen melden"),
             ("Konkret und wertfrei schildern", "Pauschal urteilen"),
             ("Vereinbarungen schriftlich festhalten", "Mündliche Absprachen offen lassen"),
         ],
         quelle="KLARTEXT-Praxis, Anschluss an LK-Basis-Deck (Zusammenarbeit Schule–Schulbegleitung)."),

    dict(nr=11, id_text="TK-11", brainy=True, kategorie="kind", tischwerkzeug=False,
         titel="Elternkontakt begleiten",
         situation="Kontakt zu Eltern ist angespannt, unklar oder es besteht Vertrauensverlust.",
         schritte=[
             "Transparenz herstellen: was wird dokumentiert, was weitergegeben",
             "Erwartungen beiderseits offen klären",
             "Regelmäßigen, verlässlichen Kontakt anbieten",
             "Grenzen der eigenen Rolle klar benennen",
         ],
         abgrenzung=[
             ("Offen sagen, was dokumentiert wird", "Heimlich wirkende Berichte"),
             ("Regelmäßig, nicht nur bei Problemen melden", "Nur bei Krise Kontakt aufnehmen"),
             ("Eigene Rolle klar benennen", "Zu viel/zu wenig Nähe suggerieren"),
         ],
         quelle="KLARTEXT-Praxis, angelehnt an Grundsätze transparenter Elternarbeit in der Eingliederungshilfe."),

    dict(nr=12, id_text="TK-12", brainy=True, kategorie="kind", tischwerkzeug=False,
         titel="Zieldefinition & Hilfeplan",
         situation="Im Hilfeplan sollen Ziele für die kommende Phase formuliert werden, bisherige Ziele waren zu vage.",
         schritte=[
             "Ziel so konkret formulieren, dass beobachtbar ist, ob es erreicht wurde",
             "Realistischen Zeitrahmen setzen",
             "Wer prüft wann, woran wird der Fortschritt festgemacht",
             "Ziel mit Kind/Familie besprechen, nicht nur intern festlegen",
         ],
         abgrenzung=[
             ("Messbar formulieren", '"Soll sich besser fühlen" ohne Kriterium'),
             ("Zeitrahmen festlegen", "Offen lassen, bis wann"),
             ("Mit Kind/Familie besprechen", "Nur intern festlegen"),
         ],
         quelle="Doran, G. T. (1981). SMART-Ziele-Modell; SGB VIII § 36."),

    dict(nr=13, id_text="TK-13", brainy=True, kategorie="kind", tischwerkzeug=True,
         titel="Abschlussgespräch INGRA",
         situation="Eine Begleitung endet (Zielerreichung, Schulwechsel, Beendigung) – Abschluss soll professionell gestaltet werden.",
         schritte=[
             "Abschluss ankündigen, nicht überraschend beenden",
             "Rückblick gemeinsam mit Kind/Familie: was hat sich verändert",
             "Übergabe an Nachfolgende strukturiert vorbereiten",
             'Bewusster Abschied statt "stilles Verschwinden"',
         ],
         abgrenzung=[
             ("Abschluss frühzeitig ankündigen", "Überraschend beenden"),
             ("Gemeinsamen Rückblick halten", "Nur organisatorisch abwickeln"),
             ("Bewusst verabschieden", "Kommentarlos verschwinden"),
         ],
         quelle="KLARTEXT-Praxis, angelehnt an Prinzipien professioneller Beziehungsbeendigung in der sozialen Arbeit."),

    dict(nr=14, id_text="TK-14", brainy=False, kategorie="team", tischwerkzeug=False,
         titel="Dokumentationsprüfung",
         situation="Eine Dokumentation (Fallakte, Notiz, Bericht) soll geprüft werden, bevor sie weitergeht.",
         schritte=[
             "Fakten von Interpretation trennen",
             "Nur entscheidungsrelevante Informationen, keine Nebensächlichkeiten",
             "Datenschutz prüfen: darf das so stehen, wer darf es lesen",
             "Bei Unsicherheit: Rücksprache statt eigenmächtig kürzen",
         ],
         abgrenzung=[
             ("Fakten von Meinung trennen", "Vermutungen als Fakten formulieren"),
             ("Nur Relevantes dokumentieren", "Alles Private mit aufschreiben"),
             ("Datenschutz aktiv prüfen", '"Wird schon passen" denken'),
         ],
         quelle="DSGVO – Grundsatz der Datenminimierung, Art. 5 Abs. 1 lit. c."),

    dict(nr=15, id_text="TK-15", brainy=False, kategorie="system", tischwerkzeug=False,
         titel="Vertretungsorganisation",
         situation="Eine INGRA fällt aus (Krankheit, Urlaub), Vertretung muss kurzfristig organisiert werden.",
         schritte=[
             "Übergabedokument bereithalten, nicht erst im Ausfall erstellen",
             "Wichtigste Informationen priorisieren",
             "Vertretung kurz einweisen, nicht nur Dokument schicken",
             "Rückmeldung nach Einsatz einholen für nächstes Mal",
         ],
         abgrenzung=[
             ("Übergabedokument aktuell halten", "Erst im Ausfall improvisieren"),
             ("Kurze persönliche Einweisung", "Nur Dokument ohne Gespräch schicken"),
             ("Rückmeldung einholen", "Nach Einsatz nichts nachfragen"),
         ],
         quelle="KLARTEXT-Praxis, Anschluss an TK_Vertretungsassistent (App)."),

    dict(nr=16, id_text="TK-16", brainy=True, kategorie="system", tischwerkzeug=False,
         titel="Selbstfürsorge TK",
         situation="TK trägt viel Verantwortung für mehrere Fälle/Teams gleichzeitig – Erschöpfungssignale zeigen sich.",
         schritte=[
             "Frühwarnzeichen bei sich selbst erkennen (Reizbarkeit, Rückzug, Zynismus)",
             "Aufgaben realistisch delegieren statt alles selbst zu tragen",
             "Feste Erholungszeiten aktiv schützen",
             "Bei anhaltender Erschöpfung offen ansprechen, nicht durchhalten",
         ],
         abgrenzung=[
             ("Frühwarnzeichen ernst nehmen", '"Geht schon noch" bis zum Zusammenbruch'),
             ("Aufgaben delegieren", "Alles selbst kontrollieren wollen"),
             ("Erholungszeiten schützen", "Pausen als Erstes streichen"),
         ],
         quelle="Maslach, C. & Jackson, S. E. (1981). Maslach Burnout Inventory – etabliertes Burnout-Modell."),

    dict(nr=17, id_text="TK-17", brainy=False, kategorie="system", tischwerkzeug=False,
         titel="Zeitmanagement",
         situation="Zu viele Aufgaben gleichzeitig, unklar, was zuerst dran ist.",
         schritte=[
             "Aufgaben nach Dringlichkeit und Wichtigkeit sortieren",
             "Nicht-Dringendes bewusst terminieren, nicht aufschieben",
             "Pufferzeiten für Unvorhergesehenes einplanen",
             "Am Ende kurz reflektieren, was funktioniert hat",
         ],
         abgrenzung=[
             ("Nach Dringlichkeit/Wichtigkeit sortieren", 'Nach "was zuerst reinkam" abarbeiten'),
             ("Pufferzeiten einplanen", "Tag komplett verplanen"),
             ("Kurz reflektieren", "Nur weitermachen ohne Rückblick"),
         ],
         quelle="Eisenhower-Matrix (Dringlichkeit/Wichtigkeit-Prinzip), verbreitetes Zeitmanagement-Werkzeug."),

    dict(nr=18, id_text="TK-18", brainy=False, kategorie="system", tischwerkzeug=True,
         titel="Meetingstruktur",
         situation="Ein Meeting steht an, Gefahr: zu lang, ohne klares Ergebnis, Teilnehmende unvorbereitet.",
         schritte=[
             "Klare Tagesordnung vorher verschicken",
             "Zeitrahmen pro Punkt festlegen",
             "Ergebnis/Entscheidung pro Punkt explizit festhalten",
             "Nächste Schritte mit Verantwortlichen am Ende zusammenfassen",
         ],
         abgrenzung=[
             ("Tagesordnung vorher verschicken", "Ohne Agenda starten"),
             ("Zeitrahmen einhalten", "Einzelne Punkte ausufern lassen"),
             ("Ergebnisse festhalten", "Ohne Protokoll auseinandergehen"),
         ],
         quelle="KLARTEXT-Praxis, angelehnt an verbreitete Meeting-Moderationsprinzipien (Timeboxing)."),

    dict(nr=19, id_text="TK-19", brainy=True, kategorie="team", tischwerkzeug=True,
         titel="Feedback geben",
         situation="Rückmeldung an ein Teammitglied ist nötig – konstruktiv, nicht verletzend, nicht vermieden.",
         schritte=[
             "Konkrete Situation benennen, nicht pauschal urteilen",
             "Beobachtetes Verhalten und dessen Wirkung beschreiben",
             "Raum für die Sicht der anderen Person lassen",
             "Gemeinsam nächsten Schritt vereinbaren",
         ],
         abgrenzung=[
             ("Konkrete Situation benennen", 'Pauschal "du machst immer…"'),
             ("Verhalten/Wirkung trennen von Person", "Charakter bewerten"),
             ("Nächsten Schritt vereinbaren", "Feedback ohne Konsequenz stehen lassen"),
         ],
         quelle="SBI-Modell (Situation-Behavior-Impact, Center for Creative Leadership); Rosenberg, M. B. (GfK) – vorgeschlagen zur Gegenprüfung."),
]

def run():
    for card in CARDS:
        img_path = find_image(card["nr"])
        vorn = os.path.join(OUT_DIR, f"{card['id_text']}_Vorderseite.png")
        hinten = os.path.join(OUT_DIR, f"{card['id_text']}_Rueckseite.png")
        build_front(card, img_path, vorn)
        build_back(card, hinten)
        status = "mit Bild" if img_path else "OHNE BILD (Platzhalter)"
        print(f"{card['id_text']} fertig ({status})")

if __name__ == "__main__":
    run()
