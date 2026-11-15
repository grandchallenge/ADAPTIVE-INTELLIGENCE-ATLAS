# OWI-DS-002 — ExeDec typed outcome-only enumerative pilot

**Research issue:** #483. **Evidence status:** candidate benchmark experiment; no scientific admission or protected merge until exact-head CI, review and evidence readback. This is an **initial non-differential enumerator**, *not* claimed to be the strongest known DeepCoder solver.

## Input, grammar, and leakage control

The engine receives only an allowlisted participant-view object from source-locked ExeDec DeepCoder, including public I/O examples, source split and source blob. Program ASTs, published reference solutions, evaluator-probe outputs, oracle task identity, gradients and fault labels are not passed into the search function. The evaluator has separate access to the reference source and verifies extracted programs only *after* search. The public source already contains target programs and hence does not support a secret holdout or prevention of a competitor reading references outside this programme.

The enumerator builds typed first-order and higher-order DSL expression trees from inputs, using the same original operation and lambda tokens as the protected executable verifier. Bottom-up enumeration uses finite observed-output signatures and per-depth deduplication (one representative per observed signature); search is seeded and bounded by node depth, maximum attempted expressions and retained signatures per type and depth. On an I/O match, the engine **extracts a discrete executable DeepCoder program** and replays all published examples independently. Distinct programs that agree on the three observed inputs can be collapsed by this pruning; this may lose a correct solution.

## Source-pinned five-seed pilot

Run the CI job with indices 0,17,49 on each of six published ExeDec compositional-generalization distributions (18 task identities), seeds 1–5, maximum three non-input expression nodes, maximum 3,000 attempted expression evaluations per task and 220 retained observational states per type/depth. The 90 task × seed trials include all evaluator decisions; do not silently drop failures. Each extracted candidate is submitted to the independent previously admitted reference checker on 16 fresh valid generated cases; the evaluator may reject even an exact match to public examples.

Log counts (attempts, invalid candidates, signature collisions, deduplicated states, extraction errors), actual elapsed CPU/wall clock search and evaluation, process-wide peak RSS and end-to-end wall time, plus per-task and per-split receipts. Each published split's exact upstream blob is preserved in records. The random seed controls enumeration order, not any simulated gradient or oracle action. The engine does not train a neural controller.

**This is not full compute-matched A/B/C/D**, and the sum of per-task wall times is not an actual physical total across devices. One sequential process is used; process-wide peak RSS must not be misreported as per-task memory. A 90-row pilot does not establish distribution-wide error bounds. Report the observed solve and verified rates as descriptive results only.

## Research controls and next obligation

Go/no-go for selected-run derivatives remains **unresolved**. If this bounded enumerator fails on difficult compositional tasks, the result is a search-baseline lower bound, not proof of structural headroom against cvc5, Dryad, contemporary DeepCoder engines or learned baselines. Source comparison against a mature external non-differential synthesizer and matched compute remains necessary. Any C1/D experiment requires a separately justified differentiable fixed-shape real submodule, actual chosen-run JVP charges, shuffled and surrogate-only controls, held-out mechanism design and five-plus seeds. No categorical differential claim follows from evaluating discrete DeepCoder lists/integers.
