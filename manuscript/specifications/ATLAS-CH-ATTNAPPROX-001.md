# Chapter Specification — ATLAS-CH-ATTNAPPROX-001

## Identity

**Title:** Approximate and Structured Attention  
**Part:** Attention, Sequence, and Position  
**Status target:** draft-v0.1  
**Implementation issue:** #223  
**Protected baseline:** 01e72c6c33a411d83f10913d7e8db0dd5305dfbd

## Hard prerequisites

- ATLAS-CH-ATTNOP-001 / AUDIT-002;
- ATLAS-CH-KRYLOV-001 / AUDIT-039.

Exact prerequisite identities are frozen in sources/source-locks/ATLAS-CH-ATTNAPPROX-001.yaml.

The chapter may inherit from ATTNOP:

- the distinction among score matrix S, exponential kernel K, normalized mixing operator A, value field V, and full state-dependent map X -> A(X)V(X);
- row-wise softmax normalization;
- masking and positional structure as part of the admissible operator family;
- kernel-feature reassociation for linear attention.

The chapter may inherit from KRYLOV:

- reduced-representation and projection language;
- the distinction between residual-like quantities and true target error;
- the warning that low-dimensional structure alone does not imply fast or accurate approximation.

It may not inherit a theorem that a random-feature, low-rank, landmark, sparse, or learned attention approximation is accurate merely because it is lower dimensional.

## Governing question

When an attention mechanism is made cheaper, what exactly has been changed, what object is being approximated, and what error is controlled?

The chapter must answer this before comparing asymptotic complexity or downstream task quality.

## Mandatory object separation

For one head with fixed queries, keys, and values, define

\[
S_{ij}=\frac{q_i^\top k_j}{\sqrt{d_k}},
\qquad
K_{ij}=e^{S_{ij}},
\]

\[
D=\operatorname{diag}(K\mathbf 1),
\qquad
A=D^{-1}K,
\qquad
Y=AV.
\]

The chapter must keep distinct:

1. score approximation: \(\widehat S\approx S\);
2. kernel approximation: \(\widehat K\approx K\);
3. normalized-operator approximation: \(\widehat A\approx A\);
4. output approximation: \(\widehat Y\approx Y\);
5. alternative normalization/operator: \(\widetilde A\) intentionally defined by a different map, such as entmax.

The full attention map remains state-dependent because Q, K, and V depend on X.

## Error contract

No sentence of the form “method M approximates attention well” is admissible without naming the target and metric.

Preferred finite-dimensional diagnostics:

### Kernel error

\[
E_K=\|\widehat K-K\|_F.
\]

A relative form may be reported when \(\|K\|_F>0\).

Raw kernel error is not equivalent to attention-operator error because positive row rescaling of K leaves A unchanged.

### Operator error

\[
E_A^{(F)}=\|\widehat A-A\|_F,
\qquad
E_A^{(2)}=\|\widehat A-A\|_2.
\]

Also report structural defects when relevant:

- row-sum defect;
- negativity;
- support/mask violation;
- rank;
- exact sparsity.

### Output error

\[
E_Y=\|\widehat A V-AV\|_F.
\]

For fixed V,

\[
E_Y\le
\|\widehat A-A\|_2\|V\|_F.
\]

Small output error for one V is not sufficient evidence of small operator error.

## Mechanisms to compare

### FAVOR+ / positive random features

Use Choromanski et al. as the primary source.

Required account:

- exponential dot-product kernel representation;
- positive random features;
- orthogonalization as a variance-control structure;
- reassociation of feature factors;
- feature dimension as an explicit accuracy/cost parameter;
- normalization denominator as part of the approximation.

Do not generalize FAVOR+ guarantees to arbitrary learned feature maps.

### Low-rank learned projection

Use Linformer as a representative source.

Required account:

- projection of sequence-length structure to a smaller dimension;
- low-rank hypothesis as a model/empirical premise, not a universal theorem;
- distinction between approximating an attention matrix and approximating the exponential kernel entrywise;
- rank budget as an explicit approximation parameter.

### Landmark / Nyström structure

Use Nyströmformer as a representative source.

Required account:

- landmark selection;
- reduced matrix reconstruction;
- approximation of the normalized attention matrix;
- landmark count as an explicit cost/accuracy parameter;
- numerical stability of any inverse/pseudoinverse-like reduced object as a declared implementation issue.

### Sparse alternatives

Use Peters, Niculae, and Martins for alpha-entmax.

Required account:

- alpha-entmax is a score-to-simplex family;
- alpha=1 corresponds to softmax in the limiting formulation;
- alpha=2 gives sparsemax;
- alpha>1 may produce exact zeros;
- this changes the operator family rather than estimating softmax unless an explicit softmax-distance objective is imposed.

Exact sparsity of A does not prove subquadratic end-to-end attention if dense scores were already materialized.

## Random-feature derivation requirement

For \(\omega\sim N(0,I)\), define

\[
\phi_\omega(x)
=
\exp\left(
\omega^\top x-\frac12\|x\|_2^2
\right).
\]

The chapter must derive

\[
\mathbb E_\omega[
\phi_\omega(q)\phi_\omega(k)
]
=
e^{q^\top k}.
\]

This establishes an unbiased positive random-feature identity for the exponential dot-product kernel.

The Atlas must then distinguish this expectation identity from:

- finite-feature variance;
- orthogonal-feature improvements;
- normalized operator error;
- finite-precision stability;
- trained-model task performance.

## Exact finite witness requirement

Use the row-stochastic rank-2 operator

\[
A=
\begin{pmatrix}
1/2&1/3&1/6\\
1/2&1/3&1/6\\
1/6&1/3&1/2
\end{pmatrix}
\]

and value field

\[
V=
\begin{pmatrix}
1&0\\
0&1\\
1&-1
\end{pmatrix}.
\]

Use the rank-1 row-average approximation

\[
\widehat A=
\begin{pmatrix}
7/18&1/3&5/18\\
7/18&1/3&5/18\\
7/18&1/3&5/18
\end{pmatrix}.
\]

The witness must verify exactly:

\[
\|A-\widehat A\|_F^2=\frac{4}{27},
\]

\[
\|A-\widehat A\|_2=\frac{2\sqrt3}{9},
\]

and

\[
\|(A-\widehat A)V\|_F^2=\frac{2}{27}.
\]

It must also verify the operator-to-output bound.

## Sparse-alternative witness requirement

For score row

\[
s=(2,0,-1),
\]

softmax has three strictly positive entries.

The alpha=2 entmax member equals sparsemax, the Euclidean projection onto the simplex. It gives

\[
\operatorname{sparsemax}(s)=(1,0,0).
\]

The chapter must use this only to show:

- an alternative normalization can change support exactly;
- sparsity is not the same object as softmax approximation;
- the support change can be intentional rather than an approximation defect.

## Row-scaling invariance requirement

For any positive diagonal C,

\[
D(CK)^{-1}CK=D(K)^{-1}K.
\]

The chapter must explain that softmax is invariant to adding a constant to each score row, equivalently to positive row scaling of K.

Therefore raw absolute kernel error can be large while normalized-operator error is zero.

## Complexity discipline

Complexity statements must expose the approximation parameter.

Examples:

- random features: feature count m;
- Linformer-like projection: rank/projection width k;
- Nyström: landmark count m;
- sparse support: support size only yields computational benefit when the algorithm avoids or exploits dense work.

Claims of “linear attention” must state what is held fixed as n grows.

## Required chapter structure

1. The word approximation needs an object.
2. Score, kernel, operator, output.
3. Row scaling and why kernel error is not operator error.
4. Positive random features and FAVOR+.
5. Low-rank projection.
6. Landmark/Nyström reconstruction.
7. Sparse alternatives and entmax.
8. Three error surfaces.
9. Exact rank-reduction witness.
10. Exact sparse-support witness.
11. Complexity versus accuracy.
12. Masking, position, and support.
13. Failure modes and non-implications.
14. Research bridges.

## Required non-implications

The manuscript must explicitly reject:

\[
\text{small kernel error}
\not\Rightarrow
\text{small normalized-operator error}
\]

without denominator/normalization control;

\[
\text{small output error on one }V
\not\Rightarrow
\text{small operator error};
\]

\[
\text{low rank}
\not\Rightarrow
\text{sparsity};
\]

\[
\text{sparsity}
\not\Rightarrow
\text{low rank};
\]

\[
\text{exact zeros}
\not\Rightarrow
\text{subquadratic implementation};
\]

\[
\text{few random features}
\not\Rightarrow
\text{uniformly accurate attention};
\]

\[
\text{good task accuracy}
\not\Rightarrow
\text{small softmax-operator error}.
\]

## Downstream handoff

The chapter should provide reusable notation for later work on:

- relative-position operators;
- spectral diagnostics;
- token/sequence compression;
- systems-level attention implementation;
- context compression;
- learned routing and memory.

No downstream chapter may inherit an accuracy theorem stronger than the target/metric actually established here.

## Sources

- [@ChoromanskiEtAl2021Performer]
- [@WangEtAl2020Linformer]
- [@XiongEtAl2021Nystromformer]
- [@PetersNiculaeMartins2019Entmax]

Source lock: sources/source-locks/ATLAS-CH-ATTNAPPROX-001.yaml
