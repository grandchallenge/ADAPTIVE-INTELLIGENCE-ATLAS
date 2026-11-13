# OWI-EC-002 — Active Epistemic Self-Probing: Theorem, Witness, and Falsification Protocol

**Grand Challenge Labs · 2026-11-12**  
**Claim status:** controlled toy theorem/witness; no claim of neural emergence, general metacognition, sapience, or phenomenology.  
**Parent:** [From Open-World Adequacy to Endogenous Epistemic Control](OWI-ENDOGENOUS-EPISTEMIC-CONTROL-20261112.md).  
**Executable:** [owi_selfprobe.py](../../experiments/owi_selfprobe.py).  
**Relevant Atlas prerequisite:** [MECHDIAG-001 derivation](../derivations/ATLAS-CH-MECHDIAG-001-DERIVATIONS.md): readability is not functional dependence.

## 1. The transition that needs explaining

An ordinary sequence learner has state evolution \(z_{t+1}=F_\theta(z_t,x_t)\). An instrumented, controlled learner also has internal evidence \(S_t\), computational interventions \(a_t\), and an action-conditional self-model \(\widehat Q(S_t,a_t)\). We need **three experimentally separable claims**:

1. **Self-observability:** internal diagnostics distinguish states with different corrective consequences, before the outcome is known;
2. **Causal self-prediction:** the self-model estimates outcomes under randomized alternative interventions, not only the actual selected action;
3. **Active epistemic control:** the learner can choose a self-probing experiment because the information it generates is expected to improve subsequent corrective action enough to justify its cost.

The last property is the transition from passive introspection to **dual control of cognition**. An agent should not always inspect itself: probing is only rational when the decision value of reduced uncertainty exceeds its cost.

## 2. An exact finite model

A hidden fault \(Z\in\{E,C\}\) has equal prior probabilities. The faults mean *evidence absent* and *computation impaired*. There are three cognitive actions \(a\in\{N,R,T\}\): do nothing, retrieve, recompute.

Conditional task-error probabilities are:
| Hidden fault | N | R | T |
|---|---:|---:|---:|
| E | 0.80 | 0.10 | 0.80 |
| C | 0.80 | 0.80 | 0.10 |

Both repair actions cost \(0.03\); N is free. These are *assumed environmental probabilities*, not learned neural dynamics.

Passive telemetry \(S\in\{E,C,?\}\) has distribution \(P(S=Z\mid Z)=0.70\), \(P(S\neq Z,S\neq ?\mid Z)=0.10\), \(P(S=?\mid Z)=0.20\). The stronger optional probe returns \(P\in\{E,C\}\), correct with probability \(r=0.95\), conditionally independent of S given Z, and costs \(c_p=0.09\).

Bayes' rule gives \(P(E\mid S=E)=0.875\) and \(P(E\mid S=? )=0.5\).

A controller with no diagnostics picks a fixed repair, achieving exact expected loss \(R_0=0.48\). The optimal passive controller picks the repair matching a non-ambiguous S, and either repair when S is ?, achieving
\[
R_{\mathrm{passive}}=0.8(0.2175)+0.2(0.48)=0.27.
\]

The optional probe should be invoked only for the ambiguous symptom. For clear S, the reduction in expected task error from replacing accuracy 0.875 with 0.95 is \((0.95-0.875)(0.8-0.1)=0.0525<0.09\). For ambiguous S it is \((0.95-0.5)(0.8-0.1)=0.315>0.09\).

Thus
\[
R_{\mathrm{active}}=0.8(0.2175)+0.2(0.95\cdot0.1+0.05\cdot0.8+0.03+0.09)=\boxed{0.225}.
\]
The exact value of full endogenous information relative to a controller without telemetry is \(V_{\mathrm{int}}=0.48-0.225=\boxed{0.255}\).

A self-model must *learn this policy from interventions* without being given Z at training or decision time; Z is retained only by the evaluator.

## 3. A policy-error bound for active probing

Let \(\mathcal S\) be a finite set of diagnostic states, \(\mathcal P\) a finite set of possible probe results, and \(\mathcal A\) a finite action set. Define true, action-conditional expected terminal losses (including declared action costs)
\[
\mu(s,\varnothing,a),\qquad \mu(s,p,a),\quad p\in\mathcal P,
\]
and the conditional probe distribution \(w(p\mid s)\). Define \(\widehat\mu,\widehat w\) as estimates. Let \(0\leq\mu,\widehat\mu\leq B\) and assume
\[
\sup_{s,p,a}|\widehat\mu-\mu|\leq\epsilon,\qquad
\sup_s\operatorname{TV}(\widehat w(\cdot\mid s),w(\cdot\mid s))\leq\kappa .
\]
Probe cost is known and is applied identically in true and estimated objectives. The policy chooses (i) whether to probe and (ii) an intervention contingent on its result by minimizing its estimated total cost.

**Proposition EC-002.1 (active self-probing regret).** Under these assumptions,
\[
0\leq R(\widehat\pi)-R(\pi^*)\leq\boxed{2(\epsilon+B\kappa)}.
\]

**Proof.** Regard every available decision as a complete *contingent plan*: either act immediately with a fixed \(a\), or probe and apply a map \(p\mapsto a(p)\). For a non-probing plan, estimated and true expected losses differ by at most \(\epsilon\). For a probing plan, conditional outcome-error contributes at most \(\epsilon\); changing its probe-outcome weights changes the expectation of an outcome bounded in \([0,B]\) by at most \(B\kappa\). Thus every contingent plan's estimated value differs from its true value by at most \(d=\epsilon+B\kappa\). The selected plan minimizes estimated loss, and the usual three-term comparison against the truly optimal plan bounds excess true loss by \(2d\). Average the bound over S. \(\square\)

The result specializes the parent OWI programme's conditional-regret argument to **active information acquisition**. It is a standard finite decision-theoretic argument, not a claim of mathematical novelty independent of that literature. It assumes that probe semantics and action-outcome laws remain stable at evaluation.

### Finite-sample certificate

Training randomizes whether to probe and then randomizes the corrective intervention. Consequently, every positive-support diagnostic/probe/action cell estimates its **interventional** response, rather than the response produced by an adaptively selected action.

Suppose the realized training dataset contains at least \(n_{\min}\) independent bounded outcome observations in each of \(K=|\mathcal S|(|\mathcal P|+1)|\mathcal A|\) cells and at least \(m_{\min}\) probe observations per passive symptom. With \(\delta_\mu+\delta_w=\delta\), Hoeffding + union bounds give, with probability at least \(1-\delta\),
\[
\epsilon=\sqrt{\frac{\log(2K/\delta_\mu)}{2n_{\min}}},\quad
\kappa=\sqrt{\frac{\log(2|\mathcal S|/\delta_w)}{2m_{\min}}}
\]
for **binary** probes. The counts are random; the concentration statement holds conditional on cell counts under the stipulated randomized independent sampling.

In the code, \(K=27\), \(B=1.03\), and \(\delta_\mu=\delta_w=0.025\). The guarantee is **per independently trained seed**, not a simultaneous 95% guarantee over all five seeds. If the exact oracle information advantage satisfies \(V_{\mathrm{int}}>2(\epsilon+B\kappa)\), the learned policy is guaranteed, with the specified confidence under the model, to outperform the optimal non-telemetric policy. The code reports both sides.

This is a statistical guarantee in a discrete, stationary, randomized environment; it should not be extrapolated to neural generalization without new assumptions and tests.

## 4. Executed computational witness

Reproduction, with no dependencies beyond Python 3.10+:

~~~bash
python experiments/owi_selfprobe.py --self-test
python experiments/owi_selfprobe.py --seeds 1,2,3,4,5 --train 100000 --eval 70000 --output results.json
~~~

Optional explicitly configured W&B logging: add \`--wandb-project <project-name>\` after installing the W&B client and arranging credentials. The default path uses standard-library Python and modest memory; no GPU or hosted experiment tracking is required. Future neural pilots should prefer a single GPU and multi-seed W&B-logged CLI runs.

**Locally executed on 2026-11-12:** five seeds, 100,000 randomized training and 70,000 evaluation episodes per seed. Risks are *means of realized Bernoulli task loss plus explicit compute/probe costs*, not percentages of deterministic classification accuracy.

| Evaluation policy | Mean realized loss | Exact theoretical loss (where applicable) |
|---|---:|---:|
| No correction | 0.79943 | 0.800 |
| Optimal fixed repair | 0.47968 | 0.480 |
| Same-marginal shuffled diagnostic | 0.48090 | 0.480 |
| Learned passive diagnosis | 0.27023 | 0.270 |
| Learned active self-probing | **0.22546** | **0.225** |
| Passive diagnosis under reversed telemetry semantics | 0.68944 | 0.690 |

The mean maximum action-conditional prediction error across all 27 training cells was \(0.01822\). Every run learned **probe if and only if S=?**. The per-seed 95% regret upper bounds were approximately \(0.15535,0.15424,0.15644,0.15526,0.15824\), each below the oracle information value \(0.255\), making the finite-model improvement certificate positive in each independently analyzed seed.

The reversed-telemetry negative control is deliberately **out of distribution**. It fails because the meaning of the diagnostic channel changes while the learned policy remains frozen. It is evidence of a failure boundary, not evidence of generalizable introspection. Shuffled telemetry was generated independently with the same marginal symptom distribution.

## 5. Why observational training is inadequate

A simple confounding witness: half of tasks are hard. On hard tasks, a repair decreases expected loss from \(0.9\) to \(0.4\); on easy tasks, from \(0.1\) to \(0.05\). Suppose the existing policy repairs hard tasks with probability \(0.9\) and easy tasks with probability \(0.1\).

Then observationally
\[
\mathbb E[L\mid A=\mathrm{repair}]
 =0.9(0.4)+0.1(0.05)=0.365,
\]
\[
\mathbb E[L\mid A=\mathrm{no\ repair}]
 =0.1(0.9)+0.9(0.1)=0.18.
\]
The observational comparison wrongly favors no repair, despite repair being better within both difficulty strata. Randomized action assignment avoids this confounding in the synthetic witness. An observational neural self-critic cannot be assumed causal merely because its predictions are calibrated.

## 6. Next: a genuinely neural, falsifiable experiment

The synthetic result is a **positive control** for the causal-policy mechanism, not a positive result for neural emergence. A neural test must additionally use:

1. A small frozen, actually trained recurrent or Transformer sequence core with a documented task and meaningful latent representations.
2. Physically applied interventions to internal computations: branch ablations, depth truncation, routing changes, benign reparameterizations, and external verification.
3. Low-bandwidth internal telemetry (hidden-state projections, margin/entropy estimates, activation changes) that does **not** reveal the intervention label or outcome.
4. Randomized action assignments and a learned action-conditional self-model trained without ground-truth fault IDs.
5. A learned choice whether to run extra diagnostic computations; costs in actual FLOPs/latency.
6. Separate held-out *intervention mechanisms*, not merely held-out random seeds or inputs.
7. Matched-compute, passive-probe, oracle-feature, shuffled-feature, noncausal-proxy, and always/never-probe controls.

**Primary endpoint:** out-of-distribution reduction in task loss after total compute cost, versus matched-compute baselines, with calibrated predicted intervention effects. **Failure criteria:** gain disappears under held-out perturbations, diagnostic identity is leaked, shuffled signals give equivalent improvements, or intervention predictions are only associative.

## 7. What this licenses

The witness establishes a small but exact fact: under randomized causal identification, a system can learn a policy that selectively acquires information about its own hidden failure regime, chooses a corrective action using that information, and realizes the predicted benefit, subject to a finite-sample regret certificate.

It does **not** show that task-trained representations spontaneously encode such causal self-knowledge, or that a genuine neural sequence learner will discover the quotient. Those remain the substantive research hypotheses.

**Editorial disposition:** standalone bounded mathematical experiment companion. No promotion of Atlas canonical chapters, proof certification, or broad sapience claims.