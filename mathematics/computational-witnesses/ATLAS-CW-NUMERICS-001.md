# ATLAS-CW-NUMERICS-001 — Discretization and Splitting Witness

**Chapter:** \`ATLAS-CH-NUMERICS-001\`  
**Runtime:** Wolfram Language service, 2026-10-02

## Purpose

Replay the exact calibration calculations for:

- explicit/implicit Euler amplification;
- stiff two-timescale stability;
- harmonic-oscillator structure preservation;
- Lie-Trotter and Strang splitting defect order.

## Scalar test equation

For

\[
y'=\lambda y,
\qquad
z=h\lambda,
\]

explicit Euler has

\[
R_E(z)=1+z.
\]

Implicit Euler has

\[
R_I(z)=\frac{1}{1-z}.
\]

## Stiff diagonal witness

For eigenvalues

\[
-1,
\qquad
-100,
\]

at

\[
h=0.03,
\]

explicit Euler gives amplification factors

\[
\{0.97,-2\}.
\]

Implicit Euler gives

\[
\left\{
\frac{1}{1.03},
\frac14
\right\}
\approx
\{0.9708737864,0.25\}.
\]

The exact fast amplification is

\[
e^{-3}
\approx
0.04978706837.
\]

Thus implicit Euler is stable at this step while still strongly damping the fast transient inaccurately.

## Harmonic-oscillator structure witness

Explicit Euler:

\[
M_E
=
\begin{pmatrix}
1&h\\
-h&1
\end{pmatrix},
\]

with

\[
\det M_E=1+h^2.
\]

Symplectic Euler:

\[
M_{SE}
=
\begin{pmatrix}
1-h^2&h\\
-h&1
\end{pmatrix},
\]

with

\[
\det M_{SE}=1,
\]

and

\[
M_{SE}^\top J M_{SE}-J=0.
\]

## Noncommuting split witness

Use

\[
A=
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix},
\qquad
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

For

\[
\Psi^{LT}_h
=
e^{hA}e^{hB},
\]

symbolic expansion gives

\[
\Psi^{LT}_h-e^{h(A+B)}
=
\begin{pmatrix}
h^2/2-h^4/24&-h^3/6\\
-h^3/6&-h^2/2-h^4/24
\end{pmatrix}
+
O(h^5)
\]

at the displayed series depth.

The leading defect is \(O(h^2)\).

For

\[
\Psi^S_h
=
e^{hA/2}e^{hB}e^{hA/2},
\]

symbolic expansion gives leading terms

\[
\Psi^S_h-e^{h(A+B)}
=
\begin{pmatrix}
-h^4/24&h^3/12+O(h^5)\\
-h^3/6+O(h^5)&-h^4/24
\end{pmatrix}.
\]

The leading defect is \(O(h^3)\).

## Replay expression

\`\`\`wolfram
ClearAll[h,z];

aa={{0,1},{0,0}};
bb={{0,0},{1,0}};

comm=aa.bb-bb.aa;

exact=MatrixExp[h(aa+bb)];

lie=
 MatrixExp[h aa].
 MatrixExp[h bb];

strang=
 MatrixExp[(h/2) aa].
 MatrixExp[h bb].
 MatrixExp[(h/2) aa];

lieSeries=
 Map[
  Normal@Series[#,{h,0,4}]&,
  lie-exact,
  {2}
 ];

strangSeries=
 Map[
  Normal@Series[#,{h,0,5}]&,
  strang-exact,
  {2}
 ];

me={{1,h},{-h,1}};

mse={{
  1-h^2,h
 },{
  -h,1
 }};

jj={{0,1},{-1,0}};

{
  1+z,
  1/(1-z),
  {1-0.03,1-100*0.03},
  {1/(1+0.03),1/(1+3)},
  comm,
  lieSeries,
  strangSeries,
  Factor[Det[me]],
  Factor[Det[mse]],
  FullSimplify[
   Transpose[mse].jj.mse-jj
  ]
}
\`\`\`

## Claim boundary

This witness checks exact finite-dimensional calibration systems only.

It does not establish numerical stability, order, or structure preservation for an arbitrary learned architecture unless the corresponding numerical assumptions and update equations are actually satisfied.
