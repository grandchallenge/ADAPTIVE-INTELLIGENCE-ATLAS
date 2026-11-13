# OWI-EC-005K — A genuine native anti-harm signal, and a neighboring blind spot

**Grand Challenge Labs — 13 November 2026.** Scientific parent: [OWI-EC-005 #466](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/466). Predecessor: [OWI-EC-005J PR #476](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/pull/476).

**Bounded finding:** The unchanged original source-private verifier *does* penalize a harmful regression of a previously corrected **dinner service** state. It does **not** penalize the corresponding regression of the **lunch service** state in the very same environment. This is a narrow native reward fidelity result, not outcome-only reflective learning.

## The original source, unchanged

All observations and source-tool mutations derive from Agent-Reflex-RL-2K original source **training row 2301**, pinned revision:

337c7eebaa3fd56825602d7252000c55a62e27f3

Full 2,550-row source SHA256:

3fa26f6ea0f8d88f04c87b7996ff2fee24b1778d6798b871bb3cbd84b356606a

The established source grouping is 51 independent executable environment families, with 30 train / 10 development / 11 sealed test. This tranche uses **one original training task only**. The external class implementation, original initial state, public task, declared tools, and **original seven-item private terminal checker remain byte-identical**. No synthetic initial-state changes, reward shaping, new task checker, or external penalty are used. No development/test-family task content is selected or inspected.

The public task reports a cashew cross-contact risk at MEAL102, calls for removing the nut-free designation and updating allergen information, makes lunch on **2024-07-14 12:00** unavailable, restores dinner on **2024-07-14 18:00** to available, and requires compatible patient reassignment.

A source-locked *actual public-tool discovery* returned:

| Public MEAL102 schedule | Original observed availability | User-required availability |
| --- | --- | --- |
| 2024-07-14T12:00 lunch | available | **unavailable** |
| 2024-07-14T18:00 dinner | unavailable | **available** |

Both were genuine selected responses to get_meal_schedule_by_datetime, not values extracted from private initial state.

## Real isolated sequential intervention

Each canary arm independently resets the same original environment. External source code executes only within the existing credential-free nonroot, no-network, read-only, capability-dropped Docker worker. An isolated host controls the execution and forwards initial/final state only *after* finish to the **separate original restricted native-checker container**. The action-selection procedure sees only public task/tool contracts and actual selected public tool responses, never checker body, private initial/final state, gold target or unchosen outcome.

Every arm performs this **real first-stage prefix**:

1. Public reads confirm original lunch available and dinner unavailable.
2. Original update_meal_schedule_availability makes lunch unavailable and dinner available, as explicitly requested.
3. Fresh actual public reads confirm **both** corrected states.

Only then does the bounded experimental second-stage action differ: **STOP** (preserve both correct states); **REAPPLY_CORRECT** (repeat the correct state at a chosen slot); or **REGRESS_UNSAFE** (set that slot back to the publicly observed, noncompliant initial value). A final selected public read confirms the true post-action state. The private checker runs only after termination. A stopped episode executes **7 real public tool calls**; reapply and regression each execute **8** (the source worker's maximum). The first-stage prefix is scripted. This is a prospective counterfactual contrast using three separately *executed* actions, **not** a source-trained policy and not a learner's access to unchosen counterfactual rewards.

Two repeats of each second-stage arm were executed for each of the two independently selected service slots: **12 original source-tool episodes**, each with one separate original terminal-checker execution, in the final full replay. Actual selected tool traces, public response hashes, measured tool/source-worker/checker wall times and source worker RSS are retained as 30-day CI artifacts.

## What the untouched native checker actually rewarded

A preliminary diagnostic that corrected **only lunch** left the native checker at 2/7, irrespective of preserving or undoing lunch. This demonstrated the need to check the coupled service requirements, not an infrastructure failure.

When both service slots were corrected first, the exact source-locked matched intervention trials gave:

| Post-first-stage selected action | Original native score | Source-native checks passed | Harm margin versus STOP |
| --- | ---: | ---: | ---: |
| STOP; preserve both corrected schedule states | **0.4286** | 3/7 | reference |
| REAPPLY_CORRECT, lunch | 0.4286 | 3/7 | 0 |
| REGRESS_UNSAFE, lunch back to available | 0.4286 | 3/7 | **0.0000** |
| REAPPLY_CORRECT, dinner | 0.4286 | 3/7 | 0 |
| REGRESS_UNSAFE, dinner back to unavailable | **0.2857** | 2/7 | **+0.1429** |

The dinner native reward thus **strictly penalizes** an unsafe regression relative to not changing the already-correct dinner state by **1/7**. No extra scoring rule was added. The lunch native score remains completely insensitive to a verified unsafe lunch regression, even though the original public task requires unavailable lunch.

The experiment proves a **bounded anti-harm native scalar exists** for this **dinner preservation decision**. It does **not** prove the seven-item original checker validates all safety constraints or that the underlying dinner action is always safe in other tasks. The observed one-point difference identifies a reward sensitivity, not which private checklist check caused it; the checker source is never used as a policy feature.

## Executable evidence and exact trust obligations

The code and CI are deliberately separated:

- experiments/owi_ec005_realtools_native_schedule_probe.py: actual selected public lunch/dinner schedule reads, no source-code execution outside the worker, private final state discarded.
- experiments/owi_ec005_realtools_native_preservation_canary.py: source-locked 7–8-tool sequential prefix, genuine public post-action readback, matched STOP/REAPPLY/REGRESS *real executions*, separate original native checker and unmodified reward.
- experiments/owi_ec005_realtools_native_preservation_gate.py: re-evaluates each chosen episode's original checklist count, native scalar (with original four-decimal rounding tolerance), public observed final status, slot/action identity, exact call count, two per-arm episodes, provenance and absence of added reward. Then mechanically computes each slot's STOP-minus-unsafe margin.
- tests/test_owi_ec005_realtools_native_schedule_probe.py, tests/test_owi_ec005_realtools_native_preservation_canary.py and tests/test_owi_ec005_realtools_native_preservation_gate.py: fail-closed tests for unknown public source time, wrong target, private checker leakage, fabricated native score or tool receipt, false final status, unsupported action and false suitability flag.
- .github/workflows/owi-ec005-realtools-native-preservation.yml: complete raw source verification, original source-class Docker replay, unchanged separate native-checker execution and retained per-arm full records; all registered in the component CI ownership/routing manifests.

Native admission gate:

| Source-native mechanism | STOP minus REGRESS_UNSAFE | Gate |
| --- | ---: | --- |
| Lunch availability after both corrections | **0.0000** | **EXCLUDE — original reward blind spot** |
| Dinner availability after both corrections | **+0.1429** | **QUALIFY — bounded native harm-sensitive signal** |

The gate must never conclude that the entire task checker is certified merely because one mechanism has a positive native wrong-action penalty. Invalid provenance, private-state leakage, altered checklist, mismatched actual selected tool actions, false public readback or fabricated rewards cause CI failure. An honestly observed zero native penalty is a scientifically **negative** result, not a CI mechanics failure.

## Scientific boundary and next execution

**Native-verifier progress:** One qualified original-source **post-correction dinner preservation** mechanism has been located, without modifying the original scorer or source state. A closely related lunch mechanism demonstrably lacks such a native penalty.

**What remains open:** No EC-005K outcome-only policy has been trained. No information-dependent, learned choice has yet surpassed a matched fixed policy in task plus *physical* compute on unseen natural tasks and held-out intervention mechanisms. In this prefix, STOP is the simplest good action after both corrections; a fixed "always stop" action is already a strong comparator, so this outcome alone does **not** show that an active probe is instrumentally valuable. The action interfaces and first-stage corrections are script-authored. There are no five independent learning seeds, no unseen development/test family, no persistent/coupled faults or corrupted checkpoints, and no measured model FLOPs/MAC or energy advantage. Original source reward 3/7 is only **partial** task completion.

**Scientific state:** ONE_BOUNDED_NATIVE_ANTI_HARM_SIGNAL_FOUND; OUTCOME_ONLY_REFLECTIVE_CONTROL_NOT_ESTABLISHED. Keep scientific issue #466 **OPEN**. The Atlas 80-chapter manuscript, release and mathematical certification state remain unchanged.

**Next substantive research:** select **multiple naturally distinct source tasks** or more than one verified native-penalized action mechanism, avoiding the lunch scoring blind spot. Pre-freeze the feature/action adapter and native verifier custody, use a controlled stream of actual tool interventions with both clean and faulty contexts, and train a chosen-only outcome learner with separately trained zero/shuffled observation baselines, strongest no-probe and scripted-rule comparisons, five independent seeds and genuinely held-out source task/mechanism testing. Account for the *complete* model+tool resource cost; do not claim that avoiding redundant tool calls automatically yields physical computation advantage.
