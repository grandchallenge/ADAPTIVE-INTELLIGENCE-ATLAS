# Retrieval and Associative Access
<!-- ATLAS-CH-RETRIEVAL-001 -->

**Epistemic status:** established information-retrieval/database/vector-search foundations + audited Memory Taxonomy and Attention prerequisites + Atlas synthesis + exact finite witness.  
**Specification:** manuscript/specifications/ATLAS-CH-RETRIEVAL-001.md  
**Formal packet:** mathematics/derivations/ATLAS-CH-RETRIEVAL-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-RETRIEVAL-001.md  
**Source lock:** sources/source-locks/ATLAS-CH-RETRIEVAL-001.yaml

A memory is useful only if a system can find the right part of it.

That sounds obvious.

The difficulty begins when we ask what **right** means.

A record can be right because:

- its exact key matches;
- its metadata satisfies a predicate;
- its vector is nearest to the query;
- its lexical score is highest;
- it survives a symbolic filter;
- it wins a fused rank;
- it is recent;
- it comes from an admissible source.

These are different retrieval contracts.

The governing rule of this chapter is:

> retrieval is a declared read operation over records, not a synonym for relevance, truth, provenance, or usefulness.

The same immutable records can support several retrieval behaviours.

That is not inconsistency.

It is the architecture.

## 1. Retrieval starts where the memory taxonomy stops

The Memory Taxonomy chapter wrote a memory object as

`M=(L,W,R,T,A,U,P,S)`

for storage locus, write path, read path, lifetime, addressability, mutability, provenance, and sharing.

Retrieval is chiefly about the read side:

`R`

and the addressability coordinate:

`A`.

But the other coordinates still matter.

A result may be easy to retrieve but stale.

A result may be relevant but lack provenance.

An index may be external while the record is ephemeral.

A query may be associative while the store itself is exact-key addressable.

So retrieval must not collapse the rest of the memory contract.

## 2. A retrieval contract

Let `D` be the underlying record set.

Write a retrieval contract as

`R=(D,Q,F,s,pi,k,O)`.

Here:

- `Q` is the query space;
- `F(q,D)` is an optional admissibility/filter operator;
- `s(q,d)` is a score, distance, or match relation;
- `pi` is a ranking/selection rule;
- `k` is a truncation or budget;
- `O` is the returned projection or set of fields.

This representation makes one fact explicit:

> a retrieval result is defined by more than a score.

The candidate set matters.

The filter matters.

The tie rule matters.

The top-k budget matters.

The fields returned matter.

Two systems can use the same embeddings and still implement different retrieval semantics.

## 3. Exact-key lookup

The simplest access contract is exact addressing.

Let every record carry a unique key:

`key(d) in K`.

Then exact-key retrieval asks for the unique record satisfying

`key(d)=u`.

This is not approximate.

It is not semantic.

It does not ask whether the key's record resembles the query.

A key is an address.

Dynamo is a large-scale systems example of key-value access in which a caller supplies a key and the system manages distributed storage and availability around that interface [@DeCandiaEtAl2007].

This chapter uses only the access distinction.

Replication, versioning, failure recovery, and consistency policies are separate systems concerns.

## 4. Key-value retrieval is not semantic retrieval

Suppose key

`invoice-2026-1042`

maps to a record.

The lookup can be exact even if:

- the record is obsolete;
- the payload is wrong;
- another record would be semantically more useful;
- the record has poor provenance.

Exactness refers to the address relation.

It does not certify the payload.

This distinction will recur throughout the chapter.

## 5. Symbolic retrieval

A symbolic query specifies conditions over structured fields.

Let

`P_q(d)`

be a predicate compiled from query `q`.

Then symbolic retrieval returns

`{d in D : P_q(d)}`.

Examples include:

- `year>=2024`;
- `type="paper"`;
- `source_id in approved_sources`;
- `status="audited"`;
- conjunctions and disjunctions of structured conditions.

Codd's relational model provides the foundational idea that data can be addressed through declarative relations and operations rather than by exposing physical storage layout [@Codd1970].

The Atlas takes a narrow lesson:

> symbolic admissibility can be specified independently of physical storage.

## 6. A predicate is not a ranking

The result of a predicate can be a set.

If a caller needs an ordered list, another rule is required.

For example:

- sort by date;
- sort by score;
- sort by source priority;
- rank by a learned model;
- apply a deterministic record-ID tie break.

So a system that says

> retrieve all approved papers

has specified admissibility.

It has not yet specified which approved paper should come first.

Selection and ranking are distinct operators.

## 7. Vector retrieval

Vector retrieval maps queries and records into a shared coordinate space.

Let

`phi_Q(q) in R^m`

and

`phi_D(d) in R^m`.

Then a distance-based retrieval rule can be written as

`d^*
in
argmin_{d in D}
delta(phi_Q(q),phi_D(d))`.

Or a similarity rule can maximize a score.

Salton, Wong, and Yang's vector-space model is a foundational information-retrieval construction in which stored objects and queries are compared through vector representations [@SaltonWongYang1975].

Modern learned embeddings change how the vectors are obtained.

They do not change the core fact that ranking is relative to a representation and a similarity geometry.

## 8. Similarity is representation-relative

Suppose two embedding models map the same records to different coordinates.

The nearest record can change.

Suppose the embeddings remain fixed but cosine similarity is replaced by Euclidean distance.

The ranking can change again.

Suppose vectors are normalized before scoring.

The ranking may change again.

Therefore the statement

> record A is nearest

is incomplete without:

- query embedding;
- record embedding;
- normalization rule;
- distance or similarity;
- candidate set.

Nearest is never representation-free.

## 9. A similarity score is not automatically relevance probability

A dense retriever can emit a score:

`s(q,d)`.

That score can be useful for ordering candidates.

But unless a separate calibration argument is established, it does not mean

`P(relevant | q,d)`.

Scores may be:

- inner products;
- cosine similarities;
- negative distances;
- logits;
- learned ranking outputs.

Their numerical scale can be arbitrary.

A score of 0.9 need not mean 90 percent relevant.

Ranking and probability calibration are different tasks.

## 10. Top-k is a budgeted truncation operator

Suppose candidate order is

`d_(1),...,d_(n)`.

Top-k returns only

`d_(1),...,d_(k)`.

This is a computational and interface decision.

It does not prove:

- the omitted records are irrelevant;
- the returned records are all relevant;
- the k-th score marks a natural semantic boundary.

Top-k converts an ordering into a bounded working set.

That is useful precisely because downstream systems cannot consume everything.

## 11. Tie rules matter for exact replay

Two records can have the same score.

If the system needs reproducible ordered output, it must declare a tie rule.

Examples include:

- stable record ID;
- insertion order;
- timestamp;
- secondary score.

Without such a rule, two conforming implementations can return different top-k lists while agreeing on all primary scores.

This is not always a problem.

But it matters when exact replay is part of the evidence contract.

## 12. Exact nearest neighbour

Exact nearest-neighbor search asks for the global optimum under the declared metric and candidate set.

For query `q`:

`NN(q,D)
=
argmin_{d in D}
delta(q,d)`.

If the store is small, exhaustive comparison may be acceptable.

At large scale, exhaustive search can become too expensive.

That motivates indexes and approximation.

## 13. Approximate nearest neighbour

Approximate nearest-neighbor search changes the search procedure.

The target remains similarity search.

The algorithm accepts some risk of missing the exact global nearest candidate in exchange for improvements such as:

- lower latency;
- lower query compute;
- better scalability;
- bounded memory structures;
- practical billion-scale search.

Malkov and Yashunin's HNSW algorithm is one graph-based approximate nearest-neighbor construction [@MalkovYashunin2020].

Its layered navigable graph is a search structure.

The crucial Atlas boundary is:

> an ANN result is not silently identical to the exact nearest-neighbor result.

## 14. Search approximation and representation error are different

Imagine the truly task-relevant record is semantically important but badly embedded.

Exact nearest-neighbor search can retrieve the wrong semantic record perfectly.

That is not an index failure.

The index exactly solved the wrong geometric proxy.

Now reverse the case.

Suppose the embedding geometry puts the relevant record closest to the query, but an approximate index misses it.

That is a search/index approximation failure.

So separate:

1. representation error;
2. search/index error;
3. downstream relevance error.

Without this separation, retrieval diagnostics become confused.

## 15. Sparse and lexical retrieval

Not every retrieval system needs dense embeddings.

Classical text retrieval can score overlap and term evidence through sparse representations.

The probabilistic relevance framework and BM25 family are an important lineage for such ranking [@RobertsonZaragoza2009].

Sparse lexical systems can be attractive because their matching evidence is often easier to inspect:

- term occurrence;
- term frequency;
- document frequency;
- field structure.

Dense systems can recover conceptual proximity that exact lexical overlap misses.

Neither representation dominates universally.

## 16. Symbolic, sparse, and dense are different axes

It is tempting to place all retrieval into two boxes:

- lexical;
- vector.

That misses structured predicates.

A symbolic filter such as

`source="primary" AND year>=2024`

does not need to behave like BM25 or embedding similarity.

It declares admissibility.

A complete retrieval architecture may therefore combine:

- symbolic filtering;
- sparse lexical scoring;
- dense similarity;
- recency weighting;
- source constraints.

The composition rule is the system.

## 17. One store can have many indices

A record can be reachable through:

- primary key;
- metadata index;
- inverted lexical index;
- vector index;
- temporal index;
- provenance index.

These do not necessarily duplicate the logical record.

They are access structures.

This gives a useful invariant:

`record_id != index_entry_id`.

One logical record may have several index entries.

Changing or deleting the record can therefore require coordinated index maintenance.

## 18. Multi-index retrieval

The phrase **multi-index** can mean more than one thing.

At the broad architecture level, the Atlas uses it for multiple access structures over one record set.

At the algorithm level, Babenko and Lempitsky's inverted multi-index is a specific similarity-search construction based on product quantization [@BabenkoLempitsky2012].

These meanings should not be conflated.

The paper establishes one concrete structured vector-search index.

The Atlas generalization is an architectural synthesis:

> one record identity can participate in several independent retrieval access paths.

## 19. Hybrid retrieval requires composition semantics

The word **hybrid** is often too vague.

A hybrid retriever might mean:

- symbolic filter, then vector rank;
- lexical candidate generation, then dense reranking;
- dense and sparse score fusion;
- vector candidates intersected with policy constraints;
- several retrievers feeding a learned reranker.

These pipelines are not equivalent.

A serious description should state the operator order.

## 20. Exact witness store

Use three immutable records.

A:

- id = A;
- kind = paper;
- year = 2024;
- vector = `(1,0)`;
- value = alpha.

B:

- id = B;
- kind = paper;
- year = 2022;
- vector = `(4/5,3/5)`;
- value = beta.

C:

- id = C;
- kind = note;
- year = 2025;
- vector = `(24/25,1/25)`;
- value = gamma.

Query vector:

`q=(19/20,1/20)`.

Use squared Euclidean distance.

Nothing about the records changes across the following reads.

## 21. Exact vector distances

To A:

`d(q,A)^2=1/200`.

To B:

`d(q,B)^2=13/40`.

To C:

`d(q,C)^2=1/5000`.

Therefore:

`C,A,B`

is the exact vector ranking.

Unfiltered top-1 is C.

## 22. Exact-key read of the same store

Ask for:

`id=B`.

The answer is B.

Vector proximity is irrelevant.

The store did not change.

The access contract did.

This is the same structural lesson established abstractly by MEMTAX-001, now made specific to retrieval.

## 23. Symbolic read of the same store

Ask for:

`year>=2024`.

A qualifies.

B does not.

C qualifies.

So the result set is:

`{A,C}`.

This query defines admissibility but not an order.

A secondary ranking clause would be required to choose which record comes first.

## 24. Hybrid retrieval does not generally commute

Now require:

`kind=paper`

and also rank by vector distance.

There are at least two plausible pipelines.

### Filter then rank

First keep papers:

`{A,B}`.

Then rank by distance.

A is closer.

Top-1 result:

`A`.

### Rank then filter

First rank the full store.

Top-1 is C.

Then apply the paper predicate.

C fails.

The result is empty.

Thus:

`FilterThenRank != RankThenFilter`.

The difference arises only from operator order and top-k truncation.

## 25. Why filter-then-rank often has cleaner semantics

If a symbolic predicate means

> only these records are admissible,

then applying it before ranking ensures the ranking operates inside the permitted set.

This is particularly important for constraints such as:

- approved sources;
- tenant boundaries;
- date windows;
- document status;
- legal access permissions.

But the Atlas does not declare filter-first universally superior.

Other pipelines can be legitimate.

The requirement is to state what the operators mean.

## 26. Score fusion is another hybrid family

Suppose a document has sparse score

`s_sparse(q,d)`

and dense score

`s_dense(q,d)`.

A fused ranker may use:

`s_hybrid
=
lambda s_sparse
+
(1-lambda)s_dense`

after suitable normalization.

This immediately creates new questions:

- are the score scales commensurate?
- how is `lambda` chosen?
- what happens when one retriever has no score?
- are ranks fused instead of raw scores?
- is the rule query-dependent?

Calling the system hybrid does not answer them.

## 27. Retrieval can be staged

A large corpus may use a cheap first stage to generate candidates and a more expensive second stage to rerank them.

Write:

`D
-> C_k(q)
-> Rank_expensive(C_k(q))`.

This reduces cost.

It can also introduce a hard ceiling:

if the relevant record never enters the candidate set, the reranker cannot recover it.

Candidate recall and reranker quality are therefore separate quantities.

## 28. Attention and retrieval overlap at the operator level

ATTNOP-001 showed attention as a state-dependent operator built from query-key scores and values.

Retrieval can share the pattern:

`query
-> candidate scores
-> selection
-> returned values`.

This resemblance is real.

It does not make attention and retrieval architecturally identical.

## 29. Retrieval can exceed the active field

Attention normally operates over the keys and values supplied to the active computation.

A retriever can search:

- a database;
- a document collection;
- a vector index;
- a file store;
- a shared organizational memory.

The persistent corpus can be much larger than the active context.

Retrieval therefore often acts as the bridge between long-lived memory and bounded working context.

## 30. Retrieval can use hard identity

Attention weights usually mix supplied values.

Retrieval can instead return explicit record identities.

That creates capabilities such as:

- source citation;
- stable replacement;
- deletion;
- access control;
- provenance lookup;
- deduplication.

The record can remain independently addressable after retrieval.

This becomes central in the External-Memory chapter.

## 31. Retrieval is not causal explanation

A high retrieval score says:

> this candidate ranked highly under this retrieval contract.

It does not say:

> this record caused the final output.

A downstream model may:

- ignore it;
- contradict it;
- combine it with other records;
- distort it;
- fail for unrelated reasons.

ATTNOP-001 already enforced the analogous boundary for attention coefficients.

The same discipline applies here.

## 32. Retrieval and provenance

Suppose record A ranks first.

The score does not tell us:

- where A came from;
- who authored it;
- whether it has been superseded;
- which transformation produced its embedding;
- whether it was audited.

Those belong to the record/provenance system.

A governed retriever should preserve a path from result to stable record identity and source metadata when downstream claims depend on provenance.

## 33. Rank does not create authority

A record can rank first because its vector is close.

That does not promote it to:

- verified;
- approved;
- authoritative;
- current.

A retrieval index is not an adjudicator.

The Evidence and Replay chapters remain relevant whenever retrieved material is used to support claims.

## 34. Retrieval correctness, relevance, and usefulness

Three distinct questions are:

1. **contract correctness:** did the retriever return what its algorithm specifies?
2. **task relevance:** does the record bear on the user's task?
3. **downstream usefulness:** does giving the record to the consumer improve the objective?

A result can be correct under the retrieval contract and irrelevant to the task.

A relevant record can be too long for the available context.

A useful summary can rank below a less useful full document under raw similarity.

Evaluation should therefore name which layer it measures.

## 35. Recall and precision require a relevance judgment

Information retrieval metrics such as precision and recall need a declared notion of relevance.

For retrieved set `S` and relevant set `G`:

`precision=|S intersect G|/|S|`

and

`recall=|S intersect G|/|G|`

when denominators are nonzero.

The formulas are simple.

The hard question is how `G` is defined.

Human labels, task outcomes, source policies, and benchmark annotations can produce different relevance notions.

Metrics inherit that choice.

## 36. ANN recall is not semantic recall

Approximate-nearest-neighbor evaluation often asks whether the ANN method recovered exact nearest neighbors under a metric.

That is an index-quality question.

Semantic retrieval recall asks whether task-relevant records were found.

These should not be conflated.

An ANN system can have perfect recall relative to exact vector nearest neighbors while the vector model itself has poor semantic recall.

Again:

representation and search are separate layers.

## 37. Retrieval-augmented generation is downstream composition

Lewis et al. combine a parametric generator with a dense vector index used as non-parametric memory [@LewisEtAl2020RAG].

This is a useful architecture example because it makes retrieval a distinct stage in a larger model.

The retrieval stage can be inspected separately from generation.

But retrieval augmentation does not create a theorem that generated answers are true.

The pipeline can fail at:

- query representation;
- index search;
- relevance;
- context assembly;
- generation;
- interpretation.

Each layer deserves its own evidence.

## 38. Retrieval is not memory writing

A read can be excellent while the memory is stale.

A memory can be correct while the retriever is weak.

A retriever can repeatedly surface one record without changing the store.

This preserves the MEMTAX distinction:

- write path;
- read path;
- lifetime;
- mutability.

Retrieval is one side of the memory interface.

## 39. Retrieval under updates

When records change, indexes may need maintenance.

A system should be able to state whether updates are:

- synchronous;
- asynchronous;
- transactional;
- eventually indexed;
- versioned.

A record can exist in the source store before it becomes visible to one index.

That creates a freshness gap.

The chapter records the issue but does not develop distributed consistency.

That belongs to systems/coordination layers.

## 40. Deletion is also a retrieval property

If a record is deleted from the canonical store but remains in an index, retrieval can surface a ghost.

If an index deletes the vector but the canonical record remains, one access path disappears while others survive.

So deletion semantics require:

- canonical record identity;
- index maintenance;
- visibility rules.

This is another reason record and index identity must remain separate.

## 41. Multi-index consistency

Suppose one record has:

- primary-key entry;
- lexical postings;
- vector node;
- time index.

An update to the record can leave these access structures temporarily inconsistent.

The retrieval layer should therefore distinguish:

- logical record version;
- index version;
- query-time snapshot.

The chapter does not prescribe a transaction protocol.

It makes the state distinction visible.

## 42. Retrieval budgets shape cognition

A downstream model rarely receives the full store.

It receives a working set.

The retrieval budget `k` therefore shapes what information becomes available for reasoning.

A small `k` can exclude complementary evidence.

A large `k` can consume context and introduce distractors.

So retrieval is not only a search problem.

It is a compilation boundary between persistent memory and active computation.

The later Context Compilation chapter will build on this.

## 43. The nearest record need not be the best context item

Suppose one highly similar document repeats the query without adding evidence.

A slightly less similar record may contain the decisive fact.

Vector similarity can therefore be a useful proxy without being the downstream utility function.

Possible downstream reranking signals include:

- novelty;
- coverage;
- provenance quality;
- contradiction;
- diversity;
- recency;
- task-specific expected utility.

The Atlas keeps these as separate design layers.

## 44. Diversification changes the objective

Top-k nearest-neighbor retrieval can return near-duplicates.

A diversified retriever may intentionally sacrifice some score to cover different aspects of a query.

Then its objective is no longer:

> return the k highest individual scores.

It becomes a set-selection problem.

The distinction matters when evaluating retrieval quality.

Individual rank and set utility are different objects.

## 45. Retrieval over governed records

A governed store can expose symbolic fields such as:

- epistemic class;
- review state;
- source identity;
- supersession state;
- authority;
- validity interval.

These fields can participate in filters.

That makes retrieval policy-aware.

But the filter must not invent those statuses.

It can only consume statuses established elsewhere.

Retrieval applies governance metadata.

It does not create governance authority.

## 46. Failure modes

### Address conflation

Treat exact key match as semantic relevance.

### Similarity laundering

Treat nearest vector as correct answer.

### Score calibration fiction

Interpret arbitrary ranking scores as probabilities.

### Top-k completeness fiction

Treat omitted records as irrelevant.

### ANN/exact conflation

Describe approximate search output as the exact global nearest neighbour without verification.

### Hybrid ambiguity

Say "hybrid retrieval" without specifying operator order or fusion.

### Index/record conflation

Treat multiple index entries as multiple independent records.

### Provenance laundering

Infer source authority from retrieval rank.

### Retrieval/generation conflation

Treat a retrieval-augmented answer as correct because retrieval occurred.

### Read/write conflation

Treat a retrieval improvement as a memory freshness improvement.

## 47. A practical retrieval ledger

Before evaluating a retriever, record:

| Field | Question |
|---|---|
| corpus | What records are eligible in principle? |
| record identity | What is the stable logical record ID? |
| query | How is the query represented? |
| filter | What makes a record admissible? |
| index | Which access structure is searched? |
| representation | Sparse, dense, symbolic, mixed? |
| score | What quantity orders candidates? |
| approximation | Exact or approximate search? |
| budget | What is k or the candidate limit? |
| tie rule | How are equal scores ordered? |
| projection | Which fields are returned? |
| provenance | How is source identity preserved? |
| relevance target | What labels or task define relevance? |
| downstream target | What consumer/usefulness metric matters? |

This is the minimum grammar needed to interpret a retrieval result.

## 48. What the exact witness establishes

The companion witness proves four facts about one immutable finite store.

First:

`id=B`

returns B by exact key.

Second:

`year>=2024`

returns the symbolic set

`{A,C}`.

Third, vector ranking under the declared squared Euclidean geometry is:

`C,A,B`.

Fourth, with the paper predicate:

- filter-then-rank top-1 returns A;
- rank-top-1-then-filter returns nothing.

Therefore retrieval semantics depend on the read contract and operator order even before learned embeddings, ANN approximations, or large-scale infrastructure are introduced.

## 49. Downstream handoff

**The External-Memory Thesis — ATLAS-CH-EXTMEM-001** may now assume:

- exact-key versus associative access;
- symbolic predicate retrieval;
- vector similarity retrieval;
- top-k semantics;
- ANN versus exact-NN distinction;
- multiple indices over one record identity;
- explicit hybrid-composition rules;
- provenance preservation;
- retrieval correctness versus relevance versus downstream usefulness.

The downstream chapter must independently argue:

- which information should leave model parameters;
- which memory loci should persist;
- how shared memory changes system architecture;
- what update/provenance/governance contract makes external memory preferable.

Retrieval provides access.

It does not by itself establish the case for externalization.

## References used in this chapter

- Salton, Wong, and Yang, *A Vector Space Model for Automatic Indexing* [@SaltonWongYang1975].
- Codd, *A Relational Model of Data for Large Shared Data Banks* [@Codd1970].
- Robertson and Zaragoza, *The Probabilistic Relevance Framework: BM25 and Beyond* [@RobertsonZaragoza2009].
- Malkov and Yashunin, *Efficient and Robust Approximate Nearest Neighbor Search Using Hierarchical Navigable Small World Graphs* [@MalkovYashunin2020].
- Babenko and Lempitsky, *The Inverted Multi-Index* [@BabenkoLempitsky2012].
- DeCandia et al., *Dynamo: Amazon's Highly Available Key-value Store* [@DeCandiaEtAl2007].
- Lewis et al., *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks* [@LewisEtAl2020RAG].

Exact source identities and authority boundaries are recorded in:

sources/source-locks/ATLAS-CH-RETRIEVAL-001.yaml
