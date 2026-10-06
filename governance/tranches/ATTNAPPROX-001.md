# ATTNAPPROX-001 — Transaction Receipt

## Identity

- chapter: ATLAS-CH-ATTNAPPROX-001
- title: Approximate and Structured Attention
- implementation issue: #223
- branch: work/attnapprox-223
- protected baseline: 01e72c6c33a411d83f10913d7e8db0dd5305dfbd
- controller branch: state/atlas-controller

## Hard prerequisite bindings

### ATTNOP-001

- manuscript: d6fa97fbbd1a2410055ca2cd4bc034ca54ccd26c
- source lock: 4af4e53230776daaf0be825cffd1263957ed97c8
- AUDIT-002: 4671995f0cd7465a5df2bb60431244f482e5e3c9

### KRYLOV-001

- manuscript: 59e169723ca068bef817e7bc9e28727d03b45f6a
- source lock: adbe97c750ed79d09462a5e867e5beb772ad72e2
- AUDIT-039: 03660b0dbd1d0604e943d0d09c7b52c6605b256c

## Implementation artifact blobs

- specification: 38ae190a4d303d5bfdbfc9726777f8942f4fb519
- derivation packet: c84aa9479debc0d8f014c8edde2e914f5941376a
- computational witness: 0952f80e270c77753bbfe92573ae821a220017f3
- reader manuscript: 25a040be85328d76e4b09eb3495fd9127082173d
- source lock: f9bc3fa255ba95785d86f43433b728109e93d16c
- Chapter Ledger: e236a12fb5979d8db2a16ea9f6218a6a4f5f2fb8
- Source Register: 033a20f617449c0c939191c6a2f08185df650187
- bibliography: f3cfe2393979d88a6c6262f656ee7e1cd61d0665

## Durable mathematical substrate

The tranche establishes:

1. an explicit separation among score, exponential-kernel, normalized-operator, value-output, and alternative-normalization targets;
2. a rule that approximation claims name both target and error metric;
3. exact row-scale invariance of normalized softmax attention;
4. a bounded rowwise kernel-to-operator perturbation inequality requiring denominator control;
5. the fixed-value operator-to-output bound;
6. the positive Gaussian random-feature expectation identity for the exponential dot-product kernel;
7. a disciplined separation among FAVOR+ random features, low-rank projection, Nyström/landmark reconstruction, and alpha-entmax sparse normalization;
8. explicit feature/rank/landmark/support budgets in complexity claims;
9. an exact rank-reduction witness with separately measured operator and output error;
10. an exact sparsemax witness showing a deliberate support change rather than a softmax-estimation failure;
11. explicit mask, position, conditioning, and finite-precision boundaries;
12. a safe Krylov inheritance limited to reduced-representation/projection vocabulary, not convergence guarantees.

## Exact rank-reduction witness

\[
A=
\begin{pmatrix}
1/2&1/3&1/6\\
1/2&1/3&1/6\\
1/6&1/3&1/2
\end{pmatrix},
\qquad
\widehat A=
\begin{pmatrix}
7/18&1/3&5/18\\
7/18&1/3&5/18\\
7/18&1/3&5/18
\end{pmatrix}.
\]

Then:

- rank(A)=2;
- rank(Ahat)=1;
- both are positive and row-stochastic;
- ||A-Ahat||_F^2 = 4/27;
- ||A-Ahat||_2 = 2 sqrt(3) / 9.

For

\[
V=
\begin{pmatrix}
1&0\\
0&1\\
1&-1
\end{pmatrix},
\]

the exact squared output error is

\[
||(A-Ahat)V||_F^2=2/27.
\]

## Exact normalization witness

For any positive diagonal C,

\[
D(CG)^{-1}CG=D(G)^{-1}G.
\]

Thus positive row scaling can make raw kernel norm error arbitrarily large while normalized-operator error remains exactly zero.

## Exact sparse-alternative witness

For score row

\[
s=(2,0,-1),
\]

softmax has three strictly positive entries, while alpha=2 entmax (sparsemax) gives

\[
(1,0,0).
\]

The support change is a property of a different normalization family, not an approximation defect.

## Source scope

- Choromanski et al.: Performer/FAVOR+ positive orthogonal random features for softmax-kernel attention.
- Wang et al.: Linformer low-dimensional sequence projection / low-rank attention approximation.
- Xiong et al.: Nyströmformer landmark-based approximation of self-attention.
- Peters, Niculae, and Martins: alpha-entmax sparse score-to-simplex normalization.

Source-specific empirical or concentration claims are not universalized beyond their stated assumptions.

## Claim boundaries

This transaction does not establish that:

- small raw kernel error alone guarantees small normalized-operator error;
- small output error for one value field certifies small operator error;
- a low-rank attention approximation is universally accurate;
- exact sparsity implies low rank or cheap execution;
- low rank implies sparsity;
- a finite random-feature budget is uniformly accurate for arbitrary states;
- good retrained task performance proves softmax fidelity;
- classical Krylov convergence theorems apply to structured or learned attention;
- one efficient-attention mechanism is uniformly superior to the others.

## Validation state

Implementation remains unmerged until:

1. exact branch-head canonical Linux validation is green;
2. exact witness replay is green;
3. GitHub Actions validation is green on the exact PR head;
4. the implementation is merged into protected main;
5. a fresh post-draft audit is completed and merged.
