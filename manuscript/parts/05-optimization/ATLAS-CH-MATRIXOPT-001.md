# Matrix-Aware Optimization
<!-- ATLAS-CH-MATRIXOPT-001 -->

**Epistemic status:** audited Linear Algebra and Curvature/Second-Order prerequisites + primary Shampoo, polar-decomposition, norm-steepest-descent, and Muon design sources + Atlas derivation + exact rectangular witness.  
**Specification:** manuscript/specifications/ATLAS-CH-MATRIXOPT-001.md  
**Derivation packet:** mathematics/derivations/ATLAS-CH-MATRIXOPT-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-MATRIXOPT-001.md  
**Source lock:** sources/source-locks/ATLAS-CH-MATRIXOPT-001.yaml

## 1. A matrix parameter is not merely a bag of scalars

A linear layer may have a weight

\[
W\in\mathbb R^{m\times n},
\]

with gradient

\[
G=\nabla_W f(W).
\]

An optimizer can legitimately treat every entry of \(G\) as one scalar coordinate.

But the same matrix also has row directions, column directions, singular vectors, singular values, rank, and aspect ratio.

Matrix-aware optimization asks whether that structure should shape the update.

The claim is not that matrix-aware methods are automatically better.

The claim is that they define a different local geometry.

## 2. Three ways to change a matrix gradient

An elementwise rule may rescale entries separately.

A row/column-aware rule may transform

\[
G\mapsto AGB.
\]

An orthogonalizing rule may preserve singular vectors while transforming singular values.

These operations can produce different updates from the same \(G\).

They should not share one name merely because each is called “preconditioning” informally.

## 3. Left and right multiplication

For compatible \(A,G,B\),

\[
\operatorname{vec}(AGB)
=
(B^\top\otimes A)\operatorname{vec}(G).
\]

So a left-right matrix transform is a structured operator on the vectorized gradient.

It can couple coordinates across rows and columns.

That is richer than independent scalar scaling.

It is still not automatically a full Hessian or Fisher inverse. A structured preconditioner and exact curvature are distinct unless a separate result identifies them.

## 4. Shampoo: accumulated matrix geometry

Shampoo was introduced as a preconditioned stochastic tensor optimization method [@GuptaKorenSinger2018Shampoo].

For a matrix gradient sequence, its structure can be seen through accumulated left and right statistics:

\[
L_t=\sum_{s\le t}G_sG_s^\top,
\]

\[
R_t=\sum_{s\le t}G_s^\top G_s.
\]

A representative damped matrix update is

\[
P_t
=
(L_t+\varepsilon I)^{-1/4}
G_t
(R_t+\varepsilon I)^{-1/4}.
\]

This remembers row-space and column-space gradient correlations and applies matrix inverse roots rather than only coordinatewise division.

But it deliberately uses structured factors. It is not, by definition, an arbitrary dense full-curvature inverse over every scalar parameter.

The convergence and empirical statements in the original paper remain scoped to that paper's assumptions and experiments.

## 5. Rectangular matrices change the algebra

Take a tall matrix

\[
G\in\mathbb R^{m\times n},
\qquad m>n.
\]

Even if \(G\) has full column rank,

\[
\operatorname{rank}(G)=n,
\]

the left Gram matrix obeys

\[
\operatorname{rank}(GG^\top)=n<m.
\]

Thus \(GG^\top\) is singular.

Nothing is defective. The gradient's column space simply occupies only an \(n\)-dimensional subspace of \(\mathbb R^m\).

This is why square inverse formulas cannot be transferred mechanically to rectangular blocks.

Damping, accumulated history, pseudoinverse conventions, or support-restricted inverse powers change the actual method.

## 6. The polar factor

Let \(r=\operatorname{rank}(G)\), and take a compact SVD retaining only the \(r\) strictly positive singular values:

\[
G=U_r\Sigma_rV_r^\top.
\]

The support-restricted polar factor is

\[
Q=U_rV_r^\top.
\]

For \(G=0\), set \(Q=0\). For full-column-rank tall \(G\), this agrees with the usual \(UV^\top\).

For a tall full-column-rank matrix,

\[
Q^\top Q=I_n.
\]

But generally

\[
QQ^\top\ne I_m.
\]

In the full-column-rank case, the columns are orthonormal; the rows cannot all be orthonormal because there are more rows than columns. If \(G\) has rank \(r<n\), instead \(Q^\top Q=V_rV_r^\top\), a rank-\(r\) projector.

For a wide full-row-rank matrix, the roles reverse.

This is semi-orthogonality.

Higham's classical treatment supplies the numerical-analysis setting for polar decomposition and its computation [@Higham1986Polar].

## 7. Polar orthogonalization is singular-value flattening

Using the compact rank-\(r\) SVD, the polar factor is

\[
Q=U_rI_rV_r^\top.
\]

Every nonzero singular value is replaced by \(1\).

The nonzero singular subspaces remain; zero singular directions remain zero. For example, \(G=\operatorname{diag}(1,0)\) has compact polar factor \(Q=\operatorname{diag}(1,0)\), not \(I_2\).

That is exact singular-value flattening on the nonzero support.

It is a strong and specific spectral transformation.

It does not by itself prove improved conditioning, training stability, convergence, or generalization for a learning problem.

## 8. “Steepest” depends on the norm

Locally,

\[
f(W+\Delta)
\approx
f(W)+\langle G,\Delta\rangle_F.
\]

For \(G\ne0\) and \(\rho>0\), if equally large moves are defined by

\[
\|\Delta\|_F\le\rho,
\]

then a steepest direction is

\[
\Delta_F^\star
=
-\rho\frac{G}{\|G\|_F}.
\]

If equally large moves are instead defined by

\[
\|\Delta\|_2\le\rho,
\]

then one steepest direction is

\[
\Delta_2^\star
=
-\rho U_rV_r^\top.
\]

If \(G=0\), the linearized objective is constant on both norm balls; every feasible displacement minimizes it, and choosing \(\Delta=0\) is valid. In particular, do not divide by \(\|G\|_F=0\).

The polar factor therefore appears naturally as a spectral-norm steepest direction for nonzero \(G\). Bernstein and Newhouse develop this norm-dependent optimizer viewpoint [@BernsteinNewhouse2024OldOptimizer].

The two directions do not contradict one another. They minimize the same linear functional over different feasible sets.

## 9. Why their local decreases are not optimizer scores

For the Frobenius ball,

\[
\min_{\|\Delta\|_F\le\rho}
\langle G,\Delta\rangle_F
=
-\rho\|G\|_F.
\]

For the spectral ball,

\[
\min_{\|\Delta\|_2\le\rho}
\langle G,\Delta\rangle_F
=
-\rho\|G\|_*.
\]

A larger magnitude in the second expression does not prove a better optimizer. The constraint defining an equally large step has changed.

The norm is part of the optimization problem.

## 10. A one-step inverse-root identity

On the nonzero singular support,

\[
(GG^\top)^{-1/4}
G
(G^\top G)^{-1/4}
=
UV^\top.
\]

This explains an algebraic meeting point between a two-sided inverse-root transform and the polar factor.

But two warnings are essential.

First, a rectangular Gram matrix on the larger side is singular, so a full-space inverse needs damping or another declared convention.

Second, Shampoo is stateful. Its \(L_t\) and \(R_t\) accumulate earlier gradients.

The identity does not say that stateful Shampoo is “take the polar factor of the current gradient.”

## 11. Muon adds state and numerical approximation

Muon is a concrete optimizer design for matrix-shaped hidden-layer parameters [@JordanEtAl2024Muon].

At a high level, it combines momentum with a finite Newton-Schulz-like matrix iteration intended to produce an approximately orthogonalized update.

The momentum state means the transformed matrix is not simply the raw current gradient.

And a finite polynomial iteration is not the exact SVD or polar decomposition.

A finite iteration implements a finite singular-value map.

The exact numerical realization therefore matters.

## 12. Exact versus approximate matrix functions

Exact expressions such as

\[
(G^\top G)^{-1/2}
\]

define mathematical targets.

Large-scale optimizers may realize related transforms through eigendecomposition, iterative matrix roots, Newton-Schulz iterations, low-precision polynomials, blocking, distribution, or delayed refresh.

The realized update can differ from the exact target.

An optimizer is therefore not specified by the ideal matrix function alone. Its state, damping, numerical method, precision, and refresh schedule are also part of the algorithm.

## 13. The exact \(3\times2\) witness

Take

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

so the singular values are

\[
\sqrt5,\ 1.
\]

The left Gram matrix is

\[
GG^\top
=
\begin{pmatrix}
4&0&2\\
0&1&0\\
2&0&1
\end{pmatrix}.
\]

It has rank \(2\), not \(3\).

The right one-step statistic is invertible while the left one is singular.

The aspect ratio is already visible in the algebra.

## 14. Polarizing the witness

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
Q^\top Q=I_2.
\]

But

\[
QQ^\top
=
\begin{pmatrix}
4/5&0&2/5\\
0&1&0\\
2/5&0&1/5
\end{pmatrix},
\]

which is a rank-two projector rather than \(I_3\).

The witness is deliberately rectangular so “orthogonalized” cannot silently mean “square orthogonal.”

## 15. A diagonal control

Apply

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
\end{pmatrix}.
\]

Its singular values are

\[
\sqrt5/2,\ 1.
\]

The original singular-value ratio was \(\sqrt5\). The diagonal control changes it to \(\sqrt5/2\). The polar factor makes it \(1\).

Both operations reshape the spectrum, but they do so differently.

This control is generic. It is not presented as the exact rule used by Adam or another named elementwise optimizer.

## 16. Flattening is not the whole spectral story

The polar factor gives the simplest possible nonzero singular spectrum:

\[
1,1,\ldots,1.
\]

But an optimizer might instead want to suppress only large modes, temper near-zero modes, preserve relative scale over a band, or impose another target spectrum.

Those questions belong to ATLAS-CH-SPECTRALSHAPE-001.

This chapter supplies the boundary:

\[
\boxed{
\text{singular-value flattening}
\neq
\text{arbitrary intentional spectral shaping}.
}
\]

## 17. Matrix-aware does not mean manifold-constrained

An optimizer can choose a semi-orthogonal update \(Q_t\) while leaving the parameter \(W_t\) unconstrained:

\[
W_{t+1}=W_t-\eta Q_t.
\]

Even if

\[
Q_t^\top Q_t=I,
\]

there is no general implication that

\[
W_{t+1}^\top W_{t+1}=I.
\]

Manifold optimization instead declares a parameter constraint and uses tangent/retraction machinery to maintain it.

Orthogonalized updates and orthogonality-constrained parameters are different objects.

## 18. Matrix-aware does not mean full second order

A matrix preconditioner can encode more structure than an elementwise rule without becoming an exact Newton method.

A full Hessian for a matrix block acts on the vectorized parameter space and may couple every scalar coordinate.

Left-right factors impose a structured form.

That structure may be computationally attractive. It is still only the structure actually specified.

The Atlas therefore keeps separate:

- matrix-aware preconditioning;
- second-order curvature;
- hard manifold constraints.

## 19. Optimizer state is part of the trajectory

An instantaneous map

\[
G_t\mapsto T(G_t)
\]

does not describe a stateful optimizer.

A stateful optimizer has a law such as

\[
S_t=\Phi(S_{t-1},G_t),
\]

\[
\Delta_t=\Psi(S_t,G_t).
\]

Shampoo's accumulated factors and Muon's momentum make this explicit.

Two methods can share a similar instantaneous transform and still produce different trajectories because their states differ.

## 20. What this chapter establishes

The chapter establishes a controlled vocabulary and exact finite algebra for matrix-aware updates.

It supports these claims:

- rectangular geometry matters;
- left and right Gram matrices encode different sides of a matrix block;
- a rectangular polar factor is semi-orthogonal;
- polar orthogonalization flattens nonzero singular values;
- norm choice changes the steepest direction;
- a support-restricted one-step inverse-root transform meets the polar factor algebraically;
- state, damping, and numerical realization prevent that identity from collapsing named optimizers into one another.

It does not establish that one update geometry is universally best.

## 21. Failure boundaries

Keep these separations intact:

\[
\text{elementwise scaling}
\neq
\text{matrix preconditioning},
\]

\[
\text{matrix preconditioning}
\neq
\text{full Hessian inversion},
\]

\[
\text{one-step inverse-root identity}
\neq
\text{stateful Shampoo equivalence},
\]

\[
\text{exact polar factor}
\neq
\text{finite Newton-Schulz realization},
\]

\[
\text{orthogonalized update}
\neq
\text{orthogonality-constrained parameter},
\]

\[
\text{singular-value flattening}
\neq
\text{all spectral shaping},
\]

and

\[
\text{instantaneous transform}
\neq
\text{stateful optimizer dynamics}.
\]

## References used in this chapter

- Shampoo: Gupta, Koren, and Singer [@GuptaKorenSinger2018Shampoo].
- Polar decomposition and numerical computation: Higham [@Higham1986Polar].
- Norm-dependent steepest-descent interpretation: Bernstein and Newhouse [@BernsteinNewhouse2024OldOptimizer].
- Muon design and finite Newton-Schulz update construction: Jordan et al. [@JordanEtAl2024Muon].
- Audited Atlas prerequisites: ATLAS-CH-LINALG-001 and ATLAS-CH-SECOND-001.

Exact bibliographic authority, prerequisite blob identities, and claim boundaries are recorded in:

sources/source-locks/ATLAS-CH-MATRIXOPT-001.yaml
