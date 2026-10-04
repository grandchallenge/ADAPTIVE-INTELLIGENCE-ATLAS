# ATLAS-CW-OPTIONALITY-001 — Equal-Value Correction-Capacity Witness

**Chapter:** ATLAS-CH-OPTIONALITY-001  
**Witness class:** exact finite rational decision calculation  
**Purpose:** show that prior expected return and Bayesian regret can tie while functional optionality, conditional correction feasibility, and ex-ante correction capacity differ.

## Setup

Environment:

`Theta={L,R}`.

Prior:

`P(L)=P(R)=1/2`.

Stage-0 actions:

| action | immediate reward | next state | stage-1 feasible actions |
|---|---:|---|---|
| preserve `P` | `-1/2` | `s_P` | `{L,R}` |
| commit-left `C_L` | `0` | `s_L` | `{L}` |
| commit-right `C_R` | `0` | `s_R` | `{R}` |

At stage 1 the environment label is revealed perfectly.

Terminal reward:

`u_theta(a)=1` when `a=theta`, otherwise `0`.

Learner policies compared:

- `pi_P`: preserve, then choose the revealed matching terminal action;
- `pi_L`: commit left, then choose L.

The symmetric action `C_R` is declared so the comparator below is well typed; it is not a third learner policy in the pairwise comparison.

## Exact returns

For preservation:

`G(pi_P,L)=-1/2+1=1/2`.

`G(pi_P,R)=-1/2+1=1/2`.

Hence:

`E[G(pi_P)]=1/2`.

For left commitment:

`G(pi_L,L)=1`.

`G(pi_L,R)=0`.

Hence:

`E[G(pi_L)]=1/2`.

Therefore the prior action-value gap is exactly:

`0`.

## Exact regret

Use a clairvoyant environment-informed comparator that observes `theta` before stage 0 and chooses the declared matching commitment `C_theta`:

`V_L^*=V_R^*=1`.

Preservation regret:

- L: `1/2`;
- R: `1/2`.

Bayesian regret:

`BR(pi_P)=1/2`.

Commit-left regret:

- L: `0`;
- R: `1`.

Bayesian regret:

`BR(pi_L)=1/2`.

Thus prior expected return and Bayesian regret both tie.

Worst-case regret differs:

- preserve: `1/2`;
- commit-left: `1`.

The witness does not claim optionality is invisible to every risk criterion.

## Functional option sets

Use terminal consequence identity as the declared consequence signature.

Then:

`O_1(s_P)={L,R}`,
so
`|O_1(s_P)|=2`.

`O_1(s_L)={L}`,
so
`|O_1(s_L)|=1`.

## Conditional correction and ex-ante capacity

Target under environment `theta`:

perform terminal action `theta`.

Correction cost:

- `0` if the matching action is feasible;
- `+infinity` otherwise.

Therefore:

`k(s_P,L)=k(s_P,R)=0`,

so the post-evidence conditional indicators are

`C_{1,0}(s_P,L)=C_{1,0}(s_P,R)=1`.

The ex-ante capacity is

`CC_{1,0}(s_P;b)=1`.

For the committed state:

`k(s_L,L)=0`;

`k(s_L,R)=+infinity`.

Thus

`C_{1,0}(s_L,L)=1`;

`C_{1,0}(s_L,R)=0`;

and the ex-ante capacity is

`CC_{1,0}(s_L;b)=1/2`.

## Information gain

The environment is observed perfectly in both branches.

Thus:

`H(Theta)=1 bit`;

`H(Theta|Y)=0`;

`I(Theta;Y)=1 bit`.

Information gain is identical.

Correction capacity is not.

This proves, for the declared finite model, that knowing what correction is needed and retaining the ability to execute it are separate properties.

## Preservation-cost counterexample

Let the preservation cost be `c` instead of `1/2`.

Then:

`Q(P)=1-c`;

`Q(C_L)=1/2`.

At:

`c=3/4`,

`Q(P)=1/4`

while:

`Q(C_L)=1/2`.

Preservation still has two functional terminal options and correction capacity 1, but has lower expected return.

Therefore more correction capacity is not universally preferable when maintaining it is costly.

## Alias counterexample

Suppose a state offers two action labels `x_1,x_2`, but both have identical transitions, costs, and consequences.

Raw action count is 2.

Under consequence equivalence they form one class.

Functional option count is 1.

Therefore raw action labels are not a sound optionality metric.

## Exact receipt

| quantity | preserve | commit-left |
|---|---:|---:|
| prior expected return | `1/2` | `1/2` |
| Bayesian regret | `1/2` | `1/2` |
| worst-case regret | `1/2` | `1` |
| functional option count | `2` | `1` |
| zero-tolerance ex-ante correction capacity | `1` | `1/2` |
| information gain | `1 bit` | `1 bit` |

## Claim boundary

This witness establishes only the exact finite calculations above.

It does not prove:

- that functional-option count is the unique correct optionality measure;
- that correction capacity should always be maximized;
- that empowerment equals correction capacity;
- that the same separation holds under every regret comparator;
- that optionality implies safety, robustness, or good long-run performance.

Its role is narrower:

> equal prior value and equal Bayesian regret do not determine post-evidence correction capacity.
