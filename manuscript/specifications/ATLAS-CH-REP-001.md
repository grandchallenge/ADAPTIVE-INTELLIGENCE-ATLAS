# Chapter Specification — ATLAS-CH-REP-001

## Identity

**Title:** Representations and Invariants  
**Part:** Representation Learning  
**Status:** specification-ready.

## Chapter contract

Develop representations as information-bearing encodings whose usefulness depends on geometry, invariances, equivalences, and downstream computation.

The chapter should move the reader from “a representation is a vector” to “a representation is a structured encoding whose transformation laws matter.”

## Dependency contract

Hard prerequisites:

- `ATLAS-CH-INFO-001`;
- `ATLAS-CH-GEOM-001`.

Inherited:

- `ATLAS-CH-LINALG-001`;
- `ATLAS-CH-OBJECTS-001`;
- `ATLAS-CH-THESIS-001`.

## Reader outcome

A reader should be able to:

1. distinguish representation, state, coordinate system, and semantics;
2. define invariance and equivariance under a group action;
3. explain representation equivalence under invertible recoding when downstream computation transforms consistently;
4. explain why identifiability requires assumptions;
5. interpret sparsity and feature dictionaries;
6. understand superposition only at the bounded toy-model/research-evidence level used here;
7. identify the handoff to normalized and quotient representations.

## Formal spine

Let a representation map be

[
r:mathcal X	omathcal Z.
]

For group (G) acting on inputs and representation space, define:

invariance

[
r(gcdot x)=r(x),
]

and equivariance

[
r(gcdot x)=ho(g)r(x).
]

Introduce representation equivalence through an invertible recoding

[
	ilde r = Tcirc r
]

when downstream maps transform compatibly.

Do not identify coordinate equality with representational equivalence.

## Principal pedagogical device

### Allegory: languages that preserve the same message

Two encodings can differ symbol-by-symbol yet support the same downstream distinctions.

Limit:

Natural-language translation is not a formal proof of invertible or task-preserving equivalence.

## Exact examples

Include:

- rotation-equivariant 2D vector;
- invariant norm;
- two representations related by an invertible basis change;
- sparse dictionary representation;
- non-identifiable latent factors under unconstrained invertible mixing.

## Computational witness

A small exact group-action example verifying invariance/equivariance and a recoding example where downstream predictions are unchanged after transforming the readout.

## Counterexamples and failure boundaries

- invariance can erase information needed downstream;
- equivariance is relative to specified group actions;
- unsupervised disentanglement is not assumed identifiable without inductive bias [@LocatelloEtAl2019];
- sparse features need not be unique;
- superposition evidence is bounded to toy/research models, not a universal theorem about all networks.

## Source roles

Representation-learning overview: [@BengioCourvilleVincent2013].

Concrete equivariant architecture: [@CohenWelling2016].

Identifiability limit: [@LocatelloEtAl2019].

Sparse coding historical example: [@OlshausenField1996].

Toy-model superposition programme evidence: [@ElhageEtAl2022Superposition].

Source lock: `sources/source-locks/ATLAS-CH-REP-001.yaml`.

## Downstream obligations

Primary consumers:

- `ATLAS-CH-NORMREP-001`;
- `ATLAS-CH-QUOTIENT-001`;
- later Residual/transfer branches.

## Acceptance

The draft must preserve the distinctions:

- coordinates ≠ semantics;
- invariance ≠ equivariance;
- representation quality ≠ identifiability;
- toy superposition evidence ≠ universal empirical prevalence.
