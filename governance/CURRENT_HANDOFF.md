# CURRENT HANDOFF — Adaptive Intelligence Atlas

**Date:** 2026-10-06
**Recovery authority:** governance/ACTIVE_TRANSACTION.yaml on state/atlas-controller
**Current main:** 21597e4f2bb7af5312dc9967417a60dc3d8dc0f5

## Restart rule

1. Read ACTIVE_TRANSACTION.yaml first.
2. Read this handoff.
3. Fetch live main.
4. If live main differs from the recorded baseline, recompute the frontier from governance/CHAPTER_LEDGER.yaml.
5. Repository state overrides chat history.

## Current state

- state: idle-ready
- next target: ATLAS-CH-COMPINTEL-001 — **Compression as Discovery and Intelligence Probe**
- downstream architecture count: 0
- direct consumers: none currently in architecture state

Atlas contract:

> Examine compression as discovery of reusable computation and as an empirical probe of predictive structure.

Hard prerequisites on exact current main:

### ATLAS-CH-COMPRESS-001

- manuscript: e8db79df51b64cfd4d5ef6957d4d10313886b6f4
- source lock: 156cd6afe1a06b49d2761b54d32b586fe5d23cec
- AUDIT-042: 677efa90a2d606c0400b8e471465278d19857393

Inherited boundary:

- every compression claim must declare the object, code or representation, approximation mechanism, and tolerated distortion;
- description length is not interchangeable with parameter count;
- exact factorization, low-rank approximation, pruning, quantization/weight sharing, and distillation are different mechanisms;
- compression ratio must be paired with retained behavior;
- COMPINTEL must independently justify any claim that compression reveals reusable computation, mechanism, abstraction, intelligence, or discovery.

### ATLAS-CH-RESIDUAL-001

- manuscript: 02b0886a87e1e17c749e15349e14f43674c3d1ff
- source lock: 6e6a25c4b4e01475e68a6c616eefb6ba7b039341
- AUDIT-006: b24ef782bedfe76a4c52d832562a0dd29d2a64a9

Inherited boundary:

- a Residual is capability/task-relative, not a universal coordinate object;
- invariance alone is insufficient: reconstructive capability sufficiency is separately required;
- leastness is relative to declared descriptor and admissible post-processing classes;
- semantic factorization and operational/computable factorization remain distinct;
- existence, uniqueness, finite dimensionality, and efficient learnability are not assumed.

Before drafting COMPINTEL, bind these exact audited prerequisites and source-lock the minimum primary references needed for claims connecting compression to reusable computation, predictive structure, discovery, or intelligence. Define a falsifiable probe: what observable compression result would count as evidence for reusable structure, and what controls would show that the effect is merely codec choice, regularization, memorization, or task-specific distortion.

## Immediately completed transaction — ATTNAPPROX-001

- implementation issue: #223 — closed completed
- implementation PR: #224
- exact green implementation head: 35844412e9189172fb8d7262c644ea34aecdee08
- implementation GitHub Actions run: 37461213741 — success
- implementation merge: 8c5ad59ccacb3991e1ec7646be057a72b8bec495
- post-draft audit: AUDIT-056
- audit issue: #225 — closed completed
- audit PR: #226
- exact green audit head: 5a06ba97b0d803abbea0ed84113f4b39fc0675a8
- audit GitHub Actions run: 37461795337 — success
- audit merge/current main: 21597e4f2bb7af5312dc9967417a60dc3d8dc0f5
- audit record blob: aec970752de5de74b1bfb49846ea94d203defc3f
- audit disposition: **PASS — NO REPAIR**
- final canonical Linux validation on current main: green

Final ATTNAPPROX artifacts:

- specification: 38ae190a4d303d5bfdbfc9726777f8942f4fb519
- derivation packet: c84aa9479debc0d8f014c8edde2e914f5941376a
- computational witness: 0952f80e270c77753bbfe92573ae821a220017f3
- reader manuscript: 25a040be85328d76e4b09eb3495fd9127082173d
- source lock: f9bc3fa255ba95785d86f43433b728109e93d16c
- Chapter Ledger: e236a12fb5979d8db2a16ea9f6218a6a4f5f2fb8
- Source Register: 033a20f617449c0c939191c6a2f08185df650187
- bibliography: f3cfe2393979d88a6c6262f656ee7e1cd61d0665
- transaction receipt: b07b5b7e649a75297dadf84e9206e83c09e0ed95

Durable ATTNAPPROX substrate:

- score, exponential-kernel, normalized-operator, fixed-value output, and alternative-normalization targets are distinct;
- approximation claims must name both target and error notion;
- positive row scaling of the exponential kernel leaves the normalized softmax operator exactly unchanged;
- raw kernel error therefore need not track normalized-operator error;
- kernel perturbation requires denominator control before promotion to an operator-error statement;
- for fixed V, ||(Ahat-A)V||_F <= ||Ahat-A||_2 ||V||_F, while one output witness does not identify the full operator;
- positive Gaussian random features give an expectation identity for the exponential dot-product kernel, but finite-feature error and FAVOR+ guarantees remain source/assumption scoped;
- FAVOR+ random features, Linformer-style low-rank projection, Nyström/landmark reconstruction, and alpha-entmax sparse normalization are different mechanisms;
- alpha-entmax is an alternative score-to-simplex family, not automatically a softmax estimator;
- sparsity does not imply low rank, low rank does not imply sparsity, and exact zeros do not by themselves imply subquadratic execution;
- feature/rank/landmark/support budgets must remain explicit in complexity claims;
- mask, position, conditioning, and finite precision belong inside the approximation contract;
- classical Krylov convergence guarantees do not transfer to structured or learned attention by analogy.

Exact rank-reduction witness:

- A is positive, row-stochastic, rank 2;
- Ahat is positive, row-stochastic, rank 1;
- ||A-Ahat||_F^2 = 4/27;
- ||A-Ahat||_2 = 2 sqrt(3) / 9;
- for the declared V, ||(A-Ahat)V||_F^2 = 2/27.

Exact sparse-alternative witness:

- for s=(2,0,-1), softmax is strictly positive in all coordinates;
- alpha=2 entmax/sparsemax equals (1,0,0).

## Recomputed dependency-legal frontier

Every remaining dependency-legal architecture chapter has downstream architecture count 0.

Deterministic ID ordering therefore selects:

- ATLAS-CH-COMPINTEL-001

Other dependency-legal count-0 chapters remain available:

- ATLAS-CH-COMPOSE-001
- ATLAS-CH-CONTEXTCOMP-001
- ATLAS-CH-CPS-001
- ATLAS-CH-JOINTUNC-001
- ATLAS-CH-LATENTTIME-001
- ATLAS-CH-MINCURR-001
- ATLAS-CH-NEURALKRYLOV-001
- ATLAS-CH-REGRETROUTE-001
- ATLAS-CH-SHIFT-001
- ATLAS-CH-SPECTRALDIAG-001
- ATLAS-CH-SPECTRALSHAPE-001
- ATLAS-CH-SYNTHESIS-001
- ATLAS-CH-SYSTEMS-001
- ATLAS-CH-TOKENCOMP-001
- ATLAS-CH-VARIOPT-001

## Legitimate stop conditions

- genuine external blocker;
- failed validation requiring human judgment;
- explicit human governance gate.
