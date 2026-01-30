#!/usr/bin/env bash
set -euo pipefail

# Ensure a Linux-native uv venv exists outside the bind-mounted workspace so
# host OS venvs never shadow container binaries.
if [[ ! -x "/opt/venv/bin/jupyter" ]]; then
  echo "Creating uv venv in /opt/venv..."
  uv venv /opt/venv
  # Install exact locked dependencies for reproducible workshop environments.
  uv sync --frozen --no-dev
fi

# Default to a token for basic protection; allow explicit empty token if desired.
TOKEN_ARG=("--NotebookApp.token=${JUPYTER_TOKEN}")
if [[ -z "${JUPYTER_TOKEN:-}" ]]; then
  TOKEN_ARG=("--NotebookApp.token=" "--NotebookApp.password=")
fi

# Run Jupyter Lab in-container (root) and expose it on all interfaces.
exec /opt/venv/bin/jupyter lab \
  --ip=0.0.0.0 \
  --port=8888 \
  --no-browser \
  --allow-root \
  "${TOKEN_ARG[@]}"
