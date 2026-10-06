# AUDIT-055 — Adaptive Depth as Error Control

## Disposition

**PASS — NO REPAIR**

ATLAS-CH-ADAPTDEPTH-001 remains at draft-v0.1.

The audit found no mathematical, epistemic, source-scope, dependency, citation, or documentary defect requiring repair.

No publication, theorem certification, or release promotion is implied.

## Audited baseline

- implementation merge: e4ead968c9c38bc4c99f40ef154437adbfe58200
- implementation PR: #220
- implementation issue: #219
- audit issue: #221
- chapter: ATLAS-CH-ADAPTDEPTH-001

Merged implementation artifact blobs:

- specification: 00cd2477035b9d106a8b16157e03520d1652e67e
- derivation packet: cd67d0d4fb987ddbc6cbe4c25192f593f8a7007c
- computational witness: 6d4240764b3e7be447f436d330ca4b88174ac22f
- manuscript: 61d47ce36a825effb75c246501ca8b66f446261e
- source lock: 717bbe901d7bc4514919f70bd65a1712e6d3aae7
- Chapter Ledger: 487fb507262ca9520d37e42397c3dc52f375ac6b
- Source Register: 4b5b06e0c702eaa79eb7a0771b15ab10a860762b
- bibliography: 7a7a89bc7c3789e0865755e446ee41d7d95815f2
- transaction receipt: d98a533564fb6f8b43d280501cc590e50f526bfb

## 1. Hard prerequisite identity

PASS.

The source lock binds exactly to current protected baseline e8129376ef673822ed6b43775a0d2439b88c47fb.

Depth as Computational Time:

- manuscript: 9d365778e873217c40604a621dbe9f88ca2153e0
- source lock: b6c18e2e0e3ab82c65d830967e2874bfb41e9bb2
- AUDIT-018: 0c9f5405bd7d94018d76aa93ebe74ec3e505cabe

Networks as Numerical Schemes:

- manuscript: cbaf0b96c996c821df50f985075f64028459c587
- source lock: 02bbe77d19da4a6a123e430f8aae058d666c4e35
- AUDIT-023: 746e0c297e4ddf29122d4735108becc33e599030

No downstream architecture-state chapter is used as hidden prerequisite authority.

## 2. External source scope

PASS.

The source lock uses:

- Graves, Adaptive Computation Time for Recurrent Neural Networks, for learned recurrent compute allocation;
- Figurnov et al., Spatially Adaptive Computation Time for Residual Networks, for learned spatially varying compute allocation;
- Dormand and Prince, A family of embedded Runge-Kutta formulae, for embedded numerical formulas of differing order and their local-error-control role.

The chapter does not claim:

- learned halting = local truncation error;
- spatially adaptive network depth = adaptive PDE mesh;
- embedded Runge-Kutta adaptation = learned neural halting;
- any of these mechanisms is universally compute-optimal.

The Dormand-Prince bibliographic identity is consistent with Journal of Computational and Applied Mathematics 6(1), 19-26 (1980), DOI 10.1016/0771-050X(80)90013-3.

## 3. Four-object separation

PASS.

The chapter keeps distinct:

1. execution depth;
2. numerical step size;
3. local error estimate;
4. learned halting/compute score.

This separation is preserved in the specification, derivation, witness, and reader manuscript.

No implication among these objects is asserted without additional structure.

## 4. Embedded-pair semantics

PASS.

The chapter defines paired approximations

\[
x_{n+1}^{[p]},
\qquad
x_{n+1}^{[p+1]}
\]

and estimator

\[
\widehat e_n
=
\left\|
x_{n+1}^{[p+1]}
-
x_{n+1}^{[p]}
\right\|.
\]

It correctly treats the difference as a method-specific local error estimator under declared order/smoothness assumptions rather than as a universal exact error oracle.

## 5. Exact Euler/Heun witness

PASS.

For

\[
y'(t)=t,
\qquad
y(0)=0,
\]

the exact solution is

\[
y(t)=t^2/2.
\]

Euler from t=0 over step h gives

\[
y_E=0.
\]

Heun gives

\[
y_H=h^2/2.
\]

The exact endpoint is also

\[
y(h)=h^2/2.
\]

Therefore

\[
|y_H-y_E|
=
h^2/2
\]

equals the exact Euler one-step error in this declared witness.

The chapter explicitly marks this exact equality as witness-specific.

## 6. Exact accept/reject arithmetic

PASS.

With tolerance

\[
\tau=1/8,
\]

at

\[
h=1
\]

the estimator is

\[
\widehat e=1/2,
\]

so the step is rejected.

For low-order p=1, the idealized controller

\[
h_{\mathrm{new}}
=
h(\tau/\widehat e)^{1/2}
\]

gives

\[
h_{\mathrm{new}}
=
\sqrt{(1/8)/(1/2)}
=
1/2.
\]

At

\[
h=1/2,
\]

the estimator is

\[
(1/2)^2/2
=
1/8.
\]

Thus the retry meets the non-strict tolerance exactly.

## 7. Step-controller claim boundary

PASS.

The controller is explicitly described as idealized.

The manuscript states that production controllers may add safety factors and growth/shrinkage clamps.

No universal optimality claim is made.

## 8. Local versus global error

PASS.

The chapter explicitly records that local acceptance does not algebraically imply a global error bound.

It names the missing ingredients:

- error accumulation;
- stability/amplification;
- mesh sequence;
- problem regularity;
- method order/consistency.

This preserves the audited NETNUM boundary.

## 9. Learned halting semantics

PASS.

The bounded stopping rule

\[
\tau
=
\min
\left(
\{k\le K_{\max}:q_k\le\delta\}
\cup
\{K_{\max}\}
\right)
\]

is used only to define stopping.

The chapter does not assign error semantics to q merely because it is learned or thresholded.

It preserves criterion_met versus budget_exhausted from AUDIT-018.

## 10. Exact monotone-but-miscalibrated score witness

PASS.

The recurrence

\[
x_{k+1}=(x_k+2)/2,
\qquad
x_0=0
\]

has exact fixed-point error

\[
E_k=2^{1-k}.
\]

Define

\[
q_k=4^{-k}.
\]

Then

\[
E_k^2
=
2^{2-2k}
=
4\cdot4^{-k},
\]

so

\[
q_k=E_k^2/4.
\]

Thus q is a strictly monotone function of E and ranks depth perfectly.

At k=2,

\[
q_2=1/16,
\qquad
E_2=1/2.
\]

Using the same numerical threshold 1/16 for score and target error therefore stops eight times outside the requested error tolerance.

This is a valid counterexample to the implication:

\[
\text{perfect ranking}
\Rightarrow
\text{magnitude-calibrated error control}.
\]

## 11. Exact score-to-error threshold map

PASS.

From

\[
q_k=E_k^2/4,
\]

the exact inverse relation is

\[
E_k=2\sqrt{q_k}.
\]

Therefore target error

\[
E_k\le\varepsilon
\]

is equivalent in this witness to

\[
q_k\le(\varepsilon/2)^2.
\]

For

\[
\varepsilon=1/16,
\]

the score threshold is

\[
1/1024.
\]

At k=5,

\[
q_5=1/1024
\]

and

\[
E_5=1/16.
\]

The arithmetic is exact.

## 12. Calibration versus certification

PASS.

The chapter distinguishes a conditional-mean relation such as

\[
E[E_k\mid q_k=s]=g(s)
\]

from a per-instance bound

\[
E_k\le g(s).
\]

It correctly states that expected calibration does not supply deterministic per-instance certification.

No stronger probabilistic guarantee is inferred without being separately declared.

## 13. Adaptive depth versus adaptive step size

PASS.

Variable stage count is written as

\[
z_{k+1}=F_k(z_k),
\qquad
k<\tau(x).
\]

Adaptive numerical stepping is written as

\[
x_{n+1}=\Psi_{h_n}(x_n)
\]

for a declared reference evolution with error-controlled h_n.

The chapter does not identify these objects.

It correctly requires a fixed reference problem, discretization, and step-scale semantics before treating network depth as a numerical mesh.

## 14. Fixed-horizon boundary

PASS.

For a declared time horizon T, the chapter records

\[
\sum_n h_n=T
\]

up to the end-step convention.

It correctly notes that increasing stage count with unchanged step sizes generally changes represented horizon rather than refining a fixed horizon.

Thus:

\[
\text{more layers}
\not\Rightarrow
\text{smaller numerical step}
\]

without additional structure.

## 15. Spatial adaptive computation boundary

PASS.

Figurnov et al. are used only to establish learned nonuniform compute allocation.

The chapter explicitly blocks:

\[
\text{spatially variable neural depth}
\Rightarrow
\text{adaptive PDE mesh refinement}.
\]

The missing PDE, discretization, estimator, and interface structure is stated.

## 16. Residual/error-indicator boundary

PASS.

The chapter notes that residual-like quantities may be useful stopping signals while correctly refusing the general implication

\[
\text{small residual}
\Rightarrow
\text{small target error}.
\]

The need for conditioning/operator-specific relations is preserved.

## 17. Fixed-point stopping boundary

PASS.

For equilibrium computation, the manuscript distinguishes fixed-point residual

\[
\|F(z_k)-z_k\|
\]

from state error

\[
\|z_k-z^*\|.
\]

It states that converting one to the other requires additional structure such as contraction-type assumptions.

This is consistent with AUDIT-018.

## 18. Budget semantics

PASS.

If no candidate meets tolerance before K_max, termination is recorded as budget_exhausted.

Budget exhaustion is not labeled convergence or criterion satisfaction.

## 19. Error control versus compute optimality

PASS.

The chapter separately treats:

- accuracy/error constraint;
- FLOPs;
- latency;
- energy;
- memory traffic;
- resource optimization.

It does not infer resource optimality from tolerance satisfaction.

## 20. Learned-error-estimator research bridge

PASS.

The manuscript permits a learned module to estimate a declared error but keeps visible the required questions:

- target;
- norm;
- distribution;
- calibration;
- tail/high-probability behavior;
- out-of-distribution behavior;
- rejection action.

No learned estimator is certified merely by naming it an error predictor.

## 21. Citation and bibliography integrity

PASS.

Reader-facing citations resolve for:

- Graves2016ACT;
- FigurnovEtAl2017;
- DormandPrince1980.

The two new bibliography entries are bounded to the ADAPTDEPTH source lock; FigurnovEtAl2017 was already registered.

## 22. Repository integrity

PASS subject to audit-PR validation.

At the implementation merge:

- Chapter Ledger: 487fb507262ca9520d37e42397c3dc52f375ac6b
- Source Register: 4b5b06e0c702eaa79eb7a0771b15ab10a860762b
- bibliography: 7a7a89bc7c3789e0865755e446ee41d7d95815f2
- chapter status: draft-v0.1
- hard dependencies unchanged
- no governed figure introduced

Implementation exact head 43ec942015e5e6ce0f7e50875500117f880e2c48 passed:

- canonical Linux validation;
- GitHub Actions validation.

## Final disposition

AUDIT-055 passes with no repair.

The durable ADAPTDEPTH layer is:

**adaptive computation + declared target error + estimator/error relation + tolerance + accept/stop controller + explicit budget/failure state, with learned halting and numerical error control kept distinct unless a relation is actually established.**
