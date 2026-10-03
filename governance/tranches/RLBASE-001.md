# RLBASE-001 — Reinforcement Learning and Control

## Status

**Tranche state:** implemented on branch pending merge validation.

## Baseline

- baseline: 17e85ed4002bc6d176b4cd787fa46a0af73a73c5;
- issue: #80;
- hard prerequisites:
  - ATLAS-CH-DYN-001 at draft-v0.1;
  - ATLAS-CH-INFO-001 at draft-v0.1.

## Objective

Establish the controlled stochastic-decision substrate consumed by Exploration and Joint Uncertainty.

## Central object

M = (S, A, P, r, gamma, rho_0).

The chapter keeps environment dynamics, policy, reward, return, value, model, uncertainty, and observability distinct.

## Exact witness

A two-state deterministic MDP with gamma=1/2 gives:

- initial policy value V^pi=(2,4);
- alternative action value Q^pi(s0,b)=3;
- improved policy value V^{pi'}=(4,4).

The environment is unchanged; only the policy changes.

## External basis

Source lock includes Bellman, Sutton and Barto, Watkins-Dayan Q-learning, Williams REINFORCE, Sutton Dyna, and Kaelbling-Littman-Cassandra POMDPs.

## Figure decision

No governed figure is added in v0.1.

The finite MDP table and Bellman equations are semantically sufficient.

## Durable objects

- sources/source-locks/ATLAS-CH-RLBASE-001.yaml;
- manuscript/specifications/ATLAS-CH-RLBASE-001.md;
- mathematics/derivations/ATLAS-CH-RLBASE-001-DERIVATIONS.md;
- mathematics/computational-witnesses/ATLAS-CW-RLBASE-001.md;
- manuscript/parts/11-decision-making/ATLAS-CH-RLBASE-001.md;
- Chapter Ledger promotion;
- Source Register entry.

## Next step after merge

Run a bounded post-draft audit of Bellman equations, witness arithmetic, source scope, reward/value/uncertainty boundaries, approximation caveats, POMDP semantics, and downstream handoffs.
