.PHONY: release patch minor major

# Cut a release:  make release patch | make release minor | make release major
#
# Bumps desktop-app's version, commits "(ver) bump", tags v<version> and pushes.
# The tag push triggers .github/workflows/release.yml, which publishes a public
# GitHub Release — see scripts/release.sh for the guards around that.
release:
	@scripts/release.sh $(filter-out release,$(MAKECMDGOALS))

# The bump level is written as a goal (`make release patch`) rather than a
# variable, so make would otherwise try to build it as a target. Absorb it.
patch minor major:
	@:
