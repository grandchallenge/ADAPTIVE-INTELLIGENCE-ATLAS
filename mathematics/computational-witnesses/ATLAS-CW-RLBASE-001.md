# ATLAS-CW-RLBASE-001 — Exact Bellman and Policy Improvement Witness

**Chapter:** ATLAS-CH-RLBASE-001  
**Witness class:** exact finite rational computation

## MDP

Discount:

gamma = 1/2.

States:

s0, s1.

Transitions and rewards:

- s1, action c: reward 2, next state s1;
- s0, action a: reward 0, next state s1;
- s0, action b: reward 2, next state s0.

Initial policy pi:

- pi(s0)=a;
- pi(s1)=c.

## Exact policy evaluation

For s1:

V(s1) = 2 + (1/2)V(s1),

therefore

V(s1)=4.

For s0 under action a:

V(s0)=0+(1/2)V(s1)=2.

Thus:

V^pi = (2,4).

## Policy improvement

Evaluate b at s0 using V^pi:

Q^pi(s0,b)
=
2+(1/2)V^pi(s0)
=
3.

Since

3 > 2,

the greedy improved policy selects b at s0.

Under the improved policy:

V(s0)=2+(1/2)V(s0),

so

V(s0)=4.

State s1 remains at value 4.

Thus:

V^{pi'} = (4,4).

The environment dynamics and rewards are unchanged.

## Replay procedure

    from fractions import Fraction

    gamma = Fraction(1, 2)

    v1 = Fraction(2, 1) / (1 - gamma)
    v0_pi = gamma * v1
    q_b = Fraction(2, 1) + gamma * v0_pi
    v0_improved = Fraction(2, 1) / (1 - gamma)

    print("V_pi_s0=" + str(v0_pi))
    print("V_pi_s1=" + str(v1))
    print("Q_pi_s0_b=" + str(q_b))
    print("V_improved_s0=" + str(v0_improved))
    print("improves=" + str(q_b > v0_pi))

Expected output:

    V_pi_s0=2
    V_pi_s1=4
    Q_pi_s0_b=3
    V_improved_s0=4
    improves=True

## Claim boundary

This witness proves only the exact finite calculation for the declared two-state deterministic discounted MDP.

It does not establish convergence of approximate RL, usefulness of one discount factor, adequacy of the reward specification, robustness to partial observability, or superiority of a particular control algorithm.

Its purpose is to make the separation among environment dynamics, policy, value, and policy improvement exact.
