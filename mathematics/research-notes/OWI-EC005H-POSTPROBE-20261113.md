# OWI-EC-005H — Real post-probe outcome-only intervention learning

**Grand Challenge Labs — 13 November 2026.** Parent [OWI-EC-005 #466](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/466), after [EC-005G PR #473](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/pull/473).

**Outcome:** BOUNDED_REAL_POSTPROBE_CHOSEN_ONLY_LEARNING_REPRODUCED_5_SEEDS. The broader scientific status remains **OUTCOME_ONLY_REFLECTIVE_CONTROL_NOT_ESTABLISHED**, because a stronger no-probe direct-action baseline outperforms the learner on task-plus-designed-computation cost.

## Scientific question and source custody

EC-005G trained a first-stage decision among STOP, DIRECT and PROBE, but every response-dependent second-stage repair remained scripted. EC-005H instead learns the **second-stage** STOP-versus-UPDATE decision after an actual source-locked public tool call. The learner is a two-option empirical contextual bandit with no private checker source, hidden initial/final environment state, RSD skill, fault ID, reference solution or unchosen action outcome in its training features.

The full upstream Agent-Reflex-RL-2K corpus is pinned at revision 337c7eebaa3fd56825602d7252000c55a62e27f3, with 2,550 tasks, 51 independently grouped environment families, split into 30 training, 10 development and 11 sealed test families. Raw source JSONL SHA256: 3fa26f6ea0f8d88f04c87b7996ff2fee24b1778d6798b871bb3cbd84b356606a.

The experiment exclusively uses original **training-family row 2** (a request to reactivate user USR002 as one part of a sleep-log cleanup task). Full source bytes and partition identity are checked before use. A **privileged fixture preparer**, not the learner, builds three controlled scenarios by copying the source-locked original environment and changing exactly one initial-state field: users.USR002.account_status.

| Controlled initial status | Experimental role | Original upstream task? |
| --- | --- | --- |
| suspended | Training | Yes: original value |
| active | Training | No: artificial one-field intervention |
| closed | Unsupported-state diagnostic after freeze | No: artificial one-field intervention |

The executable class code, all other state entries, advertised tool schemas, public task and **original private terminal checker are unchanged**. The manifest records source and variant state/class/checker digests. These are **not three independent source tasks or environment families**. The public request presumes a suspended account; the already-active and closed variants deliberately alter that presumption for a controlled causal intervention test. Treat this as a mechanistic proof of operation, not natural-distribution generalization.

## Genuinely conditional real execution

Each training episode begins with an independently reset instance of the source-locked external Python class, executed **inside a nonroot, no-network, capability-dropped, read-only Docker child**. The controller sends a real selected check_user_account_status call for the publicly specified user USR002. Only after receiving the actual public result does it choose whether to call update_user_account_status(new_status=active), or finish without updating. Invalid/truncated/wrong-user or unsupported status results cause fail-closed abstention.

The host assigns suspended/active scenarios at equal frequency **but never sends their scenario labels to the bandit decision**; only the actual selected tool reply supplies the context. The host knows scenario identity solely for integrity checks and experimental randomization. On terminal finish, a trusted host bridge forwards the worker's actual initial/final state to an **independent restricted private verifier container**. No privileged information is sent into the chooser or optimizer.

The chosen-outcome estimate for observed status z and executed action a is

\[
\widehat Q(z,a)
  =\frac{1}{N(z,a)}
     \sum_{\{i:Z_i=z,\ A_i=a\}}
       [R_i-\lambda C_i],\qquad \lambda=0.01,
\]

where R is the **actual realized private scalar terminal checklist reward** and C is the number of **actually executed tool calls, including the probe**. The 0.01 price is an explicitly designed per-call proxy, not a measured physical FLOP, memory, energy or model-cost estimate.

Four randomized forced-exploration rounds per **observed** status choose each action once without replacement; logged conditional propensities are 1/2 and then 1. These blocks **do not** have both-action support at every step. Thereafter epsilon-greedy with epsilon 0.20 provides at least 0.10 support for either action. There is no oracle, full-information update, unchosen counterfactual rollout or off-policy correction. A **hand-specified list of permissible tool actions and arguments** remains in place; the learner does not acquire general tool planning or free-form reflective reasoning.

## Five independent seeds: actual terminal evidence

The source-locked proof-of-operation first passed with 40 real training episodes at [run 43430462721](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/actions/runs/43430462721). The complete five-seed experiment passed in [run 43430860383](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/actions/runs/43430860383). Seeds **11, 23, 37, 41 and 53** each executed 72 independently reset real chosen-action training episodes, **360 total**, with a separate private checker on every episode. Each seed then froze its policy and executed real evaluation episodes under true, flipped, pooled zero-status, fixed always-update, fixed abstain, and scripted public-status controls. The evaluator also ran **fixed direct-without-probe and stop-without-probe controls** only after training freeze; none of their unchosen outcomes entered the learner.

All five seeds learned exactly the same observed-status-dependent second-stage policy:

| Seed | Public probe returns suspended | Public probe returns active | Unknown closed |
| ---: | --- | --- | --- |
| 11 | UPDATE | STOP | STOP, fail closed |
| 23 | UPDATE | STOP | STOP, fail closed |
| 37 | UPDATE | STOP | STOP, fail closed |
| 41 | UPDATE | STOP | STOP, fail closed |
| 53 | UPDATE | STOP | STOP, fail closed |

The closed scenario was **never trained**. Its abstention is an explicitly programmed unsupported-state rule, **not learned generalization to a held-out intervention mechanism**. The private checker returned valid results for all three controlled scenarios.

Source-matched terminal results from fresh real evaluation:

| Account initial state | After-probe action | Private terminal reward | Selected tool calls | Designed utility |
| --- | --- | ---: | ---: | ---: |
| Suspended | UPDATE | 0.5385 | 2 | **0.5185** |
| Suspended | STOP | 0.4615 | 1 | 0.4515 |
| Already active | STOP | 0.5385 | 1 | **0.5285** |
| Already active | UPDATE | 0.5385 | 2 | 0.5185 |

The checker contains 13 checklist items. A real account update improves reward by 1/13 when the account is suspended; making the already-active account active again adds no reward. The learner avoids that redundant *second-stage* mutation based on the actual observed status.

### Ablations and stronger fixed comparator

Equal-weight means across the two **controlled training scenarios**:

| Policy | Mean designed utility | Interpretation |
| --- | ---: | --- |
| Learned second stage with true observation | **0.5235** | 1.5 selected calls on average |
| Same frozen policy with flipped status feature | **0.4850** | Actual tool observations unchanged; learner input deliberately reversed |
| Zero-status pooled chosen-outcome estimate | **0.5128** (five-seed mean) | Four seeds always-update: 0.5185; one always-stop: 0.4900; NOT independently retrained |
| Hand-coded public-status rule after probe | 0.5235 | Ties learned policy |
| **Fixed direct update, no probe** | **0.5285** | **Stronger, cheaper end-to-end baseline**, one call |

The actual learned second-stage behavior is sensitive to its real information: the status flip reduces designed utility by **0.0385** compared with the normal policy. The five-seed average gain over the pooled zero-status selector is **0.0107**, but that selector was derived from the learner's own selected training data, **not an independently retrained equal-budget control**.

**Decisive negative:** the best simple direct-without-probe policy achieves **0.5285**, versus the learned post-probe policy's **0.5235**. A direct update is effectively idempotent when the account is already active. Thus paying for the status probe is not instrumentally worthwhile on this source-task-plus-call-price distribution. The experiment has established **bounded response-dependent learning**, but **not** positive task-plus-compute advantage over the strongest fixed no-probe policy. It also does not outperform the hand-coded public-rule baseline.

Physical instrumentation includes actual selected tool wall times, source-worker Docker wall time, separate checker wall time and peak source-worker RSS (approximately 19–20 MiB in these runs). These are real measurements but **not** an integrated physical compute/FLOP, CPU-energy or host-level model cost. The learner is a tiny CPU-only empirical table; there is no claimed Colab GPU, W&B run or hardware energy saving. Docker-start timing variability is not controlled tightly enough for an efficiency certification.

## Reproducibility, custody and limitations

The code is admitted as a bounded scientific experiment, not a release promotion:

- experiments/owi_ec005_realtools_postprobe_discover.py: inspect **public** natural variants from training families only, with development/test tasks sealed.
- experiments/owi_ec005_realtools_postprobe_status_audit.py: privileged source-locked state-path diagnosis; **never** imported or used as a learner feature.
- experiments/owi_ec005_realtools_postprobe_variants.py: authenticate the full pinned corpus, check training partition, create exactly one-field altered state variants, preserve source class, tool declarations and original private checker, write exact provenance digests.
- experiments/owi_ec005_realtools_postprobe_learner.py: genuine conditional public probe -> chosen second-stage action -> separate terminal verifier; chosen-only contextual value estimates, exact behavior propensities, flipped/zero feedback, strong no-probe fixed baselines, actual container and RSS costs.
- tests/test_owi_ec005_realtools_postprobe_discover.py and tests/test_owi_ec005_realtools_postprobe_learner.py: reject held-out-family source selection, private information, incorrect targeted IDs, invalid public replies, wrong source-state change and incorrect chosen-option support.
- .github/workflows/owi-ec005-realtools-postprobe.yml: actual source-pinned live five-seed CI and 30-day per-seed full chosen-action/cost/reward records, without private checker source or environment state in retained artifacts.

**Positive, narrowly supported result:** a second-stage intervention choice can be learned from **actual selected post-probe observations and realized terminal scalar rewards only**, reproduced across five seeds. Unlike EC-005G, the *decision after receiving the tool's live response* is learned, rather than encoded as a fixed response-to-action rule.

**Scientific boundary:** OUTCOME_ONLY_REFLECTIVE_CONTROL_NOT_ESTABLISHED. The same task was artificially varied at one initial-state field; the upstream verifier and hand-authored action interface remain known, and no truly unseen development/test environment, novel mechanism, free-form tool plan, independent matched-budget zero-information learner or physical task-compute improvement has been demonstrated. The controlled closed-state diagnostic is **fixed abstention**, not learned transfer. The parent issue **#466 remains OPEN**; Atlas 80-chapter manuscript, public release and mathematical certification state are unchanged.

**Next executable science:** introduce *potentially harmful wrong repairs*, e.g. source-locked valid versus invalid subscription association links, with a private checker that genuinely penalizes unjustified cancellation. Train a post-observation repair/abstain selector across multiple naturally distinct training task instances. Reproduce 5+ independent seeds, then freeze the feature/tool adapter before independent development-family testing and held-out perturbation mechanisms. Include **separately trained** zero/shuffled-information controls, strongest no-probe and task-aware fixed controllers, and physical model+tool MAC/latency/RSS accounting. Do not treat additional repetitions of this same idempotent update as scientific closure.
