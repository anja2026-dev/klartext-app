#!/bin/bash
# build_shop_package.sh
# Baut eine Supabase-freie Kopie von klartext-app für den Shop-Verkauf (Strang 38/44).
# Kopiert das komplette Repo in ein Zielverzeichnis, OHNE die in
# SHOP_PACKAGE_AUSSCHLUSSLISTE.md dokumentierten Supabase-/Firebase-abhängigen Dateien
# und internen Planungsdokumente. Das Haupt-Repo bleibt dabei unverändert (nur Lesezugriff).
#
# Nutzung:
#   ./build_shop_package.sh /pfad/zum/zielordner        # echte Kopie
#   ./build_shop_package.sh /pfad/zum/zielordner --dry-run   # nur anzeigen, nichts kopieren
#
# Voraussetzung: rsync (auf macOS vorinstalliert).

set -euo pipefail

QUELLE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ZIEL="${1:-}"
DRYRUN="${2:-}"

if [ -z "$ZIEL" ]; then
  echo "Fehler: Zielordner fehlt."
  echo "Nutzung: $0 /pfad/zum/zielordner [--dry-run]"
  exit 1
fi

RSYNC_FLAGS=(-av)
if [ "$DRYRUN" = "--dry-run" ]; then
  RSYNC_FLAGS+=(--dry-run)
  echo ">>> DRY RUN — es wird nichts kopiert, nur angezeigt."
fi

mkdir -p "$ZIEL"

rsync "${RSYNC_FLAGS[@]}" \
  --exclude ".git/" \
  --exclude "supabase/" \
  --exclude "__pycache__/" \
  --exclude "storybooks/" \
  --exclude "BAROMETER_KIND.html" \
  --exclude "CHAT_List.html" \
  --exclude "CHAT_New.html" \
  --exclude "CHAT_View.html" \
  --exclude "DASHBOARD.html" \
  --exclude "DASHBOARD_mobile.html" \
  --exclude "Kinderverwaltung.html" \
  --exclude "KLARTEXT_Feedback_INGRA.html" \
  --exclude "KLARTEXT_Feedback_TK.html" \
  --exclude "KLARTEXT_Forward_Read.html" \
  --exclude "KLARTEXT_Krankmeldung.html" \
  --exclude "KLARTEXT_Listen.html" \
  --exclude "KLARTEXT_Login.html" \
  --exclude "KLARTEXT_Logout.html" \
  --exclude "KLARTEXT_Notizblock.html" \
  --exclude "KLARTEXT_Portale.html" \
  --exclude "KLARTEXT_Setup_Demo_Kinder.html" \
  --exclude "KLARTEXT_Tagesjournal.html" \
  --exclude "KLARTEXT_Teilnehmer_Protokoll.html" \
  --exclude "KLARTEXT_TK_Inbox.html" \
  --exclude "KLARTEXT_UnserBuch.html" \
  --exclude "KLARTEXT_Urlaubsantrag_INGRA.html" \
  --exclude "KLARTEXT_Weiterleiten.html" \
  --exclude "KLARTEXT_Weiterleitungen.html" \
  --exclude "KLARTEXT_Zeitkonto.html" \
  --exclude "TK_Fallmanagement.html" \
  --exclude "TK_Kinderzuordnung.html" \
  --exclude "TK_Landing.html" \
  --exclude "TK_Uebergaben.html" \
  --exclude "TK_Vertretungsassistent.html" \
  --exclude "feedback.html" \
  --exclude "feedbackAdmin.html" \
  --exclude "Admin_Backend.html" \
  --exclude "KLARTEXT_Vertretungsassistent_Architektur.html" \
  --exclude "SHOP_PACKAGE_AUSSCHLUSSLISTE.md" \
  --exclude "build_shop_package.sh" \
  --exclude "KLARTEXT_Merkliste.md" \
  "$QUELLE/" "$ZIEL/"

if [ "$DRYRUN" != "--dry-run" ]; then
  echo ""
  echo ">>> Fertig. Rest-Check auf Supabase/Firebase-Reste im Zielordner:"
  if grep -rlEq "supabase\.(from|auth|storage|channel|createClient)|firebase\.(initializeApp|auth|database)|createClient\(" "$ZIEL" --include="*.html" 2>/dev/null; then
    echo "!!! WARNUNG: es gibt noch Treffer — bitte prüfen:"
    grep -rlE "supabase\.(from|auth|storage|channel|createClient)|firebase\.(initializeApp|auth|database)|createClient\(" "$ZIEL" --include="*.html" 2>/dev/null
  else
    echo "OK — keine funktionalen Supabase/Firebase-Aufrufe mehr gefunden."
  fi
fi
