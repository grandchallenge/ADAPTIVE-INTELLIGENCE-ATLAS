# ATLAS-CW-MATRIXOPT-001 — Exact Rectangular Matrix-Update Witness

## Purpose

This witness separates four operations on the same \(3\times2\) gradient matrix:

1. the raw Euclidean matrix gradient;
2. a representative diagonal row scaling;
3. the exact polar/orthogonalized factor;
4. one-step left/right Shampoo statistics.

It also checks the Frobenius- and spectral-norm steepest-direction formulas.

## Claim boundary

This is an exact finite-dimensional algebra witness.

It establishes the singular values and norms of the declared matrix, the rank defect of the tall left Gram matrix, the semi-orthogonality of the exact polar factor, the singular values of one declared diagonal scaling, and the norm-duality values for two local steepest-direction problems.

It does **not** establish optimizer superiority, identify the diagonal control with a named optimizer, identify stateful Shampoo with a polar transform, or identify finite Newton-Schulz iterations with an exact polar decomposition.

## Input

\[
G=
\begin{pmatrix}
2&0\\
0&1\\
1&0
\end{pmatrix}.
\]

The columns

\[
g_1=(2,0,1)^\top,
\qquad
g_2=(0,1,0)^\top
\]

are orthogonal, with squared norms \(5\) and \(1\).

Therefore

\[
\sigma(G)=\{\sqrt5,1\}.
\]

## Gram matrices

\[
G^\top G
=
\begin{pmatrix}
5&0\\
0&1
\end{pmatrix}.
\]

Hence \(G^\top G\) is positive definite.

But

\[
GG^\top
=
\begin{pmatrix}
4&0&2\\
0&1&0\\
2&0&1
\end{pmatrix}.
\]

The third row is half the first, so

\[
\operatorname{rank}(GG^\top)=2,
\qquad
\det(GG^\top)=0.
\]

This is the tall-matrix one-step rank obstruction.

## Reduced SVD and polar factor

Choose

\[
U=
\begin{pmatrix}
2/\sqrt5&0\\
0&1\\
1/\sqrt5&0
\end{pmatrix},
\quad
\Sigma=
\begin{pmatrix}
\sqrt5&0\\
0&1
\end{pmatrix},
\quad
V=I_2.
\]

Then

\[
U^\top U=I_2,
\qquad
U\Sigma V^\top=G.
\]

The exact polar factor is

\[
Q=UV^\top
=
\begin{pmatrix}
2/\sqrt5&0\\
0&1\\
1/\sqrt5&0
\end{pmatrix}.
\]

It satisfies

\[
Q^\top Q=I_2,
\]

but

\[
QQ^\top
=
\begin{pmatrix}
4/5&0&2/5\\
0&1&0\\
2/5&0&1/5
\end{pmatrix}
\neq I_3.
\]

Thus \(Q\) is column-semi-orthogonal, not a square orthogonal matrix.

## Norms

From the singular values,

\[
\|G\|_2=\sqrt5,
\qquad
\|G\|_F=\sqrt6,
\qquad
\|G\|_*=\sqrt5+1.
\]

For a unit Frobenius ball,

\[
\Delta_F^\star=-G/\sqrt6
\]

has local linearized change

\[
\langle G,\Delta_F^\star\rangle_F=-\sqrt6.
\]

For a unit spectral ball,

\[
\Delta_2^\star=-Q
\]

has local linearized change

\[
\langle G,\Delta_2^\star\rangle_F=-(\sqrt5+1).
\]

These values do not rank optimizers because the admissible norm balls differ.

## Diagonal row-scaling control

Let

\[
D=\operatorname{diag}(1/2,1,1/2).
\]

Then

\[
DG=
\begin{pmatrix}
1&0\\
0&1\\
1/2&0
\end{pmatrix}.
\]

Its singular values are

\[
\sqrt5/2,\ 1.
\]

Thus the original ratio \(\sqrt5\) becomes \(\sqrt5/2\), while the polar factor has ratio \(1\).

The control changes anisotropy without becoming the polar factor.

## Support-restricted one-step inverse-root identity

On the nonzero singular subspaces,

\[
(GG^\top)^{-1/4}
G
(G^\top G)^{-1/4}
=
Q.
\]

A strict full-space inverse of \(GG^\top\) does not exist.

The identity is therefore support-restricted, or equivalently approached through an explicitly declared damping/pseudoinverse convention.

## Pure-Python exact replay

The following uses only the Python standard library.

```python
from fractions import Fraction as F

G = [
    [F(2), F(0)],
    [F(0), F(1)],
    [F(1), F(0)],
]

def transpose(A):
    return [list(row) for row in zip(*A)]

def matmul(A, B):
    BT = transpose(B)
    return [
        [sum(a*b for a, b in zip(row, col)) for col in BT]
        for row in A
    ]

GTG = matmul(transpose(G), G)
GGT = matmul(G, transpose(G))

assert GTG == [[F(5), F(0)], [F(0), F(1)]]
assert GGT == [
    [F(4), F(0), F(2)],
    [F(0), F(1), F(0)],
    [F(2), F(0), F(1)],
]

q1_num = [F(2), F(0), F(1)]
q2 = [F(0), F(1), F(0)]
assert sum(x*x for x in q1_num) == 5
assert sum(x*x for x in q2) == 1
assert sum(a*b for a, b in zip(q1_num, q2)) == 0

DG = [
    [F(1), F(0)],
    [F(0), F(1)],
    [F(1, 2), F(0)],
]
DGT_DG = matmul(transpose(DG), DG)
assert DGT_DG == [[F(5, 4), F(0)], [F(0), F(1)]]

print("MATRIXOPT witness: PASS")
```

Expected standard output:

```text
MATRIXOPT witness: PASS
```

## Interpretation

The witness makes five distinctions concrete:

- a full-column-rank rectangular gradient can have a singular left Gram matrix;
- a polar factor of a tall matrix is column-semi-orthogonal;
- diagonal scaling can reshape singular values without producing the polar factor;
- a support-restricted one-step inverse-root transform can collapse algebraically to the polar factor;
- stateful Shampoo and finite Muon-like realizations remain distinct from this exact one-step identity.
