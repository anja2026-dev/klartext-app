#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baut alle 32 OGS-Basis-Karten (Vorder-/Rückseite PNG)."""
import os, glob, sys
sys.path.insert(0, os.path.dirname(__file__))
from build_card_ogs import build_front, build_back

BILDER = "/sessions/kind-beautiful-ptolemy/mnt/klartext-app/bilder/ogs/"
OUT = "/sessions/kind-beautiful-ptolemy/mnt/outputs/ogs_karten_komplett/"
os.makedirs(OUT, exist_ok=True)

def find_image(nr):
    for pattern in (f"OGS-{nr:02d}.jpg", f"OGS-{nr:02d} *.jpg", f"OGS-{nr:02d}.jpeg", f"OGS-{nr:02d}.png"):
        files = sorted(glob.glob(os.path.join(BILDER, pattern)))
        if files:
            return files[0]
    return None

# nr: (titel, anleitung, [frage1, frage2], systemfrage, tipp_fuer_dich, quelle)
CARDS = {
    # Block 1 – Gruppendynamik verstehen (Quelle: Tuckman 1965, bereits im Projekt verwendet)
    1: ("Die Gruppe gerade lesen",
        "Guter Einstieg, um die aktuelle Gruppenphase bewusst wahrzunehmen.",
        ["In welcher Phase steckt deine Gruppe gerade – neu zusammen, mitten im Aushandeln, oder schon eingespielt?",
         "Was verändert sich gerade spürbar in der Gruppe?"],
        "Wie reagiert die Gruppe als Ganzes, wenn ein einzelnes Kind fehlt?",
        "Jede Gruppe durchläuft diese Phasen mehrfach im Jahr – neue Kinder, Ferien, Jahreszeiten verändern die Dynamik immer wieder neu.",
        "Tuckman, B. W. (1965). Developmental Sequence in Small Groups – bereits im Projekt bestätigt."),
    2: ("Wenn zwei Grüppchen entstehen",
        "Für Momente, in denen sich die Gruppe sichtbar in kleinere Grüppchen aufteilt.",
        ["Woran erkennst du, dass sich hier zwei Grüppchen gebildet haben?",
         "Braucht das gerade eine Reaktion, oder ist das völlig normal?"],
        "Welche Rolle spielst du selbst dabei, ob sich Grüppchen verfestigen oder wieder mischen?",
        "Nicht jede Kleingruppe ist ein Problem – manche Kinder brauchen einfach einen kleineren Rahmen.",
        "Tuckman, B. W. (1965) – Gruppenphasenmodell, angewendet auf Kleingruppenbildung."),
    3: ("Unruhe im Raum verstehen",
        "Wenn die ganze Gruppe unruhig wirkt, ohne dass ein einzelnes Kind auffällig ist.",
        ["Was ist heute anders als sonst – Wetter, Personal, Tagesablauf?",
         "Steckt die Unruhe in einzelnen Kindern oder in der ganzen Gruppe?"],
        "Wie verändert sich die Stimmung, wenn du selbst ruhiger oder präsenter wirst?",
        "Gruppenstimmung ist ansteckend – in beide Richtungen.",
        "Tuckman, B. W. (1965) – Gruppendynamik, konzeptionell verwandt."),
    4: ("Die stille Mehrheit sehen",
        "Für den Blick auf Kinder, die in der Gruppendynamik wenig auffallen.",
        ["Welche Kinder hast du heute kaum wahrgenommen?",
         "Was würde sich ändern, wenn du bewusst zu ihnen gehst?"],
        "Wie verteilt sich deine Aufmerksamkeit normalerweise in der Gruppe – und warum?",
        "Laute Kinder bekommen oft mehr Aufmerksamkeit, nicht weil sie mehr brauchen, sondern weil sie mehr auffallen.",
        "KLARTEXT-Praxis, angelehnt an Gruppendynamik-Forschung (Tuckman 1965)."),

    # Block 2 – Rituale nutzen (Quelle: Wulf & Zirfas 2004, Rituale in der Pädagogik – vorgeschlagen)
    5: ("Der Start in den Nachmittag",
        "Für die Gestaltung eines verlässlichen Ankommens in der OGS.",
        ["Wie sieht das Ankommen bei euch gerade aus – gibt es einen festen Ablauf?",
         "Woran merkst du, ob ein Kind gut angekommen ist?"],
        "Was würde sich verändern, wenn jedes Kind ein festes Ankommens-Ritual hätte?",
        "Ein Ritual muss nicht groß sein – ein fester Gruß, ein fester Platz reicht oft schon.",
        "Wulf, C. & Zirfas, J. (2004). Die Kultur des Rituals – vorgeschlagen, bitte gegenprüfen."),
    6: ("Wenn ein Ritual nicht mehr trägt",
        "Für Situationen, in denen ein bewährtes Ritual plötzlich nicht mehr funktioniert.",
        ["Seit wann trägt das Ritual nicht mehr?",
         "Ist es das Ritual selbst, oder hat sich die Gruppe verändert?"],
        "Braucht die Gruppe gerade eher mehr oder weniger Struktur?",
        "Rituale dürfen sich mit der Gruppe weiterentwickeln – ein Ritual ist kein Gesetz.",
        "Wulf, C. & Zirfas, J. (2004) – vorgeschlagen, bitte gegenprüfen."),
    7: ("Signale statt Ansagen",
        "Für wiederkehrende Übergänge, die ohne viele Worte funktionieren sollen.",
        ["Welches Signal nutzt du schon – und verstehen es wirklich alle Kinder?",
         "Wo würde ein festes Signal Zeit und Nerven sparen?"],
        "Wie reagieren die Kinder auf dein Signal, wenn du selbst gestresst bist?",
        "Ein Signal wirkt nur, wenn es immer gleich bleibt – auch an stressigen Tagen.",
        "Visual Supports (Hodgdon, 1995) – konzeptionell verwandt, bereits im Projekt genutzt."),
    8: ("Rituale am Ende des Tages",
        "Für einen ruhigen, klaren Abschluss des Nachmittags.",
        ["Wie endet der Nachmittag bei euch gerade – fließend oder klar markiert?",
         "Was würde den Kindern helfen, gut loszulassen?"],
        "Was nehmen die Kinder aus deinem Abschluss-Ritual mit nach Hause?",
        "Ein guter Abschluss ist oft wichtiger als ein guter Anfang – er bleibt länger im Gedächtnis.",
        "Wulf, C. & Zirfas, J. (2004) – vorgeschlagen, bitte gegenprüfen."),

    # Block 3 – Konflikte begleiten (Quelle: Jefferys-Duden, Streitschlichter-Programm)
    9: ("Erst zuhören, dann handeln",
        "Für den ersten Moment, wenn ein Streit auffällt.",
        ["Was hast du wirklich gesehen, bevor du eingegriffen hast?",
         "Was hättest du übersehen, wenn du sofort reagiert hättest?"],
        "Wie oft greifst du ein, obwohl die Kinder es allein regeln könnten?",
        "Nicht jeder Streit braucht sofort einen Erwachsenen – manchmal reicht Beobachten aus der Nähe.",
        "Jefferys-Duden, K. – Streitschlichter-Programm – vorgeschlagen, bitte gegenprüfen."),
    10: ("Beide Seiten hören",
        "Für die eigentliche Streitschlichtung zwischen zwei Kindern.",
        ["Hat wirklich jedes Kind seine Version erzählen können?",
         "Wessen Version hast du zuerst geglaubt – und warum?"],
        "Welches Kind bekommt bei euch häufiger automatisch Recht?",
        "Die erste Version ist selten die ganze Geschichte.",
        "Jefferys-Duden, K. – Streitschlichter-Programm – vorgeschlagen, bitte gegenprüfen."),
    11: ("Wenn derselbe Streit wiederkommt",
        "Für wiederkehrende Konflikte zwischen denselben Kindern.",
        ["Was ist an diesem Streit eigentlich immer gleich?",
         "Was müsste sich strukturell ändern, damit der Streit nicht wiederkommt?"],
        "Sitzen, spielen oder warten diese Kinder regelmäßig an denselben Reibungspunkten?",
        "Wiederkehrende Konflikte sind oft ein Strukturproblem, kein Charakterproblem.",
        "Jefferys-Duden, K. – konzeptionell erweitert – vorgeschlagen, bitte gegenprüfen."),
    12: ("Lösung finden lassen",
        "Für den Moment, in dem die Kinder selbst eine Lösung entwickeln sollen.",
        ["Was schlagen die Kinder selbst vor, wenn du nicht gleich eine Lösung anbietest?",
         "Woran erkennst du, ob eine Lösung wirklich trägt?"],
        "Was traust du dieser Gruppe an eigener Konfliktlösung wirklich zu?",
        "Eine von Kindern selbst gefundene Lösung hält oft länger als eine vorgegebene.",
        "Jefferys-Duden, K. – Streitschlichter-Programm – vorgeschlagen, bitte gegenprüfen."),

    # Block 4 – Regeln vermitteln (Quelle: Nolting, Störungen in der Schulklasse)
    13: ("Wenige, klare Regeln",
        "Für den Grundstock an Regeln im OGS-Alltag.",
        ["Wie viele Regeln gelten bei euch gerade wirklich – und kennt sie jedes Kind?",
         "Welche Regel könntet ihr streichen, ohne dass etwas fehlt?"],
        "Gelten eure Regeln für alle Kinder gleich, oder gibt es stille Ausnahmen?",
        "Fünf Regeln, die wirklich gelten, wirken mehr als fünfzehn, die niemand kennt.",
        "Nolting, H.-P. – Störungen in der Schulklasse – vorgeschlagen, bitte gegenprüfen."),
    14: ("Regeln gemeinsam entwickeln",
        "Für die Beteiligung der Kinder an der Regelfindung.",
        ["Welche Regel würden die Kinder selbst vorschlagen, wenn du sie fragst?",
         "Was verändert sich, wenn eine Regel von den Kindern selbst kommt?"],
        "Wie viel Mitsprache trauen wir den Kindern bei Regeln wirklich zu?",
        "Mitbestimmte Regeln werden seltener gebrochen als verordnete.",
        "Nolting, H.-P. – vorgeschlagen, bitte gegenprüfen."),
    15: ("Eine Grenze halten",
        "Für Situationen, in denen eine Regel klar durchgesetzt werden muss.",
        ["Was macht es dir gerade schwer, konsequent zu bleiben?",
         "Was würde passieren, wenn du diese Grenze nicht hältst?"],
        "Wie reagiert die ganze Gruppe, wenn eine Regel bei einem Kind nicht gilt?",
        "Konsequent sein heißt nicht hart sein – nur verlässlich.",
        "Nolting, H.-P. – vorgeschlagen, bitte gegenprüfen."),
    16: ("Regeln überprüfen",
        "Für die regelmäßige Reflexion, ob bestehende Regeln noch passen.",
        ["Welche eurer Regeln ist eigentlich schon lange nicht mehr sinnvoll?",
         "Was hat sich in der Gruppe verändert, seit diese Regel entstand?"],
        "Wer würde es merken, wenn ihr eine überholte Regel einfach streicht?",
        "Regeln, die nie überprüft werden, verlieren irgendwann ihren Sinn – und ihre Wirkung.",
        "Nolting, H.-P. – vorgeschlagen, bitte gegenprüfen."),

    # Block 5 – Beziehungsarbeit im OGS (Quelle: Ahnert, Fachkraft-Kind-Bindung)
    17: ("Ankommen dürfen",
        "Für den ersten Kontakt mit einem neuen Kind in der Gruppe.",
        ["Was braucht dieses Kind gerade am meisten, um sich sicher zu fühlen?",
         "Wie zeigst du ihm, dass es willkommen ist, ohne es zu bedrängen?"],
        "Wie nimmt die bestehende Gruppe ein neues Kind normalerweise auf?",
        "Sicherheit entsteht nicht durch viele Worte, sondern durch verlässliche kleine Gesten.",
        "Ahnert, L. – Fachkraft-Kind-Bindung – vorgeschlagen, bitte gegenprüfen."),
    18: ("Die Stillen im Blick behalten",
        "Für Kinder, die sich zurückziehen, ohne aufzufallen.",
        ["Seit wann zieht sich dieses Kind zurück?",
         "Was würde es brauchen, um sich wieder zu zeigen?"],
        "Wie leicht übersiehst du ruhige Kinder im Trubel der Gruppe?",
        "Rückzug ist nicht immer ein Problem – aber er verdient immer einen zweiten Blick.",
        "Ahnert, L. – vorgeschlagen, bitte gegenprüfen."),
    19: ("Nähe zeigen, professionell bleiben",
        "Für die Balance zwischen echter Wärme und professioneller Distanz.",
        ["Woran merkst du bei dir selbst, wann Nähe genau richtig ist?",
         "Wo würdest du dir mehr Klarheit über deine eigene Rolle wünschen?"],
        "Wie unterscheidet sich deine Beziehung zu diesem Kind von der zu seinen Eltern?",
        "Bindung in der pädagogischen Arbeit ist real – und trotzdem nicht dasselbe wie eine Elternbindung.",
        "Ahnert, L. – Erzieherin-Kind-Bindung, Abgrenzung zur Eltern-Kind-Bindung – vorgeschlagen, bitte gegenprüfen."),
    20: ("Jedes Kind einmal am Tag",
        "Für die bewusste, individuelle Zuwendung im vollen Gruppenalltag.",
        ["Mit welchem Kind hattest du heute noch keinen direkten Moment?",
         "Was würde ein kurzer, echter Moment für dieses Kind bedeuten?"],
        "Wie verteilt sich deine Zuwendung über eine ganze Woche betrachtet?",
        "Ein kurzer, echter Moment wiegt oft mehr als eine lange, abgelenkte Aufmerksamkeit.",
        "Ahnert, L. – vorgeschlagen, bitte gegenprüfen."),

    # Block 6 – Selbstständigkeit fördern (Quelle: Deci & Ryan, Self-Determination Theory)
    21: ("Zutrauen statt Abnehmen",
        "Für Momente, in denen es leichter wäre, einem Kind etwas abzunehmen.",
        ["Was nimmst du diesem Kind gerade ab, das es eigentlich selbst könnte?",
         "Was hält dich davon ab, es zuzutrauen?"],
        "Wie würde sich die Gruppe verändern, wenn allen Kindern mehr zugetraut würde?",
        "Zutrauen fühlt sich manchmal langsamer an – ist aber meist der schnellere Weg.",
        "Deci, E. L. & Ryan, R. M. – Self-Determination Theory (Autonomieunterstützung)."),
    22: ("Scheitern erlauben",
        "Für Situationen, in denen ein Kind an einer Aufgabe zu scheitern droht.",
        ["Was würde passieren, wenn du jetzt nicht eingreifst?",
         "Wie könntest du begleiten, ohne zu übernehmen?"],
        "Was lernt dieses Kind aus einem Scheitern, das es aus Erfolg nicht lernen würde?",
        "Kleine, sichere Rückschläge sind oft die besten Lehrmeister.",
        "Deci, E. L. & Ryan, R. M. – Self-Determination Theory, konzeptionell verwandt."),
    23: ("Aufgaben mit echtem Wert",
        "Für die Vergabe kleiner Verantwortungen an Kinder.",
        ["Welche echte Aufgabe könnte ein Kind heute übernehmen?",
         "Woran würde das Kind merken, dass die Aufgabe wichtig ist?"],
        "Welche Aufgaben in eurem Alltag könnten grundsätzlich an Kinder abgegeben werden?",
        "Kinder spüren den Unterschied zwischen einer echten Aufgabe und einer Beschäftigung.",
        "Deci, E. L. & Ryan, R. M. – Self-Determination Theory (Kompetenzerleben)."),
    24: ("Geduld mit dem eigenen Tempo",
        "Für Momente, in denen ein Kind langsamer ist als der Gruppenrhythmus.",
        ["Wessen Zeitdruck ist das gerade – deiner oder der der Gruppe?",
         "Was würde sich ändern, wenn dieses Kind seine Zeit bekommt?"],
        "Wie geht die Gruppe mit einem Kind um, das sichtbar sein eigenes Tempo hat?",
        "Eigenes Tempo ist keine Verzögerung – es ist ein Zeichen von Selbstständigkeit.",
        "Deci, E. L. & Ryan, R. M. – Self-Determination Theory, konzeptionell verwandt."),

    # Block 7 – Übergänge gestalten (Quelle: Griebel & Niesel, Transitionsforschung)
    25: ("Von der Klasse in die OGS",
        "Für den täglichen Übergang aus dem Unterricht in den Ganztag.",
        ["Wie unterschiedlich fühlen sich Unterricht und OGS für die Kinder an?",
         "Was würde einen sanfteren Wechsel ermöglichen?"],
        "Wie viel Absprache gibt es zwischen Lehrkräften und OGS-Team über diesen Übergang?",
        "Der Übergang selbst ist oft anstrengender für Kinder als beide Bereiche einzeln.",
        "Griebel, W. & Niesel, R. (2004). Transitionsforschung – vorgeschlagen, bitte gegenprüfen."),
    26: ("Vom Spiel zur Hausaufgabe",
        "Für den Wechsel von freier Zeit zu konzentrierter Arbeit.",
        ["Wie kündigst du diesen Wechsel gerade an?",
         "Was würde den Kindern helfen, leichter umzuschalten?"],
        "Welche Rolle spielt der Zeitpunkt dieses Übergangs für die ganze Gruppe?",
        "Ein Vorlauf von wenigen Minuten reicht oft, um einen Wechsel deutlich leichter zu machen.",
        "Griebel, W. & Niesel, R. (2004) – vorgeschlagen, bitte gegenprüfen."),
    27: ("Abholsituationen entspannen",
        "Für den oft hektischen Moment der Abholung.",
        ["Was macht die Abholzeit bei euch gerade stressig?",
         "Was würde einen ruhigeren Übergang an die Eltern ermöglichen?"],
        "Wie viel Information gebt ihr Eltern in diesem kurzen Moment wirklich weiter?",
        "Ein kurzer, klarer Satz an die Eltern ist oft wertvoller als viele hastige.",
        "Griebel, W. & Niesel, R. (2004) – Mikrotransitionen, konzeptionell erweitert."),
    28: ("Ferien und besondere Tage",
        "Für Übergänge außerhalb des normalen Alltagsrhythmus.",
        ["Was ist an Ferientagen für die Kinder besonders unsicher?",
         "Welches Stück Alltagsstruktur könnte auch an diesen Tagen bleiben?"],
        "Wie unterschiedlich reagieren einzelne Kinder auf den Bruch der gewohnten Struktur?",
        "Gerade an Ausnahmetagen hilft ein kleines Stück Vertrautem am meisten.",
        "Griebel, W. & Niesel, R. (2004) – vorgeschlagen, bitte gegenprüfen."),

    # Block 8 – Rahmen und Zusammenarbeit (ergänzt 30.07.2026, auf Basis externer Analyse + Anjas Freigabe)
    29: ("Wenn ein Kind anders reagiert",
        "Für Situationen mit einem Kind, dessen Verhalten immer wieder herausfordert – ohne Diagnose oder Ferndiagnose.",
        ["Was passiert unmittelbar bevor sich das Verhalten zeigt?",
         "Was würde diesem Kind gerade wirklich helfen – nicht nur, was würde dich entlasten?"],
        "Wie reagiert die Gruppe, wenn dieses Kind sich anders verhält als erwartet?",
        "Verhalten ist Kommunikation. Je ruhiger dein eigener Ton bleibt, desto eher beruhigt sich die Situation.",
        "Hejlskov Elvén, B. (2022). Keine Macht den Mächtigen: Warum Zwang und Druck in der Erziehung "
        "scheitern. Probst. – bereits im Projekt bestätigt (AT-Deck, 26.07.2026)."),
    30: ("Wer ist wofür zuständig?",
        "Für Situationen, in denen im Team unklar ist, wer die Verantwortung für ein Kind oder ein Thema trägt.",
        ["Wer hat sich heute eigentlich schon um dieses Thema gekümmert – und wer nicht?",
         "Was würde sich klären, wenn ihr die Zuständigkeit einmal offen ansprecht?"],
        "Wie verteilt sich Verantwortung in eurem Team normalerweise – zufällig oder klar vereinbart?",
        "Unklare Zuständigkeit ist selten Bequemlichkeit – meist fehlt einfach ein kurzes Gespräch darüber.",
        "Speck, K., Olk, T., Böhm-Kasper, O., Stolz, H.-J. & Wiezorek, C. (Hrsg.) (2011). Ganztagsschulische "
        "Kooperation und Professionsentwicklung. Juventa. – vorgeschlagen, bitte gegenprüfen."),
    31: ("Wenn Hausaufgaben zum Kampf werden",
        "Für wiederkehrende Konflikte rund um die Hausaufgabenzeit im Ganztag.",
        ["Wo genau entsteht der Streit – bei der Aufgabe selbst oder beim Drumherum?",
         "Was wäre dein kleinster nächster Schritt, um aus dem Kampf auszusteigen?"],
        "Wessen Erwartung an die Hausaufgabenzeit prägt gerade den Konflikt – deine, die der Eltern oder die der Schule?",
        "Nicht jede Hausaufgaben-Verantwortung muss bei dir liegen – manchmal hilft es, das offen auszusprechen.",
        "Thematischer Transfer aus EL-22 („Hausaufgaben ohne Kampf“) auf die OGS-Perspektive – keine neue "
        "Quelle nötig."),
    32: ("Der Raum als stille Fachkraft",
        "Für den Blick auf Räume und Materialien als Teil der pädagogischen Arbeit, nicht nur als Rahmen dafür.",
        ["Was sagt dieser Raum gerade über das, was hier erlaubt und erwünscht ist?",
         "Welche kleine Veränderung am Raum würde am meisten bewirken?"],
        "Wie oft sprecht ihr im Team bewusst über die Wirkung eurer Räume – und nicht nur über ihre Nutzung?",
        "Ein Raum erzieht mit, ob gewollt oder nicht. Es lohnt sich, ihn regelmäßig neu zu betrachten.",
        "Rinaldi, C. (2006). In Dialogue with Reggio Emilia: Listening, Researching and Learning. Routledge. "
        "– Konzept „Raum als dritter Erzieher“ (Malaguzzi) – vorgeschlagen, bitte gegenprüfen."),
}

BLOCK_BADGE = {
    range(1, 5): "OGS · GRUPPENDYNAMIK",
    range(5, 9): "OGS · RITUALE",
    range(9, 13): "OGS · KONFLIKTE",
    range(13, 17): "OGS · REGELN",
    range(17, 21): "OGS · BEZIEHUNGSARBEIT",
    range(21, 25): "OGS · SELBSTSTÄNDIGKEIT",
    range(25, 29): "OGS · ÜBERGÄNGE",
    range(29, 33): "OGS · RAHMEN & TEAM",
}

def badge_for(nr):
    for rng, label in BLOCK_BADGE.items():
        if nr in rng:
            return label
    return "OGS · OFFENER GANZTAG"

def run():
    for nr in range(1, 33):
        titel, anleitung, fragen, systemfrage_text, tipp, quelle = CARDS[nr]
        card = dict(
            nr=nr,
            id_text=f"OGS-{nr:02d}",
            total=len(CARDS),
            badge=badge_for(nr),
            titel=titel,
            anleitung=anleitung,
            fragen=fragen,
            systemfrage=("SYSTEMISCH GEDACHT", systemfrage_text),
            hinweis=tipp,
            footer_deck="OGS-Basis-Deck",
        )
        image_path = find_image(nr)
        front_out = os.path.join(OUT, f"OGS-{nr:02d}_front.png")
        back_out = os.path.join(OUT, f"OGS-{nr:02d}_back.png")
        build_front(card, image_path or "", front_out)
        build_back(card, back_out)
        status = "mit Bild" if image_path else "OHNE BILD (Platzhalter)"
        print(f"OGS-{nr:02d}: {status} – {titel}")

if __name__ == "__main__":
    run()
