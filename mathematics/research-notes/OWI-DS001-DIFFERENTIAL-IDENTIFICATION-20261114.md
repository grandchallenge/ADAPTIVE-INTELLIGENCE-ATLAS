# OWI-DS-001 — Differential information versus causal identification in runtime program synthesis

**Grand Challenge Labs · 14 November 2026.** Research candidate; no mathematical certification, empirical win or chapter promotion asserted. Scientific parent: [OWI-EC-005 #466](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/466). This is *not* an alternative OWI-EC-005 reward, controller, or source-native checker.

## 1. Decision

The question is **whether compositional derivative information increases verified, intervention-generalizing synthesis efficiency beyond an equally resourced symbolic/neural-guided search**, not whether a tiny algebraic grammar can recover a known expression. An exhaustive search over `x*x+y` is not evidence for this research claim.

Cartesian differential categories supply a coherent derivative of a differentiable program's *denotation*. They do not supply a canonical derivative on discrete syntax, and they do not imply that finite-task behavior identifies a causal program. These three objects must remain separate:

- typed syntax `p : A -> B`, with operational semantics `[[p]]`;
- a categorical directional derivative `D[[p]](x,v)`, if the chosen semantic category supports it;
- a search distribution `q_alpha(p)` or a continuous relaxation of syntax, which is a separate statistical optimization construction.

## 2. Exact finite-search identity (proposition)

For finitely many fixed programs `p_i`, a temperature `tau>0`, costs `R_i` **independent of alpha**, and `q_i=softmax(alpha_i/tau)`, let `J(alpha)=sum_i q_i R_i`. Then

`dJ/dalpha_i = q_i (R_i - J)/tau`.

**Proof.** `dq_j/dalpha_i = q_j (1[j=i]-q_i)/tau`. Multiply by `R_j` and sum. QED.

This gradient is only a reweighting of *already evaluated* candidate costs. It contains no additional behavioral information and is not evidence that program structure itself is differentiable. For large grammar spaces, computing all `R_i` is intractable; sampling introduces variance/credit-assignment obligations. Temperature annealing does not remove this limitation.

## 3. Observational-identification obstruction (proposition)

Let `H_0,H_1` be two candidate executable causal mechanisms with identical distributions of **all observations and chosen-action rewards available under a training policy** `pi`, but different outcomes under some supported test intervention `do(a*)`. Then no estimator measurable with respect to the training history under `pi` can distinguish the two mechanisms with better-than-prior performance for equiprobable `H_0,H_1` (Bayes error 1/2). Adding a deterministic function of that history, including an autodifferentiated loss or a synthesized derivative surrogate, cannot restore identification.

**Proof.** The two hypotheses induce the same law on the training-history sigma-algebra; every history-measurable estimator therefore has the same output distribution under both. Under equal priors, the joint success probability of any binary classification is 1/2. Any derived gradient is a measurable transformation and cannot distinguish equal input laws. QED.

**Qualification.** If genuine measured derivative or intervention observations are *additional observable data*, they may distinguish the mechanisms. This is precisely the hypothesis to test. The proposition does not prohibit learning from such extra measurements, nor from identifiable parametric assumptions.

## 4. Admissible differential signal

Use only tangent observations actually accessible to the agent from a **chosen, executed operation**, and bill their computation. Define a differential oracle as an operational query `(s,a,v) -> J_v F(s,a)` only when: (i) the operation is differentiable in the specified state coordinates; (ii) its derivative is computed from the chosen run or a separately charged permitted experiment; (iii) no fault ID, clean trajectory, privileged action outcome, or sealed checker is used.

A derivative of the learner's own surrogate `m_phi` is *not* evidence of the true environment derivative. Evaluate alignment separately on withheld interventions, without training leakage. For discrete tool/state mutations, use intervention differences, typed finite-difference queries where valid, or a tangent model of a differentiable subcomponent; do not silently extend a CDC to arbitrary branch changes.

## 5. Pre-registered experimental comparison

Build on the existing conditional environment in `experiments/owi_ec005_conditional.py` and randomized on-policy identification in `experiments/owi_ec005_identify.py`; do not replace the native-source fidelity gate in `OWI-EC005J`.

**Unit of synthesis:** a typed probe/repair *policy program* with bounded conditional branches and reusable subroutines, not a regression polynomial. Program execution must be operationally conditional. Extract a discrete, replayable policy; score its actually invoked tools, memory and latency.

Compare four matched systems:

A. typed enumerative/e-graph or stochastic symbolic search without derivative measurements;
B. neural-guided typed program search, same model/compute budget, without derivative measurements;
C. same as B plus **charged chosen-run tangent or local sensitivity observations**;
D. same as C plus an explicit learned causal self-model predicting unseen intervention outcomes.

Use two differential controls: C-shuffled (permute measured tangent features across examples within source family) and C-surrogate-only (differentiate a learned model without additional observations). Add no-probe, passive-telemetry, fixed-repair, privileged oracle (evaluation-only) and OWI-EC-004 upper benchmark where compatible.

**Tasks:** (1) held-out perturbation mechanisms and sequence lengths from OWI-EC-005; (2) source-disjoint native tool tasks *only after* their unchanged source checker demonstrates correct-versus-harmful and correct-versus-abstain reward margins; (3) independent differentiable algorithmic submodules with source-locked reference derivatives and hidden compositional task splits. Never claim that one task family establishes transfer to another.

**Primary endpoint:** paired, five-or-more-seed difference in *verified out-of-distribution solve rate at equal measured computation budget*, with confidence intervals. Secondary: median physical runtime per verified solution, actual activated operations/MACs where measurable, program length, valid proof/refinement admission rate, and unseen intervention prediction calibration. Count synthesis search and tangent queries, not only deployed inference.

**Causal endpoint:** on test mechanisms unseen in training, D must predict chosen intervention outcomes better than C, with outcome-only learning and randomized logged propensities; reject gains that vanish on shuffled/surrogate controls. Require positivity/support and separate training/test families. If natural reward signals remain non-identifying, report a negative result rather than fabricate shaped rewards.

## 6. Implementation and validation obligations

1. Establish a source-locked benchmark manifest and exact commit of OWI-EC-005 environment, original native verifier, and training/test splits. Reject any checksum mismatch.
2. Type the program grammar, semantics, tangent primitives, branching cost, and allowed probes. Test CDC chain/product/linearity laws on eligible smooth primitives; document non-smooth exclusions.
3. Implement paired A/B/C/D runners using **identical** task exposures, parameter and search budgets, repeated seeds, and a single-GPU-first implementation. Log W&B metrics and deterministic JSONL receipts.
4. Implement a runtime leakage test proving policy/trainer cannot access fault IDs, clean references, unchosen counterfactuals, sealed rewards, or evaluation-only oracle functions.
5. Record actual conditional execution traces; do not claim hardware speedups from proxy cost. Benchmark measured runtime/memory and distinguish host evaluator work from learner work.
6. Preserve separate training, proof checking, adversarial review, and protected merge stages. A green test suite is not mathematical certification.
7. Run the **C-shuffled and C-surrogate-only** controls before interpreting any gain. Gate source-native work on the OWI-EC005J reward-fidelity obstruction.
8. Publish full negative results and confidence intervals, even when C/D fail.

## 7. Decision gates

- **Go / differentiation adds value:** C beats B on verified OOD solve rate under equal total compute and survives C-shuffled, C-surrogate-only, and mechanism holdout.
- **Go / reflective causal modeling adds value:** D beats C on held-out intervention prediction and verified repair utility, with leakage/propensity controls.
- **No-go:** gain appears only in smooth interpolations, only in training-family tasks, or only when uncharged tangent/counterfactual oracles are provided.
- **Unresolved:** source-native reward does not distinguish harmful mutations; repair identification first, or restrict claims to the synthetic conditional environment.

## 8. Current status

**SPECIFIED; NOT IMPLEMENTED OR VALIDATED.** This document supplies a falsifiable research boundary and two elementary proved limitations, not experimental evidence for differential synthesis, a claim of agent introspection, or an authorized Atlas release. Exact runner, baseline, cost, and adjudication evidence remain outstanding.
