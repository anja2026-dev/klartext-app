#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2-Seiten-Handbuch-Booklets fürs Zonen-Set (Jugendliche Sek I/II): Schule (LK & INGRA gemeinsam,
da beide Rollen dasselbe Token-System im selben Raum nutzen) + Eltern (Zuhause). Nutzt dieselben
Zeichenhelfer wie build_booklet_insel.py."""
from PIL import ImageFont
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from build_booklet_insel import (new_page, footer, draw_h2, draw_para, draw_bullet,
                                  draw_numbered_short, wrap, draw_digitalzugang, KT_INK, KT_MUTED,
                                  F_SANS_REG, MARGIN)

ZONEN_4 = ["Rückzugs-Zone", "Fokus-Zone", "Klärungs-Zone", "Gesprächs-Zone"]

MINI_ANLEITUNG_ZONEN = [
    "Kleine Zonen-Markierung (A6) ausdrucken, laminieren – bewusst dezent, nicht auffällig platzieren",
    "Token-Karten-Sheets ausdrucken, ausschneiden, laminieren – pro Person 1 Set aus 4 Karten (1 je Zone)",
    "Ablage/Postfach für Token festlegen (z. B. kleine Box beim Pult) – Ort vorher mit der Gruppe klären",
    "Fertige Vinyl-Aufkleber nur auf Anfrage, kein Standard-Bestandteil des Sets",
]

def schule_seite1():
    img, d, y = new_page("GEBRAUCHSANWEISUNG", "Zonen-Set – Schule (LK & INGRA)")
    y = draw_h2(d, y, "Ziel")
    y = draw_para(d, y, "Jugendliche brauchen dieselbe Orientierung wie jüngere Kinder (Zustand → Ort "
                  "statt Zustand → Verhalten), aber ohne Bühne. Das Zonen-Set überträgt das Prinzip des "
                  "Insel-Sets auf Sek I/II: weniger Zonen, unauffälligere Markierung, Selbstwahl per "
                  "Token statt sichtbarem Hingehen.")
    y += mm_gap()
    y = draw_h2(d, y, "Prinzipien")
    for p in ["Diskretion vor Sichtbarkeit – anders als beim Kinder-Set bewusst umgekehrt",
              "Selbstwahl statt Fremdzuweisung (Autonomie, Deci & Ryan)",
              "Wenige, klare Zonen statt vieler kleinteiliger",
              "Kein Maskottchen – altersangemessene, nüchterne Gestaltung"]:
        y = draw_bullet(d, y, p)
    y += mm_gap(4)
    y = draw_h2(d, y, "Die 4 Zonen")
    y = draw_para(d, y, " · ".join(ZONEN_4), size=4.2, color=KT_MUTED)
    y += mm_gap(6)
    y = draw_h2(d, y, "Token-Karten statt sichtbares Hingehen")
    y = draw_para(d, y, "Jede/r Jugendliche bekommt 4 Token-Karten (eine pro Zone). Wer eine Zone "
                  "braucht, legt die passende Karte auf eine vereinbarte Ablage – ohne Ansage vor der "
                  "Klasse. Die Lehrkraft/INGRA bestätigt kurz (Blickkontakt, Nicken), keine öffentliche "
                  "Reaktion nötig.")
    y += mm_gap(6)
    y = draw_h2(d, y, "Einbindung in Barometer & kLAR")
    y = draw_para(d, y, "Grün: alle Zonen frei per Token wählbar. Gelb: Rückzugs- oder Fokus-Zone "
                  "selbstständig per Token. Orange: Rückzugs-Zone = kLAR-Schritt R (Reizreduktion & "
                  "Rückzug), Gesprächs-Zone = kLAR-Schritte K & A (Kontakt, Anerkennung) – LK/INGRA "
                  "begleitet aktiv, Token allein reicht nicht mehr. Rot: keine freie Zonenwahl, "
                  "Feuerwehr-Protokoll gilt. Grau: erschöpft oder orientierungslos – weiß selbst nicht, "
                  "was er/sie braucht. Rückzugs-Zone, nicht drängen.")
    footer(d, "Zonen-Set · Schule", "Handbuch · 1/2")
    return img

def schule_seite2():
    img, d, y = new_page("GEBRAUCHSANWEISUNG", "Umsetzung, Anleitung & Quellen")
    y = draw_h2(d, y, "Umsetzung")
    for i, s in enumerate([
        "Zonen im Raum festlegen, klein/dezent markieren – nicht als Blickfang gestalten",
        "Token-System einmalig der Gruppe erklären, ohne es zu erzwingen",
        "Ablage für Token einrichten, regelmäßig unauffällig prüfen",
        "Nach 2–3 Wochen reflektieren: wird das System genutzt, muss etwas angepasst werden?"], 1):
        y = draw_numbered_short(d, y, i, s)
    y += mm_gap(4)
    y = draw_h2(d, y, "Mini-Anleitung: Zonen-Markierung & Token anbringen")
    for i, s in enumerate(MINI_ANLEITUNG_ZONEN, 1):
        y = draw_numbered_short(d, y, i, s)
    y += mm_gap(4)
    y = draw_h2(d, y, "Quellen")
    f_q = ImageFont.truetype(F_SANS_REG_PATH(), mm_(4.1))
    quellen = [
        "Kuypers, L. (2011). The Zones of Regulation – Grundprinzip, deckt explizit auch Sek-I-Alter ab.",
        "Siegel, D. (1999). The Developing Mind – Window of Tolerance.",
        "Deci, E. & Ryan, R. – Selbstbestimmungstheorie, bereits für OGS-Block „Selbstständigkeit“ verwendet.",
        "Reeve, J. (2006). Teachers as Facilitators – autonomieförderende Klassenführung.",
    ]
    for q in quellen:
        for ln in wrap(d, q, f_q, content_w()):
            d.text((MARGIN + mm_(4), y), ln, font=f_q, fill=KT_INK)
            y += mm_(6.3)
        y += mm_(1.5)
    y += mm_(2)
    y = draw_para(d, y, "Kuypers und Siegel bereits im KLARTEXT-Register bestätigt. Deci & Ryan "
                  "etabliert. Reeve 2006 vorgeschlagen, bitte gegenprüfen.", size=3.9, color=(150, 120, 50))
    y += mm_(5)
    y = draw_digitalzugang(img, d, y, "https://karten.klartext-mentoring.de/?deck=zonen-schule", "qj874v")
    footer(d, "Zonen-Set · Schule", "Handbuch · 2/2")
    return img

def eltern_seite1():
    img, d, y = new_page("GEBRAUCHSANWEISUNG", "Zonen-Set – Zuhause (Eltern)")
    y = draw_h2(d, y, "Ziel")
    y = draw_para(d, y, "Auch zuhause hilft Jugendlichen ein fester, benannter Ort mehr als eine "
                  "Diskussion in der Situation selbst. Das Zonen-Set überträgt dieselben 4 Zonen aus der "
                  "Schule auf den Familienalltag – gleiche Bilder, gleiche Farben, damit Jugendliche das "
                  "System wiedererkennen.")
    y += mm_gap()
    y = draw_h2(d, y, "Prinzipien")
    for p in ["Rückzug ohne Rechtfertigung ermöglichen", "Autonomie respektieren, nicht kontrollieren",
              "Gleiche Zonen wie in der Schule – Wiedererkennung entlastet",
              "Kein Kleinkind-Design – altersangemessen bleiben"]:
        y = draw_bullet(d, y, p)
    y += mm_gap(4)
    y = draw_h2(d, y, "Die 4 Zonen zuhause")
    y = draw_para(d, y, " · ".join(ZONEN_4), size=4.2, color=KT_MUTED)
    y += mm_gap(6)
    y = draw_h2(d, y, "Token-Karten auch zuhause nutzbar")
    y = draw_para(d, y, "Optional: dieselben Token-Karten wie in der Schule (z. B. auf die Küchentheke "
                  "legen), wenn das Kind im Schulkontext bereits daran gewöhnt ist. Kein separater Druck "
                  "nötig – gleiche Vorlage wie fürs Schul-Set.")
    footer(d, "Zonen-Set · Zuhause", "Handbuch · 1/2")
    return img

def eltern_seite2():
    img, d, y = new_page("GEBRAUCHSANWEISUNG", "Umsetzung, Anleitung & Quellen")
    y = draw_h2(d, y, "Umsetzung")
    for i, s in enumerate([
        "Zonen zuhause festlegen (Zimmer-Ecke, Schreibtisch, neutraler Ort, Sofa) – klein markieren",
        "Kurz erklären, wofür jede Zone da ist – ohne es zur Pflicht zu machen",
        "Nutzung nicht kommentieren oder hinterfragen, wenn sie in Anspruch genommen wird",
        "Nach ein paar Wochen locker nachfragen, ob es hilft"], 1):
        y = draw_numbered_short(d, y, i, s)
    y += mm_gap(4)
    y = draw_h2(d, y, "Mini-Anleitung: Zonen-Markierung anbringen")
    for i, s in enumerate(MINI_ANLEITUNG_ZONEN[:3], 1):
        y = draw_numbered_short(d, y, i, s)
    y += mm_gap(4)
    y = draw_h2(d, y, "Quellen")
    f_q = ImageFont.truetype(F_SANS_REG_PATH(), mm_(4.1))
    quellen = [
        "Deci, E. & Ryan, R. – Selbstbestimmungstheorie, Autonomiebedürfnis im Jugendalter.",
        "Siegel, D. (1999). The Developing Mind – Window of Tolerance.",
        "Kuypers, L. (2011). The Zones of Regulation.",
    ]
    for q in quellen:
        for ln in wrap(d, q, f_q, content_w()):
            d.text((MARGIN + mm_(4), y), ln, font=f_q, fill=KT_INK)
            y += mm_(6.3)
        y += mm_(1.5)
    y += mm_(2)
    y = draw_para(d, y, "Kuypers und Siegel bereits im KLARTEXT-Register bestätigt. Deci & Ryan etabliert.",
                  size=3.9, color=(150, 120, 50))
    y += mm_(5)
    y = draw_digitalzugang(img, d, y, "https://karten.klartext-mentoring.de/?deck=zonen-eltern", "ay3e6j")
    footer(d, "Zonen-Set · Zuhause", "Handbuch · 2/2")
    return img

# --- kleine Helfer, um mm()/MARGIN/CONTENT_W aus build_booklet_insel wiederzuverwenden ---
def mm_(v):
    from build_booklet_insel import mm as _mm
    return _mm(v)

def mm_gap(v=6):
    return mm_(v)

def content_w():
    from build_booklet_insel import CONTENT_W
    return CONTENT_W

def F_SANS_REG_PATH():
    return F_SANS_REG

if __name__ == "__main__":
    pages = {
        "zonen_schule1": schule_seite1(), "zonen_schule2": schule_seite2(),
        "zonen_eltern1": eltern_seite1(), "zonen_eltern2": eltern_seite2(),
    }
    for name, img in pages.items():
        img.save(f"/sessions/kind-beautiful-ptolemy/mnt/outputs/booklet_{name}.png")
        print(name, "ok")
