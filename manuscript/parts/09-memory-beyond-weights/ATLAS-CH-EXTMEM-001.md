# The External-Memory Thesis
<!-- ATLAS-CH-EXTMEM-001 -->

**Epistemic status:** audited retrieval + audited continual-learning mechanisms + primary retrieval-augmented/model-editing examples + Atlas synthesis + exact finite witness.  
**Specification:** manuscript/specifications/ATLAS-CH-EXTMEM-001.md  
**Formal packet:** mathematics/derivations/ATLAS-CH-EXTMEM-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-EXTMEM-001.md  
**Source lock:** sources/source-locks/ATLAS-CH-EXTMEM-001.yaml

A model can know something in at least two radically different ways.

It can carry the information implicitly in its parameters.

Or it can retrieve an explicit record when the information is needed.

Those two forms of knowing have different update semantics, provenance semantics, sharing semantics, latency costs, and failure modes.

The governing thesis of this chapter is:

> an intelligent system should not force every useful fact into its weights when some information is better represented as explicit, versioned, retrievable state.

The thesis has an equally important converse:

> external memory is not a universal substitute for learning.

Stable structure, reusable procedures, compressed regularities, and learned representations may belong in parameters.

The architecture is usually hybrid.

## 1. The wrong question is parameters versus memory

A simple binary question asks:

> should knowledge live in parameters or external memory?

That framing is too coarse.

The same system can use:

- parameters for syntax, features, procedures, and compressed regularities;
- an external store for mutable facts, records, evidence, and shared organizational state;
- a working context for the subset needed now.

Placement is an architectural decision about which representation best serves which kind of information.

## 2. What is parametric knowledge?

Call knowledge **parametric** when its use is mediated by learned model state.

For parameters `theta`, behavior is:

`f_theta(q)`.

The knowledge may not correspond to a single readable parameter.

It can be distributed across many coordinates and interactions.

That distribution is often the point.

It enables compression and generalization.

## 3. What is external memory?

External memory means explicit state outside the model parameters.

A record can carry:

- key;
- value/content;
- source;
- timestamp;
- version;
- type;
- access policy;
- status;
- supersession relation.

The important property is not merely that bytes are stored elsewhere.

It is that the system can address and update an explicit memory object under a declared read/write contract.

## 4. Retrieval is the read path, not the memory itself

RETRIEVAL-001 established:

> retrieval is a declared read operation over records, not a synonym for relevance, truth, provenance, or usefulness.

That distinction remains active here.

A perfectly maintained memory can still fail if retrieval:

- misses the record;
- applies the wrong filter;
- ranks badly;
- uses a stale index;
- returns an unauthorized version.

External storage and successful memory use are separate layers.

## 5. Continual learning is the parameter-update side

CONTINUAL-001 established that sequential parameter learning can alter earlier behavior.

It also separated:

- replay;
- consolidation/EWC;
- episodic gradient constraints;
- parameter isolation.

Those mechanisms matter because moving knowledge into parameters creates update obligations.

The external-memory thesis asks when some of those obligations can be avoided by leaving selected knowledge explicit.

## 6. The placement descriptor

For knowledge item or class `k`, use:

`Place(k)=(V,P,S,D,R,L,A,G)`.

The coordinates are:

- volatility `V`;
- provenance/audit need `P`;
- sharing scope `S`;
- deletion/supersession need `D`;
- retrievability/addressability `R`;
- latency/availability constraint `L`;
- access-control/privacy requirement `A`;
- value of parametric generalization/compression `G`.

The chapter defines no universal scalar score over these dimensions.

## 7. Why no scalar placement score?

Suppose one fact is highly volatile and provenance-critical.

That points toward external memory.

But suppose the same fact is required on every token with a hard microsecond latency budget.

That points toward parameterization or aggressive caching.

Neither fact cancels the other.

A placement decision must expose the tradeoff rather than hide it in an unexplained number.

## 8. Volatility favors explicit state

Some information changes often:

- current prices;
- active policies;
- account permissions;
- schedules;
- inventory;
- organizational decisions;
- scientific records under revision.

Repeatedly changing model weights for every update may be operationally awkward or behaviorally risky.

A versioned external record has a direct update operation.

That makes volatility one pressure toward externalization.

## 9. Provenance favors explicit state

Some claims must answer:

- where did this come from?
- which version?
- who authorized it?
- what replaced it?
- when was it observed?

A record can carry those fields directly.

A bare parameter vector does not, by itself, expose a per-fact source record.

This is a representation distinction, not a claim that parametric systems can never maintain provenance.

They can maintain auxiliary provenance externally.

## 10. Deletion and supersession favor explicit records

An explicit record can be marked:

- current;
- superseded;
- revoked;
- quarantined;
- deleted.

That does not make erasure trivial in replicated infrastructure.

But it gives the semantic operation a named target.

By contrast, removing one learned association from model behavior is a model-editing problem.

The two deletion semantics are not equivalent.

## 11. Sharing can favor external memory

Suppose ten agents need the same mutable operational fact.

One authoritative record can, in principle, be updated once.

Every agent can then retrieve the same current version.

But this advantage exists only if synchronization, access control, and freshness are well-defined.

A shared store with divergent caches can create multiple effective memories.

## 12. Addressability matters

Some knowledge naturally has a key:

- customer ID;
- document ID;
- theorem ID;
- experiment run;
- date;
- entity-relation pair;
- configuration name.

Such information is easy to imagine as an explicit memory record.

Other knowledge is diffuse.

There may be no sensible lookup key for:

- fluency;
- visual invariance;
- a learned optimization heuristic;
- a broad concept manifold.

Addressability is therefore a real placement coordinate.

## 13. Parametric compression has value

Parameters can compress many examples into reusable behavior.

The system does not need to retrieve every training example whenever it applies a learned rule.

This is a major advantage.

A database of examples is not the same thing as learning a representation or procedure from them.

External memory should not become an excuse to avoid learning stable structure.

## 14. Low-latency ubiquitous structure can favor parameters

Some knowledge is required constantly.

An explicit retrieval on every use may add:

- index lookup;
- memory traffic;
- network latency;
- synchronization;
- failure modes.

Parametric behavior is already present in the model's forward computation.

This can favor parameterization for stable, ubiquitous structure.

No universal latency ordering is claimed.

## 15. RAG makes the hybrid idea concrete

Lewis et al. combine a parametric sequence model with a dense non-parametric Wikipedia index [@LewisEtAl2020RAG].

Their formulation is useful here because it makes the two loci explicit:

- a learned parametric model;
- a retrievable external corpus.

The source also explicitly motivates retrieval in part through provenance and world-knowledge update limitations of parameter-only systems.

The Atlas uses this as one primary example, not as proof that RAG is the universal architecture.

## 16. kNN-LM shows datastore substitution

Khandelwal et al. augment a pretrained language model with a nearest-neighbor datastore.

In their reported experiments, changing the datastore supports domain adaptation without further model training.

The bounded architectural lesson is:

> some behavior can be changed by changing explicit memory while freezing the model.

That is exactly the update-separation property the external-memory thesis cares about.

## 17. RETRO shows scale, not universal superiority

Borgeaud et al. condition language modeling on chunks retrieved from a very large text database.

Their result demonstrates that explicit retrieved memory can complement model parameters at large scale.

It does not prove that every knowledge item belongs in retrieval.

Scale is evidence that the architecture is viable, not a universal placement rule.

## 18. ROME gives the necessary counterexample

Meng et al. show that specific factual associations can be edited directly in model parameters in their reported setting.

That matters because it blocks an overstrong thesis.

It would be false to say:

> mutable facts must always be external.

Parametric editing is possible.

The real question is which update semantics and system guarantees are desirable.

## 19. The exact parametric witness

Use two queries:

`A` and `B`.

Let:

`f_theta(A)=theta_1+theta_2`

and:

`f_theta(B)=theta_1-theta_2`.

Initial target facts are:

`A=2`

`B=0`.

The unique parameter vector is:

`theta=(1,1)`.

## 20. Updating one fact requires a coordinated edit here

Now change only the target for A:

`A:2 -> 4`

while preserving:

`B=0`.

The new unique parameter vector is:

`theta'=(2,2)`.

Therefore:

`Delta theta=(1,1)`.

Both coordinates change.

This is a property of the chosen representation.

It is not a theorem that factual parameter edits always require many changed weights.

## 21. A naive coordinate-local edit interferes

Change only:

`theta_1:1 -> 2`

and leave:

`theta_2=1`.

Then:

`f(A)=3`

and:

`f(B)=1`.

The edit fails twice:

- A does not reach 4;
- B no longer remains 0.

This is the smallest exact example of representation-induced edit coupling.

## 22. The external-store version

Represent the same two facts as records.

Initial state:

`A -> (2,s_A1,v1)`

`B -> (0,s_B1,v1)`.

Update A by adding:

`A -> (4,s_A2,v2,supersedes=v1)`.

B is unchanged.

A latest-version exact-key read now returns:

`A=4`

`B=0`.

Only logical key A changed.
