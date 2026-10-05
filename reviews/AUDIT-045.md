# AUDIT-045 — Optimization on Manifolds

## Disposition

**PASS — NO MATHEMATICAL REPAIR REQUIRED**

ATLAS-CH-MANOPT-001 remains at \`draft-v0.1\`.

The chapter's tangent-space formulas, induced-metric gradient projections, normalized sphere retraction, Stiefel tangent condition, polar retraction, finite sphere/orthogonality witnesses, retraction-versus-exponential boundary, stationarity/optimality boundary, source scope, and downstream VARIOPT separation pass audit.

No mathematical, source-scope, prose, witness, or dependency repair was required.

## Audited implementation

- implementation issue: #180
- implementation PR: #181
- implementation merge: \`b47e9d42557428bb2c985b2ba916bbcdf6489a8f\`
- audit issue: #182
- audit branch: \`audit/manopt-182\`

Implementation artifact identities:

- canonical source lock: \`e98e655839f521250d25350c33006c9eed60e23c\`
- byte-identical register alias: \`e98e655839f521250d25350c33006c9eed60e23c\`
- specification: \`2da08cd5682390fee676e237ae9f9116bb8ee4bf\`
- derivation packet: \`021593fb425ec917de930418e4ef6de14599c8e8\`
- computational witness: \`704585afd3ca2192eb421d4372ee91979a3f5242\`
- manuscript: \`62ded6bc72c980feb96dff2c77c122141171f64f\`
- Chapter Ledger: \`06b3fa814d5b7610a4edb12f0ad5fb897dee7b7f\`
- Source Register: \`5438094c3abd185009816ded02ef966060494d13\`
- transaction receipt: \`b6c3e387c9ee1ab25849b44fb1e12b0ddb2b12b6\`

## 1. Hard prerequisites

PASS.

### Geometry

Exact binds:

- manuscript: \`f8e406f24a01bd852996e11118e04427ff549f35\`
- source lock: \`d75e8bcf5a5920eca6b09cb8bb181182c7827b5c\`
- AUDIT-001: \`f13b7ac01f7b10dfadd64da6f31c45832344c082\`

The consumed geometry includes sphere and Stiefel tangent spaces, retractions, exponential-map language, and constrained-state distinctions.

### First-Order Optimization

Exact binds:

- manuscript: \`42df47c50c2d6d26da65a58b230040e2663f901f\`
- source lock: \`fa610d3d763cc1a7e76ee4b83e85ce2c965c2825\`
- AUDIT-012: \`28929ba6b4a16a3cef4a871fd9253d76e8a93634\`

The consumed optimization substrate explicitly scopes Euclidean steepest descent to the Euclidean metric, making the downstream manifold generalization appropriate.

## 2. External source identity and scope

PASS.

The chapter uses:

- Absil, Mahony, Sepulchre, \`Optimization Algorithms on Matrix Manifolds\` (2008), as the standard matrix-manifold optimization source;
- Edelman, Arias, Smith, \`The Geometry of Algorithms with Orthogonality Constraints\`, SIAM Journal on Matrix Analysis and Applications 20(2):303-353 (1998), DOI \`10.1137/S0895479895290954\`.

The latter source was independently rechecked against the SIAM record.

The sources support standard tangent/retraction/orthogonality-constrained geometry. They are not used to claim universal superiority of manifold optimization.

## 3. Sphere tangent geometry

PASS.

For

\[
S^{n-1}
=
\{x:x^\top x=1\},
\]

differentiation gives

\[
T_xS^{n-1}
=
\{\xi:x^\top\xi=0\}.
\]

For the induced Euclidean metric,

\[
\Pi_x(g)
=
g-(x^\top g)x.
\]

The manuscript correctly scopes this projection identity to the induced metric setting.

## 4. Exact sphere witness

PASS.

For

\[
x=(1,0)^\top,
\qquad
a=(1,2)^\top,
\]

the tangent gradient is

\[
(0,2)^\top.
\]

With \(\eta=1/2\),

\[
\xi=(0,-1)^\top.
\]

Independent exact replay gives:

- ambient Euclidean-step squared norm: \(5/4\);
- raw tangent-step squared norm: \(2\);
- normalized-retraction squared norm: \(1\).

Thus the witness correctly separates ambient descent, tangent direction, and finite feasibility.

## 5. Sphere retraction versus exponential map

PASS.

The normalized retraction endpoint is

\[
(1,-1)^\top/\sqrt2.
\]

The exponential endpoint is

\[
(\cos1,-\sin1)^\top.
\]

Both are on the unit circle and are distinct.

The chapter therefore correctly states that a valid retraction need not equal the exponential map.

## 6. Stiefel tangent condition

PASS.

For

\[
\operatorname{St}(n,p)
=
\{X:X^\top X=I\},
\]

differentiation gives

\[
X^\top Z+Z^\top X=0.
\]

The embedded-metric projection

\[
\Pi_X(G)
=
G-X\operatorname{sym}(X^\top G)
\]

is checked to satisfy the tangent condition.

## 7. Polar retraction

PASS.

For tangent \(\Xi\),

\[
R_X(\Xi)
=
(X+\Xi)
(I+\Xi^\top\Xi)^{-1/2}.
\]

Using

\[
X^\top\Xi+\Xi^\top X=0,
\]

the chapter derives

\[
(X+\Xi)^\top(X+\Xi)
=
I+\Xi^\top\Xi
\]

and therefore

\[
R_X(\Xi)^\top R_X(\Xi)=I.
\]

The derivation is exact.

## 8. Exact orthogonality witness

PASS.

For

\[
X=I_2,
\qquad
\Xi=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix},
\]

independent exact replay gives:

- tangent residual: \(0\);
- raw-step Gram: \(2I\);
- polar-retracted Gram: \(I\).

The polar endpoint is rotation by \(\pi/4\).

The exponential endpoint is rotation by \(1\) radian.

Both are orthogonal and distinct.

## 9. Retraction and vector-transport boundary

PASS.

The chapter distinguishes:

- retraction: moving a point from tangent data back to the manifold;
- vector transport: moving tangent information between tangent spaces.

Momentum-like tangent state is therefore not silently reused across changing tangent spaces.

## 10. Constraint preservation and optimality

PASS.

The chapter explicitly denies the implications:

- constraint preservation \(\Rightarrow\) descent;
- descent \(\Rightarrow\) convergence;
- manifold stationarity \(\Rightarrow\) global optimality;
- orthogonality preservation \(\Rightarrow\) optimizer quality.

These boundaries are appropriate.

## 11. Generic versus GCL-specific optimization

PASS.

The chapter does not promote its generic manifold substrate into a theorem about:

- nGPT;
- Muon;
- rectangular spectral updates;
- MODULUS;
- another named GCL optimizer.

Those programmes require separate objectives, metrics, update rules, and evidence.

## 12. Downstream VARIOPT boundary

PASS.

ATLAS-CH-VARIOPT-001 may inherit tangent-gradient, retraction, metric, and constrained-motion language.

It must independently establish any divergence-derived, variational, symplectic, or duality-based motion rule.

## 13. Repository integrity

Implementation head \`64a57189692ca0c7e68e245117840db51dd48a63\` passed canonical validation before merge.

All chapter artifacts were byte-scanned before implementation merge.

The neutral source-lock alias is byte-identical to the canonical source lock and exists only to recover from a connector filter on Source Register text.

## Final disposition

AUDIT-045 passes with no substantive repair required.

The durable substrate is:

**metric-dependent tangent gradients + exact sphere/Stiefel constraint geometry + practical retractions + explicit separation of feasibility, geodesic exactness, stationarity, and global optimality.**
