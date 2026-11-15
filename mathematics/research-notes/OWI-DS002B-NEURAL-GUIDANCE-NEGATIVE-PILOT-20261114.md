# OWI-DS-002B — Outcome-only neural guidance pilot: no measured advantage over typed symbolic search

Grand Challenge Labs research evidence note; 14 November 2026 Vancouver / 15 November UTC.

Scientific issue: [#483](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/483). Stacked candidate PR [#488](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/pull/488). Exact executed head `de3e5a2dc01e080a82e7971f2c16d61559e83479`. [Five-seed workflow 43657291643](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/actions/runs/43657291643), artifact `14137999329`, ZIP SHA256 `8ec6987616964f482df50f5851b74fa7297055433cb42734049d6e9c4d94de7e`.

## Actual method and evidence

A symbolic selector and a learned, two-stage neural guide consumed the **same** 4,095 logged action/outcome examples per seed, the same five independent pretrained core seeds, and the same finite 209-program typed grammar. B trains 300 steps on sequential importance-weighted chosen-action outcomes, then projects predicted action distributions into that grammar via first-stage propensity correction; B's gradients are gradients of a learned policy risk, not measured derivatives of the environment. Both extracted programs were evaluated on identical fresh exogenous cases for six held-out conditions (512 examples per condition and seed).

The executed workflow and repository-wide validation reported success. Direct inspection of all five retained result JSONs established:

| Seed | A extracted probe | B extracted probe | A/B extracted repair |
|---|---|---|---|
| 1 | never | always A | always both |
| 2 | always A | always A | always both |
| 3 | always A | always A | always both |
| 4 | always B | never | always both |
| 5 | always B | always B | always both |

Each of the six held-out condition-level mean B-minus-A normalized task-plus-compute differences is **0.0**, exactly as printed in the retained aggregate JSON. Despite distinct probe rules, the cached replays and fixed repair-both action produce equivalent measured task/compute objectives.

Measured mean symbolic A selection time: `0.031949078` seconds per seed. Measured mean additional B neural-training time: `1.264877573` seconds per seed (approximately 39.6 times the A selection time). These are **not** matched end-to-end computational budgets and cannot establish universal B inefficiency.

## Scientific disposition

`B_NO_GAIN_OVER_A__ALL_POLICIES_REPAIR_BOTH__DIFFERENTIAL_INFORMATION_UNTESTED`.

This result does not show derivative-informed synthesis fails: neither system used measured environmental derivatives. The fixed grammar and training distribution make fixed-both attractive; importantly, both systems transfer badly to checkpoint corruption, where the recovery checkpoint itself is damaged and the raw trajectory is intact. The negative result narrows future hypotheses rather than establishing a general no-go.

## Next controlled question

For C, use the existing chosen-run authorized tangent capability to add **genuinely measured** checkpoint sensitivity observations from selected replay computations. Charge every query and separately record runtime, query counts, and replay counts. Compare C to B and the appropriate information controls (shuffled measured tangent; surrogate-only), reusing the **same** grammar subset where possible. Test whether checkpoint-corruption cases become distinguishable *after permitted probes*; pre-probe public telemetry is source-level invariant under checkpoint-only corruption. Any claimed improvement must survive held-out mechanisms and equal total compute, and failure must be retained.

D causal self-modeling remains a separate, unimplemented hypothesis. No source-native reward fidelity claim or formal proof-carrying synthesis admission is made.
