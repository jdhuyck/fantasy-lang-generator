#!/bin/bash

# Exit on error and trace commands
set -eo pipefail
set -x

# Get current version
CURRENT_VERSION=$(poetry version -s)
TAG_NAME="v${CURRENT_VERSION}"

# Verify we're on main branch
CURRENT_BRANCH=$(git branch --show-current)
if [[ "$CURRENT_BRANCH" != "main" ]]; then
    echo "ERROR: Releases must be created from main branch (currently on $CURRENT_BRANCH)"
    exit 1
fi

# Verify clean working directory
if [[ -n $(git status --porcelain) ]]; then
    echo "ERROR: Working directory not clean - commit changes before releasing"
    exit 1
fi

# Build package
echo "Building package version ${CURRENT_VERSION}..."
poetry build

# Create git tag
echo "Creating tag ${TAG_NAME}..."
git tag -a "${TAG_NAME}" -m "Release ${TAG_NAME}"
git push origin "${TAG_NAME}"

# Create GitHub release
echo "Creating GitHub release..."
gh release create "${TAG_NAME}" \
    --title "${TAG_NAME}" \
    --notes "Release ${TAG_NAME}" \
    dist/*.whl dist/*.tar.gz

echo "Successfully released ${TAG_NAME}!"