# AUDIT-056 — Approximate and Structured Attention

## Disposition

**PASS — NO REPAIR**

ATLAS-CH-ATTNAPPROX-001 remains at draft-v0.1.

The audit found no mathematical, epistemic, source-scope, dependency, citation, provenance, or repository defect requiring repair.

No publication, theorem certification, empirical superiority claim, or release promotion is implied.

## Audited baseline

- implementation issue: #223
- implementation PR: #224
- exact green implementation head: 35844412e9189172fb8d7262c644ea34aecdee08
- implementation merge / audited protected baseline: 8c5ad59ccacb3991e1ec7646be057a72b8bec495
- audit issue: #225
- audit branch: audit/a225
- chapter: ATLAS-CH-ATTNAPPROX-001

Merged implementation artifact blobs:

- specification: 38ae190a4d303d5bfdbfc9726777f8942f4fb519
- derivation packet: c84aa9479debc0d8f014c8edde2e914f5941376a
- computational witness: 0952f80e270c77753bbfe92573ae821a220017f3
- reader manuscript: 25a040be85328d76e4b09eb3495fd9127082173d
- source lock: f9bc3fa255ba95785d86f43433b728109e93d16c
- Chapter Ledger: e236a12fb5979d8db2a16ea9f6218a6a4f5f2fb8
- Source Register: 033a20f617449c0c939191c6a2f08185df650187
- bibliography: f3cfe2393979d88a6c6262f656ee7e1cd61d0665
- transaction receipt: b07b5b7e649a75297dadf84e9206e83c09e0ed95

## 1. Hard prerequisite identity

PASS.

The source lock binds exactly to audited prerequisites on protected baseline 01e72c6c33a411d83f10913d7e8db0dd5305dfbd.

Attention as an Operator:

- manuscript: d6fa97fbbd1a2410055ca2cd4bc034ca54ccd26c
- source lock: 4af4e53230776daaf0be825cffd1263957ed97c8
- AUDIT-002: 4671995f0cd7465a5df2bb60431244f482e5e3c9

Krylov Subspaces and Iterative Solves:

- manuscript: 59e169723ca068bef817e7bc9e28727d03b45f6a
- source lock: adbe97c750ed79d09462a5e867e5beb772ad72e2
- AUDIT-039: 03660b0dbd1d0604e943d0d09c7b52c6605b256c

No downstream architecture-state chapter is used as hidden prerequisite authority.

## 2. External source identity and scope

PASS.

Primary/public source verification confirms:

- Choromanski et al., Rethinking Attention with Performers, ICLR 2021, introducing Performer and FAVOR+ as positive orthogonal random-feature approximation machinery for softmax attention kernels with linear-in-sequence-length computation under the declared approximation dimension and source assumptions.
- Wang et al., Linformer: Self-Attention with Linear Complexity, arXiv:2006.04768, presenting a low-rank self-attention approximation and reduced sequence projection route.
- Xiong et al., Nyströmformer: A Nyström-based Algorithm for Approximating Self-Attention, AAAI 2021, 35(16), 14138-14148, DOI 10.1609/aaai.v35i16.17664, using landmarks/Nyström structure to approximate standard self-attention.
- Peters, Niculae, and Martins, Sparse Sequence-to-Sequence Models, ACL 2019, 1504-1519, DOI 10.18653/v1/P19-1146, introducing the alpha-entmax family, including softmax and sparsemax as particular cases and exact sparsity for alpha>1.

The implementation does not universalize source-specific empirical results or finite-sample/concentration guarantees.

## 3. Target-object separation

PASS.

The chapter keeps distinct:

1. score matrix S;
2. exponential kernel G;
3. normalized mixing operator A;
4. value field V;
5. output Y=AV;
6. an intentionally different normalization/operator such as alpha-entmax.

The chapter does not treat these as interchangeable approximation targets.

This is consistent with the audited ATTNOP boundary.

## 4. Row-scale invariance

PASS.

For positive diagonal C and positive kernel G,

\[
D(CG)=CD(G).
\]

Hence

\[
D(CG)^{-1}CG
=
D(G)^{-1}G.
\]

Therefore rowwise positive kernel rescaling can change raw kernel norm arbitrarily while leaving the normalized attention operator exactly unchanged.

The score-space equivalent is rowwise additive-shift invariance of softmax.

The derivation is exact.

## 5. Kernel-to-operator perturbation bound

PASS.

For one row,

\[
a=g/z,
\qquad
\widehat a=(g+e)/\widehat z,
\qquad
\widehat z=z+\delta,
\qquad
\delta=\mathbf 1^\top e,
\]

the chapter derives

\[
\widehat a-a
=
e/\widehat z
-
g\delta/(z\widehat z).
\]

Using \(\|g\|_1=z\) for positive g and \(|\delta|\le\|e\|_1\),

\[
\|\widehat a-a\|_1
\le
2\|e\|_1/\widehat z.
\]

If

\[
\|e\|_1\le\rho z,
\qquad
0\le\rho<1,
\]

then

\[
\widehat z\ge(1-\rho)z
\]

and

\[
\|\widehat a-a\|_1
\le
2\rho/(1-\rho).
\]

The manuscript correctly presents this as a simple sufficient normalization-control bound rather than as the Performer theorem.

## 6. Operator-to-output bound

PASS.

For fixed V,

\[
Y-\widehat Y
=
(A-\widehat A)V.
\]

The standard induced-norm inequality gives

\[
\|(A-\widehat A)V\|_F
\le
\|A-\widehat A\|_2
\|V\|_F.
\]

The chapter correctly blocks the converse inference from one value field.

## 7. Exact rank-reduction witness

PASS.

For

\[
A=
\begin{pmatrix}
1/2&1/3&1/6\\
1/2&1/3&1/6\\
1/6&1/3&1/2
\end{pmatrix}
\]

and

\[
\widehat A=
\begin{pmatrix}
7/18&1/3&5/18\\
7/18&1/3&5/18\\
7/18&1/3&5/18
\end{pmatrix},
\]

both matrices are positive and row-stochastic.

A has rank 2.

Ahat has rank 1.

The difference factors exactly as

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

Thus the error has rank one.

## 8. Exact Frobenius and spectral errors

PASS.

Independent exact replay confirms

\[
\|A-\widehat A\|_F^2
=
4/27.
\]

From the rank-one factorization,

\[
\|A-\widehat A\|_2
=
\frac19
\sqrt6\sqrt2
=
\frac{2\sqrt3}{9}.
\]

The arithmetic is exact.

## 9. Exact value-output witness

PASS.

For

\[
V=
\begin{pmatrix}
1&0\\
0&1\\
1&-1
\end{pmatrix},
\]

independent exact replay confirms

\[
AV=
\begin{pmatrix}
2/3&1/6\\
2/3&1/6\\
2/3&-1/6
\end{pmatrix},
\]

\[
\widehat A V=
\begin{pmatrix}
2/3&1/18\\
2/3&1/18\\
2/3&1/18
\end{pmatrix},
\]

and

\[
\|(A-\widehat A)V\|_F^2
=
2/27.
\]

The chapter uses this to demonstrate that one output-error measurement is not the same object as operator error.

## 10. Positive random-feature identity

PASS.

For

\[
\phi_\omega(x)
=
\exp(
\omega^\top x-\|x\|_2^2/2
),
\qquad
\omega\sim N(0,I),
\]

the Gaussian moment-generating function gives

\[
\mathbb E[
\phi_\omega(q)\phi_\omega(k)
]
=
e^{q^\top k}.
\]

The scaled-dot-product adaptation using

\[
q'=q/d_k^{1/4},
\qquad
k'=k/d_k^{1/4}
\]

correctly yields

\[
q'^\top k'
=
q^\top k/\sqrt{d_k}.
\]

The chapter distinguishes this expectation identity from finite-feature variance, orthogonal-feature refinements, normalized-operator error, numerical stability, and trained-model performance.

## 11. Feature reassociation and denominator semantics

PASS.

With

\[
\widehat G=\Phi_Q\Phi_K^\top,
\]

the numerator can be evaluated as

\[
\Phi_Q(\Phi_K^\top V)
\]

and the denominator as

\[
\Phi_Q(\Phi_K^\top\mathbf 1).
\]

The chapter explicitly records that normalized feature attention is a ratio and that approximating only the numerator is insufficient.

## 12. Low-rank projection boundary

PASS.

Linformer is treated as a representative low-dimensional projection/low-rank route, not as a random-feature estimator.

The chapter states that the useful rank budget is a premise/approximation parameter rather than a universal property of all heads, layers, inputs, masks, or distributions.

No universal low-rank theorem is inferred.

## 13. Nyström/landmark boundary

PASS.

Nyströmformer is treated as a landmark/reconstruction route with an explicit landmark budget.

The generic

\[
C W^\dagger R
\]

notation is presented schematically; the manuscript explicitly states that the exact Nyströmformer construction is source-specific.

Conditioning and finite-precision issues around reduced inverse/pseudoinverse-like operations are retained as implementation concerns.

## 14. Alpha-entmax boundary

PASS.

The source scope correctly records that the alpha-entmax family contains softmax and sparsemax as particular cases and becomes sparse for alpha>1.

The chapter correctly classifies alpha-entmax as an alternative score-to-simplex mapping rather than as an unbiased or consistent estimator of softmax.

## 15. Exact sparsemax witness

PASS.

For

\[
s=(2,0,-1),
\]

softmax has three strictly positive coordinates.

For alpha=2, entmax equals sparsemax.

The simplex projection threshold

\[
\tau=1
\]

gives

\[
\max(s-\tau,0)
=
(1,0,0),
\]

which sums to one.

The witness is exact.

## 16. Sparsity versus low rank

PASS.

The chapter correctly uses:

- \(I_n\) as a sparse full-rank counterexample;
- \(n^{-1}\mathbf1\mathbf1^\top\) as a dense rank-one counterexample.

Therefore neither sparsity nor low rank implies the other.

## 17. Sparsity versus end-to-end complexity

PASS.

The chapter correctly notes that exact zeros in the normalized operator do not by themselves avoid dense score formation.

Computational savings require an explicit mechanism that avoids or exploits work at the score, factorization, support, or hardware level.

No asymptotic saving is inferred from sparsity alone.

## 18. Complexity discipline

PASS.

The chapter exposes approximation budgets:

- random-feature dimension m;
- projection/rank width k or r;
- landmark count m;
- support size only when computationally exploited.

It states that “linear in n” requires declaring what is held fixed and that effective scaling can change if approximation budgets grow with sequence length.

## 19. Mask and position boundary

PASS.

Masks are treated as support constraints on the target operator.

Positional score terms are treated as part of the target rather than optional decoration.

The chapter does not silently transfer an unmasked/content-only approximation guarantee to masked or position-modified attention.

## 20. Task-performance boundary

PASS.

The chapter separates:

1. kernel fidelity;
2. normalized-operator fidelity;
3. fixed-value output fidelity;
4. retrained system/task performance.

It explicitly rejects the inference that good benchmark performance proves small softmax-operator error.

## 21. Krylov inheritance

PASS.

The chapter inherits only reduced-representation/projection/error/conditioning/budget vocabulary from the audited KRYLOV chapter.

It explicitly distinguishes operator-generated Krylov spaces from random features, learned projections, and landmarks.

No classical Krylov convergence theorem is transferred to learned or structured attention.

## 22. Citation and bibliography integrity

PASS.

Reader-facing citation keys resolve for:

- ChoromanskiEtAl2021Performer;
- WangEtAl2020Linformer;
- XiongEtAl2021Nystromformer;
- PetersNiculaeMartins2019Entmax.

The source register points to the exact ATTNAPPROX source lock.

Bibliographic identities and source-lock identities are coherent.

## 23. Repository integrity

PASS subject to audit-PR validation.

At audited protected implementation main 8c5ad59ccacb3991e1ec7646be057a72b8bec495:

- chapter status: draft-v0.1;
- canonical specification/manuscript/derivation/source-lock/witness paths are populated in the Chapter Ledger;
- hard dependencies remain ATTNOP-001 and KRYLOV-001;
- no governed figure is introduced;
- canonical Linux repository validation is green;
- implementation exact head 35844412e9189172fb8d7262c644ea34aecdee08 passed GitHub Actions run 37461213741;
- protected implementation merge replay is green.

## Final disposition

AUDIT-056 passes with no repair.

The durable ATTNAPPROX layer is:

**declared attention target + declared approximation structure + explicit approximation budget + target-specific error metric + normalization/support/position semantics + implementation cost, with random-feature, low-rank, landmark, and sparse-normalization mechanisms kept mathematically distinct.**
