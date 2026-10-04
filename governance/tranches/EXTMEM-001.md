# EXTMEM-001 — The External-Memory Thesis

## Identity

- chapter: `ATLAS-CH-EXTMEM-001`
- issue: #122
- baseline: `7604f00fe257ade14adf01718bda0b8f9aa8feb9`
- branch: `work/extmem-001`
- hard prerequisites:
  - `ATLAS-CH-RETRIEVAL-001`
  - `ATLAS-CH-CONTINUAL-001`

Exact prerequisite binds:

- Retrieval manuscript: `a4cf5482885ae61ec5751168187365afd1866f3a`
- AUDIT-027: `71b9c41a343acb1e00c2fd572d1b28bd16eed078`
- Retrieval source lock: `beee17eb3f727d0eb78083f5bd7afdd1028382a2`
- Continual manuscript: `0e9d13767e63ea4464ccaa61ce58809e38332d6c`
- AUDIT-024: `40da1dba9274d9e5b23104051b736bdcc13468a8`
- Continual source lock: `51cf1617f6d888f968dcbc4892abd8655b388f3a`

## Placement descriptor

`Place(k)=(V,P,S,D,R,L,A,G)`

for volatility, provenance need, sharing scope, deletion/supersession need, retrievability, latency/availability, access control/privacy, and value of parametric generalization/compression.

No universal scalar placement score is assumed.

## Exact witness

Parametric representation:

`f(A)=theta1+theta2`
`f(B)=theta1-theta2`.

Initial targets `A=2,B=0` give `theta=(1,1)`.

Updating only A to 4 while preserving B gives `theta'=(2,2)`; both coordinates change.

Naive one-coordinate edit `(2,1)` gives `A=3,B=1`.

Versioned external store updates only logical key A from value 2/version 1 to value 4/version 2 while B stays 0 and old/new source metadata remain explicit.

A stale snapshot still returns A=2 after the authoritative store moves to A=4.

## Durable distinctions

- parametric knowledge versus explicit external records;
- storage correctness versus retrieval/use correctness;
- record-local update versus systems cost;
- provenance visibility versus factual correctness;
- authoritative update versus freshness at consumers;
- shared store versus synchronized effective memory;
- externalization versus later consolidation into parameters;
- mutable records versus stable compressed structure.

## Remaining gates

Validate, merge implementation, run bounded audit, repair and validate audit, merge, verify closure, recompute frontier, reset controller.
