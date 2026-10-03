# AUDIT-027 — Retrieval and Associative Access

## Disposition

**PASS AFTER TWO FORMAL PRECISION REPAIRS**

ATLAS-CH-RETRIEVAL-001 remains at `draft-v0.1`.

The chapter correctly separates exact-key, symbolic, sparse, vector, approximate-nearest-neighbor, hybrid, and multi-index access while preserving distinctions among retrieval score, relevance, provenance, record identity, and downstream usefulness.

AUDIT-027 found two in-scope formal defects:

1. the draft reused `R` for the complete retrieval-contract tuple even though the audited Memory Taxonomy already uses `R` for the read-path coordinate in `M=(L,W,R,T,A,U,P,S)`. The repaired chapter names the full contract `Retr=(D,Q,F,s,pi,k,O)`, preserving `R` as the inherited generic read-path coordinate;
2. the derivation defined top-k with set braces while later reasoning relied on ordered ranking. The repaired derivation defines `TopK_k(D)=(d_(1),...,d_(k))` as an ordered list and separately names `TopKSet_k(D)` when set semantics are required.

No source identity, exact witness result, hybrid noncommutation result, ANN boundary, or downstream dependency required reversal.

## Audited baseline

- implementation merge:
  `e675cf95bb4a8df788bc96aed0b786b21d9fcb96`;
- implementation PR:
  #112;
- audit issue:
  #113;
- chapter:
  `ATLAS-CH-RETRIEVAL-001`.

## 1. Hard prerequisites

PASS.

The source lock binds exactly:

### Memory Taxonomy

- manuscript blob:
  `de0cc5225e84748311f4a36e7a81f1978414aa6e`;
- AUDIT-019 blob:
  `68bb06442a7f1f6137b24bf6e7fc583977053ded`;
- source-lock blob:
  `c5db4c7bea2011a28c8ce54c70e8cade9b373405`.

### Attention as an Operator

- manuscript blob:
  `d6fa97fbbd1a2410055ca2cd4bc034ca54ccd26c`;
- AUDIT-002 blob:
  `4671995f0cd7465a5df2bb60431244f482e5e3c9`;
- source-lock blob:
  `4af4e53230776daaf0be825cffd1263957ed97c8`.

The chapter consumes only the declared memory-taxonomy/access distinctions and attention query/key/value/operator substrate.

No External-Memory or Context-Compilation manuscript is used as hidden prerequisite authority.

## 2. External source identities and scope

PASS.

The source lock identifies:

- Salton, Wong, and Yang (1975), vector-space retrieval;
- Codd (1970), relational/symbolic data access;
- Robertson and Zaragoza (2009), probabilistic relevance/BM25-family sparse ranking;
- Malkov and Yashunin (2020), HNSW approximate nearest-neighbor search;
- Babenko and Lempitsky (2012), one inverted multi-index construction;
- DeCandia et al. (2007), Dynamo key-value access;
- Lewis et al. (2020), retrieval-augmented generation over dense non-parametric memory.

The source roles remain bounded.

The chapter does not attribute its general hybrid filter/rank composition algebra or general multi-index architecture to one paper.

## 3. Retrieval contract notation

PASS AFTER REPAIR.

The complete retrieval object is now

`Retr=(D,Q,F,s,pi,k,O)`

for:

- record set;
- query space;
- filter/admissibility operator;
- score or match relation;
- ranking/selection rule;
- truncation budget;
- returned projection.

This avoids collision with the inherited Memory Taxonomy read-path coordinate `R`.

## 4. Exact-key retrieval

PASS.

For a unique-key function, exact-key lookup is treated as address-based retrieval.

The chapter explicitly refuses to infer semantic relevance or payload truth from exact address correctness.

Dynamo is used only as a representative key-value systems source.

## 5. Symbolic retrieval

PASS.

A symbolic query compiles to a predicate

`P_q(d)`

and returns the admissible set.

The chapter correctly distinguishes predicate admissibility from ranking.

Codd's relational model is used at the appropriate conceptual level rather than as a source for modern vector/hybrid retrieval.

## 6. Vector retrieval

PASS.

The chapter makes vector retrieval relative to:

- query representation;
- record representation;
- normalization;
- declared distance/similarity;
- candidate set.

It does not identify embedding similarity with semantic truth.

## 7. Score versus calibrated relevance

PASS.

A retrieval score may order candidates without representing

`P(relevant|q,d)`.

Calibration is correctly treated as an additional property.

## 8. Top-k semantics

PASS AFTER REPAIR.

The derivation now defines

`TopK_k(D)=(d_(1),...,d_(k))`

as an ordered list.

Its underlying selected set is separately defined as

`TopKSet_k(D)={d_(1),...,d_(k)}`.

The manuscript also states that deterministic tie rules are required when exact replay of ordered results matters.

Top-k truncation is not promoted into a completeness or irrelevance theorem.

## 9. Exact versus approximate nearest neighbor

PASS.

Exact nearest-neighbor search is defined through the global optimum under the declared metric and candidate set.

Approximate search is treated as a distinct algorithmic layer that trades search exactness for practical resource advantages.

HNSW is correctly used as a representative graph-based ANN method.

The chapter does not claim HNSW returns the exact nearest neighbor for every query.

## 10. Representation versus search error

PASS.

The manuscript distinguishes:

- representation error;
- index/search approximation error;
- downstream relevance/usefulness error.

This is a load-bearing diagnostic separation.

Exact search can solve an inadequate geometry perfectly; an approximate index can also fail even when the geometry is task-aligned.

## 11. Sparse and dense retrieval

PASS.

Robertson–Zaragoza supports the sparse/BM25-family route.

Salton supports the vector-space lineage.

The manuscript does not claim that sparse and dense scores are directly commensurate without normalization or an explicit fusion rule.

## 12. Record identity versus index identity

PASS.

The chapter explicitly keeps:

`record_id != index_entry_id`.

One logical record may be exposed through multiple access structures.

Multiple index entries do not become multiple independent epistemic records.

## 13. Multi-index scope

PASS.

Babenko–Lempitsky is used only as one concrete structured vector multi-index construction.

The broader statement that one logical record set can expose several independent access structures is clearly labeled as Atlas architectural synthesis.

## 14. Exact finite witness

PASS.

Independent exact rational replay confirms, for

`q=(19/20,1/20)`:

- `d(q,A)^2=1/200`;
- `d(q,B)^2=13/40`;
- `d(q,C)^2=1/5000`.

Therefore the exact vector ranking is

`C,A,B`.

The exact-key query `id=B` returns B.

The symbolic predicate `year>=2024` returns `{A,C}`.

## 15. Hybrid noncommutation witness

PASS.

For predicate

`kind=paper`:

### Filter then rank

Candidate set is

`{A,B}`.

Nearest record is A.

### Rank top-1 then filter

Global vector top-1 is C.

C fails the paper predicate.

The result is empty.

Thus the chapter correctly establishes:

`FilterThenRank != RankThenFilter`

for this finite store.

The result proves composition-order dependence, not universal superiority of one hybrid pipeline.

## 16. Attention versus retrieval

PASS.

The chapter preserves the genuine overlap:

- query-dependent scoring;
- selection/mixing structure.

It also preserves architectural differences:

- persistence beyond the active sequence;
- explicit record identity;
- hard predicates;
- non-differentiable or independently maintained indices;
- asynchronous storage/index lifecycles.

It does not collapse retrieval into attention or vice versa.

## 17. Retrieval versus provenance

PASS.

Rank does not create provenance.

A governed retrieval result must preserve or reference stable record identity/source metadata when downstream evidence claims depend on provenance.

The chapter does not infer authority from rank.

## 18. Retrieval correctness versus relevance versus usefulness

PASS.

The chapter distinguishes:

- contract correctness;
- task relevance;
- downstream usefulness.

A mathematically correct nearest-neighbor result can be irrelevant to the task.

A relevant record can be unusable to a downstream consumer.

These are not silently merged into one retrieval-quality variable.

## 19. Retrieval-augmented generation boundary

PASS.

Lewis et al. is used as a representative architecture in which a dense non-parametric memory index supplies retrieved records to a parametric generator.

The chapter explicitly refuses the implication:

`retrieval occurred => generated answer is correct`.

Retrieval and generation remain separate error-bearing stages.

## 20. Integrity

PASS subject to audit merge validation.

The Chapter Ledger records RETRIEVAL-001 at `draft-v0.1`.

The Source Register contains `ATLAS-SRC-RETRIEVAL-LOCK-001`.

The bibliography closes all seven manuscript citation keys:

- `SaltonWongYang1975`;
- `Codd1970`;
- `RobertsonZaragoza2009`;
- `MalkovYashunin2020`;
- `BabenkoLempitsky2012`;
- `DeCandiaEtAl2007`;
- `LewisEtAl2020RAG`.

The exact witness contains an explicit Claim boundary.

No governed figure is required for this tranche; the finite retrieval table and exact rational replay are sufficient.

## 21. Downstream handoff

PASS.

ATLAS-CH-EXTMEM-001 may inherit:

- exact-key versus associative access;
- symbolic/vector/hybrid semantics;
- sparse/dense distinction;
- ANN versus exact-NN boundary;
- multi-index access;
- record/index identity separation;
- provenance preservation;
- retrieval correctness/relevance/usefulness separation.

It must independently establish the External-Memory Thesis.

## 22. Final disposition

AUDIT-027 passes after the two precision repairs.

The durable retrieval layer is:

**one record universe -> explicit access/index contract -> admissibility -> scoring/ranking -> ordered truncation -> stable result identity/provenance, with retrieval correctness kept distinct from relevance and downstream usefulness.**
