# CURRENT HANDOFF — Adaptive Intelligence Atlas

**Date:** 2026-10-06
**Recovery authority:** governance/ACTIVE_TRANSACTION.yaml on state/atlas-controller
**Current main:** c6b690725a0c89dd1746015d3e688c50553e0f28

## Restart rule

1. Read ACTIVE_TRANSACTION.yaml first.
2. Read this handoff.
3. Fetch live main.
4. If live main differs from the recorded baseline, recompute the frontier from governance/CHAPTER_LEDGER.yaml.
5. Repository state overrides chat history.

## Current state

- state: idle-ready
- next target: ATLAS-CH-JOINTUNC-001 — **Joint Uncertainty Propagation**
- downstream architecture count: 0
- direct consumers: none currently in architecture state

Atlas contract:

> Treat transition, reward, observation, and future-value uncertainty jointly rather than by naive independent summation.

Hard prerequisites on exact current main:

### ATLAS-CH-RLBASE-001

- manuscript: a99f78b788b97bc1bb3346ca1f1b97802c0f84db
- source lock: b29ecea9134227cb5ce3fcd7cc47303a90bd6699
- AUDIT-017: 8b7a1f9b61c15ab9c2c010ea538e25c11a7ed1cc

Inherited boundary:

- state, action, transition kernel, reward, policy, return, value, and model are distinct objects;
- value is expected future return under declared conditions, not calibrated uncertainty;
- an exact Bellman identity is distinct from an approximate learned value/model;
- optimality is relative to the declared MDP/reward/discount/observation problem;
- partial observability can require information state/belief state;
- transition-model, reward-model, observation-model, and future-value errors can interact;
- RLBASE explicitly does not solve their joint propagation;
- JOINTUNC may inherit the controlled stochastic substrate but must add a genuinely joint treatment rather than mechanical addition of independent error bars.

### ATLAS-CH-INFO-001

- manuscript: 0fca10cbc7476c5b729ee15dfad0dec563665821
- source lock: ea5a1b0db3aadf052fc0b749d7e813bb0ca5d43c
- AUDIT-004: 948f76b3f86d27fa4830efc30d8ef0135134256e

Inherited boundary:

- information and uncertainty quantities are defined only relative to a declared probability model;
- joint and conditional distributions must remain explicit;
- entropy, conditional entropy, mutual information, and KL divergence have distinct semantics;
- mutual information is statistical dependence, not causal direction;
- equal aggregate information summaries need not imply equal distributions, geometry, robustness, or causal role;
- concentration bounds retain their assumptions;
- sufficiency is relative to a declared statistical family/problem.

Before drafting JOINTUNC:

1. bind the exact audited RLBASE and INFO triples above;
2. source-lock only additional primary references genuinely needed for joint uncertainty propagation beyond those prerequisites;
3. define at least one exact finite witness where covariance/dependence changes the propagated uncertainty relative to naive independent summation;
4. define the decision-specific propagation object explicitly—e.g. coupled uncertainty in transition, reward, observation, and future value—rather than collapsing everything into one generic variance scalar;
5. include an independence control where the covariance terms vanish;
6. keep predictive/statistical dependence distinct from causal attribution;
7. state when linearized/error-propagation formulas are local approximations rather than exact global decision-system guarantees.

## Immediately completed transaction — CPS-001

- implementation issue: #239 — closed completed
- implementation PR: #240
- exact green implementation head: c2a6330cdc68d741ccc7c12477113e253d13a90d
- implementation GitHub Actions run: 37533936696 — success
- implementation merge: 7ca2ee93f1f2bc60ffadc696f2893ac0c29fed4c
- post-draft audit: AUDIT-060
- audit issue: #241 — closed completed
- audit PR: #242
- exact green audit head: fbbc4502c833c80e22cf135082b3147d2bf96a23
- audit GitHub Actions run: 37534286657 — success
- audit merge/current main: c6b690725a0c89dd1746015d3e688c50553e0f28
- audit record blob: 1be483be1f3768bd6921769b5e31bf9c2e7e7106
- audit disposition: **PASS — NO REPAIR**
- final canonical Linux validation on current main: green

Final CPS artifacts:

- specification: 05d1d186cce4f911790f8cd0a9bb25556bc56484
- derivation packet: 1ced647197f9af6567736e5edbccfefd7f200d5e
- computational witness: aafd136691e45b675ea05dc268f15f86302ba625
- reader manuscript: c07337d1bdf013ad5ac5a2caa69c4efbb45eea50
- source lock: 372dd928a77cf30e2e9b903239e4a49a5d479b79
- Chapter Ledger: dcc92835850f1f4fd33ba598e94097c6be55dc1a
- Source Register: 546eba7a627a71af4d27430e16c379457aa15ead
- transaction receipt: be766d28d50a22036a2f9ed780f60811b34d116b

Durable CPS substrate:

- optimizer/model state is treated as an augmented dynamical state;
- behavioral transition target, local diagnostic, retrospective alignment, heldout prediction, and causal optimizer mechanism are separate evidence objects;
- current public GSD state was refreshed on 2026-10-06 rather than inheriting the stale 2026-10-02 source gap;
- GSD-001 currently contains GSD-WP04 — CPS transition-local dynamics;
- GSD-WP03R establishes one confirmed OLMo2-1B behavioral transition under the frozen protocol;
- the exact public step-2000/3000/4000 revisions lack optimizer/trainer/scheduler/gradient/update-direction artifacts;
- GSD-WP04 is therefore BLOCKED_EXTERNAL_ARTIFACT_ABSENT, explicitly not NO_SIGNAL;
- for the exact toy momentum family with eta=1/10, beta=9/10:
  - J(h)=[[1-h/10,-9/100],[h,9/10]];
  - det J(h)=9/10;
  - tr J(h)=19/10-h/10;
  - kappa(J)=1+det J-tr J=h/10;
- discovery windows h=2,8 freeze tau=1/2;
- heldout toy windows h=3,7 are classified exactly as (0,1);
- all four toy matrices have identical spectral radius sqrt(9/10), so spectral radius alone is provably blind to the toy separation;
- retrospective alignment does not imply heldout prediction;
- heldout prediction does not imply causal mechanism;
- one confirmed 1B transition does not imply scale-general CPS prediction.

Current public GSD project sources bound in CPS:

- grandchallenge/GSD commit: ebd4681e1815a3d7f0285cc4ce2bc090b38fae8c
- research programme blob: 6a898efbdbe23eb6e947cd1c12f4a4b8fcee631f
- work-package index blob: c7af5b65f6496ff4a3c8533f4bb6ee8721467385
- campaign state blob: bc5ef87989fbeb094b0ffe5b348d06fe409397dc
- WP03R transition receipt blob: 01acb64e536f13bd689d20a74608a7170900d0e3
- WP04 artifact-block receipt blob: 9e999395fd14d1e8ac1b0ea5a209a1da66abab06

## Recomputed dependency-legal frontier

Every remaining dependency-legal architecture chapter has downstream architecture count 0.

Deterministic ID ordering selects:

- ATLAS-CH-JOINTUNC-001

Other dependency-legal count-0 chapters remain available:

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
