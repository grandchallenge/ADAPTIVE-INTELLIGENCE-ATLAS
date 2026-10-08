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

For knowledge item or class $k$, use:

\[
\operatorname{Place}(k)=(V,P,S,D,R,L,H,A,G).
\]

The coordinates are:

- volatility $V$;
- provenance/audit need $P$;
- sharing scope $S$;
- deletion/supersession need $D$;
- retrievability/addressability $R$;
- latency constraint $L$;
- availability/failure-tolerance requirement $H$;
- access-control/privacy requirement $A$;
- value of parametric generalization/compression $G$.

The chapter defines no universal scalar score over these dimensions. External locus and persistence also remain distinct: this thesis focuses on persistent external records when that lifetime is deliberately chosen; it does not redefine every external memory object as persistent.

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

Khandelwal et al. augment a pretrained language model with a nearest-neighbor datastore [@KhandelwalEtAl2020].

In their reported experiments, changing the datastore supports domain adaptation without further model training.

The bounded architectural lesson is:

> some behavior can be changed by changing explicit memory while freezing the model.

That is exactly the update-separation property the external-memory thesis cares about.

## 17. RETRO shows scale, not universal superiority

Borgeaud et al. condition language modeling on chunks retrieved from a very large text database [@BorgeaudEtAl2022].

Their result demonstrates that explicit retrieved memory can complement model parameters at large scale.

It does not prove that every knowledge item belongs in retrieval.

Scale is evidence that the architecture is viable, not a universal placement rule.

## 18. ROME gives the necessary counterexample

Meng et al. show that specific factual associations can be edited directly in model parameters in their reported setting [@MengEtAl2022].

That matters because it blocks an overstrong thesis.

It would be false to say:

> mutable facts must always be external.

Parametric editing is possible.

The real question is which update semantics and system guarantees are desirable.

## 19. The exact parametric witness

Use two queries:

$A$ and $B$.

Let:

\[
f_\theta(A)=\theta_1+\theta_2
\]

and:

\[
f_\theta(B)=\theta_1-\theta_2.
\]

Initial target facts are:

\[
f_\theta(A)=2, \qquad f_\theta(B)=0.
\]

The unique parameter vector is:

\[
\theta=(1,1).
\]

## 20. Updating one fact requires a coordinated edit here

Now change only the target for A:

\[
A: 2 \to 4
\]

while preserving:

\[
f_\theta(B)=0.
\]

The new unique parameter vector is:

\[
\theta'=(2,2).
\]

Therefore:

\[
\Delta \theta=(1,1).
\]

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

Update A by making the version transition explicit:

`A,v1 -> (2,s_A1,v1,status=superseded)`

`A,v2 -> (4,s_A2,v2,status=current,supersedes=v1)`.

B is unchanged and current.

A latest-version exact-key read now returns:

`A=4`

`B=0`.

Only logical key A changed.


## 23. Record-locality is not compute optimality

The external witness changes one logical key.

That is a statement about state mutation locality.

It does not prove that the external update uses fewer machine operations than a model edit.

The database may replicate records, rebuild indexes, invalidate caches, or synchronize across regions.

Representation-locality and systems cost are different claims.

## 24. Provenance is explicit in the store

The external records retain:

`s_A1`

for version 1 and:

`s_A2`

for version 2.

The supersession edge preserves the update history.

The bare parameter vector:

`theta=(1,1)`

does not itself expose which source supported fact A.

Again, the correct conclusion is not:

> parameters cannot have provenance.

The correct conclusion is:

> provenance is not encoded as an explicit per-fact record in the bare parameter representation.

## 25. The stale-read counterexample

External memory creates a new failure mode.

Suppose one consumer still reads snapshot `M_1` after the authoritative store advances to `M_2`.

The authoritative latest value is:

`A=4`.

The stale consumer still observes:

`A=2`.

Externalization has made updating the authoritative record easy.

It has not made every read fresh.

## 26. Freshness needs a contract

Let:

`v_star(k)`

be the authoritative current version for key `k`.

Let:

`v_C(k)`

be the version observed by consumer `C`.

A strict freshness rule might require:

`v_C(k)=v_star(k)`.

A bounded-staleness policy might permit some lag.

The point is architectural:

> freshness must be specified.

It is not implied by the word **memory**.

## 27. Caching creates local memory again

A system may externalize knowledge into a shared store and then cache retrieved results near each model instance.

That is often sensible for latency.

It also means the system now has several memory loci:

- authoritative store;
- retrieval index;
- cache;
- working context;
- parameters.

The memory taxonomy has returned.

Externalization does not make the architecture simple.

It makes some state explicit.

## 28. Write correctness and read correctness differ

A memory update can be correct while a later answer is wrong.

Possible causes include:

- stale cache;
- stale index;
- wrong query;
- wrong filter;
- wrong rank;
- context omission;
- downstream reasoning error.

This separation matters operationally.

It lets the system ask:

> did we store the right fact?

before asking:

> did the model use it correctly?

## 29. Retrieval failure is not memory-write failure

Suppose version 2 of A is present and current.

A vector retriever fails to return it.

That is a read-path failure.

Rewriting the memory record will not necessarily fix it.

The correct repair may be in:

- indexing;
- query formulation;
- ranking;
- filters;
- context compilation.

Typed failure boundaries prevent useless updates.

## 30. Poisoning is a memory-layer risk

Explicit memory can be modified.

That is an advantage for legitimate updates.

It is also an attack surface.

A malicious or low-quality record can be:

- inserted;
- ranked highly;
- given false metadata;
- propagated to many consumers.

External memory therefore needs evidence and authority controls, not only retrieval quality.

## 31. Access control becomes first-class

A shared store may contain facts that not every agent may read.

Let:

`allow(agent,key,operation)`

be an authorization predicate.

A successful lookup should not bypass this predicate merely because the record is relevant.

This creates another separation:

> retrievable does not mean authorized.

The downstream Polity chapter will need this distinction.

## 32. Sharing is not global visibility

A memory can be shared among:

- one team;
- one model family;
- one tenant;
- one organization;
- one scientific programme.

Shared does not mean public.

Scope is part of the memory contract.

This is especially important when memory contains private, licensed, embargoed, or role-restricted information.

## 33. Deletion is not trivial even externally

An explicit record can be marked deleted or revoked.

But copies may remain in:

- caches;
- replicas;
- logs;
- backups;
- derived indexes;
- compiled contexts.

Therefore external memory gives deletion a clear target but not necessarily immediate total erasure.

A serious system must define deletion propagation.

## 34. Parametric erasure is a different problem

If information has been learned into parameters, deleting the original training record does not imply the behavior disappears.

The two operations target different objects.

This distinction is especially important for systems with both:

- learned parametric state;
- retained external records.

Deletion policy should say which loci are in scope.

## 35. Consolidation moves in the other direction

The external-memory thesis is not a one-way migration out of parameters.

Sometimes repeated external evidence becomes stable enough that learning it into parameters is useful.

Call this **consolidation**.

Examples might include:

- repeated tool-use patterns;
- stable schema structure;
- durable domain regularities;
- procedural skills.

Consolidation is a parameter-learning operation.

It is distinct from memory write.

## 36. Externalization can precede consolidation

A system can first store new evidence externally because it is:

- recent;
- uncertain;
- volatile;
- provenance-sensitive.

Later, after enough evidence accumulates, some stable regularity can be learned parametrically.

This creates a useful architecture:

> explicit first, consolidate later.

The chapter presents this as a design pattern, not a theorem of optimal learning.

## 37. Parameter isolation and external memory solve different problems

CONTINUAL-001 showed that parameter isolation can avoid direct overwrite by adding capacity or routing.

External memory avoids some parameter updates by moving selected state elsewhere.

Those are not the same strategy.

Parameter isolation still places knowledge in learned capacity.

Externalization places it in explicit records.

The costs differ.

## 38. Replay uses external evidence without making it the final answer source

Replay stores examples or exemplars externally.

During learning, those records return to the optimizer.

This is different from runtime retrieval of a fact for direct use.

So even within one system, external records can have multiple roles:

- training evidence;
- episodic replay;
- semantic knowledge;
- runtime retrieval;
- audit/provenance archive.

Role should not be inferred from locus alone.

## 39. A record is not automatically knowledge

An external store can contain:

- false statements;
- conflicting statements;
- stale statements;
- unsupported statements;
- low-authority sources.

The system still needs:

- provenance;
- ranking;
- authority;
- reconciliation;
- uncertainty handling.

External memory makes records inspectable.

It does not make them true.

## 40. Multiple records can legitimately conflict

Suppose two sources disagree.

Parameter-only consolidation may blur the conflict into one behavior.

An external store can preserve both records explicitly.

That can be useful when the disagreement itself matters.

But then the reader must decide:

- which source is authoritative;
- whether both are shown;
- whether uncertainty is retained.

Preserving conflict is not the same as resolving it.

## 41. Update frequency is only one axis

A highly volatile fact often favors external memory.

But a rarely changing fact can also be external if:

- provenance is critical;
- deletion must be possible;
- sharing is required;
- access policy is complex.

Conversely, some moderately changing information may still be parameterized if retrieval is too costly.

Placement is multi-dimensional.

## 42. The "world in weights" failure mode

A system that tries to carry every changing fact in parameters inherits several burdens:

- weight updates for factual changes;
- unclear per-fact provenance;
- difficult selective deletion;
- duplicated updates across model copies;
- interference risk;
- stale deployed checkpoints.

This is the core motivation for the external-memory thesis.

But the remedy must not become a slogan.

## 43. The "database as intelligence" failure mode

The opposite mistake is to externalize everything.

A datastore does not replace:

- abstraction;
- reasoning;
- representation learning;
- compression;
- procedure learning;
- transfer.

If every answer requires finding a memorized record, the system may fail whenever exact evidence is absent.

External memory should complement learned capability.

## 44. The hybrid architecture

A mature system may use four layers:

1. **parameters** for compressed reusable structure;
2. **persistent external memory** for explicit versioned records;
3. **retrieval** for selecting candidate evidence;
4. **working context** for the task-specific subset currently active.

The next chapter, Context Compilation, will develop layer 4.

This chapter stops before that step.

## 45. A practical placement ledger

Before moving a knowledge class into or out of parameters, record:

| Field | Question |
|---|---|
| item/class | What knowledge is being placed? |
| volatility | How often does it change? |
| provenance | Must source/version be visible per item? |
| sharing | Which agents/models need one common state? |
| supersession | Must updates, revocation, or deletion be explicit? |
| retrievability | Is there a meaningful key/query/index? |
| latency | Can retrieval cost be tolerated? |
| availability | What happens if the store is unavailable? |
| access control | Who may read/write it? |
| privacy | Does explicit storage create new exposure? |
| generalization | Is compression into reusable behavior valuable? |
| consolidation | Should stable evidence later move into parameters? |
| freshness | Which version guarantees are required? |
| fallback | What should happen on retrieval failure? |

This ledger turns "put it in memory" into an auditable design decision.

## 46. Failure modes

### External-equals-fresh

The record is updated but consumers use stale snapshots.

### External-equals-correct

A stored record is treated as true merely because it is explicit.

### Retrieved-equals-authorized

A relevant record bypasses access policy.

### Parameter-change-equals-forgetting

Any weight movement is called forgetting without behavioral evaluation.

### External-equals-cheap

Record-local updates are assumed to imply lower wall-clock cost.

### Parametric-equals-uneditable

Direct model editing is ignored despite evidence that some factual associations can be changed parametrically.

### Shared-equals-consistent

Multiple agents point to one store, so consistency is assumed without version/synchronization semantics.

### Externalize-everything

Explicit memory is treated as a replacement for learning compressed structure.

## 47. What the exact witness establishes

The companion witness proves only that, for the chosen two-fact representations:

- initial parameter state is `(1,1)`;
- updated parameter state is `(2,2)`;
- both parameter coordinates change under the exact preserving update;
- the naive one-coordinate edit produces `A=3,B=1`;
- the external latest-version update changes only logical key A;
- external provenance retains old/new source/version information;
- a stale snapshot still returns A=2 after authoritative A becomes 4.

It does not prove universal systems superiority.

## 48. Downstream handoff: Context Compilation

**ATLAS-CH-CONTEXTCOMP-001** may now assume:

- hybrid parametric/external placement;
- versioned external records;
- freshness as an explicit policy;
- retrieval success as distinct from storage correctness;
- provenance-preserving record semantics.

It must independently define how retrieved records become the bounded working context of a model invocation.

## 49. Downstream handoff: Polity

**ATLAS-CH-POLITY-001** may now assume:

- shared memory is an explicit architectural locus;
- shared visibility requires synchronization/version semantics;
- access control is distinct from relevance;
- common memory can coexist with private parametric and working state.

It must independently define multi-agent governance, coordination, authority, and shared-state policy.

## References used in this chapter

- Lewis et al., *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks* [@LewisEtAl2020RAG].
- Khandelwal et al., *Generalization through Memorization: Nearest Neighbor Language Models* [@KhandelwalEtAl2020].
- Borgeaud et al., *Improving language models by retrieving from trillions of tokens* [@BorgeaudEtAl2022].
- Meng et al., *Locating and Editing Factual Associations in GPT* [@MengEtAl2022].

Exact source identities and authority boundaries are recorded in:

sources/source-locks/ATLAS-CH-EXTMEM-001.yaml
