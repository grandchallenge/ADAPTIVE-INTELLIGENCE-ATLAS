# Atlas Dependency Graph v0.2

**Status:** refined architecture  
**Canonical hard adjacency:** `CHAPTER_LEDGER.yaml`  
**Semantic supplement:** `DEPENDENCY_GRAPH.yaml`

## Structural audit

The v0.1 graph has:

- 80 chapter nodes;
- 126 hard prerequisite edges;
- one root: `ATLAS-CH-THESIS-001`;
- no directed cycles.

The graph therefore does not need structural repair. The v0.2 refinement adds semantics and drafting consequences.

## Reading rule

A hard dependency means the target chapter may use material from the source without rebuilding it from first principles.

A soft cross-link means the chapters illuminate one another but neither is entitled to assume the other has been read.

This distinction allows the Atlas to support multiple reading paths without allowing hidden prerequisites.

## Keystone cones

### ATLAS-CH-GEOM-001 — Geometry of Constrained State Spaces

Immediate hard prerequisite:

- `ATLAS-CH-LINALG-001` — formal.

Inherited foundation:

- `ATLAS-CH-OBJECTS-001`;
- `ATLAS-CH-THESIS-001`.

Material downstream reach includes representation geometry, normalized representations, quotient geometry, manifold optimization, positional geometry, transport, and the later synthesis programme. It is the most structurally central keystone in the current graph.

Drafting consequence: this chapter must introduce enough manifold geometry to support later chapters without becoming a general differential-geometry textbook.

### ATLAS-CH-NONNORMAL-001 — Normality, Pseudospectra, and Transient Growth

Immediate hard prerequisite:

- `ATLAS-CH-LINALG-001` — formal.

Inherited foundation:

- `ATLAS-CH-OBJECTS-001`;
- `ATLAS-CH-THESIS-001`.

Material downstream reach includes spectral shaping, optimizer-state dynamics, router dynamics, spectral diagnostics, and related stability arguments.

Drafting consequence: the chapter must make the failure of eigenvalue-only intuition mathematically undeniable in a minimal finite-dimensional example before introducing pseudospectral machinery.

### ATLAS-CH-ATTNOP-001 — Attention as an Operator

Immediate hard prerequisites:

- `ATLAS-CH-TRANSFORMER-001` — conceptual/formal;
- `ATLAS-CH-LINALG-001` — formal.

Inherited foundation includes the architecture history and Atlas object taxonomy.

Material downstream reach includes approximate attention, positional geometry, retrieval, mechanistic diagnosis, and later operator-valued position work.

Drafting consequence: the operator viewpoint must be shown to recover ordinary attention exactly before it is used to motivate more speculative operator language.

### ATLAS-CH-OPTDYN-001 — Optimizer-State Dynamics

Immediate hard prerequisites:

- `ATLAS-CH-NONNORMAL-001` — formal;
- `ATLAS-CH-OPTBASE-001` — formal/conceptual.

Its inherited cone includes linear algebra, dynamics, and the Atlas object taxonomy.

Material downstream reach includes coupling-phase spectroscopy, router dynamics, and spectral diagnosis.

Drafting consequence: model parameters and optimizer state must be treated as one coupled state variable before any claims about transient instability are made.

### ATLAS-CH-BCONTRACT-001 — Boundary Contracts

Immediate hard prerequisites:

- `ATLAS-CH-BOUNDARYPROBE-001` — formal;
- `ATLAS-CH-LOCALGLOBAL-001` — conceptual.

Its inherited cone includes linear algebra, numerical schemes, architecture history, and the Atlas interface taxonomy.

Material downstream reach includes composition without catastrophe, frontier synthesis, and governed compositional learning.

Drafting consequence: “contract” must be a mathematical/interface object, not merely a software metaphor. The chapter must expose both semantic and differential/sensitivity obligations.

### ATLAS-CH-REPLAY-001 — Replayable Evidence Objects

Immediate hard prerequisites:

- `ATLAS-CH-EXPERIMENT-001` — methodological;
- `ATLAS-CH-EVIDEX-001` — methodological/conceptual.

Its inherited cone includes evidence classification, coordination, agents, and the Atlas thesis.

Material downstream reach includes formal methods, research state machines, governed adaptation, and final synthesis.

Drafting consequence: replay must be separated from truth, verification, certification, and authority. Reconstructability is necessary for strong scientific handoff but does not itself promote a claim.

## Cross-keystone bridges

The six keystones are deliberately not arranged as a single chain.

Instead they form three paired bridges:

[
\text{Geometry} \leftrightarrow \text{Attention as Operator}
]

Geometry supplies admissible state spaces; attention supplies a concrete operator family acting on learned states.

[
\text{Non-normality} \leftrightarrow \text{Optimizer-State Dynamics}
]

The first supplies the mathematics of transient amplification; the second turns it into a learning-system diagnostic.

[
\text{Boundary Contracts} \leftrightarrow \text{Replayable Evidence}
]

The first governs composition of computational components; the second governs composition of scientific claims and evidence.

These are soft conceptual bridges, not added hard prerequisites.

## Drafting order

The recommended keystone drafting order is:

1. `ATLAS-CH-GEOM-001`
2. `ATLAS-CH-NONNORMAL-001`
3. `ATLAS-CH-ATTNOP-001`
4. `ATLAS-CH-OPTDYN-001`
5. `ATLAS-CH-BCONTRACT-001`
6. `ATLAS-CH-REPLAY-001`

This order is editorial, not mathematical authority. Geometry and non-normality establish the mathematical level; attention and optimizer dynamics demonstrate reinterpretive power; boundary contracts and replay establish the compositional and scientific-governance register.

## Global rule

The graph is a dependency structure, not the book’s narrative. A reader may enter through many chapters. The author must nevertheless never make a chapter depend silently on mathematics or doctrine that the graph does not expose.
