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


## Exact-head executed capacity and generalization result — 2026-11-15 UTC

**[CI EVIDENCE, candidate not yet admitted]** [Source-pinned enumerative workflow 43712455175](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/actions/runs/43712455175), exact candidate head \`937daf0cbdba72d05090cfb179796163786a8700\`, passed all seven enumerator unit tests and ten inherited executable-admission tests, plus both 90-trial actual-source experiments. [Full Atlas repository validation 43712455208](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/actions/runs/43712455208) passed, as did [upstream semantic admission 43712455339](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/actions/runs/43712455339). Artifact \`14161630614\` contains 90 per-task, per-seed source/lookup/evaluator records for each budget plus the paired comparison; archive SHA256 \`0932169720af8d7b8b3ed80d59ea12b7c5655e0154f61c9ddd0965f20996ac8a\`. These are published-source behavioral tests, not certifying proofs.

| ExeDec published structural split | 3-node / 3,000-eval | 4-node / 15,000-eval | Task identities |
| --- | ---: | ---: | ---: |
| NONE | 15 / 15 | 15 / 15 | 3 |
| ADD_OP_FUNCTIONALITY | 15 / 15 | 15 / 15 | 3 |
| SWITCH_CONCEPT_ORDER | 9 / 15 | 13 / 15 | 3 |
| COMPOSE_NEW_OP | 7 / 15 | 11 / 15 | 3 |
| COMPOSE_DIFFERENT_CONCEPTS | 5 / 15 | 11 / 15 | 3 |
| LENGTH_GENERALIZATION | 1 / 15 | 3 / 15 | 3 |
| **Total bounded-verified task–seed trials** | **52 / 90** | **68 / 90** | **18** |

Each split reports three fixed task identities (indices 0,17,49) and five independent enumeration-order seeds (1–5), **not fifteen independent tasks**. The larger-capacity regime simultaneously changed maximum nodes, expression attempts and state-retention width; the +16 paired-trial improvement is therefore a capacity *bundle* effect, not identified as a causal effect of node depth alone. The larger run found 70 programs that match public I/O; two were rejected by evaluator-only tests. All 52 small-capacity public I/O candidates passed the independent bounded evaluator. The failed candidates demonstrate the importance of separately checked unseen input behavior. They are negative evidence, not deletable outliers.

**Measured resource/coverage:** The first regime performed 79,507 attempted expressions, CPU 1.413 s end-to-end in the final paired run; the larger regime performed 217,936 attempts, CPU 3.500 s end-to-end. These timings are run-local and are not equal-compute A/B/C/D comparisons. Source download, worker provisioning, CI checkout and external tool installation are not included in these end-to-end script timings. No physical MAC/FLOP count was inferred. Both runs use one CPU process, and their recorded peak resident set size represents the entire process, not a per-task peak.

**Disposition:** \`INITIAL_NONDIFFERENTIAL_EXECUTABLE_COMPARATOR__CAPACITY_GAIN__LENGTH_GENERALIZATION_WEAK__NO_DIFFERENTIAL_CLAIM\`. The bounded search illustrates useful headroom at realistic source-pinned tasks but is not an external mature symbolic-search reference. The sample is deliberately small, public, and source reference programs are available. Next obligations are an appropriately stronger enumerative and/or established third-party synthesis solver, unambiguous search/full-compute accounting, broader stratified evaluation and a separately justified legal selected-run differentiable submodule before C1 and D.
