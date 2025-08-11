#!/bin/bash

# Exit on error
set -e

# Determine bump type (major/minor/patch)
BUMP_TYPE=${1:-patch}

# Bump version using poetry
poetry version $BUMP_TYPE
NEW_VERSION=$(poetry version -s)
echo "Version bumped to: $NEW_VERSION"

# Update package init version
INIT_FILE="fantasy_langgen/__init__.py"
# BSD sed - macOS
sed -i '' "s/^__version__ = .*/__version__ = \"${NEW_VERSION}\"/" "$INIT_FILE"
# # GNU sed - Linux
# sed -i "s/^__version__ = .*/__version__ = \"${NEW_VERSION}\"/" "$INIT_FILE"
rm -f "${INIT_FILE}.bak"
echo "Updated package init version"

# Commit version change
git add pyproject.toml
git commit -m "Bump version to ${NEW_VERSION}"

# Push the version bump
git push

# For minor or major bumps, ask about release
if [[ "$BUMP_TYPE" == "minor" ]] || [[ "$BUMP_TYPE" == "major" ]]; then
    read -p "Create release for v${NEW_VERSION}? [y/N] " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        ./scripts/release.sh
    fi
fi