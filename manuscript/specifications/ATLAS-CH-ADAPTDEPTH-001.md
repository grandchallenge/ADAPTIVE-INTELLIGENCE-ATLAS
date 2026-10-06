# Chapter Specification — ATLAS-CH-ADAPTDEPTH-001

## Identity

**Title:** Adaptive Depth as Error Control  
**Part:** Numerical Intelligence and Composition  
**Status:** specification-ready.  
**Epistemic class:** audited numerical/adaptive-depth substrate + primary adaptive-computation sources + Atlas synthesis.

## Chapter contract

Connect learned stopping and adaptive computation to local error estimation and adaptive time stepping without identifying those mechanisms by analogy alone.

The chapter must keep four control objects separate:

1. **execution depth** — how many computational stages are run;
2. **numerical step size** — mesh spacing for a declared reference evolution problem;
3. **local error estimate** — an estimator tied to a declared numerical method and target error;
4. **learned halting/compute score** — a learned signal used to stop, route, or allocate computation.

## Hard prerequisites

- ATLAS-CH-DEPTH-001 / AUDIT-018;
- ATLAS-CH-NETNUM-001 / AUDIT-023.

Exact prerequisite identities and external claim boundaries are locked in:

sources/source-locks/ATLAS-CH-ADAPTDEPTH-001.yaml

## Reader outcome

A reader should be able to:

1. distinguish adaptive depth from adaptive numerical step size;
2. define a local error estimator and state what it is estimating;
3. explain why an embedded pair can support accept/reject and step-size control;
4. explain why low estimated local error does not automatically imply low global error;
5. explain why a learned halting score is not an error estimate without a declared relation;
6. distinguish criterion_met from budget_exhausted;
7. write an explicit interface that converts an error estimate or calibrated halting signal into a stopping rule;
8. identify what must be re-proved before importing adaptive-step convergence guarantees into learned systems.

## Formal spine

Let a declared numerical state evolve by a one-step method

\[
x_{n+1}=\Psi_{h_n}(x_n).
\]

A local error-control mechanism additionally requires an estimator

\[
\widehat e_n
\]

for a declared local error quantity in a declared norm.

An accept/reject controller has the form

\[
\text{accept step}
\iff
\widehat e_n\le \tau_n,
\]

where \(\tau_n\) is a declared tolerance.

If the method order relevant to the estimator is \(p\), a generic idealized step-size update has the form

\[
h_{n+1}
=
\eta h_n
\left(
\frac{\tau_n}{\widehat e_n}
\right)^{1/(p+1)},
\]

subject in practice to safety factors and growth/shrinkage clamps.

The chapter uses this only as a controller template, not as a universal optimal rule.

## Embedded-pair object

Suppose two same-step approximations are available:

\[
x_{n+1}^{[p]},
\qquad
x_{n+1}^{[p+1]}.
\]

An embedded estimator can use

\[
\widehat e_n
=
\left\|
x_{n+1}^{[p+1]}
-
x_{n+1}^{[p]}
\right\|.
\]

The difference estimates a method-specific local error under the corresponding order/smoothness assumptions.

It is not automatically:

- the exact local error;
- the accumulated global error;
- a task loss;
- a learned uncertainty score.

Dormand-Prince is used as a primary embedded Runge-Kutta precedent [@DormandPrince1980].

## Exact witness A — embedded local-error control

Take

\[
y'(t)=t,
\qquad
y(0)=0.
\]

The exact solution is

\[
y(t)=t^2/2.
\]

For one step of length \(h\):

Euler gives

\[
y_E(h)=0.
\]

Explicit trapezoid / Heun gives

\[
y_H(h)=h^2/2.
\]

Since the exact value is \(h^2/2\),

\[
y_H(h)=y(h)
\]

and

\[
\widehat e(h)
=
|y_H(h)-y_E(h)|
=
h^2/2
\]

is exactly the Euler one-step error for this witness.

Choose

\[
\tau=1/8.
\]

At \(h=1\),

\[
\widehat e=1/2>\tau,
\]

so the step is rejected.

For low-order \(p=1\), the unclamped unit-safety controller gives

\[
h_{\mathrm{new}}
=
h
\left(
\frac{\tau}{\widehat e}
\right)^{1/2}
=
1\sqrt{\frac{1/8}{1/2}}
=
1/2.
\]

At \(h=1/2\),

\[
\widehat e
=
(1/2)^2/2
=
1/8,
\]

so the step meets the tolerance exactly.

## Learned halting object

Let a learned computation produce states

\[
z_0,z_1,\ldots
\]

and a halting score

\[
q_k=q(z_k,\text{context}).
\]

A generic bounded stopping rule is

\[
\tau
=
\min
\left(
\{k\le K_{\max}:q_k\le \delta\}
\cup
\{K_{\max}\}
\right).
\]

The system must retain whether it stopped because:

- criterion_met; or
- budget_exhausted.

This is inherited from DEPTH.

The score \(q_k\) becomes an error-control object only after a relation to a declared target error \(E_k\) is established.

Examples of sufficient relations include:

\[
E_k\le B(q_k)
\]

for a known bound function \(B\), or another explicitly proved/certified guarantee.

Correlation, ranking, or monotonicity alone is insufficient.

## Exact witness B — monotone halting score is not calibrated error

Use the audited DEPTH recurrence

\[
x_{k+1}=(x_k+2)/2,
\qquad
x_0=0.
\]

Its true fixed-point error is

\[
E_k=|x_k-2|=2^{1-k}.
\]

Define the perfectly monotone score

\[
q_k=4^{-k}.
\]

Then

\[
q_k=E_k^2/4.
\]

The score ranks all depths exactly by error, but it is not on the error scale.

At \(k=2\),

\[
q_2=1/16,
\qquad
E_2=1/2.
\]

A stopping rule that incorrectly treats

\[
q_k\le 1/16
\]

as equivalent to

\[
E_k\le1/16
\]

stops at \(k=2\) while the true error is eight times the requested tolerance.

If the exact relation

\[
E_k=2\sqrt{q_k}
\]

is known, the correct threshold for target error \(\varepsilon\) is instead

\[
q_k\le(\varepsilon/2)^2.
\]

This witness separates ranking quality from magnitude calibration.

## Adaptive depth versus adaptive step size

Two common controls must not be conflated.

### Variable number of fixed stages

\[
z_{k+1}=F_k(z_k),
\qquad
k<\tau(x).
\]

The input chooses how many stages execute.

### Variable mesh spacing

\[
x_{n+1}=\Psi_{h_n}(x_n),
\]

with \(h_n\) chosen by a numerical error controller for a declared reference evolution.

Both allocate computation adaptively.

Only the second is an adaptive time-step method by definition.

A learned architecture becomes the numerical object only when the reference dynamics, discretization, error estimator, and control law are actually declared and justified.

## Spatial adaptive computation

Figurnov et al. provide a source-scoped example of computation allocated differently across spatial locations [@FigurnovEtAl2017].

The chapter may use this to illustrate nonuniform execution.

It must not infer:

\[
\text{spatially variable network depth}
\Rightarrow
\text{adaptive spatial discretization of a PDE}.
\]

That stronger statement requires an actual PDE/discretization interface.

## Error-control interface

A complete error-control declaration names:

- target quantity;
- target error \(E\);
- norm or loss;
- estimator \(\widehat e\);
- tolerance \(\tau\);
- acceptance/stopping rule;
- budget cap;
- criterion_met versus budget_exhausted;
- update policy after rejection;
- assumptions linking estimator to target error;
- global-error/stability obligations.

## Failure boundaries

- adaptive depth != adaptive numerical step size;
- learned halting score != local-error estimate;
- monotone score != calibrated magnitude;
- local error estimate != global error guarantee;
- embedded difference != exact error in general;
- smaller estimated local error != task correctness;
- more computation != monotone quality improvement;
- budget exhaustion != convergence;
- learned spatial compute != adaptive PDE mesh;
- expected calibration != per-instance certified upper bound;
- error control != compute optimality.

## Source use

- Graves ACT: learned variable recurrent computation [@Graves2016ACT];
- Figurnov et al.: spatially varying adaptive computation in residual networks [@FigurnovEtAl2017];
- Dormand-Prince: embedded Runge-Kutta formulas and numerical local-error-control mechanism [@DormandPrince1980].

## Downstream role

This chapter currently has no architecture-state direct consumer.

It nevertheless supplies a reusable interface for later synthesis:

\[
\boxed{
\text{adaptive computation}
=
\text{state evolution}
+
\text{error/halting signal}
+
\text{declared semantics}
+
\text{controller}
+
\text{budget/failure state}.
}
\]

No later chapter may treat a learned stop signal as certified numerical error without importing the corresponding relation and assumptions.
