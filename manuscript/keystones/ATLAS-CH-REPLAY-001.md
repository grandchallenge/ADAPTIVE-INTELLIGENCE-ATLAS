# Keystone Specification — ATLAS-CH-REPLAY-001

## Identity

**Title:** Replayable Evidence Objects  
**Part:** Scientific Method, Governed Adaptation, and Frontier Synthesis  
**Status:** specification-ready  
**Keystone role:** establish the documentary and computational structure required for another competent actor to reconstruct why a claim is believed.

## Chapter contract

The chapter must make one distinction repeatedly and unambiguously:

> replayability is a property of the evidence path; truth, verification, certification, and authority are separate properties.

A replayable evidence object should bind the identity of the claim, sources, derivations or code, environment, observations, interpretation, and review status strongly enough that another actor can reconstruct the support route.

The chapter should turn documentary provenance from administrative metadata into a scientific object.

## Dependency contract

Immediate hard prerequisites:

- ATLAS-CH-EXPERIMENT-001 — methodological;
- ATLAS-CH-EVIDEX-001 — methodological/conceptual.

Inherited cone includes evidence classification, agent coordination, the Atlas map, and the book's object taxonomy.

The chapter may assume baseline scientific-method concepts, provenance-aware handoffs, and bounded work packages. It may not assume formal verification or MATHCERT certification.

## Reader outcome

The reader should be able to:

1. distinguish reproducibility, replay, independent reproduction, formal verification, and certification;
2. identify the minimum identity information required for a replayable result;
3. explain why mutable URLs and unpinned environments weaken provenance;
4. construct a content-addressed evidence chain;
5. separate observation from interpretation;
6. state what a successful replay establishes and what it does not;
7. understand why independent actors change epistemic status only when their independence and support route are themselves recorded.

## Formal/documentary spine

### Evidence object

Introduce a provisional structured object such as

\[
E=(C,S,M,A,O,I,R),
\]

where:

- \(C\): claim identity and exact wording;
- \(S\): source identities;
- \(M\): method, derivation, code, or proof object;
- \(A\): execution environment and artifact identities;
- \(O\): observations/results;
- \(I\): interpretation and claim boundary;
- \(R\): review/replay/certification records.

The tuple is an Atlas explanatory model, not a universal institutional schema.

### Identity discipline

Explain:

- immutable commit/blob/content hashes;
- environment/version locks;
- dataset identities;
- deterministic versus stochastic replay;
- random seeds and why a seed is not a complete environment;
- semantic identity versus byte identity.

### Support classes

Use the inherited GCL distinction among exploratory evidence, regression audit, exact finite verification, certificate replay, formal proof, and continuum proof where appropriate, preserving the exact current source wording when quoted or normatively inherited.

## Principal intuition device

### Allegory: the chain of custody

A scientific claim resembles an exhibit only in one structural sense: its identity and transformation history must remain traceable.

Structural correspondence:

- evidence label ↔ stable artifact identity;
- custody record ↔ provenance chain;
- laboratory procedure ↔ replay method;
- analyst conclusion ↔ interpretation;
- court judgment ↔ review/certification decision.

Limit of allegory:

Scientific truth is not determined by legal procedure, and institutional acceptance is not equivalent to mathematical truth. The analogy is solely about traceable custody and transformation.

## Figure programme

### ATLAS-FIG-REPLAY-001 — From source to replayable evidence object

Render an exact provenance graph:

\[
\text{source}
\to
\text{derivation/method}
\to
\text{execution}
\to
\text{observation}
\to
\text{interpretation}
\to
\text{claim}
\to
\text{review state}.
\]

The visual must distinguish evidence edges from authority/promotion edges.

Primary representation class: exact, provided the graph is generated from the recorded manifest.

## Computational/documentary witnesses

1. a tiny deterministic calculation with source hash, code hash, environment record, output hash, and replay command;
2. the same example with one mutable dependency intentionally changed, showing replay failure;
3. a stochastic example showing why seed + code is not necessarily enough;
4. a content-addressed figure regeneration example;
5. a semantic-bridge example where byte-exact replay does not validate the intended human claim because the formal/computational statement was narrower.

## Counterexamples and failure boundaries

The chapter must include:

- a perfectly replayable incorrect program;
- a non-replayable but mathematically correct handwritten argument;
- a formal proof of the wrong formalized statement;
- an exact finite verification improperly generalized to a continuum claim;
- a successful internal replay that is not independent reproduction.

These counterexamples are central to the chapter.

## GCL institutional example

The chapter may use the GCL Forge → Solve → Cert separation and OPENMATH-style replay lifecycle as a concrete example of role separation.

It must explicitly state that the Atlas is describing a GCL process, not claiming that one governance system is universally optimal.

Exact GCL doctrine must be source-locked to the repository state actually cited.

## Downstream obligations

Provides the documentary language for:

- ATLAS-CH-FORMAL-001;
- ATLAS-CH-RESEARCHSM-001;
- ATLAS-CH-GOVADAPT-001;
- final Atlas synthesis.

## Source-lock plan

Before review-ready drafting, source-lock:

- current GCL technical-writing/pedagogy/provenance doctrine;
- relevant reproducible-science references;
- software/environment reproducibility references;
- formal-verification references only where needed to distinguish replay from proof;
- exact GCL pipeline records for institutional examples.

## Acceptance criteria

The drafted chapter must:

- define a replayable evidence object without confusing it with truth;
- include at least three counterexamples separating replay from stronger epistemic states;
- provide one complete tiny replay package;
- show semantic-bridge failure explicitly;
- render the provenance graph from recorded data;
- preserve exact institutional scope for GCL examples;
- end with the acceptance test:

> Can another competent actor reconstruct why we believe this, and can they see exactly what that reconstruction does not establish?
