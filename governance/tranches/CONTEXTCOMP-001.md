# CONTEXTCOMP-001 — Transaction Receipt

## Identity
- chapter: ATLAS-CH-CONTEXTCOMP-001
- implementation issue: #235
- protected baseline: b00d6020b809145a99689418db13ff6d6561a659
- branch: work/contextcomp-235

## Hard prerequisite
EXTMEM-001:
- manuscript 181685ceda93defb7a7051e0865898c7c4e3fb1d
- source lock 6ac2940c5a9432588ace9a82b15c73e7e00d874f
- AUDIT-031 a33ee84f0bfc69f8dc00e165506c55cabd68fec4

## Implementation artifacts
- specification 8243b3b000f34bf454564d00a9599923d5fdfeae
- derivations c974ac991c24bf00e65ddfd5ef46007945d983cf
- witness a4c662a7e80c40f1b715c0572be6b438059a7ee5
- manuscript 6ad1bdba01e731fd189e825cf43bd418e6a257b4
- source lock fe0f8449b501afa23af6b98b111396b3b967ba94
- Chapter Ledger ce262fc4530a36c1d7650189b6c27cd3a2fd3522
- Source Register e2bc3d53cbe68f31eaeb0d22082cf77084d60ba4

## Durable substrate
- retrieved candidate sets are distinct from compiled working contexts;
- authorization and freshness/version policy are hard admissibility constraints;
- mandatory current records create an explicit feasibility test before optional selection;
- provenance-preserving records are atomic in the finite formalism;
- complete serialized record cost, including provenance envelope, counts against context budget;
- optional selection maximizes only declared compiler utility under residual budget;
- serialization order is deterministic but not claimed universally optimal for model behavior;
- compiler validity is distinct from downstream answer correctness;
- compilation events admit replayable receipts.

## Exact budget-8 witness
Candidate ranks/costs/utilities:
- superseded policy v1: rank 1, cost 3, utility 9;
- task fact: rank 2, cost 4, utility 7;
- current mandatory policy v2: rank 3, cost 4, utility 8;
- background: rank 4, cost 2, utility 3;
- detail: rank 5, cost 3, utility 5.

Freshness removes policy v1.
Mandatory policy v2 consumes 4 budget units.
Residual budget is 4.
The unique maximum-utility optional set is the task fact.
Final compiled set is {current policy v2, task fact}, total cost 8, total declared utility 15.

## Rank-prefix control
A raw retrieval-rank prefix under budget 8 selects superseded policy v1 plus the task fact at cost 7 and cannot fit current mandatory policy v2. It therefore violates both freshness and mandatory-inclusion obligations. One-unit truncation of policy v2 violates the declared atomic provenance-envelope rule.

## Mandatory-overflow control
At budget 3, current mandatory policy cost 4 implies explicit MANDATORY_OVERFLOW; no valid atomic compiled context exists.

## Source boundary
No new external primary authority was added. External authority is inherited through audited EXTMEM-001. All new formal compilation claims are Atlas-owned finite definitions, derivations, and witnesses.

## Validation gate
Merge requires exact-head canonical repository validation, independent exact witness replay, exact-head GitHub Actions success, and a fresh post-draft audit.
