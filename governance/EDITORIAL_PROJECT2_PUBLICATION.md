# Atlas editorial Project #2 publication receipt

Record: EDITORIAL-PROJECT2-PUBLICATION/1  
Recorded: 2026-10-08  
Parent: [Atlas editorial issue #314](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/314)  
Project: [GCL Worker Queue, organization Project #2](https://github.com/orgs/grandchallenge/projects/2)  
Project node: `PVT_kwDOB9Ao_c4Blwur`; AVAILABLE view: `PVTV_lADOB9Ao_c4BlwurzgL64bo`  
Exact editorial candidate PR #320: `ff3ed0972e3637350c9140eaa85de7169fe6ca76` at publication checkpoint. Public `atlas-v0.1.0` remains unchanged.

## Why publication was missing

Earlier work created the Atlas GitHub issues and a chapter queue YAML, but **did not add those issues to Project #2** or populate the organization Issue Fields used by its AVAILABLE view. The Project consequently held 25 MATHSOLVE items and no Atlas jobs. The AVAILABLE view filter is `is:open "GCL State":AVAILABLE`.

The GCL State, Campaign, Role, Collaboration, and Phase columns are **organization Issue Fields** projected into GitHub Projects (not mutable custom Project field options). A Project GraphQL `updateProjectV2Field` attempt was rejected with `Only custom fields can be updated`; the supported REST route is `POST repos/{owner}/{repo}/issues/{n}/issue-field-values`.

## Verified post-repair publication

- Scope: all **25 open Atlas issues #321–#345**, exactly one Project item per issue.
- Functional work: #321 typography, #322 independent Part I technical check, #323 all 18 figures, #324 OPTBASE repair/review, #325 accessibility.
- Corpus editorial work: 20 zero-context issues #326–#345, covering all 76 non-Part-I chapters without duplicates (per candidate `governance/editorial/v0.1.0/CHAPTER_AGENT_QUEUE.yaml`).
- Field `GCL State` (REST id `47953501`) = `AVAILABLE` on all 25; field `GCL Campaign` (REST id `47953502`) = `ATLAS-EDITORIAL-REVIEW-001`.
- Other issue fields: `GCL Role` = `VERIFY` (except #324 `CONSTRUCTIVE`); `GCL Collaboration` = `COOPERATIVE`; `GCL Phase` = `SHARED`. Project column `Status` is `Todo`.
- Labels: `gcl-job`, `gcl-state:available`, `gcl-collab:cooperative`, applicable role, and `gcl-pickup:direct-editorial`.
- Post-repair project items = **50**, of which **25** Atlas items. Exact live GraphQL readback verified issue uniqueness, open state, GCL State = AVAILABLE, GCL Campaign, and original repository identity for every #321–#345.
- Project README now documents the Atlas-specific pickup protocol; readback confirms the `Atlas editorial jobs — direct contribution lane` section exists.

## Authority and pickup distinction

MATHSOLVE queue-managed issues continue to use `/claim`, a `GCL-WORKER-RESERVATION/1` response, an immutable task, and `/release`; that controller responds to **MATHSOLVE issue comments**, not Atlas issues. **Do not tell an Atlas worker to wait for a nonexistent MATHSOLVE reservation on an Atlas issue.**

These Atlas jobs are directly offered as bounded editorial work through their zero-context GitHub issue instructions. Workers read the current controller and exact PR head, carry out the scoped work, and post the required `RESULT/1` on the Atlas issue. `AVAILABLE` is a *discovery projection*, not a protected execution lease, authenticated claim, review signoff, or permission to mutate protected main. Atlas agent outputs still require adjudication. There is no claim that an independent agent has picked up or returned work.

## Reconciliation rule

When a new Atlas editorial WP is created: (1) publish its self-contained issue; (2) add exactly one item to Project #2; (3) set the organization-level Issue Fields through the issue-field-values REST API; (4) label with `gcl-pickup:direct-editorial`; (5) **read back both the Issue Fields and Project's item node**, checking the AVAILABLE filter; (6) only then say that the job is discoverable. Idempotently reuse an existing Project item; never create a duplicate. If protected queue-managed reservations are desired in future, implement them through a separately governed dispatch/lease integration rather than implying that direct editorial pickup is the MATHSOLVE reservation protocol.

This receipt reports operational discovery, **not** independent mathematical or editorial acceptance (0/80 final signoffs at this checkpoint).
