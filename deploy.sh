#!/usr/bin/env bash
set -euo pipefail

REMOTE=arpeggio
REMOTE_DIR=/app/snappy-case-dashboard

rsync -avz --progress \
  --exclude='web-app/node_modules' \
  --exclude='web-app/.next' \
  --exclude='web-app/.yarn/cache' \
  --exclude='web-app/.env' \
  --exclude='.env' \
  --exclude='.env.*' \
  --exclude='web-app/.env.*' \
  --exclude='web-app/coverage' \
  --exclude='web-app/storybook-static' \
  --exclude='.git' \
  . "$REMOTE:$REMOTE_DIR"

ssh "$REMOTE" "cd /app/snappy-case-dashboard && \
    docker compose -p snappy-case-dashboard down && \
    docker compose -p snappy-case-dashboard-test-01 -f docker-compose.test-01.yml down && \
    docker compose -p snappy-case-dashboard up -d --build && \
    docker compose -p snappy-case-dashboard-test-01 -f docker-compose.test-01.yml --env-file .env.test-01 up -d --build"
