# REGRET-001 — Regret

## Identity

- chapter: `ATLAS-CH-REGRET-001`
- issue: #110
- baseline: `f94a18010d969f80ddb96663bec02e449f4eb5eb`
- branch: `work/regret-001`
- hard prerequisite: `ATLAS-CH-EXPLORE-001`

Exact prerequisite binds:

- EXPLORE manuscript: `d358ec986bb1baa604668707ae0d598856247d89`
- EXPLORE audit: `f4b76500f62e5d92571e0fcab648d4f3c6d81abf`
- EXPLORE source lock: `44bf1f2ca6f98a1b852f50ecc6eaf2d42cadadcc`

## Central result

Regret is explicitly bound to horizon, environment, policy, reward/loss convention, comparator, and expectation/prior convention.

The chapter separates:

- pathwise mean-benchmark regret;
- expected/pseudo-regret;
- Bayesian regret;
- worst-case/minimax regret;
- comparator-relative regret;
- cumulative versus simple regret.

Exact witnesses show:

- pathwise regret can be negative while pseudo-regret is positive;
- Bayes-optimal and minimax-optimal policies can differ;
- changing only the comparator class changes regret;
- cumulative regret can be positive while final simple regret is zero.

## Durable artifacts

- source lock
- specification
- derivation packet
- exact computational witness
- full manuscript
- Chapter Ledger promotion
- Source Register entry
- bibliography closure

## Remaining gates

Validate, merge implementation, run bounded audit, repair and validate audit, merge, verify closure, recompute frontier, reset controller.
