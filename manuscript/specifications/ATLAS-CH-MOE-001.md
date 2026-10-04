# Chapter Specification — ATLAS-CH-MOE-001

## Identity

- Stable ID: `ATLAS-CH-MOE-001`
- Title: **Mixture-of-Experts Systems**
- Part: `ATLAS-PART-SPARSE`
- Status target: `draft-v0.1`
- Hard prerequisites:
  - `ATLAS-CH-SPARSE-001`
  - `ATLAS-CH-TRANSFORMER-001`
- Implementation issue: #127
- Baseline: `a15170c608c5b83048ce2310e68e527e041438cb`

## Contract

Develop routing, capacity, load balancing, specialization, collapse, and expert parallelism.

## Baseline MoE object

Let token state `h_i in R^d`.

Let experts be:

`E_e:R^d->R^d`

for `e=1,...,M`.

A router produces scores:

`z_i in R^M`

and probabilities:

`p_i=softmax(z_i)`.

A dispatch policy converts `p_i` into a discrete accepted assignment set.

This conversion is not determined by the probabilities alone.

It also requires:

- top-k rule;
- tie breaking;
- expert capacity;
- overflow policy;
- optional gate weights.

## Sparse expert block

For accepted experts `A_i`, one generic mixture form is:

`MoE(h_i)=sum_{e in A_i} alpha_{i,e} E_e(h_i)`.

For top-1 Switch-style routing:

`|A_i|<=1`

after capacity handling.

The expert sublayer typically replaces or augments the transformer's dense position-wise feed-forward sublayer rather than replacing attention.

## Routing objects

Keep separate:

1. router logits `z_{i,e}`;
2. router probabilities `p_{i,e}`;
3. preferred top-k set;
4. accepted dispatch after capacity/overflow;
5. gate weights used in aggregation;
6. realized expert execution.

A soft probability on an expert does not imply that expert executed.

## Expert load

For accepted assignment indicator:

`a_{i,e} in {0,1}`,

token load is:

`n_e=sum_i a_{i,e}`.

Probability mass is:

`m_e=sum_i p_{i,e}`.

In general:

`n_e/N != m_e/N`.

Neither quantity is automatically equal to realized wall-clock cost.

## Capacity

For batch/token count `N`, experts `M`, top-k `k`, and capacity factor `c_f`, a common nominal form is:

`C=ceil(c_f k N / M)`.

The exact formula and granularity are implementation-specific.

Capacity is a constraint on accepted token-expert assignments, not on router probabilities.

## Overflow policy

If an expert receives more than capacity `C`, the system must declare a policy.

Examples:

- drop overflow;
- reroute to another expert;
- use a residual/dense fallback;
- buffer or increase capacity.

The chapter does not privilege one universal policy.

## Exact routing witness

Use six tokens and three equal-cost experts.

Capacity:

`C=2`.

Router probabilities:

| token | E1 | E2 | E3 |
|---|---:|---:|---:|
| t1 | 9/10 | 1/20 | 1/20 |
| t2 | 4/5 | 3/20 | 1/20 |
| t3 | 1/2 | 1/10 | 2/5 |
| t4 | 1/20 | 9/10 | 1/20 |
| t5 | 1/20 | 3/4 | 1/5 |
| t6 | 1/20 | 1/20 | 9/10 |

Naive top-1 preferences:

- E1: t1,t2,t3;
- E2: t4,t5;
- E3: t6.

Preferred loads:

`(3,2,1)`.

E1 exceeds capacity.

## Declared reroute policy

For an overloaded expert:

1. retain the `C` tokens with highest probability for that expert;
2. process overflow tokens in descending rejected score;
3. send each to its highest-probability alternative expert with remaining capacity;
4. if no capacity remains, drop the token.

For E1, t3 has the lowest E1 probability among its three preferred tokens.

Its best alternative is E3 with probability `2/5`.

Reroute:

`t3:E1->E3`.

Accepted loads become:

`(2,2,2)`.

No token is dropped.

## Probability-mass distinction

Summed router probability mass is:

`m=(47/20,2,33/20)`.

Normalized by six tokens:

`m/N=(47/120,1/3,11/40)`.

Thus accepted token counts are perfectly balanced while router probability mass is not.

## Utility distinction

For illustration, define an independently evaluated task-utility contribution on the final accepted assignments:

- E1/t1: 4;
- E1/t2: 4;
- E2/t4: 2;
- E2/t5: 2;
- E3/t3: 1;
- E3/t6: 1.

Then utility totals are:

`u=(8,4,2)`.

Equal token counts do not imply equal usefulness.

These utility numbers are a toy diagnostic, not a training objective.

## Drop-policy counterfactual

Under a drop-overflow policy instead of rerouting:

- t3 is dropped;
- loads are `(2,2,1)`;
- only five tokens receive expert execution.

Same router probabilities, different overflow semantics, different realized computation.

## Specialization boundary

Specialization requires evidence relating expert identity to inputs, functions, or performance.

Examples of evidence could include:

- conditional expert performance;
- input-domain enrichment;
- stable feature selectivity;
- functional differences among expert outputs.

Traffic imbalance alone is not specialization.

## Collapse boundary

Keep distinct:

- router collapse: traffic concentrates on few experts;
- expert underuse: some experts receive too little training signal;
- expert redundancy: different experts learn nearly identical functions;
- capacity collapse/overflow: routing demand repeatedly exceeds expert capacity.

These can co-occur but are not synonyms.

## Load-balancing objective boundary

An auxiliary balancing loss acts on a proxy such as token fractions or router probability mass.

Reducing that loss does not prove:

- semantic specialization;
- task-optimal dispatch;
- equal compute time;
- lower communication;
- improved main-task loss.

The auxiliary objective and task objective must remain separate.

## Expert parallelism

Experts can be partitioned across devices.

Then routing induces token/activation communication.

A useful systems record includes:

- expert-to-device placement;
- dispatch counts;
- bytes moved;
- all-to-all or equivalent communication;
- per-expert compute;
- synchronization;
- peak capacity;
- stragglers.

Sparse arithmetic can therefore coexist with expensive communication.

## Downstream handoff

`ATLAS-CH-ROUTERDYN-001` may inherit:

- router probabilities versus accepted dispatch;
- token load and probability-mass diagnostics;
- capacity/overflow semantics;
- specialization/collapse distinctions.

`ATLAS-CH-SYSTEMS-001` may inherit:

- expert placement;
- communication/dispatch accounting;
- capacity/straggler boundaries;
- active versus total parameter capacity.

Neither may assume that balanced token counts imply stable routing, useful specialization, or efficient hardware execution.
