# Chapter Specification — ATLAS-CH-MEMTAX-001

## Identity

**Title:** A Taxonomy of Machine Memory  
**Part:** Memory Beyond the Weights  
**Status:** specification-ready.  
**Epistemic class:** established memory mechanisms plus Atlas taxonomy.

## Chapter contract

Define machine memory by engineering role rather than biological analogy.

The chapter must distinguish parametric, working, episodic, semantic, associative, and external persistent memory while showing that these labels describe overlapping coordinates rather than six mutually exclusive devices.

## Dependency contract

Hard prerequisite:

- ATLAS-CH-REP-001 — Representations and Invariants.

The prerequisite supplies representation maps, task-relative equivalence, identifiability limits, and the distinction between representation geometry and semantics.

No Retrieval, Continual Learning, External-Memory Thesis, or Context Compilation chapter may be used as hidden prerequisite authority.

## Reader outcome

A reader should be able to:

1. classify a memory system by storage locus, write path, read path, lifetime, addressability, mutability, provenance, and sharing scope;
2. distinguish storage from retrieval;
3. explain parametric memory without treating parameters as a reliable database;
4. distinguish working/context memory from durable memory;
5. distinguish episodic event records from semantic consolidation;
6. explain associative memory as an access contract;
7. explain external memory as a locus/persistence property rather than an authority claim;
8. identify when one physical store plays several memory roles;
9. state the main failure surface for each role;
10. state what Retrieval and Continual Learning may assume after this chapter.

## Formal spine

Represent a memory system as

M = (L, W, R, T, A, U, P, S),

where:

- L is storage locus;
- W is write/update operator;
- R is read/retrieval operator;
- T is lifetime/retention policy;
- A is addressability scheme;
- U is mutability/update cadence;
- P is provenance metadata/traceability;
- S is sharing and synchronization scope.

A memory role is a region or pattern in this coordinate space, not necessarily a unique storage device.

## Six roles

### Parametric memory

Information encoded in model parameters and accessed through forward computation.

Typical properties:
- persistent across calls/checkpoints;
- slow/batch writes through optimization or editing;
- distributed/implicit addressing;
- provenance often diffuse.

### Working memory

Transient state actively available to the current computation.

Examples may include recurrent hidden state, active context, scratch state, and attention KV state.

Typical lifetime is one step, sequence, episode, or bounded task.

### Episodic memory

Records tied to particular events, trajectories, observations, or attempts.

Key properties:
- event identity/time/context retained;
- relatively rapid write;
- retrieval may use time, context, similarity, or keys.

### Semantic memory

Consolidated/generalized knowledge whose use need not recover the single event that produced it.

This is an engineering role, not a claim of biological equivalence.

Semantic content may be stored parametrically or externally.

### Associative memory

Memory retrieved by content/similarity/pattern rather than only by an exact explicit address.

Associative is primarily an access property and can coexist with episodic, semantic, parametric, or external storage.

### External persistent memory

Durable state outside the current model parameters and transient working state.

Examples include databases, files, journals, knowledge stores, vector indices, tuple spaces, or differentiable memory matrices.

External does not imply shared, trustworthy, fresh, or semantically correct.

## Exact computational witness

Create mathematics/computational-witnesses/ATLAS-CW-MEMTAX-001.md.

Use the same three immutable records:

A: id=A, vector=(1,0), time=1, value=red;
B: id=B, vector=(0,1), time=2, value=blue;
C: id=C, vector=(1,1), time=3, value=green.

Show three read operators over the same store:

1. exact-key read R_key(B) -> blue;
2. associative nearest-vector read for q=(4/5,1/5) -> A/red because squared distances are 2/25, 32/25, 17/25;
3. recency/event read for time>=2 -> [B,C], latest -> C/green.

The bytes do not change; the access contract changes the memory role.

## Figure decision

No governed figure is required for v0.1.

The coordinate matrix and exact multi-access witness carry the chapter semantics directly.

## Failure boundaries

Include:

- stale parametric knowledge;
- interference/catastrophic overwrite;
- context eviction;
- unbounded working-state growth;
- episodic duplication and identity loss;
- semantic consolidation that destroys provenance;
- approximate associative false neighbors;
- exact-key brittleness;
- external-store staleness or synchronization failure;
- provenance absent or detached from payload;
- treating retrievability as correctness.

## Downstream handoff

ATLAS-CH-RETRIEVAL-001 may assume:
- the storage/access distinction;
- exact versus associative addressing;
- memory locus and lifetime taxonomy;
- external/parametric separation;
- provenance as a separate coordinate.

It must add vector, symbolic, hybrid, multi-index, and key-value retrieval.

ATLAS-CH-CONTINUAL-001 may assume:
- parametric writes;
- episodic/replay roles;
- semantic consolidation role;
- retention/mutability coordinates.

It must add forgetting, replay, consolidation, regularization, and parameter isolation.

## Acceptance

The draft must:
- define the eight-coordinate memory object;
- present six roles without scalar ranking;
- make overlap/non-exclusivity explicit;
- separate biological naming lineage from machine implementation claims;
- include the exact three-access witness;
- distinguish storage from access and persistence from truth;
- state downstream handoffs by stable ID;
- remain mathematical systems prose rather than a neuroscience or product taxonomy.
