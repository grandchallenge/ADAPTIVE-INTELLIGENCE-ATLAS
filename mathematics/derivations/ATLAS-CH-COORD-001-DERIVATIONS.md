# ATLAS-CH-COORD-001 — Formal and Documentary Packet

## Purpose

This packet reconstructs the chapter's coordination object and proves the finite concurrency statements used in the manuscript.

It separates established coordination mechanisms from Atlas-owned synthesis.

## 1. Hard prerequisite

ATLAS-CH-AGENTS-001 supplies the audited single-agent object

A = (M, C, X, O, Γ, U, B, σ).

AUDIT-015 confirms its model/action/authority/state boundaries.

COORD-001 does not redefine the single-agent loop.

It asks what additional structure is required when several such loops may affect one another.

## 2. Coordination object

The chapter uses

C = (I, {A_i}, {X_i}, S, K, ≺, T, F).

I indexes participating actors.

A_i is actor i's single-agent transition loop.

X_i is actor-local state.

S is shared coordination state or a shared substrate.

K is the family of coordination operations: send, receive, publish, append, read, take, rendezvous, transaction commit, or other declared channels.

≺ is the causal or application-relevant event-order relation.

T records declared atomicity, isolation, commit, and recovery semantics.

F records failure, retry, deduplication, timeout, and redelivery semantics.

The tuple is intentionally broad enough to describe several coordination families without pretending they are identical.

## 3. Communication is weaker than agreement

Suppose actor i sends message m to actor j.

The event

send_i(m)

does not by itself imply:

- delivery;
- receipt;
- interpretation;
- acceptance;
- agreement;
- effect.

Each implication requires additional system semantics.

This is why the chapter keeps message transport, application state transition, and epistemic acceptance separate.

## 4. Causal partial order

Following Lamport, define a happens-before relation ≺ on events by the transitive closure of:

1. local program order within one actor;
2. send(m) ≺ receive(m) for a delivered message;
3. transitivity.

The relation is a partial order.

Two events can be incomparable when neither can causally influence the other under the declared execution.

A runtime may impose a total order for implementation convenience.

That total order is extra structure, not causal necessity.

## 5. Architecture mappings

### Actor/message passing

S may be minimal or absent as an application-visible shared store.

K contains addressed send/receive operations.

Coordination depends on mailbox/delivery/ordering semantics.

### Rendezvous

A communication transition occurs only when compatible participants synchronize.

The synchronization itself is part of the transition semantics rather than a later consequence of buffered delivery.

### Blackboard

S is the visible shared problem state.

Actors inspect and modify S according to domain rules.

Scheduling and conflict semantics remain separate questions.

### Tuple space

S is a multiset of tuples.

out(t) adds tuple t.

rd(p) returns a tuple matching pattern p without removal.

in(p) returns and removes one matching tuple.

The destructive nature of in can serve as a coordination primitive because competing takers cannot all remove the same tuple under a correct atomic implementation.

### Event log

S is represented by an append-only history or journal plus one or more derived materializations.

K includes append and subscription/query operations.

Replay and materialization become first-class.

### Transactions

T groups several primitive effects into a declared atomic unit.

The application must still identify external effects not covered by the transaction boundary.

## 6. Lost-update witness

Initial shared state:

x = 0.

Actors P and Q each execute two program-ordered operations:

R_P: read x into local r_P;

W_P: write r_P + 1 to x;

R_Q: read x into local r_Q;

W_Q: write r_Q + 1 to x.

Constraints:

R_P ≺ W_P,

R_Q ≺ W_Q.

There are exactly

binomial(4,2) = 6

interleavings that preserve these two local orders.

They are:

R_P W_P R_Q W_Q -> final 2;

R_P R_Q W_P W_Q -> final 1;

R_P R_Q W_Q W_P -> final 1;

R_Q W_Q R_P W_P -> final 2;

R_Q R_P W_Q W_P -> final 1;

R_Q R_P W_P W_Q -> final 1.

Thus four of six legal non-atomic interleavings lose one update.

The result is exact for this toy schedule model.

## 7. Atomic increment comparison

Replace each read/write pair with one atomic transition:

INC_P: x <- x + 1;

INC_Q: x <- x + 1.

There are two serial orders:

INC_P INC_Q;

INC_Q INC_P.

Both yield x = 2.

The witness therefore isolates what atomicity changes in this example:

intermediate reads/writes are no longer interleavable across the transaction boundary.

It does not establish that every transaction implementation provides the same isolation or recovery semantics.

## 8. Delivery and effect

Let message m carry stable operation identity id(m).

Under at-least-once delivery, a receiver may observe the same logical operation more than once.

If the effect function E satisfies

E(E(s,m),m) = E(s,m),

then replaying the same operation is idempotent with respect to state s.

If not, duplicate delivery can duplicate effect.

A deduplication map keyed by stable operation identity can implement an alternative:

apply m only if id(m) has not already been committed.

This is an Atlas derivation of a simple exactly-once-effect pattern under strong assumptions:

- stable unique identity;
- durable deduplication state;
- atomic coupling of effect and identity commit;
- no untracked external side effect outside that atomic boundary.

Remove those assumptions and the exactly-once-effect claim weakens.

## 9. Transactions do not automatically cover the world

Suppose a transaction commits database state and then an external email is sent outside the transaction.

A retry after an ambiguous failure can duplicate the email even if the database transaction itself is atomic.

Therefore:

atomic database commit

does not imply

atomic database-plus-external-world effect.

The boundary T must be stated explicitly.

## 10. Coordination cost

Let c_comm count communication cost, c_sync synchronization/serialization delay, c_retry expected retry/recovery cost, and c_meta provenance/coordination metadata cost.

The chapter uses the bookkeeping identity

c_coord = c_comm + c_sync + c_retry + c_meta

only as an explanatory decomposition.

It is not assumed that all terms share a universal physical unit.

The point is that coordination consumes resources and can constrain throughput or latency.

## 11. AETHER bounded example

At public commit

74b2e322a4453f1665a076bc0682adcd0c5cfb44,

AETHER records an append-only causal journal, deterministic resolver, rule/runtime layers, derivation provenance, and interface invariants including deterministic results for a fixed journal prefix and compiled program.

These exact public objects justify using AETHER as a GCL case study in event/provenance-oriented coordination.

They do not establish that AETHER realizes every architecture in this chapter or that its design is universally preferable.

## 12. Downstream handoff

ATLAS-CH-EVIDEX-001 may consume:

- stable actor/event identity;
- local versus shared state;
- channel semantics;
- causal order;
- retry/deduplication policy;
- transaction boundaries.

ATLAS-CH-POLITY-001 may consume the full coordination object

C = (I, {A_i}, {X_i}, S, K, ≺, T, F)

and the distinction among message, rendezvous, shared-state, tuple-space, event-log, and transaction coordination.

## Claim boundary

This packet proves the finite lost-update enumeration, the two-order atomic comparison, and the simple idempotence/deduplication conditions stated above.

It does not prove universal distributed-system reliability, consensus, linearizability, serializability for arbitrary implementations, or exactly-once delivery in open systems.
