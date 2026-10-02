# Keystone Specification — ATLAS-CH-ATTNOP-001

## Identity

**Title:** Attention as an Operator  
**Part:** Attention, Sequence, and Position  
**Status:** specification-ready  
**Keystone role:** provide the Atlas’s canonical example of the shift from vectors and tables of scores to state-dependent operators.

## Chapter contract

The chapter must begin from ordinary scaled dot-product attention and recover it exactly. Only then may it change viewpoint.

The central move is:

> attention is not merely a matrix to visualize; it is a state-dependent operator that transports and mixes information.

The operator language must clarify computation rather than replace standard notation with abstraction.

## Dependency contract

Immediate hard prerequisites:

- `ATLAS-CH-TRANSFORMER-001` — conceptual/formal;
- `ATLAS-CH-LINALG-001` — formal.

Inherited cone includes architecture history, object taxonomy, and the Atlas thesis.

The chapter may assume conventional (Q,K,V) construction and linear algebra. It may not assume relative-position operators, kernel approximation, or mechanistic diagnosis.

## Reader outcome

The reader should be able to:

1. derive scaled dot-product attention from (Q,K,V);
2. distinguish the score matrix from the normalized attention operator and from the value transformation;
3. express one attention head as a state-dependent linear operator on the value field conditional on (Q,K);
4. explain row-stochastic structure under softmax;
5. identify what is nonlinear in the full attention map;
6. connect attention to kernels and integral-operator intuition without falsely claiming equivalence in every setting;
7. understand why this viewpoint helps later analysis of approximation, position, retrieval, and intervention.

## Formal spine

Start with

[
Q=XW_Q,qquad K=XW_K,qquad V=XW_V,
]

and

[
A(X)=operatorname{softmax}!left(rac{QK^	op}{sqrt{d_k}}ight).
]

Then

[
Y=A(X)V.
]

The chapter should distinguish:

- (S(X)=QK^	op/sqrt{d_k}): score operator/matrix;
- (A(X)): normalized mixing operator;
- (V): transformed value field;
- (Xmapsto A(X)V(X)): the full nonlinear attention transformation.

This distinction is essential. Calling the entire attention layer “linear” would be false because the operator depends on the state.

## Core results and observations

Establish or derive:

1. for fixed (Q,K), (Vmapsto A V) is linear;
2. softmax attention rows form probability simplices under ordinary row-wise softmax;
3. causal masking changes the admissible operator structure;
4. permutation behavior should be stated carefully with or without position information;
5. multihead attention is not merely “several maps”; it is a collection of separately parameterized state-dependent operators whose outputs are recombined.

The chapter should distinguish exact algebra from interpretive operator language.

## Principal intuition device

### Allegory: a dynamic switching board

Each token emits a query; the current state configures a switching board that determines how value streams are mixed.

Structural correspondence:

- switch configuration ↔ attention weights;
- incoming channels ↔ value vectors;
- state-dependent configuration ↔ dependence of (A) on (Q,K);
- mixed output ↔ (AV).

Limit of allegory:

Attention is differentiable weighted mixing, not discrete circuit switching, and multihead structure is not literally a bank of physical wires.

## Figure programme

### ATLAS-FIG-ATTNOP-001 — Attention as a state-dependent operator

The figure should have three coordinated views:

1. scores (S);
2. normalized operator (A);
3. action (Vmapsto AV).

A small toy sequence should permit exact numerical inspection.

Representation class: `data-derived`.

A second schematic may show how (X) changes both the operator and the values, making the full transformation nonlinear.

## Wolfram computational witnesses

1. exact small-matrix (Q,K,V) example with rational or simple algebraic inputs where feasible;
2. row-sum verification for softmax weights;
3. perturb one query and show the induced change in the operator;
4. hold (A) fixed and verify linearity in (V);
5. optional spectral/singular analysis of (A) with explicit warning that interpretation depends on structure and norm.

## Failure boundaries

The chapter must explicitly state:

- an attention map is not an explanation by itself;
- (A) is not fixed independently of input;
- operator language does not imply the operator is linear in the original hidden state;
- stochastic-matrix intuition is useful but does not capture learned value transformations;
- kernel analogies require explicit assumptions;
- head weights should not automatically be interpreted as feature importance.

## Downstream obligations

This chapter must supply notation and viewpoint for:

- `ATLAS-CH-ATTNAPPROX-001`;
- `ATLAS-CH-POSGEOM-001`;
- `ATLAS-CH-RPO-001`;
- `ATLAS-CH-RETRIEVAL-001`;
- `ATLAS-CH-MECHDIAG-001`.

The operator distinction (S) versus (A) versus full (Xmapsto Y) should remain stable across those chapters.

## Source-lock plan

Before review-ready drafting, source-lock:

- the original Transformer attention formulation;
- canonical sources for kernel interpretations if used;
- primary sources for sparse/linear attention only where previewed;
- separate sources for any claim about mechanistic interpretation.

## Acceptance criteria

The drafted chapter must:

- recover conventional attention exactly before abstraction;
- formalize the fixed-(Q,K) operator action;
- show full-state nonlinearity;
- include an exact toy computational witness;
- contain the switching-board allegory and its limit;
- preserve a strict boundary between attention visualization and causal explanation.
