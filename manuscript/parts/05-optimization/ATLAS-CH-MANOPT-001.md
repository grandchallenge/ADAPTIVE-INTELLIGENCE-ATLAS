# Optimization on Manifolds
<!-- ATLAS-CH-MANOPT-001 -->

**Epistemic status:** audited Geometry + audited First-Order Optimization prerequisites + standard matrix-manifold optimization sources + Atlas derivation + exact finite witness.  
**Specification:** manuscript/specifications/ATLAS-CH-MANOPT-001.md  
**Derivation packet:** mathematics/derivations/ATLAS-CH-MANOPT-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-MANOPT-001.md  
**Source lock:** sources/source-locks/ATLAS-CH-MANOPT-001.yaml

## 1. Optimization changes when legal states form a curved space

Ordinary first-order optimization usually assumes parameters may move freely in Euclidean coordinates.

Many useful objects do not have that freedom.

Examples include:

- unit vectors;
- orthonormal frames;
- rotation matrices;
- fixed-rank factorizations;
- positive-definite matrices;
- subspaces.

If the parameter must satisfy

\[
\|x\|=1
\]

or

\[
X^\top X=I,
\]

then an arbitrary Euclidean update generally leaves the admissible set.

Optimization on manifolds changes the question from:

> Which ambient direction decreases the objective?

to:

> Which locally legal direction decreases the objective, and how do we turn it into a legal finite move?

That separation is the chapter's organizing idea.

## 2. Tangent directions are local legal velocities

For a smooth manifold \(M\), the tangent space

\[
T_xM
\]

is a linear approximation to the legal directions at \(x\).

A tangent vector is not usually another point on the manifold.

It is a velocity.

This matters because the update

\[
x+\xi
\]

can leave \(M\) even when

\[
\xi\in T_xM.
\]

A constrained optimizer therefore needs two distinct operations:

1. choose a tangent direction;
2. map the finite displacement back to the manifold.

The first is local differential geometry.

The second is finite constrained motion.

## 3. The gradient depends on the metric

The First-Order Optimization chapter treated the Euclidean gradient as the steepest direction under the Euclidean metric.

A manifold may have a different metric.

So the Riemannian gradient is defined by

\[
Df(x)[\xi]
=
\langle \operatorname{grad}f(x),\xi\rangle_x
\]

for every tangent vector

\[
\xi\in T_xM.
\]

The metric appears inside the definition.

Therefore:

\[
\boxed{
\text{gradient}
=
\text{objective derivative + metric}.
}
\]

Changing the metric can change the steepest direction even when the objective function is unchanged.

## 4. Embedded manifolds and tangent projection

For an embedded manifold with the induced Euclidean metric, the Riemannian gradient is obtained by projecting the ambient Euclidean gradient onto the tangent space [@AbsilMahonySepulchre2008].

Write

\[
\Pi_x
\]

for the orthogonal tangent projection.

Then

\[
\operatorname{grad}f(x)
=
\Pi_x(\nabla F(x)),
\]

where \(F\) is an ambient extension of \(f\).

This formula is powerful and easy to misuse.

It is valid for the induced metric setting being described.

It should not be promoted into a universal formula for every Riemannian metric.

## 5. Sphere geometry

For the unit sphere

\[
S^{n-1}
=
\{x\in\mathbb R^n:\|x\|=1\},
\]

the tangent space is

\[
T_xS^{n-1}
=
\{\xi:x^\top\xi=0\}.
\]

The induced-metric tangent projection is

\[
\Pi_x(g)
=
g-(x^\top g)x.
\]

The normal component lies along \(x\).

The tangent component is what first-order constrained motion may use.

## 6. Tangent projection is not the update

Suppose

\[
g=\nabla F(x).
\]

A projected direction

\[
-\Pi_x(g)
\]

is tangent.

But the raw finite step

\[
x-\eta\Pi_x(g)
\]

need not satisfy the original nonlinear constraint.

The tangent plane touches the manifold.

It is not the manifold.

This gives a basic boundary:

\[
\boxed{
\text{legal infinitesimal direction}
\neq
\text{legal finite endpoint}.
}
\]

## 7. Retractions

A retraction is a practical map from tangent data back to the manifold [@AbsilMahonySepulchre2008].

Locally it satisfies:

\[
R_x(0_x)=x
\]

and

\[
DR_x(0_x)
=
\operatorname{id}_{T_xM}.
\]

So the retraction agrees with tangent motion to first order.

It does not have to trace an exact geodesic.

This matters computationally because exact exponential maps may be expensive while useful retractions can be cheaper.

## 8. Sphere normalization as a retraction

For tangent \(\xi\) on the unit sphere, define:

\[
R_x(\xi)
=
\frac{x+\xi}{\|x+\xi\|}.
\]

Because

\[
x^\top\xi=0,
\]

we have

\[
\|x+\xi\|^2
=
1+\|\xi\|^2.
\]

Therefore

\[
\|R_x(\xi)\|=1.
\]

The normalized endpoint is exactly feasible.

The move is not generally the sphere exponential map.

## 9. Exact sphere witness

Take

\[
x=(1,0)^\top,
\qquad
a=(1,2)^\top,
\qquad
f(z)=a^\top z.
\]

The ambient gradient is

\[
a=(1,2)^\top.
\]

Projecting onto the tangent space at \(x\) gives

\[
\operatorname{grad}f(x)
=
(0,2)^\top.
\]

Choose

\[
\eta=\frac12.
\]

The tangent descent vector is

\[
\xi=(0,-1)^\top.
\]

The unconstrained Euclidean update is

\[
(1/2,-1)^\top,
\]

whose squared norm is

\[
5/4.
\]

It leaves the sphere.

The raw tangent displacement

\[
x+\xi=(1,-1)^\top
\]

also leaves the sphere because its squared norm is \(2\).

After normalization:

\[
R_x(\xi)
=
\frac1{\sqrt2}(1,-1)^\top,
\]

and the norm is exactly \(1\).

The witness separates three things:

- ambient Euclidean descent;
- tangent descent;
- feasible finite motion.

## 10. Retraction versus exponential map

For the same sphere witness,

\[
\|\xi\|=1.
\]

The exact exponential endpoint is

\[
\operatorname{Exp}_x(\xi)
=
(\cos1,-\sin1)^\top.
\]

The normalized retraction endpoint is

\[
(1/\sqrt2,-1/\sqrt2)^\top.
\]

Both are legal.

They differ.

Therefore:

\[
\boxed{
\text{retraction}
\neq
\text{exponential map}.
}
\]

A retraction earns its role through local first-order agreement and feasibility, not by being an exact geodesic solver.

## 11. The Stiefel manifold

The Stiefel manifold is

\[
\operatorname{St}(n,p)
=
\{X\in\mathbb R^{n\times p}:X^\top X=I_p\}.
\]

Its columns are orthonormal.

This constraint appears throughout numerical linear algebra and optimization with orthogonality constraints [@EdelmanAriasSmith1998].

A tangent matrix \(Z\) satisfies

\[
X^\top Z+Z^\top X=0.
\]

This is obtained by differentiating

\[
X^\top X=I.
\]

The condition is linear in \(Z\), as a tangent-space constraint should be.

## 12. Stiefel tangent projection

Under the induced Euclidean metric, an ambient matrix \(G\) can be projected by

\[
\Pi_X(G)
=
G-X\operatorname{sym}(X^\top G),
\]

where

\[
\operatorname{sym}(A)
=
\frac12(A+A^\top).
\]

The projected matrix satisfies

\[
X^\top\Pi_X(G)
+
\Pi_X(G)^\top X
=
0.
\]

Again, this produces a legal local direction.

It does not by itself produce a legal finite orthonormal matrix after ambient addition.

## 13. Polar retraction on the Stiefel manifold

For tangent \(\Xi\), one retraction is

\[
R_X(\Xi)
=
(X+\Xi)
(I+\Xi^\top\Xi)^{-1/2}.
\]

The tangent condition implies

\[
(X+\Xi)^\top(X+\Xi)
=
I+\Xi^\top\Xi.
\]

Therefore:

\[
R_X(\Xi)^\top R_X(\Xi)=I.
\]

The retraction restores the orthogonality constraint exactly.

## 14. Exact \(2\times2\) witness

Let

\[
X=I_2
\]

and

\[
\Xi=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix}.
\]

Because \(\Xi\) is skew-symmetric,

\[
X^\top\Xi+\Xi^\top X=0.
\]

So it is tangent.

The raw step is

\[
X+\Xi
=
\begin{pmatrix}
1&-1\\
1&1
\end{pmatrix}.
\]

Its Gram matrix is

\[
2I.
\]

Thus the raw tangent displacement is not orthogonal.

The polar retraction is

\[
\frac1{\sqrt2}
\begin{pmatrix}
1&-1\\
1&1
\end{pmatrix},
\]

whose Gram matrix is exactly \(I\).

Constraint restoration is exact.

## 15. Orthogonal does not mean geodesically exact

For the same skew generator,

\[
e^\Xi
=
\begin{pmatrix}
\cos1&-\sin1\\
\sin1&\cos1
\end{pmatrix}.
\]

This is rotation by \(1\) radian.

The polar-retracted endpoint is rotation by

\[
\pi/4.
\]

Both are orthogonal.

They are different.

This is the matrix-manifold version of the same distinction:

\[
\text{constraint preservation}
\not\Rightarrow
\text{exponential/geodesic motion}.
\]

## 16. A generic first-order manifold step

A simple constrained first-order method can be written:

\[
\xi_k
=
-\eta_k\operatorname{grad}f(x_k),
\]

followed by

\[
x_{k+1}
=
R_{x_k}(\xi_k).
\]

This compact notation hides important design choices:

- metric;
- gradient estimator;
- tangent projection;
- step size;
- retraction;
- momentum;
- vector transport;
- stochastic sampling.

Optimization on a manifold is not one algorithm.

It is a family of algorithms respecting a declared geometric structure.

## 17. Momentum creates a tangent-space problem

Suppose an optimizer stores momentum

\[
m_k\in T_{x_k}M.
\]

After moving to

\[
x_{k+1},
\]

the new tangent space is

\[
T_{x_{k+1}}M.
\]

These two vector spaces are generally different subspaces of the ambient space.

Blindly reusing \(m_k\) as if nothing changed can ignore geometry.

A vector transport supplies a declared way to move tangent information between tangent spaces [@AbsilMahonySepulchre2008].

This is distinct from retraction:

- retraction moves a point;
- vector transport moves tangent information.

## 18. Intrinsic and extrinsic viewpoints

A manifold can be described intrinsically through its metric and curves.

It can also be embedded in a larger Euclidean space and manipulated through ambient coordinates.

Neither viewpoint is automatically superior.

The extrinsic viewpoint can make projections and constraints concrete.

The intrinsic viewpoint helps identify coordinate-independent structure.

The Atlas uses whichever representation makes the relevant claim precise.

## 19. Constraint preservation is not optimization quality

A method can preserve the constraint perfectly and still:

- increase the objective;
- take poor step sizes;
- converge slowly;
- stagnate;
- approach a bad stationary point.

Therefore:

\[
\boxed{
\text{constraint preservation}
\neq
\text{optimizer quality}.
}
\]

Geometry defines legal motion.

Optimization still requires a useful search rule.

## 20. Stationarity on a manifold

A first-order stationary point satisfies

\[
\operatorname{grad}f(x)=0.
\]

For an embedded manifold under induced metric, this means the ambient gradient has no tangent component.

The ambient gradient can still have a normal component.

Thus constrained stationarity differs from unconstrained Euclidean stationarity.

And first-order stationarity still does not imply global optimality.

## 21. Sphere versus Stiefel

The sphere constrains one vector:

\[
x^\top x=1.
\]

The Stiefel manifold constrains multiple columns simultaneously:

\[
X^\top X=I.
\]

The sphere tangent condition is scalar:

\[
x^\top\xi=0.
\]

The Stiefel tangent condition is matrix-valued:

\[
X^\top Z+Z^\top X=0.
\]

The two geometries are related but not interchangeable.

## 22. Stiefel versus Grassmann

A Stiefel point is an orthonormal frame.

A Grassmann point represents a subspace independent of which orthonormal basis is chosen for it.

The Geometry chapter already established this distinction.

It matters for optimization.

If the objective depends only on the spanned subspace, then treating different bases as distinct states may introduce redundant directions.

This is where quotient geometry enters.

MANOPT uses the distinction but does not redevelop quotient optimization in full.

## 23. Why parameterization matters

One can sometimes avoid an explicit constrained optimizer by parameterizing the constraint indirectly.

Examples include:

- normalized vectors;
- matrix exponentials;
- factorizations;
- Householder products;
- Cayley-like transforms.

Such choices change:

- coordinates;
- conditioning;
- computational cost;
- reachable sets;
- singularities;
- optimization dynamics.

A constraint-preserving parameterization is not automatically equivalent to direct manifold optimization.

The effective geometry can differ.

## 24. Geometry can change steepest descent

In Euclidean space, steepest descent depends on the Euclidean inner product.

On a manifold, the Riemannian metric changes the local notion of unit direction.

Therefore changing geometry can change the gradient even before any adaptive optimizer state is introduced.

This is one reason later Atlas work on geometry-aware and matrix-aware optimization must keep separate:

- the objective;
- the metric;
- the optimizer;
- the parameterization.

## 25. Retraction choice can matter

Two valid retractions agree to first order at the tangent origin.

They can differ at finite step sizes.

So a large-step optimization trajectory can depend on the retraction even when the tangent gradient is unchanged.

This is not a defect.

It is part of the algorithm.

A convergence theorem must state what retraction properties it assumes.

An experiment must state which retraction it used.

## 26. Step size still matters

Geometry does not remove ordinary optimization concerns.

A constrained method still needs to choose:

- step size;
- stochastic batch;
- line search or schedule;
- momentum state;
- clipping or trust restrictions;
- stopping rule.

A legal step can still be too large.

A legal trajectory can still be poor.

Manifold structure constrains the search space.

It does not solve the search problem by itself.

## 27. Relation to normalized models

Unit-norm states and orthogonality constraints appear naturally in normalized neural architectures.

The mathematical substrate in this chapter is directly relevant to such systems.

But the chapter stops at generic manifold optimization.

It does not establish:

- a theorem for nGPT;
- a theorem for Muon;
- a theorem for rectangular spectral updates;
- a theorem for MODULUS;
- a theorem for any specific GCL optimizer.

Those require their own objectives, metrics, updates, and evidence.

## 28. Relation to variational optimization

The direct downstream consumer is:

**Variational and Divergence-Derived Optimization — ATLAS-CH-VARIOPT-001.**

VARIOPT may inherit:

- tangent gradients;
- constrained finite motion;
- retractions;
- metric dependence;
- vector-transport distinctions;
- sphere/Stiefel examples.

It must independently justify any claim that an update follows from:

- a divergence;
- a discrete Lagrangian;
- a symplectic principle;
- a duality relation;
- another variational construction.

Manifold optimization says how to respect a constrained geometry.

Variational optimization asks where the motion rule itself comes from.

## 29. Durable boundaries

The chapter leaves ten distinctions:

1. Euclidean gradient is not automatically the Riemannian gradient.
2. Tangent projection is not a complete optimizer.
3. Tangent direction is not a finite feasible endpoint.
4. Retraction is not the exponential map.
5. First-order agreement is not geodesic exactness.
6. Sphere and Stiefel constraints are different.
7. Retraction and vector transport have different roles.
8. Constraint preservation is not convergence.
9. Manifold stationarity is not global optimality.
10. Generic manifold optimization is not a specific GCL optimizer theorem.

These boundaries are the reusable substrate.

## References used in this chapter

- [@AbsilMahonySepulchre2008]
- [@EdelmanAriasSmith1998]

Exact source identities and authority scopes are pinned in:

sources/source-locks/ATLAS-CH-MANOPT-001.yaml
