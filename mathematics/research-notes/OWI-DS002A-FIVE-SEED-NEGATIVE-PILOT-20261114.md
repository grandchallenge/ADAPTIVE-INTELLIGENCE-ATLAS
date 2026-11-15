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

### Exact-artifact inspection

The retained ZIP was independently opened and all five per-seed JSON records inspected. **Every extracted program has `Repair(fixed, action=3)`**, always repairing both branches. Probe rules were fixed no-probe for seed 1, fixed probe A for seeds 2–3, and fixed probe B for seeds 4–5. Consequently each extracted program is behaviorally equivalent to always-repair-both on the measured final action and normalized replay cost, even when the extra probe is executed. This explains the exactly zero paired difference to the fixed-both comparator for every condition.

The earlier one-seed smoke (20 pretraining steps) selected a norm-triggered probe plus fixed repair both. The five-seed full-pretraining study instead collapses to fixed probe choices plus always-both repair.

The following are **five-seed means calculated from the retained per-seed JSON artifacts**, not just a qualitative diagnosis:

| Held-out condition | Synthesized policy mean cost | Never-repair mean cost | Delta (synthesized minus never) |
|---|---:|---:|---:|
| persistent | 0.077434 | 1.005545 | -0.928111 |
| coupled | 0.077406 | 1.022495 | -0.945089 |
| **checkpoint** | **0.791860** | **0.007698** | **+0.784161** |
| roll | 0.077791 | 0.462930 | -0.385139 |
| length 13 | 0.103551 | 0.631648 | -0.528097 |
| parity | 3.618723 | 3.757326 | -0.138603 |

The checkpoint condition is decisive as a *failure witness*, not proof of a general causal theorem. In this held-out mechanism the trusted recovery checkpoint is damaged while the raw task trajectory is unchanged. The synthesized policy always uses both recovered checkpoints, losing substantially relative to leaving the raw states alone. The synthetic environment's normalized task-plus-compute loss does not imply verified correctness on external tasks.

The next experimental discriminator should ask whether **chosen observations can identify checkpoint integrity before repair**, whether additional charged derivative observations help distinguish such cases, and whether the conditional-repair programme can abstain when recovery is contraindicated. Observational equivalence must be tested rather than assumed.

## Source-level checkpoint observability obstruction

**Conditional proposition.** For a fixed input sequence `x` and frozen `Core`, the pre-probe observation `public_telemetry(make_batch(core,cfg,rng,kind="checkpoint"))` is independent of the randomly selected checkpoint-fault index, provided the mechanism and code path are exactly those defined in `owi_ec005_conditional.py`. The checkpoint-fault branch perturbs only `check` and leaves the raw forward hidden trajectory `state=h1` unchanged; the post-suffix hidden states and output logits used by `public_telemetry` are therefore independent of the fault index. A controller seeing pre-probe telemetry alone cannot identify this fault within this mechanism. This does **not** imply indistinguishability *after* an informative selected replay probe, nor equivalence to a different fault mechanism or task distribution.

**Operational falsification test.** The regression `test_checkpoint_fault_is_preprobe_observationally_invisible` constructs paired no-fault and all-fault checkpoint environments from the same exogenous input seed, asserting identical input sequences, raw logits and four public pre-probe features while the checkpoint tensors actually differ. This is a source-conditional invariant; the code test does not establish a formal categorical theorem or identify the full causal mechanism.

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
