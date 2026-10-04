#!/usr/bin/env bash
set -euo pipefail

ROOT="$(git rev-parse --show-toplevel)"
cd "$ROOT"

RUNNER_ROOT="${GCL_COLAB_RUNNER_ROOT:-/mnt/f/_codex/MATH/QUANTUM-TECHNOLOGIES}"
GDSUITE_DIR="${GDSUITE_DIR:-/home/jim/GDsuite}"
JOB="${1:-$ROOT/experiments/gsd-001/colab/jobs/wp01_olmo2_1b_crt_coarse20_t4.json}"

VENV_PY="$RUNNER_ROOT/.venv/bin/python"
COLAB_BIN="$RUNNER_ROOT/.venv/bin/colab"
COLAB_AUTH="${COLAB_AUTH:-oauth2}"

[[ -x "$VENV_PY" ]] || { echo "missing existing runner python: $VENV_PY" >&2; exit 2; }
[[ -x "$COLAB_BIN" ]] || { echo "missing existing runner colab CLI: $COLAB_BIN" >&2; exit 2; }
[[ -f "$JOB" ]] || { echo "missing job: $JOB" >&2; exit 2; }
[[ -d "$GDSUITE_DIR" ]] || { echo "missing locked GDsuite checkout: $GDSUITE_DIR" >&2; exit 2; }

EXPERIMENT_ID="$("$VENV_PY" - "$JOB" <<'PY'
import json,sys
job=json.load(open(sys.argv[1],encoding="utf-8"))
print(job["experiment_id"])
PY
)"
REMOTE_TIMEOUT="$("$VENV_PY" - "$JOB" <<'PY'
import json,sys
job=json.load(open(sys.argv[1],encoding="utf-8"))
print(int(job["remote_timeout_seconds"]))
PY
)"
ACCELERATOR="$("$VENV_PY" - "$JOB" <<'PY'
import json,sys
job=json.load(open(sys.argv[1],encoding="utf-8"))
print(job["resource"]["accelerator"])
PY
)"

RUN_ID="$(date -u +%Y%m%dT%H%M%SZ)-$$"
SESSION="gcl-gsd-wp01-$RANDOM-$$"
LOCAL_RUN="$ROOT/experiments/gsd-001/runs/hosted/$EXPERIMENT_ID/$RUN_ID"
mkdir -p "$LOCAL_RUN"

PAYLOAD="$LOCAL_RUN/gcl_source.tar.gz"
MANIFEST="$LOCAL_RUN/gcl_manifest.json"
cp "$JOB" "$LOCAL_RUN/gcl_job.json"

"$VENV_PY" experiments/gsd-001/colab/build_payload.py   --upstream-dir "$GDSUITE_DIR"   --output "$PAYLOAD"   --manifest "$MANIFEST"

ALLOCATED=0
cleanup() {
  rc=$?
  set +e
  if [[ "$ALLOCATED" -eq 1 ]]; then
    "$COLAB_BIN" --auth="$COLAB_AUTH" log -s "$SESSION"       -o "$LOCAL_RUN/colab-execution.md" >"$LOCAL_RUN/colab-log-command.txt" 2>&1 || true
    "$COLAB_BIN" --auth="$COLAB_AUTH" stop -s "$SESSION"       >"$LOCAL_RUN/colab-stop.txt" 2>&1 || true
  fi
  "$COLAB_BIN" --auth="$COLAB_AUTH" sessions     >"$LOCAL_RUN/colab-sessions-after.txt" 2>&1 || true
  exit "$rc"
}
trap cleanup EXIT INT TERM

echo "[GSD] allocating session=$SESSION accelerator=$ACCELERATOR"
"$COLAB_BIN" --auth="$COLAB_AUTH" new -s "$SESSION" --gpu "$ACCELERATOR"
ALLOCATED=1

"$COLAB_BIN" --auth="$COLAB_AUTH" status -s "$SESSION" >"$LOCAL_RUN/colab-status.txt"
"$COLAB_BIN" --auth="$COLAB_AUTH" upload -s "$SESSION" "$PAYLOAD" /content/gcl_source.tar.gz
"$COLAB_BIN" --auth="$COLAB_AUTH" upload -s "$SESSION" "$LOCAL_RUN/gcl_job.json" /content/gcl_job.json
"$COLAB_BIN" --auth="$COLAB_AUTH" upload -s "$SESSION" "$MANIFEST" /content/gcl_manifest.json

set +e
"$COLAB_BIN" --auth="$COLAB_AUTH" exec -s "$SESSION"   -f "$ROOT/experiments/gsd-001/colab/gsd_remote_job.py"   --timeout "$REMOTE_TIMEOUT"   > >(tee "$LOCAL_RUN/remote-stdout.txt")   2> >(tee "$LOCAL_RUN/remote-stderr.txt" >&2)
REMOTE_RC=$?
set -e

"$COLAB_BIN" --auth="$COLAB_AUTH" download -s "$SESSION"   /content/experiment_receipt.json "$LOCAL_RUN/experiment_receipt.json"   >"$LOCAL_RUN/download-receipt.txt" 2>&1 || true
"$COLAB_BIN" --auth="$COLAB_AUTH" download -s "$SESSION"   /content/gcl_output_bundle.tar.gz "$LOCAL_RUN/gcl_output_bundle.tar.gz"   >"$LOCAL_RUN/download-bundle.txt" 2>&1 || true

[[ -f "$LOCAL_RUN/experiment_receipt.json" ]] || {
  echo "[GSD] missing experiment receipt; evidence retained at $LOCAL_RUN" >&2
  exit 11
}
[[ -f "$LOCAL_RUN/gcl_output_bundle.tar.gz" ]] || {
  echo "[GSD] missing output bundle; evidence retained at $LOCAL_RUN" >&2
  exit 12
}

"$VENV_PY" - "$LOCAL_RUN/experiment_receipt.json" "$MANIFEST" "$LOCAL_RUN/gcl_job.json" <<'PY'
import hashlib,json,sys
from pathlib import Path
receipt=json.load(open(sys.argv[1],encoding="utf-8"))
manifest=json.load(open(sys.argv[2],encoding="utf-8"))
job_path=Path(sys.argv[3])
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
print("[GSD] receipt status:", receipt.get("status"))
print("[GSD] observed runtime:", receipt.get("runtime"))
if receipt.get("status") != "GREEN_ENGINEERING":
    raise SystemExit(10)
if receipt.get("source_commit") != manifest.get("source_commit"):
    raise SystemExit("receipt source commit mismatch")
if receipt.get("source_payload_sha256") != manifest.get("payload_sha256"):
    raise SystemExit("receipt source payload mismatch")
if receipt.get("job_sha256") != sha(job_path):
    raise SystemExit("receipt job digest mismatch")
PY

if [[ "$REMOTE_RC" -ne 0 ]]; then
  echo "[GSD] remote execution failed rc=$REMOTE_RC; evidence retained at $LOCAL_RUN" >&2
  exit "$REMOTE_RC"
fi

echo "[GSD] WP01 hosted job GREEN: $LOCAL_RUN"
