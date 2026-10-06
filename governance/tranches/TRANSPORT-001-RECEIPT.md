# TRANSPORT-001 — Transaction Receipt

## Identity

- chapter: `ATLAS-CH-TRANSPORT-001`
- title: **Representation as Transport**
- implementation issue: #211
- branch: `work/transport-211`
- protected baseline: `db2b19c4730a938babe9a2734eb40f898ee9913e`
- controller branch: `state/atlas-controller`

## Hard prerequisite bindings

### NORMREP-001

- manuscript: `1500987b384fb931bbd01879756c08b42ebcff28`
- source lock: `58b8331e56f5c9859e72be5c58f283706b5c436e`
- AUDIT-005: `11f45d9edf309cf55d9c4b0582ca88cd25c02c4d`

### SPLIT-001

- manuscript: `bcaf1db6b1fc7144e2472ff2725f7ff561fe7fc0`
- source lock: `afb84e2f3ebb941f320c52693b088b0eb078b8ce`
- AUDIT-036: `5e093460550c15fe491ba3214b2f52d48076dc0a`

## Implementation artifact blobs

- specification: `3498ea034cef08ff659cd5bf6a93059d66e12464`
- derivation packet: `26ba43d43d911c4c689ce60d01443e84d48bea01`
- computational witness: `09759b3d0d324507f1478c06cd04ff6078b37380`
- reader manuscript: `2346ec5fcde35e899db31fc91e5ef34a3e1b24e5`
- source lock: `55fcd80bc3d94e3b270ddcf28873242ba21f823f`
- Chapter Ledger: `f8b94379c507776e031dced47a7fc602f95ab5b7`
- Source Register: `eeaceee0b1a70b972987d66d68b1dd4bc63b12e0`
- bibliography (unchanged): `d162e7ba05c510a6d1580bbfec714141d9325f62`

## Durable mathematical substrate

The tranche establishes:

1. a finite representation trajectory as an ordered composition of declared state maps;
2. a strict separation between discrete map composition and exact continuous flow;
3. sphere-constrained transport by normalized retraction;
4. an exact counterexample showing retraction endpoint != exponential-map endpoint;
5. base-point ownership of tangent data;
6. an exact projection witness showing old tangent coordinates need not remain tangent after the state moves;
7. an exact two-stage \(S^2\) witness showing feasible constrained updates can be order-sensitive;
8. constraint preservation != information preservation;
9. shared-map versus stage-dependent/nonautonomous transport semantics;
10. a strict firewall between representation transport and optimal/vector/parallel transport.

## Exact finite witnesses

### Retraction versus exponential map

\[
u=(1,0),\qquad \xi=(0,1).
\]

Normalized retraction:

\[
R_u(\xi)=\frac{(1,1)}{\sqrt2}
\]

has angular displacement \(\pi/4\).

The unit-speed exponential endpoint at unit time has angular displacement \(1\).

Therefore the endpoints differ.

### Tangent ownership

After moving to

\[
u_1=(1,1)/\sqrt2,
\]

the old tangent vector

\[
v_0=(0,1)
\]

satisfies

\[
u_1^\top v_0=1/\sqrt2\neq0.
\]

Its new tangent projection is

\[
(-1/2,1/2).
\]

### Ordered constrained transport

\[
u_{ab}
=
(1/2,1/2,1/\sqrt2),
\]

\[
u_{ba}
=
(1/2,1/\sqrt2,1/2).
\]

Both have unit norm, but

\[
u_{ab}\neq u_{ba}.
\]

Their exact inner product is

\[
1/4+1/\sqrt2.
\]

## Claim boundaries

This transaction does **not** establish that:

- arbitrary neural layers are exact ODE flows;
- finite residual stacks have unique continuous generators;
- retractions are geodesic/exponential maps;
- state transport is vector or parallel transport;
- representation transport is optimal transport;
- constraint preservation implies invertibility, information preservation, stability, or task quality;
- classical Krylov convergence transfers to learned nonlinear transport.

## Downstream handoff

Direct consumer:

- `ATLAS-CH-NEURALKRYLOV-001`.

The downstream chapter may inherit the declared transport-map interface and local linearization objects, but must independently establish every Krylov, projection, residual, preconditioning, and convergence claim.

## Validation state

Implementation remains unmerged until:

1. canonical Linux validation passes on the exact implementation head;
2. GitHub Actions validation passes on that exact head;
3. implementation PR merges with an exact-head lease;
4. a fresh post-draft audit runs from the implementation merge;
5. repaired audit head, if any, receives fresh exact-head validation;
6. audit merges;
7. final merged `main` validation passes;
8. frontier is recomputed and controller/handoff are reset.
