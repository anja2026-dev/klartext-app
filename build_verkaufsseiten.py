#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generator für alle restlichen KLARTEXT-Verkaufsseiten (10 Decks).
Wiederverwendet das etablierte Design-System (Navy/Mint/Cream/Gold, Playfair+DM Sans).
"""
import re, json
from collections import Counter

CSS = """
*{box-sizing:border-box;margin:0;padding:0;}
html{scroll-behavior:smooth;}
body{font-family:"DM Sans",sans-serif;background:#fff;color:#1A1A2E;}
.nav{background:#1B3A4B;padding:.75rem clamp(1rem,4vw,3rem);display:flex;align-items:center;justify-content:space-between;position:sticky;top:0;z-index:100;}
.nav-logo{font-family:"Playfair Display",serif;font-size:1.3rem;font-weight:700;color:#fff;text-decoration:none;}
.nav-logo span{color:#6EC6A0;}
.nav-cta{background:#6EC6A0;color:#1B3A4B;border:none;padding:.45rem 1.1rem;border-radius:20px;font-family:"DM Sans",sans-serif;font-size:.82rem;font-weight:700;cursor:pointer;text-decoration:none;}
.hero{background:linear-gradient(135deg,#1B3A4B 0%,#2A4A5B 60%,#1B3A4B 100%);padding:5rem clamp(1rem,5vw,4rem) 4rem;text-align:center;position:relative;overflow:hidden;}
.hero::before{content:"";position:absolute;top:-50%;left:-50%;width:200%;height:200%;background:radial-gradient(circle at 30% 50%,rgba(110,198,160,.08) 0%,transparent 60%);pointer-events:none;}
.hero-badge{display:inline-flex;align-items:center;gap:.4rem;background:rgba(110,198,160,.15);border:1px solid rgba(110,198,160,.4);border-radius:20px;padding:.3rem .85rem;font-size:.72rem;font-weight:700;color:#6EC6A0;letter-spacing:.1em;text-transform:uppercase;margin-bottom:1.25rem;}
.hero h1{font-family:"Playfair Display",serif;font-size:clamp(2rem,5vw,3.5rem);font-weight:900;color:#fff;line-height:1.15;margin-bottom:1rem;max-width:800px;margin-left:auto;margin-right:auto;}
.hero h1 span{color:#6EC6A0;}
.hero-sub{font-size:clamp(.95rem,2vw,1.15rem);color:rgba(255,255,255,.7);line-height:1.8;max-width:640px;margin:0 auto 2rem;}
.hero-cta-wrap{display:flex;gap:.75rem;justify-content:center;flex-wrap:wrap;margin-bottom:2.5rem;}
.btn-primary{background:#6EC6A0;color:#1B3A4B;padding:.75rem 2rem;border-radius:8px;font-family:"DM Sans",sans-serif;font-size:1rem;font-weight:700;text-decoration:none;display:inline-block;transition:all .2s;}
.btn-primary:hover{background:#5AB490;transform:translateY(-1px);}
.btn-secondary{background:transparent;color:#fff;border:1.5px solid rgba(255,255,255,.4);padding:.75rem 2rem;border-radius:8px;font-family:"DM Sans",sans-serif;font-size:1rem;font-weight:600;text-decoration:none;display:inline-block;}
.hero-stats{display:flex;gap:2rem;justify-content:center;flex-wrap:wrap;}
.hero-stat{text-align:center;}
.hero-stat .n{font-family:"Playfair Display",serif;font-size:1.8rem;font-weight:700;color:#6EC6A0;display:block;}
.hero-stat .l{font-size:.72rem;color:rgba(255,255,255,.5);letter-spacing:.08em;text-transform:uppercase;}
.sek{padding:4rem clamp(1rem,5vw,4rem);}
.sek-titel{font-family:"Playfair Display",serif;font-size:clamp(1.5rem,3vw,2.2rem);font-weight:700;color:#1B3A4B;text-align:center;margin-bottom:.5rem;}
.sek-sub{font-size:.95rem;color:#6A6878;text-align:center;margin-bottom:2.5rem;line-height:1.75;max-width:680px;margin-left:auto;margin-right:auto;}
.sek.grau{background:#F5F0E8;}
.sek.dunkel{background:#1B3A4B;}
.fuer-wen-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:1rem;max-width:900px;margin:0 auto;}
.fw-karte{background:#fff;border-radius:12px;border:1.5px solid #DDD8CE;padding:1.25rem 1.5rem;}
.fw-emoji{font-size:2rem;margin-bottom:.65rem;display:block;}
.fw-titel{font-family:"Playfair Display",serif;font-size:1rem;font-weight:700;color:#1B3A4B;margin-bottom:.4rem;}
.fw-desc{font-size:.83rem;color:#3A3A4A;line-height:1.75;}
.leistungen{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:1rem;max-width:1000px;margin:0 auto;}
.l-karte{background:#fff;border-radius:12px;padding:1.25rem 1.5rem;border-left:4px solid;}
.l-icon{font-size:1.5rem;margin-bottom:.5rem;display:block;}
.l-titel{font-size:.88rem;font-weight:700;color:#1B3A4B;margin-bottom:.3rem;}
.l-desc{font-size:.8rem;color:#3A3A4A;line-height:1.7;}
.block-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:.85rem;max-width:1000px;margin:0 auto;}
.block-karte{background:#fff;border-radius:10px;padding:1rem 1.1rem;border:1.5px solid #DDD8CE;}
.block-nr{font-family:"Playfair Display",serif;font-size:.75rem;font-weight:900;color:#6EC6A0;letter-spacing:.06em;}
.block-titel{font-size:.85rem;font-weight:700;color:#1B3A4B;margin-top:.2rem;line-height:1.4;}
.quellen-liste{max-width:750px;margin:0 auto;list-style:none;}
.quellen-liste li{font-size:.82rem;color:#3A3A4A;line-height:1.8;padding:.6rem 0;border-bottom:1px solid #DDD8CE;}
.quellen-liste li:last-child{border-bottom:none;}
.baro-grid{display:grid;grid-template-columns:repeat(5,1fr);gap:.5rem;max-width:800px;margin:0 auto 1.5rem;}
.baro-item{text-align:center;padding:.75rem .5rem;border-radius:10px;}
.baro-dot{width:36px;height:36px;border-radius:50%;margin:0 auto .4rem;}
.baro-name{font-size:.72rem;font-weight:700;color:#1B3A4B;}
.baro-desc{font-size:.65rem;color:#6A6878;margin-top:.2rem;line-height:1.4;}
.klar-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:.75rem;max-width:800px;margin:0 auto;}
.klar-item{background:#fff;border-radius:10px;padding:1rem;text-align:center;border-top:4px solid #C47A00;}
.klar-buch{font-family:"Playfair Display",serif;font-size:2.5rem;font-weight:900;color:#C47A00;display:block;line-height:1;}
.klar-titel{font-size:.8rem;font-weight:700;color:#1B3A4B;margin:.3rem 0;}
.klar-desc{font-size:.72rem;color:#6A6878;line-height:1.5;}
.preis-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:1.25rem;max-width:900px;margin:0 auto;}
.preis-karte{background:#fff;border-radius:14px;padding:1.75rem 1.5rem;border:1.5px solid #DDD8CE;text-align:center;position:relative;}
.preis-karte.highlight{border-color:#6EC6A0;border-width:2px;}
.preis-badge{position:absolute;top:-12px;left:50%;transform:translateX(-50%);background:#6EC6A0;color:#1B3A4B;font-size:.65rem;font-weight:700;padding:.25rem .85rem;border-radius:20px;letter-spacing:.1em;text-transform:uppercase;white-space:nowrap;}
.preis-name{font-family:"Playfair Display",serif;font-size:1.1rem;font-weight:700;color:#1B3A4B;margin-bottom:.5rem;}
.preis-betrag{font-family:"Playfair Display",serif;font-size:2.5rem;font-weight:900;color:#1B3A4B;display:block;margin:.5rem 0;}
.preis-betrag span{font-size:1rem;font-weight:400;color:#6A6878;}
.preis-was{font-size:.78rem;color:#6A6878;margin-bottom:1.25rem;line-height:1.7;}
.preis-liste{list-style:none;text-align:left;font-size:.8rem;color:#3A3A4A;margin-bottom:1.5rem;}
.preis-liste li{padding:.25rem 0;padding-left:1.25rem;position:relative;line-height:1.6;}
.preis-liste li::before{content:"✓";position:absolute;left:0;color:#6EC6A0;font-weight:700;}
.preis-btn{display:block;background:#1B3A4B;color:#fff;padding:.65rem 1.5rem;border-radius:8px;font-family:"DM Sans",sans-serif;font-size:.85rem;font-weight:700;text-decoration:none;transition:background .2s;}
.preis-btn:hover{background:#2A4A5B;}
.preis-karte.highlight .preis-btn{background:#6EC6A0;color:#1B3A4B;}
.preis-karte.highlight .preis-btn:hover{background:#5AB490;}
.zitat-wrap{max-width:700px;margin:0 auto;text-align:center;}
.zitat-text{font-family:"Playfair Display",serif;font-size:clamp(1.1rem,2.5vw,1.5rem);font-weight:700;color:#fff;line-height:1.6;margin-bottom:1rem;}
.zitat-autor{font-size:.82rem;color:rgba(255,255,255,.5);}
.ref-wrap{display:flex;gap:2rem;align-items:flex-start;max-width:780px;margin:0 auto;flex-wrap:wrap;}
.ref-bild{width:120px;height:120px;border-radius:50%;background:none;border:4px solid #6EC6A0;overflow:hidden;flex-shrink:0;display:flex;align-items:center;justify-content:center;padding:0;}
.ref-bild img{width:100%;height:100%;object-fit:cover;}
.ref-text h3{font-family:"Playfair Display",serif;font-size:1.3rem;font-weight:700;color:#1B3A4B;margin-bottom:.25rem;}
.ref-text .titel{font-size:.82rem;color:#6EC6A0;font-weight:700;margin-bottom:.75rem;display:block;}
.ref-text p{font-size:.85rem;color:#3A3A4A;line-height:1.85;}
.badge-liste{display:flex;flex-wrap:wrap;gap:.4rem;margin-top:.75rem;}
.badge{background:#F5F0E8;border:1px solid #DDD8CE;border-radius:20px;padding:.2rem .65rem;font-size:.72rem;color:#1B3A4B;font-weight:600;}
.faq-liste{max-width:700px;margin:0 auto;}
.faq-item{border-bottom:1px solid #DDD8CE;padding:1rem 0;}
.faq-frage{font-size:.9rem;font-weight:700;color:#1B3A4B;margin-bottom:.4rem;}
.faq-antwort{font-size:.83rem;color:#3A3A4A;line-height:1.8;}
.vorbestell-hinweis{max-width:700px;margin:0 auto 2.5rem;background:#FFF4E0;border:1.5px solid #F0D9A8;border-radius:12px;padding:1rem 1.25rem;text-align:center;font-size:.85rem;color:#6B4600;line-height:1.7;}
.vorbestell-hinweis strong{color:#8A5A00;}
.fach-hinweis-box{max-width:700px;margin:0 auto 2.5rem;background:#FDEAEA;border:1.5px solid #F5C6C6;border-radius:12px;padding:1rem 1.25rem;text-align:center;font-size:.85rem;color:#8A1F1F;line-height:1.7;}
.fach-hinweis-box strong{color:#C62828;}
.cta-final{text-align:center;padding:4rem clamp(1rem,5vw,4rem);background:linear-gradient(135deg,#1B3A4B,#2A4A5B);}
.cta-final h2{font-family:"Playfair Display",serif;font-size:clamp(1.5rem,3vw,2.2rem);color:#fff;margin-bottom:.75rem;}
.cta-final p{color:rgba(255,255,255,.6);margin-bottom:2rem;font-size:.95rem;max-width:520px;margin-left:auto;margin-right:auto;}
footer{background:#0F2535;padding:2rem clamp(1rem,4vw,3rem);text-align:center;font-size:.75rem;color:rgba(255,255,255,.35);}
footer a{color:rgba(255,255,255,.4);text-decoration:none;}
@media(max-width:600px){.baro-grid{grid-template-columns:repeat(3,1fr);}.klar-grid{grid-template-columns:repeat(2,1fr);}.ref-wrap{flex-direction:column;align-items:center;text-align:center;}}
"""

BARO_HTML = """
<section class="sek grau">
  <h2 class="sek-titel">Das Barometer — 5 Zustände</h2>
  <p class="sek-sub">Erkenne sofort, wo dein Kind gerade steht — und was jetzt hilft.</p>
  <div class="baro-grid">
    <div class="baro-item" style="background:#E8F5EE;"><div class="baro-dot" style="background:#2E7D47;"></div><div class="baro-name" style="color:#2E7D47;">GRÜN</div><div class="baro-desc">Stabil · lernbereit</div></div>
    <div class="baro-item" style="background:#FBF4E8;"><div class="baro-dot" style="background:#C47A00;"></div><div class="baro-name" style="color:#C47A00;">GELB</div><div class="baro-desc">Angespannt · aufmerksam</div></div>
    <div class="baro-item" style="background:#FEF0E8;"><div class="baro-dot" style="background:#D4500A;"></div><div class="baro-name" style="color:#D4500A;">ORANGE</div><div class="baro-desc">Dysreguliert → kLAR</div></div>
    <div class="baro-item" style="background:#FDEAEA;"><div class="baro-dot" style="background:#C62828;"></div><div class="baro-name" style="color:#C62828;">ROT</div><div class="baro-desc">Akute Krise → Feuerwehr</div></div>
    <div class="baro-item" style="background:#F0F0F0;"><div class="baro-dot" style="background:#6A6878;"></div><div class="baro-name" style="color:#6A6878;">GRAU</div><div class="baro-desc">Unklar · beobachten</div></div>
  </div>
</section>
<section class="sek">
  <h2 class="sek-titel">Das kLAR-Modell</h2>
  <p class="sek-sub">4 Schritte, wenn ein Kind dysreguliert ist — in dieser Reihenfolge, keinen überspringen.</p>
  <div class="klar-grid">
    <div class="klar-item"><span class="klar-buch">k</span><div class="klar-titel">Kontakt &amp; Sicherheit</div><div class="klar-desc">Augenhöhe · ruhige Haltung · "Ich bin da."</div></div>
    <div class="klar-item"><span class="klar-buch">L</span><div class="klar-titel">Leise &amp; Langsam</div><div class="klar-desc">Keine Fragen · keine Erklärungen · wenige Worte</div></div>
    <div class="klar-item"><span class="klar-buch">A</span><div class="klar-titel">Anerkennung &amp; Atmen</div><div class="klar-desc">"Das war zu viel." · gemeinsam atmen · keine Wertung</div></div>
    <div class="klar-item"><span class="klar-buch">R</span><div class="klar-titel">Reizreduktion &amp; Rückzug</div><div class="klar-desc">Raus aus der Situation · Reize minimieren · Ruheplatz</div></div>
  </div>
</section>
"""

def fw_card(emoji, titel, desc):
    return f'<div class="fw-karte"><span class="fw-emoji">{emoji}</span><div class="fw-titel">{titel}</div><div class="fw-desc">{desc}</div></div>'

def l_card(color, icon, titel, desc):
    return f'<div class="l-karte" style="border-color:{color};"><span class="l-icon">{icon}</span><div class="l-titel">{titel}</div><div class="l-desc">{desc}</div></div>'

def block_card(nr, titel):
    return f'<div class="block-karte"><div class="block-nr">{nr}</div><div class="block-titel">{titel}</div></div>'

def quelle_li(text):
    return f'<li>{text}</li>'

def faq_item(frage, antwort):
    return f'<div class="faq-item"><div class="faq-frage">{frage}</div><div class="faq-antwort">{antwort}</div></div>'

def preis_karte(name, betrag, unit, was, items, mail_subject, highlight=False, badge=None, btn_text="Vormerken"):
    cls = "preis-karte highlight" if highlight else "preis-karte"
    badge_html = f'<div class="preis-badge">{badge}</div>' if badge else ""
    items_html = "".join(f"<li>{i}</li>" for i in items)
    return f'''<div class="{cls}">
      {badge_html}
      <div class="preis-name">{name}</div>
      <span class="preis-betrag">{betrag}<span> {unit}</span></span>
      <div class="preis-was">{was}</div>
      <ul class="preis-liste">{items_html}</ul>
      <a href="mailto:anja.jolk@gmx.de?subject={mail_subject}" class="preis-btn">{btn_text}</a>
    </div>'''

REF_TEXT_P1 = "Die KLARTEXT-Materialien entstehen nicht aus der Theorie, sondern aus systemischer Praxis und sorgfältig geprüfter Fachliteratur."
REF_BADGES = ["Systemisches Coaching (SCGD/IHK)", "Fortbildung Transitionspsychiatrie (1.7, Prof. Dr. Fegert, Uniklinikum Ulm)", "Fachkraft für Integrationspädagogik", "Sprachentwicklungsexpertin", "4 Jahre Vertretungslehrkraft"]

def build_page(d):
    blocks_html = ""
    if d.get("blocks"):
        cards = "".join(block_card(nr, titel) for nr, titel in d["blocks"])
        blocks_html = f'''
<section class="sek grau">
  <h2 class="sek-titel">{d.get("blocks_titel","Themenblöcke")}</h2>
  <p class="sek-sub">{d.get("blocks_sub","")}</p>
  <div class="block-grid">{cards}</div>
</section>'''

    quellen_html = ""
    if d.get("quellen"):
        lis = "".join(quelle_li(q) for q in d["quellen"])
        quellen_html = f'''
<section class="sek">
  <h2 class="sek-titel">Wissenschaftliche Grundlage</h2>
  <p class="sek-sub">{d.get("quellen_sub","")}</p>
  <ul class="quellen-liste">{lis}</ul>
</section>'''

    baro_html = BARO_HTML if d.get("baro_klar") else ""

    fw_html = "".join(fw_card(*c) for c in d["fuer_wen"])
    l_html = "".join(l_card(*c) for c in d["leistungen"])

    hinweis_html = ""
    if d.get("fach_hinweis"):
        hinweis_html = f'<div class="fach-hinweis-box"><strong>Hinweis:</strong> {d["fach_hinweis"]}</div>'

    preis_html = "".join(d["preise"])
    faq_html = "".join(faq_item(*f) for f in d["faq"])

    return f'''<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{d["code"]} · {d["seiten_titel"]} | KLARTEXT</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Sans:wght@300;400;500;700&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>

<nav class="nav">
  <a class="nav-logo" href="/">KLAR<span>TEXT</span></a>
  <a class="nav-cta" href="#preise">Vormerken</a>
</nav>

<section class="hero">
  <div class="hero-badge">{d["hero_badge"]}</div>
  <h1>{d["hero_h1"]}</h1>
  <p class="hero-sub">{d["hero_sub"]}</p>
  <div class="hero-cta-wrap">
    <a href="#preise" class="btn-primary">Jetzt vormerken</a>
    <a href="#was-ist" class="btn-secondary">Mehr erfahren</a>
  </div>
  <div class="hero-stats">
    {"".join(f'<div class="hero-stat"><span class="n">{n}</span><span class="l">{l}</span></div>' for n,l in d["hero_stats"])}
  </div>
</section>

<section class="sek grau">
  <h2 class="sek-titel">Für wen ist {d["fuer_wen_titel"]}?</h2>
  <p class="sek-sub">{d.get("fuer_wen_sub","")}</p>
  <div class="fuer-wen-grid">{fw_html}</div>
</section>

<section class="sek" id="was-ist">
  <h2 class="sek-titel">Was bekommst du?</h2>
  <p class="sek-sub">{d.get("leistungen_sub","")}</p>
  <div class="leistungen">{l_html}</div>
</section>
{blocks_html}
{quellen_html}
{baro_html}
<section class="sek dunkel">
  <div class="zitat-wrap">
    <div class="zitat-text">{d["zitat"]}</div>
    <div class="zitat-autor">— Anja Jolk, KLARTEXT</div>
  </div>
</section>

<section class="sek grau" id="preise">
  <h2 class="sek-titel">{d["code"]} vormerken</h2>
  <p class="sek-sub">Einmalig zahlen — dauerhaft nutzen. Kein Abo, keine versteckten Kosten.</p>
  {hinweis_html}
  <div class="vorbestell-hinweis"><strong>{d["status_hinweis"]}</strong> Wir bereiten gerade Druck und Verkaufsstart vor. Trag dich jetzt schon unverbindlich ein, wir melden uns, sobald es bestellbar ist.</div>
  <div class="preis-grid">{preis_html}</div>
</section>

<section class="sek">
  <h2 class="sek-titel">Die Entwicklerin</h2>
  <p class="sek-sub">{REF_TEXT_P1}</p>
  <div class="ref-wrap">
    <div class="ref-bild">__PHOTO_IMG__</div>
    <div class="ref-text">
      <h3>Anja Jolk</h3>
      <span class="titel">Systemische Beraterin und Coachin (SCGD/IHK) · Entwicklerin KLARTEXT</span>
      <p>{d["ref_text"]}</p>
      <div class="badge-liste">{"".join(f'<span class="badge">{b}</span>' for b in REF_BADGES)}</div>
    </div>
  </div>
</section>

<section class="sek grau">
  <h2 class="sek-titel">Häufige Fragen</h2>
  <div class="faq-liste">{faq_html}</div>
</section>

<section class="cta-final">
  <h2>{d["cta_titel"]}</h2>
  <p>{d["cta_sub"]}</p>
  <a href="mailto:anja.jolk@gmx.de?subject={d['code']} Vorbestellung" class="btn-primary">Jetzt vormerken</a>
</section>

<footer>
  <p>{d["code"]} · ein KLARTEXT-{d.get("footer_typ","Kartendeck")} · © 2026 Anja Jolk · Schwerte</p>
  <p style="margin-top:.4rem;">
    <a href="https://klartext-ingra.h9cyz7d9pj.workers.dev/KLARTEXT_Impressum.html">Impressum</a> ·
    <a href="https://klartext-ingra.h9cyz7d9pj.workers.dev/KLARTEXT_Datenschutz.html">Datenschutz</a> ·
    anja.jolk@gmx.de · +49 176 62311567
  </p>
</footer>

</body>
</html>
'''

# ============================================================
# DECK-DATEN
# ============================================================

DECKS = {}

# ---------- FS ----------
DECKS["fs"] = dict(
    dateiname="FS_Verkaufsseite.html", code="FS", seiten_titel="Impulskarten für die Förderschule",
    hero_badge="🃏 FS · Impulskarten Förderschule",
    hero_h1='Dieselben Impulse — <span>in wirklich einfacher Sprache.</span>',
    hero_sub="FS ist die Sprach-Adaption des KD-Decks für die Förderschule: 32 Coaching-Impulskarten nach den Regeln der Leichten Sprache, plus 2 förderschulspezifische Zusatzkarten.",
    hero_stats=[("32","Impulskarten"),("8","Themenblöcke"),("fertig","Karten & PDF stehen")],
    fuer_wen_titel="das FS-Deck", fuer_wen_sub="Für alle, die mit Kindern an der Förderschule arbeiten.",
    fuer_wen=[
        ("🧑‍🏫","INGRA / Schulbegleitung","Ihr setzt die Karten im Förderschulalltag ein — sprachlich vereinfacht, ohne den Kern der Fragen zu verlieren."),
        ("👪","Eltern","Ihr nutzt die Karten zuhause — in einfacher Sprache verständlich für euer Kind."),
        ("📚","Lehrkräfte Förderschule","Einsetzbar im Unterricht und in Einzelsituationen, angepasst an unterschiedliche Sprachniveaus."),
        ("🏫","Träger","Ihr stattet euer INGRA-Team mit dem Kartendeck aus — als Lizenzpaket."),
    ],
    leistungen_sub="Kein Zubehör, kein Zusatzmodul — das Kartendeck selbst ist das Produkt.",
    leistungen=[
        ("#1B3A4B","🃏","32 Impulskarten","30 Karten als Sprachvereinfachung von KD, plus 2 FS-eigene Karten zu Lernfrust und Kommunikationshilfsmitteln."),
        ("#DEB234","🗣️","Leichte Sprache","Nach den Standards von Netzwerk Leichte Sprache, Inclusion Europe und DIN SPEC 33429 — kurze Sätze, aktiv statt passiv, konkrete Beispiele."),
        ("#6EC6A0","🌡️","Anschluss ans KLARTEXT-System","Barometer und kLAR-Modell wie bei KD — wer die App oder andere Decks kennt, findet sich sofort zurecht."),
        ("#C47A00","🖨️","Digital oder Print","Sofort als PDF zum Download, oder als physisches Kartendeck im Print-on-Demand-Verfahren."),
    ],
    blocks_titel="8 Themenblöcke", blocks_sub="Dieselbe inhaltliche Struktur wie KD — nur sprachlich vereinfacht.",
    blocks=[("BLOCK A–F","Wie KD: Gefühle, Freundschaft, Schule, Familie, Selbstbild, Alltag"),
            ("BLOCK G","Lernen &amp; Kommunikation (2 Karten, förderschulspezifisch)")],
    quellen=[
        "Netzwerk Leichte Sprache e.V. (2022). <em>Die Regeln für Leichte Sprache</em> (Neuauflage). Berlin.",
        "Inclusion Europe (2009). <em>Information for all: European standards for making information easy to read and understand.</em> Brüssel.",
        "DIN SPEC 33429:2025-03. <em>Empfehlungen für Deutsche Leichte Sprache.</em> Berlin: DIN Media (im Auftrag des BMAS).",
    ],
    quellen_sub="Die Sprachvereinfachung folgt drei anerkannten Standards für einfache und leichte Sprache — kein Ersatz für eine zertifizierte Leichte-Sprache-Prüfung, aber eine fundierte Grundlage.",
    baro_klar=True,
    zitat="&bdquo;Einfache Sprache heißt nicht: weniger Tiefe. Es heißt: derselbe Gedanke, für jedes Kind erreichbar.&ldquo;",
    status_hinweis="Die Kartentexte stehen bereits — alle 32.",
    preise=[
        preis_karte("📄 Digital / PDF","13–15 €","einmalig","Sofort als Download nach Erscheinen.",["32 Impulskarten als PDF","Sofort selbst ausdruckbar","Für 1:1-Einsatz gedacht","Dauerhafter Zugriff"],"FS Vorbestellung Digital/PDF"),
        preis_karte("🃏 Print (Print-on-Demand)","24–27 €","einmalig","Physisches Kartendeck, gedruckt erst bei Bestellung.",["32 Karten, physisch gedruckt","Druck über Print-on-Demand-Partner","Robustes Format für den Alltag","Ideal für zuhause &amp; Schule"],"FS Vorbestellung Print",highlight=True,badge="Beliebt"),
        preis_karte("🏫 Träger-/Schul-Lizenz","Auf Anfrage","","Für Träger und Förderschulen fürs ganze Team.",["Lizenzpaket fürs ganze INGRA-Team","Auch als Klassensatz","Für mehrere Gruppen geeignet","Individuelle Stückzahlen"],"FS Träger-/Schul-Lizenz Anfrage",btn_text="Jetzt anfragen"),
    ],
    ref_text="Anja Jolk hat das FS-Deck als Sprach-Adaption des KD-Decks entwickelt — dieselbe fachliche Grundlage, konsequent in Leichter Sprache umgesetzt. Neben ihrer Ausbildung als systemische Beraterin und Coachin bringt sie eine Fortbildung in Transitionspsychiatrie mit (Note 1.7, Prof. Dr. Jörg Fegert, Uniklinikum Ulm) sowie Qualifikationen als Fachkraft für Integrationspädagogik und als Sprachentwicklungsexpertin.",
    faq=[
        ("Ist FS einfach nur KD mit weniger Text?","Nein. FS folgt denselben inhaltlichen Themen wie KD, aber jede Karte wurde eigenständig nach den Regeln der Leichten Sprache neu formuliert — plus 2 zusätzliche, förderschulspezifische Karten."),
        ("Ersetzt das Deck eine zertifizierte Leichte-Sprache-Prüfung?","Nein, das FS-Deck ist eine sorgfältige Sprachvereinfachung nach anerkannten Standards, aber keine zertifizierte Prüfung mit Betroffenen-Gegenlesen."),
        ("Ist das Deck auch ohne die KLARTEXT-App nutzbar?","Ja, das FS-Deck ist eigenständig nutzbar — ganz ohne Zugang, Login oder Internetverbindung."),
        ("Kann meine Schule/mein Träger über Rechnung bezahlen?","Ja, wie bei allen KLARTEXT-Materialien stellen wir gerne eine Rechnung aus."),
    ],
    cta_titel="Das FS-Deck ist startklar", cta_sub="Trag dich unverbindlich für die Vorbestellung ein.",
)

# ---------- DaZ-GS ----------
DECKS["dazgs"] = dict(
    dateiname="DaZGS_Verkaufsseite.html", code="DaZ-GS", seiten_titel="Impulskarten Deutsch als Zweitsprache Grundschule",
    hero_badge="🃏 DaZ-GS · Impulskarten Grundschule",
    hero_h1='Zwischen zwei Sprachen — <span>und trotzdem ganz du selbst.</span>',
    hero_sub="DaZ-GS sind 25 sprachsensible Coaching-Impulskarten für Kinder mit Deutsch als Zweitsprache im Grundschulalter — Ankommen, Sprache lernen, Zugehörigkeit.",
    hero_stats=[("25","Impulskarten"),("7","Themenblöcke"),("fertig","Karten & PDF stehen")],
    fuer_wen_titel="das DaZ-GS-Deck", fuer_wen_sub="Für alle, die mit mehrsprachig aufwachsenden Grundschulkindern arbeiten.",
    fuer_wen=[
        ("🧑‍🏫","INGRA / Schulbegleitung","Ihr nutzt die Karten als Gesprächsöffner für Kinder, die zwischen Herkunftssprache und Deutsch navigieren."),
        ("👪","Eltern","Ihr nutzt die Karten zuhause — wertschätzend gegenüber der Familiensprache."),
        ("📚","Lehrkräfte","Einsetzbar in DaZ-Förderung und Regelunterricht, sprachsensibel formuliert."),
        ("🏫","Träger","Lizenzpaket fürs ganze INGRA-Team, analog zu den anderen KLARTEXT-Decks."),
    ],
    leistungen_sub="Kein Trauma-Verarbeitungs-Deck — ein Coaching-Impulsdeck für Ankommen und Zugehörigkeit.",
    leistungen=[
        ("#1B3A4B","🃏","25 Impulskarten","Sprachsensible Coaching-Fragen zu Ankommen, Sprache lernen, Freundschaft und Stolz auf die eigene Herkunft."),
        ("#00ACD6","🌍","Zwei Sprachwelten wertschätzen","Die Herkunftssprache wird nicht als Defizit behandelt, sondern als Stärke — fachlich fundiert."),
        ("#6EC6A0","🌡️","Anschluss ans KLARTEXT-System","Barometer und kLAR-Modell ziehen sich durch alle KLARTEXT-Materialien."),
        ("#C47A00","🖨️","Digital oder Print","Sofort als PDF zum Download, oder als physisches Kartendeck im Print-on-Demand-Verfahren."),
    ],
    blocks_titel="7 Themenblöcke", blocks_sub="Von Ankommen bis zum Übergang in die Regelklasse.",
    blocks=[("BLOCK A","Ankommen"),("BLOCK B","Sprache lernen"),("BLOCK C","Zwischen zwei Welten"),
            ("BLOCK D","Freundschaft trotz Sprachbarriere"),("BLOCK E","Was ich vermisse"),
            ("BLOCK F","Stolz auf mich"),("BLOCK G","Übergang in die Regelklasse")],
    quellen=[
        "Gogolin, I. (1994/2008). <em>Der monolinguale Habitus der multilingualen Schule.</em> Münster: Waxmann. — Grundlage für Block C und die Wertschätzung der Herkunftssprache.",
        "Mecheril, P. (2004). <em>Einführung in die Migrationspädagogik.</em> Weinheim/Basel: Beltz. — Grundlage für die Grundhaltung des Decks: Zugehörigkeit stärken statt Differenz betonen.",
    ],
    quellen_sub="Zwei anerkannte Werke der Migrationspädagogik bilden die fachliche Grundlage des Decks.",
    baro_klar=True,
    zitat="&bdquo;Zwei Sprachen zu sprechen ist kein Umweg. Es ist ein zweiter Zugang zur Welt.&ldquo;",
    status_hinweis="Die Kartentexte stehen bereits — alle 25.",
    preise=[
        preis_karte("📄 Digital / PDF","13–15 €","einmalig","Sofort als Download nach Erscheinen.",["25 Impulskarten als PDF","Sofort selbst ausdruckbar","Für 1:1-Einsatz gedacht","Dauerhafter Zugriff"],"DaZ-GS Vorbestellung Digital/PDF"),
        preis_karte("🃏 Print (Print-on-Demand)","22–25 €","einmalig","Physisches Kartendeck, gedruckt erst bei Bestellung.",["25 Karten, physisch gedruckt","Druck über Print-on-Demand-Partner","Robustes Format für den Alltag","Ideal für zuhause &amp; Schule"],"DaZ-GS Vorbestellung Print",highlight=True,badge="Beliebt"),
        preis_karte("🏫 Träger-/Schul-Lizenz","Auf Anfrage","","Für Träger und Schulen fürs ganze Team.",["Lizenzpaket fürs ganze INGRA-Team","Auch als Klassensatz","Für mehrere Gruppen geeignet","Individuelle Stückzahlen"],"DaZ-GS Träger-/Schul-Lizenz Anfrage",btn_text="Jetzt anfragen"),
    ],
    ref_text="Anja Jolk hat das DaZ-GS-Deck auf Basis anerkannter migrationspädagogischer Literatur und systemischer Coaching-Methodik entwickelt. Neben ihrer Ausbildung als systemische Beraterin und Coachin bringt sie eine Fortbildung in Transitionspsychiatrie mit (Note 1.7, Prof. Dr. Jörg Fegert, Uniklinikum Ulm) sowie Qualifikationen als Fachkraft für Integrationspädagogik und als Sprachentwicklungsexpertin.",
    faq=[
        ("Ist das ein Trauma-Verarbeitungs-Deck für geflüchtete Kinder?","Nein, bewusst nicht. DaZ-GS ist ein Coaching-Impulsdeck für den Schulalltag mehrsprachiger Kinder — keine Traumatherapie-Karten."),
        ("Funktioniert das Deck auch bei sehr unterschiedlichen Herkunftssprachen?","Ja, die Fragen sind bewusst offen formuliert und beziehen sich auf die Erfahrung des Zwischen-zwei-Welten-Seins, unabhängig von der konkreten Sprache."),
        ("Ist das Deck auch ohne die KLARTEXT-App nutzbar?","Ja, eigenständig nutzbar — ganz ohne Zugang, Login oder Internetverbindung."),
        ("Kann meine Schule/mein Träger über Rechnung bezahlen?","Ja, wie bei allen KLARTEXT-Materialien stellen wir gerne eine Rechnung aus."),
    ],
    cta_titel="Das DaZ-GS-Deck ist startklar", cta_sub="Trag dich unverbindlich für die Vorbestellung ein.",
)

# ---------- DaZ-Sek1 ----------
DECKS["dazsek1"] = dict(
    dateiname="DaZSek1_Verkaufsseite.html", code="DaZ-Sek I", seiten_titel="Impulskarten Deutsch als Zweitsprache Sekundarstufe I",
    hero_badge="🃏 DaZ-Sek I · Impulskarten Sek I",
    hero_h1='Ankommen im neuen System —<br><span>und trotzdem man selbst bleiben.</span>',
    hero_sub="DaZ-Sek I sind 25 sprachsensible Coaching-Impulskarten für Jugendliche mit Deutsch als Zweitsprache in der weiterführenden Schule.",
    hero_stats=[("25","Impulskarten"),("7","Themenblöcke"),("fertig","Karten & PDF stehen")],
    fuer_wen_titel="das DaZ-Sek-I-Deck", fuer_wen_sub="Für alle, die mit mehrsprachigen Jugendlichen in der Sek I arbeiten.",
    fuer_wen=[
        ("🧑‍🏫","INGRA / Schulbegleitung","Ihr nutzt die Karten als Gesprächsöffner für Jugendliche zwischen Herkunft, Sprache und Leistungsdruck."),
        ("👪","Eltern","Ihr nutzt die Karten zuhause — wertschätzend gegenüber der Familiensprache und -herkunft."),
        ("📚","Lehrkräfte Sek I","Einsetzbar in DaZ-Förderung und Regelunterricht, altersgerecht für Jugendliche formuliert."),
        ("🏫","Träger","Lizenzpaket fürs ganze INGRA-Team, analog zu den anderen KLARTEXT-Decks."),
    ],
    leistungen_sub="Kein Trauma-Verarbeitungs-Deck — ein Coaching-Impulsdeck für Ankommen, Identität und Zukunft.",
    leistungen=[
        ("#1B3A4B","🃏","25 Impulskarten","Coaching-Fragen zu Ankommen im neuen System, Sprache &amp; Leistung, Identität zwischen Kulturen, Zukunft."),
        ("#6E1438","🌍","Identität zwischen den Kulturen","Zugehörigkeit wird gestärkt statt Differenz betont — fachlich fundiert für die Altersgruppe Jugendliche."),
        ("#6EC6A0","🌡️","Anschluss ans KLARTEXT-System","Barometer und kLAR-Modell ziehen sich durch alle KLARTEXT-Materialien."),
        ("#C47A00","🖨️","Digital oder Print","Sofort als PDF zum Download, oder als physisches Kartendeck im Print-on-Demand-Verfahren."),
    ],
    blocks_titel="7 Themenblöcke", blocks_sub="Von Ankommen im neuen System bis zum Übergang in die Regelklasse.",
    blocks=[("BLOCK A","Ankommen im neuen System"),("BLOCK B","Sprache &amp; Leistung"),
            ("BLOCK C","Identität zwischen den Kulturen"),("BLOCK D","Freundschaft &amp; Zugehörigkeit"),
            ("BLOCK E","Herkunft &amp; was ich vermisse"),("BLOCK F","Zukunft &amp; Stolz"),
            ("BLOCK G","Übergang in die Regelklasse")],
    quellen=[
        "Gogolin, I. (1994/2008). <em>Der monolinguale Habitus der multilingualen Schule.</em> Waxmann.",
        "Mecheril, P. (2004). <em>Einführung in die Migrationspädagogik.</em> Beltz.",
    ],
    quellen_sub="Dieselbe fachliche Grundlage wie DaZ-GS, für die Altersgruppe der Sekundarstufe I angepasst.",
    baro_klar=True,
    zitat="&bdquo;Neu ankommen heißt nicht, alles zurücklassen zu müssen.&ldquo;",
    status_hinweis="Die Kartentexte stehen bereits — alle 25.",
    preise=[
        preis_karte("📄 Digital / PDF","13–15 €","einmalig","Sofort als Download nach Erscheinen.",["25 Impulskarten als PDF","Sofort selbst ausdruckbar","Für 1:1-Einsatz gedacht","Dauerhafter Zugriff"],"DaZ-Sek1 Vorbestellung Digital/PDF"),
        preis_karte("🃏 Print (Print-on-Demand)","22–25 €","einmalig","Physisches Kartendeck, gedruckt erst bei Bestellung.",["25 Karten, physisch gedruckt","Druck über Print-on-Demand-Partner","Robustes Format für den Alltag","Ideal für Schule &amp; Zuhause"],"DaZ-Sek1 Vorbestellung Print",highlight=True,badge="Beliebt"),
        preis_karte("🏫 Träger-/Schul-Lizenz","Auf Anfrage","","Für Träger und Schulen fürs ganze Team.",["Lizenzpaket fürs ganze INGRA-Team","Auch als Klassensatz","Für mehrere Gruppen geeignet","Individuelle Stückzahlen"],"DaZ-Sek1 Träger-/Schul-Lizenz Anfrage",btn_text="Jetzt anfragen"),
    ],
    ref_text="Anja Jolk hat das DaZ-Sek-I-Deck auf Basis anerkannter migrationspädagogischer Literatur und systemischer Coaching-Methodik entwickelt. Neben ihrer Ausbildung als systemische Beraterin und Coachin bringt sie eine Fortbildung in Transitionspsychiatrie mit (Note 1.7, Prof. Dr. Jörg Fegert, Uniklinikum Ulm) sowie Qualifikationen als Fachkraft für Integrationspädagogik und als Sprachentwicklungsexpertin.",
    faq=[
        ("Wie unterscheidet sich DaZ-Sek I von DaZ-GS?","Gleiche fachliche Grundlage, aber altersgerecht für Jugendliche formuliert — mit Themen wie Leistungsdruck, Identität und Zukunftsperspektive statt Grundschul-Alltag."),
        ("Ist das ein Trauma-Verarbeitungs-Deck?","Nein, bewusst nicht. Ein Coaching-Impulsdeck für den Schulalltag, keine Traumatherapie-Karten."),
        ("Ist das Deck auch ohne die KLARTEXT-App nutzbar?","Ja, eigenständig nutzbar — ganz ohne Zugang, Login oder Internetverbindung."),
        ("Kann meine Schule/mein Träger über Rechnung bezahlen?","Ja, wie bei allen KLARTEXT-Materialien stellen wir gerne eine Rechnung aus."),
    ],
    cta_titel="Das DaZ-Sek-I-Deck ist startklar", cta_sub="Trag dich unverbindlich für die Vorbestellung ein.",
)

# ---------- OGS ----------
DECKS["ogs"] = dict(
    dateiname="OGS_Verkaufsseite.html", code="OGS", seiten_titel="Impulskarten Offene Ganztagsschule",
    hero_badge="🃏 OGS · Impulskarten Ganztagsschule",
    hero_h1='Zwischen Unterricht, Freispiel<br>und Übergängen — <span>klare Impulse für den OGS-Alltag.</span>',
    hero_sub="OGS sind 32 Coaching-Impulskarten für die Offene Ganztagsschule: Gruppendynamik, Rituale, Konflikte, Selbstständigkeit und die Zusammenarbeit im Team.",
    hero_stats=[("32","Impulskarten"),("8","Themenblöcke"),("fertig","Karten & PDF stehen")],
    fuer_wen_titel="das OGS-Deck", fuer_wen_sub="Für alle, die im offenen Ganztag mit Gruppen arbeiten.",
    fuer_wen=[
        ("🧑‍🏫","OGS-Fachkräfte / INGRA","Ihr nutzt die Karten für Gruppendynamik, Rituale und Konfliktbegleitung im Ganztag."),
        ("👪","Eltern","Ihr bekommt Einblick, wie euer Kind den OGS-Alltag zwischen Freispiel und Übergängen erlebt."),
        ("📚","Lehrkräfte im Ganztag","Einsetzbar für die Zusammenarbeit zwischen Unterricht und Betreuung."),
        ("🏫","Träger","Lizenzpaket fürs ganze OGS-Team, analog zu den anderen KLARTEXT-Decks."),
    ],
    leistungen_sub="Kein Zubehör, kein Zusatzmodul — das Kartendeck selbst ist das Produkt.",
    leistungen=[
        ("#1B3A4B","🃏","32 Impulskarten","Coaching-Fragen zu Gruppendynamik, Ritualen, Konflikten, Regeln, Beziehungsarbeit und Übergängen."),
        ("#8BC34A","🔄","Für den Ganztag gedacht","Anders als reine Unterrichtskarten berücksichtigt OGS die besondere Struktur zwischen Schule und Freizeit."),
        ("#6EC6A0","🌡️","Anschluss ans KLARTEXT-System","Barometer und kLAR-Modell ziehen sich durch alle KLARTEXT-Materialien."),
        ("#C47A00","🖨️","Digital oder Print","Sofort als PDF zum Download, oder als physisches Kartendeck im Print-on-Demand-Verfahren."),
    ],
    blocks_titel="8 Themenblöcke", blocks_sub="Von Gruppendynamik bis zur Zusammenarbeit im Team.",
    blocks=[("BLOCK 1","Gruppendynamik verstehen"),("BLOCK 2","Rituale nutzen"),("BLOCK 3","Konflikte begleiten"),
            ("BLOCK 4","Regeln vermitteln"),("BLOCK 5","Beziehungsarbeit im OGS"),
            ("BLOCK 6","Selbstständigkeit fördern"),("BLOCK 7","Übergänge gestalten"),
            ("BLOCK 8","Rahmen &amp; Zusammenarbeit")],
    quellen=None, quellen_sub=None,
    baro_klar=True,
    zitat="&bdquo;Der Ganztag ist kein verlängerter Unterricht. Er ist ein eigener Raum — mit eigenen Regeln.&ldquo;",
    status_hinweis="Die Kartentexte stehen bereits — alle 32.",
    preise=[
        preis_karte("📄 Digital / PDF","13–15 €","einmalig","Sofort als Download nach Erscheinen.",["32 Impulskarten als PDF","Sofort selbst ausdruckbar","Für 1:1-Einsatz gedacht","Dauerhafter Zugriff"],"OGS Vorbestellung Digital/PDF"),
        preis_karte("🃏 Print (Print-on-Demand)","24–27 €","einmalig","Physisches Kartendeck, gedruckt erst bei Bestellung.",["32 Karten, physisch gedruckt","Druck über Print-on-Demand-Partner","Robustes Format für den Alltag","Ideal für den OGS-Alltag"],"OGS Vorbestellung Print",highlight=True,badge="Beliebt"),
        preis_karte("🏫 Träger-Lizenz","Auf Anfrage","","Für Träger, die das ganze OGS-Team ausstatten wollen.",["Lizenzpaket fürs ganze OGS-Team","Für mehrere Gruppen geeignet","Individuelle Stückzahlen möglich","Auf Wunsch mit Einführung"],"OGS Träger-Lizenz Anfrage",btn_text="Jetzt anfragen"),
    ],
    ref_text="Anja Jolk hat das OGS-Deck aus der Praxis heraus entwickelt — angepasst an die besondere Struktur des offenen Ganztags zwischen Unterricht, Freispiel und Übergängen. Neben ihrer Ausbildung als systemische Beraterin und Coachin bringt sie eine Fortbildung in Transitionspsychiatrie mit (Note 1.7, Prof. Dr. Jörg Fegert, Uniklinikum Ulm) sowie Qualifikationen als Fachkraft für Integrationspädagogik und als Sprachentwicklungsexpertin.",
    faq=[
        ("Was unterscheidet OGS von KD?","OGS ist speziell auf die Struktur des offenen Ganztags zugeschnitten — Übergänge, Freispiel, Teamarbeit — statt auf den regulären Unterricht."),
        ("Ist das Deck auch für den gebundenen Ganztag geeignet?","Ja, die meisten Karten funktionieren auch dort — der Fokus liegt aber auf den offenen, weniger strukturierten Situationen des OGS."),
        ("Ist das Deck auch ohne die KLARTEXT-App nutzbar?","Ja, eigenständig nutzbar — ganz ohne Zugang, Login oder Internetverbindung."),
        ("Kann mein Träger über Rechnung bezahlen?","Ja, wie bei allen KLARTEXT-Materialien stellen wir gerne eine Rechnung aus."),
    ],
    cta_titel="Das OGS-Deck ist startklar", cta_sub="Trag dich unverbindlich für die Vorbestellung ein.",
)

# ---------- Geschichtenkarten (GK) ----------
DECKS["gk"] = dict(
    dateiname="GK_Verkaufsseite.html", code="GK", seiten_titel="Geschichtenkarten mit Brainy",
    hero_badge="🃏 GK · Geschichtenkarten",
    hero_h1='Geschichten, die zeigen —<br><span>nicht nur erklären.</span>',
    hero_sub="30 Erzählkarten mit Brainy in drei Sets: Mobbing erleben, anderen helfen, Strategien lernen — für Gespräche über Mobbing, die bei der Geschichte ansetzen statt beim Vorwurf.",
    hero_stats=[("30","Geschichtenkarten"),("3","Sets à 10"),("fertig","Karten & PDF stehen")],
    fuer_wen_titel="das Geschichtenkarten-Deck", fuer_wen_sub="Für alle, die mit jüngeren Kindern über Mobbing sprechen wollen.",
    fuer_wen=[
        ("🧑‍🏫","INGRA / Schulbegleitung","Ihr nutzt die Geschichten als Gesprächseinstieg — über Brainys Erleben statt direkt über das Kind."),
        ("👪","Eltern","Ihr lest die Geschichten gemeinsam vor und sprecht über die enthaltenen Fragen."),
        ("📚","Lehrkräfte Grundschule","Einsetzbar im Klassenrat oder in Einzelgesprächen zum Thema Mobbing."),
        ("🏫","Träger","Lizenzpaket fürs ganze Team, analog zu den anderen KLARTEXT-Decks."),
    ],
    leistungen_sub="Kein Zubehör, kein Zusatzmodul — das Kartendeck selbst ist das Produkt.",
    leistungen=[
        ("#1B3A4B","📖","30 Geschichtenkarten","3 Sets à 10 Karten mit eigens gemalter Brainy-Illustration je Karte, im Serienlook der anderen KLARTEXT-Decks."),
        ("#961E23","💬","3 Fragen zum Gespräch","Jede Karte hat Titel, Situation, 3 Gesprächsfragen und ein Impuls-Zitat — Format A6."),
        ("#8BC34A","🎁","Bonus-Material inklusive","Das bestehende A4-Druckset bleibt zusätzlich als kostenloses Bonusmaterial downloadbar."),
        ("#C47A00","🖨️","Digital oder Print","Sofort als PDF zum Download, oder als physisches Kartendeck im Print-on-Demand-Verfahren."),
    ],
    blocks_titel="3 Sets à 10 Karten", blocks_sub="Drei Perspektiven auf dasselbe Thema.",
    blocks=[("SET A","Brainy erlebt Mobbing — Opferperspektive"),
            ("SET B","Brainy hilft anderen — Verteidiger-/Helferperspektive"),
            ("SET C","Brainy lernt Strategien — Übungskarten")],
    quellen=None, quellen_sub=None,
    baro_klar=False,
    zitat="&bdquo;Manchmal versteht ein Kind eine Geschichte über sich selbst leichter, wenn sie zuerst über jemand anderen erzählt wird.&ldquo;",
    status_hinweis="Die Kartentexte stehen bereits — alle 30.",
    preise=[
        preis_karte("📄 Digital / PDF","15–18 €","einmalig","Sofort als Download nach Erscheinen.",["30 Geschichtenkarten als PDF","Bonus: A4-Druckset kostenlos inklusive","Sofort selbst ausdruckbar","Dauerhafter Zugriff"],"GK Vorbestellung Digital/PDF"),
        preis_karte("🃏 Print (Print-on-Demand)","26–29 €","einmalig","Physisches Kartendeck, gedruckt erst bei Bestellung.",["30 Karten, physisch gedruckt","Druck über Print-on-Demand-Partner","Robustes Format für den Alltag","Ideal für Vorlesesituationen"],"GK Vorbestellung Print",highlight=True,badge="Beliebt"),
        preis_karte("🏫 Träger-/Schul-Lizenz","Auf Anfrage","","Für Träger und Schulen fürs ganze Team.",["Lizenzpaket fürs ganze Team","Auch als Klassensatz","Für mehrere Gruppen geeignet","Individuelle Stückzahlen"],"GK Träger-/Schul-Lizenz Anfrage",btn_text="Jetzt anfragen"),
    ],
    ref_text="Anja Jolk hat die Geschichtenkarten als niedrigschwelligen Einstieg ins Thema Mobbing entwickelt — über die Brainy-Figur, die den Kindern aus den anderen KLARTEXT-Materialien bereits vertraut ist. Neben ihrer Ausbildung als systemische Beraterin und Coachin bringt sie eine Fortbildung in Transitionspsychiatrie mit (Note 1.7, Prof. Dr. Jörg Fegert, Uniklinikum Ulm) sowie Qualifikationen als Fachkraft für Integrationspädagogik und als Sprachentwicklungsexpertin.",
    faq=[
        ("Muss ich die anderen KLARTEXT-Decks kennen, um Brainy zu verstehen?","Nein, jede Geschichte funktioniert eigenständig — Vorwissen aus anderen Decks ist hilfreich, aber nicht nötig."),
        ("Für welches Alter ist das Deck gedacht?","Für Grundschulkinder — die Sprache und Bildwelt ist an KD/JD angelehnt."),
        ("Was ist das kostenlose Bonus-Material?","Ein bereits bestehendes A4-Druckset zum selben Thema, das zusätzlich zum Kartendeck kostenlos zum Download bereitsteht."),
        ("Kann meine Schule/mein Träger über Rechnung bezahlen?","Ja, wie bei allen KLARTEXT-Materialien stellen wir gerne eine Rechnung aus."),
    ],
    cta_titel="Die Geschichtenkarten sind startklar", cta_sub="Trag dich unverbindlich für die Vorbestellung ein.",
)

# ---------- TK (Teamkoordination) ----------
DECKS["tk"] = dict(
    dateiname="TK_Verkaufsseite.html", code="TK", seiten_titel="Handlungskarten Teamkoordination",
    hero_badge="🃏 TK · Handlungskarten Teamkoordination",
    hero_h1='Klare Abstimmung statt<br><span>Zuständigkeits-Chaos.</span>',
    hero_sub="19 Handlungskarten für die Abstimmung zwischen INGRA, Lehrkraft, Familie und Träger — konkrete Schritte statt offener Coaching-Impulse.",
    hero_stats=[("19","Handlungskarten"),("3","Themenfelder"),("fertig","Karten & PDF stehen")],
    fuer_wen_titel="das TK-Deck", fuer_wen_sub="Für Teams, die Zuständigkeiten und Übergaben klären müssen.",
    fuer_wen=[
        ("🧑‍🏫","INGRA / Schulbegleitung","Ihr nutzt die Karten für Übergaben, Fallbesprechungen und Abstimmung mit Lehrkraft und Familie."),
        ("📚","Lehrkräfte","Klare Handlungsschritte für die Zusammenarbeit mit Schulbegleitung und Familie."),
        ("🏫","Träger","Ihr stattet euer Team mit einem gemeinsamen Handlungsrahmen für Koordination aus."),
        ("🤝","Kind &amp; Familie","Einige Karten adressieren direkt die Abstimmung mit Familie und externen Stellen."),
    ],
    leistungen_sub="Handlungskarten statt Coaching-Impulse: konkrete Schritte für den Koordinations-Alltag.",
    leistungen=[
        ("#1B3A4B","🃏","19 Handlungskarten","Konkrete Schritt-für-Schritt-Anleitungen für Team-, Familien- und Systemkoordination."),
        ("#4A148C","🧩","3 Themenfelder","Team &amp; Koordination, Kind &amp; Familie, System &amp; Schnittstellen — der ganze Koordinationsalltag."),
        ("#6EC6A0","✅","Inhaltlich fachlich geprüft","Basierend auf den bereits fachlich geprüften Inhalten der KLARTEXT-App, für den physischen Einsatz aufbereitet."),
        ("#C47A00","🖨️","Digital oder Print","Sofort als PDF zum Download, oder als physisches Kartendeck im Print-on-Demand-Verfahren."),
    ],
    blocks_titel="3 Themenfelder", blocks_sub="Von der Teamabstimmung bis zur Zusammenarbeit mit externen Stellen.",
    blocks=[("FELD 1","Team &amp; Koordination"),("FELD 2","Kind &amp; Familie"),("FELD 3","System &amp; Schnittstellen")],
    quellen=None, quellen_sub=None,
    baro_klar=False,
    zitat="&bdquo;Gute Unterstützung scheitert selten an gutem Willen — sondern an fehlender Abstimmung.&ldquo;",
    status_hinweis="Die Kartentexte stehen bereits — alle 19, inhaltlich identisch zur geprüften App-Version.",
    preise=[
        preis_karte("📄 Digital / PDF","15–18 €","einmalig","Sofort als Download nach Erscheinen.",["19 Handlungskarten als PDF","Sofort selbst ausdruckbar","Für Team-Einsatz gedacht","Dauerhafter Zugriff"],"TK Vorbestellung Digital/PDF"),
        preis_karte("🃏 Print (Print-on-Demand)","24–27 €","einmalig","Physisches Kartendeck, gedruckt erst bei Bestellung.",["19 Karten, physisch gedruckt","Druck über Print-on-Demand-Partner","Robustes Format für Teamsitzungen","Ideal fürs INGRA-Team"],"TK Vorbestellung Print",highlight=True,badge="Beliebt"),
        preis_karte("🏫 Träger-Lizenz","Auf Anfrage","","Für Träger, die das ganze Team ausstatten wollen.",["Lizenzpaket fürs ganze Team","Für mehrere Teams geeignet","Individuelle Stückzahlen möglich","Auf Wunsch mit Einführung"],"TK Träger-Lizenz Anfrage",btn_text="Jetzt anfragen"),
    ],
    ref_text="Anja Jolk hat das TK-Deck aus der praktischen Notwendigkeit heraus entwickelt, Zuständigkeiten zwischen INGRA, Lehrkraft, Familie und Träger klar zu regeln. Neben ihrer Ausbildung als systemische Beraterin und Coachin bringt sie eine Fortbildung in Transitionspsychiatrie mit (Note 1.7, Prof. Dr. Jörg Fegert, Uniklinikum Ulm) sowie Qualifikationen als Fachkraft für Integrationspädagogik und als Sprachentwicklungsexpertin.",
    faq=[
        ("Ist TK ein Coaching-Deck wie KD oder EL?","Nein. TK sind Handlungskarten — konkrete Schritte für die Teamkoordination, keine offenen Gesprächsimpulse."),
        ("Sind die Inhalte neu oder aus der App übernommen?","Die App-Inhalte gelten als bereits fachlich geprüft. Das physische Deck adaptiert und kürzt diesen Text, erfindet aber keine neuen Handlungsanweisungen."),
        ("Ist das Deck auch ohne die KLARTEXT-App nutzbar?","Ja, eigenständig nutzbar — ganz ohne Zugang, Login oder Internetverbindung."),
        ("Kann mein Träger über Rechnung bezahlen?","Ja, wie bei allen KLARTEXT-Materialien stellen wir gerne eine Rechnung aus."),
    ],
    cta_titel="Das TK-Deck ist startklar", cta_sub="Trag dich unverbindlich für die Vorbestellung ein.",
    footer_typ="Handlungskartendeck",
)

# ---------- Krisendeck (FK) ----------
DECKS["fk"] = dict(
    dateiname="FK_Verkaufsseite.html", code="FK", seiten_titel="Krisendeck – Feuerwehrkarten",
    hero_badge="🚨 FK · Krisendeck",
    hero_h1='Wenn jede Sekunde zählt —<br><span>griffbereit, ohne Bildschirm.</span>',
    hero_sub="8 Feuerwehrkarten für akute Krisensituationen (Barometer Rot): Eskalation, Shutdown, Panikattacke, Dissoziation, Meltdown und mehr — als laminiertes Ringbuch sofort griffbereit.",
    hero_stats=[("8","Feuerwehrkarten"),("Barometer","Rot"),("fertig","Karten & PDF stehen")],
    fuer_wen_titel="das Krisendeck", fuer_wen_sub="Nur für qualifizierte Fachkräfte, die im Alltag mit akuten Krisensituationen umgehen.",
    fuer_wen=[
        ("🧑‍🏫","INGRA / Schulbegleitung","Ihr habt die 8 Karten physisch griffbereit — kein Bildschirm nötig, wenn's darauf ankommt."),
        ("🏫","Träger","Ihr stattet euer Team mit einem einheitlichen Schnellgriff-Werkzeug für Barometer Rot aus."),
        ("🚑","Leitungskräfte","Ihr nutzt das Deck als Ergänzung zu bestehenden Kinderschutz-Verfahren, nicht als Ersatz."),
    ],
    leistungen_sub="Sekunden-Schnellgriff für Barometer Rot — kein Ersatz fürs Feuerwehr-Protokoll der App, sondern seine physische Griffbereitschaft.",
    leistungen=[
        ("#1B3A4B","🚨","8 Feuerwehrkarten","FK-01 bis FK-08: Akute Eskalation, Shutdown, Panikattacke, Fremdgefährdung, Selbstverletzung, Weglaufen/Flucht, Dissoziation, Meltdown."),
        ("#C62828","⚡","Sofortmaßnahmen auf einen Blick","Lead-Satz, nummerierte Sofortmaßnahmen, Erkennungssignale und eine Jetzt-tun/Jetzt-nicht-tun-Tabelle je Karte."),
        ("#6EC6A0","✅","Inhaltlich fachlich geprüft","Die App-Inhalte gelten als bereits geprüft — das physische Deck adaptiert, erfindet keine neuen Handlungsanweisungen."),
        ("#C47A00","🖨️","Digital oder Print","Sofort als PDF zum Download, oder als laminiertes Kartenset im Print-on-Demand-Verfahren."),
    ],
    blocks_titel="8 Karten, FK-01 bis FK-08", blocks_sub="Gleiche Reihenfolge und Titel wie in der App.",
    blocks=[("FK-01","Akute Eskalation"),("FK-02","Shutdown"),("FK-03","Panikattacke"),
            ("FK-04","Fremdgefährdung"),("FK-05","Selbstverletzung"),("FK-06","Weglaufen/Flucht"),
            ("FK-07","Dissoziation"),("FK-08","Meltdown")],
    quellen=None, quellen_sub=None,
    baro_klar=False,
    fach_hinweis="Das Krisendeck ersetzt kein Kinderschutz-Verfahren und keine Rechtsberatung. Bei Fremdgefährdung oder Selbstverletzung gelten immer zuerst die trägerinternen Meldewege.",
    zitat="&bdquo;In der Krise zählt nicht, was du weißt — sondern was du in dem Moment griffbereit hast.&ldquo;",
    status_hinweis="Die Kartentexte stehen bereits — alle 8, inhaltlich identisch zur geprüften App-Version.",
    preise=[
        preis_karte("📄 Digital / PDF","12–15 €","einmalig","Sofort als Download nach Erscheinen.",["8 Feuerwehrkarten als PDF","Sofort selbst ausdruckbar","Laminierbar für den Alltag","Dauerhafter Zugriff"],"FK Vorbestellung Digital/PDF"),
        preis_karte("🃏 Print (Print-on-Demand)","19–22 €","einmalig","Laminiertes Ringbuch, gedruckt erst bei Bestellung.",["8 Karten, laminiert im Ringbuch","Druck über Print-on-Demand-Partner","Sekunden-Schnellgriff im Alltag","Kein Bildschirm nötig"],"FK Vorbestellung Print",highlight=True,badge="Beliebt"),
        preis_karte("🏫 Träger-Lizenz","Auf Anfrage","","Für Träger, die das ganze Team ausstatten wollen.",["Lizenzpaket fürs ganze Team","Für mehrere Standorte geeignet","Individuelle Stückzahlen möglich","Auf Wunsch mit Einführung"],"FK Träger-Lizenz Anfrage",btn_text="Jetzt anfragen"),
    ],
    ref_text="Anja Jolk hat das Krisendeck als physische Ergänzung zum bereits fachlich geprüften Feuerwehr-Protokoll der KLARTEXT-App entwickelt — für den Moment, in dem kein Bildschirm zur Hand ist. Neben ihrer Ausbildung als systemische Beraterin und Coachin bringt sie eine Fortbildung in Transitionspsychiatrie mit (Note 1.7, Prof. Dr. Jörg Fegert, Uniklinikum Ulm) sowie Qualifikationen als Fachkraft für Integrationspädagogik und als Sprachentwicklungsexpertin.",
    faq=[
        ("Wer sollte das Krisendeck nutzen?","Ausschließlich qualifizierte Fachkräfte im pädagogischen Kontext — es ersetzt keine Ausbildung und keine Rechtsberatung."),
        ("Ersetzt das Deck ein Kinderschutz-Verfahren?","Nein, ausdrücklich nicht. Es ergänzt bestehende Verfahren um ein physisches Schnellgriff-Werkzeug für den akuten Moment."),
        ("Woher kommen die Inhalte?","Aus dem bereits fachlich geprüften Feuerwehr-Protokoll der KLARTEXT-App — hier adaptiert und vereinheitlicht fürs physische Format."),
        ("Kann mein Träger über Rechnung bezahlen?","Ja, wie bei allen KLARTEXT-Materialien stellen wir gerne eine Rechnung aus."),
    ],
    cta_titel="Das Krisendeck ist startklar", cta_sub="Trag dich unverbindlich für die Vorbestellung ein.",
    footer_typ="Handlungskartendeck",
)

# ---------- Werkzeugkarten (M3) ----------
DECKS["m3"] = dict(
    dateiname="M3_Verkaufsseite.html", code="M3", seiten_titel="Werkzeugkarten – Mini-Interventionen",
    hero_badge="🧰 M3 · Werkzeugkarten",
    hero_h1='Nicht jede Situation<br>braucht <span>ein großes Konzept.</span>',
    hero_sub="20 Mini-Interventionen für den pädagogischen Alltag — 8 Situationskarten und 12 Werkzeugkarten, direkt anwendbar bei Gelb und Orange.",
    hero_stats=[("20","Werkzeugkarten"),("2","Kartentypen"),("fertig","Karten & PDF stehen")],
    fuer_wen_titel="das Werkzeugkarten-Deck", fuer_wen_sub="Für den schnellen Griff im pädagogischen Alltag.",
    fuer_wen=[
        ("🧑‍🏫","INGRA / Schulbegleitung","Ihr habt für typische Situationen (Barometer Gelb/Orange) sofort ein passendes Werkzeug zur Hand."),
        ("📚","Lehrkräfte","Kleine, schnell umsetzbare Interventionen für den Unterrichtsalltag."),
        ("🏫","Träger","Ihr stattet euer Team mit einem gemeinsamen Werkzeugkoffer aus."),
    ],
    leistungen_sub="Situation erkennen, passendes Werkzeug greifen — in unter einer Minute umsetzbar.",
    leistungen=[
        ("#1B3A4B","🧰","20 Werkzeugkarten","8 Situationskarten (typische Momente) + 12 Werkzeugkarten (konkrete Mini-Interventionen)."),
        ("#B07D2A","⚡","Sofort umsetzbar","Jede Werkzeugkarte in nummerierten Schritten — z. B. der Atemanker: 4 Sekunden ein, 4 halten, 6 aus."),
        ("#6EC6A0","🌡️","Barometer-Bezug","Jede Karte zeigt, bei welchem Barometer-Zustand sie passt — Gelb, Orange, vor Übergängen, nach der Pause."),
        ("#C47A00","🖨️","Digital oder Print","Sofort als PDF zum Download, oder als physisches Kartenset im Print-on-Demand-Verfahren."),
    ],
    blocks_titel="2 Kartentypen", blocks_sub="Situation erkennen, dann das passende Werkzeug greifen.",
    blocks=[("TYP 1","Situationskarten (8) — typische Momente wie 'Kind kommt aufgewühlt an'"),
            ("TYP 2","Werkzeugkarten (12) — konkrete Mini-Interventionen wie der Atemanker")],
    quellen=None, quellen_sub=None,
    baro_klar=False,
    zitat="&bdquo;Kein Kind kommt absichtlich aufgewühlt. Was draußen passiert ist, landet im Körper — und braucht Zeit.&ldquo;",
    status_hinweis="Die Kartentexte stehen bereits — alle 20.",
    preise=[
        preis_karte("📄 Digital / PDF","13–15 €","einmalig","Sofort als Download nach Erscheinen.",["20 Werkzeugkarten als PDF","Sofort selbst ausdruckbar","Für den täglichen Griff gedacht","Dauerhafter Zugriff"],"M3 Vorbestellung Digital/PDF"),
        preis_karte("🃏 Print (Print-on-Demand)","22–25 €","einmalig","Physisches Kartenset, gedruckt erst bei Bestellung.",["20 Karten, physisch gedruckt","Druck über Print-on-Demand-Partner","Robustes Format für den Alltag","Ideal für die Kitteltasche"],"M3 Vorbestellung Print",highlight=True,badge="Beliebt"),
        preis_karte("🏫 Träger-Lizenz","Auf Anfrage","","Für Träger, die das ganze Team ausstatten wollen.",["Lizenzpaket fürs ganze Team","Für mehrere Standorte geeignet","Individuelle Stückzahlen möglich","Auf Wunsch mit Einführung"],"M3 Träger-Lizenz Anfrage",btn_text="Jetzt anfragen"),
    ],
    ref_text="Anja Jolk hat die Werkzeugkarten als niedrigschwellige Ergänzung zu den ausführlicheren KLARTEXT-Materialien entwickelt — für Momente, in denen es schnell gehen muss. Neben ihrer Ausbildung als systemische Beraterin und Coachin bringt sie eine Fortbildung in Transitionspsychiatrie mit (Note 1.7, Prof. Dr. Jörg Fegert, Uniklinikum Ulm) sowie Qualifikationen als Fachkraft für Integrationspädagogik und als Sprachentwicklungsexpertin.",
    faq=[
        ("Was ist der Unterschied zu den Coaching-Impulskarten wie KD?","Werkzeugkarten sind Handlungsanleitungen für die Fachkraft, keine Gesprächsfragen für das Kind — für den schnellen Griff im Alltag."),
        ("Was ist der Unterschied zum Krisendeck?","Werkzeugkarten sind für Gelb/Orange gedacht — vorbeugend und regulierend. Das Krisendeck ist für Barometer Rot, akute Krisen."),
        ("Ist das Deck auch ohne die KLARTEXT-App nutzbar?","Ja, eigenständig nutzbar — ganz ohne Zugang, Login oder Internetverbindung."),
        ("Kann mein Träger über Rechnung bezahlen?","Ja, wie bei allen KLARTEXT-Materialien stellen wir gerne eine Rechnung aus."),
    ],
    cta_titel="Die Werkzeugkarten sind startklar", cta_sub="Trag dich unverbindlich für die Vorbestellung ein.",
    footer_typ="Handlungskartendeck",
)

# ---------- Mobbing-Materialien (MB) ----------
DECKS["mb"] = dict(
    dateiname="MB_Verkaufsseite.html", code="MB", seiten_titel="Mobbing-Soforthilfe-Materialien",
    hero_badge="🆘 MB · Soforthilfe-Mini-Deck",
    hero_h1='Im ersten Moment zählt<br><span>Handlungssicherheit.</span>',
    hero_sub="3 Soforthilfe-Karten für akute Mobbingfälle im Quick-Reference-Format — plus 3 bestehende A5-Vorlagen als gebündeltes PDF.",
    hero_stats=[("3","Soforthilfe-Karten"),("+3","A5-Vorlagen inklusive"),("fertig","Karten & PDF stehen")],
    fuer_wen_titel="das MB-Set", fuer_wen_sub="Für den ersten Moment, wenn ein akuter Mobbingfall auftritt.",
    fuer_wen=[
        ("🧑‍🏫","INGRA / Schulbegleitung","Ihr habt im akuten Moment sofort die richtigen ersten Schritte zur Hand."),
        ("📚","Lehrkräfte","Schnellorientierung für die ersten Minuten nach Bekanntwerden eines Mobbingfalls."),
        ("🏫","Träger","Ihr stattet euer Team mit einem einheitlichen Soforthilfe-Werkzeug aus."),
    ],
    leistungen_sub="Quick-Reference statt langem Handbuch — für den Moment, in dem schnelles Handeln zählt.",
    leistungen=[
        ("#1B3A4B","🆘","3 Soforthilfe-Karten","Icon statt Illustration, Quick-Reference-Format wie Werkzeugkarten/Krisendeck — für den ersten Moment."),
        ("#D81B60","📄","3 A5-Vorlagen inklusive","Die bestehenden ausführlichen A5-Vorlagen werden unverändert als zusätzliches PDF gebündelt."),
        ("#6EC6A0","✅","Inhaltlich fachlich geprüft","Basierend auf den bereits vorhandenen, geprüften Mobbing-Materialien der KLARTEXT-App."),
        ("#C47A00","🖨️","Digital oder Print","Sofort als PDF zum Download, oder als physisches Kartenset im Print-on-Demand-Verfahren."),
    ],
    blocks_titel=None, blocks_sub=None, blocks=None,
    quellen=None, quellen_sub=None,
    baro_klar=False,
    zitat="&bdquo;Der erste Moment entscheidet oft, ob sich ein Kind gesehen fühlt.&ldquo;",
    status_hinweis="Die Kartentexte stehen bereits — alle 3, plus 3 A5-Vorlagen als Bonus.",
    preise=[
        preis_karte("📄 Digital / PDF","8–10 €","einmalig","Sofort als Download nach Erscheinen.",["3 Soforthilfe-Karten als PDF","Bonus: 3 A5-Vorlagen inklusive","Sofort selbst ausdruckbar","Dauerhafter Zugriff"],"MB Vorbestellung Digital/PDF"),
        preis_karte("🃏 Print (Print-on-Demand)","14–16 €","einmalig","Physisches Kartenset, gedruckt erst bei Bestellung.",["3 Karten, physisch gedruckt","Druck über Print-on-Demand-Partner","Robustes Format für den Akutfall","Ideal für die Kitteltasche"],"MB Vorbestellung Print",highlight=True,badge="Beliebt"),
        preis_karte("🏫 Träger-Lizenz","Auf Anfrage","","Für Träger, die das ganze Team ausstatten wollen.",["Lizenzpaket fürs ganze Team","Für mehrere Standorte geeignet","Individuelle Stückzahlen möglich","Auf Wunsch mit Einführung"],"MB Träger-Lizenz Anfrage",btn_text="Jetzt anfragen"),
    ],
    ref_text="Anja Jolk hat das Soforthilfe-Mini-Deck als schnellen ersten Zugriff entwickelt, ergänzend zu den ausführlicheren Mobbing-Materialien und den Geschichtenkarten. Neben ihrer Ausbildung als systemische Beraterin und Coachin bringt sie eine Fortbildung in Transitionspsychiatrie mit (Note 1.7, Prof. Dr. Jörg Fegert, Uniklinikum Ulm) sowie Qualifikationen als Fachkraft für Integrationspädagogik und als Sprachentwicklungsexpertin.",
    faq=[
        ("Was ist der Unterschied zu den Geschichtenkarten?","Die Geschichtenkarten sind für Gespräche mit dem Kind gedacht. MB ist ein Soforthilfe-Werkzeug für die Fachkraft im akuten Moment."),
        ("Was ist in den 3 A5-Vorlagen enthalten?","Bereits bestehende, ausführlichere Materialien zum Thema Mobbing — als Bonus-PDF ohne Mehrkosten enthalten."),
        ("Ist das Set auch ohne die KLARTEXT-App nutzbar?","Ja, eigenständig nutzbar — ganz ohne Zugang, Login oder Internetverbindung."),
        ("Kann mein Träger über Rechnung bezahlen?","Ja, wie bei allen KLARTEXT-Materialien stellen wir gerne eine Rechnung aus."),
    ],
    cta_titel="Die MB-Materialien sind startklar", cta_sub="Trag dich unverbindlich für die Vorbestellung ein.",
    footer_typ="Materialienset",
)

# ---------- Insel-Set (IS) ----------
DECKS["is"] = dict(
    dateiname="IS_Verkaufsseite.html", code="IS", seiten_titel="Insel-Set – Raumzonen für Schule & Zuhause",
    hero_badge="🏝️ IS · Insel-Set",
    hero_h1='Barometer und kLAR<br>brauchen einen <span>Ort.</span>',
    hero_sub="Das Insel-Set macht Raumstrukturierung konkret: Ruhe-, Regel-, Arbeits- und Emotions-Insel als Basis-Set, plus Erweiterungen — je eine Variante für Schule und für Zuhause.",
    hero_stats=[("8+8","Karten (Schule+Zuhause)"),("4","Basis-Inseln je Set"),("fertig","Karten & PDF stehen")],
    fuer_wen_titel="das Insel-Set", fuer_wen_sub="Für alle, die Barometer und kLAR räumlich sichtbar machen wollen.",
    fuer_wen=[
        ("🧑‍🏫","INGRA / Kita / Grundschule","Ihr richtet feste Orte für Ruhe, Regeln, Arbeit und Emotionen ein — Barometer wird räumlich greifbar."),
        ("👪","Eltern","Das Eltern-Set überträgt dasselbe Prinzip aufs Zuhause — inklusive Übergangs- und Geschwister-Konflikt-Insel."),
        ("🏫","Träger","Ihr stattet eure Einrichtung mit einem einheitlichen Raumkonzept aus, kompatibel zu Barometer/kLAR."),
    ],
    leistungen_sub="Barometer = Zustand, kLAR = Skript — dem Insel-Set fehlte bisher die dritte Ebene: der Ort.",
    leistungen=[
        ("#1B3A4B","🏝️","8 Inseln pro Set","Schul-Set: Basis-Set (Regel-, Ruhe-, Arbeits-, Emotions-Insel) + Erweiterungs-Set (Bewegungs-, Kreativ-, Gesprächs-, Material-Insel)."),
        ("#26A69A","🏠","Eltern-Set fürs Zuhause","Dieselben Inselfarben wie das Schul-Set, plus zwei neue: Übergangs-Insel und Geschwister-Konflikt-Insel."),
        ("#6EC6A0","🌡️","Funktional an Barometer/kLAR gekoppelt","Jede Insel ist einem Barometer-Zustand zugeordnet — z. B. Ruhe-Insel für Schritt R im kLAR-Modell."),
        ("#C47A00","🖨️","Druckvorlagen inklusive","Badge-Druckvorlage (laminierbar), Begleitkarte je Insel, gemeinsames Einführungs-Booklet fürs Morgenkreis-Ritual."),
    ],
    blocks_titel="Produktstruktur", blocks_sub="Zwei komplette Sets, dieselbe Logik, unterschiedliche Kontexte.",
    blocks=[("SCHUL-SET","4 Basis-Inseln + 4 Erweiterungs-Inseln"),
            ("ELTERN-SET","6 übertragene Inseln + Übergangs- &amp; Geschwister-Konflikt-Insel")],
    quellen=[
        "Kuypers, L. (2011). <em>The Zones of Regulation.</em> — Farbbasierte Selbstregulation, Grundprinzip für die Zustand-zu-Ort-Zuordnung.",
        "Siegel, D. (1999). <em>The Developing Mind.</em> — Window of Tolerance, Grundlage für die Reizreduktions-Logik der Ruhe-Insel.",
        "Dokumentierte &bdquo;Calming Corners&ldquo; in PBIS- und traumainformierten pädagogischen Ansätzen — Time-in- statt Time-out-Prinzip.",
    ],
    quellen_sub="Das Insel-Set überträgt anerkannte Selbstregulationsmodelle in ein konkretes Raumkonzept.",
    baro_klar=True,
    zitat="&bdquo;Wo findet Reizreduktion konkret statt? Das Insel-Set gibt dem kLAR-Modell einen Ort.&ldquo;",
    status_hinweis="Die Materialien stehen bereits — beide Sets, Druckvorlagen und Booklet.",
    preise=[
        preis_karte("📄 Digital / PDF","18–22 €","einmalig","Sofort als Download nach Erscheinen — ein Set (Schule ODER Zuhause).",["8 Insel-Begleitkarten + Badges als PDF","Einführungs-Booklet inklusive","Selbst laminierbar","Dauerhafter Zugriff"],"IS Vorbestellung Digital/PDF"),
        preis_karte("🏝️ Beide Sets (Schule + Zuhause)","32–36 €","einmalig","Schul-Set und Eltern-Set im Bundle — passend, weil Kinder dieselben Inseln wiedererkennen.",["16 Begleitkarten + Badges (8+8)","Zwei Einführungs-Booklets","Aufeinander abgestimmte Farben","Ideal für INGRA + Familie"],"IS Vorbestellung Bundle",highlight=True,badge="Beliebt"),
        preis_karte("🏫 Träger-Lizenz","Auf Anfrage","","Für Träger, die mehrere Einrichtungen ausstatten wollen.",["Lizenzpaket für mehrere Standorte","Individuelle Stückzahlen möglich","Auf Wunsch mit Einführung","Vinyl-Aufkleber als Zusatzoption"],"IS Träger-Lizenz Anfrage",btn_text="Jetzt anfragen"),
    ],
    ref_text="Anja Jolk hat das Insel-Set entwickelt, um Barometer und kLAR eine räumliche Ebene zu geben — abgesichert durch Kuypers' Zones of Regulation und traumainformierte Calming-Corner-Ansätze. Neben ihrer Ausbildung als systemische Beraterin und Coachin bringt sie eine Fortbildung in Transitionspsychiatrie mit (Note 1.7, Prof. Dr. Jörg Fegert, Uniklinikum Ulm) sowie Qualifikationen als Fachkraft für Integrationspädagogik und als Sprachentwicklungsexpertin.",
    faq=[
        ("Sind das Aufkleber oder Druckvorlagen?","Standard ist Selbstausdruck als PDF-Druckvorlage (Badge), die man laminiert und mit Klebeband oder Lochung anbringt. Vinyl-Aufkleber sind auf Anfrage als Zusatzoption möglich."),
        ("Erkennt mein Kind die Insel aus der Schule auch zuhause wieder?","Ja, das war ein bewusstes Designziel — gleicher Inseltyp, gleiche Farbe in Schul- und Eltern-Set."),
        ("Brauche ich das Erweiterungs-Set zwingend?","Nein, das Basis-Set (4 Inseln) deckt die wichtigsten Barometer-Zustände bereits ab. Das Erweiterungs-Set ist optional."),
        ("Kann mein Träger über Rechnung bezahlen?","Ja, wie bei allen KLARTEXT-Materialien stellen wir gerne eine Rechnung aus."),
    ],
    cta_titel="Das Insel-Set ist startklar", cta_sub="Trag dich unverbindlich für die Vorbestellung ein.",
    footer_typ="Raumzonen-Set",
)

# ---------- Zonen-Set (ZS) ----------
DECKS["zs"] = dict(
    dateiname="ZS_Verkaufsseite.html", code="ZS", seiten_titel="Zonen-Set Jugendliche – Schule & Zuhause",
    hero_badge="🏝️ ZS · Zonen-Set Jugendliche",
    hero_h1='Selbstregulation —<br><span>ohne Bühne, ohne Stigma.</span>',
    hero_sub="Das Zonen-Set überträgt das Insel-Prinzip auf Jugendliche: 4 Zonen, unauffällige Raummarkierung und ein Token-Kartensystem statt sichtbarem Hingehen.",
    hero_stats=[("4+4","Karten (Schule+Zuhause)"),("4","Zonen"),("fertig","Karten & PDF stehen")],
    fuer_wen_titel="das Zonen-Set", fuer_wen_sub="Für den Sek-I/II-Kontext, wo Sichtbarkeit zum Stigma-Risiko wird.",
    fuer_wen=[
        ("📚","Lehrkräfte Sek I/II","Ihr ermöglicht Selbstregulation, ohne dass Jugendliche sich vor der Klasse erklären müssen."),
        ("🧑‍🏫","INGRA / Schulbegleitung","Ihr nutzt das Token-System als unauffälligen Kanal für Rückzug, Fokus, Klärung oder Gespräch."),
        ("🏫","Träger","Ihr stattet eure weiterführende Einrichtung mit einem altersgerechten Regulationssystem aus."),
    ],
    leistungen_sub="Weniger Zonen, neutrale Symbole, unauffällige Selbstwahl — bewusst anders als das Insel-Set für Kinder.",
    leistungen=[
        ("#1B3A4B","🚪","4 Zonen","Rückzugs-Zone, Fokus-Zone, Klärungs-Zone, Gesprächs-Zone — der Kern statt 8 kindlicher Inseln."),
        ("#5B7A80","🎫","Token-Karten statt sichtbarem Gang","4 Karten im Scheckkartenformat pro Person — eine Karte legen statt öffentlich durch den Raum laufen."),
        ("#37474F","🏠","Auch fürs Zuhause","Gleiche Logik, gleiche Farben — Eltern können das System zuhause spiegeln."),
        ("#C47A00","🖨️","Druckvorlagen inklusive","Raummarkierung (A6), Token-Karten, Mini-Handbuch mit Begründung und Quellen für LK/INGRA."),
    ],
    blocks_titel="Die 4 Zonen", blocks_sub="Bewusst reduziert gegenüber dem Insel-Set für jüngere Kinder.",
    blocks=[("RÜCKZUGS-ZONE","Reizreduktion, alleine sein dürfen"),
            ("FOKUS-ZONE","Konzentriertes Arbeiten, Lernzeit"),
            ("KLÄRUNGS-ZONE","Kurze Konfliktklärung, sachlich statt 'Regel'-Framing"),
            ("GESPRÄCHS-ZONE","1:1-Gespräch mit Vertrauensperson, auf eigenen Wunsch")],
    quellen=[
        "Kuypers, L. (2011). <em>The Zones of Regulation.</em> — Grundprinzip, von der Autorin selbst auch für die Sek-I-Altersgruppe adressiert.",
        "Siegel, D. (1999). <em>The Developing Mind.</em> — Window of Tolerance.",
        "Deci, E. &amp; Ryan, R. — Selbstbestimmungstheorie. Grundlage für die bewusste Autonomie in der Zonen-Selbstwahl statt Fremdsteuerung.",
    ],
    quellen_sub="Dieselbe Forschungsbasis wie das Insel-Set, ergänzt um die Selbstbestimmungstheorie als Grundlage für die diskrete Selbstwahl.",
    baro_klar=True,
    zitat="&bdquo;Was bei jüngeren Kindern Teil des Rituals sein darf, würde bei Jugendlichen genau das Gegenteil bewirken — deshalb keine Bühne, sondern ein Token.&ldquo;",
    status_hinweis="Die Materialien stehen bereits — beide Sets, Druckvorlagen und Mini-Handbuch.",
    preise=[
        preis_karte("📄 Digital / PDF","15–18 €","einmalig","Sofort als Download nach Erscheinen — Schul-Set.",["4 Raummarkierungen + Token-Karten-Vorlage als PDF","Mini-Handbuch inklusive","Selbst laminierbar","Dauerhafter Zugriff"],"ZS Vorbestellung Digital/PDF"),
        preis_karte("🎫 Print (Print-on-Demand)","24–27 €","einmalig","Physisches Set, gedruckt erst bei Bestellung.",["Raummarkierungen + Token-Karten, physisch gedruckt","Druck über Print-on-Demand-Partner","Scheckkartenformat, robust laminiert","Ideal für Sek I/II"],"ZS Vorbestellung Print",highlight=True,badge="Beliebt"),
        preis_karte("🏫 Träger-/Schul-Lizenz","Auf Anfrage","","Für Träger und weiterführende Schulen fürs ganze System.",["Lizenzpaket für mehrere Klassen","Individuelle Stückzahlen möglich","Auf Wunsch mit Einführung","Für mehrere Standorte geeignet"],"ZS Träger-/Schul-Lizenz Anfrage",btn_text="Jetzt anfragen"),
    ],
    ref_text="Anja Jolk hat das Zonen-Set als altersgerechte Weiterentwicklung des Insel-Set-Prinzips für Jugendliche entwickelt — mit besonderem Augenmerk auf das höhere Stigma-Risiko in dieser Altersgruppe. Neben ihrer Ausbildung als systemische Beraterin und Coachin bringt sie eine Fortbildung in Transitionspsychiatrie mit (Note 1.7, Prof. Dr. Jörg Fegert, Uniklinikum Ulm) sowie Qualifikationen als Fachkraft für Integrationspädagogik und als Sprachentwicklungsexpertin.",
    faq=[
        ("Warum nur 4 Zonen statt 8 Inseln wie im Kinder-Set?","Bewegungs-, Kreativ-, Emotions- und Material-Insel wurden bewusst nicht übernommen — zu kleinteilig/kindlich für die Altersgruppe. Emotionsregulation läuft bei Jugendlichen eher über die Rückzugs-Zone plus Barometer."),
        ("Wie funktioniert die Selbstwahl konkret?","Jede/r Jugendliche bekommt 4 Token-Karten im Scheckkartenformat. Wer eine Zone braucht, legt die passende Karte ab — die Lehrkraft bestätigt per Blickkontakt, ohne öffentliche Ansage."),
        ("Gibt es auch ein Eltern-Pendant?","Aktuell nicht separat vorgesehen, da der Fokus auf dem Schulkontext liegt — bei Bedarf später ergänzbar."),
        ("Kann meine Schule/mein Träger über Rechnung bezahlen?","Ja, wie bei allen KLARTEXT-Materialien stellen wir gerne eine Rechnung aus."),
    ],
    cta_titel="Das Zonen-Set ist startklar", cta_sub="Trag dich unverbindlich für die Vorbestellung ein.",
    footer_typ="Raumzonen-Set",
)

print("Alle Deck-Daten geladen:", list(DECKS.keys()))

# ============================================================
# BUILD LOOP
# ============================================================

photo_line = open('/tmp/photo_line.txt', encoding='utf-8').read()
_start = photo_line.index('<img')
_end = photo_line.index('</div>', _start)
IMG_TAG = photo_line[_start:_end]

TAG_RE_OPEN = re.compile(r'<(section|div|nav|footer|a|style|head|body|html)\b')
TAG_RE_CLOSE = re.compile(r'</(section|div|nav|footer|a|style|head|body|html)>')

results = []
for key, d in DECKS.items():
    html = build_page(d)
    html = html.replace('__PHOTO_IMG__', IMG_TAG)
    path = d["dateiname"]
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    opens = Counter(TAG_RE_OPEN.findall(html))
    closes = Counter(TAG_RE_CLOSE.findall(html))
    mismatches = {t: (opens.get(t,0), closes.get(t,0)) for t in set(list(opens)+list(closes)) if opens.get(t,0) != closes.get(t,0)}
    results.append((path, len(html), mismatches))

print("\n=== ERGEBNIS ===")
for path, ln, mismatches in results:
    status = "OK" if not mismatches else f"MISMATCH {mismatches}"
    print(f"{path}: {ln} Zeichen — {status}")
