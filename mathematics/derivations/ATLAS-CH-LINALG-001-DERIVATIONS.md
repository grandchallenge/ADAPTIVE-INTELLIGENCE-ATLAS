# ATLAS-CH-LINALG-001 — Derivation Packet

## D1. Matrix as linear-map representation

Given bases for finite-dimensional spaces, a linear map

\[
T:V\to W
\]

is represented by a matrix \(A\). A basis change changes the coordinate matrix but need not change the underlying map.

## D2. Orthogonal projection

If \(Q\in\mathbb R^{n\times k}\) has orthonormal columns,

\[
Q^\top Q=I,
\]

then

\[
P=QQ^\top
\]

satisfies

\[
P^2=P,
\qquad
P^\top=P.
\]

Hence \(P\) is the orthogonal projector onto \(\operatorname{col}(Q)\).

## D3. Singular-value decomposition

For

\[
A\in\mathbb R^{m\times n},
\]

the SVD is

\[
A=U\Sigma V^\top.
\]

The induced Euclidean operator norm is

\[
\|A\|_2=\sigma_{\max}(A).
\]

For the non-normal witness

\[
A=
\begin{pmatrix}
1&1\\
0&1
\end{pmatrix},
\]

the eigenvalues are both \(1\), while the singular values are

\[
\sigma_1=\frac{1+\sqrt{5}}{2},
\qquad
\sigma_2=\frac{\sqrt{5}-1}{2}.
\]

Thus eigenvalue magnitude and one-step Euclidean amplification answer different questions.

## D4. Low-rank approximation

For singular values

\[
\sigma_1\ge\cdots\ge\sigma_r>0,
\]

the best rank-\(k\) approximation in induced \(2\)-norm has error

\[
\sigma_{k+1}.
\]

For the witness matrix above, the best rank-one approximation error is

\[
\frac{\sqrt{5}-1}{2}.
\]

## D5. Conditioning

For nonsingular

\[
D=
\begin{pmatrix}
1&0\\
0&1/100
\end{pmatrix},
\]

\[
\kappa_2(D)
=
\frac{\sigma_{\max}(D)}{\sigma_{\min}(D)}
=
100.
\]

A relative perturbation aligned with the weak singular direction can therefore be amplified by a factor governed by this conditioning.

## D6. Pseudoinverse

For

\[
A=U\Sigma V^\top,
\]

the Moore-Penrose pseudoinverse is

\[
A^+=V\Sigma^+ U^\top,
\]

with nonzero singular values inverted.

For least squares,

\[
x_\star=A^+b
\]

is the minimum-norm least-squares solution when the standard finite-dimensional conditions apply.

## Claim boundary

This packet establishes standard finite-dimensional identities and one exact witness. It does not claim that spectral structure alone determines neural training behavior.

## D7. Basis covariance and a non-real normal spectrum

Let $S_V$ and $S_W$ be invertible coordinate transforms from a new
domain and codomain basis respectively to old coordinates. The new
matrix describing the **same** linear map is

$$
[T]_{\widetilde C\leftarrow\widetilde B}
=
S_W^{-1}[T]_{C\leftarrow B}S_V.
$$

Only an endomorphism described with the same change of basis in its
domain and codomain gives a similarity $S^{-1}AS$. A general two-sided
basis change need not preserve the matrix eigenvalues.

For $R=\begin{psmallmatrix}0&-1\\1&0\end{psmallmatrix}$,
$R^\top R=RR^\top=I$, yet its characteristic polynomial is
$\lambda^2+1$. The complex spectral theorem is applicable, but no
nonzero real eigenvector exists. This limits the loose claim that all
real normal matrices have a real orthonormal eigenbasis.

## D8. Rank-deficient least squares and pseudoinverse

With $A=\operatorname{diag}(1,0)$ and $b=(2,3)^\top$, the squared
residual is

$$
\|Ax-b\|_2^2=(x_1-2)^2+9.
$$

Every vector $(2,t)^\top$ minimizes the residual; the Moore--Penrose
solution $A^+b=(2,0)^\top$ is the unique **minimum norm** minimizer.
It leaves residual $(0,-3)^\top$, whose Euclidean norm is $3$.
This separates least-squares optimality, exact solvability, and
identifiability of the unconstrained null-space component.
