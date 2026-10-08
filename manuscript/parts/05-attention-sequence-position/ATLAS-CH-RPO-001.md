# Relative-Position Operators
<!-- ATLAS-CH-RPO-001 -->

**Epistemic status:** audited Positional Geometry/Linear Algebra prerequisites + primary relative-position sources + Atlas synthesis + exact finite witness  
**Specification:** manuscript/specifications/ATLAS-CH-RPO-001.md  
**Derivation packet:** mathematics/derivations/ATLAS-CH-RPO-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-RPO-001.md

Position can enter a Transformer as a vector.

It can also enter as an operator.

That shift matters because an operator can be decomposed into modes, projected, truncated, compared across heads, and composed with other structure. The chapter develops that viewpoint without pretending that every positional mechanism is the same object.

## 1. Two spaces, two frequency notions

The audited Positional Geometry chapter already gives a precise RoPE identity.

For a relative offset \(\Delta\), one can write a feature-space operator

\[
\rho(\Delta)
=
\bigoplus_a R(\omega_a\Delta),
\]

where each \(R(\omega_a\Delta)\) is a 2D rotation block.

Those frequencies live in feature coordinates.

This chapter also studies translation-invariant operators over sequence index.

Those operators have Fourier modes over positions.

The two frequency notions are not automatically the same.

That distinction is the first discipline of RPO.

## 2. Relative position as an operator over sequence index

Suppose positions lie on the cyclic set

\[
\mathbb Z_L.
\]

For one attention head, define a relative-position kernel

\[
\kappa_h(\Delta).
\]

Then let

\[
(K_hx)_i
=
\sum_{\Delta=0}^{L-1}
\kappa_h(\Delta)
x_{i+\Delta\;\mathrm{mod}\;L}.
\]

This is a circulant linear operator.

The periodic boundary is deliberate.

It makes the algebra exact.

It is not a claim that real language sequences wrap around from the end to the beginning.

For ordinary finite nonperiodic sequences, a relative-position matrix is generally Toeplitz-like rather than circulant.

## 3. Why the Fourier basis appears

A circulant operator commutes with cyclic shifts.

The natural basis is therefore the Fourier basis

\[
\phi_k(n)
=
L^{-1/2}
e^{2\pi i kn/L}.
\]

Each mode is an eigenvector:

\[
K_h\phi_k
=
\lambda_{h,k}\phi_k,
\]

with

\[
\lambda_{h,k}
=
\sum_{\Delta}
\kappa_h(\Delta)
e^{2\pi i k\Delta/L}.
\]

So the operator becomes

\[
K_h
=
\sum_k
\lambda_{h,k}
\phi_k\phi_k^\ast.
\]

This is the core low-dimensional operator view.

A relative-position rule becomes a collection of labeled mode gains.

## 4. The DC mode

The zero-frequency mode is

\[
\phi_0
=
L^{-1/2}\mathbf1.
\]

Its eigenvalue is

\[
\lambda_{h,0}
=
\sum_\Delta \kappa_h(\Delta).
\]

The corresponding operator is

\[
K_h^{DC}
=
\frac{\lambda_{h,0}}{L}
\mathbf1\mathbf1^\top.
\]

It acts on the constant sequence-index mode.

This is what DC means here.

It is not an absolute-position embedding.

It contains no distinguished position label.

## 5. RoPE can have a feature-space DC block too

There is a parallel feature-space idea.

If a RoPE-style block uses

\[
\omega=0,
\]

then

\[
R(\omega\Delta)=I
\]

for every offset.

That block is offset-invariant.

It is natural to call it a zero-frequency feature-space block.

But it is still not the same object as the sequence-index Fourier DC mode.

One lives in feature coordinates.

The other lives over positions.

## 6. Low-dimensional operator reduction

Suppose only a subset of Fourier modes is retained:

\[
S\subseteq\{0,\ldots,L-1\}.
\]

Define

\[
K_{h,S}
=
\sum_{k\in S}
\lambda_{h,k}
\phi_k\phi_k^\ast.
\]

For a circulant operator,

\[
\|K_h-K_{h,S}\|_F^2
=
\sum_{k\notin S}
|\lambda_{h,k}|^2,
\]

and, when at least one mode is omitted,

\[
\|K_h-K_{h,S}\|_2
=
\max_{k\notin S}
|\lambda_{h,k}|.
\]

If \(S=\{0,\ldots,L-1\}\), no mode is omitted and \(K_{h,S}=K_h\); both errors are exactly zero. This avoids interpreting a maximum over the empty set as a numerical value.

These are exact approximation statements.

They do not imply that the truncated operator preserves downstream language-model quality.

An operator norm is not a task metric.

## 7. Relative position in actual attention architectures

Shaw, Uszkoreit, and Vaswani introduced relative-position representations directly into self-attention rather than relying only on absolute input-position representations [@ShawUszkoreitVaswani2018Relative].

T5 uses a simpler relative-position mechanism: a learned scalar positional bias is added to attention logits, and different heads within a layer use different learned relative-position embeddings [@RaffelEtAl2020T5].

These architectures motivate an operator question:

> what positional operator does each head implement before content-dependent attention is applied?

The Atlas answers that question mathematically without claiming the papers themselves performed the Fourier decomposition developed here.

## 8. Relative bias is not full attention

Suppose a head has relative-position logit bias

\[
B_h(i,j)
=
b_h(j-i).
\]

That positional component can be studied as an operator.

But the full attention logits are

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

The content term changes from input to input.

Softmax is nonlinear.

Therefore diagonalizing the positional bias does not diagonalize the full attention mechanism in general.

This chapter diagnoses one component of attention, not the entire head.

## 9. Head-specific positional mode profiles

For a head \(h\) whose declared relative-position operator is nonzero, so that \(\sum_j|\lambda_{h,j}|^2>0\), define

\[
q_{h,k}
=
\frac{|\lambda_{h,k}|^2}
{\sum_j|\lambda_{h,j}|^2}.
\]

This is a probability distribution over labeled sequence-index modes. When \(K_h=0\), the denominator vanishes and the normalized profile is undefined; report a zero-energy operator instead of assigning it a fictitious frequency preference.

It answers a narrow question:

> where does this head's relative-position operator place its spectral energy?

That is a useful notion of positional specialization.

It is not yet semantic specialization.

It does not tell us whether the head is causally necessary for a task.

## 10. Exact two-head witness

Take four cyclic positions.

Head A has kernel

\[
\kappa_A
=
\left(
1,\frac12,0,\frac12
\right).
\]

Its mode eigenvalues are

\[
\lambda_A=(2,1,0,1).
\]

Head B has

\[
\kappa_B
=
\left(
1,-\frac12,0,-\frac12
\right),
\]

with

\[
\lambda_B=(0,1,2,1).
\]

Both heads have the same unordered singular values:

\[
(2,1,1,0).
\]

If we looked only at the singular-value multiset, they would appear identical.

But the mode labels reveal a sharp difference.

## 11. One head is DC-dominant

Head A has energy profile

\[
q_A
=
\left(
\frac23,\frac16,0,\frac16
\right).
\]

Two-thirds of its spectral energy lies in the DC mode.

Its DC component is

\[
K_A^{DC}
=
\frac12
\mathbf1\mathbf1^\top.
\]

A DC-only approximation has Frobenius error

\[
\sqrt2.
\]

## 12. The other head is Nyquist-dominant

Head B has

\[
q_B
=
\left(
0,\frac16,\frac23,\frac16
\right).
\]

Its DC eigenvalue is zero.

Two-thirds of its spectral energy lies in the \(k=2\) mode, the Nyquist mode on four cyclic positions.

A DC-only approximation is therefore the zero operator and has Frobenius error

\[
\sqrt6.
\]

The same approximation strategy can be reasonable for one head and useless for another.

## 13. Singular values lose mode identity

The witness gives the chapter's main finite warning:

\[
\boxed{
\text{same singular values}
\not\Rightarrow
\text{same positional-frequency specialization}
}
\]

Singular values retain magnitude.

They do not retain which Fourier mode carries that magnitude.

For positional operators, the label can be the interesting part.

## 14. Head specialization needs a qualifier

T5 gives an architectural precedent for different relative-position parameters across heads.

That does not mean every head develops a meaningful positional role.

A head-specific profile can differ because of:

- initialization;
- optimization;
- architecture;
- redundancy;
- incidental parameterization;
- genuinely useful positional structure.

Therefore this chapter uses the phrase **positional-operator specialization**.

Semantic or causal specialization requires additional evidence.

## 15. The DC component is not always desirable

A large DC component means strong response to the constant sequence-index mode.

That may be useful.

It may also be an uninformative offset-like component.

The meaning depends on how the positional operator enters the model.

RPO therefore reports DC energy before interpreting it.

## 16. Boundary conditions matter

The Fourier diagonalization above is exact because the toy operator is circulant.

Real relative-position schemes may use:

- finite clipping;
- logarithmic buckets;
- causal masks;
- nonperiodic boundaries;
- asymmetric left/right treatment;
- context-length-dependent rules.

Those operations break or modify simple circulant structure.

The right generalization may involve Toeplitz analysis, block structure, finite-section operators, or numerical spectral diagnostics rather than a single exact DFT.

## 17. Bucketing is an operator approximation too

T5 maps ranges of relative offsets into shared learned buckets.

That can be viewed as reducing the degrees of freedom of the positional operator.

But bucket reduction is not the same as Fourier truncation.

One constrains the kernel in offset space.

The other constrains it in mode space.

The two approximations preserve different structures.

## 18. Frequency truncation can be head-specific

Suppose a system wants a low-dimensional positional operator.

A global rule such as “keep the DC mode first” can fail badly when different heads emphasize different modes.

The exact witness makes this concrete:

- head A: DC-only error \(\sqrt2\);
- head B: DC-only error \(\sqrt6\).

A head-specific reduction can therefore be mathematically better even before any task-specific evaluation is considered.

## 19. Multi-frequency RoPE and sequence modes should not be collapsed

RoPE already uses multiple frequencies.

RPO also uses multiple sequence-index Fourier modes.

The notation can look temptingly similar.

But the two decompositions diagonalize different actions.

RoPE blocks encode relative phase in feature coordinates.

Sequence Fourier modes diagonalize a translation-invariant operator acting across positions.

A model can contain both structures at once.

## 20. What a positional-operator diagnostic should record

At minimum:

- the space on which the operator acts;
- the sequence boundary convention;
- the relative-position kernel or bias rule;
- clipping or bucketing;
- whether the operator is before or after content interaction;
- the head/layer identity;
- the basis used for decomposition;
- retained mode labels, not only sorted magnitudes;
- the norm used for approximation error;
- any task metric used to interpret the approximation.

Without these fields, “low-frequency positional behavior” can refer to several different mathematical objects.

## 21. Handoff to Latent Clocks

Observed sequence position and latent time are not the same thing.

But relative-position operators supply useful structure for asking whether a model treats some offsets as equivalent, periodic, slowly varying, or high-frequency.

ATLAS-CH-LATENTTIME-001 may inherit:

- feature-space relative-offset operators;
- sequence-index relative-position kernels;
- Fourier-mode decomposition;
- DC components;
- exact low-dimensional truncation errors;
- head-specific positional-mode profiles;
- the finite example separating singular values from labeled frequencies.

LATENTTIME must add the inference problem:

> when do observed sequence offsets correspond to an underlying latent temporal coordinate, and how should asynchronous or warped sequences be aligned?

## 22. Durable lesson

A positional mechanism is easier to reason about once we ask:

\[
\text{what operator acts on what space?}
\]

Then frequency, DC structure, truncation, and head-specific variation become typed mathematical questions instead of metaphors.

The operator view does not replace empirical evaluation.

It makes the positional object explicit enough to evaluate.

## References used in this chapter

- [@ShawUszkoreitVaswani2018Relative]
- [@RaffelEtAl2020T5]

Exact source authority, prerequisite identities, and claim boundaries are locked in:

sources/source-locks/ATLAS-CH-RPO-001.yaml
