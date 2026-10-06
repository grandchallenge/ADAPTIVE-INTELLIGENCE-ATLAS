# AUDIT-052 — Tokenization and Representation Boundaries

## Disposition

**PASS — NO REPAIR**

ATLAS-CH-TOKEN-001 remains at `draft-v0.1`.

No mathematical, witness, source-scope, provenance, reader-maturity, fertility, morphology, multilingual-boundary, or downstream-boundary defect requiring repair was found.

This audit does not promote the chapter to publication-ready, certified, or final-copy status.

## Audited implementation

- implementation issue: #207
- implementation PR: #208
- exact green implementation head: `4fc0bedf5ccf21aec4fe390d1531eb0a26aa5f58`
- implementation merge: `d51ad8b0bd05d7457a635c71325b129cdc0ef866`
- audit issue: #209
- audit branch: `audit/token-209`
- chapter: `ATLAS-CH-TOKEN-001`

Implementation artifact identities:

- specification: `f87dce93093efe26e2483195f294e98c7016adf6`
- manuscript: `07c1edd5103ff179bbb3727ede9c4e15f2ec949a`
- derivation: `0161b85fda989ac828ff968b6edb44ad4c4f7fa4`
- witness: `f8004ba6abf348a001fbdb918bfaac3bb1452e21`
- source lock: `616c92bb63ed33e5c5587b3fe4491ae21a0eba54`
- Chapter Ledger: `0f7f83a0dc5664fecec910c6c4210e271153a206`
- Source Register: `ae57731f36bc10b9c0c718b06b800e7fbc0e00cc`
- bibliography: `d162e7ba05c510a6d1580bbfec714141d9325f62`

## 1. Hard prerequisites

PASS.

Information exact binds:

- manuscript: `0fca10cbc7476c5b729ee15dfad0dec563665821`
- source lock: `ea5a1b0db3aadf052fc0b749d7e813bb0ca5d43c`
- AUDIT-004: `948f76b3f86d27fa4830efc30d8ef0135134256e`

Representations exact binds:

- manuscript: `6109e6ac9505a339cb8bc2dd85a8b9bc882f72bb`
- source lock: `dfe9176c458a56ca5cda5f258c440aea52f9b9fa`
- AUDIT-004: `948f76b3f86d27fa4830efc30d8ef0135134256e`

The chapter preserves the inherited firewall that information quantities require a declared probability model and that coordinates/representations are not semantics.

## 2. External source scope

PASS.

Sennrich et al. (2016) are used only for BPE-inspired subword NMT and rare-word/open-vocabulary motivation.

Kudo (2018) is used for unigram-language-model segmentation and subword regularization.

Kudo and Richardson (2018) are used for SentencePiece's raw-sentence, language-independent tokenizer/detokenizer framework.

Xue et al. (2022) are used for byte-level modeling and the reported robustness/sequence-length/compute trade-offs.

Rust et al. (2021) are used for controlled multilingual evidence that tokenizer adequacy can affect downstream performance.

No source is promoted to a universal tokenizer optimum.

## 3. Typed boundary ladder

PASS.

The chapter explicitly separates bytes, Unicode codepoints, grapheme-like visible characters, words under a declared convention, subwords, token IDs, and embeddings.

It does not equate counts or semantics across these levels.

## 4. Unicode witness

PASS.

Independent replay gives:

- NFC `é`: 1 codepoint, 2 UTF-8 bytes;
- decomposed `e` + U+0301: 2 codepoints, 3 UTF-8 bytes.

The chapter correctly uses this only to separate byte/codepoint/normalization boundaries and does not claim codepoint count equals grapheme count.

## 5. Segmentation-ambiguity witness

PASS.

For `abab` with piece probabilities

\[
p(ab)=1/2,\qquad p(a)=p(b)=1/4,
\]

the four declared segmentation weights replay as

\[
(1/4,1/32,1/32,1/256).
\]

The normalization constant is

\[
81/256,
\]

and the conditional probabilities are

\[
(64/81,8/81,8/81,1/81).
\]

The highest-probability segmentation is therefore not the only legal segmentation under the declared model.

## 6. Token count versus description length

PASS.

Under the declared toy token model:

- two tokens at probability `1/16` each give 8 bits;
- three tokens at probability `1/2` each give 3 bits.

Thus fewer tokens need not imply smaller model-based description length.

This correctly preserves the Information prerequisite's probability-model dependency.

## 7. Fertility

PASS.

The corpus-scoped definition

\[
F_\tau(C)=\frac{\sum_x|\tau(x)|}{W(C)}
\]

is well-typed relative to a declared reference-word segmentation.

The exact toy witness gives fertility `2.5` versus `1.0`.

The chapter explicitly denies the stronger claims that fertility is a language constant, a measure of language complexity, or a complete compute/performance metric.

## 8. Morphological boundary diagnostic

PASS.

Boundary precision/recall are defined relative to a declared morphological analysis.

The chapter correctly treats morphology alignment as a diagnostic rather than a theorem of tokenizer quality.

## 9. BPE/unigram/SentencePiece boundaries

PASS.

The chapter separates:

- BPE merge state/order from the vocabulary alone;
- unigram piece scoring from deterministic or sampled segmentation inference;
- SentencePiece's removal of mandatory conventional word pretokenization from the remaining normalization/segmentation choices.

The algorithms are not collapsed into one generic subword method.

## 10. Byte-level boundary

PASS.

The manuscript explains the byte-level coverage advantage under a complete byte alphabet while retaining the sequence-length and compute trade-off.

It does not interpret byte-level modeling as representation-free text processing.

## 11. Multilingual boundary

PASS.

The chapter requires corpus-scoped measurement of fertility, coverage, byte/codepoint expansion, morphology alignment, and downstream behavior.

Tokenizer adequacy is treated as one factor among data, model, training, vocabulary allocation, and task effects.

No single-cause explanation is claimed.

## 12. Representation interface

PASS.

Token IDs are treated as discrete coordinates indexing learned embeddings, not as semantic objects.

Changing segmentation is correctly identified as a different intervention from merely permuting IDs and correspondingly permuting an embedding table.

## 13. Bibliography and provenance

PASS.

The declared bibliography keys resolve:

- `SennrichHaddowBirch2016BPE`;
- `Kudo2018SubwordRegularization`;
- `KudoRichardson2018SentencePiece`;
- `XueEtAl2022ByT5`;
- `RustEtAl2021Tokenizer`.

The Source Register contains `ATLAS-SRC-TOKEN-LOCK-001`.

The Chapter Ledger binds specification, reader, derivation, source lock, and computational witness paths at `draft-v0.1`.

Canonical Linux validation passed on the exact implementation head before merge, and exact-head GitHub validation also passed.

## 14. Reader maturity

PASS.

The reader contains:

- the representation-boundary obstruction;
- deterministic and stochastic tokenization objects;
- byte/codepoint normalization witness;
- BPE, unigram, SentencePiece, and byte-level distinctions;
- fertility and code-length diagnostics;
- morphology and multilingual boundaries;
- representation-interface consequences;
- controlled comparison obligations;
- direct TOKENCOMP handoff;
- epistemic status, references, and source-lock pointer.

## 15. TOKENCOMP handoff

PASS.

ATLAS-CH-TOKENCOMP-001 may inherit typed tokenization boundaries, fertility, probability-model code length, segmentation ambiguity, morphology diagnostics, multilingual measurement, and the exact finite witnesses.

TOKEN does not pre-claim the downstream compression/compute/interoperability or tokenizer-lingua-franca conclusions.

## Final audit boundary

The durable separations are:

\[
\text{token count}\ne\text{description length},
\]

\[
\text{fertility}\ne\text{language complexity},
\]

and

\[
\text{tokenizer representation}\ne\text{semantics}.
\]

No repair is required.

The next legitimate operation is exact-head canonical validation of this audit record, audit PR merge, final main validation, frontier recomputation, issue closure, and controller/handoff reset.
