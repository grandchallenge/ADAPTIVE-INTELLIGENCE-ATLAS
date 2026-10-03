# Chapter Specification — ATLAS-CH-RLBASE-001

## Identity

**Title:** Reinforcement Learning and Control  
**Part:** Decision Making Under Uncertainty  
**Status:** specification-ready.  
**Epistemic class:** established RL/control foundations plus Atlas synthesis.

## Chapter contract

Develop the mathematical substrate for sequential decision making under stochastic dynamics before later chapters add exploration, regret, optionality, and joint uncertainty.

The chapter must make environment, policy, reward, return, value, model, and uncertainty distinct objects.

## Dependency contract

Hard prerequisites:

- ATLAS-CH-DYN-001 — Dynamics;
- ATLAS-CH-INFO-001 — Probability, Information, and Statistical Structure.

## Reader outcome

A reader should be able to:

1. define a finite Markov decision process;
2. distinguish policy from environment dynamics;
3. define discounted return, state value, and action value;
4. derive Bellman expectation and optimality equations;
5. explain policy evaluation and policy improvement;
6. distinguish dynamic programming from sampled temporal-difference updates;
7. state what Q-learning estimates and what its classical convergence theorem assumes;
8. recognize REINFORCE as a stochastic policy-gradient estimator rather than a Bellman backup;
9. explain model-based planning and Dyna;
10. explain why POMDP control acts on information state or belief rather than hidden state directly.

## Formal spine

Use a discounted MDP

M = (S, A, P, r, gamma, rho_0),

with:

- state space S;
- admissible actions A(s);
- transition kernel P(s'|s,a);
- reward model r(s,a,s');
- discount gamma in [0,1);
- initial-state distribution rho_0.

For policy pi(a|s), define

G_t = sum_{k=0}^\infty gamma^k R_{t+k+1},

V^pi(s) = E_pi[G_t | S_t=s],

Q^pi(s,a) = E_pi[G_t | S_t=s,A_t=a].

Use Bellman expectation and optimality operators explicitly.

## Computational witness

Create mathematics/computational-witnesses/ATLAS-CW-RLBASE-001.md.

Use a two-state deterministic discounted MDP with gamma=1/2.

At state s1 the only action yields reward 2 and returns to s1.

At state s0:

- action a yields reward 0 and moves to s1;
- action b yields reward 2 and returns to s0.

Under policy pi choosing a at s0:

V^pi(s1)=4,
V^pi(s0)=2.

But

Q^pi(s0,b)=3 > V^pi(s0)=2,

so one policy-improvement step switches s0 to b.

Under the improved policy:

V(s0)=4,
V(s1)=4.

Verify all equalities exactly with rational arithmetic.

## Figure decision

No governed figure is required for v0.1.

The state/action table and Bellman equations carry the semantics more precisely than a decorative control-loop figure.

## Failure boundaries

Include:

- non-Markov state representation;
- reward misspecification;
- function-approximation error;
- bootstrapping instability;
- distribution shift under off-policy learning;
- learned-model error;
- partial observability;
- discount/horizon mismatch;
- conflating estimated value with calibrated uncertainty;
- interpreting optimization of a declared reward as universal desirability.

## Downstream handoff

ATLAS-CH-EXPLORE-001 may assume the MDP/value/Bellman substrate and must add information acquisition and exploration-exploitation.

ATLAS-CH-JOINTUNC-001 may assume the same substrate and must add joint treatment of transition, reward, observation, and future-value uncertainty.

## Acceptance

The draft must:
- define the MDP and value objects exactly;
- derive Bellman expectation and optimality equations;
- distinguish policy evaluation from improvement;
- include sampled TD/Q-learning and policy-gradient roles without collapsing them;
- develop model-based/Dyna and POMDP boundaries;
- include the exact two-state witness;
- preserve reward/value/uncertainty distinctions;
- state optimality relative to the declared problem;
- remain mathematical/control prose rather than an algorithm catalogue.
