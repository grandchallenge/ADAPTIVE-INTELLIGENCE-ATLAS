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

## Executable finite policy and correction-capacity replay

The program below constructs the two-state decision problem directly. The
environment reveals its label at stage 1 for either first-stage action;
preservation retains both terminal choices, whereas commitment restricts
the feasible action set. The clairvoyant comparator knows the label *before*
the first-stage decision. All reported payoffs, Bayes/worst-case regrets,
feasible action classes and correction indicators are calculated using exact
rational arithmetic, not copied from the receipt table.

    from fractions import Fraction as F

    environments = ("L", "R")
    prior = {"L": F(1, 2), "R": F(1, 2)}
    feasible = {
        "P": frozenset(("L", "R")),
        "C_L": frozenset(("L",)),
        "C_R": frozenset(("R",)),
    }

    def terminal_payoff(theta, terminal_action):
        return int(theta == terminal_action)

    def first_stage_reward(action, cost=F(1, 2)):
        return -cost if action == "P" else F(0)

    def policy_return(action, theta, cost=F(1, 2)):
        # With perfect stage-1 information, choose a feasible
        # terminal action maximizing the declared terminal payoff.
        best_terminal = max(
            terminal_payoff(theta, a) for a in feasible[action]
        )
        return first_stage_reward(action, cost) + best_terminal

    def prior_mean(values):
        return sum((prior[t] * values[t] for t in environments), F(0))

    preserve = {t: policy_return("P", t) for t in environments}
    commit_left = {t: policy_return("C_L", t) for t in environments}
    clairvoyant = {
        t: policy_return("C_" + t, t) for t in environments
    }
    assert preserve == {"L": F(1, 2), "R": F(1, 2)}
    assert commit_left == {"L": F(1), "R": F(0)}
    assert clairvoyant == {"L": F(1), "R": F(1)}
    assert prior_mean(preserve) == prior_mean(commit_left) == F(1, 2)

    def regrets(policy):
        return {t: clairvoyant[t] - policy[t] for t in environments}

    preserve_regret = regrets(preserve)
    commit_regret = regrets(commit_left)
    assert prior_mean(preserve_regret) == F(1, 2)
    assert prior_mean(commit_regret) == F(1, 2)
    assert max(preserve_regret.values()) == F(1, 2)
    assert max(commit_regret.values()) == F(1)

    # A terminal consequence is identified by the action's outcome
    # signature. Here L and R have distinct consequences across theta.
    def signature(a):
        return tuple(terminal_payoff(t, a) for t in environments)

    def distinct_consequences(action):
        return {signature(a) for a in feasible[action]}

    assert len(distinct_consequences("P")) == 2
    assert len(distinct_consequences("C_L")) == 1

    # Correction target is to perform the matching terminal action,
    # not merely to achieve the same reward by some alternative action.
    def correctable(action, theta):
        return int(theta in feasible[action])

    def capacity(action):
        return prior_mean({
            t: F(correctable(action, t)) for t in environments
        })

    assert tuple(correctable("P", t) for t in environments) == (1, 1)
    assert tuple(correctable("C_L", t) for t in environments) == (1, 0)
    assert capacity("P") == F(1)
    assert capacity("C_L") == F(1, 2)

    # Both observations reveal theta, so each contributes one bit.
    # The two equally likely labels require exactly one binary bit.
    observation_class_count = len(environments)
    assert observation_class_count == 2
    info_bits_P = info_bits_CL = 1
    assert info_bits_P == info_bits_CL

    costly_preserve = {
        t: policy_return("P", t, F(3, 4))
        for t in environments
    }
    assert prior_mean(costly_preserve) == F(1, 4)
    assert prior_mean(costly_preserve) < prior_mean(commit_left)

    # An alias must not create a new functional option merely
    # because the action string is different.
    alias_outcomes = {"x_1": (0, 1), "x_2": (0, 1)}
    assert len(alias_outcomes) == 2
    assert len(set(alias_outcomes.values())) == 1

    print("OPTIONALITY_EXACT_POLICY_REPLAY_OK")

Expected output:

    OPTIONALITY_EXACT_POLICY_REPLAY_OK

This verifies the finite decision contract and the two counterexamples.
The Shannon information identity uses the stipulated *perfect* observation
of a uniform binary label; no general entropy or Bayesian exploration theorem
is being asserted. All claims remain conditional on the declared action
feasibility, terminal reward and clairvoyant comparator.

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
