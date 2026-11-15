# OWI-DS-002A — Five-seed symbolic policy-search pilot: no improvement over fixed repair

**Research evidence note · 14 November 2026 (Vancouver) / 15 November 2026 UTC.**
Scientific issue: [#483](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/483).
Candidate stacked PR: [#486](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/pull/486).
Exact executed PR head: `e6fcc3d5236a475420aab2f881f3ac797be868fa`.
Five-seed source: [GitHub Actions 43656688540](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/actions/runs/43656688540).
Artifact: `owi-ds002-symbolic-baseline-five-seed` (artifact ID `14137934608`, SHA256 `fc05f93626cfc1e15f6fdf1eeade352473e811849bebaa1365273363ac28944d`), containing five full seed JSON records and `five_seed_summary.json`. Retention 30 days.

## Protocol actually executed

- Five independent seeded baseline pretrains (seeds 1–5), 250 pretraining steps each.
- 4,095 logged on-policy samples per seed, using randomized probe and repair actions with known propensities; candidate search uses only selected-action, realized terminal losses.
- A fixed finite grammar of 209 typed two-stage probe/repair programs. Candidate selection uses self-normalized sequential importance weighting, descriptive uncertainty penalty, and complexity penalty.
- Each extracted deterministic program was executed afresh under the OWI-EC-005 conditional replay environment.
- Six evaluation scenarios per seed: persistent, coupled, checkpoint, roll, Gaussian at length 13, and Gaussian parity shift. Each scenario has 512 examples.
- Comparator arms: no repair, fixed A, fixed B, and always-repair-both, evaluated on matched exogenous environment seeds; comparator outcomes were *evaluation-only*, never exposed to candidate selection.

## Observed result

The CI job successfully completed. Its deterministic `five_seed_summary.json` prints the following paired mean cost differences, defined as synthesized programme cost minus always-repair-both cost:

| Held-out condition | Five-seed mean paired difference |
|---|---:|
| persistent | 0.0 |
| coupled | 0.0 |
| checkpoint | 0.0 |
| roll | 0.0 |
| length 13 | 0.0 |
| parity | 0.0 |

This is exact equality in the reported finite-precision aggregate, **not** an estimated performance gain. The baseline failed to improve task-plus-compute cost against the fixed-both policy in these six settings. This excludes no other tasks, priors, grammars, objectives, or greater sample sizes.

The earlier one-seed smoke at 20 pretraining steps selected a redundant norm-triggered probe with always-repair-both, consuming two suffix replays per example. The five-seed aggregate also shows no effective cost reduction against fixed-both. The complete per-seed extracted expressions must be inspected before assigning a unique causal failure explanation; observational equivalence and redundant controls are candidate explanations, not proven root causes.

## Important accounting and inferential limitations

The implementation relies on normalized replay charges, not equal measured *total synthesis* physical compute. Its inherited neural-controller MAC estimate was identified as inapplicable to discrete grammar policies and removed from the symbolic report at head `e6fcc3d`: recurrent base/replay MAC proxies are reported separately; symbolic-policy MACs remain unmeasured.

The sampled importance-weighting estimator is used for policy selection, so its naive descriptive standard error is not a post-selection inferential confidence interval. The six held-out conditions share a pretrained core within each seed; they are not 30 independent model seeds.

No B/C/D implementation exists; the experiment is **not** a test of whether derivative observations or reflective models help. No formally verified synthesized program was admitted. This is a bounded, negative A-baseline pilot.

## Decisions and next obligations

1. **Retain the negative result.** Do not optimize the benchmark or hide the equality result in CI success language.
2. **Inspect per-seed extracted programs and coverage.** Determine whether an observationally degenerate grammar/cost function forces fixed-both behavior, or selection uncertainty prevents available useful conditionals from winning.
3. **Design a matched-trajectory B baseline** using learned guidance over the same typed grammar, same training samples and exogenous seeds, with explicit total search-compute accounting and no additional information sources.
4. **Only after B is stable**, add C with execution-authorized, charged tangent information and mandatory shuffled/surrogate controls, then D with causal self-modeling and held-out intervention-prediction loss.
5. **Add a stronger verification measure:** exact discrete replay equivalence, per-example task correctness where exposed by an appropriate public scoring interface, and proof/refinement checks if relevant. BCE alone is not 'verified solve rate'.
6. **Preserve native-reward fidelity gate.** Source-native rewards are not suitable until the separately recorded harmful-versus-abstain identification objection is resolved.

**Disposition:** `A_BASELINE_EXECUTED__NO_GAIN_OVER_FIXED_BOTH__DIFFERENTIAL_HYPOTHESIS_UNTESTED`.

The workflow's passing status confirms the experiment executed; it does not convert the negative result into scientific success.
