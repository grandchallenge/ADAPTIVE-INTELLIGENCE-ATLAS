# Chapter Specification — ATLAS-CH-RETRIEVAL-001

## Identity

- Stable ID: `ATLAS-CH-RETRIEVAL-001`
- Title: **Retrieval and Associative Access**
- Part: `ATLAS-PART-MEM`
- Status target: `draft-v0.1`
- Hard prerequisites: `ATLAS-CH-MEMTAX-001`, `ATLAS-CH-ATTNOP-001`
- Implementation issue: #112
- Baseline: `e1709bc5744a260c0a1eec5234d5ac4cb261b3b7`

## Contract

Develop vector, symbolic, hybrid, multi-index, and key–value retrieval.

## Opening obstruction

The sentence

> retrieve the relevant memory

is underspecified.

A retrieval system must declare at least:

- record universe;
- query representation;
- admissibility/filter rule;
- index or access structure;
- score or match relation;
- ranking rule;
- truncation rule;
- returned fields;
- provenance/identity behavior.

Different retrieval contracts can return different valid results from the same immutable store.

## Retrieval object

Write a retrieval contract as

`Retr=(D,Q,F,s,pi,k,O)`

where:

- `D`: underlying record set;
- `Q`: query space;
- `F(q,D)`: optional admissibility/filter operator;
- `s(q,d)`: score, similarity, distance, or predicate relation;
- `pi`: ranking/selection rule;
- `k`: truncation/budget;
- `O`: returned projection/fields.

Record identity and index identity are separate.

## Exact-key retrieval

For unique key function

`key:D->K`,

exact lookup is

`R_key(k)=d`

when exactly one record satisfies

`key(d)=k`.

The key is an address.

No semantic similarity is implied.

## Symbolic retrieval

For predicate

`P_q(d) in {true,false}`,

symbolic selection returns

`R_sym(q)={d in D : P_q(d)}`.

Predicates may reference structured fields such as:

- type;
- date;
- provenance;
- owner;
- status;
- exact token/string fields.

Symbolic admissibility is not a similarity score.

## Vector retrieval

Let

`phi_D(d) in R^m`

and

`phi_Q(q) in R^m`.

For distance `delta`:

`Retr_vec(q,k)=TopK_{d in D}[-delta(phi_Q(q),phi_D(d))]`.

Equivalent similarity formulations are allowed when declared.

A vector score is representation- and metric-relative.

## Top-k boundary

Top-k is a truncation operator.

It does not imply:

- calibrated relevance;
- semantic truth;
- completeness outside k;
- causal importance;
- downstream usefulness.

Ties require a deterministic tie rule if exact replay is required.

## Exact versus approximate nearest neighbor

Exact nearest-neighbor search returns the global optimum under the declared metric and candidate set.

Approximate nearest-neighbor (ANN) search uses an index/search procedure that may trade exactness for speed, memory, or scalability.

The chapter must not equate an ANN result with the exact global nearest neighbor unless independently verified.

HNSW is used as one representative ANN construction.

## Multi-index access

One immutable record set may expose several indices:

- primary/exact-key index;
- metadata/predicate index;
- vector-similarity index;
- temporal index;
- provenance/source index.

These are different access paths to records, not different copies of epistemic truth.

The Babenko–Lempitsky inverted multi-index is one concrete vector-search construction, not the universal meaning of multi-index access.

## Hybrid retrieval

Hybrid retrieval requires an explicit composition rule.

Examples:

1. `filter -> rank -> top-k`;
2. `rank -> top-k -> filter`;
3. sparse/dense score fusion;
4. staged candidate generation and reranking.

These are not generally equivalent.

## Exact witness store

Use immutable records:

`A=(id=A, kind=paper, year=2024, v=(1,0), value=alpha)`

`B=(id=B, kind=paper, year=2022, v=(4/5,3/5), value=beta)`

`C=(id=C, kind=note, year=2025, v=(24/25,1/25), value=gamma)`.

Query vector:

`q=(19/20,1/20)`.

Use squared Euclidean distance.

Exact distances:

`d(q,A)^2=1/200`;

`d(q,B)^2=13/40`;

`d(q,C)^2=1/5000`.

Therefore unfiltered vector top-1 is C.

## Exact-key witness

Query:

`id=B`.

Result:

`B`.

This result is independent of vector proximity.

## Symbolic witness

Predicate:

`year>=2024`.

Result set:

`{A,C}`.

This is a filter result, not a ranking.

## Hybrid witness

Predicate:

`kind=paper`.

### Filter then rank

Admissible set:

`{A,B}`.

Nearest to q is A.

Result:

`A`.

### Rank top-1 then filter

Global vector top-1 is C.

C fails `kind=paper`.

Result:

empty.

Thus

`FilterThenRank != RankThenFilter`

for this exact finite store.

Hybrid composition order is semantically load-bearing.

## Retrieval versus attention

Attention and retrieval can both compute query-dependent similarity/weights.

Do not collapse them.

Typical retrieval can involve:

- persistent records outside the active sequence;
- explicit record identity;
- non-differentiable indices;
- hard top-k selection;
- metadata predicates;
- storage/index lifecycle independent of model execution.

Attention can instead operate over the currently supplied key/value field.

The overlap is operator-level selection/mixing, not architectural identity.

## Retrieval versus relevance

A returned record can be:

- mathematically nearest;
- lexically matched;
- symbolically admissible;
- top-ranked by a model;

and still be irrelevant to the user's actual task.

Relevance is task-relative and may require labels or downstream evaluation.

## Retrieval versus provenance

Rank does not create provenance.

A retrieval result must preserve or reference record identity/provenance if downstream claims depend on source identity.

A high score from an unprovenanced record is still unprovenanced.

## Retrieval versus downstream usefulness

A retrieval result can be correct under its read contract yet harmful or useless to a downstream generator.

Therefore distinguish:

- retrieval-contract correctness;
- relevance;
- context usefulness;
- answer correctness.

RAG is used only as a representative downstream architecture consuming dense retrieved non-parametric memory.

## Downstream handoff

`ATLAS-CH-EXTMEM-001` may inherit:

- exact-key versus associative access;
- symbolic/vector/hybrid retrieval semantics;
- multi-index access;
- ANN versus exact-NN distinction;
- record identity versus index identity;
- retrieval/provenance/relevance/usefulness separation.

It must independently establish the external-memory thesis.

## Completion

Source lock, derivation packet, exact witness, manuscript, ledger/register/bibliography updates, tranche receipt, green validation, implementation merge, bounded audit, audit merge, frontier recomputation, and controller reset are required.
