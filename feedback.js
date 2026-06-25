// ════════════════════════════════════════
// KLARTEXT · feedback.js
// Allgemeines System-Feedback
// Speichert unter /feedback in Firebase Realtime Database
// Setzt voraus: firebase.js ist geladen (stellt `db` bereit)
// ════════════════════════════════════════

(function () {
  'use strict';

  // ── Zustand ──────────────────────────────────────────────
  var gewaehltesRating = 0;

  // ── Hilfsfunktionen ──────────────────────────────────────
  function userId() {
    try { return sessionStorage.getItem('klartext_user_id') || 'anonym'; }
    catch (e) { return 'anonym'; }
  }

  function deviceInfo() {
    try { return navigator.userAgent || ''; }
    catch (e) { return ''; }
  }

  function elById(id) {
    return document.getElementById(id);
  }

  function zeigeFehler(msg) {
    var el = elById('fb-fehler');
    if (!el) return;
    el.textContent = msg;
    el.style.display = 'block';
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  function verbergeFehler() {
    var el = elById('fb-fehler');
    if (el) el.style.display = 'none';
  }

  // ── Sterne-Bewertung ─────────────────────────────────────
  function sternAktivieren(wert) {
    gewaehltesRating = wert;
    for (var i = 1; i <= 5; i++) {
      var stern = elById('stern-' + i);
      if (stern) stern.classList.toggle('aktiv', i <= wert);
    }
    var hinweis = elById('sterne-hinweis');
    if (hinweis) hinweis.textContent = wert + ' von 5 Sternen';
  }

  // ── Formular absenden ────────────────────────────────────
  function feedbackAbsenden() {
    verbergeFehler();

    if (gewaehltesRating === 0) {
      zeigeFehler('Bitte wähle eine Bewertung (1–5 Sterne).');
      return;
    }

    var textFeedback = (elById('fb-text') ? elById('fb-text').value.trim() : '');
    var btn = elById('fb-btn');

    if (btn) { btn.disabled = true; btn.textContent = 'Wird gesendet …'; }

    var eintrag = {
      userId:      userId(),
      rating:      gewaehltesRating,
      textFeedback: textFeedback,
      timestamp:   Date.now(),
      deviceInfo:  deviceInfo()
    };

    db.ref('feedback').push(eintrag)
      .then(function () {
        // Formular ausblenden, Bestätigung einblenden
        var formular = elById('fb-formular');
        var bestaetigung = elById('fb-bestaetigung');
        if (formular) formular.style.display = 'none';
        if (bestaetigung) bestaetigung.style.display = 'block';
      })
      .catch(function (error) {
        if (btn) { btn.disabled = false; btn.textContent = 'Feedback absenden'; }
        zeigeFehler('Fehler beim Senden: ' + error.message);
      });
  }

  // ── Init: Event-Listener nach DOM-Load ───────────────────
  function init() {
    // Stern-Buttons
    for (var i = 1; i <= 5; i++) {
      (function (wert) {
        var stern = elById('stern-' + wert);
        if (stern) stern.addEventListener('click', function () { sternAktivieren(wert); });
      })(i);
    }

    // Senden-Button
    var btn = elById('fb-btn');
    if (btn) btn.addEventListener('click', feedbackAbsenden);

    // Enter im Textfeld sendet NICHT (Zeilenumbruch erlauben)
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
