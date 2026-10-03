# ATLAS-CH-SPARSE-001 — Formal and Derivation Packet

## 1. Typed sparsity object

Use

`S=(P,A,T,B,D,R)`

for parameter sparsity, activation sparsity, token/item sparsity, block/module sparsity, conditional depth, and routing rule.

These coordinates are independent.

A network may have high parameter sparsity with a fixed execution path, or dense parameters with strongly input-dependent execution.

## 2. Hard conditional execution

For residual-style branch `F_k`:

`x_{k+1}=x_k+g_k(x_k)F_k(x_k)`.

If

`g_k(x_k) in {0,1}`

and the implementation does not evaluate `F_k` when `g_k=0`, branch cost can be avoided.

The algebraic zero coefficient alone is insufficient to prove skipped execution.

## 3. Soft gating

If

`g_k(x_k) in [0,1]`

but execution computes

`F_k(x_k)`

before multiplication, the branch arithmetic is still incurred.

Therefore:

`soft coefficient zero != skipped operator`

without an execution-semantic bridge.

## 4. Token selection

Let active tokens before stage k be `X_k`.

Selector:

`A_k=Select_k(X_k)`.

If the next operator is evaluated only on `A_k`, token sparsification can reduce later work.

If a dense operator is evaluated first and tokens are masked only afterward, that earlier dense work is not saved.

## 5. Router/executor separation

Write:

`p(x)=Route(x)`

and

`y=Execute(p(x),x)`.

Total cost must include both.

If the router costs `C_route(x)` and selected execution costs `C_exec(p(x),x)`, then:

`C_total(x)=C_route(x)+C_exec(p(x),x)`

within one declared resource unit.

For heterogeneous resources use a vector rather than scalar addition of unlike units.

## 6. Resource vectors

Let

`C(x)=(F(x),K(x),M(x),E(x))`

for arithmetic operations, dispatch/kernel launches, memory traffic, and energy.

For finite evaluation set `X={x_1,...,x_n}`:

`C_avg=(1/n)sum_i C(x_i)`.

A componentwise comparison can be partial.

One system may use fewer FLOPs but more launches.

No total ordering exists until a scalarization or hardware model is declared.

## 7. Exact finite witness

Fixed network:

- four blocks;
- 10 arithmetic units per block;
- one fused launch.

Thus:

`C_fixed=(40,1)`.

Conditional paths:

- `x_1:{1,4}`;
- `x_2:{1,2,4}`;
- `x_3:{1,4}`;
- `x_4:{1,2,3,4}`.

Assume one router launch and one launch per active block.

Then:

`C_1=(20,3)`;

`C_2=(30,4)`;

`C_3=(20,3)`;

`C_4=(40,5)`.

Average arithmetic:

`(20+30+20+40)/4=110/4=55/2`.

Average launches:

`(3+4+3+5)/4=15/4`.

Hence:

`C_cond_avg=(55/2,15/4)`.

## 8. Arithmetic reduction

Baseline arithmetic is 40.

Conditional average is `55/2`.

Fractional reduction:

`1-(55/2)/40
=
1-55/80
=
25/80
=
5/16`.

So average arithmetic falls by:

`5/16=31.25%`.

## 9. Peak arithmetic

The conditional system executes all four blocks on `x_4`.

Therefore:

`F_peak_cond=40=F_fixed`.

The average falls while the peak does not.

Hence average compute and provisioning/peak compute are different quantities.

## 10. Two latency scalarizations

Define toy latency model:

`T_{alpha,beta}(F,K)=alpha F+beta K`.

### Compute-dominated

Take:

`alpha=1,beta=0`.

Fixed:

`T_fixed=40`.

Conditional average:

`T_cond=55/2=27.5`.

Conditional is faster.

### Launch-dominated

Take:

`alpha=1/10,beta=10`.

Fixed:

`T_fixed=(1/10)40+10(1)=14`.

Conditional average:

`T_cond=(1/10)(55/2)+10(15/4)`

`=11/4+150/4`

`=161/4=40.25`.

Fixed is faster.

Thus the same execution trace can be preferable or worse under different declared hardware cost models.

## 11. Pareto interpretation

Compare average resource pairs:

`(40,1)`

and

`(55/2,15/4)`.

Conditional computation is better in arithmetic and worse in launches.

Neither point dominates the other componentwise.

Therefore a scalar efficiency claim requires either:

- a declared resource priority;
- a scalarization;
- or direct measurement on the target system.

## 12. Structural sparsity versus conditional computation

Static parameter sparsity can be represented by a fixed mask:

`W'=M odot W`

with `M` constant over evaluated inputs.

Conditional execution instead has a state/input-dependent mask:

`M=M(x)`.

Both may reduce active arithmetic.

Only the second is conditional by this definition.

## 13. Load imbalance

Suppose a batch contains inputs with active-block counts:

`2,3,2,4`.

If hardware executes the batch synchronously at the slowest path, effective stage time may track the maximum rather than the mean.

Thus:

`mean active blocks=11/4`

while:

`max active blocks=4`.

Average routing sparsity does not determine synchronous batch latency.

## 14. Training/inference mismatch

Let training use soft gate `g_k in [0,1]` while inference thresholds:

`hat g_k=1{g_k>=tau}`.

Training and inference then evaluate different computational graphs.

Any claim about inference sparsity must be measured on the hard execution graph, not inferred solely from soft training gates.

## 15. Token-count scaling

For self-attention over n tokens, the score matrix contains `n^2` pair interactions before structure/approximation.

If token selection reduces the active count to `m<n` before a later dense attention stage, that later pair count changes from `n^2` to `m^2`.

This arithmetic observation does not by itself predict end-to-end latency.

## 16. Hardware-performance boundary

Roofline-style reasoning bounds attainable floating-point performance using compute capability, memory bandwidth, and arithmetic intensity.

Conditional computation adds irregularity not represented by FLOP count alone:

- launch/dispatch overhead;
- memory traffic;
- synchronization;
- load imbalance;
- communication;
- variable batch shapes.

Therefore:

`lower FLOPs => lower latency`

is not a theorem without additional assumptions.

## 17. Quality-efficiency frontier

Let task quality be `Q` and resource vector/scalar be `C`.

A conditional method should be reported as a pair or frontier:

`(Q,C)`.

Compute reduction that changes the model's decision function is not an efficiency improvement unless the quality change is also acceptable under the declared objective.

## 18. Downstream interface

MOE-001 may consume:

- typed sparsity coordinates;
- hard/soft routing distinction;
- route/execute separation;
- resource-vector accounting;
- average/peak compute distinction;
- hardware scalarization boundary.

It must independently define expert capacities, balancing, specialization, collapse, and distributed expert communication.
