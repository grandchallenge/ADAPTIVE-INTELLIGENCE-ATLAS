# OWI-EC-003 — Neural Representational Dynamics and Causal Self-Correction

**Grand Challenge Labs · experiment executed 2026-11-12**  
**Status:** bounded *neural* positive result on an intentionally simple synthetic sequence task; mixed out-of-distribution result; no sapience or spontaneous general metacognition claim.  
**Parent theory:** [OWI endogenous epistemic control](OWI-ENDOGENOUS-EPISTEMIC-CONTROL-20261112.md) and [active self-probing](OWI-ACTIVE-SELF-PROBING-20261112.md).  
**Executable:** [experiments/owi_neural_dynamics_pilot.py](../../experiments/owi_neural_dynamics_pilot.py).

## Claim and hypothesis

Does a **trained neural sequence system**, without providing hidden fault identities to the observer, contain internal representations sufficient for a separate learner to identify causal response differences between alternate repairs and select helpful corrections?

The finite-state OWI-EC-002 result alone cannot answer this because its fault states and observation laws are hand specified. This experiment moves the causal process into a trained GRU's internal hidden-state transitions. It does **not** test whether unaugmented task-only training spontaneously creates metacognition; the action-value reader is explicitly trained.

## Core, environment and interventions

- Two separately learned GRU branches, hidden width 14; seven 2-channel binary input tokens per episode. Each branch learns to output whether its corresponding channel contains a strict majority of positive tokens. The two binary targets are not given to the self-estimator as inputs.
- Freeze the trained GRUs and classifiers before collecting diagnostic data.
- At the last recurrent step, corrupt **exactly one** of the two hidden states with probability 0.8 (each branch equally likely); leave both untouched with probability 0.2.
- Only **Gaussian** additive corruption (sigma 2.3) appears in the randomized causal-action training distribution.
- Actions: no repair; recompute the trusted final recurrent update for branch A; recompute branch B; recompute both. Each branch repair costs **0.035 loss units**.
- True action outcomes are computed by **actually re-executing the frozen GRU's trusted final transition** from the penultimate hidden state and final input. A runtime equality check establishes agreement with an uncorrupted forward pass. Outcomes for all actions are available to the experiment's *evaluator*; training discloses only the one action's outcome selected uniformly at random for each episode.
- Observable self-telemetry includes each branch's current *corrupted* hidden state, trusted penultimate state, current output logit, hidden norm and temporal difference norm. Crucially it excludes fault identity, clean final state, repair outcome, and target label.
- The learner is a 2-layer 64-unit MLP predicting expected **loss per action**, trained from the randomized intervention log. It chooses the minimum predicted-loss action on evaluation episodes.
- An independent **self-supervised** linear dynamics predictor is also trained from clean pairs (penultimate hidden state + final input, next hidden state), without task or fault labels. Its residuals form a compact alternative telemetry channel; the reported loss for this arm includes a separately declared **0.008 probe cost**.

The mechanism is best understood as learned **task-relative self-diagnosis with causal repair selection**. Diagnostic data may make the injected abnormality easy to identify; nothing here establishes a domain-general account of the agent's own thought.

## Reproduction and provenance

Executed locally with Python 3.13 and **PyTorch 2.10.0+cpu**, one CPU thread, seeds **1,2,3,4,5**. Per seed: 330 mini-batch steps for the GRU core, 22,000 randomized logged action/outcome examples, 650 optimizer steps per Q estimator, 750 self-supervised updates for each dynamics predictor, and 7,000 held-out evaluation episodes per mechanism. W&B is optional in the CLI, not claimed for these local runs.

~~~bash
python experiments/owi_neural_dynamics_pilot.py \
  --seeds 1,2,3,4,5 --core-steps 330 --q-steps 650 \
  --q-train 22000 --test 7000 --output neural-results.json
~~~

**Evaluation mean loss (task mistakes averaged over the two bits + declared repair/probe costs):**

| Policy | Trained Gaussian corruption | Held-out dropout | Held-out signflip | Held-out permutation |
|---|---:|---:|---:|---:|
| No repair | 0.057100 | 0.030086 | 0.399029 | 0.209257 |
| Fixed repair A | 0.063357 | 0.050186 | 0.232886 | 0.114629 |
| Repair both | 0.070000 | 0.070000 | **0.070000** | 0.070000 |
| Learned logits-only reader | 0.034601 | 0.033144 | 0.311245 | 0.048035 |
| Self-supervised dynamics residual + logits, including declared probe charge | 0.032993 | 0.040592 | 0.283609 | 0.051964 |
| Shuffled full telemetry | 0.059321 | 0.040059 | 0.288758 | 0.142384 |
| **Learned full internal-telemetry controller** | **0.016992** | **0.024431** | 0.119543 | **0.035727** |
| Privileged per-episode oracle (not deployable) | 0.003997 | 0.002106 | 0.027932 | 0.014648 |

The five frozen GRU cores each reached 1.0 accuracy on their separate 4,096-example uncorrupted checks (the binary-majority task is deliberately easy). Relative to no repair, the learned full-telemetry reader reduced loss by **70.2%** under the trained Gaussian corruption. Mean paired across-seed improvement was **0.040108**; a descriptive 95% Student-t interval using five independently initialized seeds is approximately **[0.03688, 0.04334]**. This interval describes variation over these five model seeds; it is not a distribution-free generalization guarantee.

Under held-out signflip, learned control improves dramatically over no repair, **but is worse than repairing both branches** (0.119543 vs 0.070000). Thus there is **no claim of universally cost-optimal transfer**. Held-out dropout offers only a small improvement over doing nothing, and permutation shows substantial per-seed variability.

The explicit self-supervised dynamics-prediction arm does **not** outperform the richer raw-hidden-state model and does not consistently outperform the logits-only model after the probe charge. This is an important negative finding: *learning to predict one's own next hidden state does not automatically supply a superior corrective policy*.

## Controls and distinctions

1. **Randomized action intervention:** a fault may be correlated with uncertainty; assigning corrective actions uniformly independently of state identifies the action-specific response on the training support, rather than using observational action correlations.
2. **Hidden fault identity:** injected branch index is unavailable to every learned controller; retained solely for auditing.
3. **Shuffled telemetry:** destroys sample-specific internal evidence but preserves its marginal distribution. The resulting policy loses most of the improvement in the trained regime.
4. **Logits-only matched learner:** receives the same number of randomized training episodes and a similar-size action-value network, but only sees two output logits rather than hidden trajectories.
5. **Held-out mechanisms:** dropout (85% masking), full hidden-state signflip, and deterministic latent-coordinate permutation never appear during Q training.
6. **Privileged oracle:** scores the best intervention based on all counterfactual outcomes and serves only as an upper bound on achievable repair.
7. **Actual neural repair:** each branch's corrected last transition is re-executed, not produced by a hand-coded fault classification.
8. **Clean-false-positive cost:** 20% of all evaluation episodes have no fault, and the learned policy incurs unnecessary repairs on a subset of those episodes.

## Strong limitations and falsification

- **Task simplicity:** seven-bit majority can be learned very accurately and does not demonstrate advanced reasoning or sapience.
- **Intervention locality:** perturbations act only on the final recurrent hidden states, and repair restores the trusted final step. Errors earlier in the sequence, corrupted checkpoints, catastrophic memory loss, and coupled faults are not covered.
- **Self-model is supervised:** internal representations are task-trained; the causal observer additionally learns from randomized action outcomes. The experiment does not establish spontaneous introspection from the task objective alone.
- **Non-equivalent compute budgets:** repair costs and probe charge are defined *loss-unit proxies*, not physical FLOPs/energy/latency. Q-network inference itself is not charged. The measured trained-regime gain over no repair is 0.040108 loss units per episode, so a previously unaccounted controller cost greater than that amount would erase the demonstrated economic benefit.
- **No invariance proof:** held-out permutation tests a specific latent transformation, not a function-preserving network reparameterization. The latter requires coordinated adjustment of adjacent weights.
- **OOD failure:** signflip result fails against the always-recompute-both policy. This directly limits the reflective generalization claim.
- **No formal statistical guarantee for neural OOD:** reported mean differences are exploratory and hypothesis generating, not a proof of robust metacognition.

## Next bounded research obligations

1. Replace the synthetic loss-unit cost proxies with measured FLOPs, memory, and latency; compare with a compute-matched policy using the same controller FLOPs for task reasoning.
2. Add **nonterminal, persistent perturbations** to recurrent updates and recoveries: hidden-state noise that propagates through several steps, branching errors, and corrupted checkpoints.
3. Evaluate a *learned active probe selection policy* that sometimes purchases a self-prediction measurement before choosing repair, with honest probe computation cost.
4. Test function-preserving conjugations of the recurrent hidden space and an exactly specified held-out intervention family; prevent mechanism-ID leakage through telemetry.
5. Change task family and sequence length; establish whether self-model information transfers across task semantics or is merely detecting a final-state outlier.
6. Advance to single-GPU logged training with multi-seed CLI and W&B under GCL conventions; do not promote this pilot to a general sapience claim.

**Disposition:** a real trained-neural causal-self-correction pilot with mixed OOD results, held as a separate research note and executable. It does not alter the canonical Atlas 80-chapter ledger or certification standing.