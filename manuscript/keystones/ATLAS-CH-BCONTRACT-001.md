# Keystone Specification — ATLAS-CH-BCONTRACT-001

## Identity

**Title:** Boundary Contracts  
**Part:** Numerical Intelligence and Composition  
**Status:** specification-ready  
**Keystone role:** make interfaces mathematical objects carrying enough information for separately developed components to compose without silent semantic or numerical failure.

## Chapter contract

The chapter must answer:

> what must a component expose at its boundary so that another component can use it without reopening the entire interior?

A boundary contract is not a software API description. It is an explicit set of obligations concerning meaning, admissible inputs/outputs, sensitivities, invariants, error, and interaction.

The chapter should connect local-to-global reasoning with practical JVP/VJP and spectral probes.

## Dependency contract

Immediate hard prerequisites:

- ATLAS-CH-BOUNDARYPROBE-001 — formal;
- ATLAS-CH-LOCALGLOBAL-001 — conceptual.

Inherited cone includes linear algebra, numerical schemes, residual architectures, and the Atlas interface taxonomy.

The chapter may assume Jacobian-vector products, vector-Jacobian products, operator norms, local compatibility, and numerical error concepts. It may not assume the later "Composition Without Catastrophe" synthesis.

## Reader outcome

The reader should be able to:

1. distinguish an interface signature from a boundary contract;
2. state semantic, geometric, differential, and numerical obligations separately;
3. explain why matching tensor shapes is not sufficient for composability;
4. estimate local amplification across a boundary using JVP/VJP machinery;
5. understand the role of separator variables or low-order interface summaries;
6. identify which obligations are local and which require global composition tests;
7. understand the limits of any contract that summarizes a high-dimensional component.

## Formal spine

### Minimal component model

Let

\[
y=f(x;\theta)
\]

be one component and

\[
z=g(y;\phi)
\]

a downstream component.

A boundary contract \(C_f\) should be introduced as a structured object containing selected obligations, for example:

\[
C_f=(\mathcal X,\mathcal Y,\sigma,\mathcal I,\mathcal S,\mathcal E),
\]

where the components represent admissible domains/codomains, semantic interpretation, invariants, sensitivity information, and error statements.

The precise tuple is provisional until the chapter's source and GCL machinery are reconciled; the manuscript must not present it as a universal standard merely because it is useful here.

### Core obligations

Develop four classes:

1. **semantic** — what the state means;
2. **geometric** — which constraints or equivalence classes are admissible;
3. **differential** — how perturbations and gradients cross the boundary;
4. **numerical** — error, conditioning, stability, and precision assumptions.

### Boundary probes

Use

\[
J_f(x)v
\]

and

\[
J_f(x)^\top u
\]

to show directional forward and reverse sensitivities.

Use power iteration only with explicit assumptions and state what quantity is being estimated.

### Composition question

For \(g\circ f\),

\[
J_{g\circ f}(x)=J_g(f(x))J_f(x).
\]

This elementary identity should anchor the discussion of local amplification and why compatible-looking modules can become badly conditioned together.

## Principal intuition device

### Allegory: the engineered flange

Two machines can be connected only if more than their bolt patterns match. The interface must specify what loads, tolerances, directions, and operating conditions can safely cross the joint.

Structural correspondence:

- bolt geometry ↔ shape/type compatibility;
- load direction ↔ perturbation direction;
- tolerance ↔ numerical/error budget;
- rated load ↔ sensitivity bound;
- fluid/electrical convention ↔ semantic interpretation.

Limit of allegory:

Learned systems need not obey fixed mechanical constitutive laws, and their interface behavior can be state-dependent. The flange is a mnemonic for explicit obligations, not a claim of mechanical equivalence.

## Working example

Use two small learned or analytic maps whose tensor dimensions match but whose scale/semantics do not.

Example structure:

- \(f\) produces a normalized direction;
- \(g\) interprets magnitude as meaningful.

The composition is shape-compatible but semantically incompatible.

A second example should show numerical compatibility failure through Jacobian amplification.

## Figure programme

### ATLAS-FIG-BCONTRACT-001 — Interface sensitivity and boundary contract

Required elements:

- upstream component;
- boundary variables;
- downstream component;
- semantic obligations;
- JVP/VJP channels;
- local amplification indicator;
- explicit label that flange imagery is schematic.

Optional Wolfram inset: singular-value field or directional-gain surface across a toy boundary.

## Computational witnesses

1. exact Jacobian-chain calculation;
2. JVP/VJP agreement check;
3. power-iteration estimate versus exact singular value on a small matrix;
4. counterexample where individually bounded maps compose to an undesirable gain under chosen conditions;
5. separator-variable example showing what is lost by too-aggressive interface compression.

## Failure boundaries

The chapter must say:

- a contract is only as strong as the properties it records;
- local sensitivity bounds do not automatically imply global stability;
- interface summaries can erase important state;
- shape/type agreement does not establish semantic agreement;
- power iteration is an estimate with convergence conditions;
- a boundary contract is not a mathematical certificate unless its obligations and support route warrant that status.

## GCL connection

The chapter may use MODULUS/BoundaryContract/SeparatorCompiler as a concrete GCL research programme example, but must preserve the distinction between:

- Atlas definition;
- project implementation;
- experimentally observed behavior;
- proved mathematical property.

The project slogan "Modula tells the optimizer how to move. Boundary contracts tell the system how to compose." may be used as a pedagogical bridge only if its status is clearly rhetorical.

## Downstream obligations

Provides the core interface language for:

- ATLAS-CH-COMPOSE-001;
- ATLAS-CH-FRONTIER-001;
- compositional optimization and verification discussions.

## Source-lock plan

Before review-ready drafting, source-lock:

- numerical sensitivity/conditioning references;
- automatic differentiation/JVP/VJP references;
- local-to-global/sheaf references used materially;
- exact GCL MODULUS source state for project-specific examples.

## Acceptance criteria

The drafted chapter must include:

- a formal provisional contract object;
- separate semantic/geometric/differential/numerical obligations;
- one shape-compatible but semantically incompatible example;
- one sensitivity/composition calculation;
- the flange allegory with explicit limits;
- a project-example provenance boundary;
- no claim that local contracts automatically guarantee global safety.
