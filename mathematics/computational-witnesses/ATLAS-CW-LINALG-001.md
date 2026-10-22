# ATLAS-CW-LINALG-001 — Linear Algebra Witness

**Chapter:** `ATLAS-CH-LINALG-001`  
**Runtime:** Wolfram Language service, 2026-10-02

## Purpose

Check the exact distinction among eigenvalues, singular values, projection structure, low-rank approximation error, and conditioning.

## Witness A — non-normal matrix

\[
A=
\begin{pmatrix}
1&1\\
0&1
\end{pmatrix}.
\]

Wolfram returns eigenvalues

\[
\{1,1\},
\]

but singular values

\[
\left\{
\frac{1+\sqrt{5}}{2},
\frac{\sqrt{5}-1}{2}
\right\}.
\]

Thus equal eigenvalue moduli do not determine one-step Euclidean amplification.

The best rank-one approximation error in induced \(2\)-norm is

\[
\sigma_2(A)
=
\frac{\sqrt{5}-1}{2}.
\]

## Witness B — orthogonal projection

For

\[
P=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix},
\]

Wolfram returns

\[
P^2=P.
\]

## Witness C — conditioning

For

\[
D=
\begin{pmatrix}
1&0\\
0&1/100
\end{pmatrix},
\]

the singular values are

\[
1,\quad 1/100,
\]

hence

\[
\kappa_2(D)=100.
\]

## Original replay expression

```wolfram
aa={{1,1},{0,1}};
sv=SingularValueList[aa];
pp={{1,0},{0,0}};
dd={{1,0},{0,1/100}};
{Eigenvalues[aa],FullSimplify[sv],pp.pp==pp,
 SingularValueList[dd],
 FullSimplify[Max[SingularValueList[dd]]/Min[SingularValueList[dd]]],
 FullSimplify[Last[sv]]}
```

## Claim boundary

This witness checks exact finite-dimensional identities and one conditioning example. It does not establish claims about optimization dynamics, model training, or empirical representation geometry.

## Witness D — minimum-norm least squares under rank deficiency

With $A_0=\operatorname{diag}(1,0)$ and $b_0=(2,3)^\top$, the entire
minimizer set is $\{(2,t)^\top:t\in\mathbb R\}$ because

$$
\|A_0x-b_0\|_2^2=(x_1-2)^2+9.
$$

The pseudoinverse chooses $A_0^+b_0=(2,0)^\top$, giving residual norm
$3$ and zero null-space component. This was missing from the earlier
three-case replay despite the acceptance specification explicitly
requiring a pseudoinverse least-squares witness.

## Witness E — real normal need not mean real eigenvectors

For $R=\begin{psmallmatrix}0&-1\\1&0\end{psmallmatrix}$,
$R^\top R=RR^\top=I$ and
$\det(\lambda I-R)=\lambda^2+1$. Its eigenvalues are $\pm i$;
there is no nonzero real eigenvector. Complex unitary diagonalization
is still valid.

## Extended exact replay

The following self-contained Wolfram expressions add both obligations:

```wolfram
a0={{1,0},{0,0}};
b0={2,3};
x0=PseudoInverse[a0].b0;
r0=a0.x0-b0;
rot={{0,-1},{1,0}};
{
 x0, r0, r0.r0,
 FullSimplify[(a0.{2,t}-b0).(a0.{2,t}-b0)],
 Transpose[rot].rot==rot.Transpose[rot],
 Eigenvalues[rot]
}
(* Expected: {{2,0},{0,-3},9,9,True,{-I,I}} up to order *)
```

These finite identities do not certify any nonlinear-system property.
