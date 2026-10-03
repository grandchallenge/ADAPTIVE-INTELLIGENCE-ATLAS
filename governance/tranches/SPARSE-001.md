# SPARSE-001 — Conditional Computation

## Identity

- chapter: `ATLAS-CH-SPARSE-001`
- issue: #114
- baseline: `98e146cbd150625ecac4a5f1416da221ec7abff3`
- branch: `work/sparse-001`
- hard prerequisite: `ATLAS-CH-DEPTH-001`

Exact prerequisite binds:

- DEPTH manuscript: `9d365778e873217c40604a621dbe9f88ca2153e0`
- DEPTH audit: `0c9f5405bd7d94018d76aa93ebe74ec3e505cabe`
- DEPTH source lock: `b6c18e2e0e3ab82c65d830967e2874bfb41e9bb2`

## Central object

Typed sparsity/conditional-computation coordinates:

`S=(P,A,T,B,D,R)`

for parameter sparsity, activation sparsity, token sparsity, block/module sparsity, conditional depth, and routing rule.

Realized resource accounting uses a declared resource vector rather than silently scalarizing unlike units.

## Exact witness

Fixed baseline:

`C_fixed=(40,1)`

for arithmetic units and launches.

Conditional four-input workload:

- `(20,3)`
- `(30,4)`
- `(20,3)`
- `(40,5)`

Average:

`C_cond=(55/2,15/4)`.

Thus average arithmetic falls by `5/16=31.25%`, while peak arithmetic remains 40 and average launches increase.

Two exact toy latency scalarizations reverse the system ordering, proving that arithmetic count alone does not determine latency.

## Durable distinctions

- static sparsity vs input-dependent conditional computation;
- parameter, activation, token, block/module, and depth sparsity;
- hard skipped execution vs soft gating;
- routing cost vs selected execution cost;
- average vs peak/tail compute;
- arithmetic vs memory/launch/communication costs;
- training graph vs inference graph;
- total capacity vs active per-input work;
- quality/compute frontier vs unqualified efficiency.

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
