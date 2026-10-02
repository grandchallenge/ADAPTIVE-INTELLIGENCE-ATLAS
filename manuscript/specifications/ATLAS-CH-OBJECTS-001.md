# Chapter Specification — ATLAS-CH-OBJECTS-001

## Identity

**Title:** States, Operators, Flows, and Interfaces  
**Part:** Orientation  
**Status:** specification-ready  
**Epistemic class:** Atlas synthesis with standard mathematical instances.

## Chapter contract

Introduce the four recurring object roles used across the Atlas:

1. states;
2. operators;
3. flows/dynamics;
4. interfaces/contracts.

The chapter teaches category-error avoidance. The same array shape may represent different mathematical objects; the role is determined by semantics and transformation law, not storage layout.

## Dependency contract

Hard prerequisite:

- `ATLAS-CH-THESIS-001`.

May not assume linear algebra beyond elementary vector/matrix notation.

## Reader outcome

A reader should be able to:

- distinguish a state from an operator acting on states;
- distinguish one operator application from a flow/evolution;
- distinguish an interface contract from the component interior;
- identify when one object changes role under a different model;
- read later Atlas notation without collapsing all tensors into “representations.”

## Formal spine

Use typed maps:

[
xinmathcal X,
qquad
F:mathcal X	omathcal Y,
qquad
Phi_t:mathcal X	omathcal X,
]

and a provisional interface declaration

[
C_F=(	ext{domain},	ext{codomain},	ext{semantics},	ext{obligations}).
]

The chapter does not need category theory.

## Principal pedagogical device

### Allegory: noun, verb, motion, handshake

- state ↔ noun;
- operator ↔ verb;
- flow ↔ unfolding motion;
- interface ↔ handshake between systems.

Limit:

Mathematical objects can play multiple roles and natural language grammar is not a formal ontology.

## Working counterexamples

- a square matrix used once as a state versus used as a linear operator;
- a Transformer residual block versus the depth-indexed sequence it induces;
- an API shape signature that composes while semantics do not.

## Witness

A small typed table classifying identical-shaped arrays under different meanings.

## Downstream obligations

Direct consumers include:

- `ATLAS-CH-LINALG-001`;
- `ATLAS-CH-INFO-001`;
- later architecture, dynamics, memory, and boundary-contract chapters.

## Source lock

`sources/source-locks/ATLAS-CH-OBJECTS-001.yaml`.

## Acceptance

The draft must include:

- stable project-local definitions;
- at least three category-error counterexamples;
- explicit statement that the taxonomy is explanatory, not universal;
- handoff to Linear Algebra and Information without importing their later machinery.
