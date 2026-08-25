#!/bin/bash
set -e

export GIT_SSH_COMMAND="ssh -i /home/odoo/.ssh/id_rsa -o StrictHostKeyChecking=no"

REPO_SSH_URL="git@ssh.dev.azure.com:v3/${DEVOPS_ORG}/${DEVOPS_PROJECT}/${DEVOPS_REPO}"

if [ "$ROLE" = "control" ]; then
    # Control plane: poller + API + warmer + base restore + the dev instance manager.
    # Both dev sources restore unconditionally (the pool warmer stays gated below —
    # that's test-01-only and only feeds the init test).
    echo "Ensuring test-01 and test-02 base DBs are restored..."
    python3 /opt/base_db.py ensure-all
else
    # Worker: needs the repo checkout, pre-commit, and its own odoo-init.conf.
    if [ ! -d "/opt/repo/.git" ]; then
        echo "Cloning repository from ${REPO_SSH_URL}..."
        git clone --branch 15.0-dev "$REPO_SSH_URL" /opt/repo
        echo "Clone complete."
    else
        echo "Repository present, fetching latest..."
        git -C /opt/repo fetch --all
    fi

    echo "Installing pre-commit..."
    pip install --quiet pre-commit

    if [ "$ENABLE_TEST01_INIT_TEST" = "1" ]; then
        python3 /opt/base_db.py init-conf
    fi
fi

exec python3 /opt/orchestrator.py
