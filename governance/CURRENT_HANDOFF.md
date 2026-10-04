# CURRENT HANDOFF — Adaptive Intelligence Atlas

**Handoff date:** 2026-10-03  
**Repository:** `grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS`  
**Controller branch:** `state/atlas-controller`  
**Recovery authority:** `governance/ACTIVE_TRANSACTION.yaml`  
**Current main:** `ed3f07a2531c520e0fad43f072340f8099448098`

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
- baseline/main: `ed3f07a2531c520e0fad43f072340f8099448098`;
- next target: `ATLAS-CH-LOCALGLOBAL-001`;
- title: **Local-to-Global Mathematics**;
- reason: it ties for the largest unlocked downstream architecture cone at 3 nodes and is first under deterministic frontier ordering.

Current frontier, recomputed from the live Chapter Ledger after AUDIT-031:

1. `ATLAS-CH-LOCALGLOBAL-001` — downstream architecture count 3.
2. `ATLAS-CH-MOE-001` — count 3; direct consumers `ATLAS-CH-ROUTERDYN-001`, `ATLAS-CH-SYSTEMS-001`.
3. `ATLAS-CH-OPTIONALITY-001` — count 3; direct consumer `ATLAS-CH-GOVADAPT-001`.
4. `ATLAS-CH-RESEARCHSM-001` — count 3; direct consumer `ATLAS-CH-GOVADAPT-001`.
5. `ATLAS-CH-SPLIT-001` — count 3; direct consumers `ATLAS-CH-COMPOSE-001`, `ATLAS-CH-TRANSPORT-001`.
6. `ATLAS-CH-CURRICULUM-001` — count 2; direct consumer `ATLAS-CH-PROGRESSSEARCH-001`.
7. `ATLAS-CH-KRYLOV-001` — count 2; direct consumers `ATLAS-CH-ATTNAPPROX-001`, `ATLAS-CH-NEURALKRYLOV-001`.
8. `ATLAS-CH-POSGEOM-001` — count 2; direct consumer `ATLAS-CH-RPO-001`.

## 5. Immediately preceding completed tranches

### EXTMEM-001 — The External-Memory Thesis

- implementation PR: #122;
- implementation merge: `c775a398062736c372f13f65dd2bb7349c2796c7`;
- audit: `AUDIT-031`;
- audit issue: #123;
- audit PR: #124;
- audit merge / current main: `ed3f07a2531c520e0fad43f072340f8099448098`.

Central placement descriptor:

`Place(k)=(V,P,S,D,R,L,H,A,G)`

for volatility, provenance/audit need, sharing scope, deletion/supersession need, retrievability, latency, availability/failure tolerance, access control/privacy, and value of parametric generalization/compression.

Load-bearing distinctions:

- parametric knowledge versus explicit external records;
- external locus versus persistent lifetime;
- storage correctness versus retrieval/use correctness;
- record-local update versus systems cost;
- provenance visibility versus factual correctness;
- authoritative update versus consumer freshness;
- shared store versus synchronized effective memory;
- externalization versus later consolidation into parameters.

Exact witness:

- initial parametric state `theta=(1,1)` represents `A=2,B=0`;
- updating only A to 4 while preserving B requires `theta'=(2,2)`;
- naive one-coordinate edit `(2,1)` yields `A=3,B=1`;
- versioned external memory marks A/v1 superseded and A/v2 current while B is unchanged;
- latest read returns A=4, while a stale snapshot still returns A=2.

AUDIT-031 repairs:

- split latency and availability/failure tolerance into separate placement coordinates;
- preserved the inherited distinction between external locus and persistent lifetime;
- made the witness's supersession state explicit so only one A version is current.

### DATA-001 — Data Quality, Mixtures, and Contamination

- implementation PR: #119;
- implementation merge: `703e763cac01d224eec87aeeca43d5f1acf9c58c`;
- audit: `AUDIT-030`;
- audit issue: #120;
- audit PR: #121;
- audit merge / current main: `7604f00fe257ade14adf01718bda0b8f9aa8feb9`.

Central data object:

`D=(R,S,P,Phi,Delta,mu,E)`

for records, sources/domains, provenance/lineage, processing pipeline, duplicate/overlap predicates, sampling measure, and evaluation boundary.

Load-bearing distinctions:

- exact duplication versus near duplication versus semantic redundancy;
- raw corpus proportions versus post-filter/dedup proportions versus training sampling weights;
- synthetic provenance versus quality judgment;
- detected overlap versus memorization versus causal benchmark-score effects;
- unweighted item contamination rate versus weighted evaluation measures;
- publication date versus actual pre-cutoff content availability.

Exact witness:

- exact overlap rate `1/3`;
- near-overlap rate `2/3` at token-Jaccard threshold `3/4`;
- raw training count `5`;
- exact-dedup representatives `4`;
- near-duplicate graph clusters `3`;
- raw domain proportions `(2/5,1/5,1/5,1/5)`;
- exact-dedup proportions `(1/4,1/4,1/4,1/4)`;
- declared training weights `(1/2,1/4,1/8,1/8)`.

AUDIT-030 repairs:

- named the chapter's contamination-rate formula as the unweighted item rate and required explicit weights for weighted evaluation;
- required a declared counting unit before corpus/mixture proportions are interpreted;
- repaired the temporal boundary so post-cutoff benchmark publication alone is not treated as proof that the content did not exist earlier.

### BOUNDARYPROBE-001 — Boundary Probes

- implementation PR: #116;
- implementation merge: `a6ef32bbd43347907833b0812cb776162ade01c6`;
- audit: `AUDIT-029`;
- audit issue: #117;
- audit PR: #118;
- audit merge / current main: `53583191c96a9657bbb247d683c25ee9f7bedacf`.

Central probe objects:

- JVP: `J_F(x)v`;
- VJP under the declared Euclidean coordinate convention: `J_F(x)^T w`;
- local Euclidean gain: `sigma_max(J_F(x))`;
- power iteration on `J^T J`;
- boundary-probe contract `B=(F,X,Y,O,U,N_X,N_Y,P,E,tau)`.

Exact witness:

- nonlinear map `F(x1,x2)=(x1^2+x2,x1+2x2)` at `x0=(1,1)`;
- exact Jacobian `[[2,1],[1,2]]`;
- singular values `3,1`;
- JVP `(3,3)`, VJP `(4,5)`, exact pairing value `9`;
- exact nonlinear remainder `(epsilon^2,0)`;
- mixed-start Rayleigh values `365/41`, `29525/3281` approach `9`;
- weak-eigenspace initialization remains at Rayleigh value `1` despite true singular norm `3`.

AUDIT-029 repairs:

- made the Euclidean coordinate/inner-product convention explicit for `J^T w`;
- separated a finite monitoring estimate `hat sigma <= tau` from the stronger true-norm claim `||J||_2 <= tau`;
- aligned the Griewank–Walther bibliography record with the locked second-edition SIAM source identity.

### SPARSE-001 — Conditional Computation

- implementation PR: #114;
- implementation merge: `817cc0267c48235c50024a26f5473e1b4de0f935`;
- audit: `AUDIT-028`;
- audit PR: #115;
- audit merge / current main: `c82f61da1ca457b9670273669c04fe3fd5459652`.

Central sparsity/conditional-computation object:

`S=(P,A,T,B,D,R)`

for parameter sparsity, activation sparsity, token sparsity, block/module sparsity, conditional depth, and routing.

Load-bearing distinctions:

- static sparsity versus input/state-dependent conditional execution;
- hard skipped work versus soft gating;
- router cost versus executed-path cost;
- average versus peak/tail compute;
- total capacity versus active per-input work;
- arithmetic operations versus launches, memory traffic, energy, communication, latency, and throughput;
- training graph versus inference graph;
- efficiency versus task-quality preservation.

Exact witness:

- fixed resource pair `(40,1)`;
- conditional average `(55/2,15/4)`;
- average arithmetic reduction `5/16=31.25%`;
- unchanged peak arithmetic `40`;
- compute-dominated toy cost favors conditional execution;
- launch-dominated toy cost favors fixed execution.

AUDIT-028 repairs:

- aligned the primitive resource vector to `C=(F,K,M,E)`, keeping latency/throughput as hardware-dependent modeled or measured outputs;
- aligned the Roofline manuscript title with the locked CACM source identity.

### RETRIEVAL-001 — Retrieval and Associative Access

- implementation PR: #112;
- implementation merge: `e675cf95bb4a8df788bc96aed0b786b21d9fcb96`;
- audit: `AUDIT-027`;
- audit PR: #113;
- audit merge / current main: `98e146cbd150625ecac4a5f1416da221ec7abff3`.

Central retrieval contract:

`Retr=(D,Q,F,s,pi,k,O)`.

Load-bearing distinctions:

- exact-key, symbolic, sparse, dense/vector, hybrid, and multi-index access remain distinct;
- ranking score is not calibrated relevance probability;
- top-k is an ordered truncation, not a completeness theorem;
- exact nearest-neighbor and ANN semantics remain distinct;
- logical record identity and index-entry identity remain separate;
- retrieval rank does not create provenance or authority;
- retrieval-contract correctness, task relevance, and downstream usefulness are separate evaluation layers.

Exact witness:

- exact-key `id=B` -> B;
- symbolic `year>=2024` -> `{A,C}`;
- vector ranking -> `C,A,B`;
- paper-filter then rank top-1 -> A;
- rank top-1 then paper-filter -> empty.

AUDIT-027 repairs:

- renamed the complete retrieval tuple from `R` to `Retr` to preserve the MEMTAX read-path coordinate;
- made top-k an ordered list with a separate selected-set view.

### REGRET-001 — Regret

- implementation PR: #110;
- implementation merge:
  `915911dfd5b6b6daf7084edd75e2341d7a727d10`;
- audit:
  `AUDIT-026`;
- audit PR: #111;
- audit merge / current main:
  `e1709bc5744a260c0a1eec5234d5ac4cb261b3b7`.

Central regret contract:

- horizon `T`;
- environment `theta` or class `Theta`;
- admissible policy class `Pi`;
- reward/loss convention;
- comparator;
- expectation/prior convention.

Load-bearing distinctions:

- pathwise mean-benchmark regret versus expected/pseudo-regret;
- Bayesian regret versus worst-case/minimax regret;
- fixed versus dynamic comparator classes;
- cumulative regret versus simple/final recommendation regret;
- sublinear cumulative regret versus zero/bounded regret;
- regret guarantees versus safety, fairness, calibration, robustness, tail risk, recoverability, and optionality.

Exact witnesses:

- two-round Bernoulli example: pseudo-regret `1`, while pathwise regret takes `3/2`, `1/2`, or `-1/2` and has expectation `1`;
- one-step two-environment example: minimax policy uses `q=1/2` with regret `1/2`, while prior `9/10,1/10` makes `q=1` Bayes-optimal with Bayes regret `1/10` and worst-case regret `1`;
- one fixed learner trajectory has regret `0` against the best fixed action and `1` against an unrestricted dynamic comparator;
- one exploration sequence has cumulative regret `1` and simple regret `0`.

AUDIT-026 repairs:

- bound Bayesian/minimax optimization to an explicit admissible policy class `Pi`;
- replaced the general comparator-class `max` with `sup`, while preserving the finite witness maximum.

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
- `ATLAS-CH-MEMTAX-001`;
- `ATLAS-CH-RETRIEVAL-001`;
- `ATLAS-CH-CONTINUAL-001`.

Do not treat already-drafted downstream chapters as hidden prerequisite authority unless the Chapter Ledger explicitly declares them as dependencies.

## 7. Next tranche — LOCALGLOBAL-001

Stable ID:

`ATLAS-CH-LOCALGLOBAL-001`

Title:

**Local-to-Global Mathematics**

Declared hard dependency:

- `ATLAS-CH-OBJECTS-001`.

Atlas contract:

> Introduce graphs, sheaves, compatibility, gluing, and compositional viewpoints only to the degree needed later.

The next session should instantiate this tranche from current main only if the controller remains `idle-ready` and main still equals the recorded baseline.

The audited Objects prerequisite may supply the Atlas distinction among states, operators, flows, and interfaces. LOCALGLOBAL-001 should not import later sheaf/composition chapters as hidden authority.

A sound intellectual spine should distinguish at least:

1. a graph/incidence structure from data assigned to its vertices/edges;
2. local observations/sections from restriction maps;
3. pairwise/local compatibility from existence of one global assignment;
4. gluing existence from gluing uniqueness;
5. exact compatibility from approximate/inconsistent data;
6. local interface contracts from global system consistency;
7. sheaf language as a precise local-to-global tool rather than decorative abstraction;
8. graph topology/combinatorics from the algebra carried over it;
9. compositional reuse from naive aggregation;
10. obstruction certificates from successful global reconstruction.

A bounded exact witness should use a tiny finite cover or graph with explicit local values and restriction maps. It should include one compatible family that glues uniquely and one locally plausible family with an explicit compatibility obstruction. The witness should prove only the finite gluing/obstruction statements and avoid implying that every distributed-learning or data-fusion problem is naturally a sheaf.

The chapter should remain elementary enough to support later composition, boundary-contract, and data-fusion arguments without turning Part 2 into a full sheaf-theory text.

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
