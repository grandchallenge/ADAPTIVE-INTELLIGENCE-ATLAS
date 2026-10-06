# ATLAS-CH-ADAPTDEPTH-001 — Derivation Packet

## Scope

This packet establishes the exact finite-dimensional claims used by Adaptive Depth as Error Control.

It does not prove convergence of arbitrary adaptive solvers, correctness of learned stopping, or equivalence between neural depth and numerical mesh refinement.

## D1. Local error-control objects

For a declared one-step method

\[
x_{n+1}=\Psi_h(x_n),
\]

a local error-control mechanism requires:

- a target local error quantity \(e_n\);
- an estimator \(\widehat e_n\);
- a tolerance \(\tau_n\);
- an accept/reject rule;
- a step-size or execution-depth update.

Without these objects, “adaptive” only means computation changes with state/input.

It does not yet mean error control.

## D2. Embedded pair

Suppose the same stage evaluations produce approximations of nominal orders \(p\) and \(p+1\):

\[
x_{n+1}^{[p]},
\qquad
x_{n+1}^{[p+1]}.
\]

Define

\[
\widehat e_n
=
\left\|
x_{n+1}^{[p+1]}-x_{n+1}^{[p]}
\right\|.
\]

For a proper embedded pair, this difference carries method-specific asymptotic information about local truncation error.

The exact relation depends on the pair and assumptions.

Therefore the Atlas treats \(\widehat e_n\) as an estimator, not a universal equality.

## D3. Exact Euler/Heun witness

Consider

\[
y'(t)=t,
\qquad
y(0)=0.
\]

Integrating exactly gives

\[
y(t)=t^2/2.
\]

At \(t_0=0\), one step of length \(h\) begins from \(y_0=0\).

Euler:

\[
k_1=f(0,0)=0,
\]

so

\[
y_E
=
y_0+h k_1
=
0.
\]

Heun / explicit trapezoid uses

\[
k_1=0,
\]

Euler predictor

\[
\widetilde y
=
y_0+h k_1
=
0,
\]

and

\[
k_2=f(h,\widetilde y)=h.
\]

Therefore

\[
y_H
=
y_0+\frac h2(k_1+k_2)
=
\frac{h^2}{2}.
\]

The exact endpoint is

\[
y(h)=h^2/2.
\]

Hence

\[
y_H=y(h).
\]

The Euler one-step error is therefore

\[
e_E(h)
=
|y(h)-y_E|
=
h^2/2.
\]

The pair difference is

\[
|y_H-y_E|
=
h^2/2.
\]

Thus for this declared witness,

\[
\widehat e(h)=e_E(h)
\]

exactly.

This exact identity is special to the witness, not a general theorem about embedded pairs.

## D4. Accept/reject witness

Choose tolerance

\[
\tau=1/8.
\]

At \(h=1\),

\[
\widehat e(1)=1/2.
\]

Since

\[
1/2>1/8,
\]

the step is rejected.

At \(h=1/2\),

\[
\widehat e(1/2)
=
\frac{(1/2)^2}{2}
=
1/8.
\]

Under a non-strict accept rule,

\[
\widehat e\le\tau,
\]

the \(h=1/2\) step is accepted.

## D5. Idealized step-size update

For a low-order method of order \(p\), local truncation error scales asymptotically like

\[
C h^{p+1}.
\]

Ignoring safety factors and clamps, an idealized controller rescales by

\[
h_{\mathrm{new}}
=
h
\left(
\frac{\tau}{\widehat e}
\right)^{1/(p+1)}.
\]

For the Euler low-order member, \(p=1\).

Using \(h=1\), \(\widehat e=1/2\), and \(\tau=1/8\),

\[
h_{\mathrm{new}}
=
1
\left(
\frac{1/8}{1/2}
\right)^{1/2}
=
(1/4)^{1/2}
=
1/2.
\]

Substitution into the exact witness gives

\[
\widehat e(1/2)=1/8.
\]

The controller therefore lands exactly on tolerance in this witness.

## D6. Local error versus global error

A local estimate controls one proposed step.

A global error over many accepted steps depends on:

- how local errors accumulate;
- stability/amplification;
- the evolving state;
- mesh sequence;
- method consistency/order;
- problem regularity.

Therefore

\[
\widehat e_n\le\tau_n\quad\forall n
\]

does not by algebra alone prove a specific global-error bound.

Such a theorem requires the numerical-analysis hypotheses inherited from NETNUM/NUMERICS.

## D7. Learned halting

Let a learned iterative computation have states

\[
z_{k+1}=F_k(z_k)
\]

and halting score

\[
q_k.
\]

With budget \(K_{\max}\) and score threshold \(\delta\),

\[
\tau
=
\min
\left(
\{k\in\{0,\ldots,K_{\max}\}:q_k\le\delta\}
\cup
\{K_{\max}\}
\right).
\]

This defines a stopping rule.

It does not define what \(q_k\) means.

The semantics of \(q_k\) come from its training target, probabilistic interpretation, or proved relation to another quantity.

## D8. Exact halting-score counterexample

Use

\[
x_{k+1}
=
(x_k+2)/2,
\qquad
x_0=0.
\]

The audited DEPTH derivation gives

\[
x_k=2(1-2^{-k})
\]

and true fixed-point error

\[
E_k
=
|x_k-2|
=
2^{1-k}.
\]

Define

\[
q_k=4^{-k}.
\]

Then

\[
E_k^2
=
2^{2-2k}
=
4\cdot4^{-k},
\]

so

\[
q_k=E_k^2/4.
\]

Thus \(q_k\) is a strictly monotone function of the true error.

It ranks depth perfectly.

At \(k=2\),

\[
q_2=4^{-2}=1/16.
\]

But

\[
E_2=2^{-1}=1/2.
\]

Therefore the stopping predicate

\[
q_k\le1/16
\]

is not equivalent to

\[
E_k\le1/16.
\]

The score can be perfectly rank-aligned with error yet badly miscalibrated in magnitude.

## D9. Recovering a correct threshold when the mapping is known

Since

\[
E_k=2\sqrt{q_k},
\]

a desired error tolerance \(\varepsilon\) satisfies

\[
E_k\le\varepsilon
\]

iff

\[
2\sqrt{q_k}\le\varepsilon.
\]

Equivalently,

\[
q_k\le(\varepsilon/2)^2.
\]

This illustrates the missing object in an uncalibrated halting rule: a relation between score and target error.

## D10. Ranking is weaker than control

Suppose \(q_i<q_j\) iff \(E_i<E_j\).

This establishes perfect ordering.

An error-control threshold requires a magnitude implication such as

\[
q\le\delta
\Rightarrow
E\le\varepsilon.
\]

Ordering alone does not determine \(\delta\) for a requested \(\varepsilon\).

Therefore:

\[
\text{perfect ranking}
\not\Rightarrow
\text{calibrated error control}.
\]

## D11. Expected calibration is weaker than per-instance certification

Suppose a learned score has an average relation such as

\[
E[E_k\mid q_k=s]=g(s).
\]

This is useful probabilistic calibration.

It does not imply

\[
E_k\le g(s)
\]

for every individual state.

Thus a controller that requires a hard per-instance error guarantee needs a bound or high-probability statement appropriate to that requirement, not merely conditional mean calibration.

## D12. Adaptive depth versus adaptive time stepping

Variable computation count:

\[
z_{k+1}=F_k(z_k),
\qquad
k<\tau(x).
\]

Adaptive time step:

\[
x_{n+1}
=
\Psi_{h_n}(x_n),
\]

where \(h_n\) parameterizes a declared discretization of a reference evolution and is changed by an error controller.

The first changes how many computational stages execute.

The second changes the mesh of a declared numerical problem.

The same architecture may eventually instantiate both, but neither implies the other.

## D13. Fixed horizon accounting

If adaptive steps advance a declared time coordinate by \(h_n\), then reaching horizon \(T\) requires

\[
\sum_{n=0}^{N-1}h_n=T
\]

up to the method's end-step convention.

Changing \(N\) while keeping every \(h_n\) fixed generally changes the represented horizon.

Changing \(h_n\) while keeping \(T\) fixed changes the mesh.

This is why “more layers” and “smaller step size” are not interchangeable without a fixed reference horizon and scale relation.

## D14. Budget exhaustion

Let an error controller have maximum work \(K_{\max}\).

If no candidate meets tolerance before the cap, termination is

\[
\text{budget_exhausted},
\]

not

\[
\text{criterion_met}.
\]

This distinction is inherited from AUDIT-018 and applies equally to learned halting and numerical error control.

## D15. Compute optimality is another problem

An error controller can target accuracy without minimizing:

- FLOPs;
- latency;
- energy;
- memory traffic;
- dollar cost.

A learned halting policy can target expected cost without certifying numerical error.

Therefore error control and compute optimization are separate objectives unless a joint objective is declared.

## Durable propositions

1. Adaptive computation is not automatically adaptive numerical integration.
2. An embedded pair supplies a method-specific local-error estimator, not a universal exact error oracle.
3. In the Euler/Heun witness on y'=t, the embedded difference equals the Euler one-step error exactly.
4. The idealized order-based controller maps h=1 to h=1/2 for tolerance 1/8 in the exact witness.
5. Local error acceptance does not by itself prove a global error bound.
6. A learned halting score can perfectly rank true error while being badly miscalibrated in magnitude.
7. Turning a learned score into error control requires an explicit relation between score and target error.
8. Probabilistic calibration is weaker than a per-instance certified upper bound.
9. Budget exhaustion must remain distinct from criterion satisfaction.
10. Error control is distinct from compute optimality.
