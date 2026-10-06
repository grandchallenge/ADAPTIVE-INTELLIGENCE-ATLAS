# CURRENT HANDOFF — Adaptive Intelligence Atlas

**Date:** 2026-10-06
**Recovery authority:** governance/ACTIVE_TRANSACTION.yaml on state/atlas-controller
**Current main:** 506d2642398330a27bc9b6e6c17ec38969b6f6a0

## Restart rule

1. Read ACTIVE_TRANSACTION.yaml first.
2. Read this handoff.
3. Fetch live main.
4. If live main differs from the recorded baseline, recompute the frontier from governance/CHAPTER_LEDGER.yaml.
5. Repository state overrides chat history.

## Current state

- state: idle-ready
- next target: ATLAS-CH-REGRETROUTE-001 — **Routing as Online Decision Making**
- downstream architecture count: 0
- direct consumers: none currently in architecture state

Atlas contract:

> Add the online-decision layer to sparse routing: routing action, comparison policy/class, reward/loss timing, regret, optionality, correction capacity, and nonstationarity assumptions.

## Hard prerequisite on exact current main

### ATLAS-CH-ROUTERDYN-001

- manuscript: 4c3c4b22d7f6a564b255a251ba646d11dbbc29a4
- source lock: 27aca5556b902c679132780e4f74ba8822420762
- AUDIT-050: 19a7e4bf2d0291380b195d2ad7cc0091922bcb8b

Inherited boundary:

- probability, preferred-route, accepted-dispatch, and load dynamics are distinct observables;
- exact route-churn and probability-drift definitions may be inherited;
- empirical expert-transition operators may be inherited;
- taxonomy-relative specialization profiles may be inherited;
- local augmented-state commutator diagnostics may be inherited;
- stable loads do not imply stable token assignments;
- zero preferred-route churn does not imply zero probability drift;
- equal singular spectra do not imply equal routing dynamics;
- nonzero commutator does not identify a causal training mechanism;
- temporal diagnostics are not regret theory.

## Before drafting REGRETROUTE

1. bind the exact audited ROUTERDYN triple above;
2. source-lock only primary online-learning/bandit/regret references genuinely needed beyond ROUTERDYN;
3. define the routing action space and whether actions are preferred routes, accepted dispatch decisions, capacity allocations, or another explicitly declared object;
4. define the comparator class before defining regret;
5. define reward/loss timing and what feedback is observed after each routing action;
6. define optionality and correction capacity operationally rather than metaphorically;
7. state nonstationarity assumptions and whether regret is static, dynamic, shifting, or another declared notion;
8. include an exact finite witness where low churn can coexist with high regret or high churn can coexist with low regret under the declared comparator/loss process;
9. keep load balance, churn, probability drift, specialization, regret, and downstream task loss as separate metrics;
10. keep capacity/overflow mechanics explicit because accepted dispatch can differ from preferred action.

## Immediately completed transaction — NEURALKRYLOV-001

- implementation issue: #255 — closed completed
- implementation PR: #256
- exact green implementation head: ba58e1e990c818e5c45a8007e7a0314fa4cd9d47
- implementation GitHub Actions run: 37547958975 — success
- implementation merge: 0efe3dc8bfd47f268cd2a5f088026e95b3a6c52e
- post-draft audit: AUDIT-064
- audit issue: #257 — closed completed
- audit PR: #258
- exact green audit head: eb5b1d10e72b33e393a15813740738628a97b380
- audit GitHub Actions run: 37548244047 — success
- audit merge/current main: 506d2642398330a27bc9b6e6c17ec38969b6f6a0
- audit record blob: b9e5e8afdb1943dba65f26a605e1fd7da11c9e95
- audit disposition: **PASS — NO REPAIR**
- final canonical Linux validation on current main: green

Final NEURALKRYLOV artifacts:

- specification: 6ac203b25f1155b3eaed4b063af8fa559b69ce2d
- derivation packet: afe1798ce77b74b79478d79553bd72323da8545b
- computational witness: 02e383c1ff0237199be5ac757c4aebdd4cb8e011
- reader manuscript: d2740a2d47c004dc48a0dc97ae0ebbb43d60707b
- source lock: f030acac3c8269ab6c3a4856c1ec53cc75cedee9
- Chapter Ledger: 2149fa3ae83e57fd46391e6b36a0af3931da5af0
- Source Register: 536349056012148899077b9d0d1f0badd18dd684
- transaction receipt: 0c94c9a90987f79960d6b3d89c3ad2316b3de75a

Durable NEURALKRYLOV substrate:

- every Krylov construction must name its linear operator;
- positive witness: A=diag(1,4), b=(1,1), fixed left M=diag(1,2), transformed B=diag(1,2), c=(1,1/2);
- best K1 transformed-residual coefficient is alpha=3/4;
- transformed residual squared is 1/8;
- original residual squared is 5/16;
- true error squared is 5/64;
- K2(B,c)=R^2 because det[c,Bc]=1/2;
- x*=(3/2)c-(1/2)Bc, so K2 admits the exact solve;
- bad one-dimensional control B_bad=diag(1,10), c_bad=(1,1) has minimum residual squared 81/101;
- low trial-space dimension alone is not a convergence certificate;
- downstream readout w=(1,2) is exact at the non-exact one-step solution, so task/readout quality is distinct from solve residual/error;
- local Jacobian/surrogate operator is not the global nonlinear transport map;
- fixed-left, right, flexible, learned, state-dependent, and nonlinear preconditioners require different semantics;
- classical Krylov convergence does not transfer to learned nonlinear transport by analogy.

## Recomputed dependency-legal frontier

Every remaining dependency-legal architecture chapter has downstream architecture count 0.

Deterministic ID ordering selects:

- ATLAS-CH-REGRETROUTE-001

Other dependency-legal count-0 chapters remain:

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
