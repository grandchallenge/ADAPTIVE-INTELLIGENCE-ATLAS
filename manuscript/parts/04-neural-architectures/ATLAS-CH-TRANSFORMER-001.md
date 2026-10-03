# The Transformer as Baseline Object
<!-- ATLAS-CH-TRANSFORMER-001 -->

**Epistemic status:** Established Architecture + Atlas Synthesis + Exact Computational Witness  
**Specification:** manuscript/specifications/ATLAS-CH-TRANSFORMER-001.md  
**Derivation packet:** mathematics/derivations/ATLAS-CH-TRANSFORMER-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-TRANSFORMER-001.md  
**Source lock:** sources/source-locks/ATLAS-CH-TRANSFORMER-001.yaml

## 1. We need one reference object

The Atlas will later discuss:

- normalized Transformers;
- sparse Transformers;
- mixture-of-experts;
- split-operator residual transport;
- relative-position operators;
- adaptive depth;
- mechanistic diagnostics;
- network numerics.

Those chapters can only say what they change if the baseline object is explicit.

This chapter therefore asks a deliberately conservative question:

> What is the conventional Transformer object we are modifying?

The answer is not “attention.”

A Transformer is an organized state-update system built from:

- token-state representations;
- positional information;
- attention sublayers;
- position-wise feed-forward sublayers;
- residual paths;
- normalization;
- masking;
- topology;
- readout.

## 2. Attention is a component, not the architecture

The Attention-as-an-Operator chapter studies attention deeply.

Here we need less mathematics and more assembly.

One attention head computes a score-derived mixing operator and applies it to values.

A Transformer block then wraps that operation inside:

- projections;
- multi-head factorization;
- output projection;
- residual transport;
- normalization;
- a feed-forward sublayer.

So:

\[
\boxed{
\text{attention}
\neq
\text{Transformer block}
\neq
\text{Transformer system}.
}
\]

This distinction will matter repeatedly downstream.

## 3. The shared blackboard allegory

Imagine a shared blackboard.

Each token position owns one row.

Attention allows one row to read selected information from other rows.

A causal mask closes some sight lines before the read weights are normalized.

The feed-forward network then updates each row locally.

Residual paths preserve the evolving shared state while sublayers add corrections.

The analogy is useful because it separates:

- shared state;
- cross-row communication;
- local transformation;
- access restrictions.

Its limit is equally important.

The residual stream is not literally a blackboard service, and an attention weight is not automatically a semantic explanation.

## 4. Residual-stream state

Let sequence length be \(n\) and model width be \(d\).

Write the Transformer state as

\[
\boxed{
H\in\mathbb R^{n\times d}.
}
\]

Each row represents one sequence position.

The initial state is typically formed from token embeddings plus positional information:

\[
H_0
=
E(\text{tokens})+P.
\]

The positional mechanism \(P\) is a separate design axis.

The chapter does not assume that sinusoidal, learned, rotary, relative, or operator-valued position is universally correct.

## 5. One attention head

For one head,

\[
Q=HW_Q,
\qquad
K=HW_K,
\qquad
V=HW_V.
\]

The score matrix is

\[
S
=
\frac{QK^\top}{\sqrt{d_k}}+M.
\]

The row-normalized mixing matrix is

\[
A
=
\operatorname{softmax}_{\rm row}(S).
\]

The head output is

\[
O=AV.
\]

This creates a useful object chain:

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

Each object answers a different question.

## 6. Scores are not weights

The score matrix \(S\) is unnormalized.

The mixing matrix \(A\) is normalized row-wise.

The values \(V\) are the content being mixed.

The output \(O\) is the result of applying the mixing operator.

Therefore:

\[
\text{score}
\neq
\text{attention weight}
\neq
\text{value}
\neq
\text{output}.
\]

This may look elementary.

Many later diagnostic errors begin by collapsing these distinctions.

## 7. The original Transformer

Vaswani and colleagues introduced the Transformer architecture built around self-attention, multi-head attention, position-wise feed-forward layers, residual connections, LayerNorm, positional encoding, and an encoder-decoder topology [@VaswaniEtAl2017].

The historical claim here is source-scoped.

The Atlas uses that paper as the canonical source for the original architecture.

It does not claim every modern Transformer follows the original block ordering.

## 8. Multi-head attention

Suppose there are \(m\) heads.

Each head produces

\[
O_h.
\]

The outputs are concatenated:

\[
C
=
\operatorname{Concat}
(O_1,\ldots,O_m).
\]

The multi-head sublayer then applies an output projection:

\[
\boxed{
\operatorname{MHA}(H)
=
CW_O.
}
\]

The heads therefore do not simply remain separate.

Their projected outputs are recombined.

## 9. Exact two-head witness

Take one token and two head outputs:

\[
O_1=(1,2),
\]

\[
O_2=(3,4).
\]

Concatenate:

\[
C=(1,2,3,4).
\]

Let

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
\boxed{
CW_O=(12,1).
}
\]

This exact witness checks head concatenation and output projection only.

It says nothing about whether the heads learned distinct semantic roles.

## 10. Multi-head does not mean one monolithic attention matrix

Each head can have its own:

- query projection;
- key projection;
- value projection;
- score matrix;
- normalized mixing matrix.

The resulting head outputs are then concatenated and projected.

One can sometimes derive equivalent block representations.

But the baseline architecture should not be casually described as one giant attention matrix unless that equivalence is stated precisely.

The factorization is part of the architecture.

## 11. Causal masking is architectural access control

For left-to-right autoregressive self-attention, define the ideal causal mask:

\[
M_{ij}
=
\begin{cases}
0,&j\le i,\\
-\infty,&j>i.
\end{cases}
\]

After adding the mask to scores, future positions receive ideal score

\[
-\infty.
\]

Therefore their exponentiated contribution is zero.

After softmax,

\[
\boxed{
A_{ij}=0
\qquad
(j>i).
}
\]

The mask changes which dependencies are permitted before learned weights are normalized.

It is not a learned preference.

## 12. Mathematical mask versus implementation mask

The exact mathematical notation uses

\[
-\infty.
\]

Real systems usually implement this with:

- masked-softmax logic;
- a representable very negative number;
- fused attention kernels with explicit mask semantics.

That distinction matters.

The theorem is about zero support on forbidden positions.

The implementation is about realizing that support reliably in finite arithmetic.

## 13. Exact three-token causal witness

Take zero unmasked scores.

Then each row distributes weight uniformly over its allowed prefix:

\[
A
=
\begin{pmatrix}
1&0&0\\
1/2&1/2&0\\
1/3&1/3&1/3
\end{pmatrix}.
\]

Let

\[
V=
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

Now replace the third value only:

\[
V'
=
\begin{pmatrix}
2\\
5\\
101
\end{pmatrix}.
\]

Then

\[
AV'
=
\begin{pmatrix}
2\\
7/2\\
36
\end{pmatrix}.
\]

The first two outputs remain exactly unchanged.

The future value cannot affect earlier rows through this masked attention operation.

## 14. Causal mask does not imply causal understanding

The dependency graph is causal in the narrow left-to-right architectural sense:

future token states are unavailable.

This does not imply that:

- the model has discovered causal structure in the scientific sense;
- attention weights identify causal explanations;
- generated text is causally grounded.

“Causal mask” describes permitted sequence dependence.

Nothing more follows automatically.

## 15. Position-wise feed-forward network

After attention, the Transformer applies a feed-forward network independently at each position.

For token state \(h\),

\[
\boxed{
\operatorname{FFN}(h)
=
\phi(hW_1+b_1)W_2+b_2.
}
\]

The same FFN parameters are reused across sequence positions within the layer.

This is an important contrast:

- attention mixes across positions;
- FFN transforms each position locally in state space.

## 16. Different kinds of sharing

The architecture now contains several kinds of repeated structure.

Convolution shares a local kernel across spatial positions.

Recurrence shares one transition across time.

Transformer FFNs share one position-wise map across sequence positions.

Attention shares projection matrices across positions while the mixing pattern is content-dependent.

Parameter sharing is therefore not one phenomenon.

Its geometry depends on the operator.

## 17. Residual transport

A Transformer sublayer usually sits inside a residual connection.

Schematically:

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

The exact identity path from the Architecture History chapter survives here.

The sublayer adds a correction to the evolving residual-stream state.

## 18. Exact residual identity witness

Take

\[
H=(2,-1,3).
\]

Let

\[
S(H)=(0,0,0).
\]

Then

\[
H+S(H)
=
(2,-1,3).
\]

This is the precise identity-path claim.

It does not establish that the total Transformer Jacobian remains well conditioned.

## 19. Layer Normalization

Layer Normalization normalizes features within a state vector [@BaKirosHinton2016].

For

\[
x\in\mathbb R^d,
\]

define

\[
\mu(x)
=
\frac1d
\sum_i x_i,
\]

and

\[
\sigma^2(x)
=
\frac1d
\sum_i
(x_i-\mu)^2.
\]

Then

\[
\boxed{
\operatorname{LN}(x)
=
\gamma\odot
\frac{x-\mu}
{\sqrt{\sigma^2+\varepsilon}}
+
\beta.
}
\]

The stabilizing constant

\[
\varepsilon>0
\]

belongs in the definition.

## 20. LayerNorm is not bookkeeping

LayerNorm changes the representation.

Before the learned affine parameters are applied, it centers the declared feature vector by its sample mean and rescales it by the regularized sample standard deviation:

\[
x
\mapsto
\frac{x-\mu(x)}
{\sqrt{\sigma^2(x)+\varepsilon}}.
\]

It then applies learned coordinatewise scale and shift through \(\gamma\) and \(\beta\).

This operation changes:

- geometry;
- scale;
- derivative structure;
- how residual and sublayer signals interact.

It should not be summarized as an unconditional exact invariance to arbitrary affine rescaling. In particular, the explicit \(\varepsilon>0\) term breaks exact scale invariance in general, and learned \(\gamma,\beta\) restore trainable coordinatewise scale and offset after normalization.

Later normalized-geometry chapters will ask whether some normalization machinery can be replaced by more intrinsic constraints.

For now, LayerNorm is part of the baseline object.

## 21. Post-LN ordering

The original Transformer applies residual addition and then LayerNorm around a sublayer.

Write attention sublayer \(\mathcal A\).

Then

\[
Y
=
\operatorname{LN}
\left(
H+\mathcal A(H)
\right).
\]

For feed-forward sublayer \(\mathcal F\),

\[
H'
=
\operatorname{LN}
\left(
Y+\mathcal F(Y)
\right).
\]

This is a post-LN arrangement.

## 22. Pre-LN ordering

A common later design moves normalization before the residual branch:

\[
Y
=
H
+
\mathcal A
\left(
\operatorname{LN}(H)
\right),
\]

\[
H'
=
Y
+
\mathcal F
\left(
\operatorname{LN}(Y)
\right).
\]

Xiong and colleagues analyze pre-LN versus post-LN Transformer behavior and optimization differences [@XiongEtAl2020].

The Atlas uses that work only to support the architectural distinction and its training relevance.

It does not declare one ordering universally superior.

## 23. Pre-LN and post-LN are not notation variants

Compare:

\[
\operatorname{LN}
\left(
H+\mathcal A(H)
\right)
\]

with

\[
H+
\mathcal A
\left(
\operatorname{LN}(H)
\right).
\]

Normalization and nonlinear sublayer evaluation occur in different places.

The residual-stream state therefore evolves differently.

A chapter that says only “Transformer with LayerNorm” is underspecified.

## 24. Baseline pre-LN block

For later Atlas work, it is useful to display one common modern baseline:

\[
Y
=
H+\operatorname{MHA}(\operatorname{LN}(H)),
\]

\[
H'
=
Y+\operatorname{FFN}(\operatorname{LN}(Y)).
\]

This chapter uses that form for its main visual plate.

The choice is descriptive.

The original Transformer remains post-LN.

![A three-panel baseline Transformer plate showing a pre-LN residual-stream block, the exact 3x3 causal mixing matrix, and encoder-only/decoder-only/encoder-decoder topology families.](../../figures/masters/ATLAS-FIG-TRANSFORMER-001.png)

## 25. Positional information is a separate axis

Attention without positional information is permutation-sensitive only through content, not sequence order in the intended way.

The original Transformer adds positional encodings [@VaswaniEtAl2017].

Modern systems may instead use:

- learned absolute position;
- rotary position;
- relative bias;
- multidimensional schemes;
- operator-valued position.

The baseline object only requires that the positional mechanism be stated explicitly.

The Geometry of Position chapter develops this axis separately.

## 26. Encoder-only topology

An encoder-only Transformer applies self-attention and FFN blocks to an input sequence.

The attention pattern is not autoregressively causal by architectural necessity.

BERT is a representative encoder-only family [@DevlinChangLeeToutanova2019].

Its pretraining objectives and masking procedure are training/task choices layered on top of the architecture.

Encoder-only therefore does not mean:

> every token always sees every other token under every possible masking policy.

Topology and task masking are separate.

## 27. Decoder-only topology

A decoder-only autoregressive Transformer uses causally masked self-attention.

Each position can depend on:

- itself;
- previous positions;
- not future positions under the ideal mask.

GPT-2 is a representative decoder-only autoregressive family [@RadfordEtAl2019].

Again, the source is used only to document topology.

Decoder-only is not a synonym for every language model.

## 28. Encoder–decoder topology

The original Transformer uses two stacks.

The encoder produces memory:

\[
E
=
\operatorname{Encoder}(X).
\]

The decoder first uses masked self-attention over its generated prefix.

It then cross-attends to encoder memory.

For cross-attention:

\[
Q
=
H_{\rm dec}W_Q,
\]

while

\[
K
=
EW_K,
\]

and

\[
V
=
EW_V.
\]

Decoder queries therefore read from encoder-derived keys and values.

## 29. Cross-attention is an interface

Encoder-decoder architecture creates an explicit computational boundary:

\[
\text{encoder state}
\to
\text{decoder access}.
\]

Cross-attention is the read mechanism.

The interface can be interpreted using the same sufficiency questions developed earlier:

> Did the encoder memory preserve what the decoder still needs?

This becomes especially important in multimodal and modular systems.

## 30. Three topologies, three dependency graphs

The topology families differ in which state can directly interact.

### Encoder-only

Self-attention within one encoded sequence.

### Decoder-only

Causally restricted self-attention over a prefix.

### Encoder–decoder

Encoder self-attention, decoder causal self-attention, and decoder-to-encoder cross-attention.

These are graph differences.

They should not be collapsed into one generic phrase such as “a Transformer.”

## 31. Architecture versus training objective

A decoder-only Transformer can be trained with different objectives.

An encoder-only Transformer can be trained with different corruption/masking schemes.

An encoder–decoder Transformer can be used for different conditional tasks.

Therefore:

\[
\boxed{
\text{architecture}
\neq
\text{training objective}.
}
\]

The distinction is necessary for interpreting experimental claims.

## 32. Architecture versus optimizer

The block equations do not determine:

- SGD versus Adam;
- learning rate;
- warmup;
- clipping;
- weight decay;
- batch size;
- precision;
- initialization.

These choices alter training behavior without changing the nominal architecture.

The First-Order Optimization chapter treats that machinery separately.

## 33. Architecture versus scale

Two systems can share architecture and differ dramatically in:

- depth;
- width;
- head count;
- context length;
- vocabulary;
- parameter count;
- training compute.

Calling both “Transformers” can be correct and still conceal most of the engineering difference.

The Atlas therefore uses architecture labels carefully.

## 34. Architecture versus tokenizer

A Transformer consumes token states.

How text becomes tokens is external to the Transformer block.

Different tokenizers can change:

- sequence length;
- morphology;
- multilingual fertility;
- information boundaries;
- effective context usage.

The Tokenization chapter will treat that interface separately.

## 35. The residual stream as the persistent state

The Architecture History chapter moved from static composition toward state transport.

The Transformer makes that transport explicit through repeated additive residual updates.

One useful lens is:

\[
H_0
\to
H_1
\to
\cdots
\to
H_L.
\]

Attention and FFN sublayers write corrections into this evolving state.

This residual-stream viewpoint will matter in:

- mechanistic analysis;
- split operators;
- routing;
- normalization geometry;
- adaptive depth.

## 36. But “residual stream” is not an ontological primitive

The residual stream is an architectural coordinate system.

Another architecture may store equivalent information through:

- recurrent state;
- external memory;
- operator state;
- sparse experts;
- multiple coupled streams.

The Atlas uses the residual stream as a baseline object, not as the unique natural representation of computation.

## 37. Attention as communication, FFN as local transformation

A useful first approximation is:

- attention:
  position-to-position communication;
- FFN:
  position-local nonlinear transformation.

This is not a complete mechanistic theory.

Attention changes state content.

FFNs can implement complex feature transformations.

Residual mixing across layers entangles the two.

Still, the decomposition is operationally useful.

## 38. Multi-head factorization creates multiple projected interaction spaces

Each head receives its own projected Q/K/V spaces.

Thus head \(h\) operates on

\[
Q_h,
K_h,
V_h.
\]

The outputs are later recombined.

This creates a structured factorization of the communication mechanism.

It does not guarantee that every head learns a cleanly separable function.

Later mechanistic chapters will test specialization rather than assume it.

## 39. Masking changes the operator support

A causal mask sets certain attention entries to zero after normalization.

A sparse mask can remove other edges.

A local-window mask restricts interaction distance.

Therefore masking changes the support of the mixing operator.

This will connect directly to sparse computation and structured attention.

## 40. Normalization placement changes the update law

In post-LN:

\[
H
\mapsto
\operatorname{LN}(H+S(H)).
\]

In pre-LN:

\[
H
\mapsto
H+S(\operatorname{LN}(H)).
\]

The residual state is therefore normalized at different points in the computation.

This becomes crucial when asking whether normalized geometry should be enforced intrinsically rather than repeatedly imposed.

## 41. Residual identity path is necessary context for depth

Because each block contains an additive identity path, a deep Transformer is not simply a composition of unrelated maps.

It is a sequence of corrections around a transported state.

This is one reason depth admits a dynamical interpretation.

But the earlier warning remains:

\[
\text{identity path}
\not\Rightarrow
\text{automatic stability}.
\]

The product of block Jacobians still matters.

## 42. The baseline object in one equation

A simplified pre-LN decoder-only block can be written:

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

This is the reference object many later Atlas chapters will modify.

They may change:

- normalization;
- position;
- attention approximation;
- sparsity;
- expert routing;
- depth;
- residual transport;
- memory.

## 43. What the baseline does not contain

The equation above does not specify:

- tokenizer;
- embedding tying;
- bias conventions;
- dropout;
- activation function;
- attention kernel implementation;
- KV cache;
- sequence packing;
- distributed parallelism;
- optimizer;
- objective;
- data mixture.

Those are real system choices.

They are simply outside this baseline architectural abstraction.

## 44. Failure modes of vague Transformer language

### “Attention model”

Too coarse.

It hides residual and FFN structure.

### “Causal Transformer”

Still underspecified.

Normalization placement and topology remain open.

### “Standard Transformer”

Often ambiguous between the 2017 post-LN encoder-decoder and later pre-LN decoder-only systems.

### “Transformer layer”

Can refer to different arrangements of attention, cross-attention, FFN, normalization, and residuals.

The cure is equations.

## 45. Atlas connections

**Attention as an Operator.**  
Supplies the deeper score/operator/value analysis.

**Geometry of Position.**  
Treats position as a mathematical object rather than an embedding afterthought.

**Normalized representations.**  
Questions whether LayerNorm-like machinery should be replaced by intrinsic constraints.

**Split operators.**  
Treats attention and FFN/residual updates as composable evolution operators.

**Mixture-of-experts.**  
Replaces or augments the FFN sublayer with routed conditional computation.

**Mechanistic diagnostics.**  
Uses the residual stream, heads, keys, queries, values, and MLP channels as intervention sites.

**Adaptive depth.**  
Questions whether every token/input requires the same number of block updates.

## 46. What would falsify a baseline claim?

A baseline statement should be architectural and checkable.

If we claim a mask is causal, inspect support.

If we claim a block is pre-LN, inspect equations.

If we claim an architecture is decoder-only, inspect whether encoder memory/cross-attention exists.

If we claim identity transport, zero the sublayer and verify state preservation.

If we claim position-wise FFN sharing, inspect parameter reuse across positions.

If the implementation violates the equations, the label is wrong.

## 47. Closing view

The Transformer is not one idea.

It is an assembly of:

- projected communication;
- normalized mixing;
- position-local nonlinear transformation;
- residual transport;
- normalization;
- masking;
- topology.

That assembly became a baseline because it is modular enough to vary and stable enough to serve as a reference point.

The Atlas now has a precise object to depart from.

From here, later chapters can ask sharper questions:

- What if normalization becomes geometry?
- What if position becomes an operator?
- What if depth becomes adaptive time?
- What if FFNs become routed experts?
- What if attention is approximated or split?
- What if persistent memory moves outside the weights?

Those questions only become meaningful once “the Transformer” stops being a vague noun and becomes an explicit computational object.

## References used in this chapter

- [@VaswaniEtAl2017]
- [@BaKirosHinton2016]
- [@XiongEtAl2020]
- [@DevlinChangLeeToutanova2019]
- [@RadfordEtAl2019]

See \`sources/source-locks/ATLAS-CH-TRANSFORMER-001.yaml\` for exact source roles, internal Atlas provenance, and claim boundaries.
