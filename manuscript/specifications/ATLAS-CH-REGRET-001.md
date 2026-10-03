# Chapter Specification — ATLAS-CH-REGRET-001

## Identity

- Stable ID: `ATLAS-CH-REGRET-001`
- Title: **Regret**
- Part: `ATLAS-PART-DECISION`
- Status target: `draft-v0.1`
- Hard prerequisite: `ATLAS-CH-EXPLORE-001`
- Implementation issue: #110
- Baseline: `f94a18010d969f80ddb96663bec02e449f4eb5eb`

## Contract

Develop Bayesian and minimax regret and clarify what regret controls do and do not imply.

## Opening obstruction

The sentence

> this algorithm has low regret

is incomplete.

Regret is always relative to:

- a horizon;
- an environment or environment class;
- a reward/loss convention;
- a policy;
- a comparator;
- an expectation or prior convention.

Changing any of these can change the numerical regret without changing the realized learner trajectory.

## Stochastic-bandit convention

Let environment `theta` define arm means

`mu_theta(a)`

for actions `a in A`.

Let

`mu_theta^*=max_a mu_theta(a)`.

Let `Pi` be the declared admissible policy class. Let policy `pi in Pi` select actions `A_1,...,A_T` and receive rewards `Y_t`.

Define gaps

`Delta_theta(a)=mu_theta^*-mu_theta(a)>=0`.

## Pathwise mean-benchmark regret

For a realized reward path define

`R_T^path(theta)
=
T mu_theta^*
-
sum_{t=1}^T Y_t`.

This is random in a stochastic environment and can be negative on a lucky path.

It compares realized learner reward with the expected reward of the best fixed arm.

The chapter must label this convention explicitly because "realized regret" is used differently across literatures.

## Expected/pseudo-regret

Define

`bar R_T(pi,theta)
=
E_theta^pi[
sum_{t=1}^T Delta_theta(A_t)
]`.

For the stationary stochastic-bandit convention above,

`E_theta^pi[R_T^path(theta)]
=
bar R_T(pi,theta)`.

This identity must be derived.

The manuscript should state that terminology varies: many bandit sources call `bar R_T` expected regret or pseudo-regret depending on setup.

## Bayesian regret

For prior `nu` over environments:

`BR_T(pi,nu)
=
E_{theta~nu}[bar R_T(pi,theta)]`.

Bayesian regret therefore weights environments by the declared prior.

The prior is part of the claim.

## Worst-case and minimax regret

For environment class `Theta`:

`W_T(pi,Theta)
=
sup_{theta in Theta} bar R_T(pi,theta)`.

Define minimax regret:

`R_T^*(Theta,Pi)
=
inf_{pi in Pi} sup_{theta in Theta} bar R_T(pi,theta)`.

All Bayes/minimax comparisons must use the same declared policy class `Pi` unless a different class is explicitly stated. The policy minimizing Bayesian regret for one prior need not minimize worst-case regret.

## Bayes versus minimax exact witness

One-step environment family:

- `theta=+`: rewards `A=1, B=0`;
- `theta=-`: rewards `A=0, B=1`.

Let a randomized policy choose A with probability `q`.

Then:

`bar R_1(q,+)=1-q`;

`bar R_1(q,-)=q`.

Worst-case regret:

`max(q,1-q)`.

The minimax solution is:

`q=1/2`,
value `1/2`.

Now take prior

`P(theta=+)=9/10`,
`P(theta=-)=1/10`.

Bayesian regret:

`BR_1(q)=9/10(1-q)+1/10 q`.

It is minimized at

`q=1`

with Bayes regret

`1/10`.

That Bayes-optimal policy has worst-case regret `1`.

Thus prior-weighted and minimax optimization solve different problems.

## Pathwise versus pseudo-regret exact witness

Take one stochastic environment with two Bernoulli arms:

`mu(A)=1/4`,
`mu(B)=3/4`.

Let policy always choose A for `T=2`.

Then

`bar R_2=2(3/4-1/4)=1`.

But

`R_2^path=3/2-(Y_1+Y_2)`

takes values:

- `3/2` if both A rewards are zero;
- `1/2` if exactly one reward is one;
- `-1/2` if both rewards are one.

The exact expectation is `1`.

This shows that a pathwise regret variable and its expectation are different objects.

## Comparator-class witness

Use deterministic reward table:

| round | A | B |
|---|---:|---:|
| 1 | 1 | 0 |
| 2 | 0 | 1 |

Learner chooses `A,A`, total reward `1`.

Against best fixed arm:

- A total = 1;
- B total = 1;
- regret = 0.

Against an unrestricted per-round dynamic comparator:

- choose A then B;
- comparator total = 2;
- regret = 1.

Same learner trajectory, same reward table, different comparator, different regret.

## Cumulative versus simple regret witness

In a deterministic two-arm environment with means

`mu(A)=1`,
`mu(B)=0`,

suppose the learner pulls B once and A once, then recommends A.

Cumulative regret over the two pulls is

`1`.

Final simple regret is

`mu^*-mu(A)=0`.

Therefore low cumulative regret and low final recommendation error are different objectives.

## Sublinear regret

A cumulative regret guarantee

`bar R_T=o(T)`

means

`bar R_T/T -> 0`.

It does not mean:

- zero regret;
- bounded cumulative regret;
- no bad individual round;
- best-action identification after every finite horizon;
- safety or robustness.

For logarithmic regret, cumulative regret can still diverge while average regret vanishes.

## Asymptotic lower-bound boundary

Lai–Robbins supports asymptotic logarithmic information costs under regular parametric stochastic-bandit assumptions.

Do not generalize its constants or assumptions to arbitrary adversarial, contextual, nonstationary, or structured bandits.

## Comparator discipline

For any regret statement explicitly record:

- comparator action/policy class;
- whether the comparator is fixed, dynamic, clairvoyant, or restricted;
- whether the comparator uses expected means or realized reward table;
- whether switching costs or constraints apply.

Regret is not intrinsic to the learner trajectory alone.

## What regret does not imply

Low regret does not by itself imply:

- safety;
- fairness;
- calibration;
- robustness to distribution shift;
- low tail risk;
- recoverability;
- preserved optionality;
- identifiability of the environment;
- low simple regret.

Any such property requires its own object or an explicit theorem connecting it to the regret objective.

## Downstream handoff

`ATLAS-CH-OPTIONALITY-001` may inherit:

- comparator-relative cumulative regret;
- Bayesian versus minimax distinction;
- pathwise versus expected/pseudo-regret distinction;
- sublinear-regret semantics;
- the fact that low regret need not preserve recoverability or future action sets.

It must independently formalize optionality/correction capacity and may not redefine regret retroactively.

## Completion

Source lock, derivation packet, exact witness, manuscript, ledger/register/bibliography updates, tranche receipt, green validation, implementation merge, bounded audit, audit merge, frontier recomputation, and controller reset are required.
