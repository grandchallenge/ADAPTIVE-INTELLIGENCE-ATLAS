# ATLAS-CH-TRANSFORMER-001 — Derivation Packet

## D1. Residual-stream state

For sequence length \(n\) and model width \(d\), let

\[
H\in\mathbb R^{n\times d}.
\]

Each row is one token-position state.

A conventional initial state is

\[
H_0
=
E(\text{tokens})+P,
\]

where \(P\) supplies positional information.

The positional mechanism is a separate design axis.

## D2. One attention head

For one head,

\[
Q=HW_Q,
\qquad
K=HW_K,
\qquad
V=HW_V.
\]

Define the masked score matrix

\[
S
=
\frac{QK^\top}{\sqrt{d_k}}+M.
\]

The row-normalized attention matrix is

\[
A
=
\operatorname{softmax}_{\rm row}(S).
\]

The head output is

\[
O=AV.
\]

These are four distinct objects:

\[
H
\to
(Q,K,V)
\to
S
\to
A
\to
O.
\]

The full Transformer block contains additional residual, normalization, and FFN operations.

## D3. Ideal causal mask

For left-to-right autoregressive self-attention, define

\[
M_{ij}
=
\begin{cases}
0,&j\le i,\\
-\infty,&j>i.
\end{cases}
\]

Row softmax uses

\[
A_{ij}
=
\frac{\exp(S_{ij})}
{\sum_k\exp(S_{ik})}.
\]

For any masked position \(j>i\),

\[
S_{ij}=-\infty,
\]

so in the ideal mathematical convention,

\[
\exp(S_{ij})=0.
\]

Therefore

\[
\boxed{
A_{ij}=0
\qquad
(j>i).
}
\]

Thus row \(i\) cannot depend on future value rows through the attention output.

Finite implementations generally realize this with masked-softmax logic or a sufficiently negative finite sentinel.

## D4. Exact three-token causal witness

Take all unmasked logits equal to zero.

Then each row is uniform over the permitted prefix:

\[
A
=
\begin{pmatrix}
1&0&0\\
1/2&1/2&0\\
1/3&1/3&1/3
\end{pmatrix}.
\]

Let scalar values be

\[
V
=
\begin{pmatrix}
2\\
5\\
11
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

Now replace only the future value

\[
v_3=11
\]

by

\[
v_3'=101.
\]

Then

\[
V'
=
\begin{pmatrix}
2\\
5\\
101
\end{pmatrix},
\]

and

\[
AV'
=
\begin{pmatrix}
2\\
7/2\\
36
\end{pmatrix}.
\]

The first two outputs are unchanged exactly.

This is a finite witness of future-value independence induced by the declared ideal mask.

## D5. Multi-head aggregation

For heads \(O_1,\ldots,O_m\),

\[
C
=
\operatorname{Concat}(O_1,\ldots,O_m).
\]

The multi-head output is

\[
\boxed{
\operatorname{MHA}(H)
=
C W_O.
}
\]

The output projection is part of the multi-head sublayer.

Different heads can occupy distinct projected subspaces before recombination.

## D6. Exact two-head witness

For one token, take

\[
O_1=(1,2),
\qquad
O_2=(3,4).
\]

Then

\[
C=(1,2,3,4).
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

Therefore

\[
CW_O
=
\boxed{
(12,1).
}
\]

This checks concatenation plus output projection only.

It is not an empirical claim about head specialization.

## D7. Position-wise feed-forward network

For one token state \(h\),

\[
\operatorname{FFN}(h)
=
\phi(hW_1+b_1)W_2+b_2.
\]

The same FFN parameters are applied to every token position in the layer.

Thus the FFN is position-wise in its state action while sharing parameters across positions.

This is distinct from attention, which mixes information across positions.

## D8. Layer Normalization

For token vector

\[
x\in\mathbb R^d,
\]

define

\[
\mu
=
\frac1d\sum_{i=1}^d x_i,
\]

\[
\sigma^2
=
\frac1d
\sum_{i=1}^d
(x_i-\mu)^2.
\]

Then

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

Normalization acts within each token state over the chosen feature dimension.

Before the learned affine parameters, the operation centers by the token's feature mean and rescales by the regularized feature standard deviation. Because (arepsilon>0) is explicit, the chapter does not claim exact invariance to arbitrary positive rescaling in general. The learned (gamma,eta) then apply coordinatewise affine parameters.

## D9. Post-LN block

The original Transformer uses residual addition followed by LayerNorm around each sublayer.

For attention sublayer \(\mathcal A\),

\[
Y
=
\operatorname{LN}
\left(
H+\mathcal A(H)
\right).
\]

For FFN sublayer \(\mathcal F\),

\[
H'
=
\operatorname{LN}
\left(
Y+\mathcal F(Y)
\right).
\]

The residual addition occurs before normalization.

## D10. Pre-LN block

A pre-LN arrangement moves normalization before each residual branch:

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

These equations are architecturally different from post-LN.

They should not be treated as notation variants.

## D11. Residual identity path

For any sublayer \(S\),

\[
R(H)
=
H+S(H).
\]

If

\[
S(H)=0,
\]

then

\[
\boxed{
R(H)=H.
}
\]

For exact witness state

\[
H=(2,-1,3),
\]

zero sublayer output gives exactly the same state.

The identity path does not imply the full trained Jacobian product is well-conditioned.

## D12. Encoder-only topology

An encoder-only Transformer stack applies unmasked or task-masked self-attention and FFN blocks to an input sequence.

At the baseline level:

\[
H_{l+1}
=
\operatorname{Block}_{\rm enc}^{(l)}(H_l).
\]

There is no autoregressive causal mask by architectural necessity.

Specific pretraining tasks may introduce their own masking schemes.

## D13. Decoder-only topology

A decoder-only autoregressive stack uses causal self-attention:

\[
H_{l+1}
=
\operatorname{Block}_{\rm dec}^{(l)}(H_l;M_{\rm causal}).
\]

The causal mask constrains the dependency graph before learned attention weights are normalized.

A readout head maps final token states to output logits or another declared target space.

## D14. Encoder-decoder topology

Let encoder memory be

\[
E
=
\operatorname{Encoder}(X).
\]

The decoder state first uses masked self-attention.

Cross-attention then uses:

\[
Q
=
H_{\rm dec}W_Q,
\]

\[
K
=
EW_K,
\]

\[
V
=
EW_V.
\]

Thus decoder queries read from encoder-produced keys and values.

This creates an explicit interface:

\[
\text{encoder memory}
\to
\text{decoder cross-attention}.
\]

## D15. Architecture versus training recipe

The architecture equations do not determine:

- dataset;
- pretraining objective;
- optimizer;
- batch size;
- learning-rate schedule;
- parameter count;
- context length;
- tokenizer;
- regularization;
- initialization.

These are separate experimental/system choices.

## Claim boundary

This packet defines baseline Transformer anatomy and exact toy witnesses.

It does not claim:

- that one normalization placement is universally superior;
- that attention weights are explanations;
- that one topology dominates the others;
- that causal masking alone guarantees good autoregressive modeling;
- that architecture equations determine training behavior.
