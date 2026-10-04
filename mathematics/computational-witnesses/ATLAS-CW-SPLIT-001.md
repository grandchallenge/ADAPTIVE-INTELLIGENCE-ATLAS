# Computational Witness — ATLAS-CW-SPLIT-001

## Purpose

Reproduce the bounded matrix calculations used by `ATLAS-CH-SPLIT-001`.

This witness establishes only the declared finite-dimensional identities and numeric comparisons.

**Product-order convention:** states are column vectors. Thus \(L_{AB}=e^{hA}e^{hB}\) applies the \(B\) subflow first and then the \(A\) subflow. The subscripts record matrix-product order, not chronological execution wording.

## Exact objects

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

Exact products:

\[
A^2=B^2=0,
\]

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

\[
[A,B]
=
AB-BA
=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}.
\]

Because \(A^2=B^2=0\),

\[
e^{hA}=I+hA,
\qquad
e^{hB}=I+hB.
\]

Therefore

\[
L_{AB}\(h\)=
\begin{pmatrix}
1+h^2&h\\
h&1
\end{pmatrix},
\]

\[
L_{BA}\(h\)=
\begin{pmatrix}
1&h\\
h&1+h^2
\end{pmatrix},
\]

and

\[
L_{AB}\(h\)-L_{BA}\(h\)=h^2[A,B].
\]

## Exact combined flow

Since

\[
(A+B)^2=I,
\]

\[
E\(h\)=e^{h(A+B)}
=
\begin{pmatrix}
\cosh h&\sinh h\\
\sinh h&\cosh h
\end{pmatrix}.
\]

Series comparison:

\[
L_{AB}\(h\)-E\(h\)
=
\frac{h^2}{2}[A,B]+O(h^3),
\]

\[
L_{BA}\(h\)-E\(h\)
=
-\frac{h^2}{2}[A,B]+O(h^3).
\]

## Strang witness

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

Compared with the exact series,

\[
S_{ABA}\(h\)-E\(h\)
=
\begin{pmatrix}
O\(h^4\)&h^3/12+O(h^5)\\
-h^3/6+O(h^5)&O\(h^4\)
\end{pmatrix}.
\]

Thus this witness has local defect \(O(h^3)\).

## Numerical checkpoint at h = 1/2

\[
L_{AB}
=
\begin{pmatrix}
5/4&1/2\\
1/2&1
\end{pmatrix},
\]

\[
L_{BA}
=
\begin{pmatrix}
1&1/2\\
1/2&5/4
\end{pmatrix},
\]

\[
S_{ABA}
=
\begin{pmatrix}
9/8&17/32\\
1/2&9/8
\end{pmatrix}.
\]

The exact flow is

\[
E(1/2)
=
\begin{pmatrix}
\cosh(1/2)&\sinh(1/2)\\
\sinh(1/2)&\cosh(1/2)
\end{pmatrix}.
\]

Using double-precision evaluation only for the reported norms:

- `||L_AB-E||_F ≈ 0.1793148493970293`;
- `||L_BA-E||_F ≈ 0.1793148493970293`;
- `||S_ABA-E||_F ≈ 0.02370487546729764`.

The smaller Strang error at this one \(h\) is a witness value, not the proof of second-order convergence. The order statement comes from the series derivation under the declared matrix setting.

## Commuting control

\[
A_c=\operatorname{diag}(1,2),
\qquad
B_c=\operatorname{diag}(3,4).
\]

Then

\[
[A_c,B_c]=0
\]

and exactly

\[
e^{hA_c}e^{hB_c}
=
e^{hB_c}e^{hA_c}
=
e^{h(A_c+B_c)}.
\]

## Minimal reproduction

A symbolic algebra system can reproduce the witness with the following operations:

1. define the two exact matrices;
2. compute `A*A`, `B*B`, `A*B-B*A`;
3. form `(I+h*A)(I+h*B)` and the reversed product;
4. expand `exp(h*(A+B))` as a series through at least \(h^4\);
5. form `(I+h*A/2)(I+h*B)(I+h*A/2)`;
6. compare coefficients;
7. substitute \(h=1/2\) and evaluate Frobenius norms;
8. repeat the order check for diagonal commuting controls.

## Claim boundary

This witness does not evaluate a trained neural network, does not estimate a neural commutator, does not establish task-performance improvement, and does not promote the splitting analogy into a numerical-integration theorem for learned blocks.
