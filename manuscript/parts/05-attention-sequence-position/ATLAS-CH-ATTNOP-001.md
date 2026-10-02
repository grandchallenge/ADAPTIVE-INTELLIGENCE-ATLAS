# Attention as an Operator
<!-- ATLAS-CH-ATTNOP-001 -->

**Epistemic status:** mathematical exposition built from the standard Transformer equations, source-locked kernel interpretations, and Atlas-owned operator decompositions.  
**Primary figure:** \`ATLAS-FIG-ATTNOP-001\`  
**Derivation packet:** \`mathematics/derivations/ATLAS-CH-ATTNOP-001-DERIVATIONS.md\`

## 1. From an attention picture to an attention action

Attention is often introduced as a matrix of weights. The matrix is useful, but it is easy to confuse a picture of coefficients with the computation those coefficients perform.

For one attention head there are at least four distinct objects:

\[
\text{scores}
\longrightarrow
\text{mixing operator}
\longrightarrow
\text{value field}
\longrightarrow
\text{output}.
\]

The score matrix records pairwise compatibility. Softmax turns each score row into normalized mixing coefficients. Those coefficients define an operator acting on value vectors. The full attention transformation is nonlinear because both the operator and the values depend on the input state.

The useful allegory is a **dynamic switching board**.

Incoming channels carry values. The present state determines how strongly each channel contributes to each output. The board is not fixed; queries and keys reconfigure it.

The correspondence is:

- compatibility signal ↔ query-key score;
- switch configuration ↔ normalized mixing operator;
- incoming channels ↔ value vectors;
- outgoing channels ↔ mixed outputs.

The limit matters. Softmax attention is not discrete switching. It is differentiable weighted mixing, often dense, and the weights themselves are computed from the state. The board is a mnemonic for state-dependent transformation, not a literal circuit.

## 2. Standard scaled dot-product attention

Let

\[
X\in\mathbb R^{n\times d}
\]

contain \(n\) token representations.

For one head,

\[
Q=XW_Q,\qquad
K=XW_K,\qquad
V=XW_V.
\]

The score matrix is

\[
S(X)
=
\frac{QK^\top}{\sqrt{d_k}}.
\]

Row-wise softmax produces

\[
A(X)
=
\operatorname{softmax}_{\rm row}(S(X)),
\]

and the head output is

\[
Y=A(X)V.
\]

This is the standard scaled dot-product attention construction [@VaswaniEtAl2017].

The Atlas reserves different names for different roles:

\[
\boxed{
S=\text{score matrix}
}
\]

\[
\boxed{
A=\text{normalized mixing operator}
}
\]

\[
\boxed{
V=\text{value field}
}
\]

\[
\boxed{
F(X)=A(X)V(X)=\text{full attention transformation}.
}
\]

This distinction prevents several category errors. The score matrix is not the normalized operator. The operator is not the value field. And the fact that \(Y=AV\) is linear in \(V\) for fixed \(A\) does not make \(F\) linear in \(X\).

## 3. Why “operator” is the right word

Fix \(Q\) and \(K\). Then \(A\) is fixed.

For two value fields \(V_1,V_2\) and scalars \(\alpha,\beta\),

\[
A(\alpha V_1+\beta V_2)
=
\alpha AV_1+\beta AV_2.
\]

So

\[
V\mapsto AV
\]

is an ordinary linear operator on the value field.

The operator language changes the question.

A heat-map reading asks:

> Which coefficients are large?

An operator reading asks:

> What transformation is being performed on the information carried by the values?

The second question naturally leads to rank, singular values, invariants, sparsity, support constraints, approximation, perturbation, and composition.

Those are properties of transformations rather than images.

## 4. Softmax gives a row-stochastic mixing stage

For finite unmasked scores,

\[
A_{ij}
=
\frac{e^{S_{ij}}}
{\sum_{\ell=1}^n e^{S_{i\ell}}}.
\]

Therefore

\[
A_{ij}>0
\]

and

\[
\sum_{j=1}^n A_{ij}=1.
\]

Equivalently,

\[
\boxed{A\mathbf 1=\mathbf 1.}
\]

Each output row is a convex combination of value rows before any later output projection.

There is a useful but limited Markov analogy here. The rows lie on probability simplices. But an attention head is not generally a fixed Markov chain: the operator changes with the input, values are learned feature vectors rather than probabilities, and later transformations change the state again.

The algebraic fact is row-stochasticity. The Markov story is only an intuition aid.

## 5. The full self-attention map is nonlinear

Conditional linearity in \(V\) can produce the opposite mistake: calling the whole self-attention layer linear.

It is not.

Take two scalar tokens,

\[
X=
\begin{pmatrix}
1\\
0
\end{pmatrix},
\qquad
W_Q=W_K=W_V=1,
\qquad
d_k=1.
\]

Then

\[
Q=K=V=X,
\]

and

\[
S=XX^\top.
\]

The first output component is

\[
F(X)_1=\frac{e}{1+e}.
\]

Now double the input. The scores scale quadratically, so

\[
F(2X)_1
=
\frac{2e^4}{1+e^4}.
\]

But

\[
2F(X)_1
=
\frac{2e}{1+e}.
\]

Therefore

\[
F(2X)\neq 2F(X).
\]

Numerically the first-component discrepancy has magnitude about \(0.5019104228\).

The exact statement is:

> for fixed queries and keys, attention is linear in the value field; ordinary self-attention is nonlinear in the hidden state because the operator itself depends on that state.

## 6. A small operator we can inspect completely

The primary figure uses three tokens:

\[
Q=K=
\begin{pmatrix}
1&0\\
0&1\\
1&1
\end{pmatrix},
\qquad
V=
\begin{pmatrix}
1&0\\
0&1\\
1&-1
\end{pmatrix},
\qquad
d_k=2.
\]

Then

\[
S
=
\frac1{\sqrt2}
\begin{pmatrix}
1&0&1\\
0&1&1\\
1&1&2
\end{pmatrix}.
\]

Wolfram evaluation gives

\[
A\approx
\begin{pmatrix}
0.401112&0.197776&0.401112\\
0.197776&0.401112&0.401112\\
0.248255&0.248255&0.503490
\end{pmatrix},
\]

and

\[
Y=AV\approx
\begin{pmatrix}
0.802224&-0.203336\\
0.598888&0\\
0.751745&-0.255235
\end{pmatrix}.
\]

![Four numeric matrix panels showing the score matrix S, row-softmax mixing operator A, value field V, and output Y equals A V.](../../figures/masters/ATLAS-FIG-ATTNOP-001.png)

The gray intensity is deliberately redundant. Every cell carries its numerical value. The plate is intended to be read as a transformation rather than interpreted as a color pattern.

The computational witness verifies two bounded claims:

\[
A\mathbf 1=\mathbf 1
\]

to numerical precision, and, with \(A\) fixed,

\[
A(2V)=2AV.
\]

## 7. The operator changes when the query changes

Keep \(K\) and \(V\) fixed, but perturb the first query:

\[
q_1=(1,0)
\quad\longrightarrow\quad
q_1'=(1,\tfrac12).
\]

Only the first score row changes. Consequently, only the first row of the mixing operator changes.

The replay gives

\[
\Delta A_{1,:}
\approx
(-0.08124593,\;0.02683053,\;0.05441540).
\]

This exposes a useful local chain:

\[
\text{state perturbation}
\longrightarrow
\text{operator perturbation}
\longrightarrow
\text{changed information mixing}.
\]

Later chapters will ask whether a perturbation is causally important. Here the purpose is narrower: to make state dependence explicit.

## 8. Permutation equivariance before position enters

Suppose no positional signal or asymmetric mask is present.

Let \(P\) permute token order:

\[
X'=PX.
\]

Then

\[
Q'=PQ,\qquad
K'=PK,\qquad
V'=PV.
\]

Thus

\[
S'
=
\frac{Q'K'^\top}{\sqrt{d_k}}
=
PSP^\top.
\]

Row-wise softmax respects the simultaneous row/column permutation:

\[
A'=PAP^\top.
\]

Therefore

\[
Y'
=
A'V'
=
PAP^\top PV
=
PY.
\]

Hence

\[
\boxed{F(PX)=PF(X).}
\]

This is permutation **equivariance**, not invariance. Reordering inputs reorders outputs in the same way.

The result is useful precisely because sequence models need order-sensitive structure somewhere. Positional encodings and causal masks modify the admissible operator family and break arbitrary permutation symmetry.

## 9. A mask is a constraint on the operator family

For causal attention, define

\[
M_{ij}
=
\begin{cases}
0,&j\le i,\\
-\infty,&j>i.
\end{cases}
\]

Then

\[
A
=
\operatorname{softmax}_{\rm row}(S+M)
\]

satisfies

\[
A_{ij}=0
\qquad\text{for }j>i.
\]

The usual phrase says that a token “cannot attend to the future.”

The operator view says something slightly sharper:

> causal masking restricts the admissible support pattern of the mixing operator.

This places causal masking in the same mathematical family as local windows, graph adjacency, block sparsity, and learned sparse support.

## 10. Multihead attention is a family of state-dependent operators

For head \(h\),

\[
Q_h=XW_Q^{(h)},\qquad
K_h=XW_K^{(h)},\qquad
V_h=XW_V^{(h)},
\]

and

\[
A_h(X)
=
\operatorname{softmax}_{\rm row}
\left(
\frac{Q_hK_h^\top}{\sqrt{d_k}}
\right).
\]

Each head produces

\[
Y_h=A_hV_h.
\]

The layer then concatenates and projects the head outputs.

A useful abstraction is therefore

\[
X
\longmapsto
\{A_1(X),\ldots,A_H(X)\}
\longmapsto
\{A_1V_1,\ldots,A_HV_H\}
\longmapsto
Y.
\]

This is more informative than saying that a layer contains several attention maps. It contains a family of separately parameterized, state-dependent mixing operators whose outputs are recombined.

That viewpoint prepares later questions about head specialization, redundancy, substitution, spectral structure, and relative-position modes.

## 11. The kernel lens

Attention can also be written as normalized similarity-weighted smoothing. Tsai et al. develop an explicit kernel-smoother interpretation of Transformer attention [@TsaiEtAl2019].

In generic form,

\[
y_i
=
\frac{\sum_j k(q_i,k_j)v_j}
{\sum_j k(q_i,k_j)}.
\]

For

\[
k(q,k)
=
\exp\left(
\frac{q^\top k}{\sqrt{d_k}}
\right),
\]

this recovers ordinary softmax attention.

The lens is useful because it isolates the similarity function. But it does not erase the rest of the architecture. Queries and keys are learned and state-dependent; masks and position alter interactions; multihead attention constructs several such operators and recombines them.

The disciplined conclusion is:

> kernel language is one productive mathematical lens on attention, not a universal identification of every attention mechanism with one fixed kernel machine.

## 12. Feature maps and linear attention

Suppose the similarity has a feature representation

\[
k(q,k)=\phi(q)^\top\phi(k).
\]

Then a numerator

\[
\sum_j
\phi(q_i)^\top\phi(k_j)v_j^\top
\]

can be reassociated:

\[
\phi(q_i)^\top
\left(
\sum_j \phi(k_j)v_j^\top
\right).
\]

This is the algebraic move exploited by linear-attention constructions such as Katharopoulos et al. [@KatharopoulosEtAl2020].

From the Atlas viewpoint, the interesting fact is not merely lower asymptotic cost. The representation of the operator action has changed.

That prepares a later question:

> when we change the factorization or approximation of attention, which properties of the original operator survive?

## 13. Attention sensitivity has a concrete Jacobian

For one softmax row

\[
a=\operatorname{softmax}(s),
\]

the Jacobian is

\[
J_{\rm softmax}(a)
=
\operatorname{diag}(a)-aa^\top.
\]

A query perturbation \(\delta q_i\) changes the score row by

\[
\delta s_i
=
\frac{\delta q_iK^\top}{\sqrt{d_k}}.
\]

Therefore, to first order,

\[
\delta a_i
\approx
\left(
\operatorname{diag}(a_i)-a_i a_i^\top
\right)
\frac{\delta q_iK^\top}{\sqrt{d_k}}.
\]

This is already an interface-style sensitivity calculation. A representation perturbation induces an operator perturbation with a measurable local Jacobian.

Nothing about this calculation says that a large coefficient is semantically important. Sensitivity is not explanation.

## 14. Three distinctions that must remain visible

### 14.1 Score matrix versus mixing operator

The score matrix can contain arbitrary real values.

The softmax operator is positive and row-normalized. Adding a constant to one score row changes nothing:

\[
\operatorname{softmax}(s+c\mathbf 1)
=
\operatorname{softmax}(s).
\]

So even the score representation has a redundancy.

### 14.2 Mixing operator versus full head

The operator \(A\) determines how value rows mix. The value projection decides what information is available to be mixed. A visually striking \(A\) can have little downstream effect if the value/output pathway contributes little or is canceled.

### 14.3 Operator versus explanation

An observed \(A\) answers:

> what mixing coefficients were produced?

It does not automatically answer:

> which component caused the model’s output?

Causal claims require interventions, substitutions, ablations, or comparable evidence.

## 15. Why this viewpoint matters for position

Position is often introduced as extra information attached to vectors.

The operator view suggests a broader possibility: relative displacement may change how representations are transformed.

RoPE already points in that direction because displacement appears through compositions of rotations. Later the Atlas will ask whether position can be isolated into a low-dimensional family

\[
R(\Delta)
\]

acting on representation space.

That question is natural once attention is already being described through operator action and composition.

## 16. What the computational witness establishes

The figure and Wolfram replay establish:

1. a concrete score matrix \(S\);
2. a row-softmax operator \(A\);
3. a concrete value field \(V\);
4. the operator output \(Y=AV\);
5. row-stochasticity of \(A\);
6. linearity in \(V\) when \(A\) is fixed;
7. change in \(A\) under a query perturbation.

They do **not** establish:

- that an attention map explains a model decision;
- that a high weight is a causal feature importance;
- that the toy operator resembles a trained head;
- that kernel language is the only useful interpretation.

The witness makes the decomposition visible. It does not settle interpretation.

## 17. Atlas connections

**Approximate and structured attention.**  
Approximation can now be evaluated in terms of operator error, output error, complexity, and preserved structure.

**Position geometry.**  
Position can modify structured transformations rather than merely decorate vectors.

**Relative-position operators.**  
The operator vocabulary becomes explicit: displacement may be encoded by a low-dimensional transformation family.

**Retrieval.**  
Attention and retrieval both perform state-dependent selection and mixing, but differ in persistence, indexing, and externality.

**Mechanistic diagnosis.**  
Operator substitution and counterfactual replacement are stronger tests than coefficient inspection.

The recurring Atlas shift is now concrete:

\[
\boxed{
\text{vectors and pairwise scores}
\longrightarrow
\text{state-dependent operators acting on representations}.
}
\]

## 18. Closing view

The attention matrix is worth looking at.

Its deeper importance is that it **acts**.

A query-key state constructs a transformation. That transformation mixes information carried by values. Masks restrict its support. Position changes its structure. Heads create a family of such transformations. Approximation changes how the action is represented.

The dynamic switching board is only an allegory.

The operator is the object.

## References used in this chapter

- [@VaswaniEtAl2017]
- [@TsaiEtAl2019]
- [@KatharopoulosEtAl2020]

See \`sources/source-locks/ATLAS-CH-ATTNOP-001.yaml\` for exact source identities and claim scope.
