# Chapter Specification — ATLAS-CH-MATRIXOPT-001

## Identity

**Title:** Matrix-Aware Optimization  
**Part:** Optimization, Landscapes, and Learning Rules  
**Status:** specification-ready.  
**Epistemic class:** audited Linear Algebra and Curvature/Second-Order prerequisites + primary Shampoo, polar-decomposition, norm-steepest-descent, and Muon design sources + Atlas synthesis.

## Contract

Develop optimization rules that act on a matrix parameter block as a matrix rather than as an undifferentiated list of scalar coordinates.

The chapter must distinguish:

- scalar or elementwise adaptive scaling from matrix preconditioning;
- left and right geometry for rectangular parameter blocks;
- structured matrix second moments from a full curvature matrix;
- inverse-root preconditioning from polar or orthogonalized update construction;
- singular-value flattening from intentional spectral shaping;
- Frobenius, spectral, and other norm-dependent steepest directions;
- square intuition from genuinely rectangular behavior;
- exact SVD/polar objects from finite numerical approximations;
- instantaneous gradient transforms from optimizer-state dynamics;
- matrix-aware updates from hard manifold constraints.

The chapter must not claim universal empirical superiority for any named optimizer.

## Hard prerequisites

- ATLAS-CH-LINALG-001
- ATLAS-CH-SECOND-001

Exact prerequisite identities and source scopes are locked in:

sources/source-locks/ATLAS-CH-MATRIXOPT-001.yaml

## Matrix block

Let

\[
G\in\mathbb R^{m\times n}
\]

be the gradient of a scalar objective with respect to one matrix parameter block.

Write a reduced singular-value decomposition

\[
G=U\Sigma V^\top.
\]

The singular values expose directional anisotropy in the matrix update. They do not by themselves determine the best optimizer.

## Elementwise versus matrix-aware transformations

A left-right matrix rule has the form

\[
\widetilde G=A\,G\,B.
\]

Vectorization gives

\[
\operatorname{vec}(AGB)
=
(B^\top\otimes A)\operatorname{vec}(G).
\]

Thus left-right preconditioning represents a structured operator on the vectorized parameter block. It is not automatically the full Hessian, Fisher matrix, or another exact curvature operator.

## Shampoo structure

For a matrix gradient sequence \(G_t\), a matrix specialization of Shampoo accumulates

\[
L_t=\sum_{s\le t}G_sG_s^\top,
\qquad
R_t=\sum_{s\le t}G_s^\top G_s.
\]

A representative damped preconditioned direction is

\[
P_t
=
(L_t+\varepsilon I_m)^{-1/4}
\,G_t\,
(R_t+\varepsilon I_n)^{-1/4}.
\]

The fourth-root exponents arise from the two-mode matrix specialization.

This is a structured accumulated preconditioner. It must not be described as an exact full-Hessian inverse.

## Rectangular rank boundary

At one step,

\[
L=GG^\top,
\qquad
R=G^\top G.
\]

If \(m>n\) and \(G\) has full column rank, then

\[
\operatorname{rank}(L)=n<m,
\]

so \(L\) is singular even though \(G\) has maximal possible rank.

If \(n>m\), the corresponding statement holds for \(R\).

Damping, accumulated history, support-restricted inverse powers, or another declared convention is therefore material.

## Polar factor

For reduced SVD

\[
G=U\Sigma V^\top,
\]

define

\[
Q=UV^\top.
\]

If \(m\ge n\) and \(G\) has full column rank,

\[
Q=G(G^\top G)^{-1/2},
\qquad
Q^\top Q=I_n.
\]

If \(n\ge m\) and \(G\) has full row rank,

\[
Q=(GG^\top)^{-1/2}G,
\qquad
QQ^\top=I_m.
\]

For a non-square matrix, \(Q\) is semi-orthogonal.

## Singular-value flattening

The exact polar factor replaces every nonzero singular value of \(G\) by \(1\):

\[
U\Sigma V^\top
\longmapsto
UIV^\top.
\]

This is exact singular-value flattening.

It is not synonymous with improving every optimization problem, whitening data, approximating a Hessian inverse, or choosing an intentionally non-flat target spectrum.

The last topic belongs downstream in ATLAS-CH-SPECTRALSHAPE-001.

## Norm-dependent steepest directions

For a local linearized objective

\[
f(W+\Delta)
\approx
f(W)+\langle G,\Delta\rangle_F,
\]

under

\[
\|\Delta\|_F\le\rho,
\]

one minimizer is

\[
\Delta_F^\star
=
-\rho\frac{G}{\|G\|_F}.
\]

Under

\[
\|\Delta\|_2\le\rho,
\]

a minimizer is

\[
\Delta_2^\star
=
-\rho UV^\top.
\]

Because the dual of the spectral norm is the nuclear norm,

\[
\min_{\|\Delta\|_2\le\rho}
\langle G,\Delta\rangle_F
=
-\rho\|G\|_*.
\]

These are different optimization problems because the feasible sets differ.

## One-step Shampoo/polar relation

On the nonzero singular support,

\[
(GG^\top)^{-1/4}
\,G\,
(G^\top G)^{-1/4}
=
UV^\top.
\]

For a rectangular matrix, a strict full-space inverse may not exist.

The identity therefore requires a declared support-restricted inverse convention, pseudoinverse-style extension, or appropriate zero-damping limit.

Actual Shampoo is stateful because \(L_t\) and \(R_t\) accumulate earlier gradients. The one-step identity does not collapse stateful Shampoo into an exact polar transform at every step.

## Muon-like update construction

A representative Muon-like design is:

1. construct a momentum-like matrix update;
2. scale it into a numerically suitable range;
3. apply a finite Newton-Schulz-like polynomial iteration intended to approximate an orthogonalized/polar-style transform;
4. use the transformed matrix as the parameter update.

The finite iteration is not the exact SVD or exact polar decomposition. Its effect is a finite singular-value map, and the momentum state is part of the optimizer.

## Exact rectangular witness

Use

\[
G=
\begin{pmatrix}
2&0\\
0&1\\
1&0
\end{pmatrix}.
\]

Then

\[
G^\top G
=
\begin{pmatrix}
5&0\\
0&1
\end{pmatrix},
\]

while

\[
GG^\top
=
\begin{pmatrix}
4&0&2\\
0&1&0\\
2&0&1
\end{pmatrix}.
\]

The singular values are

\[
\sqrt5,\ 1.
\]

The left Gram matrix has rank \(2<3\).

The exact polar factor is

\[
Q=
\begin{pmatrix}
2/\sqrt5&0\\
0&1\\
1/\sqrt5&0
\end{pmatrix}.
\]

Then

\[
Q^\top Q=I_2,
\]

but

\[
QQ^\top
=
\begin{pmatrix}
4/5&0&2/5\\
0&1&0\\
2/5&0&1/5
\end{pmatrix}
\neq I_3.
\]

## Diagonal-scaling control

Choose

\[
D=\operatorname{diag}(1/2,1,1/2).
\]

Then

\[
DG=
\begin{pmatrix}
1&0\\
0&1\\
1/2&0
\end{pmatrix},
\]

whose singular values are

\[
\sqrt5/2,\ 1.
\]

The diagonal transform changes anisotropy but does not produce the exact polar factor. This is a generic control, not a claim that a named elementwise optimizer uses this \(D\).

## Exact-versus-approximate realization

Large optimizers may approximate matrix functions by eigendecomposition, iterative roots, Newton-Schulz iterations, low-precision polynomials, blocking, distribution, or delayed refresh.

The realized update can therefore differ from the exact target. The numerical method is part of the optimizer specification.

## Optimizer-state boundary

An instantaneous map

\[
G_t\mapsto T(G_t)
\]

does not describe a stateful optimizer when

\[
S_t=\Phi(S_{t-1},G_t).
\]

Shampoo accumulators and Muon-style momentum make this distinction concrete.

## Manifold boundary

An orthogonalized update matrix is not the same as an orthogonality-constrained parameter matrix.

A method may use

\[
\Delta_t\approx UV^\top
\]

while \(W_t\) remains unconstrained.

Manifold optimization instead declares a feasible set for the parameter/state and uses tangent/retraction machinery to maintain it.

## Failure boundaries

- elementwise scaling != matrix preconditioning;
- matrix preconditioning != full Hessian inversion;
- left/right Gram factors != a full dense curvature matrix;
- one-step support identity != stateful Shampoo equivalence;
- polar factor != hard manifold constraint on the parameter;
- exact SVD/polar != finite Newton-Schulz iteration;
- orthogonalized update != universal optimizer improvement;
- singular-value flattening != arbitrary spectral shaping;
- square orthogonality intuition != rectangular semi-orthogonality;
- instantaneous matrix transform != optimizer-state dynamics;
- empirical source result != universal deep-learning theorem.

## Downstream handoff

Direct consumer:

- ATLAS-CH-SPECTRALSHAPE-001.

SPECTRALSHAPE may inherit SVD/polar language, rectangular semi-orthogonality, norm-dependent steepest directions, and exact-versus-approximate singular-value transformations.

It must independently justify intentional non-flat spectral targets and their claimed effects.

## Sources

- [@GuptaKorenSinger2018Shampoo]
- [@Higham1986Polar]
- [@BernsteinNewhouse2024OldOptimizer]
- [@JordanEtAl2024Muon]

Exact source authority and claim boundaries are locked in:

sources/source-locks/ATLAS-CH-MATRIXOPT-001.yaml
