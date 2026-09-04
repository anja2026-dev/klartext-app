// KLARTEXT-Mentoring Karten – Service Worker
// Cache-Version erhöhen (v1 -> v2 ...), wenn App-Shell-Dateien sich ändern.
const SHELL_CACHE = 'klartext-shell-v16';
const RUNTIME_CACHE = 'klartext-runtime-v1';

const SHELL_FILES = [
  './index.html',
  './style.css',
  './app.js',
  './manifest.json',
  './icons/icon-192.png',
  './icons/icon-512.png',
  './data/decks.json'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(SHELL_CACHE).then((cache) => cache.addAll(SHELL_FILES)).then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(
        keys
          .filter((k) => k !== SHELL_CACHE && k !== RUNTIME_CACHE)
          .map((k) => caches.delete(k))
      )
    ).then(() => self.clients.claim())
  );
});

// App-Shell: cache-first. Deck-Daten/Bilder (data/, images/): cache-first mit
// Hintergrund-Update, damit einmal geöffnete Decks offline nutzbar bleiben.
self.addEventListener('fetch', (event) => {
  const url = new URL(event.request.url);
  if (event.request.method !== 'GET' || url.origin !== self.location.origin) return;

  const isRuntimeAsset = url.pathname.includes('/data/') || url.pathname.includes('/images/')
    || url.pathname.includes('/icons/deck-');
  const cacheName = isRuntimeAsset ? RUNTIME_CACHE : SHELL_CACHE;

  event.respondWith(
    caches.open(cacheName).then((cache) =>
      cache.match(event.request).then((cached) => {
        const network = fetch(event.request)
          .then(async (response) => {
            // Safari verweigert Navigations-Antworten, die vom Service Worker
            // stammen und "redirected" sind (z.B. wenn Cloudflare Pages /pwa
            // intern auf /pwa/ umleitet) - Fehler "Response served by service
            // worker has redirections". Fix: Body in eine neue, nicht als
            // redirected markierte Response verpacken, bevor sie gecacht/
            // zurückgegeben wird.
            let safeResponse = response;
            if (response && response.redirected) {
              const body = await response.clone().blob();
              // Content-Encoding/-Length nicht uebernehmen: der Blob ist
              // bereits entpackt, mit den Original-Headern wuerde der
              // Browser eine (nicht mehr vorhandene) Kompression erwarten
              // und die Antwort mit ERR_FAILED verwerfen.
              const safeHeaders = new Headers();
              response.headers.forEach((value, key) => {
                const k = key.toLowerCase();
                if (k === 'content-encoding' || k === 'content-length' || k === 'transfer-encoding') return;
                safeHeaders.append(key, value);
              });
              safeResponse = new Response(body, {
                status: response.status,
                statusText: response.statusText,
                headers: safeHeaders
              });
            }
            if (safeResponse && safeResponse.status === 200) cache.put(event.request, safeResponse.clone());
            return safeResponse;
          })
          .catch(() => cached);
        return cached || network;
      })
    )
  );
});
