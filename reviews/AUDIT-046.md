# AUDIT-046 — Matrix-Aware Optimization

## Disposition

**PASS — NO REPAIR**

ATLAS-CH-MATRIXOPT-001 remains at \`draft-v0.1\`.

The audit found no mathematical, derivational, witness, source-scope, bibliography, dependency, or downstream-boundary defect requiring a repair commit.

This audit does not promote the chapter to publication-ready, certified, or final-copy status.

## Audited implementation

- implementation issue: #184
- implementation PR: #185
- exact implementation head: \`ae75df4c1b1016b873b48b3367bede2b01e507af\`
- implementation merge: \`bd9863891fb8edfb48f14414e7aceee50a798a54\`
- audit issue: #187
- audit branch: \`audit/matrixopt-187\`
- chapter: \`ATLAS-CH-MATRIXOPT-001\`

Implementation artifact identities at the audited merge:

- specification: \`7a47e966a946baaf14dd0f89b7bbca46f5e32002\`
- derivation packet: \`591d457fe4cef1dbb7798b482a08234f631fd882\`
- computational witness: \`f582684a2cc55c24f4d0f50cc7ec12dc2bd27b20\`
- manuscript: \`ac860c93b99ee33d8213bf05845b3670061fba53\`
- source lock: \`f4fb1797bc93a8f038ddb06e6d3139ab6367ffcb\`
- Chapter Ledger: \`1a01d9496b515b552d765818313034199f3c70cd\`
- Source Register: \`c695eb0fff9e09dbdeede0e53edf7e22d8c5aa9c\`
- tranche receipt: \`6736651dcb9e8de2598aa59fb5ada8fad6e2f505\`
- bibliography: \`39819371804118021eaf13ea55757375ba40ed2b\`

## 1. Hard prerequisites

PASS.

### Linear Algebra

Exact protected binds:

- manuscript: \`e7fcf56322f26d232d3a3043038d9850792b4bde\`
- source lock: \`f24e93ee0c2496ca0b9d71f6f824b0d13dbdc08e\`
- Foundation audit AUDIT-004: \`948f76b3f86d27fa4830efc30d8ef0135134256e\`

All three identities match the audited implementation merge.

The inherited interface is correctly limited to finite-dimensional linear maps, SVD, singular values, matrix/operator norms, conditioning, low-rank structure, projections, and rectangular-matrix language.

### Curvature and Second-Order Structure

Exact protected binds:

- manuscript: \`10ee7db734df519e886e335301bf107d01d27f5c\`
- source lock: \`bc74588fd65df1a88a524b5241ca08ff498e0231\`
- post-draft audit AUDIT-041: \`32d55baa0f8c3d5967f704c699fed81772ae2fd8\`

All three identities match the audited implementation merge.

The inherited interface is correctly limited to preconditioning/metric language, exact-versus-approximate curvature distinctions, and optimizer-state discipline.

No full-Hessian equivalence is imported without proof.

## 2. External source identity and scope

PASS.

### Shampoo

Gupta, Koren, and Singer, *Shampoo: Preconditioned Stochastic Tensor Optimization*, PMLR 80, 1842–1850, ICML 2018.

Canonical source:

\`https://proceedings.mlr.press/v80/gupta18a.html\`

Independent source recheck confirms:

- Shampoo is presented as structure-aware tensor preconditioning;
- it maintains a preconditioning matrix for each tensor dimension;
- the paper's formal convergence guarantee is in the stochastic convex setting;
- deep-learning speed/convergence statements are empirical results of the paper.

The Atlas chapter preserves those boundaries.

It does not promote Shampoo to an exact full-Hessian method or universal deep-network convergence theorem.

### Polar decomposition

Nicholas J. Higham, *Computing the Polar Decomposition—with Applications*, SIAM Journal on Scientific and Statistical Computing 7(4), 1160–1174, 1986, DOI \`10.1137/0907079\`.

Canonical DOI locator:

\`https://doi.org/10.1137/0907079\`

Independent source recheck confirms that the paper treats full-rank polar decomposition, a quadratically convergent Newton method for computing it, and best-approximation properties of the polar factor.

The Atlas uses the source only for classical polar-decomposition/numerical-analysis facts.

### Norm-dependent steepest descent

Jeremy Bernstein and Laker Newhouse, *Old Optimizer, New Norm: An Anthology*, arXiv:2409.20325.

Canonical source:

\`https://arxiv.org/abs/2409.20325\`

Independent source recheck confirms the paper's stated interpretation: after switching off moving averages, Adam-, Shampoo-, and Prodigy-like methods can be understood as first-order steepest descent under different norms.

The chapter uses this as a norm/steepest-direction interpretation, not a universal empirical-superiority theorem.

### Muon

Keller Jordan et al., *Muon: An optimizer for hidden layers in neural networks*, 2024 design note.

Canonical source:

\`https://kellerjordan.github.io/posts/muon/\`

Independent source recheck confirms:

- Muon targets 2D hidden-layer parameters;
- it applies Newton-Schulz post-processing to an SGD-momentum update;
- the stated purpose is approximate orthogonalization;
- the note identifies exact SVD replacement by \(UV^\top\) as the idealized orthogonalization object;
- the implementation uses a finite Newton-Schulz-style iteration.

The chapter correctly distinguishes this stateful finite numerical realization from an exact instantaneous polar factor.

## 3. Matrix Shampoo specialization

PASS.

The chapter states

\[
L_t=\sum_{s\le t}G_sG_s^\top,
\qquad
R_t=\sum_{s\le t}G_s^\top G_s,
\]

with representative damped update

\[
P_t
=
(L_t+\varepsilon I_m)^{-1/4}
G_t
(R_t+\varepsilon I_n)^{-1/4}.
\]

This is the correct order-two/two-mode Shampoo structure.

The manuscript explicitly describes \(L_t\) and \(R_t\) as accumulated gradient statistics and does not identify them with a full Hessian.

## 4. Rectangular rank obstruction

PASS.

For

\[
G\in\mathbb R^{m\times n},
\]

the standard identity

\[
\operatorname{rank}(GG^\top)=\operatorname{rank}(G)
\]

implies that, for a tall full-column-rank matrix with \(m>n\),

\[
\operatorname{rank}(GG^\top)=n<m.
\]

Therefore the one-step left Gram matrix is singular.

The chapter correctly treats damping, accumulation, pseudoinverse/support conventions, or another declared numerical rule as material rather than cosmetic.

## 5. Exact rectangular witness

PASS.

For

\[
G=
\begin{pmatrix}
2&0\\
0&1\\
1&0
\end{pmatrix},
\]

independent symbolic replay gives

\[
G^\top G
=
\begin{pmatrix}
5&0\\
0&1
\end{pmatrix},
\]

and

\[
GG^\top
=
\begin{pmatrix}
4&0&2\\
0&1&0\\
2&0&1
\end{pmatrix}.
\]

The singular values are exactly

\[
\{\sqrt5,1\}.
\]

Also,

\[
\operatorname{rank}(GG^\top)=2,
\qquad
\det(GG^\top)=0.
\]

The embedded pure-Python witness independently prints:

\`MATRIXOPT witness: PASS\`.

## 6. Polar factor and semi-orthogonality

PASS.

The declared reduced SVD is exact with

\[
U=
\begin{pmatrix}
2/\sqrt5&0\\
0&1\\
1/\sqrt5&0
\end{pmatrix},
\qquad
\Sigma=\operatorname{diag}(\sqrt5,1),
\qquad
V=I_2.
\]

Thus

\[
Q=UV^\top
=
\begin{pmatrix}
2/\sqrt5&0\\
0&1\\
1/\sqrt5&0
\end{pmatrix}.
\]

Independent replay confirms

\[
Q^\top Q=I_2,
\]

while

\[
QQ^\top
=
\begin{pmatrix}
4/5&0&2/5\\
0&1&0\\
2/5&0&1/5
\end{pmatrix}
\neq I_3.
\]

The chapter therefore uses the correct rectangular concept: column semi-orthogonality rather than square orthogonality.

## 7. Singular-value flattening

PASS.

Because

\[
G=U\Sigma V^\top
\]

and

\[
Q=UIV^\top,
\]

the polar factor replaces the nonzero singular values by \(1\) while preserving the singular subspaces.

The chapter correctly calls this singular-value flattening.

It does not equate flattening with arbitrary intentional spectral shaping or claim that flattening is universally optimal.

## 8. Norm-duality derivation

PASS.

For the Frobenius ball,

\[
\min_{\|\Delta\|_F\le\rho}
\langle G,\Delta\rangle_F
=
-\rho\|G\|_F
\]

is attained by

\[
\Delta_F^\star
=
-\rho G/\|G\|_F.
\]

For the spectral-norm ball, duality with the nuclear norm gives

\[
\min_{\|\Delta\|_2\le\rho}
\langle G,\Delta\rangle_F
=
-\rho\|G\|_*.
\]

The choice

\[
\Delta_2^\star=-\rho UV^\top
\]

is feasible and attains that value.

For the exact witness,

\[
\|G\|_2=\sqrt5,
\qquad
\|G\|_F=\sqrt6,
\qquad
\|G\|_*=\sqrt5+1.
\]

The manuscript explicitly warns that objective decreases under different norm balls are not direct optimizer-quality comparisons.

## 9. One-step Shampoo/polar support identity

PASS.

On the nonzero singular support,

\[
(GG^\top)^{-1/4}
G
(G^\top G)^{-1/4}
=
UV^\top.
\]

Independent symbolic replay of the \(3\times2\) witness confirms the identity exactly when the left inverse fourth root is interpreted on \(\operatorname{range}(GG^\top)\).

The chapter also records the crucial boundary:

- the full-space left inverse does not exist for the tall one-step witness;
- finite damping changes the exact singular-value map;
- accumulated state means stateful Shampoo is not identical to the instantaneous polar transform.

## 10. Diagonal-scaling control

PASS.

For

\[
D=\operatorname{diag}(1/2,1,1/2),
\]

the chapter gives

\[
DG=
\begin{pmatrix}
1&0\\
0&1\\
1/2&0
\end{pmatrix}.
\]

Independent replay confirms singular values

\[
\{\sqrt5/2,1\}.
\]

The example is explicitly labeled as a generic diagonal control, not as the exact rule of Adam or another named optimizer.

## 11. Muon exact-versus-approximate boundary

PASS.

The manuscript keeps separate:

- raw current gradient;
- momentum-like optimizer state;
- finite Newton-Schulz-style post-processing;
- exact SVD/polar orthogonalization.

It does not claim that a finite Newton-Schulz iteration is an exact polar decomposition.

It does not claim that Muon is an instantaneous gradient map without state.

## 12. Manifold boundary

PASS.

The chapter correctly distinguishes an orthogonalized update direction from an orthogonality-constrained parameter.

From

\[
Q_t^\top Q_t=I
\]

and

\[
W_{t+1}=W_t-\eta Q_t
\]

it does not infer

\[
W_{t+1}^\top W_{t+1}=I.
\]

This preserves the boundary with ATLAS-CH-MANOPT-001.

## 13. Downstream SPECTRALSHAPE boundary

PASS.

ATLAS-CH-SPECTRALSHAPE-001 may inherit:

- SVD/polar language;
- rectangular semi-orthogonality;
- norm-dependent steepest-direction language;
- exact-versus-approximate singular-value transformations;
- the distinction between flattening and conditioning.

MATRIXOPT does not pre-claim that a flat spectrum is always desirable or establish any particular non-flat target spectrum.

The downstream obligation remains live and correctly scoped.

## 14. Governance and provenance

PASS.

The Chapter Ledger promotes ATLAS-CH-MATRIXOPT-001 to \`draft-v0.1\` and points to the exact specification, manuscript, derivation, source-lock, and witness paths.

The Source Register contains a unique Matrix-Aware Optimization source-lock entry.

The bibliography contains all four citation keys used by the manuscript.

The tranche receipt binds the protected baseline, exact prerequisite artifacts, source-lock checkpoint, witness, and completion rule.

Repository-wide canonical validation at implementation merge reports:

\`OK: 80 chapters, 126 hard edges, 1 root(s), 0 specification-ready keystones, 54 draft chapters, 18 rendered witnesses, 18 registered figures, 60 sources, 134 bibliography keys\`

## Final audit boundary

The durable result is:

\[
\boxed{
\text{matrix-aware update geometry}
\neq
\text{full curvature}
\neq
\text{parameter-manifold constraint}
}
\]

and, separately,

\[
\boxed{
\text{polar singular-value flattening}
\neq
\text{arbitrary spectral shaping}.
}
\]

No repair is required.

The next legitimate operation is exact-head canonical validation of this audit record, followed by audit PR merge, frontier recomputation, and controller/handoff reset.
