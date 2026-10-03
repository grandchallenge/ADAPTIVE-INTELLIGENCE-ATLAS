# ATLAS-CW-NUMERICS-001 — Numerics Witness

**Chapter:** \`ATLAS-CH-NUMERICS-001\`  
**Runtime:** Wolfram Language service, 2026-10-03

## Purpose

Replay exact symbolic facts used in the chapter:

- explicit and implicit Euler stability functions;
- stiff scalar amplification factors;
- a noncommuting split-system commutator;
- exact, Lie, and Strang Taylor expansions;
- Lie leading \(O(h^2)\) defect;
- Strang leading \(O(h^3)\) defect.

## Euler stability functions

For

\[
y'=\lambda y,
\qquad
z=h\lambda,
\]

explicit Euler has

\[
R_{\rm EE}(z)=1+z.
\]

Implicit Euler has

\[
R_{\rm IE}(z)=\frac{1}{1-z}.
\]

## Stiff scalar witness

For

\[
\lambda=-100,
\qquad
h=0.05,
\]

we have

\[
z=-5.
\]

Wolfram returns:

\[
R_{\rm EE}(-5)=-4,
\]

and

\[
R_{\rm IE}(-5)=\frac16.
\]

The exact factor is

\[
e^{-5}.
\]

Thus explicit Euler is unstable, while implicit Euler is stable but substantially inaccurate at this coarse step.

## Split matrices

Use

\[
A=
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix},
\]

\[
B=
\begin{pmatrix}
0&0\\
1&0
\end{pmatrix}.
\]

The commutator is

\[
[A,B]
=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}.
\]

## Lie–Trotter defect

For

\[
S_{\rm LT}(h)=e^{hA}e^{hB},
\]

Wolfram series gives

\[
S_{\rm LT}(h)-e^{h(A+B)}
=
\begin{pmatrix}
h^2/2-h^4/24&-h^3/6\\
-h^3/6&-h^2/2-h^4/24
\end{pmatrix}
+
O(h^5).
\]

The leading term is

\[
\frac{h^2}{2}[A,B].
\]

## Strang defect

For

\[
S_{\rm S}(h)
=
e^{hA/2}e^{hB}e^{hA/2},
\]

Wolfram series gives

\[
S_{\rm S}(h)-e^{h(A+B)}
=
\begin{pmatrix}
-h^4/24&h^3/12\\
-h^3/6&-h^4/24
\end{pmatrix}
+
O(h^5).
\]

The first nonzero terms are order

\[
h^3.
\]

## Replay expression

\`\`\`wolfram
A={{0,1},{0,0}};
B={{0,0},{1,0}};

exact=MatrixExp[h(A+B)];
lie=MatrixExp[h A].MatrixExp[h B];
strang=
 MatrixExp[(h/2) A].
 MatrixExp[h B].
 MatrixExp[(h/2) A];

{
 A.B-B.A,
 Normal[Series[exact,{h,0,4}]],
 Normal[Series[lie,{h,0,4}]],
 Normal[Series[lie-exact,{h,0,4}]],
 Normal[Series[strang,{h,0,4}]],
 Normal[Series[strang-exact,{h,0,4}]],
 1+z,
 1/(1-z),
 1-100*(1/20),
 FullSimplify[1/(1+100*(1/20))]
}
\`\`\`

Expected exact objects include:

\[
[A,B]
=
\operatorname{diag}(1,-1),
\]

explicit factor \(-4\), implicit factor \(1/6\), Lie leading order \(h^2\), and Strang leading order \(h^3\).

## Claim boundary

This witness checks the declared scalar and bounded-matrix examples.

It does not establish splitting order for unbounded operators without domain assumptions, or convergence of arbitrary learned split architectures.
