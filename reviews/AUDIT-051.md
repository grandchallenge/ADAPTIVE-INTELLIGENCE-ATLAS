# AUDIT-051 — Relative-Position Operators

## Disposition

**PASS — NO REPAIR**

ATLAS-CH-RPO-001 remains at \`draft-v0.1\`.

No mathematical, witness, source-scope, provenance, reader-maturity, operator-space, Fourier/DC, head-specialization, or downstream-boundary defect requiring repair was found.

This audit does not promote the chapter to publication-ready, certified, or final-copy status.

## Audited implementation

- implementation issue: #203
- implementation PR: #204
- exact green implementation head: \`481a814e2690940979f09de8b150aa18256c7162\`
- implementation merge: \`d43ac5950888c47028d9a5613838f8838ddcb173\`
- audit issue: #205
- audit branch: \`audit/rpo-205\`
- chapter: \`ATLAS-CH-RPO-001\`

Implementation artifact identities:

- specification: \`a7b3df8b55595a4317885949009e0983af6aba98\`
- manuscript: \`0483a358aa486aab5ae213e05b5bbd23161e021d\`
- derivation: \`db0189517f44c072ef6032fce94123eb41975e43\`
- witness: \`8eda34332e831248df2f6d04e962adfb44de2a07\`
- source lock: \`9ad49c8e7950fa4e534c3083500fbdac288127a9\`
- Chapter Ledger: \`3a76d54c79f08629974481f925ec25f4bb5d3f1c\`
- Source Register: \`bda0d392d91466edece5b2a52235d562e1f75baf\`
- bibliography: \`15fcf790c0919bdda4b46afaedfb5aee69a2821a\`
- transaction receipt: \`ed4d36ba18f77a968e4b0f99c0f1bd8829b19ec4\`

## 1. Hard prerequisites

PASS.

Positional Geometry exact binds:

- manuscript: \`841bc96c696e58fb7914c851c7c13f2e5d076b53\`
- source lock: \`a94a592d68a5f6ddadf450127dde0e261acf429f\`
- AUDIT-040: \`6c33d4994d683e953a70813ed422e8d887b67a02\`

Linear Algebra exact binds:

- manuscript: \`e7fcf56322f26d232d3a3043038d9850792b4bde\`
- source lock: \`f24e93ee0c2496ca0b9d71f6f824b0d13dbdc08e\`
- AUDIT-004: \`948f76b3f86d27fa4830efc30d8ef0135134256e\`

The chapter inherits only audited rotation/relative-offset geometry and standard finite-dimensional operator/decomposition discipline.

## 2. External source scope

PASS.

Shaw, Uszkoreit, and Vaswani (2018) are used only as a primary architectural precedent for relative-position representations in self-attention.

Raffel et al. (2020) are used only as a primary precedent for scalar relative-position attention bias and different learned relative-position embeddings across heads.

The Fourier/DC/operator decomposition is explicitly Atlas-owned and is not attributed to those sources.

## 3. Feature-space relative operator

PASS.

The chapter defines

\[
\rho(\Delta)
=
\bigoplus_a R(\omega_a\Delta)
\]

and preserves the exact group law

\[
\rho(\Delta_1)\rho(\Delta_2)
=
\rho(\Delta_1+\Delta_2).
\]

It correctly treats any \(\omega=0\) block as a feature-space zero-frequency block and does not assert that all RoPE implementations contain such a block.

## 4. Sequence-index operator

PASS.

The cyclic operator

\[
(K_hx)_i
=
\sum_\Delta
\kappa_h(\Delta)
x_{i+\Delta\;\mathrm{mod}\;L}
\]

is explicitly scoped to the declared periodic boundary.

The text separately warns that finite nonperiodic relative-position matrices are generally Toeplitz-like rather than circulant.

## 5. Fourier diagonalization and DC

PASS.

The chapter derives

\[
K_h\phi_k
=
\lambda_{h,k}\phi_k
\]

with

\[
\lambda_{h,k}
=
\sum_\Delta
\kappa_h(\Delta)e^{2\pi i k\Delta/L}.
\]

The zero-frequency component is

\[
K_h^{DC}
=
\frac{\lambda_{h,0}}{L}
\mathbf1\mathbf1^\top.
\]

DC is correctly identified as the constant sequence-index mode and is not conflated with absolute position.

## 6. Low-dimensional truncation

PASS.

For a selected mode set S, the chapter gives

\[
\|K_h-K_{h,S}\|_F^2
=
\sum_{k\notin S}|\lambda_{h,k}|^2
\]

and

\[
\|K_h-K_{h,S}\|_2
=
\max_{k\notin S}|\lambda_{h,k}|.
\]

The best-rank statement is correctly scoped to the cyclic normal operator and unitarily invariant operator approximation, not downstream task quality.

## 7. Exact two-head witness

PASS.

Independent replay gives head A:

- eigenvalues: \((2,1,0,1)\);
- mode-energy profile: \((2/3,1/6,0,1/6)\);
- DC-only Frobenius error: \(\sqrt2\).

Head B:

- eigenvalues: \((0,1,2,1)\);
- mode-energy profile: \((0,1/6,2/3,1/6)\);
- DC-only Frobenius error: \(\sqrt6\).

Both have the same unordered singular-value multiset:

\[
(2,1,1,0).
\]

Therefore the witness correctly separates singular-value magnitude from labeled positional-mode identity.

## 8. Head-specific specialization boundary

PASS.

The chapter defines head-specific positional-mode profiles as spectral-energy distributions over labeled sequence modes.

It explicitly denies the stronger inference from positional-mode concentration to semantic importance, task necessity, or causal specialization.

## 9. Relative bias versus full attention

PASS.

The reader keeps a learned relative-position bias operator separate from the full content-dependent attention logits and softmax map.

Diagonalizing the positional bias is not claimed to diagonalize the full attention mechanism.

## 10. RoPE frequency versus sequence Fourier frequency

PASS.

The manuscript states that RoPE frequencies index rotations in feature coordinates while sequence-index Fourier modes diagonalize translation-invariant positional operators over positions.

The two decompositions are not silently identified.

## 11. Bibliography and provenance

PASS.

The declared bibliography keys resolve:

- \`ShawUszkoreitVaswani2018Relative\`;
- \`RaffelEtAl2020T5\`.

The Source Register contains \`ATLAS-SRC-RPO-LOCK-001\`.

The Chapter Ledger binds specification, reader, derivation, source lock, and witness paths.

## 12. Reader maturity

PASS.

The reader includes:

- the operator-space obstruction;
- feature-space and sequence-index operator definitions;
- Fourier and DC derivations;
- low-dimensional truncation;
- exact two-head witness;
- head-specific specialization boundary;
- finite-boundary/circulant warning;
- relative-bias versus full-attention distinction;
- direct LATENTTIME handoff;
- epistemic status, references, and source-lock pointer.

## 13. LATENTTIME handoff

PASS.

ATLAS-CH-LATENTTIME-001 may inherit relative-position operators, Fourier/DC decomposition, truncation errors, head-specific positional-mode profiles, and the exact finite witness.

RPO does not pre-claim latent temporal coordinates, asynchronous alignment, dynamic time warping, or the mapping from sequence offset to inferred time.

## Final audit boundary

The durable result is:

\[
\text{same singular values}
\not\Rightarrow
\text{same labeled positional-frequency structure}.
\]

The companion boundary is:

\[
\text{relative-position operator}
\ne
\text{full content-dependent attention operator}.
\]

No repair is required.

The next legitimate operation is exact-head canonical validation of this audit record, audit PR merge, final main validation, frontier recomputation, issue closure, and controller/handoff reset.
