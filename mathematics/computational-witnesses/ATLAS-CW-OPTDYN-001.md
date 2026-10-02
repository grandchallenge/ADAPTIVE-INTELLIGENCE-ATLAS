# ATLAS-CW-OPTDYN-001 — Optimizer-State Dynamics Witness

**Chapter:** \`ATLAS-CH-OPTDYN-001\`  
**System:** Wolfram Language 15.0.1 for Linux x86 (64-bit), July 2 2026  
**System ID:** Linux-x86-64  
**Norm:** spectral/operator \(2\)-norm  
**Figure source:** \`figures/wolfram/ATLAS-FIG-OPTDYN-001.wl\`

## Purpose

Exhibit a stable momentum recurrence whose augmented optimizer-state Jacobian is non-normal and displays finite-horizon amplification.

## Quadratic and optimizer

\[
L(\theta)=\frac12\theta^2,
\qquad
\eta=\frac1{10},
\qquad
\beta=\frac9{10}.
\]

With state

\[
z=
\begin{pmatrix}
\theta\\
v
\end{pmatrix},
\]

the recurrence is

\[
z_{t+1}=Jz_t,
\]

where

\[
J=
\begin{pmatrix}
\frac9{10}&-\frac9{100}\\
1&\frac9{10}
\end{pmatrix}.
\]

## Eigenvalue check

Wolfram returns

\[
\lambda_\pm
=
\frac9{10}\pm\frac3{10}i.
\]

Hence

\[
|\lambda_\pm|
=
\sqrt{\frac9{10}}
\approx0.9486832980505138<1.
\]

The linear recurrence is asymptotically stable.

## Non-normality check

\[
J^\top J
=
\begin{pmatrix}
\frac{181}{100}&\frac{819}{1000}\\
\frac{819}{1000}&\frac{8181}{10000}
\end{pmatrix},
\]

while

\[
JJ^\top
=
\begin{pmatrix}
\frac{8181}{10000}&\frac{819}{1000}\\
\frac{819}{1000}&\frac{181}{100}
\end{pmatrix}.
\]

Therefore \(J\) is non-normal.

## Finite-horizon check

Wolfram evaluates

\[
\|J^4\|_2
=
2.610090585959495\ldots
\]

and a sweep over \(n=0,\ldots,20\) finds the peak in that interval at

\[
n=4.
\]

The exact fourth power is

\[
J^4
=
\begin{pmatrix}
\frac{567}{2500}&-\frac{729}{3125}\\
\frac{324}{125}&\frac{567}{2500}
\end{pmatrix}.
\]

Thus asymptotic spectral stability coexists with substantial short-horizon gain.

## Rendered witness

\`figures/masters/ATLAS-FIG-OPTDYN-001.png\`

Committed PNG Git blob:

\`fa8e5231cb6451c026a0ccd7beecdfcff330c98d\`.

## Claim boundary

The witness establishes the mechanism for one exact scalar-quadratic momentum system. It does not establish that a real neural-training trajectory follows a constant Jacobian, that every observed loss spike is caused by non-normal optimizer-state amplification, or that the toy parameters are representative of frontier training.
