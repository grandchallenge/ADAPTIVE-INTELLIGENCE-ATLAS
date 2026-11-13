# OWI-EC-004 — Jointly Learned Computation, Endogenous Probing, and the Online-Credit-Assignment Boundary

**Grand Challenge Labs · 2026-11-12/13 UTC**  
**Disposition:** bounded neural experimental research note; *exploratory*, not a certified mathematical result or a new Atlas canonical chapter.  
**Parents:** [OWI endogenous epistemic control](OWI-ENDOGENOUS-EPISTEMIC-CONTROL-20261112.md), [OWI-EC-002 active probing](OWI-ACTIVE-SELF-PROBING-20261112.md), and [OWI-EC-003 neural self-dynamics](OWI-NEURAL-SELF-DYNAMICS-PILOT-20261112.md).  
**Executable:** `experiments/owi_ec004_core.py`, `owi_ec004_train.py`, `owi_ec004_onpolicy.py`, `owi_ec004_summarize.py`; continuous integration: `.github/workflows/owi-ec004.yml`.

## Question and answer

Can a neural sequence system **learn to inspect and regulate its own computations from a task-and-computation objective**, without explicit fault-identity labels, hand-coded diagnosis rules, or auxiliary self-model prediction targets?

**Bounded positive:** yes, in a controlled two-branch recurrent environment, when training evaluates the task consequences of *all candidate cognitive interventions*. On five independent seeds, an active summary-telemetry controller learns to use a costly recurrent self-probe and reduces expected task-plus-computation loss relative to a passive summary-telemetry controller.

**Decisive negative:** learning the same controller from *only the chosen action's observed outcome* using a simple REINFORCE optimization procedure **fails** in all five seeds. Each learned policy defaults to recomputing both branches. Thus the experiment does not establish that ordinary online experience spontaneously produces metacognition.

## Exact training model

- Task: two parallel 9-token binary sequences; predict whether each has a strict positive majority.
- Base model: two trained GRU branches, hidden width 12. Per seed, each branch is pretrained for 250 Adam steps and reaches 100% accuracy on 4,096 fresh uncorrupted binary-majority checks.
- Fault: with probability 0.8, perturb one branch uniformly at random; otherwise no perturbation. Add Gaussian noise with standard deviation 2.5 **after the first of the final three recurrent steps**, and allow the corruption to propagate through the two remaining steps. Ground-truth fault identity is *not* accessible to a learned controller.
- Corrective action set: no recomputation, recompute branch A, branch B, or both; each repair reruns the **three actual GRU steps** from a trusted preceding checkpoint.
- Optional self-probe: rerun one selected branch's three-step suffix, observe the RMS difference between its corrupted hidden state and trusted replay, and cache the replay to avoid charging twice for that branch. The controller may choose no probe, probe A, or probe B.
- Passive diagnostic channels: **summary** (two logits and two hidden-state norms), or **rich** (those quantities plus corrupted hidden states and checkpoint-relative information). Neither channel contains the fault ID, task target, counterfactual outcomes, or an unrevealed trusted final state.
- Cost objective: binary cross-entropy averaged over the two sequence outputs, plus 0.035 **normalized loss units** for every distinct trusted suffix replay and 0.005 normalized units for controller operation. The proxy cost is *not* a measured FLOP, energy, or latency charge.

The evaluation-time policy observes only its chosen probe's outcome; it cannot inspect unchosen probes' results. The vectorized experiment implementation nevertheless executes all possible trusted suffix replays internally to construct training/evaluation counterfactuals and audit task outcomes. Hence **reported compute savings are conditional virtual charges, not measured hardware savings**.

## Joint objective and strong training assumption

Let \(s_\theta\) be the internal telemetry of the task-trained recurrent model, \(p\) a probe decision, \(q_p\) the resulting probe observation if performed, and \(a\) a repair action. The exact expected task-plus-compute objective optimized during training is

\[
J(\theta,\phi)
= \mathbb E\left[
\sum_p \pi_\phi(p\mid s_\theta)
\sum_a\pi_\phi(a\mid s_\theta,q_p)
\big\{\ell(\hat y_{\theta,p,a},y)+\lambda C(p,a)+c_\phi\big\}
\right],
\]

with an annealed policy-entropy exploration term during training. All probe and repair **counterfactual task outcomes** are enumerated to differentiate this objective. Their scalar task losses are *not* diagnostic-label or self-model targets, but they provide privileged full-information feedback unavailable to an ordinary deployed agent.

Training is a controlled curriculum, *not* spontaneous task-only emergence: pretrain the GRU; optimize the controller for 1,200 steps with the GRU temporarily frozen (uniform probe exploration for half the controller phase and annealed entropy); then **jointly fine-tune both** for 100 steps on the same task-and-compute objective. Evaluation uses deterministic policy argmax.

The comparators share the same architecture, training procedure, seeds, task distribution, repair catalogue and compute-charge schedule, except for the explicitly varied telemetry/probe affordances. No fault identity supervision is used.

## Five-seed results: in-training Gaussian fault

Five seeds (1–5); 4,000 fresh examples per seed, policy and condition; 20 jointly fine-tuned models in four arms. Lower objective is better. All five clean pretrained GRU cores reached 100% on the specified check.

| Policy | Mean charged objective | Probe rate | Mean distinct suffix replays |
|---|---:|---:|---:|
| Fixed recompute-both baseline | ~0.0717 | — | 2.000 |
| Passive, summary telemetry | 0.064680 | 0% | 1.651 |
| **Active, summary telemetry** | **0.053109** | **100%** | **1.328** |
| Passive, rich telemetry | 0.048365 | 0% | 1.081 |
| Active, rich telemetry | 0.046681 | 72.1% | 1.068 |

Paired active-summary versus passive-summary improvement: \(0.011571\) loss units, descriptive 95% Student-t interval \([0.010267,0.012876]\) over five independent seeds. The active-summary improvement appears in **all five seeds**. When the diagnostic probe's result is forcibly zeroed, the active-summary policy's loss increases by approximately 0.0170; sample-shuffled telemetry destroys substantially more of the advantage. These are ablations of the learned policy, not an independent causal identification theorem.

**Important distinctions:** summary-telemetry agents **always** purchase a probe; they learn *how to use the acquired information*, not a selective probe-or-not gate. The richer active policies sometimes decline probing (~28%), but the resulting improvement over the rich passive agents (0.001684) is small under the declared proxy and does not establish compute efficiency on real hardware. All active-summary agents also unnecessarily repair a branch on clean examples. Reflective *restraint* remains immature.

## More realistic compute sensitivity

The 0.005 controller overhead is not a FLOP measurement. As a stress test, count approximate dense multiply-accumulate operations: three-step GRU replay plus output head ~1,416 MACs; active-rich controller ~1,380, passive-rich ~680, active-summary ~340, passive-summary ~160. Set each policy's fixed overhead equal to \(0.035 \times \mathrm{MAC}_{\rm policy}/1416\), preserving the original charge per replay.

| Policy | Original objective | MAC-proxy sensitivity |
|---|---:|---:|
| Active rich | 0.046681 | 0.075792 |
| Passive rich | 0.048365 | 0.060173 |
| **Active summary** | **0.053109** | **0.056513** |
| Passive summary | 0.064680 | 0.063635 |
| Fixed recompute both | ~0.0717 | ~0.0717 |

Thus the purported rich-telemetry active advantage **does not survive** this plausible overhead reweighting. The active-summary advantage over passive-summary **does** (~0.007122). MAC proxies exclude nonlinear operations, memory traffic, scheduling and actual hardware timing. This is sensitivity analysis, **not** a hardware-compute result.

## Held-out disturbances and transfer

Training exposes only Gaussian faults. Held-out transformations include 85% hidden-state masking, sign reversal, coordinate rolling, and smaller-amplitude Gaussian noise. Mean charged losses are:

| Mechanism | Active rich | Passive rich | Active summary | Passive summary | Fixed both (~) |
|---|---:|---:|---:|---:|---:|
| Gaussian (train) | 0.04668 | 0.04837 | 0.05311 | 0.06468 | 0.0717 |
| Dropout (held out) | 0.07061 | 0.07432 | 0.08221 | 0.10146 | 0.0717 |
| Sign reversal (held out) | 0.11316 | 0.13209 | 0.08183 | 0.11295 | **0.0717** |
| Coordinate roll (held out) | 0.07607 | 0.08053 | 0.08273 | 0.09782 | **0.0717** |
| Small noise (held out) | 0.05882 | 0.06124 | 0.07450 | 0.07913 | 0.0717 |

The generalization boundary is substantial. In particular, under sign reversal, **every active-rich run is worse than always recomputing both**. Sequence length 5 and 13, with no retraining from length 9, retained a narrow active-summary advantage over passive summary and fixed-both, but this tests nearby lengths of the *same* elementary task, not transfer to new cognitive domains.

## On-policy outcome-only comparator: a negative result

A separate active-summary controller was optimized by REINFORCE from the **actually sampled** probe and repair's downstream task loss plus compute charge. A uniform-probe first-half curriculum and annealed entropy encourage exploration. It sees neither fault labels nor unchosen counterfactual task outcomes, and its pretrained GRU stays frozen in this control. After 1,500 policy steps on each seed, every learned policy chooses recompute-both. Its mean loss is 0.077686 versus 0.072686 for the corresponding fixed-both baseline; the extra 0.005 is controller overhead. This result is **not** proof that on-policy policy optimization cannot succeed, only that this tested recipe did not establish it.

## Falsifiable next conditions for a stronger claim

1. Train without privileged all-action task counterfactuals, using active data collection, off-policy correction, or variance-reduced actor-critic methods, and demonstrate a nontrivial policy on independent seeds.
2. Measure real FLOPs, wall latency, and peak memory of **conditionally executed** inference, including controller, probe, repair, telemetry and tool overhead. Confirm efficiency at matched resource budgets.
3. Test longer persistent faults, corrupted checkpoints, coupled branch faults and genuinely new task semantics; avoid passing labels or mechanism identities to any introspection head.
4. Evaluate function-preserving hidden-state reparameterizations with appropriate conjugation of recurrent weights, instead of relying on unpreserved-coordinate perturbations alone.
5. Demonstrate active **probe abstention** under summary telemetry when no repair is needed, not simply learned use of an always-purchased diagnostic replay.
6. Develop a sequential partial-observability regret bound tied to the endogenous structural gap, with finite-sample conditions and drift detection.

## Claim boundary

These are trained neural dynamics, real recurrent internal interventions, and a controller jointly fine-tuned against task-plus-compute loss. They support **endogenous task-relative self-diagnosis under privileged full-information optimization**. They do **not** establish spontaneous introspection under ordinary next-token learning, robust cross-domain metacognition, global structural faithfulness, sapience, consciousness, or net hardware efficiency. The outcome-only negative control is retained, not buried. The Atlas's 80-chapter ledger, release authority, and mathematical certification boundaries are unchanged.
