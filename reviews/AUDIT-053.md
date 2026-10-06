# AUDIT-053 — Representation as Transport

## Disposition

**PASS AFTER ONE DOCUMENTARY REPAIR**

ATLAS-CH-TRANSPORT-001 remains at draft-v0.1.

The mathematical and epistemic substrate passes. The audit found one documentary defect: Markdown backticks in the specification, reader manuscript, and computational witness had been escaped during raw-string generation, causing code/path markers and the witness code fence to render literally. Those delimiters were repaired without changing mathematical content.

No publication, theorem certification, or release promotion is implied.

## Audited baseline

- implementation merge: 9d6d5bd100663b8c2587a32c16be190e6b5aac85
- implementation PR: #212
- implementation issue: #211
- audit issue: #213
- chapter: ATLAS-CH-TRANSPORT-001

Implementation artifact blobs before audit repair:

- specification: 3498ea034cef08ff659cd5bf6a93059d66e12464
- derivation packet: 26ba43d43d911c4c689ce60d01443e84d48bea01
- computational witness: 09759b3d0d324507f1478c06cd04ff6078b37380
- manuscript: 2346ec5fcde35e899db31fc91e5ef34a3e1b24e5
- source lock: 55fcd80bc3d94e3b270ddcf28873242ba21f823f
- Chapter Ledger: f8b94379c507776e031dced47a7fc602f95ab5b7
- Source Register: eeaceee0b1a70b972987d66d68b1dd4bc63b12e0

Repaired audit-head artifacts before this audit record:

- specification: 3f8e5542f2b55b63f5296f8bcc916d5086628b6f
- derivation packet: 26ba43d43d911c4c689ce60d01443e84d48bea01
- computational witness: da81a51881e0f159d2d1194e990ebe9ea7e972ec
- manuscript: 0a81b39a457384f7a265bbac2955ea282217bc3f
- source lock: 55fcd80bc3d94e3b270ddcf28873242ba21f823f

## 1. Hard prerequisite identity

PASS.

The source lock binds exactly to the protected baseline db2b19c4730a938babe9a2734eb40f898ee9913e.

Normalized and Hyperspherical Representations:

- manuscript: 1500987b384fb931bbd01879756c08b42ebcff28
- source lock: 58b8331e56f5c9859e72be5c58f283706b5c436e
- AUDIT-005: 11f45d9edf309cf55d9c4b0582ca88cd25c02c4d

Split-Operator Networks:

- manuscript: bcaf1db6b1fc7144e2472ff2725f7ff561fe7fc0
- source lock: afb84e2f3ebb941f320c52693b088b0eb078b8ce
- AUDIT-036: 5e093460550c15fe491ba3214b2f52d48076dc0a

No downstream Neural Krylov chapter is used as hidden prerequisite authority.

## 2. External source scope

PASS.

The source lock uses:

- Lee for manifold, tangent-space, geodesic, and differential-geometric background;
- Absil–Mahony–Sepulchre for retractions and vector transport;
- He et al. for residual identity-plus-increment architecture;
- Chen et al. for explicit Neural ODE continuous-depth evolution;
- Haber–Ruthotto for dynamical-systems and discrete-ODE architecture motivation.

The chapter does not convert paper-scoped architectural or empirical results into universal transport theorems.

Representation transport is explicitly identified as Atlas synthesis.

## 3. Primary transport object

PASS.

The chapter defines finite representation transport by

\[
z_{k+1}=\Phi_k(z_k)
\]

and

\[
z_K=(\Phi_{K-1}\circ\cdots\circ\Phi_0)(z_0).
\]

This is exact as a finite composition.

The chapter does not infer an ODE, manifold, metric, probability measure, invertibility, or infinitesimal semantics from this composition alone.

## 4. Residual versus exact-flow boundary

PASS.

The residual stage

\[
\Phi_k(z)=z+F_k(z)
\]

is treated as an exact discrete-map statement.

The scaled form

\[
\Phi_{k,h}(z)=z+hF_k(z)
\]

is allowed to resemble an Euler update only when a declared ODE reference exists.

The chapter explicitly blocks

\[
\text{residual stack}\Rightarrow\text{unique exact ODE}.
\]

Neural ODEs are treated separately as architectures that explicitly declare

\[
\dot z=f(z,t;\theta).
\]

## 5. Retraction versus exponential-map witness

PASS.

For

\[
u=(1,0),
\qquad
\xi=(0,1),
\]

the normalized retraction gives

\[
R_u(\xi)=\frac{(1,1)}{\sqrt2}.
\]

Its angular displacement is \(\pi/4\).

The standard sphere exponential endpoint for the unit tangent at unit time is

\[
(\cos1,\sin1),
\]

with angular displacement \(1\).

Since

\[
\pi/4\neq1,
\]

the endpoints differ.

The chapter therefore correctly distinguishes manifold feasibility from geodesic exactness.

## 6. Base-point ownership of tangent data

PASS.

At

\[
u_0=(1,0),
\qquad
v_0=(0,1),
\]

we have

\[
u_0^\top v_0=0.
\]

After moving the state to

\[
u_1=(1,1)/\sqrt2,
\]

independent replay gives

\[
u_1^\top v_0=1/\sqrt2.
\]

Thus the old ambient vector is not tangent at the new base point.

The projected tangent vector is

\[
P_{u_1}v_0=(-1/2,1/2),
\]

and independent algebra verifies

\[
u_1^\top P_{u_1}v_0=0.
\]

The chapter does not call this projection parallel transport.

## 7. State transport versus vector and parallel transport

PASS.

The chapter keeps separate:

- moving the representation point;
- moving tangent information between tangent spaces;
- parallel transport under a connection;
- ambient Jacobian propagation.

It correctly states that a state update does not automatically provide a vector-transport or parallel-transport rule.

## 8. Exact order-sensitive constrained witness

PASS.

On the sphere, start from

\[
u_0=(1,0,0)
\]

with

\[
a=(0,1,0),
\qquad
b=(0,0,1).
\]

Independent symbolic replay gives:

\[
u_{ab}
=
(1/2,1/2,1/\sqrt2),
\]

\[
u_{ba}
=
(1/2,1/\sqrt2,1/2).
\]

Both satisfy unit norm.

They are unequal.

The exact inner product is

\[
u_{ab}^\top u_{ba}
=
1/4+1/\sqrt2.
\]

The chapter correctly treats this as a finite counterexample to order independence, not as a universal noncommutation theorem for all constrained neural updates.

## 9. Constraint versus information preservation

PASS.

The chapter uses

\[
N(x)=x/\|x\|
\]

and

\[
N(cx)=N(x),\qquad c>0,
\]

to show non-injectivity along positive rays.

It therefore correctly states that a constraint-preserving trajectory can erase radial information.

No claim is made that normalization is universally harmful or beneficial.

## 10. Autonomous versus stage-dependent transport

PASS.

The chapter distinguishes repeated shared transport

\[
\Phi_k=\Phi
\]

from stage-dependent maps

\[
\Phi_k.
\]

A continuous analogy for the latter is described as naturally nonautonomous unless stronger structure is proved.

The chapter does not collapse layer-varying learned maps into one autonomous generator.

## 11. Differential pushforward boundary

PASS.

For differentiable maps, the chapter uses local Jacobian propagation only as a local differential object.

It explicitly distinguishes:

- the nonlinear state map;
- its ambient Jacobian;
- intrinsic tangent-space maps;
- vector transport;
- global flow semantics.

No hidden equivalence is asserted.

## 12. Optimal-transport boundary

PASS.

The chapter does not formulate a probability-measure transport problem.

It explicitly notes that representation state evolution by itself supplies no source/target probability measures, coupling, transport cost, or optimality problem.

Thus the phrase "representation transport" is not silently promoted to optimal transport.

No positive optimal-transport theorem is claimed.

## 13. Stability and invertibility boundaries

PASS.

The chapter states that constraint-preserving transport does not imply:

- perturbation stability;
- invertibility;
- reversibility;
- information preservation;
- task quality.

Jacobian-product sensitivity is presented as a separate analysis question.

## 14. Neural Krylov handoff

PASS.

The downstream chapter may inherit:

- declared transport maps;
- state/base-point semantics;
- constrained retraction witnesses;
- local linearization objects;
- shared versus stage-dependent transport semantics.

It may not inherit:

- a Krylov subspace theorem;
- convergence;
- residual minimization;
- preconditioning effectiveness;
- finite-precision guarantees.

The hard boundary is preserved:

\[
\text{representation transport}
\not\Rightarrow
\text{Krylov convergence guarantee}.
\]

## 15. Documentary repair

PASS AFTER REPAIR.

The implementation artifacts were generated with escaped Markdown backticks in three files:

- chapter specification;
- reader manuscript;
- computational witness.

This caused path/code markers and the witness code fence to render literally.

The audit branch replaced only those delimiter escapes.

No equations, prose claims, citations, source identities, ledger state, or witness values changed.

Repaired blobs are:

- specification: 3f8e5542f2b55b63f5296f8bcc916d5086628b6f
- manuscript: 0a81b39a457384f7a265bbac2955ea282217bc3f
- computational witness: da81a51881e0f159d2d1194e990ebe9ea7e972ec

## 16. Repository integrity

PASS subject to audit-PR validation.

At the repaired pre-audit-record head:

- Chapter Ledger: f8b94379c507776e031dced47a7fc602f95ab5b7
- Source Register: eeaceee0b1a70b972987d66d68b1dd4bc63b12e0
- chapter status: draft-v0.1
- hard dependencies unchanged
- no governed figure introduced
- bibliography unchanged
- source register contains one TRANSPORT source-lock entry

Canonical Linux validation on repaired head 456447d14fcae36a64af1a1f808b1432d28119f6 reported:

OK: 80 chapters, 126 hard edges, 1 root(s), 0 specification-ready keystones, 61 draft chapters, 18 rendered witnesses, 18 registered figures, 66 sources, 149 bibliography keys

## Final disposition

AUDIT-053 passes after one documentary repair.

The durable TRANSPORT layer is:

**declared representation state + declared ordered stage maps + explicit constraint/retraction semantics + base-point ownership of tangent data + exact separation of state transport, vector/parallel transport, optimal transport, and continuous-flow claims.**
