# Chapter Specification — ATLAS-CH-SPARSE-001

## Identity

- Stable ID: `ATLAS-CH-SPARSE-001`
- Title: **Conditional Computation**
- Part: `ATLAS-PART-SPARSE`
- Status target: `draft-v0.1`
- Hard prerequisite: `ATLAS-CH-DEPTH-001`
- Implementation issue: #114
- Baseline: `98e146cbd150625ecac4a5f1416da221ec7abff3`

## Contract

Develop sparsity, dynamic computation, token selection, conditional depth, and hardware implications.

## Opening obstruction

The sentence

> this model is sparse, so it is cheaper

is incomplete.

A compute claim must state at least:

- what is sparse;
- whether sparsity is static or input-dependent;
- which operations are actually skipped;
- whether routing itself costs work;
- which resource units are counted;
- whether the claim concerns average, peak, or tail cost;
- which hardware/software execution model is assumed.

## Sparsity coordinates

Use a typed sparsity description

`S=(P,A,T,B,D,R)`

where:

- `P`: parameter sparsity;
- `A`: activation sparsity;
- `T`: token/item sparsity;
- `B`: block/expert/module sparsity;
- `D`: conditional depth/execution path;
- `R`: routing/selection rule.

These coordinates need not agree.

## Static versus conditional sparsity

Static sparsity means the zero/absent structure is fixed across inputs during the evaluated execution regime.

Conditional computation means the executed path depends on input or intermediate state.

A statically pruned matrix can be sparse without conditional routing.

A dense model can execute conditionally by skipping whole blocks for some inputs.

## Hard versus soft selection

For branch `F_k(x)` and gate `g_k(x)`:

`x_{k+1}=x_k+g_k(x_k)F_k(x_k)`.

If `g_k in {0,1}` and the implementation avoids evaluating `F_k` when the gate is zero, the branch can be genuinely skipped.

If `g_k in [0,1]` but `F_k` is evaluated before multiplication, the arithmetic is not skipped merely because the coefficient is small.

## Token selection

For token set `X_k`, a selector produces active subset

`A_k(X_k) subseteq X_k`.

Later operators act only on the active subset if the implementation truly materializes shorter/sparser execution.

Masking a token after computing all dense interactions is not the same hardware object as removing it before those interactions.

## Routing versus execution

Separate:

`route(x) -> path(x)`

from:

`execute(path(x),x)`.

The router has its own cost and failure modes.

## Resource vector

For input `x`, define realized resource vector

`C(x)=(F(x),K(x),M(x),E(x))`

for example:

- FLOPs/arithmetic operations `F`;
- memory traffic `M`;
- kernel or dispatch count `K`;
- energy `E`.

Do not add unlike units without a declared scalarization. Latency/throughput are hardware-dependent measured or modeled outputs of this lower-level resource state, not universal primitive coordinates.

## Average versus peak/tail

For data distribution or finite evaluation set:

- average cost: `E[C(X)]`;
- peak cost: componentwise or scalarized maximum over the declared set;
- tail cost: declared quantile or tail statistic.

A low average does not imply low worst-case or tail compute.

## Exact witness

Fixed baseline has four blocks.

Each block contributes 10 arithmetic units.

Assume fixed execution is fused into one launch.

Per input baseline resource pair:

`C_fixed=(40,1)`

where coordinates are:

- arithmetic units;
- launches.

Conditional paths over four inputs are:

- `x_1:{1,4}` — 2 blocks;
- `x_2:{1,2,4}` — 3 blocks;
- `x_3:{1,4}` — 2 blocks;
- `x_4:{1,2,3,4}` — 4 blocks.

Assume one routing launch plus one launch per active block.

Then conditional resource pairs are:

- `x_1:(20,3)`;
- `x_2:(30,4)`;
- `x_3:(20,3)`;
- `x_4:(40,5)`.

Average:

`C_cond_avg=(55/2,15/4)=(27.5,3.75)`.

Thus average arithmetic falls by

`1-(27.5/40)=5/16=31.25%`

while launch count rises.

Neither resource vector dominates the other componentwise.

## Hardware scalarization witness

Let toy latency model be

`T_{alpha,beta}(F,K)=alpha F+beta K`.

Compute-dominated model:

`alpha=1,beta=0`.

Then:

- fixed latency = 40;
- conditional average = 27.5.

Conditional wins.

Launch-dominated model:

`alpha=1/10,beta=10`.

Then:

- fixed latency = 14;
- conditional average = `(1/10)(55/2)+10(15/4)=161/4=40.25`.

Fixed wins.

Same execution patterns, opposite latency ordering.

Therefore arithmetic reduction alone does not determine hardware latency.

## Peak-compute witness

Conditional peak arithmetic is still 40 because `x_4` executes all four blocks.

So:

- average arithmetic falls;
- peak arithmetic does not.

This distinguishes expected savings from capacity/provisioning requirements.

## Quality boundary

Compute reduction must be reported jointly with a declared quality/performance metric.

Skipping, pruning, or dropping tokens changes the computation.

No efficiency claim alone proves task quality is preserved.

## Training/inference boundary

Training can use:

- dense relaxations;
- auxiliary router losses;
- straight-through estimators;
- reinforcement learning;
- stochastic masks;

while inference uses hard sparse execution.

Training cost and inference cost must therefore be measured separately.

## Hardware boundary

Nominal FLOPs do not determine realized speed.

Roofline-style reasoning makes performance depend on machine balance, arithmetic intensity, and memory bandwidth.

Conditional execution additionally introduces:

- branch/routing overhead;
- kernel-launch overhead;
- irregular shapes;
- load imbalance;
- communication;
- batching fragmentation.

Measured throughput/latency claims are therefore hardware/software/batch dependent.

## Downstream handoff

`ATLAS-CH-MOE-001` may inherit:

- static versus conditional sparsity;
- hard versus soft routing;
- routing/execution separation;
- average versus peak/tail compute;
- resource-vector accounting;
- arithmetic versus hardware-efficiency boundary.

It must independently develop expert routing, capacity, balancing, specialization, collapse, and expert parallelism.

## Completion

Source lock, derivation packet, exact witness, manuscript, ledger/register/bibliography updates, tranche receipt, green validation, implementation merge, bounded audit, audit merge, frontier recomputation, and controller reset are required.
