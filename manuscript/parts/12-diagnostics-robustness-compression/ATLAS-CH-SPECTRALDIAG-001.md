# Spectral and Operator Diagnostics
<!-- ATLAS-CH-SPECTRALDIAG-001 -->

**Epistemic status:** audited non-normal/operator substrate + audited mechanistic-diagnostics substrate + one primary Koopman source + Atlas-owned exact finite controls.  
**Specification:** manuscript/specifications/ATLAS-CH-SPECTRALDIAG-001.md  
**Derivation packet:** mathematics/derivations/ATLAS-CH-SPECTRALDIAG-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-SPECTRALDIAG-001.md  
**Source lock:** sources/source-locks/ATLAS-CH-SPECTRALDIAG-001.yaml

A spectrum is never just “the spectrum.”

It is the spectrum of a particular object:

- a weight matrix;
- a transition matrix;
- a Jacobian at a reference state;
- a Hessian at a parameter point;
- a Koopman operator on a declared observable space;
- a finite empirical approximation to one of these.

The governing rule is:

\[
\boxed{\text{name the operator, reference point, and metric before interpreting the diagnostic.}}
\]

## 1. Different spectral objects answer different questions

For a matrix A, eigenvalues summarize invariant linear modes in one sense.

Singular values summarize Euclidean amplification geometry.

Pseudospectra and resolvent norms expose sensitivity and non-normal behavior that eigenvalues alone may hide.

A Jacobian spectrum is local to a state.

A Hessian spectrum is local to a parameter point and objective.

A Koopman spectrum belongs to an operator acting on observables.

These are not interchangeable.

## 2. The non-normal boundary

The audited NONNORMAL chapter already establishes the crucial warning:

\[
\rho(A)<1
\]

need not prevent finite-horizon amplification when A is non-normal.

Therefore an eigenvalue diagnostic cannot silently substitute for transient-response or pseudospectral diagnostics.

## 3. Exact equal-eigenvalue control

Take

\[
D=\begin{pmatrix}1/2&0\\0&1/2\end{pmatrix},
\qquad
N=\begin{pmatrix}1/2&2\\0&1/2\end{pmatrix}.
\]

Both have eigenvalue multiset

\[
\{1/2,1/2\}.
\]

For

\[
e_2=(0,1)^\top,
\]

\[
\|De_2\|_2^2=1/4,
\]

while

\[
\|Ne_2\|_2^2=17/4.
\]

So equal eigenvalues coexist with sharply different finite response.

The diagnostic lesson is simple:

\[
\boxed{\text{eigenvalue equality}\not\Rightarrow\text{response equality}}.
\]

## 4. Singular values are different from eigenvalues

The singular values of A are the square roots of the eigenvalues of

\[
A^*A.
\]

They describe Euclidean input-output amplification.

For non-normal systems they can be much more directly related to one-step gain than eigenvalues are.

But singular values still discard orientation information.

## 5. Equal singular values can hide interface differences

Let

\[
A=\operatorname{diag}(2,1/2),
\qquad
B=\operatorname{diag}(1/2,2).
\]

Both have the same eigenvalue multiset and the same singular-value multiset:

\[
\{2,1/2\}.
\]

Yet for a fixed interface vector

\[
e_1=(1,0)^\top,
\]

\[
\|Ae_1\|_2=2,
\]

while

\[
\|Be_1\|_2=1/2.
\]

The difference is not in the global singular-value list.

It is in relative position.

## 6. Relative-position diagnostics

A system often interacts with fixed subspaces, readouts, token directions, residual channels, control inputs, or protected interfaces.

A useful diagnostic may therefore involve quantities such as

\[
\|Av\|,
\]

principal angles between singular subspaces and a declared interface subspace, or projected gains such as

\[
\|P_Y A P_X\|.
\]

These are not purely spectral invariants of A.

They are operator-plus-interface diagnostics.

## 7. Zero spectral drift need not mean zero behavioral drift

Move from A to B in the previous example.

The sorted eigenvalue multiset is unchanged.

The sorted singular-value multiset is unchanged.

So a drift score using only either multiset is zero.

But the response to e1 changes from 2 to 1/2.

Thus

\[
\boxed{\text{zero spectral-summary drift}\not\Rightarrow\text{zero interface drift}}.
\]

## 8. Pseudospectra remain a separate diagnostic family

Under the inherited 2-norm convention,

\[
\Lambda_\varepsilon(A)
=\{z:\sigma_{\min}(zI-A)\le\varepsilon\}.
\]

This captures resolvent growth and spectral sensitivity that the bare eigenvalue set may miss.

But a pseudospectrum is still descriptive evidence about a declared operator.

It does not by itself identify which component of a learned system is functionally necessary.

## 9. Jacobian spectra are local

For nonlinear map

\[
z^+=\Phi(z),
\]

a Jacobian diagnostic at z0 is based on

\[
J_\Phi(z_0).
\]

The reference state is part of the object.

Removing z0 from the report removes part of the diagnostic definition.

## 10. Same local Jacobian, different nonlinear maps

Let

\[
F(x)=x/2,
\]

and

\[
G(x)=x/2+x^2.
\]

At zero,

\[
F'(0)=G'(0)=1/2.
\]

But

\[
F(1/2)=1/4,
\]

while

\[
G(1/2)=1/2.
\]

Therefore a local Jacobian spectrum cannot be promoted into a global nonlinear theorem.

## 11. Transition-local signatures

If a system moves through states

\[
z_0,z_1,z_2,\ldots,
\]

then one may study

\[
J_t=D\Phi(z_t).
\]

A spectral sequence

\[
\sigma(J_t)
\]

is a transition-local diagnostic.

Its interpretation requires the state/time index, estimation window, and operator-estimation method.

## 12. Hessian spectra are also local and incomplete

For objective L(theta), the Hessian

\[
H_L(\theta_0)
\]

captures second-order curvature at a declared parameter point.

It does not by itself determine the gradient.

## 13. Exact Hessian control

Let

\[
f(x,y)=x^2+y^2,
\]

\[
g(x,y)=x^2+y^2+x.
\]

Both have Hessian

\[
2I
\]

and therefore the same Hessian spectrum

\[
\{2,2\}.
\]

But at the origin

\[
\nabla f=(0,0),
\]

while

\[
\nabla g=(1,0).
\]

The same Hessian spectrum can occur at a stationary point and a non-stationary point.

## 14. Koopman changes the object being diagonalized

For nonlinear state map T and observable h, the Koopman operator acts as

\[
(Uh)(x)=h(T(x)).
\]

It is linear as an operator on observables even when T is nonlinear.

Mezić develops this spectral viewpoint for dynamical systems and model reduction [@Mezic2005Spectral].

The important semantic point is:

\[
\boxed{\text{Koopman spectrum is an observable-operator spectrum.}}
\]

It is not the Jacobian spectrum of T by definition.

## 15. Exact two-state Koopman witness

Let

\[
T(0)=1,
\qquad
T(1)=0.
\]

On indicator observables delta0 and delta1,

\[
U\delta_0=\delta_1,
\qquad
U\delta_1=\delta_0.
\]

So

\[
U=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

Hence

\[
U^2=I,
\]

with trace zero and determinant -1, giving eigenvalues

\[
\boxed{\{1,-1\}}.
\]

## 16. Finite Koopman approximations need their own error language

In practice one may estimate a finite matrix from data and call it a Koopman approximation.

That introduces choices:

- observable dictionary;
- sampling distribution;
- time window;
- truncation/rank;
- regression method;
- regularization;
- finite precision.

The spectrum of that finite matrix is exactly the spectrum of the fitted matrix.

Its relation to an underlying infinite-dimensional Koopman operator requires additional approximation theory.

## 17. Spectral drift is definition-relative

A drift diagnostic can compare

- eigenvalue sets;
- singular-value lists;
- pseudospectral contours;
- resolvent norms;
- subspace angles;
- projected gains;
- local Jacobian spectra;
- Koopman estimates.

These are different drift objects.

A single scalar named “spectral drift” is incomplete unless the underlying object and discrepancy are declared.

## 18. Descriptive quality is not functional necessity

The audited MECHDIAG packet supplies a second firewall.

A probe or diagnostic can track a property without showing that the measured feature is necessary for the system’s output.

The same applies to spectral signatures.

A signature can correlate strongly with performance and still be epiphenomenal.

## 19. Predictive utility is not mechanism

Suppose a spectral statistic predicts failure one step before failure occurs.

That is useful predictive evidence.

It does not yet show that manipulating the associated eigenspace, singular direction, or pseudospectral region will change the failure.

Prediction and mechanism are different claims.

## 20. Mechanistic significance requires intervention

To promote a spectral signature toward mechanism, pair it with a functional test such as:

- ablation of the implicated subspace;
- controlled perturbation of the operator block;
- substitution of a matched spectral control;
- recovery/rescue after restoring the implicated component;
- another explicitly justified intervention.

The intervention must target the object that the spectral interpretation claims matters.

## 21. A matched-spectrum control is especially valuable

The A/B control above has the same eigenvalue and singular-value multisets but different fixed-interface response.

This is useful because it holds the global spectral summaries fixed while changing a functional interface relation.

Matched controls can therefore falsify over-strong spectral explanations.

## 22. Finite precision and conditioning

Empirical spectra can be sensitive to:

- roundoff;
- non-normality;
- ill-conditioning;
- nearly repeated eigenvalues;
- low-rank truncation;
- finite-sample noise.

A plotted spectrum should therefore carry enough numerical context to distinguish exact structure from estimated structure.

## 23. No universal scalar diagnostic

Different systems can fail for different reasons.

A scalar that is useful for one operator family can become blind under another family or another interface.

The exact controls already show this for eigenvalue and singular-value summaries.

Thus the chapter rejects:

\[
\text{one spectral scalar}\equiv\text{universal health metric}.
\]

## 24. Reporting protocol

For every spectral/operator diagnostic report:

1. operator/object identity;
2. reference state, parameter point, or time window;
3. spectrum/diagnostic type;
4. norm and numerical convention;
5. estimation/truncation method;
6. uncertainty/tolerance;
7. interface or relative-position object, if used;
8. descriptive versus predictive versus functional claim class;
9. intervention evidence, if mechanistic significance is claimed;
10. known non-implications.

## 25. Durable non-implications

\[
\text{same eigenvalues}\not\Rightarrow\text{same transient behavior},
\]

\[
\text{same singular values}\not\Rightarrow\text{same interface behavior},
\]

\[
\text{same local Jacobian spectrum}\not\Rightarrow\text{same nonlinear map},
\]

\[
\text{same Hessian spectrum}\not\Rightarrow\text{same stationarity status},
\]

\[
\text{spectral correlation}\not\Rightarrow\text{functional necessity},
\]

and

\[
\text{functional association}\not\Rightarrow\text{causal mechanism without a suitable intervention}.
\]

## 26. Closing view

Spectral diagnostics are powerful precisely because they expose structure that scalar performance metrics can miss.

They become misleading when their object is unnamed or their epistemic role is inflated.

The durable rule is:

\[
\boxed{\text{a spectral signature is evidence about a declared operator; mechanistic meaning requires a separate functional bridge.}}
\]

## References used in this chapter

- [@HornJohnson2012]
- [@TrefethenEmbree2005]
- [@Mezic2005Spectral]

Mechanistic-diagnostics sources and exact prerequisite identities are recorded in sources/source-locks/ATLAS-CH-SPECTRALDIAG-001.yaml.
