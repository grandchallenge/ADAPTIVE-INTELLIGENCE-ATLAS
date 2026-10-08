# ATLAS-CH-RPO-001 — Derivation Packet

## 1. Scope

This packet formalizes two distinct relative-position operator views:

1. feature-space relative operators inherited from RoPE geometry;
2. sequence-index relative-position operators built from translation-invariant kernels.

The two frequency notions are related only by analogy unless an explicit model identifies them.

Source boundary:

\`sources/source-locks/ATLAS-CH-RPO-001.yaml\`.

## 2. Feature-space representation

For a 2D rotation block,

\[
R(\theta)
=
\begin{pmatrix}
\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta
\end{pmatrix}.
\]

For frequencies \(\omega_a\), define

\[
\rho(\Delta)
=
\bigoplus_a R(\omega_a\Delta).
\]

Using

\[
R(\alpha)R(\beta)=R(\alpha+\beta),
\]

we obtain

\[
\rho(\Delta_1)\rho(\Delta_2)
=
\rho(\Delta_1+\Delta_2).
\]

Thus \(\rho\) is a finite-dimensional representation of additive relative offset.

If \(\omega_a=0\), the corresponding block is

\[
R(0)=I
\]

for every offset. This is a feature-space zero-frequency block.

## 3. Sequence-index cyclic kernel

Let sequence positions be \(\mathbb Z_L\) and let

\[
\kappa:\mathbb Z_L\to\mathbb C.
\]

Define

\[
(Kx)_i
=
\sum_{\Delta=0}^{L-1}
\kappa(\Delta)
x_{i+\Delta\;\mathrm{mod}\;L}.
\]

The matrix entries satisfy

\[
K_{ij}
=
\kappa(j-i\;\mathrm{mod}\;L),
\]

so K is circulant.

The cyclic boundary is part of the definition.

For finite nonperiodic indexing, the analogous matrix with entries \(b(j-i)\) is generally Toeplitz-like rather than circulant.

## 4. Fourier diagonalization

Let

\[
\phi_k(n)
=
L^{-1/2}e^{2\pi i kn/L}.
\]

Then

\[
(K\phi_k)_i
=
\sum_{\Delta}
\kappa(\Delta)
L^{-1/2}
e^{2\pi i k(i+\Delta)/L}.
\]

Factor out \(\phi_k(i)\):

\[
(K\phi_k)_i
=
\phi_k(i)
\sum_{\Delta}
\kappa(\Delta)
e^{2\pi i k\Delta/L}.
\]

Therefore

\[
K\phi_k=\lambda_k\phi_k,
\]

with

\[
\lambda_k
=
\sum_{\Delta}
\kappa(\Delta)
e^{2\pi i k\Delta/L}.
\]

Since the Fourier basis is unitary,

\[
K
=
\sum_k
\lambda_k\phi_k\phi_k^\ast.
\]

## 5. DC mode

For k=0,

\[
\phi_0
=
L^{-1/2}\mathbf1,
\]

and

\[
\lambda_0
=
\sum_\Delta\kappa(\Delta).
\]

Hence

\[
K^{DC}
=
\lambda_0\phi_0\phi_0^\ast
=
\frac{\lambda_0}{L}
\mathbf1\mathbf1^\top.
\]

This operator acts on the constant sequence-index mode.

It contains no absolute position label.

## 6. Mode truncation

For a mode set S, define

\[
K_S
=
\sum_{k\in S}
\lambda_k\phi_k\phi_k^\ast.
\]

Then

\[
K-K_S
=
\sum_{k\notin S}
\lambda_k\phi_k\phi_k^\ast.
\]

Unitary invariance gives

\[
\|K-K_S\|_F^2
=
\sum_{k\notin S}
|\lambda_k|^2.
\]

Because \(K\) is normal, its singular values are \(|\lambda_k|\). When \(S\) omits at least one mode,

\[
\|K-K_S\|_2
=
\max_{k\notin S}|\lambda_k|.
\]

If \(S\) contains every mode, \(K_S=K\) and the spectral and Frobenius truncation errors are both zero. No maximum over an empty index set is needed.

Selecting the r largest magnitudes gives the best rank-at-most-r approximation under Frobenius and spectral norm for this cyclic normal operator.

This does not imply best downstream task performance.

## 7. Head-specific mode profile

For head h with nonzero energy,

\[
q_{h,k}
=
\frac{|\lambda_{h,k}|^2}
{\sum_j|\lambda_{h,j}|^2}.
\]

Then

\[
q_{h,k}\ge0,
\qquad
\sum_kq_{h,k}=1.
\]

This is a probability distribution over labeled sequence-index modes. For the zero operator all \(\lambda_{h,k}=0\), so the spectral-energy denominator vanishes; the normalized mode profile is undefined and should not be assigned an arbitrary distribution.

Its labels matter.

Sorting singular values discards those labels.

## 8. Exact head-A witness

Take L=4 and

\[
\kappa_A
=
\left(
1,\frac12,0,\frac12
\right).
\]

For k=0,

\[
\lambda_{A,0}
=
1+\frac12+0+\frac12
=
2.
\]

For k=1,

\[
\lambda_{A,1}
=
1+\frac12 i+\frac12(-i)
=
1.
\]

For k=2,

\[
\lambda_{A,2}
=
1-\frac12-\frac12
=
0.
\]

For k=3,

\[
\lambda_{A,3}=1.
\]

Therefore

\[
\lambda_A=(2,1,0,1).
\]

The squared magnitudes sum to

\[
4+1+0+1=6.
\]

Hence

\[
q_A
=
\left(
\frac23,\frac16,0,\frac16
\right).
\]

The head is DC-dominant under this positional-mode diagnostic.

## 9. Exact head-B witness

Let

\[
\kappa_B
=
\left(
1,-\frac12,0,-\frac12
\right).
\]

Then

\[
\lambda_B=(0,1,2,1).
\]

Again the squared magnitudes sum to 6, giving

\[
q_B
=
\left(
0,\frac16,\frac23,\frac16
\right).
\]

This head has zero DC component and is dominated by the k=2 Nyquist mode.

## 10. Same singular values, different mode identity

Both heads have singular values

\[
(2,1,1,0)
\]

as an unordered multiset.

But

\[
q_A\neq q_B.
\]

Therefore

\[
\text{unordered singular values}
\not\Rightarrow
\text{labeled positional-mode profile}.
\]

The missing information is the association between singular/eigenvalue magnitude and Fourier mode label.

## 11. Exact DC matrices

For head A,

\[
\lambda_{A,0}=2,
\qquad
\phi_0\phi_0^\ast
=
\frac14\mathbf1\mathbf1^\top.
\]

Thus

\[
K_A^{DC}
=
\frac12\mathbf1\mathbf1^\top.
\]

It has rank one.

The residual eigenvalues after retaining DC only are

\[
(0,1,0,1),
\]

so

\[
\|K_A-K_A^{DC}\|_F=\sqrt2,
\]

and

\[
\|K_A-K_A^{DC}\|_2=1.
\]

For head B,

\[
\lambda_{B,0}=0,
\]

so

\[
K_B^{DC}=0.
\]

Its DC-only errors are

\[
\|K_B\|_F=\sqrt6,
\qquad
\|K_B\|_2=2.
\]

The same truncation policy can therefore have very different approximation error across heads.

## 12. Relative-bias operator versus attention

Suppose a head has an additive relative-position logit bias

\[
B_h(i,j)=b_h(j-i).
\]

Under cyclic unbucketed assumptions, \(B_h\) can be treated as a circulant relative-position operator.

But full attention logits are content dependent:

\[
L_h
=
Q_hK_h^\top/\sqrt d+B_h.
\]

The attention weights are

\[
A_h
=
\operatorname{softmax}(L_h).
\]

Because content logits and softmax enter, diagonalizing \(B_h\) does not diagonalize \(A_h\) in general.

Thus the relative-position operator is a component of attention, not the whole attention operator.

## 13. RoPE frequency versus sequence frequency

RoPE frequencies \(\omega_a\) index 2D rotation blocks in feature coordinates.

Sequence-index Fourier modes k diagonalize a translation-invariant operator over positions.

These are different spaces.

A mathematical relation between them requires a declared construction.

No notation should imply they are automatically identical.

## 14. Head-specific positional specialization

T5 provides a source-scoped architectural precedent in which different heads within a layer use different learned relative-position embeddings/biases.

For an Atlas diagnostic, head-specific positional specialization can therefore mean a difference among the declared operators \(K_h\) or their mode profiles \(q_h\).

This remains positional-operator specialization.

It does not prove that one head is semantically specialized, necessary, or causally sufficient for a task.

## 15. Downstream handoff

ATLAS-CH-LATENTTIME-001 may inherit:

- feature-space relative-offset operators;
- cyclic sequence-index relative-position operators;
- Fourier mode and DC decomposition;
- exact norm formulas for mode truncation;
- head-specific positional-mode profiles;
- the exact two-head witness.

LATENTTIME must independently define latent temporal coordinates, asynchronous alignment, dynamic time warping or alternatives, and the mapping from observed position differences to inferred time.

## Claim boundary

This packet proves the displayed finite cyclic-operator identities and exact four-position witnesses.

It does not establish that production attention is circulant, that periodic boundaries are realistic for every task, that Fourier truncation preserves task performance, or that positional-mode concentration is semantic specialization.
