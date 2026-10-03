# AUDIT-017 — Reinforcement Learning and Control

## Disposition

**PASS WITH THREE FORMAL PRECISION REPAIRS AND ONE SOURCE-METADATA REPAIR**

ATLAS-CH-RLBASE-001 remains at draft-v0.1.

The chapter correctly establishes the finite discounted MDP substrate consumed by later exploration and joint-uncertainty chapters. It keeps environment dynamics, policy, reward, return, value, model, uncertainty, and observability separate.

The audit made four bounded repairs:

1. Bellman's 1957 paper is now identified in its original venue, Journal of Mathematics and Mechanics, volume 6, issue 5, pages 679-684.
2. The discounted-return discussion now states the finite/bounded reward assumption under which gamma<1 gives a bounded infinite discounted return.
3. The Bellman contraction statement now names its domain: bounded real-valued functions on the finite state space with the sup norm.
4. REINFORCE and POMDP belief-state statements now make their trajectory/posterior assumptions explicit.

No Bellman equation, policy-improvement calculation, witness result, Q-learning boundary, or downstream handoff required reversal.

## Audited baseline

- RLBASE-001 merge:
  39932c4067bd3d3f85a4d223586875cd2063e3b7;
- drafting baseline:
  17e85ed4002bc6d176b4cd787fa46a0af73a73c5;
- audit issue:
  #82;
- chapter:
  ATLAS-CH-RLBASE-001.

## 1. Prerequisites

PASS.

The source lock binds:

- ATLAS-CH-DYN-001 manuscript blob f4aa89075f221529401e56a152a6cdfca3dcc47d;
- AUDIT-008A blob 525254a67510636cf39b0758c300c77a479de9a5;
- ATLAS-CH-INFO-001 manuscript blob 0fca10cbc7476c5b729ee15dfad0dec563665821;
- AUDIT-004 blob 948f76b3f86d27fa4830efc30d8ef0135134256e.

No Exploration or Joint Uncertainty manuscript is used as hidden prerequisite authority.

## 2. External source basis

PASS AFTER METADATA REPAIR.

The source lock identifies:

- Richard Bellman, A Markovian Decision Process, Journal of Mathematics and Mechanics 6(5), 679-684, 1957, DOI 10.1512/iumj.1957.6.56038;
- Sutton and Barto, Reinforcement Learning: An Introduction, 2nd ed., MIT Press, 2018, ISBN 9780262039246;
- Watkins and Dayan, Q-learning, Machine Learning 8, 279-292, DOI 10.1007/BF00992698;
- Williams, REINFORCE, Machine Learning 8, 229-256, DOI 10.1007/BF00992696;
- Sutton, Dyna, ICML 1990, 216-224, DOI 10.1016/B978-1-55860-141-3.50030-4;
- Kaelbling, Littman, and Cassandra, Planning and Acting in Partially Observable Stochastic Domains, Artificial Intelligence 101, 99-134, DOI 10.1016/S0004-3702(98)00023-X.

Their roles remain representative and scoped.

## 3. MDP object

PASS.

The chapter defines

M = (S, A, P, r, gamma, rho_0)

and keeps policy pi separate from environment dynamics P.

Optimality is explicitly relative to the declared state/action/reward/dynamics/discount/observation problem.

## 4. Return and value

PASS AFTER PRECISION REPAIR.

The chapter now states finite one-step rewards in the finite MDP section. Hence the reward table is bounded, and for gamma<1 the discounted return is absolutely bounded.

V^pi and Q^pi are correctly defined as conditional expected returns.

The manuscript explicitly denies that value is itself calibrated uncertainty.

## 5. Bellman expectation equation

PASS.

The displayed expectation equation correctly conditions over policy action choice and transition dynamics.

The distinction between exact Bellman identity and approximate learned representation is preserved.

## 6. Contraction and fixed point

PASS AFTER PRECISION REPAIR.

The formal packet now states that T^pi acts on bounded real-valued functions over the finite state space and is a gamma-contraction in the sup norm.

The unique fixed-point conclusion is therefore stated on an explicit function space.

## 7. Bellman optimality and policy improvement

PASS.

The optimality operator is correctly defined with a maximizing action.

The policy-improvement claim is restricted to the exact finite discounted setting.

The text explicitly rejects transferring that theorem automatically to an inaccurate learned critic.

## 8. Exact computational witness

PASS.

ATLAS-CW-RLBASE-001 uses gamma=1/2 and exact Fraction arithmetic.

The replayed values are:

- V_pi(s0)=2;
- V_pi(s1)=4;
- Q_pi(s0,b)=3;
- V_improved(s0)=4;
- improvement test true.

The environment and reward function remain unchanged between the two policies.

## 9. Temporal-difference update

PASS.

The one-step TD update is correctly presented as a sampled stochastic-approximation step toward a Bellman fixed point, not as the Bellman identity itself.

## 10. Q-learning

PASS.

The tabular Q-learning update is standard.

The chapter preserves the Watkins-Dayan theorem boundary by requiring classical sampling and learning-rate conditions and explicitly refusing automatic transfer to arbitrary nonlinear function approximation, replay, target-network, or nonstationary settings.

## 11. Policy gradient

PASS AFTER PRECISION REPAIR.

The formal packet now states the score-function structure

grad log pi_theta(A_t|S_t) G_t

and ties equality in expectation to the declared trajectory-distribution assumptions.

The manuscript no longer uses loose "unbiased-style" wording.

Policy-gradient and Bellman/value-estimation routes remain distinct even though actor-critic methods may combine them.

## 12. Model-based reinforcement learning

PASS.

Dyna is used as a representative integration of direct experience, model learning, and planning.

The chapter explicitly introduces model error as an additional failure surface.

Planning with a learned model is not promoted into planning with the real environment.

## 13. Partial observability

PASS AFTER PRECISION REPAIR.

Belief state is defined as a posterior over hidden states conditioned on available history.

The Markov-information-state statement is now scoped to the standard POMDP model with fixed transition/observation kernels and exact posterior updating from complete available history.

Approximate memory is not granted exact sufficiency.

## 14. Reward, value, and uncertainty

PASS.

The chapter explicitly distinguishes reward from human or moral value and value from uncertainty, information value, safety, and recoverability.

This is the correct handoff boundary for the later decision chapters.

## 15. Downstream handoff

PASS.

ATLAS-CH-EXPLORE-001 may assume the MDP, return, value, Bellman, and model-based/model-free substrate.

ATLAS-CH-JOINTUNC-001 may assume the same controlled stochastic substrate plus the Information prerequisite.

Both are identified by stable chapter ID.

## 16. Integrity

PASS.

The manuscript, derivation packet, and witness contain no hidden C0 control characters or tabs.

The Chapter Ledger records ATLAS-CH-RLBASE-001 at draft-v0.1.

The Source Register contains ATLAS-SRC-RLBASE-LOCK-001.

The witness contains an explicit Claim boundary.

## 17. Final disposition

AUDIT-017 passes with the bounded precision repairs above.

The Atlas now has an explicit progression from dynamics and probability to controlled stochastic decision making, with the Bellman substrate available for later exploration, regret, optionality, and joint uncertainty work.
