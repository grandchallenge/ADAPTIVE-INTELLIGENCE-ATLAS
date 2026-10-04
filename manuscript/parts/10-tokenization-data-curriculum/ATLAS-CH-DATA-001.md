# Data Quality, Mixtures, and Contamination
<!-- ATLAS-CH-DATA-001 -->

**Epistemic status:** established empirical dataset results + audited Evidence prerequisite + Atlas synthesis + exact finite corpus witness.  
**Specification:** manuscript/specifications/ATLAS-CH-DATA-001.md  
**Formal packet:** mathematics/derivations/ATLAS-CH-DATA-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/DATA-001.md  
**Source lock:** sources/source-locks/ATLAS-CH-DATA-001.yaml

A dataset is not a bag of text.

It is a governed sampling object with lineage.

Two collections can contain the same visible records and still train different models because they differ in:

- duplication;
- filters;
- provenance;
- partition boundaries;
- sampling weights;
- synthetic-data lineage;
- evaluation overlap.

The governing rule of this chapter is:

> data quality is not one scalar property, and contamination is not one predicate.

Every empirical claim must retain the exact dataset construction and evaluation threat model that support it.

## 1. Start with the data object

Use:

`D=(R,S,P,Phi,Delta,mu,E)`.

Here:

- `R` is the logical record set;
- `S` contains source and domain labels;
- `P` records provenance and lineage;
- `Phi` is the transformation/filtering pipeline;
- `Delta` contains duplicate and overlap relations;
- `mu` is the training sampling measure;
- `E` is the evaluation boundary.

This object is richer than a directory of files.

## 2. Why lineage matters

Suppose two records contain identical text.

One may be copied from the other.

Both may descend from the same upstream source.

One may be human-authored and the other generated.

One may have entered through a benchmark-derived instructional set.

The bytes alone do not recover this history.

Provenance is therefore part of the data object.

This follows directly from the Evidence chapter's rule that support and source identity remain attached to claims.

## 3. Exact duplicates

Let `canon(r)` be a declared canonicalization.

Define:

`delta_exact(a,b)
=
1{canon(a)=canon(b)}`.

Even "exact" requires a method.

Do we normalize whitespace?

Unicode?

HTML?

Case?

Boilerplate?

A deduplication claim without canonicalization semantics is incomplete.

## 4. Near duplicates

Exact equality misses modified copies.

Let `T(r)` be a token-set representation.

A simple near-duplicate score is token Jaccard:

`J(a,b)
=
|T(a) intersect T(b)|
/
|T(a) union T(b)|`.

At threshold `tau`:

`delta_near_tau(a,b)
=
1{J(a,b)>=tau}`.

The result depends on both representation and threshold.

Lee et al. demonstrate why exact and near-duplicate structure both matter in language-model corpora.

## 5. Semantic redundancy is different again

Two records can have low lexical overlap while conveying nearly the same information.

Conversely, boilerplate can create high lexical overlap without carrying the same substantive content.

So we need at least three distinct relations:

- exact duplicate;
- near duplicate under a declared representation;
- semantic redundancy under a declared semantic method.

No one relation silently substitutes for the others.

## 6. Deduplication changes the training measure

Suppose a record appears ten times.

Uniform record sampling gives the underlying content roughly ten times the probability mass of a singleton.

Remove nine copies and the empirical training distribution changes.

Therefore:

> deduplication is not merely storage compression.

It changes the effective sampling measure unless the sampler explicitly compensates.

This is one reason deduplication can alter model behavior.

## 7. Deduplication itself has policy

A near-duplicate relation can induce clusters.

Then someone must decide:

- which representative survives;
- whether source metadata are merged;
- whether domain labels are preserved;
- whether all cluster members remain addressable;
- whether a canonical source is preferred.

The clustering threshold and representative policy can change corpus composition.

## 8. Cross-domain duplicates are especially revealing

Suppose one article appears on the open web and in a curated book corpus.

If deduplication keeps only the web copy, the text survives but the book-domain count falls.

If mixture weights are later computed from retained counts, the deduplication policy has affected the mixture.

This is not a bug in arithmetic.

It is a consequence of how lineage, clustering, and sampling interact.

## 9. "Clean" is not a mathematical primitive

Dataset pipelines often use words such as:

- clean;
- filtered;
- high quality;
- safe;
- curated.

These words can hide several separate criteria.

Dodge et al.'s analysis of C4 is important because it shows that web-corpus filtering choices change both content and population composition, and that large corpora can contain unexpected material and benchmark examples.

The Atlas therefore treats "clean" as a pipeline label, not a theorem.

## 10. Quality is multidimensional

For application `A`, write a quality feature vector:

`Q_A(r)
=
(q_prov,q_valid,q_relevance,q_fresh,q_label,...)`.

Possible dimensions include:

- provenance completeness;
- parse/format validity;
- domain relevance;
- freshness;
- label reliability;
- duplication burden;
- policy admissibility.

A scalar score may be constructed for a particular application.

The chapter assumes no universal weighting.

## 11. Filters can trade one quality for another

A strict filter can remove malformed text.

It can also remove rare dialects, minority language, domain-specific notation, or valuable edge cases.

A permissive filter can preserve breadth.

It can also preserve noise.

The correct filter depends on the objective and the evidence.

A change in retained distribution should be measured, not inferred from the word "quality."

## 12. Raw corpus proportions

Suppose domain `d` has `n_d` retained records.

Raw corpus proportion is:

`p_d
=
n_d / sum_j n_j`.

This describes the retained corpus under the counting unit being used.

It does not yet say how often domain `d` will appear during training.

## 13. Training mixture weights

A training sampler can declare separate weights:

`w_d>=0`

with:

`sum_d w_d=1`.

A two-stage sampler may:

1. sample domain `d` with probability `w_d`;
2. sample a record inside that domain.

Then record probability depends on both the domain weight and the number of retained records in that domain.

DoReMi makes mixture proportions an explicit optimizable training variable in its reported experiments.

## 14. Corpus composition and training composition differ

Three distributions should be kept separate:

- raw source/corpus proportions `p`;
- post-filter/dedup proportions `p'`;
- training sampling weights `w`.

In general:

`p != p' != w`.

The difference is often intentional.

The important thing is to document it.

## 15. Mixture weights are an intervention

Changing `w` changes the examples a model expects to see.

That makes mixture weighting part of the training intervention.

A downstream performance claim should therefore retain:

- domain definitions;
- weights;
- sampler;
- number of draws/tokens;
- any dynamic weight schedule.

A dataset name alone is not enough.

## 16. Synthetic provenance

Add a lineage field:

`origin(r)
in
{human,synthetic,mixed,unknown}`.

This says something about where the record came from.

It does not determine whether the record is correct, useful, novel, or harmful.

Synthetic data should not be collapsed into a scalar quality judgment.

## 17. Recursive generated-data failure mode

Shumailov et al. study recursive training on generated data and report model-collapse behavior in the investigated settings.

The bounded lesson is:

> recursive generated-data pipelines can create distributional failure modes that provenance-aware dataset accounting should expose.

The chapter does not infer:

`synthetic => bad`.

## 18. Synthetic data need lineage depth

For generated records, useful provenance may include:

- generator model/version;
- prompt or conditioning source;
- decoding policy;
- upstream human or synthetic inputs;
- generation date;
- filtering;
- whether the generator was trained on earlier synthetic generations.

A single Boolean "synthetic" can be too weak to diagnose recursive lineage.

## 19. Train/evaluation contamination

Let `T` be training data and `V` evaluation data.

For overlap predicate `delta`, define:

`C_delta(e;T)=1`

when some training record overlaps evaluation item `e` under `delta`.

Measured contamination rate is:

`CR_delta(T,V)
=
(1/|V|)
sum_(e in V) C_delta(e;T)`.

This is not one universal number.

It is relative to the predicate and partitions.

## 20. Exact overlap is one threat model

An exact-match threat model asks whether the evaluation item itself, under a declared canonicalization, occurs in training.

This is precise.

It is also narrow.

Paraphrased, templated, or answer-bearing variants can evade it.

## 21. Near overlap is a different threat model

A near-duplicate threat model may detect modified copies.

But it introduces:

- representation choice;
- threshold choice;
- false positives;
- false negatives.

So a near-contamination rate should always travel with the detector definition.

## 22. Benchmark examples in web corpora

Dodge et al. found examples from evaluation datasets inside C4.

Lee et al. also measured train-test overlap and showed that deduplication can reduce such overlap in the studied datasets.

These findings justify treating benchmark overlap as an empirical threat worth measuring.

They do not make every lexical overlap equally damaging.

## 23. Exposure is not memorization

Suppose an evaluation item overlaps training.

This establishes an opportunity for exposure.

It does not automatically establish that the trained model memorized the item.

Memorization is a model-behavior claim.

It needs its own evidence.

## 24. Memorization is not causal score inflation

Even demonstrated memorization does not by itself prove that a benchmark score was inflated by that memorization.

A causal claim would ask something like:

> what would the model's score have been if the overlapping material had not been available?

That counterfactual generally requires a stronger experimental design or other causal evidence.

## 25. Benchmark pathology is broader than exact leakage

Potential pathologies include:

- exact item reuse;
- near-duplicate item reuse;
- answer leakage;
- template leakage;
- benchmark-derived instruction examples;
- public benchmark discussions repeated in web data;
- tuning on evaluation feedback.

Each has a different detection problem.

"Contaminated" should therefore name the threat model.


## 26. Benchmark version matters

A benchmark name can hide version changes.

Items may be corrected, expanded, translated, reordered, or reformatted.

A contamination claim should therefore bind to:

- exact benchmark version;
- exact item set;
- canonicalization;
- detector.

Otherwise two analyses can report different numbers while appearing to discuss the same object.

## 27. Exact finite witness

Use five training records:

- t1: web, {alpha,beta,gamma};
- t2: web, exact duplicate of t1;
- t3: books, {alpha,beta,gamma,delta};
- t4: code, {lambda,mu,nu};
- t5: synthetic, {theta,iota,kappa}.

Use three evaluation records:

- e1: {alpha,beta,gamma};
- e2: {alpha,beta,gamma,epsilon};
- e3: {omega,psi,chi}.

The records never change across the following calculations.

## 28. Exact-match contamination in the witness

Under exact token-sequence equality:

- e1 overlaps t1 and t2;
- e2 does not exactly match any training record;
- e3 does not match any training record.

Therefore:

`CR_exact=1/3`.

This is an exact statement under one overlap predicate.

## 29. Near-overlap contamination in the witness

Use token-set Jaccard with threshold:

`tau=3/4`.

For e2 and t1:

`J(e2,t1)
=
3/4`.

Therefore e2 now counts as overlapping.

e1 remains overlapping.

e3 remains non-overlapping.

Hence:

`CR_near=2/3`.

The data did not change.

The detection rule did.

## 30. Why this does not make either rate false

The rates answer different questions.

`1/3` means:

> one third of evaluation items have an exact match under this canonicalization.

`2/3` means:

> two thirds have a training neighbor at or above this Jaccard threshold.

Neither statement should be reported without its predicate.

## 31. Exact deduplication changes the corpus

Training contains five records.

t1 and t2 are exact duplicates.

After exact deduplication there are four representatives.

The raw domain histogram changes from:

`(2,1,1,1)`

for web, books, code, synthetic

to:

`(1,1,1,1)`.

The corresponding proportions change from:

`(2/5,1/5,1/5,1/5)`

to:

`(1/4,1/4,1/4,1/4)`.

## 32. Near-duplicate clustering changes it again

At threshold `3/4`:

`J(t1,t3)=3/4`.

So a graph-clustering policy over pairwise near-duplicate edges places t1, t2, and t3 in one connected cluster.

Together with t4 and t5, there are three clusters.

If the cluster representative is chosen from the web copy, the books-domain representative disappears.

This is not a theorem that such a representative policy is good.

It is a demonstration that deduplication policy can alter domain balance.

## 33. Pairwise near-duplication need not be transitive

Suppose A is near B and B is near C.

It need not follow that A is near C.

Therefore a dataset pipeline must distinguish:

- pairwise duplicate edges;
- connected-component clustering;
- complete-link clustering;
- representative-based clustering;
- other grouping policies.

The cluster definition is part of the data method.

## 34. Mixture weights in the witness

The raw proportions are:

`p_raw=(2/5,1/5,1/5,1/5)`.

The exact-deduplicated proportions are:

`p_dedup=(1/4,1/4,1/4,1/4)`.

Now declare training weights:

`w=(1/2,1/4,1/8,1/8)`.

These are different from both corpus distributions.

For eight expected domain draws:

`8w=(4,2,1,1)`.

The sampling plan is a training decision, not a passive reflection of file counts.

## 35. Why mixture records should be first-class

If a training run reports only:

> trained on corpus X

we may still not know:

- domain weights;
- temperature sampling;
- oversampling;
- epoch boundaries;
- token caps;
- curriculum changes;
- dynamic reweighting.

A reproducible run should treat mixture configuration as a first-class artifact.

## 36. Data quality and model quality are not identical

A more carefully curated corpus can still produce a worse model under a different architecture, optimizer, budget, or objective.

Conversely, a model may perform well despite obvious corpus defects.

Therefore:

> dataset quality is not defined by one downstream score alone.

The data object and the training system should be evaluated separately and jointly.

## 37. Deduplication precision and recall

A deduplication detector can make two kinds of error.

False merge:

- distinct useful records are treated as duplicates.

Missed duplicate:

- redundant records survive.

Therefore deduplication itself has precision/recall-like tradeoffs relative to a declared duplicate gold standard or evaluation protocol.

One threshold cannot be interpreted without this tradeoff.

## 38. Contamination detection also has precision and recall

A contamination detector can:

- miss paraphrased benchmark content;
- flag legitimate domain overlap;
- confuse generic templates with copied items.

So the detector's own error profile matters.

A high measured contamination rate can reflect a broad detector.

A low rate can reflect a weak detector.

The measurement process itself needs validation.

## 39. Source-level versus span-level overlap

A source document can overlap a benchmark without containing the exact benchmark answer.

A small span can exactly reproduce an answer while the source documents are otherwise unrelated.

Useful overlap units include:

- source;
- document;
- paragraph;
- span;
- item;
- template;
- semantic neighborhood.

The unit should match the evaluation threat model.

## 40. Time can be part of contamination

If an evaluation set was published before the training crawl, exposure may be possible.

If it was published after the final training cutoff, exact exposure through that crawl is impossible.

Therefore useful lineage includes:

- source timestamps;
- crawl dates;
- benchmark release date;
- preprocessing date;
- training cutoff.

Temporal reasoning can eliminate some contamination hypotheses before expensive similarity analysis.

## 41. Public benchmarks create a moving target

Widely discussed benchmarks can appear in:

- tutorials;
- blog posts;
- solution repositories;
- papers;
- forum discussions;
- synthetic instructional data.

Over time, the benchmark becomes part of the public data ecosystem.

That does not make evaluation impossible.

It means the validity claim must become more explicit.

## 42. Synthetic data can carry contamination too

A generator trained on benchmark material can emit benchmark-derived examples.

A synthetic record therefore has at least two relevant lineage questions:

1. who or what generated it?
2. what data influenced the generator?

Synthetic generation does not erase upstream provenance concerns.

It can make them harder to trace.

## 43. Recursive lineage is a graph

For synthetic and transformed data, lineage is naturally a directed graph.

Nodes can include:

- source documents;
- filtering stages;
- model versions;
- prompts;
- generated records;
- downstream datasets.

Edges encode derivation.

A flat source label can lose this structure.

The chapter does not require every corpus to maintain a perfect lineage graph.

It establishes why one may be needed for strong provenance claims.

## 44. Data mixtures can evolve during training

A fixed vector `w` is the simplest case.

A curriculum or adaptive sampler can use:

`w_t`.

Then the effective training distribution changes with training time.

A later Curriculum chapter will study ordering and adaptive selection.

DATA-001 supplies the prerequisite distinction between corpus contents and sampling policy.

## 45. "More data" is underspecified

Adding records can change:

- corpus size;
- domain balance;
- duplication;
- freshness;
- synthetic fraction;
- overlap with evaluation;
- number of unique sources;
- effective sampling weights.

So a scaling statement such as:

> performance improved with more data

should identify what actually changed.

## 46. A practical dataset ledger

Before accepting a dataset-dependent empirical claim, record:

| Field | Question |
|---|---|
| records | What is the logical record unit? |
| sources | Which domains and source IDs contribute? |
| provenance | What lineage is retained? |
| processing | Which filters and transformations ran? |
| duplicate rule | Exact, near, semantic? Which threshold? |
| clustering | How are duplicate edges grouped? |
| representative policy | Which record survives a cluster? |
| raw proportions | What is the corpus histogram? |
| post-filter proportions | How did processing alter it? |
| sampling weights | What distribution does training actually draw from? |
| synthetic lineage | Which records/models are generated? |
| train/eval boundary | Which exact partitions? |
| overlap detector | Which unit, representation, threshold? |
| benchmark version | Which exact item set? |
| timestamps | Which release/crawl/training dates matter? |
| claim boundary | Exposure, memorization, or causal score effect? |

This ledger makes "the data" inspectable.

## 47. Failure modes

### Exact-equals-near

Exact duplicates are treated as the whole redundancy problem.

### Near-equals-semantic

A lexical threshold is treated as semantic equivalence.

### Dedup-equals-storage

Deduplication is described as compression while its sampling effect is ignored.

### Corpus-proportion-equals-mixture

Raw record counts are treated as training probabilities.

### Synthetic-equals-bad

Generated provenance is turned into a universal quality judgment.

### Overlap-equals-memorization

Detected training/evaluation overlap is described as model memorization.

### Memorization-equals-score-inflation

Behavioral recall is treated as proof of a causal benchmark effect.

### Clean-equals-quality

A pipeline label substitutes for measured quality dimensions.

## 48. What the exact witness establishes

The companion witness proves:

- exact contamination rate `1/3`;
- near-overlap contamination rate `2/3` under token-Jaccard threshold `3/4`;
- exact deduplication changes five records to four representatives;
- near-duplicate graph clustering yields three clusters;
- raw domain proportions are `(2/5,1/5,1/5,1/5)`;
- exact-dedup proportions are `(1/4,1/4,1/4,1/4)`;
- declared training weights are `(1/2,1/4,1/8,1/8)`;
- eight expected domain draws under those weights are `(4,2,1,1)`.

These facts require no learned model.

They expose the data semantics directly.

## 49. Downstream handoff

**Curriculum Learning — ATLAS-CH-CURRICULUM-001** may now assume:

- corpus lineage;
- exact/near duplicate distinctions;
- overlap-predicate semantics;
- raw versus effective data distributions;
- explicit mixture weights;
- synthetic lineage;
- scoped contamination evidence.

The downstream chapter must independently define:

- ordering;
- difficulty;
- competence;
- pacing;
- automatic curriculum policies.

DATA-001 defines what is being sampled.

CURRICULUM-001 will define how sampling changes over learning time.

## References used in this chapter

- Lee et al., *Deduplicating Training Data Makes Language Models Better*.
- Dodge et al., *Documenting Large Webtext Corpora: A Case Study on the Colossal Clean Crawled Corpus*.
- Xie et al., *DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining*.
- Shumailov et al., *AI models collapse when trained on recursively generated data*.

Exact source identities and authority boundaries are recorded in:

sources/source-locks/ATLAS-CH-DATA-001.yaml
