#!/usr/bin/env bash
#
# Cuts a release: bumps desktop-app's version, commits it as "(ver) bump",
# tags it v<version> and pushes both.
#
# Pushing the tag is what actually ships: .github/workflows/release.yml fires
# on 'v*' and publishes a public GitHub Release. Everything before the push is
# local and undoable; the push is not. Hence the checks below.
#
# Usage: scripts/release.sh patch|minor|major

set -euo pipefail

BUMP="${1:-}"
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
APP_DIR="$REPO_ROOT/desktop-app"
RELEASE_BRANCH="master"

die() {
  echo "release: $*" >&2
  exit 1
}

case "$BUMP" in
  patch | minor | major) ;;
  "") die "missing bump level. Usage: make release patch|minor|major" ;;
  *) die "unknown bump level '$BUMP'. Expected patch, minor or major." ;;
esac

cd "$REPO_ROOT"

branch="$(git rev-parse --abbrev-ref HEAD)"
[ "$branch" = "$RELEASE_BRANCH" ] ||
  die "on branch '$branch'; releases are cut from '$RELEASE_BRANCH'."

# A dirty tree would get swept into the version commit, which is supposed to
# touch nothing but the manifests.
[ -z "$(git status --porcelain)" ] ||
  die "working tree is dirty. Commit or stash first."

# Being ahead of origin is the normal case — the whole point is to release
# commits that are still local, and the push below fast-forwards them. What
# must not happen is releasing while origin holds commits we do not: the tag
# would name a tree that never contained them, and the push would be rejected
# anyway. So require origin to be an ancestor, not an equal.
git fetch --quiet origin "$RELEASE_BRANCH"
git merge-base --is-ancestor "origin/$RELEASE_BRANCH" HEAD ||
  die "origin/$RELEASE_BRANCH has commits you don't. Pull (or rebase) first."

# --no-git-tag-version: npm would otherwise commit and tag with its own message,
# and we want "(ver) bump" plus an annotated tag to match the existing history.
# This also drags package-lock.json's stale version field along, so the two
# manifests stop disagreeing.
# tail -n1: npm prints the new "v<version>" last, but may emit notices above it.
tag="$(cd "$APP_DIR" && npm version "$BUMP" --no-git-tag-version | tail -n1)"
[[ "$tag" =~ ^v[0-9]+\.[0-9]+\.[0-9]+$ ]] ||
  die "could not read the new version from npm (got '$tag')."

git add desktop-app/package.json desktop-app/package-lock.json
git commit --quiet -m "(ver) bump"
git tag -a "$tag" -m "$tag"

echo "release: created $tag at $(git rev-parse --short HEAD)"

git push --quiet origin "$RELEASE_BRANCH"
git push --quiet origin "$tag"

echo "release: pushed. GitHub Actions is building $tag:"
echo "  https://github.com/waron97/snappy-case-dashboard/actions"
