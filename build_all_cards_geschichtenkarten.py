#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rendert alle 30 Geschichtenkarten. Text unveraendert aus M6_Geschichtenkarten_Galerie.html
uebernommen (Content-Treuepflicht). Bilder werden erwartet unter bilder/geschichtenkarten/{ID}.png
(z.B. bilder/geschichtenkarten/A1.png) - falls noch nicht vorhanden, wird ein Platzhalter gerendert
(siehe build_card_geschichtenkarten.py)."""
import os, glob, sys
sys.path.insert(0, os.path.dirname(__file__))
from build_card_geschichtenkarten import build_front, build_back

OUT_DIR = "/sessions/kind-beautiful-ptolemy/mnt/outputs/geschichtenkarten_komplett/"
BILDER_DIR = "/sessions/kind-beautiful-ptolemy/mnt/klartext-app/bilder/geschichtenkarten/"
os.makedirs(OUT_DIR, exist_ok=True)

def find_image(id_text):
    """Bilder kamen als .jpg an (nicht .png wie urspruenglich im Prompt-Dateiname angegeben) -
    robuste Suche wie bei KD/FS ueber mehrere Endungen."""
    for pattern in (f"{id_text}.png", f"{id_text}.jpg", f"{id_text}.jpeg", f"{id_text} *.jpg"):
        files = sorted(glob.glob(os.path.join(BILDER_DIR, pattern)))
        if files:
            return files[0]
    return os.path.join(BILDER_DIR, f"{id_text}.png")  # Fallback: nicht vorhanden -> Platzhalter

CARDS = [
    # ═══ SET A · BRAINY ERLEBT MOBBING ═══
    dict(id_text="A1", set="A", titel="Brainy wird ausgelacht",
         situation="Brainy erzählt etwas, zwei Kinder lachen. Brainy wird klein und grau.",
         fragen=["Was fühlt Brainy?", "Warum tut das weh?", "Was könnte Brainy helfen?"],
         impuls="Brainy könnte sagen: Hör bitte auf. Das verletzt mich."),
    dict(id_text="A2", set="A", titel="Brainy wird ausgeschlossen",
         situation="Eine Gruppe spielt. Brainy steht daneben. Niemand reagiert.",
         fragen=["Warum fühlt sich Brainy allein?", "Was könnte Brainy Mut machen?", "Was würdest du tun?"],
         impuls="Brainy könnte fragen: Kann ich mitmachen?"),
    dict(id_text="A3", set="A", titel="Brainy bekommt gemeine Nachrichten",
         situation="Auf dem Tablet steht: Du bist dumm.",
         fragen=["Was macht das mit Brainy?", "Was sollte Brainy NICHT tun?", "Wer kann helfen?"],
         impuls="Brainy könnte sagen: Ich zeige das einem Erwachsenen."),
    dict(id_text="A4", set="A", titel="Brainy wird geschubst",
         situation="Brainy stolpert, ein Kind lacht.",
         fragen=["Warum ist das nicht okay?", "Was braucht Brainy?", "Was wäre sicher?"],
         impuls="Brainy könnte weggehen und Hilfe holen."),
    dict(id_text="A5", set="A", titel="Brainy wird bedroht",
         situation="Ein Kind sagt: Wenn du was sagst, passiert was.",
         fragen=["Warum macht das Angst?", "Was braucht Brainy?", "Wer kann schützen?"],
         impuls="Brainy könnte sofort zu einer erwachsenen Person gehen."),
    dict(id_text="A6", set="A", titel="Brainy wird nachgeäfft",
         situation="Brainy spricht, ein Kind imitiert ihn spöttisch.",
         fragen=["Was fühlt Brainy?", "Warum ist das unfair?", "Was wäre ein guter Schritt?"],
         impuls="Brainy könnte sagen: Ich möchte so nicht behandelt werden."),
    dict(id_text="A7", set="A", titel="Brainy wird ignoriert",
         situation="Brainy spricht, niemand reagiert.",
         fragen=["Warum tut Ignorieren weh?", "Was könnte Brainy helfen?", "Was würdest du Brainy raten?"],
         impuls="Brainy könnte sagen: Ich möchte gehört werden."),
    dict(id_text="A8", set="A", titel="Brainy wird beschämt",
         situation="Brainy macht einen Fehler, andere lachen.",
         fragen=["Was fühlt Brainy?", "Was hilft bei Scham?", "Was wäre freundlich?"],
         impuls="Brainy könnte sagen: Bitte hör auf. Das ist mir unangenehm."),
    dict(id_text="A9", set="A", titel="Brainy sieht, wie jemand anderes gemobbt wird",
         situation="Ein Kind wird ausgelacht. Brainy schaut unsicher.",
         fragen=["Was fühlt Brainy?", "Was wäre mutig?", "Wie kann Brainy helfen?"],
         impuls="Brainy könnte jemanden holen, der helfen kann."),
    dict(id_text="A10", set="A", titel="Brainy traut sich nicht, etwas zu sagen",
         situation="Brainy wurde verletzt, schweigt aber.",
         fragen=["Warum schweigt Brainy?", "Was könnte Mut machen?", "Wem könnte Brainy vertrauen?"],
         impuls="Brainy könnte sagen: Ich brauche jemanden, der mir zuhört."),

    # ═══ SET B · BRAINY HILFT ANDEREN ═══
    dict(id_text="B1", set="B", titel="Brainy sagt Stopp",
         situation="Brainy sieht, wie ein Kind ausgelacht wird. Er stellt sich daneben und sagt ruhig: Stopp. Das ist nicht okay.",
         fragen=["Was fühlt Brainy in diesem Moment?", "Warum ist Stopp sagen mutig?", "Was könnte danach passieren?"],
         impuls="Brainy könnte sagen: Ich möchte, dass du aufhörst."),
    dict(id_text="B2", set="B", titel="Brainy holt Hilfe",
         situation="Brainy sieht, dass ein Kind geschubst wird. Er geht sofort zu einer Lehrkraft und sagt: Ich brauche Hilfe.",
         fragen=["Warum ist Hilfe holen wichtig?", "Wen kann Brainy ansprechen?", "Was ist daran mutig?"],
         impuls="Brainy könnte sagen: Komm bitte mit, ich brauche Unterstützung."),
    dict(id_text="B3", set="B", titel="Brainy tröstet jemanden",
         situation="Ein Kind sitzt traurig auf der Bank. Brainy setzt sich daneben und sagt: Ich bin da.",
         fragen=["Warum hilft es, nicht allein zu sein?", "Was könnte Brainy noch tun?", "Was hilft dir, wenn du traurig bist?"],
         impuls="Brainy könnte sagen: Du bist nicht allein."),
    dict(id_text="B4", set="B", titel="Brainy stärkt einen Verteidiger",
         situation="Ein anderes Kind sagt Hör auf!. Brainy nickt und stellt sich dazu.",
         fragen=["Warum ist es leichter, wenn man nicht allein ist?", "Was macht Brainy hier richtig?", "Wie fühlt sich das Opfer jetzt?"],
         impuls="Brainy könnte sagen: Ich bin bei dir."),
    dict(id_text="B5", set="B", titel="Brainy meldet etwas sicher",
         situation="Brainy sieht eine gemeine Nachricht. Er zeigt sie einer erwachsenen Person, ohne sie weiterzuleiten.",
         fragen=["Warum ist Weiterleiten falsch?", "Was ist sichere Meldung?", "Wen kann Brainy informieren?"],
         impuls="Brainy könnte sagen: Ich möchte das melden, weil es unfair ist."),
    dict(id_text="B6", set="B", titel="Brainy begleitet jemanden",
         situation="Ein Kind hat Angst, in die Pause zu gehen. Brainy sagt: Ich gehe mit dir.",
         fragen=["Warum hilft Begleitung?", "Was könnte Brainy beachten?", "Was wäre ein guter nächster Schritt?"],
         impuls="Brainy könnte sagen: Wir gehen zusammen."),
    dict(id_text="B7", set="B", titel="Brainy zeigt Mut",
         situation="Brainy sieht eine ungerechte Situation und sagt: Das fühlt sich nicht richtig an.",
         fragen=["Warum ist das mutig?", "Was könnte Brainy danach tun?", "Was hilft, wenn man unsicher ist?"],
         impuls="Brainy könnte sagen: Ich möchte, dass wir fair bleiben."),
    dict(id_text="B8", set="B", titel="Brainy schützt jemanden",
         situation="Ein Kind wird bedroht. Brainy stellt sich daneben und sagt: Ich bleibe bei dir.",
         fragen=["Warum hilft Nähe?", "Was darf Brainy NICHT tun?", "Wer kann zusätzlich helfen?"],
         impuls="Brainy könnte sagen: Ich bleibe hier, bis Hilfe kommt."),
    dict(id_text="B9", set="B", titel="Brainy erklärt, warum etwas weh tut",
         situation="Brainy sagt zu einem Kind: Wenn du so redest, tut mir das weh.",
         fragen=["Warum ist das wichtig?", "Wie fühlt sich das Opfer?", "Was könnte danach passieren?"],
         impuls="Brainy könnte sagen: Ich möchte freundlich behandelt werden."),
    dict(id_text="B10", set="B", titel="Brainy zeigt Grenzen",
         situation="Brainy sagt klar: Ich möchte nicht, dass du mich so behandelst.",
         fragen=["Warum sind Grenzen wichtig?", "Wie fühlt sich Brainy danach?", "Was wäre ein guter nächster Schritt?"],
         impuls="Brainy könnte sagen: Stopp. Das möchte ich nicht."),

    # ═══ SET C · BRAINY LERNT STRATEGIEN ═══
    dict(id_text="C1", set="C", titel="Brainy übt Ich-Botschaften",
         situation="Brainy sagt: Ich fühle mich schlecht, wenn du mich auslachst.",
         fragen=["Warum helfen Ich-Botschaften?", "Wie klingt das freundlich?", "Was könnte Brainy noch sagen?"],
         impuls="Brainy könnte sagen: Ich brauche, dass du aufhörst."),
    dict(id_text="C2", set="C", titel="Brainy übt Grenzen setzen",
         situation="Brainy sagt: Nein, ich möchte das nicht.",
         fragen=["Warum ist Nein sagen schwer?", "Was hilft dabei?", "Wie kann Brainy ruhig bleiben?"],
         impuls="Brainy könnte sagen: Ich entscheide das für mich."),
    dict(id_text="C3", set="C", titel="Brainy übt Weggehen",
         situation="Brainy merkt, dass eine Situation kippt. Er dreht sich um und geht.",
         fragen=["Warum ist Weggehen klug?", "Was schützt Brainy dadurch?", "Wohin könnte er gehen?"],
         impuls="Brainy könnte sagen: Ich gehe jetzt weg."),
    dict(id_text="C4", set="C", titel="Brainy übt Hilfe holen",
         situation="Brainy sagt: Ich brauche Unterstützung.",
         fragen=["Wen kann Brainy ansprechen?", "Warum ist das kein Petzen?", "Was passiert danach?"],
         impuls="Brainy könnte sagen: Kannst du mir helfen?"),
    dict(id_text="C5", set="C", titel="Brainy übt digitale Sicherheit",
         situation="Brainy bekommt eine gemeine Nachricht und macht sofort einen Screenshot.",
         fragen=["Warum ist das wichtig?", "Was darf Brainy NICHT tun?", "Wen informiert Brainy?"],
         impuls="Brainy könnte sagen: Ich sichere das und hole Hilfe."),
    dict(id_text="C6", set="C", titel="Brainy übt Selbstschutz",
         situation="Brainy merkt, dass er Angst bekommt. Er geht zu einem sicheren Ort.",
         fragen=["Was ist ein sicherer Ort?", "Was hilft Brainy, ruhig zu werden?", "Wen könnte er informieren?"],
         impuls="Brainy könnte sagen: Ich brauche kurz Sicherheit."),
    dict(id_text="C7", set="C", titel="Brainy übt Mut",
         situation="Brainy hebt die Hand und sagt: Ich möchte etwas sagen.",
         fragen=["Warum ist das mutig?", "Was könnte Brainy sagen?", "Was hilft bei Unsicherheit?"],
         impuls="Brainy könnte sagen: Ich probiere es."),
    dict(id_text="C8", set="C", titel="Brainy übt Teamarbeit",
         situation="Brainy sagt zu einem anderen Kind: Lass uns zusammenhalten.",
         fragen=["Warum hilft Teamarbeit?", "Was stärkt eine Gruppe?", "Was könnte Brainy tun?"],
         impuls="Brainy könnte sagen: Wir schaffen das gemeinsam."),
    dict(id_text="C9", set="C", titel="Brainy übt Ruhe",
         situation="Brainy atmet tief ein, bevor er reagiert.",
         fragen=["Warum hilft Atmen?", "Was passiert im Körper?", "Was könnte Brainy danach tun?"],
         impuls="Brainy könnte sagen: Ich brauche kurz Ruhe."),
    dict(id_text="C10", set="C", titel="Brainy übt Nein sagen",
         situation="Brainy sagt klar: Nein, ich mache da nicht mit.",
         fragen=["Warum ist das wichtig?", "Was schützt Brainy dadurch?", "Was könnte danach passieren?"],
         impuls="Brainy könnte sagen: Ich entscheide das selbst."),
]

def run():
    for card in CARDS:
        image_path = find_image(card['id_text'])
        vorn = os.path.join(OUT_DIR, f"{card['id_text']}_Vorderseite.png")
        hinten = os.path.join(OUT_DIR, f"{card['id_text']}_Rueckseite.png")
        build_front(card, image_path, vorn)
        build_back(card, hinten)
        print(f"{card['id_text']} fertig")

if __name__ == "__main__":
    run()
