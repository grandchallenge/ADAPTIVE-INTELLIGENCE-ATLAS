# ATLAS-CW-BCONTRACT-001 — Boundary Contracts Witness

**Chapter:** \`ATLAS-CH-BCONTRACT-001\`  
**Figure:** \`ATLAS-FIG-BCONTRACT-001\`  
**System:** Wolfram Language 15.0.1 for Linux x86 (64-bit), July 2 2026  
**System ID:** Linux-x86-64  
**Norm:** spectral/operator \(2\)-norm  
**Source lock:** \`sources/source-locks/ATLAS-CH-BCONTRACT-001.yaml\`

## Purpose

Replay the exact local sensitivity calculation used by the Boundary Contracts chapter and keep it separate from the chapter's semantic/interface obligations.

## Exact maps

Let

\[
f(x)=Ax,
\qquad
A=
\begin{pmatrix}
2&0\\
0&1/2
\end{pmatrix},
\]

and

\[
g(y)=By,
\qquad
B=
\begin{pmatrix}
1&1\\
0&2
\end{pmatrix}.
\]

Then

\[
C=BA=
\begin{pmatrix}
2&1/2\\
0&1
\end{pmatrix}.
\]

The chain-rule boundary Jacobian is exactly \(C\).

## JVP replay

For

\[
v=
\begin{pmatrix}
1\\
-1
\end{pmatrix},
\]

\[
Cv=
\begin{pmatrix}
3/2\\
-1
\end{pmatrix}.
\]

This is the exact Jacobian-vector product.

## VJP replay

For

\[
u=
\begin{pmatrix}
1\\
1
\end{pmatrix},
\]

\[
C^\top u=
\begin{pmatrix}
2\\
3/2
\end{pmatrix}.
\]

This is the exact vector-Jacobian product under the Euclidean pairing convention used here.

## Exact spectral norm

\[
C^\top C
=
\begin{pmatrix}
4&1\\
1&5/4
\end{pmatrix}.
\]

Its eigenvalues are

\[
\lambda_\pm
=
\frac{21\pm\sqrt{185}}8.
\]

Therefore

\[
\boxed{
\|C\|_2
=
\sqrt{\frac{21+\sqrt{185}}8}
=
2.079707626949502\ldots
}
\]

The second singular value is

\[
0.9616736381996075\ldots
\]

## Power-iteration replay

Starting from the normalized vector proportional to \((1,1)\), power iteration on

\[
M=C^\top C
\]

produces spectral-norm estimates

\[
1.9039432765,
\]

\[
2.0701070106,
\]

\[
2.0792647056,
\]

\[
2.0796873684,
\]

\[
2.0797067007,
\]

\[
2.0797075846,
\]

and then converges numerically to the exact dominant singular value.

The witness therefore checks the estimator against a known exact answer.

## Semantic incompatibility witness

Define

\[
f_{\rm dir}(x)=\frac{x}{\|x\|_2}
\]

and let the downstream component interpret

\[
g_{\rm mag}(y)=\|y\|_2
\]

as preserved amplitude.

For

\[
x=(3,4),
\]

the input amplitude is \(5\), but

\[
g_{\rm mag}(f_{\rm dir}(x))=1.
\]

The tensor dimensions compose. The semantics do not.

This is a mathematical counterexample to the proposition that shape compatibility alone establishes composability.

## Figure provenance

Source:

\`figures/wolfram/ATLAS-FIG-BCONTRACT-001.wl\`

Source Git blob SHA-1:

\`e064df23ccea715198fe91f9e20a817fb59302e9\`

Rendered master:

\`figures/masters/ATLAS-FIG-BCONTRACT-001.png\`

Rendered Git blob SHA-1:

\`e3106af2b200823fb3b2cb699e8436a7fc89d0b8\`

Rendered size:

\`48,873 bytes\`

The right panel is the exact image of the unit circle under \(C\). The left-panel interface layout is schematic.

## GCL project-state boundary

The current public \`grandchallenge/MODULUS\` repository was inspected at commit

\`9fc42eb5f29d5fff396f13e1a6c972af8fe64b35\`.

Its public tree contains typed contract machinery, including

\`modulus/online/contracts.py\`

with Git blob

\`33b8c325203adc7a54a5b8b3ad4e0db6092af51d\`.

However, the names

- \`BoundaryContract\`;
- \`SeparatorCompiler\`;
- \`Modula\`

were not found in the inspected public tree or searchable commit history.

Therefore this witness does **not** attribute the remembered named extension to current public MODULUS code.

## Claim boundary

This witness establishes one exact finite-dimensional composition Jacobian, JVP/VJP values, an exact singular-value calculation, a power-iteration replay, and a semantic incompatibility counterexample.

It does not establish:

- a universal contract schema;
- a global nonlinear stability theorem;
- sufficiency of any low-order separator;
- a certified component interface;
- existence of the remembered named GCL extension in current public MODULUS.
