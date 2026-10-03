# TRANSFORMER-001 — The Transformer as Baseline Object

## Status

**Tranche state:** implemented on branch pending merge validation.

## Baseline

- audited ARCHHIST merge:
  \`ecb15c976e4bb5cbc79b560ec19cbfdf9618607d\`;
- issue:
  \`#54\`;
- hard prerequisite:
  \`ATLAS-CH-ARCHHIST-001\` at audited \`draft-v0.1\`.

## Objective

Define a conventional Transformer reference object precisely enough that later Atlas chapters can state exactly what they modify.

The chapter freezes the distinction:

\[
\text{attention}
\neq
\text{Transformer block}
\neq
\text{Transformer system}.
\]

## A. Baseline state

For sequence length \(n\) and width \(d\),

\[
H\in\mathbb R^{n\times d}.
\]

Initial state:

\[
H_0
=
E(\text{tokens})+P.
\]

The positional mechanism is kept as a separate design axis.

## B. Attention sublayer

For one head,

\[
Q=HW_Q,
\qquad
K=HW_K,
\qquad
V=HW_V,
\]

\[
S
=
\frac{QK^\top}{\sqrt{d_k}}+M,
\]

\[
A
=
\operatorname{softmax}_{\rm row}(S),
\]

\[
O=AV.
\]

The chapter preserves:

\[
\text{scores}
\neq
\text{mixing weights}
\neq
\text{values}
\neq
\text{head output}.
\]

## C. Exact causal witness

For ideal left-to-right mask and zero unmasked logits,

\[
A
=
\begin{pmatrix}
1&0&0\\
1/2&1/2&0\\
1/3&1/3&1/3
\end{pmatrix}.
\]

With

\[
V=(2,5,11)^\top,
\]

\[
AV=(2,7/2,6)^\top.
\]

Replacing only the future value with

\[
V'=(2,5,101)^\top
\]

gives

\[
AV'=(2,7/2,36)^\top.
\]

The first two outputs remain exactly unchanged.

This demonstrates future-value independence for the declared ideal mask.

## D. Multi-head witness

For

\[
O_1=(1,2),
\qquad
O_2=(3,4),
\]

concatenate:

\[
C=(1,2,3,4).
\]

With

\[
W_O
=
\begin{pmatrix}
1&0\\
0&1\\
1&1\\
2&-1
\end{pmatrix},
\]

the exact projected output is

\[
CW_O=(12,1).
\]

## E. Feed-forward sublayer

For each token independently,

\[
\operatorname{FFN}(h)
=
\phi(hW_1+b_1)W_2+b_2.
\]

Parameters are shared across sequence positions within the layer.

## F. LayerNorm and block order

LayerNorm is defined explicitly with mean, variance, learned \(\gamma,\beta\), and \(\varepsilon>0\).

Post-LN:

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

Pre-LN:

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

The chapter does not declare one ordering universally superior.

## G. Residual identity witness

For

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

Exact witness state:

\[
H=(2,-1,3).
\]

## H. Topology families

The chapter distinguishes:

- encoder-only;
- decoder-only;
- encoder-decoder.

Cross-attention is defined by decoder queries with encoder-memory keys/values:

\[
Q=H_{\rm dec}W_Q,
\qquad
K=EW_K,
\qquad
V=EW_V.
\]

BERT and GPT-2 are used only as representative topology sources.

## I. Architecture / training separation

The chapter freezes:

\[
\text{architecture}
\neq
\text{objective}
\neq
\text{optimizer}
\neq
\text{tokenizer}
\neq
\text{scale}.
\]

A simplified pre-LN decoder-only baseline is written:

\[
Y_l
=
H_l
+
\operatorname{MHA}_l
\left(
\operatorname{LN}_l^{(1)}(H_l);
M_{\rm causal}
\right),
\]

\[
H_{l+1}
=
Y_l
+
\operatorname{FFN}_l
\left(
\operatorname{LN}_l^{(2)}(Y_l)
\right).
\]

This is a reference equation, not a universal canonical Transformer.

## J. Source boundary

External sources:

- Vaswani et al. 2017:
  original Transformer architecture;
- Ba–Kiros–Hinton 2016:
  Layer Normalization;
- Xiong et al. 2020:
  pre-LN/post-LN analysis;
- Devlin et al. 2019:
  representative encoder-only topology;
- Radford et al. 2019:
  representative decoder-only topology.

Atlas internal prerequisite:

- audited ARCHHIST manuscript blob:
  \`3d373695ed5516dbc3b0557112f204636e911897\`.

## K. Figure

\`ATLAS-FIG-TRANSFORMER-001\`

- generator blob:
  \`1f2bc09736f1b5a2cbf6969c9edc24b625c4c283\`;
- rendered blob:
  \`3df30e0d94696afe5ca503cb30ad17609243d12c\`;
- rendered bytes:
  \`39,242\`;
- representation class:
  schematic.

Panels:

1. pre-LN residual-stream block;
2. exact \(3\times3\) causal mixing matrix;
3. encoder-only / decoder-only / encoder-decoder topology comparison.

## L. Durable objects

The branch contains:

- source lock;
- chapter specification;
- derivation packet;
- exact computational witness;
- complete manuscript;
- Wolfram figure generator/master/manifest;
- Figure Register entry;
- Chapter Ledger promotion to \`draft-v0.1\`.

## M. Frozen distinctions

\[
\text{attention}
\neq
\text{full Transformer}.
\]

\[
\text{causal mask}
\neq
\text{learned preference}.
\]

\[
\text{pre-LN}
\neq
\text{post-LN}.
\]

\[
\text{encoder-only}
\neq
\text{decoder-only}
\neq
\text{encoder-decoder}.
\]

\[
\text{identity path}
\neq
\text{guaranteed good conditioning}.
\]

\[
\text{architecture}
\neq
\text{training recipe}.
\]

## N. Next step after merge

Run a bounded post-draft audit checking:

- attention/block/system distinctions;
- causal-mask exact support;
- multi-head output algebra;
- residual identity limit;
- LayerNorm definition;
- pre-LN/post-LN equations;
- topology-family scope;
- source provenance;
- figure identity.

Do not begin direct consumers until this audit merges.
