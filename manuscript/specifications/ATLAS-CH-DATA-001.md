# Chapter Specification — ATLAS-CH-DATA-001

## Identity

- Stable ID: `ATLAS-CH-DATA-001`
- Title: **Data Quality, Mixtures, and Contamination**
- Part: `ATLAS-PART-DATA`
- Status target: `draft-v0.1`
- Hard prerequisite: `ATLAS-CH-EVIDENCE-001`
- Implementation issue: #119
- Baseline: `53583191c96a9657bbb247d683c25ee9f7bedacf`

## Contract

Develop deduplication, quality, synthetic data, mixture weighting, contamination, and benchmark pathology.

## Dataset object

Use a dataset contract

`D=(R,S,P,Phi,Delta,mu,E)`

where:

- `R`: logical records;
- `S`: source/domain labels;
- `P`: provenance and lineage;
- `Phi`: filtering/transformation pipeline;
- `Delta`: duplicate/overlap predicates;
- `mu`: sampling measure or mixture weights;
- `E`: evaluation partition and benchmark boundary.

File count alone does not determine this object.

## Duplicate relations

Exact duplicate:

`delta_exact(a,b)=1{canonical(a)=canonical(b)}`.

Near duplicate requires a declared representation, similarity, and threshold.

For token sets:

`J(a,b)=|T(a) intersect T(b)| / |T(a) union T(b)|`.

At threshold `tau`:

`delta_near_tau(a,b)=1{J(a,b)>=tau}`.

Semantic redundancy is a separate relation and must not be silently identified with lexical near-duplication.

## Contamination predicate

For training set `T`, evaluation set `V`, and declared overlap predicate `delta`:

`C_delta(e;T)=1`

iff there exists `t in T` with `delta(t,e)=1`.

Measured contamination rate:

`CR_delta(T,V)=|{e in V:C_delta(e;T)=1}|/|V|`.

This quantity is predicate-relative.

Detected overlap proves exposure opportunity under the declared predicate. It does not by itself prove memorization or causal benchmark inflation.

## Mixture accounting

For domains `d=1,...,k`, distinguish:

- raw corpus proportion `p_d=n_d/sum_j n_j`;
- post-filter proportion `p'_d`;
- training sampling weight `w_d`, with `sum_d w_d=1`.

In general:

`p != p' != w`.

Mixture weights are part of the training intervention.

## Quality boundary

Data quality is application-relative and multidimensional.

Possible dimensions include:

- provenance completeness;
- format/parse validity;
- duplication burden;
- task/domain relevance;
- freshness;
- label reliability;
- policy/admissibility status.

The chapter does not define one universal scalar quality score.

## Synthetic-data boundary

Synthetic provenance is a lineage attribute.

Synthetic records may be useful, harmful, redundant, or high quality depending on generation and use.

Recursive generated-data degradation shown in the locked Nature source is a specific failure mode, not a universal theorem that synthetic data are bad.

## Exact witness corpus

Training records:

- `t1`: domain web, source A, tokens `{alpha,beta,gamma}`;
- `t2`: domain web, source A-copy, exact same tokens/text as `t1`;
- `t3`: domain books, source B, tokens `{alpha,beta,gamma,delta}`;
- `t4`: domain code, source C, tokens `{lambda,mu,nu}`;
- `t5`: domain synth, source G, tokens `{theta,iota,kappa}`, provenance synthetic.

Evaluation records:

- `e1={alpha,beta,gamma}`;
- `e2={alpha,beta,gamma,epsilon}`;
- `e3={omega,psi,chi}`.

## Exact contamination witness

Exact-string predicate:

- `e1` overlaps;
- `e2,e3` do not.

So:

`CR_exact=1/3`.

Token-set Jaccard with `tau=3/4`:

- `e1` overlaps;
- `e2` has Jaccard `3/4` with `t1`;
- `e3` does not overlap.

So:

`CR_near=2/3`.

The records did not change. The overlap predicate changed.

## Deduplication witness

Raw training count: 5.

Exact deduplication merges `t1,t2`:

- logical representatives: 4.

Near-duplicate clustering at Jaccard `>=3/4` also links `t3` with the `t1/t2` cluster:

- three clusters remain.

Thus deduplication policy changes the effective sampling measure and can alter domain representation.

## Mixture witness

Raw domain proportions:

`p=(2/5,1/5,1/5,1/5)`

for web, books, code, synth.

Declare training weights:

`w=(1/2,1/4,1/8,1/8)`.

The training distribution therefore differs from raw corpus proportions even before stochastic sampling variance.

## Downstream handoff

`ATLAS-CH-CURRICULUM-001` may inherit:

- dataset lineage;
- deduplication predicates;
- mixture-weight semantics;
- quality-vector discipline;
- contamination measurement boundaries.

It must independently develop ordering, difficulty, competence, and curriculum policies.
