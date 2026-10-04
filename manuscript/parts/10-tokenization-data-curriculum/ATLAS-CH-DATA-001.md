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

Lee et al. demonstrate why exact and near-duplicate structure both matter in language-model corpora [@LeeEtAl2022Dedup].

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

Dodge et al.'s analysis of C4 is important because it shows that web-corpus filtering choices change both content and population composition, and that large corpora can contain unexpected material and benchmark examples [@DodgeEtAl2021C4].

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

DoReMi makes mixture proportions an explicit optimizable training variable in its reported experiments [@XieEtAl2023DoReMi].

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

Shumailov et al. study recursive training on generated data and report model-collapse behavior in the investigated settings [@ShumailovEtAl2024ModelCollapse].

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

Dodge et al. found examples from evaluation datasets inside C4 [@DodgeEtAl2021C4].

Lee et al. also measured train-test overlap and showed that deduplication can reduce such overlap in the studied datasets [@LeeEtAl2022Dedup].

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
