# CURRENT HANDOFF — Adaptive Intelligence Atlas

**Date:** 2026-10-06
**Recovery authority:** governance/ACTIVE_TRANSACTION.yaml on state/atlas-controller
**Current main:** e8129376ef673822ed6b43775a0d2439b88c47fb

## Restart rule

1. Read ACTIVE_TRANSACTION.yaml first.
2. Read this handoff.
3. Fetch live main.
4. If live main differs from the recorded baseline, recompute the frontier from governance/CHAPTER_LEDGER.yaml.
5. Repository state overrides chat history.

## Current state

- state: idle-ready
- next target: ATLAS-CH-ADAPTDEPTH-001 — **Adaptive Depth as Error Control**
- downstream architecture count: 0
- direct consumers: none currently in architecture state

Atlas contract:

> Connect learned stopping and adaptive compute to local error estimation and adaptive time stepping.

Hard prerequisites on exact current main:

### ATLAS-CH-DEPTH-001

- manuscript: 9d365778e873217c40604a621dbe9f88ca2153e0
- source lock: b6c18e2e0e3ab82c65d830967e2874bfb41e9bb2
- AUDIT-018: 0c9f5405bd7d94018d76aa93ebe74ec3e505cabe

Inherited boundary:

- computational depth, recurrent/adaptive computation, equilibrium computation, and stopping semantics must remain distinct;
- learned halting or conditional depth does not automatically become a numerical local-error estimator.

### ATLAS-CH-NETNUM-001

- manuscript: cbaf0b96c996c821df50f985075f64028459c587
- source lock: 02bbe77d19da4a6a123e430f8aae058d666c4e35
- AUDIT-023: 746e0c297e4ddf29122d4735108becc33e599030

Inherited boundary:

- residual-network / numerical-scheme analogies require declared reference dynamics and discretization semantics;
- local error, global error, stability, and exact-flow claims remain separate;
- learned or nonlinear transport does not inherit classical numerical convergence guarantees by analogy.

Before drafting ADAPTDEPTH, bind these exact audited prerequisites and source-lock the minimum additional primary references needed for adaptive step-size / local-error control and learned stopping. The chapter must distinguish an actual numerical error estimator from a learned halting signal or compute-allocation policy.

## Immediately completed transaction — UNCERTAINTY-001

- implementation issue: #215
- implementation PR: #216
- exact green implementation head: 845a5e62b7b2e2a40d01683f98954f3ff9dcbc12
- implementation merge: 8dfb5a09bebf4c15d8257bb74d9b3657688b2d8b
- post-draft audit: AUDIT-054
- audit issue: #217
- audit PR: #218
- exact green audit head: e1d9c24d1a96ff2813ef243a3c31d4db5313c547
- audit merge/current main: e8129376ef673822ed6b43775a0d2439b88c47fb
- audit record blob: 132a0df9a603ec88811312d193971100549648a4
- audit disposition: **PASS — NO REPAIR**
- final GitHub Actions validation on current main: green
- final canonical Linux validation on current main: green

Final UNCERTAINTY artifacts:

- specification: efa855b00af94780f08f9267ed6357ec847374c9
- derivation packet: 997cba9eb0c8f48d06c1155c5e17f7db74c964ae
- computational witness: 01f8fff254fb0a458935c716ce07da389a4a33ef
- reader manuscript: e6714d0505a96e2bfdc431b4ec60d50b0044efa6
- source lock: b9f38d496efe2d704b759510cf171d5a3e83a2c8
- Chapter Ledger: 4c854cfd4f7e19db3399d78c95cb90a99a4da9eb
- Source Register: ae7b98bb7b758631c202f004c444180dcfbb5401
- bibliography: afafee05f9fd71932e067e34a061e970c1685f90

Durable UNCERTAINTY substrate:

- calibration is E[Y|S]=S, not confidence magnitude;
- calibration does not imply sharpness, accuracy, or low Brier risk;
- predictive entropy does not identify an aleatoric/epistemic decomposition;
- the aleatoric/epistemic split is model-relative rather than exhaustive;
- MC dropout carries only the cited approximate-Bayesian semantics;
- deep ensembles are empirical predictive-uncertainty methods, not posterior samples by definition;
- conformal prediction supplies marginal coverage under exchangeability/randomness assumptions, not calibration or arbitrary conditional coverage;
- selective prediction trades accepted-population coverage against selective risk;
- in-distribution guarantees do not silently survive distribution shift.

Exact finite witnesses:

- same Bernoulli(1/2) predictive law and one bit of predictive entropy can have either conditional entropy 1 / mutual information 0, or conditional entropy 0 / mutual information 1;
- two calibrated predictors can have Brier risks 0.25 and 0.09;
- split-conformal n=4, alpha=0.2 rank witness gives k=4 and exact no-tie marginal coverage 4/5;
- selective witness changes coverage from 1 to 3/5 while selective risk falls from 2/5 to 0.

## Recomputed dependency-legal frontier

After UNCERTAINTY, every dependency-legal architecture chapter has downstream architecture count 0.

Deterministic ID ordering therefore selects:

- ATLAS-CH-ADAPTDEPTH-001

Newly dependency-legal after UNCERTAINTY:

- ATLAS-CH-SHIFT-001

Other dependency-legal count-0 chapters remain available, including ATTNAPPROX, COMPINTEL, COMPOSE, CONTEXTCOMP, CPS, JOINTUNC, LATENTTIME, MINCURR, NEURALKRYLOV, REGRETROUTE, SPECTRALDIAG, SPECTRALSHAPE, SYNTHESIS, SYSTEMS, TOKENCOMP, and VARIOPT.

## Legitimate stop conditions

- genuine external blocker;
- failed validation requiring human judgment;
- explicit human governance gate.
