// ════════════════════════════════════════════════════════
// KLARTEXT · feedbackAdmin.js  (vollständig neu)
// Admin/Trainer: Feedback verwalten aus Firebase /feedback
// ════════════════════════════════════════════════════════
(function () {
  'use strict';

  // ── Zustand ────────────────────────────────────────────
  var alleEintraege = {};   // { key: eintrag }
  var liveRef       = null;
  var detailKey     = null; // aktuell geöffnetes Detail

  var filter = {
    rolle:    '',
    typ:      '',
    sterne:   0,
    vonDatum: '',
    bisDatum: ''
  };

  // ── Hilfsfunktionen ────────────────────────────────────
  function esc(s) {
    return String(s || '').replace(/&/g,'&amp;').replace(/</g,'&lt;')
      .replace(/>/g,'&gt;').replace(/"/g,'&quot;');
  }

  function fmtDatum(ts) {
    if (!ts) return '—';
    var d = new Date(ts);
    return d.toLocaleDateString('de-DE',{day:'2-digit',month:'2-digit',year:'numeric'})
      + ' · ' + d.toLocaleTimeString('de-DE',{hour:'2-digit',minute:'2-digit'});
  }

  function sterne(n, farbe) {
    var s = '';
    n = parseInt(n, 10) || 0;
    for (var i=1;i<=5;i++) s += '<span style="color:'+(i<=n?farbe||'#C47A00':'#DDD')+'">'+(i<=n?'★':'☆')+'</span>';
    return s;
  }

  function ratingFarbe(n) {
    n = parseInt(n,10)||0;
    if (n>=4) return '#2E7D32';
    if (n<=2) return '#C62828';
    return '#C47A00';
  }

  function bestimmeTyp(e) {
    if (e.quelle === 'KLARTEXT_Feedback_INGRA') return 'Testbogen';
    return 'Allgemeines Feedback';
  }

  function bestimmeRolle(e) {
    return e.userId ? e.userId.replace('_',' ') : (e.name||'anonym');
  }

  function kurzvorschau(e) {
    var text = e.textFeedback || '';
    if (!text && e.rohdaten) {
      text = [e.rohdaten.eindruck, e.rohdaten.fazit].filter(Boolean).join(' / ');
    }
    return text.length > 80 ? text.substring(0,80)+'…' : text;
  }

  // ── Filter anwenden ────────────────────────────────────
  function gefilterteIds() {
    return Object.keys(alleEintraege).filter(function(id) {
      var e = alleEintraege[id];
      if (e.archiviert) return false;
      if (filter.rolle  && (e.userId||'').indexOf(filter.rolle) < 0 &&
          (e.name||'').indexOf(filter.rolle) < 0) return false;
      if (filter.typ === 'testbogen' && e.quelle !== 'KLARTEXT_Feedback_INGRA') return false;
      if (filter.typ === 'allgemein' && e.quelle === 'KLARTEXT_Feedback_INGRA') return false;
      if (filter.sterne && parseInt(e.rating,10) !== filter.sterne) return false;
      if (filter.vonDatum) {
        var von = new Date(filter.vonDatum).getTime();
        if ((e.timestamp||0) < von) return false;
      }
      if (filter.bisDatum) {
        var bis = new Date(filter.bisDatum).getTime() + 86400000;
        if ((e.timestamp||0) > bis) return false;
      }
      return true;
    }).sort(function(a,b){
      return (alleEintraege[b].timestamp||0) - (alleEintraege[a].timestamp||0);
    });
  }

  // ── Liste rendern ──────────────────────────────────────
  function renderListe() {
    var container = document.getElementById('fb-liste');
    var zaehler   = document.getElementById('fb-zaehler');
    if (!container) return;

    var ids = gefilterteIds();
    var gesamt = Object.keys(alleEintraege).filter(function(id){
      return !alleEintraege[id].archiviert;
    }).length;
    var archiviert = Object.keys(alleEintraege).filter(function(id){
      return alleEintraege[id].archiviert;
    }).length;

    if (zaehler) zaehler.innerHTML =
      '<strong>' + ids.length + '</strong> Einträge' +
      (ids.length !== gesamt ? ' (gefiltert von ' + gesamt + ')' : '') +
      (archiviert ? ' · <span style="color:var(--muted);">' + archiviert + ' archiviert</span>' : '');

    if (ids.length === 0) {
      container.innerHTML = '<div class="fb-leer">Keine Einträge' +
        (Object.keys(filter).some(function(k){ return filter[k]; }) ? ' für diesen Filter' : '') +
        '.</div>';
      return;
    }

    container.innerHTML = ids.map(function(id) {
      var e = alleEintraege[id];
      var typ = bestimmeTyp(e);
      var rolle = bestimmeRolle(e);
      var farbe = ratingFarbe(e.rating);
      var gelesen = e.gelesen ? ' fb-gelesen' : ' fb-neu';
      return '<div class="fb-zeile' + gelesen + '" id="zeile-' + id + '">' +
        '<div class="fb-zeile-sterne">' + sterne(e.rating, farbe) + '</div>' +
        '<div class="fb-zeile-info">' +
          '<div class="fb-zeile-meta">' +
            '<span class="fb-chip fb-chip-rolle">' + esc(rolle) + '</span>' +
            '<span class="fb-chip fb-chip-typ' + (typ==='Testbogen'?' fb-chip-test':'') + '">' + esc(typ) + '</span>' +
            (e.gelesen ? '' : '<span class="fb-chip fb-chip-neu">Neu</span>') +
          '</div>' +
          '<div class="fb-zeile-datum">' + fmtDatum(e.timestamp) + '</div>' +
          '<div class="fb-zeile-vorschau">' + esc(kurzvorschau(e)) + '</div>' +
        '</div>' +
        '<button class="fb-detail-btn" onclick="zeigeDetail(\'' + id + '\')">Details ›</button>' +
      '</div>';
    }).join('');

    renderStatistik(ids);
  }

  // ── Statistik ──────────────────────────────────────────
  function renderStatistik(ids) {
    var stat = document.getElementById('fb-statistik');
    if (!stat) return;
    if (!ids || ids.length === 0) { stat.textContent = ''; return; }
    var summe = ids.reduce(function(s,id){ return s + (parseInt(alleEintraege[id].rating,10)||0); }, 0);
    var schnitt = (summe / ids.length).toFixed(1);
    var vert = [0,0,0,0,0];
    ids.forEach(function(id){ var r=parseInt(alleEintraege[id].rating,10)||0; if(r>=1&&r<=5) vert[r-1]++; });
    stat.innerHTML = 'Ø <strong>' + schnitt + '</strong> Sterne · ' +
      vert.map(function(n,i){ return (i+1)+'★: '+n; }).join(' · ');
  }

  // ── Detail-Panel ───────────────────────────────────────
  window.zeigeDetail = function(id) {
    detailKey = id;
    var e = alleEintraege[id];
    if (!e) return;

    // Als gelesen markieren
    if (!e.gelesen) {
      db.ref('feedback/'+id+'/gelesen').set(true).catch(function(){});
    }

    var panel = document.getElementById('fb-detail-panel');
    var overlay = document.getElementById('fb-overlay');
    if (!panel || !overlay) return;

    var typ = bestimmeTyp(e);
    var farbe = ratingFarbe(e.rating);

    // Rohdaten-Tabelle für Testbogen
    var rohdatenHtml = '';
    if (e.rohdaten) {
      var r = e.rohdaten;
      var felder = [
        ['Name', r.name], ['Erfahrung', r.erfahrung], ['Technik', r.tech],
        ['Erster Eindruck', r.eindruck], ['Orientierung', r.orientierung ? r.orientierung+' Sterne' : ''],
        ['Barometer genutzt', r.baro_nutzung], ['Barometer Bewertung', r.baro_bewertung ? r.baro_bewertung+' Sterne' : ''],
        ['Barometer Anmerkung', r.baro_anmerkung], ['Praxis', r.praxis],
        ['Praxis Situation', r.praxis_situation], ['Genutzte Funktionen', r.genutzt],
        ['Was fehlt', r.fehlt], ['Was stört', r.stoert], ['Empfehlung', r.empfehlung],
        ['Gesamtbewertung', r.gesamt ? r.gesamt+' Sterne' : ''],
        ['Fazit', r.fazit], ['Priorität', r.prio]
      ].filter(function(f){ return f[1]; });

      if (felder.length > 0) {
        rohdatenHtml = '<div class="fb-detail-sektion"><div class="fb-detail-sektion-titel">📋 Alle Antworten</div>' +
          '<table class="fb-rohdaten-tabelle">' +
          felder.map(function(f){
            return '<tr><td class="fb-roh-label">' + esc(f[0]) + '</td><td class="fb-roh-wert">' + esc(f[1]) + '</td></tr>';
          }).join('') +
          '</table></div>';
      }
    }

    panel.innerHTML =
      '<div class="fb-detail-kopf">' +
        '<div class="fb-detail-sterne">' + sterne(e.rating, farbe) + ' <span style="color:'+farbe+';font-weight:700;">' + (e.rating||'?') + '/5</span></div>' +
        '<div class="fb-detail-badges">' +
          '<span class="fb-chip fb-chip-rolle">' + esc(bestimmeRolle(e)) + '</span>' +
          '<span class="fb-chip fb-chip-typ' + (typ==='Testbogen'?' fb-chip-test':'') + '">' + esc(typ) + '</span>' +
        '</div>' +
        '<div class="fb-detail-datum">🕐 ' + fmtDatum(e.timestamp) + '</div>' +
      '</div>' +

      (e.textFeedback ? '<div class="fb-detail-sektion"><div class="fb-detail-sektion-titel">💬 Feedback-Text</div>' +
        '<div class="fb-detail-text">' + esc(e.textFeedback) + '</div></div>' : '') +

      rohdatenHtml +

      '<div class="fb-detail-aktionen">' +
        '<button class="fb-aktion-btn fb-aktion-lesen" onclick="alsGelesenMarkieren(\'' + id + '\')">' +
          (e.gelesen ? '✓ Gelesen' : '👁 Als gelesen markieren') + '</button>' +
        '<button class="fb-aktion-btn fb-aktion-archiv" onclick="archivieren(\'' + id + '\')">📦 Archivieren</button>' +
        '<button class="fb-aktion-btn fb-aktion-loeschen" onclick="loeschen(\'' + id + '\')">🗑 Löschen</button>' +
      '</div>';

    overlay.classList.add('aktiv');
  };

  // ── Aktionen ───────────────────────────────────────────
  window.alsGelesenMarkieren = function(id) {
    db.ref('feedback/'+id+'/gelesen').set(true)
      .then(function(){ zeigeDetail(id); })
      .catch(function(e){ alert('Fehler: '+e.message); });
  };

  window.archivieren = function(id) {
    if (!confirm('Eintrag archivieren?')) return;
    db.ref('feedback/'+id+'/archiviert').set(true)
      .then(function(){ schliesseDetail(); })
      .catch(function(e){ alert('Fehler: '+e.message); });
  };

  window.loeschen = function(id) {
    if (!confirm('Eintrag unwiderruflich löschen?')) return;
    db.ref('feedback/'+id).remove()
      .then(function(){ schliesseDetail(); })
      .catch(function(e){ alert('Fehler: '+e.message); });
  };

  window.schliesseDetail = function() {
    var overlay = document.getElementById('fb-overlay');
    if (overlay) overlay.classList.remove('aktiv');
    detailKey = null;
  };

  // ── Filter-Logik ───────────────────────────────────────
  window.filterAendern = function(feld, wert) {
    filter[feld] = wert;
    // Aktive Klasse auf Buttons setzen
    document.querySelectorAll('[data-filter="'+feld+'"]').forEach(function(btn){
      btn.classList.toggle('aktiv', btn.dataset.wert == wert);
    });
    renderListe();
  };

  window.filterZeitraum = function() {
    filter.vonDatum  = (document.getElementById('f-von')  || {}).value || '';
    filter.bisDatum  = (document.getElementById('f-bis')  || {}).value || '';
    renderListe();
  };

  window.filterZuruecksetzen = function() {
    filter = { rolle:'', typ:'', sterne:0, vonDatum:'', bisDatum:'' };
    document.querySelectorAll('.filter-btn').forEach(function(b){ b.classList.remove('aktiv'); });
    document.querySelectorAll('.filter-btn[data-wert=""]').forEach(function(b){ b.classList.add('aktiv'); });
    var von = document.getElementById('f-von'); if (von) von.value = '';
    var bis = document.getElementById('f-bis'); if (bis) bis.value = '';
    renderListe();
  };

  // ── Firebase live ──────────────────────────────────────
  function ladeEintraege() {
    var lade = document.getElementById('fb-lade');
    if (lade) lade.style.display = 'block';

    liveRef = db.ref('feedback');
    liveRef.on('value', function(snap) {
      alleEintraege = snap.val() || {};
      if (lade) lade.style.display = 'none';
      renderListe();
      // Detail aktualisieren falls offen
      if (detailKey && alleEintraege[detailKey]) zeigeDetail(detailKey);
    }, function(err) {
      if (lade) lade.style.display = 'none';
      var c = document.getElementById('fb-liste');
      if (c) c.innerHTML = '<div class="fb-leer" style="color:#C62828;">Fehler: ' + esc(err.message) + '</div>';
    });
  }

  // ── Init ───────────────────────────────────────────────
  function init() {
    ladeEintraege();
    // Overlay schließen bei Klick auf Hintergrund
    var overlay = document.getElementById('fb-overlay');
    if (overlay) overlay.addEventListener('click', function(ev){
      if (ev.target === overlay) schliesseDetail();
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else { init(); }

  window.addEventListener('beforeunload', function(){
    if (liveRef) liveRef.off('value');
  });
})();
