#!/usr/bin/env bash
# Sammelt die Befunde aller Agenten ein und zeigt nur, was seit dem letzten
# Einsammeln dazugekommen ist. Macht keine Bewertung — das ist Alfreds Teil.
#
#   bin/lernen-sammeln.sh            zeigt das Neue
#   bin/lernen-sammeln.sh --quittieren   markiert das Gezeigte als eingesammelt
#
# Der Stand liegt in lernen/.gelesen/<schluessel>.md — eine Kopie dessen, was
# beim letzten Mal verarbeitet wurde. Diff dagegen ueberlebt auch einen
# force-push oder ein Umschreiben auf dem Agenten-Branch.
set -uo pipefail
cd "$(dirname "$0")/.."

declare -A ZWEIG=(
  [content-schlicht]=claude/content-assistant
  [content-cinematic]=claude/content-cinematic
  [content-shorts-2]=claude/content-shorts-2
  [content-vlog]=claude/content-vlog
  [content-gastauftritte]=claude/content-gastauftritte
  [thumbnails]=claude/thumbnails
  [head-of-content]=claude/head-of-content
  [youtube-manager]=claude/youtube-manager
  [guest-booking]=claude/guest-booking
)

QUITTIEREN=0
[ "${1:-}" = "--quittieren" ] && QUITTIEREN=1

mkdir -p lernen/.gelesen lernen/.frisch
NEUES=0

for K in "${!ZWEIG[@]}"; do
  Z="${ZWEIG[$K]}"
  if ! git fetch -q origin "$Z" 2>/dev/null; then
    echo "### $K — Zweig $Z nicht erreichbar"; echo
    continue
  fi
  SPITZE=$(git rev-parse --short "origin/$Z")
  COMMITS=$(git rev-list --count "origin/claude/ai-chief-of-staff-cz83jv..origin/$Z" 2>/dev/null || echo 0)

  if git cat-file -e "origin/$Z:lernen/$K.md" 2>/dev/null; then
    git show "origin/$Z:lernen/$K.md" > "lernen/.frisch/$K.md"
  else
    : > "lernen/.frisch/$K.md"
  fi

  ALT="lernen/.gelesen/$K.md"; [ -f "$ALT" ] || : > "$ALT"
  DIFF=$(diff --unchanged-line-format= --old-line-format= --new-line-format='%L' \
           "$ALT" "lernen/.frisch/$K.md" 2>/dev/null | sed '/^[[:space:]]*$/d')

  if [ -n "$DIFF" ]; then
    NEUES=1
    echo "### $K  ($Z @ $SPITZE, $COMMITS eigene Commits)"
    echo "$DIFF"
    echo
  elif [ "$COMMITS" != "0" ]; then
    echo "### $K  ($Z @ $SPITZE, $COMMITS eigene Commits) — gearbeitet, aber nichts in den Kanal geschrieben"
    git log --oneline "origin/claude/ai-chief-of-staff-cz83jv..origin/$Z" | sed 's/^/    /'
    echo
  fi

  [ "$QUITTIEREN" = "1" ] && cp "lernen/.frisch/$K.md" "$ALT"
done

[ "$NEUES" = "0" ] && echo "Nichts Neues im Kanal."
exit 0
