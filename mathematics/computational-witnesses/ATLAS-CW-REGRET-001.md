# ATLAS-CW-REGRET-001 — Regret Object Separation Witnesses

**Chapter:** ATLAS-CH-REGRET-001  
**Witness class:** exact finite rational and deterministic calculations  
**Purpose:** separate pathwise regret, pseudo-regret, Bayesian/minimax regret, comparator-relative regret, and simple regret.

## A. Pathwise versus pseudo-regret

Environment:

- arm A mean `1/4`;
- arm B mean `3/4`;
- rewards Bernoulli and conditionally independent given chosen arm.

Policy:

always choose A.

Horizon:

`T=2`.

Pseudo-regret:

`bar R_2=2(3/4-1/4)=1`.

Pathwise mean-benchmark regret:

`R_2^path=3/2-(Y_1+Y_2)`.

Exact distribution:

- `Y_1+Y_2=0`: probability `9/16`, regret `3/2`;
- `Y_1+Y_2=1`: probability `6/16`, regret `1/2`;
- `Y_1+Y_2=2`: probability `1/16`, regret `-1/2`.

Expected pathwise regret:

`1`.

Thus a realized path can have negative regret even though pseudo-regret is positive.

## B. Bayesian versus minimax regret

One-step environment family:

- `+`: A=1, B=0;
- `-`: A=0, B=1.

Policy chooses A with probability `q`.

Environment-specific regret:

`R(q,+)=1-q`;

`R(q,-)=q`.

Worst-case regret:

`max(1-q,q)`.

Minimax policy:

`q=1/2`.

Minimax value:

`1/2`.

Prior:

`P(+)=9/10`,
`P(-)=1/10`.

Bayesian regret:

`BR(q)=9/10-(8/10)q`.

Bayes-optimal policy:

`q=1`.

Bayes regret:

`1/10`.

Worst-case regret of that Bayes-optimal policy:

`1`.

## C. Comparator class changes regret

Reward table:

| round | A | B |
|---:|---:|---:|
| 1 | 1 | 0 |
| 2 | 0 | 1 |

Learner chooses A,A and earns 1.

Best fixed-action comparator earns 1.

Regret against best fixed action:

`0`.

Best unrestricted per-round comparator chooses A,B and earns 2.

Regret against that comparator:

`1`.

## D. Cumulative versus simple regret

Deterministic arm means:

- A=1;
- B=0.

Learner:

- pulls B;
- pulls A;
- recommends A.

Cumulative regret:

`1`.

Final simple regret:

`0`.

## Exact replay

```python
from fractions import Fraction

# A. Pathwise distribution.
p0 = Fraction(9, 16)
p1 = Fraction(6, 16)
p2 = Fraction(1, 16)

r0 = Fraction(3, 2)
r1 = Fraction(1, 2)
r2 = Fraction(-1, 2)

expected_path = p0*r0 + p1*r1 + p2*r2
pseudo = 2 * (Fraction(3,4) - Fraction(1,4))

# B. Bayes/minimax.
q_minimax = Fraction(1,2)
minimax = max(1-q_minimax, q_minimax)

q_bayes = Fraction(1,1)
bayes = Fraction(9,10)*(1-q_bayes) + Fraction(1,10)*q_bayes
bayes_worst = max(1-q_bayes, q_bayes)

# C. Comparator class.
learner_reward = 1
fixed_best = 1
dynamic_best = 2

# D. Simple regret.
cumulative = 1
simple = 0

print("expected_path=", expected_path)
print("pseudo=", pseudo)
print("minimax_q=", q_minimax, "minimax=", minimax)
print("bayes_q=", q_bayes, "bayes=", bayes, "bayes_worst=", bayes_worst)
print("fixed_regret=", fixed_best-learner_reward)
print("dynamic_regret=", dynamic_best-learner_reward)
print("cumulative=", cumulative, "simple=", simple)
```

Expected exact outputs:

```text
expected_path= 1
pseudo= 1
minimax_q= 1/2 minimax= 1/2
bayes_q= 1 bayes= 1/10 bayes_worst= 1
fixed_regret= 0
dynamic_regret= 1
cumulative= 1 simple= 0
```

## Independent enumeration of the stochastic and comparator controls

The original short script prints the declared probability table and regret
values. This second replay *derives* those probabilities by enumerating all
four two-round Bernoulli reward paths, derives comparator rewards from the
two-round reward table, and checks the Bayes/minimax claims at the interval
endpoints and their analytic crossing. It uses no random-number generator.

    from fractions import Fraction as F
    from itertools import product

    mu_A, mu_B = F(1, 4), F(3, 4)
    paths = tuple(product((0, 1), repeat=2))

    def path_probability(ys):
        return (mu_A if ys[0] else 1 - mu_A) * (
            mu_A if ys[1] else 1 - mu_A
        )

    def path_regret(ys):
        return 2 * mu_B - sum(ys)

    assert sum((path_probability(p) for p in paths), F(0)) == 1
    distribution = {}
    for path in paths:
        r = path_regret(path)
        distribution[r] = distribution.get(r, F(0)) + path_probability(path)
    assert distribution == {
        F(3, 2): F(9, 16),
        F(1, 2): F(6, 16),
        F(-1, 2): F(1, 16),
    }
    expected = sum((r * mass for r, mass in distribution.items()), F(0))
    pseudo = 2 * (mu_B - mu_A)
    assert expected == pseudo == 1

    def worst_case_regret(q):
        return max(1 - q, q)

    def bayesian_regret(q):
        return F(9, 10) * (1 - q) + F(1, 10) * q

    # max(1-q,q) has the unique crossing q=1/2, where both
    # affine branches attain 1/2. For q below/above 1/2,
    # the respective branch exceeds 1/2.
    q_star = F(1, 2)
    assert worst_case_regret(q_star) == F(1, 2)
    for q in (F(0), F(1, 4), F(3, 4), F(1)):
        assert worst_case_regret(q) > worst_case_regret(q_star)

    # Bayes regret = 9/10 - (4/5)q, strictly decreasing
    # on the whole [0,1]. Its optimum is the endpoint q=1.
    q_bayes = F(1)
    assert bayesian_regret(q_bayes) == F(1, 10)
    assert worst_case_regret(q_bayes) == 1
    for q in (F(0), F(1, 4), F(1, 2), F(3, 4)):
        assert bayesian_regret(q) > bayesian_regret(q_bayes)

    rewards = ((1, 0), (0, 1))
    selected_actions = (0, 0)
    learner = sum(rewards[t][a] for t, a in enumerate(selected_actions))
    best_fixed = max(sum(rewards[t][a] for t in range(2)) for a in (0, 1))
    best_per_round = sum(max(row) for row in rewards)
    assert (learner, best_fixed, best_per_round) == (1, 1, 2)
    assert (best_fixed - learner, best_per_round - learner) == (0, 1)

    print("REGRET_ENUMERATED_CONTROLS_OK")

Expected output:

    REGRET_ENUMERATED_CONTROLS_OK

The finite samples above witness the analytic Bayes/minimax formulas;
their global optima follow from the stated monotonicity and crossing
arguments, not from checking four grid points. The path distribution uses
independent Bernoulli rewards for the *fixed always-A policy*. No
environment-uniform regret rate is inferred.

## Claim boundary

These witnesses prove only the declared finite calculations.

They do not establish universal minimax rates, Lai–Robbins asymptotic constants, UCB optimality outside its assumptions, equivalence of pseudo-regret terminology across all literatures, or any implication from low regret to safety, robustness, fairness, calibration, recoverability, or optionality.
