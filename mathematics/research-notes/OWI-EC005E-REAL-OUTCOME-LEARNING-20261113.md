# OWI-EC-005E — Real outcome-only neural option learning

**13 November 2026. Parent:** [OWI-EC-005 #466](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/466). **Status:** bounded five-seed real chosen-outcome training completed; scientific reflective-control acceptance **not established**.

## Research problem and exact information boundary

The previous [PR #470](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/pull/470) used a scripted public-task planner to complete a series of genuine state-changing tool calls in an isolated executable environment, moving private terminal reward from 0.1538 to 0.3846. The present tranche tests whether a small neural controller can **learn its own intervention-gating decisions from realized terminal outcomes**, without access to the private checklist or unexecuted counterfactual branches.

The goal-oriented public-task planner still supplies the detailed tool arguments and tool sequence. The *new* trained actor controls exactly three binary decisions: stop or begin public inspection; stop or create a report after the actual public lookups; and stop or continue after the generated new-report identifier has been recovered from an actual selected public read tool. The actor is **not** a language model and does not learn tool-argument planning. Each environment episode runs only the chosen actions, inside the existing nonroot, no-network, capability-dropped, read-only Docker container. Only after finish does the trusted host bridge the actual initial/final state to a second, independent no-network container running the source-pinned private terminal checker. No private state, verifier code, reference answer, RSD reflection skill, unchosen intervention outcome, or fault ID enters actor state or its optimizer.

The neural actor has 11 input features derived from public observations and decision stage; a 16-unit tanh hidden layer; and one Bernoulli output (209 trainable parameters). Training uses an epsilon-supported Bernoulli with epsilon 0.20, giving both choices support at least 0.10. Every chosen action and its exact behavior probability is recorded. Optimization updates *only after a single realized terminal scalar reward*, with an exponential moving baseline, REINFORCE log-probability gradient, entropy regularization at 0.002, and Adam learning rate 0.024.

The explicitly designed episode utility is terminal-checker reward minus 0.01 times the **number of actually selected tool calls**. This is a *chosen price* rather than a physical FLOP/energy estimator. The bridge additionally records real child wall times and actual tool-invocation times. No unchosen branch is run to compute the training gradient.

## Exact source and replay

The original corpus has 2,550 tasks and 51 executable environment families, already split into source-disjoint 30/10/11 training/development/test families. This experiment only uses **one pinned task**, row 1, to validate actual outcome-only neural learning.

- Source: dongguanting/Agent-Reflex-RL-2K at immutable revision 337c7eebaa3fd56825602d7252000c55a62e27f3.
- Original full JSONL SHA256: 3fa26f6ea0f8d88f04c87b7996ff2fee24b1778d6798b871bb3cbd84b356606a.
- Public task SHA256: 1cf6a7891a1c9ba68afd06a45bc04389ae0e89e9131d4500146cf66a125e0d0e.
- Actual training: seeds **11, 23, 37, 41, 53**, each 72 fully chosen real episodes, **360 real training episodes** total.
- Each seed additionally runs four greedy evaluation episodes, four neural-gate zero-feedback evaluation episodes, and three matched fixed-policy baseline episodes, all executing the source-pinned environment and independent private terminal checker.

The first one-seed attempt reached all 72 real training episodes, but evidence serialization relied on unavailable NumPy; this was repaired by pure-PyTorch-to-JSON digest encoding. Full single-seed replay and evidence retention passed in [run 43400311446](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/actions/runs/43400311446). Five independently trained and evaluated seed jobs plus neural boundary tests all passed in [run 43400725730](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/actions/runs/43400725730). The numerical evidence below comes from that actual run.

## Five-seed result

| Seed | Trained terminal reward | Trained tool calls | Designed utility | Utility with zero neural feedback features | Trained parameter L1 change |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 11 | 0.3846 | 8 | 0.3046 | 0.3046 | 56.8893 |
| 23 | 0.3846 | 8 | 0.3046 | 0.3046 | 58.2659 |
| 37 | 0.3846 | 8 | 0.3046 | 0.3046 | 41.4625 |
| 41 | 0.3846 | 8 | 0.3046 | 0.3046 | 58.0117 |
| 53 | 0.3846 | 8 | 0.3046 | 0.3046 | 52.3950 |

**All five neural actors changed their actual parameters through on-policy outcome-only gradient updates**, and all five selected continue at all three gates in greedy evaluation. The result is reproducible *learning of the best fixed continue strategy on the repeated task*.

| Source-matched baseline | Real tool calls | Private reward | Designed utility |
| --- | ---: | ---: | ---: |
| Immediate stop | 0 | 0.1538 | 0.1538 |
| Three public read-only calls | 3 | 0.1538 | 0.1238 |
| Fixed scripted full-action control | 8 | 0.3846 | 0.3046 |
| Learned neural option gates, every seed | 8 | 0.3846 | 0.3046 |

The learned policies exceed the stop/no-repair baseline under the *selected* tool-call charge, but **do not exceed the matched fixed full-action baseline**. They show neither adaptive abstention nor physical compute savings. The numeric evaluation cohorts are independent resets of *the same task*, not unseen-task or unseen-environment generalization.

## Negative self-observation result

A neural-gate feedback ablation replaces the *learned gate's* post-observation feature indicators with zero, while retaining the true public tool observations in the **underlying scripted planner** (which needs them for valid tool arguments). That is a deliberately limited diagnostic: it does not deny information to the complete tool agent. All five learned gate policies behave identically under this ablation, with unchanged eight calls and unchanged utility 0.3046.

**Interpretation:** the neural gate demonstrably optimizes the task's fixed continue-versus-stop tradeoff from chosen terminal rewards, but it **does not demonstrate that access to observation information is causally useful for the learned decision rule**. The task is static and full-action continuation is advantageous. This is a negative scientific result for the hypothesized emergence of epistemically useful self-observation *in this experiment*, not a general impossibility theorem.

## Reproducible artifacts and outstanding obligations

- Implementation: experiments/owi_ec005_realtools_outcome_learner.py; 209-parameter actor, three sequential actual choice gates, propensity/trace recording, task plus selected-call objective, real verifier outcomes.
- Adversarial tests: tests/test_owi_ec005_realtools_learner.py; public-only features, exact chosen-action log probability, epsilon support, real terminal-gradient step, state/stage and ablation boundaries.
- Workflow: .github/workflows/owi-ec005-realtools-learning.yml; pinned CPU PyTorch 2.10.0, locked source selector, real two-container execution, five independent seed jobs, immutable per-seed output artifacts retained for 30 days.
- The 5 model-digest/trace artifacts are linked from the completed Actions run. The source lock and this numerical result summary are durable repository content. No private source or verifier is uploaded in the artifact.
- CPU training is sufficient for this small model; no GPU run was performed or claimed. W&B online logging was **not** performed; reproducible JSON episode traces are the actual evidence.

**Engineering disposition:** REAL_OUTCOME_ONLY_NEURAL_OPTION_OPTIMIZATION_REPRODUCED_5_SEEDS.

**Scientific disposition:** INFORMATIONAL_SELF_OBSERVATION_ADVANTAGE_NOT_ESTABLISHED. Issue #466 remains **OPEN**, and Atlas 80-chapter manuscript, publication and mathematical certification state are unchanged.

The next meaningful experiment must change the *task and information structure*. Use multiple source-locked environment families and held-out tool/fault interventions, including cases where probe results justify doing nothing and cases requiring different repairs. Make alternatives genuinely consequential and heterogeneous in execution price. Train and evaluate across those regimes with 5+ seeds, passive/fixed compute-matched baselines, shuffled/zero information, recorded action support, source-family holdout and physical tool/model times. Merely adding more seeds to this repeated task would not establish reflective control.
