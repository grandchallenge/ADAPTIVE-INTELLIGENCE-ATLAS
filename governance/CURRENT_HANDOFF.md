# CURRENT HANDOFF — Adaptive Intelligence Atlas

**Date:** 2026-10-06
**Recovery authority:** governance/ACTIVE_TRANSACTION.yaml on state/atlas-controller
**Current main:** c9d5c61bf611327a1ed054206c5d8e778559e28a

## Restart rule

1. Read ACTIVE_TRANSACTION.yaml first.
2. Read this handoff.
3. Fetch live main.
4. If live main differs from the recorded baseline, recompute the frontier from governance/CHAPTER_LEDGER.yaml.
5. Repository state overrides chat history.

## Current state

- state: idle-ready
- next target: ATLAS-CH-NEURALKRYLOV-001 — **Neural Krylov Transport**
- downstream architecture count: 0
- direct consumers: none currently in architecture state

Atlas contract:

> Explore short-horizon preconditioned iterative solves as representation computation, without inheriting classical Krylov convergence merely by analogy.

## Hard prerequisites on exact current main

### ATLAS-CH-KRYLOV-001

- manuscript: 59e169723ca068bef817e7bc9e28727d03b45f6a
- source lock: adbe97c750ed79d09462a5e867e5beb772ad72e2
- AUDIT-039: 03660b0dbd1d0604e943d0d09c7b52c6605b256c

Inherited boundary:

- operator-generated Krylov spaces, Arnoldi/Lanczos projected structure, Galerkin/minimum-residual distinctions, residual/error conditioning boundaries, and preconditioning semantics may be inherited;
- matrix-vector access can be sufficient without explicit dense matrix formation;
- residual and true error are distinct and linked through operator/conditioning assumptions;
- exact-arithmetic orthogonality does not automatically survive finite precision;
- convergence can depend on spectrum, field of values, non-normality, right-hand side, preconditioner, and polynomial approximation structure;
- classical Krylov identities do not by themselves establish correctness or convergence of learned nonlinear Neural Krylov mechanisms.

### ATLAS-CH-TRANSPORT-001

- manuscript: 0a81b39a457384f7a265bbac2955ea282217bc3f
- source lock: 55fcd80bc3d94e3b270ddcf28873242ba21f823f
- AUDIT-053: 060d0b9dc320cd16fdcfe10b87484a3bbfda4c75

Inherited boundary:

- representation transport is an exact finite composition of declared state maps;
- state transport, tangent/vector transport, parallel transport, and optimal transport are distinct objects;
- residual stages are exact discrete maps and are not automatically exact ODE flows;
- local Jacobians are local differential objects, not the global nonlinear map;
- constraint preservation does not imply information preservation, stability, invertibility, or task quality;
- shared versus stage-dependent transport maps must remain distinct;
- TRANSPORT explicitly hands NEURALKRYLOV declared transport maps, state/base-point semantics, constrained retraction witnesses, local linearization objects, and shared/stage-dependent semantics;
- representation transport does not imply a Krylov convergence guarantee.

## Before drafting NEURALKRYLOV

1. bind the exact audited KRYLOV and TRANSPORT triples above;
2. source-lock only primary references genuinely needed for learned/preconditioned iterative representation computation beyond those prerequisites;
3. declare the operator on which any Krylov space is built — e.g. a local Jacobian, normal-equation operator, Hessian-like map, or learned linear surrogate — and do not leave it implicit;
4. define at least one exact finite witness where a short Krylov subspace recovers a declared component/solve more accurately than a one-step baseline under fixed operator access;
5. include a failure/control case showing that low subspace dimension alone does not guarantee convergence or task improvement;
6. state the preconditioner and whether it is fixed, learned, state-dependent, left/right, or nonlinear;
7. distinguish exact linear Krylov identities from learned nonlinear transport architectures;
8. keep residual norm, true state/solution error, representation quality, and downstream task quality as separate metrics;
9. keep local Jacobian-based iteration distinct from global nonlinear dynamics unless an explicit bridge is proved;
10. include finite-precision/restart boundaries if the construction depends on orthogonality or accumulated directions.

## Immediately completed transaction — MINCURR-001

- implementation issue: #251 — closed completed
- implementation PR: #252
- exact green implementation head: 1a1974edd3b077c6ef37503b6c6f21237f8e952c
- implementation GitHub Actions run: 37544743541 — success
- implementation merge: f4ef49601bf2c306918f75a2e0abfc242379935e
- post-draft audit: AUDIT-063
- audit issue: #253 — closed completed
- audit PR: #254
- exact green audit head: 9d01bcfc92e81d9ec9062572b952e2303e56aa3d
- audit GitHub Actions run: 37545076163 — success
- audit merge/current main: c9d5c61bf611327a1ed054206c5d8e778559e28a
- audit record blob: edd7724b560249e17f732b2c47aa2e789c2fd067
- audit disposition: **PASS — NO REPAIR**
- final canonical Linux validation on current main: green

Final MINCURR artifacts:

- specification: a90bf935ef124bc9a748123d2ba67474049a5314
- derivation packet: b49724dba87f9cf58a59ac611b781665b57dbc95
- computational witness: 8d7142ed8f457a7a8647904b6e4c8e04e4b20ed7
- reader manuscript: 01a5491100430fe8bf56793e6e1b557ba91dc652
- source lock: e7cb725448a35b31fa879528dc01b02a72d052ca
- bibliography: c95dbd1d1e3ddd0e3b99e067ce3dd654bf8201da
- Chapter Ledger: a8d40ef1f4144def1c6e5cbd363d9837186b50f0
- Source Register: 2b4ba80c4d8ccbf68804ab54b99b926204a387d5
- transaction receipt: 90a8635137ed5fd761387c93faa780fbf95b4459

Durable MINCURR substrate:

- for H={h00,h01,h10,h11} over q1,q2 with target h11, T*={(q1,1),(q2,1)} uniquely identifies the target;
- every strict smaller target-consistent subset leaves version-space size greater than one;
- exact minimum teaching-set size is 2 for the declared concept class/example language/reconstructor;
- auxiliary e3 outside the target probe family has the highest frozen progress score but leaves V_H({e3})=H;
- therefore highest current learning progress does not imply membership in a minimal reconstructive basis;
- minimality is relative to target/capability class, admissible examples, learner/reconstructor, and side information;
- minimal set does not imply unique optimal sequence;
- acquisition, persistence, accessibility, and behavioural expression are separate evidence levels;
- later behavioural success does not prove persistence or causality of a particular early mechanism.

## Recomputed dependency-legal frontier

Every remaining dependency-legal architecture chapter has downstream architecture count 0.

Deterministic ID ordering selects:

- ATLAS-CH-NEURALKRYLOV-001

Other dependency-legal count-0 chapters remain:

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
