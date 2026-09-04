// KLARTEXT-Mentoring Karten – PWA app logic (kein Framework, kein Build-Schritt)

const screenDecks = document.getElementById('screen-decks');
const screenCards = document.getElementById('screen-cards');
const deckCategories = document.getElementById('deckCategories');
const backBtn = document.getElementById('backBtn');

// Kategorie-Reihenfolge + Überschriften, angelehnt an die Struktur der Shop-Übersichtsseite
// (klartext-shop/KLARTEXT_Shop_Uebersicht.html) — damit App und Website gleich sortiert wirken.
const KATEGORIEN = {
  zielgruppe: { titel: 'Kartendecks nach Zielgruppe', sub: 'Eigene Zielgruppe, eigene Impulse, dieselbe systemische Grundhaltung.' },
  handlung:   { titel: 'Handlungskarten & Spezialdecks', sub: 'Konkrete Handlungsanleitungen statt offener Coaching-Impulse.' },
  material:   { titel: 'Material-Pakete für Zuhause & Klassenzimmer', sub: 'Raumzonen-Konzepte statt Gesprächskarten.' },
};
const KATEGORIE_ORDER = ['zielgruppe', 'handlung', 'material'];
const progressEl = document.getElementById('progress');

const flashcard = document.getElementById('flashcard');
const cardImg = document.getElementById('cardImg');
const frontImgWrap = document.getElementById('frontImgWrap');
const frontIconWrap = document.getElementById('frontIconWrap');
const frontIcon = document.getElementById('frontIcon');
const cardBadge = document.getElementById('cardBadge');
const cardTitelFront = document.getElementById('cardTitelFront');
const cardTitelBack = document.getElementById('cardTitelBack');
const impulsBack = document.getElementById('impulsBack');
const cardAnleitung = document.getElementById('cardAnleitung');
const cardFragen = document.getElementById('cardFragen');
const cardHinweis = document.getElementById('cardHinweis');
const hinweisWrap = document.getElementById('hinweisWrap');
const systemfrageWrap = document.getElementById('systemfrageWrap');
const systemfrageLabel = document.getElementById('systemfrageLabel');
const cardSystemfrage = document.getElementById('cardSystemfrage');

const handlungBack = document.getElementById('handlungBack');
const introWrap = document.getElementById('introWrap');
const introLabel = document.getElementById('introLabel');
const cardIntro = document.getElementById('cardIntro');
const schritteLabel = document.getElementById('schritteLabel');
const cardSchritte = document.getElementById('cardSchritte');
const abgrenzungWrap = document.getElementById('abgrenzungWrap');
const cardAbgrenzung = document.getElementById('cardAbgrenzung');
const notizWrap = document.getElementById('notizWrap');
const notizLabel = document.getElementById('notizLabel');
const cardNotiz = document.getElementById('cardNotiz');

const prevBtn = document.getElementById('prevBtn');
const nextBtn = document.getElementById('nextBtn');
const shuffleBtn = document.getElementById('shuffleBtn');

const appleTouchIcon = document.getElementById('appleTouchIcon');
const DEFAULT_TITLE = document.title;
const DEFAULT_ICON = 'icons/icon-192.png';

const pwOverlay = document.getElementById('pwOverlay');
const pwDeckTitel = document.getElementById('pwDeckTitel');
const pwInput = document.getElementById('pwInput');
const pwError = document.getElementById('pwError');
const pwCancel = document.getElementById('pwCancel');
const pwSubmit = document.getElementById('pwSubmit');

let currentDeck = null;
let currentIndex = 0;
let allDecks = [];
let accessMap = {};

function lastIndexKey(deckId) { return `klartext_last_${deckId}`; }
function unlockedKey(deckId) { return `klartext_unlocked_${deckId}`; }
function isUnlocked(deckId) { return localStorage.getItem(unlockedKey(deckId)) === '1'; }

async function loadAccess() {
  try {
    const res = await fetch('data/access.json');
    accessMap = await res.json();
  } catch (e) {
    accessMap = {};
  }
}

async function sha256Hex(text) {
  const buf = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(text));
  return Array.from(new Uint8Array(buf)).map(b => b.toString(16).padStart(2, '0')).join('');
}

// Passwort pro Deck: Hash-Vergleich, damit der Klartext-Code nicht 1:1 im Code steht.
// Kein Ersatz für echten Login/Backend (die App bleibt eine rein statische Seite) — reicht
// aber als Zugriffsschranke gegen zufälliges/beiläufiges Mitlesen fremder, nicht gekaufter Decks.
async function checkPassword(deckId, pw) {
  const expected = accessMap[deckId];
  if (!expected) return false;
  const hash = await sha256Hex(`${deckId}:${pw.trim().toLowerCase()}`);
  return hash === expected;
}

function askForPassword(deckId, deckTitel) {
  return new Promise((resolve) => {
    pwDeckTitel.textContent = deckTitel;
    pwInput.value = '';
    pwError.hidden = true;
    pwOverlay.hidden = false;
    pwInput.focus();

    function cleanup() {
      pwOverlay.hidden = true;
      pwSubmit.removeEventListener('click', onSubmit);
      pwCancel.removeEventListener('click', onCancel);
      pwInput.removeEventListener('keydown', onKeydown);
    }
    async function onSubmit() {
      const ok = await checkPassword(deckId, pwInput.value);
      if (ok) {
        localStorage.setItem(unlockedKey(deckId), '1');
        cleanup();
        resolve(true);
      } else {
        pwError.hidden = false;
        pwInput.value = '';
        pwInput.focus();
      }
    }
    function onCancel() {
      cleanup();
      resolve(false);
    }
    function onKeydown(e) {
      if (e.key === 'Enter') { e.preventDefault(); onSubmit(); }
      if (e.key === 'Escape') { e.preventDefault(); onCancel(); }
    }
    pwSubmit.addEventListener('click', onSubmit);
    pwCancel.addEventListener('click', onCancel);
    pwInput.addEventListener('keydown', onKeydown);
  });
}

// Setzt Titel + apple-touch-icon passend zum offenen Deck, damit "Zum Home-Bildschirm
// hinzufügen" (während das Deck offen ist) ein eigenes, unterscheidbares Icon + einen
// eigenen Namen für genau dieses Deck übernimmt.
function setAppIdentity(deckOrNull) {
  if (!deckOrNull) {
    document.title = DEFAULT_TITLE;
    appleTouchIcon.setAttribute('href', DEFAULT_ICON);
    return;
  }
  document.title = `KLARTEXT – ${deckOrNull.titel}`;
  const deckIconUrl = `icons/deck-${deckOrNull.id}.png`;
  // Existenz-Check: falls für ein Deck noch kein eigenes Icon erzeugt wurde (z.B. neu
  // hinzugefügtes Deck), auf das allgemeine App-Icon zurückfallen statt ein kaputtes Bild.
  const probe = new Image();
  probe.onload = () => appleTouchIcon.setAttribute('href', deckIconUrl);
  probe.onerror = () => appleTouchIcon.setAttribute('href', DEFAULT_ICON);
  probe.src = deckIconUrl;
}

// ═══════════════════════════════════════
// 22.08.2026 Rollen-Sperre fuer Kartendecks: zusaetzlich zum bestehenden
// Zugangscode-System (pro Deck, localStorage) wird jetzt geprueft, ob die
// aktuelle klartext_role (gleiche Domain wie der App-Login) das jeweilige
// Deck ueberhaupt sehen/oeffnen darf. Ohne bekannte Rolle bleibt alles
// sichtbar (fail-open, wie ueberall sonst im System). Wird bei jedem
// 'pageshow' erneut angewendet, damit auch eine per Browser-Zurueck aus dem
// bfcache wiederhergestellte Ansicht den aktuellen Rollen-Stand zeigt statt
// eines veralteten, ungefilterten Snapshots.
// ═══════════════════════════════════════
const ROLLEN_DECKS = {
  ingra: null, tk: null, admin: null, // null = alle Decks erlaubt
  eltern: ['el', 'kd', 'at', 'fs', 'to', 'ds', 'lrs-sek1', 'insel-eltern', 'zonen-eltern', 'geschichtenkarten'],
  lehrkraft: ['lk', 'kd', 'at', 'fs', 'dazgs', 'dazsek1', 'ogs', 'to', 'ds', 'lrs-sek1', 'hb', 'insel-schule', 'zonen-schule', 'geschichtenkarten'],
  jobcoach: ['jd', 'adhs', 'zonen-schule', 'zonen-eltern', 'geschichtenkarten', 'werkzeug', 'krisendeck', 'mb'],
  mobbing: ['mb', 'smi', 'krisendeck', 'geschichtenkarten'],
};

function deckErlaubt(deckId) {
  const rolle = sessionStorage.getItem('klartext_role') || '';
  if (!rolle) return true; // keine Rolle bekannt -> nichts sperren
  if (!(rolle in ROLLEN_DECKS)) return true; // unbekannte Rolle -> fail-open
  const erlaubt = ROLLEN_DECKS[rolle];
  return erlaubt === null || erlaubt.includes(deckId);
}

// 22.08.2026 Auto-Freischaltung fuer im Rollen-Paket enthaltene Decks: anders als
// deckErlaubt() (die bei UNBEKANNTER Rolle grosszuegig fail-open ist, nur fuer die
// Kachel-Sichtbarkeit gedacht) greift diese Funktion NUR, wenn eine echte, bekannte
// Rolle vorliegt UND das Deck laut ROLLEN_DECKS Teil des gekauften Pakets ist. Nur
// dann entfaellt die zusaetzliche Einzeldeck-Passwortabfrage - eine unbekannte/fehlende
// Rolle schaltet dagegen NICHTS automatisch frei, das bestehende Passwort-System bleibt
// fuer alle anderen Faelle unveraendert bestehen (z.B. Einzelkauf zusaetzlicher Decks).
function deckAutoFreigeschaltet(deckId) {
  const rolle = sessionStorage.getItem('klartext_role') || '';
  if (!rolle) return false;
  if (!(rolle in ROLLEN_DECKS)) return false;
  const erlaubt = ROLLEN_DECKS[rolle];
  return erlaubt === null || erlaubt.includes(deckId);
}

function deckSperrHinweisZeigen() {
  const alt = document.getElementById('deck-sperr-popup');
  if (alt) alt.remove();
  const pop = document.createElement('div');
  pop.id = 'deck-sperr-popup';
  pop.setAttribute('role', 'alert');
  pop.style.cssText = 'position:fixed;left:50%;bottom:28px;transform:translateX(-50%);background:#1B3A4B;color:#fff;padding:.85rem 1.3rem;border-radius:12px;font-size:.85rem;font-weight:600;box-shadow:0 8px 24px rgba(0,0,0,.3);border:1px solid rgba(110,198,160,.4);z-index:9999;max-width:90vw;text-align:center;opacity:0;transition:opacity .25s;';
  pop.textContent = '🔒 Dieses Kartendeck ist in deinem Paket nicht enthalten.';
  document.body.appendChild(pop);
  requestAnimationFrame(() => { pop.style.opacity = '1'; });
  setTimeout(() => { pop.style.opacity = '0'; }, 2600);
  setTimeout(() => { pop.remove(); }, 3000);
}

function deckKachelnRollenFiltern() {
  document.querySelectorAll('.decktile[data-deck-id]').forEach(function(tile) {
    const id = tile.getAttribute('data-deck-id');
    tile.style.display = deckErlaubt(id) ? '' : 'none';
  });
}

async function loadDecks() {
  const res = await fetch('data/decks.json');
  const decks = await res.json();
  allDecks = decks;
  deckCategories.innerHTML = '';

  KATEGORIE_ORDER.forEach(katId => {
    const inKat = decks.filter(d => d.kategorie === katId);
    if (!inKat.length) return;
    const kat = KATEGORIEN[katId];

    const block = document.createElement('section');
    block.className = 'katblock';
    block.innerHTML = `
      <h2 class="kattitel">${kat.titel}</h2>
      <p class="katsub">${kat.sub}</p>
    `;
    const grid = document.createElement('div');
    grid.className = 'deckgrid';

    inKat.forEach(d => {
      const btn = document.createElement('button');
      btn.className = 'decktile';
      btn.setAttribute('data-deck-id', d.id);
      btn.innerHTML = `
        <div class="dt-kopf" style="background:${d.farbe};">
          <span class="dt-code">${d.code}</span>
          <span class="dt-count">${d.anzahl} Karten</span>
        </div>
        <div class="dt-body">
          <div class="dt-titel">${d.titel}</div>
          <div class="dt-sub">${d.untertitel}</div>
        </div>
      `;
      btn.addEventListener('click', () => openDeck(d.id));
      grid.appendChild(btn);
    });

    block.appendChild(grid);
    deckCategories.appendChild(block);
  });
}

async function openDeck(deckId, opts = {}) {
  const { pushState = true, karteNr = null } = opts;

  if (!deckErlaubt(deckId)) {
    deckSperrHinweisZeigen();
    if (!pushState) closeDeck({ pushState: true });
    return;
  }

  if (!isUnlocked(deckId) && !deckAutoFreigeschaltet(deckId)) {
    const meta = allDecks.find(d => d.id === deckId);
    const ok = await askForPassword(deckId, meta ? meta.titel : 'dieses Deck');
    if (!ok) {
      // Abgebrochen: bei Deep-Link (?deck=...) URL bereinigen, sonst einfach auf der
      // Übersicht bleiben (Klick auf eine Kachel hat noch keine URL geändert).
      if (!pushState) closeDeck({ pushState: true });
      return;
    }
  }

  let res;
  try {
    res = await fetch(`data/${deckId}.json`);
    if (!res.ok) throw new Error('not found');
  } catch (e) {
    return; // unbekannte/veraltete Deck-ID im Link – still zurück zur Übersicht
  }
  currentDeck = await res.json();

  document.documentElement.style.setProperty('--deck-color', currentDeck.farbe);
  document.documentElement.style.setProperty('--deck-light', currentDeck.farbe_hell);
  document.documentElement.style.setProperty('--deck-border', currentDeck.farbe_rand);

  // Deep-Link auf eine bestimmte Karte (z.B. aus der Skill-Matrix: ?deck=jd&karte=5) hat
  // Vorrang vor der zuletzt gesehenen Karte – wer gezielt verlinkt wird, soll auch genau
  // diese Karte sehen, nicht die vom letzten Besuch.
  let startIndex = null;
  if (karteNr !== null) {
    const treffer = currentDeck.karten.findIndex(k => k.nr === karteNr);
    if (treffer !== -1) startIndex = treffer;
  }
  if (startIndex === null) {
    const saved = parseInt(localStorage.getItem(lastIndexKey(deckId)), 10);
    startIndex = (!isNaN(saved) && saved >= 0 && saved < currentDeck.karten.length) ? saved : 0;
  }
  currentIndex = startIndex;

  screenDecks.hidden = true;
  screenCards.hidden = false;
  backBtn.hidden = false;
  renderCard();
  window.scrollTo(0, 0);
  setAppIdentity(currentDeck);
  if (pushState) {
    const url = karteNr !== null ? `?deck=${deckId}&karte=${karteNr}` : `?deck=${deckId}`;
    history.pushState({ deck: deckId, karte: karteNr }, '', url);
  }
}

function closeDeck(opts = {}) {
  const { pushState = true } = opts;
  currentDeck = null;
  screenCards.hidden = true;
  screenDecks.hidden = false;
  backBtn.hidden = true;
  progressEl.textContent = '';
  window.scrollTo(0, 0);
  setAppIdentity(null);
  if (pushState) history.pushState({}, '', './');
}

function renderCard() {
  if (!currentDeck) return;
  const karte = currentDeck.karten[currentIndex];
  flashcard.classList.remove('flipped');

  // Zusatzblock-Karten (z.B. EL-AT, LK-R-PF) tragen ihr eigenes Badge aus der Quelldatei -
  // das zeigt gleich an, dass es sich um einen Zusatzblock handelt, nicht nur die Kartennummer.
  cardBadge.textContent = karte.badge
    ? `${karte.badge} · ${String(karte.nr).padStart(2, '0')}/${currentDeck.karten.length}`
    : `${currentDeck.titel.toUpperCase()} · ${String(karte.nr).padStart(2, '0')}/${currentDeck.karten.length}`;
  cardTitelFront.textContent = karte.titel;
  cardTitelBack.textContent = karte.titel;

  // Kartenvorderseite: Foto (Standard-Impulskarten, TK-Deck) ODER Icon (Krisendeck/Werkzeug/mb,
  // die kein eigenes Foto haben, sondern ein Font-Awesome-Symbol als Erkennungszeichen).
  if (karte.icon) {
    frontImgWrap.hidden = true;
    frontIconWrap.hidden = false;
    frontIcon.className = `fa-solid fa-${karte.icon}`;
  } else {
    frontIconWrap.hidden = true;
    frontImgWrap.hidden = false;
    cardImg.src = karte.bild;
    cardImg.alt = karte.titel;
  }

  // Kartenrückseite: zwei grundverschiedene Inhaltsformen. Standard-Impulskarten haben
  // "fragen" (Anleitung + offene Fragen zum Reflektieren). Handlungskarten (TK-Deck,
  // Krisendeck, Werkzeugkarten, Mobbing-Materialien) haben stattdessen "schritte"
  // (konkrete Handlungsanleitung) und optional eine Tun/Nicht-tun-Tabelle.
  const istHandlungskarte = Array.isArray(karte.schritte);

  if (istHandlungskarte) {
    impulsBack.hidden = true;
    handlungBack.hidden = false;

    if (karte.situation) {
      introWrap.hidden = false;
      introLabel.textContent = karte.intro_label || 'SITUATION';
      cardIntro.textContent = karte.situation;
    } else {
      introWrap.hidden = true;
    }

    schritteLabel.textContent = karte.schritte_label || 'SCHRITTE';
    cardSchritte.innerHTML = '';
    karte.schritte.forEach(s => {
      const li = document.createElement('li');
      li.textContent = s;
      cardSchritte.appendChild(li);
    });

    if (karte.abgrenzung && (karte.abgrenzung.tun || karte.abgrenzung.nicht_tun)) {
      abgrenzungWrap.hidden = false;
      const tun = karte.abgrenzung.tun || [];
      const nicht = karte.abgrenzung.nicht_tun || [];
      const rows = Math.max(tun.length, nicht.length);
      let html = '<tr><th class="th-tun">TUN</th><th class="th-nicht">NICHT TUN</th></tr>';
      for (let i = 0; i < rows; i++) {
        html += `<tr><td class="td-tun">${tun[i] || ''}</td><td class="td-nicht">${nicht[i] || ''}</td></tr>`;
      }
      cardAbgrenzung.innerHTML = html;
    } else {
      abgrenzungWrap.hidden = true;
    }

    const notiz = karte.tipp || karte.merksatz || karte.verweis || karte.nutzen || karte.quelle;
    if (notiz) {
      notizWrap.hidden = false;
      notizLabel.textContent = karte.tipp ? 'TIPP FÜR DICH' : karte.merksatz ? 'MERKSATZ' : karte.verweis ? 'HINWEIS' : karte.nutzen ? 'NUTZEN' : 'QUELLE';
      cardNotiz.textContent = notiz;
    } else {
      notizWrap.hidden = true;
    }
  } else {
    handlungBack.hidden = true;
    impulsBack.hidden = false;

    cardAnleitung.textContent = karte.anleitung;

    cardFragen.innerHTML = '';
    (karte.fragen || []).forEach(f => {
      const box = document.createElement('div');
      box.className = 'frage-box';
      box.textContent = f;
      cardFragen.appendChild(box);
    });

    if (karte.systemfrage) {
      systemfrageWrap.hidden = false;
      systemfrageLabel.textContent = karte.systemfrage_label || 'SYSTEMISCH GEDACHT';
      cardSystemfrage.textContent = karte.systemfrage;
    } else {
      systemfrageWrap.hidden = true;
    }

    if (karte.hinweis) {
      hinweisWrap.hidden = false;
      cardHinweis.textContent = karte.hinweis;
    } else {
      hinweisWrap.hidden = true;
    }
  }

  progressEl.textContent = `${karte.nr}/${currentDeck.karten.length}`;
  localStorage.setItem(lastIndexKey(currentDeck.id), String(currentIndex));
}

function flip() {
  flashcard.classList.toggle('flipped');
}

function goNext() {
  if (!currentDeck) return;
  currentIndex = (currentIndex + 1) % currentDeck.karten.length;
  renderCard();
}

function goPrev() {
  if (!currentDeck) return;
  currentIndex = (currentIndex - 1 + currentDeck.karten.length) % currentDeck.karten.length;
  renderCard();
}

function goRandom() {
  if (!currentDeck || currentDeck.karten.length < 2) return;
  let next;
  do { next = Math.floor(Math.random() * currentDeck.karten.length); } while (next === currentIndex);
  currentIndex = next;
  renderCard();
}

flashcard.addEventListener('click', flip);
flashcard.addEventListener('keydown', (e) => {
  if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); flip(); }
});
prevBtn.addEventListener('click', (e) => { e.stopPropagation(); goPrev(); });
nextBtn.addEventListener('click', (e) => { e.stopPropagation(); goNext(); });
shuffleBtn.addEventListener('click', (e) => { e.stopPropagation(); goRandom(); });
backBtn.addEventListener('click', closeDeck);

// Einfaches Swipe-Gestensteuerung
let touchStartX = null;
flashcard.addEventListener('touchstart', (e) => { touchStartX = e.touches[0].clientX; }, { passive: true });
flashcard.addEventListener('touchend', (e) => {
  if (touchStartX === null) return;
  const dx = e.changedTouches[0].clientX - touchStartX;
  if (Math.abs(dx) > 50) {
    dx < 0 ? goNext() : goPrev();
  }
  touchStartX = null;
}, { passive: true });

// Tastatur (Desktop-Test)
document.addEventListener('keydown', (e) => {
  if (screenCards.hidden) return;
  if (e.key === 'ArrowRight') goNext();
  if (e.key === 'ArrowLeft') goPrev();
  if (e.key === ' ') { e.preventDefault(); flip(); }
});

// Rollen-Filter bei jedem Seitenaufruf neu anwenden - auch wenn die Seite aus
// dem Browser-Cache (bfcache) wiederhergestellt wird, wofuer 'load'/
// 'DOMContentLoaded' NICHT erneut feuern, 'pageshow' aber schon.
window.addEventListener('pageshow', function() {
  deckKachelnRollenFiltern();
  if (currentDeck && !deckErlaubt(currentDeck.id)) {
    closeDeck({ pushState: false });
  }
});

// Zurück/Vor-Buttons des Browsers respektieren (falls genutzt), ohne neuen History-Eintrag
window.addEventListener('popstate', () => {
  const params = new URLSearchParams(location.search);
  const deckId = params.get('deck');
  const karteParam = params.get('karte');
  const karteNr = karteParam !== null ? parseInt(karteParam, 10) : null;
  if (deckId) openDeck(deckId, { pushState: false, karteNr: (karteNr !== null && !isNaN(karteNr)) ? karteNr : null });
  else closeDeck({ pushState: false });
});

// Deep-Link beim Start: ?deck=<id> öffnet direkt dieses Deck (z.B. eigenes Home-Bildschirm-Icon pro Deck).
// Zusätzlich &karte=<nr> springt direkt zu einer bestimmten Karte (z.B. Verweis aus der Skill-Matrix
// auf JD-05: pwa/index.html?deck=jd&karte=5), statt dass man sich durchs ganze Deck klicken muss.
Promise.all([loadDecks(), loadAccess()]).then(() => {
  deckKachelnRollenFiltern();
  const params = new URLSearchParams(location.search);
  const deckId = params.get('deck');
  const karteParam = params.get('karte');
  const karteNr = karteParam !== null ? parseInt(karteParam, 10) : null;
  if (deckId) openDeck(deckId, { pushState: false, karteNr: (karteNr !== null && !isNaN(karteNr)) ? karteNr : null });
});

if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('service-worker.js').catch(() => {});
  });
}
