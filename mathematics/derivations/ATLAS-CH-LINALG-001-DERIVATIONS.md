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
