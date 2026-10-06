# COMPOSE-001 — Transaction Receipt

## Identity
- chapter: ATLAS-CH-COMPOSE-001
- implementation issue: #231
- protected baseline: eab85ed47695e1c3ae19f69e85b194c48a576a31
- branch: work/compose-231

## Hard prerequisites
BCONTRACT-001:
- manuscript a270c38cda7ff280e517bd1a09ed196bb48dc759
- source lock 80463b18216747650d3ff8e99d6da933173d4486
- AUDIT-003 9723fcb3dfa0111829b98f1c9bb416a13dbd714e

SPLIT-001:
- manuscript bcaf1db6b1fc7144e2472ff2725f7ff561fe7fc0
- source lock afb84e2f3ebb941f320c52693b088b0eb078b8ce
- AUDIT-036 5e093460550c15fe491ba3214b2f52d48076dc0a

## Implementation artifacts
- specification 9eef5fff041a255f7fc137d24ac7457fcc1db8a7
- derivations f698e1f2ddf35099b53ad85af8e9e357de19166b
- witness 878a85b8b163f99fb68b8a9a5e4f414a14fa8426
- manuscript da94fe5d6106a50b168a4f95fa0765c9c7c6b415
- source lock c16ab3f6ce67e81cff9f85f2f98a79ad55549cd5
- Chapter Ledger 210dbb1d892a2cc58756e262457e5696a0d69729
- Source Register a03c6c3f9ea02fdc74fa20d3a9f6546d46f49824

## Durable substrate
- local component validity does not imply system validity;
- chronological A-then-B is BA for column-vector action;
- the exact witness has ||A||_2=||B||_2=3/2, ||BA||_2=1, ||AB||_2=9/4;
- under system gain budget tau=2, one chronology passes and the reverse fails;
- the commuting control has the same component norm ceilings and product I in either order;
- local approximation errors compose as epsilon_g + L_g epsilon_f under explicit connecting-domain assumptions;
- the n-stage bound is sum_j epsilon_j product_{k>j} L_k;
- component, interface, composition, and system-level certificates are distinct evidence levels;
- local certificates are not promoted to global safety theorems.

## Exact error-budget witness
With epsilon_f=epsilon_g=1/10 and downstream gain L_g=3/2:
- derived composition error bound = 1/4;
- declared system budget = 1/5;
- both local error budgets can pass while the system-level derived budget fails.

## Source boundary
No new external primary authority was added. All external mathematical authority is inherited through audited BCONTRACT-001 and SPLIT-001.

## Validation gate
Merge requires exact-head canonical repository validation, independent exact witness replay, exact-head GitHub Actions success, and a fresh post-draft audit.


## Audit provenance repair
AUDIT-058 identified that the original receipt predated the two documentary protocol-marker repairs required by canonical validation. The receipt is corrected to the exact implementation-merge identities:
- witness 878a85b8b163f99fb68b8a9a5e4f414a14fa8426
- manuscript da94fe5d6106a50b168a4f95fa0765c9c7c6b415

The repairs changed only required documentary headings; no mathematical statement or witness arithmetic changed.
