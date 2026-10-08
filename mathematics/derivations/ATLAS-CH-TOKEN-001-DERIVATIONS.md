# ATLAS-CH-TOKEN-001 — Derivation Packet

## 1. Tokenization as a boundary map

A deterministic tokenizer is

\[
\tau:\mathcal X\to V^*.
\]

A stochastic tokenizer defines

\[
q_\tau(s\mid x),\qquad s\in\operatorname{Seg}_V(x).
\]

The tokenizer boundary is therefore part of the model interface, not merely a display convention.

## 2. Length measures are typed

For text \(x\), define:

- byte length \(B(x)\);
- Unicode codepoint length \(C(x)\);
- token length \(L_\tau(x)=|\tau(x)|\).

No identity among these counts is assumed.

For NFC `é`:

\[
B=2,\qquad C=1.
\]

For decomposed `e` + U+0301:

\[
B=3,\qquad C=2.
\]

Thus normalization can change both counts.

## 3. Fertility

For corpus \(C\) with declared reference-word count \(W(C)>0\), define

\[
F_\tau(C)=\frac{\sum_{x\in C}L_\tau(x)}{W(C)}.
\]

For the toy corpus `unbelievable cats`, let tokenizer A return five tokens and tokenizer B return two.

Then

\[
F_A=\frac52,
\qquad
F_B=1,
\]

and

\[
R_F(A,B)=\frac52.
\]

This is a segmentation-length statement only.

## 4. Token count versus code length

Given a declared token model \(p\), idealized code length is

\[
\ell_p(s)=-\sum_i\log_2 p(v_i).
\]

A two-token sequence can have larger code length than a three-token sequence if its tokens are sufficiently improbable.

Example:

Sequence A has two tokens each with probability \(1/16\):

\[
\ell_A=8\text{ bits}.
\]

Sequence B has three tokens each with probability \(1/2\):

\[
\ell_B=3\text{ bits}.
\]

Hence

\[
|A|<|B|
\not\Rightarrow
\ell_p(A)<\ell_p(B).
\]

## 5. Unigram segmentation ambiguity

Let

\[
V=\{a,b,ab\}
\]

with

\[
p(ab)=\frac12,
\qquad
p(a)=p(b)=\frac14.
\]

For `abab`, the valid segmentations are

\[
s_1=[ab,ab],
\]

\[
s_2=[a,b,ab],
\]

\[
s_3=[ab,a,b],
\]

\[
s_4=[a,b,a,b].
\]

Under the unigram product score,

\[
w(s_1)=\frac14,
\]

\[
w(s_2)=w(s_3)=\frac1{32},
\]

and

\[
w(s_4)=\frac1{256}.
\]

The normalization constant is

\[
Z
=
\frac{64+8+8+1}{256}
=
\frac{81}{256}.
\]

Therefore

\[
q(s_1\mid abab)=\frac{64}{81},
\]

\[
q(s_2\mid abab)=q(s_3\mid abab)=\frac8{81},
\]

and

\[
q(s_4\mid abab)=\frac1{81}.
\]

The Viterbi segmentation is \(s_1\), but it is not the only legal segmentation.

## 6. BPE state is more than the vocabulary

A BPE-style tokenizer uses a base symbolization and an ordered merge rule/table.

Two tokenizers can expose the same final piece strings while using different merge ranks or preprocessing rules.

Therefore a reproducible BPE tokenizer specification must bind at least:

- normalization;
- base alphabet/pretokenization;
- merge ranks or equivalent encoder procedure;
- special-token rules;
- vocabulary/ID mapping.

## 7. Morphological-boundary alignment

Given declared internal morphology boundaries \(B_M(x)\) and token boundaries \(B_\tau(x)\), represent both as offsets in the same normalized \(x\) and coordinate unit (e.g. inter-codepoint positions); otherwise their intersection has no declared meaning. When the corresponding denominator is positive, define

\[
P_M=\frac{|B_M\cap B_\tau|}{|B_\tau|},
\qquad
R_M=\frac{|B_M\cap B_\tau|}{|B_M|}.
\]

If \(|B_\tau|=0\), \(P_M\) is undefined; if \(|B_M|=0\), \(R_M\) is undefined. Do not silently assign a score to \(0/0\). A separate reporting protocol may adopt an explicit empty-boundary convention.

For a toy analysis `un|believ|able`, the morphology boundary set has size two.

Tokenizer A `un|believ|able` gives

\[
P_M=R_M=1.
\]

Tokenizer B `unbel|ievable` has one token boundary and no exact morphology-boundary match, hence

\[
P_M=R_M=0.
\]

This does not establish that tokenizer A is better for a language model.

## 8. Multilingual measurement vector

For corpus/language index \(\ell\), define a tokenizer measurement vector such as

\[
m_\tau(C_\ell)
=
(F_\tau,U_\tau,B/T,M_\tau,C_\tau),
\]

where components may denote fertility, unknown-token rate, byte-per-token expansion, morphology alignment, and another declared coverage measure.

These coordinates have different meanings and units.

No scalar tokenizer-quality score exists until an evaluation rule is declared.

## 9. Representation interface

Let token IDs be \(i_1,\ldots,i_n\), and let embedding table \(E\) map IDs to vectors.

Then the representation passed to a model is

\[
(E_{i_1},\ldots,E_{i_n}).
\]

Changing \(\tau\) changes the sequence length and coordinates of this representation even when detokenization recovers the same text.

Thus tokenization is part of representation design.

## 10. Downstream handoff

ATLAS-CH-TOKENCOMP-001 may inherit:

- typed length measures;
- fertility and relative fertility;
- probability-model code length;
- segmentation ambiguity;
- morphology-boundary alignment;
- multilingual measurement vectors;
- tokenization as a representation interface.

It must independently analyze description length, compute scaling, interoperability, vocabulary design, and lingua-franca questions.

## Claim boundary

This packet proves only the displayed finite arithmetic and defines Atlas-local diagnostics.

It does not establish a universally optimal tokenizer, a universal morphology objective, or a single-cause explanation of multilingual performance.
