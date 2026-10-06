# Chapter Specification — ATLAS-CH-RPO-001

## Identity

**Title:** Relative-Position Operators  
**Part:** Attention, Sequence, and Position  
**Status:** specification-ready.  
**Epistemic class:** audited Positional Geometry and Linear Algebra prerequisites + primary relative-position sources + Atlas synthesis.

## Contract

Move from positional vectors to low-dimensional relative-position operators, frequency modes, DC components, and head-specific specialization.

The chapter must distinguish:

- feature-space relative-position operators from sequence-index relative-position operators;
- relative-position logit biases from the full content-dependent attention operator;
- finite nonperiodic Toeplitz structure from cyclic/circulant structure;
- frequency labels from unordered singular-value summaries;
- the zero-frequency/DC component from absolute position;
- positional-operator specialization from semantic or causal head specialization;
- exact mode truncation error from downstream task performance.

## Hard prerequisites

- ATLAS-CH-POSGEOM-001
- ATLAS-CH-LINALG-001

Exact prerequisite identities and source authority are locked in:

\`sources/source-locks/ATLAS-CH-RPO-001.yaml\`.

## Feature-space relative operator

From the audited RoPE geometry, let

\[
R(\theta)
=
\begin{pmatrix}
\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta
\end{pmatrix}.
\]

For frequencies \(\omega_1,\ldots,\omega_m\), define

\[
\rho(\Delta)
=
\bigoplus_{a=1}^{m}
R(\omega_a\Delta).
\]

Then

\[
\rho(\Delta_1)\rho(\Delta_2)
=
\rho(\Delta_1+\Delta_2),
\qquad
\rho(0)=I.
\]

This is a low-dimensional operator representation of relative offset in feature coordinates.

If one block has \(\omega_a=0\), then that block is

\[
R(0\cdot\Delta)=I
\]

for every \(\Delta\). This is a feature-space DC block.

The existence of a zero-frequency block is a modeling choice, not an automatic property of RoPE implementations.

## Sequence-index relative-position operator

Let sequence positions form the cyclic group

\[
\mathbb Z_L.
\]

For head h, let

\[
\kappa_h:\mathbb Z_L\to\mathbb C
\]

be a declared translation-invariant relative-position kernel.

Define

\[
(K_h x)_i
=
\sum_{\Delta=0}^{L-1}
\kappa_h(\Delta)\,
x_{i+\Delta\;\mathrm{mod}\;L}.
\]

Then \(K_h\) is circulant.

This cyclic model is an exact algebraic witness. It must not be silently substituted for finite nonperiodic sequence boundaries, where relative-position matrices are generally Toeplitz-like rather than circulant.

## Fourier modes

Define

\[
\phi_k(n)
=
L^{-1/2}
e^{2\pi i kn/L},
\qquad
k=0,\ldots,L-1.
\]

Then

\[
K_h\phi_k
=
\lambda_{h,k}\phi_k,
\]

with

\[
\lambda_{h,k}
=
\sum_{\Delta=0}^{L-1}
\kappa_h(\Delta)
e^{2\pi i k\Delta/L}.
\]

Thus

\[
K_h
=
\sum_{k=0}^{L-1}
\lambda_{h,k}\phi_k\phi_k^\ast.
\]

## DC component

The zero-frequency mode is

\[
\phi_0
=
L^{-1/2}\mathbf 1.
\]

Its eigenvalue is

\[
\lambda_{h,0}
=
\sum_{\Delta}
\kappa_h(\Delta).
\]

The DC operator is

\[
K_h^{DC}
=
\lambda_{h,0}\phi_0\phi_0^\ast
=
\frac{\lambda_{h,0}}{L}
\mathbf 1\mathbf 1^\top.
\]

This is the constant sequence-index mode.

It is not an absolute-position embedding.

## Low-dimensional mode reduction

For a selected mode set

\[
S\subseteq\{0,\ldots,L-1\},
\]

define

\[
K_{h,S}
=
\sum_{k\in S}
\lambda_{h,k}\phi_k\phi_k^\ast.
\]

Because a circulant matrix is normal and the Fourier basis is unitary,

\[
\|K_h-K_{h,S}\|_F^2
=
\sum_{k\notin S}
|\lambda_{h,k}|^2.
\]

Also,

\[
\|K_h-K_{h,S}\|_2
=
\max_{k\notin S}
|\lambda_{h,k}|.
\]

Retaining the r modes with largest \(|\lambda_{h,k}|\) gives a best rank-at-most-r approximation in these unitarily invariant senses for the cyclic normal operator.

This is an operator approximation statement, not a task-performance theorem.

## Head-specific positional-mode profile

For head h with nonzero operator energy, define

\[
q_{h,k}
=
\frac{|\lambda_{h,k}|^2}
{\sum_j|\lambda_{h,j}|^2}.
\]

Then

\[
q_h
\]

is a probability distribution over sequence-index Fourier modes.

It measures where the relative-position operator places spectral energy.

It does not by itself establish semantic or causal head specialization.

## Exact two-head witness

Take

\[
L=4.
\]

Head A has kernel

\[
\kappa_A
=
\left(
1,\frac12,0,\frac12
\right).
\]

Its Fourier eigenvalues are

\[
\lambda_A=(2,1,0,1).
\]

Head B has kernel

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

Therefore both heads have the same unordered singular-value multiset

\[
(2,1,1,0),
\]

but their labeled frequency profiles differ.

For head A,

\[
q_A=
\left(
\frac23,\frac16,0,\frac16
\right),
\]

while for head B,

\[
q_B=
\left(
0,\frac16,\frac23,\frac16
\right).
\]

Head A is DC-dominant in this toy witness.

Head B is Nyquist-mode dominant.

Thus:

\[
\text{same singular values}
\not\Rightarrow
\text{same positional-frequency specialization}.
\]

## Exact DC witness

For head A,

\[
K_A^{DC}
=
\frac12
\mathbf 1\mathbf 1^\top.
\]

Its rank is one.

The DC-only Frobenius approximation error is

\[
\sqrt{1^2+0^2+1^2}
=
\sqrt2.
\]

For head B,

\[
\lambda_{B,0}=0,
\]

so its DC operator is zero.

A DC-only approximation to head B has Frobenius error

\[
\sqrt{0^2+1^2+2^2+1^2}
=
\sqrt6.
\]

The same truncation rule can therefore have very different approximation quality across heads.

## Relative bias versus full attention

A learned relative-position bias can define a matrix

\[
B_h(i,j)=b_h(j-i)
\]

under a declared clipping/bucketing rule.

This matrix may be studied as a relative-position operator.

But if full attention logits are

\[
L_h=Q_hK_h^\top/\sqrt d+B_h,
\]

then

\[
\operatorname{softmax}(L_h)
\]

is content-dependent and nonlinear in the combined logits.

The Fourier decomposition of \(B_h\) does not automatically diagonalize the full attention map.

## Head-specific architecture precedent

Shaw et al. provide primary precedent for relative-position representations inside self-attention.

T5 provides primary precedent for scalar relative-position biases added to attention logits and for different learned relative-position embeddings across attention heads.

The Atlas operator/Fourier decomposition is not attributed to either paper.

## Failure boundaries

- relative-position vector != relative-position operator;
- RoPE feature-space frequency != sequence-index Fourier mode;
- relative-bias matrix != full attention operator;
- Toeplitz-like finite-boundary structure != circulant structure;
- DC mode != absolute position;
- large DC energy != head importance;
- mode concentration != semantic specialization;
- same singular values != same labeled frequency profile;
- low-rank operator approximation != preserved task behavior;
- cyclic witness != universal sequence-boundary model;
- head-specific relative bias != proof that every head specializes positionally;
- exact Fourier algebra != long-context generalization theorem.

## Downstream handoff

Direct consumer:

- ATLAS-CH-LATENTTIME-001.

LATENTTIME may inherit:

- feature-space relative-position operators;
- sequence-index relative-position kernels;
- Fourier-mode and DC decomposition;
- low-dimensional mode truncation with exact norm errors;
- head-specific positional-mode profiles;
- the exact two-head counterexample separating singular values from labeled frequencies.

LATENTTIME must independently define inferred/latent time, alignment between asynchronous sequences, dynamic time warping or alternative alignment operators, and the relationship between observed relative position and latent temporal coordinate.

## Sources

- [@ShawUszkoreitVaswani2018Relative]
- [@RaffelEtAl2020T5]

Exact source authority and claim boundaries are locked in:

\`sources/source-locks/ATLAS-CH-RPO-001.yaml\`.
