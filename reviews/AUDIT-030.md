# AUDIT-030 — Data Quality, Mixtures, and Contamination

## Disposition

**PASS AFTER THREE FORMAL/INTERPRETIVE REPAIRS**

ATLAS-CH-DATA-001 remains at `draft-v0.1`.

The chapter correctly separates dataset lineage, exact/near duplication, semantic redundancy, corpus proportions, training mixture weights, synthetic provenance, contamination detection, memorization, and causal benchmark effects.

AUDIT-030 found three in-scope precision defects:

1. the contamination-rate formula was written as if it were the only natural benchmark measure. It is now explicitly the **unweighted item contamination rate**; benchmarks with item/task weights require a separately declared weighted measure;
2. raw/post-filter mixture proportions silently used record counts. The repaired chapter now requires the counting unit to be declared first, for example records, tokens, or bytes;
3. the manuscript stated that a benchmark published after the training cutoff could not have been exposed through the crawl. Publication date alone is insufficient because the same item or source may have existed earlier. The repaired text now requires evidence that the relevant content was unavailable to the training pipeline before the cutoff.

No exact witness value, source identity, deduplication result, mixture result, or downstream dependency required reversal.

## Audited baseline

- implementation merge:
  `703e763cac01d224eec87aeeca43d5f1acf9c58c`;
- implementation PR:
  #119;
- audit issue:
  #120;
- chapter:
  `ATLAS-CH-DATA-001`.

## 1. Hard prerequisite

PASS.

The source lock binds exactly:

- Evidence manuscript blob:
  `17eaa9caf90ede47c74dccff052f93d9fb3d901e`;
- AUDIT-014 blob:
  `6af518de0687a9cd8fe5635e2fba8f6a6271c77c`;
- Evidence source-lock blob:
  `432aa650c0c2e7679af8602b6d4c3af6a1c691ed`.

The chapter inherits only the audited evidence grammar: claim/support separation, provenance, witness boundaries, and dataset/mixture/benchmark scope discipline.

No Curriculum manuscript is used as hidden prerequisite authority.

## 2. External source scope

PASS.

The source lock identifies:

- Lee et al. (2022), *Deduplicating Training Data Makes Language Models Better*;
- Dodge et al. (2021), *Documenting Large Webtext Corpora: A Case Study on the Colossal Clean Crawled Corpus*;
- Xie et al. (2023), *DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining*;
- Shumailov et al. (2024), *AI models collapse when trained on recursively generated data*.

Their roles remain bounded to representative empirical results on deduplication, corpus documentation, mixture weighting, and recursive generated-data behavior.

The chapter does not promote those findings into universal laws about data quality, deduplication, synthetic data, or benchmark validity.

## 3. Dataset contract

PASS.

The chapter uses:

`D=(R,S,P,Phi,Delta,mu,E)`

for:

- logical records;
- source/domain labels;
- provenance/lineage;
- processing/filter pipeline;
- duplicate/overlap relations;
- sampling measure;
- evaluation boundary.

File count alone is not treated as the full data object.

## 4. Exact, near, and semantic duplication

PASS.

Exact duplication is defined relative to a declared canonicalization.

Near duplication is defined relative to a representation, similarity, and threshold.

Semantic redundancy remains a distinct relation.

The chapter does not silently equate the three.

## 5. Near-duplicate clustering

PASS.

The finite example explicitly uses graph clustering of pairwise near-duplicate edges.

The derivation notes that pairwise near-duplicate relations need not be transitive, so cluster construction must be declared separately from the pairwise predicate.

## 6. Contamination predicate

PASS AFTER REPAIR.

For training set `T`, evaluation set `V`, and overlap predicate `delta`:

`C_delta(e;T)=1`

iff some training record overlaps `e`.

The chapter now names:

`CR_delta(T,V)
=
(1/|V|) sum_e C_delta(e;T)`

as the **unweighted item contamination rate**.

If evaluation items/tasks carry unequal weights, a weighted measure must be declared separately.

## 7. Exposure, memorization, and causal score effects

PASS.

Detected overlap supports an exposure-opportunity claim under the declared predicate.

It does not by itself establish:

- memorization;
- parameter influence;
- answer retrieval;
- counterfactual score inflation.

Those remain separate empirical or causal claims requiring additional support.

## 8. Mixture accounting

PASS AFTER REPAIR.

The chapter now requires a counting unit before defining raw/post-filter proportions.

Thus:

- record proportions;
- token proportions;
- byte proportions;

are not silently treated as identical.

The training sampling weights `w` remain a separate distribution.

## 9. Raw corpus versus training sampler

PASS.

The chapter keeps distinct:

- raw corpus proportions `p`;
- post-filter/dedup proportions `p'`;
- training sampling weights `w`.

It correctly notes that mixture weighting changes the effective training distribution even when retained files are unchanged.

## 10. Deduplication changes the measure

PASS.

The chapter correctly observes that duplicated records receive additional mass under uniform record sampling.

Removing duplicates therefore changes the empirical training measure unless the sampler compensates.

Deduplication is not reduced to a storage-only transformation.

## 11. Synthetic provenance

PASS.

Synthetic origin is treated as a lineage property, not a universal quality verdict.

The Shumailov et al. source is used only for a recursive generated-data failure mode in studied settings.

The chapter explicitly refuses the implication:

`synthetic => low quality`.

## 12. Quality semantics

PASS.

Data quality is treated as application-relative and multidimensional.

The chapter offers a quality-feature vector rather than asserting one universal scalar score.

Filters may improve some dimensions while worsening others.

## 13. Exact finite witness

PASS.

Training records:

- `t1`, web;
- `t2`, exact duplicate of `t1`;
- `t3`, books;
- `t4`, code;
- `t5`, synthetic.

Evaluation records:

- `e1`;
- `e2`;
- `e3`.

Independent exact replay confirms:

`J(e2,t1)=3/4`;

`J(t1,t3)=3/4`.

## 14. Exact contamination rate

PASS.

Under exact token-sequence equality, only `e1` overlaps.

Therefore:

`CR_exact=1/3`.

## 15. Near-overlap contamination rate

PASS.

At token-Jaccard threshold `3/4`:

- `e1` overlaps;
- `e2` overlaps because `J(e2,t1)=3/4`;
- `e3` does not.

Therefore:

`CR_near=2/3`.

The records are unchanged between the two calculations; only the detector changes.

## 16. Exact deduplication

PASS.

Raw training count is 5.

Exact deduplication collapses `t1,t2`, leaving 4 representatives.

The raw domain proportions:

`(2/5,1/5,1/5,1/5)`

become, under record counting:

`(1/4,1/4,1/4,1/4)`.

## 17. Near-duplicate clusters

PASS.

Because:

`J(t1,t3)=3/4`

and `t1,t2` are exact duplicates, connected-component graph clustering at threshold `3/4` places `t1,t2,t3` together.

With `t4,t5`, there are 3 clusters.

The chapter correctly treats representative choice as a separate policy.

## 18. Training mixture witness

PASS.

Declared weights:

`w=(1/2,1/4,1/8,1/8)`.

For eight expected domain draws:

`8w=(4,2,1,1)`.

These differ from both the raw and exact-deduplicated corpus proportions.

## 19. Temporal contamination boundary

PASS AFTER REPAIR.

The manuscript no longer infers non-exposure solely from benchmark publication date.

It now requires evidence that the relevant item/content was unavailable to the training pipeline before the cutoff.

This preserves the distinction between publication metadata and actual exposure opportunity.

## 20. Benchmark threat models

PASS.

The chapter distinguishes:

- exact item reuse;
- near-duplicate reuse;
- answer leakage;
- template leakage;
- benchmark-derived instructional data;
- repeated public benchmark discussion;
- tuning on evaluation feedback.

Each requires a declared detector or evidence route.

## 21. Integrity

PASS subject to audit-PR validation.

The Chapter Ledger records DATA-001 at `draft-v0.1`.

The Source Register contains `ATLAS-SRC-DATA-LOCK-001`.

The manuscript uses no unresolved bibliography citation keys; exact external identities are bound through the source lock.

The computational witness is durably stored at:

`mathematics/computational-witnesses/DATA-001.md`

and the Chapter Ledger points to that exact path.

The witness includes an explicit Claim boundary.

No governed figure is required.

## 22. Downstream handoff

PASS.

ATLAS-CH-CURRICULUM-001 may inherit:

- dataset lineage;
- exact/near duplicate semantics;
- contamination detector scope;
- raw versus effective distributions;
- mixture-weight semantics;
- synthetic lineage;
- evidence boundaries.

It must independently define ordering, difficulty, competence, pacing, and curriculum policy.

## 23. Final disposition

AUDIT-030 passes after the three repairs above.

The durable data layer is:

**exact lineage + declared processing + explicit duplicate/overlap predicate + declared counting/sampling measure + scoped evaluation boundary, with exposure evidence kept separate from memorization and causal benchmark effects.**
