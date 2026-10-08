# ATLAS-CH-MATRIXOPT-001 — Derivation Packet

## Scope

This packet derives the finite-dimensional identities used by **Matrix-Aware Optimization**.

It does not prove empirical superiority of Shampoo, Muon, polar updates, or any other optimizer.

Source boundary:

`sources/source-locks/ATLAS-CH-MATRIXOPT-001.yaml`.

## 1. Matrix gradient as a linear functional

Let \(W\in\mathbb R^{m\times n}\) and \(G=\nabla_W f(W)\).

For small \(\Delta\),

\[
f(W+\Delta)
=
f(W)+\langle G,\Delta\rangle_F+o(\|\Delta\|_F),
\]

where

\[
\langle A,B\rangle_F=\operatorname{tr}(A^\top B).
\]

The local first-order problem is therefore determined by both \(G\) and the admissible set for \(\Delta\).

## 2. SVD bookkeeping

Let

\[
G=U\Sigma V^\top
\]

be a reduced SVD of rank \(r\).

Then

\[
G^\top G=V\Sigma^2V^\top,
\]

and on the nonzero singular subspace,

\[
GG^\top=U\Sigma^2U^\top.
\]

The nonzero eigenvalues of the two Gram matrices are the same:

\[
\sigma_1^2,\ldots,\sigma_r^2.
\]

If an ambient dimension exceeds \(r\), the corresponding Gram matrix has a nullspace.

## 3. Left-right transformation

For compatible \(A,G,B\),

\[
\operatorname{vec}(AGB)
=
(B^\top\otimes A)\operatorname{vec}(G).
\]

Thus \(G\mapsto AGB\) is a Kronecker-structured operator on the vectorized gradient.

This identity does not imply that the structured operator equals a Hessian.

## 4. Matrix Shampoo specialization

For an order-two tensor, define

\[
L_t=\sum_{s\le t}G_sG_s^\top,
\qquad
R_t=\sum_{s\le t}G_s^\top G_s.
\]

A damped matrix Shampoo direction has the form

\[
P_t
=
(L_t+\varepsilon I_m)^{-1/4}
G_t
(R_t+\varepsilon I_n)^{-1/4}.
\]

The two inverse fourth roots produce a structured inverse-root action on vectorized coordinates. The accumulated factors are gradient statistics, not an exact Hessian without a separate theorem.

## 5. Rectangular rank obstruction

At one step,

\[
L=GG^\top,
\qquad
R=G^\top G.
\]

Because

\[
\operatorname{rank}(GG^\top)=\operatorname{rank}(G),
\]

if \(m>n\) and \(G\) has full column rank \(n\), then

\[
\operatorname{rank}(GG^\top)=n<m.
\]

Therefore \(GG^\top\) is singular.

The wide case is symmetric.

## 6. Polar factor

Let \(r=\operatorname{rank}(G)\), and use a compact SVD with only positive singular values:

\[
G=U_r\Sigma_rV_r^\top.
\]

Define the support-restricted polar factor

\[
Q=U_rV_r^\top,
\]

with \(Q=0\) if \(G=0\). In the full-column-rank case \(m\ge n=r\), write \(U=U_r,\Sigma=\Sigma_r,V=V_r\). Then

\[
G^\top G=V\Sigma^2V^\top,
\]

so

\[
(G^\top G)^{-1/2}=V\Sigma^{-1}V^\top,
\]

and

\[
G(G^\top G)^{-1/2}=UV^\top=Q.
\]

Moreover,

\[
Q^\top Q=I_n.
\]

For a full-column-rank tall matrix,

\[
QQ^\top=UU^\top,
\]

the projector onto the column space of \(G\), not \(I_m\). For rank-deficient \(G\), the support-restricted factor instead satisfies \(Q^\top Q=V_rV_r^\top\) and \(QQ^\top=U_rU_r^\top\).

## 7. Polar flattening

Because

\[
Q=U_rI_rV_r^\top,
\]

all nonzero singular values of \(Q\) equal \(1\), while null directions remain zero. For \(G=\operatorname{diag}(1,0)\), its compact polar factor is \(\operatorname{diag}(1,0)\), not \(I_2\).

The map removes magnitude information on the nonzero singular support encoded by \(\Sigma_r\), while retaining the corresponding singular subspaces.

## 8. One-step inverse-root support identity

On the nonzero singular support, write \(U=U_r,V=V_r,\Sigma=\Sigma_r\), and interpret inverse powers as support-restricted matrix powers:

\[
(GG^\top)^{-1/4}
=
U\Sigma^{-1/2}U^\top,
\]

and

\[
(G^\top G)^{-1/4}
=
V\Sigma^{-1/2}V^\top.
\]

Hence

\[
(GG^\top)^{-1/4}
G
(G^\top G)^{-1/4}
=
UV^\top.
\]

For a rectangular matrix, the larger-side Gram matrix has a nullspace, so this is a support-restricted identity.

With damping, the transform is defined on the full space but does not give exactly unit nonzero singular values at finite \(\varepsilon\).

## 9. Frobenius-ball steepest direction

Assume \(G\ne0\) and \(\rho>0\). Solve

\[
\min_{\|\Delta\|_F\le\rho}
\langle G,\Delta\rangle_F.
\]

Cauchy-Schwarz gives

\[
\langle G,\Delta\rangle_F
\ge
-\|G\|_F\|\Delta\|_F
\ge
-\rho\|G\|_F.
\]

Equality is attained by

\[
\Delta_F^\star
=
-\rho\frac{G}{\|G\|_F}.
\]

## 10. Spectral-ball steepest direction

Continue under \(G\ne0\) and \(\rho>0\). Solve

\[
\min_{\|\Delta\|_2\le\rho}
\langle G,\Delta\rangle_F.
\]

The dual norm of \(\|\cdot\|_2\) is the nuclear norm, so

\[
\langle G,\Delta\rangle_F
\ge
-\|G\|_*\|\Delta\|_2
\ge
-\rho\|G\|_*.
\]

Set

\[
\Delta=-\rho UV^\top.
\]

Because \(\|UV^\top\|_2=1\),

\[
\langle G,\Delta\rangle_F
=
-\rho\operatorname{tr}(\Sigma)
=
-\rho\|G\|_*.
\]

Therefore

\[
\Delta_2^\star=-\rho UV^\top
\]

is a spectral-ball steepest direction.

For \(G=0\), every point in either norm ball minimizes the zero linear functional; \(\Delta=0\) is one valid choice. The Frobenius formula above must not divide by \(\|G\|_F=0\).

The Frobenius- and spectral-ball decreases are not directly comparable optimizer scores because the feasible sets differ.

## 11. Exact rectangular witness

Take

\[
G=
\begin{pmatrix}
2&0\\
0&1\\
1&0
\end{pmatrix}.
\]

The columns are orthogonal with norms \(\sqrt5\) and \(1\). Thus a reduced SVD is

\[
U=
\begin{pmatrix}
2/\sqrt5&0\\
0&1\\
1/\sqrt5&0
\end{pmatrix},
\qquad
\Sigma=
\begin{pmatrix}
\sqrt5&0\\
0&1
\end{pmatrix},
\qquad
V=I_2.
\]

Direct multiplication gives

\[
G^\top G=
\begin{pmatrix}
5&0\\
0&1
\end{pmatrix},
\]

and

\[
GG^\top=
\begin{pmatrix}
4&0&2\\
0&1&0\\
2&0&1
\end{pmatrix}.
\]

The first and third rows are dependent, so \(\operatorname{rank}(GG^\top)=2\) and its determinant is zero.

## 12. Exact polar witness

The polar factor is

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

while

\[
QQ^\top
=
\begin{pmatrix}
4/5&0&2/5\\
0&1&0\\
2/5&0&1/5
\end{pmatrix}.
\]

The latter is a rank-two orthogonal projector, not \(I_3\).

## 13. Norms of the witness

From the singular values,

\[
\|G\|_2=\sqrt5,
\qquad
\|G\|_F=\sqrt6,
\qquad
\|G\|_*=\sqrt5+1.
\]

At radius \(1\),

\[
\Delta_F^\star=-G/\sqrt6,
\]

and

\[
\Delta_2^\star=-Q.
\]

## 14. Diagonal scaling control

Let

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

Its columns are orthogonal with norms \(\sqrt5/2\) and \(1\). Therefore

\[
\sigma(DG)=\{\sqrt5/2,1\}.
\]

The original singular-value ratio is \(\sqrt5\), the diagonal-control ratio is \(\sqrt5/2\), and the polar-factor ratio is \(1\).

This compares transformations, not optimizer quality.

## 15. Finite Newton-Schulz boundary

A finite polynomial matrix iteration induces a finite polynomial map on singular values under the usual aligned singular-vector analysis:

\[
\sigma\mapsto p_k(\sigma).
\]

A finite number of steps is therefore an approximation to the polar/sign target, not the exact target in general.

The exact polynomial and scaling convention belong to the implementation being analyzed.

## 16. Orthogonalized update is not parameter constraint

Suppose an unconstrained parameter uses

\[
W_{t+1}=W_t-\eta Q_t
\]

with \(Q_t^\top Q_t=I\).

There is no general implication that

\[
W_{t+1}^\top W_{t+1}=I.
\]

Therefore update orthogonalization does not put the parameter on a Stiefel manifold.

## 17. Downstream boundary

ATLAS-CH-SPECTRALSHAPE-001 may inherit:

- SVD bookkeeping;
- exact polar flattening;
- rectangular semi-orthogonality;
- norm-dependent steepest directions;
- exact-versus-approximate singular-value transforms.

It must independently justify any non-flat target spectrum or claimed benefit.

## Claim boundary

This derivation packet establishes the displayed finite-dimensional matrix identities and exact properties of the declared witness.

It does not establish universal convergence, generalization, stability, or empirical superiority for any optimizer.
