# A Taxonomy of Machine Memory
<!-- ATLAS-CH-MEMTAX-001 -->

**Epistemic status:** established memory mechanisms plus Atlas synthesis and exact finite witness.  
**Specification:** manuscript/specifications/ATLAS-CH-MEMTAX-001.md  
**Formal packet:** mathematics/derivations/ATLAS-CH-MEMTAX-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-MEMTAX-001.md  
**Source lock:** sources/source-locks/ATLAS-CH-MEMTAX-001.yaml

A machine does not have one thing called memory.

It has states that live in different places, survive for different lengths of time, are written by different mechanisms, and can be reached through different kinds of address.

A model's parameters can carry information across deployments.

A context can carry information across one inference.

A cache can survive seconds.

A replay buffer can preserve individual experience.

A database can survive model replacement.

A vector index can recover a record because its content resembles a query even when the caller does not know its exact key.

Calling all of these "memory" is useful only if we preserve the distinctions.

This chapter builds that vocabulary.

## 1. Memory is an interface, not merely a medium

Suppose two systems store exactly the same records.

One lets us retrieve them only by exact identifier.

The other lets us retrieve them by similarity.

The storage is the same. The memory behavior is different.

Now reverse the example.

One system stores a fact in model parameters.

Another stores the same fact in a database.

Both may answer the same query, yet their write paths, update costs, provenance, mutability, and failure modes are radically different.

So the first question should not be merely:

Where is the memory?

It should be:

What memory contract does this state satisfy?

For the Atlas, write a memory system as

M = (L, W, R, T, A, U, P, S).

Here:

L is storage locus;

W is the write or update path;

R is the read or retrieval path;

T is lifetime and retention policy;

A is addressability;

U is mutability and update cadence;

P is provenance;

S is sharing and synchronization scope.

The familiar memory labels are patterns across these coordinates.

They are not six boxes into which every implementation must fit exactly once.

## 2. Six roles, not six rungs

The chapter uses six recurring labels:

parametric memory;

working memory;

episodic memory;

semantic memory;

associative memory;

external persistent memory.

They do not form a hierarchy.

They are not even all the same kind of category.

Parametric and external primarily describe where state lives and how it is updated.

Working primarily describes active availability and lifetime.

Episodic and semantic primarily describe how stored information relates to experience.

Associative primarily describes how memory is addressed.

A single store can therefore occupy several roles at once.

An external vector store of timestamped experiences can be external, episodic, and associative simultaneously.

That overlap is not a defect in the taxonomy.

It is the point.

## 3. Parametric memory

A trained model carries information in its parameters.

Let theta denote the parameter state.

A training or editing procedure changes it:

theta' = W_param(theta, data, objective, update_rule).

A forward pass reads from that state implicitly:

y = f_theta(x).

There may be no explicit record saying that one fact is stored at one address.

Information can be distributed across many parameters and activated only by particular inputs.

This is what the chapter means by parametric memory.

Empirical work on language models has shown that factual associations can sometimes be elicited without supplying an external knowledge source at inference time.

That is evidence that parameters can function as a memory substrate.

It is not evidence that parameters behave like a clean database.

A stored association can be hard to locate.

A correction can interfere with other behavior.

Provenance may be diffuse.

Freshness depends on retraining, editing, or replacement.

And the model may generate a plausible relation that was never stored as a stable factual record.

Parametric memory is powerful partly because storage and computation are fused.

That same fusion makes explicit memory management difficult.

## 4. Working memory

Some state exists only because a computation is currently in progress.

A recurrent hidden state.

An active context.

A scratch buffer.

A temporary plan.

A cache of intermediate keys and values.

These are examples of machine working memory when they remain directly available to the current computation but are not intended to survive indefinitely.

The term has a cognitive-science lineage. Baddeley and Hitch used working memory for limited active storage and processing in human cognition.

The Atlas borrows the engineering intuition, not the biological architecture.

For machines, the operational question is:

what state is actively available now, and when will it disappear?

Working memory is often cheap to read because it is already in the active computation.

It is also easy to lose.

A context can be truncated.

A process can restart.

A cache can be evicted.

A session can end.

High immediate availability and long-term persistence are different properties.

## 5. Context is not durable memory

Modern systems often call context memory.

That can be reasonable.

But context residence should not be confused with persistence.

If a fact appears in the current prompt, the model can use it.

If the next session begins without that prompt, the fact may be gone.

The same applies to hidden state and caches.

A useful test is:

if the process is destroyed and reconstructed, does the state still exist somewhere from which it can be recovered?

If no, the state may be working memory without being durable memory.

A system that repeatedly compiles durable state into an active context therefore has at least two memory layers, not one.

## 6. Episodic memory

An episode remembers an event as an event.

A machine episodic record might contain:

event identity;

time;

task;

observation;

action;

outcome;

local context;

provenance.

Write one record as

e_i = (id_i, time_i, context_i, payload_i, provenance_i).

The key feature is event binding.

If we later ask,

what happened on attempt 17?

we are asking an episodic question.

If we ask,

what general rule did the last thousand attempts support?

we are asking for something closer to semantic consolidation.

Neural Episodic Control is a concrete machine-learning example of rapidly written experience records used in decision making.

The Atlas uses it as a mechanism example.

It does not infer that every replay buffer or event log has the same semantics.

## 7. Semantic memory

Semantic memory stores generalized content that can be used without reconstructing one originating event.

Suppose many episodes support a relation:

objects of type X usually require operation Y.

A consolidation procedure can produce a reusable knowledge object:

K = C({e_i}).

The new object may be more compact and easier to reuse than the raw episodes.

But consolidation can destroy information.

Which event first supported the claim?

Which examples were exceptions?

How uncertain was the conclusion?

Which source supplied the observation?

A semantic representation may preserve the relation and discard the path that produced it.

This is why semantic memory and provenance must remain separate coordinates.

The term semantic memory comes from the episodic/semantic distinction associated with Tulving.

Again, the Atlas imports a useful distinction in information organization.

It does not claim that a knowledge graph, parameter tensor, or vector store reproduces a human semantic-memory system.

## 8. Episodic and semantic are not storage media

The same physical store can contain both.

A database can hold raw event records and consolidated facts.

A parameterized model can acquire abstractions from many episodes.

An external memory can store summaries whose provenance links back to source events.

Thus episodic and semantic are not answers to:

where are the bits?

They are answers to:

what relationship does the stored object preserve to the experience that produced it?

Representation role and storage substrate should not be collapsed.

## 9. Associative memory

Exact addressing asks for a known location or key.

Associative addressing asks for a memory because the query resembles its content or pattern.

Hopfield's classic content-addressable model makes this distinction concrete.

A partial or noisy cue can drive the system toward a stored pattern.

In modern systems, association may be implemented through nearest-neighbor search, attention, learned key matching, hashing, pattern predicates, energy minimization, or hybrid symbolic/vector indices.

The Atlas therefore treats associative memory primarily as an access contract.

A memory can be both episodic and associative.

It can be both semantic and associative.

It can even be parametric and exhibit associative behavior.

The access path does not uniquely identify the storage locus.

## 10. One store, three memory behaviors

The computational witness makes this exact.

Store three immutable records.

A has identifier A, vector (1,0), time 1, and value red.

B has identifier B, vector (0,1), time 2, and value blue.

C has identifier C, vector (1,1), time 3, and value green.

Nothing about the stored records changes.

Now change only the read operator.

Ask for exact identifier B.

The answer is blue.

Ask for the record nearest to

q=(4/5,1/5).

The squared distances to A, B, and C are respectively

2/25,
32/25,
17/25.

So the associative answer is A, red.

Now ask for episodes with time at least 2.

The result is B and C.

The latest is C, green.

Same store.

Three access contracts.

This is why a memory taxonomy that looks only at storage media is incomplete.

## 11. External persistent memory

External memory places state outside the current model parameters and transient active state.

That can include files, databases, journals, knowledge graphs, vector stores, tuple spaces, object stores, or differentiable memory matrices.

"External" is relative to the model/process boundary.

It does not necessarily mean remote over a network.

Memory Networks, Neural Turing Machines, and Differentiable Neural Computers all make external memory an explicit part of the learned computational architecture.

Their mechanisms differ.

The shared idea is that stored state can be read and written through an interface distinct from ordinary parameter access.

That separation opens possibilities unavailable to purely parametric memory:

rapid writes;

explicit record identity;

large persistent stores;

different retention policies;

independent indexing;

provenance;

sharing across models.

It also creates new systems problems.

## 12. External does not mean trustworthy

A database can contain false data.

A vector store can return the wrong neighbor.

A file can be stale.

A journal can contain a bad event with perfect provenance.

A knowledge graph can encode an obsolete relation.

An external memory can be unavailable during a partition.

The important gain is controllability of the memory interface.

Truth remains a separate question.

External memory is sometimes described as if retrieval itself solved hallucination or knowledge reliability.

It does not.

It can make information more inspectable, replaceable, and independently updateable.

Whether the information is correct still depends on evidence, provenance, validation, and retrieval quality.

## 13. Memory Networks and explicit long-term state

Memory Networks were designed around a long-term memory component used jointly with learned inference.

That is an important architectural separation.

Instead of forcing every relevant fact into parameters or current input, the system can maintain a memory object that is read and written as part of the task.

Inference asks what to do with available memory.

Memory management asks what to store and how to expose it.

These can be learned jointly while remaining conceptually distinct.

That separation becomes essential in later chapters, where retrieval quality and continual update must be analyzed independently.

## 14. Differentiable external memory

Neural Turing Machines and Differentiable Neural Computers expose explicit read/write memory to a neural controller and make addressing differentiable enough to learn from data.

This demonstrates that memory management can itself become part of learned computation.

But differentiability does not erase memory semantics.

A read head still has an address rule.

A write still changes stored state.

A usage policy still determines overwrite.

A link structure still changes what sequences can be recovered.

The memory is learnable infrastructure, not magic persistence.

## 15. Lifetime is a separate axis

Consider four pieces of information:

a token in a current context;

a record in an episodic buffer;

a fact encoded in model weights;

a row in a durable database.

Their lifetimes can differ by many orders of magnitude.

But longer is not automatically better.

A stale fact persisting forever can be worse than a fresh fact retained briefly.

A replay buffer that never evicts may become computationally unusable.

A context that keeps every previous token may exceed its budget.

Retention is therefore a policy.

The taxonomy records lifetime T separately from semantic role.

## 16. Writes have different costs

Parametric writes can require training, editing, or optimization.

Working-memory writes can happen every step.

Episodic writes may be append-like.

Semantic writes may require consolidation.

External stores may support transactional updates.

These differences determine how quickly a system can incorporate new information.

A system that knows something only after retraining has a very different adaptation loop from one that can append a validated record immediately.

This is one reason Continual Learning depends on this taxonomy.

Continual learning is not only about retaining old information.

It is about how different write mechanisms interact over time.

## 17. Provenance can be preserved or destroyed

Suppose a memory contains:

Paris is the capital of France.

The payload alone does not tell us:

who asserted it;

when;

from which source;

under which transformation;

with what evidence;

whether the source has since been superseded.

An episodic record can retain those fields.

A semantic consolidation step can drop them.

A parameterized model can make them difficult to recover.

An external governed store can preserve them explicitly.

This makes provenance a first-class memory coordinate rather than decorative metadata.

A memory system that preserves provenance supports different downstream claims from one that stores only payloads.

## 18. Shared memory introduces coordination

A memory can be private to one process.

It can be shared across agents.

It can be replicated.

It can be transactional.

It can be eventually synchronized.

These choices belong to the sharing coordinate S.

Once several actors write to one memory, the Coordination chapter's concerns return:

ordering;

atomicity;

duplicate effects;

stale views;

partial failure.

Memory architecture and coordination architecture therefore meet at shared state.

But they remain distinct.

A shared store tells us where state resides and who can access it.

Coordination semantics tell us how concurrent access behaves.

## 19. Failure by memory role

Different roles fail differently.

Parametric memory can become stale, entangled, or difficult to edit without interference.

Working memory can overflow, truncate, or vanish.

Episodic memory can duplicate events, lose identity, or grow without bound.

Semantic memory can overgeneralize or lose provenance during consolidation.

Associative memory can return false neighbors or suffer representation drift.

External memory can become unavailable, inconsistent, stale, or disconnected from the process that needs it.

These are not one failure called forgetting.

A useful memory diagnosis begins by identifying which coordinate failed.

## 20. Memory is not knowledge

A stored object may be a fact, a hypothesis, a failed attempt, a prediction, a raw observation, a proof, or an obsolete record.

The memory system does not decide which is true merely by retaining it.

The Evidence chapter taught us to separate claim from support.

The same discipline applies here.

Memory is infrastructure for persistence and access.

Knowledge is an epistemic status that requires more.

This is particularly important for agent systems that retrieve old outputs from themselves.

Self-retrieval is not self-verification.

## 21. What Retrieval may assume

ATLAS-CH-RETRIEVAL-001 can now start from a stable distinction between storage and access.

It may assume:

M=(L,W,R,T,A,U,P,S);

exact-key versus associative addressing;

parametric versus external locus;

working versus durable lifetime;

episodic versus semantic organization;

provenance as an independent coordinate.

Its job is to develop retrieval itself:

vector search;

symbolic lookup;

hybrid retrieval;

multi-index access;

key-value memory;

ranking and selection.

It need not rebuild the taxonomy.

## 22. What Continual Learning may assume

ATLAS-CH-CONTINUAL-001 may assume:

parametric write semantics;

episodic records;

semantic consolidation;

retention and mutability coordinates;

the distinction between preserving records and preserving behavior.

Its job is to study what happens when learning continues:

interference;

catastrophic forgetting;

replay;

consolidation;

regularization;

parameter isolation.

Again, the taxonomy becomes useful because "remembering" can now mean several different things.

## 23. The boundary to remember

The most useful question is not:

Does the system have memory?

Almost every nontrivial adaptive system does.

The useful questions are:

Where does the state live?

How is it written?

How is it read?

How long does it survive?

How is it addressed?

How can it change?

What provenance survives with it?

Who else can see or modify it?

Once those coordinates are explicit, the familiar labels become precise.

Parametric memory tells us that information is carried in learned parameters.

Working memory tells us that state is actively available for current computation.

Episodic memory tells us that event identity matters.

Semantic memory tells us that generalized content can survive without the full originating episode.

Associative memory tells us that access can be content-driven.

External persistent memory tells us that durable state can live outside the current model and active context.

None of these labels is the whole memory system.

Together they give us enough structure to ask the next question:

given that something has been stored, how should the system find the right thing again?

That is where retrieval begins.

## References used in this chapter

Exact source identities and authority scopes are pinned in:

sources/source-locks/ATLAS-CH-MEMTAX-001.yaml

The external basis includes Baddeley and Hitch for working-memory terminology lineage, Tulving for episodic/semantic terminology lineage, Hopfield for content-addressable memory, Memory Networks, Neural Turing Machines, Differentiable Neural Computers, Neural Episodic Control, and empirical work on factual associations stored in language-model parameters.
