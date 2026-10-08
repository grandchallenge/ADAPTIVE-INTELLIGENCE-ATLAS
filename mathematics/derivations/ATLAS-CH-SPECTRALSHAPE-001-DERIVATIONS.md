# ATLAS-CH-SPECTRALSHAPE-001 — Derivation Packet

## D1. Witness matrix

Let

\[
G=
\begin{pmatrix}
4&0\\
0&1
\end{pmatrix}.
\]

Because \(G\) is positive diagonal, its singular values are exactly

\[
\sigma_1=4,
\qquad
\sigma_2=1.
\]

Thus

\[
\boxed{
\kappa_2(G)=4.
}
\]

## D2. Scalar normalization

Since

\[
\|G\|_2=4,
\]

operator-norm normalization gives

\[
G_{\rm scale}
=
\frac14G
=
\begin{pmatrix}
1&0\\
0&1/4
\end{pmatrix}.
\]

Its singular values are

\[
1,\frac14.
\]

Therefore

\[
\boxed{
\kappa_2(G_{\rm scale})=4.
}
\]

This proves exactly that scalar normalization need not improve conditioning.

More generally, for any nonzero scalar \(c\),

\[
\kappa_2(cG)=\kappa_2(G)
\]

whenever \(G\) is full rank.

## D3. Upper clipping

Define

\[
f_{\rm clip}(\sigma)=\min(\sigma,2).
\]

Then

\[
f_{\rm clip}(4)=2,
\qquad
f_{\rm clip}(1)=1.
\]

Hence

\[
G_{\rm clip}
=
\begin{pmatrix}
2&0\\
0&1
\end{pmatrix}.
\]

Therefore

\[
\boxed{
\kappa_2(G_{\rm clip})=2.
}
\]

The spectrum remains non-flat.

## D4. Polar flattening

For positive singular values, the square full-rank polar factor replaces each singular value by one.

Thus

\[
G_{\rm polar}
=
I_2.
\]

Therefore

\[
\boxed{
\kappa_2(G_{\rm polar})=1.
}
\]

## D5. Explicit non-flat target

Declare target singular values

\[
\tau_1=3,
\qquad
\tau_2=2.
\]

Keeping the witness singular vectors fixed gives

\[
G_\tau
=
\begin{pmatrix}
3&0\\
0&2
\end{pmatrix}.
\]

Hence

\[
\boxed{
\kappa_2(G_\tau)=\frac32.
}
\]

The target is deliberately non-flat.

## D6. Pairwise distinction

The four shaped singular spectra are:

\[
(1,1/4),
\]

\[
(2,1),
\]

\[
(1,1),
\]

\[
(3,2).
\]

No two are equal.

Therefore the four finite operations are pairwise distinct on this witness.

## D7. Condition-number ordering

The exact condition numbers are:

\[
4,
\quad
4,
\quad
2,
\quad
1,
\quad
\frac32,
\]

for:

- original;
- scalar-normalized;
- clipped;
- polar;
- non-flat target.

Thus:

\[
\boxed{
\kappa_2(G_{\rm polar})
<
\kappa_2(G_\tau)
<
\kappa_2(G_{\rm clip})
<
\kappa_2(G).
}
\]

This ordering is a property of the chosen witness and targets, not a universal optimizer ranking.

## D8. Non-normal control

Let

\[
A=
\begin{pmatrix}
1/2&2\\
0&1/2
\end{pmatrix},
\qquad
N=
\begin{pmatrix}
1/2&0\\
0&1/2
\end{pmatrix}.
\]

Both have characteristic polynomial

\[
(\lambda-1/2)^2.
\]

Hence both have eigenvalue multiset

\[
\boxed{
\{1/2,1/2\}.
}
\]

## D9. Interface response

Take

\[
e_2=
\begin{pmatrix}
0\\1
\end{pmatrix}.
\]

Then

\[
Ae_2=
\begin{pmatrix}
2\\1/2
\end{pmatrix}.
\]

Therefore

\[
\|Ae_2\|_2^2
=
4+\frac14
=
\boxed{
\frac{17}{4}
}.
\]

For the normal control,

\[
Ne_2=
\begin{pmatrix}
0\\1/2
\end{pmatrix},
\]

so

\[
\boxed{
\|Ne_2\|_2^2
=
\frac14.
}
\]

Thus identical eigenvalues do not determine even one-step response on the same probe vector.

## D10. Pseudospectral control

For

\[
A=
\begin{pmatrix}
a&K\\
0&a
\end{pmatrix},
\]

Nonnormal-001 gives the exact closed 2-norm boundary:

\[
|z-a|^2
=
\varepsilon(\varepsilon+K).
\]

Use

\[
a=\frac12,
\qquad
K=2,
\qquad
\varepsilon=\frac14.
\]

Then:

\[
|z-a|^2
=
\frac14
\left(
\frac14+2
\right)
=
\frac9{16}.
\]

So:

\[
\boxed{
r_A=\frac34.
}
\]

For

\[
N=\frac12I,
\]

the closed \(\varepsilon\)-pseudospectrum is the disk

\[
|z-1/2|\le\varepsilon.
\]

Thus:

\[
\boxed{
r_N=\frac14.
}
\]

The radii differ by a factor of three.

## D11. Why eigenvalue shaping is insufficient

The control has matched eigenvalues but different:

- one-step amplification;
- resolvent geometry;
- pseudospectral radius.

Therefore:

\[
\boxed{
\text{matched eigenvalue spectrum}
\not\Rightarrow
\text{matched transient behavior}.
}
\]

## D12. Instantaneous versus dynamical spectrum

Suppose an optimizer produces update matrix

\[
\Delta_t=T_f(G_t).
\]

Its singular spectrum concerns the instantaneous update.

A stateful optimizer instead has coupled state map

\[
(W_t,S_t)
\mapsto
(W_{t+1},S_{t+1}).
\]

The Jacobian of that joint map is a different operator.

Therefore no identity of the form

\[
\sigma(\Delta_t)
=
\sigma(J_{\rm state})
\]

is available without an explicit theorem.

## D13. Conditioning versus nonlinear convergence

Even if

\[
\kappa_2(T_f(G))
<
\kappa_2(G),
\]

this does not imply a smaller optimization loss after one or more parameter updates.

The optimization trajectory also depends on:

- objective geometry;
- step size;
- optimizer state;
- parameterization;
- nonlinear interactions;
- stochasticity.

Thus condition-number improvement is only the declared matrix diagnostic.

## D14. Rank boundary

If a matrix has zero singular values, then

\[
\kappa_2=\infty
\]

under the standard full-space convention.

A spectral map that floors zero singular values changes rank and therefore changes the operator class.

Such rank modification must be declared.

A zero singular value also makes the choice of singular vectors in the nullspaces nonunique. A rule \(G=U\Sigma V^\top\mapsto Uf(\Sigma)V^\top\) is SVD-independent on those directions when \(f(0)=0\); if \(f(0)\ne0\), pairing the left and right nullspace directions requires additional data.

For instance, \(G=\operatorname{diag}(1,0)\) has both \(U=V=I_2\) and \(U=\operatorname{diag}(1,-1), V=I_2\), with the same \(\Sigma=\operatorname{diag}(1,0)\). Setting \(f(1)=f(0)=1\) yields two distinct images, \(I_2\) and \(\operatorname{diag}(1,-1)\). The input matrix alone does not choose between them.

## D15. Target-profile boundary

A target spectrum

\[
\tau
\]

is a design object.

Its desirability cannot be inferred from its condition number alone.

For example, both

\[
(1,1)
\]

and

\[
(3,2)
\]

have better condition number than

\[
(4,1),
\]

but they encode different relative directional gains.

## Durable propositions

1. Scalar normalization preserves the witness condition number \(4\).
2. Upper clipping reduces it to \(2\).
3. Polar flattening reduces it to \(1\).
4. The explicit non-flat target gives \(3/2\).
5. These maps are pairwise distinct on the witness.
6. Equal eigenvalues do not imply equal finite-horizon response.
7. At \(\varepsilon=1/4\), the non-normal and normal pseudospectral radii are \(3/4\) and \(1/4\).
8. Instantaneous update spectra and optimizer-state spectra are different objects.
9. Better instantaneous conditioning does not prove faster nonlinear convergence.
10. Spectral-shape quality does not prove task quality.

## Claim boundary

This packet proves only the exact finite matrix identities above. It does not prove that a particular spectral target improves a named optimizer, that a flat spectrum is universally optimal, or that instantaneous update shaping controls the nonlinear training trajectory.
