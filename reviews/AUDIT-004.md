# AUDIT-004 — FOUNDATION-001 Reader Spine

## Disposition

**PASS WITH PROVENANCE-VALIDATOR REPAIR**

The five FOUNDATION-001 chapters are fit to remain at draft-v0.1.

No mathematical, source-scope, dependency, or figure-semantics defect requiring manuscript repair was found during this post-merge audit.

AUDIT-004 did identify one infrastructure gap: rendered-figure manifests recorded exact Git blob identities and byte counts, but CI did not verify those recorded identities against the checked-out files. The validator is strengthened by this audit to make that provenance relation machine-enforced.

This audit does not promote any chapter to publication-ready, certified, or final-copy status.

## Audited baseline

- FOUNDATION-001 merge: ed0b2d6f40cbd95498810315d416a7ee610edc88
- audit issue: #22
- audited chapters:
  - ATLAS-CH-THESIS-001
  - ATLAS-CH-OBJECTS-001
  - ATLAS-CH-LINALG-001
  - ATLAS-CH-INFO-001
  - ATLAS-CH-REP-001

## 1. Adaptive-System Thesis

### Epistemic status

PASS.

The manuscript labels the governing claim as Atlas Synthesis.

The source lock binds only project-local objects:

- the 2026-10-02 source inventory;
- Atlas Map;
- Editorial Profile;
- Chapter Composition Protocol.

The pinned Git blob identities at baseline 3f74175d14e587d2567140025a79bfa78eefd125 were re-fetched and match the lock.

The chapter explicitly denies the stronger claim that its organizing thesis is an externally established theorem or universal ontology of intelligence.

### System boundary

PASS.

The manuscript distinguishes a learned model from a larger adaptive computational system that may also include memory, retrieval, tools, interfaces, evidence and governance.

The inclusion

\[
\text{model}
\subseteq
\text{adaptive computational system}
\]

is presented as the Atlas explanatory boundary, not as a universal mathematical theorem.

### Vulnerability / failure boundary

PASS.

The chapter states pressure points under which the thesis would become less useful.

Examples are used to motivate the programme, not prove it.

## 2. States, Operators, Flows, and Interfaces

### Four-role taxonomy

PASS.

The chapter distinguishes:

- state: an instantiated information-bearing value;
- operator: a transformation;
- flow/dynamics: accumulated evolution;
- interface: what composition may assume across a boundary.

The source lock explicitly identifies this taxonomy as Atlas synthesis rather than a canonical external classification.

### Category errors

PASS.

The chapter gives concrete cases where identical storage shape does not determine role:

- matrix as covariance state versus linear operator;
- single residual update versus depth-indexed evolution;
- shape-compatible interface versus semantic compatibility;
- evidence record versus the object described by that evidence.

### Flow scope

PASS.

The exact flow law

\[
\Phi_{t+s}
=
\Phi_t\circ\Phi_s
\]

is stated only for a true flow structure.

Depth-indexed neural computation is described more cautiously as flow-like or admitting a dynamical/integrator interpretation where appropriate.

### Interface scope

PASS.

The chapter does not claim that shape/type compatibility is sufficient for semantic composability.

## 3. Linear Maps and Decompositions

### Source scope

PASS.

The source lock uses:

- Trefethen and Bau, Numerical Linear Algebra;
- Horn and Johnson, Matrix Analysis;
- Golub and Van Loan, Matrix Computations.

These sources are used for standard finite-dimensional linear and numerical linear algebra, not for empirical neural-network claims.

### Projection algebra

PASS.

For orthonormal-column matrix \(Q\),

\[
P=QQ^\top
\]

satisfies

\[
P^2=P,
\qquad
P^\top=P.
\]

The derivation is correct.

### SVD and eigenvalue distinction

PASS.

For

\[
A=
\begin{pmatrix}
1&1\\
0&1
\end{pmatrix},
\]

independent Wolfram replay gives eigenvalues

\[
\{1,1\},
\]

and singular values

\[
\left\{
\frac{1+\sqrt5}{2},
\frac{\sqrt5-1}{2}
\right\}.
\]

This correctly demonstrates that eigenvalue magnitude and one-step Euclidean amplification are different quantities for a non-normal matrix.

### Low-rank approximation

PASS.

The chapter states the Eckart–Young spectral-norm error

\[
\|A-A_k\|_2=\sigma_{k+1}
\]

for the standard truncated SVD setting.

For the witness matrix, the rank-one error is independently replayed as

\[
\frac{\sqrt5-1}{2}.
\]

### Conditioning

PASS.

For

\[
D=\operatorname{diag}(1,1/100),
\]

independent replay gives

\[
\kappa_2(D)=100.
\]

The manuscript correctly distinguishes problem conditioning from algorithmic stability and from general nonlinear optimization difficulty.

### Pseudoinverse scope

PASS.

The Moore-Penrose pseudoinverse is used only in the standard finite-dimensional least-squares/minimum-norm setting.

### Figure identity

PASS.

ATLAS-FIG-LINALG-001:

- source blob: 94450cbddb6c10c06d61f758454ef0aa0090caf8
- rendered blob: d861c038e841450ccfabb8f0709e161d6a555450
- rendered bytes: 41,238

The manifest values match the merged Git tree.

## 4. Probability, Information, and Statistical Structure

### Source scope

PASS.

The source lock uses:

- Cover and Thomas for entropy, KL divergence, mutual information and information inequalities;
- Wainwright and Jordan for exponential-family/sufficient-statistic structure;
- Vershynin for high-dimensional probability and concentration.

The chapter does not use these sources to make semantic or causal claims that exceed their scope.

### Entropy and KL

PASS.

The discrete entropy and KL definitions are standard.

The manuscript preserves that:

- KL is asymmetric;
- KL is not a metric;
- KL may be infinite when the relevant absolute-continuity/support condition fails.

### Mutual information

PASS.

For

\[
P_{XY}
=
\begin{pmatrix}
3/8&1/8\\
1/8&3/8
\end{pmatrix},
\]

independent Wolfram replay gives uniform marginals and

\[
I(X;Y)
=
\frac{\log(27/16)}{\log16}
\approx
0.1887218755408671
\]

bits.

For a fair deterministic relation \(Y=X\), replay gives

\[
I(X;Y)=1
\]

bit.

The manuscript explicitly states that mutual information is statistical dependence, not causal direction.

### Exponential-family witness

PASS.

For Bernoulli \(x\in\{0,1\}\),

\[
\eta
=
\log\frac{p}{1-p},
\qquad
A(\eta)
=
\log(1+e^\eta),
\]

and

\[
p(x)
=
\exp\{x\eta-A(\eta)\}.
\]

Independent symbolic replay reconstructs the Bernoulli parameter exactly.

### Concentration scope

PASS.

The chapter refuses to state concentration bounds independently of assumptions and uses boundedness/independence as an explicit example of required hypotheses.

### Figure identity

PASS.

ATLAS-FIG-INFO-001:

- source blob: 9b4feabb9f0413dd3fa499b8353e84e405391da4
- rendered blob: 46ac60a0ff3c0b14fa81bf970e8307f182442d08
- rendered bytes: 21,815

The manifest values match the merged Git tree.

## 5. Representations and Invariants

### Source scope

PASS.

The source lock distinguishes:

- peer-reviewed representation-learning survey context;
- peer-reviewed group-equivariance example;
- peer-reviewed identifiability limitation;
- peer-reviewed historical sparse-coding example;
- non-peer-reviewed superposition toy-model research evidence.

The broader representation-equivalence organization is explicitly Atlas synthesis.

### Invariance and equivariance

PASS.

The manuscript defines:

\[
r(g\cdot x)=r(x)
\]

for invariance, and

\[
r(g\cdot x)=\rho(g)r(x)
\]

for equivariance.

The distinction is maintained throughout.

### Reflection witness

PASS.

For

\[
G=
\operatorname{diag}(-1,1),
\qquad
x=(2,3),
\]

independent replay gives

\[
Gx=(-2,3)
\]

and verifies

\[
\|x\|_2^2
=
\|Gx\|_2^2
=
13.
\]

### Invertible recoding

PASS.

For

\[
T=
\begin{pmatrix}
1&1\\
0&1
\end{pmatrix},
\qquad
z=(2,3),
\qquad
w=(4,-1),
\]

the manuscript defines

\[
\tilde z=Tz,
\qquad
\tilde w=T^{-\top}w.
\]

Independent replay gives

\[
\tilde z=(5,3),
\qquad
\tilde w=(4,-5),
\]

and

\[
w^\top z
=
\tilde w^\top\tilde z
=
5.
\]

The manuscript correctly scopes this as readout-preserving recoding for the declared task, not universal semantic equivalence.

### Identifiability

PASS.

The chapter uses Locatello et al. to limit unsupervised-disentanglement identifiability claims under the source's assumptions.

It does not generalize the result into a claim that useful representation learning is impossible.

### Sparse coding

PASS.

Olshausen–Field is used as a historical sparse-coding model/example, not as a universal theorem about neural feature sparsity.

### Superposition

PASS.

Elhage et al. is explicitly labeled non-peer-reviewed toy-model/research evidence.

The chapter does not promote its toy-model mechanism to universal empirical prevalence in frontier models.

### Figure identity and semantics

PASS.

ATLAS-FIG-REP-001:

- source blob: 9aad5571d51fd9c8dcfc08dfebd300c3758c5a2a
- rendered blob: e14a1b9738190ed9b5930657c82dbe3c8ea21492
- rendered bytes: 44,643

The manifest values match the merged Git tree.

The representation class is correctly schematic because the recoding panel's box geometry is presentational even though the displayed algebraic values are exact.

## 6. Dependency closure

PASS.

The merged Chapter Ledger records:

\[
\text{THESIS}
\to
\text{OBJECTS},
\]

\[
\text{OBJECTS}
\to
\{\text{LINALG},\text{INFO}\},
\]

\[
\text{LINALG}
\to
\text{GEOM},
\]

and

\[
\{\text{INFO},\text{GEOM}\}
\to
\text{REP}.
\]

All six nodes in this path, including the previously drafted Geometry keystone, are at draft-v0.1.

Normalized and quotient representation chapters are therefore downstream of a now-explicit reader spine, but remain blocked until this audit merges.

## 7. Source and citation closure

PASS.

The FOUNDATION-001 branch passed repository-wide citation closure before merge.

The source locks contain exact citation keys for every external source consumed by the three technical chapters.

The Thesis and Objects chapters explicitly identify their internal project sources and do not convert those project-local documents into external scientific authority.

## 8. Figure provenance repair

### Audit finding

The merged figure manifests already recorded:

- generator source path;
- generator Git blob SHA-1;
- rendered path;
- rendered Git blob SHA-1;
- rendered byte count;
- claim boundary.

However, the validator checked file existence and manifest identity fields without recomputing the recorded Git blob identities or byte count.

### Repair

AUDIT-004 extends tools/validate_atlas.py with Git-compatible blob hashing:

\[
\operatorname{SHA1}
(
\texttt{"blob "}\Vert
\text{byte length}
\Vert
\texttt{NUL}
\Vert
\text{content}
).
\]

For every rendered witness figure, CI now verifies:

1. source file exists;
2. rendered file exists;
3. manifest source Git blob SHA-1 equals the checked-out source;
4. manifest rendered Git blob SHA-1 equals the checked-out rendered file;
5. manifest rendered byte count equals the checked-out rendered file length.

All nine current rendered figure manifests already carry these fields.

This converts an audit convention into a durable invariant.

## 9. Integrity history

FOUNDATION-001's first validation runs exposed hidden control characters caused by TeX escape serialization in generated Markdown.

Those defects were repaired before merge and recorded in the tranche receipt.

The merged manuscripts, specifications, derivations and witnesses passed the whole-tree control-character guard.

AUDIT-004 does not rewrite that historical repair.

## 10. Final disposition

AUDIT-004 passes with one provenance-validator repair.

No manuscript claim requires epistemic promotion or demotion.

The five Foundation chapters remain:

draft-v0.1.

After this audit merges, the reader path through Representation is clear to advance into the next bounded representation tranche, beginning with normalized and quotient representations only after their own source-lock/specification step.
