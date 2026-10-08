# Tokenization and Representation Boundaries
<!-- ATLAS-CH-TOKEN-001 -->

**Epistemic status:** audited Information/Representation prerequisites + primary tokenizer sources + Atlas synthesis + exact finite witnesses  
**Specification:** manuscript/specifications/ATLAS-CH-TOKEN-001.md  
**Derivation packet:** mathematics/derivations/ATLAS-CH-TOKEN-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-TOKEN-001.md

A model never receives “text” in the abstract.

It receives a representation of text produced by a boundary convention.

That convention decides where symbols begin and end, which units receive IDs, how long the model's input sequence becomes, and which distinctions are preserved before the first learned layer acts.

Tokenization is therefore part of the representation interface.

## 1. A ladder of boundaries

Several units are routinely called characters or tokens even though they are mathematically different:

1. bytes;
2. Unicode codepoints;
3. grapheme-like visible characters;
4. words under a declared word-boundary convention;
5. subword pieces;
6. token IDs;
7. learned token embeddings.

A count at one level is not a count at another.

That sounds elementary, but many comparisons silently move between these levels.

## 2. Tokenization as a map

For normalized text space \(\mathcal X\) and vocabulary \(V\), write a deterministic tokenizer as

\[
\tau:\mathcal X\to V^*.
\]

A stochastic tokenizer instead defines a conditional distribution

\[
q_\tau(s\mid x)
\]

over valid segmentations \(s\) of \(x\).

Detokenization is another map:

\[
\delta:V^*\to\mathcal X'.
\]

Whether

\[
\delta(\tau(x))=x
\]

holds exactly depends on normalization, whitespace handling, byte conventions, special tokens, and the tokenizer design.

Lossless detokenization is an engineering property, not an automatic fact about all tokenizers.

## 3. Bytes and codepoints are not the same unit

Take the visible string `é` in NFC form.

It is one Unicode codepoint, U+00E9, but two UTF-8 bytes.

Normalize it into the decomposed form `e` plus U+0301.

Now it is two codepoints and three UTF-8 bytes.

Thus:

\[
\text{byte length}\neq\text{codepoint length},
\]

and Unicode normalization can change both.

This also warns against treating codepoint count as identical to user-perceived character count.

## 4. Why subwords became useful

Sennrich, Haddow, and Birch introduced a practical BPE-inspired subword strategy for neural machine translation to reduce the rare-word/open-vocabulary problem [@SennrichHaddowBirch2016BPE].

The important conceptual move is between whole-word and character extremes.

A recurring string can become one reusable unit while rarer forms remain decomposable.

That gives a finite vocabulary a route to representing strings it did not store as whole words.

The source establishes this method in its NMT setting.

It does not prove that BPE is universally optimal.

## 5. BPE is an algorithm, not merely a vocabulary

A BPE-style encoder starts from a base symbolization and applies learned pair merges in a declared order or ranking.

The procedure matters.

A list of piece strings is not always enough to reproduce segmentation.

A reproducible tokenizer therefore needs more than “vocabulary size = 32k.”

It should bind, at minimum:

- normalization;
- base symbols or pretokenization;
- merge ranks or equivalent encoder state;
- special-token rules;
- vocabulary/ID mapping.

This is a recurring Atlas lesson: an interface is more than a tensor shape or a list of names.

## 6. Unigram tokenization treats segmentation differently

Kudo's unigram method assigns scores to candidate pieces and evaluates whole segmentations under a unigram-language-model assumption [@Kudo2018SubwordRegularization].

That makes segmentation ambiguity explicit.

The same vocabulary can support several legal decompositions of the same string.

One can select the highest-scoring segmentation, or sample alternatives during training.

Those are different inference rules over the same segmentation space.

## 7. Exact ambiguity witness

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

For `abab`, consider:

\[
[ab,ab],
\]

\[
[a,b,ab],
\]

\[
[ab,a,b],
\]

and

\[
[a,b,a,b].
\]

Their unigram product weights are

\[
\frac14,
\quad
\frac1{32},
\quad
\frac1{32},
\quad
\frac1{256}.
\]

After normalization, the probabilities are

\[
\left(
\frac{64}{81},
\frac8{81},
\frac8{81},
\frac1{81}
\right).
\]

The first segmentation is the mode.

It is not the only segmentation admitted by the model.

## 8. SentencePiece moves the boundary again

SentencePiece was designed to train subword models directly from raw sentences rather than requiring conventional pretokenized word sequences [@KudoRichardson2018SentencePiece].

This matters because word pretokenization is itself a language-dependent representation choice.

Removing that requirement does not remove every preprocessing decision.

Normalization, vocabulary construction, segmentation model, special-token policy, and byte/codepoint handling still remain part of the interface.

## 9. Token count is a useful but narrow quantity

Define token length

\[
L_\tau(x)=|\tau(x)|.
\]

It directly controls how many discrete input positions a token-level Transformer sees.

But it is not entropy.

It is not automatically code length.

It is not a complete compute model.

Attention, embedding lookup, softmax vocabulary cost, architecture, batching, sequence packing, and hardware all matter downstream.

## 10. Token count is not description length

Under a declared token probability model \(p\), idealized code length is

\[
\ell_p(s)=-\sum_i\log_2p(v_i).
\]

Take a two-token sequence in which each token has probability \(1/16\).

Its idealized length is 8 bits.

Now take a three-token sequence in which each token has probability \(1/2\).

Its idealized length is 3 bits.

Therefore:

\[
|s_A|<|s_B|
\not\Rightarrow
\ell_p(s_A)<\ell_p(s_B).
\]

This preserves the Information chapter's firewall: description length is defined relative to a probability/coding model.

## 11. Fertility measures segmentation expansion

For corpus \(C\) with declared reference-word count \(W(C)\), define

\[
F_\tau(C)
=
\frac{\sum_{x\in C}|\tau(x)|}{W(C)}.
\]

A fertility of 1 means one tokenizer unit per reference word on average.

A fertility of 2.5 means two and a half units per reference word on average.

The number is useful precisely because it is simple.

It is also easy to overinterpret.

Fertility depends on the corpus, normalization, reference-word convention, and tokenizer.

It is not a fixed property of a language.

## 12. Exact fertility witness

Take the two-word toy corpus:

`unbelievable cats`.

Tokenizer A returns

`un | believ | able | cat | s`.

Five tokens over two reference words gives

\[
F_A=\frac52.
\]

Tokenizer B returns

`unbelievable | cats`,

so

\[
F_B=1.
\]

Tokenizer B produces the shorter model sequence.

That alone does not tell us which tokenizer gives better morphology, likelihood, transfer, robustness, compute efficiency, or downstream quality.

## 13. Morphology gives a different diagnostic

Suppose a declared linguistic analysis places internal boundaries in a word.

Let \(B_M(x)\) be those boundaries and \(B_\tau(x)\) the tokenizer's internal boundaries. Both sets must be measured as offsets in the **same declared canonical form of \(x\)** and the **same unit** (for example, positions between Unicode codepoints). Byte offsets from one representation cannot be compared directly with codepoint offsets from another.

One can define boundary precision and recall:

\[
P_M
=
\frac{|B_M\cap B_\tau|}{|B_\tau|},
\]

\[
R_M
=
\frac{|B_M\cap B_\tau|}{|B_M|}.
\]

These ratios are defined only when their respective denominators are nonzero: \(P_M\) requires \(|B_\tau|>0\) and \(R_M\) requires \(|B_M|>0\). When a boundary set is empty, report the affected quantity as **undefined/not applicable** rather than silently replacing \(0/0\) with zero or one. A particular evaluation protocol may separately declare a different empty-set convention.

For the toy analysis

`un | believ | able`,

an identical tokenization scores perfectly.

A segmentation `unbel | ievable` need not hit either declared morphology boundary.

This is a legitimate diagnostic.

It is not a theorem that morphology-aligned tokenization is always superior for neural language modeling.

## 14. Morphology and subword frequency optimize different objects

BPE primarily responds to frequent adjacent symbol patterns under its training procedure.

Unigram tokenization chooses a probabilistic piece inventory and segmentation model.

A linguistic morphology may instead aim to identify stems, affixes, roots, or other language-specific units.

These objectives can agree.

They can also disagree.

A frequent string is not necessarily a morpheme.

A morpheme is not necessarily frequent enough to earn its own vocabulary item.

## 15. Byte-level models remove one tokenizer bottleneck

ByT5 studies models that operate directly on UTF-8 bytes and reports robustness and modeling trade-offs relative to token-level counterparts [@XueEtAl2022ByT5].

A byte alphabet can cover arbitrary UTF-8 text without requiring a learned word/subword vocabulary.

That removes one kind of out-of-vocabulary boundary.

It does not make representation free.

Byte sequences are often longer.

Longer sequences alter compute and memory costs.

The empirical trade-off belongs to a declared model and workload.

## 16. Byte-level does not mean text has no structure

A byte-level model still receives an ordered symbol sequence.

UTF-8 itself is an encoding convention.

Unicode normalization still matters.

The model must learn useful regularities across multibyte sequences and longer spans.

“Token-free” therefore means free of a learned word/subword tokenizer in this context, not free of discrete representation choices altogether.

## 17. Multilingual tokenization creates allocation problems

A shared vocabulary has finite capacity.

Across many languages, that capacity must cover different scripts, frequency distributions, morphology, and corpus sizes.

Rust et al. conduct controlled comparisons showing that tokenizer adequacy can materially affect monolingual downstream performance inside multilingual models [@RustEtAl2021Tokenizer].

Their result motivates measurement.

It does not justify reducing multilingual performance to one tokenizer statistic.

Training-data scale, architecture, pretraining objective, vocabulary allocation, and downstream task all remain potential factors.

## 18. A multilingual tokenizer report should be vector-valued

For a language/corpus \(C_\ell\), useful quantities can include:

- fertility;
- unknown-token rate, if the tokenizer has unknowns;
- byte-per-token or codepoint-per-token expansion;
- vocabulary coverage;
- morphology-boundary alignment;
- sequence-length tails;
- downstream performance under controlled model/data comparisons.

These quantities do not share units.

A single scalar “tokenizer quality” score requires an explicit aggregation rule.

## 19. Token IDs are coordinates, not meaning

After segmentation, each piece receives an ID.

That ID indexes a learned embedding vector.

The Representation chapter's boundary applies directly:

\[
\text{coordinate}\neq\text{semantics}.
\]

Changing the ID assignment while consistently permuting the embedding table leaves the representational interface equivalent.

Changing the segmentation itself changes sequence length and decomposition, which is a different intervention.

## 20. Tokenization changes the learning problem

Two tokenizers can detokenize to the same text while presenting the model with different:

- sequence lengths;
- boundary locations;
- frequency distributions;
- embedding lookup events;
- context allocation;
- prediction targets;
- softmax classes.

Thus tokenizer replacement is not a neutral input formatting change.

It changes the model's representation boundary and often its training objective at the discrete-symbol level.

## 21. Comparing tokenizers requires controlled scope

A credible tokenizer comparison should state:

- normalization;
- tokenizer algorithm and version/state;
- vocabulary size;
- training corpus;
- language mixture;
- special tokens;
- byte/codepoint convention;
- sequence truncation policy;
- model architecture;
- parameter-count accounting;
- training token/byte/character budget;
- evaluation corpus and downstream metric.

Without these fields, “tokenizer A is more efficient” can conceal several different interventions.

## 22. What this chapter does not claim

TOKEN does not claim:

- BPE is universally superior to unigram tokenization;
- unigram sampling is always beneficial;
- byte models are universally more robust or efficient;
- low fertility is always good;
- high morphology alignment is always good;
- multilingual vocabulary sharing is always harmful or beneficial;
- token count alone determines compute;
- tokenizer choice alone determines multilingual performance.

The chapter supplies typed objects and diagnostics, not a universal ranking.

## 23. Handoff to Tokenization as Compression and Interface

ATLAS-CH-TOKENCOMP-001 may now assume:

- tokenization as an explicit representation boundary;
- byte/codepoint/subword separation;
- fertility and relative fertility;
- probability-model code length distinct from token count;
- BPE and unigram algorithms as different tokenizer families;
- morphology-boundary diagnostics;
- multilingual measurement as a vector rather than a single score;
- the exact normalization, segmentation-ambiguity, code-length, and fertility witnesses.

TOKENCOMP must add the harder systems question:

> how should vocabulary design trade description length, model compute, embedding/softmax cost, interoperability, and cross-model tokenizer interfaces?

## 24. Durable lesson

Tokenization chooses the discrete units on which the rest of the model operates.

That makes it neither mere preprocessing nor hidden semantics.

It is a representation boundary with measurable costs, ambiguities, and language-dependent effects.

## References used in this chapter

- [@SennrichHaddowBirch2016BPE]
- [@Kudo2018SubwordRegularization]
- [@KudoRichardson2018SentencePiece]
- [@XueEtAl2022ByT5]
- [@RustEtAl2021Tokenizer]

Exact source authority, prerequisite identities, and claim boundaries are locked in:

sources/source-locks/ATLAS-CH-TOKEN-001.yaml
