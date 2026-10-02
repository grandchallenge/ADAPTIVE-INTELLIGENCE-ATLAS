# Keystone Specification — ATLAS-CH-NONNORMAL-001

## Identity

**Title:** Normality, Pseudospectra, and Transient Growth  
**Part:** Mathematical Substrate  
**Status:** specification-ready  
**Keystone role:** establish the mathematics needed to understand why apparently stable operators can amplify disturbances over finite horizons.

## Chapter contract

The chapter must break one naive intuition:

> Eigenvalues alone determine whether finite-time behavior is benign.

The reader should leave understanding why non-normal operators can have stable-looking spectra and still produce substantial transient amplification, why eigenvector geometry matters, and what pseudospectra reveal beyond ordinary eigenvalue plots.

## Dependency contract

Immediate hard prerequisite:

- \`ATLAS-CH-LINALG-001\` — formal.

Inherited foundation:

- \`ATLAS-CH-OBJECTS-001\`;
- \`ATLAS-CH-THESIS-001\`.

The chapter may assume eigenvalues, eigenvectors, SVD, induced norms, singular values, and conditioning. It may not assume optimizer dynamics.

## Reader outcome

The reader should be able to:

1. define normal and non-normal matrices;
2. explain the role of orthogonal/unitary diagonalization;
3. construct a stable-eigenvalue matrix with transient growth;
4. distinguish spectral radius from operator norm;
5. explain eigenvector conditioning;
6. define the \(\varepsilon\)-pseudospectrum;
7. interpret resolvent growth;
8. connect the mathematics to later learning-system diagnostics without universalizing the mechanism.

## Formal spine

Open with

\[
A=
\begin{pmatrix}
a&K\\
0&a
\end{pmatrix},
\qquad |a|<1.
\]

Derive

\[
A^n
=
\begin{pmatrix}
a^n&nKa^{n-1}\\
0&a^n
\end{pmatrix}.
\]

Definitions:

- normal matrix/operator;
- spectral radius;
- transient amplification;
- resolvent;
- \(\varepsilon\)-pseudospectrum.

Core results should establish or source-lock:

1. for a normal matrix,
   \[
   \|A^n\|_2=\rho(A)^n;
   \]
2. diagonalizable non-normal bounds include eigenvector conditioning;
3. resolvent norm controls pseudospectral expansion;
4. broad pseudospectra expose sensitivity invisible in the eigenvalue set alone.

Every norm convention and hypothesis must be explicit.

## Principal intuition device

### Allegory: aligned currents in a harbor

Several individually decaying directions can be aligned so that interaction among them produces a temporary surge before decay dominates.

Structural correspondence:

- asymptotic decay ↔ eigenvalues inside the unit disk;
- non-orthogonal directions ↔ non-normal modal geometry;
- temporary surge ↔ transient operator-norm growth.

Limit of allegory:

The matrix need not describe a fluid. The analogy is only about geometric interaction among directions.

## Figure programme

### ATLAS-FIG-PSPECTRUM-001

Compare:

- one normal matrix;
- one non-normal matrix;
- matched eigenvalues;
- \(\|A^n\|_2\) over finite \(n\);
- pseudospectral contours.

The teaching frame is:

> same eigenvalue story, different finite-time story.

## Wolfram witnesses

1. exact power of the \(2\times2\) Jordan-like example;
2. singular-value computation of \(A^n\);
3. pseudospectral contours via \(\sigma_{\min}(zI-A)\);
4. parameter sweep in \(K\);
5. matched normal comparison.

## Counterexamples and failure boundaries

State explicitly:

- non-normal does not mean unstable;
- transient growth does not imply eventual divergence;
- broad pseudospectra do not identify a neural causal mechanism;
- eigenvalues remain informative but may be insufficient;
- transient gain depends on norm and horizon.

## Downstream obligations

Provides machinery for:

- \`ATLAS-CH-SPECTRALSHAPE-001\`;
- \`ATLAS-CH-OPTDYN-001\`;
- \`ATLAS-CH-ROUTERDYN-001\`;
- \`ATLAS-CH-SPECTRALDIAG-001\`.

## Source-lock plan

Source-lock:

- a standard matrix-analysis reference;
- a canonical pseudospectra reference;
- primary work on transient growth in non-normal systems;
- separate primary sources for later neural/optimization applications.

## Acceptance criteria

The draft must include:

- an exact \(2\times2\) transient-growth derivation;
- a normal/non-normal comparison;
- a precise pseudospectrum convention;
- a Wolfram-rendered contour witness;
- explicit norm conventions;
- failure-boundary statements;
- no claim that non-normality alone explains training instability.
