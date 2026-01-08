#!/usr/bin/env bash
set -euo pipefail

# Run the Streamlit app using the project's virtual environment Python so
# the correct site-packages (e.g., matplotlib) are used.
# Usage: ./scripts/run_streamlit.sh [additional streamlit args]

BASE_DIR="/workspaces/blank-app-260108"
VENV_PY="$BASE_DIR/.venv/bin/python"

if [ ! -x "$VENV_PY" ]; then
  echo "Error: virtualenv python not found at $VENV_PY"
  echo "Make sure you created the venv and installed requirements into it."
  exit 1
fi

# Forward any additional args to streamlit
"$VENV_PY" -m streamlit run "$BASE_DIR/streamlit_app.py" --server.enableCORS false --server.enableXsrfProtection false "$@"
