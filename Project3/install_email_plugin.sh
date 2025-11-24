#!/usr/bin/env bash
# install_email_plugin.sh
# Usage: bash scripts/install_email_plugin.sh

set -e
PLUGINS_REPO="https://github.com/Significant-Gravitas/Auto-GPT-Plugins.git"

if [ ! -d "Auto-GPT" ]; then
  echo "Auto-GPT directory not found. Run setup_autogpt.sh first."
  exit 1
fi

echo "Cloning plugins repo..."
git clone ${PLUGINS_REPO} tmp-plugins
mkdir -p Auto-GPT/plugins
cp -r tmp-plugins/plugins/email Auto-GPT/plugins/
rm -rf tmp-plugins

echo "Installing email plugin dependencies..."
# activate your venv first or run with environment
source Auto-GPT/autogpt-env/bin/activate
pip install -r Auto-GPT/plugins/email/requirements.txt

echo "Email plugin copied to Auto-GPT/plugins/email and dependencies installed."
echo "Please edit Auto-GPT/plugins/email/README.md and set your credentials."
