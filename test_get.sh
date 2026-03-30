#!/usr/bin/env bash
set -euo pipefail

# Change only APP_URL, then run:
# bash test_get.sh

APP_URL="https://hf-fastapi-app-etu1.redgrass-d540cf0f.westeurope.azurecontainerapps.io"

echo "== GET /health =="
curl -s "${APP_URL}/health"
echo
