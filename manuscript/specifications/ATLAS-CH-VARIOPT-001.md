# Chapter Specification — ATLAS-CH-VARIOPT-001

## Identity

**Title:** Variational and Divergence-Derived Optimization  
**Part:** Optimization  
**Status:** specification-ready.  
**Epistemic class:** audited Numerics and Manifold Optimization prerequisites + primary Bregman/variational sources + exact GCL MODULUS programme evidence + Atlas finite derivations.

## Contract

Develop a disciplined bridge among:

- convex divergences and local geometry;
- divergence-derived first-order updates;
- continuous-time variational optimization;
- discrete action principles;
- symplectic update structure;
- explicit geometry-to-update construction in the GCL MODULUS programme.

The chapter must distinguish derivation mechanism from performance guarantee.

## Hard prerequisites

- ATLAS-CH-NUMERICS-001.
- ATLAS-CH-MANOPT-001.

Exact prerequisite identities, external sources, and GCL programme evidence are locked in:

sources/source-locks/ATLAS-CH-VARIOPT-001.yaml

## Required distinctions

1. divergence versus metric;
2. global divergence versus local Hessian quadratic form;
3. objective versus geometry generator;
4. mirror/Bregman step versus Euclidean gradient step;
5. action/Lagrangian versus objective function;
6. continuous Euler-Lagrange flow versus a discrete update;
7. discrete stationarity versus optimization stationarity;
8. variational derivation versus numerical accuracy;
9. symplecticity versus exact energy conservation;
10. structure preservation versus objective descent;
11. constraint preservation versus optimizer quality;
12. GCL programme mechanism versus established mathematical authority.

## Bregman divergence

Let \(\phi:\Omega\to\mathbb R\) be differentiable and strictly convex on a convex domain.

Define:

\[
D_\phi(y,x)
=
\phi(y)-\phi(x)-\langle\nabla\phi(x),y-x\rangle.
\]

The arguments are ordered.

In general:

\[
D_\phi(y,x)\ne D_\phi(x,y).
\]

Therefore Bregman divergence is not generally a metric.

## Local geometry

If \(\phi\) is \(C^2\), then for small displacement \(\delta\):

\[
D_\phi(x+\delta,x)
=
\frac12\delta^\top\nabla^2\phi(x)\delta
+
O(\|\delta\|^3).
\]

When the Hessian is positive definite, it supplies a local quadratic form.

The chapter must not promote this local statement into global metric symmetry or triangle inequality.

## Exact asymmetry witness

Take:

\[
\phi(x)=e^x.
\]

Then:

\[
D_\phi(1,0)=e-2,
\]

while:

\[
D_\phi(0,1)=1.
\]

They are unequal.

At \(x=0\):

\[
D_\phi(\delta,0)
=
e^\delta-1-\delta
=
\frac{\delta^2}{2}
+
O(\delta^3).
\]

Thus the local Hessian is \(1\) while the global divergence remains asymmetric.

## Bregman proximal / mirror-style step

Given current point \(x_k\), gradient-like covector \(g_k\), step \(\eta>0\), and generator \(\phi\), define:

\[
x_{k+1}
=
\arg\min_{x\in\Omega}
\left[
\eta\langle g_k,x\rangle
+
D_\phi(x,x_k)
\right].
\]

Under differentiability and interior stationarity:

\[
\nabla\phi(x_{k+1})
=
\nabla\phi(x_k)-\eta g_k.
\]

This is a dual-coordinate update.

The map depends on \(\phi\), \(\Omega\), \(g_k\), and \(\eta\).

## Euclidean special case

For:

\[
\phi(x)=\frac12\|x\|^2,
\]

the Bregman divergence is:

\[
D_\phi(y,x)=\frac12\|y-x\|^2.
\]

The stationarity relation reduces to:

\[
x_{k+1}=x_k-\eta g_k.
\]

Thus Euclidean gradient descent is one special divergence-derived update, not the definition of the whole class.

## Entropic one-dimensional example

For \(x>0\), let:

\[
\phi(x)=x\log x-x.
\]

Then:

\[
\nabla\phi(x)=\log x.
\]

The mirror step satisfies:

\[
\log x_{k+1}
=
\log x_k-\eta g_k,
\]

hence:

\[
x_{k+1}
=
x_k e^{-\eta g_k}.
\]

For:

\[
x_k=1,\qquad
\eta=1,\qquad
g_k=\log2,
\]

the exact update is:

\[
x_{k+1}=\frac12.
\]

## Non-descent control

A divergence-derived update need not decrease the objective without appropriate step assumptions.

Take:

\[
f(x)=\frac12(x-2)^2,
\qquad
x_0=0.
\]

Then:

\[
g_0=f'(0)=-2.
\]

Using the Euclidean Bregman step with \(\eta=3\):

\[
x_1
=
0-3(-2)
=
6.
\]

But:

\[
f(x_0)=2,
\qquad
f(x_1)=8.
\]

Therefore:

\[
\boxed{
\text{Bregman-derived first-order update}
\not\Rightarrow
\text{one-step descent}.
}
\]

## Continuous-time variational optimization

Wibisono, Wilson, and Jordan supply a source-scoped Bregman-Lagrangian perspective in which a Lagrangian built from a Bregman divergence and objective generates broad families of accelerated optimization flows.

The chapter may use that result to show that optimization dynamics can be organized variationally.

It must not infer that arbitrary discretizations inherit acceleration, stability, descent, or optimality.

## Action and Euler-Lagrange equation

For configuration \(q(t)\), Lagrangian \(L(q,\dot q,t)\), and action:

\[
\mathcal A[q]
=
\int_{t_0}^{t_1}
L(q,\dot q,t)\,dt,
\]

stationarity under suitable variations gives:

\[
\frac{d}{dt}
\frac{\partial L}{\partial\dot q}
-
\frac{\partial L}{\partial q}
=
0.
\]

This is stationarity of an action functional.

It is not objective-function stationarity.

## Discrete Lagrangian

Let:

\[
L_d(q_k,q_{k+1};h)
\]

approximate or otherwise represent one step of action.

The discrete action is:

\[
\mathcal A_d
=
\sum_k L_d(q_k,q_{k+1};h).
\]

Discrete stationarity gives the discrete Euler-Lagrange equation:

\[
D_2L_d(q_{k-1},q_k)
+
D_1L_d(q_k,q_{k+1})
=
0.
\]

Under the regularity assumptions of discrete variational mechanics, the induced phase-space map is symplectic.

## Exact harmonic-oscillator discrete Lagrangian

Take:

\[
L(q,\dot q)
=
\frac12\dot q^2-\frac12q^2.
\]

Use the left-endpoint discrete Lagrangian:

\[
L_d(q_k,q_{k+1};h)
=
\frac{(q_{k+1}-q_k)^2}{2h}
-
\frac{h}{2}q_k^2.
\]

The discrete Euler-Lagrange equation yields:

\[
q_{k+1}
=
(2-h^2)q_k-q_{k-1}.
\]

Define:

\[
p_k=\frac{q_k-q_{k-1}}{h}.
\]

Then:

\[
p_{k+1}=p_k-hq_k,
\]

\[
q_{k+1}=q_k+h p_{k+1}.
\]

This is the declared symplectic-Euler update.

## Symplectic matrix

For state:

\[
z_k=
\begin{pmatrix}
q_k\\
p_k
\end{pmatrix},
\]

the update is:

\[
z_{k+1}
=
M_h z_k,
\]

with:

\[
M_h
=
\begin{pmatrix}
1-h^2 & h\\
-h & 1
\end{pmatrix}.
\]

For:

\[
J=
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix},
\]

the exact identity is:

\[
M_h^\top J M_h=J.
\]

Thus the finite map is symplectic.

## Energy non-conservation control

The oscillator Hamiltonian is:

\[
H(q,p)=\frac12(q^2+p^2).
\]

Take:

\[
h=\frac12,
\qquad
(q_0,p_0)=(0,1).
\]

Then:

\[
p_1=1,
\qquad
q_1=\frac12.
\]

Hence:

\[
H_0=\frac12,
\qquad
H_1=\frac58.
\]

Therefore the exactly symplectic update does not conserve this Hamiltonian exactly.

## Objective non-descent control

Using:

\[
F(q)=\frac12q^2,
\]

the same step gives:

\[
F(q_0)=0,
\qquad
F(q_1)=\frac18.
\]

Thus:

\[
\boxed{
\text{symplectic update}
\not\Rightarrow
\text{objective descent}.
}
\]

## MODULUS programme bridge

At protected MODULUS commit:

7ca4ffcdace32d5ff79c27ad557bfb690fac0af3

Hyperball implements the following programme-specific pipeline for selected parameter groups:

1. a base Optax optimizer proposes update \(u\);
2. optionally remove the radial component relative to parameter \(w\);
3. optionally scale the tangent update to a declared norm or approximate angular-control target;
4. apply a sphere retraction or ball norm control.

This is an explicit geometry-to-update construction.

It is not claimed to arise from the Bregman Lagrangian or a discrete action.

## Exact MODULUS-style finite witness

Take:

\[
w=(1,0),
\qquad
u=(1,1).
\]

The tangent projection is:

\[
u_\perp
=
u-\frac{\langle u,w\rangle}{\|w\|^2}w
=
(0,1).
\]

For radius \(1\) and programme parameter \(\alpha=1\), the implementation's target-angle branch sets desired tangent norm:

\[
\alpha\|w\|=1.
\]

The tangent proposal remains:

\[
(0,1).
\]

Sphere retraction gives:

\[
w_+
=
\frac{(1,1)}{\sqrt2}.
\]

The exact post-retraction angle is:

\[
\theta
=
\arccos\frac1{\sqrt2}
=
\frac\pi4,
\]

not \(1\) radian.

More generally, for unit \(w\), unit tangent \(v\), and pre-retraction proposal \(w+\alpha v\):

\[
\theta=\arctan\alpha.
\]

Therefore the programme knob is a small-step angular proxy through tangent-norm control, not an exact geodesic-angle equation at finite \(\alpha\).

## Programme-authority boundary

The GCL repository profile classifies MODULUS as:

- optimization research provider;
- benchmark provider;
- implementation provider;

with no claim-promotion or certification authority.

VARIOPT must preserve that governance distinction.

## Reader spine

1. Why optimization can be derived from geometry or action.
2. Divergence is not distance.
3. Bregman local quadratic geometry.
4. Mirror/Bregman proximal updates.
5. Euclidean and entropic examples.
6. Non-descent counterexample.
7. Continuous-time variational optimization.
8. Action versus objective.
9. Discrete action and discrete stationarity.
10. Exact harmonic-oscillator derivation.
11. Symplectic Euler.
12. Symplecticity versus energy.
13. Symplecticity versus descent.
14. Manifold/retraction handoff.
15. MODULUS geometry-to-update pipeline.
16. Exact finite Hyperball control.
17. Programme evidence versus established theory.
18. Failure boundaries.

## Failure boundaries

- divergence != metric;
- Hessian local geometry != global distance;
- mirror step != universal descent;
- variational derivation != numerical accuracy;
- discrete stationarity != optimization stationarity;
- symplecticity != energy conservation;
- symplecticity != stability;
- symplecticity != objective descent;
- constraint preservation != convergence;
- retraction != exponential map;
- source-scoped Bregman-Lagrangian theory != arbitrary optimizer theorem;
- MODULUS mechanism != established universal theory;
- target-angle parameter != exact finite geodesic angle under the current retraction implementation.

## Sources

- L. M. Bregman (1967), DOI 10.1016/0041-5553(67)90040-7.
- J. E. Marsden and M. West (2001), DOI 10.1017/S096249290100006X.
- Andre Wibisono, Ashia C. Wilson, and Michael I. Jordan (2016), DOI 10.1073/pnas.1614734113.
- exact protected GCL MODULUS programme evidence recorded in the source lock.

Exact source identities and boundaries are recorded in:

sources/source-locks/ATLAS-CH-VARIOPT-001.yaml
