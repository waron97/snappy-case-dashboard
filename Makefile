.PHONY: reset-base

SOURCE ?= test-01

# Re-restore SOURCE's base DB from its current dump-<source>/ directory, in-process,
# via base_db.reset_source() — the same code path the web UI's "Reset base" button
# calls, so the CLI and the API can't drift. Use after swapping a dump.
# Usage: make reset-base [SOURCE=test-01|test-02]
reset-base:
	docker compose exec -T testrunner-control python3 /opt/base_db.py reset $(SOURCE)
	@echo ">>> $(SOURCE) base reset from dump-$(SOURCE)/. Tail: docker compose logs -f testrunner-control"
