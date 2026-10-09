# ATLAS-CH-DEPTH-001 — Formal and Derivation Packet

## Purpose

This packet records the exact depth/computational-time objects and the finite witness used by the chapter.

## 1. Fixed depth

A depth-L network is written

\[
x_{k+1}=F_k(x_k),\qquad k=0,\ldots,L-1.
\]

The final state is

\[
x_L=(F_{L-1}\circ\cdots\circ F_0)(x_0).
\]

The index k orders computation.

No physical-time interpretation follows from this equation alone.

## 2. Recurrent depth

If parameters/operators are tied,

\[
x_{k+1}=F(x_k).
\]

The computation now reuses one transformation across depth.

Weight tying changes parameterization.

It does not imply:

- F is a contraction;
- the sequence converges;
- later states improve monotonically;
- arbitrarily many iterations are useful.

## 3. Computational time

Let \(c_k(x_k)\ge0\) be the realized cost of executed step \(k\) in one declared resource unit.

For a stopping depth tau, define

\[
C(x_0)=\sum_{k=0}^{\tau-1}c_k(x_k).
\]

If several heterogeneous resources are tracked simultaneously, use a resource vector rather than summing unlike units without a declared scalarization.

Only when all c_k are the same normalized unit does tau itself equal total compute cost.

Thus the following should be separated:

- number of sequential state transitions;
- arithmetic operation count;
- memory traffic;
- parallel critical-path depth;
- wall-clock latency;
- energy.

## 4. Adaptive stopping

Let h_k be a declared halting signal, epsilon a threshold, and K_max a finite depth cap induced by the current budget.

Define

\[
\tau=\min\left(\{k\in\{0,\ldots,K_{\max}\}:h_k\le\varepsilon\}\cup\{K_{\max}\}\right).
\]

Record the termination status separately:

- `criterion_met` if \(h_\tau\le\varepsilon\);
- `budget_exhausted` otherwise.

This makes termination total under the finite cap without pretending budget exhaustion satisfies the numerical/task criterion.

The definition still does not say that h_k is a calibrated error estimator.

That extra relation is deferred to ATLAS-CH-ADAPTDEPTH-001.

## 5. Exact contraction witness

Consider

\[
x_{k+1}=\frac{x_k+2}{2},\qquad x_0=0.
\]

The fixed point \(x_\star=2\) satisfies

\[
2=\frac{2+2}{2}.
\]

Subtract the fixed point:

\[
x_{k+1}-2=\frac12(x_k-2).
\]

Hence

\[
x_k-2=2^{-k}(x_0-2)=-2^{1-k}.
\]

Therefore

\[
x_k=2(1-2^{-k}),\qquad |x_k-2|=2^{1-k}.
\]

This is exact.

## 6. Exact stopping depth

For epsilon in (0,2), require

\[
2^{1-k}\le\varepsilon.
\]

Equivalently,

\[
k\ge\log_2\!\left(\frac{2}{\varepsilon}\right).
\]

The minimal integer depth is

\[
\tau(\varepsilon)=\left\lceil\log_2\!\left(\frac{2}{\varepsilon}\right)\right\rceil.
\]

For dyadic tolerances:

epsilon=1/2:
tau=2;

epsilon=1/4:
tau=3;

epsilon=1/16:
tau=5.

The recurrence therefore gives a concrete instance where requested approximation tolerance determines computation depth.

## 7. Fixed depth versus tolerance-driven depth

A fixed-depth system chooses K before seeing its stopping criterion.

Its error in the witness is

\[
e_K=2^{1-K}.
\]

A tolerance-driven system chooses the smallest k satisfying the declared threshold.

The two systems can execute the same recurrence.

What differs is the stopping policy.

Thus adaptive depth can be studied independently of changing the transformation itself.

## 8. Fixed points and equilibrium depth

An equilibrium model seeks x* satisfying

\[
x_\star=F(x_\star).
\]

This equation states a root/fixed-point condition.

It does not identify a unique numerical method.

Naive iteration

x_{k+1}=F(x_k)

is one possible solver.

Newton, quasi-Newton, Anderson-like acceleration, or other root-finding methods may follow different trajectories.

Therefore:

\[
\text{equilibrium definition}\neq\text{explicit infinite unrolling}.
\]

For a contraction on a complete metric space, fixed-point iteration has a standard convergence guarantee.

Without such conditions, existence, uniqueness, and solver convergence require separate analysis.

## 9. Conditional execution

A residual-style conditional block can be written

\[
x_{k+1}=x_k+g_k(x_k)\Delta_k(x_k).
\]

For a hard gate

\[
g_k\in\{0,1\},
\]

g_k=0 leaves the state unchanged across that block and permits an implementation to skip Delta_k.

For a relaxed gate

\[
g_k\in[0,1],
\]

Delta_k may still need to be computed in order to multiply it by g_k.

Therefore a small soft coefficient is not itself realized computational sparsity.

## 10. Realized path

For hard gates, define the active set

\[
\mathcal A(x_0)=\{k:g_k(x_k)=1\}.
\]

If block k has cost c_k, realized block cost is

\[
C_{\mathrm{block}}(x_0)=\sum_{k\in\mathcal A(x_0)}c_k,
\]

plus controller/gating overhead.

Input-dependent paths can reduce average executed work while increasing variance or load imbalance.

## 11. Recurrent and adaptive mechanisms

Graves ACT supplies a representative differentiable halting mechanism for recurrent computation.

Universal Transformer supplies a representative depth-wise recurrent transformation and dynamic per-position halting mechanism.

These sources demonstrate concrete mechanisms.

They do not establish that every task benefits from deeper recurrence or adaptive halting.

## 12. Equilibrium mechanism

Deep Equilibrium Models solve for an equilibrium of a weight-tied transformation and use implicit differentiation.

The Atlas consumes the mechanism at this structural level.

Claims about constant-memory training or empirical performance remain claims of that source under its implementation and experimental conditions.

## 13. Conditional routing mechanism

SkipNet learns an input-dependent policy for skipping residual blocks.

The Atlas uses it to demonstrate that effective execution depth can depend on the input.

The chapter does not infer that all conditional-compute systems save wall-clock time, because realized speed depends on hardware, batching, branch divergence, scheduling, and overhead.

## 14. Downstream handoff

ATLAS-CH-ADAPTDEPTH-001 may consume:

- x_{k+1}=F_k(x_k);
- recurrent tied depth;
- stopping time tau;
- computational cost C;
- fixed-point/equilibrium boundary.

It must add error-control semantics.

ATLAS-CH-SPARSE-001 may consume:

- hard/soft gates;
- active execution set A(x);
- realized block cost;
- input-dependent path semantics.

It must add broader sparse and conditional computation.

## Claim boundary

This packet proves the closed form and stopping depth for one scalar contraction and gives exact bookkeeping identities for the declared computation models.

It does not prove that neural-network depth is physical time, that arbitrary learned recurrences converge, that learned halting signals estimate error, or that conditional routing guarantees hardware speedup.
