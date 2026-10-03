# AUDIT-011 — The Transformer as Baseline Object

## Disposition

**PASS AFTER ONE LAYERNORM WORDING REPAIR**

\`ATLAS-CH-TRANSFORMER-001\` remains at \`draft-v0.1\`.

The chapter's baseline architecture equations, exact causal-mask witness, multi-head aggregation witness, topology distinctions, source scope, internal provenance, and figure identities pass audit.

AUDIT-011 found one substantive wording defect:

> the manuscript said LayerNorm “removes one affine scale/offset component.”

That phrasing was too coarse. With explicit \(\varepsilon>0\) and learned \(\gamma,\beta\), it could be misread as an unconditional exact affine-scale invariance claim.

The manuscript, derivation packet, specification, and source lock now state LayerNorm operationally as:

1. centering by the feature mean;
2. rescaling by the regularized feature standard deviation;
3. applying learned coordinatewise \(\gamma,\beta\).

The audit explicitly denies unconditional exact scale invariance when \(\varepsilon>0\).

No witness or figure identity changed.

## Audited baseline

- TRANSFORMER-001 merge:
  \`531a38072dff564649d53fb44eb1d3e07569fa70\`;
- audit issue:
  \`#56\`;
- chapter:
  \`ATLAS-CH-TRANSFORMER-001\`.

## 1. Residual-stream state

PASS.

For sequence length \(n\) and model width \(d\), the chapter uses

\[
H\in\mathbb R^{n\times d}.
\]

The initial state is written

\[
H_0
=
E(\text{tokens})+P,
\]

with positional information kept as a separate design axis.

The chapter does not privilege one positional scheme.

## 2. Attention object separation

PASS.

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

The chapter preserves the distinctions among:

- state;
- projected queries/keys/values;
- unnormalized scores;
- normalized mixing operator;
- value field;
- head output;
- full Transformer block.

The deeper operator analysis remains delegated to \`ATLAS-CH-ATTNOP-001\`.

## 3. Ideal causal mask

PASS.

For left-to-right self-attention,

\[
M_{ij}
=
\begin{cases}
0,&j\le i,\\
-\infty,&j>i.
\end{cases}
\]

In the ideal mathematical convention,

\[
\exp(-\infty)=0.
\]

Therefore after row softmax,

\[
\boxed{
A_{ij}=0
\qquad
(j>i).
}
\]

The chapter correctly treats this as an architectural support restriction, not a learned preference.

It also distinguishes the mathematical \(-\infty\) mask from finite-precision implementations.

## 4. Exact future-value independence witness

PASS.

The exact causal mixing matrix is

\[
A=
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

independent replay gives

\[
AV=(2,7/2,6)^\top.
\]

Changing only the future value gives

\[
V'=(2,5,101)^\top,
\]

and

\[
AV'=(2,7/2,36)^\top.
\]

The first two outputs remain exactly

\[
(2,7/2).
\]

This proves the declared future-value independence for the exact masked mixing operation.

It does not claim causal understanding in the scientific sense.

## 5. Multi-head aggregation

PASS.

The chapter uses

\[
C
=
\operatorname{Concat}(O_1,\ldots,O_m),
\]

and

\[
\operatorname{MHA}(H)=CW_O.
\]

The exact witness takes

\[
O_1=(1,2),
\qquad
O_2=(3,4),
\]

so

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

independent replay gives

\[
CW_O=(12,1).
\]

The chapter does not infer semantic head specialization from this factorization.

## 6. Position-wise feed-forward sublayer

PASS.

For token state \(h\),

\[
\operatorname{FFN}(h)
=
\phi(hW_1+b_1)W_2+b_2.
\]

The chapter correctly states that the same FFN parameters are reused across sequence positions within a layer while the operation itself acts position-wise.

This is distinguished from attention's cross-position mixing.

## 7. Layer Normalization definition

PASS AFTER REPAIR.

The chapter defines

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
\frac{x-\mu}
{\sqrt{\sigma^2+\varepsilon}}
+
\beta,
\qquad
\varepsilon>0.
\]

The repaired prose now describes this as:

- centering;
- regularized variance rescaling;
- learned coordinatewise affine transformation.

It no longer says LayerNorm simply “removes one affine scale/offset component.”

The chapter also now states explicitly that \(\varepsilon>0\) prevents an unconditional exact scale-invariance claim in general.

## 8. Post-LN ordering

PASS.

The chapter gives the original-Transformer-style ordering:

\[
Y
=
\operatorname{LN}
\left(
H+\mathcal A(H)
\right),
\]

\[
H'
=
\operatorname{LN}
\left(
Y+\mathcal F(Y)
\right).
\]

Residual addition occurs before normalization.

## 9. Pre-LN ordering

PASS.

The chapter gives:

\[
Y
=
H+\mathcal A(\operatorname{LN}(H)),
\]

\[
H'
=
Y+\mathcal F(\operatorname{LN}(Y)).
\]

The manuscript correctly treats pre-LN and post-LN as different computational graphs, not notation variants.

Xiong et al. are used only to document/analyze this ordering distinction and its training relevance.

No universal superiority claim is made.

## 10. Residual identity path

PASS.

For

\[
R(H)=H+S(H),
\]

if

\[
S(H)=0,
\]

then

\[
R(H)=H.
\]

Independent replay with

\[
H=(2,-1,3)
\]

returns the state unchanged exactly.

The chapter explicitly denies that this identity path alone guarantees good conditioning.

## 11. Encoder-only topology

PASS.

The chapter uses BERT only as a representative encoder-only family.

It correctly separates:

- encoder-only topology;
- task/pretraining masking choices.

It does not claim every encoder-only model always exposes every token to every other token.

## 12. Decoder-only topology

PASS.

The chapter uses GPT-2 only as a representative decoder-only autoregressive family.

It keeps decoder-only topology distinct from the broader category of language models.

The causal mask is treated as an architectural dependency constraint.

## 13. Encoder-decoder topology

PASS.

The chapter defines encoder memory

\[
E=\operatorname{Encoder}(X).
\]

For decoder cross-attention,

\[
Q=H_{\rm dec}W_Q,
\]

while

\[
K=EW_K,
\qquad
V=EW_V.
\]

Thus decoder state supplies queries and encoder memory supplies keys and values.

This is the correct baseline interface.

## 14. Architecture versus training recipe

PASS.

The chapter explicitly separates architecture from:

- pretraining objective;
- optimizer;
- learning-rate schedule;
- tokenizer;
- scale;
- context length;
- data mixture;
- implementation details.

The simplified pre-LN decoder-only equation is presented as a reference object, not as a universal “standard Transformer.”

## 15. Source scope

PASS.

### Vaswani et al. 2017

Used for:

- original encoder-decoder Transformer architecture;
- multi-head attention;
- FFN sublayers;
- residual connections;
- LayerNorm placement in the original architecture;
- positional encoding;
- causal masking in the decoder.

### Ba–Kiros–Hinton 2016

Used for Layer Normalization.

### Xiong et al. 2020

Used for the pre-LN/post-LN ordering distinction and analysis.

### Devlin et al. 2019

Used only as a representative encoder-only topology source.

### Radford et al. 2019

Used only as a representative decoder-only autoregressive topology source.

No topology is ranked as universally superior.

## 16. ARCHHIST provenance

PASS.

The source lock pins the audited ARCHHIST manuscript:

- commit:
  \`ecb15c976e4bb5cbc79b560ec19cbfdf9618607d\`;
- blob:
  \`3d373695ed5516dbc3b0557112f204636e911897\`.

Independent re-fetch matches exactly.

The seed inventory pin also matches:

- blob:
  \`ee83f2cadfcf725930b2076ba4c52ae1190647f8\`.

## 17. Bibliography closure

PASS.

The canonical bibliography contains:

- \`VaswaniEtAl2017\`;
- \`BaKirosHinton2016\`;
- \`XiongEtAl2020\`;
- \`DevlinChangLeeToutanova2019\`;
- \`RadfordEtAl2019\`.

## 18. Figure provenance

PASS.

\`ATLAS-FIG-TRANSFORMER-001\`:

- generator blob:
  \`1f2bc09736f1b5a2cbf6969c9edc24b625c4c283\`;
- rendered blob:
  \`3df30e0d94696afe5ca503cb30ad17609243d12c\`;
- rendered bytes:
  \`39,242\`.

The manifest matches the audited Git tree.

The figure is correctly classed schematic, with the center causal matrix carrying exact annotations.

## 19. Chapter status

PASS.

\`ATLAS-CH-TRANSFORMER-001\` remains:

\`draft-v0.1\`.

Its hard prerequisite remains:

- \`ATLAS-CH-ARCHHIST-001\`.

## 20. Final disposition

AUDIT-011 passes after one LayerNorm wording repair.

The durable baseline distinctions are:

\[
\text{attention}
\neq
\text{Transformer block}
\neq
\text{Transformer system},
\]

\[
\text{causal support restriction}
\neq
\text{learned attention preference},
\]

\[
\text{pre-LN}
\neq
\text{post-LN},
\]

\[
\text{architecture}
\neq
\text{training recipe}.
\]

The chapter is suitable to unlock its direct consumers after successful repository validation and merge of this audit.
