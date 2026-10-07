# Tokenization as Compression and Interface
<!-- ATLAS-CH-TOKENCOMP-001 -->

**Epistemic status:** audited Tokenization prerequisite + Atlas-owned exact compression/compute/interoperability constructions.  
**Specification:** manuscript/specifications/ATLAS-CH-TOKENCOMP-001.md  
**Derivation packet:** mathematics/derivations/ATLAS-CH-TOKENCOMP-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-TOKENCOMP-001.md  
**Source lock:** sources/source-locks/ATLAS-CH-TOKENCOMP-001.yaml

TOKEN-001 treated tokenization as a representation boundary.

This chapter asks what happens when that boundary is also treated as a compression and systems interface.

The immediate temptation is to rank tokenizers by one number:

> fewer tokens is better.

That rule is too coarse.

Vocabulary size changes how many distinct IDs must be represented.

Segmentation changes sequence length.

A model may pay costs that grow differently with sequence length and vocabulary size.

Two systems may need to exchange text while using incompatible token IDs.

The governing rule is:

\[
\boxed{
\text{tokenizer design is a multi-objective representation/interface choice, not a token-count scalar.}
}
\]

## 1. The inherited boundary

TOKEN-001 already established:

\[
\tau:\mathcal X\to V^*
\]

for a deterministic tokenizer, together with a separate detokenizer:

\[
\delta:V^*\to\mathcal X'.
\]

It also established that:

- byte length is not codepoint length;
- token count is not description length;
- fertility is corpus-relative;
- vocabulary is not the whole segmentation algorithm;
- token IDs and embeddings are representations, not semantics.

TOKENCOMP keeps all of those firewalls.

## 2. Compression requires a code

A token sequence is not yet a bit string.

To ask how many bits it occupies, we need a code.

One simple toy choice is a fixed-width code over token IDs.

Let:

\[
m=|V|\ge2.
\]

Then a fixed-width ID needs:

\[
w=\lceil\log_2m\rceil
\]

bits.

For a token sequence of length \(n\):

\[
D_{\mathrm{fw}}=nw.
\]

This is a code definition.

It is not an intrinsic property of the text.

## 3. Vocabulary size enters the accounting

Suppose one tokenizer halves the number of tokens but increases vocabulary size enough to require more bits per ID.

The two effects compete.

So:

\[
\boxed{
\text{shorter token sequence}
\not\Rightarrow
\text{shorter fixed-width ID stream}.
}
\]

This is the first compression/interface obstruction.

## 4. Fixed-width length is not entropy coding

TOKEN-001 inherited model-based idealized code length:

\[
\ell_p(s)
=
-\sum_i\log_2p(v_i).
\]

That quantity depends on a declared probability model.

Fixed-width length instead depends only on sequence length and vocabulary cardinality under the declared code.

They can disagree.

A complete comparison must state which description-length convention is being used.

## 5. A tokenizer is part of the codebook

The token-ID stream can be decoded only if the recipient already knows the tokenizer specification.

That can include:

- normalization;
- base alphabet;
- vocabulary;
- token-to-ID mapping;
- merge ranks or unigram scores;
- special-token rules;
- decoder behavior;
- version identity.

If that state is not shared, its description or transmission cost belongs somewhere in the protocol.

Therefore:

\[
\boxed{
\text{ID-stream length}
\neq
\text{complete compressor size}.
}
\]

## 6. Compression ratio needs a baseline

A ratio is meaningful only relative to something.

For byte string \(x\) with byte length \(B(x)>0\), define one toy ratio:

\[
R_{\mathrm{fw}}
=
\frac{D_{\mathrm{fw}}}{8B(x)}.
\]

This compares a token-ID stream to an 8-bit-per-byte baseline.

It does not count tokenizer state.

It does not claim optimal compression.

## 7. Token count is not compute

A model may perform several kinds of work.

Some costs can grow strongly with sequence length.

Others can grow with vocabulary size.

Still others depend on hidden dimension, sparsity, batching, memory, hardware, or implementation.

So the chapter refuses the shortcut:

\[
\text{token count}
=
\text{compute}.
\]

Instead it declares toy cost functions explicitly.

## 8. Two exact compute proxies

For token length \(n\), define:

\[
C_{\mathrm{pair}}(n)=n^2.
\]

This counts all ordered token-position pairs in a toy pair-interaction model.

For vocabulary size \(m\), define:

\[
C_{\mathrm{vocab}}(n,m)=nm.
\]

This counts one toy dense token-by-vocabulary scoring grid.

These are not universal model FLOP equations.

They are exact counters inside the declared finite model.

## 9. The finite witness

Take:

\[
x=\texttt{abababab}.
\]

It is eight ASCII bytes.

Thus the byte baseline contains:

\[
64
\]

bits.

We compare two lossless tokenizers.

## 10. Small-vocabulary tokenizer

Let:

\[
V_S=\{a,b\}.
\]

The tokenizer emits:

\[
[a,b,a,b,a,b,a,b].
\]

So:

\[
n_S=8,
\qquad
m_S=2.
\]

One bit identifies each of two token IDs.

Hence:

\[
D_S=8\cdot1=8\text{ bits}.
\]

The toy compute vector is:

\[
K_S=(8^2,8\cdot2)=(64,16).
\]

## 11. Piece tokenizer

Let:

\[
V_P=\{a,b,ab,x,y,z,w,q\}.
\]

The witness text is segmented as:

\[
[ab,ab,ab,ab].
\]

Thus:

\[
n_P=4,
\qquad
m_P=8.
\]

Three bits are required for one of eight fixed-width IDs.

Therefore:

\[
D_P=4\cdot3=12\text{ bits}.
\]

The toy compute vector is:

\[
K_P=(4^2,4\cdot8)=(16,32).
\]

## 12. The orderings conflict

The piece tokenizer uses fewer tokens:

\[
4<8.
\]

Its pair proxy is smaller:

\[
16<64.
\]

But its fixed-width ID stream is larger:

\[
12>8.
\]

And its dense-vocabulary proxy is larger:

\[
32>16.
\]

Thus the same design change improves one declared cost while worsening others.

## 13. There is no scalar winner without an objective

Write:

\[
J_\tau=
(D_{\mathrm{fw}},C_{\mathrm{pair}},C_{\mathrm{vocab}}).
\]

Then:

\[
J_S=(8,64,16),
\]

\[
J_P=(12,16,32).
\]

Neither is componentwise smaller.

So neither Pareto-dominates the other in this toy objective space.

To choose a winner we must add:

- weights;
- constraints;
- workload frequencies;
- a model architecture;
- or another explicit objective.

The tokenizer alone does not supply those choices.

## 14. Shorter can still matter

The counterexample does not say token length is irrelevant.

A shorter sequence can reduce any declared cost that increases with sequence length while other variables remain fixed.

The point is narrower:

> sequence length is one coordinate, not the whole resource model.

## 15. Vocabulary can buy reusable pieces

A larger vocabulary can encode recurring substrings as single tokens.

That can reduce sequence length.

But the vocabulary also creates state:

- more token identities;
- a wider fixed-width ID alphabet in the toy code;
- potentially more tokenizer specification;
- a different representation boundary.

The useful question is not "large or small vocabulary?"

It is:

> which objective vector is being optimized for which corpus and system?

## 16. Corpus distribution matters

Our witness contains only repeated "ab".

A different corpus can reverse which pieces are useful.

For corpus \(C\), one might compare:

\[
\mathbb E_{x\sim C}[L_\tau(x)]
\]

or:

\[
\mathbb E_{x\sim C}[D_{\mathrm{fw}}(x;\tau)].
\]

Those expectations depend on the corpus distribution.

No finite example creates a language-independent ranking.

## 17. Tokenizer interoperability

Now consider two systems that use different tokenizers.

A direct exchange of token IDs is unsafe unless the two sides share exactly the relevant tokenizer state.

Integer ID 17 in one vocabulary need not correspond to ID 17 in another.

Even identical token strings can have different IDs.

The interface must name what crosses the boundary.

## 18. Canonical transport domain

Let:

\[
\mathcal X_c
\]

be a declared domain of canonical byte strings.

Tokenizer A has:

\[
\tau_A:\mathcal X_c\to V_A^*,
\]

with decoder:

\[
\delta_A:V_A^*\to\mathcal X_c.
\]

Tokenizer B similarly has:

\[
\tau_B,\delta_B.
\]

Assume both round trip exactly on the declared domain:

\[
\delta_A(\tau_A(x))=x,
\]

\[
\delta_B(\tau_B(x))=x.
\]

## 19. Lossless translation theorem

Define:

\[
T_{A\to B}
=
\tau_B\circ\delta_A.
\]

Then:

\[
T_{A\to B}(\tau_A(x))
=
\tau_B(x).
\]

Applying B's decoder:

\[
\delta_B(T_{A\to B}(\tau_A(x)))
=
x.
\]

So the canonical bytes survive translation exactly.

This is an interface theorem.

It is not a model-behavior theorem.

## 20. The witness translates exactly

For the finite example:

Tokenizer S emits:

\[
[a,b,a,b,a,b,a,b].
\]

Its decoder concatenates these pieces back to:

\[
\texttt{abababab}.
\]

Tokenizer P then emits:

\[
[ab,ab,ab,ab].
\]

The reverse process recovers the S sequence.

The token identities and sequence lengths change.

The canonical byte string does not.

## 21. Lossless does not mean representation-equivalent

Suppose system A looks up embeddings using table \(E_A\) and B uses \(E_B\).

Their internal sequences can be:

\[
E_A(\tau_A(x))
\]

and:

\[
E_B(\tau_B(x)).
\]

Canonical byte equality supplies no equality between these vector sequences.

Therefore:

\[
\boxed{
\text{lossless transport}
\not\Rightarrow
\text{equal internal representation}.
}
\]

## 22. Nor does lossless mean semantic equivalence

Canonical byte equality is a syntactic identity under the declared interface.

It does not prove:

- equal human interpretation under every context;
- equal model probability;
- equal model activation;
- equal downstream answer;
- equal learned semantics.

The representation layer has been translated.

Nothing stronger follows automatically.

## 23. Direct ID interoperability is stronger

A direct token-ID mapping would avoid decode and retokenize.

But that requires more structure.

A simple permutation works only when the token alphabets and segmentation semantics align appropriately.

In the witness, one P token "ab" corresponds to two S tokens.

So no one-to-one token permutation can implement the translation.

Canonical translation is more general.

## 24. Special tokens require protocol semantics

Real token streams may contain control tokens not meant to decode as ordinary text.

Examples can include boundary, role, padding, or control symbols.

Such objects fall outside the simple canonical-byte theorem unless their transport semantics are explicitly defined.

A tokenizer interface therefore needs both:

- text/byte semantics;
- control-token semantics.

The chapter proves only the first finite case.

## 25. Version identity matters

A tokenizer is versioned protocol state.

Changing any of these can change the meaning of an ID stream:

- normalization;
- vocabulary;
- merge order;
- token scores;
- ID assignment;
- special tokens;
- decoder.

So "uses BPE" is not a sufficient interoperability identifier.

Neither is a vocabulary size.

## 26. Three meanings of lingua franca

The phrase **tokenizer lingua franca** can refer to different architectures.

### Canonical transport

Systems exchange normalized bytes/text and retokenize locally.

### Shared tokenizer

Systems adopt one tokenization specification and exchange its IDs.

### Translation layer

Systems keep local tokenizers and use explicit adapters.

These are distinct designs.

## 27. Canonical bytes as a bounded lingua franca

A canonical byte domain has one useful property:

different lossless tokenizers can translate through it without requiring matching vocabularies.

That makes it a candidate **transport interface**.

But this chapter does not claim:

- that every model should use bytes internally;
- that byte transport is always efficient;
- that a particular normalization should be universal;
- that all control tokens can be represented this way;
- that industry has adopted one standard.

"Candidate lingua franca" is therefore an architectural idea, not an adoption fact.

## 28. Shared tokenizers trade interoperability for constraints

A shared tokenizer can remove translation ambiguity at the token-ID layer.

It also couples systems to:

- one vocabulary allocation;
- one normalization;
- one version lifecycle;
- one special-token namespace.

That can be desirable in one architecture and restrictive in another.

No universal choice follows.

## 29. Translation layers preserve local freedom

A translation layer lets each subsystem retain its own tokenizer.

That preserves local representation choices.

But it adds:

- encode/decode work;
- protocol state;
- version management;
- possible normalization hazards;
- control-token mapping obligations.

Again, interoperability has costs.

## 30. Compression and interoperability are different objectives

Tokenizer S compresses the witness's fixed-width ID stream better than P.

That tells us nothing by itself about which is easier to standardize across systems.

Conversely, a widely shared tokenizer could improve ID-level interoperability without minimizing description length on a particular corpus.

Thus:

\[
\boxed{
\text{compression quality}
\neq
\text{interoperability quality}.
}
\]

## 31. Compute and interoperability are different objectives

Tokenizer P reduces the witness's pair proxy.

That does not make its token IDs meaningful to another system.

A compute optimization inside one model can worsen a protocol boundary if it increases specialization or version coupling.

System objectives must remain typed.

## 32. A practical comparison vector

A tokenizer/interface comparison might track:

\[
M_\tau(C)=
(
L,
D,
F,
C_{\mathrm{pair}},
C_{\mathrm{vocab}},
I_{\mathrm{roundtrip}},
I_{\mathrm{control}},
Q
),
\]

where the coordinates could denote:

- token length;
- declared description length;
- fertility;
- compute proxies or measured costs;
- round-trip interoperability;
- control-token interoperability;
- downstream quality.

These coordinates do not share one unit.

A scalar score requires an explicit objective.

## 33. Multilingual scope remains explicit

TOKEN-001 already required language/corpus-specific measurement.

TOKENCOMP preserves that rule.

A shared vocabulary may allocate capacity differently across scripts and languages.

A canonical byte interface may be lossless while token lengths vary substantially across local tokenizers.

Neither fact creates a universal multilingual optimum.

## 34. Modeled compute versus measured compute

The exact witness uses:

\[
n^2
\]

and:

\[
n|V|
\]

as toy counters.

A real system can have:

- different algorithms;
- sparsity;
- caching;
- batching;
- hardware kernels;
- memory effects;
- parallelism;
- compiler transformations.

Therefore the toy counters must not be relabeled as measured runtime.

A runtime claim requires a runtime experiment.

## 35. What would an empirical comparison require?

At minimum:

- exact tokenizer versions;
- normalization;
- corpus/language distribution;
- vocabulary sizes;
- sequence-length distribution;
- code-length convention;
- model architecture;
- model parameterization affected by vocabulary size;
- training or serving workload;
- hardware/software stack for runtime;
- downstream quality metrics.

Without these, "tokenizer A is more efficient" is underspecified.

## 36. Durable non-implications

The chapter preserves:

\[
\text{fewer tokens}
\not\Rightarrow
\text{fewer encoded bits},
\]

\[
\text{fewer tokens}
\not\Rightarrow
\text{lower cost under every compute model},
\]

\[
\text{lossless translation}
\not\Rightarrow
\text{equal tokenization},
\]

\[
\text{equal decoded bytes}
\not\Rightarrow
\text{equal embeddings or behavior},
\]

\[
\text{shared interface}
\not\Rightarrow
\text{universal standard}.
\]

## 37. Tokenization as interface design

The central systems lesson is not that one tokenizer should dominate.

It is that a tokenizer boundary carries several contracts at once:

- representation;
- compression;
- compute shape;
- serialization;
- versioning;
- interoperability.

Those contracts can favor different designs.

A mature tokenizer choice therefore begins by naming the objective vector rather than by minimizing token count in isolation.

## References used in this chapter

No new external academic authority is added in TOKENCOMP-001.

Tokenizer mechanisms, probability-model code length, multilingual boundaries, and representation-interface authority are inherited through the audited TOKEN-001 source lock. TOKENCOMP's new compression/compute/interoperability results are exact Atlas-owned constructions.

Exact source identity and claim boundaries are recorded in:

sources/source-locks/ATLAS-CH-TOKENCOMP-001.yaml
