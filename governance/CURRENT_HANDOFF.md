# CURRENT HANDOFF — Adaptive Intelligence Atlas

**Handoff date:** 2026-10-03  
**Repository:** `grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS`  
**Controller branch:** `state/atlas-controller`  
**Recovery authority:** `governance/ACTIVE_TRANSACTION.yaml`  
**Current main:** `743df1ab6d3cb7ac8f7d35b248c988995170a3e0`

This file exists so a fresh session can resume the Atlas composition programme without reconstructing state from chat history.

## 1. Mandatory restart sequence

On every fresh session or interruption:

1. Read `governance/ACTIVE_TRANSACTION.yaml` from branch `state/atlas-controller`.
2. Read this handoff file.
3. Fetch the current `main` SHA.
4. If `main` still equals the controller's recorded `baseline_commit`, execute the controller's `next_action`.
5. If `main` has advanced, recompute the dependency-legal frontier from `governance/CHAPTER_LEDGER.yaml` before instantiating new work.
6. Do not reconstruct live execution state from conversational memory when repository state is available.

## 2. Execution protocol

The Atlas uses transaction-mode execution.

For one bounded chapter tranche, carry the work through the full real boundary:

- create issue;
- create work branch from recorded baseline;
- lock exact prerequisites and external sources;
- write chapter specification;
- write formal/derivation or documentary packet;
- add a computational witness only when it materially clarifies the claim;
- write the full manuscript prose;
- update Chapter Ledger;
- update Source Register;
- write tranche receipt;
- open implementation PR;
- run repository validation;
- repair all in-scope defects until green;
- merge implementation PR;
- instantiate bounded post-draft audit;
- repair every in-scope audit defect;
- write audit record;
- open audit PR;
- validate and merge;
- verify issues closed/completed;
- recompute the dependency-legal frontier;
- return controller to `idle-ready` with the new baseline and next action.

Legitimate stop conditions are only:

- genuine external blocker;
- failed validation requiring human judgment;
- explicit human governance gate.

Do not hand back merely because an intermediate step completed.

## 3. Working style

Execute in short durable bursts.

Checkpoint live state to `governance/ACTIVE_TRANSACTION.yaml` whenever the transaction crosses a real phase boundary.

Avoid progress-only handbacks. A user message such as `next`, `resume`, `continue`, `proceed`, or `make it so` means: read the durable controller and continue the recorded transaction.

## 4. Current state

The controller is currently:

- state: `idle-ready`;
- baseline/main: `743df1ab6d3cb7ac8f7d35b248c988995170a3e0`;
- next target: `ATLAS-CH-EXPLORE-001`;
- title: **Exploration and Information Value**;
- reason: it ties for the largest unlocked downstream architecture cone at 5 nodes and is first under deterministic frontier ordering.

Current frontier, recomputed from the live Chapter Ledger after AUDIT-021:

1. `ATLAS-CH-EXPLORE-001` — downstream architecture count 5; direct consumer `ATLAS-CH-REGRET-001`.
2. `ATLAS-CH-NETNUM-001` — count 5; direct consumers `ATLAS-CH-ADAPTDEPTH-001`, `ATLAS-CH-BOUNDARYPROBE-001`.
3. `ATLAS-CH-CONTINUAL-001` — count 4; direct consumer `ATLAS-CH-EXTMEM-001`.
4. `ATLAS-CH-FORMAL-001` — count 4; direct consumer `ATLAS-CH-RESEARCHSM-001`.
5. `ATLAS-CH-RETRIEVAL-001` — count 4; direct consumer `ATLAS-CH-EXTMEM-001`.
6. `ATLAS-CH-SPARSE-001` — count 4; direct consumer `ATLAS-CH-MOE-001`.
7. `ATLAS-CH-DATA-001` — count 3; direct consumer `ATLAS-CH-CURRICULUM-001`.
8. `ATLAS-CH-LOCALGLOBAL-001` — count 3; no architecture-status direct consumer.
9. `ATLAS-CH-SPLIT-001` — count 3; direct consumers `ATLAS-CH-COMPOSE-001`, `ATLAS-CH-TRANSPORT-001`.
10. `ATLAS-CH-KRYLOV-001` — count 2; direct consumers `ATLAS-CH-ATTNAPPROX-001`, `ATLAS-CH-NEURALKRYLOV-001`.

## 5. Immediately preceding completed tranches

### EXPERIMENT-001 — Experiments as Arguments

- implementation issue: #96, closed completed;
- implementation PR: #97;
- implementation merge:
  `0e441ea8725a7527f138bf0b11b202a737b0dec8`;
- audit issue: #98, closed completed;
- audit:
  `AUDIT-021`;
- audit PR: #99;
- audit merge / current main:
  `743df1ab6d3cb7ac8f7d35b248c988995170a3e0`.

Central experiment object:

`E=(q,theta,U,A,Z,Y,g,V,rho,Omega)`

with:

- bounded claim;
- estimand;
- units/population/sample frame;
- intervention/assignment rule;
- nuisance structure;
- outcome;
- estimator/comparison rule;
- variation/uncertainty description;
- stopping/tuning/selection/reporting rule;
- interpretation scope.

Load-bearing doctrine:

- a run is not yet an experimental argument;
- hypothesis is distinct from estimand;
- intervention is distinct from observational association;
- a baseline is any comparator, while an ablation is a structured intervention on a component;
- seed variance is conditional run-to-run variation, not a substitute for data/population/implementation uncertainty;
- effect magnitude is distinct from statistical significance;
- reproducibility is distinct from replication and from validity;
- benchmark superiority does not by itself identify mechanism;
- selection and stopping are part of the design and may not be erased from the report.

Exact witness:

a deterministic 20-unit two-stratum construction has individual treatment effect +1 everywhere, yet confounded assignment yields a naive aggregate contrast of -7 while both within-stratum contrasts and the equal-stratum standardized contrast are +1.

AUDIT-021 repair:

the original stopping/selection coordinate `tau` collided with the audited Evidence chapter's `tau` epistemic-class coordinate. The chapter now uses `rho` throughout. No mathematical claim changed.

### RLBASE-001 — Reinforcement Learning and Control

- implementation merge:
  `39932c4067bd3d3f85a4d223586875cd2063e3b7`;
- audit:
  `AUDIT-017`;
- audit merge / resulting main:
  `015bc4dc465bde59105530cda2ad6d2d3500ab0e`.

Load-bearing content:

- finite discounted MDP object;
- Bellman expectation and optimality equations;
- dynamic programming versus sampled TD/Q-learning;
- policy-gradient boundary;
- model-based/Dyna boundary;
- POMDP belief-state boundary;
- exact rational two-state policy-improvement witness.

### DEPTH-001 — Depth as Computational Time

- implementation merge:
  `4ef01e5c1d88a09e107a8ca95ed7fc9fb9766855`;
- audit:
  `AUDIT-018`;
- audit merge:
  `9a00ed8fc6b0ca160a9b7e1fb4deef7c078f69cf`.

Load-bearing content:

- fixed, recurrent, adaptive, equilibrium, and conditional depth;
- separation of architectural, parameter, and execution depth;
- exact contraction witness
  `x_{k+1}=(x_k+2)/2`;
- stopping depth
  `tau(epsilon)=ceil(log_2(2/epsilon))`;
- explicit `criterion_met` versus `budget_exhausted`;
- heterogeneous compute resources represented separately unless scalarization is declared.

### MEMTAX-001 — A Taxonomy of Machine Memory

- implementation merge:
  `cd78611a76ba58a27644c37425a55c466090613b`;
- audit:
  `AUDIT-019`;
- audit merge:
  `ffca5ab3dbc75ef0b3ce0ff5afe13d86f32ae75e`.

Central taxonomy:

`M=(L,W,R,T,A,U,P,S)`

with:

- locus;
- write path;
- read path;
- lifetime;
- addressability;
- mutability;
- provenance;
- sharing/synchronization.

Six overlapping roles:

- parametric;
- working;
- episodic;
- semantic;
- associative;
- external.

Important audit repair:

**external memory is a locus property; persistence is the independent lifetime coordinate T.**

Exact witness:

one immutable three-record store supports exact-key, nearest-neighbor associative, and recency/episodic reads solely by changing the read contract.

### EVIDEX-001 — Evidence Exchange and Zero-Context Work

- implementation merge:
  `dceb03af6b0c253b66a1c04a00f2285acd899c73`;
- audit:
  `AUDIT-020`;
- audit merge / current main:
  `55085755626d60d2981a7cf17a6af7cbac60f9fc`.

Central dispatch object:

`D=(delta,Q,B,Sigma,C,Lambda,Gamma,rho)`

Central return object:

`R=(delta,chi,K,Pi,V,Delta)`

Load-bearing doctrine:

- zero-context work is **compiled context**, not absence of context;
- zero-context sufficiency constrains the **normative authorized task contract**, not worker psychology;
- hidden conversation state may not supply an authorized premise, permission, source, success criterion, or return requirement;
- provenance does not imply truth;
- durable identity does not imply authority;
- receipt != acceptance != promotion != certification;
- `independent_blind` is an information-flow declaration, not proof of statistical or institutional independence;
- synthesis requires an explicit logical composition rule;
- only the explicit pointwise proposition schema automatically supports union of domains.

Exact witness:

two different `inputs.txt` versions share the same pathname.

Pathname-only provenance leaves two source candidates.

Exact v1 SHA-256 selects one candidate and replay reproduces `result=5`.

## 6. Existing key prerequisite chapters

The following are already at `draft-v0.1` and audited where applicable:

- `ATLAS-CH-EVIDENCE-001` — Claims, Evidence, and Computational Witnesses;
- `ATLAS-CH-AGENTS-001` — From Models to Agents;
- `ATLAS-CH-COORD-001` — Coordination Architectures;
- `ATLAS-CH-REPLAY-001` — Replayable Evidence Objects;
- `ATLAS-CH-RLBASE-001`;
- `ATLAS-CH-DEPTH-001`;
- `ATLAS-CH-MEMTAX-001`.

Do not treat already-drafted downstream chapters as hidden prerequisite authority unless the Chapter Ledger explicitly declares them as dependencies.

## 7. Next tranche — EXPLORE-001

Stable ID:

`ATLAS-CH-EXPLORE-001`

Title:

**Exploration and Information Value**

Declared hard dependency in the Atlas Map/Ledger:

- `ATLAS-CH-RLBASE-001`.

The chapter contract in the Atlas Map is:

> Develop bandits, exploration–exploitation, information gain, value of information, and safe exploration.

The next session should instantiate this tranche from current main only if the controller remains `idle-ready` and main still equals the recorded baseline.

The audited RLBASE prerequisite may supply the MDP/control substrate. No later Regret or Optionality chapter may be used as hidden prerequisite authority unless the Chapter Ledger explicitly changes.

A sound intellectual spine should distinguish at least:

1. exploration as information acquisition from reward maximization under known dynamics;
2. multi-armed-bandit regret from full MDP exploration;
3. epistemic uncertainty from environment stochasticity;
4. value of information from immediate expected reward;
5. optimism, posterior sampling, and information-directed strategies as different mechanisms rather than synonyms;
6. safe exploration as constrained information acquisition, with the exact safety notion stated rather than assumed.

The tranche should use an exact finite witness where information has positive decision value despite a lower immediate expected reward, or another comparably small construction that makes exploration value mathematically visible.

## 8. Durable restart instruction for a fresh chat

A fresh session can be started with only:

> Resume the Adaptive Intelligence Atlas. Read `grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS` branch `state/atlas-controller`, `governance/ACTIVE_TRANSACTION.yaml` first, then `governance/CURRENT_HANDOFF.md`. Follow the recorded recovery rule and continue the bounded transaction through its real completion boundary. Work in short durable bursts; do not reconstruct state from chat.

No other chat history should be required.

## 9. Invariants that must remain true

- `ACTIVE_TRANSACTION.yaml` is the live recovery authority.
- Main must never be assumed unchanged; verify it.
- Chapter eligibility comes from the current Chapter Ledger.
- A chapter may consume only declared hard prerequisites plus explicitly source-locked external/public project evidence.
- Every strengthened claim requires strengthened support.
- Computational witnesses prove only their declared finite/bounded claims.
- Audit repairs must repair the manuscript/formal/source artifacts, not merely document defects.
- Validation must be green before merge.
- After completion, recompute the frontier and checkpoint `idle-ready`.

This handoff is a recovery aid. If it ever conflicts with the live controller or current repository state, the live controller plus current `main` and Chapter Ledger take precedence.
