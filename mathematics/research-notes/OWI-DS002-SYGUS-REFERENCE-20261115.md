# OWI-DS-002 — Official SyGuS non-differential reference baseline

**Evidence class:** exact-head GitHub Actions results for a bounded non-differential reference experiment; no independent GCL scientific admission.

This unit adds an off-the-shelf, source-independent program-synthesis comparator to the separately tested [SyGuS admission PR #490](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/pull/490). The solver, cvc5 `1.4.2`, receives the exact upstream SyGuS-Comp 2017 invariant task, without hand-provided positive witnesses. Each result is independently admitted by Z3 `4.13.4.0` using *all three* induction obligations on the same source-locked input.

## Protocol

- Official task source remains fixed to upstream repository `SyGuS-Org/benchmarks` at commit `13c8deb68a873635879c9a69bc78caebd340f646` and per-file Git blob SHA1.
- cvc5 executes in an isolated subprocess with a bounded 15-second wall-clock deadline per task; a 20-second cap is used for the required `inc` smoke gate.
- Parse the generated `inv-f` definition; require a matching integer-parameter signature, a Boolean return, and membership in the allowed, bounded expression fragment. Do not accept a solver's claim of success on faith.
- The independent verifier checks `pre -> I`, `I & trans -> I'`, and `I -> post` with Z3; only three `unsat` results authorize a `VERIFIED_INDUCTIVE_INVARIANT` receipt. Unsolved, unsupported syntax, timeout, solver exception, bad source or any counterexample all remain distinct non-success statuses.
- Report per-task candidate, source blob, verifier result, wall time, and per-split success. Solver success is not a claim of external-program correctness or general algorithmic transfer.

This is a strong **non-differential SMT-based baseline**, not a new differentiable reasoner. Its presence is intended to stop misleading claims that neural or gradient-guided search improves synthesis without comparison to established SyGuS tooling.

## Exact-head executed evidence — 15 November 2026 UTC

**[CI EVIDENCE]** [GitHub Actions run 43703896145](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/actions/runs/43703896145) passed on candidate head `03be937e566b5b8969e0cd561c02364ba1dad60b`. Archive `owi-ds002-sygus-cvc5-z3-reference-ten`, artifact ID `14156634691`, ZIP SHA256 `37d2b154bd93347a292a5184f02fd4754b7517500fe9521c6eddf6b03bbfb02e`. The archive contains a smoke receipt and a full ten-task JSON report, inspected separately from workflow status.

**[SMT VERIFICATION EVIDENCE]** Standard cvc5 1.4.2 generated ten candidate invariants, and independent Z3 4.13.4.0 returned three UNSAT negated induction VCs for each: **10/10 independently solver-checked**, with five developer and five designated held-out tasks. The result is relative to the pinned formal specifications, not to any verified real program or a novel synthesis system.

| Official task | Split | cvc5 subprocess seconds | Z3 initiation / step / safety |
|---|---|---:|---|
| inc | dev | 0.090 | UNSAT / UNSAT / UNSAT |
| dec | dev | 0.093 | UNSAT / UNSAT / UNSAT |
| w1 | dev | 0.087 | UNSAT / UNSAT / UNSAT |
| ex11 | dev | 0.087 | UNSAT / UNSAT / UNSAT |
| sum4 | dev | 0.097 | UNSAT / UNSAT / UNSAT |
| ex7 | heldout | 0.097 | UNSAT / UNSAT / UNSAT |
| ex14 | heldout | 0.096 | UNSAT / UNSAT / UNSAT |
| ex23 | heldout | 2.156 | UNSAT / UNSAT / UNSAT |
| fig1 | heldout | 0.085 | UNSAT / UNSAT / UNSAT |
| fig3 | heldout | 0.087 | UNSAT / UNSAT / UNSAT |

The sum of measured solver-subprocess wall times is **2.974 seconds**, median **0.091 seconds**, maximum **2.156 seconds**. This is not total benchmark wall time; source download, test setup, checker time, and CI installation are separate.

**[ENGINEERING CORRECTION]** The first cvc5 run failed to parse the legacy SyGuS-2015 `declare-primed-var` command. The solver-only normalization now expands it to two `declare-var` declarations, as specified by the old language standard. All ten **original** benchmark sources remain unmodified, SHA-locked, and independently checked by Z3. A second correction extended the strictly typed candidate reader to accept linear products of constant coefficients and bounded, nonrecursive SMT `let` bindings. Its negative tests still prohibit symbolic oracle calls, nonlinear products, binding shadowing, malformed terms and excessive complexity. After this correction, the verified reference count increased from six to ten; this was an interpreter-coverage repair, **not** a new synthesis algorithm.

**[SCIENTIFIC DECISION]** This small cohort is saturated by an established solver. It is unsuitable for claiming that a custom differentiable or reflective synthesizer improves verified solve rate. The next benchmarking requirement is a materially harder, stratified, source-locked SyGuS task population with unsolved instances or computational headroom, together with a demonstrably meaningful smooth/differential execution interface. A fresh solver comparison must use equal total compute and prevent mechanism labels, holdout targets and independent verification counterexamples from leaking into the learner.

## Open conditions

This ten-task cohort remains limited; independently measured solve rate here is not a SyGuS competition ranking. Inputs are publicly available, so the dev/heldout split is experimental rather than secret. Source original intent, exact solver packaging, command semantics and missing libraries remain subject to CI/adjudication. No fair A/B/C/D total compute matching exists; C1 and D are not implemented. The source language is integer-state LIA and should not be silently treated as a smooth differential category.

**Evidence disposition:** `STANDARD_SYGUS_REFERENCE_10_OF_10_Z3_CHECKED__SMALL_COHORT_SATURATED__GCL_DIFFERENTIAL_HYPOTHESIS_UNTESTED`. Protected admission, independent mathematical review and merge remain separate uncompleted obligations.
