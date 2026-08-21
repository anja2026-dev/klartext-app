# Übergabe-Prompt für neuen Chat

Kontext: KLARTEXT-Mentoring-System (Anja Jolk)

Zwei Repos sind relevant: `klartext-app` (die App selbst) und `klartext-shop` (Verkaufsseiten/Landing Pages). Bitte fordere zuerst Ordnerfreigabe für beide an, damit Anja dich freischalten kann.

## Etablierte Arbeitsweise (bitte durchgehend einhalten)

- Vor jedem Bauen: Fakten (Preise, Tool-Namen, Modulzahlen, Qualifikationen, URLs) gegen echte Dateien oder Anjas eigene Aussagen prüfen, Korrekturen offen ansprechen statt sie stillschweigend zu übernehmen.
- Bei echten Architektur-/Scope-Entscheidungen die AskUserQuestion-Funktion nutzen statt zu raten.
- Testen: jsdom für App-Seiten (HTML/JS-Logik), pypdf/weasyprint bzw. docx-Skill für PDF/Word-Dokumente.
- Git-Commits nur mit den tatsächlich bearbeiteten Dateien stagen (`git add <Datei1> <Datei2> ...`), niemals pauschal mit `git add -A` — im Repo liegen viele unabhängige, nicht committete Änderungen (.DS_Store, __pycache__, KLARTEXT_Plattform_Preisstrategie.md, tools/, diverse PDFs), die nichts mit der aktuellen Aufgabe zu tun haben und unangetastet bleiben müssen.
- Ausführliche deutsche Commit-Messages.
- Nach jeder abgeschlossenen Arbeitseinheit einen neuen nummerierten "Strang"-Eintrag in `klartext-app/KLARTEXT_Merkliste.md` schreiben (Fact-Checks, Korrekturen, was gebaut/getestet wurde, was noch offen ist) und die Kopfzeile "Stand: ... (Strang X ergänzt)" aktualisieren.
- Am Ende Push-Hinweis geben — du (Claude) kannst nicht selbst pushen, das muss Anja manuell machen.
- Anjas Präferenzen: knapp/direkt kommunizieren; bei Fakten wissenschaftliche Originalquellen und Zitate nutzen.

## Was heute gemacht wurde (Stränge 73–76, alle committet, noch nicht gepusht — 4 Commits warten)

1. Zwei Honorar-Flyer für Familienzentren/Migrationszentren (Kleingewerbe-Angebote: Struktur-Coaching vor Ort, Emotionale Stabilisierung, Ausfüllhilfe & Strukturgeberin — keine Rechtsberatung).
2. Neue App-Seite `KLARTEXT_Antraege_Links.html` mit recherchierten offiziellen Antrags-Links (BuT, SGB IX, Pflegekasse) für Dortmund/Schwerte/Unna/Hagen.
3. `KLARTEXT_Ressourcenbericht_Jobcoach.html` komplett neu gebaut (4 Fachbereich-Varianten: Struktur & Familie, Neurodivergenz, Sprache & Integration, Admin-Support) — auf ausdrücklichen Wunsch von Anja komplett ohne Supabase, rein lokal (localStorage), mit Teilnehmer-ID-Verwaltung, Barometer-Verlauf und einer "Bericht zusammenfassen & per E-Mail versenden"-Funktion. Wichtig: `BAROMETER_KIND.html` bleibt bewusst unverändert auf Supabase (dort ist geräteübergreifender Verlauf gewünscht) — das war eine bewusste, mit Anja abgestimmte Scope-Entscheidung.
4. Word/PDF-Dokument `Anja_Jolk_Leistungsuebersicht_Pflegedienste.docx/.pdf` für Kooperation mit ambulanten Pflegediensten (Preise 40/45/55 €/h, mit Korrekturen: MDK→MD, echte Tool-Namen Barometer/Insel-Set, "keine Rechtsberatung"-Hinweis, Pflegekassen-Anträge zurückhaltender formuliert).

Details zu allen Fact-Checks und offenen Punkten stehen in `klartext-app/KLARTEXT_Merkliste.md`, Stränge 73–76.

## Nächste Aufgabe: Landing-Page überarbeiten

Anja möchte als Nächstes eine Landing-Page überarbeiten lassen. Es gibt mehrere Kandidaten im Repo — unklar, welche gemeint ist:

- `klartext-app/KLARTEXT_Landing.html`
- `klartext-app/TK_Landing.html`
- `klartext-shop/KLARTEXT_Verkaufsseite.html`
- ggf. eine der produktspezifischen `*_Verkaufsseite.html`-Seiten in `klartext-shop`

Bitte zuerst bei Anja nachfragen, welche konkrete Seite gemeint ist und was genau überarbeitet werden soll (Inhalt, Design, Struktur, Zielgruppe), bevor mit der Arbeit begonnen wird.
