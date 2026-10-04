# DATA-001 — Data Quality, Mixtures, and Contamination

## Identity

- chapter: `ATLAS-CH-DATA-001`
- issue: #119
- baseline: `53583191c96a9657bbb247d683c25ee9f7bedacf`
- branch: `work/data-001`
- hard prerequisite: `ATLAS-CH-EVIDENCE-001`

Exact prerequisite binds:

- Evidence manuscript: `17eaa9caf90ede47c74dccff052f93d9fb3d901e`
- AUDIT-014: `6af518de0687a9cd8fe5635e2fba8f6a6271c77c`
- Evidence source lock: `432aa650c0c2e7679af8602b6d4c3af6a1c691ed`

## Core object

`D=(R,S,P,Phi,Delta,mu,E)`

for records, sources/domains, provenance, processing pipeline, duplicate/overlap predicates, sampling measure, and evaluation boundary.

## Exact witness

- exact overlap rate: `1/3`;
- near-overlap rate at Jaccard threshold `3/4`: `2/3`;
- raw record count: 5;
- exact-dedup count: 4;
- near-duplicate graph clusters: 3;
- raw domain proportions: `(2/5,1/5,1/5,1/5)`;
- exact-dedup proportions: `(1/4,1/4,1/4,1/4)`;
- declared sampling weights: `(1/2,1/4,1/8,1/8)`.

## Durable distinctions

- exact duplicate vs near duplicate vs semantic redundancy;
- raw corpus distribution vs post-filter distribution vs sampling mixture;
- synthetic provenance vs quality verdict;
- detected overlap vs memorization vs causal score inflation;
- detector semantics vs benchmark validity claim.

## Remaining gates

Validate, merge implementation, audit, repair, validate audit, merge, recompute frontier, reset controller.
