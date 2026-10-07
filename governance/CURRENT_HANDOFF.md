# CURRENT HANDOFF — Adaptive Intelligence Atlas

**Date:** 2026-10-06
**Recovery authority:** governance/ACTIVE_TRANSACTION.yaml on state/atlas-controller
**Current main:** 7d2da2ceb970bbba7c43a387ce2ce74f8035e8cf

## Restart rule

1. Read ACTIVE_TRANSACTION.yaml first.
2. Read this handoff.
3. Fetch live main.
4. If live main differs from the recorded baseline, recompute the frontier from governance/CHAPTER_LEDGER.yaml.
5. Repository state overrides chat history.

## Current state

- state: idle-ready
- next target: ATLAS-CH-SPECTRALDIAG-001 — **Spectral and Operator Diagnostics**
- downstream architecture count: 0
- direct consumers: none currently in architecture state

Atlas contract:

> Develop singular spectra, Jacobian/Hessian spectra, pseudospectra, Koopman views, relative-position diagnostics, spectral drift, and transition-local signatures without assuming a universal scalar diagnostic.

## Hard prerequisites on exact current main

### ATLAS-CH-NONNORMAL-001

- manuscript: a8b4cde747df1a986eeca1439203b08512a1471c
- source lock: f8c868af0fc35b73d9acadbdf6d952b03c1d89e9
- AUDIT-001: f13b7ac01f7b10dfadd64da6f31c45832344c082

Inherited boundary:

- eigenvalues alone need not control finite-horizon behavior for non-normal operators;
- transient norm growth, resolvent growth, pseudospectra, and eigenvalue sensitivity are distinct but related diagnostics;
- exact finite-dimensional non-normal witnesses and pseudospectral definitions may be inherited;
- a spectral or pseudospectral signature is descriptive evidence, not automatically a mechanistic or functional explanation.

### ATLAS-CH-MECHDIAG-001

Ledger-selected manuscript:
- manuscript: 4682d5b4abc77c40aa27fd5144d6909250add86f
- source lock: 94362bbe21c5f7f29123e461cc749e617bc117c7
- AUDIT-047: 960e75262c69c0fdb24cc3d33813b250879f25eb

AUDIT-047 additionally binds:
- mature reader companion `ATLAS-CH-DIAGREAD-001.md`: 8275d106f3960eb21e385b3d9130b3cb7686fec0
- source-scope packet `AUDIT-047-SOURCES.yaml`: fe3a99a8a162dc2d364ff2db2674d737a1fdeb20

Inherited boundary:

- readability and functional necessity are different;
- probes, ablations, interventions, substitution, recovery, and diagnostic bookkeeping must be typed separately;
- redundant coordinates can defeat one-component necessity tests;
- the diagnostic record and exact finite witness may be inherited;
- any proposed spectral signature still requires its own functional evidence.

## Before drafting SPECTRALDIAG

1. bind the exact NONNORMAL and MECHDIAG packets above, including the AUDIT-047 mature reader and source-scope packet;
2. source-lock only the minimum primary references genuinely needed for singular/Jacobian/Hessian spectra, pseudospectra, Koopman/operator views, relative-position diagnostics, spectral drift, or transition-local signatures;
3. declare the exact operator, matrix, Jacobian, Hessian, transition map, or empirical object whose spectrum is being measured;
4. distinguish eigenvalues, singular values, pseudospectra/resolvent diagnostics, and local linearizations rather than collapsing them into one spectral scalar;
5. distinguish global spectra from transition-local signatures and state the reference state/time/window for every local object;
6. include exact finite controls showing why equal eigenvalue or singular-value summaries need not imply equal transient dynamics or functional mechanism;
7. pair any claimed mechanistic significance with an intervention, ablation, substitution, recovery, or other functional test rather than spectral correlation alone;
8. keep descriptive diagnostic quality, predictive utility, functional necessity, and causal mechanism as separate epistemic claims;
9. state finite-precision, estimation, sampling, and conditioning limits for empirical spectra;
10. do not infer a universal scalar diagnostic from successful behavior in one operator family or transition regime.

## Immediately completed transaction — SHIFT-001

- implementation issue: #263 — closed completed
- implementation PR: #264
- exact green implementation head: 98eeee1ed12d9ed513617ce33ee96d663f6706a5
- implementation GitHub Actions run: 37551352063 — success
- implementation merge: af551d732d83c6751051c864206df4bb153e5a3f
- post-draft audit: AUDIT-066
- audit issue: #265 — closed completed
- audit PR: #266
- exact green audit head: 67d4d56b7974225434bdc7f0211488cb4f8e8026
- audit GitHub Actions run: 37551682501 — success
- audit merge/current main: 7d2da2ceb970bbba7c43a387ce2ce74f8035e8cf
- audit record blob: 3077637aae2f87e6230bc30a2ea4e24af6aedb3a
- audit disposition: **PASS — NO REPAIR**
- final canonical Linux validation on current main: green

Final SHIFT artifacts:

- specification: b0d7a0a85e56c065b8977ba523b75601366ffc6f
- derivation packet: b12d6ef827f8095c8599c7dcc610e223ae2c769d
- computational witness: 4bf2a0b95d8e1ade101b00c9aa15afb4ee1dd77b
- reader manuscript: 064b7f05068eb212eacbb64228e51b6069d2728f
- source lock: 5c96c8b3efc459308db680dada19ebc767209634
- bibliography: ed8976909306cde1ef6a92de5383c1cd61600484
- Chapter Ledger: 94ae4b045410a8fe1e2dce84d160b78a0f163629
- Source Register: 540d7ff9a0e0e2668ca5444a4a42456b22c94d4a
- transaction receipt: 62a0f5405b0837b1a199d968b0d7a6308f5fefe9

Durable SHIFT substrate:

- source law P and deployment law Q are different objects unless a bridge is proved;
- covariate shift and conditional/concept shift are distinct;
- under covariate shift with Q_X absolutely continuous with respect to P_X, target risk can be represented by source importance weighting;
- ordinary density-ratio correction fails on target-only support without additional assumptions;
- exact calibration witness: unchanged score 1/2 is calibrated under P_X=(1/2,1/2) but has deployment calibration gap 1/4 under Q_X=(3/4,1/4), while Brier risk remains 1/4 under both laws;
- exact importance weights in that witness are 3/2 and 1/2;
- benign marginal-shift control has TV distance 2/5 but source and target 0/1 risk both zero;
- conditional-shift control has unchanged X-marginal, density ratio one, and target risk one for the source-perfect predictor;
- clean risk zero can coexist with adversarial risk one under a declared perturbation set;
- average-case deployment-law risk and worst-case adversarial risk are different objects;
- calibration, coverage, selective risk, predictive risk, adversarial risk, and structural sensitivity remain separate metrics;
- changed predictive statistics do not by themselves identify a structural cause.

## Recomputed dependency-legal frontier

Every remaining dependency-legal architecture chapter has downstream architecture count 0.

Deterministic ID ordering selects:

- ATLAS-CH-SPECTRALDIAG-001

Other dependency-legal count-0 chapters remain:

- ATLAS-CH-SPECTRALSHAPE-001
- ATLAS-CH-SYNTHESIS-001
- ATLAS-CH-SYSTEMS-001
- ATLAS-CH-TOKENCOMP-001
- ATLAS-CH-VARIOPT-001

## Legitimate stop conditions

- genuine external blocker;
- failed validation requiring human judgment;
- explicit human governance gate.
