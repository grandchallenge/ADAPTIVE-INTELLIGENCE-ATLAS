# AUDIT-002 — Attention + Optimizer-State Dynamics

## Disposition

**PASS WITH REPAIRS ALREADY APPLIED IN KEYSTONE-003**

The two chapters are fit to remain at \`draft-v0.1\` and to serve as the operator/dynamical style reference for the final keystone pair.

This audit does not promote either chapter to theorem, certification, publication-ready, or final-copy status.

## Audited baseline

- KEYSTONE-003 merge: \`35ec41f9dceb0ce7c598f594c75163ca09d1dd5d\`;
- work issue: \`#9\`.

## 1. Attention as an Operator

### Standard equations

PASS.

The chapter uses

\[
Q=XW_Q,\qquad K=XW_K,\qquad V=XW_V,
\]

\[
S=\frac{QK^\top}{\sqrt{d_k}},
\qquad
A=\operatorname{softmax}_{\rm row}(S),
\qquad
Y=AV.
\]

The dimensions and operator decomposition agree with the canonical Transformer formulation.

### Score/operator/value/full-map distinction

PASS.

The manuscript preserves four separate objects:

- score matrix \(S\);
- normalized mixing operator \(A\);
- value field \(V\);
- full state-dependent transformation \(F(X)=A(X)V(X)\).

No sentence reviewed collapses conditional linearity in \(V\) into linearity in \(X\).

### Full-map nonlinearity

PASS.

The scalar two-token counterexample is algebraically correct. The first-component discrepancy between \(F(2X)\) and \(2F(X)\) has magnitude approximately

\[
0.5019104228.
\]

### Row stochasticity

PASS.

For finite, unmasked row-softmax scores,

\[
A\mathbf 1=\mathbf 1.
\]

The text correctly limits the Markov analogy and does not describe the complete attention layer as a Markov process.

### Permutation equivariance

PASS.

The derivation

\[
F(PX)=PF(X)
\]

is explicitly scoped to the absence of positional information or asymmetric masking. The source-lock claim scope repeats that qualification.

### Causal masking

PASS.

The statement that a causal mask constrains the admissible support pattern of the mixing operator is exact for the stated row-softmax construction.

### Softmax sensitivity

PASS.

The row-softmax Jacobian

\[
J_{\rm softmax}(a)
=
\operatorname{diag}(a)-aa^\top
\]

and the first-order query perturbation calculation are correct.

### Kernel and linear-attention scope

PASS.

The source-lock correctly distinguishes:

- Tsai et al. as a kernel-smoother interpretation;
- Katharopoulos et al. as a kernel-feature/associativity construction for linear attention.

The chapter uses these as qualified lenses rather than claiming that every attention mechanism is one fixed positive-definite kernel machine.

Canonical source metadata was rechecked during the audit against the ACL Anthology and PMLR records.

### Figure and computational witness

PASS.

\`ATLAS-FIG-ATTNOP-001\`:

- source: \`figures/wolfram/ATLAS-FIG-ATTNOP-001.wl\`;
- rendered blob SHA-1: \`2ba96f6f30311c117f27c0717961145ce9cbb0cd\`;
- exact decoded PNG size: 24,852 bytes;
- manifest blob identity and byte count agree.

Independent Wolfram replay verified:

\[
\sum_jA_{ij}=1
\]

to numerical precision,

\[
A(2V)-2AV=0,
\]

and

\[
\Delta A_{1,:}
\approx
(-0.08124592681,\;0.02683052899,\;0.05441539782).
\]

The manuscript alt text is descriptive and the matrix cells carry numeric labels, so gray intensity is not the sole carrier of information.

### Epistemic boundary

PASS.

The manuscript repeatedly states that an attention operator or heat map is not, by itself, a causal explanation.

## 2. Optimizer-State Dynamics

### Momentum convention and augmented state

PASS WITH EXPLICIT-CONVENTION NOTE.

The chapter defines its recurrence before using it:

\[
v_{t+1}=\beta v_t+h\theta_t,
\qquad
\theta_{t+1}=\theta_t-\eta v_{t+1}.
\]

Momentum conventions differ across the literature. The manuscript does not silently assume equivalence of notation; all subsequent algebra is derived from the stated convention.

### State matrix

PASS.

For

\[
z_t=
\begin{pmatrix}
\theta_t\\
v_t
\end{pmatrix},
\]

the exact matrix is

\[
J=
\begin{pmatrix}
1-\eta h&-\eta\beta\\
h&\beta
\end{pmatrix}.
\]

### Characteristic polynomial

PASS.

\[
p(\lambda)
=
\lambda^2-(1-\eta h+\beta)\lambda+\beta.
\]

For

\[
h=1,\qquad
\eta=\frac1{10},\qquad
\beta=\frac9{10},
\]

Wolfram and hand algebra agree on

\[
\lambda_\pm
=
\frac9{10}\pm\frac3{10}i,
\]

with

\[
\rho(J)=\sqrt{\frac9{10}}
\approx0.9486832980505138<1.
\]

### Non-normality

PASS.

The exact matrices \(J^\top J\) and \(JJ^\top\) differ, so the worked state matrix is non-normal.

### Finite-horizon gain

PASS.

\[
J^4
=
\begin{pmatrix}
\frac{567}{2500}&-\frac{729}{3125}\\
\frac{324}{125}&\frac{567}{2500}
\end{pmatrix}.
\]

Independent Wolfram replay gives

\[
\sigma_{\max}(J^4)
=
2.610090585959495\ldots
\]

and the peak over \(n=0,\ldots,20\) occurs at \(n=4\).

The chapter therefore establishes, for this exact toy recurrence,

\[
\rho(J)<1
\quad\text{while}\quad
\|J^4\|_2>1.
\]

### Fixed system versus training trajectory

PASS.

The manuscript explicitly distinguishes the autonomous quadratic example from the time-varying local product

\[
J_{t+k-1}\cdots J_t
\]

encountered along a nonlinear stochastic training trajectory.

It does not promote one frozen local Jacobian to a global training model.

### Adam scope

PASS.

Adam is used only to demonstrate that modern optimizers enlarge the augmented state. The exact transient-growth witness remains the transparent momentum example.

### Control/IQC source scope

PASS.

Lessard, Recht, and Packard are cited as established precedent for analyzing iterative optimization algorithms through a control-theoretic/IQC framework. The Atlas does not claim its local non-normality analysis is identical to that framework.

The SIAM record was rechecked during the audit and explicitly lists Heavy-ball among the methods analyzed.

### CPS boundary

PASS.

The source-lock records that no separate public source for the exact CPS/optimizer-state-Jacobian results was bound. The chapter therefore names CPS only as a downstream GCL research programme and attributes no unsupported empirical result to it.

### Figure and computational witness

PASS.

\`ATLAS-FIG-OPTDYN-001\`:

- source: \`figures/wolfram/ATLAS-FIG-OPTDYN-001.wl\`;
- rendered blob SHA-1: \`fa8e5231cb6451c026a0ccd7beecdfcff330c98d\`;
- exact decoded PNG size: 65,403 bytes;
- manifest blob identity and byte count agree.

The three figure panels show trajectories, eigenvalues with unit circle, and finite-horizon \(2\)-norm gain. The manuscript alt text identifies all three.

### Epistemic boundary

PASS.

The text distinguishes:

- existence of a mechanism;
- local diagnosis along a trajectory;
- empirical prevalence in frontier training.

It does not infer the third from the first.

## 3. Source and citation audit

PASS.

Source-lock records are present for both chapters.

The canonical metadata checked during this audit agrees with the retained records for:

- Vaswani et al. 2017;
- Tsai et al. 2019;
- Katharopoulos et al. 2020;
- Polyak 1964;
- Sutskever et al. 2013;
- Kingma and Ba;
- Lessard, Recht, and Packard 2016.

Repository CI closes all manuscript citation keys against \`sources/bibliography.bib\`.

## 4. TeX and encoding integrity

PASS AFTER KEYSTONE-003 REPAIR.

During KEYSTONE-003, a stronger whole-tree validator exposed inherited JavaScript-escape corruption in earlier Atlas Markdown. The affected files were rewritten from their intended mathematics.

The durable validator now rejects every C0 control character except newline in Atlas-authored manuscript and mathematics Markdown.

The final KEYSTONE-003 validation result was:

\`OK: 80 chapters, 126 hard edges, 1 root(s), 2 specification-ready keystones, 4 draft keystones, 4 rendered witnesses, 6 registered figures, 10 sources, 15 bibliography keys\`

## 5. Final disposition

No additional mathematical or source-scope defect requiring manuscript repair was found in the Attention/Optimizer pair after the KEYSTONE-003 integrity repair.

The pair remains:

\`draft-v0.1\`

and is suitable to serve as the second style-setting pair.

The next substantive target is:

- \`ATLAS-CH-BCONTRACT-001\` — Boundary Contracts;
- \`ATLAS-CH-REPLAY-001\` — Replayable Evidence Objects.

These should be composed as the final keystone pair because they establish the Atlas’s compositional and scientific-evidence register.
