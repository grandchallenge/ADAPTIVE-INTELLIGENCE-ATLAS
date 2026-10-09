# Atlas Chapter Composition Protocol

**Protocol ID:** `GCL-ATLAS-CHAPTER-001`  
**Status:** canonical project-local authoring protocol  
**Derived from:** six audited keystone drafts, 2026-10-02

## Purpose

This protocol records the composition grammar demonstrated by the six Atlas keystones. It is not a demand that every chapter use identical headings or equal amounts of mathematics. It defines the **functions** a mature Atlas chapter should perform.

The guiding rule is:

> make the object visible, make the mathematics exact, make the evidence reconstructable, and make the claim boundary explicit.

## Concept-first chapter freedom

The Atlas follows an Axler-inspired pedagogical preference: lead with the mathematical question and a revealing example; introduce abstraction when it solves a visible problem; prove what needs proof; use counterexamples, exercises, and figures to make structure intelligible. This is not a requirement to imitate another author's style or exclusions.

The ten functions below need not appear as ten headings or as administrative prose in the reader-facing book. The Atlas is opinionated, not thesis-driven. A chapter can be excellent without contributing toward a book-wide architecture theorem. Reader comprehension, precise hypotheses, well-chosen examples and mathematical insight govern editorial acceptance.

## Default chapter grammar

### 1. Opening problem

Begin with the obstruction, tension, or question that makes the chapter necessary.

The reader should understand the problem before being asked to absorb the full formalism.

Preferred opening forms include:

- a minimal counterexample;
- a concrete failure mode;
- a geometric tension;
- an apparently reasonable statement that later proves incomplete;
- a compositional or evidentiary mismatch.

### 2. Bounded pedagogical device

Use an allegory, toy system, or visual analogy when it reveals structure.

If an allegory is used, the chapter must expose:

1. the structural correspondence;
2. the point at which the correspondence fails.

The required sequence is:

allegory -> structural mapping -> mathematics -> limit of allegory.

An allegory must never carry a claim that the mathematics does not support.

### 3. Formal or documentary object

Introduce the smallest formal object that resolves the opening problem.

Examples established by the keystones include:

- tangent space and retraction;
- non-normal operator and pseudospectrum;
- state-dependent attention operator;
- augmented optimizer state;
- boundary contract;
- replayable evidence object.

Definitions should be stable enough for downstream chapters to consume.

### 4. Exact derivation or reconstruction

Every load-bearing mathematical claim should have one of:

- a derivation in the chapter;
- a linked derivation packet;
- a source-locked theorem/result;
- a machine-checkable proof object;
- an exact documentary reconstruction.

Toy examples are encouraged when they expose the mechanism completely.

### 5. Computational witness

Use a computational witness when symbolic, numerical, graphical, finite-search, or replay machinery materially strengthens the exposition.

A witness must remain bounded to what it actually establishes.

A witness is not promoted to proof merely because it is exact or reproducible.

### 6. Figure with semantics

A governed figure must declare:

- representation class;
- literal semantics;
- nonliteral semantics;
- support role;
- generator/runtime where applicable;
- exact source and rendered identities where applicable;
- claim boundary.

Color, layout, perspective, marker choice, or line style must not silently carry mathematical meaning unless explicitly declared.

### 7. Counterexamples and failure boundaries

A mature chapter should say how its central idea can be misused.

Preferred forms include:

- smallest counterexample;
- false converse;
- local-versus-global failure;
- mechanism-versus-prevalence distinction;
- exact-versus-approximate distinction;
- identity-versus-semantics distinction;
- evidence-versus-authority distinction.

The chapter should teach not only what the object can do, but what it cannot justify.

### 8. Downstream handoff

State which later chapters consume the chapter's notation, results, or viewpoint.

A handoff should answer:

> What may a later chapter now assume without rebuilding this material?

Hard prerequisites remain canonical in `CHAPTER_LEDGER.yaml`. Soft conceptual bridges remain non-blocking.

### 9. Source lock and provenance

A load-bearing external or project-specific claim must be source-locked at the strength required by the claim.

Project memory, conversation memory, mutable URLs, and unsourced recollection may motivate research, but must not be presented as public documentary evidence.

### 10. Epistemic status and promotion

Every mature chapter must expose its epistemic status.

Presentation quality does not promote evidence.

A chapter may contain several support classes at once, but the reader must be able to distinguish:

- established external theory;
- Atlas-owned derivation or synthesis;
- computational witness;
- empirical observation;
- GCL public project evidence;
- GCL programme context;
- conjecture;
- open problem;
- institutional status.

## Optional elements

Not every chapter needs:

- a bespoke allegory;
- a Wolfram figure;
- a new theorem;
- a GCL case study;
- an executable witness.

These are used when they improve understanding or evidentiary strength.

What is not optional is the distinction among object, support route, interpretation, and claim boundary.

## Chapter maturity test

A chapter may be considered mature for editorial review when a competent reader can answer:

1. What object is this chapter about?
2. What obstruction motivated it?
3. What may I treat as definition or established result?
4. What did the Atlas derive itself?
5. What did a computational witness actually establish?
6. Which figures are literal and which parts are schematic?
7. Where does the central intuition fail?
8. Which downstream chapters depend on this material?
9. What sources and artifact identities support load-bearing claims?
10. What remains unresolved?

## Keystone precedent

The six style-setting keystones are:

- `ATLAS-CH-GEOM-001`;
- `ATLAS-CH-NONNORMAL-001`;
- `ATLAS-CH-ATTNOP-001`;
- `ATLAS-CH-OPTDYN-001`;
- `ATLAS-CH-BCONTRACT-001`;
- `ATLAS-CH-REPLAY-001`.

They are examples of the protocol, not immutable prose templates.

**Editorial maxim:** rigorous enough to survive inspection; imaginative enough to make the structure visible.
