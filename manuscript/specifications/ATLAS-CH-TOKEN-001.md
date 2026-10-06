# Chapter Specification — ATLAS-CH-TOKEN-001

## Identity

**Title:** Tokenization and Representation Boundaries  
**Part:** Tokenization, Data, and Curriculum  
**Status:** specification-ready.  
**Epistemic class:** audited Information/Representation prerequisites + primary tokenizer sources + Atlas synthesis.

## Contract

Develop bytes, characters/codepoints, subwords, BPE, unigram methods, morphology, fertility, and multilingual effects while treating tokenization as an explicit representation boundary.

## Hard prerequisites

- `ATLAS-CH-INFO-001`
- `ATLAS-CH-REP-001`

Exact prerequisite identities and source authority are locked in:

`sources/source-locks/ATLAS-CH-TOKEN-001.yaml`.

## Tokenization object

For normalized text space \(\mathcal X\) and vocabulary \(V\), a deterministic tokenizer is a map

\[
\tau:\mathcal X\to V^*.
\]

A stochastic tokenizer is a conditional distribution

\[
q_\tau(s\mid x),\qquad s\in\operatorname{Seg}_V(x),
\]

on valid segmentations of \(x\).

Detokenization is a separate map

\[
\delta:V^*\to\mathcal X'.
\]

Round-trip equality \(\delta(\tau(x))=x\) depends on normalization, whitespace, byte/codepoint conventions, special-token rules, and whether the tokenizer is lossless by construction.

## Boundary ladder

Distinguish at least:

1. bytes;
2. Unicode codepoints;
3. grapheme-like user-perceived characters;
4. pretokenized words, if a word boundary convention is imposed;
5. subword pieces;
6. token IDs;
7. token embeddings.

Equal counts at one level do not imply equal counts at another.

## Token length and fertility

Let

\[
L_\tau(x)=|\tau(x)|.
\]

For corpus \(C\) with a declared reference word segmentation containing \(W(C)\) words, define fertility

\[
F_\tau(C)=\frac{\sum_{x\in C}L_\tau(x)}{W(C)}.
\]

Fertility is corpus- and normalization-dependent. It is not a language constant.

For two tokenizers \(\tau_1,\tau_2\), define relative fertility

\[
R_F(C;\tau_1,\tau_2)=\frac{F_{\tau_1}(C)}{F_{\tau_2}(C)}.
\]

## Compression-like quantities

If a token sequence \(s=(v_1,\ldots,v_n)\) is modeled by a declared token probability model \(p\), then an idealized code length is

\[
\ell_p(s)=-\sum_{i=1}^n\log_2 p(v_i).
\]

This is model-dependent description length, not semantic information.

Token count alone is not a code length unless every token is assigned the same code cost.

## BPE boundary

BPE-style subword tokenization begins from a base symbol inventory and repeatedly merges selected adjacent symbol pairs according to a learned merge table/order.

The merge order is part of the tokenizer state.

A BPE vocabulary by itself does not generally determine the segmentation without the merge ranks or equivalent procedure.

## Unigram boundary

A unigram tokenizer assigns scores/probabilities to pieces and scores a segmentation by a product or sum of log piece scores under the declared model.

Multiple valid segmentations can therefore coexist under one vocabulary.

Deterministic Viterbi segmentation and stochastic segmentation sampling are different inference rules over the same segmentation space.

## SentencePiece boundary

SentencePiece supplies a raw-text tokenizer/detokenizer framework that can train subword models without requiring conventional word pretokenization.

This removes one boundary assumption; it does not make normalization or segmentation choices disappear.

## Byte-level boundary

A byte tokenizer maps a byte stream rather than a word/subword analysis.

For UTF-8 text, byte count and Unicode codepoint count can differ substantially.

Byte-level modeling removes out-of-vocabulary Unicode codepoints at the tokenizer boundary only if the byte alphabet is fully represented; it generally increases sequence length relative to many subword schemes.

## Exact Unicode witness

Compare two canonically related strings:

- NFC `é` = U+00E9: one codepoint, two UTF-8 bytes;
- decomposed `e` + U+0301: two codepoints, three UTF-8 bytes.

Thus byte length and codepoint length differ, and normalization can change both without a user necessarily intending a different visible glyph.

The chapter must not equate codepoints with grapheme clusters.

## Exact segmentation-ambiguity witness

Let

\[
V=\{a,b,ab\}
\]

with unigram probabilities

\[
p(ab)=\frac12,\qquad p(a)=p(b)=\frac14.
\]

For text `abab`, valid segmentations include:

\[
[ab,ab],\quad[a,b,ab],\quad[ab,a,b],\quad[a,b,a,b].
\]

Their unnormalized probabilities are respectively

\[
\frac14,\quad\frac1{32},\quad\frac1{32},\quad\frac1{256}.
\]

The normalization constant over these four segmentations is

\[
Z=\frac{81}{256}.
\]

Therefore

\[
q([ab,ab]\mid abab)=\frac{64}{81},
\]

while the two three-piece segmentations each have probability \(8/81\), and the four-piece segmentation has probability \(1/81\).

The best segmentation is not the only legal segmentation.

## Morphological-boundary diagnostic

Given a declared linguistic/morphological analysis with internal boundary set \(B_M(x)\) and tokenizer boundary set \(B_\tau(x)\), define

\[
P_M=\frac{|B_M\cap B_\tau|}{|B_\tau|},
\qquad
R_M=\frac{|B_M\cap B_\tau|}{|B_M|},
\]

when denominators are nonzero.

These are alignment diagnostics relative to a declared morphological analysis.

High alignment is not automatically a better language-model tokenizer, and low alignment is not automatically worse.

## Exact fertility witness

Take a two-word toy corpus with reference words `unbelievable cats`.

Tokenizer A produces

\[
[un,believ,able,cat,s]
\]

for five tokens total, so

\[
F_A=\frac52.
\]

Tokenizer B produces

\[
[unbelievable,cats]
\]

for two tokens total, so

\[
F_B=1.
\]

The shorter segmentation does not by itself prove lower compute, better morphology, better likelihood, or better downstream accuracy.

## Multilingual boundary

For language/corpus \(C_\ell\), tokenizer fertility, unknown-token rate, byte/codepoint expansion, vocabulary coverage, and morphology alignment must be measured on the declared corpus and normalization.

A shared multilingual vocabulary allocates finite vocabulary capacity across heterogeneous scripts and distributions.

Source-scoped evidence may show performance differences associated with tokenizer adequacy, but fertility alone must not be promoted to the sole causal explanation.

## Representation boundary

A token ID is a coordinate/index in a tokenizer vocabulary.

An embedding lookup maps that discrete coordinate into a learned vector representation.

Neither the ID nor the embedding is the semantic object itself.

Changing tokenization changes the sequence of model inputs and therefore the representation interface, even when detokenized text is unchanged.

## Failure boundaries

- byte != codepoint != grapheme != subword != token ID != embedding;
- token count != entropy or description length;
- vocabulary != segmentation algorithm;
- BPE != unigram segmentation;
- deterministic segmentation != stochastic segmentation sampling;
- shorter token sequence != universally better model;
- morphology alignment != model quality theorem;
- fertility != language complexity;
- multilingual fertility gap != single-cause explanation of downstream quality;
- lossless detokenization != semantic equivalence of all preprocessing pipelines;
- byte-level robustness evidence != universal compute advantage.

## Downstream handoff

Direct consumer:

- `ATLAS-CH-TOKENCOMP-001`.

TOKENCOMP may inherit:

- the tokenization boundary map;
- byte/codepoint/subword separation;
- fertility and relative-fertility definitions;
- declared probability-model code length;
- BPE/unigram distinction;
- morphology-boundary diagnostics;
- the exact Unicode, segmentation-ambiguity, and fertility witnesses;
- the multilingual measurement firewall.

TOKENCOMP must independently connect vocabulary design to description length, compute, interoperability, and tokenizer lingua-franca questions.

## Sources

- [@SennrichHaddowBirch2016BPE]
- [@Kudo2018SubwordRegularization]
- [@KudoRichardson2018SentencePiece]
- [@XueEtAl2022ByT5]
- [@RustEtAl2021Tokenizer]

Exact source authority and claim boundaries are locked in:

`sources/source-locks/ATLAS-CH-TOKEN-001.yaml`.
