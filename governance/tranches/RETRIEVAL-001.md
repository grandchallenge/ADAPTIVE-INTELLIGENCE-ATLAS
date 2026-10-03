# RETRIEVAL-001 — Retrieval and Associative Access

## Identity

- chapter: `ATLAS-CH-RETRIEVAL-001`
- issue: #112
- baseline: `e1709bc5744a260c0a1eec5234d5ac4cb261b3b7`
- branch: `work/retrieval-001`
- hard prerequisites:
  - `ATLAS-CH-MEMTAX-001`
  - `ATLAS-CH-ATTNOP-001`

Exact prerequisite binds:

- MEMTAX manuscript: `de0cc5225e84748311f4a36e7a81f1978414aa6e`
- MEMTAX audit: `68bb06442a7f1f6137b24bf6e7fc583977053ded`
- MEMTAX source lock: `c5db4c7bea2011a28c8ce54c70e8cade9b373405`
- ATTNOP manuscript: `d6fa97fbbd1a2410055ca2cd4bc034ca54ccd26c`
- ATTNOP audit: `4671995f0cd7465a5df2bb60431244f482e5e3c9`
- ATTNOP source lock: `4af4e53230776daaf0be825cffd1263957ed97c8`

## Central object

Retrieval contract:

`R=(D,Q,F,s,pi,k,O)`

for record set, query space, filter/admissibility, score or match relation, ranking/selection, truncation budget, and returned projection.

## Exact witness

Immutable records A, B, C support:

- exact-key query `id=B` -> B;
- symbolic query `year>=2024` -> `{A,C}`;
- exact vector ranking -> `C,A,B`;
- paper-filter then vector rank top-1 -> A;
- vector rank top-1 then paper-filter -> empty.

Thus hybrid retrieval composition order is semantically load-bearing.

## Durable distinctions

- exact-key vs symbolic vs vector retrieval;
- sparse lexical ranking vs dense similarity;
- exact nearest neighbor vs ANN;
- record identity vs index identity;
- ranking score vs calibrated relevance probability;
- top-k truncation vs completeness;
- retrieval-contract correctness vs task relevance vs downstream usefulness;
- retrieval rank vs provenance/authority.

## Durable artifacts

- source lock;
- specification;
- derivation packet;
- exact witness;
- full manuscript;
- Chapter Ledger promotion;
- Source Register entry;
- bibliography closure.

## Remaining gates

Validate, merge implementation, run bounded audit, repair and validate audit, merge, verify closure, recompute frontier, reset controller.
