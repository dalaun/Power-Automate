#!/bin/bash
# Sync docs/wiki/ files to GitHub wiki repository
#
# Usage: ./sync-wiki.sh
#
# This script:
# 1. Clones the wiki repository (if not already cloned)
# 2. Copies updated files from docs/wiki/ to the wiki repo
# 3. Commits and pushes to the wiki

set -e

WIKI_REPO="https://github.com/dalaun/Finch-Dagen-Foundation.wiki.git"
WIKI_DIR="../Finch-Dagen-Foundation.wiki"
DOCS_WIKI_DIR="./docs/wiki"

echo "═══════════════════════════════════════════════════════════════"
echo "Syncing docs/wiki/ to GitHub wiki repository"
echo "═══════════════════════════════════════════════════════════════"

# Check if wiki repo exists
if [ ! -d "$WIKI_DIR" ]; then
    echo "→ Cloning wiki repository..."
    cd ..
    git clone "$WIKI_REPO"
    cd Power-Automate
else
    echo "→ Wiki repository already cloned"
    cd "$WIKI_DIR"
    git pull origin master
    cd -
fi

# Copy files from docs/wiki/ to wiki repo
echo "→ Copying updated files..."
cp -v "$DOCS_WIKI_DIR"/*.md "$WIKI_DIR/"

# Commit and push
cd "$WIKI_DIR"
git add .
if git diff --cached --quiet; then
    echo "✓ No changes to commit"
else
    echo "→ Committing changes..."
    git commit -m "Update wiki documentation from main repository

Synced from docs/wiki/ in main repository
Latest commit: $(cd ../Power-Automate && git rev-parse --short HEAD)"

    echo "→ Pushing to wiki repository..."
    git push origin master
    echo "✓ Wiki updated successfully!"
fi

cd ../Power-Automate
echo "═══════════════════════════════════════════════════════════════"
echo "Done!"
echo "═══════════════════════════════════════════════════════════════"
