# DEPTH-001 — Depth as Computational Time

## Status

**Tranche state:** implemented on branch pending merge validation.

## Baseline

- baseline: 015bc4dc465bde59105530cda2ad6d2d3500ab0e;
- issue: #84;
- hard prerequisites:
  - ATLAS-CH-NUMERICS-001 at audited draft-v0.1;
  - ATLAS-CH-ARCHHIST-001 at audited draft-v0.1.

## Objective

Make depth an explicit computational-time coordinate and distinguish fixed, recurrent, adaptive, equilibrium, and conditional execution depth.

## Central objects

Fixed/recurrent update:

x_{k+1}=F_k(x_k)
or
x_{k+1}=F(x_k).

Adaptive stopping:

tau=inf{k: h_k <= epsilon or budget exhausted}.

Equilibrium:

x*=F(x*).

Conditional execution:

x_{k+1}=x_k+g_k(x_k)Delta_k(x_k).

## Exact witness

For

x_{k+1}=(x_k+2)/2,
x_0=0,

the exact solution is

x_k=2(1-2^{-k})

with error

e_k=2^{1-k}.

For epsilon in (0,2),

tau(epsilon)=ceil(log_2(2/epsilon)).

## External mechanism basis

- Graves ACT;
- Universal Transformer;
- Deep Equilibrium Models;
- SkipNet.

These are representative mechanisms, not universal superiority claims.

## Figure decision

No governed figure is added in v0.1.

The recurrence, stopping, equilibrium, gating equations, and exact witness carry the semantics directly.

## Durable objects

- sources/source-locks/ATLAS-CH-DEPTH-001.yaml;
- manuscript/specifications/ATLAS-CH-DEPTH-001.md;
- mathematics/derivations/ATLAS-CH-DEPTH-001-DERIVATIONS.md;
- mathematics/computational-witnesses/ATLAS-CW-DEPTH-001.md;
- manuscript/parts/04-neural-architectures/ATLAS-CH-DEPTH-001.md;
- Chapter Ledger promotion;
- Source Register entry.

## Next step after merge

Run a bounded post-draft audit of source identity, computational-time scope, witness arithmetic, fixed-point/convergence distinctions, hard/soft gating, realized compute accounting, and downstream handoffs.
