# Chapter Specification — ATLAS-CH-TOKENCOMP-001

## Identity

**Title:** Tokenization as Compression and Interface  
**Part:** Tokenization, Data, and Curriculum  
**Status:** specification-ready.  
**Epistemic class:** audited Tokenization prerequisite + Atlas-owned exact compression/compute/interoperability constructions.

## Contract

Connect vocabulary design to:

- description length;
- declared compute models;
- interoperability;
- tokenizer lingua-franca questions.

The chapter must not collapse token count, code length, compute, semantic adequacy, or interface compatibility into one tokenizer-quality scalar.

## Hard prerequisite

- ATLAS-CH-TOKEN-001.

Exact prerequisite identity and source authority are locked in:

sources/source-locks/ATLAS-CH-TOKENCOMP-001.yaml

## Inherited TOKEN boundaries

TOKENCOMP may inherit:

- deterministic and stochastic tokenizer objects;
- byte/codepoint/subword/token-ID distinctions;
- fertility and relative fertility;
- probability-model code length;
- BPE/unigram/SentencePiece/byte-level distinctions;
- multilingual scope discipline;
- exact finite TOKEN witnesses.

It must preserve:

\[
\text{token count}
\neq
\text{description length},
\]

and:

\[
\text{tokenizer representation}
\neq
\text{semantics}.
\]

## Typed compression quantities

For tokenizer \(\tau\), text \(x\), and vocabulary \(V_\tau\), define token length:

\[
L_\tau(x)=|\tau(x)|.
\]

For a declared toy fixed-width token-ID code with \(|V_\tau|\ge2\), define:

\[
w_\tau=\lceil\log_2 |V_\tau|\rceil
\]

bits per ID, and sequence-ID length:

\[
D_{\mathrm{fw}}(x;\tau)
=
L_\tau(x)w_\tau.
\]

This counts only the encoded token-ID stream under a shared tokenizer specification.

It excludes:

- vocabulary transmission;
- merge tables;
- normalization rules;
- special-token conventions;
- framing;
- entropy coding;
- model parameters.

For a declared token probability model \(p\), retain the inherited model-based code length:

\[
\ell_p(s)
=
-\sum_i\log_2 p(v_i).
\]

In general:

\[
D_{\mathrm{fw}}\neq\ell_p.
\]

## Compression ratio

A compression ratio is valid only relative to a declared baseline encoding.

For baseline byte length \(B(x)>0\), one possible toy ID-stream ratio is:

\[
R_{\mathrm{fw}}
=
\frac{D_{\mathrm{fw}}}{8B(x)}.
\]

This is not a complete compressor ratio unless tokenizer/dictionary overhead is shared or separately counted.

## Typed compute proxies

Token length is not compute.

The chapter uses only explicitly declared toy proxies to expose trade-offs.

For sequence length \(n\) and vocabulary size \(m\), define:

\[
C_{\mathrm{pair}}(n)=n^2
\]

as a pair-interaction-count proxy, and:

\[
C_{\mathrm{vocab}}(n,m)=nm
\]

as a dense token-by-vocabulary scoring proxy.

These are exact functions of \(n,m\) in the toy model.

They are not universal Transformer FLOP counts, measured runtime, or hardware laws.

## Exact finite trade-off witness

Take canonical byte string:

\[
x=\texttt{abababab}.
\]

Tokenizer S:

\[
V_S=\{a,b\},
\]

\[
\tau_S(x)=[a,b,a,b,a,b,a,b].
\]

Thus:

\[
|V_S|=2,\qquad L_S=8,\qquad w_S=1,
\]

\[
D_{\mathrm{fw},S}=8.
\]

Toy compute proxies:

\[
C_{\mathrm{pair},S}=8^2=64,
\]

\[
C_{\mathrm{vocab},S}=8\cdot2=16.
\]

Tokenizer P:

\[
V_P=\{a,b,ab,x,y,z,w,q\},
\]

\[
\tau_P(x)=[ab,ab,ab,ab].
\]

Thus:

\[
|V_P|=8,\qquad L_P=4,\qquad w_P=3,
\]

\[
D_{\mathrm{fw},P}=12.
\]

Toy compute proxies:

\[
C_{\mathrm{pair},P}=4^2=16,
\]

\[
C_{\mathrm{vocab},P}=4\cdot8=32.
\]

Therefore P has:

- half the token count;
- one quarter the pair-interaction proxy;
- a larger fixed-width token-ID stream;
- twice the dense-vocabulary proxy.

No scalar tokenizer optimum follows.

## Canonical interoperability object

Let \(\mathcal X_c\) be a declared canonical byte-string domain.

For tokenizer A:

\[
\tau_A:\mathcal X_c\to V_A^*,
\qquad
\delta_A:V_A^*\to\mathcal X_c.
\]

For tokenizer B:

\[
\tau_B:\mathcal X_c\to V_B^*,
\qquad
\delta_B:V_B^*\to\mathcal X_c.
\]

Assume both are lossless on the declared domain:

\[
\delta_A(\tau_A(x))=x,
\qquad
\delta_B(\tau_B(x))=x.
\]

Define translation:

\[
T_{A\to B}
=
\tau_B\circ\delta_A.
\]

Then for every declared-domain \(x\):

\[
T_{A\to B}(\tau_A(x))
=
\tau_B(x),
\]

and:

\[
\delta_B(T_{A\to B}(\tau_A(x)))
=
x.
\]

This is lossless representation translation.

It does not imply:

- equal token counts;
- equal token probabilities;
- equal embeddings;
- equal model activations;
- equal semantics outside the declared byte identity;
- equal downstream behavior.

## Tokenizer lingua franca

A tokenizer lingua franca can mean at least three different things:

1. a shared canonical transport representation, such as declared bytes/text;
2. a shared tokenizer specification used by multiple systems;
3. a translation layer among tokenizer-specific internal representations.

These must not be conflated.

The chapter uses "canonical interface" for (1), not as an adoption claim or universal standard.

## Interface specification

A reproducible tokenizer interface should bind:

- canonical input domain;
- normalization;
- byte/text encoding;
- tokenizer algorithm/state;
- vocabulary and ID map;
- special-token rules;
- decoder;
- framing/serialization if token sequences cross system boundaries;
- version identity.

A vocabulary name alone is insufficient.

## Failure boundaries

- fewer tokens != fewer encoded bits;
- fewer tokens != lower cost under every compute model;
- larger vocabulary != better compression;
- smaller vocabulary != better interoperability;
- fixed-width ID length != entropy-coded description length;
- ID-stream compression != complete compressor size;
- common decoded bytes != common tokenization;
- common tokenization != common embeddings;
- lossless representation translation != semantic/model-behavior equivalence;
- a canonical transport interface != a universal tokenizer standard;
- measured runtime != a toy compute proxy.

## Reader spine

1. Why tokenization is also an interface.
2. Compression needs a code definition.
3. Vocabulary size and ID width.
4. Sequence length and code length.
5. Model-based versus fixed-width description length.
6. Token length is not compute.
7. Two explicit compute proxies.
8. Exact trade-off witness.
9. Pareto rather than scalar tokenizer comparison.
10. Tokenizer specification as protocol state.
11. Canonical lossless interoperability.
12. Token IDs are local coordinates.
13. Shared tokenizer versus translation layer.
14. What a tokenizer lingua franca could mean.
15. Multilingual/corpus scope.
16. Benchmark and measurement discipline.
17. Failure boundaries.

## Evidence discipline

Any empirical tokenizer comparison should declare:

- corpus/language;
- normalization;
- tokenizer identities/versions;
- vocabulary sizes;
- token-length distribution;
- description-length convention;
- model architecture if compute is measured or modeled;
- hardware/software if runtime is measured;
- downstream task and metric if quality is claimed.

## Sources

No new external academic source is required for this bounded chapter.

External tokenizer authority is inherited through audited TOKEN-001. The new compression/compute/interface results are exact Atlas-owned constructions.

Exact source authority and claim boundaries are locked in:

sources/source-locks/ATLAS-CH-TOKENCOMP-001.yaml
