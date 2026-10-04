# ATLAS-CH-DATA-001 — Formal and Derivation Packet

## 1. Dataset contract

Use

`D=(R,S,P,Phi,Delta,mu,E)`

for logical records, sources/domains, provenance/lineage, processing pipeline, duplicate/overlap predicates, sampling measure, and evaluation boundary.

Two corpora with identical text bytes can define different training objects if they differ in provenance, filtering, partitioning, or sampling measure.

## 2. Exact duplication

Let `canon(r)` be a declared canonicalization.

Define:

`delta_exact(a,b)=1{canon(a)=canon(b)}`.

The canonicalization itself is part of the method.

Changing normalization can change which records count as exact duplicates.

## 3. Near duplication

Let `T(r)` be the declared token-set representation.

Define token-set Jaccard similarity:

`J(a,b)=|T(a) intersect T(b)|/|T(a) union T(b)|`.

For threshold `tau`:

`delta_near_tau(a,b)=1{J(a,b)>=tau}`.

Near duplication is therefore relative to representation and threshold.

## 4. Semantic redundancy

Semantic redundancy need not imply lexical near duplication.

Two records can express the same information with low token overlap.

Conversely, high lexical overlap can occur in boilerplate without equal semantic value.

Thus exact, near, and semantic duplicate relations must remain distinct.

## 5. Contamination predicate

Let `T` be the training records and `V` the evaluation records.

For overlap relation `delta`:

`C_delta(e;T)=1`

iff:

`exists t in T: delta(t,e)=1`.

Unweighted item contamination rate:

`CR_delta(T,V)
=
(1/|V|) sum_{e in V} C_delta(e;T)`.

If evaluation items carry unequal weights, a weighted measure must declare them explicitly. The unweighted rate is a property of the partitions plus the declared predicate.

## 6. Exposure versus causal inflation

If `C_delta(e;T)=1`, the evaluator has established overlap under `delta`.

That supports an exposure-opportunity claim.

It does not establish:

- the model memorized the item;
- the item affected its parameters materially;
- the benchmark answer was retrieved from memory;
- the score would have been lower without the overlap.

Those require additional evidence or interventions.

## 7. Raw and effective corpus proportions

For domain counts `n_d`:

`p_d=n_d/N`

with:

`N=sum_d n_d`.

After filtering/deduplication, counts can become `n'_d` and proportions:

`p'_d=n'_d/sum_j n'_j`.

A training sampler can then use independent weights:

`w_d>=0`,
`sum_d w_d=1`.

No identity among `p,p',w` is assumed.

## 8. Sampling measure

If training first samples domain `d` with probability `w_d` and then samples uniformly within that domain, record-level probability is:

`Pr(r)=w_d/n'_d`

for `r` in domain `d`.

Thus mixture weighting changes the effective frequency of records even when the retained corpus is fixed.

## 9. Deduplication changes the measure

Suppose duplicate records are sampled uniformly before deduplication.

A duplicated underlying text receives more probability mass simply because it appears multiple times.

Removing duplicates changes the induced empirical measure.

Deduplication is therefore not only a storage transformation.

It changes the training distribution unless the sampler compensates.

## 10. Exact witness records

Training records:

`t1=(web,A,{alpha,beta,gamma})`;

`t2=(web,A-copy,{alpha,beta,gamma})`;

`t3=(books,B,{alpha,beta,gamma,delta})`;

`t4=(code,C,{lambda,mu,nu})`;

`t5=(synth,G,{theta,iota,kappa})`.

Evaluation records:

`e1={alpha,beta,gamma}`;

`e2={alpha,beta,gamma,epsilon}`;

`e3={omega,psi,chi}`.

## 11. Exact-match contamination

Under exact token-sequence equality:

- `e1=t1=t2`;
- `e2` differs;
- `e3` differs.

Therefore:

`C_exact(e1)=1`;

`C_exact(e2)=0`;

`C_exact(e3)=0`.

Hence:

`CR_exact=1/3`.

## 12. Near-overlap contamination

Use token-set Jaccard and threshold:

`tau=3/4`.

For `e2` and `t1`:

intersection size:

`3`.

union size:

`4`.

Therefore:

`J(e2,t1)=3/4`.

So `e2` is contaminated under the declared near-overlap predicate.

`e1` remains contaminated.

`e3` has zero token overlap with every training record.

Thus:

`CR_near=2/3`.

## 13. Same records, different measured overlap

The training and evaluation records are unchanged between Sections 11 and 12.

Only the predicate changes.

Therefore:

`CR_exact != CR_near`

does not indicate inconsistent data.

It indicates different contamination definitions.

## 14. Exact deduplication

In the training set:

`t1` and `t2` are exact duplicates.

Exact deduplication produces four logical representatives:

`{t1/t2,t3,t4,t5}`.

Raw record count falls:

`5 -> 4`.

## 15. Near-duplicate clustering

At token-Jaccard threshold `3/4`:

`J(t1,t3)=3/4`;

`J(t2,t3)=3/4`.

Thus `t1,t2,t3` lie in one connected duplicate cluster under graph clustering of pairwise near-duplicate edges.

Together with `t4` and `t5`, there are three clusters.

This clustering rule must be declared because pairwise near-duplicate relations need not be transitive in general.

## 16. Domain proportions before processing

Raw counts:

- web: 2;
- books: 1;
- code: 1;
- synth: 1.

So:

`p=(2/5,1/5,1/5,1/5)`.

## 17. Domain proportions after exact deduplication

If one of `t1,t2` is retained, exact-deduplicated counts are:

- web: 1;
- books: 1;
- code: 1;
- synth: 1.

Therefore:

`p'=(1/4,1/4,1/4,1/4)`.

Deduplication has changed the domain proportions.

## 18. Near-cluster representative policy

If the near-duplicate cluster `{t1,t2,t3}` is collapsed to representative `t1`, retained domain counts become:

- web: 1;
- books: 0;
- code: 1;
- synth: 1.

This demonstrates that cross-domain deduplication can alter domain representation.

It does not imply that choosing `t1` is the correct representative policy.

Representative selection and provenance preservation are separate decisions.

## 19. Training mixture weights

Declare sampling weights:

`w=(1/2,1/4,1/8,1/8)`

for web, books, code, synth.

These differ from both raw proportions and exact-deduplicated proportions.

For an eight-draw expectation, expected domain counts are:

`(4,2,1,1)`.

This is a property of the sampler, not of the file-count histogram.

## 20. Quality as a vector

Let an application define a quality feature vector:

`Q(r)=(q_prov,q_valid,q_relevance,q_fresh,q_label,...)`.

No universal scalar combination is assumed.

A filter can improve one coordinate and worsen another.

Dodge et al. provide a representative empirical example where filtering choices alter corpus composition and can have uneven social effects.

Thus filter consequences require evidence, not the label "clean".

## 21. Synthetic-data provenance

Add provenance field:

`origin(r) in {human,synthetic,mixed,unknown}`.

This field says where a record came from.

It does not determine its correctness or usefulness.

The locked Shumailov et al. source establishes a recursive generated-data failure mode in specific settings.

The Atlas does not infer:

`synthetic => low quality`.

## 22. Benchmark pathology

Possible benchmark pathologies include:

- exact item reuse;
- near-duplicate item reuse;
- answer leakage;
- template leakage;
- benchmark-derived instructional data;
- repeated benchmark discussion in web corpora.

Each requires a declared detection rule.

Different threat models can legitimately produce different contamination rates.

## 23. Evaluation claim boundary

A benchmark score is evidence relative to:

- benchmark version;
- item set;
- prompting/evaluation protocol;
- model version;
- contamination threat model;
- scoring procedure.

If any of these changes, the empirical claim changes.

This is inherited directly from EVIDENCE-001 claim/support discipline.

## 24. Downstream interface

CURRICULUM-001 may consume:

- raw versus effective data distributions;
- deduplication and overlap predicates;
- provenance/lineage;
- quality-vector semantics;
- synthetic-data lineage;
- contamination measurement boundaries.

It must independently define ordering, difficulty, competence, and curriculum policies.
