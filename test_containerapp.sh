#!/usr/bin/env bash
set -euo pipefail

# ------------------------------------------------------------
# Student usage:
# 1) Change APP_URL
# 2) (Optional) change PROMPT
# 3) Run: bash test_containerapp.sh
# ------------------------------------------------------------

APP_URL="https://hf-fastapi-app-etu1.redgrass-d540cf0f.westeurope.azurecontainerapps.io"
PROMPT="Hello from etu1"

echo "== Test 1: GET /health =="
HEALTH_RESPONSE="$(curl -s "${APP_URL}/health")"
echo "${HEALTH_RESPONSE}"
echo

echo "== Test 2: POST /generate =="
GENERATE_RESPONSE="$(curl -s -X POST "${APP_URL}/generate" \
  -H "Content-Type: application/json" \
  -d "{\"prompt\":\"${PROMPT}\"}")"
echo "${GENERATE_RESPONSE}"
echo

echo "Done."
