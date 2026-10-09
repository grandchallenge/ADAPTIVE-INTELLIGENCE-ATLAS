# Variational and Divergence-Derived Optimization
<!-- ATLAS-CH-VARIOPT-001 -->

**Epistemic status:** audited Numerics and Manifold Optimization prerequisites + primary Bregman/variational sources + exact GCL MODULUS programme evidence + Atlas finite derivations.  
**Specification:** manuscript/specifications/ATLAS-CH-VARIOPT-001.md  
**Derivation packet:** mathematics/derivations/ATLAS-CH-VARIOPT-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-VARIOPT-001.md  
**Source lock:** sources/source-locks/ATLAS-CH-VARIOPT-001.yaml

Optimization rules can be written down directly.

They can also be derived from a declared geometry, a divergence, an action, or a constraint.

Those derivations are valuable because they expose which structure the update is intended to respect.

But the derivation does not grant every desirable property at once.

The governing rule is:

\[
\boxed{
\text{derivation structure}
\neq
\text{performance guarantee}.
}
\]

This chapter develops that distinction through Bregman geometry, variational mechanics, symplectic updates, and an exact GCL MODULUS programme bridge.

## 1. Two inherited firewalls

NUMERICS-001 established that:

\[
\text{exact flow}
\neq
\text{numerical update},
\]

and that:

- stability is not accuracy;
- structure preservation is not exact energy conservation;
- order claims require assumptions;
- a computational analogy is not automatically a theorem.

MANOPT-001 established that:

- gradients depend on metric;
- tangent directions are local legal velocities;
- retractions return tangent data to the constraint set;
- retractions need not equal exponential maps;
- constraint preservation does not imply descent;
- stationarity does not imply global optimality.

VARIOPT inherits both.

## 2. Why divergences enter optimization

Euclidean distance is only one way to measure a local change.

A convex generator can define a directed discrepancy that adapts to the geometry of the domain.

Let:

\[
\phi:\Omega\to\mathbb R
\]

be differentiable and strictly convex.

The Bregman divergence is:

\[
D_\phi(y,x)
=
\phi(y)-\phi(x)-\langle\nabla\phi(x),y-x\rangle.
\]

Geometrically, it measures how far the graph of \(\phi\) at \(y\) sits above the tangent hyperplane to \(\phi\) at \(x\).

## 3. Divergence is not distance

The ordering matters.

Take:

\[
\phi(x)=e^x.
\]

Then:

\[
D_\phi(1,0)=e-2,
\]

but:

\[
D_\phi(0,1)=1.
\]

Thus:

\[
D_\phi(1,0)\ne D_\phi(0,1).
\]

A Bregman divergence is therefore not generally a metric.

That remains true even though it can generate useful local geometry.

## 4. Local geometry from a Hessian

Assume \(\phi\) has a locally Lipschitz Hessian near \(x\), for example bounded third derivatives. Then for a small displacement \(\delta\):

\[
D_\phi(x+\delta,x)
=
\frac12
\delta^\top\nabla^2\phi(x)\delta
+
O(\|\delta\|^3).
\]

The Hessian acts as a local quadratic form. Under merely continuous second differentiability, the same expansion holds with the weaker remainder \(o(\|\delta\|^2)\); the displayed cubic-order remainder requires the stated stronger regularity.

For:

\[
\phi(x)=e^x,
\]

at \(x=0\):

\[
D_\phi(\delta,0)
=
e^\delta-1-\delta
=
\frac12\delta^2
+
\frac16\delta^3
+\cdots.
\]

The local quadratic geometry can be symmetric even when the full divergence is not.

## 5. Geometry can define an update

Suppose the objective supplies a local covector \(g_k\).

Instead of taking a Euclidean step, choose the next state by minimizing:

\[
\eta\langle g_k,x\rangle
+
D_\phi(x,x_k).
\]

The first term asks for progress under the local linearized objective.

The second penalizes movement according to the chosen geometry.

At an interior optimum:

\[
\nabla\phi(x_{k+1})
=
\nabla\phi(x_k)-\eta g_k.
\]

The step is simple in the dual coordinate \(\nabla\phi\).

## 6. Euclidean descent is one special case

For:

\[
\phi(x)=\frac12\|x\|^2,
\]

we have:

\[
\nabla\phi(x)=x.
\]

So:

\[
x_{k+1}=x_k-\eta g_k.
\]

Ordinary gradient descent therefore sits inside the broader divergence-derived construction.

The broader construction should not be reduced back to Euclidean distance by terminology.

## 7. An entropic coordinate system

For positive scalar \(x\), choose:

\[
\phi(x)=x\log x-x.
\]

Then:

\[
\nabla\phi(x)=\log x.
\]

The update becomes:

\[
\log x_{k+1}
=
\log x_k-\eta g_k.
\]

Hence:

\[
x_{k+1}
=
x_k e^{-\eta g_k}.
\]

For:

\[
x_k=1,
\qquad
\eta=1,
\qquad
g_k=\log2,
\]

we obtain exactly:

\[
x_{k+1}=\frac12.
\]

A change that is additive in dual coordinates becomes multiplicative in primal coordinates.

## 8. Divergence-derived does not mean descending

Consider:

\[
f(x)=\frac12(x-2)^2.
\]

At \(x_0=0\):

\[
g_0=-2.
\]

With the Euclidean Bregman generator and step size:

\[
\eta=3,
\]

the update is:

\[
x_1=6.
\]

Yet:

\[
f(x_0)=2,
\qquad
f(x_1)=8.
\]

The objective increased.

Thus:

\[
\boxed{
\text{derived from a convex divergence}
\not\Rightarrow
\text{automatic descent}.
}
\]

Step-size, smoothness, convexity, and algorithm-specific conditions still matter.

## 9. From geometry to dynamics

A first-order update uses a local objective model plus a movement penalty.

A variational formulation can instead define a whole trajectory through an action.

For path \(q(t)\):

\[
\mathcal A[q]
=
\int L(q,\dot q,t)\,dt.
\]

Stationarity gives the Euler-Lagrange equation:

\[
\frac{d}{dt}
\frac{\partial L}{\partial\dot q}
-
\frac{\partial L}{\partial q}
=
0.
\]

The object being made stationary is the action.

It need not be the optimization objective itself.

## 10. Bregman Lagrangian

Wibisono, Wilson, and Jordan introduced a Bregman Lagrangian:

\[
\mathcal L(X,V,t)
=
e^{\alpha_t+\gamma_t}
\left[
D_h(X+e^{-\alpha_t}V,X)
-
e^{\beta_t}f(X)
\right].
\]

Under their declared ideal-scaling conditions and regularity assumptions, its Euler-Lagrange dynamics organize broad families of accelerated continuous-time optimization flows.

This is a powerful bridge:

\[
\text{divergence geometry}
+
\text{variational dynamics}
\to
\text{optimization flow}.
\]

But the source does not license every possible discretization of that flow.

## 11. Continuous flow still is not the algorithm

The audited Numerics boundary remains active.

Even when a continuous optimization flow has a proved rate:

\[
\text{continuous theorem}
\not\Rightarrow
\text{arbitrary discrete theorem}.
\]

A discrete method must be analyzed as its own map.

That map can have different:

- stability;
- error;
- invariants;
- energy behavior;
- descent behavior.

## 12. Discrete action

Variational mechanics offers a different route.

Instead of discretizing the differential equation directly, discretize the action.

Let:

\[
L_d(q_k,q_{k+1};h)
\]

represent one discrete action contribution.

Then:

\[
\mathcal A_d
=
\sum_k
L_d(q_k,q_{k+1};h).
\]

Stationarity with respect to an interior point \(q_k\) gives:

\[
D_2L_d(q_{k-1},q_k)
+
D_1L_d(q_k,q_{k+1})
=
0.
\]

This is the discrete Euler-Lagrange equation.

## 13. Why derive the discrete rule this way?

A discrete variational principle can preserve geometric structure inherited from the action formulation.

Marsden and West develop this framework systematically and show how regular discrete variational mechanics generates symplectic schemes.

The important word is **structure**.

The theorem is not:

> variational integrator = exact trajectory.

Nor is it:

> symplectic integrator = monotonically improving objective.

## 14. Exact oscillator construction

Take the harmonic-oscillator Lagrangian:

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
\frac h2q_k^2.
\]

This is now a finite algebraic object.

## 15. Discrete Euler-Lagrange equation

The two derivatives are:

\[
D_2L_d(q_{k-1},q_k)
=
\frac{q_k-q_{k-1}}h,
\]

and:

\[
D_1L_d(q_k,q_{k+1})
=
-\frac{q_{k+1}-q_k}h
-hq_k.
\]

Set their sum to zero:

\[
\frac{q_k-q_{k-1}}h
-
\frac{q_{k+1}-q_k}h
-hq_k
=
0.
\]

Rearrange:

\[
q_{k+1}
=
(2-h^2)q_k-q_{k-1}.
\]

The update has been derived from a discrete stationarity condition rather than guessed from the ODE.

## 16. Momentum lift

Define:

\[
p_k=
\frac{q_k-q_{k-1}}h.
\]

Then the recurrence becomes:

\[
p_{k+1}=p_k-hq_k,
\]

followed by:

\[
q_{k+1}=q_k+h p_{k+1}.
\]

This is one ordering of symplectic Euler.

## 17. Exact map

Write:

\[
z_k=
\begin{pmatrix}
q_k\\
p_k
\end{pmatrix}.
\]

Then:

\[
z_{k+1}=M_hz_k,
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

Its determinant is exactly:

\[
1.
\]

More strongly:

\[
M_h^\top J M_h=J
\]

for the canonical symplectic matrix:

\[
J=
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix}.
\]

## 18. Symplectic is a precise property

Symplecticity means the map preserves the canonical symplectic form.

It is not a synonym for:

- stable;
- accurate;
- energy conserving;
- reversible;
- objective descending;
- globally optimal.

These properties require their own evidence.

## 19. Exact energy counterexample

Use:

\[
h=\frac12,
\qquad
(q_0,p_0)=(0,1).
\]

The update gives:

\[
p_1=1,
\]

\[
q_1=\frac12.
\]

For:

\[
H(q,p)=\frac12(q^2+p^2),
\]

the initial energy is:

\[
H_0=\frac12.
\]

After one exactly symplectic step:

\[
H_1=\frac58.
\]

So energy increased by:

\[
\frac18.
\]

The symplectic identity remains exact.

## 20. Exact objective counterexample

Define a toy objective:

\[
F(q)=\frac12q^2.
\]

At the same states:

\[
F(q_0)=0,
\]

\[
F(q_1)=\frac18.
\]

Therefore the symplectic map moved uphill under this objective.

This is not a defect in the integrator.

The map was derived to preserve variational/symplectic structure, not to minimize \(F\) at every step.

## 21. Optimization and mechanics use different objectives

This distinction is easy to blur.

In mechanics:

- the action determines equations of motion;
- the Hamiltonian can represent energy;
- a symplectic map preserves phase-space geometry.

In optimization:

- an objective is to be minimized;
- a step may be designed for descent, convergence, acceleration, constraint preservation, or another criterion.

A variational optimizer can connect these worlds.

It must still state which mathematical object is doing which job.

## 22. Manifold geometry re-enters

MANOPT-001 established another route to geometry-derived updates.

Given a constrained state:

1. compute an ambient or Riemannian gradient;
2. project or represent it in the tangent space;
3. choose a tangent step;
4. retract back to the manifold.

This pipeline resembles variational construction in one broad sense:

the update is constrained by declared geometry.

But a retraction-based update need not arise from an action principle.

## 23. MODULUS as programme evidence

At protected commit:

7ca4ffcdace32d5ff79c27ad557bfb690fac0af3

the GCL MODULUS project describes itself as an optimization research toolkit that treats geometry as a first-class optimizer control surface.

Its Hyperball implementation wraps a base optimizer.

The base optimizer proposes an update.

Hyperball can then:

- project it into a tangent space;
- control its norm;
- apply an approximate angular-step policy;
- retract the result to a sphere;
- or apply ball-style norm control.

This is a concrete programme example of deriving an update from explicit geometric constraints.

## 24. The exact MODULUS pipeline

For parameter group \(w\) and base proposal \(u\), the source implements:

\[
u_\parallel
=
\frac{\langle u,w\rangle}{\|w\|^2}w,
\]

\[
u_\perp
=
u-u_\parallel.
\]

A target-angle branch sets desired tangent-update norm approximately to:

\[
\alpha\|w\|.
\]

The finite point is then retracted.

This separates:

- base optimizer policy;
- tangent geometry;
- step-control policy;
- finite constraint restoration.

## 25. Exact programme witness

Take:

\[
w=(1,0),
\qquad
u=(1,1).
\]

Then:

\[
u_\parallel=(1,0),
\]

and:

\[
u_\perp=(0,1).
\]

With programme parameter:

\[
\alpha=1
\]

and unit radius, the pre-retraction tangent update has norm \(1\).

The retracted point is:

\[
w_+
=
\frac{(1,1)}{\sqrt2}.
\]

## 26. The target-angle subtlety

The exact angle from \(w\) to \(w_+\) is:

\[
\frac\pi4.
\]

That is not \(1\) radian.

For unit tangent direction \(v\), the general finite update:

\[
w_+
=
\frac{w+\alpha v}{\sqrt{1+\alpha^2}}
\]

has:

\[
\theta=\arctan\alpha.
\]

For small \(\alpha\):

\[
\theta
=
\alpha-\frac{\alpha^3}{3}
+
O(\alpha^5).
\]

So the implementation's target-angle parameter acts as a tangent-norm angular proxy.

It agrees to first order.

It is not an exact exponential-map/geodesic-angle control at finite step.

## 27. Why this distinction matters

If a parameter is called an angle, users may mentally identify it with a geodesic angle.

The exact construction shows the actual semantics.

This is the same discipline applied throughout the Atlas:

- name the representation;
- name the update;
- derive what it actually preserves;
- do not import stronger semantics from a convenient label.

## 28. MODULUS is not being promoted to general theory

The GCL repository profile for MODULUS is explicit.

Its authority covers:

- versioned implementation;
- benchmarks;
- empirical evidence.

It has no claim-promotion or certification authority.

Accordingly, VARIOPT uses MODULUS to show what one governed GCL geometry-first update pipeline actually does.

Established mathematical claims continue to come from established sources or Atlas proofs.

## 29. Geometry-derived is broader than variational

There are now at least three distinct mechanisms in view.

### Divergence-derived

Choose a convex generator and derive a local proximal/mirror step.

### Variational

Choose an action or Lagrangian and derive stationarity equations.

### Constraint-geometric

Choose a legal state geometry and transform an update through projection/retraction.

All three can produce structured updates.

They are not interchangeable derivations.

## 30. A variational derivation is not a convergence certificate

Suppose a discrete rule comes from a stationary discrete action.

That tells us where the rule came from.

Convergence of an optimization objective can still require:

- convexity;
- smoothness;
- coercivity;
- step restrictions;
- damping;
- Lyapunov arguments;
- stochastic assumptions;
- constraint regularity.

The derivation and the convergence proof are separate artifacts.

## 31. A divergence is not automatically the right geometry

Bregman divergences are generated by a chosen convex function.

Different generators define different local Hessians and different dual coordinates.

The right generator can depend on:

- domain;
- constraints;
- scale;
- sparsity;
- probability structure;
- desired invariances.

No source in this chapter proves one universal generator.

## 32. A symplectic optimizer would still need an optimization story

If an optimization method is designed to preserve a symplectic form in an enlarged state containing momentum, that can be a meaningful structural property.

But one must still answer:

- what objective is minimized?
- what damping is present?
- what convergence notion is used?
- how is the discrete step chosen?
- what happens to energy-like quantities?
- what does the structure buy empirically?

Symplecticity alone does not answer them.

## 33. Bregman-Lagrangian acceleration remains source-scoped

The Bregman-Lagrangian framework demonstrates that acceleration can be organized through continuous-time variational structure under specific scaling conditions.

That is stronger than an analogy.

But it remains a theorem about a declared framework.

The Atlas does not infer:

\[
\text{has a divergence}
\Rightarrow
\text{accelerated},
\]

nor:

\[
\text{has a Lagrangian}
\Rightarrow
\text{optimal convergence}.
\]

## 34. The final architecture lesson

The useful abstraction is not "physics-inspired optimizer."

It is more precise to **choose a mathematical structure, derive the dynamics that it permits, specify a discrete update, and prove or measure the actual property of interest**. Each transition requires its own assumptions and justification; a variational analogy alone establishes neither optimization descent nor empirical superiority.

## 35. Evidence classes

A VARIOPT claim should identify whether it is:

- a standard theorem from the mathematical literature;
- an Atlas exact finite derivation;
- a numerical model;
- a GCL programme implementation fact;
- an empirical benchmark result;
- an architectural proposal.

This chapter deliberately contains all but the empirical-superiority class.

They remain separate.

## 36. Durable non-implications

The chapter freezes:

\[
\text{divergence}
\not\Rightarrow
\text{metric},
\]

\[
\text{divergence-derived update}
\not\Rightarrow
\text{descent},
\]

\[
\text{variational derivation}
\not\Rightarrow
\text{accuracy or stability},
\]

\[
\text{symplecticity}
\not\Rightarrow
\text{energy conservation},
\]

\[
\text{symplecticity}
\not\Rightarrow
\text{objective descent},
\]

\[
\text{constraint preservation}
\not\Rightarrow
\text{optimizer superiority},
\]

and:

\[
\text{GCL programme mechanism}
\not\Rightarrow
\text{established general theory}.
\]

## 37. Closing the architecture layer

VARIOPT is the last chapter still in architecture state at this transaction baseline.

Its role is therefore not to add another optimizer catalog.

It closes an architectural question that runs through the Atlas:

> how should adaptive systems derive updates when the state space, numerical structure, or optimization geometry matters?

The answer is not one universal rule.

It is a disciplined methodology:

1. declare the geometry or action;
2. derive the update;
3. identify the preserved structure;
4. distinguish the discrete algorithm from its continuous source;
5. test descent, stability, accuracy, and empirical utility separately;
6. bind programme-specific mechanisms to their actual authority.

## References used in this chapter

- L. M. Bregman (1967), *The relaxation method of finding the common point of convex sets and its application to the solution of problems in convex programming*, DOI 10.1016/0041-5553(67)90040-7.
- J. E. Marsden and M. West (2001), *Discrete mechanics and variational integrators*, Acta Numerica 10:357–514, DOI 10.1017/S096249290100006X.
- Andre Wibisono, Ashia C. Wilson, and Michael I. Jordan (2016), *A variational perspective on accelerated methods in optimization*, PNAS 113(47):E7351–E7358, DOI 10.1073/pnas.1614734113.
- protected GCL MODULUS implementation/programme evidence at commit 7ca4ffcdace32d5ff79c27ad557bfb690fac0af3.

Exact authority and claim boundaries are recorded in:

sources/source-locks/ATLAS-CH-VARIOPT-001.yaml
