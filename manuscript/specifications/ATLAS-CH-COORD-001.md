# Chapter Specification — ATLAS-CH-COORD-001

## Identity

**Title:** Coordination Architectures  
**Part:** Agents, Systems, and Hardware  
**Status:** specification-ready.  
**Epistemic class:** established coordination mechanisms plus Atlas synthesis.

## Chapter contract

Explain what changes when several bounded agent loops can communicate, observe shared state, synchronize, retry, or act on common resources.

The chapter must distinguish communication from agreement, shared state from consistency, delivery from effect, and concurrency from atomicity.

## Dependency contract

Hard prerequisite:

- ATLAS-CH-AGENTS-001 — From Models to Agents.

The prerequisite supplies the single-agent transition object, persistent state, typed action interfaces, authority/resource state, delegation packets, and stop rules.

No later Evidence Exchange, Computational Polity, or external-memory chapter may be used as hidden prerequisite authority.

## Reader outcome

A reader should be able to:

1. explain why a collection of agents is not yet a coordination architecture;
2. distinguish direct message passing, rendezvous, blackboards, tuple spaces, event streams, and transactions;
3. state the role of a causal partial order;
4. explain why concurrent shared-state updates can lose effects without atomicity;
5. distinguish at-most-once delivery, at-least-once delivery, deduplicated processing, and exactly-once effect claims;
6. explain why retries require idempotence or stable operation identity when effects may duplicate;
7. state what a transaction boundary does and does not guarantee;
8. distinguish local state, shared coordination state, and authoritative state;
9. identify failure surfaces caused by races, stale reads, duplicate events, partial failure, and deadlock/livelock;
10. state what Evidence Exchange and Computational Polity may inherit.

## Formal spine

Use the coordination object

C = (I, {A_i}, {X_i}, S, K, ≺, T, F),

where:

- I is the actor/agent index set;
- A_i is the audited single-agent loop for actor i;
- X_i is local state;
- S is shared coordination state or shared substrate;
- K is the set of coordination channels and operations;
- ≺ is the causal/event-order relation;
- T is the declared transaction/atomicity semantics;
- F is the failure, retry, and deduplication policy.

This is an Atlas explanatory object, not a universal distributed-systems ontology.

## Architecture families

### Direct message passing

Actors address messages to other actors or endpoints.

Delivery semantics and mailbox ordering must be declared separately from application meaning.

### Rendezvous

Communication is a synchronization event requiring compatible sender/receiver participation.

Use CSP as a representative formal lineage.

### Blackboard

Actors contribute to and inspect a shared structured problem state.

The blackboard coordinates through shared visible state rather than direct pairwise addressing.

### Tuple space

Use a shared multiset of tuples with associative pattern matching.

Representative operations:

out(t) — add tuple t;

rd(p) — read a matching tuple without removing it;

in(p) — take a matching tuple destructively.

Use Linda as the representative mechanism source.

### Event-driven / append-only coordination

Actors append events and derive or react to later state.

Ordering, replay, duplicate delivery, and materialization semantics must be explicit.

Use AETHER only as exact public GCL project evidence for one governed event/provenance-oriented implementation direction.

### Transactions

Group a set of effects under declared atomicity/recovery/isolation semantics.

Do not use the word transaction without saying which effects belong to the boundary and which failures are covered.

## Causality

Use Lamport's happens-before relation as the canonical example of causal partial order.

If event a can causally affect event b, write

a ≺ b.

Independent events need not be ordered by causality merely because a runtime can assign them a total order.

## Computational witness

Create mathematics/computational-witnesses/ATLAS-CW-COORD-001.md.

Exhaustively enumerate all legal interleavings of two non-atomic read-modify-write increments on a shared integer initially zero.

Each actor performs:

read x;

write previously_read + 1.

Among the six legal interleavings preserving each actor's program order:

- two serial interleavings produce final x=2;
- four overlapping interleavings produce final x=1.

Then compare with two atomic increment transactions, for which either serial transaction order produces x=2.

This witness establishes a finite concurrency fact and the need for an atomicity story. It does not prove that transactions are always the right coordination mechanism.

## Figure decision

No governed figure is required for v0.1.

The architecture comparison table, partial-order diagrams in notation, and exact interleaving table carry the core semantics. A multi-agent topology plate may be added in the Computational Polity chapter when the actors, memory, tools, humans, and validators are assembled together.

## Failure boundaries

Include:

- message loss or delay;
- duplicate delivery;
- stale reads;
- lost update;
- conflicting concurrent writers;
- inconsistent materialized views;
- deadlock;
- livelock;
- retry storms;
- non-idempotent duplicate effects;
- transaction boundary that omits an external side effect;
- partition or partial failure;
- treating shared state as automatically authoritative.

## GCL bounded example

The chapter may use exact public AETHER objects as one concrete GCL example of a governed shared coordination substrate.

It must state that this is project evidence, not proof that AETHER is a universal coordination architecture.

## Downstream handoff

ATLAS-CH-EVIDEX-001 may assume:

- actor identity;
- local/shared-state separation;
- channels and event identities;
- ordering semantics;
- retry/deduplication semantics;
- transaction boundaries.

ATLAS-CH-POLITY-001 may assume:

- the coordination object;
- shared-state and communication families;
- causal ordering;
- atomicity/failure surfaces;
- coordination cost.

Those chapters must add evidence semantics or polity-level composition rather than rebuilding basic coordination.

## Acceptance

The draft must:

- preserve the audited single-agent boundary;
- define the coordination object exactly;
- compare at least six coordination families without ranking them universally;
- introduce causal partial order;
- include the exact lost-update witness;
- distinguish delivery from effect;
- make idempotence/retry assumptions explicit;
- treat transactions as bounded semantics rather than magic atomicity;
- include the bounded AETHER public-project example;
- state downstream handoffs by stable identity;
- remain mathematical systems prose rather than product documentation.
