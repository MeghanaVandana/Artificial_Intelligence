#!/usr/bin/env bash
# setup_autogpt.sh
# Usage: bash scripts/setup_autogpt.sh

set -e

REPO_URL="https://github.com/Significant-Gravitas/Auto-GPT.git"
VENV_DIR="autogpt-env"

echo "Cloning Auto-GPT..."
git clone ${REPO_URL} Auto-GPT || { echo "Clone failed (maybe directory exists)."; exit 1; }
cd Auto-GPT

echo "Creating virtual environment: ${VENV_DIR}"
python3 -m venv ${VENV_DIR}

echo "Activating virtual environment and installing requirements..."
# shellcheck disable=SC1091
source ${VENV_DIR}/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo "Setup complete. Remember to create a .env file with OPENAI_API_KEY."
echo "Example: echo 'OPENAI_API_KEY=your_key_here' > .env"
