# ATLAS-CH-CPS-001 — Derivation Packet

## Scope

This packet formalizes an exact finite Coupling-Phase Spectroscopy toy and a transition-local prediction protocol.

It inherits the augmented optimizer-state recurrence from ATLAS-CH-OPTDYN-001.

It does not establish an empirical GSD optimizer-state signal.

The current public GSD-WP04 lane is artifact-blocked.

## D1. Momentum augmented-state Jacobian

For scalar quadratic curvature \(h\), learning rate \(\eta\), and momentum \(\beta\), OPTDYN gives:

\[
J(h)
=
\begin{pmatrix}
1-\eta h & -\eta\beta\\
h & \beta
\end{pmatrix}.
\]

Fix:

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

## D2. Determinant

Compute:

\[
\det J(h)
=
\left(1-\frac h{10}\right)\frac9{10}
-
\left(-\frac9{100}\right)h.
\]

Therefore:

\[
\det J(h)
=
\frac9{10}
-
\frac{9h}{100}
+
\frac{9h}{100}
=
\boxed{\frac9{10}}.
\]

The determinant is independent of \(h\) in this fixed-\(\eta,\beta\) family.

## D3. Trace

\[
\operatorname{tr}J(h)
=
1-\frac h{10}
+
\frac9{10}
=
\boxed{
\frac{19}{10}-\frac h{10}.
}
\]

## D4. Matrix-derived coupling coordinate

Define:

\[
\kappa(J)
=
1+\det J-\operatorname{tr}J.
\]

For the exact family:

\[
\begin{aligned}
\kappa(J(h))
&=
1+\frac9{10}
-
\left(
\frac{19}{10}-\frac h{10}
\right)\\
&=
\frac h{10}.
\end{aligned}
\]

Thus:

\[
\boxed{
\kappa(J(h))=\frac h{10}.
}
\]

This is an exact matrix-derived coordinate for the toy family.

It is not claimed to be a universal optimizer diagnostic.

## D5. Four exact local windows

Use:

\[
h\in\{2,8,3,7\}.
\]

Define:

### Discovery window \(d_0\)

\[
h=2,
\qquad
\kappa=\frac15,
\qquad
Y=0.
\]

### Discovery window \(d_1\)

\[
h=8,
\qquad
\kappa=\frac45,
\qquad
Y=1.
\]

### Heldout window \(h_0\)

\[
h=3,
\qquad
\kappa=\frac3{10},
\qquad
Y=0.
\]

### Heldout window \(h_1\)

\[
h=7,
\qquad
\kappa=\frac7{10},
\qquad
Y=1.
\]

The labels are synthetic next-window transition labels.

They are part of the protocol witness, not empirical training evidence.

## D6. Discovery-only threshold

Using only discovery windows:

\[
\frac15<\frac12<\frac45.
\]

Freeze:

\[
\boxed{
\tau=\frac12.
}
\]

Define predictor:

\[
\widehat Y
=
\mathbf 1\{\kappa>\tau\}.
\]

No heldout label is used to select \(\tau\).

## D7. Heldout evaluation

For \(h_0\):

\[
\kappa=\frac3{10}<\frac12.
\]

Therefore:

\[
\widehat Y_{h_0}=0.
\]

For \(h_1\):

\[
\kappa=\frac7{10}>\frac12.
\]

Therefore:

\[
\widehat Y_{h_1}=1.
\]

Hence:

\[
\boxed{
(\widehat Y_{h_0},\widehat Y_{h_1})
=
(0,1),
}
\]

which matches the synthetic heldout labels exactly.

This proves only that the declared discovery-freeze-heldout procedure is internally coherent on the finite toy.

## D8. Characteristic polynomial

For the exact family:

\[
p_h(\lambda)
=
\lambda^2
-
\left(
\frac{19}{10}-\frac h{10}
\right)\lambda
+
\frac9{10}.
\]

The discriminant is:

\[
\Delta_h
=
\left(
\frac{19-h}{10}
\right)^2
-
\frac{18}{5}.
\]

## D9. Exact discriminants

### \(h=2\)

\[
\operatorname{tr}J=\frac{17}{10}.
\]

Thus:

\[
\Delta_2
=
\frac{289}{100}
-
\frac{360}{100}
=
-\frac{71}{100}<0.
\]

### \(h=3\)

\[
\operatorname{tr}J=\frac85.
\]

Thus:

\[
\Delta_3
=
\frac{64}{25}
-
\frac{18}{5}
=
-\frac{26}{25}<0.
\]

### \(h=7\)

\[
\operatorname{tr}J=\frac65.
\]

Thus:

\[
\Delta_7
=
\frac{36}{25}
-
\frac{18}{5}
=
-\frac{54}{25}<0.
\]

### \(h=8\)

\[
\operatorname{tr}J=\frac{11}{10}.
\]

Thus:

\[
\Delta_8
=
\frac{121}{100}
-
\frac{360}{100}
=
-\frac{239}{100}<0.
\]

All four matrices have a complex-conjugate eigenvalue pair.

## D10. Identical spectral radius

For a real \(2\times2\) matrix with conjugate eigenvalues:

\[
\lambda_2=\overline{\lambda_1}.
\]

Their product is the determinant:

\[
|\lambda_1|^2
=
\lambda_1\lambda_2
=
\det J.
\]

Here:

\[
\det J=\frac9{10}.
\]

Therefore for all four toy matrices:

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

Thus the toy label separation cannot be implemented by spectral radius alone.

## D11. Same spectral radius does not imply same matrix

For example:

\[
J(2)
=
\begin{pmatrix}
\frac45&-\frac9{100}\\
2&\frac9{10}
\end{pmatrix},
\]

while:

\[
J(8)
=
\begin{pmatrix}
\frac15&-\frac9{100}\\
8&\frac9{10}
\end{pmatrix}.
\]

They have identical determinant and spectral radius but different trace and off-diagonal coupling.

Therefore:

\[
\boxed{
\text{same spectral radius}
\not\Rightarrow
\text{same augmented-state dynamics}.
}
\]

The phrase "dynamics" here refers to the local linear maps themselves, not a global nonlinear training theorem.

## D12. Spectroscopy vector

A CPS probe may collect several coordinates:

\[
\mathcal S(J)
=
\left(
\operatorname{tr}J,
\det J,
\rho(J),
\sigma_{\max}(J),
\mathcal N(J),
G_k(J),
\mathcal A(J)
\right).
\]

No one coordinate is assumed sufficient.

The exact toy makes this concrete because:

\[
\rho(J)
\]

is identical while:

\[
\kappa(J)
=
1+\det J-\operatorname{tr}J
\]

changes.

## D13. Local versus finite-horizon probe

A local statistic depends on one matrix:

\[
s_t=s(J_t).
\]

A finite-horizon statistic can depend on:

\[
P_{t,k}
=
J_{t+k-1}\cdots J_t.
\]

For nonautonomous training, the second cannot generally be replaced by:

\[
J_t^k.
\]

That distinction is inherited from OPTDYN.

## D14. Transition target

Let the behavioural transition target be defined independently:

\[
Y_t
=
\mathbf 1
\{
\text{declared behavioural state transition occurs in }(t,t+\Delta]
\}.
\]

CPS predicts \(Y_t\).

CPS must not redefine \(Y_t\) after seeing optimizer-state diagnostics.

## D15. Discovery stage

On discovery windows only, choose:

- augmented-state coordinates;
- layer/block scope;
- probe statistic;
- estimator;
- finite horizon;
- lead \(\Delta\);
- threshold/model;
- normalization.

Call the complete fitted probe configuration:

\[
\Pi_{\rm CPS}.
\]

After discovery:

\[
\boxed{
\Pi_{\rm CPS}
\text{ is frozen.}
}
\]

## D16. Heldout prediction

For heldout checkpoint \(t\), compute:

\[
X_t
=
\mathrm{Probe}_{\Pi_{\rm CPS}}
(\text{artifacts available at or before }t).
\]

Then predict:

\[
\widehat Y_t
=
g_{\Pi_{\rm CPS}}(X_t).
\]

No artifact from after \(t\) may enter \(X_t\).

Otherwise the protocol leaks the outcome window into the predictor.

## D17. Descriptive alignment versus prediction

A retrospective statistic can be chosen after inspecting all transition windows.

Such a statistic may support:

\[
\mathrm{DESCRIPTIVE\_ONLY}.
\]

It cannot support:

\[
\mathrm{PREDICTIVE\_SIGNAL}
\]

unless its full selection rule was frozen before heldout evaluation.

Thus:

\[
\boxed{
\text{retrospective alignment}
\not\Rightarrow
\text{heldout prediction}.
}
\]

## D18. Prediction versus causality

Suppose:

\[
X_t
\]

predicts:

\[
Y_t.
\]

This supports association with temporal ordering.

It does not prove that changing \(X_t\) or the optimizer state changes the transition.

Therefore:

\[
\boxed{
\text{heldout prediction}
\not\Rightarrow
\text{causal mechanism}.
}
\]

Causal promotion requires intervention or another valid causal design.

## D19. Exact disposition logic

Define four possible CPS outcomes.

### Artifact block

If required exact artifacts are unavailable:

\[
D=
\mathrm{BLOCKED\_EXTERNAL\_ARTIFACT\_ABSENT}.
\]

No signal claim is authorized.

### Predictive signal

If artifacts exist and the frozen predictor clears the preregistered heldout criterion:

\[
D=
\mathrm{PREDICTIVE\_SIGNAL}.
\]

### Descriptive only

If retrospective alignment exists but heldout predictive requirements are not met:

\[
D=
\mathrm{DESCRIPTIVE\_ONLY}.
\]

### No signal

If artifacts exist and the declared probe family fails its preregistered criteria:

\[
D=
\mathrm{NO\_SIGNAL}.
\]

These dispositions are mutually distinguishable because evidence availability and scientific outcome are separate.

## D20. Current public GSD state

The bound GSD-WP03R receipt establishes:

- one robust behavioural transition;
- step 2000 GENERALIZING;
- step 3000 PATTERN_MATCHING;
- step 4000 PATTERN_MATCHING;
- transition localized between steps 2000 and 3000;
- explicit firewall against optimizer cause.

The bound WP04 artifact receipt establishes:

- exact public revisions inspected at steps 2000, 3000, 4000;
- model artifacts are present;
- optimizer/trainer/scheduler/gradient/update-direction artifacts are absent.

Therefore:

\[
\boxed{
D_{\rm GSD,public}
=
\mathrm{BLOCKED\_EXTERNAL\_ARTIFACT\_ABSENT}.
}
\]

No CPS signal result follows.

## D21. Artifact completeness predicate

For selected probe \(\Pi\), define:

\[
A_\Pi(t)=1
\]

when every exact artifact required to compute the pre-registered feature at checkpoint \(t\) is available with identity/provenance.

If:

\[
A_\Pi(t)=0,
\]

then that window is unavailable for the declared CPS test.

This prevents silently substituting a weaker statistic after discovering missing artifacts.

## D22. One transition is not a general predictor test

The current public GSD state has one confirmed transition.

A general heldout transition predictor requires separate discovery and heldout transition windows.

Therefore one transition can serve as:

- a target for artifact-completeness testing;
- a descriptive case study if artifacts exist.

It cannot, by itself, establish a general heldout predictor.

## D23. Durable propositions

1. CPS treats optimizer/model state as an augmented dynamical object.
2. Local Jacobian diagnostics are distinct from behavioural transition labels.
3. The exact toy family has \(\det J=9/10\) and \(\kappa=h/10\).
4. The discovery threshold \(1/2\) correctly classifies both heldout synthetic toy windows.
5. All four toy matrices have identical spectral radius \(\sqrt{9/10}\).
6. Spectral radius alone therefore cannot implement the toy classifier.
7. Retrospective alignment is weaker than heldout prediction.
8. Heldout prediction is weaker than causal optimizer-state evidence.
9. Missing optimizer artifacts are an evidentiary block, not a negative CPS result.
10. Current public GSD state supplies a confirmed behavioural transition but no optimizer-state signal disposition.

## Claim boundary

This packet proves exact properties of a scalar-quadratic momentum family and defines a transition-local prediction/falsification protocol.

It does not prove that the toy coupling coordinate predicts real neural-training transitions, that the GSD behavioural transition was optimizer-caused, that any CPS signal exists in the blocked public checkpoint series, or that one local Jacobian globally describes nonlinear stochastic training.
