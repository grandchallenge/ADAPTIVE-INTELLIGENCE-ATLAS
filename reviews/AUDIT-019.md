# AUDIT-019 — A Taxonomy of Machine Memory

## Disposition

**PASS AFTER ONE TAXONOMY REPAIR**

ATLAS-CH-MEMTAX-001 remains at draft-v0.1.

The chapter successfully defines machine memory through eight engineering coordinates and presents six overlapping memory roles without turning them into a scalar hierarchy or claiming biological identity.

The audit found one substantive taxonomy defect:

> the draft called the sixth role "external persistent memory," which coupled storage locus to lifetime even though lifetime is already an independent coordinate T.

The repair changes the role to **external memory** and states explicitly:

- externality is a locus property relative to the model/process boundary;
- lifetime may be ephemeral or durable;
- persistence is specified independently by T;
- external memory does not imply truth, provenance, synchronization, or reliability.

No source identity, exact witness, prerequisite boundary, or downstream handoff required reversal.

## Audited baseline

- MEMTAX-001 merge:
  cd78611a76ba58a27644c37425a55c466090613b;
- drafting baseline:
  9a00ed8fc6b0ca160a9b7e1fb4deef7c078f69cf;
- audit issue:
  #90;
- chapter:
  ATLAS-CH-MEMTAX-001.

## 1. Hard prerequisite

PASS.

The source lock binds:

- ATLAS-CH-REP-001 manuscript blob
  6109e6ac9505a339cb8bc2dd85a8b9bc882f72bb;
- AUDIT-004 blob
  948f76b3f86d27fa4830efc30d8ef0135134256e.

The Representation prerequisite supplies task-relative representation and identifiability boundaries.

No Retrieval, Continual Learning, External-Memory Thesis, or Context Compilation manuscript is used as hidden prerequisite authority.

## 2. Source scope

PASS.

The source lock distinguishes terminology lineage from machine mechanism evidence.

Working-memory terminology is sourced to Baddeley and Hitch.

Episodic/semantic terminology is sourced to Tulving.

Those sources are used only as naming lineage. The chapter explicitly refuses biological-homology claims for machine implementations.

Machine-memory mechanisms are sourced separately:

- Hopfield for content-addressable associative memory;
- Memory Networks for learned inference coupled to long-term memory;
- Neural Turing Machines for learned read/write access to external differentiable memory;
- Differentiable Neural Computer for dynamic external memory;
- Neural Episodic Control for rapidly assimilated experience memory;
- Roberts, Raffel, and Shazeer for empirical parametric factual associations.

No one mechanism is promoted into a universal memory architecture.

## 3. Eight-coordinate memory object

PASS.

The chapter defines

M = (L, W, R, T, A, U, P, S),

with:

- L — locus;
- W — write/update path;
- R — read/retrieval path;
- T — lifetime/retention;
- A — addressability;
- U — mutability/update cadence;
- P — provenance;
- S — sharing/synchronization scope.

The object is Atlas synthesis.

No scalar "memory strength" is implied.

## 4. Role taxonomy

PASS AFTER REPAIR.

The six roles are now:

- parametric;
- working;
- episodic;
- semantic;
- associative;
- external.

The manuscript explicitly states that:

- the roles do not form a hierarchy;
- they are not mutually exclusive physical stores;
- one store can occupy several roles at once.

This is the correct typed-role interpretation.

## 5. Parametric memory

PASS.

Parametric memory is defined by information encoded in model parameters and accessed through model computation.

The chapter does not claim:

- one fact has one parameter address;
- all parameter content is factual;
- parameter provenance is recoverable automatically;
- editing weights is equivalent to a database transaction.

The empirical language-model source is used only to support the narrower claim that factual associations can sometimes be retrieved from parameters without external context.

## 6. Working memory

PASS.

Working memory is defined by active availability and bounded lifetime.

Examples include active context, hidden state, scratch state, and cached intermediate state.

The chapter correctly separates immediate availability from durable persistence.

The cognitive terminology is explicitly non-homologous.

## 7. Episodic and semantic memory

PASS.

Episodic memory preserves event linkage:

e_i = (id_i, time_i, context_i, payload_i, provenance_i).

Semantic memory is modeled as generalized/consolidated content whose use need not reconstruct one originating episode.

The manuscript explicitly notes that consolidation may discard event identity, exceptions, uncertainty, or provenance.

Thus episodic versus semantic is an organizational distinction, not a storage-medium distinction.

## 8. Associative memory

PASS.

Associative memory is treated primarily as an access relation.

The chapter does not require a distinct physical associative-memory store.

Associative access may apply to episodic, semantic, external, or parametric state.

Hopfield is used as a canonical content-addressable mechanism example.

## 9. External memory

PASS AFTER REPAIR.

The repaired chapter defines externality relative to the model/process boundary.

External memory may be:

- ephemeral;
- durable;
- private;
- shared;
- indexed;
- unindexed;
- provenance-aware;
- provenance-free.

Persistence is independently specified by T.

This repair restores internal consistency to the eight-coordinate taxonomy.

## 10. Exact computational witness

PASS.

ATLAS-CW-MEMTAX-001 keeps one immutable three-record store fixed.

Exact-key read:

B -> blue.

Associative query

q=(4/5,1/5)

gives squared distances:

- A: 2/25;
- B: 32/25;
- C: 17/25.

Therefore the unique nearest record is A -> red.

Recency query

time >= 2

returns [B,C], and the latest record is C -> green.

The arithmetic is exact.

Only the read contract changes.

The witness therefore supports the chapter's central claim that memory role cannot be inferred from stored bytes alone.

## 11. Storage versus retrieval

PASS.

The chapter explicitly separates:

what state exists

from

how computation can access it.

This creates the correct dependency boundary for ATLAS-CH-RETRIEVAL-001.

## 12. Persistence versus availability

PASS.

The chapter states that durable state may be temporarily inaccessible and transient state may be immediately available.

Persistence, indexing, credentials, partition state, and retrieval budget are therefore not collapsed into one property.

## 13. Provenance

PASS.

Provenance is an independent coordinate P.

The chapter correctly allows:

- payload without provenance;
- provenance without complete transformation history;
- semantic consolidation that weakens provenance;
- external storage that preserves provenance explicitly.

Memory is therefore not automatically auditable memory.

## 14. Shared memory and coordination

PASS.

The sharing coordinate S is kept distinct from memory locus and lifetime.

Once several actors access a store, ordering, atomicity, duplicate effects, stale views, and partial failure re-enter through the previously audited Coordination substrate.

Memory architecture and coordination architecture are related but not fused.

## 15. Memory versus knowledge

PASS.

The manuscript explicitly states that retained information may be true, false, obsolete, hypothetical, or unverified.

Retrievability is not epistemic authority.

Self-retrieval is not self-verification.

## 16. Downstream handoff

PASS.

ATLAS-CH-RETRIEVAL-001 may inherit:

- M=(L,W,R,T,A,U,P,S);
- exact versus associative addressing;
- storage/access separation;
- external versus parametric locus;
- provenance as an independent coordinate.

ATLAS-CH-CONTINUAL-001 may inherit:

- parametric write semantics;
- episodic record role;
- semantic consolidation role;
- lifetime and mutability coordinates.

Both consumers are identified by stable chapter ID.

## 17. Integrity

PASS.

The manuscript, specification, formal packet, and witness contain no hidden C0 control characters or tabs.

The Chapter Ledger records ATLAS-CH-MEMTAX-001 at draft-v0.1.

The Source Register contains ATLAS-SRC-MEMTAX-LOCK-001.

The witness contains an explicit Claim boundary.

No governed figure is registered, consistent with the tranche decision.

## 18. Final disposition

AUDIT-019 passes after the external-locus/persistence repair.

The Atlas now has a stable memory vocabulary in which storage locus, write path, access mode, lifetime, mutability, provenance, and sharing can vary independently.

The next memory chapters may therefore ask how to retrieve, update, consolidate, and preserve memory without first deciding that every kind of memory is the same object.
