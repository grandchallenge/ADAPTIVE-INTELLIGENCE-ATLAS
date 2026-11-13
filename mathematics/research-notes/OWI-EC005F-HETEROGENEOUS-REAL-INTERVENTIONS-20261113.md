# OWI-EC-005F — Heterogeneous real-tool intervention value

**Date:** 13 November 2026. **Parent issue:** [OWI-EC-005 #466](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/466). **Status:** 27 actual selected-action trials in three independent, source-locked training families, with separate private terminal verification. Outcome-only *learned* reflective control is NOT established.

## Motivation and provenance

The prior [OWI-EC-005E five-seed experiment](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/pull/471) optimized real chosen-action neural gates on one static outbreak-report task. Every policy converged to the same full-action script and remained unchanged under zero neural feedback. It did not establish informational self-observation. The next causal-learning substrate needs situations in which the useful, cost-adjusted action **depends on what the public task already tells the agent and what a probe can discover**.

The complete source-locked Agent-Reflex-RL-2K dataset contains 2,550 tasks in 51 independent executable environment families. Source revision: 337c7eebaa3fd56825602d7252000c55a62e27f3. Raw JSONL SHA256: 3fa26f6ea0f8d88f04c87b7996ff2fee24b1778d6798b871bb3cbd84b356606a. The existing seed-4611 grouping by environment ID **and** class-code SHA yields 30 train / 10 development / 11 test families.

The byte-locked source is verified before trial preparation. Computing the grouped split and its no-duplicate-prompt evidence necessarily **reads and hashes** public prompts in all three partitions, including test. Test task texts, declared tool schemas and private verifier instructions are **not exported, printed, examined by the experimental action designer or used for choosing the cohort**. This is a precise distinction: we do not claim test content was never processed by the split algorithm. The live training trial uses only distinct family indices 0, 2 and 3 from the train partition.

## Three predeclared real training tasks

| Source task row | Environment domain | Public intervention target |
| ---: | --- | --- |
| 0 | Subscription administration | Cancel only the correctly identified Alice Chan PureView monthly subscription, then halt related scheduling |
| 2 | Sleep/account administration | Reactivate explicitly identified suspended account USR002 |
| 3 | Dietary profile administration | Create explicitly identified missing restriction DR5 (Low-Carb) |

The full original task descriptions include additional tasks **not completed by this bounded intervention**. Partial terminal reward improvement is not whole-task success.

Each task is independently reset for three repetitions per arm. Arm assignment is randomized in a seeded, family-stratified sequence (seed 2026): stop, public direct action, or live public probe plus conditionally selected action. First-stage action propensity is 1/3. This yields 27 real environment episodes but only **three distinct tasks**, so repeats must not be interpreted as 27 independent unseen tasks. There is no learned controller in this tranche.

The direct arm uses only identifiers explicitly present in the public task. The subscription direct arm abstains rather than inventing the missing subscription ID. The account and dietary direct arms perform one permitted state-changing call. The probe arm first checks the public status or existence of the object; for subscription work it looks up the user's subscriptions, resolves product identity through a selected read call, requires both user_linked and product_linked to be true, then cancels and performs bounded post-cancellation scheduling changes. **Neither source code nor hidden initial state, gold trace, RSD skill or checklist program is ever supplied to the action planner**. Third-party class source runs only inside an existing restricted, nonroot, no-network, read-only Docker container. A different restricted container runs the private checklist after the selected episode terminates. The trusted host bridge transports terminal initial/final state to that checker, never back into the policy.

## Observed outcomes

Initial real replay: [run 43404441390](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/actions/runs/43404441390). All 27 real runs verified, but the subscription arm safely stopped at link validation, because the public API returns separate user_linked and product_linked booleans rather than a generic valid flag. The exact public tool reply—not any private checker source—identified this interface discrepancy. The policy was corrected to require **both** booleans explicitly; its adversarial test refuses cancellation if either is false.

Corrected live replay: [run 43404806219](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/actions/runs/43404806219). All 27 selected-action real episodes and independent private terminal verifications passed.

| Train family | Assigned arm | Mean private reward | Mean real tool calls | Designed utility = reward − 0.01 per call |
| --- | --- | ---: | ---: | ---: |
| Subscription (0) | Stop | 0.2500 | 0 | 0.2500 |
| | Direct / abstain | 0.2500 | 0 | 0.2500 |
| | **Public probe + conditional action** | **0.5000** | **7** | **0.4300** |
| Account (2) | Stop | 0.4615 | 0 | 0.4615 |
| | **Public direct action** | **0.5385** | **1** | **0.5285** |
| | Probe + conditional action | 0.5385 | 2 | 0.5185 |
| Dietary (3) | Stop | 0.2857 | 0 | 0.2857 |
| | **Public direct action** | **0.4762** | **1** | **0.4662** |
| | Probe + conditional action | 0.4762 | 2 | 0.4562 |

These results demonstrate **heterogeneous value for selected intervention packages** on the three specific training tasks. In the subscription task, resolving the missing ID allows a genuine state change and raises reward; direct action cannot safely proceed. In the other tasks, the public description already contains sufficient identifiers; the additional read probe has the same reward but greater tool cost. This is evidence that both probe and no-probe choices can be useful, not evidence that a learned policy can identify them.

The full recorded trace includes chosen tools, hashed observations, exact assignment propensity, actual selected-tool timing, Docker child timing, checker validity/counts and terminal scalar rewards. The unit price of 0.01 per call is a **chosen objective weighting**, not a physical FLOP or energy measurement. The comparison is among **whole probe-plus-action policies**, not a pure causal estimate of information independent of the downstream mutation. An unmeasured or unknown policy would not be entitled to those outcomes at decision time.

## Reproduction and epistemic limits

Sources and jobs:
- experiments/owi_ec005_realtools_family_survey.py: complete source/digest audit, partition grouping, train/dev public description inventory, sealed test export.
- experiments/owi_ec005_realtools_family_public_specs.py: three predeclared train public tasks and declared tool schemas.
- experiments/owi_ec005_realtools_family_prepare.py: rejects held-out/duplicate-family selection; separates public, untrusted environment and private verifier mounts.
- experiments/owi_ec005_realtools_family_public_probe.py: real selected public read calls, never checker access.
- experiments/owi_ec005_realtools_heterogeneous_trial.py: randomized live stop/direct/probe arms, actual conditional tool interactions, private terminal scoring and cost evidence.
- tests/test_owi_ec005_realtools_family_survey.py and tests/test_owi_ec005_realtools_heterogeneous_trial.py: digest mismatch, source/test sealing, duplicate-family rejection, privileged-field exclusion, probe-informed abstention and subscription-link integrity.
- .github/workflows/owi-ec005-realtools-heterogeneous.yml: exact CI replay, 30-day real episode artifact retention.

**Engineering status:** THREE_FAMILY_REAL_INTERVENTION_COST_HETEROGENEITY_OBSERVED.

**Scientific boundary:** OUTCOME_ONLY_REFLECTIVE_CONTROL_NOT_ESTABLISHED. This tranche used three predeclared **train** families only, one source task each, and *scripted* option policies. It does not establish a trained contextual controller, zero/shuffled-information learning advantage, held-out development/test family transfer, unseen fault-mechanism robustness, a computational gain over matched learned/fixed policies, or general introspection.

**Next executable unit:** train a contextual outcome-only controller on diverse real task-action pairs, with actual first- and second-stage propensities and no unchosen outcomes. Compare direct, always-probe, information-ablated, passive and matched-budget baselines across five seeds, then make a predeclared evaluation on a still-sealed independent development family and held-out intervention mechanisms. Do not open the test partition or promote manuscript/release/certification state until those evidence obligations are met.
