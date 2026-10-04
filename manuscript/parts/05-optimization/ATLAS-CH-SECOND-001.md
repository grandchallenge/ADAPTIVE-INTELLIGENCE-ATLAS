# Curvature and Second-Order Structure
<!-- ATLAS-CH-SECOND-001 -->

**Epistemic status:** mathematical exposition built from audited First-Order Optimization and Geometry prerequisites, classical second-order optimization sources, and Atlas-owned exact witnesses.  
**Derivation packet:** \`mathematics/derivations/ATLAS-CH-SECOND-001-DERIVATIONS.md\`  
**Computational witness:** \`mathematics/computational-witnesses/ATLAS-CW-SECOND-001.md\`  
**Source lock:** \`sources/source-locks/ATLAS-CH-SECOND-001.yaml\`

## 1. The gradient tells you a direction; curvature tells you how that direction changes

First-order optimization begins with a local slope.

For a differentiable objective \(f\), the Euclidean gradient

\[
g=\nabla f(x)
\]

is the first-order signal.

It answers:

> What infinitesimal direction changes the objective most rapidly under the declared Euclidean metric?

Second-order structure asks another question:

> How does that first-order signal change as we move?

For twice-differentiable \(f\), the Hessian

\[
H=\nabla^2 f(x)
\]

is the local linear map that differentiates the gradient.

Gradient magnitude and curvature are therefore different objects.

A small gradient can occur in a flat basin, at a sharp local extremum, or near a saddle.

Curvature helps distinguish those cases locally.

## 2. Local quadratic model

Near \(x\), a twice-differentiable objective has the local model

\[
m_x(p)
=
f(x)
+
g^\top p
+
\frac12 p^\top H p.
\]

The first term is the current objective.

The linear term is the first-order prediction.

The quadratic term describes how the prediction bends.

If \(H\) is positive definite, the quadratic term bends upward in every nonzero direction.

If \(H\) is indefinite, some directions bend upward and others downward.

That sign structure is central.

## 3. Newton's equation

A stationary point of the local quadratic model satisfies

\[
\nabla_p m_x(p)
=
g+Hp
=
0.
\]

If \(H\) is nonsingular,

\[
\boxed{
p_N=-H^{-1}g.
}
\]

This is the Newton step.

It is tempting to read this as "divide the gradient by curvature."

That phrase is useful only if we remember that curvature is a matrix, not a scalar.

The inverse Hessian rotates and rescales the gradient according to local curvature directions.

## 4. Positive-definite curvature gives a descent direction

Suppose

\[
H\succ0
\]

and

\[
g\neq0.
\]

Then

\[
g^\top p_N
=
-g^\top H^{-1}g
<
0.
\]

So the Newton direction is locally descending.

This fact depends on positive definiteness.

It is not true for arbitrary invertible Hessians.

That boundary will matter immediately.

## 5. Exact positive-definite witness

Take

\[
H=
\begin{pmatrix}
1&0\\
0&4
\end{pmatrix},
\qquad
b=
\begin{pmatrix}
1\\
1
\end{pmatrix},
\]

and

\[
f(x)
=
\frac12 x^\top Hx-b^\top x.
\]

At

\[
x_0=0,
\]

the gradient is

\[
g_0=-b
=
\begin{pmatrix}
-1\\
-1
\end{pmatrix}.
\]

The Newton equation is

\[
Hp=-g_0=b.
\]

Thus

\[
p_N
=
H^{-1}b
=
\begin{pmatrix}
1\\
1/4
\end{pmatrix}.
\]

Because the objective itself is quadratic, the local model is exact.

The step reaches the unique minimizer in one move.

The objective changes from

\[
f(0)=0
\]

to

\[
f(p_N)=-5/8.
\]

The directional derivative is

\[
g_0^\top p_N=-5/4<0.
\]

This is the clean case.

## 6. Indefinite curvature breaks the simple Newton story

Now consider

\[
f(x,y)
=
\frac12(x^2-y^2).
\]

At

\[
z_0=(0,1)^\top,
\]

we have

\[
g=
\begin{pmatrix}
0\\
-1
\end{pmatrix},
\qquad
H=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}.
\]

The Newton equation gives

\[
p_N=
\begin{pmatrix}
0\\
-1
\end{pmatrix}.
\]

But

\[
g^\top p_N=1>0.
\]

So the raw Newton direction is an ascent direction.

The full step moves to

\[
(0,0),
\]

where

\[
f(0,0)=0
\]

instead of the starting value

\[
f(0,1)=-1/2.
\]

The objective increases.

The Newton equation solved the stationary condition of the local quadratic model.

That stationary point was a saddle.

This is why second-order methods need more than "invert the Hessian."

## 7. Curvature signatures

For a symmetric Hessian:

- all positive eigenvalues indicate locally positive curvature;
- all negative eigenvalues indicate locally negative curvature;
- mixed signs indicate an indefinite saddle-like quadratic model;
- zero eigenvalues indicate locally flat or degenerate directions.

This is local information.

A positive-definite Hessian at one point does not make the entire objective globally convex.

An indefinite Hessian at one point does not completely describe the global landscape.

## 8. Damped and regularized Newton systems

One response to difficult curvature is to modify the local system.

A common form is

\[
(H+\lambda I)p=-g.
\]

For sufficiently large positive \(\lambda\), the shifted matrix may become positive definite.

This changes the local model.

It can improve stability.

But it is no longer the exact unmodified Newton step.

The Atlas keeps that distinction explicit:

\[
\boxed{
\text{exact Hessian}
\neq
\text{regularized Hessian}.
}
\]

## 9. Trust regions: constrain where the model is trusted

A different globalization strategy is to keep the quadratic model but limit how far we are willing to follow it.

A trust-region subproblem has the form

\[
\min_p
\left(
g^\top p
+
\frac12 p^\top Bp
\right)
\]

subject to

\[
\|p\|\le\Delta.
\]

The radius \(\Delta\) is not merely a clipping threshold.

It expresses a model-validity region.

The algorithm compares predicted and actual decrease and can adjust the radius accordingly [@NocedalWright2006].

## 10. Exact trust-region control on the indefinite witness

Return to

\[
f(x,y)=\frac12(x^2-y^2)
\]

at

\[
(0,1).
\]

Use trust-region radius

\[
\Delta=1.
\]

The model increment is

\[
q(p)
=
-p_2
+
\frac12 p_1^2
-
\frac12 p_2^2.
\]

Over the unit disk, the exact minimizer is

\[
p_{\rm TR}
=
\begin{pmatrix}
0\\
1
\end{pmatrix}.
\]

The model change is

\[
q(p_{\rm TR})=-3/2.
\]

The new point is

\[
(0,2),
\]

where

\[
f(0,2)=-2.
\]

The raw Newton step climbed toward the saddle.

The trust-region subproblem moved along negative curvature and decreased the objective.

This one example does not prove a universal trust-region advantage.

It shows why indefinite curvature needs different logic from positive-definite Newton.

## 11. Exact Hessians can be too large to store

For \(d\) parameters, a dense Hessian has \(d^2\) entries.

That quickly becomes impractical.

But many second-order algorithms do not need the full matrix.

They need the action

\[
Hv
\]

on selected vectors.

Pearlmutter showed how such products can be computed exactly in the cited neural-computation setting without explicitly forming the dense Hessian [@Pearlmutter1994Hessian].

The fundamental identity is

\[
Hv
=
\frac{d}{d\varepsilon}
\nabla f(x+\varepsilon v)
\Big|_{\varepsilon=0}.
\]

This is the second-order analogue of matrix-free operator access.

## 12. Matrix-free second-order structure

Once Hessian-vector products are available, several operations become possible without storing \(H\):

- curvature probing;
- iterative linear solves for Newton-like systems;
- extremal-eigenvalue estimation;
- conjugate-gradient methods in suitable positive-definite systems;
- trust-region subproblem methods.

This does not make second-order computation free.

The relevant costs move into repeated products, iterative solves, damping, preconditioning, and numerical stability.

## 13. Fisher information is a different matrix

Optimization discussions sometimes slide from "curvature" to "Fisher information" as if they were synonyms.

They are not.

For a probabilistic model

\[
p_\theta(y),
\]

the Fisher information matrix is built from score covariances, for example

\[
F(\theta)
=
\mathbb E
\left[
\nabla_\theta \log p_\theta(y)
\nabla_\theta \log p_\theta(y)^\top
\right]
\]

under the declared distribution.

The Hessian is a second derivative of a declared scalar objective.

These matrices can be related in important settings.

They are not generically identical.

## 14. Natural gradient

The ordinary gradient depends on the metric used to define steepest descent.

In the Euclidean metric, the local squared norm is

\[
\|\delta\|_2^2
=
\delta^\top\delta.
\]

Under a positive-definite metric \(G(\theta)\),

\[
\|\delta\|_G^2
=
\delta^\top G(\theta)\delta.
\]

The steepest-descent direction changes to a direction proportional to

\[
-G^{-1}g.
\]

When \(G\) is the Fisher information metric, this gives the natural gradient [@Amari1998NaturalGradient].

This is a geometric metric statement.

It is not automatically a Newton step.

## 15. Exact metric witness

Let

\[
G=
\begin{pmatrix}
1&0\\
0&4
\end{pmatrix},
\qquad
g=
\begin{pmatrix}
1\\
1
\end{pmatrix}.
\]

Euclidean steepest descent uses

\[
-g=
\begin{pmatrix}
-1\\
-1
\end{pmatrix}.
\]

Metric steepest descent uses

\[
-G^{-1}g
=
\begin{pmatrix}
-1\\
-1/4
\end{pmatrix}.
\]

The directions differ.

Changing the metric changes what "steepest" means.

The numerical coincidence that this matrix resembles the positive-definite Hessian in our earlier witness does not identify natural gradient with Newton.

The interpretation of the matrix is different.

## 16. Hessian versus Fisher

A useful discipline is to ask three separate questions:

1. What scalar objective is being differentiated?
2. What probability distribution defines the Fisher expectation?
3. What metric is being used to define steepest descent?

If those objects are not explicitly aligned, the words "curvature," "Fisher," and "natural gradient" should not be substituted for one another.

This prevents a common category error.

## 17. Quasi-Newton methods

Exact Hessians can be expensive.

Quasi-Newton methods instead update a matrix approximation using observed changes in gradients.

Let

\[
s_k=x_{k+1}-x_k
\]

and

\[
y_k=
\nabla f(x_{k+1})
-
\nabla f(x_k).
\]

A Hessian approximation \(B_{k+1}\) may be required to satisfy the secant equation

\[
B_{k+1}s_k=y_k.
\]

This forces the approximation to match the observed curvature action along the most recent displacement.

It does not make \(B_{k+1}\) the exact Hessian in every direction.

## 18. BFGS and curvature conditions

BFGS is one of the canonical quasi-Newton updates [@NocedalWright2006].

For the standard positive-definite Hessian-approximation form, the condition

\[
y_k^\top s_k>0
\]

is load-bearing for preserving positive definiteness when the previous approximation is positive definite.

This matters because the sign of the approximate curvature influences whether the resulting search direction is descending.

The update formula is not magic.

Its guarantees have hypotheses.

## 19. Secant replay

For our positive-definite quadratic

\[
H=
\operatorname{diag}(1,4),
\]

take

\[
s=
\begin{pmatrix}
1\\
2
\end{pmatrix}.
\]

Then the exact gradient change is

\[
y=Hs
=
\begin{pmatrix}
1\\
8
\end{pmatrix}.
\]

Any quasi-Newton matrix satisfying

\[
Bs=y
\]

matches the true curvature along that one displacement.

That single equation still leaves many degrees of freedom in \(B\).

A secant condition is partial curvature information.

## 20. Proximal structure is not "more curvature"

Second-order optimization is often discussed alongside proximal methods because both go beyond a bare gradient step.

But proximal structure addresses a different problem.

Suppose

\[
F(x)=f(x)+h(x),
\]

where \(f\) is smooth and \(h\) may be nonsmooth.

The proximal operator is

\[
\operatorname{prox}_{\alpha h}(v)
=
\arg\min_x
\left[
h(x)
+
\frac{1}{2\alpha}\|x-v\|_2^2
\right].
\]

It is an implicit local optimization primitive [@ParikhBoyd2014Proximal].

It is not a Hessian approximation.

## 21. Soft thresholding witness

Take

\[
h(x)=\lambda |x|
\]

with

\[
\alpha\lambda=1.
\]

Then

\[
\operatorname{prox}_{\alpha h}(v)
=
\operatorname{sign}(v)
\max(|v|-1,0).
\]

Thus

\[
v=3
\longmapsto
2,
\]

while

\[
v=1/2
\longmapsto
0.
\]

The zero output comes from solving the nonsmooth proximal subproblem.

It is not ordinary gradient clipping.

## 22. Proximal gradient

For composite objectives

\[
F(x)=f(x)+h(x),
\]

a proximal-gradient step takes the form

\[
x_{k+1}
=
\operatorname{prox}_{\alpha h}
\left(
x_k-\alpha\nabla f(x_k)
\right).
\]

The step explicitly separates:

- smooth first-order information from \(f\);
- implicit nonsmooth structure from \(h\).

This is a different axis from exact second derivatives.

## 23. What second-order methods actually buy

Second-order structure can provide:

- anisotropic rescaling;
- local curvature-aware directions;
- faster local convergence in favorable regimes;
- curvature diagnostics;
- principled handling of local quadratic models.

But the price can include:

- expensive curvature access;
- difficult indefinite systems;
- noisy estimates;
- storage or iterative-solve costs;
- damping/globalization logic;
- metric or model misspecification.

There is no free "use curvature" switch.

## 24. Local models and global optimization

A second-order method is still local.

The Hessian tells us how the objective bends near the current point.

A trust region limits how far we believe that local model.

A line search tests a step along a direction.

A quasi-Newton matrix infers curvature from recent changes.

A natural gradient changes the metric.

A proximal operator solves a declared local implicit subproblem.

These mechanisms solve different problems.

They should not be merged into one vague notion of sophistication.

## 25. Failure modes

### 25.1 Hessian equals Fisher

Not in general.

They arise from different constructions.

### 25.2 Natural gradient equals Newton

Not in general.

Natural gradient uses a metric; Newton uses the objective Hessian.

### 25.3 Invertible Hessian means safe Newton step

False.

The indefinite witness gives an ascent direction.

### 25.4 Trust region equals clipping

False.

A trust region solves a constrained model subproblem and reasons about model validity.

### 25.5 Quasi-Newton equals exact curvature

False.

The approximation satisfies limited secant information.

### 25.6 HVP means Hessian is cheap

False.

It avoids explicit formation but repeated products and solves still cost computation.

### 25.7 Proximal method is second-order

Not by definition.

It is an implicit optimization construction, especially useful for nonsmooth/composite structure.

### 25.8 Positive local curvature means global convexity

False.

Local Hessian information is local.

### 25.9 Exact local model means global optimum

False.

Newton solves the local quadratic stationary condition.

Global behavior requires additional assumptions and globalization logic.

## 26. Downstream handoff

Matrix-Aware Optimization may inherit:

- Hessian and curvature notation;
- positive/indefinite curvature distinctions;
- matrix-free operator action;
- natural-gradient metric language;
- quasi-Newton exact-versus-approximate discipline;
- trust-region and damping boundaries.

It may not assume that these classical objects already justify:

- Shampoo's specific preconditioner;
- polar-factor updates;
- orthogonalized matrix steps;
- Muon-like spectral shaping;
- square-to-rectangular generalization.

Those are downstream obligations.

## References used in this chapter

- [@NocedalWright2006] — Newton, quasi-Newton, trust-region, and large-scale smooth optimization.
- [@Amari1998NaturalGradient] — natural gradient and information geometry.
- [@Pearlmutter1994Hessian] — exact Hessian-vector products.
- [@ParikhBoyd2014Proximal] — proximal operators and algorithms.

Exact provenance and claim boundaries are locked in:

\`sources/source-locks/ATLAS-CH-SECOND-001.yaml\`
