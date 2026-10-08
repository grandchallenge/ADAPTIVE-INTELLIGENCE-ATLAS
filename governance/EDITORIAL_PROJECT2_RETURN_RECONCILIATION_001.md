# Atlas editorial direct-return projection — checkpoint 001

**Date:** 2026-10-08  
**Campaign:** ATLAS-EDITORIAL-REVIEW-001  
**Parent:** #314  
**Project:** https://github.com/orgs/grandchallenge/projects/2  
**Corrected-edition source:** PR #320 at `ff3ed0972e3637350c9140eaa85de7169fe6ca76` (result inputs)  
**Authority:** operational queue projection only; NO acceptance or certification.

## Discovery and original defect

Atlas issues #321–#345 were correctly published in Project #2 with `GCL State=AVAILABLE`; the direct-pickup lane had no issue_comment intake workflow to project newly posted `RESULT/1` records into `GCL State=RETURNED`. Consequently, nine existing returns (#326–#334) were incorrectly still shown in AVAILABLE rather than RETURNED.

## Authenticated return capture (not adjudication)

Nine distinct, human-readable `RESULT/1` comments were found directly on Atlas issues #326–#334. Each contained its assignment identifier, exact `input_head` at `ff3ed0972e3637350c9140eaa85de7169fe6ca76`, authenticated commenter identity `fyremael` matching the beginning of its stated reviewer identity, and a disposition of `completed` or `partial`.

| Issue | Assignment | Comment ID | Self-reported status |
|---|---|---:|---|
| #326 | ATLAS-EDITORIAL-P02-A | 6058138109 | completed |
| #327 | ATLAS-EDITORIAL-P02-B | 6057807495 | partial |
| #328 | ATLAS-EDITORIAL-P03 | 6057980533 | partial |
| #329 | ATLAS-EDITORIAL-P04 | 6058069115 | partial |
| #330 | ATLAS-EDITORIAL-P05 | 6058433117 | partial |
| #331 | ATLAS-EDITORIAL-P06-A | 6058575276 | partial |
| #332 | ATLAS-EDITORIAL-P06-B | 6058667359 | partial |
| #333 | ATLAS-EDITORIAL-P07-A | 6059088272 | partial |
| #334 | ATLAS-EDITORIAL-P07-B | 6059219309 | partial |

**Critical independence boundary:** all nine returns originate from `fyremael`, also the author of draft PR #320. They are author/editorial contributions and **not independent peer reviews, audits, protected approvals, editorial chapter signoffs, or mathematical certification**. In particular, a `status: completed` on #326 describes self-reported work completion, not chapter acceptance. Partial returns remain incomplete; assess residuals and create successors before claiming complete coverage.

## Operational repair and readback

For each of #326–#334, the organization Issue Field `GCL State` (REST ID 47953501) was set to `RETURNED` via the GitHub issue-field-values API, `gcl-state:returned` was added, and `gcl-state:available` removed. The 16 remaining Atlas assignments retained AVAILABLE. No issue closed, no candidate promoted, no source modified.

Fresh GitHub GraphQL Project V2 readback verified:
- 25 unique Atlas items, with 9 `RETURNED` and 16 `AVAILABLE`.
- `GCL Campaign=ATLAS-EDITORIAL-REVIEW-001` and open issue status for all 25.
- The existing Project `RETURNED` view filter is `"GCL State":RETURNED`.
- Other organization project jobs remain outside the scope of this reconciliation.

This corrects the *present* projection, but future returns still require an automated Atlas-specific workflow or another routine reconciliation; do not claim automatic intake has been deployed yet.

## Safe next action

Implement an Atlas issue_comment projection on protected `main` through the standard reviewed PR path (not by editing Project data ad hoc). Event processing must be idempotent, only affect labeled Atlas direct-editorial issues with a syntactically matching RESULT/1 and authenticated author, move AVAILABLE to RETURNED, and leave mathematical/editorial adjudication entirely outside the projector. Include tests covering spoof, unrelated issue, malformed result, duplicate event and existing returned state. Update controller when that PR is approved and merged.

Editorial programme final signoffs remain **0/80** until evidenced otherwise.
