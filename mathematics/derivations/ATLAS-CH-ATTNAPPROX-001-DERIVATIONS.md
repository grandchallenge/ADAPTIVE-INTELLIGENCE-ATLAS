# ATLAS-CH-ATTNAPPROX-001 — Derivation Packet

## Scope

This packet establishes the finite mathematical claims used by Approximate and Structured Attention.

It does not prove universal superiority of any efficient-attention architecture. It does not promote source-specific empirical results into general theorems. It does not identify random-feature, low-rank, landmark, and sparse mechanisms with one another.

The governing rule is:

> approximation claims are meaningful only after the target object and error notion are named.

## D1. The exact softmax objects

For fixed queries and keys, define

\[
S_{ij}
=
\frac{q_i^\top k_j}{\sqrt{d_k}},
\]

\[
K_{ij}=e^{S_{ij}},
\]

\[
z_i=\sum_j K_{ij},
\qquad
D=\operatorname{diag}(z_1,\ldots,z_n),
\]

and

\[
A=D^{-1}K.
\]

For a fixed value field V,

\[
Y=AV.
\]

The five objects

\[
S,\quad K,\quad A,\quad V,\quad Y
\]

have different semantics.

A method may approximate one without directly approximating another.

## D2. Row-shift / row-scale invariance

Let C be a positive diagonal matrix,

\[
C=\operatorname{diag}(c_1,\ldots,c_n),
\qquad
c_i>0.
\]

The row-sum diagonal of CK is

\[
D(CK)=CD(K).
\]

Therefore

\[
D(CK)^{-1}CK
=
(CD)^{-1}CK
=
D^{-1}C^{-1}CK
=
D^{-1}K
=
A.
\]

Thus positive row scaling of K leaves the normalized operator unchanged.

At score level, adding a row constant \(b_i\) gives

\[
e^{S_{ij}+b_i}
=
e^{b_i}e^{S_{ij}},
\]

which is exactly such a row scaling.

Therefore raw absolute kernel error is not an invariant measure of attention-operator error.

Indeed, for any \(c>0\),

\[
\widehat K=cK
\]

gives

\[
\widehat A=A,
\]

while

\[
\|\widehat K-K\|_F
=
|c-1|\,\|K\|_F
\]

can be made arbitrarily large.

## D3. A rowwise kernel-to-operator perturbation identity

Consider one positive kernel row

\[
k\in\mathbb R_{>0}^n,
\qquad
z=\mathbf 1^\top k.
\]

Let

\[
\widehat k=k+e,
\qquad
\widehat z=z+\delta,
\qquad
\delta=\mathbf 1^\top e,
\]

with \(\widehat z>0\).

Define

\[
a=\frac{k}{z},
\qquad
\widehat a=\frac{k+e}{\widehat z}.
\]

The bound uses a positive denominator only. Entrywise nonnegativity of \(\widehat k\) is an additional requirement before interpreting \(\widehat a\) as a probability row; otherwise its entries can have mixed signs despite summing to one.

Then

\[
\widehat a-a
=
\frac{e}{\widehat z}
-
\frac{k\delta}{z\widehat z}.
\]

Hence

\[
\|\widehat a-a\|_1
\le
\frac{\|e\|_1}{\widehat z}
+
\frac{\|k\|_1|\delta|}{z\widehat z}.
\]

Because \(\|k\|_1=z\),

\[
\|\widehat a-a\|_1
\le
\frac{\|e\|_1+|\delta|}{\widehat z}.
\]

Also

\[
|\delta|
\le
\|e\|_1.
\]

Therefore

\[
\boxed{
\|\widehat a-a\|_1
\le
\frac{2\|e\|_1}{\widehat z}
}.
\]

If, more specifically,

\[
\|e\|_1\le \rho z,
\qquad
0\le\rho<1,
\]

then

\[
\widehat z
\ge
z-\|e\|_1
\ge
(1-\rho)z,
\]

so

\[
\boxed{
\|\widehat a-a\|_1
\le
\frac{2\rho}{1-\rho}
}.
\]

This is a deliberately simple sufficient bound.

Its role is conceptual: kernel accuracy needs denominator control before it becomes normalized-attention accuracy.

## D4. Operator error controls output error for fixed values

Let

\[
E=A-\widehat A.
\]

Then

\[
Y-\widehat Y
=
EV.
\]

Using the spectral/Frobenius submultiplicative inequality,

\[
\|EV\|_F
\le
\|E\|_2\|V\|_F.
\]

Therefore

\[
\boxed{
\|AV-\widehat A V\|_F
\le
\|A-\widehat A\|_2\|V\|_F
}.
\]

The converse does not hold from one V.

If V lies partly or wholly in a subspace annihilated by E, output error can be small or zero while operator error is nonzero.

## D5. Exact rank-2 attention operator

Define

\[
A=
\begin{pmatrix}
1/2&1/3&1/6\\
1/2&1/3&1/6\\
1/6&1/3&1/2
\end{pmatrix}.
\]

Every row sums to one and every entry is positive.

The first two rows are equal, so

\[
\operatorname{rank}(A)\le 2.
\]

The first and third rows are not scalar multiples, so

\[
\operatorname{rank}(A)=2.
\]

Because A is strictly positive and row-stochastic, it can be written as a row-softmax matrix by choosing a score row

\[
S_{i,:}=\log A_{i,:}
\]

up to arbitrary row constants.

Thus the witness is a legitimate normalized attention operator, independent of whether a particular low-dimensional query-key factorization is imposed.

## D6. Rank-1 row-average approximation

Average the three rows of A:

\[
\bar a
=
\left(
\frac{7}{18},
\frac13,
\frac{5}{18}
\right).
\]

Define

\[
\widehat A
=
\mathbf 1\bar a^\top
=
\begin{pmatrix}
7/18&1/3&5/18\\
7/18&1/3&5/18\\
7/18&1/3&5/18
\end{pmatrix}.
\]

Then

\[
\operatorname{rank}(\widehat A)=1,
\]

and \(\widehat A\) is also row-stochastic and strictly positive.

The difference is

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

This factors as

\[
A-\widehat A
=
\frac19
\begin{pmatrix}
1\\
1\\
-2
\end{pmatrix}
\begin{pmatrix}
1&0&-1
\end{pmatrix}.
\]

Hence it has rank one.

## D7. Exact Frobenius operator error

The squared Frobenius norm is

\[
\|A-\widehat A\|_F^2
=
\frac1{81}
\left(
1+1+1+1+4+4
\right)
=
\frac{12}{81}
=
\boxed{\frac4{27}}.
\]

## D8. Exact spectral operator error

For a rank-one matrix \(uv^\top\),

\[
\|uv^\top\|_2
=
\|u\|_2\|v\|_2.
\]

Here

\[
u=(1,1,-2)^\top,
\qquad
v=(1,0,-1)^\top.
\]

Thus

\[
\|u\|_2=\sqrt6,
\qquad
\|v\|_2=\sqrt2.
\]

Therefore

\[
\|A-\widehat A\|_2
=
\frac{\sqrt{12}}9
=
\boxed{\frac{2\sqrt3}{9}}.
\]

## D9. Exact output error

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
AV
=
\begin{pmatrix}
2/3&1/6\\
2/3&1/6\\
2/3&-1/6
\end{pmatrix}.
\]

Also

\[
\widehat A V
=
\begin{pmatrix}
2/3&1/18\\
2/3&1/18\\
2/3&1/18
\end{pmatrix}.
\]

Hence

\[
(A-\widehat A)V
=
\begin{pmatrix}
0&1/9\\
0&1/9\\
0&-2/9
\end{pmatrix},
\]

up to the sign convention \(A-\widehat A\) versus \(\widehat A-A\).

Therefore

\[
\|(A-\widehat A)V\|_F^2
=
\frac1{81}
(1+1+4)
=
\boxed{\frac2{27}}.
\]

## D10. Verify the operator-to-output bound

The value-field Frobenius norm satisfies

\[
\|V\|_F^2
=
1+1+1+1
=
4,
\]

so

\[
\|V\|_F=2.
\]

The general bound gives

\[
\|(A-\widehat A)V\|_F
\le
\frac{2\sqrt3}{9}\cdot 2
=
\frac{4\sqrt3}{9}.
\]

The actual output error is

\[
\sqrt{\frac2{27}}
=
\frac{\sqrt6}{9}.
\]

Since

\[
\sqrt6\le 4\sqrt3,
\]

the bound holds.

The inequality is not tight in this witness.

That is expected: an operator norm bounds the worst amplification over compatible inputs, while this V is only one value field.

## D11. Positive random-feature identity for the exponential kernel

Let

\[
\omega\sim N(0,I_d).
\]

Define

\[
\phi_\omega(x)
=
\exp\left(
\omega^\top x-\frac12\|x\|_2^2
\right).
\]

Then

\[
\phi_\omega(q)\phi_\omega(k)
=
\exp\left(
\omega^\top(q+k)
-\frac12\|q\|_2^2
-\frac12\|k\|_2^2
\right).
\]

For a standard Gaussian vector and any t,

\[
\mathbb E e^{\omega^\top t}
=
e^{\|t\|_2^2/2}.
\]

Taking \(t=q+k\),

\[
\mathbb E[
\phi_\omega(q)\phi_\omega(k)
]
=
\exp\left(
\frac12\|q+k\|_2^2
-\frac12\|q\|_2^2
-\frac12\|k\|_2^2
\right).
\]

Use

\[
\|q+k\|_2^2
=
\|q\|_2^2
+
2q^\top k
+
\|k\|_2^2.
\]

Then

\[
\boxed{
\mathbb E[
\phi_\omega(q)\phi_\omega(k)
]
=
e^{q^\top k}
}.
\]

This is the positive random-feature identity underlying the relevant softmax-kernel approximation idea.

The Performer/FAVOR+ construction adds source-specific structure, including positive orthogonal random features and associated variance/concentration analysis.

## D12. Finite-feature estimator

For samples or structured random features \(\omega_1,\ldots,\omega_m\), define

\[
\widehat K_m(q,k)
=
\frac1m
\sum_{r=1}^m
\phi_{\omega_r}(q)
\phi_{\omega_r}(k).
\]

With independent standard-Gaussian samples,

\[
\mathbb E[\widehat K_m(q,k)]
=
e^{q^\top k}.
\]

Unbiasedness is an expectation statement.

It does not imply that one finite draw has small error.

A finite implementation also has:

- variance;
- concentration behavior;
- overflow/underflow risk;
- normalization error;
- feature-generation cost;
- finite-precision accumulation error.

## D13. Reassociation for feature attention

Let

\[
\Phi_Q\in\mathbb R^{n\times m},
\qquad
\Phi_K\in\mathbb R^{n\times m}
\]

contain feature rows.

The approximate unnormalized kernel is

\[
\widehat K
=
\Phi_Q\Phi_K^\top.
\]

The numerator action can be evaluated as

\[
\widehat K V
=
\Phi_Q(\Phi_K^\top V)
\]

without materializing the full \(n\times n\) matrix.

The approximate denominator is

\[
\widehat K\mathbf 1
=
\Phi_Q(\Phi_K^\top\mathbf 1).
\]

Therefore normalized feature attention is a ratio:

\[
\widehat Y_i
=
\frac{
\phi(q_i)^\top
\left(
\sum_j \phi(k_j)v_j^\top
\right)
}{
\phi(q_i)^\top
\left(
\sum_j \phi(k_j)
\right)
}.
\]

The denominator is part of the approximation.

Approximating only the numerator is not enough.

## D14. Low-rank structure is a different approximation route

A low-rank mechanism replaces a large matrix action with a factorization or projection through a reduced dimension r.

Abstractly,

\[
\widehat A
=
UV^\top,
\qquad
U,V\in\mathbb R^{n\times r},
\]

or a method may project keys/values before constructing the final action.

This differs from random features in two ways:

1. the reduced basis need not be a random-feature approximation to \(e^{q^\top k}\);
2. the approximation target may be the normalized attention action or projected sequence representation rather than the unnormalized kernel entries.

Therefore “rank r” and “m random features” are not interchangeable accuracy parameters.

## D15. Nyström / landmark structure

A landmark method selects a reduced set of representative rows/columns or landmark states and reconstructs a larger matrix from reduced blocks.

At schematic level, a Nyström approximation has the form

\[
\widehat A
=
C W^\dagger R,
\]

where C and R are cross-blocks and W is a landmark block.

The exact Nyströmformer construction is source-specific and adapted to softmax attention.

For Atlas purposes, the durable distinction is:

- landmark count controls reduced matrix size;
- reconstruction accuracy depends on landmark quality and matrix structure;
- inverse/pseudoinverse-like reduced operations introduce conditioning and finite-precision considerations;
- this is not the same estimator as random-feature Monte Carlo.

## D16. Sparsemax as the alpha=2 entmax member

Take score row

\[
s=(2,0,-1).
\]

Softmax gives

\[
p_i
=
\frac{e^{s_i}}{e^2+1+e^{-1}}.
\]

Every entry is strictly positive.

For alpha=2, entmax reduces to sparsemax.

Sparsemax is Euclidean projection of s onto the probability simplex:

\[
\operatorname{sparsemax}(s)
=
\arg\min_{p\in\Delta^2}
\|p-s\|_2^2.
\]

The simplex projection has threshold form

\[
p_i=\max(s_i-\tau,0),
\]

with \(\tau\) chosen so the entries sum to one.

Choose

\[
\tau=1.
\]

Then

\[
\max(s-\tau,0)
=
(1,0,0),
\]

which sums to one.

Hence

\[
\boxed{
\operatorname{sparsemax}(2,0,-1)
=
(1,0,0)
}.
\]

This exact support change is not a failed softmax approximation.

It is the intended behavior of a different normalization family.

## D17. Sparsity does not imply low rank

The identity matrix \(I_n\) is maximally sparse by row support size one but has rank n.

Therefore

\[
\text{sparse}
\not\Rightarrow
\text{low rank}.
\]

Conversely, the dense rank-one matrix

\[
\frac1n\mathbf 1\mathbf 1^\top
\]

has no zero entries.

Therefore

\[
\text{low rank}
\not\Rightarrow
\text{sparse}.
\]

These structures may coexist, but neither implies the other.

## D18. Exact zeros do not imply cheap score formation

Suppose an attention mechanism first forms all pairwise scores

\[
S=QK^\top.
\]

That dense multiplication already has quadratic dependence on sequence length n for fixed head width, before any normalization creates zeros.

Therefore a sparse normalized matrix can still arise after quadratic work.

Computational savings require either:

- avoiding many score evaluations;
- exploiting structured support during score generation;
- compressed/low-rank factorization;
- feature reassociation;
- hardware-aware sparse kernels;
- another explicit mechanism.

Support sparsity is a structural property, not by itself an end-to-end complexity theorem.

## D19. Complexity with explicit approximation parameters

Let:

- n = sequence length;
- d = query/key width;
- d_v = value width;
- m = random-feature dimension or landmark count;
- r = low-rank projection width.

A feature-factorized attention numerator can be evaluated through

\[
\Phi_K^\top V
\]

followed by multiplication by \(\Phi_Q\).

Ignoring feature-generation details, this has a leading term proportional to

\[
O(nmd_v).
\]

The denominator has comparable \(O(nm)\) structure.

Thus “linear in n” means m and d_v are treated as fixed with respect to n.

A low-rank projection similarly exposes r as a cost/accuracy parameter.

A landmark method exposes m.

If m or r must grow with n to maintain an accuracy target, the effective scaling changes.

## D20. Masking and support

For an exact mask M, some interactions are forbidden.

A valid approximation must declare whether it:

- preserves masked zeros exactly;
- approximates only within allowed support;
- changes support;
- uses causal/prefix structure to obtain a specialized recurrence.

An unmasked approximation theorem cannot silently be applied to a masked operator without checking the construction.

## D21. Position is part of the operator family

If positional terms alter scores,

\[
S_{ij}
=
\frac{q_i^\top k_j}{\sqrt{d_k}}
+
b_{ij},
\]

then the target operator already contains positional structure.

Approximating only the content kernel while omitting or altering \(b_{ij}\) changes the target.

The approximation contract must therefore name positional assumptions.

## D22. Output fidelity is task-conditional

Two approximate operators may have similar matrix error but different output error for a given V.

Likewise, two operators with different matrix error may produce similar task loss after retraining.

Therefore three questions remain separate:

1. Does \(\widehat A\) approximate A?
2. Does \(\widehat A V\) approximate AV?
3. Does a model using the mechanism retain or improve task performance after training?

The third is empirical system evidence.

It does not retroactively prove the first.

## D23. Relation to Krylov language

Both Krylov methods and structured attention may exploit reduced-dimensional action.

But the generating mechanisms differ.

A Krylov space

\[
\mathcal K_m(A,r_0)
=
\operatorname{span}
\{r_0,Ar_0,\ldots,A^{m-1}r_0\}
\]

is operator-generated by repeated powers of a declared A.

A random-feature space is generated by feature samples.

A Linformer-like space is learned/projected.

A Nyström space is landmark-driven.

Therefore the useful inheritance is vocabulary:

- reduced representation;
- projection;
- residual/error distinction;
- conditioning;
- budget.

The chapter does not inherit Krylov convergence guarantees.

## D24. Durable propositions

1. Approximation of S, K, A, and Y are different claims.
2. Positive row scaling of K leaves A unchanged.
3. Raw kernel error can be arbitrarily large while operator error is zero.
4. Kernel perturbation becomes normalized-operator perturbation only with denominator control.
5. Operator error controls fixed-value output error through a standard induced-norm bound.
6. Small output error on one V does not certify small operator error.
7. The exponential dot-product kernel has a positive Gaussian random-feature expectation identity.
8. Finite-feature unbiasedness does not imply small realized normalized-attention error.
9. Low-rank, landmark, random-feature, and sparse mechanisms encode different structures.
10. Alpha-entmax is an alternative score-to-simplex family; alpha=2 can produce exact zeros where softmax remains dense.
11. Sparsity does not imply low rank, and low rank does not imply sparsity.
12. Exact sparsity does not prove subquadratic end-to-end computation.
13. Complexity claims must expose feature/rank/landmark/support budgets.
14. Masking and positional structure belong to the declared target operator.
15. Classical Krylov convergence does not transfer to learned structured attention by analogy.
