# ATLAS-CH-NONNORMAL-001 — Derivation Packet

**Status:** first-pass derivations  
**Norm convention:** spectral/operator \(2\)-norm unless explicitly stated  
**Source lock:** \`sources/source-locks/ATLAS-CH-NONNORMAL-001.yaml\`

## D1. Exact powers of the Jordan-like matrix

Consider

\[
A=
\begin{pmatrix}
a&K\\
0&a
\end{pmatrix}
=
aI+KN,
\]

with

\[
N=
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix},
\qquad
N^2=0.
\]

For integer \(n\ge1\),

\[
A^n
=
(aI+KN)^n.
\]

Because every term with \(N^j\), \(j\ge2\), vanishes,

\[
A^n
=
a^nI
+
n a^{n-1}KN.
\]

Hence

\[
\boxed{
A^n
=
\begin{pmatrix}
a^n&nKa^{n-1}\\
0&a^n
\end{pmatrix}.
}
\]

The only eigenvalue is \(a\), with algebraic multiplicity two, so

\[
\rho(A)=|a|.
\]

If \(|a|<1\), then \(A^n\to0\), although the off-diagonal term can first grow.

## D2. Exact spectral norm of the power

Write

\[
B=
\begin{pmatrix}
p&q\\
0&p
\end{pmatrix}.
\]

Then

\[
B^\top B
=
\begin{pmatrix}
p^2&pq\\
pq&p^2+q^2
\end{pmatrix}.
\]

The eigenvalues of \(B^\top B\) are

\[
\lambda_\pm
=
\frac{
2p^2+q^2
\pm
|q|\sqrt{4p^2+q^2}
}{2}.
\]

Therefore

\[
\boxed{
\|B\|_2
=
\sqrt{
\frac{
2p^2+q^2
+
|q|\sqrt{4p^2+q^2}
}{2}
}.
}
\]

For \(A^n\),

\[
p=a^n,
\qquad
q=nKa^{n-1}.
\]

This gives an exact formula for finite-horizon amplification.

## D3. Concrete Atlas witness

Set

\[
a=\frac45,
\qquad
K=4.
\]

Then

\[
A=
\begin{pmatrix}
4/5&4\\
0&4/5
\end{pmatrix},
\]

and the matched normal matrix is

\[
N_0=\frac45I.
\]

Both have the eigenvalue \(4/5\) with multiplicity two.

For the normal matrix,

\[
\|N_0^n\|_2
=
\left(\frac45\right)^n.
\]

Wolfram evaluation over \(n=0,\ldots,40\) gives

\[
\boxed{
\max_{0\le n\le40}
\|A^n\|_2
=
8.2124290544\ldots
\quad
\text{at }n=4.
}
\]

This does not contradict asymptotic stability; \(A^n\to0\).

## D4. Exact singular values of \(zI-A\)

Let

\[
z-a=\delta,
\qquad
r=|\delta|.
\]

Then

\[
zI-A
=
\begin{pmatrix}
\delta&-K\\
0&\delta
\end{pmatrix}.
\]

Its squared singular values depend only on \(r\):

\[
\boxed{
\sigma_\pm^2
=
\frac{
2r^2+K^2
\pm
K\sqrt{K^2+4r^2}
}{2},
\qquad
K>0.
}
\]

## D5. Exact \(2\)-norm \(\varepsilon\)-pseudospectrum

Use the closed convention

\[
\Lambda_\varepsilon(A)
=
\{z:\sigma_{\min}(zI-A)\le\varepsilon\}.
\]

On the boundary,

\[
\sigma_{\min}=\varepsilon.
\]

Because

\[
\sigma_{\max}\sigma_{\min}
=
|\det(zI-A)|
=
r^2,
\]

we have

\[
\sigma_{\max}
=
\frac{r^2}{\varepsilon}.
\]

Also,

\[
\sigma_{\max}^2+\sigma_{\min}^2
=
2r^2+K^2.
\]

Substitution gives

\[
\frac{r^4}{\varepsilon^2}
+
\varepsilon^2
=
2r^2+K^2.
\]

Multiplying by \(\varepsilon^2\),

\[
r^4-2\varepsilon^2r^2+\varepsilon^4-K^2\varepsilon^2=0.
\]

Therefore

\[
(r^2-\varepsilon^2)^2
=
K^2\varepsilon^2.
\]

The relevant boundary branch is

\[
\boxed{
r^2
=
\varepsilon(\varepsilon+K).
}
\]

Hence

\[
\boxed{
\Lambda_\varepsilon(A)
=
\left\{
z:
|z-a|
\le
\sqrt{\varepsilon(\varepsilon+K)}
\right\}.
}
\]

For \(N_0=aI\),

\[
\boxed{
\Lambda_\varepsilon(N_0)
=
\{z:|z-a|\le\varepsilon\}.
}
\]

## D6. Resolvent form

Outside the spectrum,

\[
\|(zI-A)^{-1}\|_2
=
\frac1{\sigma_{\min}(zI-A)}.
\]

Therefore the same closed pseudospectrum can be written

\[
\Lambda_\varepsilon(A)
=
\sigma(A)
\cup
\left\{
z:
\|(zI-A)^{-1}\|_2\ge\varepsilon^{-1}
\right\}.
\]

In finite dimensions it is also equivalent to the perturbation characterization:

\[
z\in\Lambda_\varepsilon(A)
\]

if and only if

\[
z\in\sigma(A+E)
\]

for some \(E\) with

\[
\|E\|_2\le\varepsilon.
\]

The equivalence is standard pseudospectral theory and is source-backed by the chapter references.

## D7. Small-\(\varepsilon\) scale separation

For the Jordan-like matrix,

\[
r_{\rm nonnormal}
=
\sqrt{\varepsilon(\varepsilon+K)}.
\]

For small \(\varepsilon\),

\[
r_{\rm nonnormal}
\sim
\sqrt{K\varepsilon}.
\]

For the normal comparison,

\[
r_{\rm normal}=\varepsilon.
\]

Thus the ratio is approximately

\[
\frac{r_{\rm nonnormal}}{r_{\rm normal}}
\sim
\sqrt{\frac{K}{\varepsilon}},
\]

which can become large as \(\varepsilon\to0\).

## Claim boundary

This packet proves the exact formulas for one \(2\times2\) family and records standard finite-dimensional pseudospectral equivalences. It does not claim that every non-normal matrix exhibits large transient growth, nor that broad pseudospectra alone explain any observed neural-training instability.
