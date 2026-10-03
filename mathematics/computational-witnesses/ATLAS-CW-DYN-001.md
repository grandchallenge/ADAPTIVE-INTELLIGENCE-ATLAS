# ATLAS-CW-DYN-001 — Dynamics Witness

**Chapter:** \`ATLAS-CH-DYN-001\`  
**Runtime:** Wolfram Language service, 2026-10-03

## Purpose

Replay exact symbolic facts used by the chapter:

- scalar exponential stability;
- Lyapunov derivative;
- saddle-node equilibria;
- pitchfork equilibria;
- harmonic-oscillator exact flow;
- symplectic identity;
- energy conservation.

## Stable scalar flow

For

\[
\dot x=-2x,
\qquad
x(0)=3,
\]

Wolfram returns

\[
x(t)=3e^{-2t}.
\]

For

\[
V(x)=\frac12x^2,
\]

the orbital derivative is

\[
\dot V=-2x^2.
\]

## Saddle-node

For

\[
\dot x=\mu-x^2,
\]

Wolfram solves

\[
\mu-x^2=0
\]

as

\[
x=\pm\sqrt{\mu},
\]

with derivative

\[
f'(x)=-2x.
\]

## Pitchfork

For

\[
\dot x=\mu x-x^3,
\]

Wolfram returns equilibria

\[
x=0,
\qquad
x=\pm\sqrt{\mu},
\]

with derivative

\[
f'(x)=\mu-3x^2.
\]

The real nonzero branches are interpreted only for \(\mu>0\).

## Harmonic oscillator

For

\[
A=
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix},
\]

Wolfram returns

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
J=
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix},
\]

it verifies

\[
M(t)^\top J M(t)-J
=
\begin{pmatrix}
0&0\\
0&0
\end{pmatrix}.
\]

For

\[
H(q,p)=\frac12(q^2+p^2),
\]

it also verifies

\[
H(M(t)z)-H(z)=0.
\]

## Replay expression

\`\`\`wolfram
A={{0,1},{-1,0}};
J={{0,1},{-1,0}};
M=MatrixExp[A t];

fSN[x_]:=mu-x^2;
fPF[x_]:=mu x-x^3;
H[z_]:=(z[[1]]^2+z[[2]]^2)/2;
z={q,p};

{
 DSolveValue[
   {xx'[tt]==-2 xx[tt],xx[0]==3},
   xx[tt],
   tt
 ],
 FullSimplify[D[x^2/2,x](-2x)],
 Solve[mu-x^2==0,x],
 D[mu-x^2,x],
 Solve[mu x-x^3==0,x],
 D[mu x-x^3,x],
 FullSimplify[M],
 FullSimplify[Transpose[M].J.M-J],
 FullSimplify[H[M.z]-H[z]]
}
\`\`\`

Expected exact objects include:

\[
3e^{-2t},
\]

\[
-2x^2,
\]

\[
x=\pm\sqrt{\mu},
\]

\[
x=0,\pm\sqrt{\mu},
\]

the rotation matrix \(M(t)\), the zero symplectic defect matrix, and zero energy difference.

## Claim boundary

This witness checks declared deterministic examples only.

It does not establish global stability of arbitrary nonlinear systems, the general Hopf theorem, or structure preservation by any numerical integrator.
