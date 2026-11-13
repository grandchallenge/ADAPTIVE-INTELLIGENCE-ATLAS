# OWI-EC-005 — Outcome-only Reflective Control: Conditional Execution and Identifiable Probe Interventions

**Grand Challenge Labs · 2026-11-13 UTC**  
**Issue:** [#466](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/466)  
**Parent:** [OWI-EC-004](OWI-EC004-ENDOGENOUS-LEARNED-CONTROL-20261112.md), merged by [PR #465](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/pull/465).  
**Status:** reproducible *candidate experiment*, not a positive scientific result, a theorem, a certified introspection claim, or a revised Atlas release.

## The scientific question

EC-004 showed a bounded improvement when a controller could learn from **all unchosen counterfactual task outcomes**. Its simple chosen-outcome REINFORCE control collapsed to always recomputing both branches. This successor asks whether a controller can infer the value of its own observations and corrections from **only the sequence of decisions it made and the outcomes that actually occurred**.

A successful controller must identify *when not to inspect or repair*, not merely learn to purchase an always-on probe. A useful result must persist under a held-out perturbation mechanism, repeated independent seeds, and a measured conditional-compute comparison. This tranche implements the physically conditional replay and outcome-only identification machinery; no positive result is asserted before replay.

## Conditional, non-oracular execution

The base task remains two independent 9-symbol majority checks performed by width-12 GRUs, pretrained on clean labels. The 3-step final recurrent suffix may suffer an injected disturbance after its first step. The environment computes **only the corrupted forward trajectory**. Each batch member's actor sees:

1. its two corrupted task logits (rescaled);
2. the norms of the two corrupted hidden states;
3. after choosing one of `none/A/B`, only the RMS difference from the **selected** three-step trusted suffix replay;
4. after choosing one of `none/A/B/both` repairs, a single terminal scalar task cross-entropy plus an explicit computation charge.

The live rerun implementation indexes only selected examples and branches. A trusted suffix is cached if probed and reused for subsequent repair. An unprobed/unrepaired suffix is **not executed**. There is no precomputation of the unchosen probe, clean state, oracle, or other repairs in the live path. `fault_audit` is isolated to an evaluator-only structure and is never read by the controller's features or loss construction. Labels are consumed only for the *terminal task outcome*, not as online diagnostic-state supervision.

Tests attach forward hooks to the GRUs **after** the corrupted trajectory is built: no-probe/no-repair makes zero additional GRU calls; probe A plus repair A makes exactly one replay call; repair-both makes two; probe A plus repair-both still makes only two. A sentinel overwrite of the fault-audit field must not change behavior or chosen outcomes. This tests the critical distinction between actual conditional compute and EC-004's virtual prices over vectorized counterfactuals.

## Outcome-only sequential actor-critic

For a two-decision trajectory, with \(S\) the four public telemetry features, \(P\in\{0,A,B\}\) the selected probe, \(Q_P\) the observed probe signal, and \(R\in\{0,A,B,AB\}\) the repair, the scalar terminal outcome is

\[
L=\frac12\sum_{c\in\{A,B\}}\operatorname{BCE}(\widehat y_c,y_c)
+0.035 N_{\mathrm{replay}}+0.005\mathbf1_{\mathrm{controller}}.
\]

The training update uses only the realized \(L\), chosen \(P,R\), and their recorded current-policy log-propensities:

\[
\widehat\nabla J =
(L-V_0(S))\nabla\log\mu_\phi(P\mid S)
+(L-V_1(S,P,Q_P))\nabla\log\mu_\phi(R\mid S,P,Q_P).
\]

The two fitted value baselines reduce variance; they are **not** trained to predict missing counterfactuals or fault labels. Both actors optimize the likelihood of their *actual randomized mixture behavior policy*, rather than substituting the unperturbed softmax probabilities. Training uses an explicit epsilon schedule 0.35 → 0.15 → 0.05, so all three probe and all four repair interventions have nonzero support at every update. Training and action-sampling RNG streams are independent, preventing the current action from changing the next environment draw. No replay-buffer or off-policy correction is claimed: the gradient is on-policy for the chosen mixture, with the ordinary finite-batch, evolving-policy assumptions.

A frozen task core is deliberately retained in the first tranche to isolate online credit assignment. This is **not** EC-004's 100-step joint core/controller fine-tuning and must not be described as end-to-end task-system co-learning. A later tranche can test joint changes after the basic identification experiment passes.

## Actual action identification, not mere correlation

The separate `owi_ec005_identify.py` evaluates one **frozen** controller under a known, randomized probe-selection mixture. The repair policy is allowed to react to the realized selected probe; it does not receive alternatives. For probe arm \(a\), the inverse-propensity estimate is

\[
\widehat\mu_a = \frac1N\sum_{i=1}^N
\frac{\mathbf1\{P_i=a\}L_i}{\Pr(P_i=a\mid S_i)}.
\]

The causal contrast \(\widehat\mu_0-\widehat\mu_a\) estimates the population value of **forcing the first probe decision** while preserving that controller's downstream response. It is not the value of the globally optimal dynamic policy, nor an individual-level unobserved counterfactual. The audit retains arm counts, effective sample sizes, and paired influence-score standard errors. Identification requires logged positive support, consistency, no interference, a frozen evaluation policy and complete observed terminal outcomes. High-variance weights or insufficient arm support must be reported, not silently called causal learning.

## Tests and ablations

The five-seed CLI evaluates the on-policy active controller, matched-compute passive telemetry controller (both actor networks executed but probes disabled), and fixed repair-both. For the active controller, it additionally zeroes only the actually selected probe's information or shuffles its observed residual across examples while still charging for performed probes. It measures no-probe/no-repair decisions on all examples and diagnostic abstention on evaluator-known clean examples.

The Gaussian intervention is the training distribution. Held-out mechanisms are masking, sign reversal, coordinate roll, small noise, persistent disturbance, simultaneous coupled branch faults, and corrupted recovery checkpoints. Length 13 (new length, old majority task) and parity (new task **without** task-core retraining) are transfer stress tests; poor parity performance cannot by itself diagnose introspection. All evaluator labels are excluded from the controller's trainable path.

The previously reported EC-004 full-information active-summary result (0.053109), passive summary (0.064680), fixed-both (~0.0717), and failed on-policy run (0.077686) are retained as **archival reference results only**. The new conditional execution, probe encoding, and input sampling make raw numeric comparisons across experiments *not strictly matched*.

## Compute accounting and measurement boundaries

Every actually executed GRU suffix is counted per example and branch, including cached probe-repairs only once. With hidden size \(h\), input width 1, and suffix length \(s\), the estimated dense multiply-accumulates (MACs) per replay are \(3sh(h+1)+h\), equal to 1,416 for \(h=12,s=3\). Forward-hook tests verify the calls, not just the virtual charge. The telemetry controller's two small actor MLPs add 380 dense MACs per example, while fixed-both has no controller charge.

The evaluator also records wall-clock elapsed time around actual selected actions and process peak resident memory. These are **real CPU execution observations**, but the printed MAC count is an architecture-derived estimate for *executed* operations, not a hardware FLOP/energy counter. Reported process RSS is a high-water mark, not isolated incremental replay memory. The current CPU implementation includes Python branch selection, index dispatch and synchronization; do **not** infer accelerator gains, energy improvements, or large-model speedups from it. The fixed 0.035/0.005 loss charges remain policy-training prices rather than measured joules or converted seconds.

## Reproduction

Requires Python 3.12 and PyTorch 2.10.0 (the GitHub Actions workflow pins the CPU wheel). No nondeterministic remote data is used.

```bash
python -m unittest discover -s tests -p 'test_owi_ec005.py' -v
for seed in 1 2 3 4 5; do
  python experiments/owi_ec005_actor_critic.py --seed "$seed" \
    --mode both --stage all --pretrain 250 --steps 600 \
    --batch 192 --eval 512
done
python experiments/owi_ec005_summarize.py --seeds 1,2,3,4,5
```

The CLI defaults to 1,200 on-policy controller steps and 2,048 evaluation examples; the declared CI uses a shorter 600-step exploratory curriculum and 512 test examples. Each saved record carries its seed, chosen outcomes and propensities, charge, actual replay count, estimated executed MACs, measured batch latency, high-water process RSS, held-out condition metrics and randomized probe-identification diagnostics. Pass `--wandb-project PROJECT` only when W&B is installed/authenticated; it is optional so the pinned CI reproducer runs without credentials.

## Scientific decision rule and remaining obligations

The summary emits `BOUNDED_POSITIVE_CANDIDATE_REQUIRES_REVIEW` only when **all five seeds** beat matched passive and fixed-both on Gaussian, at least one held-out mechanism beats both for all seeds, and both probe-information ablations consistently degrade the active model. Otherwise it emits `NEGATIVE_OR_INSUFFICIENT_EVIDENCE`. The randomized probe estimates are *diagnostics* and cannot override a negative task-plus-cost result. A green CI run proves code execution/invariants; it does not satisfy the scientific acceptance rule.

Not yet established: a robust positive outcome-only advantage, hardware-FLOP/energy profiling, true new-task competence, joint on-policy task/controller adaptation, and a privileged oracle reimplemented against the **same** new conditional cost model. These remain explicit obligations under #466. Neither the 80-chapter Atlas acceptance ledger nor the v0.1.0 release/certification state is modified. No sapience, consciousness, or general introspection claim is licensed.
