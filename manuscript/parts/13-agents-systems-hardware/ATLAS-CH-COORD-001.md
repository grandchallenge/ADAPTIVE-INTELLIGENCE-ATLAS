# Coordination Architectures
<!-- ATLAS-CH-COORD-001 -->

**Epistemic status:** established coordination mechanisms plus Atlas synthesis and exact finite witness.  
**Specification:** manuscript/specifications/ATLAS-CH-COORD-001.md  
**Formal packet:** mathematics/derivations/ATLAS-CH-COORD-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-COORD-001.md  
**Source lock:** sources/source-locks/ATLAS-CH-COORD-001.yaml

One agent can fail because it chose badly.

Two agents can fail even when each chooses correctly.

That is the new phenomenon.

Once several bounded interaction loops communicate or act on shared resources, correctness is no longer only a property of each local decision. It depends on what each actor can see, when events become visible, which operations may interleave, whether messages can repeat, what state is shared, and which effects are atomic.

Coordination is the mathematics and systems discipline of those relationships.

It begins where the previous chapter ended.

From Models to Agents gave us a single interaction loop with state, tools, authority, budgets, and a stop rule. We now place several such loops in one world.

The result is not simply a larger prompt.

It is a concurrent system.

## 1. From one loop to many

Let actor i carry an audited single-agent object A_i.

Each actor can observe, propose, act, update state, spend resources, and stop.

Now suppose actor P produces an output needed by actor Q.

Several questions appear immediately.

How does Q learn that the output exists?

Can Q see a partial result?

What if P changes it while Q is reading?

What if the message is delivered twice?

What if Q acts before an earlier causal dependency arrives?

What if both actors modify the same state?

What if one fails halfway through a multi-step effect?

What if both wait for one another?

None of these questions is answered by making either model more capable.

They belong to the coordination layer.

For the Atlas, write a coordination system as

C = (I, {A_i}, {X_i}, S, K, ≺, T, F).

Here:

I indexes the participating actors;

A_i is actor i's single-agent loop;

X_i is actor-local state;

S is shared coordination state or a shared substrate;

K is the set of communication and coordination operations;

≺ is the causal or application-relevant event-order relation;

T is the declared transaction and atomicity semantics;

F is the failure, retry, timeout, redelivery, and deduplication policy.

This tuple is not the definition of every distributed system.

It is the minimum map legend needed for the architectures in this chapter.

## 2. Communication is not agreement

Suppose P sends Q a message:

"candidate proof complete."

Several facts may follow, depending on the system.

The message may have been emitted.

It may have entered a queue.

It may have been delivered.

Q may have read it.

Q may have parsed it.

Q may have accepted its meaning.

Q may have changed state because of it.

The proof may even be correct.

These are different events.

A communication channel transports an object or signal.

It does not confer epistemic authority on the content.

Nor does successful delivery imply that sender and receiver now agree.

This distinction matters for multi-agent systems because a transcript can look coordinated while the actors are operating with incompatible state.

The message is part of the coordination story.

Its truth belongs to an evidence story that comes later.

## 3. Local state and shared state

Every actor has some local state X_i.

A coordination architecture may also expose shared state S.

Shared state is attractive because it creates a common surface.

Write once, and many actors may observe.

But "shared" does not mean "simultaneously identical in every observer."

A system may cache.

It may replicate.

It may materialize views at different times.

It may delay propagation.

It may expose snapshots.

It may permit concurrent writers.

The phrase "shared memory" therefore hides a second question:

what consistency semantics govern observation of that memory?

Two agents can both have access to the same named store while seeing different versions of it.

Coordination requires the visibility rule, not merely the storage location.

## 4. Six coordination families

The architectures below solve different coordination problems.

They should not be arranged on a single ladder from primitive to advanced.

### 4.1 Direct message passing

The simplest picture is an addressed channel.

P sends m to Q.

Q receives m.

This architecture makes actor identity and directed communication explicit.

It can keep local state local.

But it immediately raises delivery questions:

Is the channel reliable?

Can messages be reordered?

Can duplicates occur?

Does a send block?

Can the receiver refuse?

Does one sender's order survive mixing with messages from others?

The Actor tradition is one important lineage for thinking in terms of independent computational actors and messages.

The useful abstraction is not that every modern agent system is an Actor system.

It is that independently evolving components can coordinate through explicit messages rather than through one shared call stack.

### 4.2 Rendezvous

Sometimes the communication event should happen only when both sides participate.

A rendezvous couples progress.

A sender reaches a communication point.

A receiver reaches a compatible point.

The communication transition occurs when the two synchronize.

Communicating Sequential Processes made this kind of communication a first-class structuring idea for concurrent programs.

Rendezvous can simplify some ordering questions because synchronization is explicit.

It can also create blocking and deadlock surfaces.

Coordination is always a trade: making one relation explicit moves difficulty somewhere else.

### 4.3 Blackboard coordination

A blackboard replaces pairwise addressing with shared visible problem state.

One component posts a partial hypothesis.

Another notices it and adds a refinement.

A third may detect a conflict.

The blackboard is not merely storage.

It is a coordination surface around which heterogeneous problem-solving processes organize their activity.

H. Penny Nii's blackboard account is useful because it separates the blackboard model of problem solving from the many concrete systems built around it.

For agent systems, the same lesson remains valuable.

A shared workspace can decouple contributors from direct knowledge of one another.

But the blackboard does not decide which contribution is correct.

And once several writers can modify the same state, scheduling and consistency become unavoidable.

### 4.4 Tuple spaces

Linda sharpens shared coordination into a small algebra.

The shared object is a tuple space: a logically shared multiset of tuples.

A process may perform operations such as:

out(t): add tuple t;

rd(p): read a tuple matching pattern p without removing it;

in(p): take a matching tuple and remove it.

The important word is matching.

A consumer can coordinate by describing the shape of the object it needs rather than naming the producer that must send it.

This changes the coupling structure.

Producer and consumer can be separated in space, time, and identity.

The tuple space becomes the rendezvous surface.

The destructive in operation adds another feature: possession can become exclusive if the take operation is atomic.

A work token can be placed once and consumed by one worker.

That is coordination through state semantics rather than addressed messaging.

Again, nothing about a tuple's presence makes its content true.

The space coordinates availability, not epistemic status.

### 4.5 Event-driven coordination

Another architecture treats history as the primary object.

Actors append events.

Other actors subscribe, replay, materialize, or derive later state.

This design has a powerful consequence:

the path by which state was obtained can remain visible.

But event-driven systems acquire their own obligations.

What is the event identity?

Can delivery repeat?

Which order is authoritative?

Can consumers replay from a checkpoint?

Are materialized views deterministic?

What happens when old events are reinterpreted by new code?

An event log can make provenance easier to preserve while making state reconstruction an explicit part of the architecture.

The Atlas uses the public AETHER project as one bounded GCL example of this direction.

At its pinned public revision, AETHER describes an append-only causal journal, deterministic resolution over fixed journal prefixes, recursive rule execution, and derivation provenance.

That is exact project evidence.

It is not evidence that every coordination system should look like AETHER.

### 4.6 Transactions

Transactions answer a different question.

Which set of effects should appear as one unit?

Suppose an operation reads a value, computes a new value, and writes it back.

If another actor can interleave its own read and write halfway through, the two locally correct procedures may compose incorrectly.

A transaction boundary can prevent some harmful interleavings by grouping operations under declared atomicity and isolation semantics.

Jim Gray's transaction work is a foundational reference point for this view.

But "transaction" is not a magic word.

A transaction must have a boundary.

Database writes may be inside it while network calls, emails, actuator effects, or external APIs remain outside.

Atomicity is only as broad as the set of effects the transaction system actually controls.

## 5. Causality before total order

When several actors run concurrently, it is tempting to ask:

What happened first?

Sometimes the question has no application-level answer.

Leslie Lamport's happens-before relation gives a disciplined way to say what the system actually knows.

Write

a ≺ b

when event a can causally precede event b under the declared execution.

Local program order contributes causal edges.

Sending a delivered message precedes receiving it.

Transitivity contributes further edges.

But two independent events may be incomparable.

Neither happened "before" the other in the causal sense relevant to the computation.

A runtime can still assign them timestamps and impose a total order.

That can be useful.

It is also extra structure.

A total order can serialize events that the application did not need to order.

The distinction matters because unnecessary ordering can create coordination cost.

If two events are genuinely independent, forcing global agreement about their order may buy no semantic value.

## 6. A small race with a complete answer

The easiest concurrency bug is already enough to justify the chapter.

Let shared state begin at

x = 0.

Actors P and Q both intend to increment x once.

Each performs:

read x;

write the value it read plus one.

Individually, each program is correct.

If P runs completely and then Q runs completely, the final value is 2.

If Q runs completely and then P runs completely, the final value is also 2.

But concurrency introduces four more legal schedules.

The computational witness enumerates all six interleavings that preserve each actor's local read-before-write order.

Only two finish at 2.

Four finish at 1.

Both actors "succeeded" locally.

The shared effect is wrong.

This is the lost-update problem in its smallest useful form.

The lesson is not merely that concurrency is dangerous.

It is more precise:

local correctness plus shared state does not imply compositional correctness under interleaving.

## 7. Atomicity changes the schedule space

Now replace each two-step increment with one atomic operation:

INC: x <- x + 1.

There are still two possible actor orders.

P then Q.

Q then P.

Both produce 2.

The arithmetic did not change.

The allowed interleavings changed.

That is what atomicity buys in this example.

It removes intermediate states from the schedule space visible to competing actors.

This is a recurring systems theme.

Many coordination mechanisms do not improve the intelligence of any participant.

They change which global executions are possible.

## 8. Delivery is not effect

Messages introduce a related distinction.

Suppose a worker receives:

charge account by 10.

If the transport provides at-least-once delivery, the same logical message may arrive twice.

If the worker blindly applies the command twice, the effect is 20.

The transport may be behaving exactly as designed.

The application is still wrong.

One repair is idempotence.

For state transition E and message m, idempotence means:

E(E(s,m),m) = E(s,m).

Applying the same logical operation twice has the same effect as applying it once.

Another repair is deduplication.

Give the logical operation a stable identity.

Record that identity durably when its effect commits.

Ignore a later delivery carrying an already-committed identity.

This sounds like exactly-once processing.

It is only as strong as its assumptions.

If the deduplication record commits but an external side effect does not, or the external side effect occurs but the record does not, ambiguity returns.

Exactly-once effect is therefore not obtained merely by writing "exactly once" on a queue.

It is an end-to-end claim about identity, atomicity, persistence, and side effects.

## 9. Retry is a semantic operation

Retries are often treated as infrastructure.

They are part of the program.

Suppose an actor sends an operation and sees no reply.

Three states are compatible with that observation:

the operation never arrived;

the operation arrived and failed;

the operation succeeded but the reply was lost.

Retrying is correct in the first case.

It may be correct in the second.

It can duplicate an effect in the third.

A retry policy F must therefore be read together with the operation semantics.

For a pure read, retry may be harmless.

For a non-idempotent side effect, retry may require an operation identity, transaction boundary, compensating action, or human review.

The absence of a reply is not the same thing as evidence that nothing happened.

## 10. Shared state is not authority

Blackboards, tuple spaces, event logs, databases, and shared memories can all become central surfaces.

That centrality creates a temptation.

If a fact is in the shared store, treat it as true.

The previous evidence chapter already taught us why that fails.

A coordination substrate answers questions such as:

Who can see this object?

Who can consume it?

Who can overwrite it?

In what order did related events occur?

Has this operation already been applied?

Those are important facts.

They do not establish the semantic truth of the payload.

A bad hypothesis can be perfectly replicated.

A false tuple can be atomically committed.

An incorrect event can have impeccable provenance.

Coordination and evidence meet later.

They must first remain distinct.

## 11. Deadlock and livelock

Synchronization can fail even when no data is corrupted.

Consider two actors.

P holds resource a and waits for b.

Q holds b and waits for a.

No actor is locally broken.

The system stops making progress.

That is deadlock.

Livelock is different.

Actors continue changing state but repeatedly interfere so that useful progress does not occur.

A pair of overly polite processes can continually yield to one another.

An agentic analogue is a pair of workers that repeatedly reassign a disputed task without resolving it.

Progress therefore needs its own semantics.

"Nothing crashed" is weaker than "the system advanced."

## 12. Partial failure changes reasoning

In a local sequential program, a function call usually returns, raises, or the process fails.

Distributed coordination adds ambiguous partial outcomes.

One actor can remain healthy while another fails.

A network can partition.

A shared service can be unreachable from one participant and reachable from another.

A timeout can mean failure, delay, overload, or a lost response after success.

This makes absence difficult to interpret.

Silence is not a single state.

The coordination architecture must decide what evidence about failure is available and what actions are justified under uncertainty.

This is one reason distributed protocols become more elaborate than their local analogues.

They are not merely moving bytes.

They are managing incomplete knowledge about a changing joint state.

## 13. Coordination cost is real

Coordination can improve correctness and enlarge what a group can accomplish.

It also costs something.

Messages consume bandwidth and serialization work.

Synchronization introduces waiting.

Transactions constrain concurrency.

Retries consume repeated work.

Provenance and deduplication require metadata.

Global ordering can create contention.

A useful bookkeeping decomposition is

c_coord = c_comm + c_sync + c_retry + c_meta.

The terms need not share one universal physical unit.

The equation is a reminder that coordination is not free structure.

This leads to a design question that will recur throughout the Atlas:

What is the weakest coordination semantics that still preserve the claim or invariant we care about?

If two computations are independent, do not synchronize them merely because synchronization is available.

If a task requires exclusive consumption, a destructive tuple-space take may be more natural than global locking.

If a shared decision requires a transaction, pretending eventual convergence is sufficient may be dangerous.

Architecture begins by identifying the invariant.

## 14. The AETHER example

AETHER is useful here because it makes one particular coordination choice explicit.

At the pinned public revision, its center of gravity is an authoritative semantic kernel built around an append-only causal journal, deterministic state resolution, recursive rule evaluation, and provenance/explanation.

Its interface record separates journal, resolver, rules, runtime, and explanation roles.

It also states an invariant that fixed journal prefix plus compiled program yields deterministic results.

This is exactly the sort of claim that belongs in a coordination chapter because it exposes the chosen shared-state semantics.

AETHER does not replace the general theory.

It is one design point.

Compared with direct message passing, it makes shared history more central.

Compared with a bare blackboard, it makes derivation and replay more explicit.

Compared with a simple queue, it treats the semantic state reconstructed from history as a first-class object.

Those are architectural choices with costs and benefits.

The Atlas records them as public project evidence, not as a universal optimum.

## 15. What coordination does not solve

A coordination system can ensure that one worker takes a task token.

It cannot ensure the worker solves the task correctly.

It can serialize two writes.

It cannot ensure the serialized value is scientifically valid.

It can deliver every message.

It cannot ensure the actors interpret the messages the same way.

It can replay every event.

It cannot ensure the original event was truthful.

It can give every actor the same state.

It cannot ensure the common state encodes the right world model.

This boundary is central.

Coordination can preserve relationships among computational events.

It cannot replace the semantics of the work those events carry.

## 16. What the next chapters may assume

Two direct architectural consumers depend on this chapter.

ATLAS-CH-EVIDEX-001 — Evidence Exchange and Zero-Context Work may assume stable actor/event identity, local/shared-state separation, channel semantics, causal order, retry and deduplication policy, and transaction boundaries.

Its task is to add evidence semantics:

what a returned object establishes;

how provenance follows a handoff;

how an independent actor receives enough context to reproduce or challenge a claim.

ATLAS-CH-POLITY-001 — The Computational Polity may assume the full coordination object

C = (I, {A_i}, {X_i}, S, K, ≺, T, F),

together with the architecture families and failure surfaces developed here.

Its task is larger:

compose models, agents, memory, tools, humans, validators, and governance into a coherent computational polity.

Neither chapter needs to rediscover what a race condition or duplicate effect is.

That is the point of dependency.

## 17. The boundary to remember

The simplest distributed-system mistake is to believe that because every component is correct, the system is correct.

The lost-update witness shows otherwise.

Correct local steps can compose into a wrong global state when the coordination semantics are underspecified.

The reverse lesson is equally important.

Coordination machinery should not be worshipped for its own sake.

Messages, blackboards, tuple spaces, event logs, rendezvous, clocks, and transactions are ways of constraining or exposing possible interactions.

They are useful when those constraints match an invariant the larger system actually needs.

The governing question is therefore not:

Which coordination architecture is best?

It is:

Which relationships among actors, events, state, and effects must remain true, even when execution is concurrent and failure is partial?

Once that question is explicit, coordination stops being plumbing.

It becomes part of the mathematics of adaptive systems.

## References used in this chapter

The source lock pins the mechanism references and Atlas project objects used by this draft:

sources/source-locks/ATLAS-CH-COORD-001.yaml

External mechanism sources include the 1973 Actor formalism, Hoare's Communicating Sequential Processes, Carriero and Gelernter's Linda in Context, Nii's blackboard-system account, Lamport's event-ordering paper, and Gray's transaction paper.

The AETHER material is exact GCL public project evidence at commit 74b2e322a4453f1665a076bc0682adcd0c5cfb44 and is used only as a bounded coordination case study.
