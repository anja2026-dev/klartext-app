/* ══════════════════════════════════════════════════════════════════════
   KLARTEXT_ContextMapper.js

   Zweck: Macht Seiten, die pädagogische Begriffe verwenden (Schüler, Kind,
   Lehrkraft, Schultag, Hausaufgaben), im Gespräch mit erwachsenen
   Jobcoaching-Klient:innen professioneller nutzbar, ohne den
   schulpädagogischen Kern der Inhalte selbst zu verändern.

   Aktivierung: URL-Parameter ?modus=jobcoach ODER localStorage-Flag
   klartext_modus = 'jobcoach'. Ein per URL gesetzter Modus wird in
   localStorage gespiegelt, damit er über mehrere Seiten der gleichen
   Sitzung hinweg erhalten bleibt (sonst müsste der Parameter bei jedem
   Klick manuell wieder angehängt werden). ?modus=schule schaltet aktiv
   zurück und löscht das Flag.

   Einbindung: <script src="KLARTEXT_ContextMapper.js"></script> kurz vor
   </body>, NACH den Skripten, die die Seite selbst aufbauen — dann fängt
   der erste Durchlauf bereits synchron gerendertes JSON-/JS-generiertes
   HTML ab, und ein MutationObserver deckt alles ab, was danach noch
   dynamisch entsteht (Tab-Wechsel, Muster laden, Profil-Overlay etc.).

   ── Bekannte, bewusste Vereinfachungen (lightweight, kein NLP) ──────────
   1. „Kontextabhängig" Schüler/Kind → Teilnehmer ODER Klient ist mit
      reinem Text-Ersetzen nicht sauber entscheidbar (das bräuchte
      Satzverständnis, nicht nur Wortabgleich). Es wird EINE feste
      Zielformulierung pro Begriffsfamilie verwendet (s. u.). Wer lieber
      „Klient:in" statt „Teilnehmer:in" möchte, ändert das an einer
      Stelle in ERSETZUNGEN weiter unten.
   2. Die Begriffslisten decken die im Auftrag genannten Wortfamilien in
      ihren gängigen Flexionsformen ab (Singular/Plural/Genitiv/Dativ),
      nicht die komplette deutsche Grammatik. Taucht in der Praxis eine
      Form auf, die nicht erfasst wird, einfach unten ergänzen.
   3. Nur Textknoten und die Attribute placeholder/aria-label/title werden
      ersetzt — NIE der value eines Eingabefelds, damit echte
      Nutzereingaben nie überschrieben werden.
   ────────────────────────────────────────────────────────────────────── */

(function () {
  'use strict';

  var STORAGE_KEY = 'klartext_modus';
  var MODUS_WERT = 'jobcoach';

  /* ── Aktivierung ermitteln + persistieren ─────────────────────────── */
  var urlModus = null;
  try {
    urlModus = new URLSearchParams(window.location.search).get('modus');
  } catch (e) { /* ältere Umgebungen ohne URLSearchParams: ignorieren, localStorage greift trotzdem */ }

  if (urlModus === MODUS_WERT) {
    try { localStorage.setItem(STORAGE_KEY, MODUS_WERT); } catch (e) {}
  } else if (urlModus === 'schule') {
    try { localStorage.removeItem(STORAGE_KEY); } catch (e) {}
  }

  function istAktiv() {
    if (urlModus === MODUS_WERT) return true;
    if (urlModus === 'schule') return false;
    try { return localStorage.getItem(STORAGE_KEY) === MODUS_WERT; } catch (e) { return false; }
  }

  /* ── Begriffs-Mapping ──────────────────────────────────────────────
     Reihenfolge in der Liste ist egal — sie wird unten automatisch nach
     Musterlänge absteigend sortiert, damit z. B. "Lehrkraft reagiert"
     immer vor der generischen "Lehrkraft"-Regel greift und "Schülerinnen"
     nicht erst als "Schüler" + Rest-"innen" fehlinterpretiert wird. */
  var ERSETZUNGEN_ROH = [
    // Spezialfall Joker-Karte (Punkt 2 des Auftrags) — vor der generischen Lehrkraft-Regel
    { muster: 'Lehrkraft reagiert', ersatz: 'Mein Gegenüber reagiert' },
    { muster: 'Lehrkräfte reagieren', ersatz: 'Meine Gegenüber reagieren' },

    // Schüler-Familie → Teilnehmer:in
    { muster: 'Schülerinnen und Schüler', ersatz: 'Teilnehmerinnen und Teilnehmer' },
    { muster: 'Schüler:innen', ersatz: 'Teilnehmer:innen' },
    { muster: 'Schülerinnen', ersatz: 'Teilnehmerinnen' },
    { muster: 'Schülerin', ersatz: 'Teilnehmerin' },
    { muster: 'Schülern', ersatz: 'Teilnehmern' },
    { muster: 'Schüler', ersatz: 'Teilnehmer' },

    // Kind-Familie → Teilnehmer:in (feste Wahl, s. Hinweis oben zur Kontextabhängigkeit)
    { muster: 'Kindern', ersatz: 'Teilnehmenden' },
    { muster: 'Kindes', ersatz: 'Teilnehmenden' },
    { muster: 'Kinder', ersatz: 'Teilnehmende' },
    { muster: 'Kind', ersatz: 'Teilnehmer:in' },

    // Lehrkraft-Familie → Coach
    { muster: 'Lehrkräften', ersatz: 'Coaches' },
    { muster: 'Lehrkräfte', ersatz: 'Coaches' },
    { muster: 'Lehrkraft', ersatz: 'Coach' },

    // Schultag-Familie → Arbeitstag
    { muster: 'Schultagen', ersatz: 'Arbeitstagen' },
    { muster: 'Schultage', ersatz: 'Arbeitstage' },
    { muster: 'Schultag', ersatz: 'Arbeitstag' },

    // Hausaufgaben-Familie → Aufgaben
    { muster: 'Hausaufgaben', ersatz: 'Aufgaben' },
    { muster: 'Hausaufgabe', ersatz: 'Aufgabe' }
  ];

  function regexEscape(text) {
    return text.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  }

  var ERSETZUNGEN = ERSETZUNGEN_ROH
    .slice()
    .sort(function (a, b) { return b.muster.length - a.muster.length; })
    .map(function (e) {
      return { regex: new RegExp('\\b' + regexEscape(e.muster) + '\\b', 'gi'), ersatz: e.ersatz };
    });

  function textErsetzen(text) {
    var ergebnis = text;
    for (var i = 0; i < ERSETZUNGEN.length; i++) {
      ergebnis = ergebnis.replace(ERSETZUNGEN[i].regex, ERSETZUNGEN[i].ersatz);
    }
    return ergebnis;
  }

  /* ── DOM-sicheres Ersetzen: nur Textknoten + ausgewählte Attribute,
     nie innerHTML, nie der value eines Eingabefelds. ─────────────────── */
  var IGNORIERTE_TAGS = ['SCRIPT', 'STYLE', 'NOSCRIPT', 'TEXTAREA', 'CODE'];
  var ATTRIBUTE = ['placeholder', 'aria-label', 'title'];

  function textknotenErsetzen(root) {
    if (!document.createTreeWalker) return;
    var walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
      acceptNode: function (node) {
        var eltern = node.parentNode;
        if (eltern && eltern.tagName && IGNORIERTE_TAGS.indexOf(eltern.tagName) !== -1) {
          return NodeFilter.FILTER_REJECT;
        }
        return NodeFilter.FILTER_ACCEPT;
      }
    });
    var knoten = [];
    var n;
    while ((n = walker.nextNode())) knoten.push(n);
    knoten.forEach(function (node) {
      var neu = textErsetzen(node.nodeValue);
      if (neu !== node.nodeValue) node.nodeValue = neu;
    });
  }

  function attributeErsetzen(root) {
    if (!root.querySelectorAll) return;
    ATTRIBUTE.forEach(function (attr) {
      var elemente = root.querySelectorAll('[' + attr + ']');
      elemente.forEach(function (el) {
        var wert = el.getAttribute(attr);
        var neu = textErsetzen(wert);
        if (neu !== wert) el.setAttribute(attr, neu);
      });
    });
  }

  function anwenden(root) {
    root = root || document.body;
    textknotenErsetzen(root);
    attributeErsetzen(root);
  }

  /* ── Läuft nach dynamisch nachgeladenem/gerendertem Inhalt automatisch
     erneut (Skill-Matrix-Cluster, Bewerbungs-Generator-Werdegang-Zeilen,
     Muster-Laden usw.) — ohne dass die aufrufenden Seiten etwas dafür tun
     müssen. Trennt sich während des eigenen Schreibens kurz vom
     Beobachten, damit die eigenen Änderungen keine Endlosschleife
     auslösen. ─────────────────────────────────────────────────────── */
  var beobachter = null;
  function beobachtungStarten() {
    if (beobachter || !window.MutationObserver) return;
    beobachter = new MutationObserver(function () {
      beobachter.disconnect();
      anwenden(document.body);
      beobachter.observe(document.body, { childList: true, subtree: true, characterData: true });
    });
    beobachter.observe(document.body, { childList: true, subtree: true, characterData: true });
  }

  function init() {
    if (!istAktiv()) return;
    anwenden(document.body);
    beobachtungStarten();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  /* ── Öffentliche API ──────────────────────────────────────────────
     Erlaubt Seiten, den Modus auch ohne Reload umzuschalten, und dient
     als manueller Trigger, falls eine Seite ganz sicher gehen will, dass
     nach einer eigenen Render-Aktion sofort ersetzt wird (der
     MutationObserver deckt das normalerweise bereits automatisch ab). */
  window.KLARTEXT_CONTEXT_MAPPER = {
    istAktiv: istAktiv,
    anwenden: function () { anwenden(document.body); },
    aktivieren: function () {
      try { localStorage.setItem(STORAGE_KEY, MODUS_WERT); } catch (e) {}
      anwenden(document.body);
      beobachtungStarten();
    },
    deaktivieren: function () {
      try { localStorage.removeItem(STORAGE_KEY); } catch (e) {}
      if (beobachter) { beobachter.disconnect(); beobachter = null; }
      console.info('KLARTEXT_ContextMapper: Modus deaktiviert. Bereits ersetzter Text bleibt bis zum Neuladen der Seite stehen (reine Text-Ersetzung, kein Undo).');
    }
  };
})();
