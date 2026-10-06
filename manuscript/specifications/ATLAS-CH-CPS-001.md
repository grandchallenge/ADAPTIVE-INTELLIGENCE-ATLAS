# Chapter Specification — ATLAS-CH-CPS-001

## Identity

**Title:** Coupling-Phase Spectroscopy  
**Part:** Optimization as Geometry and Dynamics  
**Status target:** draft-v0.1  
**Implementation issue:** #239  
**Protected baseline:** 0ca38f5d7129db6209b2f245c14a27148df09608

## Hard prerequisite

ATLAS-CH-OPTDYN-001 / AUDIT-002.

Exact prerequisite identities, the refreshed GSD project state, and the claim boundary are frozen in:

sources/source-locks/ATLAS-CH-CPS-001.yaml

## Current public GCL boundary

The October 6, 2026 source refresh changes the older OPTDYN source-gap statement.

Current public GCL state now contains:

- GSD-001 as an executable Generalization-State Dynamics programme;
- GSD-WP04 — CPS transition-local dynamics;
- one confirmed OLMo2-1B behavioural transition under the frozen GSD protocol;
- an exact WP04 artifact-availability receipt.

The confirmed transition is:

\[
\text{GENERALIZING at step 2000}
\longrightarrow
\text{PATTERN\_MATCHING by step 3000/4000}
\]

for truthy_answer/surprising_truth.

The public transition-local revisions inspected by WP04 expose model weights/config/tokenizer artifacts but no:

- optimizer state;
- trainer state;
- scheduler state;
- gradient artifact;
- update-direction artifact.

Therefore the current project-level CPS disposition is:

\[
\boxed{\mathrm{BLOCKED\_EXTERNAL\_ARTIFACT\_ABSENT}}.
\]

This is not:

\[
\mathrm{NO\_SIGNAL}.
\]

No optimizer-state signature was tested because the required artifacts are absent.

## Chapter contract

Define Coupling-Phase Spectroscopy as a disciplined diagnostic programme over the augmented model-optimizer state.

The chapter must distinguish:

1. **behavioural transition target**;
2. **local augmented-state diagnostic**;
3. **retrospective descriptive alignment**;
4. **held-out pre-transition prediction**;
5. **causal optimizer-state mechanism evidence**.

The chapter must not infer the fifth from any of the first four.

## Core augmented-state object

For local training state \(z_t\),

\[
z_{t+1}=F_t(z_t,\xi_t),
\]

with local Jacobian

\[
J_t=
\frac{\partial F_t}{\partial z}(z_t,\xi_t).
\]

For a short horizon \(k\),

\[
P_{t,k}
=
J_{t+k-1}\cdots J_t.
\]

Candidate CPS diagnostics can include:

- trace;
- determinant;
- eigenvalue/spectral-radius estimates;
- dominant singular gain;
- finite-horizon gain;
- non-normality proxies;
- JVP/VJP sketches;
- selected matrix blocks;
- angles between transient directions and task-gradient/update directions.

No one scalar is assumed universally sufficient.

## Spectroscopy vector

Use the explanatory diagnostic vector

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
\Bigr),
\]

where:

- \(\rho\): spectral radius estimate;
- \(\widehat\sigma_{\max}\): dominant singular-gain estimate;
- \(\mathcal N\): declared non-normality proxy;
- \(\widehat G_{t,k}\): finite-horizon gain estimate;
- \(\mathcal A_t\): declared directional/alignment statistic.

This vector is diagnostic notation, not a latent-state ontology.

## Exact finite momentum family

Inherit the scalar quadratic momentum recurrence from OPTDYN:

\[
J(h)
=
\begin{pmatrix}
1-\eta h & -\eta\beta\\
h & \beta
\end{pmatrix}.
\]

Fix

\[
\eta=\frac1{10},
\qquad
\beta=\frac9{10}.
\]

Then:

\[
\boxed{
J(h)
=
\begin{pmatrix}
1-\frac h{10} & -\frac9{100}\\
h & \frac9{10}
\end{pmatrix}.
}
\]

Its determinant is:

\[
\boxed{
\det J(h)=\frac9{10}.
}
\]

Its trace is:

\[
\operatorname{tr}J(h)
=
\frac{19}{10}-\frac h{10}.
\]

Define the matrix-derived toy coupling coordinate:

\[
\boxed{
\kappa(J)
=
1+\det J-\operatorname{tr}J.
}
\]

For this exact family:

\[
\boxed{
\kappa(J(h))=\frac h{10}.
}
\]

The coordinate is not proposed as a universal CPS statistic.

It exists to make the finite prediction protocol exact.

## Exact four-window toy

Define four synthetic local windows:

| Window | role | \(h\) | \(\kappa\) | next-window transition label |
|---|---|---:|---:|---:|
| \(d_0\) | discovery | 2 | \(1/5\) | 0 |
| \(d_1\) | discovery | 8 | \(4/5\) | 1 |
| \(h_0\) | heldout | 3 | \(3/10\) | 0 |
| \(h_1\) | heldout | 7 | \(7/10\) | 1 |

The labels are synthetic protocol labels.

They are not derived from GSD.

## Frozen discovery rule

Using only discovery windows \(d_0,d_1\), freeze threshold:

\[
\tau=\frac12.
\]

Prediction rule:

\[
\widehat Y=
\mathbf 1\{\kappa>\tau\}.
\]

Then do not change:

- \(\kappa\);
- threshold;
- horizon;
- state coordinates;
- window construction.

Evaluate on heldout windows.

## Exact heldout prediction

For \(h_0\):

\[
\kappa=\frac3{10}<\frac12
\]

so:

\[
\widehat Y=0.
\]

For \(h_1\):

\[
\kappa=\frac7{10}>\frac12
\]

so:

\[
\widehat Y=1.
\]

Thus:

\[
\boxed{
(\widehat Y_{h_0},\widehat Y_{h_1})=(0,1),
}
\]

matching the synthetic heldout labels.

This validates only the mechanics of discovery-freeze-heldout evaluation.

It does not establish empirical CPS predictive value.

## Spectral-radius control

For \(h\in\{2,3,7,8\}\),

\[
\det J(h)=\frac9{10}.
\]

The traces are:

\[
\frac{17}{10},
\frac{16}{10},
\frac{12}{10},
\frac{11}{10}.
\]

For all four matrices:

\[
(\operatorname{tr}J)^2
-
4\det J
<0.
\]

Therefore each matrix has a complex-conjugate eigenvalue pair.

For a real \(2\times2\) matrix with conjugate eigenvalues and determinant \(9/10\),

\[
|\lambda_1|
=
|\lambda_2|
=
\sqrt{\frac9{10}}.
\]

Hence:

\[
\boxed{
\rho(J(2))
=
\rho(J(3))
=
\rho(J(7))
=
\rho(J(8))
=
\sqrt{\frac9{10}}.
}
\]

The spectral radius alone is therefore constant across the four toy windows and cannot implement the toy threshold classifier.

This is an exact demonstration that one spectral scalar can miss state information present elsewhere in the matrix.

## Real transition target versus toy probe

The real GSD transition supplies an empirical target object.

The exact Jacobian family supplies a mathematical protocol witness.

They must not be fused.

The chapter must say explicitly:

> the current GSD source establishes a behavioural transition but does not provide the optimizer artifacts required to compute the corresponding CPS probe.

## Transition-local prediction protocol

For a future artifact-complete campaign:

### P0 — behavioural target lock

Freeze:

- task;
- behavioural score;
- transition criterion;
- checkpoint identities;
- transition windows.

CPS may not redefine transitions after inspecting optimizer diagnostics.

### P1 — discovery partition

Use designated discovery transitions/checkpoint windows to choose:

- augmented-state coordinates;
- layer/block scope;
- probe statistic;
- JVP/VJP estimator;
- finite horizon \(k\);
- lead time \(\Delta\);
- threshold or prediction model;
- normalization.

Post hoc best-layer/statistic selection is exploratory only.

### P2 — freeze

Freeze the probe configuration before heldout transition evaluation.

The freeze record must include exact code/environment/artifact identities.

### P3 — pre-transition measurement

For checkpoint \(t\), compute the frozen CPS probe using only artifacts available at or before \(t\).

Do not use \(t+\Delta\) state in the feature.

### P4 — heldout target

Define:

\[
Y_t
=
\mathbf 1
\{
\text{predeclared behavioural transition occurs in }(t,t+\Delta]
\}.
\]

### P5 — heldout evaluation

Evaluate the frozen predictor on heldout windows.

The heldout set cannot have been used to choose:

- layer;
- metric;
- horizon;
- threshold;
- normalization;
- checkpoint offset.

### P6 — controls

Include at least:

- non-transition windows;
- shuffled transition labels;
- checkpoint-time or training-progress baseline;
- parameter-only baseline where meaningful;
- simple optimizer scalars such as learning rate/update norm;
- stable conventional-capability controls.

The exact control set is experiment-specific and must be preregistered.

## Disposition grammar

The chapter inherits GSD-WP04's three scientific exits but adds an evidentiary block state.

### PREDICTIVE_SIGNAL

Use only when a frozen pre-transition probe clears the preregistered heldout criterion.

This supports predictive association.

It does not prove cause.

### DESCRIPTIVE_ONLY

Use when a signal aligns retrospectively with transition windows but does not satisfy heldout predictive requirements.

### NO_SIGNAL

Use when artifacts are available and the declared frozen probe family fails its preregistered descriptive/predictive criteria.

### BLOCKED_EXTERNAL_ARTIFACT_ABSENT

Use when the required optimizer-state artifacts are unavailable.

This is the current public GSD-WP04 disposition.

It is not scientific rejection of CPS.

## Evidence ladder

### C0 — behavioural transition

A GSD-style transition is established independently of CPS.

### C1 — local diagnostic movement

A CPS statistic changes near the transition.

This is descriptive.

### C2 — heldout prediction

A frozen pre-transition CPS probe predicts heldout transition windows.

This supports predictive association.

### C3 — intervention sensitivity

A controlled optimizer-state/update intervention changes the probe and transition probability under matched controls.

This begins causal evidence.

### C4 — mechanism-specific support

Multiple intervention/reconstruction results support a declared optimizer-state mechanism class while alternatives are attacked.

None of these levels is a universal phase theorem.

## Causal firewall

The chapter must reject:

\[
\text{CPS diagnostic moves}
\not\Rightarrow
\text{optimizer state caused transition}.
\]

It must also reject:

\[
\text{CPS predicts transition}
\not\Rightarrow
\text{CPS variable is causal}.
\]

Causal promotion requires intervention or another valid causal design.

## Generalization-state firewall

A predictor for one GSD behavioural transition does not automatically predict:

- other probes;
- other datasets;
- other model scales;
- other optimizers;
- downstream post-training transfer.

Cross-task/model claims require new heldout evidence.

## Artifact completeness contract

A CPS execution packet should include exact identities for:

- model parameters;
- optimizer first/second moments or equivalent state;
- scheduler state;
- trainer/global step;
- gradient or update-direction artifacts where required by the selected probe;
- tokenizer/evaluator;
- code;
- transition labels;
- hardware/runtime.

If the selected statistic cannot be computed from available artifacts, return an explicit block.

## Current GSD interpretation

The public GSD record supports:

\[
\boxed{
\text{one confirmed behavioural transition}
}
\]

and:

\[
\boxed{
\text{WP04 optimizer-state evidence unavailable at exact public revisions}.
}
\]

It does not currently support:

\[
\mathrm{PREDICTIVE\_SIGNAL},
\]

\[
\mathrm{DESCRIPTIVE\_ONLY},
\]

or:

\[
\mathrm{NO\_SIGNAL}.
\]

The correct current disposition is the artifact block.

## Required non-implications

The manuscript must explicitly reject:

\[
\text{behavioural transition}
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

and

\[
\text{one small-model transition}
\not\Rightarrow
\text{general predictor across scale}.
\]

## Reader outcomes

A reader should be able to:

1. define CPS as augmented-state diagnostic instrumentation;
2. distinguish behavioural target from optimizer-state probe;
3. reproduce the exact \(J(h)\) family;
4. derive \(\det J=9/10\);
5. derive \(\kappa=h/10\);
6. reproduce the discovery/heldout toy;
7. prove that spectral radius is identical across the four toy windows;
8. state the discovery-freeze-heldout protocol;
9. distinguish descriptive, predictive, and causal evidence;
10. state why current public GSD WP04 is blocked rather than negative.

## Required artifacts

- source lock with current GSD refresh;
- specification;
- derivation packet;
- exact computational witness;
- reader manuscript;
- Chapter Ledger promotion;
- Source Register entry;
- transaction receipt;
- mandatory post-draft audit.

## Downstream handoff

CPS should provide reusable language for:

- spectral diagnostics;
- optimizer stabilization studies;
- generalization-state dynamics;
- transition-local experimental design;
- heldout mechanistic prediction;
- controlled optimizer interventions.

Downstream chapters may inherit:

- augmented-state probe grammar;
- discovery/freeze/heldout discipline;
- disposition separation;
- artifact-completeness checks.

They may not inherit a project-specific predictive or causal CPS result until one is actually supported.

## References used in this chapter

External mathematical authority is inherited through audited ATLAS-CH-OPTDYN-001.

Current project evidence is bound to exact public files in grandchallenge/GSD at commit:

ebd4681e1815a3d7f0285cc4ce2bc090b38fae8c

Exact source identities and claim boundaries are recorded in:

sources/source-locks/ATLAS-CH-CPS-001.yaml
