# ATLAS-CH-RESIDUAL-001 — Derivation Packet

## D1. Declared representation, transformations, and capability

Let

\[
X
\]

be a representation/state space.

Let a declared transformation family \(G\) act on \(X\).

Let

\[
B:X\to\mathcal Y
\]

be the declared capability or behavior object to be preserved.

The definition is intentionally task-relative.

Changing \(B\) can change the Residual.

## D2. Transformation invariance

A descriptor

\[
R:X\to\mathcal Z
\]

is invariant to the declared transformations when

\[
\boxed{
R(g\cdot x)=R(x)
}
\]

for every admissible \(g\in G\) and \(x\in X\).

Invariance alone is not enough.

The constant map

\[
R_0(x)=0
\]

is invariant under every transformation family.

It is usually useless.

## D3. Capability sufficiency

A descriptor \(R\) is sufficient for the declared capability \(B\) if there exists a reconstructor

\[
D:\mathcal Z\to\mathcal Y
\]

such that

\[
\boxed{
B=D\circ R.
}
\]

This means the capability can be reconstructed from the descriptor.

It does not require reconstruction of the full original state.

## D4. Factorization preorder

For descriptors

\[
R_1:X\to Z_1,
\qquad
R_2:X\to Z_2,
\]

define

\[
R_1\preceq R_2
\]

when there exists a map

\[
\phi:Z_2\to Z_1
\]

such that

\[
R_1=\phi\circ R_2.
\]

Interpretation:

\(R_1\) contains no more distinctions than \(R_2\), because \(R_1\) can be recovered from \(R_2\).

This is a preorder rather than necessarily a partial order because distinct codings can factor through one another.

## D5. Provisional Residual

Let \(\mathcal S_{B,G}\) be the class of descriptors that are both:

- invariant under \(G\);
- sufficient for \(B\).

A provisional Residual is a **least element** of this class under \(\preceq\).

Thus \(R\in\mathcal S_{B,G}\) is a Residual if for every

\[
S\in\mathcal S_{B,G},
\]

we have

\[
\boxed{
R\preceq S.
}
\]

Equivalently, every other invariant sufficient descriptor can be post-processed into \(R\).

Existence is not guaranteed.

## D6. Uniqueness up to realized-image recoding

Suppose \(R\) and \(R'\) are both least elements.

Then:

\[
R=\phi\circ R',
\]

and

\[
R'=\psi\circ R
\]

for some \(\phi,\psi\).

For every

\[
z'\in\operatorname{Im}(R'),
\]

choose \(x\) with \(z'=R'(x)\).

Then

\[
\psi(\phi(z'))
=
\psi(\phi(R'(x)))
=
\psi(R(x))
=
R'(x)
=
z'.
\]

Thus

\[
\psi\circ\phi
=
\operatorname{id}
\]

on \(\operatorname{Im}(R')\).

Similarly,

\[
\phi\circ\psi
=
\operatorname{id}
\]

on \(\operatorname{Im}(R)\).

Therefore two least Residuals are bijectively equivalent on their realized images.

This does not imply a unique coordinate representation.

## D7. Exact nuisance-orbit model

Let

\[
X=\mathbb R^2,
\]

with state

\[
x=(s,n).
\]

Interpret:

- \(s\): task-relevant signal;
- \(n\): nuisance.

Let the transformation group be translations in the nuisance coordinate:

\[
g_a(s,n)
=
(s,n+a),
\qquad
a\in\mathbb R.
\]

Let capability be

\[
B(s,n)=s.
\]

Define

\[
R(s,n)=s.
\]

### Invariance

\[
R(g_a(s,n))
=
R(s,n+a)
=
s
=
R(s,n).
\]

### Sufficiency

Let

\[
D(r)=r.
\]

Then

\[
D(R(s,n))
=
s
=
B(s,n).
\]

### Leastness

Let \(S\) be any descriptor sufficient for \(B\).

By sufficiency, there exists \(D_S\) such that

\[
B=D_S\circ S.
\]

But

\[
R=B.
\]

Therefore

\[
R
=
D_S\circ S.
\]

Hence

\[
R\preceq S.
\]

This holds for every invariant sufficient \(S\).

Therefore \(R=s\) is a least invariant sufficient descriptor in this toy setting.

## D8. Full state is sufficient but not least

The identity descriptor

\[
S_{\rm full}(s,n)
=
(s,n)
\]

is sufficient.

Indeed,

\[
B(s,n)
=
\pi_1(S_{\rm full}(s,n)).
\]

It is also not invariant under nuisance translations.

Even if invariance were not required, it contains unnecessary information because

\[
R
=
\pi_1\circ S_{\rm full}.
\]

The Residual reconstructs the declared capability without reconstructing the nuisance.

## D9. Constant descriptor is invariant but insufficient

Define

\[
S_0(s,n)=0.
\]

It is invariant.

But take

\[
x_1=(2,0),
\qquad
x_2=(3,0).
\]

Then

\[
S_0(x_1)=S_0(x_2)=0,
\]

while

\[
B(x_1)=2,
\qquad
B(x_2)=3.
\]

No deterministic decoder from the constant descriptor can reconstruct both capability values.

Thus invariance does not imply sufficiency.

## D10. Representation change

Let

\[
T=
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix}.
\]

For

\[
x=(s,n),
\]

define recoded coordinates

\[
z=Tx.
\]

Then

\[
z_1=s+n,
\]

and

\[
z_2=s-n.
\]

Therefore

\[
\boxed{
s
=
\frac{z_1+z_2}{2}.
}
\]

The Residual survives the coordinate change, but it is no longer stored in one coordinate slot.

This is the sense in which the Residual is intended to be transferable rather than coordinate-bound.

## D11. Exact numeric recoding witness

Take

\[
x=(2,5).
\]

Then

\[
z=T x=(7,-3).
\]

Reconstruction gives

\[
\frac{7+(-3)}{2}=2.
\]

Thus the capability-relevant signal is exactly reconstructed after the invertible recoding.

## D12. Task dependence

Change the declared capability to

\[
B'(s,n)=(s,n).
\]

Then

\[
R(s,n)=s
\]

is no longer sufficient.

The Residual therefore depends on what capability is required to survive.

Without a declared capability or test family, “the Residual” is underspecified.

## D13. Relation to sufficient statistics

Classical sufficient statistics ask whether a statistic preserves all information needed for inference about a declared parameter under a statistical model [@LehmannCasella1998].

The Residual borrows the structure:

- declare what must be preserved;
- compress away what is not needed;
- define minimality by factorization.

The Residual generalization is broader and therefore not automatically covered by classical sufficiency theorems.

## D14. Relation to minimal/invariant representations

Achille and Soatto study representations that are sufficient for a task while becoming minimal and invariant to nuisance variation under their declared information-theoretic setting [@AchilleSoatto2018].

This supports the combination of:

- sufficiency;
- minimality;
- nuisance invariance.

It does not establish the general Atlas Residual object for arbitrary computational capabilities.

## D15. Relation to information bottleneck

The information bottleneck programme seeks compressed encodings that preserve information relevant to a declared target [@TishbyPereiraBialek2000].

This supplies another precedent for the principle:

> preserve what matters; remove what does not.

The Residual is not defined as an information-bottleneck optimum unless a specific probabilistic formulation makes that identification valid.

## D16. Reconstruction test

A proposed Residual \(R\) should be tested by:

1. apply admissible representation changes;
2. compute or extract \(R\);
3. reconstruct the declared capability;
4. intervene on or replace non-Residual structure;
5. verify that capability remains within the declared tolerance.

Failure at step 3 refutes sufficiency.

Failure of invariance under declared transformations refutes transferability.

A strictly coarser sufficient invariant descriptor refutes leastness.

## Claim boundary

This packet defines a provisional least invariant sufficient descriptor under a factorization preorder and proves its properties in one exact toy setting.

It does not prove that frontier neural systems possess a unique, finite-dimensional, learnable, or architecture-independent Residual.
