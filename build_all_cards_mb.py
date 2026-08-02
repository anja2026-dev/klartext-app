#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rendert alle 15 Karten des Mobbing-Interventionsdecks. MB-01 bis MB-03 aus den App-Vorlagen
M6_DL_Mini-Krisenkarte.html, M6_DL_Mini-Checkliste_Erkennen.html, M6_DL_Digitale_Spuren_Sichern.html
uebernommen. MB-04 bis MB-15 aus den bestehenden, fachlich geprueften Modulseiten M6-03 bis M6-15
kondensiert (Content-Treuepflicht: Kernaussagen, Reihenfolge und Zitate unveraendert, nur gekuerzt
auf Kartenformat). Quellen der Ursprungsseiten: Olweus 1993, Schaefer 2010, Rose et al. 2011 (M6-01),
BMBF 2022 (M6-03), Salmivalli et al. 1996 (M6-04), Salmivalli 2010 (M6-13), Maines & Robinson 1992
(M6-12), Salmivalli et al. 2011 KiVa (M6-15) – vollstaendige Angaben im Anleitungs-Booklet."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from build_card_mb import build_front, build_back

OUT_DIR = "/sessions/kind-beautiful-ptolemy/mnt/outputs/mb_karten_komplett/"
os.makedirs(OUT_DIR, exist_ok=True)

CARDS = [
    dict(id_text="MB-01", icon="warndreieck", titel="Was tun bei Mobbing?",
         fuer="Schulbegleitung & Teamkoordination",
         lead="Sofortige Handlungssicherheit im akuten Mobbing-Fall — was zuerst zu tun ist.",
         schritte=[
             "Ruhe bewahren – nicht mitgehen, nicht eskalieren, klare ruhige Stimme",
             "Sicherheit herstellen – betroffene Person aus der Situation holen, Abstand schaffen",
             "Betroffene Person schützen – „Ich bin da.“ – nicht nach Details drängen",
             "Lehrkraft informieren – sofort, nicht später, kurze sachliche Info",
             "TK informieren – zeitnah, Fakten statt Bewertungen",
             "Dokumentieren – Was? Wer? Wann? Wo? – wörtliche Zitate, keine Vermutungen",
             "Elternkontakt über TK – SB informiert nicht selbst, TK übernimmt",
             "§8a prüfen – bei körperlicher Gewalt, Drohungen, digitaler Gewalt, Selbstgefährdung",
         ],
         merksatz="„Sicherheit zuerst. Fakten danach.“",
         brainy="Im Ernstfall zählt zuerst Schutz — alles andere kommt danach."),

    dict(id_text="MB-02", icon="suche", titel="Mobbing erkennen",
         fuer="Schulbegleitung & Lehrkraft – zur frühzeitigen Einschätzung",
         lead="Frühzeitig erkennen, nicht erst im Akutfall.",
         schritte=[
             "Wiederholung – Passiert es immer wieder?",
             "Absicht – Ist es gezielt verletzend?",
             "Machtungleichgewicht – Mehrere gegen eine Person – körperlich, sozial oder digital überlegen?",
             "Ausschluss – Systematisches Ignorieren, „Du darfst nicht mitspielen“?",
             "Demütigung – Lächerlich machen, Nachäffen, Bloßstellen",
             "Digitale Spuren – Nachrichten, Screenshots, Gruppenchat-Druck",
             "Reaktion des Opfers – Rückzug, Angst, Bauchschmerzen, Schweigen",
             "Umfeld – Niemand greift ein, Verteidiger fehlen",
         ],
         merksatz="„Mobbing ist ein Muster — kein Moment.“",
         brainy="Wenn ein Kind leidet und nicht mehr rauskommt — Muster prüfen, nicht nur Einzelsituationen."),

    dict(id_text="MB-03", icon="mobil", titel="Digitale Spuren sichern",
         fuer="Schulbegleitung & Teamkoordination bei Cybermobbing",
         lead="Sofortige Handlungssicherheit bei Cybermobbing.",
         schritte=[
             "Screenshots machen – gesamte Nachricht, Absender, Datum & Uhrzeit sichtbar",
             "Chatverläufe sichern – nicht nur einzelne Nachrichten, als Bildreihe sichern",
             "Nichts löschen – keine Nachrichten entfernen, keine Chats verlassen, keine Apps deinstallieren",
             "Nicht antworten – keine Gegenreaktion, keine Rechtfertigung, nichts weiterleiten",
             "Gerät sichern – Passwort nicht ändern, Gerät nicht aus der Hand geben, Akku laden",
             "TK informieren – zeitnah, sachlich, ohne Interpretation",
             "Eltern informieren – über TK, SB informiert nicht selbst",
             "Schule informieren – Klassenleitung, ggf. Schulleitung",
             "§8a prüfen – bei Drohungen, sexualisierten Inhalten, Erpressung",
             "Weiteres Vorgehen abstimmen – TK + Lehrkraft + Eltern, ggf. Schulsozialarbeit oder Polizei",
         ],
         merksatz="„Sichern — nicht reagieren.“",
         brainy="In der Hitze des Moments zählt: Beweise sichern, nicht selbst eingreifen."),

    dict(id_text="MB-04", icon="cyber", titel="Cybermobbing",
         fuer="Schulbegleitung – digitale Gewalt einordnen",
         lead="Cybermobbing ist rund um die Uhr da — kein Zuhause, keine Pause vor ihm.",
         schritte=[
             "Rund um die Uhr – keine Rückzugsräume mehr, auch zuhause kein Schutz",
             "Schnelle Verbreitung – Screenshots und Weiterleitungen erreichen in Minuten alle",
             "Typische Formen – Beleidigungen, peinliche Fotos, Ausschluss aus Gruppen, Fake-Profile, Gerüchte",
             "Zuhören – ohne zu bewerten, beruhigen und Sicherheit vermitteln",
             "Dokumentieren – Vorfälle mit Datum und Beschreibung festhalten",
             "Weitergeben – an Lehrkraft und Träger, Kind stärken: es ist nicht schuld",
             "Nicht selbst ermitteln – keine Chatverläufe auf privaten Geräten speichern, nicht bei Plattformen melden",
         ],
         merksatz="„Digital ist real — und Schweigen macht es schlimmer.“",
         brainy="Was online passiert, ist für Kinder genauso real wie physisches Mobbing."),

    dict(id_text="MB-05", icon="gruppe", titel="Die Rollen im Mobbing-System",
         fuer="Schulbegleitung – die Gruppendynamik verstehen",
         lead="Mobbing ist ein Gruppenprozess. Wer nur Täter und Opfer sieht, versteht das System nicht.",
         schritte=[
             "Täter – initiieren und führen das Mobbing an",
             "Mitläufer – machen mit, ohne selbst zu initiieren",
             "Unterstützer – lachen, schauen zu, geben Anerkennung",
             "Außenstehende – beobachten, ohne einzugreifen",
             "Verteidiger – seltene Kinder, die eingreifen oder das Opfer unterstützen",
             "Opfer – Ziel der Gruppe",
             "INGRAs Aufgabe – beobachten und dokumentieren, wer welche Rolle einnimmt",
         ],
         merksatz="„Mobbing ist ein Gruppenphänomen – nicht nur ein Zweier-Problem.“",
         brainy="Mobbing verändert sich nur, wenn die Gruppe sich verändert – nicht nur der Täter."),

    dict(id_text="MB-06", icon="wechsel", titel="Täter-Opfer-Umkehr erkennen",
         fuer="Schulbegleitung – Fehleinschätzungen vermeiden",
         lead="Manchmal wird das Opfer als Täter wahrgenommen — eine der gefährlichsten Mobbing-Fallen.",
         schritte=[
             "Das Opfer reagiert auf Provokation sichtbar und emotional",
             "Die Reaktion wird beobachtet – nicht die Provokation davor",
             "Erwachsene sehen nur den Ausbruch, nicht das System dahinter",
             "Das Opfer wird als „schwierig“ oder „aggressiv“ bezeichnet",
             "Die eigentlichen Täter wirken harmlos und kooperativ",
             "INGRA beobachtet längere Zeiträume – nicht nur den Moment",
             "Muster dokumentieren: Wer provoziert zuerst?",
         ],
         merksatz="„Das Opfer reagiert – der Täter provoziert. Beobachte, wer anfängt.“",
         brainy="Wer nur die Reaktion sieht, versteht die Situation nicht."),

    dict(id_text="MB-07", icon="schule", titel="Mobbing und Lehrkraft",
         fuer="Schulbegleitung & Teamkoordination",
         lead="Lehrkraft und INGRA müssen an einem Strang ziehen. Unterschiedliche Einschätzungen gefährden das Opfer.",
         schritte=[
             "INGRA beobachtet und meldet – systematisch, sachlich, ohne Eigenintervention auf Gruppenebene",
             "Lehrkraft koordiniert – Klassenintervention, Elterngespräche, Schulsozialarbeit, Konsequenzen",
             "Bei unterschiedlichen Einschätzungen: nie vor dem Kind diskutieren",
             "TK einbeziehen als vermittelnde Stelle",
             "Dokumentation als sachliche Grundlage nutzen",
             "Gemeinsames Ziel benennen: das Wohl des Kindes",
         ],
         merksatz="„Koordiniert handeln schützt das Kind. Alleingänge gefährden es.“",
         brainy="Lehrkraft und INGRA müssen dasselbe Ziel haben: Sicherheit für das Kind."),

    dict(id_text="MB-08", icon="dialog", titel="Elterngespräch bei Mobbing",
         fuer="Schulbegleitung – Rolle im Elterngespräch",
         lead="Elterngespräche bei Mobbing sind emotional aufgeladen. Vorbereitung und klare Rolle schützen alle.",
         schritte=[
             "INGRA führt keine eigenständigen Elterngespräche über Mobbing",
             "Beobachtungen fließen über TK in das Gespräch ein",
             "Bei Gesprächen dabei sein: zuhören, nicht kommentieren",
             "Sachliche Dokumentation als Grundlage bereitstellen",
             "Eltern des Opfers bringen oft mit: Wut, Hilflosigkeit, Schuldgefühle, Misstrauen",
             "Eltern des Täters bringen oft mit: Verneinung, Gegenanschuldigungen, Verharmlosung",
             "Nie allein – Elterngespräche über Mobbing immer mit TK oder Lehrkraft zusammen",
         ],
         merksatz="„Deine Beobachtungen sind Gold wert – führe sie ein, aber nicht das Gespräch.“",
         brainy="Elterngespräche bei Mobbing gehören nicht zu INGRA allein – aber die Beobachtungen schon."),

    dict(id_text="MB-09", icon="schutz", titel="Wenn INGRA selbst betroffen ist",
         fuer="Schulbegleitung – Selbstschutz",
         lead="Manchmal richten sich Aggression oder Ausgrenzung auch gegen INGRA. Das ist ernst zu nehmen.",
         schritte=[
             "Verbale Angriffe durch Kinder oder Jugendliche",
             "Ausgrenzung von INGRA durch die Klasse",
             "Gerüchteverbreitung oder Lügen über INGRA",
             "Feindselige Haltung durch Mitschüler des begleiteten Kindes",
             "Grenzüberschreitungen durch Eltern (verbal oder digital)",
             "Sofort: dokumentieren → TK informieren → nicht allein tragen → Reaktion abstimmen",
         ],
         merksatz="„Wer sich selbst nicht schützt, kann auf Dauer niemanden anderen schützen.“",
         brainy="Du bist nicht weniger schützenswert als das Kind, das du begleitest."),

    dict(id_text="MB-10", icon="auge", titel="Prävention im Klassenzimmer",
         fuer="Schulbegleitung – tägliche Präventionsarbeit",
         lead="Mobbing entsteht nicht über Nacht. Wer die frühen Zeichen kennt, verhindert das meiste bevor es beginnt.",
         schritte=[
             "Beobachten – wer spielt mit wem? Wer ist immer allein? Wer wird nie gewählt?",
             "Brücken bauen – ausgeschlossene Kinder diskret einbeziehen, ohne es zu thematisieren",
             "Stärken sichtbar machen – jedes Kind hat etwas, das andere beeindruckt",
             "Beobachtungen dokumentieren und an TK und Lehrkraft weitergeben",
             "Frühwarnzeichen ernst nehmen – regelmäßig allein, nie gewählt, aufgewühlt nach der Pause",
         ],
         merksatz="„Prävention beginnt mit Aufmerksamkeit — bevor ein Name fällt.“",
         brainy="Prävention ist keine Einzelaktion — sie ist eine Haltung, die täglich gelebt wird."),

    dict(id_text="MB-11", icon="ablauf", titel="Gruppenintervention Step by Step",
         fuer="Schulbegleitung & Teamkoordination",
         lead="Sobald Mobbing festgestellt ist, braucht es eine koordinierte Gruppenintervention.",
         schritte=[
             "Stoppen & Sichern – Opfer schützen, sofortige Sicherheit herstellen",
             "Einzelgespräche – Lehrkraft spricht mit allen Beteiligten, INGRA liefert Beobachtungen",
             "Gruppenarbeit – strukturierte Klassenarbeit mit professioneller Leitung",
             "Nachsorge – regelmäßige Beobachtung, ob die Situation stabil bleibt",
             "Elterninformation – koordiniert durch Lehrkraft und TK, INGRA nicht allein",
             "INGRAs Rolle: beobachten, dokumentieren, weitergeben, Opfer im Alltag stärken",
             "INGRA tut nicht: eigenständige Intervention, Täteransprache ohne Abstimmung",
         ],
         merksatz="„Gruppenintervention gelingt nur koordiniert — nicht im Alleingang.“",
         brainy="Fünf Phasen, ein Ziel: Sicherheit für das Kind."),

    dict(id_text="MB-12", icon="handschlag", titel="No-Blame-Approach",
         fuer="Schulbegleitung – Methode kennen, nicht selbst durchführen",
         lead="Eine evidenzbasierte Methode: nicht bestrafen, sondern Verantwortung aktivieren.",
         schritte=[
             "Gespräch mit dem Opfer – wie fühlt es sich, was wünscht es sich?",
             "Gruppe zusammenstellen – Täter, Mitläufer, Zuschauer, mögliche Unterstützer",
             "Situation beschreiben – wie es dem Opfer geht, ohne Anklage",
             "Verantwortung ansprechen – „Ihr könnt helfen, das zu ändern“",
             "Ideen sammeln – was wird jeder konkret tun?",
             "Gruppe in die Pflicht nehmen – jeder berichtet nach einer Woche",
             "Nachgespräch – hat sich etwas verändert?",
         ],
         merksatz="„Verantwortung aktivieren ist wirksamer als Strafe verhängen.“",
         brainy="No-Blame wird von geschulten Fachkräften durchgeführt — INGRA bereitet vor und begleitet nach."),

    dict(id_text="MB-13", icon="herz", titel="Verteidiger stärken",
         fuer="Schulbegleitung – Prävention über die Gruppe",
         lead="Kinder, die instinktiv eingreifen wollen, aber nicht wissen wie — sie zu stärken ist hochwirksam.",
         schritte=[
             "Wenn Zuschauer eingreifen, stoppt Mobbing in über 57 % der Fälle innerhalb von 10 Sekunden",
             "Verteidiger erkennen – wer reagiert, wenn jemand ausgelacht wird? Wer spielt mit dem Außenseiter?",
             "Verhalten konkret und privat loben – zeigen, dass es gesehen wird",
             "Konkrete Reaktionsmöglichkeiten zeigen, Mut benennen ohne zu exponieren",
             "Sätze die helfen: „Hör auf, das macht ihr/ihm nicht gut.“ · „Komm, wir gehen zusammen.“ · „Das finde ich nicht okay.“",
             "Auch ohne Wort wirksam: sich einfach neben die Person stellen",
         ],
         merksatz="„Ein Kind, das eingreift, verändert alles — auch wenn es nur danebensteht.“",
         brainy="Die meisten Kinder wollen helfen — sie brauchen nur einen Satz, den sie sich trauen zu sagen."),

    dict(id_text="MB-14", icon="familie", titel="Eltern informieren & einbeziehen",
         fuer="Schulbegleitung – Rolle im Elternkontakt",
         lead="Elterngespräche bei Mobbing gehören zu den emotionalsten Situationen in der Schulbegleitung.",
         schritte=[
             "Häufige Reaktionen der Eltern des Opfers: Wut, Hilflosigkeit, Erwartung sofortiger Konsequenzen, Misstrauen, Schuldgefühle",
             "Was hilft: zuhören ohne zu unterbrechen, Gefühle anerkennen",
             "Konkrete nächste Schritte nennen, Zeitplan und Zuständigkeiten klären",
             "INGRA: nie allein – immer mit TK oder Lehrkraft zusammen",
             "Beobachtungen sachlich einbringen, ohne Interpretation",
             "Schweigen, wenn TK oder Lehrkraft sprechen – kein Widerspruch vor Eltern",
             "Keine Versprechen machen, die nicht eingehalten werden können",
         ],
         merksatz="„Eltern wollen gehört werden — bevor sie informiert werden wollen.“",
         brainy="Eltern ernst nehmen ist der erste Schritt zu echter Zusammenarbeit."),

    dict(id_text="MB-15", icon="wachstum", titel="Nachsorge — nach dem Mobbing",
         fuer="Schulbegleitung – langfristige Beobachtung",
         lead="Nach der Intervention ist vor der Wiederholung. Ohne Nachsorge kehrt Mobbing in bis zu 40 % der Fälle zurück.",
         schritte=[
             "Wöchentlicher Barometer-Check mit besonderem Fokus",
             "Pausensituationen beobachten – wer spielt mit wem?",
             "Digitales Verhalten im Blick behalten – Hinweise des Kindes ernst nehmen",
             "Monatliche Kurznotiz an TK: Situation stabil oder Veränderungen?",
             "Selbstwirksamkeit des Kindes stärken – was ist ihm diese Woche gelungen?",
             "Soziale Einbindung fördern – Verteidiger aktivieren",
         ],
         merksatz="„Mobbing endet, wenn das Kind weiß: Ich bin nicht allein. Ich werde gesehen.“",
         brainy="Nachsorge ist kein Anhang — sie ist der entscheidende Teil der Intervention."),
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
