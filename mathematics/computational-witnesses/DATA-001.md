# DATA-001 Exact Corpus Witness

**Chapter:** ATLAS-CH-DATA-001  
**Witness class:** exact finite deterministic computation

## Records

Training:

- t1: web, {alpha,beta,gamma}
- t2: web, exact duplicate of t1
- t3: books, {alpha,beta,gamma,delta}
- t4: code, {lambda,mu,nu}
- t5: synth, {theta,iota,kappa}

Evaluation:

- e1: {alpha,beta,gamma}
- e2: {alpha,beta,gamma,epsilon}
- e3: {omega,psi,chi}

## Exact overlap

Under exact token-sequence equality, only e1 overlaps training.

`CR_exact=1/3`.

## Near overlap

Use token-set Jaccard with threshold `3/4`.

`J(e2,t1)=3/4`.

Thus e1 and e2 overlap, while e3 does not.

`CR_near=2/3`.

The records are unchanged; only the overlap predicate changes.

## Deduplication

Raw training count: `5`.

Exact deduplication collapses t1 and t2, leaving `4` representatives.

Also:

`J(t1,t3)=3/4`.

Under graph clustering of pairwise near-duplicate edges at threshold `3/4`, {t1,t2,t3} forms one cluster. Together with t4 and t5, there are `3` clusters.

## Domain proportions

Raw proportions for web, books, code, synth:

`p_raw=(2/5,1/5,1/5,1/5)`.

After exact deduplication:

`p_dedup=(1/4,1/4,1/4,1/4)`.

Declared training sampling weights:

`w=(1/2,1/4,1/8,1/8)`.

For eight expected draws:

`8w=(4,2,1,1)`.

Thus raw proportions, post-dedup proportions, and sampling weights are three different distributions.

## Exact replay values

- `J(e2,t1)=3/4`
- `J(t1,t3)=3/4`
- `CR_exact=1/3`
- `CR_near=2/3`
- raw proportions `(2/5,1/5,1/5,1/5)`
- exact-dedup proportions `(1/4,1/4,1/4,1/4)`
- sampling weights `(1/2,1/4,1/8,1/8)`
- expected eight-draw counts `(4,2,1,1)`

## Claim boundary

This witness proves only these finite calculations. It does not establish a universal overlap threshold, causal benchmark inflation from overlap, universal benefit from deduplication, optimality of the example mixture weights, or a universal quality judgment from synthetic provenance.
