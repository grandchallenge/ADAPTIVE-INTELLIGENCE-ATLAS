# KEYSTONE-001 — Dependency Refinement and Keystone Specifications

## Status

**Tranche state:** implemented on branch pending merge validation.

## Scope

This tranche executes the first substantive phase after `atlas-v0.1-architecture`:

1. refine the chapter dependency graph;
2. specify the six keystone chapters that establish the Atlas mathematical, interpretive, compositional, and evidentiary standard.

## Baseline

- architecture tag: `atlas-v0.1-architecture`;
- baseline commit: `4300108c51c029b27ecc8596d51c0f0846dcfd69`;
- baseline graph: 80 nodes, 126 hard edges, one root, acyclic.

## Dependency refinement

Added:

- `governance/DEPENDENCY_GRAPH.md`;
- `governance/DEPENDENCY_GRAPH.yaml`;
- `governance/decisions/ADR-0004-dependency-semantics.md`.

The existing Chapter Ledger remains canonical for hard adjacency. The supplement distinguishes formal, conceptual, methodological, and synthesis roles where useful and records non-blocking soft cross-links separately.

## Keystone specifications

The following chapters are now `specification-ready`:

- `ATLAS-CH-GEOM-001` — Geometry of Constrained State Spaces;
- `ATLAS-CH-NONNORMAL-001` — Normality, Pseudospectra, and Transient Growth;
- `ATLAS-CH-ATTNOP-001` — Attention as an Operator;
- `ATLAS-CH-OPTDYN-001` — Optimizer-State Dynamics;
- `ATLAS-CH-BCONTRACT-001` — Boundary Contracts;
- `ATLAS-CH-REPLAY-001` — Replayable Evidence Objects.

Each specification declares:

- dependency contract;
- reader outcome;
- formal or documentary spine;
- principal allegory and its limit;
- figure programme;
- Wolfram/computational witness obligations;
- counterexamples and failure boundaries;
- downstream obligations;
- source-lock plan;
- chapter acceptance criteria.

## Drafting order

Recommended editorial order:

1. Geometry;
2. Non-normality;
3. Attention as an Operator;
4. Optimizer-State Dynamics;
5. Boundary Contracts;
6. Replayable Evidence Objects.

This is an editorial sequence, not an additional hard dependency chain.

## Validation obligations

CI now checks:

- uniqueness of chapter IDs;
- resolution of hard dependencies;
- acyclicity of the hard dependency graph;
- graph audit counts;
- semantic hard-edge annotations against canonical adjacency;
- soft-link chapter identities;
- existence of every specification-ready keystone file;
- figure and source registry integrity.

## Next executable phase

For each keystone, source-lock the primary/canonical external literature and exact GCL project sources needed by its specification. Then draft the first two chapters, Geometry and Non-normality, as the style-setting mathematical pair, including their first Wolfram computational witnesses.

No chapter is promoted beyond specification-ready merely because this tranche merges.
