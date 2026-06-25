// ════════════════════════════════════════
// KLARTEXT CHAT — chat.js
// Etappe 7.1 — Grundgerüst
// Setzt voraus: firebase.js ist bereits geladen (stellt `db` bereit)
// ════════════════════════════════════════

// ── ROLLENFARBEN ──
const CHAT_ROLLENFARBEN = {
  ingra: '#1B3A4B',
  springer_ingra: '#1B3A4B',
  pool_ingra: '#3B8A68',
  vertretung_ingra: '#3B8A68',
  tk: '#C47A00',
  lk: '#1565C0',
  eltern: '#AD1457',
  trainer: '#B07D2A',
  admin: '#1B3A4B'
};

function chatRollenfarbe(rolle) {
  return CHAT_ROLLENFARBEN[rolle] || '#6A6878';
}

// ── AKTUELLER USER (aus sessionStorage, von KLARTEXT_Login.html gesetzt) ──
function chatAktuellerUser() {
  return {
    id: sessionStorage.getItem('klartext_user_id') || '',
    role: sessionStorage.getItem('klartext_role') || '',
    name: sessionStorage.getItem('klartext_name') || ''
  };
}

// ── ZEITFORMATIERUNG ──
function chatFormatZeit(timestamp) {
  if (!timestamp) return '';
  const datum = new Date(timestamp);
  const heute = new Date();
  const istHeute = datum.toDateString() === heute.toDateString();
  if (istHeute) {
    return datum.toLocaleTimeString('de-DE', { hour: '2-digit', minute: '2-digit' });
  }
  return datum.toLocaleDateString('de-DE', { day: '2-digit', month: '2-digit' }) +
         ' · ' + datum.toLocaleTimeString('de-DE', { hour: '2-digit', minute: '2-digit' });
}

function chatFormatZeitKurz(timestamp) {
  if (!timestamp) return '';
  const datum = new Date(timestamp);
  const heute = new Date();
  const istHeute = datum.toDateString() === heute.toDateString();
  if (istHeute) {
    return datum.toLocaleTimeString('de-DE', { hour: '2-digit', minute: '2-digit' });
  }
  return datum.toLocaleDateString('de-DE', { day: '2-digit', month: '2-digit' });
}

// ── CONVERSATIONS LADEN ──
// callback erhält ein Objekt { conversationId: conversationDaten, ... }
// gefiltert auf Konversationen, in denen der aktuelle User Mitglied ist
function chatLadeConversations(callback) {
  const user = chatAktuellerUser();
  if (!user.id) { callback({}); return; }

  db.ref('conversations').on('value', function(snapshot) {
    const alle = snapshot.val() || {};
    const gefiltert = {};
    Object.keys(alle).forEach(function(cid) {
      const conv = alle[cid];
      if (conv.members && conv.members[user.id]) {
        gefiltert[cid] = conv;
      }
    });
    callback(gefiltert);
  });
}

// ── NEUE CONVERSATION ANLEGEN ──
// targetUser: { id, name, role }
// gibt ein Promise zurück, das die neue conversationId liefert
function chatNeueConversation(targetUser, type, childId) {
  const user = chatAktuellerUser();
  const members = {};
  members[user.id] = true;
  members[targetUser.id] = true;

  const conversationDaten = {
    members: members,
    type: type || 'direct',
    lastMessage: '',
    lastTimestamp: Date.now()
  };
  if (childId) conversationDaten.childId = childId;

  // Zusätzlich Anzeigenamen der Mitglieder merken, damit die Chatliste
  // ohne weitere Lookups Namen anzeigen kann
  conversationDaten.memberNames = {};
  conversationDaten.memberNames[user.id] = user.name;
  conversationDaten.memberNames[targetUser.id] = targetUser.name;
  conversationDaten.memberRoles = {};
  conversationDaten.memberRoles[user.id] = user.role;
  conversationDaten.memberRoles[targetUser.id] = targetUser.role;

  return db.ref('conversations').push(conversationDaten).then(function(ref) {
    return ref.key;
  });
}

// ── NACHRICHT SENDEN ──
function chatNachrichtSenden(conversationId, text) {
  const user = chatAktuellerUser();
  if (!text || !text.trim()) return Promise.reject(new Error('Leere Nachricht'));

  const readBy = {};
  readBy[user.id] = true;

  const nachricht = {
    senderId: user.id,
    senderRole: user.role,
    senderName: user.name,
    text: text.trim(),
    timestamp: Date.now(),
    readBy: readBy,
    type: 'text'
  };

  return db.ref('messages/' + conversationId).push(nachricht).then(function(ref) {
    // lastMessage/lastTimestamp der Conversation aktualisieren, für die Chatliste
    db.ref('conversations/' + conversationId).update({
      lastMessage: nachricht.text,
      lastTimestamp: nachricht.timestamp
    });
    return ref.key;
  });
}

// ── NACHRICHTEN LIVE LADEN ──
// callback wird für jede neu eintreffende Nachricht aufgerufen (onChildAdded)
// gibt die Firebase-Referenz zurück, damit der Aufrufer sie später mit .off() abmelden kann
function chatLadeNachrichtenLive(conversationId, callback) {
  const ref = db.ref('messages/' + conversationId).orderByChild('timestamp');
  ref.on('child_added', function(snapshot) {
    callback(snapshot.key, snapshot.val());
  });
  return ref;
}

// ── READBY AKTUALISIEREN ──
// markiert eine einzelne Nachricht als gelesen durch den aktuellen User
function chatMarkiereGelesen(conversationId, messageId) {
  const user = chatAktuellerUser();
  if (!user.id) return;
  db.ref('messages/' + conversationId + '/' + messageId + '/readBy/' + user.id).set(true);
}

// markiert alle Nachrichten einer Konversation als gelesen (einmaliger Abruf, kein Live-Listener)
function chatMarkiereAlleGelesen(conversationId) {
  const user = chatAktuellerUser();
  if (!user.id) return;
  db.ref('messages/' + conversationId).once('value').then(function(snapshot) {
    const nachrichten = snapshot.val() || {};
    Object.keys(nachrichten).forEach(function(messageId) {
      const n = nachrichten[messageId];
      if (!n.readBy || !n.readBy[user.id]) {
        db.ref('messages/' + conversationId + '/' + messageId + '/readBy/' + user.id).set(true);
      }
    });
  });
}

// ── UNGELESENE NACHRICHTEN ZÄHLEN (für Chatliste-Badge) ──
// callback erhält die Anzahl ungelesener Nachrichten für eine Konversation
function chatZaehleUngelesen(conversationId, callback) {
  const user = chatAktuellerUser();
  db.ref('messages/' + conversationId).once('value').then(function(snapshot) {
    const nachrichten = snapshot.val() || {};
    let anzahl = 0;
    Object.keys(nachrichten).forEach(function(messageId) {
      const n = nachrichten[messageId];
      // eigene Nachrichten zählen nie als ungelesen
      if (n.senderId === user.id) return;
      if (!n.readBy || !n.readBy[user.id]) anzahl++;
    });
    callback(anzahl);
  });
}

// ── KONVERSATIONS-ANZEIGENAME ERMITTELN ──
// liefert den Namen, der in der Chatliste/im Header angezeigt werden soll
function chatKonversationsName(conv, kinderNamen) {
  const user = chatAktuellerUser();
  if (conv.type === 'child' && conv.childId) {
    return (kinderNamen && kinderNamen[conv.childId]) ? kinderNamen[conv.childId] : 'Kind';
  }
  if (conv.type === 'group') {
    return conv.groupName || 'Gruppe';
  }
  // direct: Name des jeweils ANDEREN Mitglieds
  if (conv.memberNames) {
    const andereId = Object.keys(conv.members || {}).find(function(id) { return id !== user.id; });
    if (andereId && conv.memberNames[andereId]) return conv.memberNames[andereId];
  }
  return 'Unbekannt';
}

// ════════════════════════════════════════
// BRAINY-COACH (Etappe 7.2) — reiner Copy-Paste-Helfer, KEINE API-Calls
// ════════════════════════════════════════

// sammelt die letzten 10 Nachrichten der aktuellen Konversation, formatiert als Textblock,
// schreibt sie ins Panel und blendet es ein. Reagiert nur auf Knopfdruck.
function brainyCoachStart() {
  if (typeof conversationId === 'undefined' || !conversationId) return;

  db.ref('messages/' + conversationId).orderByChild('timestamp').limitToLast(10).once('value').then(function(snapshot) {
    const nachrichten = snapshot.val() || {};
    const ids = Object.keys(nachrichten).sort(function(a, b) {
      return (nachrichten[a].timestamp || 0) - (nachrichten[b].timestamp || 0);
    });

    const zeilen = ids.map(function(id) {
      const n = nachrichten[id];
      const name = n.senderName || n.senderRole || 'Unbekannt';
      return name + ' (' + (n.senderRole || '?') + '): ' + (n.text || '');
    });

    document.getElementById('brainy-chattext').value = zeilen.join('\n');

    const panel = document.getElementById('brainy-panel');
    panel.classList.remove('hidden');

    // Winken-Animation erneut auslösen (Klasse kurz entfernen und wieder hinzufügen)
    const icon = document.getElementById('brainy-icon');
    icon.classList.remove('brainy-wink');
    void icon.offsetWidth; // erzwingt Reflow, damit die Animation neu startet
    icon.classList.add('brainy-wink');
  });
}

// kopiert den Chatverlauf-Text in die Zwischenablage, zum Einfügen in eine beliebige KI
function brainyCopy() {
  const feld = document.getElementById('brainy-chattext');
  feld.select();
  navigator.clipboard.writeText(feld.value).catch(function() {
    document.execCommand('copy'); // Fallback für ältere Browser
  });
}

// übernimmt den manuell eingefügten KI-Vorschlag ins Chat-Eingabefeld
function brainyUebernehmen() {
  const vorschlag = document.getElementById('brainy-vorschlag').value;
  if (!vorschlag.trim()) return;
  const eingabe = document.getElementById('chat-eingabe');
  if (eingabe) {
    eingabe.value = vorschlag;
    eingabe.dispatchEvent(new Event('input')); // löst die Auto-Resize-Logik der Eingabe aus
    eingabe.focus();
  }
}
