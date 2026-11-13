# OWI-EC-005G — Real contextual outcome-only option learning

**Grand Challenge Labs / 13 November 2026**

**Parent scientific issue:** [OWI-EC-005 #466](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/466). **Predecessor:** [PR #472](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/pull/472). **Scientific status:** a narrow public-context intervention choice has been learned from actually chosen terminal outcomes, but outcome-only *reflective self-observation* and the acceptance criteria of issue #466 remain unestablished.

## Rationale

EC-005F showed heterogeneous real task-option value in three independently source-locked training environment families. A subscription task required public lookup before safe cancellation; account reactivation and dietary-restriction creation had fully specified public identifiers, making additional probes unnecessary. This tranche tests whether a policy can learn **the option choice**, instead of using a hand-specified family-to-option routing rule.

The executable option procedures are **still hand-authored**. The learner selects only among STOP, PUBLIC DIRECT, and PUBLIC PROBE WITH CONDITIONAL ACTION. It does not learn tool arguments, free-form language reasoning, error recovery, or the response-dependent repair sequence. The fixed procedure implementing the probe's follow-up actions is itself an important capability provided to the learner. Consequently, success cannot be called general reflective cognition.

## Provenance and independent information boundaries

Source is the same pinned 2,550-task Agent-Reflex-RL-2K JSONL at immutable revision 337c7eebaa3fd56825602d7252000c55a62e27f3, raw SHA256 3fa26f6ea0f8d88f04c87b7996ff2fee24b1778d6798b871bb3cbd84b356606a. The preexisting grouping uses BOTH environment IDs and executable class-source digests, yielding 30 train, 10 development and 11 sealed test families.

Two training task/family rows, **0 and 2**, supply learning trajectories. A distinct training-partition row **3** is excluded from all outcome updates. Its public task and features are first opened by the learner program **after training is frozen**. This is a prospective parameter-update holdout, **not a fully blinded or independent test-family evaluation**: row 3 and its hand-authored tool procedure were already inspected in EC-005F when constructing the research substrate. The actual development and test partitions remain unevaluated.

All task-specific identifiers and tool parameters are obtained from public task text or genuinely selected tool replies through the preexisting scripted planner. The actor's only input is a *hand-engineered public affordance*: whether a valid direct option can be constructed from the public task and declared tool interface. It receives **neither environment-family ID nor private verifier/state**, but the pre-authored planner uses known family-specific rules to derive this affordance. This is not learned semantic interpretation of an unfamiliar task.

Every chosen tool action is executed in the established untrusted-source Docker jail: nonroot, no network, read-only filesystem, capabilities dropped, bounded CPU/memory, no host credentials. A **separate** restricted verifier container runs checklist source only after episode termination; initial and final environment states pass through the trusted host bridge, never into the actor's features. Only the delayed realized scalar terminal reward, the cost of actually chosen tool calls and logged action probability are supplied to the optimizer. There are no training-time rollouts or counterfactual scores for unchosen arms.

## First learner: neural REINFORCE negative result

An initial **12-parameter contextual linear-softmax neural actor** was trained with Adam/REINFORCE and epsilon-supported sampling on two training families for 96 genuine chosen real episodes (seed 11). Its features contained the public direct-action feasibility bit and intercept; zero and shuffled-feature controls were evaluated after training. The completed [first exact-head run 43414296473](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/actions/runs/43414296473) demonstrated nonzero learned parameter updates and valid chosen-only terminal reward training.

It nevertheless chose **probe for all three task families**, including the account and withheld dietary task where a direct action has equal task reward with lower tool cost. Removing or shuffling the context did not change its selected action. This was a **negative optimization / information-use result**, not evidence of reflective self-correction. Do not silently replace this result with the successful estimator below.

## Second learner: chosen-only contextual empirical bandit

The independent estimator uses a separate table of three actual *chosen-action* utility means for each of the two public affordance categories. During the first three cycles per context, it draws a fresh random permutation of the three options, executing one and observing a real terminal reward per episode. Its **conditional** chosen-option propensities during each without-replacement cycle are 1/3, 1/2 and 1. These forced exploration blocks guarantee every option is actually sampled, but **do not have positive support for every arm at every conditional decision**. There is no off-policy extrapolation claim based on those blocks.

After those cycles the actor uses epsilon-greedy sampling with epsilon 0.24, which gives each of the three options unconditional behavior support at least 0.08 per decision. Its empirical utility for a context/action pair is the arithmetic mean of *only the executed episodes assigned that pair*. The frozen policy selects the option with the highest such mean. Task price is the same explicitly chosen 0.01 per selected tool call from EC-005F; this is not hardware FLOPs or energy.

This simple estimator changes the optimization mechanism, not the intervention substrate. It does not implement a neural self-model or a learned response-dependent follow-up policy. Unlike the first neural actor, it gives direct empirical identification of the three action options under repeated, deterministic tasks.

## Five independent actual source-locked runs

The completed [five-seed run 43415686435](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/actions/runs/43415686435) used initialization/action sampling seeds **11, 23, 37, 41, 53**, with **72 genuinely chosen real episodes per seed**, totaling **360 training episodes**. Each seed additionally executed source-pinned post-training evaluations on all three tasks under normal, zero-context pooled and shuffled-context conditions (2 real episodes per condition), plus three fixed-policy baseline episodes per task. This is another 135 real evaluator episodes over the five seeds. The original code and full per-seed chosen actions, propensities, rewards, actual tool and environment/verifier wall times are retained in separate Actions artifacts.

All five runs made **identical frozen choices**, although their exploratory action counts differed:

| Seed | Subscription: no public direct target | Account: public direct target | Withheld dietary family |
| ---: | --- | --- | --- |
| 11 | Probe | Direct | Direct |
| 23 | Probe | Direct | Direct |
| 37 | Probe | Direct | Direct |
| 41 | Probe | Direct | Direct |
| 53 | Probe | Direct | Direct |

The chosen-only estimates were supported by at least three actual samples per arm/context in every seed; no checker or unchosen action reward was available during those updates.

### Terminal values and context ablations

| Source row | Normal learned option / utility | Zero-context pooled option / utility | Shuffled-context option / utility | Fixed always-probe utility |
| ---: | --- | --- | --- | ---: |
| 0: subscription | Probe / **0.4300** | Direct (abstains) / 0.2500 | Direct (abstains) / 0.2500 | 0.4300 |
| 2: account | Direct / **0.5285** | Direct / 0.5285 | Probe / 0.5185 | 0.5185 |
| 3: withheld dietary | Direct / **0.4662** | Direct / 0.4662 | Probe / 0.4562 | 0.4562 |
| Equal-task mean | **0.4749** | **0.4149** | **0.4082** (rounded) | **0.4682** (rounded) |

The zero-context evaluation uses an option selected by pooling the **actually chosen training observations** across both contexts; it is **not a separately retrained equal-budget zero-context policy**. The shuffled-context evaluation supplies the other publicly derived feature category to the *frozen choice policy* while leaving the underlying fixed tool planner's true public task intact. These ablations demonstrate dependence on the engineered public option-availability feature, not dependence on hidden state or learned interpretation of probe results.

For these three tasks, normal context improves the mean designed utility by **0.0600** over the pooled zero-context selector and approximately **0.0667** over shuffled context. Relative to the stronger **fixed always-probe** controller the advantage is only **about 0.0067**, entirely explained by avoiding one unnecessary call in each of the account and dietary tasks. The learned policy matches the hand-chosen best option for each of the three task instances; **it does not outperform that hindsight, task-specific best fixed option**.

Repeated episodes of the same initial task instance yield almost deterministic scores. Five independently sampled training runs do NOT constitute statistical evidence over 360 independent tasks; there are only two task instances in training and a single previously engineered holdout family in evaluation. No inferential confidence interval, broad generalization estimate, or absolute physical-compute improvement claim follows.

Actual selected tool elapsed time and container wall times are recorded in each artifact, including separate environment and checker costs in the evaluation outputs. The reward-minus-0.01-per-call figures above are an **explicit experimental cost proxy**, not full processor time, FLOPs, energy or hardware efficiency; Docker cold-start effects and the tiny actor's overhead must be accounted for in any later compute-optimality claim.

## Code and independent checks

- experiments/owi_ec005_realtools_contextual_learner.py: public-feasibility contextual 12-parameter neural softmax, chosen-only REINFORCE, first-seed negative result, delayed holdout opening, matched baseline and feature ablations.
- experiments/owi_ec005_realtools_contextual_bandit.py: contextual chosen-outcome empirical value estimates, balanced without-replacement exploration, correct conditional propensities, epsilon-greedy support, delayed holdout, real terminal checker and counterfactual-free training.
- tests/test_owi_ec005_realtools_contextual_learner.py and tests/test_owi_ec005_realtools_contextual_bandit.py: public-field nonleakage, strict affordance, exact selected-action probabilities, contextual permutation independence, neural gradient, negative-context and support invariants.
- .github/workflows/owi-ec005-realtools-contextual.yml: pinned CPU PyTorch 2.10.0 for the neural model/feature extractor; pinned full dataset-source verification; isolated external-code and checker execution; deterministic seed matrix with retained evidence. The bandit itself is computationally trivial; neither a GPU run nor W&B upload is claimed.

## Adjudication, insufficiencies, next frontier

**Engineering evidence:** REAL_CONTEXTUAL_CHOSEN_ONLY_OPTION_SELECTION_REPRODUCED_5_SEEDS.

**Positive narrow result:** a chosen-outcome learner can exploit a *hand-engineered public availability feature* to choose between information gathering and direct action, and the chosen policy has greater designed utility than always probing on two of three tasks. The policy's behavior changes under context ablation. The withheld family is source-disjoint from the two training families, but its scripted procedure was already designed in the predecessor experiment.

**Scientific acceptance:** OUTCOME_ONLY_REFLECTIVE_CONTROL_NOT_ESTABLISHED. This is **not** learned causal self-observation or a model that predicts its own errors. The probe outcome is processed by the *scripted* plan, not learned by the bandit. There is no true unseen development/test family, no new tool planner, no held-out intervention-mechanism acceptance, no persistent/coupled fault evaluation, no full equal-budget zero-information retraining, and no verified gain over a compute-matched adaptable policy in physical FLOPs, memory and latency. Consequently, parent issue #466 remains **OPEN** and there is no Atlas 80-chapter release, publication or mathematical certification promotion.

The next required research unit must learn **post-observation** interventions with real alternative repairs and explicit no-action regimes on multiple independent tasks within each source family. Freeze the feature extractor and tool-interface adapter *before* opening any held-out development family, then evaluate under new fault/intervention mechanisms. Include fully retrained zero/shuffled-information policies, passive telemetry and strongest matched fixed policies, at least five independent seeds, and measured model+tool physical costs. A small single-GPU model with W&B logging is appropriate once free-form semantic tool choice is trained; further repetition of these same three scripted cases is not.
