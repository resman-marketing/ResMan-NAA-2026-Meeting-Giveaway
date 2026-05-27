#!/usr/bin/env bash
# Rebuild index.html from src/ and publish to GitHub Pages.
# Usage: ./deploy.sh "optional commit message"
set -euo pipefail
cd "$(dirname "$0")"

GH="${GH_BIN:-$HOME/bin/gh}"   # gh isn't on the default PATH on this machine

echo "› Building index.html from src/build.py ..."
python3 src/build.py

if git diff --quiet -- index.html; then
  echo "› No changes in index.html — nothing to deploy."
  exit 0
fi

MSG="${1:-Update field guide}"
echo "› Committing: $MSG"
git add index.html src
git -c user.email="earllacey13@gmail.com" -c user.name="ResMan Marketing" commit -m "$MSG"

echo "› Pushing to GitHub ..."
git push

echo ""
echo "✓ Deployed. Pages will refresh in ~1 minute:"
echo "  https://resman-marketing.github.io/ResMan-NAA-2026-Meeting-Giveaway/"
