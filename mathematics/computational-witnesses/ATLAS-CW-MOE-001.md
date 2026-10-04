# ATLAS-CW-MOE-001 — Capacity, Rerouting, and Balance Witness

**Chapter:** ATLAS-CH-MOE-001  
**Witness class:** exact finite routing/resource computation  
**Purpose:** show that router probabilities, preferred top-1 routes, accepted capacity-constrained dispatch, load balance, utility, and realized compute are distinct objects.

## Setup

Six tokens:

`t1,...,t6`.

Three equal-cost experts:

`E1,E2,E3`.

Top-1 routing.

Expert capacity:

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

Every row sums to one.

## Naive top-1 demand

Preferred assignments:

- t1 -> E1;
- t2 -> E1;
- t3 -> E1;
- t4 -> E2;
- t5 -> E2;
- t6 -> E3.

Preferred loads:

`(3,2,1)`.

E1 exceeds capacity by one token.

## Declared overflow-reroute policy

For an overloaded expert:

1. retain its C tokens with highest probability for that expert;
2. process the rejected tokens;
3. reroute each to its highest-probability alternative with free capacity;
4. drop only if no alternative has space.

At E1:

- t1 has 9/10;
- t2 has 4/5;
- t3 has 1/2.

So retain t1,t2.

For t3 the alternatives are:

- E2: 1/10;
- E3: 2/5.

E3 has free capacity.

Reroute:

`t3:E1->E3`.

## Accepted rerouted dispatch

Final assignments:

- E1: t1,t2;
- E2: t4,t5;
- E3: t3,t6.

Accepted loads:

`n=(2,2,2)`.

Accepted load fractions:

`f=(1/3,1/3,1/3)`.

No token is dropped.

## Router probability mass

Summed probability masses:

`m_1=47/20`;

`m_2=2`;

`m_3=33/20`.

Normalized by N=6:

`q=(47/120,1/3,11/40)`.

Thus:

`f != q`.

Balanced accepted token counts do not imply balanced router probability mass.

## Exact imbalance values

Count imbalance:

`B_count=sum_e(f_e-1/3)^2=0`.

Probability-mass imbalance:

`47/120-1/3=7/120`;

`11/40-1/3=-7/120`.

Therefore:

`B_prob=2*(7/120)^2=49/7200`.

So:

`B_count=0`

while:

`B_prob=49/7200>0`.

## Toy utility diagnostic

Define independent post-routing utility contributions:

- U(t1,E1)=4;
- U(t2,E1)=4;
- U(t4,E2)=2;
- U(t5,E2)=2;
- U(t3,E3)=1;
- U(t6,E3)=1.

Expert utility totals:

`u=(8,4,2)`.

Traffic counts remain:

`(2,2,2)`.

Equal traffic does not imply equal expert usefulness.

The utility numbers are illustrative evaluation values, not router probabilities and not a recommended training objective.

## Drop-policy counterfactual

Keep the same probability table and C=2.

Instead of rerouting overflow, drop t3.

Then:

`n_drop=(2,2,1)`.

Drop rate:

`D=1/6`.

If every expert evaluation has arithmetic cost c per accepted token:

- reroute policy expert arithmetic = `6c`;
- drop policy expert arithmetic = `5c`.

Same router probabilities, different overflow semantics, different execution.

## Claim boundary

This witness proves only the exact finite routing, balance, utility, and arithmetic statements above.

It does not prove that the reroute policy is optimal; that balanced counts improve task quality; that probability-mass balance is the correct training objective; that equal token counts imply equal communication or latency; that the toy utilities measure real expert specialization; or that any one capacity factor or overflow policy is universally preferable.
