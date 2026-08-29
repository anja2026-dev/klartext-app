# -*- coding: utf-8 -*-

def patch_file(path, replacements):
    with open(path, encoding="utf-8") as f:
        content = f.read()
    for old, new, label in replacements:
        cnt = content.count(old)
        assert cnt == 1, f"{path} / {label}: erwartet 1 Treffer, gefunden {cnt}"
        content = content.replace(old, new)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"OK: {path} aktualisiert ({len(replacements)} Ersetzung/en)")


# ---------- 1) KLARTEXT_Downloads.html ----------
patch_file(
    "KLARTEXT_Downloads.html",
    [
        (
            """    var rolle = sessionStorage.getItem('klartext_role') || '';
    if(!rolle) return; // keine Rolle bekannt -> nichts ausblenden (sicherer Default)
    document.querySelectorAll('[data-roles]').forEach(function(el){
      var erlaubt = el.getAttribute('data-roles').split(/\\s+/);
      if(erlaubt.indexOf(rolle) === -1){
        el.style.display = 'none';
      }
    });""",
            """    var rolle = sessionStorage.getItem('klartext_role') || '';
    // Fail-closed: fehlt die Rolle, werden ALLE data-roles-Elemente versteckt statt gezeigt.
    document.querySelectorAll('[data-roles]').forEach(function(el){
      if(!rolle){ el.style.display = 'none'; return; }
      var erlaubt = el.getAttribute('data-roles').split(/\\s+/);
      if(erlaubt.indexOf(rolle) === -1){
        el.style.display = 'none';
      }
    });""",
            "Fail-closed-Fix",
        )
    ],
)

# ---------- 2) KLARTEXT_Systemanleitung.html ----------
_STANDARD_OLD = """    var rolle = sessionStorage.getItem('klartext_role') || '';
    if (!rolle) return;
    document.querySelectorAll('[data-roles]').forEach(function(el){
      var erlaubt = el.getAttribute('data-roles').split(/\\s+/);
      if (erlaubt.indexOf(rolle) === -1){
        el.style.display = 'none';
      }
    });"""

_STANDARD_NEW = """    var rolle = sessionStorage.getItem('klartext_role') || '';
    // Fail-closed: fehlt die Rolle, werden ALLE data-roles-Elemente versteckt statt gezeigt.
    document.querySelectorAll('[data-roles]').forEach(function(el){
      if (!rolle) { el.style.display = 'none'; return; }
      var erlaubt = el.getAttribute('data-roles').split(/\\s+/);
      if (erlaubt.indexOf(rolle) === -1){
        el.style.display = 'none';
      }
    });"""

patch_file(
    "KLARTEXT_Systemanleitung.html",
    [(_STANDARD_OLD, _STANDARD_NEW, "Fail-closed-Fix")],
)

# ---------- 3) KLARTEXT_Workbook.html (identisches Muster) ----------
patch_file(
    "KLARTEXT_Workbook.html",
    [(_STANDARD_OLD, _STANDARD_NEW, "Fail-closed-Fix")],
)

# ---------- 4) DASHBOARD.html ----------
patch_file(
    "DASHBOARD.html",
    [
        (
            """  // OFFLINE-FIRST ROLLEN-FILTER: Elemente mit data-roles="rolle1 rolle2 ..."
  // werden ausgeblendet, wenn die aktuelle klartext_role NICHT in der Liste
  // steht. Sicherer Default: fehlt data-roles ganz, oder ist klartext_role
  // (noch) leer/nicht gesetzt, bleibt das Element sichtbar - lieber zu viel
  // zeigen als jemanden mit gueltigem Login versehentlich auszusperren.
  // ═══════════════════════════════════════
  document.addEventListener('DOMContentLoaded', function(){
    try {
      var rolle = sessionStorage.getItem('klartext_role') || '';
      if(!rolle) return; // keine Rolle bekannt -> nichts ausblenden
      document.querySelectorAll('[data-roles]').forEach(function(el){
        var erlaubt = el.getAttribute('data-roles').split(/\\s+/);
        if(erlaubt.indexOf(rolle) === -1){
          el.style.display = 'none';
        }
      });""",
            """  // OFFLINE-FIRST ROLLEN-FILTER: Elemente mit data-roles="rolle1 rolle2 ..."
  // werden ausgeblendet, wenn die aktuelle klartext_role NICHT in der Liste
  // steht. Fail-closed: fehlt data-roles ganz, bleibt das Element sichtbar
  // (kein Zugriffsschutz nötig); ist klartext_role (noch) leer/nicht gesetzt,
  // wird JEDES data-roles-Element versteckt - lieber kurz zu wenig zeigen
  // als bezahlten Rollen-Inhalt an alle ausliefern.
  // ═══════════════════════════════════════
  document.addEventListener('DOMContentLoaded', function(){
    try {
      var rolle = sessionStorage.getItem('klartext_role') || '';
      document.querySelectorAll('[data-roles]').forEach(function(el){
        if(!rolle){ el.style.display = 'none'; return; }
        var erlaubt = el.getAttribute('data-roles').split(/\\s+/);
        if(erlaubt.indexOf(rolle) === -1){
          el.style.display = 'none';
        }
      });""",
            "Fail-closed-Fix + Kommentar",
        )
    ],
)

# ---------- 5) KLARTEXT_Spiele.html ----------
patch_file(
    "KLARTEXT_Spiele.html",
    [
        (
            """// OFFLINE-FIRST ROLLEN-FILTER (gleiches Muster wie DASHBOARD.html):
// Kacheln mit data-roles="rolle1 rolle2 ..." werden ausgeblendet, wenn die
// aktuelle klartext_role nicht enthalten ist. Ohne data-roles oder ohne
// gesetzte Rolle bleibt die Kachel sichtbar (sicherer Default).
// ═══════════════════════════════════════
document.addEventListener('DOMContentLoaded', function(){
  try {
    var rolle = sessionStorage.getItem('klartext_role') || '';
    if(!rolle) return;
    document.querySelectorAll('[data-roles]').forEach(function(el){
      var erlaubt = el.getAttribute('data-roles').split(/\\s+/);
      if(erlaubt.indexOf(rolle) === -1){
        el.style.display = 'none';
      }
    });""",
            """// OFFLINE-FIRST ROLLEN-FILTER (gleiches Muster wie DASHBOARD.html):
// Kacheln mit data-roles="rolle1 rolle2 ..." werden ausgeblendet, wenn die
// aktuelle klartext_role nicht enthalten ist. Fail-closed: fehlt data-roles
// ganz, bleibt die Kachel sichtbar; fehlt die Rolle, wird JEDE Kachel mit
// data-roles versteckt.
// ═══════════════════════════════════════
document.addEventListener('DOMContentLoaded', function(){
  try {
    var rolle = sessionStorage.getItem('klartext_role') || '';
    document.querySelectorAll('[data-roles]').forEach(function(el){
      if(!rolle){ el.style.display = 'none'; return; }
      var erlaubt = el.getAttribute('data-roles').split(/\\s+/);
      if(erlaubt.indexOf(rolle) === -1){
        el.style.display = 'none';
      }
    });""",
            "Fail-closed-Fix + Kommentar",
        )
    ],
)

# ---------- 6) KLARTEXT_Glossar.html ----------
patch_file(
    "KLARTEXT_Glossar.html",
    [
        (
            """    var rolle = sessionStorage.getItem('klartext_role') || '';
    if (!rolle) return; // keine Rolle bekannt -> nichts sperren
    var erlaubt = MODUL_ZUGRIFF[modul] || [];
    if (erlaubt.indexOf(rolle) === -1){""",
            """    var rolle = sessionStorage.getItem('klartext_role') || '';
    var erlaubt = MODUL_ZUGRIFF[modul] || [];
    // Fail-closed: fehlt die Rolle, wird gesperrt statt durchgelassen.
    if (!rolle || erlaubt.indexOf(rolle) === -1){""",
            "Fail-closed-Fix",
        )
    ],
)

print("ALLE 6 DATEIEN GEPATCHT")
