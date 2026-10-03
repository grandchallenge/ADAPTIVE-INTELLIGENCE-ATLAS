# ATLAS-CH-RETRIEVAL-001 — Formal and Derivation Packet

## 1. Retrieval contract

Let the immutable record set be `D`.

Define a retrieval contract

`Retr=(D,Q,F,s,pi,k,O)`

with:

- query space `Q`;
- admissibility/filter operator `F`;
- score or match relation `s`;
- ranking/selection rule `pi`;
- truncation budget `k`;
- returned projection `O`.

The output is determined by the complete contract, not by the stored records alone.

## 2. Exact-key lookup

Let every record have a unique key.

For query key `u`, define

`R_key(u)=d`

iff

`key(d)=u`.

If no such record exists, return no record.

If keys are required unique, multiple matches are an integrity defect rather than a ranking problem.

Exact-key retrieval is address-based.

## 3. Symbolic selection

Let query `q` compile to a predicate

`P_q:D->{true,false}`.

Then

`R_sym(q)
=
{d in D : P_q(d)}`.

This operation defines admissibility.

It need not define an ordering.

A separate order/rank clause is required if a deterministic ordered result is desired.

## 4. Vector retrieval

Let

`phi_Q(q),phi_D(d) in R^m`.

For a distance function `delta`, exact nearest-neighbor retrieval is

`d^*
in
argmin_{d in D}
delta(phi_Q(q),phi_D(d))`.

For top-k retrieval, sort by the declared score/distance and select the first k, with a declared deterministic tie-break rule if exact replay matters.

Similarity search is therefore representation-relative:

changing `phi_Q`, `phi_D`, normalization, or `delta` can change the ranking without changing the records.

## 5. Score is not relevance probability

A score

`s(q,d)`

can be used to rank records without satisfying

`s(q,d)=P(relevant | q,d)`.

Calibration is an additional property.

Therefore:

`rank score != calibrated relevance probability`

unless a calibration claim is separately established.

## 6. Top-k truncation

Let a total order under score be

`d_(1),...,d_(n)`.

Then

`TopK_k(D)=(d_(1),...,d_(k))` as an ordered list.

Its underlying selected set is

`TopKSet_k(D)={d_(1),...,d_(k)}`.

Records outside the set are omitted because of the budget/order.

No logical conclusion

`d not in TopKSet_k(D) => irrelevant(d)`

follows from truncation alone.

## 7. Exact finite store

Define:

`A=(A,paper,2024,(1,0),alpha)`;

`B=(B,paper,2022,(4/5,3/5),beta)`;

`C=(C,note,2025,(24/25,1/25),gamma)`.

Fields are:

`(id,kind,year,vector,value)`.

Query vector:

`q=(19/20,1/20)`.

Distance:

squared Euclidean distance.

## 8. Exact distance calculations

For A:

`q-A=(-1/20,1/20)`.

Therefore

`d_A^2
=
1/400+1/400
=
1/200`.

For B:

`q-B=(3/20,-11/20)`.

Therefore

`d_B^2
=
9/400+121/400
=
130/400
=
13/40`.

For C:

`q-C=(-1/100,1/100)`.

Therefore

`d_C^2
=
1/10000+1/10000
=
1/5000`.

Hence

`1/5000 < 1/200 < 13/40`.

The exact vector ranking is:

`C, A, B`.

## 9. Exact-key witness

For key query B:

`R_key(B)=B`.

The distance ordering does not matter.

This establishes that exact-key and vector access can select different records from the same store.

## 10. Symbolic witness

Predicate:

`P(d): year(d)>=2024`.

Then:

- A satisfies P;
- B does not;
- C satisfies P.

Therefore:

`R_sym(P)={A,C}`.

No ranking is implied by this set.

## 11. Hybrid filter-then-rank

Let predicate:

`P_paper(d): kind(d)=paper`.

Then:

`F_paper(D)={A,B}`.

Ranking that admissible set by vector distance gives:

`A,B`.

So:

`Top1(Rank(F_paper(D)))=A`.

## 12. Hybrid rank-then-filter

Rank the full set first.

The global vector top-1 is:

`C`.

Apply paper filter after top-1:

`P_paper(C)=false`.

Therefore the result is empty.

So, exactly:

`FilterThenRank_1(q,D)=A`;

`Filter(RankTop1(q,D))=empty`.

The operators do not commute.

## 13. Why the noncommutation matters

The two pipelines differ because top-k truncation discards information before the filter is applied in the second pipeline.

In general:

`TopK(F(D))`

need not equal the order-preserving filtered sequence

`Filter(TopK(D))`.

Equality requires additional conditions, for example that the globally selected top-k records already satisfy the filter strongly enough to fill the requested result budget.

Hybrid retrieval must therefore declare composition order.

## 14. Multiple indices, one record identity

Suppose record A is reachable through:

- primary key index;
- year/kind metadata index;
- vector index.

These are three index entries/access paths pointing to the same logical record.

The index identifiers are not new epistemic records.

A useful architecture keeps:

`record_id != index_entry_id`

as separate concepts.

Updating one record may require maintaining several index structures consistently.

## 15. Multi-index vector search

The inverted multi-index of Babenko–Lempitsky provides one concrete vector-search example where the vector space is decomposed and indexed using product quantization.

The Atlas uses it to establish existence of structured multi-part indexing.

It does not infer that every system with several access paths implements that algorithm.

## 16. Exact versus approximate nearest neighbor

Define exact nearest-neighbor result:

`NN(q,D)=argmin_{d in D}delta(q,d)`.

An approximate algorithm returns a candidate according to its index/search procedure.

The semantic distinction is:

- exact NN: global optimum under declared metric and candidate set;
- ANN: algorithmically approximated search result, evaluated through measures such as recall, latency, memory, or problem-specific approximation guarantees.

HNSW is one graph-based ANN method.

The chapter does not assume it returns the exact nearest neighbor for every query.

## 17. Approximation and representation are different error sources

Suppose an embedding places the task-relevant record far from the query.

Exact nearest-neighbor search can still return the wrong record for the semantic task.

That is a representation/relevance defect, not a search-approximation defect.

Conversely, the embedding may place the relevant record nearest, while an approximate index fails to retrieve it.

That is an index/search defect.

Therefore separate:

1. representation error;
2. search/index approximation error;
3. downstream relevance/usefulness error.

## 18. Attention versus retrieval

ATTNOP-001 defines state-dependent query/key similarity and value mixing inside attention.

Retrieval can share the structure:

`query -> score candidates -> select/mix`.

But retrieval can also include:

- persistent stores;
- exact record IDs;
- hard filters;
- non-differentiable indices;
- asynchronous updates;
- top-k candidate materialization.

Thus:

`attention-like scoring`

does not imply:

`same memory architecture`.

## 19. Key-value retrieval

For mapping

`K: key -> value`,

a key-value read returns the value associated with a supplied key under the store's declared semantics.

Dynamo is a representative large-scale key-value systems source.

This chapter uses only the access-interface distinction.

Availability, replication, consistency, versioning, and conflict resolution are separate systems properties.

## 20. Retrieval-augmented downstream use

Lewis et al. provide a concrete architecture in which a dense vector index acts as explicit non-parametric memory consumed by a generator.

This supports the architecture pattern:

`query -> retrieve records -> downstream model`.

It does not prove:

`retrieved record is correct -> generated answer is correct`

or its converse.

Retrieval and generation remain separate stages with separate error modes.

## 21. Provenance preservation

Let record `d` contain provenance pointer `p(d)`.

A retrieval operator should return either:

- the record including `p(d)`; or
- a stable record identity from which `p(d)` can be recovered.

Ranking score alone cannot reconstruct provenance.

The order:

`record -> index -> retrieval result`

should therefore preserve an identity path back to the source object when downstream evidence claims depend on provenance.

## 22. Retrieval correctness versus usefulness

Define three predicates:

- `ContractCorrect(q,d)`: d satisfies the declared retrieval contract;
- `Relevant(q,d,task)`: d is relevant to the task;
- `Useful(q,d,consumer)`: consuming d improves the downstream objective.

None is automatically equivalent to the others.

A mathematically nearest vector can be irrelevant.

A relevant record can be unusable because it exceeds context budget.

A useful summary can fail strict exact-key identity.

The evaluation target must be named.

## 23. Downstream interface

EXTMEM-001 may consume:

- exact-key, symbolic, vector, hybrid, and multi-index access;
- ANN versus exact-NN semantics;
- record/index identity separation;
- provenance preservation;
- retrieval-contract correctness versus relevance/usefulness.

It must independently argue which knowledge should reside outside parameters and under which persistence/governance contract.
