# ATLAS-CW-NONNORMAL-001 — Non-normal Transient-Growth Witness

**Chapter:** \`ATLAS-CH-NONNORMAL-001\`  
**System:** Wolfram Language 15.0.1 for Linux x86 (64-bit), July 2 2026  
**System ID:** Linux-x86-64  
**Norm:** spectral/operator \(2\)-norm  
**Figure source:** \`figures/wolfram/ATLAS-FIG-PSPECTRUM-001.wl\`

## Matrices

\[
A=
\begin{pmatrix}
4/5&4\\
0&4/5
\end{pmatrix},
\qquad
N_0=\frac45I.
\]

Both matrices have the same eigenvalue \(4/5\), with multiplicity two.

## Exact power check

For integer \(n\ge1\),

\[
A^n
=
\begin{pmatrix}
(4/5)^n&
4n(4/5)^{n-1}\\
0&
(4/5)^n
\end{pmatrix}.
\]

## Singular-value check

For

\[
B=
\begin{pmatrix}
p&q\\
0&p
\end{pmatrix},
\]

Wolfram confirms squared singular values

\[
\frac{
2p^2+q^2
\pm
|q|\sqrt{4p^2+q^2}
}{2}.
\]

## Finite-horizon check

Over \(n=0,\ldots,40\),

\[
\max_n\|A^n\|_2
=
8.2124290544\ldots
\]

at

\[
n=4.
\]

By contrast,

\[
\|N_0^n\|_2
=
(4/5)^n.
\]

## Pseudospectral-boundary check

For

\[
r^2
=
\varepsilon(\varepsilon+K),
\]

Wolfram symbolically verifies that the exact smallest-singular-value expression satisfies

\[
\sigma_{\min}^2-\varepsilon^2=0.
\]

For \(K=4\), the non-normal boundary radius is

\[
\sqrt{\varepsilon(\varepsilon+4)},
\]

while the normal boundary radius is

\[
\varepsilon.
\]

## Rendered witness

\`figures/masters/ATLAS-FIG-PSPECTRUM-001.png\`

The active figure manifest records the displayed epsilon levels, parameters, and literal/nonliteral semantics.

## Claim boundary

The witness establishes exact finite-dimensional behavior for the stated matrices. It does not establish that non-normality is sufficient for large transient growth in general, nor that the same mechanism is responsible for a particular learning-system failure.
