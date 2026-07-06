// KLARTEXT Service Worker — Safari-kompatibel
const CACHE = 'klartext-v3';

self.addEventListener('install', e => {
  self.skipWaiting();
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys().then(namen =>
      Promise.all(namen.filter(name => name !== CACHE).map(name => caches.delete(name)))
    )
  );
  self.clients.claim();
});

// Fetch: nur direkte Requests cachen, KEINE Redirects abfangen
self.addEventListener('fetch', e => {
  // Nur GET, nur same-origin, keine Navigation-Redirects
  if (e.request.method !== 'GET') return;
  if (e.request.mode === 'navigate') {
    // Bei Navigation: immer Netzwerk bevorzugen
    e.respondWith(fetch(e.request).catch(() => caches.match(e.request)));
    return;
  }
  e.respondWith(
    caches.match(e.request).then(cached => {
      if (cached) return cached;
      return fetch(e.request).then(response => {
        // Nur 200er cachen — KEINE Redirects (301/302)
        if (response && response.status === 200 && response.type === 'basic') {
          const clone = response.clone();
          caches.open(CACHE).then(c => c.put(e.request, clone));
        }
        return response;
      });
    })
  );
});