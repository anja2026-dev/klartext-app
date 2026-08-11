/* ══════════════════════════════════════════════════════════════════════
   KLARTEXT_Profil_Codec.js

   Zweck: Gemeinsam genutzte Kodier-/Dekodier-Logik für die
   "Superpower-Card" (KLARTEXT_Superpower_Card.html, erzeugt die
   Druckvorlage + den QR-Code) und die Profil-Ansicht
   (KLARTEXT_Profil_Ansicht.html, die Zielseite des QR-Codes).

   Bewusste Design-Entscheidung: Im QR-Code/Link werden NUR der Name und
   die IDs der Top-3-Cluster kodiert (kurz, z. B. "n=Alex&c=team,fokus").
   Nicht kodiert werden Hobbys, konkrete Berufsfelder oder Beispielberufe
   aus dem Superpower-Profil — das würde den QR-Code unnötig groß/schwer
   scanbar machen UND mehr persönliche Details preisgeben, als für eine
   Karte im Bewerbungskontext nötig sind. Titel, Icon und die
   berufsbezogene Kurzbeschreibung je Cluster werden stattdessen aus der
   Tabelle CLUSTER_INFO unten nachgeschlagen — sie ist bewusst identisch
   zu den echten Cluster-Daten aus KLARTEXT_Spiel_SkillMatrix.html
   (id/icon/titel) sowie zu CLUSTER_STAERKE_LABEL aus
   KLARTEXT_Bewerbungs_Generator.html (gleiche Berufssprache wie im
   Anschreiben/Lebenslauf).

   Das eigentliche Superpower-Profil (mit Hobbys etc.) bleibt weiterhin
   ausschließlich im localStorage des Teilnehmenden-Geräts unter dem
   Schlüssel klartext_skillmatrix_profil_v1 — die Profil-Ansicht liest es
   nur, wenn sie auf demselben Gerät ohne ?data=-Parameter aufgerufen
   wird (z. B. zur Vorschau vor dem Drucken).
   ══════════════════════════════════════════════════════════════════════ */
(function(){
  'use strict';

  // Muss exakt zu CLUSTERS (id/icon/titel) in KLARTEXT_Spiel_SkillMatrix.html
  // passen, damit ein gespeichertes Profil korrekt zugeordnet werden kann.
  var CLUSTER_INFO = {
    team:          { titel:'Team-Power',          icon:'🤝', staerke:'Teamfähigkeit' },
    fokus:         { titel:'Fokus-Champion',       icon:'🎯', staerke:'Konzentrationsfähigkeit & Ausdauer' },
    kreativ:       { titel:'Kreativ-Genie',        icon:'🎨', staerke:'Kreativität & Gestaltungsfreude' },
    verantwortung: { titel:'Verantwortungs-Anker', icon:'🧭', staerke:'Zuverlässigkeit' },
    problem:       { titel:'Problem-Löser',        icon:'🧩', staerke:'Lösungsorientierung' },
    mutig:         { titel:'Mutig & Stressfest',   icon:'💪', staerke:'Belastbarkeit' }
  };

  // Rueckwaerts-Lookup: Cluster-Titel (wie im gespeicherten Profil abgelegt) -> id
  var TITEL_ZU_ID = {};
  Object.keys(CLUSTER_INFO).forEach(function(id){
    TITEL_ZU_ID[CLUSTER_INFO[id].titel] = id;
  });

  var SKILLMATRIX_PROFIL_KEY = 'klartext_skillmatrix_profil_v1';

  /* Liest das zuletzt gespeicherte Superpower-Profil aus localStorage und
     gibt die Top-3-Cluster als Array von {id, titel, icon} zurueck (leeres
     Array, wenn kein Profil vorhanden ist oder ein Titel nicht bekannt
     ist — bekannt schuetzt vor kaputten/fremden Daten). */
  function clusterAusLocalStorage(){
    var roh;
    try { roh = localStorage.getItem(SKILLMATRIX_PROFIL_KEY); } catch(e) { return []; }
    if (!roh) return [];
    var daten;
    try { daten = JSON.parse(roh); } catch(e) { return []; }
    if (!daten || !Array.isArray(daten.cluster)) return [];
    return daten.cluster
      .map(function(c){
        var id = TITEL_ZU_ID[c.titel];
        return id ? { id: id, titel: CLUSTER_INFO[id].titel, icon: CLUSTER_INFO[id].icon } : null;
      })
      .filter(Boolean);
  }

  /* Baut den URL-Query-Teil fuer die Profil-Ansicht. clusterIds: Array von
     bis zu 3 bekannten Cluster-IDs (siehe CLUSTER_INFO). */
  function kodieren(name, clusterIds){
    var bekannt = (clusterIds || []).filter(function(id){ return !!CLUSTER_INFO[id]; }).slice(0, 3);
    var params = new URLSearchParams();
    params.set('n', (name || '').trim());
    params.set('c', bekannt.join(','));
    return params.toString();
  }

  /* Liest ?n= und ?c= aus einer URLSearchParams-Instanz (oder window.location.search,
     wenn nichts uebergeben wird). Gibt null zurueck, wenn kein "c"-Parameter
     vorhanden ist (= kein per QR/Link kodiertes Profil). */
  function dekodieren(searchParams){
    var params = searchParams || new URLSearchParams(window.location.search);
    if (!params.has('c')) return null;
    var name = (params.get('n') || '').trim();
    var ids = (params.get('c') || '').split(',').map(function(s){ return s.trim(); }).filter(Boolean);
    var cluster = ids
      .filter(function(id){ return !!CLUSTER_INFO[id]; })
      .map(function(id){ return { id:id, titel:CLUSTER_INFO[id].titel, icon:CLUSTER_INFO[id].icon, staerke:CLUSTER_INFO[id].staerke }; });
    return { name: name, cluster: cluster };
  }

  window.KLARTEXT_ProfilCodec = {
    CLUSTER_INFO: CLUSTER_INFO,
    clusterAusLocalStorage: clusterAusLocalStorage,
    kodieren: kodieren,
    dekodieren: dekodieren
  };
})();
