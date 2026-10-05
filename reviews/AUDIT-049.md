# AUDIT-049 — Learning Progress as a Search Operator

## Disposition

**PASS — NO REPAIR**

ATLAS-CH-PROGRESSSEARCH-001 remains at `draft-v0.1`.

The audit found no mathematical, witness, source-scope, provenance, reader-maturity, exploration, horizon, credit-assignment, generalization-state, or downstream-boundary defect requiring repair.

This audit does not promote the chapter to publication-ready, certified, or final-copy status.

## Audited implementation

- implementation issue: #195
- implementation PR: #196
- exact green implementation head: `1e78bc7ff7015e0af426cd18a9f8aa5c1cf230d2`
- implementation merge: `677755fb083e3994d09d3def9a51ff6d48d39c24`
- audit issue: #197
- audit branch: `audit/progresssearch-197`
- chapter: `ATLAS-CH-PROGRESSSEARCH-001`

Implementation artifact identities:

- specification: `ff340951d1d91efe4129d9446bbf5512d13536bb`
- manuscript: `30e988200933dbba8ad53f069acacf131b0944ee`
- derivation packet: `46f2a5aecaa3d9bf502b27ad7415bba3d622acca`
- computational witness: `01648f83544bd859c6b8797c14dc8176366b8f51`
- source lock: `6e593b0d17e4a80d5790a6ea6d580f3b4530686a`
- Chapter Ledger: `de219718bfb6a51cb4f19bff692a6c350c22053b`
- Source Register: `f5566afda2641d819265a78b95d783dce3113517`
- bibliography: `07636a55fe69e1a1220b30cb22f28782224fa6fb`
- transaction receipt: `ca02f13f251accea38dd9479ad156df6bd697656`

## 1. Hard prerequisite

PASS.

The source lock binds exact Curriculum identities at protected baseline `d9f9fe56c27d6adab923fb5057c10cef9e4591d3`:

- manuscript: `b65f88c07ad5e523cff5d0ca3bd8a28c9bed41cc`
- source lock: `97d8862c4704ae48510444bdb4e72088ddcfa2f9`
- AUDIT-037: `786888f26138cbba7e131bc4a7dcd61c47d44d02`

The chapter preserves the inherited oriented learning-progress signal and the boundary that metric change does not identify a mechanism transition.

## 2. External source scope

PASS.

The source lock uses:

- Oudeyer, Kaplan, and Hafner (2007) for progress-sensitive intrinsic-motivation systems directing autonomous exploration;
- Baranes and Oudeyer (2013) for competence-progress-driven active goal exploration;
- Portelas et al. (2020) for teacher-driven search over continuously parameterized environments using absolute learning progress.

All empirical and algorithmic claims remain scoped to the cited systems. No universal learning-progress objective or universally optimal exploration rule is inferred.

## 3. Progress-search object

PASS.

The chapter defines a search state with explicit experience space, learner/controller observation, search history, progress estimate, exploration/coverage state, generalization-state evidence, objective, horizon, and remaining budget.

The search state is not collapsed into model or optimizer state.

## 4. Generalization-state evidence

PASS.

The chapter keeps declared evidence about acquisition, persistence, accessibility, and behavioral expression as a vector rather than silently summing heterogeneous measurements.

It explicitly rejects the promotion of this evidence vector into ground-truth mechanism state.

## 5. Exploration witness

PASS.

Independent replay gives:

- exploit-only over observed regions, two rounds: `2`;
- coverage-first, two rounds: `6`.

The witness therefore proves the finite separation that exploitation restricted to observed regions can fail to discover a higher-progress unobserved region.

It does not claim forced coverage is generally optimal.

## 6. Horizon witness

PASS.

Independent replay gives:

- immediate-greedy two-step return: `2`;
- investment-then-unlock two-step return: `5`.

The witness correctly establishes that maximizing immediate progress need not maximize finite-horizon return.

## 7. Credit assignment

PASS.

The H-step return is explicitly separated from causal credit. Delayed improvement is not automatically attributed to the latest experience when multiple updates or interventions occurred.

## 8. Absolute progress

PASS.

The chapter explicitly states that absolute learning progress can be large under improvement or deterioration.

Therefore absolute progress is not equated with beneficial learning.

## 9. Search objective and cost

PASS.

Progress, uncertainty/coverage, generalization-state evidence, cost, budget, and horizon are not assumed to share units.

Any scalarization or ordering rule must be declared.

Controller/search overhead remains part of fair comparison.

## 10. Effective training distribution

PASS.

The reader preserves the inherited Curriculum boundary that search changes the training intervention by altering support, weights, exposure, ordering, or generated experience.

Endpoint differences therefore require controlled dose/recipe comparisons.

## 11. Bibliography and provenance

PASS.

All declared bibliography keys resolve:

- `OudeyerKaplanHafner2007IntrinsicMotivation`;
- `BaranesOudeyer2013GoalExploration`;
- `PortelasEtAl2020TeacherAlgorithms`.

The Source Register contains `ATLAS-SRC-PROGRESSSEARCH-LOCK-001` and the Chapter Ledger binds specification, reader, derivation, source lock, and witness paths.

## 12. Reader maturity and integrity

PASS.

The reader supplies an opening obstruction, inherited measurement boundary, formal search object, exploration semantics, two exact witnesses, delayed-credit boundary, absolute-progress warning, experiment-control obligations, failure boundaries, and downstream handoff.

The implementation passed canonical validation after two non-substantive escaping repairs: removal of accidental control characters from the specification. No mathematical content changed in those repairs.

## 13. MINCURR handoff

PASS.

ATLAS-CH-MINCURR-001 may inherit explicit experience-space search, exploration/coverage state, finite-horizon and delayed-credit semantics, generalization-state evidence, and both exact counterexamples.

PROGRESSSEARCH does not pre-claim minimality, reconstructability, or a transferable reasoning basis.

## Final audit boundary

The durable result is:

`current progress != long-horizon value`,

and

`observed-region exploitation != complete experience-space search`.

No repair is required.

The next legitimate operation is exact-head canonical validation of this audit record, audit PR merge, final main validation, frontier recomputation, issue closure, and controller/handoff reset.