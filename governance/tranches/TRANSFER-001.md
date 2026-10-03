# TRANSFER-001 — Reconstruction and Transfer

## Status

**Tranche state:** implemented on branch pending merge validation.

## Baseline

- AUDIT-006 merge: \`aaab3af8ea6e8019ac0214b613e4eafa09802a91\`;
- issue: \`#32\`;
- hard prerequisites:
  - \`ATLAS-CH-RESIDUAL-001\` — audited \`draft-v0.1\`;
  - \`ATLAS-CH-INFO-001\` — audited \`draft-v0.1\`.

## Objective

Operationalize the Residual across source/target boundaries:

> Transfer succeeds, in the exact reconstruction sense developed here, when representation-specific states can be compiled into a common capability-sufficient object from which the declared target task family can be reconstructed.

This is an Atlas synthesis layered on standard transfer-learning terminology.

## A. Standard transfer framing

The chapter uses Pan–Yang's domain/task distinction:

\[
\mathcal D=(\mathcal X,P(X)),
\]

\[
\mathcal T=(\mathcal Y,f).
\]

Transfer is always source/target relative.

No universal transfer representation is assumed.

## B. Common-Residual transfer certificate

Let:

\[
E_s:X\to Z_s,
\qquad
E_t:X\to Z_t
\]

be source and target representations.

Let

\[
R:X\to\mathcal R
\]

be a declared common Residual with compilers

\[
C_s:Z_s\to\mathcal R,
\qquad
C_t:Z_t\to\mathcal R.
\]

If

\[
C_s(E_s(x))
=
C_t(E_t(x))
=
R(x)
\]

for all declared states, and each target capability factors as

\[
B_t(x,q)=D_q(R(x)),
\]

then

\[
B_t(x,q)
=
D_q(C_s(E_s(x)))
=
D_q(C_t(E_t(x))).
\]

Thus both representations support exact target reconstruction through the same Residual.

This is explicitly a sufficient certificate, not a necessary characterization of all transfer.

## C. Exact recoding witness

Transferable object:

\[
r=(3,1).
\]

Source map:

\[
A_s=
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix}.
\]

Target map:

\[
A_t=
\begin{pmatrix}
2&0\\
0&1/2
\end{pmatrix}.
\]

Representations:

\[
z_s=(4,2),
\qquad
z_t=(6,1/2).
\]

Compilers:

\[
C_s=A_s^{-1},
\qquad
C_t=A_t^{-1}.
\]

Both reconstruct:

\[
r=(3,1).
\]

Two target tasks:

\[
D_1(a,b)=a+b,
\]

\[
D_2(a,b)=2a-b.
\]

Both source and target representations reconstruct exact outputs:

\[
D_1=4,
\qquad
D_2=5.
\]

## D. Fiber criterion

For deterministic representation

\[
Z:X\to\mathcal Z
\]

and deterministic capability

\[
B:X\to\mathcal Y,
\]

an exact decoder

\[
D:\mathcal Z\to\mathcal Y
\]

with

\[
B=D\circ Z
\]

exists if and only if \(B\) is constant on every realized fiber of \(Z\):

\[
Z(x_1)=Z(x_2)
\Rightarrow
B(x_1)=B(x_2).
\]

The derivation packet proves necessity and sufficiency.

## E. Exact lossy-bottleneck failure

Let

\[
P(a,b)=a.
\]

Take

\[
r_A=(1,0),
\qquad
r_B=(1,1).
\]

Then

\[
P(r_A)=P(r_B)=1.
\]

But for

\[
D_2(a,b)=2a-b,
\]

\[
D_2(r_A)=2,
\qquad
D_2(r_B)=1.
\]

No deterministic decoder from the bottleneck value alone can reconstruct both outputs.

This demonstrates:

\[
\text{one-task sufficiency}
\not\Rightarrow
\text{task-family sufficiency}.
\]

## F. Negative transfer

The chapter defines negative transfer operationally relative to:

- a declared target metric;
- a matched target-only baseline;
- a declared data/adaptation setting.

For higher-is-better score \(J\),

\[
J(M_{\rm transfer})
<
J(M_{\rm target-only})
\]

constitutes negative transfer in that comparison.

The chapter does not assume transfer always helps.

## G. Empirical source boundary

External sources are used only for bounded claims:

- Pan–Yang 2010:
  transfer-learning taxonomy, source/target framing, negative-transfer problem;
- Yosinski et al. 2014:
  layer/task dependence of feature transferability and co-adaptation/optimization effects;
- Kornblith et al. 2019:
  source-task performance and transferred-feature quality are not interchangeable;
- Achille–Soatto:
  task-relative sufficiency/minimality/nuisance invariance;
- Information Bottleneck:
  preservation of target-relevant information under compression as a supporting analogy.

The common-Residual reconstruction certificate and deterministic fiber framing are Atlas synthesis.

## H. Figure

\`ATLAS-FIG-TRANSFER-001\`

- generator blob:
  \`6956781f49cf189383961b3be069028abfb1ac31\`;
- rendered blob:
  \`b24dade0ca0572b1a60a08a58a37115e82a2ffc3\`;
- rendered bytes:
  \`35,171\`;
- representation class:
  schematic with exact matrix/state/output annotations.

## I. Durable objects

The branch contains:

- \`sources/source-locks/ATLAS-CH-TRANSFER-001.yaml\`;
- \`manuscript/specifications/ATLAS-CH-TRANSFER-001.md\`;
- \`mathematics/derivations/ATLAS-CH-TRANSFER-001-DERIVATIONS.md\`;
- \`mathematics/computational-witnesses/ATLAS-CW-TRANSFER-001.md\`;
- \`manuscript/parts/03-representation-learning/ATLAS-CH-TRANSFER-001.md\`;
- Wolfram generator/master/manifest;
- Figure Register entry;
- Chapter Ledger promotion to \`draft-v0.1\`.

## J. Frozen distinctions

\[
\text{parameter reuse}
\neq
\text{capability transfer}.
\]

\[
\text{source accuracy}
\neq
\text{universal transfer quality}.
\]

\[
\text{one-task sufficiency}
\neq
\text{task-family sufficiency}.
\]

\[
\text{invertible information-preserving path}
\neq
\text{guaranteed learnable adapter}.
\]

\[
\text{semantic reconstruction certificate}
\neq
\text{complete transfer-learning theory}.
\]

## K. Next step after merge

Run a bounded post-draft audit checking:

- source/target framing;
- common-Residual certificate;
- fiber criterion proof;
- exact linear witness;
- bottleneck impossibility witness;
- empirical-source scope;
- negative-transfer definition;
- figure identity;
- no promotion of transfer reconstruction into a universal transfer theorem.
