# EDITORIAL-REVIEW-001 — returned-review admission synthesis / 001

**Evidence state:** `AGENT_SYNTHESIS_CANDIDATE` (non-authoritative).  
**Parent:** [EDITORIAL-REVIEW-001 #314](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/314).  
**Work programme:** `ATLAS-EDITORIAL-REVIEW-001`; return coverage #326–#345.  
**Immutable released baseline:** `atlas-v0.1.0@1d4c2532533ff98afb998f86e0443d3fa1d8682e`.  
**Mutable workbench:** [draft PR #320](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/pull/320), exact observed head `dc560a7d1282b49fc27d9800397a2e2c6c7d8e74`.  
**As-of observation:** 2026-10-08; every status below is a snapshot and must be re-fetched before acting.

## What has actually happened

All **20 of 20** non-Part-I chapter-review issues (#326–#345) contain durable `RESULT/1` comments and currently carry `gcl-state:returned` on live issue readback. Their assignments span the **76 non-Part-I chapters** of the 80-chapter Atlas. The remaining four orientation chapters are handled separately under Part I (#318, agent pass #322); the typesetting check #321 has also returned. A RETURNED issue is evidence of a worker handback, not a passed independent acceptance gate, completed mathematical proof, or chapter signoff.

Of the 20 correction PRs associated with those chapter-review returns, **17 are merged into the mutable workbench branch** and **three are still OPEN/DRAFT** at this snapshot. GitHub's `merged=true` for these 17 means candidate admission into the editable branch, **not** into protected main or the public `atlas-v0.1.0` edition. The latest merger among these, P13-A PR #371, has merge commit exactly equal to the observed workbench head `dc560a7d...`. This is a source of truth more recent than the controller handoff's recorded earlier head.

## Return-to-admission matrix

| Assigned packet | Returned issue | Correction PR | Correction state |
| --- | --- | --- | --- |
| P02-A | [#326](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/326) | [#349](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/pull/349) | MERGED |
| P02-B | [#327](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/327) | [#346](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/pull/346) | MERGED |
| P03 | [#328](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/328) | [#347](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/pull/347) | MERGED |
| P04 | [#329](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/329) | [#348](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/pull/348) | MERGED |
| P05 | [#330](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/330) | [#350](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/pull/350) | MERGED |
| P06-A | [#331](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/331) | [#351](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/pull/351) | MERGED |
| P06-B | [#332](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/332) | [#352](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/pull/352) | MERGED |
| P07-A | [#333](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/333) | [#353](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/pull/353) | MERGED |
| P07-B | [#334](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/334) | [#354](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/pull/354) | MERGED |
| P08 | [#335](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/335) | [#355](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/pull/355) | MERGED |
| P09 | [#336](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/336) | [#357](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/pull/357) | MERGED |
| P10-A | [#337](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/337) | [#361](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/pull/361) | MERGED |
| P10-B | [#338](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/338) | [#358](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/pull/358) | MERGED |
| P11 | [#339](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/339) | [#374](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/pull/374) | DRAFT |
| P12-A | [#340](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/340) | [#365](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/pull/365) | MERGED |
| P12-B | [#341](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/341) | [#370](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/pull/370) | MERGED |
| P13-A | [#342](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/342) | [#371](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/pull/371) | MERGED |
| P13-B | [#343](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/343) | [#372](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/pull/372) | DRAFT |
| P14-A | [#344](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/344) | [#373](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/pull/373) | DRAFT |
| P14-B | [#345](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/345) | [#360](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/pull/360) | MERGED |

**Cross-matrix check:** exactly 20 distinct issue IDs; 17 `MERGED` correction PRs and 3 `DRAFT` correction PRs. All rows were compiled against live GitHub issue/PR objects and corresponding return messages, not from prior chat recollection. The issue/PR states may change independently after this frozen observation.

## Four outstanding draft evidence branches

The next bounded **admission candidates**, without implying that any is already independently approved:

1. [P13-B / PR #372](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/pull/372), issue [#343](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/343), head `ee7b9c75182582849cfdad8ab03430f07474b1f4`: exact ring all-reduce placement/byte counts and hardware Roofline traffic replay. Check six-step ring indexing, reduction semantics, integer accounting and boundary between synthetic traffic and measured hardware before admission.
2. [P14-A / PR #373](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/pull/373), issue [#344](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/344), head `59f3472ce66644e31e163a3b2f2bd801e8dc20aa`: 20-unit finite causal construction, state-machine guards and deterministic Replay LF-byte discipline. Replay source-script SHA and exact expected-output byte identities across platforms; do not replace byte checks by normalization.
3. [P11 / PR #374](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/pull/374), issue [#339](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/339), head `a23987097f3c68cd3282838ef1a4acf4cadbcbd1`: **P1 provenance precision**. The previously locked manuscript path for REGRET incorrectly carried the SHA-1 of REGRET's *specification*. Confirm the corrected historical exact Git manuscript blob `6c842b5bd41eef31891d8ce99734109aa344e0a4` against historical commit `39f419abb72c941e041f92f2834229f9968da006`, not merely matching the submitted commentary. Independently test regret/optionality witnesses.
4. [Part I / PR #375](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/pull/375), issue [#322](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/322), head `74f12d524351a409a51e22b24f42041b108c27a3`: global flow/semiflow/local flow definitions and claim-support display notation reconciled in source Markdown; one dangling RC2 overlay sentence removed by asserted generator transformation. Inspect alignment between corrected Markdown, immutable RC1 overlay and generated LaTeX. This is a **separate Part I correction**, not one of the three remaining chapter-review PRs.

At the snapshot all four PRs are open drafts; author review comments and green CI, where present, must not substitute for role-separated source/math inspection or changed-head replay. Pulls based on a formerly pinned `b0b7d037...` base require fresh comparison with the now-advanced workbench before any admission.

## Admission and publication invariants

1. **Issue returned != correction merged != chapter accepted != public release authorized.** These are distinct state axes. Return status remains valid even when a PR is draft. No issue state shall assert final proof/certification.
2. Keep the released `atlas-v0.1.0` tag, its source locks and public release assets immutable. Integrate eligible edits only into `editorial/part01-corrections-20261008` using its actual branch protections.
3. On each candidate correction, record reviewer agent role, distinct pass/run identifier, reviewed PR head, substantive evidence, tests/failure case, and explicit remaining limits. The authenticated GitHub account alone neither proves nor refutes role independence.
4. After authorized admission, re-fetch the mutable PR #320 head and run exact-head structural CI and targeted replay; regenerate/review the release-candidate TeX and relevant PDF/HTML. Baseline last-recorded counts: 80 chapters, 2,971 historical LaTeX label identities, 18 figure placements.
5. **Zero of 80 final chapter editorial signoffs** is still the last controller-reported figure. This matrix **does not** advance that figure, validate the full rendered PDF/HTML or independently re-read every research claim. Per-chapter math/narrative/figure/accessible-semantic verdicts remain evidence gates.
6. The controller `state/atlas-controller:governance/ACTIVE_TRANSACTION.yaml` and `CURRENT_HANDOFF.md` still named earlier workbench head `b0b7d037...` when sampled. That is a **stale recovery snapshot**, not an instruction to rewind or overwrite `dc560a7d...`. A separately authorized controller transaction should refresh it by protected readback, preserving previous checkpoints.

## Smallest bounded successors

- **SYNTH-002 / four draft-PR independent admission passes:** one scoped math/source-critical review of each of #372, #373, #374 and #375, with recorded evidence and failure returns; source-lock precedence for #374. No Human Steward copy/paste or login inequality gate.
- **SYNTH-003 / render and acceptance matrix:** recompute exact merged workbench, reconcile all 80 individual chapter dispositions and 18 figure semantics against source and *rendered* outputs. Do not translate a returned issue or merge into `EDITORIALLY_ACCEPTED` without chapter-specific proof of acceptance.
- **Controller-state reconciliation:** reconcile queue/projection truth and the actual PR #320 head under the controller recovery protocol, without changing scientific authority or the public release. This documentary synthesis is not itself a controller-state update.

**Disposition of this packet:** evidence synthesis complete; corrected-edition editorial acceptance and publication **not established**.
