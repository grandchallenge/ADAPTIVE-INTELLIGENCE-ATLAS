# ATLAS-CH-REGRET-001 — Formal and Derivation Packet

## 1. Regret object

A regret claim binds:

- horizon `T`;
- environment `theta` or class `Theta`;
- policy `pi`;
- reward/loss convention;
- comparator;
- expectation/prior convention.

For a stationary stochastic bandit, environment `theta` gives arm means `mu_theta(a)`. Let

`mu_theta^*=max_a mu_theta(a)`

and

`Delta_theta(a)=mu_theta^*-mu_theta(a)`.

Policy `pi` selects `A_t` and receives `Y_t`, with

`E[Y_t | H_{t-1},A_t]=mu_theta(A_t)`.

## 2. Pathwise mean-benchmark regret

Define

`R_T^path(theta)=T mu_theta^*-sum_{t=1}^T Y_t`.

This is random. Because the learner term is realized reward while the comparator term uses the best arm mean, `R_T^path` can be negative on a lucky path.

## 3. Expected/pseudo-regret

Define

`bar R_T(pi,theta)
=
E_theta^pi[
sum_{t=1}^T Delta_theta(A_t)
]`.

By conditional expectation,

`E[Y_t]=E[mu_theta(A_t)]`.

Hence

`E[R_T^path(theta)]
=
T mu_theta^*
-
sum_t E[Y_t]
=
bar R_T(pi,theta)`.

If

`N_a(T)=sum_t 1{A_t=a}`,

then

`bar R_T(pi,theta)
=
sum_a Delta_theta(a) E[N_a(T)]`.

This is the standard gap-times-expected-pulls decomposition.

## 4. Exact pathwise witness

Two Bernoulli arms:

`mu(A)=1/4`,
`mu(B)=3/4`.

Policy always selects A for `T=2`.

Pseudo-regret:

`bar R_2=2(3/4-1/4)=1`.

Pathwise regret:

`R_2^path=3/2-(Y_1+Y_2)`.

Its exact distribution is:

| A successes | probability | pathwise regret |
|---:|---:|---:|
| 0 | `9/16` | `3/2` |
| 1 | `6/16` | `1/2` |
| 2 | `1/16` | `-1/2` |

Expectation:

`(9/16)(3/2)+(6/16)(1/2)+(1/16)(-1/2)=1`.

So the pathwise random variable and expected/pseudo-regret are not the same object even though their expectations match in this convention.

## 5. Bayesian regret

For prior `nu` over environments,

`BR_T(pi,nu)
=
E_{theta~nu}[bar R_T(pi,theta)]`.

The prior is part of the performance criterion.

For a fixed policy and prior supported on `Theta`:

`BR_T(pi,nu)
<=
sup_{theta in Theta} bar R_T(pi,theta)`.

## 6. Worst-case and minimax regret

Define

`W_T(pi,Theta)
=
sup_{theta in Theta}bar R_T(pi,theta)`.

Define minimax regret

`R_T^*(Theta)
=
inf_pi sup_{theta in Theta}bar R_T(pi,theta)`.

Bayesian and minimax criteria optimize different aggregations over environments.

## 7. Exact Bayes/minimax witness

Let

`Theta={+,-}`.

One-step deterministic rewards:

- in `+`: A=1, B=0;
- in `-`: A=0, B=1.

A randomized policy chooses A with probability `q`.

Then

`bar R_1(q,+)=1-q`

and

`bar R_1(q,-)=q`.

Worst-case regret is

`max(1-q,q)`,

minimized at

`q=1/2`

with minimax value

`1/2`.

Now use prior

`P(+)=9/10`,
`P(-)=1/10`.

Bayesian regret is

`BR_1(q)
=
(9/10)(1-q)
+
(1/10)q
=
9/10-(8/10)q`.

It is minimized at

`q=1`

with Bayes regret

`1/10`.

That Bayes-optimal policy has worst-case regret `1`.

Thus Bayes-optimal and minimax-optimal policies can differ.

## 8. Comparator-relative regret

For deterministic reward table `r_t(a)` and learner actions `A_t`, let

`G_T=sum_t r_t(A_t)`.

For comparator class `C` of action sequences,

`Reg_T(C)
=
max_{c in C}sum_t r_t(c_t)-G_T`.

The comparator class is part of the definition.

## 9. Exact comparator witness

Reward table:

| round | A | B |
|---:|---:|---:|
| 1 | 1 | 0 |
| 2 | 0 | 1 |

Learner chooses A,A and earns 1.

Against the best fixed arm, both A,A and B,B earn 1, so regret is 0.

Against the unrestricted per-round comparator, A,B earns 2, so regret is 1.

Same learner trajectory, different comparator, different regret.

## 10. Cumulative versus simple regret

If `hat a_T` is a final recommendation, define simple regret

`SR_T=mu^*-mu(hat a_T)`.

In deterministic environment

`mu(A)=1`,
`mu(B)=0`,

a learner that pulls B once, A once, then recommends A has:

- cumulative regret `1`;
- simple regret `0`.

Cumulative interaction cost and terminal recommendation error are different objectives.

## 11. Sublinear regret

`bar R_T=o(T)`

means

`bar R_T/T -> 0`.

It does not mean bounded cumulative regret.

For example,

`bar R_T=log T`

diverges while average regret vanishes.

Therefore sublinear regret is an average-performance statement, not zero-regret certification.

## 12. Finite-time versus asymptotic theory

A finite-time guarantee has the form

`bar R_T <= f(T,problem parameters)`

for declared finite `T`.

Lai–Robbins provides asymptotic stochastic-bandit lower-bound structure under regular parametric assumptions.

Auer et al. provides representative finite-time stochastic-bandit analysis.

The two result classes must not be conflated.

## 13. Regret does not identify mechanism

The same regret can arise from:

- deliberate exploration;
- estimation error;
- randomization;
- model misspecification;
- constraints;
- computational approximation.

Regret evaluates opportunity cost relative to a comparator. It does not by itself explain why an action was selected.

## 14. Regret does not imply other guarantees

Low regret does not automatically imply:

- safety;
- calibration;
- fairness;
- robustness;
- low tail risk;
- recoverability;
- preserved optionality.

Those require explicit objectives, constraints, or connecting theorems.

## 15. Downstream interface

OPTIONALITY-001 may consume:

- expected/pseudo-regret;
- Bayesian regret;
- worst-case/minimax regret;
- comparator dependence;
- cumulative versus simple regret;
- sublinear-regret semantics.

It must independently define viable future actions, recoverability, and correction capacity.
