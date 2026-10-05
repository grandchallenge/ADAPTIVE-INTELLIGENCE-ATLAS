# Chapter 184 Transaction Receipt

Stable chapter ID: ATLAS-CH-MATRIXOPT-001  
Issue: #184  
Baseline: b75d840b51268d2ac43041af7a02fade2a660ba3  
Work branch: work/ch184a  
Source-lock checkpoint: 7753510f68307aff23b3285fc750aae185897af6  
Direct consumer: ATLAS-CH-SPECTRALSHAPE-001

## Prerequisite binds

LINALG:

- manuscript: e7fcf56322f26d232d3a3043038d9850792b4bde
- source lock: f24e93ee0c2496ca0b9d71f6f824b0d13dbdc08e
- Foundation audit AUDIT-004: 948f76b3f86d27fa4830efc30d8ef0135134256e

SECOND:

- manuscript: 10ee7db734df519e886e335301bf107d01d27f5c
- source lock: bc74588fd65df1a88a524b5241ca08ff498e0231
- post-draft audit AUDIT-041: 32d55baa0f8c3d5967f704c699fed81772ae2fd8

All prerequisite identities are bound at protected baseline:

`b75d840b51268d2ac43041af7a02fade2a660ba3`.

## External sources

- Gupta, Koren, Singer (2018), *Shampoo: Preconditioned Stochastic Tensor Optimization*.
- Higham (1986), *Computing the Polar Decomposition—with Applications*, DOI 10.1137/0907079.
- Bernstein and Newhouse (2024), *Old Optimizer, New Norm: An Anthology*, arXiv:2409.20325.
- Jordan et al. (2024), *Muon: An optimizer for hidden layers in neural networks*.

Empirical claims remain scoped to the cited source settings.

## Exact witness

The finite witness uses

\[
G=
\begin{pmatrix}
2&0\\
0&1\\
1&0
\end{pmatrix}.
\]

It establishes:

- singular values \(\sqrt5,1\);
- \(G^\top G=\operatorname{diag}(5,1)\);
- \(GG^\top\) has rank 2 and is singular;
- exact polar factor
  \[
  Q=
  \begin{pmatrix}
  2/\sqrt5&0\\
  0&1\\
  1/\sqrt5&0
  \end{pmatrix};
  \]
- \(Q^\top Q=I_2\) while \(QQ^\top\ne I_3\);
- \(\|G\|_F=\sqrt6\), \(\|G\|_2=\sqrt5\), and \(\|G\|_*=\sqrt5+1\);
- representative diagonal row scaling has singular values \(\sqrt5/2,1\);
- the one-step left Shampoo statistic is singular for this tall matrix;
- the support-restricted two-sided inverse-fourth-root identity yields the polar factor.

## Durable boundaries

- elementwise scaling != matrix preconditioning;
- matrix preconditioning != full Hessian inversion;
- one-step inverse-root support identity != stateful Shampoo equivalence;
- exact polar factor != finite Newton-Schulz realization;
- orthogonalized update != manifold-constrained parameter;
- singular-value flattening != arbitrary spectral shaping;
- square orthogonality != rectangular semi-orthogonality;
- empirical source result != universal optimizer theorem.

## Artifact paths

- source lock: sources/source-locks/ATLAS-CH-MATRIXOPT-001.yaml
- specification: manuscript/specifications/ATLAS-CH-MATRIXOPT-001.md
- derivation packet: mathematics/derivations/ATLAS-CH-MATRIXOPT-001-DERIVATIONS.md
- computational witness: mathematics/computational-witnesses/ATLAS-CW-MATRIXOPT-001.md
- reader manuscript: manuscript/parts/05-optimization/ATLAS-CH-MATRIXOPT-001.md
- Chapter Ledger: governance/CHAPTER_LEDGER.yaml
- Source Register: governance/SOURCE_REGISTER.yaml
- bibliography: sources/bibliography.bib

## Completion rule

Implementation may merge only after exact-head canonical validation is green.

A fresh bounded post-draft audit must then recheck prerequisite identities, source scope, rectangular algebra, norm-duality reasoning, one-step Shampoo/polar boundaries, Muon exact-versus-approximate language, and downstream SPECTRALSHAPE separation before the transaction is complete.
