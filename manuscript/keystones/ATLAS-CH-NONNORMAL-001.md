# Keystone Specification — ATLAS-CH-NONNORMAL-001

## Identity

**Title:** Normality, Pseudospectra, and Transient Growth  
**Part:** Mathematical Substrate  
**Status:** specification-ready  
**Keystone role:** establish the mathematics required to understand why apparently stable operators can amplify disturbances over finite horizons.

## Chapter contract

The chapter must destroy one specific naive intuition:

> eigenvalues alone determine whether finite-time behavior is benign.

The reader should leave understanding why non-normal operators can have stable-looking spectra and still produce large transient amplification, why eigenvectors and conditioning matter, and what pseudospectra add to ordinary spectral analysis.

## Dependency contract

Immediate hard prerequisite:

- `ATLAS-CH-LINALG-001` — formal.

Inherited prerequisite cone:

- `ATLAS-CH-OBJECTS-001`;
- `ATLAS-CH-THESIS-001`.

The chapter may assume eigenvalues, eigenvectors, SVD, induced norms, singular values, and conditioning. It may not assume dynamical-systems stability theory or optimizer dynamics.

## Reader outcome

The reader should be able to:

1. define normal and non-normal matrices;
2. explain why orthogonal/unitary diagonalization matters;
3. construct a stable-eigenvalue matrix with substantial transient norm growth;
4. distinguish spectral radius from operator norm;
5. explain eigenvector conditioning;
6. define the (arepsilon)-pseudospectrum in at least two equivalent finite-dimensional ways;
7. interpret resolvent growth;
8. connect transient amplification to later learning-system diagnostics without claiming that all training instability is non-normal.

## Formal spine

### Minimal opening counterexample

Use a (2	imes 2) upper-triangular matrix such as

[
A=egin{pmatrix}a & K\\0 & aend{pmatrix},
qquad |a|<1,
]

with (K) large.

Derive (A^k) explicitly and show that (ho(A)<1) can coexist with substantial finite-time (|A^k|).

The exact parameter choice should be selected to make the amplification visually clear while remaining numerically well-conditioned enough for reproduction.

### Definitions

- normal operator;
- departure from normality, with care that several measures exist;
- spectral radius;
- transient amplification;
- resolvent;
- (arepsilon)-pseudospectrum.

### Core results / derivations

The chapter should establish or source-lock:

1. normal matrices satisfy (|A^k|_2=ho(A)^k) when the spectral radius is realized by the largest absolute eigenvalue under unitary diagonalization;
2. diagonalizable non-normal matrices inherit bounds involving eigenvector-condition numbers;
3. resolvent norm controls pseudospectral expansion;
4. pseudospectra expose sensitivity invisible in the eigenvalue set alone.

Avoid presenting a pseudospectral bound without its norm convention and hypotheses.

## Principal intuition device

### Allegory: aligned currents in a harbor

Two individually decaying directions can be geometrically aligned so that motion transferred between them produces a temporary surge before decay dominates.

Structural correspondence:

- asymptotic decay ↔ eigenvalues inside the unit disk;
- aligned directions ↔ non-orthogonal eigenvectors/generalized directions;
- temporary surge ↔ transient operator-norm growth.

Limit of allegory:

The matrix need not represent a physical fluid, and non-normality is not identical to energy transfer in fluids. The analogy is about geometric interaction among directions.

## Figure programme

### ATLAS-FIG-PSPECTRUM-001 — Equal-looking spectra, unequal transient growth

Required comparison:

- one normal matrix;
- one non-normal matrix;
- matched or deliberately similar eigenvalue locations;
- (|A^k|_2) over finite (k);
- pseudospectral contours for both.

The strongest teaching frame is “same eigenvalue story, different finite-time story.”

Representation class: `data-derived`.

## Wolfram computational witnesses

1. exact symbolic power of the (2	imes2) Jordan-like example;
2. singular-value computation of (A^k);
3. pseudospectral contour calculation via smallest singular value of (zI-A);
4. parameter sweep in (K) showing growth of peak transient amplification;
5. optional comparison with a normal matrix sharing the same eigenvalues.

High precision should be available for contour validation near small singular values.

## Counterexamples and failure boundaries

The chapter must explicitly block these overstatements:

- non-normal does not mean unstable;
- transient growth does not imply eventual divergence;
- a large pseudospectrum does not by itself identify a causal mechanism in a neural network;
- eigenvalues remain informative, but can be insufficient;
- the magnitude of transient growth depends on norm and horizon.

## Bridge to learning systems

The final section may preview optimizer-state dynamics:

A learning update linearized around a trajectory or local state can inherit non-normal transient amplification. This is a motivation for later analysis, not yet an empirical claim about a particular optimizer.

No optimizer-specific conclusion should be promoted here.

## Downstream obligations

The chapter provides formal machinery for:

- `ATLAS-CH-SPECTRALSHAPE-001`;
- `ATLAS-CH-OPTDYN-001`;
- `ATLAS-CH-ROUTERDYN-001`;
- `ATLAS-CH-SPECTRALDIAG-001`.

Definitions and norm conventions must therefore remain stable.

## Source-lock plan

Before review-ready drafting, source-lock:

- a standard matrix-analysis reference;
- a primary or canonical pseudospectra reference;
- one reliable source for transient growth in non-normal systems;
- later, separate primary sources for any application to optimization or neural dynamics.

## Acceptance criteria

The drafted chapter must include:

- an exact (2	imes2) transient-growth derivation;
- a normal/non-normal comparison;
- a precise pseudospectrum definition;
- a Wolfram-rendered contour witness;
- explicit norm conventions;
- at least three failure-boundary statements;
- no claim that non-normality alone explains observed training instability.
