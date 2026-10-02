# KEYSTONE-002 — Geometry + Non-normality Manuscript Pair

## Status

**Tranche state:** implemented on branch pending merge validation.

## Objective

Produce the first style-setting mathematical chapter pair from the merged KEYSTONE-001 specifications:

- `ATLAS-CH-GEOM-001` — Geometry of Constrained State Spaces;
- `ATLAS-CH-NONNORMAL-001` — Normality, Pseudospectra, and Transient Growth.

## Baseline

- Architecture tag: `atlas-v0.1-architecture`
- KEYSTONE-001 merge: `47e2f4b43a9d2f8b1478ce5f4e83cda78283249e`
- Work issue: `#3`

## Source locks

Geometry:

- John M. Lee, *Introduction to Riemannian Manifolds*, 2nd ed., DOI `10.1007/978-3-319-91755-9`;
- Absil, Mahony, Sepulchre, *Optimization Algorithms on Matrix Manifolds*, ISBN `978-0-691-13298-3`, electronic DOI `10.1515/9781400830244`;
- Edelman, Arias, Smith, *The Geometry of Algorithms with Orthogonality Constraints*, DOI `10.1137/S0895479895290954`;
- Shoemake, *Animating Rotation with Quaternion Curves*, DOI `10.1145/325165.325242`.

Non-normality:

- Horn and Johnson, *Matrix Analysis*, 2nd ed., DOI `10.1017/CBO9781139020411`;
- Trefethen and Embree, *Spectra and Pseudospectra*, DOI record `10.2307/j.ctvzxx9kj`;
- Reddy, Schmid, Henningson, *Pseudospectra of the Orr–Sommerfeld Operator*, DOI `10.1137/0153002`;
- Trefethen, Trefethen, Reddy, Driscoll, *Hydrodynamic Stability Without Eigenvalues*, DOI `10.1126/science.261.5121.578`.

Exact metadata and claim scope are stored in the chapter source-lock manifests.

## Atlas-owned derivations

Geometry packet establishes:

- (T_xS^{d-1}={v:x^	op v=0});
- normalized sphere retraction and its first-order property;
- sphere exponential map versus normalized retraction;
- SLERP unit-norm derivation and antipodal boundary;
- (T_Xmathrm{St}(n,p)={Z:X^	op Z+Z^	op X=0});
- Grassmann as the quotient of Stiefel frames by the right action of (O(p)).

Non-normality packet establishes:

- exact powers of (A=[[a,K],[0,a]]);
- exact singular-value formula for (A^n);
- matched normal comparison;
- exact (2)-norm pseudospectral boundary
  [
  |z-a|^2=arepsilon(arepsilon+K);
  ]
- exact finite-dimensional claim boundaries.

## Wolfram witnesses

Runtime:

- Wolfram Language `15.0.1 for Linux x86 (64-bit) (July 2, 2026)`;
- `$SystemID = Linux-x86-64`;
- `$MaxExtraPrecision = 50`.

Rendered figures:

- `ATLAS-FIG-MANIFOLD-001`
  - source: `figures/wolfram/ATLAS-FIG-MANIFOLD-001.wl`
  - output: `figures/masters/ATLAS-FIG-MANIFOLD-001.png`
  - Git blob: `aded6f0764e04dd17457a71a32cb4a1ae5d42a84`;

- `ATLAS-FIG-PSPECTRUM-001`
  - source: `figures/wolfram/ATLAS-FIG-PSPECTRUM-001.wl`
  - output: `figures/masters/ATLAS-FIG-PSPECTRUM-001.png`
  - Git blob: `b8901f7ef153598e7b6fe60756ef14f808798734`.

For the non-normal example (a=4/5,K=4), Wolfram independently found

[
max_{0le nle40}|A^n|_2
=
8.212429054411118
]

at (n=4), and symbolically verified the pseudospectral-boundary substitution.

## Manuscript drafts

- `manuscript/parts/02-mathematical-substrate/ATLAS-CH-GEOM-001.md`
- `manuscript/parts/02-mathematical-substrate/ATLAS-CH-NONNORMAL-001.md`

Both drafts use the Atlas pattern:

problem → intuition/allegory → formal objects → derivation → computational witness → figure → interpretation → failure boundary → downstream connections.

## Promotion state

Both ledger nodes are promoted from `specification-ready` to `draft-v0.1`.

This means a complete first manuscript pass exists. It does **not** mean copy-edit complete, mathematically certified, or publication-ready.

## Validation

CI is extended so a `draft-v0.1` keystone must bind:

- specification;
- manuscript;
- derivation packet;
- source lock;
- computational witness.

A `rendered-witness` figure must bind:

- Wolfram/source generator;
- rendered image;
- figure manifest;
- runtime version;
- parameters.

## Next phase after merge

1. mathematical/editorial audit of the two drafts;
2. repair any source, derivation, notation, accessibility, or figure defects;
3. then begin the second keystone pair:
   - `ATLAS-CH-ATTNOP-001`;
   - `ATLAS-CH-OPTDYN-001`.

No claim is promoted to theorem or certification status by this tranche.
