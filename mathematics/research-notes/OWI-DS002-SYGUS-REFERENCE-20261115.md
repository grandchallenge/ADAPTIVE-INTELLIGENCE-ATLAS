# OWI-DS-002 — Official SyGuS non-differential reference baseline

**Evidence class:** candidate implementation, pending exact-head CI.

This unit adds an off-the-shelf, source-independent program-synthesis comparator to the separately tested [SyGuS admission PR #490](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/pull/490). The solver, cvc5 `1.4.2`, receives the exact upstream SyGuS-Comp 2017 invariant task, without hand-provided positive witnesses. Each result is independently admitted by Z3 `4.13.4.0` using *all three* induction obligations on the same source-locked input.

## Protocol

- Official task source remains fixed to upstream repository `SyGuS-Org/benchmarks` at commit `13c8deb68a873635879c9a69bc78caebd340f646` and per-file Git blob SHA1.
- cvc5 executes in an isolated subprocess with a bounded 15-second wall-clock deadline per task; a 20-second cap is used for the required `inc` smoke gate.
- Parse the generated `inv-f` definition; require a matching integer-parameter signature, a Boolean return, and membership in the allowed, bounded expression fragment. Do not accept a solver's claim of success on faith.
- The independent verifier checks `pre -> I`, `I & trans -> I'`, and `I -> post` with Z3; only three `unsat` results authorize a `VERIFIED_INDUCTIVE_INVARIANT` receipt. Unsolved, unsupported syntax, timeout, solver exception, bad source or any counterexample all remain distinct non-success statuses.
- Report per-task candidate, source blob, verifier result, wall time, and per-split success. Solver success is not a claim of external-program correctness or general algorithmic transfer.

This is a strong **non-differential SMT-based baseline**, not a new differentiable reasoner. Its presence is intended to stop misleading claims that neural or gradient-guided search improves synthesis without comparison to established SyGuS tooling.

## Open conditions

This ten-task cohort remains limited; independently measured solve rate here is not a SyGuS competition ranking. Inputs are publicly available, so the dev/heldout split is experimental rather than secret. Source original intent, exact solver packaging, command semantics and missing libraries remain subject to CI/adjudication. No fair A/B/C/D total compute matching exists; C1 and D are not implemented. The source language is integer-state LIA and should not be silently treated as a smooth differential category.

**Result disposition pending execution:** `STANDARD_SYGUS_REFERENCE_IMPLEMENTED__INDEPENDENT_SOLVER_ADMISSION_NOT_YET_OBSERVED`.
