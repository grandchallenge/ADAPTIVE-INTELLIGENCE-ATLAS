# CONTINUAL-001 — Continual Learning and Forgetting

## Identity

- chapter: `ATLAS-CH-CONTINUAL-001`
- issue: #105
- baseline: `8a08c5db5322f027dd9214618f21ed88ce9255c0`
- branch: `work/continual-001`

Hard prerequisites:

- MEMTAX manuscript `de0cc5225e84748311f4a36e7a81f1978414aa6e`
- AUDIT-019 `68bb06442a7f1f6137b24bf6e7fc583977053ded`
- OPTBASE manuscript `42df47c50c2d6d26da65a58b230040e2663f901f`
- AUDIT-012 `28929ba6b4a16a3cef4a871fd9253d76e8a93634`

## Central result

The chapter treats the performance-through-time matrix `R_{i,j}` as primary and keeps replay, quadratic consolidation, episodic gradient constraints, and parameter isolation as distinct mechanisms.

Exact scalar witness:

`L_A=(1/2)(w+1)^2`,
`L_B=(1/2)(w-1)^2`.

Sequential B-only learning raises old loss from `0` to `2`.

With

`J_lambda=L_B+(lambda/2)(w+1)^2`,

the minimizer is

`w_lambda=(1-lambda)/(1+lambda)`.

At `lambda=1`, both losses are `1/2`.

Equal-weight replay reaches the same point only in this deliberately quadratic toy.

## Durable artifacts

- source lock
- chapter specification
- derivation packet
- exact computational witness
- full manuscript
- Chapter Ledger promotion
- Source Register entry
- bibliography entries

## Remaining gates

Validate, merge implementation, run bounded audit, repair and validate audit, merge, verify closure, recompute frontier, reset controller.
