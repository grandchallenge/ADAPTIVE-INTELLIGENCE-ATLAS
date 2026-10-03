# AUDIT-018 — Depth as Computational Time

## Disposition

**PASS WITH TWO FORMAL PRECISION REPAIRS AND ONE SOURCE-METADATA REPAIR**

ATLAS-CH-DEPTH-001 remains at draft-v0.1.

The chapter correctly separates architectural depth, recurrent execution, adaptive stopping, equilibrium solving, conditional execution, and realized compute. It preserves the audited Numerics boundary that a network update may support a computational-time or discretization lens without thereby becoming physical time or one uniquely identified ODE.

The audit made three bounded repairs:

1. Universal Transformer and Deep Equilibrium Model records now separate conference identity from their arXiv DOI metadata.
2. Budgeted halting now uses an explicit finite depth cap and records criterion_met versus budget_exhausted instead of conflating both events in one stopping predicate.
3. Realized compute is scalar only for one declared resource unit; heterogeneous resource accounting is explicitly vector-valued unless a scalarization is declared.

No recurrence identity, fixed-point boundary, contraction witness, hard/soft gating distinction, or downstream handoff required reversal.

## Audited baseline

- DEPTH-001 merge:
  4ef01e5c1d88a09e107a8ca95ed7fc9fb9766855;
- drafting baseline:
  015bc4dc465bde59105530cda2ad6d2d3500ab0e;
- audit issue:
  #86;
- chapter:
  ATLAS-CH-DEPTH-001.

## 1. Hard prerequisites

PASS.

The source lock binds:

- ATLAS-CH-NUMERICS-001 blob a719a16e86d1feb76679e1f1cda2d9d3393d2e42;
- AUDIT-009 blob 2bbb1b7687d6c4b8c0bfeed5206de836dac92dca;
- ATLAS-CH-ARCHHIST-001 blob 3d373695ed5516dbc3b0557112f204636e911897;
- AUDIT-010 blob c9aa1488b5041805e4695f00f462f3773a27dedf.

No Adaptive Depth or Conditional Computation manuscript is used as hidden prerequisite authority.

## 2. External mechanism sources

PASS AFTER METADATA REPAIR.

The source lock identifies:

- Alex Graves, Adaptive Computation Time for Recurrent Neural Networks, arXiv:1603.08983, 2016;
- Dehghani, Gouws, Vinyals, Uszkoreit, and Kaiser, Universal Transformers, ICLR 2019, OpenReview HyzdRiR9Y7, arXiv:1807.03819;
- Bai, Kolter, and Koltun, Deep Equilibrium Models, NeurIPS 2019, arXiv:1909.01377;
- Wang, Yu, Dou, Darrell, and Gonzalez, SkipNet, ECCV 2018, pp. 409-424, arXiv:1711.09485.

Each source is used for a representative mechanism, not a universal superiority claim.

## 3. Time-coordinate separation

PASS.

The manuscript distinguishes:

- physical time;
- sequence time;
- optimization iteration;
- network depth;
- computational time.

Depth is presented as an ordered coordinate of computation, not as physical time by definition.

## 4. Fixed and recurrent depth

PASS.

The fixed-depth object

x_{k+1}=F_k(x_k)

and tied recurrence

x_{k+1}=F(x_k)

are correctly separated.

The chapter explicitly states that weight tying does not imply contraction, convergence, monotone improvement, or usefulness of unbounded iteration.

## 5. Budgeted halting

PASS AFTER FORMAL REPAIR.

The original draft used an infimum over a criterion-or-budget predicate, which stopped execution but did not preserve whether the task criterion or resource cap caused termination.

The repaired definition uses a finite K_max:

tau
=
min(
{k in {0,...,K_max}: h_k <= epsilon}
union
{K_max}
).

It separately records:

- criterion_met if h_tau <= epsilon;
- budget_exhausted otherwise.

Thus budget exhaustion is not mislabeled convergence.

## 6. Exact contraction witness

PASS.

For

x_{k+1}=(x_k+2)/2,
x_0=0,

the derivation gives

x_k=2(1-2^{-k})

and

|x_k-2|=2^{1-k}.

For epsilon in (0,2),

tau(epsilon)
=
ceil(log_2(2/epsilon)).

The exact dyadic checks are correct:

- epsilon=1/2 -> 2;
- epsilon=1/4 -> 3;
- epsilon=1/16 -> 5.

## 7. Fixed point versus solver convergence

PASS.

The chapter distinguishes the equilibrium equation

x*=F(x*)

from a particular solver.

Naive fixed-point iteration is only one possible numerical route.

Existence of an equilibrium is not promoted into convergence of arbitrary iteration.

The contraction witness is explicitly local to its declared affine map.

## 8. Adaptive-depth mechanism scope

PASS.

Graves ACT and Universal Transformer dynamic halting are used to demonstrate implementable variable-computation mechanisms.

The chapter explicitly denies that a learned halting signal is automatically a calibrated task-error estimator.

That stronger relation is deferred to ATLAS-CH-ADAPTDEPTH-001.

## 9. Conditional execution

PASS.

For the residual-style gated update

x_{k+1}
=
x_k + g_k(x_k) Delta_k(x_k),

the manuscript separates hard gates g_k in {0,1} from relaxed gates g_k in [0,1].

A soft coefficient is not treated as realized sparse execution when Delta_k must still be evaluated.

SkipNet is used only as a representative input-dependent block-skipping mechanism.

## 10. Realized computation

PASS AFTER FORMAL REPAIR.

For one declared resource unit, realized cost is

C(x_0)
=
sum_{k=0}^{tau-1} c_k(x_k).

When FLOPs, memory traffic, energy, and latency proxies are tracked simultaneously, the repaired chapter uses a resource vector rather than adding unlike units without a declared objective/scalarization.

Sequential depth tau is therefore not silently equated with wall-clock latency.

## 11. Depth coordinates

PASS.

The chapter distinguishes:

- architectural depth;
- parameter depth;
- execution depth.

These coincide in a simple untied feed-forward stack but separate under tied recurrence, equilibrium solving, and conditional execution.

## 12. Failure surfaces

PASS.

The manuscript identifies:

- unstable/noncontractive recurrence;
- premature halting;
- criterion/budget distinction;
- solver failure or root ambiguity;
- soft gating without skipped execution;
- routing overhead;
- load imbalance;
- training/inference mismatch;
- oversmoothing/collapse or degraded states under excess depth.

Depth is explicitly not a quality score.

## 13. Downstream handoff

PASS.

ATLAS-CH-ADAPTDEPTH-001 may inherit computational time, stopping semantics, recurrence/fixed-point distinctions, and resource accounting, then add numerical error-control semantics.

ATLAS-CH-SPARSE-001 may inherit hard/soft gating, active execution paths, and realized cost, then add broader conditional/sparse computation and hardware implications.

Both consumers are identified by stable chapter ID.

## 14. Integrity

PASS.

The manuscript, formal packet, and witness contain no hidden C0 control characters or tabs.

The Chapter Ledger records ATLAS-CH-DEPTH-001 at draft-v0.1.

The Source Register contains ATLAS-SRC-DEPTH-LOCK-001.

The witness contains an explicit Claim boundary.

No governed figure is registered, consistent with the tranche decision.

## 15. Final disposition

AUDIT-018 passes with the bounded precision repairs above.

The Atlas now has a stable computational-time object: depth may be fixed, recurrent, adaptively halted, solved to equilibrium, or conditionally executed without collapsing any of those mechanisms into physical time, guaranteed convergence, or guaranteed hardware savings.
