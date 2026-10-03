# Chapter Specification — ATLAS-CH-DEPTH-001

## Identity

**Title:** Depth as Computational Time  
**Part:** Neural Computation as Dynamics  
**Status:** specification-ready.  
**Epistemic class:** established adaptive-depth mechanisms plus Atlas synthesis.

## Chapter contract

Develop neural depth as a computational-time coordinate while preserving the difference between a useful dynamical interpretation and a literal physical- or continuous-time identity.

The chapter must unify fixed depth, recurrent depth, adaptive halting, equilibrium depth, and conditional block execution through the question: how much computation is allocated before a representation is declared finished?

## Dependency contract

Hard prerequisites:

- ATLAS-CH-NUMERICS-001 — Numerical Methods as Computational Dynamics;
- ATLAS-CH-ARCHHIST-001 — From Layered Networks to Residual Systems.

No Adaptive Depth as Error Control or Conditional Computation chapter may be used as hidden prerequisite authority.

## Reader outcome

A reader should be able to:

1. distinguish physical time, sequence time, optimization iteration, network depth, and computational time;
2. write fixed-depth computation as a depth-indexed state evolution;
3. explain what weight tying changes and does not change;
4. define an input-dependent stopping time;
5. distinguish halting from correctness;
6. interpret equilibrium models as fixed-point problems rather than infinite explicit loops;
7. state why existence of a fixed point is weaker than convergence of a chosen solver;
8. express conditional execution with explicit gates and realized compute;
9. explain why a soft gate is not automatically a hardware skip;
10. state what ADAPTDEPTH-001 and SPARSE-001 may assume after this chapter.

## Formal spine

Fixed depth:

x_{k+1} = F_k(x_k),  k=0,...,L-1.

Tied recurrent depth:

x_{k+1} = F(x_k).

Adaptive depth:

tau(x_0, epsilon, B)
=
inf{k >= 0 : h_k <= epsilon or budget B is exhausted},

where h_k is a declared halting/error/progress signal.

Equilibrium depth:

x* = F(x*).

Conditional execution:

x_{k+1}
=
x_k + g_k(x_k) Delta_k(x_k),

with g_k in {0,1} for hard execution and a declared relaxation when g_k is continuous.

## Computational-time accounting

Define realized computational time as a cost sum

C(x_0)
=
sum_{k=0}^{tau-1} c_k(x_k),

not merely as the integer tau unless every executed step has equal cost.

Keep wall-clock latency, parallel depth, FLOPs, memory traffic, and energy separate.

## Exact computational witness

Create mathematics/computational-witnesses/ATLAS-CW-DEPTH-001.md.

Use

x_{k+1} = (x_k + 2)/2,
x_0 = 0.

Derive

x_k = 2(1-2^{-k}),

and

|x_k-2| = 2^{1-k}.

For tolerance epsilon in (0,2), define the exact minimal stopping depth

tau(epsilon)
=
ceil(log_2(2/epsilon)).

Verify exact values for dyadic tolerances:
- epsilon=1/2 -> tau=2;
- epsilon=1/4 -> tau=3;
- epsilon=1/16 -> tau=5.

The witness demonstrates computational depth as approximation time for one contraction. It does not imply that every deep network is contractive or convergent.

## Mechanism families

### Recurrent depth

Repeated application of a tied transformation.

Use Universal Transformer as a representative mechanism.

### Adaptive halting

Input- or position-dependent number of recurrent steps.

Use Graves ACT and Universal Transformer dynamic halting as representative mechanisms.

### Equilibrium depth

Solve a fixed-point equation rather than store every explicit layer state.

Use Deep Equilibrium Models as the representative mechanism.

### Conditional execution

Skip or execute blocks depending on the input/state.

Use SkipNet as the representative mechanism.

## Figure decision

No governed figure is required for v0.1.

The recurrence, stopping rule, fixed-point equation, gating equation, and exact witness convey the semantics directly.

## Failure boundaries

Include:

- treating depth as physical time without a model;
- unstable or noncontractive recurrence;
- premature halting;
- nontermination or budget exhaustion;
- halting signal that does not track task error;
- equilibrium solver failure or root ambiguity;
- soft gating without realized sparse execution;
- load imbalance under dynamic depth;
- extra controller overhead;
- training/inference mismatch;
- confusing parameter sharing with compute sharing.

## Downstream handoff

ATLAS-CH-ADAPTDEPTH-001 may assume:
- computational-time viewpoint;
- explicit halting/stopping rule;
- exact distinction between depth and numerical error;
- fixed-point and recurrence boundaries.

It must add local error estimation and adaptive-step/error-control semantics.

ATLAS-CH-SPARSE-001 may assume:
- conditional execution gates;
- realized compute accounting;
- distinction between relaxed routing weights and actual skipped work;
- per-input execution paths.

It must add broader sparse/conditional computation, token selection, and hardware implications.

## Acceptance

The draft must:
- preserve the Numerics and Architecture History boundaries;
- define computational time without collapsing it into wall-clock or physical time;
- develop recurrent, adaptive, equilibrium, and conditional depth;
- include the exact contraction witness;
- state the fixed-point/convergence distinction;
- make hard versus soft execution explicit;
- expose resource and stopping failure surfaces;
- identify downstream handoffs by stable chapter ID;
- remain mathematical systems prose rather than a mechanism catalogue.
