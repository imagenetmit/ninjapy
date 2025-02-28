#!/bin/bash

# Install the speakeasy CLI
curl -fsSL https://raw.githubusercontent.com/speakeasy-api/speakeasy/main/install.sh | sh

# Setup samples directory
rmdir samples || true
mkdir samples

python -m pip install --upgrade pip
pip install -e .

# Generate starter usage sample with speakeasy
speakeasy generate usage -s https://app.ninjarmm.com/apidocs/NinjaRMM-API-v2.json -l python -o samples/root.py