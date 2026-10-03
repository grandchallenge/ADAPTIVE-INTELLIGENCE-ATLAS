# ATLAS-CH-MEMTAX-001 — Formal and Documentary Packet

## Purpose

This packet makes the Atlas memory taxonomy inspectable and proves the exact multi-access witness.

## 1. Memory object

The chapter uses

M = (L, W, R, T, A, U, P, S).

L — locus:
where the stored state physically or logically resides.

W — write/update:
how new information changes the store.

R — read/retrieval:
how stored state becomes available to computation.

T — lifetime:
how long the state is intended to persist and what evicts it.

A — addressability:
exact address, position, content, similarity, pattern, time, relation, or hybrid key.

U — mutability:
whether writes are append-only, overwrite, incremental, batch, learned, immutable, or otherwise constrained.

P — provenance:
what record identifies origin, transformation, timestamp, authority, or derivation.

S — sharing/synchronization scope:
private, process-local, model-local, session-local, shared, replicated, transactional, or otherwise synchronized.

These coordinates are independent enough that no single scalar "memory strength" is implied.

## 2. Parametric memory

Let theta denote model parameters.

A parameter write has generic form

theta' = W_param(theta, D, objective, optimizer).

A read is implicit in the model computation

y = f_theta(x).

The stored information is therefore accessed through the model's learned computation rather than an explicit record lookup.

Roberts, Raffel, and Shazeer provide empirical evidence that factual associations can be retrieved from model parameters without external context.

The Atlas does not infer that:
- all parameter content is factual;
- a fact has one unique parameter address;
- provenance of one answer is recoverable from weights alone;
- parameter editing is equivalent to a database transaction.

## 3. Working memory

Working memory is defined by active availability and short lifetime.

Let z_t be transient state.

A simple working-memory update is

z_{t+1}=U_work(z_t, input_t).

The state may be directly read by the next computation and discarded at the end of a task or episode.

The Baddeley-Hitch source is used only for terminology lineage around limited active storage/processing.

No biological homology is asserted.

## 4. Episodic memory

An episodic record preserves event identity or context.

Write a record as

e_i = (id_i, time_i, context_i, payload_i, provenance_i).

The event linkage is load-bearing.

If consolidation discards which event produced a claim, the resulting object may play a semantic role but no longer contains the same episodic information.

Neural Episodic Control supplies one machine-learning mechanism with rapidly assimilated experience records used in control.

## 5. Semantic memory

A semantic store contains generalized or consolidated content usable without recovering one originating episode.

Represent consolidation abstractly as

K = C({e_i}_{i in I}).

The map C can be lossy.

It may preserve a relation or fact while discarding:
- event time;
- exact source;
- local context;
- uncertainty;
- exceptions.

Thus semantic consolidation can improve compactness or reuse while weakening provenance.

Tulving supplies the episodic/semantic terminology lineage only.

## 6. Associative memory

Associative memory is primarily a read relation.

Given stored keys k_i and query q, an associative read may return

R_assoc(q)
=
argmin_i d(q,k_i),

or a weighted set based on similarity.

Hopfield's 1982 model is a canonical content-addressable memory example.

Associative access can target:
- episodic records;
- semantic records;
- external records;
- internal learned states.

Therefore associative memory is not required to have a distinct physical locus.

## 7. External memory

Let E be a state object outside current model parameters and transient working state. Externality is a locus property; the lifetime T may be short or durable.

A read/write external memory exposes explicit operations such as

E' = W_ext(E, record),

value = R_ext(E, query).

Memory Networks, Neural Turing Machines, and the Differentiable Neural Computer provide representative learned systems with explicit memory components.

External location does not imply persistence, and external memory does not imply:
- permanent retention;
- shared access;
- transactional consistency;
- provenance;
- correctness.

Those are separate coordinates.

## 8. Role-overlap matrix

A single store can satisfy several labels.

Example:

an external vector store of timestamped experience records is simultaneously:
- external by locus;
- episodic by content organization;
- associative if queried by nearest-neighbor similarity;
- semantic if it also stores consolidated facts.

A Transformer context window can be:
- working memory by lifetime and active availability;
- associative in part through attention-like content-dependent access;
without being durable external memory.

A parameter tensor can be:
- parametric memory by locus/update mechanism;
- associative in behavior for some queries;
without offering explicit record identity.

## 9. Exact multi-access witness

Use immutable records:

A = (id=A, vector=(1,0), time=1, value=red),

B = (id=B, vector=(0,1), time=2, value=blue),

C = (id=C, vector=(1,1), time=3, value=green).

### Exact-key read

R_key(B)=blue.

### Associative read

Let

q=(4/5,1/5).

Squared Euclidean distances are:

d^2(q,A)
=
(4/5-1)^2+(1/5-0)^2
=
2/25;

d^2(q,B)
=
(4/5-0)^2+(1/5-1)^2
=
32/25;

d^2(q,C)
=
(4/5-1)^2+(1/5-1)^2
=
17/25.

Therefore

R_assoc(q)=A

and returns red.

### Episodic/recency read

Filter records with time >= 2.

The result is [B,C].

The latest event is C and returns green.

The record bytes are unchanged across all three reads.

Only R changes.

Therefore memory role cannot be inferred from storage bytes alone.

## 10. Storage versus retrieval

Two systems can contain identical stored records and expose different retrieval semantics.

Conversely, two systems can expose similar nearest-neighbor behavior while storing records in different loci.

This gives two independent questions:

what state exists?

how can computation access it?

ATLAS-CH-RETRIEVAL-001 consumes the second question in detail.

## 11. Persistence versus availability

A record can be durable but currently unreachable because:
- the index is missing;
- credentials are absent;
- the query language cannot express the needed predicate;
- the retrieval budget is exhausted;
- the store is partitioned.

A transient context can be highly available yet disappear after the session.

Thus persistence and online availability are distinct.

## 12. Provenance as a memory coordinate

A payload p and provenance record pi should be represented separately.

A system may store p without pi.

It may store pi but fail to bind it transactionally to p.

It may retain source identity but lose transformation history.

Therefore "memory" does not automatically mean "auditable memory."

The later External-Memory Thesis and Context Compilation chapters may strengthen this coordinate.

## 13. Downstream handoff

ATLAS-CH-RETRIEVAL-001 may consume:
- M=(L,W,R,T,A,U,P,S);
- exact versus associative addressing;
- access-role overlap;
- external versus parametric locus;
- provenance as independent metadata.

ATLAS-CH-CONTINUAL-001 may consume:
- parametric update semantics;
- episodic record role;
- semantic consolidation role;
- lifetime and mutability coordinates.

## Claim boundary

This packet defines an Atlas engineering taxonomy and proves the exact three-read witness.

The cognitive-science sources provide terminology lineage only.

No claim is made that machine memory types are biologically homologous, that the six roles are exhaustive, or that a memory's role can be determined from its storage medium alone.
