#!/bin/bash
set -e

export GIT_SSH_COMMAND="ssh -i /home/odoo/.ssh/id_rsa -o StrictHostKeyChecking=no"

REPO_SSH_URL="git@ssh.dev.azure.com:v3/${DEVOPS_ORG}/${DEVOPS_PROJECT}/${DEVOPS_REPO}"

if [ ! -d "/opt/repo/.git" ]; then
    echo "Cloning repository from ${REPO_SSH_URL}..."
    git clone --branch 15.0-dev "$REPO_SSH_URL" /opt/repo
    echo "Clone complete."
else
    echo "Repository present, fetching latest..."
    git -C /opt/repo fetch --all
fi

# Recursively init all submodules; failures in deeply nested ones are non-fatal
echo "Initialising submodules..."
git -C /opt/repo submodule update --init --recursive || echo "Warning: some submodules failed to init, continuing"

echo "Installing pre-commit..."
pip install --quiet pre-commit

exec python3 /opt/orchestrator.py
