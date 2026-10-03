# Chapter Specification — ATLAS-CH-TRANSFORMER-001

## Identity

**Title:** The Transformer as Baseline Object  
**Part:** Neural Architectures  
**Status:** specification-ready.  
**Epistemic class:** established architecture + Atlas synthesis.

## Chapter contract

Define conventional Transformer anatomy precisely enough that later Atlas chapters can identify exactly what they retain, remove, approximate, normalize, split, sparsify, route, or reinterpret.

This chapter is the architectural reference object.

It is not a second full treatment of attention.

## Dependency contract

Hard prerequisite:

- \`ATLAS-CH-ARCHHIST-001\`.

May assume:

- layered composition;
- residual identity transport;
- interfaces;
- recurrent versus feed-forward state distinctions;
- finite-dimensional matrix algebra.

Must not assume:

- sparse/MoE routing;
- adaptive depth;
- split-operator architectures;
- relative-position operator theory;
- network numerics;
- mechanistic diagnostics.

Those are downstream.

## Reader outcome

A reader should be able to:

1. write the state shape of a Transformer residual stream;
2. locate token embeddings and positional information;
3. define Q/K/V projections and multi-head aggregation at baseline level;
4. distinguish an attention sublayer from a whole Transformer block;
5. state the causal-mask dependency rule;
6. prove that ideal causal masking removes future-value dependence;
7. write a position-wise feed-forward network;
8. distinguish pre-LN from post-LN block ordering;
9. distinguish encoder-only, decoder-only, and encoder-decoder topologies;
10. explain the role of cross-attention;
11. identify the exact residual identity path;
12. separate architecture anatomy from training recipe.

## Baseline state

For sequence length \(n\) and model width \(d\), write the residual-stream state as

\[
H\in\mathbb R^{n\times d}.
\]

Initial state:

\[
H_0
=
E(\text{tokens})+P,
\]

where \(P\) is positional information in the chosen positional scheme.

This chapter does not privilege one positional scheme.

## Single attention head

For head \(h\),

\[
Q_h=HW_Q^{(h)},
\qquad
K_h=HW_K^{(h)},
\qquad
V_h=HW_V^{(h)}.
\]

Scores:

\[
S_h
=
\frac{Q_hK_h^\top}{\sqrt{d_k}}+M.
\]

Mixing weights:

\[
A_h
=
\operatorname{softmax}_{\rm row}(S_h).
\]

Head output:

\[
O_h=A_hV_h.
\]

Keep the distinction:

\[
\text{scores}
\neq
\text{normalized mixing operator}
\neq
\text{value field}
\neq
\text{full block}.
\]

The full operator interpretation is delegated to \`ATLAS-CH-ATTNOP-001\`.

## Multi-head attention

\[
\operatorname{MHA}(H)
=
\operatorname{Concat}(O_1,\ldots,O_m)W_O.
\]

The concatenated head spaces are recombined by \(W_O\).

Do not describe multi-head attention as one monolithic attention matrix unless a specific equivalent representation is derived.

## Causal mask

For left-to-right autoregressive self-attention, use the ideal mathematical mask

\[
M_{ij}
=
\begin{cases}
0,&j\le i,\\
-\infty,&j>i.
\end{cases}
\]

After row softmax,

\[
A_{ij}=0
\]

for all \(j>i\).

State explicitly that finite implementations generally use a representable large-negative value or a masked-softmax primitive; the exact \(-\infty\) object is mathematical notation.

## Exact causal witness

Use three tokens, zero unmasked scores, and scalar values

\[
V=
\begin{pmatrix}
2\\
5\\
11
\end{pmatrix}.
\]

The exact ideal causal mixing matrix is

\[
A=
\begin{pmatrix}
1&0&0\\
1/2&1/2&0\\
1/3&1/3&1/3
\end{pmatrix}.
\]

Then

\[
AV
=
\begin{pmatrix}
2\\
7/2\\
6
\end{pmatrix}.
\]

Replace the future value \(v_3=11\) by \(101\).

The first two outputs remain exactly

\[
2,
\qquad
7/2.
\]

This is the declared exact future-independence witness.

## Position-wise feed-forward network

For each token position independently,

\[
\operatorname{FFN}(h)
=
\phi(hW_1+b_1)W_2+b_2.
\]

The same FFN parameters are reused across sequence positions within a layer.

This is different parameter sharing from convolution or recurrence.

## Layer Normalization

For token state \(x\in\mathbb R^d\),

\[
\mu(x)
=
\frac1d\sum_i x_i,
\]

\[
\sigma^2(x)
=
\frac1d\sum_i(x_i-\mu)^2,
\]

and

\[
\operatorname{LN}(x)
=
\gamma\odot
\frac{x-\mu}{\sqrt{\sigma^2+\varepsilon}}
+
\beta.
\]

Keep \(\varepsilon>0\) explicit in the architecture definition.

## Post-LN block

Original-Transformer-style ordering:

\[
Y
=
\operatorname{LN}
\left(
H+\operatorname{MHA}(H)
\right),
\]

\[
H'
=
\operatorname{LN}
\left(
Y+\operatorname{FFN}(Y)
\right).
\]

## Pre-LN block

A common later ordering is

\[
Y
=
H+
\operatorname{MHA}
\left(
\operatorname{LN}(H)
\right),
\]

\[
H'
=
Y+
\operatorname{FFN}
\left(
\operatorname{LN}(Y)
\right).
\]

Use [@XiongEtAl2020] to document/analyze this distinction.

Do not claim one ordering is universally superior.

## Exact multi-head witness

Let two head outputs for one token be

\[
O_1=(1,2),
\qquad
O_2=(3,4).
\]

Concatenate:

\[
c=(1,2,3,4).
\]

Choose

\[
W_O
=
\begin{pmatrix}
1&0\\
0&1\\
1&1\\
2&-1
\end{pmatrix}.
\]

Then

\[
cW_O=(12,1).
\]

This witnesses head concatenation plus output projection only.

It does not model learned attention scores.

## Residual identity witness

For residual update

\[
H'=H+S(H),
\]

if

\[
S(H)=0,
\]

then

\[
H'=H.
\]

Use exact state

\[
H=(2,-1,3)
\]

for the witness.

## Topology families

### Encoder-only

Bidirectional/self-attending stack without an autoregressive causal mask by default.

Use BERT only as a representative primary source.

### Decoder-only

Causally masked self-attending stack for left-to-right autoregressive generation.

Use GPT-2 only as a representative topology source.

### Encoder-decoder

Encoder self-attends its source sequence.

Decoder contains:

- masked self-attention over generated prefix;
- cross-attention whose queries come from decoder state and whose keys/values come from encoder memory;
- FFN.

The original Transformer is the canonical source for this topology.

## Principal pedagogical device

### Allegory: a shared blackboard with restricted sight lines

Each token occupies one row of a shared residual-state blackboard.

Attention lets rows read from selected other rows.

A causal mask closes future sight lines before weights are normalized.

The MLP then performs a position-local transformation.

Residual paths keep the shared state moving forward.

Limit:

The residual stream is not literally a blackboard service, and attention weights do not equal semantic explanation.

## Figure programme

### ATLAS-FIG-TRANSFORMER-001

Three panels:

1. one pre-LN baseline block showing residual stream, attention, MLP, norms, and identity paths;
2. exact \(3\times3\) causal dependency/mixing matrix;
3. topology comparison: encoder-only, decoder-only, encoder-decoder with cross-attention.

Representation class:
schematic with exact causal matrix annotations.

## Counterexamples and failure boundaries

Include:

- attention alone is not the full Transformer;
- causal masking is not a learned preference;
- residual identity path does not guarantee good conditioning;
- LayerNorm changes geometry and scale; with explicit (arepsilon>0), do not claim unconditional exact scale invariance;
- decoder-only is not synonymous with every language model;
- encoder-only is not inherently bidirectional for arbitrary masking schemes;
- pre-LN/post-LN labels must be tied to explicit equations;
- positional information is a separate design axis;
- architecture does not specify optimizer, dataset, scale, or training objective.

## Downstream obligations

Direct consumers:

- \`ATLAS-CH-SPLIT-001\`;
- \`ATLAS-CH-MOE-001\`;
- \`ATLAS-CH-MECHDIAG-001\`.

Important later consumers:

- relative position;
- normalized Transformers;
- sparse computation;
- routing;
- adaptive depth;
- network numerics.

## Sources

- [@VaswaniEtAl2017]
- [@BaKirosHinton2016]
- [@XiongEtAl2020]
- [@DevlinChangLeeToutanova2019]
- [@RadfordEtAl2019]

Source lock:
\`sources/source-locks/ATLAS-CH-TRANSFORMER-001.yaml\`.

## Acceptance

The draft must:

- define the residual-stream state and block anatomy;
- distinguish scores, mixing, values, and block output;
- prove exact causal future-independence in the declared toy system;
- exactly witness multi-head concatenation/output projection;
- define FFN sharing and LayerNorm;
- write explicit pre-LN and post-LN equations;
- distinguish topology families;
- preserve residual identity scope;
- avoid duplicating the full Attention-as-Operator chapter;
- include source lock, derivation packet, computational witness, and reproducible figure.
