# ADAPTDEPTH-001 — Transaction Receipt

## Identity

- chapter: ATLAS-CH-ADAPTDEPTH-001
- title: Adaptive Depth as Error Control
- implementation issue: #219
- branch: work/adaptdepth-219
- protected baseline: e8129376ef673822ed6b43775a0d2439b88c47fb
- controller branch: state/atlas-controller

## Hard prerequisite bindings

### DEPTH-001

- manuscript: 9d365778e873217c40604a621dbe9f88ca2153e0
- source lock: b6c18e2e0e3ab82c65d830967e2874bfb41e9bb2
- AUDIT-018: 0c9f5405bd7d94018d76aa93ebe74ec3e505cabe

### NETNUM-001

- manuscript: cbaf0b96c996c821df50f985075f64028459c587
- source lock: 02bbe77d19da4a6a123e430f8aae058d666c4e35
- AUDIT-023: 746e0c297e4ddf29122d4735108becc33e599030

## Implementation artifact blobs

- specification: 00cd2477035b9d106a8b16157e03520d1652e67e
- derivation packet: cd67d0d4fb987ddbc6cbe4c25192f593f8a7007c
- computational witness: 6d4240764b3e7be447f436d330ca4b88174ac22f
- reader manuscript: 61d47ce36a825effb75c246501ca8b66f446261e
- source lock: 717bbe901d7bc4514919f70bd65a1712e6d3aae7
- Chapter Ledger: 487fb507262ca9520d37e42397c3dc52f375ac6b
- Source Register: 4b5b06e0c702eaa79eb7a0771b15ab10a860762b
- bibliography: 7a7a89bc7c3789e0865755e446ee41d7d95815f2

## Durable mathematical substrate

The tranche establishes:

1. a formal separation among execution depth, numerical step size, local error estimate, and learned halting score;
2. an embedded-pair local-error-control interface;
3. an exact Euler/Heun one-step witness on y'=t where the pair difference equals the Euler local error;
4. an exact reject/shrink/retry witness for tolerance 1/8;
5. an idealized order-based step controller mapping h=1 to h=1/2 in that witness;
6. a strict local-versus-global error boundary;
7. a learned-halting interface with criterion_met versus budget_exhausted;
8. an exact monotone-but-miscalibrated halting-score counterexample;
9. an exact calibrated threshold transformation when the score/error map is known;
10. a strict separation between adaptive depth and adaptive numerical time stepping;
11. a strict separation between error control and compute optimality.

## Exact numerical witness

For

\[
y'(t)=t,\qquad y(0)=0,
\]

the exact solution is

\[
y(t)=t^2/2.
\]

For one step h:

- Euler: y_E=0;
- Heun: y_H=h^2/2;
- exact endpoint: y(h)=h^2/2.

Therefore

\[
|y_H-y_E|=h^2/2
\]

equals the Euler one-step error exactly for this witness.

With tolerance 1/8:

- h=1 gives estimated error 1/2 and is rejected;
- the idealized p=1 controller gives h_new=1/2;
- h=1/2 gives estimated error 1/8 and meets tolerance.

## Exact learned-halting witness

For

\[
x_{k+1}=(x_k+2)/2,\qquad x_0=0,
\]

true error is

\[
E_k=2^{1-k}.
\]

Define

\[
q_k=4^{-k}=E_k^2/4.
\]

The score ranks all depths perfectly by error.

Yet at k=2:

\[
q_2=1/16,\qquad E_2=1/2.
\]

Therefore using score threshold 1/16 as if it were error tolerance 1/16 stops eight times outside the requested error tolerance.

The exact relation is

\[
E_k=2\sqrt{q_k}.
\]

For target error epsilon, the calibrated score threshold is

\[
q_k\le(\epsilon/2)^2.
\]

For epsilon=1/16, the threshold is 1/1024, first met at k=5 where E_5=1/16.

## Claim boundaries

This transaction does not establish that:

- learned halting scores are numerical error estimators;
- adaptive execution depth is adaptive numerical step size;
- embedded differences are exact local errors for arbitrary problems;
- accepted local estimates imply a global error guarantee without further hypotheses;
- ranking quality supplies magnitude calibration;
- expected calibration supplies a per-instance upper bound;
- spatially variable neural depth is adaptive PDE mesh refinement;
- meeting an error tolerance minimizes resource use.

## Source scope

- Graves ACT: learned recurrent compute allocation;
- Figurnov et al.: learned spatial compute allocation;
- Dormand-Prince: embedded Runge-Kutta formulas of differing order and the numerical error-control mechanism.

The chapter does not universalize source-specific empirical claims.

## Validation state

Implementation remains unmerged until canonical Linux validation and exact-head GitHub validation both pass, followed by implementation merge, mandatory post-draft audit, final-main validation, frontier recomputation, issue closure, and controller/handoff reset.
