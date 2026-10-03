# AUDIT-026 — Regret

## Disposition

**PASS AFTER TWO FORMAL PRECISION REPAIRS**

ATLAS-CH-REGRET-001 remains at `draft-v0.1`.

The chapter correctly develops comparator-relative regret and separates pathwise mean-benchmark regret, expected/pseudo-regret, Bayesian regret, worst-case/minimax regret, comparator-class dependence, and cumulative versus simple regret.

AUDIT-026 found two in-scope formal defects:

1. Bayesian/minimax optimization used an untyped `inf_pi` even though policy class is part of the regret contract. The repaired chapter now binds an admissible policy class `Pi`, uses `pi in Pi`, defines `R_T^*(Theta,Pi)`, and states that Bayes/minimax comparisons use the same policy class unless explicitly changed;
2. the general comparator-regret formula used `max_{c in C}`, which assumes the optimum is attained. It now uses `sup_{c in C}`. The finite two-action witness still attains its maximum, so its arithmetic is unchanged.

No exact witness value, source identity, asymptotic/finite-time boundary, or downstream Optionality handoff required reversal.

## Audited baseline

- implementation merge:
  `915911dfd5b6b6daf7084edd75e2341d7a727d10`;
- implementation PR:
  #110;
- audit issue:
  #111;
- chapter:
  `ATLAS-CH-REGRET-001`.

## 1. Hard prerequisite

PASS.

The source lock binds exactly:

- EXPLORE manuscript blob:
  `d358ec986bb1baa604668707ae0d598856247d89`;
- AUDIT-022 blob:
  `f4b76500f62e5d92571e0fcab648d4f3c6d81abf`;
- EXPLORE source-lock blob:
  `44bf1f2ca6f98a1b852f50ecc6eaf2d42cadadcc`.

No OPTIONALITY manuscript is used as hidden prerequisite authority.

## 2. External sources

PASS.

The source lock identifies:

- Lai and Robbins (1985), asymptotically efficient adaptive allocation;
- Bubeck and Cesa-Bianchi (2012), stochastic/nonstochastic bandit regret;
- Lattimore and Szepesvári (2020), comprehensive bandit algorithms/regret reference;
- Auer, Cesa-Bianchi, and Fischer (2002), finite-time stochastic-bandit/UCB analysis;
- Russo and Van Roy (2014), information-directed sampling.

Their roles remain bounded to the cited model classes.

Lai–Robbins is not generalized beyond its regular parametric stochastic-bandit setting.

## 3. Regret contract

PASS AFTER REPAIR.

Every regret quantity is now tied to:

- horizon;
- environment or environment class;
- admissible policy class;
- reward/loss convention;
- comparator;
- expectation/prior convention.

The chapter no longer leaves the minimax policy class implicit.

## 4. Pathwise mean-benchmark regret

PASS.

The chapter defines

`R_T^path(theta)=T mu_theta^* - sum_t Y_t`.

It explicitly labels this convention because terminology varies across literatures.

The quantity is random and may be negative on a lucky path.

The manuscript does not infer that a negative pathwise value makes a suboptimal arm optimal in expectation.

## 5. Expected/pseudo-regret identity

PASS.

For the declared stationary stochastic-bandit model,

`bar R_T(pi,theta)
=
E[sum_t Delta_theta(A_t)]`.

Using

`E[Y_t|H_{t-1},A_t]=mu_theta(A_t)`,

the chapter correctly derives

`E[R_T^path(theta)]
=
bar R_T(pi,theta)`.

The source-lock terminology was tightened to preserve this exact relation rather than treating pathwise, expected, and pseudo-regret as generically interchangeable notions.

## 6. Pull-count decomposition

PASS.

With

`N_a(T)=sum_t 1{A_t=a}`,

the derivation

`bar R_T
=
sum_a Delta_theta(a) E[N_a(T)]`

is correct.

## 7. Exact pathwise witness

PASS.

For Bernoulli means

`mu(A)=1/4`,
`mu(B)=3/4`,

and always selecting A for two rounds:

pseudo-regret is

`1`.

Pathwise regret takes exact values:

- `3/2` with probability `9/16`;
- `1/2` with probability `6/16`;
- `-1/2` with probability `1/16`.

Its expectation is exactly

`1`.

## 8. Bayesian regret

PASS.

For prior `nu`,

`BR_T(pi,nu)
=
E_{theta~nu}[bar R_T(pi,theta)]`.

The chapter makes the prior part of the performance criterion and does not promote Bayesian average performance into a worst-case guarantee.

## 9. Worst-case and minimax regret

PASS AFTER REPAIR.

For environment class `Theta` and admissible policy class `Pi`:

`W_T(pi,Theta)
=
sup_{theta in Theta}bar R_T(pi,theta)`.

Minimax regret is now

`R_T^*(Theta,Pi)
=
inf_{pi in Pi}
sup_{theta in Theta}
bar R_T(pi,theta)`.

Bayes/minimax optimizer comparisons are explicitly made over the same `Pi` unless stated otherwise.

## 10. Bayes/worst-case inequality

PASS.

For a fixed policy and prior supported on `Theta`:

`BR_T(pi,nu)
<=
W_T(pi,Theta)`.

Taking the infimum over the same policy class gives

`inf_{pi in Pi}BR_T(pi,nu)
<=
R_T^*(Theta,Pi)`.

The chapter correctly states that this inequality does not imply coincident optimizers.

## 11. Exact Bayes/minimax witness

PASS.

For one-step deterministic environments:

- `+`: A=1, B=0;
- `-`: A=0, B=1;

and policy choosing A with probability `q`:

`R(q,+)=1-q`;

`R(q,-)=q`.

The minimax solution is

`q=1/2`

with value

`1/2`.

Under prior

`P(+)=9/10`,
`P(-)=1/10`,

Bayesian regret is

`9/10-(8/10)q`,

so the Bayes-optimal policy is

`q=1`

with Bayes regret

`1/10`.

Its worst-case regret is

`1`.

Thus Bayesian and minimax optimization are demonstrably different objectives.

## 12. Comparator-relative regret

PASS AFTER REPAIR.

For learner reward

`G_T=sum_t r_t(A_t)`

and comparator class `C`,

the general definition now uses

`Reg_T(C)
=
sup_{c in C}sum_t r_t(c_t)-G_T`.

This does not assume the supremum is attained.

For finite comparator sets, the supremum is a maximum.

## 13. Exact comparator witness

PASS.

For reward table:

- round 1: A=1, B=0;
- round 2: A=0, B=1;

and learner sequence A,A:

learner reward is 1.

Best fixed-action comparator reward is 1, giving regret 0.

Best unrestricted per-round comparator A,B earns 2, giving regret 1.

The learner trajectory is unchanged; only the comparator class changes.

## 14. Cumulative versus simple regret

PASS.

For deterministic arms A=1, B=0, a learner that pulls B then A and finally recommends A has:

- cumulative regret 1;
- simple regret 0.

The chapter correctly treats online interaction cost and terminal recommendation quality as distinct objectives.

## 15. Sublinear regret

PASS.

The chapter states:

`bar R_T=o(T)`

means

`bar R_T/T -> 0`.

It does not interpret sublinear cumulative regret as zero or bounded cumulative regret.

The example `log T` correctly shows divergent cumulative regret with vanishing average regret.

## 16. Finite-time versus asymptotic theory

PASS.

Auer et al. is used for representative finite-time stochastic-bandit analysis.

Lai–Robbins is used for asymptotic information-cost/lower-bound structure under its declared assumptions.

The chapter does not silently transfer either claim class into the other.

## 17. Limits of regret guarantees

PASS.

The chapter explicitly refuses to infer from low reward regret:

- safety;
- fairness;
- calibration;
- robustness;
- tail-risk control;
- recoverability;
- preserved optionality.

Each requires an explicit objective, constraint, or connecting theorem.

## 18. Downstream handoff

PASS.

ATLAS-CH-OPTIONALITY-001 may inherit:

- expected/pseudo-regret;
- pathwise versus expected regret;
- Bayesian regret;
- worst-case/minimax regret;
- comparator dependence;
- cumulative versus simple regret;
- sublinear-regret semantics.

It must independently define viable future actions, recoverability, and correction capacity.

## 19. Integrity

PASS subject to audit merge validation.

The Chapter Ledger records REGRET-001 at `draft-v0.1`.

The Source Register contains `ATLAS-SRC-REGRET-LOCK-001`.

The bibliography closes:

- `LaiRobbins1985`;
- `BubeckCesaBianchi2012`;
- `LattimoreSzepesvari2020`;
- `AuerEtAl2002Bandit`;
- `RussoVanRoy2014`.

The exact witness contains an explicit Claim boundary.

No governed figure is required.

## 20. Final disposition

AUDIT-026 passes after the two precision repairs.

The durable regret layer is:

**environment + horizon + admissible policy class + comparator + expectation/prior convention -> explicitly typed regret quantity, with Bayesian, minimax, pathwise, cumulative, and terminal objectives kept distinct.**
