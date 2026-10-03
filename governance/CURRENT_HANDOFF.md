# CURRENT HANDOFF — Adaptive Intelligence Atlas

**Handoff date:** 2026-10-03  
**Repository:** `grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS`  
**Controller branch:** `state/atlas-controller`  
**Recovery authority:** `governance/ACTIVE_TRANSACTION.yaml`  
**Current main:** `f94a18010d969f80ddb96663bec02e449f4eb5eb`

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
- baseline/main: `f94a18010d969f80ddb96663bec02e449f4eb5eb`;
- next target: `ATLAS-CH-REGRET-001`;
- title: **Regret**;
- reason: it ties for the largest unlocked downstream architecture cone at 4 nodes and is first under deterministic frontier ordering.

Current frontier, recomputed from the live Chapter Ledger after AUDIT-025:

1. `ATLAS-CH-REGRET-001` — downstream architecture count 4; direct consumer `ATLAS-CH-OPTIONALITY-001`.
2. `ATLAS-CH-RETRIEVAL-001` — count 4; direct consumer `ATLAS-CH-EXTMEM-001`.
3. `ATLAS-CH-SPARSE-001` — count 4; direct consumer `ATLAS-CH-MOE-001`.
4. `ATLAS-CH-BOUNDARYPROBE-001` — count 3; no architecture-status direct consumer.
5. `ATLAS-CH-DATA-001` — count 3; direct consumer `ATLAS-CH-CURRICULUM-001`.
6. `ATLAS-CH-LOCALGLOBAL-001` — count 3; no architecture-status direct consumer.
7. `ATLAS-CH-RESEARCHSM-001` — count 3; direct consumer `ATLAS-CH-GOVADAPT-001`.
8. `ATLAS-CH-SPLIT-001` — count 3; direct consumers `ATLAS-CH-COMPOSE-001`, `ATLAS-CH-TRANSPORT-001`.
9. `ATLAS-CH-KRYLOV-001` — count 2; direct consumers `ATLAS-CH-ATTNAPPROX-001`, `ATLAS-CH-NEURALKRYLOV-001`.

## 5. Immediately preceding completed tranches

### FORMAL-001 — Formal Methods and Machine-Checkable Claims

- implementation PR: #107;
- implementation merge:
  `ea4b586d2b2c4a2e664345613ec7300c5e18ffda`;
- audit:
  `AUDIT-025`;
- audit PR: #108;
- audit merge / current main:
  `f94a18010d969f80ddb96663bec02e449f4eb5eb`;
- duplicate audit issue #109 was closed as duplicate after a connector retry partially succeeded.

Central formal-support object set:

`F=(R,S,M,P,K,I,W)`

for requirement, formal specification, model/semantics, checked support object, checker/kernel, implementation, and deployed world.

Typed support relations:

- `Formalizes(S,R)`;
- `Interprets(M,S)`;
- `Checks(K,P,S,M)`;
- `Conforms(I,M)`;
- `AssumptionsHold(W,M)`.

Load-bearing doctrine:

- proof of a formal statement does not automatically prove adequacy of the human requirement;
- a proved model does not automatically imply implementation conformance;
- a machine-checked theorem remains conditional on its logic, axioms, definitions, trust base, and assumptions;
- finite successful tests are not universal proofs without a completeness bridge;
- replayability and formal proof are complementary, non-equivalent support routes;
- theorem checking and institutional certification remain distinct states.

Exact witness:

- specification `x_0=0`, `SpecStep(x)=x+2`, invariant `Even(x)`;
- induction proves every specified reachable state is even;
- implementation tests `0->2->4->6` pass;
- divergent implementation then maps `6->7`, violating both conformance and the invariant.

AUDIT-025 repairs:

- removed a mutable Lean `latest` documentation URL from the load-bearing source/citation chain because it did not satisfy the inherited immutable-identity discipline;
- replaced the misleading linear claim stack with the typed support graph above.

### CONTINUAL-001 — Continual Learning and Forgetting

- implementation PR: #105;
- implementation merge:
  `b726917e1b40d37ce0f0459035ef9b7e07e0fa6b`;
- audit:
  `AUDIT-024`;
- audit PR: #106;
- audit merge / current main:
  `c257c8400a329cb127ac322cf8bfb70d4693b10c`.

Central evaluation object:

- performance-through-time score `R_{i,j}`;
- encountered-context lower triangle for retention/forgetting;
- optional full matrix plus untrained/reference baseline for forward-transfer claims;
- per-context endpoint forgetting
  `F_j=max(0,max_{k=j,...,T-1}R_{k,j}-R_{T,j})`;
- average and worst-context summaries only when scores are commensurate or explicitly normalized.

Mechanism distinctions:

- replay restores earlier evidence to optimization;
- EWC adds a Fisher-weighted local quadratic parameter penalty;
- GEM uses episodic-memory gradients to constrain first-order update directions;
- parameter isolation prevents direct overwrite by changing the writable-capacity/routing contract.

Exact witness:

`L_A(w)=(1/2)(w+1)^2`,
`L_B(w)=(1/2)(w-1)^2`.

Sequential B-only training raises old-task loss from `0` to `2`.

For

`J_lambda=L_B+(lambda/2)(w+1)^2`,

`w_lambda=(1-lambda)/(1+lambda)`.

At `lambda=1`, both task losses are `1/2`.

Equal-weight replay reaches the same point only because the old task loss is exactly the chosen quadratic penalty. Two isolated task-selected parameters reach zero/zero only by adding capacity and routing.

AUDIT-024 repairs:

- bounded forgetting aggregation to `T>=2` and commensurate/normalized cross-context score scales;
- separated lower-triangular retention evaluation from forward-transfer evaluation, which requires future-context scores plus a baseline.

### NETNUM-001 — Networks as Numerical Schemes

- implementation PR: #103;
- implementation merge:
  `e7c0cda1a96f23e78120c02f66511488612a4035`;
- audit:
  `AUDIT-023`;
- audit PR: #104;
- audit merge / current main:
  `8a08c5db5322f027dd9214618f21ed88ce9255c0`.

Central numerical-network interface:

- residual map `x_{k+1}=x_k+F_k(x_k)`;
- declared continuous reference `dx/dt=f(t,x)`;
- Euler bridge `F_k(x)=h_k f(t_k,x)`;
- local defect relative to exact flow;
- global error over a declared refinement family;
- forward numerical stability separated from training/optimization stability;
- residual scale separated from numerical step size;
- invertibility separated from computational reconstruction and time reversibility.

Exact witness:

for `x'=-x`, explicit Euler gives `x_{k+1}=(1-h)x_k`.

- non-growth interval: `0<=h<=2`;
- strict-decay interval: `0<h<2`;
- `h=3` gives unstable factor `-2`;
- at `T=1`, `N=2,4,8` give exact rational values `1/4`, `81/256`, and `5764801/16777216`;
- at `h=1/2`, the forward map is invertible but forward-plus-negative-step Euler returns only `3/4`, not the identity.

AUDIT-023 repair:

the scalar stability wording was tightened to preserve the NUMERICS-001 distinction between closed non-growth and strict asymptotic decay. No numerical result changed.

### EXPLORE-001 — Exploration and Information Value

- implementation PR: #101;
- implementation merge:
  `2de8b7b6fd30f47e066eb475bbd282583926b681`;
- audit:
  `AUDIT-022`;
- audit PR: #102;
- audit merge / current main:
  `58da49a2f2969de687cbfd247e488997e57b05d6`.

Central Bayesian exploration structure:

- latent parameter `Theta`;
- belief `b_t(theta)`;
- observation law `p(y|theta,a)`;
- immediate reward `r(theta,a,y)`;
- constrained action set `C_t(b)`;
- finite-horizon Bayes value `V_t(b)`;
- information gain `IG_b(a)=I_b(Theta;Y|a)`;
- one-step value of information `VoI_b(a)`.

Load-bearing doctrine:

- exploration is purposeful information acquisition, not random action;
- epistemic uncertainty is distinct from outcome stochasticity;
- information gain is distinct from decision value;
- an action can have lower immediate expected reward and higher total finite-horizon value;
- UCB/optimism, posterior sampling, and information-directed sampling are distinct mechanisms;
- bandit feedback is a strict simplification of general MDP exploration;
- safe/constrained exploration requires an explicit constraint and guarantee semantics.

Exact witness:

a two-step Bayesian bandit with prior `P(theta=1)=2/5` gives:

- known-first total value `1`;
- informative-action-first total value `11/10`;
- immediate exploration cost `1/10`;
- future value of information `1/5`;
- net advantage `1/10`.

AUDIT-022 repairs:

- made the one-step reward notation consistent by introducing expected payoff `bar r`;
- repaired one malformed notation delimiter;
- narrowed the Moldovan–Abbeel description to the source-supported ergodicity-based safety formulation.

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

## 7. Next tranche — REGRET-001

Stable ID:

`ATLAS-CH-REGRET-001`

Title:

**Regret**

Declared hard dependency in the Atlas Map/Ledger:

- `ATLAS-CH-EXPLORE-001`.

The chapter contract in the Atlas Map is:

> Develop Bayesian and minimax regret and clarify what regret controls do and do not imply.

The next session should instantiate this tranche from current main only if the controller remains `idle-ready` and main still equals the recorded baseline.

The audited Exploration and Information Value prerequisite may supply:

- stochastic-bandit notation;
- exploration/exploitation distinction;
- immediate versus continuation value;
- representative optimism, posterior-sampling, and information-directed mechanisms;
- the distinction between information gain and decision value.

A sound intellectual spine should distinguish at least:

1. realized regret from expected regret;
2. pseudo-regret from pathwise/realized regret where source conventions require the distinction;
3. Bayesian regret from minimax/frequentist regret;
4. comparator class and horizon as part of every regret statement;
5. cumulative regret from simple/final recommendation error;
6. sublinear regret from zero regret or pointwise dominance;
7. regret guarantees from safety, calibration, fairness, robustness, or option preservation;
8. worst-case minimax guarantees from prior-weighted Bayesian performance.

A useful exact witness should use a tiny finite bandit/decision family where the same policy has different realized regret on different outcome sequences while expected/pseudo-regret remains a separate quantity, and where changing the comparator changes the numerical regret. The witness must not import the downstream Optionality chapter as authority.

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
