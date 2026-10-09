# Chapter Specification — ATLAS-CH-THESIS-001

## Identity

**Title:** A Mathematical Atlas, by Choice  
**Part:** Orientation  
**Status:** specification-ready  
**Epistemic class:** Atlas synthesis.

## Chapter contract

Introduce the opinionated perspective of a mathematical atlas without presenting one editorial preference as an Atlas-wide theorem:

> The Atlas selects mathematical viewpoints for the questions they illuminate. Geometry, operators, dynamics, memory, interfaces, evidence, and governance are recurring routes, not a unified ontology or an obligatory proof objective.

The chapter must make clear that chosen lenses illuminate different problems, and no later chapter owes a proof of the perspective.

## Dependency contract

No hard prerequisite.

The chapter may name later objects but must not assume their mathematics.

## Reader outcome

A reader should be able to:

1. describe the Atlas's selectively opinionated mathematical viewpoints;
2. distinguish a model from the larger adaptive system in which it participates;
3. explain the recurring shifts vectors→operators, layers→flows, context→compiled memory access, agents→distributed systems, and results→evidence objects;
4. distinguish descriptive claims about current ML systems from the Atlas programme;
5. understand why the book is organized by dependency rather than by a list of ML methods.

## Formal/documentary spine

Introduce only the minimum stable vocabulary:

- state;
- operator;
- dynamics/flow;
- memory;
- interface/contract;
- evidence object;
- governance.

Do not attempt to fully define these here; hand off exact definitions to `ATLAS-CH-OBJECTS-001` and later chapters.

## Principal pedagogical device

### Allegory: an atlas, not a catalogue

A catalogue lists objects. An atlas gives coordinate systems, local maps, overlaps, routes, and known blank regions.

Correspondence:

- entries ↔ isolated methods;
- charts ↔ mathematical viewpoints;
- overlaps ↔ compositional consistency;
- routes ↔ dependency paths;
- blank regions ↔ open problems.

Limit:

The research territory is not static geography. The map changes when new methods and evidence appear.

## Documentary witness

Construct a table mapping the source inventory's recurring shifts to later Atlas Parts and exact chapter IDs.

## Counterexamples and failure boundaries

Include:

- a large model that is not itself a complete adaptive system;
- a governance process that does not create mathematical truth;
- an external memory system whose capability is not located solely in model weights.

## Downstream obligations

Supply orientation and vocabulary to every chapter, directly or transitively.

Immediate hard consumer:

- `ATLAS-CH-OBJECTS-001`.

## Source lock

`sources/source-locks/ATLAS-CH-THESIS-001.yaml`.

## Acceptance

The draft must:

- label the thesis as Atlas synthesis;
- avoid pretending the thesis is proved by examples;
- expose the monograph's dependency-led structure;
- state the main conceptual spine;
- include the atlas allegory and its limit;
- identify what later chapters must establish for the thesis to become credible.
