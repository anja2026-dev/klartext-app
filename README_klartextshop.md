# klartext-shop

Marketing- und Verkaufsseiten für die KLARTEXT-Kartenset-Serie (z. B. **JD**, das Coaching-Impulskarten-Deck für Jugendliche).

Dieses Repository ist bewusst getrennt von [`klartext-app`](https://github.com/anja2026-dev/klartext-app), der Haupt-App, die aktuell in der Beta-Testphase bei einer Partnerorganisation läuft. Verkaufs-/Marketingseiten für das Kartenset-Business landen deshalb hier statt auf `main` der App, damit sie nicht versehentlich auf derselben Cloudflare-Pages-Umgebung sichtbar werden, die die Partnerorganisation gerade testet.

## Inhalt

- `JD_Verkaufsseite.html` — eigenständige, statische Verkaufsseite für das JD-Kartendeck (kein Backend, kein Login, Inline-CSS).

## Deployment

Cloudflare Pages wird für dieses Repo separat manuell im Cloudflare-Dashboard verbunden.
