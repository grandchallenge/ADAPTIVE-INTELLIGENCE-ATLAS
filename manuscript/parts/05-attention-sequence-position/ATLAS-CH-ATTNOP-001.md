# Attention as an Operator
<!-- ATLAS-CH-ATTNOP-001 -->

**Epistemic status:** mathematical exposition built from the standard Transformer equations, source-locked kernel interpretations, and Atlas-owned operator decompositions.  
**Primary figure:** `ATLAS-FIG-ATTNOP-001`  
**Derivation packet:** `mathematics/derivations/ATLAS-CH-ATTNOP-001-DERIVATIONS.md`

## 1. From a picture of attention to the thing attention does

Attention is often introduced as a matrix of weights.

That matrix is useful. It is also easy to mistake the picture for the computation.

A heat map invites a visual reading: token (i) “looks at” token (j) with strength (A_{ij}). This language is serviceable until it quietly turns into a theory of mechanism. A bright cell can begin to sound like an explanation.

The Atlas will use a stricter distinction.

For one attention head there are at least four objects worth keeping separate:

[
	ext{scores}
quadlongrightarrowquad
	ext{mixing operator}
quadlongrightarrowquad
	ext{value field}
quadlongrightarrowquad
	ext{output}.
]

The score matrix determines a state-dependent pattern of interaction. Softmax converts that pattern into a normalized operator. The operator acts on value vectors. The full attention map is nonlinear because both the operator and the values are functions of the input state.

This chapter develops that statement carefully.

The useful allegory is a **dynamic switching board**.

A set of incoming channels carries values. The current configuration of the system determines how strongly each channel is routed into each output. The board is not fixed: queries and keys reconfigure it for the present state.

The correspondence is:

- incoming channels ↔ value vectors;
- compatibility signals ↔ query-key scores;
- switch configuration ↔ normalized attention operator;
- mixed outgoing channels ↔ (AV).

The limit of the allegory is important. Softmax attention is not discrete switching. It is differentiable weighted mixing, usually dense. The “board” is computed from the state rather than operated independently. And the visible mixing weights are not, by themselves, a causal explanation of the network.

What the allegory captures is narrower and more useful:

> attention constructs an operator from the current state and then applies that operator to information-bearing values.

## 2. Standard scaled dot-product attention

Let

[
Xinmathbb R^{n	imes d}
]

collect (n) token representations of width (d).

For one attention head,

[
Q=XW_Q,qquad
K=XW_K,qquad
V=XW_V,
]

with

[
Q,Kinmathbb R^{n	imes d_k},
qquad
Vinmathbb R^{n	imes d_v}.
]

The scaled score matrix is

[
S(X)
=
rac{QK^	op}{sqrt{d_k}}.
]

The Transformer formulation applies row-wise softmax [@VaswaniEtAl2017]:

[
A(X)
=
operatorname{softmax}_{m row}(S(X)).
]

Finally,

[
Y=A(X)V.
]

These equations are familiar. The Atlas changes the emphasis.

We will reserve different names for the different roles:

[
oxed{
S
=
	ext{score matrix}
}
]

[
oxed{
A
=
	ext{normalized mixing operator}
}
]

[
oxed{
V
=
	ext{value field}
}
]

[
oxed{
F(X)
=
A(X)V(X)
=
	ext{full attention transformation}.
}
]

This prevents several common category errors.

The score matrix is not the attention operator. The normalized operator is not the value field. And the fact that (Y=AV) is linear in (V) for fixed (A) does not make (F) linear in (X).

## 3. Why call (A) an operator?

For fixed (Q) and (K), the matrix (A) is fixed.

Then

[
Vmapsto AV
]

is a linear transformation from one value field to another.

If (V_1,V_2) are two fields and (alpha,eta) are scalars,

[
A(alpha V_1+eta V_2)
=
alpha AV_1+eta AV_2.
]

Nothing speculative is happening here. This is ordinary matrix linearity.

The word **operator** becomes useful because it changes the question we ask.

A weight-map reading asks:

> Which pairwise coefficients are large?

An operator reading asks:

> What transformation does this state-dependent matrix perform on the value field?

That second question naturally invites analysis of:

- invariants;
- stochastic structure;
- sparsity;
- rank;
- singular values;
- composition;
- approximation;
- masking;
- perturbation;
- position-dependent modification.

Those are properties of transformations, not merely pictures of coefficients.

## 4. Softmax creates a row-stochastic mixing operator

For finite unmasked scores,

[
A_{ij}
=
rac{e^{S_{ij}}}{sum_{ell=1}^n e^{S_{iell}}}.
]

Therefore

[
A_{ij}>0
]

and

[
sum_{j=1}^n A_{ij}=1.
]

Equivalently,

[
oxed{
Amathbf 1=mathbf 1.
}
]

Each output token receives a convex combination of the **value rows** before any later output projection.

This gives attention a Markov-like algebraic feature: rows lie on probability simplices.

The analogy should not be pushed too far.

A self-attention head is not generally a Markov chain evolving one fixed probability distribution. The operator itself changes with the input, the value vectors are learned representations rather than probabilities, and subsequent residual and feed-forward transformations alter the state.

Still, row-stochasticity is a real structural fact. It constrains the mixing stage.

## 5. The full map is nonlinear

The conditional linearity of (Vmapsto AV) is sometimes obscured by an opposite mistake: describing the entire self-attention layer as a linear operator.

Ordinary self-attention is not linear in (X).

The smallest counterexample makes this explicit.

Take two scalar tokens,

[
X=
egin{pmatrix}
1\
0
end{pmatrix},
]

and let

[
W_Q=W_K=W_V=1.
]

Then (d_k=1), (Q=K=V=X), and the score matrix is

[
S=XX^	op.
]

The resulting output is

[
F(X)
=
egin{pmatrix}
rac{e}{1+e}\[4pt]
rac12
end{pmatrix}.
]

Now double the input:

[
2X=
egin{pmatrix}
2\
0
end{pmatrix}.
]

Because scores depend quadratically on the state, the attention weights change:

[
F(2X)
=
egin{pmatrix}
rac{2e^4}{1+e^4}\[4pt]
1
end{pmatrix}.
]

But

[
2F(X)
=
egin{pmatrix}
rac{2e}{1+e}\[4pt]
1
end{pmatrix}.
]

The difference in the first component is

[
rac{2}{1+e}
-
rac{2}{1+e^4}
approx0.5019104228.
]

Hence

[
oxed{
F(2X)
e2F(X).
}
]

The correct statement is therefore:

> for fixed queries and keys, attention defines a linear operator on values; in self-attention, the operator is itself a nonlinear function of the state.

This distinction will matter later when we discuss relative-position operators and mechanistic interventions.

## 6. An operator you can inspect exactly

The primary figure uses a deliberately small three-token system.

Let

[
Q=K=
egin{pmatrix}
1&0\
0&1\
1&1
end{pmatrix},
]

[
V=
egin{pmatrix}
1&0\
0&1\
1&-1
end{pmatrix},
]

and (d_k=2).

Then

[
S
=
rac1{sqrt2}
egin{pmatrix}
1&0&1\
0&1&1\
1&1&2
end{pmatrix}.
]

Row-wise softmax gives

[
Aapprox
egin{pmatrix}
0.401112&0.197776&0.401112\
0.197776&0.401112&0.401112\
0.248255&0.248255&0.503490
end{pmatrix}.
]

Applying that operator to the value field yields

[
Y=AVapprox
egin{pmatrix}
0.802224&-0.203336\
0.598888&0\
0.751745&-0.255235
end{pmatrix}.
]

![Four numeric matrix panels showing the score matrix S, row-softmax mixing operator A, value field V, and the resulting output Y equals A V.](../../figures/masters/ATLAS-FIG-ATTNOP-001.png)

The gray intensity is redundant. Every cell carries its numerical value.

This is intentional. The figure is meant to be read as a transformation, not admired as a heat map.

The source-controlled Wolfram computation verifies that every row of (A) sums to one and that, with (A) fixed,

[
A(2V)-2(AV)=0.
]

The figure therefore carries a bounded mathematical claim: it is an exact computational witness for one attention operator.

## 7. The operator changes when the query changes

The same toy system makes state dependence visible.

Keep (K) and (V) fixed, but perturb only the first query:

[
q_1=(1,0)
quadlongrightarrowquad
q_1'=(1,1/2).
]

Only the first row of scores changes. Consequently, only the first row of the normalized operator changes.

Wolfram gives

[
Delta A_{1,:}
approx
(-0.081246, 0.026831, 0.054415),
]

with the remaining rows unchanged.

This is a useful local picture of attention:

[
	ext{state perturbation}
longrightarrow
	ext{operator perturbation}
longrightarrow
	ext{changed information mixing}.
]

Later diagnostic chapters will ask how to distinguish a perturbation that merely changes visible coefficients from one that changes behavior in a causally important way.

For now, the point is structural: (A) is not a static connectivity matrix. It is computed.

## 8. Permutation structure

Without positional information or an asymmetric mask, self-attention has a clean permutation symmetry.

Let (P) be a permutation matrix and reorder the tokens:

[
X'=PX.
]

Then

[
Q'=PQ,qquad
K'=PK,qquad
V'=PV.
]

The scores transform as

[
S'
=
rac{Q'K'^	op}{sqrt{d_k}}
=
PSP^	op.
]

Row-wise softmax respects this simultaneous row and column permutation:

[
A'=PAP^	op.
]

Therefore

[
Y'
=
A'V'
=
PAP^	op PV
=
PY.
]

So

[
oxed{
F(PX)=PF(X)
}
]

when the architecture contains no position-dependent or order-asymmetric structure.

This is **permutation equivariance**, not permutation invariance. Reordering the inputs reorders the outputs in the same way.

The result is useful precisely because Transformers for sequences need more than it. Sequence order must enter somewhere.

Positional encodings and causal masks alter the operator family so that arbitrary token permutations are no longer symmetries of the computation.

## 9. A mask is an operator constraint

Consider causal self-attention.

Introduce

[
M_{ij}
=
egin{cases}
0,&jle i,\
-infty,&j>i.
end{cases}
]

Then

[
A
=
operatorname{softmax}_{m row}(S+M).
]

The result satisfies

[
A_{ij}=0
qquad
	ext{for }j>i.
]

In token order, (A) is lower triangular.

The usual phrase is that a token “cannot attend to the future.” The operator view sharpens that:

> causal masking restricts the admissible support pattern of the mixing operator.

This makes masking comparable to other structural constraints:

- local windows;
- block sparsity;
- routing;
- graph adjacency;
- learned sparse support.

The question becomes not merely which cells were zeroed, but which transformations remain admissible after the constraint.

## 10. Multihead attention is a family of operators

A multihead layer computes separate projections

[
Q_h=XW_Q^{(h)},
qquad
K_h=XW_K^{(h)},
qquad
V_h=XW_V^{(h)}
]

for heads (h=1,dots,H).

Each head forms

[
A_h(X)
=
operatorname{softmax}_{m row}
left(
rac{Q_hK_h^	op}{sqrt{d_k}}
ight)
]

and output

[
Y_h=A_hV_h.
]

The head outputs are concatenated and projected.

A useful abstraction is therefore:

[
X
longmapsto
{A_1(X),dots,A_H(X)}
longmapsto
{A_1V_1,dots,A_HV_H}
longmapsto
Y.
]

This is not just “several attention maps.”

It is a collection of separately parameterized, state-dependent mixing operators whose outputs are recombined.

That viewpoint naturally suggests questions about head specialization:

- Do different heads occupy different operator regimes?
- Are their spectra or singular structures distinct?
- Are some heads redundant under substitution?
- Does position enter different operator modes in different heads?

Those questions belong to later diagnostic chapters. The present chapter supplies the object language.

## 11. Attention through the lens of kernels

Attention can also be read as normalized similarity-weighted smoothing.

Tsai et al. formulate Transformer attention through a kernel-smoother lens [@TsaiEtAl2019]. In a generic form,

[
y_i
=
rac{
sum_j k(q_i,k_j)v_j
}{
sum_j k(q_i,k_j)
}.
]

For exponential dot-product similarity,

[
k(q,k)
=
expleft(
rac{q^	op k}{sqrt{d_k}}
ight),
]

this recovers ordinary softmax attention.

The kernel view is useful because it makes the algebraic role of the similarity function explicit.

But “attention is a kernel method” needs qualification.

The query and key maps are learned. The kernel-like similarity is state-dependent through those learned representations. Position and masks alter the interaction structure. Multihead attention uses several such constructions and recombines their outputs.

The correct lesson is therefore:

> kernel methods provide one mathematically productive lens on attention, not a license to erase the architecture around the kernel.

## 12. Feature maps and linear attention

Suppose a similarity admits a feature representation

[
k(q,k)
=
phi(q)^	opphi(k).
]

Then an unnormalized numerator of the form

[
sum_j
phi(q_i)^	opphi(k_j)v_j^	op
]

can be reassociated:

[
phi(q_i)^	op
left(
sum_j
phi(k_j)v_j^	op
ight).
]

That algebra is central to linear-attention methods. Katharopoulos et al. use kernel feature maps and associativity to reorganize self-attention for efficient autoregressive computation [@KatharopoulosEtAl2020].

From the Atlas perspective, this is a revealing example.

The transformation has not merely been “approximated faster.” Its computational factorization has changed.

We have moved from an explicit (n	imes n) interaction operator to a factored representation of its action.

This prepares the later chapter on approximate and structured attention, where the central question will be:

> which properties of the operator are preserved when we change how its action is represented or computed?

## 13. Scores are not operators, and operators are not explanations

Three distinctions should remain visible.

### 13.1 Score matrix versus normalized operator

The score matrix

[
S=rac{QK^	op}{sqrt{d_k}}
]

can contain arbitrary real values.

The softmax operator (A) is positive and row-normalized.

Changing a row of (S) by an additive constant leaves the corresponding row of (A) unchanged.

Thus even the score representation has a redundancy:

[
operatorname{softmax}(s+cmathbf1)
=
operatorname{softmax}(s).
]

### 13.2 Mixing operator versus full head

The operator (A) mixes rows of (V).

The value projection (W_V) decides what information is available to be mixed.

A head with visually striking (A) can have little effect if its value/output pathway is weak or canceled elsewhere.

### 13.3 Operator versus explanation

An observed (A) answers:

> what mixing coefficients were produced?

It does not automatically answer:

> which component caused the model's decision?

Causal claims require interventions, substitutions, ablations, or other evidence.

Later chapters will move from interpretability as inspection toward interpretability as intervention.

## 14. Why operator language helps position encoding

Position is usually introduced as additional information attached to vectors.

The operator view suggests a broader possibility.

Suppose position changes how representations are transformed relative to one another. Then position may be better represented not as an extra vector but as a structured operator acting on the representation space.

RoPE already points in this direction: relative displacement emerges through compositions of rotations.

The later Relative-Position Operators chapter will ask whether useful positional structure can be isolated into a low-dimensional family

[
R(Delta)
]

acting on representation space.

That question would be awkward if attention were understood only as a colored matrix of pairwise weights.

It becomes natural once the architecture is already being discussed in terms of operators and their composition.

## 15. A local perturbation viewpoint

Because (A) depends on (Q) and (K), its sensitivity can be studied.

At a fixed state, a perturbation (delta q_i) induces

[
delta s_i
=
rac{delta q_i K^	op}{sqrt{d_k}}.
]

For a softmax row (a_i=operatorname{softmax}(s_i)), the Jacobian is

[
J_{m softmax}(a_i)
=
operatorname{diag}(a_i)-a_i a_i^	op.
]

Hence, to first order,

[
delta a_i
approx
left(
operatorname{diag}(a_i)-a_i a_i^	op
ight)
rac{delta q_iK^	op}{sqrt{d_k}}.
]

This is already a boundary-probe style calculation: a perturbation to a representation induces a perturbation to an operator.

We will not develop the full differential theory here. The point is to show that the operator perspective is not metaphorical. It gives concrete Jacobians that can be measured.

## 16. What the computational witness establishes

The Wolfram plate and witness establish four bounded facts.

First, the standard equations generate a concrete score matrix (S), mixing operator (A), and output (Y=AV).

Second,

[
Amathbf1=mathbf1
]

for the ordinary softmax rows.

Third, with (A) fixed,

[
Vmapsto AV
]

is linear.

Fourth, changing a query changes (A), and the full self-attention map is nonlinear in the state.

They do **not** establish:

- that one attention map explains a prediction;
- that a high coefficient is semantically important;
- that the toy operator resembles a particular trained head;
- that kernel language is the only correct interpretation of attention.

The witness makes the decomposition visible. It does not settle interpretation.

## 17. Five mistakes to avoid

### Mistake 1: “The score matrix is the attention operator.”

No. Softmax and masking intervene between scores and mixing.

### Mistake 2: “Attention is linear.”

Conditionally, (Vmapsto AV) is linear for fixed (A). Ordinary self-attention (Xmapsto A(X)V(X)) is nonlinear.

### Mistake 3: “Rows summing to one make attention a Markov process.”

No. Row-stochasticity characterizes the mixing stage. The operator is state-dependent and acts on learned values.

### Mistake 4: “A kernel interpretation makes attention a fixed kernel machine.”

No. Learned projections, state dependence, masks, position, and head composition matter.

### Mistake 5: “Attention weights explain the model.”

No. Inspection is not intervention.

These boundaries are not defensive qualifications. They preserve the utility of the operator viewpoint by keeping it exact.

## 18. Atlas connections

**Approximate and structured attention.**  
Once attention is an operator action, approximation can be evaluated in terms of operator error, output error, complexity, and preserved structure.

**Position geometry.**  
Position can modify or generate structured operators rather than merely decorate vectors.

**Relative-position operators.**  
The operator vocabulary becomes explicit: relative displacement may be encoded by a low-dimensional transformation family.

**Retrieval.**  
Attention and retrieval both perform state-dependent selection and mixing, but they differ in persistence, indexing, and externality.

**Mechanistic diagnosis.**  
Operator substitution and counterfactual replacement become stronger tests than heat-map inspection.

The recurring Atlas shift is now concrete:

[
oxed{
	ext{vectors and pairwise scores}
longrightarrow
	ext{state-dependent operators acting on representations}.
}
]

## 19. Closing view

The matrix (A) is worth looking at.

But its real importance is not that it is visible.

It is that it **acts**.

A query-key state constructs a transformation. That transformation moves information carried by values. Masks restrict its admissible support. Position changes its structure. Heads create a family of such transformations. Approximation changes how the action is represented.

Once attention is viewed this way, several apparently separate Transformer topics begin to share one mathematical language.

The dynamic switching board is only an allegory.

The operator is the object.

## References used in this chapter

- [@VaswaniEtAl2017]
- [@TsaiEtAl2019]
- [@KatharopoulosEtAl2020]

See `sources/source-locks/ATLAS-CH-ATTNOP-001.yaml` for exact source identities and claim scope.
