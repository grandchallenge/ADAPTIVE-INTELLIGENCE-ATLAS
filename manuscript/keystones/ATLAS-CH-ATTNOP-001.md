# Keystone Specification — ATLAS-CH-ATTNOP-001

## Identity

**Title:** Attention as an Operator  
**Part:** Attention, Sequence, and Position  
**Status:** specification-ready  
**Keystone role:** provide the Atlas’s canonical example of the shift from vectors and score maps to state-dependent operators.

## Chapter contract

Begin from ordinary scaled dot-product attention and recover it exactly before changing viewpoint.

The central move is:

> Attention is not merely a matrix to visualize; it is a state-dependent operator that transports and mixes information.

The operator language must clarify computation rather than replace standard notation with abstraction.

## Dependency contract

Immediate hard prerequisites:

- \`ATLAS-CH-TRANSFORMER-001\` — conceptual/formal;
- \`ATLAS-CH-LINALG-001\` — formal.

The chapter may assume conventional \(Q,K,V\) construction and linear algebra. It may not assume relative-position operators, kernel approximation, or mechanistic diagnosis.

## Reader outcome

The reader should be able to:

1. derive scaled dot-product attention;
2. distinguish score matrix, normalized operator, value field, and full map;
3. express one head as a state-dependent linear operator on values conditional on \(Q,K\);
4. explain row-stochasticity under ordinary softmax;
5. identify what is nonlinear in the full self-attention map;
6. use kernel intuition without overstating equivalence;
7. understand why the operator view helps later work on approximation, position, retrieval, and intervention.

## Formal spine

Start with

\[
Q=XW_Q,\qquad
K=XW_K,\qquad
V=XW_V,
\]

\[
S(X)=\frac{QK^\top}{\sqrt{d_k}},
\]

\[
A(X)=\operatorname{softmax}_{\rm row}(S(X)),
\]

and

\[
Y=A(X)V.
\]

Keep distinct:

- \(S(X)\): score matrix;
- \(A(X)\): normalized mixing operator;
- \(V(X)\): value field;
- \(F(X)=A(X)V(X)\): full nonlinear transformation.

Core results:

1. for fixed \(Q,K\), \(V\mapsto AV\) is linear;
2. ordinary softmax rows form probability simplices;
3. causal masking constrains operator support;
4. permutation behavior must be stated with position/mask assumptions;
5. multihead attention is a family of state-dependent operators.

## Principal intuition device

### Allegory: a dynamic switching board

The state configures a switching board that determines how value streams are mixed.

Structural correspondence:

- switch configuration ↔ attention weights;
- incoming channels ↔ value vectors;
- state-dependent configuration ↔ \(A(Q,K)\);
- mixed output ↔ \(AV\).

Limit of allegory:

Attention is differentiable weighted mixing, not discrete electrical switching.

## Figure programme

### ATLAS-FIG-ATTNOP-001

Show coordinated views of:

1. scores \(S\);
2. normalized operator \(A\);
3. value field \(V\);
4. output \(AV\).

Numeric labels must make color redundant.

## Wolfram witnesses

1. exact/small \(Q,K,V\) example;
2. row-sum verification;
3. query perturbation and operator change;
4. fixed-\(A\) linearity in \(V\);
5. optional spectral/singular analysis with qualified interpretation.

## Failure boundaries

State explicitly:

- an attention map is not an explanation by itself;
- \(A\) is input-dependent;
- operator language does not make the full map linear in \(X\);
- row-stochasticity does not make the whole layer a Markov chain;
- kernel analogies require assumptions;
- weights are not automatically feature importance.

## Downstream obligations

Provide notation and viewpoint for:

- \`ATLAS-CH-ATTNAPPROX-001\`;
- \`ATLAS-CH-POSGEOM-001\`;
- \`ATLAS-CH-RPO-001\`;
- \`ATLAS-CH-RETRIEVAL-001\`;
- \`ATLAS-CH-MECHDIAG-001\`.

## Source-lock plan

Source-lock:

- the original Transformer formulation;
- a peer-reviewed kernel interpretation where used;
- canonical linear-attention work;
- separate mechanistic-interpretability sources for causal claims.

## Acceptance criteria

The draft must:

- recover conventional attention exactly before abstraction;
- formalize the fixed-\(Q,K\) operator action;
- demonstrate full-state nonlinearity;
- include an exact toy computational witness;
- preserve the switching-board allegory and its limit;
- preserve the boundary between visualization and causal explanation.
