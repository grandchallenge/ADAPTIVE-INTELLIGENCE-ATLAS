# Derivations — ATLAS-CH-SPLIT-001

## Scope

This packet supports the exact finite-dimensional claims used by **Split-Operator Networks**.

It does not prove that arbitrary learned neural blocks are exact flows or that classical splitting orders transfer unchanged to learned nonlinear architectures.

## 1. Lie ordering and the first commutator

**Application convention.** States are column vectors, so a matrix product acts right-to-left. The label \(S_{AB}=e^{hA}e^{hB}\) records product order, not chronological wording: \(B\) acts first and \(A\) second. Chronological A-then-B is \(e^{hB}e^{hA}\).

Let \(A,B\in\mathbb R^{d\times d}\) be constant matrices.

Expand

\[
e^{hA}
=
I+hA+\frac{h^2}{2}A^2+O(h^3),
\]

\[
e^{hB}
=
I+hB+\frac{h^2}{2}B^2+O(h^3).
\]

Then

\[
e^{hA}e^{hB}
=
I+h(A+B)
+
h^2\left(
\frac12A^2+AB+\frac12B^2
\right)
+
O(h^3).
\]

Meanwhile,

\[
e^{h(A+B)}
=
I+h(A+B)
+
\frac{h^2}{2}(A+B)^2
+
O(h^3),
\]

so

\[
e^{h(A+B)}
=
I+h(A+B)
+
h^2\left(
\frac12A^2+
\frac12AB+
\frac12BA+
\frac12B^2
\right)
+
O(h^3).
\]

Subtracting,

\[
e^{hA}e^{hB}
-
e^{h(A+B)}
=
\frac{h^2}{2}(AB-BA)
+
O(h^3)
=
\frac{h^2}{2}[A,B]
+
O(h^3).
\]

Reversing the order gives

\[
e^{hB}e^{hA}
-
e^{h(A+B)}
=
-\frac{h^2}{2}[A,B]
+
O(h^3).
\]

Therefore the leading order asymmetry between the two Lie compositions is

\[
e^{hA}e^{hB}-e^{hB}e^{hA}
=
h^2[A,B]+O(h^3).
\]

## 2. Exact nilpotent witness

Take

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

Since \(A^2=B^2=0\),

\[
e^{hA}=I+hA,
\qquad
e^{hB}=I+hB.
\]

The products are

\[
AB=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix},
\qquad
BA=
\begin{pmatrix}
0&0\\
0&1
\end{pmatrix},
\]

hence

\[
[A,B]
=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}.
\]

The product-labeled \(S_{AB}\) Lie composition is

\[
e^{hA}e^{hB}
=
I+h(A+B)+h^2AB
=
\begin{pmatrix}
1+h^2&h\\
h&1
\end{pmatrix}.
\]

The reversed product \(S_{BA}\) is

\[
e^{hB}e^{hA}
=
I+h(A+B)+h^2BA
=
\begin{pmatrix}
1&h\\
h&1+h^2
\end{pmatrix}.
\]

Their exact difference is

\[
e^{hA}e^{hB}-e^{hB}e^{hA}
=
h^2[A,B].
\]

At \(h=1/2\),

\[
e^{hA}e^{hB}
=
\begin{pmatrix}
5/4&1/2\\
1/2&1
\end{pmatrix},
\]

\[
e^{hB}e^{hA}
=
\begin{pmatrix}
1&1/2\\
1/2&5/4
\end{pmatrix}.
\]

## 3. Exact combined flow

For the witness,

\[
A+B
=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix},
\]

and

\[
(A+B)^2=I.
\]

Therefore

\[
e^{h(A+B)}
=
\cosh(h\)I+\sinh(h\)(A+B),
\]

or

\[
e^{h(A+B)}
=
\begin{pmatrix}
\cosh h&\sinh h\\
\sinh h&\cosh h
\end{pmatrix}.
\]

The leading Lie defect follows directly by comparing series.

At \(h=1/2\),

\[
\cosh(1/2)\approx1.127625965,
\qquad
\sinh(1/2)\approx0.521095305.
\]

The Frobenius error of either Lie ordering is approximately

\[
0.1793148494.
\]

This numeric norm is only a bounded witness value, not an asymptotic theorem.

## 4. Symmetric Strang composition

Because \(A^2=B^2=0\),

\[
e^{hA/2}=I+\frac h2 A,
\qquad
e^{hB}=I+hB.
\]

Multiply exactly:

\[
S_{ABA}\(h\)
=
e^{hA/2}e^{hB}e^{hA/2}
=
\begin{pmatrix}
1+h^2/2&h+h^3/4\\
h&1+h^2/2
\end{pmatrix}.
\]

The exact combined-flow series is

\[
e^{h(A+B)}
=
\begin{pmatrix}
1+h^2/2+h^4/24+O(h^6)&
h+h^3/6+O(h^5)\\
h+h^3/6+O(h^5)&
1+h^2/2+h^4/24+O(h^6)
\end{pmatrix}.
\]

Hence

\[
S_{ABA}\(h\)-e^{h(A+B)}
=
\begin{pmatrix}
O(h^4\)&h^3/12+O(h^5)\\
-h^3/6+O(h^5)&O(h^4\)
\end{pmatrix}.
\]

The local defect is therefore \(O(h^3)\) in this exact finite-dimensional witness.

At \(h=1/2\),

\[
S_{ABA}(1/2)
=
\begin{pmatrix}
9/8&17/32\\
1/2&9/8
\end{pmatrix},
\]

with Frobenius error approximately

\[
0.02370487547
\]

against the exact combined flow.

No general neural claim is inferred from this one numeric comparison.

## 5. Commuting control

Let

\[
A_c=\operatorname{diag}(1,2),
\qquad
B_c=\operatorname{diag}(3,4).
\]

Then

\[
[A_c,B_c]=0.
\]

For commuting finite matrices,

\[
e^{hA_c}e^{hB_c}=e^{h(A_c+B_c)}.
\]

The reversed product is identical:

\[
e^{hB_c}e^{hA_c}=e^{h(A_c+B_c)}.
\]

Thus the witness cleanly separates the noncommuting and commuting cases.

## 6. Additive versus sequential residual updates

Let

\[
F_A(x\)=hAx,
\qquad
F_B(x\)=hBx.
\]

An additive residual update is

\[
x^+
=
x+F_A(x\)+F_B(x\)
=
\left(I+h(A+B)\right)x.
\]

If A is applied first and B sees the updated state,

\[
x_1=(I+hA)x,
\]

\[
x^+=(I+hB)x_1.
\]

Therefore

\[
x^+
=
(I+hB)(I+hA)x
=
\left(I+h(A+B)+h^2BA\right)x.
\]

If B is applied first, the cross term becomes \(h^2AB\).

So sequential residual composition is not merely an additive sum unless the cross term vanishes or is deliberately neglected under a declared approximation.

## 7. Neural submaps and the exact-flow boundary

For a neural residual block define the actual maps, for example,

\[
\Psi_A(H\)=H+F_A(N_A(H\)),
\]

\[
\Psi_B(H\)=H+F_B(N_B(H\)).
\]

The block

\[
\Psi_B\circ\Psi_A
\]

is an ordinary composition of learned maps.

Unless one separately proves that \(\Psi_A\) and \(\Psi_B\) are exact time-\(h\) flows of declared vector fields, it is incorrect to replace them by \(e^{hA}\) and (e^{hB}) as an identity.

The splitting viewpoint still has architectural value: it asks which transformations are isolated, which order they occur in, which state each sees, and how noncommutation affects composition. The numerical-order theorem remains conditional on the stronger exact-flow/regularity assumptions.

## 8. Neural half-step and nonlinear noncommutation boundaries

A Strang-style neural expression requires more than one learned map named \(\Psi_A\). One must declare a step-parameterized family

\[
\Psi_A(h\),\qquad \Psi_B(h\),
\]

with a meaningful half-stage \(\Psi_A(h/2)\). Only then is the palindromic composition

\[
\Psi_A(h/2)\circ\Psi_B(h\)\circ\Psi_A(h/2)
\]

well-defined as a neural analogue of the classical sequence. Duplicating a block, halving a residual coefficient, or writing the symbol \(A/2\) does not by itself establish Strang semantics.

For nonlinear maps define the direct composition defect

\[
C_\Psi\(x\)
=
\Psi_B(\Psi_A(x\))
-
\Psi_A(\Psi_B(x\)).
\]

Its derivative, when defined, is

\[
DC_\Psi\(x\)
=
J_B(\Psi_A(x\))J_A(x\)
-
J_A(\Psi_B(x\))J_B(x\).
\]

This is generally not the same as the same-state algebraic Jacobian commutator

\[
J_B(x\)J_A(x\)-J_A(x\)J_B(x\).
\]

The latter can be a useful local diagnostic, but it is not automatically the derivative of the nonlinear composition defect.

## 9. Shared versus layer-varying operators

If every layer uses the same pair \(A,B\), an autonomous reference problem is at least syntactically available.

If layer \(k\) uses \(A_k,B_k\), then the appropriate reference is nonautonomous or stage-dependent.

A local commutator

\[
[A_k,B_k]
\]

describes only that stage's finite-dimensional ordering defect. One may not silently reuse a single autonomous formula across all layers.

## 10. Error taxonomy

For a neural split-operator interpretation, keep separate:

- splitting/discretization error relative to a declared reference flow;
- function-approximation error of learned submaps;
- estimation error from finite data;
- optimization error;
- stochastic training variation;
- finite-precision and implementation error.

Only the first is controlled by classical splitting-order statements.

## Claim boundary

The exact derivations above establish finite-dimensional matrix identities and series orders.

They do not establish that Transformer attention and FFN sublayers are exact flows, that their commutator is small, that Strang-style rearrangement improves task loss, or that a symmetric neural block is globally reversible.
