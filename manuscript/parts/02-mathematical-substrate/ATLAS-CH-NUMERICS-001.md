# Discretization, Stability, and Splitting
<!-- ATLAS-CH-NUMERICS-001 -->

**Epistemic status:** Established Theory + Atlas Synthesis + Exact Computational Witness  
**Specification:** manuscript/specifications/ATLAS-CH-NUMERICS-001.md  
**Derivation packet:** mathematics/derivations/ATLAS-CH-NUMERICS-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-NUMERICS-001.md  
**Source lock:** sources/source-locks/ATLAS-CH-NUMERICS-001.yaml

## 1. The continuous system is not the algorithm

The previous chapter separated the exact flow

\[
\Phi_h
\]

from a numerical update

\[
\Psi_h.
\]

That distinction is the starting point of numerical analysis.

A differential equation can be perfectly stable while a poor discretization explodes.

A numerical method can be stable while remaining inaccurate.

A high-order method can fail if used outside the regime for which its assumptions hold.

The numerical question is therefore not:

> Does this update look like the differential equation?

It is:

> In what precise sense does the discrete map approximate the exact flow, and what happens to errors as steps accumulate?

## 2. Map versus terrain

A useful allegory is navigation.

The exact flow is the true route through terrain.

A numerical method is a stepping rule based on a map.

**Consistency** says one small step points approximately where the true route points.

**Stability** says small errors in the stepping process are not catastrophically amplified.

**Convergence** says the full discrete route approaches the true route as step size shrinks.

The analogy has a limit.

Numerical error is not geographic error.

The actual theory requires norms, regularity assumptions, and method-specific bounds.

## 3. One-step methods

Consider

\[
\dot x
=
f(t,x).
\]

A one-step method has the form

\[
\boxed{
x_{n+1}
=
\Psi_h(t_n,x_n).
}
\]

The step size is

\[
h=t_{n+1}-t_n.
\]

The exact flow over one step is

\[
\Phi_h(t_n,x).
\]

The method is an approximation to this exact transport.

## 4. Local defect

Start one numerical step from the exact state.

Define

\[
\delta_{n+1}
=
\Phi_h(t_n,x(t_n))
-
\Psi_h(t_n,x(t_n)).
\]

This is the **local defect**.

It asks:

> If previous error were magically removed, how wrong would this one step be?

For an order-\(p\) method,

\[
\delta_{n+1}
=
O(h^{p+1})
\]

under the required smoothness assumptions.

## 5. Global error

The actual numerical state is not restarted from truth.

It starts from the previous approximation.

Define

\[
e_n
=
x(t_n)-x_n.
\]

This is the **global error**.

Global error combines:

- new local defect;
- propagation of old error.

That second term is where stability enters.

## 6. Consistency is not enough

A method can have a small one-step defect and still behave badly when errors are repeatedly amplified.

So:

\[
\boxed{
\text{consistency}
\not\Rightarrow
\text{convergence}
}
\]

without the relevant stability and regularity assumptions.

For a well-behaved one-step method over a finite time interval, a local defect

\[
O(h^{p+1})
\]

combined with suitable Lipschitz error propagation yields global error

\[
O(h^p).
\]

Iserles develops this numerical ODE viewpoint systematically [@Iserles2008].

## 7. Explicit Euler

Taylor-expand the exact solution:

\[
x(t_n+h)
=
x(t_n)
+
h x'(t_n)
+
\frac{h^2}{2}x''(t_n)
+
O(h^3).
\]

Using

\[
x'(t_n)=f(t_n,x(t_n)),
\]

drop the higher-order terms:

\[
\boxed{
x_{n+1}
=
x_n
+
h f(t_n,x_n).
}
\]

This is explicit Euler.

## 8. Explicit Euler local defect

If the step begins from the exact state, then

\[
\delta_{n+1}^{\rm EE}
=
\frac{h^2}{2}x''(t_n)
+
O(h^3).
\]

So the local defect is second order.

The accumulated global error is first order:

\[
e_n
=
O(h)
\]

under standard finite-time regularity and stability conditions.

The distinction between local \(h^2\) and global \(h\) is fundamental.

## 9. Implicit Euler

Implicit Euler evaluates the vector field at the future state:

\[
\boxed{
x_{n+1}
=
x_n
+
h f(t_{n+1},x_{n+1}).
}
\]

The future state appears on both sides.

So a step generally requires solving an equation.

That extra computational cost buys a different stability geometry.

## 10. Explicit versus implicit is not fast versus slow

“Explicit” means the new state can be computed directly from known quantities.

“Implicit” means the new state is defined by an equation that must be solved.

The distinction is algebraic.

It does not automatically determine:

- wall-clock cost;
- accuracy;
- parallelism;
- implementation quality.

A cheap implicit solve can outperform a tiny explicit step.

A difficult nonlinear implicit solve can dominate the computation.

## 11. The scalar test equation

To study numerical stability, use

\[
y'
=
\lambda y.
\]

Its exact one-step factor is

\[
e^{h\lambda}.
\]

Define

\[
z=h\lambda.
\]

A one-step numerical method gives

\[
y_{n+1}
=
R(z)y_n,
\]

where \(R\) is the **stability function**.

The method's behavior on this scalar problem reveals important properties of its discrete dynamics.

## 12. Explicit Euler stability function

Explicit Euler gives

\[
y_{n+1}
=
y_n+h\lambda y_n.
\]

Therefore

\[
\boxed{
R_{\rm EE}(z)=1+z.
}
\]

Use the standard non-growth absolute-stability set

\[
\mathcal S
=
\{z:|R(z)|\le1\}.
\]

For explicit Euler,

\[
|1+z|\le1
\]

is the absolute-stability disk.

For a decaying exact mode with

\[
\operatorname{Re}(\lambda)<0,
\]

strict asymptotic decay of the discrete mode requires the interior condition

\[
|1+z|<1.
\]

## 13. The explicit stability disk

The non-growth condition

\[
|1+z|\le1
\]

defines the closed disk of radius \(1\) centered at

\[
-1
\]

in the complex plane.

Its open interior

\[
|1+z|<1
\]

gives strict asymptotic decay.

A stable continuous eigenmode can therefore become unstable numerically if

\[
h\lambda
\]

falls outside this disk.

The differential equation did not become unstable.

The discretization did.

![Explicit and implicit Euler absolute-stability regions beside log-log Lie-Trotter and Strang local-defect scaling for the exact split witness.](../../figures/masters/ATLAS-FIG-NUMERICS-001.png)

## 14. Implicit Euler stability function

Implicit Euler gives

\[
y_{n+1}
=
y_n+h\lambda y_{n+1}.
\]

Rearrange:

\[
(1-z)y_{n+1}
=
y_n.
\]

Thus

\[
\boxed{
R_{\rm IE}(z)
=
\frac{1}{1-z}.
}
\]

The standard non-growth absolute-stability condition is

\[
\left|
\frac{1}{1-z}
\right|
\le1.
\]

Equivalently,

\[
|1-z|\ge1.
\]

Strict decay uses the corresponding strict inequalities.

## 15. A-stability

Every point in the closed left half-plane satisfies

\[
|1-z|\ge1.
\]

Therefore implicit Euler is A-stable in the standard non-growth sense.

For every point in the open left half-plane,

\[
|1-z|>1,
\]

so an exponentially decaying scalar mode remains strictly decaying for any positive step size.

That is a strong stability property.

It is not a claim of arbitrary accuracy.

## 16. L-stability

For implicit Euler,

\[
R_{\rm IE}(z)
=
\frac{1}{1-z}.
\]

As

\[
|z|\to\infty
\]

within the left half-plane,

\[
R_{\rm IE}(z)\to0.
\]

Thus strongly damped continuous modes are also strongly damped numerically.

Implicit Euler is L-stable.

This matters in stiff problems, where very fast decaying modes can otherwise pollute a computation.

## 17. Stability is not accuracy

Take

\[
y'=-100y.
\]

Use

\[
h=0.05.
\]

Then

\[
z=-5.
\]

The exact one-step factor is

\[
e^{-5}
\approx
0.00673795.
\]

Explicit Euler gives

\[
R_{\rm EE}(-5)
=
-4.
\]

The numerical mode grows in magnitude.

Implicit Euler gives

\[
R_{\rm IE}(-5)
=
\frac16
\approx
0.1667.
\]

It decays.

But it is not close to the exact factor.

So:

\[
\boxed{
\text{stable}
\neq
\text{accurate}.
}
\]

## 18. The stiff scalar witness

The same continuous mode can therefore produce three qualitatively different one-step behaviors:

\[
\text{exact: }
0.0067,
\]

\[
\text{explicit Euler: }
-4,
\]

\[
\text{implicit Euler: }
0.1667.
\]

Explicit Euler is unstable.

Implicit Euler is stable.

Neither numerical factor equals the exact one.

This is why numerical analysis needs both stability and error analysis.

## 19. What stiffness means

Stiffness is not simply “large derivative.”

A useful operational picture is:

> the system contains rapidly decaying modes that force a chosen numerical method to use a much smaller stable step than the slower behavior of interest would otherwise require.

The word is therefore partly problem-relative and partly method-relative.

Hairer and Wanner develop the stiff ODE framework in detail [@HairerWanner1996].

## 20. Multiple timescales

Suppose

\[
\dot x
=
\begin{pmatrix}
-1&0\\
0&-1000
\end{pmatrix}
x.
\]

The first mode evolves on timescale roughly \(1\).

The second decays on timescale roughly \(10^{-3}\).

After the fast mode has essentially vanished, an explicit method may still be forced to use tiny steps because of its stability restriction.

The numerical method is spending effort respecting a mode that no longer matters much to the observable slow trajectory.

This is the classic stiffness tension.

## 21. Implicit methods move the stability boundary

An implicit method can tolerate much larger stable steps for decaying modes.

But the price can include:

- linear solves;
- nonlinear solves;
- Jacobians;
- preconditioning;
- memory;
- implementation complexity.

Numerical method choice is therefore a systems tradeoff.

This becomes relevant when neural architectures contain implicit or equilibrium-style blocks.

## 22. Absolute stability is not nonlinear stability

The region

\[
|R(z)|<1
\]

is defined for the scalar linear test equation.

It provides powerful local/mode-level information.

It is not a universal theorem about a nonlinear problem.

A nonlinear method can leave the test region satisfied while encountering:

- changing Jacobians;
- constraints;
- bifurcations;
- non-normal amplification;
- state-dependent stiffness.

The stability region is a diagnostic object, not a complete nonlinear certificate.

## 23. From one vector field to two

Suppose the dynamics decompose:

\[
\dot x
=
(A+B)x.
\]

Perhaps:

- \(A\) is easy to integrate;
- \(B\) is easy to integrate;
- \(A+B\) is expensive;
- each subflow preserves a useful structure.

This motivates splitting.

Instead of approximating the full vector field in one step, we compose simpler exact or approximate subflows.

## 24. Lie–Trotter splitting

For constant matrices, define

\[
\boxed{
S_{\rm LT}(h)
=
e^{hA}e^{hB}.
}
\]

This means the \(B\) subflow acts first on a state vector, followed by the \(A\) subflow, under the usual right-to-left composition convention.

The result approximates

\[
e^{h(A+B)}.
\]

How accurate is it?

The answer depends on commutation.

## 25. Noncommutativity is the obstruction

Expand both subflows:

\[
e^{hA}
=
I+hA+\frac{h^2}{2}A^2+O(h^3),
\]

\[
e^{hB}
=
I+hB+\frac{h^2}{2}B^2+O(h^3).
\]

Their product has second-order term

\[
\frac12A^2+AB+\frac12B^2.
\]

The exact flow has second-order term

\[
\frac12
(A^2+AB+BA+B^2).
\]

Subtracting gives

\[
\boxed{
S_{\rm LT}(h)
-
e^{h(A+B)}
=
\frac{h^2}{2}[A,B]
+
O(h^3),
}
\]

where

\[
[A,B]
=
AB-BA.
\]

## 26. Commuting subflows

If

\[
[A,B]=0,
\]

then for constant matrices

\[
e^{hA}e^{hB}
=
e^{h(A+B)}
\]

exactly.

The split introduces no error.

This is an important lesson for architecture.

Splitting quality is not determined only by the size of the components.

It depends on their algebraic interaction.

## 27. Exact noncommuting witness

Choose

\[
A=
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix},
\]

and

\[
B=
\begin{pmatrix}
0&0\\
1&0
\end{pmatrix}.
\]

Then

\[
[A,B]
=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}.
\]

The operators do not commute.

The exact symbolic series therefore exposes a nonzero second-order Lie defect.

## 28. Lie local defect

For the declared witness,

\[
S_{\rm LT}(h)
-
e^{h(A+B)}
\]

has leading term

\[
\frac{h^2}{2}
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}.
\]

The off-diagonal terms begin at order

\[
h^3.
\]

The local defect is therefore

\[
O(h^2).
\]

Under the usual finite-time stability assumptions, Lie–Trotter is globally first order.

## 29. Strang splitting

A symmetric composition is

\[
\boxed{
S_{\rm S}(h)
=
e^{hA/2}
e^{hB}
e^{hA/2}.
}
\]

The half-step symmetry cancels the second-order local defect.

For sufficiently regular bounded operators,

\[
S_{\rm S}(h)
-
e^{h(A+B)}
=
O(h^3).
\]

This yields second-order global accuracy under the usual stability assumptions.

## 30. Exact Strang witness

For the same \(A,B\), the symbolic defect begins as

\[
\begin{pmatrix}
O(h^4)&h^3/12\\
-h^3/6&O(h^4)
\end{pmatrix}.
\]

The first nonzero terms are cubic.

The figure's log–log plot evaluates exact matrix exponentials across a declared \(h\)-grid.

The asymptotic slopes reveal the expected local orders:

- Lie–Trotter:
  \(2\);
- Strang:
  \(3\).

## 31. Symmetry is doing mathematical work

The advantage of Strang is not merely that it performs more substeps.

The composition is time-symmetric in its outer \(A\) factors.

That symmetry removes an entire order of local defect.

Architectural ordering can therefore change approximation order even when the same primitive operations are used.

This is the core mathematical motivation for later split-operator neural architectures.

## 32. Splitting is not arbitrary modularity

Suppose a model has two modules.

Calling their composition a “split method” does not make numerical splitting theory applicable.

A genuine splitting interpretation requires a declared underlying evolution such as

\[
\dot x=(A+B)x
\]

or its nonlinear/operator analogue.

The substeps should correspond to meaningful component flows or approximations.

Otherwise “splitting” is metaphor, not derivation.

## 33. Splitting can preserve structure

Suppose each subflow is symplectic.

The composition of symplectic maps is symplectic.

Thus a split integrator can preserve the symplectic form exactly even when it only approximates the full exact flow.

This is one way discrete algorithms can preserve qualitative geometry.

McLachlan and Quispel survey this splitting viewpoint [@McLachlanQuispel2002].

## 34. Structure-preserving means name the structure

A method may preserve:

- symplectic form;
- norm;
- positivity;
- mass;
- reversibility;
- constraint manifold;
- volume.

These are different promises.

A method can preserve one while violating another.

So the phrase

> structure-preserving

is incomplete unless the structure is named.

Hairer, Lubich, and Wanner develop this geometric integration perspective [@HairerLubichWanner2006].

## 35. Backward error viewpoint

A powerful later idea is to ask whether a discrete method exactly follows a nearby modified differential equation.

This is backward error analysis.

Instead of saying

> the numerical path is slightly wrong,

we ask

> for which nearby dynamics is this path more nearly exact?

This can explain excellent long-time behavior of geometric methods.

The present chapter only introduces the viewpoint.

A later Numerical Intelligence chapter can develop it more deeply.

## 36. Step size is a modeling parameter

The step size

\[
h
\]

controls more than numerical precision.

It can alter:

- stability;
- damping;
- phase error;
- effective depth;
- computational cost.

In learned systems, scale parameters that resemble step sizes can therefore influence qualitative computation.

But an analogy becomes useful only when the update admits a coherent numerical interpretation.

## 37. Depth as number of steps

If a residual block approximates

\[
x_{n+1}
=
x_n
+
h f(x_n),
\]

then increasing depth while reducing \(h\) can resemble time refinement.

The natural questions become:

- Does the output converge as depth is refined?
- Is the method stable?
- Which invariant changes with depth?
- Is the architecture approximating one flow or changing the vector field itself?

The later Adaptive Depth chapter will inherit this language.

## 38. Adaptive depth as error control

Classical adaptive integration allocates more steps where error estimates demand them.

A learned analogue might use:

- residual magnitude;
- local defect proxy;
- uncertainty;
- contract violation;
- commutator magnitude.

to decide whether more computation is needed.

That is an architectural research programme.

This chapter supplies the numerical grammar.

It does not validate a specific controller.

## 39. Commutator as split diagnostic

For Lie–Trotter,

\[
[A,B]
\]

appears directly in the leading local defect.

This suggests a diagnostic principle:

> if two learned operators are intended to be split, measure how strongly their order matters.

In nonlinear systems, Lie brackets or lifted commutators can play analogous roles.

This is one bridge to SPLICE-style diagnostics.

Again, the exact numerical theorem applies only after the operator model has been declared.

## 40. Stiff learned dynamics

A learned update can exhibit widely separated effective timescales.

Examples might include:

- fast normalization variables;
- slow feature evolution;
- rapidly decaying auxiliary states;
- momentum transients.

Calling such a system “stiff” requires an actual dynamical and numerical analysis.

The useful test is whether stability forces a step/depth scale much smaller than the behavior of interest requires.

## 41. Implicit computation

Implicit Euler solves for a future state satisfying an equation.

This creates a conceptual link to:

- equilibrium networks;
- implicit layers;
- fixed-point solvers;
- proximal updates.

But the relationship is not identity.

An implicit neural block can solve a different equation with different stability and convergence properties.

Numerical language should clarify the contract, not erase differences.

## 42. Four numerical failure modes

### Small local defect, unstable propagation

Consistency without stability.

### Stable but inaccurate coarse steps

The stiff implicit-Euler witness.

### High-order formula outside assumptions

Formal order does not protect against nonsmoothness, singularity, or unbounded-operator domain failures.

### Structure-preserving label without structure

A claim is meaningless until the preserved invariant or geometry is stated.

These are distinct failures.

## 43. What would falsify a numerical interpretation?

Suppose a neural architecture is claimed to approximate a particular flow.

Useful falsification tests include:

- depth refinement fails to converge;
- halving the apparent step size does not reduce error at the predicted order;
- stability boundaries disagree with the proposed test equation or Jacobian model;
- split ordering has no relation to predicted commutator effects;
- claimed invariants drift despite a supposed structure-preserving construction.

A numerical interpretation should generate quantitative predictions.

## 44. Atlas connections

**Dynamics.**  
The exact flow is the object being approximated.

**Adaptive Depth.**  
Depth can become an error-controlled step budget when the numerical model is justified.

**Split-operator architectures.**  
Commutators and composition order become design variables.

**Variational optimization.**  
Discrete updates can be derived from geometric or variational principles.

**Numerical Intelligence.**  
Solvers, residuals, error estimates, and backward error become computational mechanisms rather than background implementation details.

**SPINDLE.**  
The controlled-operator-splitting programme sits directly on the distinctions developed here.

## 45. Closing view

Numerical analysis asks a disciplined question:

> What discrete computation faithfully represents the behavior we intend?

The answer is not contained in one error order.

A method must negotiate:

- local approximation;
- error propagation;
- stability;
- stiffness;
- computational cost;
- algebraic interaction;
- geometric structure.

The scalar test equation showed why a stable continuous system can become numerically unstable.

The stiff witness showed why stable does not mean accurate.

The split witness showed why operator order matters.

And Strang splitting showed that composition symmetry can improve accuracy without changing the primitive operators.

These are not implementation details.

They are mathematical properties of computation.

The next Atlas chapters can now ask a sharper architectural question:

> If depth, modules, and residual updates are treated as numerical machinery, which integration contract are they actually satisfying?

## References used in this chapter

- [@Iserles2008]
- [@HairerWanner1996]
- [@McLachlanQuispel2002]
- [@HairerLubichWanner2006]

See \`sources/source-locks/ATLAS-CH-NUMERICS-001.yaml\` for exact source roles and claim boundaries.
