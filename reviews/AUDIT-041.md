# AUDIT-041 — Curvature and Second-Order Structure

## Disposition

**PASS AFTER ONE SOURCE-METADATA REPAIR**

ATLAS-CH-SECOND-001 remains at \`draft-v0.1\`.

No mathematical, derivational, witness, or prose reversal was required.

The audit found one bibliographic precision defect: the Parikh–Boyd proximal reference omitted its canonical DOI in the bibliography and source lock. AUDIT-041 added DOI \`10.1561/2400000003\` and restored the publisher locator.

## Audited implementation

- implementation issue: #163
- implementation PR: #164
- implementation merge: \`62e341cc87130dc1b937da4f126bdc0b9eb9d17a\`
- audit issue: #165
- audit branch: \`audit/second-165\`
- chapter: \`ATLAS-CH-SECOND-001\`

Implementation artifact identities:

- specification: \`54bcb079b766d418872317c7fbe4626dfb689377\`
- derivation packet: \`0ea81f098b8e175df56b9a949d4b9b2ef10d720f\`
- computational witness: \`832d410baf651404f385ddf85b57a69e95bb9d8c\`
- manuscript: \`10ee7db734df519e886e335301bf107d01d27f5c\`
- source lock before audit: \`d5344d426251de99d9dc6945c60ff919b7d27b2d\`
- bibliography before audit: \`6061a614f2310e06acbe853b1a6fa6c09af282a2\`
- Chapter Ledger: \`3aeb44b8726725d5db3607a0af691149915b1918\`
- Source Register: \`ae8cb2e572be64c2b5992fd2e22b5c000361e658\`
- tranche receipt: \`cc07b7320d7f9ab6b32a661cbaff213c05cc2e18\`

Repaired audit-head identities:

- source lock: \`bc74588fd65df1a88a524b5241ca08ff498e0231\`
- bibliography: \`0589936407cc287ea0e4835e908f07bca4771886\`

## 1. Hard prerequisites

PASS.

### First-Order Optimization

Exact protected binds:

- manuscript: \`42df47c50c2d6d26da65a58b230040e2663f901f\`
- source lock: \`fa610d3d763cc1a7e76ee4b83e85ce2c965c2825\`
- AUDIT-012: \`28929ba6b4a16a3cef4a871fd9253d76e8a93634\`

The inherited interface is correctly limited to first-order gradient/update semantics, optimizer-state discipline, and quadratic stability language.

### Geometry

Exact protected binds:

- manuscript: \`f8e406f24a01bd852996e11118e04427ff549f35\`
- source lock: \`d75e8bcf5a5920eca6b09cb8bb181182c7827b5c\`
- AUDIT-001: \`f13b7ac01f7b10dfadd64da6f31c45832344c082\`

The inherited interface is correctly limited to metric and geometric language.

## 2. External source identity

PASS AFTER ONE REPAIR.

### Nocedal and Wright

\`Numerical Optimization\`, second edition, Springer, 2006, DOI \`10.1007/978-0-387-40065-5\`.

This is correctly used for Newton, quasi-Newton, trust-region, and large-scale smooth optimization structure.

### Amari

\`Natural Gradient Works Efficiently in Learning\`, Neural Computation 10(2), 251–276, 1998, DOI \`10.1162/089976698300017746\`.

This is correctly used for natural gradient under information geometry and Fisher-metric language in the paper's setting.

### Pearlmutter

\`Fast Exact Multiplication by the Hessian\`, Neural Computation 6(1), 147–160, 1994, DOI \`10.1162/neco.1994.6.1.147\`.

This is correctly used for exact Hessian-vector multiplication without explicit dense Hessian formation in the cited setting.

### Parikh and Boyd

\`Proximal Algorithms\`, Foundations and Trends in Optimization 1(3), 127–239, 2014.

Canonical DOI:

\`10.1561/2400000003\`.

The implementation omitted that DOI.

**Repair:** add the canonical DOI to both the bibliography and source lock and use the publisher locator.

No claim-scope change was required.

## 3. Quadratic model

PASS.

The chapter uses

\[
m_x(p)
=
f(x)+g^\top p+\frac12p^\top Hp.
\]

The Newton stationarity equation

\[
Hp=-g
\]

is exact for the declared local quadratic model.

## 4. Positive-definite Newton descent

PASS.

For \(H\succ0\),

\[
p_N=-H^{-1}g.
\]

Then

\[
g^\top p_N
=
-g^\top H^{-1}g
<
0
\]

for nonzero \(g\).

The manuscript explicitly scopes this implication to positive-definite curvature.

## 5. Exact SPD witness

PASS.

For

\[
H=\operatorname{diag}(1,4),
\qquad
b=(1,1)^\top,
\qquad
x_0=0,
\]

the gradient is

\[
g_0=(-1,-1)^\top.
\]

The exact Newton step is

\[
p_N=(1,1/4)^\top.
\]

Independent replay confirms:

\[
Hp_N=b,
\]

\[
\nabla f(p_N)=0,
\]

\[
f(p_N)=-5/8,
\]

and

\[
g_0^\top p_N=-5/4<0.
\]

## 6. Indefinite Newton control

PASS.

For

\[
f(x,y)=\frac12(x^2-y^2)
\]

at

\[
(0,1)^\top,
\]

the gradient and Hessian are

\[
g=(0,-1)^\top,
\qquad
H=\operatorname{diag}(1,-1).
\]

The raw Newton step is

\[
p_N=(0,-1)^\top.
\]

Then

\[
g^\top p_N=1>0.
\]

The full Newton step reaches \((0,0)\), where the objective is \(0\), compared with the starting value \(-1/2\).

Thus the witness correctly demonstrates that an invertible indefinite Hessian does not guarantee a descent Newton direction.

## 7. Trust-region control

PASS.

At the same point with radius \(\Delta=1\), the model increment is

\[
q(p)
=
-p_2+\frac12p_1^2-\frac12p_2^2.
\]

Over the unit disk, independent replay confirms the minimizer

\[
p_{\rm TR}=(0,1)^\top.
\]

The model change is

\[
q(p_{\rm TR})=-3/2.
\]

The new point is \((0,2)\), where

\[
f(0,2)=-2.
\]

The chapter correctly uses this only as a finite control showing why globalization/negative-curvature logic differs from raw Newton stationarity.

## 8. Damped Newton boundary

PASS.

The chapter distinguishes

\[
(H+\lambda I)p=-g
\]

from the exact Newton system.

It does not call a shifted Hessian the original exact Hessian.

## 9. Hessian-vector products

PASS.

The directional derivative identity

\[
Hv
=
\frac{d}{d\varepsilon}
\nabla f(x+\varepsilon v)
\Big|_{\varepsilon=0}
\]

is correct.

The chapter uses Pearlmutter only for exact matrix-free curvature action in the cited setting and does not claim that second-order computation becomes free.

## 10. Fisher information versus Hessian

PASS.

The chapter explicitly states that these are different constructions.

It does not use a generic identity

\[
F=H.
\]

Any setting where the objects coincide would require separate assumptions.

## 11. Natural gradient

PASS.

For a positive-definite metric \(G\), the chapter uses metric steepest descent proportional to

\[
-G^{-1}g.
\]

With Fisher information as the metric this becomes the natural gradient.

The chapter does not identify natural gradient with Newton in general.

## 12. Exact metric witness

PASS.

For

\[
G=\operatorname{diag}(1,4),
\qquad
g=(1,1)^\top,
\]

the Euclidean direction is

\[
(-1,-1)^\top,
\]

while the metric direction is

\[
(-1,-1/4)^\top.
\]

The witness correctly isolates metric dependence.

## 13. Quasi-Newton secant structure

PASS.

The secant relation

\[
B_{k+1}s_k=y_k
\]

is used as partial curvature information.

For the exact quadratic witness,

\[
s=(1,2)^\top,
\qquad
y=Hs=(1,8)^\top.
\]

The text correctly states that one secant equation does not uniquely determine the full exact Hessian.

## 14. BFGS positivity scope

PASS.

The manuscript states the standard curvature-condition boundary:

if the previous Hessian approximation is positive definite and

\[
y_k^\top s_k>0,
\]

the standard BFGS Hessian update preserves positive definiteness.

It is not promoted into an assumption-free global convergence theorem.

## 15. Proximal operator

PASS.

The chapter defines

\[
\operatorname{prox}_{\alpha h}(v)
=
\arg\min_x
\left[
h(x)+\frac{1}{2\alpha}\|x-v\|^2
\right].
\]

For

\[
h(x)=\lambda|x|,
\qquad
\alpha\lambda=1,
\]

the soft-threshold witness gives

\[
3\mapsto2,
\qquad
-3\mapsto-2,
\qquad
1/2\mapsto0.
\]

The chapter correctly separates this implicit nonsmooth subproblem from gradient clipping and from Hessian approximation.

## 16. Local versus global boundary

PASS.

The chapter repeatedly distinguishes local second-order structure from:

- global convexity;
- global optimality;
- universal convergence;
- empirical optimizer superiority.

No local Hessian fact is promoted into a global landscape theorem.

## 17. Downstream MATRIXOPT handoff

PASS.

MATRIXOPT may inherit:

- Hessian/curvature notation;
- positive/indefinite distinctions;
- matrix-free curvature action;
- metric/preconditioning language;
- exact-versus-approximate curvature discipline.

It must independently justify:

- Shampoo;
- polar-factor updates;
- orthogonalized matrix steps;
- Muon-like methods;
- rectangular-matrix geometry.

No downstream theorem is smuggled upstream.

## 18. Repository integrity

PASS subject to audit-PR validation.

The implementation passed canonical validation at exact head \`c1f888569f12855e5ba416d1d1b3783b2a9db365\`.

The canonical manuscript contains:

- epistemic-status marker;
- References section;
- exact source-lock path.

The witness contains a Claim boundary.

The ledger paths exist.

The source register includes the source lock.

No governed figure is required.

## Final disposition

AUDIT-041 passes after one bibliographic/source-lock precision repair.

The durable layer is:

**Hessian curvature + exact Newton/indefinite controls + trust-region globalization + Fisher/natural-gradient separation + matrix-free curvature action + quasi-Newton secant approximation + proximal nonsmooth structure, without promoting local second-order information into global guarantees.**
