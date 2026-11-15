# OWI-DS-002 — Independent SyGuS invariant-admission benchmark

**Grand Challenge Labs · 15 November 2026 · Evidence class: research candidate.**
Scientific parent: [Atlas OWI-DS-002 issue #483](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/483).

## What is actually being established

A previously missing correctness gate: a typed candidate program is checked **against third-party, source-locked SyGuS-Comp 2017 loop-invariant specifications**, rather than graded on a handful of numeric examples or by a solver coupled to the synthesizer. This is a verification interface, **not** a solved synthesis benchmark, and no claim of reasoning superiority follows from its implementation.

Official upstream: [SyGuS-Org/benchmarks](https://github.com/SyGuS-Org/benchmarks), commit `13c8deb68a873635879c9a69bc78caebd340f646`, folder `comp/2017/Inv_Track`. Ten original problems are pinned individually by Git blob SHA1 in `experiments/owi_ds002_sygus_manifest.json`. Raw upstream benchmark bytes are retrieved from the exact commit and fail closed if their hashes differ. We do **not** vendor a fork of the benchmark sources or silently transform the source specification into self-scoring examples.

Development cohort: `inc`, `dec`, `w1`, `ex11`, `sum4`. Held-out task cohort: `ex7`, `ex14`, `ex23`, `fig1`, `fig3`. Because this is an established public benchmark, the split is an *experimental protocol*, not cryptographic secrecy: holdout compliance needs independent auditing. The corpus is intentionally bounded; further tasks and competing SyGuS solvers are required before general synthesis performance claims.

## Independent correctness contract

The checker accepts a bounded, typed Boolean invariant expression `I(x)`; it cannot invoke source predicate names such as `pre-f`, `trans-f`, or `post-f` as shortcuts. It then uses a separately installed Z3 solver to decide satisfiability of the *negated* induction verification conditions, each relative to the original pinned benchmark source:

```
INIT:   pre(x) and not I(x)
STEP:   I(x) and trans(x,x') and not I(x')
SAFE:   I(x) and not post(x)
```

Admission requires all three to return `unsat`. A `sat` counterexample rejects the program; `unknown`, timeout, parser/type errors, source-hash mismatch and incomplete data do **not** authorize admission. Each receipt identifies the source blob, candidate SHA256, solver version, three verification results and wall time.

This is **SMT-solver-checked inductive invariance relative to the supplied formal specification**, not proof-assistant certification or proof that the original benchmark accurately models an external program. The solver and parser are part of the trusted computing base. The checker makes no program-synthesis calls and obtains no reward from the searched candidate evaluator.

## Positive and negative gates

Unit tests exercise five development-set candidate invariants and require all three checks `unsat` on their official original sources. For the `inc` problem they independently require rejection and a `sat` counterexample for:

- `false` (violates initiation),
- `true` (violates safety),
- `(= x 0)` (violates transition preservation).

No held-out candidate solution is embedded in the training fixture. Ten source files must parse with intact pinned blob identities. CI archives machine-readable admitted and rejected candidate receipts.

## Critical categorical type distinction

**Integer-state SyGuS invariant problems are not themselves smooth maps in a cartesian differential category.** Assigning an automatic derivative to a symbolic branch change, an arbitrary integer relation, or a solver proof would be a category error unless an explicit differentiable interpretation is independently specified and justified.

Accordingly, this benchmark can settle whether an agent has synthesized a *correct discrete program or invariant*. A future differential-guided reasoner may use measured JVPs from *eligible smooth computational submodules* as additional search information; its candidate programs must nonetheless pass an independent discrete specification checker. Any reported C-vs-B advantage must include the cost of such observations, exclude gradients of private or unexecuted counterfactuals, and survive source-heldout structural tests. Ordinary differentiable surrogate losses do not count as new environment information.

## Next obligations, not achieved

1. Obtain exact-head CI evidence for source lock, parser and Z3 admission; record the receipts and repair any failures before review.
2. Integrate a competitive standard SyGuS enumerative/SMT baseline (e.g., a source-pinned cvc5 binary) with fixed wall/CPU budgets, plus open-ended typed generation. Five hand-specified development invariants are *verifier tests*, not a solved-rate evaluation.
3. Register concrete program-synthesis inputs/outputs and a held-out evaluation policy that prevents solver solutions and holdout constraints from being used as training guidance during the experiment.
4. Define the smooth/discrete interface and introduce chosen-run, charged derivative observations **only** where the smooth component's semantics and available information support such queries.
5. Compare A/B/C/D on verified solve rate, held-out algorithmic structure, proof-checking cost, full computational budget and negative outcomes; segregate privileged verifier outputs.
6. Require independent role-separated scientific review, source-to-formal interpretation audit and protected admission before any merge or claim promotion.

**Disposition pending CI:** `SOURCE_PINNED_EXTERNAL_CORPUS__INDEPENDENT_VERIFIER_CANDIDATE__SYNTHESIS_UNTESTED`.
