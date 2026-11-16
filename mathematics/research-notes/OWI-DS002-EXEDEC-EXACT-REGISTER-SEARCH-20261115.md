# OWI-DS-002 — ExeDec-exact straight-line register-program synthesis

Parent issue #483. Status: proposed source-locked experiment; no scientific admission until exact-head CI, evidence and review.

## Scientific and compatibility setting

Historical Microsoft DeepCoder C++ search, source-pinned in #496, is not semantically identical to the pinned 2024 ExeDec DeepCoder DSL. Nine original solver self-reported positive results fail the published ExeDec input/output checks. Historical self-reported positive results cannot substitute for independent ExeDec verification.

The protected GCL enumerator #495 searches bounded expression trees with observational-signature deduplication, but cannot represent arbitrary shared intermediate registers as naturally as straight-line DAG search. This tranche adds source-semantics-exact typed register search: each successor is executed by the already hash-pinned and cross-compared 2024 ExeDec interpreter from #493.

## Search protocol and private evidence boundary

Every search state stores typed registers, observed values on public examples, and a concrete sequence of legal DeepCoder statements. Operators may reuse any earlier appropriately typed register, including twice as a binary operand. All intermediate values must be valid under exact ExeDec integer and list bounds on every published example. Search ordering is seeded and task-independent; selection uses only distances to published I/O outputs plus seeded diversity. Observational-equivalence pruning and fixed-size beam truncation can discard valid programs; this is a bounded heuristic, not proof of equivalence.

The search function receives only an allowlisted public I/O projection. It never sees target reference source, evaluator-only probe values, few-shot programs, oracle mechanism IDs, real JVP, or candidate verifier feedback. The source reference programs are public upstream; this projection is a procedural custody boundary and not cryptographic secrecy. Candidates must pass exact public program execution, then a separate independent source-pinned ExeDec verifier checks 16 new valid generated input examples. A bounded positive means finite behavioral agreement only.

## Precommitted same-task three-way comparison

CI runs on each of six ExeDec structural splits, source indices 0 and 17, and seeds 1–5 (12 distinct tasks, 60 task–seed trials), with all successes, failures and timeouts retained.

* New exact register search: four program nodes, at most 15,000 attempted successors, beam width 160, per-trial search wall limit 1.5 s.
* Prior GCL expression-tree enumerator #495: four nodes, 15,000 attempted expressions, retained width 600, no per-trial search wall cap.
* Original pinned Microsoft C++ external search #496: four nodes, 1.5-second subprocess wall cap; every candidate is independently checked by the ExeDec verifier. The historical language remains mismatched and is labeled as such.

These are identical source task–seed identities and shared evaluator rules, not identical search algorithms, exact source semantics for the legacy solver, or equal total compute. CPU time and wall time, compilation and checker overhead must be explicitly separated and not conflated with physical FLOP cost. Do not claim mature external-solver performance on the strength of this new local search.

CI also executes nine different source indices (3,23,41,67,89,123,157,181,199) across six splits with seed 11, yielding 54 additional distinct published tasks. They are disjoint from the matched 12 tasks but are not secret. All task input projections, source blob hashes, candidate programs, failure and evaluator decisions, search attempts, signatures, CPU/wall, process-level RSS and separate evaluator costs are preserved.

## Scientific disposition

This is a source-semantics-exact nondifferential comparator and broader published-source study only. Neither C1 nor D is tested, no cartesian differential structure is inferred from integer/list execution, no chosen-run Jacobian-vector product is charged, no causal intervention prediction is measured and no reflective/introspective cognition is certified. Full equal-compute A/B/C/D and an independently authored mature compatible external search comparator remain research obligations. Keep OWI-DS-002 issue #483 open.
