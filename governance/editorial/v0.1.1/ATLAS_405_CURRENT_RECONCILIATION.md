# ATLAS #405; evidence-backed 80-chapter acceptance reconciliation

Source authority: protected main Chapter Ledger; candidate PR #320 at exact
head `07ea97f688bd8eab54f4d395aa2f6ef`. Public v0.1.0 is unchanged.
This is a **baseline**, not manuscript approval, release authority, or
a substitute for producer/critic reading of the actual physical rendered edition.

The companion `CHAPTER_ACCEPTANCE_EVIDENCE_080.json` contains **exactly 80**
canonical chapter IDs, their candidate source Git blob SHA-1 values, and
assignment-linked GitHub RESULT/1 comment identifiers/hashes. For Parts II–XIV,
20 previously published assignment packets cover 76 chapters; Part I's four
chapters retain their separate #318 route. All 80 final acceptance states
are **UNVERIFIED**, not falsely inferred from closed queue issues.

Live source inventory: 28 actual Atlas gcl-job issues #321–#345, #359, #362,
#363; every one is CLOSED and marked RETURNED. A complete read of their
GitHub comments found 29 issue-bound RESULT/1 messages. Issue #359 is an
explicit **synthetic projector canary**, excluded from all chapter review
claims. An operational return documents delivery, not chapter-critical
acceptance, correct current source head, or correction completeness.

The earlier mention of four unclaimed chapter work packages and two refreshed
technical reviews is **historical**. Do not create fresh duplicate jobs or
reopen RETURNED issues without verifying an actual new scoped need. PR #320
remains OPEN and currently reports a dirty merge baseline. Exact PR HEAD must
be read again before any correction, critic or acceptance promotion.

## Required next actions

Resolve 16 historical substantive review returns against the exact issue
comments and correction PR/head identities. Record each finding as
resolved, partial, unresolved or unverified, including precise source location,
severity and next issue owner. Then have separately accountable producer and
critic runs inspect each exact chapter source, native PDF and HTML and figure/
math/source/accessibility evidence. Only promote an individual row with both
role/run identities, justified critic verdict, exact matching candidate head,
proof of all severe findings addressed, and rendered artifact SHA-256 values.
Do not infer correctness or independence from GitHub account differences.

The evidence generator `ci/atlas_acceptance_evidence.py` reads current public
GitHub issues, the exact PR #320 source tree and the existing 20-package queue.
It fails closed if the inventory, source, status or PR head changes.
`tests/test_atlas_acceptance_evidence.py` tests missing rows, stale source,
fabricated approval, same-role acceptance and duplicate assignment.
The result is a reviewable audit ledger, **not** automatic publication.
