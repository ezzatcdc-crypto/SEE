#!/usr/bin/env bash
set -euo pipefail

RUN_ID="${RUN_ID:?RUN_ID required}"
OUTPUT_ROOT="${OUTPUT_ROOT:-out}"

RUN_DIR="${OUTPUT_ROOT}/${RUN_ID}"

if [[ -d "$RUN_DIR" && -n "$(ls -A "$RUN_DIR" 2>/dev/null)" ]]; then
  echo "Run directory exists and is non-empty: $RUN_DIR" >&2
  exit 1
fi

mkdir -p "$RUN_DIR"

LOG="$RUN_DIR/orchestration.log"
JSON="$RUN_DIR/orchestration.json"

echo "{}" > "$JSON"

echo "S1 SNAPSHOT" | tee -a "$LOG"
${TOOL_SNAPSHOT:-true}

echo "S2 CORE RUN" | tee -a "$LOG"
${TOOL_CORE_RUN:?TOOL_CORE_RUN required}

echo "S3 POSTCORE REPORTING" | tee -a "$LOG"
${TOOL_POSTCORE_REPORTING:?TOOL_POSTCORE_REPORTING required}

if [[ "${ENABLE_PUBLISH:-0}" == "1" ]]; then
  echo "S4 POSTCORE PUBLISH" | tee -a "$LOG"
  ${TOOL_POSTCORE_PUBLISH:-true}
fi

if [[ "${ENABLE_MONITORING:-0}" == "1" ]]; then
  echo "S5 POSTCORE MONITORING" | tee -a "$LOG"
  ${TOOL_POSTCORE_MONITORING:-true}
fi

echo "DONE" | tee -a "$LOG"
