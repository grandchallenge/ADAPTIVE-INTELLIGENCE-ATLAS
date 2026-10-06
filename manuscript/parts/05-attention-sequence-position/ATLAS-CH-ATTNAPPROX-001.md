# Approximate and Structured Attention
<!-- ATLAS-CH-ATTNAPPROX-001 -->

**Epistemic status:** audited attention/Krylov substrate + primary Performer, Linformer, Nyströmformer, and alpha-entmax sources + Atlas synthesis.  
**Specification:** manuscript/specifications/ATLAS-CH-ATTNAPPROX-001.md  
**Derivation packet:** mathematics/derivations/ATLAS-CH-ATTNAPPROX-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-ATTNAPPROX-001.md  
**Source lock:** sources/source-locks/ATLAS-CH-ATTNAPPROX-001.yaml

Approximate attention is not one problem.

A method may approximate the exponential kernel before normalization.

Another may compress the normalized attention matrix.

Another may avoid constructing that matrix by projecting keys and values into a lower-dimensional sequence space.

Another may intentionally replace softmax with a sparse probability map.

All four can be called “efficient attention.”

Mathematically, they are different operations.

This chapter imposes one rule before any speed or accuracy claim:

> name the object that changed.

The rule sounds administrative.

It is actually the shortest route to clear mathematics.

## 1. The attention stack

For one head, let

\[
Q=XW_Q,
\qquad
K_{\rm key}=XW_K,
\qquad
V=XW_V.
\]

To avoid using K for both “keys” and “kernel,” write the score matrix as

\[
S
=
\frac{QK_{\rm key}^\top}{\sqrt{d_k}}.
\]

Now define the positive exponential kernel matrix

\[
G_{ij}
=
e^{S_{ij}}.
\]

Its row sums are

\[
z_i
=
\sum_j G_{ij}.
\]

Let

\[
D_G
=
\operatorname{diag}(z_1,\ldots,z_n).
\]

The normalized attention operator is

\[
A
=
D_G^{-1}G.
\]

Finally,

\[
Y=AV.
\]

The audited Attention-as-an-Operator chapter already separated:

\[
S
\longrightarrow
A
\longrightarrow
V
\longrightarrow
Y.
\]

This chapter inserts one more object:

\[
S
\longrightarrow
G
\longrightarrow
A
\longrightarrow
V
\longrightarrow
Y.
\]

That extra step matters because several efficient-attention methods act on G, while others act on A, K/V sequence structure, or the normalization itself.

## 2. Five different approximation statements

Suppose a method produces hatted objects.

The following statements are not interchangeable.

### Score approximation

\[
\widehat S\approx S.
\]

This concerns pairwise compatibility before exponentiation.

Small score error can be magnified by exponentiation, especially when norms are large.

### Kernel approximation

\[
\widehat G\approx G.
\]

This is the natural target for random-feature approximations of the exponential dot-product kernel.

### Operator approximation

\[
\widehat A\approx A.
\]

This is the natural target if we care about the actual mixing coefficients.

### Output approximation

\[
\widehat Y
=
\widehat A V
\approx
AV.
\]

This is weaker than operator approximation when tested on only one value field.

### Alternative operator

\[
\widetilde A
=
T(S),
\]

where T is deliberately not softmax.

Alpha-entmax belongs here.

The method can be valuable without being an estimator of softmax.

The distinction is the central organizing principle of this chapter.

## 3. Why raw kernel error can mislead

Softmax is invariant to adding a constant to a score row.

For any row i,

\[
\operatorname{softmax}(s_i+c_i\mathbf 1)
=
\operatorname{softmax}(s_i).
\]

After exponentiation, this is positive row scaling.

Let C be any positive diagonal matrix.

Then

\[
D(CG)^{-1}CG
=
D(G)^{-1}G.
\]

So replacing G by CG leaves A unchanged.

Take the simplest case:

\[
\widehat G=cG.
\]

Then

\[
\widehat A=A,
\]

but

\[
\|\widehat G-G\|_F
=
|c-1|\|G\|_F.
\]

By taking c large, the raw kernel error becomes arbitrarily large while the attention operator does not move at all.

This is not a pathology.

It is the algebraic expression of a symmetry already present in softmax.

The practical lesson is:

> kernel error is meaningful only together with the normalization convention and the route by which kernel error propagates to normalized attention.

## 4. Kernel error needs denominator control

Take one positive kernel row g.

Let

\[
z=\mathbf 1^\top g.
\]

Suppose

\[
\widehat g=g+e,
\qquad
\widehat z=z+\delta,
\qquad
\delta=\mathbf 1^\top e.
\]

The normalized rows are

\[
a=\frac g z,
\qquad
\widehat a=\frac{g+e}{\widehat z}.
\]

Direct subtraction gives

\[
\widehat a-a
=
\frac e{\widehat z}
-
\frac{g\delta}{z\widehat z}.
\]

Hence

\[
\|\widehat a-a\|_1
\le
\frac{2\|e\|_1}{\widehat z}.
\]

If

\[
\|e\|_1\le \rho z
\]

with \(0\le\rho<1\), then

\[
\widehat z\ge(1-\rho)z
\]

and therefore

\[
\|\widehat a-a\|_1
\le
\frac{2\rho}{1-\rho}.
\]

The bound is intentionally elementary.

Its purpose is not to replace Performer’s analysis.

It isolates the missing ingredient in vague statements such as “the kernel is close, so attention is close.”

Normalization must be controlled too.

## 5. Positive random features

The exponential dot-product kernel has a useful probabilistic representation.

Let

\[
\omega\sim N(0,I)
\]

and define

\[
\phi_\omega(x)
=
\exp
\left(
\omega^\top x
-
\frac12\|x\|_2^2
\right).
\]

Then

\[
\mathbb E_\omega[
\phi_\omega(q)\phi_\omega(k)
]
=
e^{q^\top k}.
\]

The derivation is one line of Gaussian moment-generating algebra after expanding

\[
\|q+k\|_2^2.
\]

For scaled dot-product attention, choose

\[
q'
=
\frac{q}{d_k^{1/4}},
\qquad
k'
=
\frac{k}{d_k^{1/4}},
\]

so

\[
q'^\top k'
=
\frac{q^\top k}{\sqrt{d_k}}.
\]

Therefore

\[
e^{q^\top k/\sqrt{d_k}}
\]

inherits the same positive random-feature identity.

This is the clean mathematical reason random features are relevant to softmax attention.

## 6. From an expectation identity to Performer

A finite feature approximation replaces the expectation by an average:

\[
\widehat G_{ij}
=
\frac1m
\sum_{r=1}^m
\phi_{\omega_r}(q_i')
\phi_{\omega_r}(k_j').
\]

With independent Gaussian features, the kernel estimator is unbiased entrywise.

But “unbiased” does not mean “small error in one run.”

The finite estimator has variance.

The normalized operator is a ratio involving the approximate row sums.

Finite precision can matter because exponentials span large ranges.

And the cost depends explicitly on the feature count m.

Performer addresses this setting with FAVOR+, Fast Attention Via positive Orthogonal Random features [@ChoromanskiEtAl2021Performer].

The primary source develops positive orthogonal random features and source-specific accuracy/variance guarantees for softmax-kernel attention.

The Atlas inherits that result at its stated scope.

It does not convert “random features” in general into a guarantee.

## 7. Why feature attention can avoid the dense matrix

Write feature matrices

\[
\Phi_Q\in\mathbb R^{n\times m},
\qquad
\Phi_K\in\mathbb R^{n\times m}.
\]

Then

\[
\widehat G
=
\Phi_Q\Phi_K^\top.
\]

The numerator can be associated as

\[
\widehat G V
=
\Phi_Q
\left(
\Phi_K^\top V
\right).
\]

The denominator is

\[
\widehat G\mathbf 1
=
\Phi_Q
\left(
\Phi_K^\top\mathbf 1
\right).
\]

So the normalized output can be computed without constructing the full \(n\times n\) matrix.

This is the computational move.

The cost is linear in n only after exposing what is held fixed, especially m and the feature/value widths.

The word “linear” is therefore shorthand for a scaling regime, not a property independent of approximation budget.

## 8. Low-rank attention is another idea

Linformer starts from a different structural premise [@WangEtAl2020Linformer].

Its motivating claim is that self-attention can often be represented or approximated through a low-dimensional sequence structure.

Rather than Monte Carlo features for the exponential kernel, Linformer projects key/value sequence dimensions into a smaller width.

The distinction matters.

A random-feature method asks:

> can I approximate the kernel action through features?

A low-rank projection method asks:

> can I compress the sequence interaction into a lower-dimensional subspace?

Both reduce cost.

They do not have the same approximation variable.

For Performer-like methods the explicit budget is feature count m.

For Linformer-like methods it is a projection/rank width k.

A theorem about one budget does not automatically say anything about the other.

## 9. Low rank is a hypothesis, not a universal property

Any matrix has a rank.

Saying that an attention operator has a useful low-rank approximation is stronger.

It says that most of the relevant action can be captured with fewer directions than the ambient sequence length.

That may occur.

It need not occur uniformly across:

- layers;
- heads;
- inputs;
- training stages;
- positional regimes;
- masks;
- distribution shifts.

The correct experimental question is not:

> is attention low rank?

It is:

> for this declared target, norm, data regime, and rank budget, how much error remains?

This is the same discipline that classical low-dimensional numerical methods demand.

The audited Krylov chapter supplies vocabulary for reduced action.

It does not supply a convergence theorem for learned attention.

## 10. Landmark reconstruction: Nyströmformer

Nyströmformer uses a landmark-based route [@XiongEtAl2021Nystromformer].

The broad Nyström idea is to reconstruct a large matrix from interactions involving a smaller landmark set.

Schematically, one encounters an approximation of the form

\[
\widehat A
\approx
C W^\dagger R,
\]

where W is a reduced landmark block and C/R connect the full matrix to the landmarks.

Nyströmformer adapts this idea to softmax self-attention.

This introduces a third approximation budget:

\[
m
=
\text{number of landmarks}.
\]

Again, the reduced representation is not the same object as random features.

A landmark is not a Gaussian feature.

A pseudoinverse-like reduced solve is not a Monte Carlo average.

The shared idea is economy through structure, not mathematical identity.

## 11. Conditioning belongs in the landmark story

Reduced systems can be small and still be numerically awkward.

Whenever reconstruction involves an inverse or pseudoinverse-like operation, conditioning matters.

A reduced matrix that is nearly singular can amplify perturbations.

This is where the Krylov chapter contributes a useful habit:

> never identify a computable residual or reduced dimension with the true target error without the operator relation that connects them.

For attention, the analogous warning is:

> a small landmark system does not by itself imply a small reconstruction error.

Landmark quality, matrix structure, numerical conditioning, and the chosen norm remain part of the claim.

## 12. Sparse attention can mean a different normalization

Softmax has a rigid property.

For finite scores,

\[
\operatorname{softmax}(s)_i>0
\]

for every coordinate.

The resulting row is dense.

The alpha-entmax family changes this geometry [@PetersNiculaeMartins2019Entmax].

For alpha greater than one, entmax can produce exact zeros.

At alpha equal to two, the family gives sparsemax.

This is not merely “softmax with a cheap approximation.”

It is a different score-to-simplex map.

That distinction is useful because exact sparsity may be the desired inductive bias.

It is also necessary because a sparse alternative should not be penalized as a bad softmax estimator when reproducing softmax was never its goal.

## 13. An exact sparse-support witness

Take

\[
s=(2,0,-1).
\]

Softmax gives

\[
\frac1{e^2+1+e^{-1}}
(e^2,1,e^{-1}).
\]

All entries are positive.

For sparsemax, use the simplex-projection threshold form

\[
p_i=\max(s_i-\tau,0).
\]

With

\[
\tau=1,
\]

we obtain

\[
p=(1,0,0).
\]

So

\[
\operatorname{entmax}_2(2,0,-1)
=
(1,0,0).
\]

One map mixes all three positions.

The other selects one exactly.

The difference is structural, not a rounding artifact.

## 14. Sparsity and low rank are independent

A sparse matrix can have full rank.

The identity matrix is the simplest example.

A low-rank matrix can be completely dense.

For example,

\[
\frac1n\mathbf 1\mathbf 1^\top
\]

has rank one and no zero entries.

Therefore

\[
\text{sparse}
\not\Rightarrow
\text{low rank},
\]

and

\[
\text{low rank}
\not\Rightarrow
\text{sparse}.
\]

This prevents another common collapse of vocabulary.

“Structured attention” is a family name.

The structures inside the family remain different.

## 15. Exact sparsity is not yet a complexity theorem

Suppose we first form

\[
S=QK_{\rm key}^\top.
\]

That step already considers all token pairs.

If a later normalization turns most coefficients into zero, the dense pairwise score cost has already been paid.

So

\[
\text{many zeros in }A
\]

does not by itself imply

\[
\text{cheap attention}.
\]

To obtain computational savings, the implementation must exploit structure earlier or later in a way that changes actual work.

Examples include:

- structured neighborhoods;
- block support;
- hashing/routing;
- feature factorization;
- low-rank projection;
- landmark reconstruction;
- hardware-efficient sparse kernels.

The exact mechanism matters.

## 16. Three error surfaces

The Atlas uses three primary numerical surfaces.

### Kernel error

\[
E_G
=
\|\widehat G-G\|.
\]

This is natural for random-feature methods.

But it is sensitive to row scale.

### Operator error

\[
E_A
=
\|\widehat A-A\|.
\]

This measures the mixing transformation itself.

It is the central comparison surface when the target is ordinary softmax attention.

### Output error

\[
E_Y
=
\|\widehat A V-AV\|.
\]

This measures one realized action on one value field.

For fixed V,

\[
E_Y
\le
\|\widehat A-A\|_2\|V\|_F.
\]

The reverse implication fails from one V.

A large operator discrepancy can lie in directions not excited by the chosen value field.

## 17. A small exact operator approximation

Consider

\[
A=
\begin{pmatrix}
1/2&1/3&1/6\\
1/2&1/3&1/6\\
1/6&1/3&1/2
\end{pmatrix}.
\]

It is positive and row-stochastic.

Its rank is two.

Now replace all rows by their average:

\[
\widehat A=
\begin{pmatrix}
7/18&1/3&5/18\\
7/18&1/3&5/18\\
7/18&1/3&5/18
\end{pmatrix}.
\]

This approximation is rank one.

The exact error is

\[
A-\widehat A
=
\frac19
\begin{pmatrix}
1&0&-1\\
1&0&-1\\
-2&0&2
\end{pmatrix}.
\]

Therefore

\[
\|A-\widehat A\|_F^2
=
\frac4{27}
\]

and

\[
\|A-\widehat A\|_2
=
\frac{2\sqrt3}{9}.
\]

The witness is not intended to imitate a trained head.

It exists so every quantity can be inspected exactly.

## 18. The same operator error can look smaller after acting on values

Take

\[
V=
\begin{pmatrix}
1&0\\
0&1\\
1&-1
\end{pmatrix}.
\]

Then

\[
AV=
\begin{pmatrix}
2/3&1/6\\
2/3&1/6\\
2/3&-1/6
\end{pmatrix}
\]

and

\[
\widehat A V=
\begin{pmatrix}
2/3&1/18\\
2/3&1/18\\
2/3&1/18
\end{pmatrix}.
\]

The squared output error is

\[
\frac2{27}.
\]

This is smaller than the squared Frobenius operator error,

\[
\frac4{27}.
\]

Nothing paradoxical has happened.

V does not probe every operator direction equally.

This is why output fidelity and operator fidelity must be reported separately.

## 19. Task performance is a fourth question

Suppose a model is retrained with an approximate mechanism and reaches the same benchmark score as a standard Transformer.

That is important empirical evidence.

It still does not prove

\[
\widehat A\approx A
\]

for the corresponding softmax operator.

The trained model may compensate elsewhere.

Its representations may reorganize.

Its heads may specialize differently.

The approximate mechanism may be better for the task while being farther from softmax.

Thus we should ask four questions separately:

1. Is the kernel close?
2. Is the normalized operator close?
3. Is the output on the declared V close?
4. Does the trained system perform well?

The fourth does not subsume the first three.

## 20. Complexity must expose the approximation budget

Standard dense attention pays for pairwise interactions across n tokens.

Feature methods replace n-by-n interaction with a feature width m.

Low-rank methods replace sequence dimension with a projection width k.

Landmark methods replace full interaction with m landmarks.

Sparse methods introduce a support size only if the implementation actually exploits it.

Therefore every scaling statement should look like:

> cost as a function of n, with m/k/support budget declared.

The phrase “linear attention” is only meaningful after that declaration.

If maintaining a fixed error tolerance requires m to grow with n, the effective complexity can change.

## 21. Accuracy-cost curves are more informative than single points

A fair comparison should sweep the approximation budget.

For random features:

\[
m=16,32,64,\ldots
\]

For low-rank projection:

\[
k=16,32,64,\ldots
\]

For landmarks:

\[
m=16,32,64,\ldots
\]

For sparse alternatives, vary alpha or the mechanism’s support-control parameter when appropriate.

At each budget, measure:

- wall-clock or kernel time;
- memory;
- kernel/operator/output error where defined;
- support/rank diagnostics;
- downstream performance if training is part of the experiment.

One point can hide the shape of the tradeoff.

The curve is the object.

## 22. Masks must remain in the target definition

Causal attention is not ordinary unmasked attention followed by a cosmetic display rule.

The mask constrains support.

If

\[
M_{ij}=-\infty
\]

for forbidden interactions, the exact target operator has zeros there.

An approximation must state whether it:

- preserves those zeros exactly;
- approximates only the allowed region;
- uses a causal recurrence;
- leaks mass into forbidden positions.

A method that approximates unmasked attention accurately can still be invalid for a masked target if support is wrong.

## 23. Position changes what is being approximated

Suppose scores include a relative-position term:

\[
S_{ij}
=
\frac{q_i^\top k_j}{\sqrt{d_k}}
+
b_{ij}.
\]

Then b is part of the target.

A feature map derived only for the content exponential kernel does not automatically approximate the combined positional operator.

The same warning applies to rotary structure, head-specific biases, and other positional mechanisms.

The later positional chapters can inherit the approximation vocabulary developed here.

They must restate which structure is inside the target.

## 24. Finite precision is not an afterthought

Approximation changes numerical pathways.

Random-feature exponentials can overflow or underflow.

Reduced landmark systems can be ill-conditioned.

Low-rank factorizations can amplify errors through poorly scaled factors.

Sparse transformations can change gradient behavior near support transitions.

These are not reasons to reject the methods.

They are reasons to include finite precision in the contract.

The correct question is:

> what numerical operation is actually performed, and which quantity remains stable under its implementation?

## 25. A useful comparison table in words

The four representative routes can now be summarized without collapsing them.

**Performer/FAVOR+.**  
Target: exponential softmax kernel and normalized attention action.  
Structure: positive orthogonal random features.  
Budget: feature count.  
Characteristic risk: finite-feature variance and normalization error.

**Linformer.**  
Target: compressed attention action through sequence projection.  
Structure: low-dimensional learned projection.  
Budget: projection/rank width.  
Characteristic risk: low-rank premise failing on relevant states.

**Nyströmformer.**  
Target: normalized self-attention matrix/action.  
Structure: landmarks and reduced reconstruction.  
Budget: landmark count.  
Characteristic risk: landmark adequacy and reduced-system conditioning.

**Alpha-entmax.**  
Target: a different score-to-simplex operator.  
Structure: exact sparse support for alpha greater than one.  
Budget: not naturally an approximation rank; alpha controls geometry/sparsity.  
Characteristic risk: calling a changed operator a softmax approximation when it is not intended to be one.

## 26. The Krylov analogy, used carefully

The Krylov chapter taught a productive lesson:

large operator problems can sometimes be attacked through informative low-dimensional directions.

That lesson transfers.

The convergence theorems do not.

A Krylov subspace is generated by

\[
r_0,Ar_0,A^2r_0,\ldots
\]

for a declared operator.

Random features are sampled feature directions.

Linformer projections are learned sequence reductions.

Nyström landmarks are selected representatives.

These are all reduced representations.

They are not the same reduced representation.

The safe inheritance is methodological:

- define the target;
- define the reduced object;
- define the residual or error;
- expose conditioning;
- expose the budget;
- test convergence or approximation rather than assuming it.

## 27. What not to infer

This chapter rejects several tempting shortcuts.

### Small kernel error does not automatically give small operator error

Normalization can amplify errors if denominator control is weak.

### Small output error on one value field does not give small operator error

The value field may fail to excite discrepant directions.

### Low rank does not imply sparsity

Dense rank-one matrices exist.

### Sparsity does not imply low rank

The identity matrix is sparse and full rank.

### Exact zeros do not imply fast execution

Dense score formation may already have occurred.

### Few random features do not imply uniform accuracy

Finite approximation quality is a statistical question.

### Good benchmark performance does not imply softmax fidelity

Retraining can change the system.

These are not edge cases.

They are the basic claim boundaries.

## 28. A practical evaluation protocol

For a fixed trained head or controlled synthetic case:

1. freeze Q, keys, V, mask, and position;
2. compute exact dense softmax A and Y when feasible;
3. choose one approximation family;
4. state its budget m or k;
5. compute its own target objects;
6. measure operator error to A if softmax fidelity is intended;
7. measure output error on V;
8. record row sums, positivity, support violations, and rank/sparsity;
9. record memory and runtime;
10. sweep the budget;
11. repeat over representative inputs;
12. separate approximation fidelity from retrained task performance.

This turns “efficient attention” from a label into an experiment.

## 29. Research bridges

Several later Atlas questions become sharper after this chapter.

### Spectral diagnostics

If A is approximated by \(\widehat A\), how do singular values, non-normality, mixing rates, or transient amplification change?

### Context compression

Can a low-rank or landmark structure be used deliberately as a context-compression operator rather than merely as a cheaper attention surrogate?

### Relative-position operators

Can positional structure be factored exactly or approximately without destroying support or equivariance?

### Systems

When does theoretical sparsity or low rank translate into actual accelerator speed?

### Adaptive approximation

Can feature count, landmark count, or rank be selected dynamically using an error indicator rather than fixed globally?

That last question connects directly to the Atlas treatment of adaptive error control.

The error indicator would need an explicit relation to the operator or output error being controlled.

## 30. What the computational witness establishes

The finite witness establishes exactly:

1. a positive row-stochastic rank-2 operator;
2. a positive row-stochastic rank-1 approximation;
3. exact Frobenius operator error \(4/27\) in squared norm;
4. exact spectral operator error \(2\sqrt3/9\);
5. exact output error \(2/27\) in squared Frobenius norm for a declared V;
6. the standard operator-to-output inequality;
7. a score row for which softmax is dense;
8. the alpha=2 entmax/sparsemax result \((1,0,0)\);
9. row-scaling invariance showing raw kernel error and operator error can completely decouple.

It does not establish trained-model superiority or a finite-feature Performer guarantee.

## 31. Closing view

Approximate attention is best understood as a map of design choices.

One route approximates a kernel.

One route compresses an operator.

One route reconstructs from landmarks.

One route changes the normalization geometry and creates exact sparsity.

The useful unifying picture is not:

\[
\text{all efficient attention is the same}.
\]

It is:

\[
\boxed{
\text{target}
+
\text{structure}
+
\text{budget}
+
\text{error notion}
+
\text{implementation}
}.
\]

That tuple tells us what was preserved and what was changed.

Without it, “linear,” “sparse,” “low-rank,” and “approximate” are only adjectives.

With it, they become mathematical claims.

## References used in this chapter

- [@ChoromanskiEtAl2021Performer]
- [@WangEtAl2020Linformer]
- [@XiongEtAl2021Nystromformer]
- [@PetersNiculaeMartins2019Entmax]

Exact source identities and claim boundaries are recorded in sources/source-locks/ATLAS-CH-ATTNAPPROX-001.yaml.
