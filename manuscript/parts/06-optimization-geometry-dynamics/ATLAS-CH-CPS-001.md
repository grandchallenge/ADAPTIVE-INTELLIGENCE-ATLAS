# Coupling-Phase Spectroscopy
<!-- ATLAS-CH-CPS-001 -->

**Epistemic status:** audited Optimizer-State Dynamics + current public GSD-001 transition/artifact evidence + Atlas-owned exact spectroscopy and prediction protocol.  
**Specification:** manuscript/specifications/ATLAS-CH-CPS-001.md  
**Derivation packet:** mathematics/derivations/ATLAS-CH-CPS-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-CPS-001.md  
**Source lock:** sources/source-locks/ATLAS-CH-CPS-001.yaml

A training run can change behavior before we know what changed inside the optimization dynamics.

A benchmark state can flip.

A representation can drift.

An optimizer can carry momentum, moments, scheduler state, or update geometry that is invisible in a parameter-only snapshot.

Coupling-Phase Spectroscopy asks a narrow question:

> can local structure in the augmented model-optimizer state diagnose or predict a behavioral transition before the transition is observed?

The chapter begins with a strict warning.

\[
\boxed{
\text{diagnosis}
\neq
\text{prediction}
\neq
\text{causal mechanism}.
}
\]

All three can be scientifically useful.

They require different evidence.

## 1. The object is the augmented training state

Optimizer-State Dynamics established that optimizer memory belongs in the dynamical state whenever the next update depends on it.

Write:

\[
z_{t+1}=F_t(z_t,\xi_t).
\]

The local Jacobian is:

\[
J_t
=
\frac{\partial F_t}{\partial z}(z_t,\xi_t).
\]

A short-horizon perturbation is governed locally by:

\[
J_{t+k-1}\cdots J_t.
\]

CPS treats these local maps and products as instrumentation surfaces.

It does not claim that one frozen Jacobian globally describes training.

## 2. What is spectroscopy here?

The word spectroscopy is used by analogy with measuring several signatures of a state rather than collapsing everything into one scalar.

A CPS diagnostic vector can contain:

\[
\mathcal S_t
=
\Bigl(
\operatorname{tr}J_t,
\det J_t,
\rho(J_t),
\widehat\sigma_{\max}(J_t),
\mathcal N(J_t),
\widehat G_{t,k},
\mathcal A_t
\Bigr).
\]

Possible coordinates include:

- trace;
- determinant;
- spectral radius;
- dominant singular gain;
- non-normality proxy;
- finite-horizon gain;
- directional alignment.

No coordinate is promoted to a universal health score.

## 3. The behavioral transition is defined elsewhere

CPS does not get to create its own target after looking at optimizer diagnostics.

The behavioral transition must be frozen independently.

For a checkpoint \(t\), define:

\[
Y_t
=
\mathbf 1
\{
\text{declared behavioral transition occurs in }(t,t+\Delta]
\}.
\]

CPS receives \(Y_t\) as a target variable.

It does not redefine \(Y_t\).

## 4. Current GCL state changed since the first Atlas source lock

The original Optimizer-State Dynamics source lock was written on October 2, 2026.

At that time it recorded no separate public GCL source for a CPS result.

That statement is no longer a complete description of current public project state.

A fresh organization search on October 6 finds a public GSD programme with:

- GSD-WP04 — CPS transition-local dynamics;
- one confirmed behavioral transition;
- an explicit optimizer-artifact availability receipt.

The Atlas therefore replaces the old current-state gap with exact newer project evidence.

## 5. What GSD has actually established

The bound GSD-WP03R receipt establishes one robust OLMo2-1B transition for:

truthy_answer/surprising_truth.

The frozen GSD protocol reports:

- step 2000: GENERALIZING;
- step 3000: PATTERN_MATCHING;
- step 4000: PATTERN_MATCHING;
- transition localized between steps 2000 and 3000;
- stable controls passed;
- independent replay preserved the transition;
- prompt variants preserved the confirmed direction.

This is a behavioral result.

The receipt explicitly does not establish:

- mechanism;
- optimizer cause;
- persistence state;
- capacity-allocation explanation;
- architecture-level conclusion.

## 6. What GSD-WP04 asks

The public GSD research programme defines GSD-WP04 as:

CPS transition-local dynamics.

Its question is:

> does optimizer-state structure predict or explain confirmed transitions?

Its declared outputs include:

- optimizer-state extraction;
- augmented-state probes;
- transition-local traces;
- heldout predictive testing.

Its scientific exit grammar is:

- PREDICTIVE_SIGNAL;
- DESCRIPTIVE_ONLY;
- NO_SIGNAL.

That is a useful experimental contract.

## 7. Why there is no WP04 signal result yet

The exact public transition-local revisions inspected are:

- stage1-step2000-tokens5B;
- stage1-step3000-tokens7B;
- stage1-step4000-tokens9B.

The public revisions expose:

- configuration;
- tokenizer;
- model weight shards;
- weight index.

They do not expose:

- optimizer state;
- trainer state;
- scheduler state;
- gradient artifacts;
- update-direction artifacts.

Therefore the exact GSD-WP04 receipt says:

\[
\boxed{
\mathrm{BLOCKED\_EXTERNAL\_ARTIFACT\_ABSENT}.
}
\]

## 8. Blocked is not negative

This distinction matters.

A negative CPS result would require the selected CPS probe to be computed and then fail.

That did not happen.

The needed artifacts are missing.

Therefore:

\[
\boxed{
\text{missing artifacts}
\not\Rightarrow
\text{no signal}.
}
\]

The scientific question remains open.

## 9. The Atlas can still formalize the protocol

The empirical lane is blocked.

The mathematical lane is not.

The Atlas can still define:

- what a CPS probe is;
- how discovery differs from heldout testing;
- what counts as prediction;
- what counts only as description;
- what evidence would be needed for causal promotion.

That is the purpose of the exact finite witness.

## 10. Return to the exact momentum Jacobian

For scalar quadratic curvature \(h\), fix:

\[
\eta=\frac1{10},
\qquad
\beta=\frac9{10}.
\]

The augmented momentum Jacobian is:

\[
J(h)
=
\begin{pmatrix}
1-\frac h{10}&-\frac9{100}\\
h&\frac9{10}
\end{pmatrix}.
\]

This is inherited directly from the audited OPTDYN derivation.

## 11. One invariant is constant

For every \(h\):

\[
\det J(h)=\frac9{10}.
\]

The trace is:

\[
\operatorname{tr}J(h)
=
\frac{19}{10}-\frac h{10}.
\]

Define a toy matrix-derived coordinate:

\[
\kappa(J)
=
1+\det J-\operatorname{tr}J.
\]

Then:

\[
\boxed{
\kappa(J(h))=\frac h{10}.
}
\]

This coordinate is chosen for the witness.

It is not proposed as the CPS statistic for real training.

## 12. Four synthetic windows

Create two discovery windows:

\[
d_0:\quad h=2,\quad \kappa=\frac15,\quad Y=0,
\]

\[
d_1:\quad h=8,\quad \kappa=\frac45,\quad Y=1.
\]

Create two heldout windows:

\[
h_0:\quad h=3,\quad \kappa=\frac3{10},\quad Y=0,
\]

\[
h_1:\quad h=7,\quad \kappa=\frac7{10},\quad Y=1.
\]

The transition labels are synthetic.

They exist only to demonstrate protocol discipline.

## 13. Discovery comes before heldout evaluation

Using the discovery windows only:

\[
\frac15<\frac12<\frac45.
\]

Freeze threshold:

\[
\tau=\frac12.
\]

Prediction rule:

\[
\widehat Y
=
\mathbf 1\{\kappa>\tau\}.
\]

Now the rule is frozen.

The heldout labels cannot be used to change:

- statistic;
- threshold;
- state coordinates;
- horizon;
- normalization.

## 14. Exact heldout replay

For \(h_0\):

\[
\frac3{10}<\frac12,
\]

so:

\[
\widehat Y=0.
\]

For \(h_1\):

\[
\frac7{10}>\frac12,
\]

so:

\[
\widehat Y=1.
\]

Therefore:

\[
\boxed{
(\widehat Y_{h_0},\widehat Y_{h_1})=(0,1).
}
\]

The heldout synthetic labels are recovered exactly.

This proves only that the protocol mechanics are coherent.

## 15. Why one spectral scalar is not enough

All four toy Jacobians have:

\[
\det J=\frac9{10}.
\]

Their characteristic discriminants are all negative.

Therefore each has a complex-conjugate eigenvalue pair.

For each pair:

\[
|\lambda|^2
=
\det J
=
\frac9{10}.
\]

So:

\[
\boxed{
\rho(J)
=
\sqrt{\frac9{10}}
}
\]

for all four toy windows.

The toy labels differ.

The spectral radius does not.

## 16. Same spectral radius, different local maps

For \(h=2\):

\[
J(2)
=
\begin{pmatrix}
\frac45&-\frac9{100}\\
2&\frac9{10}
\end{pmatrix}.
\]

For \(h=8\):

\[
J(8)
=
\begin{pmatrix}
\frac15&-\frac9{100}\\
8&\frac9{10}
\end{pmatrix}.
\]

The matrices are not the same.

Their trace differs.

Their coupling coordinate differs.

Their action on perturbation directions differs.

Thus:

\[
\boxed{
\text{same spectral radius}
\not\Rightarrow
\text{same local augmented-state dynamics}.
}
\]

## 17. This is why CPS is multi-coordinate

The point is not that \(\kappa\) is better than spectral radius.

The point is that different matrix summaries answer different questions.

A real CPS probe may need:

- singular gain;
- finite-horizon gain;
- non-normality;
- update-direction alignment;
- layer-local block structure;
- time-varying products.

The exact toy merely proves that one scalar can be blind.

## 18. Local Jacobians remain local

Suppose a Jacobian changes sharply near a transition.

That supports a local dynamical observation.

It does not prove:

\[
\text{global phase change}.
\]

It does not prove:

\[
\text{optimizer state caused behavioral change}.
\]

It does not prove the same signature persists across checkpoints, tasks, or scales.

The local/global firewall from OPTDYN remains active.

## 19. Retrospective description is the weakest positive CPS result

Imagine scanning all layers, horizons, and statistics after the transition is known.

Suppose one statistic moves dramatically at the transition.

That is interesting.

It is also selected after seeing the answer.

The correct label is:

\[
\mathrm{DESCRIPTIVE\_ONLY}.
\]

It can motivate a new preregistered test.

It is not prediction.

## 20. Prediction requires temporal and selection discipline

A predictive test needs a probe frozen before heldout evaluation.

For checkpoint \(t\), compute:

\[
X_t
=
\mathrm{Probe}_{\Pi_{\rm CPS}}
(\text{artifacts available at or before }t).
\]

Then predict:

\[
Y_t
\]

for the future window:

\[
(t,t+\Delta].
\]

Information from \(t+\Delta\) cannot enter \(X_t\).

Otherwise the future has leaked into the predictor.

## 21. Discovery must be separated from confirmation

The discovery set can choose:

- layer;
- state block;
- horizon;
- statistic;
- threshold;
- normalization;
- estimator.

Then those choices must freeze.

The heldout set tests the frozen object.

This is the difference between:

> I found a curve that moves near transitions.

and:

> I can identify transition risk before the heldout transition occurs.

## 22. A real CPS heldout protocol

For future artifact-complete transition windows:

1. freeze the behavioral transition definition;
2. partition discovery and heldout windows;
3. choose CPS features on discovery only;
4. freeze checkpoint lead \(\Delta\);
5. compute pre-transition features only;
6. compare against non-transition windows;
7. include shuffled-label controls;
8. include simple training-time baselines;
9. test the frozen predictor on heldout transitions;
10. retain negative results.

This structure is already compatible with GSD-WP04's intended exit grammar.

## 23. What counts as PREDICTIVE_SIGNAL?

Use:

\[
\mathrm{PREDICTIVE\_SIGNAL}
\]

only when:

- exact required artifacts exist;
- the probe is frozen before heldout testing;
- the heldout metric clears its preregistered criterion;
- relevant baselines/controls do not explain the result.

This is predictive association.

It is not causality.

## 24. What counts as DESCRIPTIVE_ONLY?

Use:

\[
\mathrm{DESCRIPTIVE\_ONLY}
\]

when:

- a transition-local signature exists;
- but it was selected retrospectively;
- or it fails heldout prediction;
- or heldout confirmation was never preregistered.

Descriptive signals are legitimate research outputs.

They should not be relabeled as forecasts.

## 25. What counts as NO_SIGNAL?

Use:

\[
\mathrm{NO\_SIGNAL}
\]

when:

- the required artifacts exist;
- the declared probe family is executable;
- the preregistered test is actually run;
- the signal fails the declared criteria.

A negative result can save large downstream compute.

## 26. What counts as an artifact block?

Use:

\[
\mathrm{BLOCKED\_EXTERNAL\_ARTIFACT\_ABSENT}
\]

when the selected test cannot be executed because required exact artifacts are unavailable.

That is the current public GSD-WP04 state.

It is an evidence-availability disposition.

It is not a scientific result about CPS.

## 27. Prediction is not cause

Suppose a CPS feature predicts a transition.

The feature can still be:

- a correlate;
- a downstream symptom;
- a common-cause indicator;
- a proxy for training time;
- a proxy for curvature or data composition.

Therefore:

\[
\boxed{
\text{heldout prediction}
\not\Rightarrow
\text{causal optimizer mechanism}.
}
\]

## 28. Causal promotion needs intervention

A stronger test would manipulate the optimizer-side state or update while matching relevant controls.

Examples can include:

- controlled optimizer-state reset;
- controlled moment rescaling;
- update-direction substitution;
- matched optimizer-rule intervention;
- state patching where semantics are well-defined.

The intervention must be specified before the outcome is interpreted.

Only then can the evidence move toward a causal claim.

## 29. The causal hierarchy

Use five levels.

### C0 — behavioral transition

A transition exists independently of CPS.

### C1 — local diagnostic movement

A CPS feature changes near the transition.

### C2 — heldout prediction

A frozen pre-transition feature predicts heldout transition windows.

### C3 — intervention sensitivity

Changing optimizer-side state/update changes transition behavior under matched controls.

### C4 — mechanism-specific support

Intervention, reconstruction, and alternative-hypothesis attacks support a declared mechanism class.

Each level needs new evidence.

## 30. Current GSD is at C0 for CPS

The public source establishes one confirmed behavioral transition.

For CPS specifically, the optimizer artifacts are unavailable.

Therefore current public GSD supports:

\[
C0
\]

as a target transition.

It does not support:

\[
C1,
C2,
C3,
C4
\]

from optimizer-state evidence.

This is not a criticism.

It is the exact evidence boundary.

## 31. One transition cannot validate a general predictor

The current GSD source has one confirmed transition.

A general predictor needs:

- discovery examples;
- heldout examples.

One event can support:

- artifact-readiness work;
- a descriptive case study if artifacts exist.

It cannot establish broad heldout predictive value by itself.

## 32. Small model does not silently become large model

The confirmed public transition is OLMo2 1B.

Even a successful CPS result there would not automatically transfer to:

- OLMo3 7B;
- OLMo3 32B;
- other model families;
- other optimizers;
- post-training settings.

Scale transfer requires its own heldout evidence.

## 33. Artifact completeness is part of the experiment

A CPS packet should identify:

- model revision;
- optimizer state;
- trainer/global step;
- scheduler;
- gradient or update direction if required;
- evaluator/tokenizer;
- code;
- hardware;
- transition label provenance.

If one required artifact is absent, the test is not silently weakened.

The block should be explicit.

## 34. Why exact identity matters

A transition-local probe can be invalidated by stale identity.

Optimizer state from one checkpoint cannot be paired casually with model parameters from another.

Scheduler state from the wrong run is not equivalent.

A CPS result must bind to:

\[
(\text{model},\text{optimizer},\text{step},\text{run},\text{probe code}).
\]

This is scientific provenance, not bookkeeping.

## 35. Time-varying products matter

A real training trajectory is not generally autonomous.

The local perturbation product is:

\[
J_{t+k-1}\cdots J_t.
\]

Therefore finite-horizon CPS may need to estimate a product or its action.

One-step eigenvalues can miss transient amplification.

OPTDYN already proved that lesson in a fixed toy.

CPS turns it into an instrumentation question.

## 36. JVP/VJP sketches can make the probe tractable

A full frontier-scale Jacobian is too large to materialize naively.

The GSD programme therefore contemplates randomized JVP/VJP estimates.

These can target:

- dominant singular directions;
- local gains;
- selected subspaces;
- layer/block couplings.

The result remains an estimate of a declared local object.

It does not become a global training theorem because the computation is scalable.

## 37. Training time is an important baseline

A CPS statistic may drift smoothly with training step.

Behavioral transitions also occur at particular steps.

A naive association can therefore be explained by time itself.

A heldout protocol should compare against:

- checkpoint index;
- tokens seen;
- learning rate;
- update norm;
- other simple progress variables.

A sophisticated probe must outperform the relevant simple baseline to justify its complexity.

## 38. Parameter-only baselines matter

If a parameter-only diagnostic predicts the transition just as well as the optimizer-state probe, then the added optimizer state may not provide incremental value for that prediction task.

This does not make optimizer state irrelevant to training.

It narrows the claim.

CPS should report incremental predictive value when that is the question.

## 39. Stable capability controls matter too

A transition-specific predictor can accidentally be a generic degradation detector.

GSD already protects against this with stable conventional-capability controls.

CPS should inherit that discipline.

A broad collapse is different from a selective generalization-state transition.

## 40. Negative CPS evidence is useful

Suppose optimizer artifacts become available and a carefully preregistered probe returns:

\[
\mathrm{NO\_SIGNAL}.
\]

That is informative.

It can redirect effort toward:

- representation/operator diagnostics;
- accessibility/control mechanisms;
- data-window attribution;
- other causal routes.

The Atlas should preserve such negative results.

## 41. What the current chapter establishes

Mathematically, the chapter establishes:

\[
\det J(h)=\frac9{10},
\]

\[
\kappa(J(h))=\frac h{10},
\]

the exact synthetic discovery/heldout threshold result, and identical spectral radius across all four toy windows.

Scientifically, it establishes the current source boundary:

- one public confirmed GSD behavioral transition exists;
- the public CPS work package exists;
- the exact transition-local public revisions lack optimizer artifacts;
- therefore no public GSD CPS signal disposition is currently authorized.

## 42. Non-implications

The chapter rejects:

\[
\text{behavioral transition}
\not\Rightarrow
\text{optimizer-state transition},
\]

\[
\text{local Jacobian change}
\not\Rightarrow
\text{global training phase change},
\]

\[
\text{retrospective alignment}
\not\Rightarrow
\text{prediction},
\]

\[
\text{heldout prediction}
\not\Rightarrow
\text{causal mechanism},
\]

\[
\text{same spectral radius}
\not\Rightarrow
\text{same augmented-state dynamics},
\]

\[
\text{missing optimizer artifacts}
\not\Rightarrow
\text{no CPS signal},
\]

and:

\[
\text{one 1B transition}
\not\Rightarrow
\text{general predictor across scale}.
\]

## 43. Atlas connections

**Optimizer-State Dynamics.**  
CPS operationalizes the augmented-state Jacobian as an empirical diagnostic object.

**Generalization-State Dynamics.**  
GSD supplies behavioral transition targets and the heldout predictive question.

**Spectral Diagnostics.**  
CPS supplies a transition-local application of spectral, singular-gain, and non-normality probes.

**Experiments as Arguments.**  
Discovery/freeze/heldout separation is part of the claim structure, not merely experimental hygiene.

**Governed research systems.**  
Artifact identity and explicit block states prevent missing evidence from being silently converted into negative findings.

## 44. Closing view

Coupling-Phase Spectroscopy is not a claim that optimizer state explains every transition.

It is a way to ask the question correctly.

First establish the behavioral transition.

Then obtain the exact optimizer-state artifacts.

Then define the local augmented-state probe.

Then separate exploration from heldout prediction.

Then separate prediction from causality.

The current public GSD programme has reached the first step and specified the second.

The required optimizer artifacts are not publicly present at the exact transition checkpoints.

So the present result is neither success nor failure of CPS.

It is a precise boundary:

\[
\boxed{
\text{transition confirmed; optimizer-state spectroscopy currently artifact-blocked}.
}
\]

That is the right place to continue from when the missing evidence becomes available.

## References used in this chapter

External mathematical authority is inherited through audited ATLAS-CH-OPTDYN-001.

Current GCL project evidence is bound to exact public grandchallenge/GSD files at commit:

ebd4681e1815a3d7f0285cc4ce2bc090b38fae8c

See sources/source-locks/ATLAS-CH-CPS-001.yaml for exact identities and claim boundaries.
