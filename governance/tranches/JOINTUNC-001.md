# JOINTUNC-001 — Transaction Receipt

## Identity
- chapter: ATLAS-CH-JOINTUNC-001
- implementation issue: #243
- protected baseline: c6b690725a0c89dd1746015d3e688c50553e0f28
- branch: work/jointunc-243

## Hard prerequisites

RLBASE-001:
- manuscript a99f78b788b97bc1bb3346ca1f1b97802c0f84db
- source lock b29ecea9134227cb5ce3fcd7cc47303a90bd6699
- AUDIT-017 8b7a1f9b61c15ab9c2c010ea538e25c11a7ed1cc

INFO-001:
- manuscript 0fca10cbc7476c5b729ee15dfad0dec563665821
- source lock ea5a1b0db3aadf052fc0b749d7e813bb0ca5d43c
- AUDIT-004 948f76b3f86d27fa4830efc30d8ef0135134256e

## Source decision
- no new external academic authority added;
- exact affine covariance propagation is proved directly;
- nonlinear grad-F / covariance propagation is stated only as a local first-order approximation with explicit remainder terms.

## Implementation artifacts
- specification 0b09fc62d7eacea48c9c0ab0d71971011421d595
- derivations e3aeae34aa3e03f663f1492fe3a9d4d0950c8be2
- witness e3562d3029924cc349aa73bea3b191bfaaef47ba
- manuscript 8d9072371a5d0e168903e04feb232bde93a55447
- source lock 07e57b2c523baa4297c7cddb6fbf3e1a95cc1c36
- Chapter Ledger c474886129e0bfb4ae0513bf67ef10cb0b77b3c4
- Source Register 3f97ca6badf30361bbbab282b55f4aff8eaf8225

## Exact affine witness
Local coordinates:
- reward error epsilon_R
- transition-effect error epsilon_T
- observation/belief error epsilon_O
- future-value error epsilon_V

Declared decision error:
- delta = epsilon_R + epsilon_T + epsilon_O + (1/2) epsilon_V
- sensitivity a = [1,1,1,1/2]

All three cases have marginal variances [1,1,1,1].

Diagonal-only propagation:
- V_diag = 13/4

Positive common shock:
- (epsilon_R,epsilon_T,epsilon_O,epsilon_V)=(U,U,U,W)
- U,W independent centered Rademacher
- exact propagated variance = 37/4
- covariance correction = +6

Cancellation common shock:
- (epsilon_R,epsilon_T,epsilon_O,epsilon_V)=(U,U,-U,W)
- exact propagated variance = 5/4
- covariance correction = -2

Independence control:
- four independent centered Rademacher coordinates
- exact propagated variance = 13/4

## Exact identity
- Var(a^T epsilon)=a^T Sigma a
- expanded covariance correction retained explicitly
- pairwise zero covariance is sufficient for diagonal variance additivity
- full independence is stronger than necessary

## Nonlinear boundary
For differentiable scalar F:
- F(x+epsilon)-F(x)=grad F(x)^T epsilon + R
- exact variance includes grad F^T Sigma grad F + Var(R) + 2 Cov(grad F^T epsilon,R)
- grad F^T Sigma grad F alone is first-order unless the remainder contribution vanishes/is controlled

## Evidence firewall
- same marginal variances do not imply same propagated uncertainty
- zero covariance does not imply independence
- statistical dependence does not imply causal direction
- local first-order propagation does not imply global sequential uncertainty
- same variance does not imply same risk distribution
- expected value and uncertainty remain distinct

## Validation gate
Merge requires exact-head canonical repository validation, independent exact rational witness replay, exact-head GitHub Actions success, and a fresh post-draft audit.
