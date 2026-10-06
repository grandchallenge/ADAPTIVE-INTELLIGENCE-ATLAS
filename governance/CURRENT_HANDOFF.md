# CURRENT HANDOFF — Adaptive Intelligence Atlas

**Date:** 2026-10-06
**Recovery authority:** governance/ACTIVE_TRANSACTION.yaml on state/atlas-controller
**Current main:** 01e72c6c33a411d83f10913d7e8db0dd5305dfbd

## Restart rule

1. Read ACTIVE_TRANSACTION.yaml first.
2. Read this handoff.
3. Fetch live main.
4. If live main differs from the recorded baseline, recompute the frontier from governance/CHAPTER_LEDGER.yaml.
5. Repository state overrides chat history.

## Current state

- state: idle-ready
- next target: ATLAS-CH-ATTNAPPROX-001 — **Approximate and Structured Attention**
- downstream architecture count: 0
- direct consumers: none currently in architecture state

Atlas contract:

> Study FAVOR+, random features, structured projections, entmax, sparsity, and approximation tradeoffs.

Hard prerequisites on exact current main:

### ATLAS-CH-ATTNOP-001

- manuscript: d6fa97fbbd1a2410055ca2cd4bc034ca54ccd26c
- source lock: 4af4e53230776daaf0be825cffd1263957ed97c8
- AUDIT-002: 4671995f0cd7465a5df2bb60431244f482e5e3c9

Inherited boundary:

- attention score matrix, normalized mixing operator, value field, and full state-dependent map remain distinct;
- kernel or linear-attention interpretations are source-scoped and do not make the full attention map linear in the input;
- masking, positional structure, and normalization assumptions must remain explicit.

### ATLAS-CH-KRYLOV-001

- manuscript: 59e169723ca068bef817e7bc9e28727d03b45f6a
- source lock: adbe97c750ed79d09462a5e867e5beb772ad72e2
- AUDIT-039: 03660b0dbd1d0604e943d0d09c7b52c6605b256c

Inherited boundary:

- operator-generated Krylov subspaces, random-feature approximations, and low-rank attention approximations are different constructions;
- small residual and low-dimensional approximation do not automatically imply small solution or operator error;
- classical iterative-subspace convergence guarantees do not transfer to learned/state-dependent attention by analogy.

Before drafting ATTNAPPROX, bind these exact audited prerequisites and source-lock the minimum primary references needed for FAVOR+/Performer-style random-feature attention, structured/low-rank approximations, and sparse alternatives such as entmax. Define the approximation target and error notion before comparing methods.

## Immediately completed transaction — ADAPTDEPTH-001

- implementation issue: #219
- implementation PR: #220
- exact green implementation head: 43ec942015e5e6ce0f7e50875500117f880e2c48
- implementation merge: e4ead968c9c38bc4c99f40ef154437adbfe58200
- post-draft audit: AUDIT-055
- audit issue: #221
- audit PR: #222
- exact green audit head: 1e667e080fa6d878bd863607eaa4db0733a41ead
- audit merge/current main: 01e72c6c33a411d83f10913d7e8db0dd5305dfbd
- audit record blob: 6464d6f2ff5e101e6d9eed242f7c815fd33a34a0
- audit disposition: **PASS — NO REPAIR**
- final GitHub Actions validation on current main: green
- final canonical Linux validation on current main: green

Final ADAPTDEPTH artifacts:

- specification: 00cd2477035b9d106a8b16157e03520d1652e67e
- derivation packet: cd67d0d4fb987ddbc6cbe4c25192f593f8a7007c
- computational witness: 6d4240764b3e7be447f436d330ca4b88174ac22f
- reader manuscript: 61d47ce36a825effb75c246501ca8b66f446261e
- source lock: 717bbe901d7bc4514919f70bd65a1712e6d3aae7
- Chapter Ledger: 487fb507262ca9520d37e42397c3dc52f375ac6b
- Source Register: 4b5b06e0c702eaa79eb7a0771b15ab10a860762b
- bibliography: 7a7a89bc7c3789e0865755e446ee41d7d95815f2

Durable ADAPTDEPTH substrate:

- adaptive execution depth, numerical step size, local error estimate, and learned halting score are separate objects;
- embedded-pair differences can support method-specific local error estimation under declared assumptions;
- the exact Euler/Heun witness on y'=t has pair difference h^2/2 equal to Euler one-step error;
- with tolerance 1/8, h=1 is rejected and the idealized p=1 controller maps to h=1/2, where the estimator equals 1/8;
- local error acceptance does not by itself prove a global error bound;
- a learned halting score can perfectly rank true error while being badly miscalibrated in magnitude;
- error control requires an explicit score/estimator-to-target-error relation;
- expected calibration is weaker than a per-instance certified upper bound;
- budget exhaustion remains distinct from criterion satisfaction;
- adaptive depth is not adaptive numerical time stepping unless a reference dynamics/discretization is declared;
- error control is distinct from compute optimality.

Exact learned-halting witness:

- true error E_k = 2^(1-k);
- score q_k = 4^(-k) = E_k^2/4;
- at k=2, q_2=1/16 while E_2=1/2;
- the exact inverse is E_k=2*sqrt(q_k);
- for target E<=1/16, the correct score threshold is q<=1/1024, first met at k=5.

## Recomputed dependency-legal frontier

Every remaining dependency-legal architecture chapter has downstream architecture count 0.

Deterministic ID ordering therefore selects:

- ATLAS-CH-ATTNAPPROX-001

Other dependency-legal count-0 chapters remain available, including COMPINTEL, COMPOSE, CONTEXTCOMP, CPS, JOINTUNC, LATENTTIME, MINCURR, NEURALKRYLOV, REGRETROUTE, SHIFT, SPECTRALDIAG, SPECTRALSHAPE, SYNTHESIS, SYSTEMS, TOKENCOMP, and VARIOPT.

## Legitimate stop conditions

- genuine external blocker;
- failed validation requiring human judgment;
- explicit human governance gate.
