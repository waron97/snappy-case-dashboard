.PHONY: reset-base

# Drop the test-01 base DB + all pool/per-run copies and clear the pool bookkeeping,
# then restart the control plane so it re-restores from the CURRENT dump-test-01/ and
# rewarms the pool. Use after swapping the dump.
reset-base:
	docker compose stop testrunner-control testrunner-worker
	# Kill any orphan template-copy backends still holding the base, else DROP blocks.
	-docker compose exec -T postgres psql -U odoo -d odoo_base -tAc \
	  "SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE query LIKE 'CREATE DATABASE %TEMPLATE sorgenia_test_01_base%' AND state='active'"
	docker compose exec -T postgres psql -U odoo -d odoo_base -tAc \
	  "SELECT 'DROP DATABASE IF EXISTS \"'||datname||'\" WITH (FORCE);' FROM pg_database WHERE (datname='sorgenia_test_01_base' OR datname LIKE 'init\_%%' OR datname LIKE 'odoo\_%%') AND datname<>'odoo_base'" \
	  | docker compose exec -T postgres psql -U odoo -d odoo_base
	-docker compose exec -T redis redis-cli del test:pool:ready test:pool:building
	docker compose up -d testrunner-control testrunner-worker
	@echo ">>> Base dropped. Control is re-restoring from dump-test-01/ and will rewarm the pool."
