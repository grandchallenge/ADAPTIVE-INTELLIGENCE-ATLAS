# ATLAS-CW-DYN-001 — Dynamics Witness

**Chapter:** \`ATLAS-CH-DYN-001\`  
**Runtime:** Wolfram Language service, 2026-10-02

## Purpose

Replay the exact calibration systems used in the chapter:

- pitchfork equilibria and branch stability;
- zero-linearization stability ambiguity;
- one Lyapunov derivative;
- harmonic-oscillator exact flow;
- energy conservation;
- symplectic preservation.

## Pitchfork

\[
f(x;\mu)
=
\mu x-x^3.
\]

The derivative is

\[
\frac{\partial f}{\partial x}
=
\mu-3x^2.
\]

At the origin:

\[
\lambda_0=\mu.
\]

For \(\mu>0\), the outer equilibria are

\[
x_\star=\pm\sqrt\mu,
\]

with

\[
\lambda_\pm=-2\mu.
\]

## Zero-linearization ambiguity

For

\[
\dot x=-x^3,
\]

and

\[
\dot x=x^3,
\]

the derivative at zero is

\[
0
\]

in both cases.

The first origin is asymptotically stable.

The second origin is unstable.

## Lyapunov witness

For

\[
V(x)=\frac12x^2,
\]

along

\[
\dot x=-x^3,
\]

\[
\dot V=-x^4.
\]

## Harmonic oscillator

Let

\[
A=
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix}.
\]

Wolfram gives

\[
e^{tA}
=
\begin{pmatrix}
\cos t&\sin t\\
-\sin t&\cos t
\end{pmatrix}.
\]

With

\[
J=A,
\]

the exact flow matrix \(M(t)\) satisfies

\[
M(t)^\top J M(t)-J=0.
\]

Also,

\[
\det M(t)=1.
\]

For

\[
H(q,p)=\frac12(q^2+p^2),
\]

Wolfram verifies

\[
H(M(t)(q,p))-H(q,p)=0.
\]

## Replay expression

\`\`\`wolfram
ClearAll[x,mu,t,q,p];
f=mu x-x^3;
df=D[f,x];

branches={
 {"origin",0,FullSimplify[df/.x->0]},
 {"plus",Sqrt[mu],
   FullSimplify[df/.x->Sqrt[mu],
    Assumptions->mu>0]},
 {"minus",-Sqrt[mu],
   FullSimplify[df/.x->-Sqrt[mu],
    Assumptions->mu>0]}
};

v=x^2/2;
vdotStable=
 FullSimplify[D[v,x] (-x^3)];

zeroStable=D[-x^3,x]/.x->0;
zeroUnstable=D[x^3,x]/.x->0;

jj={{0,1},{-1,0}};
mm=MatrixExp[jj t];
z={q,p};
zt=FullSimplify[mm.z];

symp=
 FullSimplify[
  Transpose[mm].jj.mm-jj
 ];

det=
 FullSimplify[Det[mm]];

energyResidual=
 FullSimplify[
  (zt[[1]]^2+zt[[2]]^2)/2
  -(q^2+p^2)/2
 ];

{df,branches,vdotStable,
 zeroStable,zeroUnstable,
 mm,symp,det,energyResidual}
\`\`\`

Expected exact results include:

\[
\lambda_0=\mu,
\qquad
\lambda_\pm=-2\mu,
\]

\[
\dot V=-x^4,
\]

\[
M^\top J M-J=0,
\]

\[
\det M=1,
\]

and zero energy residual.

## Claim boundary

This witness establishes the declared exact calibration systems only.

It does not establish stability or Hamiltonian structure for an arbitrary neural network, optimizer, or numerical discretization.
