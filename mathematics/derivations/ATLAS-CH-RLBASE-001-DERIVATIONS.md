# ATLAS-CH-RLBASE-001 — Formal and Derivation Packet

## Purpose

This packet records the exact finite-control objects and derivations used by Reinforcement Learning and Control.

## 1. MDP object

A discounted finite Markov decision process is

M = (S, A, P, r, gamma, rho_0).

For state s and admissible action a:

P(s'|s,a)

is a probability distribution over next states and

r(s,a,s')

is the one-step reward associated with that transition.

A policy pi(a|s) is a separate object.

The environment does not become a policy merely because both appear in the same expectation.

## 2. Return and value

For gamma in [0,1),

G_t = sum_{k=0}^\infty gamma^k R_{t+k+1}.

The state value under policy pi is

V^pi(s) = E_pi[G_t | S_t=s].

The action value is

Q^pi(s,a) = E_pi[G_t | S_t=s,A_t=a].

These are expectations, not uncertainty intervals.

## 3. Bellman expectation equation

Condition on the first transition.

V^pi(s)
=
sum_a pi(a|s)
sum_{s'} P(s'|s,a)
[
r(s,a,s') + gamma V^pi(s')
].

Equivalently,

V^pi = T^pi V^pi,

where T^pi is the Bellman expectation operator.

For a finite discounted MDP, T^pi is a gamma-contraction in the sup norm and therefore has a unique fixed point.

## 4. Bellman optimality

Define

(T V)(s)
=
max_a
sum_{s'} P(s'|s,a)
[
r(s,a,s') + gamma V(s')
].

The optimal value V* satisfies

V* = T V*.

An optimal policy may choose any action attaining the maximum.

This optimality is relative to the declared MDP, reward, discount, and state representation.

## 5. Policy improvement

Given V^pi, choose a greedy policy pi' satisfying

pi'(s) in argmax_a Q^pi(s,a).

In the exact finite discounted setting, the policy-improvement theorem gives

V^{pi'}(s) >= V^pi(s)

for all states.

This theorem does not say that a greedy update under an inaccurate learned critic must improve real-world performance.

## 6. Exact two-state witness

Let gamma=1/2.

State s1 has one action c:

s1 --c, reward 2--> s1.

State s0 has two actions:

s0 --a, reward 0--> s1;

s0 --b, reward 2--> s0.

Under policy pi choosing a at s0 and c at s1:

V^pi(s1) = 2 + (1/2)V^pi(s1),

so

V^pi(s1)=4.

Then

V^pi(s0)
=
0 + (1/2)V^pi(s1)
=
2.

Evaluate the alternative:

Q^pi(s0,b)
=
2 + (1/2)V^pi(s0)
=
3.

Therefore b is strictly greedy over a at s0.

For the improved policy pi' choosing b at s0:

V^{pi'}(s0)
=
2 + (1/2)V^{pi'}(s0),

hence

V^{pi'}(s0)=4.

The environment did not change.

Only the policy changed.

## 7. Dynamic programming

If P and r are known, policy evaluation can be performed by repeated application of T^pi.

Value iteration repeatedly applies T.

Policy iteration alternates:

1. evaluate the current policy;
2. improve greedily.

These procedures use the model directly.

## 8. Sampled temporal-difference update

When the transition model is not directly used, a one-step TD value update can use a sampled transition

(S_t,R_{t+1},S_{t+1}):

V(S_t)
<-
V(S_t)
+
alpha
[
R_{t+1} + gamma V(S_{t+1}) - V(S_t)
].

The bracketed quantity is a temporal-difference error.

This is a sampled stochastic approximation to a fixed-point relation, not the Bellman identity itself.

## 9. Q-learning

For a sampled transition (S_t,A_t,R_{t+1},S_{t+1}), tabular Q-learning uses

Q(S_t,A_t)
<-
Q(S_t,A_t)
+
alpha_t
[
R_{t+1}
+
gamma max_a Q(S_{t+1},a)
-
Q(S_t,A_t)
].

Watkins and Dayan prove convergence in the tabular setting under conditions including repeated sampling and suitable learning-rate assumptions.

The theorem does not transfer automatically to arbitrary nonlinear function approximation, replay schemes, target networks, or nonstationary environments.

## 10. Policy gradients

Let pi_theta be a differentiable stochastic policy and J(theta) its expected return.

REINFORCE uses sampled returns to form an unbiased-style stochastic gradient estimator of the policy objective under its stated assumptions.

This route differentiates the policy objective directly.

It is conceptually distinct from solving a Bellman optimality fixed point, even though modern actor-critic systems combine both viewpoints.

## 11. Model-based reinforcement learning

A learned model approximates transition and reward structure.

Planning then applies updates using simulated or predicted transitions.

Dyna is a representative architecture in which direct experience, model learning, and planning updates coexist.

Model-based control adds a new error surface:

planning quality now depends on model quality in the regions where planning relies on it.

## 12. Partial observability

In a POMDP, hidden state S_t is not directly observed.

The controller receives observations generated from an observation model.

A belief state

b_t(s) = P(S_t=s | history_t)

is a probability distribution over hidden states given available history.

Under standard POMDP assumptions, the belief state can itself serve as a sufficient information state for control.

This does not mean finite approximate memories preserve exact belief-state sufficiency.

## 13. Reward and value boundary

Reward is part of the modeled control problem.

Value is expected cumulative reward under a policy and environment.

Neither object is automatically:

- calibrated uncertainty;
- human preference;
- moral value;
- safety;
- recoverability;
- information value.

Later chapters add some of these dimensions explicitly.

## Claim boundary

This packet establishes the stated finite discounted MDP identities and the exact two-state policy-improvement calculation.

External sources support the standard algorithms and convergence results only under their own assumptions.

No claim is made that reward maximization under an arbitrary specification is universally desirable or that approximate RL inherits every theorem of the tabular exact setting.
