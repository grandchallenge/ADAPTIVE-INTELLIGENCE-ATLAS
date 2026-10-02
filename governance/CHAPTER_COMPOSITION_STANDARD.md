# Atlas Chapter Composition Standard

**Standard ID:** GCL-ATLAS-COMPOSE-001  
**Version:** 1.0.0  
**Status:** project-local authoring standard  
**Derived from:** the six audited keystone drafts and AUDIT-001 through AUDIT-003.

## Purpose

This standard freezes the chapter grammar that survived six deliberately different keystone chapters:

- Geometry of Constrained State Spaces;
- Normality, Pseudospectra, and Transient Growth;
- Attention as an Operator;
- Optimizer-State Dynamics;
- Boundary Contracts;
- Replayable Evidence Objects.

It is a composition grammar, not a rigid section template. Chapters may reorder or omit elements when the subject requires it, but omissions must be deliberate rather than accidental.

The governing test is:

> Does the chapter make the object, the reason for introducing it, the support route, and the boundary of the claim visible?

## 1. Canonical chapter grammar

A mature Atlas chapter should contain the following functions.

### 1. Opening problem

Begin with the obstruction, tension, or conceptual mistake that makes the chapter necessary.

Good openings expose a problem before introducing a vocabulary.

Examples from the keystones include:

- ambient coordinates are not always the admissible state space;
- stable eigenvalues can miss transient amplification;
- an attention matrix is not the same thing as the transformation it performs;
- optimizer state changes the dynamical state space;
- matching tensor dimensions do not establish composability;
- a claim is the end of an evidence path, not the whole path.

### 2. Bounded allegory

When an allegory materially helps, use the sequence:

allegory -> structural correspondence -> mathematics -> explicit limit.

An allegory may clarify structure. It may not carry a theorem.

Every load-bearing allegory must state where it fails.

### 3. Formal or documentary object

Name the mathematical, computational, or documentary object that the chapter will reason about.

Examples:

- tangent space;
- pseudospectrum;
- state-dependent attention operator;
- augmented optimizer state;
- boundary contract;
- replayable evidence object.

The object must be defined before later claims silently depend on it.

### 4. Exact derivation or reconstruction

At least one central claim should be reconstructed in enough detail that the reader can see why it is true or why it is supported.

Possible routes include:

- proof or derivation;
- exact finite calculation;
- symbolic reduction;
- source-locked reconstruction;
- executable replay;
- controlled experiment.

A chapter should not outsource every important step to citations.

### 5. Computational witness

Use a computational witness when symbolic or numerical computation materially reveals the structure.

A witness must be bounded. It should say what it establishes and what it does not establish.

A rendered witness is not a proof merely because it is reproducible.

### 6. Figure with semantic contract

Every governed figure must identify:

- representation class;
- literal semantics;
- nonliteral semantics;
- generator and runtime where applicable;
- source identity;
- rendered identity where applicable;
- claim boundary;
- accessibility text or surrounding prose sufficient to recover the critical distinction without color alone.

### 7. Counterexamples and failure boundaries

A strong Atlas chapter contains at least one place where the reader is shown how the central idea can be misused.

Preferred forms include:

- smallest counterexample;
- degenerate case;
- local-versus-global distinction;
- approximation failure;
- semantic mismatch;
- provenance mismatch;
- correct computation supporting the wrong claim.

### 8. Downstream handoff

End the technical development by showing which later Atlas objects consume the chapter.

A downstream handoff should state what later chapters may now assume.

It should not merely list related topics.

### 9. Source-lock and provenance obligations

Every nontrivial external or project-specific claim must have a recoverable support identity.

The source lock should distinguish:

- canonical external source;
- primary historical source;
- current public GCL project object;
- GCL programme context without current public source;
- Atlas-owned derivation or synthesis;
- computational witness;
- open hypothesis or question.

Do not convert memory, a mutable URL, or a project slogan into documentary evidence.

### 10. Epistemic status and promotion rule

Every mature chapter must make its epistemic status visible.

Presentation does not create status.

A statement may move to a stronger status only when the support route required for that stronger status is present.

## 2. The recurring explanatory arc

The preferred default arc is:

problem -> intuition -> object -> derivation -> witness -> interpretation -> failure boundary -> Atlas connection.

This is deliberately not:

definition -> theorem -> proof -> next definition

for every chapter.

The Atlas is a monograph with a thesis. Formal mathematics should arrive when it resolves a visible problem.

## 3. Allegory doctrine

Allegories are first-class pedagogical tools when they preserve structural correspondence.

Use four explicit elements:

1. named allegory;
2. mapping from allegory to mathematical structure;
3. mathematical replacement;
4. stated failure boundary.

Examples established by the keystones:

- cartographer and mountain -> ambient versus admissible geometry;
- aligned currents -> non-normal transient amplification;
- dynamic switching board -> state-dependent attention mixing;
- flywheel -> optimizer memory as dynamical state;
- engineered flange -> multidimensional interface obligations;
- chain of custody -> provenance and evidence lineage.

Do not reuse an allegory after the mathematics has made it unnecessary unless it still compresses a real structural relation.

## 4. Mathematical rigor doctrine

The minimum mathematical standard is not maximal abstraction. It is explicitness.

For every substantial derivation, declare as applicable:

- domain and codomain;
- assumptions;
- norm;
- metric;
- precision;
- finite versus asymptotic regime;
- local versus global scope;
- deterministic versus stochastic setting;
- exact versus approximate equality;
- source versus Atlas derivation.

When a norm matters, prefer a norm-specific notation such as ||A||_2 over an unqualified ||A||.

When using transpose in a real-matrix example, state that the corresponding operator-theoretic object is the adjoint.

## 5. Computational witness doctrine

A governed witness should record enough to reconstruct the bounded result.

Required when applicable:

- witness ID;
- chapter ID;
- exact inputs;
- equations or algorithm;
- environment/runtime;
- norm/precision convention;
- generator or executable path;
- expected output or invariant;
- source/rendered artifact identities;
- replay command;
- deterministic seed only when relevant;
- claim boundary.

If the witness is stochastic, state what is and is not expected to replay exactly.

If exact bytes matter, bind them by content digest.

## 6. Figure doctrine

Allowed representation classes remain:

- exact;
- data-derived;
- simulation-derived;
- schematic;
- metaphorical;
- historical.

Every figure must answer two separate questions:

1. What is literal?
2. What is not literal?

For exact/data/simulation-derived figures, retain sufficient generator and parameter information to reconstruct the plotted object.

For schematic/metaphorical figures, visual polish must not imply quantitative meaning that the manifest does not support.

Wolfram is preferred where exact symbolic or high-precision mathematical structure materially strengthens the exposition. It is not mandatory where another reproducible route is more natural.

## 7. Source-lock doctrine

A source lock is a claim-to-source contract.

At minimum it should record:

- source identity;
- version/revision/date where relevant;
- path, DOI, commit, blob, or content identity where available;
- source kind;
- exact authority or claim scope;
- known limitations;
- public/private/project-memory boundary where relevant.

Rules:

- Cite a primary source for historical priority claims when practical.
- Cite a standard reference for standard mathematics when that is the real authority being used.
- Do not use a project README as sole authority for a general theorem.
- Do not use model memory as a substitute for a recoverable project object.
- If an exact GCL object cannot be found, state the source gap.
- A hash establishes byte identity, not semantic correctness.
- A successful replay establishes reconstruction under its stated conditions, not certification.

## 8. Epistemic classes

The canonical project-local classes are defined in governance/EPISTEMIC_LABELS.yaml.

Reader-facing prose should distinguish at least:

- established external theory;
- Atlas derivation;
- Atlas synthesis;
- computational witness;
- observation;
- interpretation;
- GCL public project evidence;
- GCL programme context;
- conjecture or hypothesis;
- open question/problem;
- institutional status.

These classes may coexist in one chapter.

The chapter must not let typography blur them.

## 9. Promotion ladder

A useful default progression is:

planned -> specification-ready -> draft-v0.1 -> audited-draft -> release-candidate -> released.

The current Chapter Ledger retains draft-v0.1 for the six keystones even after audit because audit records are separate evidence objects. Do not silently rewrite status semantics mid-programme.

Future promotion rules should be introduced by ADR and validator update.

## 10. Chapter completion test

Before a chapter-family PR is merged, answer:

1. What is the chapter's object?
2. What obstruction made it necessary?
3. Which definitions/results are externally established?
4. Which derivations are Atlas-owned?
5. Which statements are interpretation or synthesis?
6. Which GCL-specific claims have exact public support?
7. What computational witness is present, if one is needed?
8. What does the main figure literally encode?
9. What is the smallest important failure case?
10. What may downstream chapters now assume?
11. What remains unresolved?
12. Could another competent actor reconstruct why each substantial claim is believed?

## 11. Non-goals

This standard does not require:

- identical section numbering across chapters;
- one figure per chapter;
- one allegory per chapter;
- Wolfram for every computation;
- formal proof for every mathematical statement;
- full literature review inside every chapter;
- GCL-specific material in every chapter.

It requires visible object identity, support identity, and claim boundaries.

## 12. Editorial maxim

Make the mathematics visible without making it smaller.

The six keystones add a second operational maxim:

> Show the reader not only what the object is, but what kind of evidence entitles us to say so.
