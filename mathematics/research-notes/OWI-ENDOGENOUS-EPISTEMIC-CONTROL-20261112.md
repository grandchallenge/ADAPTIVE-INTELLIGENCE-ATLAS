# From Open-World Adequacy to Endogenous Epistemic Control

**GCL research companion, 2026-11-12.**  
**Status:** bounded mathematical derivation and research proposal; **not** certified, accepted as an Atlas chapter, or included in the released Atlas manuscript.  
**Scope:** connect the March 2026 *Toward Open-World Intelligence: Observable Adequacy, Structural Faithfulness, and Self-Diagnosing Learning Systems* (OWI) to operational neural self-observation, causal self-prediction, and epistemic self-correction.

## 0. Source reconciliation and claim boundary

The OWI manuscript models a target world as \((\mathcal X,\mathcal H,\mathcal I,\mathcal A,\omega,\mathcal U)\) and a learner as \((\mathcal Z,\Theta,\Pi,\mathcal A_M,\omega_M,\mathcal U_M,\mathcal T,\Gamma)\). It defines observable, counterfactual, and structural gaps; Proposition 5.5 states a binary self-diagnosed-escalation value bound; Section 8 defines structural critics, gating, chart switching, and the insufficiency-detection training objective; Section 10 specifies intervention-centred evaluations.

This companion **reuses** those objects. The addition is to make the learner's *own computational process* the target of a second, endogenous adequacy problem. It does not rename or supersede the OWI theory.

Related Atlas boundary: [MECHDIAG derivation packet](../derivations/ATLAS-CH-MECHDIAG-001-DERIVATIONS.md) distinguishes a readable signal from a causally used feature. Self-diagnostic probe accuracy alone must not be promoted to a mechanistic claim. The March manuscript is retained in the GCL document Library as \`open_world_intelligence_main.tex\` / \`open_world_intelligence_main.pdf\` (2026-03-27); no GitHub source path is asserted for it.

**Status of claims here:** Results A, B, C below are exact conditional statements with proofs; the interpretation as learned introspection and training-emergence hypothesis is conjectural.

## 1. Endogenizing the target

Let \(C\) be the *actual* stochastic computational process of an agent in its environment, including relevant internal representations, mutable compute resources, external observations and eventual outcomes. Let \(Z_t\) denote its hidden state; \(H_t\) the history available to its controller; \(S_t\) an internal measurement available before the correction decision; \(a_t\in\mathcal U_t\) a permitted cognitive intervention. Examples of interventions are extra compute, routing changes, a verification call, retrieval, or abstention.

At the level of the original OWI formalism, define an *endogenous target*
\[
 W_{\mathrm{endo}}=(\mathcal X_{\mathrm{int}},\mathcal H_{\mathrm{int}},
 \mathcal I_{\mathrm{int}},\mathcal A_{\mathrm{int}},
 \omega_{\mathrm{int}},\mathcal U_{\mathrm{int}}),
\]
whose observables concern actual computation and task outcomes, and a *self-model* \(\widehat W_{\mathrm{endo}}\) that predicts those observables under specified interventions.

This is not a claim that an agent must perfectly reconstruct its weights or activations. The target family should include decision-relevant quantities such as expected task loss **under alternative corrective interventions**. In particular, the endogenous counterfactual gap should be conditioned on the information used at decision time. A small **unconditional** OWI counterfactual gap does not, by itself, bound this conditional gap on rare histories.

There are therefore two distinct requirements:

* **Internal accessibility:** the measurement \(S_t\) distinguishes internal conditions when that distinction can change the optimal corrective choice;
* **Model adequacy:** predictions made using \(H_t,S_t\) approximate the real outcomes of admissible interventions.

These requirements are not identical: a feature may be easy to read yet irrelevant to the actual network's decisions, as MECHDIAG demonstrates.

## 2. Decision-relative epistemic quotients

For a single correction decision in hidden state \(z\), let \(Q(z,a)\) denote the expected loss after taking cognitive action \(a\), including a declared continuation rule and any computational cost. Define
\[
 z\sim_Q z'\iff Q(z,a)=Q(z',a)\quad\text{for every }a\in\mathcal U.
\]
The quotient \(\mathcal Z/{\sim_Q}\) retains all action-value information for that decision. Reconstructing the entire \(z\) is unnecessary for choosing an action. **Caveat:** equality of action values does not by itself produce a Markovian quotient for subsequent decision steps.

For a finite controlled Markov system \((Z,\mathcal U,P,\ell)\), a stronger equivalence relation \(\sim\) is *controlled lumpable* when for every \(z\sim z'\), every \(a\), and each equivalence class \(B\),
\[
 \ell(z,a)=\ell(z',a),\qquad
 P(B\mid z,a)=P(B\mid z',a).
\]

**Result A (exact controlled quotient).** For any finite horizon, if the action sets agree on classes and \(\sim\) is controlled lumpable, the optimal expected remaining loss is constant on equivalence classes. A Markov controller observing the class suffers no loss from quotienting.  

*Proof.* At terminal time the value is constant (zero). Assume \(V_{t+1}\) is constant on classes. For each \(a\), \(\ell(z,a)+\sum_B P(B\mid z,a)V_{t+1}(B)\) depends only on \([z]\). Minimizing over the common action set gives the same statement for \(V_t\). Backward induction completes the proof. This is the standard controlled-bisimulation/lumpability argument, restated in OWI's endogenous setting.

**Observability obstruction.** If two states belong to different decision-relevant classes, demand different optimal actions, and induce identical accessible observation-history distributions under the permitted probing protocol, no self-estimator based on those histories can reliably distinguish them. For equally likely binary states with observation laws \(P_0,P_1\), the minimum classification error is \((1-\mathrm{TV}(P_0,P_1))/2\). This is a diagnostic impossibility, not a claim of universal impossibility under additional probes.

## 3. From conditional counterfactual fidelity to a corrective policy

Consider an episode of horizon \(T\) with bounded losses and finite admissible actions at each stage. Write \(h_t\) for the *entire observed history* at the stage, including available internal telemetry. Let
\[
 Q_t^*(h_t,a)
 =\mathbb E[\text{remaining total loss}\mid h_t,\operatorname{do}(a_t=a),
 \text{ optimal continuation}],
\]
and let \(\widehat Q_t(h_t,a)\) be the self-model's estimate. Assume uniform conditional counterfactual fidelity:
\[
 \sup_{t,h_t,a}|\widehat Q_t(h_t,a)-Q_t^*(h_t,a)|\le\varepsilon
\]
on every history reachable by the evaluated policy. The policy chooses an \(\arg\min_a\widehat Q_t(h_t,a)\), with the same information and available actions as the oracle.

**Result B (finite-horizon self-correction bound).**
\[
 J(\pi_{\widehat Q})-J(\pi^*_{\mathrm{observed}})\le 2T\varepsilon.
\]

*Proof.* At any \(h_t\), denote the chosen action by \(\widehat a\) and the oracle action by \(a^*\). Uniform approximation gives
\[
 Q_t^*(h_t,\widehat a)
 \le\widehat Q_t(h_t,\widehat a)+\varepsilon
 \le\widehat Q_t(h_t,a^*)+\varepsilon
 \le Q_t^*(h_t,a^*)+2\varepsilon.
\]
The difference between actual continuation of \(\pi_{\widehat Q}\) and optimal continuation after its first action is the expected regret from the next history. Recursive substitution yields at most \(2\varepsilon\) per stage; summing over \(T\) stages proves the claim.

Let \(R_0^*\) be the optimal risk without an internal telemetry channel and \(R_1^*\) the optimal risk with it, under otherwise matched resources; let \(V_{\mathrm{int}}=R_0^*-R_1^*\ge0\). Suppose acquiring and using telemetry incurs additional expected cost at most \(c_{\mathrm{tel}}\) not already included in the Q-values. Then
\[
 J(\pi_{\widehat Q})+c_{\mathrm{tel}}
 \le R_0^*-V_{\mathrm{int}}+2T\varepsilon+c_{\mathrm{tel}}.
\]
Therefore **\(V_{\mathrm{int}}>2T\varepsilon+c_{\mathrm{tel}}\)** is sufficient for strict improvement over the best non-telemetric policy. Neither a positive mutual information score nor diagnostic accuracy alone is sufficient to guarantee this improvement.

The bound is a consequence of approximate optimal action-value control. It does **not** prove that the neural self-model can learn such a uniform bound, identify causal effects without suitable interventions, or remain accurate under arbitrary distribution shift.

## 4. A structural-fidelity route to a numerical regret bound

Result B starts from an action-value error bound. To connect it more directly to OWI structural faithfulness, take an *observable* finite Markov quotient (Result A) with true stage losses \(\ell_t\in[0,1]\) and true class-transition kernels \(P_t\), together with a self-model \((\widehat\ell_t,\widehat P_t)\) on the same quotient with \(\widehat\ell_t\in[0,1]\). Assume
\[
 \sup_{t,q,a}|\ell_t(q,a)-\widehat\ell_t(q,a)|\le e,\quad
 \sup_{t,q,a}\mathrm{TV}(P_t(\cdot\mid q,a),\widehat P_t(\cdot\mid q,a))\le d.
\]

**Result C (finite-horizon structural simulation bound).** For every Markov policy \(\pi\), its true and modeled total expected losses differ by at most
\[
 B_T=Te+\frac{T(T-1)}2\,d.
\]
Consequently the policy \(\widehat\pi^*\) optimized in the self-model has true regret at most
\[
 J_P(\widehat\pi^*)-J_P(\pi^*)\le
 2Te+T(T-1)d.
\]

*Proof.* Fix \(\pi\) and use backward induction on stage \(t\). The immediate loss mismatch contributes at most \(e\). The continuation value has range at most \(T-t-1\) since every stage loss belongs to \([0,1]\). Total-variation error changes its expectation by at most \((T-t-1)d\). The mismatch in continuation value contributes the previous inductive bound. Summing from \(t=0\) to \(T-1\) yields \(B_T\). Insert and subtract the modeled performance of the modeled-optimal policy and the true-optimal policy, and use modeled optimality; the resulting regret is at most \(2B_T\).

This supplies one **explicit** bridge from local operator fidelity (loss observables and controlled transitions) to global corrective-policy fidelity. It is not a universal bound from OWI's abstract \(\Delta_{\mathrm{str}}\): applying it requires a common observable quotient, bounded costs, well-defined kernels, and a proof that the structural surrogate controls \(e\) and \(d\). In a POMDP one must instead work with belief states or suitably controlled history representations.

## 5. Precise relation to OWI Proposition 5.5

Take two available actions, **escalate** and **do not escalate**, and two regions, hard/easy. Suppose the no-escalation action is the baseline, escalation yields gain at least \(\rho\) on the hard region, and false escalation incurs cost at most \(c\) on the easy region. If the gate escalates with conditional probabilities \(\alpha\) (hard) and \(\beta\) (easy), while other effects are absent, then
\[
 \Delta V\ge \alpha\rho\,P(\Omega_{\rm hard})
              -\beta c\,P(\Omega_{\rm easy}).
\]
This is exactly the OWI Proposition 5.5 form. If hard-region gains and easy-region costs equal their constants, the expression is an equality. If intervention costs can also occur in the hard region or are not already included in the claimed gain, they must be subtracted explicitly. The proposition is thus a binary *gating economics* instance, whereas Results B–C address multiaction, sequential corrective control.

The OWI Section 8 structural critic \(C_{\rm str}\) is a candidate self-observer; \(\Gamma\) is the corrective controller; the insufficiency label \(\mathbf 1\{\text{tool improves outcome}\}\) is a binary training signal for intervention value. Our extension requires **action-conditional** outcome labels (which repair helps, by how much, under which internal conditions) and explicit causal intervention coverage.

## 6. Non-equivalences and failure modes

1. **Readable is not used:** a probe can decode failure type without any downstream decision depending on that representation (Atlas MECHDIAG).
2. **Passive is not causal:** allocation of more compute to hard problems can correlate with lower accuracy even if extra compute helps; randomized or otherwise identifiable interventions are required for causal response estimates.
3. **Global gaps are not conditional gaps:** accurate unconditional predictions may conceal catastrophic miscalibration on rare, consequential histories.
4. **One-step quotient is not a dynamical quotient:** equality of \(Q(z,a)\) at a fixed stage does not imply controlled lumpability of transitions.
5. **Coordinates are not mechanisms:** function-preserving changes of basis can destroy neuron-level interpretations without changing computation; test action values and intervention effects.
6. **Self-knowledge is not truth:** an agent may accurately predict its own answer-generation mechanism while lacking sufficient external evidence to determine whether the answer is correct.
7. **Better diagnosis need not improve decisions:** if the same action is optimal in every diagnosable state, decision value is zero.
8. **Closed loop may be unstable:** state-dependent correction changes the distribution used for diagnosis; off-policy identification and new-outcome auditing remain necessary.

## 7. Minimum falsifiable experiment

Freeze a modest base neural model; instrument a compact internal telemetry channel; train an action-conditional self-estimator on randomized intervention assignments. Compare: (A) matched-compute task-only, (B) telemetry without control, (C) telemetry and counterfactual prediction without control, (D) telemetry plus policy, and (E) policy with shuffled telemetry. Include routing edits, activation subspace interventions, compute truncations, harmless perturbations, and available external verification. Keep an entire perturbation *mechanism* family out of training.

Report: state-distinction error before outcomes; intervention effect prediction calibration; value of information after costs; closed-loop error/regret relative to matched resource baselines; generalization to held-out perturbation mechanisms; sensitivity to function-preserving reparameterizations; and source-locked intervention provenance. No trained benchmark result is claimed in this note.

**Decision rule for the research claim:** only a causal improvement relative to matched-compute, shuffled-telemetry, and noncausal-proxy controls supports *operational introspection*. It does not establish phenomenal awareness or sapience.

## 8. Unresolved obligations

- Derive an endogenous structural gap with a nonvacuous, measurable modulus controlling the conditional value gap, not only an informal diagrammatic analogy.
- Replace exact observability/lumpability by approximate belief-state observability and prove resource-aware regret bounds under partial observability.
- Quantify active self-probing: when is it worth paying to learn which cognitive regime the agent occupies?
- Establish finite-sample statistical guarantees for action-conditional prediction under nonstationary, adaptively selected internal interventions.
- Verify experimentally that training produces stable, transferable causal self-models rather than intervention-signature memorization.

**Disposition:** a conservative bridge theorem packet, not a new Atlas chapter, not a certified intelligence criterion, and not a claim of consciousness.