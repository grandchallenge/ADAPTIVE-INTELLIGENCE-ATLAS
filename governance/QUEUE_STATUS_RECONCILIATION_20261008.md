# Project #2 queue-state reconciliation — 2026-10-08 / terminal readback

**Scope:** operational GitHub Projects `Status` projection only. The organization Issue Field `GCL State` remains the authoritative worker-lifecycle state. Project `Done` signifies worker return, not mathematical or editorial acceptance.

**Executor:** authenticated `gh` session on CHAD/WSL, running the already protected reconciler `grandchallenge/MATHSOLVE@4291d60c72f873f55cbcb220a45786a7edd6999b:ci/gcl_worker_queue_project_status.py`. The script validates 61 bound Project items against GitHub REST Issue Field state and labels, refuses unknown identities/drift, applies only mismatched status selections and checks all 61 item IDs after mutation.

**Pre-apply scan:** 61 unique items; Issue Fields = 52 RETURNED, 4 RESERVED, 1 BLOCKED, 4 AVAILABLE. Project columns before replay = 43 Done, 18 Todo. Exact authoritative target = 52 Done, 5 In Progress, 4 Todo. Changes required: **14** (the previously outstanding nine plus subsequent live lifecycle transitions).

**Executed:** `--apply --report /tmp/atlas-queue-applied.json` on 2026-10-08, 14/14 Project-only mutations. Script terminal result: `SUCCESS exact-item board projection and readback`. Retained local operator report `/tmp/atlas-queue-applied.json`. No issue labels, assignment payloads, dispatch, PRs, certification, chapter signoffs or protected mathematical claims were altered by the reconciler.

**Recovery and repetition:** run `python3 ci/gcl_worker_queue_project_status.py` from a checkout of protected MATHSOLVE first (dry run); verify target counts/mismatches and `GCL State` for every item. Only then run `--apply` with authorized organization Project-write credentials, followed by a fresh no-op dry run. The operation is idempotent and detects concurrent Issue Field drift before each write.

**Atlas specific:** All 20 non-Part-I reviewer issues #326–#345 have returned `RESULT/1` by later live readback; four formerly AVAILABLE jobs #338, #339, #343, #344 are no longer unclaimed. #321 and #322 also have returned review work. This is intake completion, not the requested 80-chapter editorial acceptance. Candidate PR #320 advanced beyond the historical controller head to `0d113bd5da51564c72c05ab54ab4c1ed1acf7afd` at review time; do not rewind it.

**Claim status:** Queue mechanics reconciled; manuscript editorial/release acceptance not established.
