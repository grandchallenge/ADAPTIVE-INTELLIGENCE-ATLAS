# AUDIT-064 — Neural Krylov Transport

## Disposition

**PASS — NO REPAIR**

ATLAS-CH-NEURALKRYLOV-001 remains at draft-v0.1.

The audit found no mathematical, dependency, source-scope, provenance, witness, protocol, or repository defect requiring repair.

## Audited implementation

- implementation issue: #255
- implementation PR: #256
- exact validated implementation head: ba58e1e990c818e5c45a8007e7a0314fa4cd9d47
- implementation GitHub Actions run: 37547958975
- implementation merge / audited protected baseline: 0efe3dc8bfd47f268cd2a5f088026e95b3a6c52e
- audit issue: #257
- audit branch: audit/a257
- chapter: ATLAS-CH-NEURALKRYLOV-001

Protected implementation artifact identities:

- specification: 6ac203b25f1155b3eaed4b063af8fa559b69ce2d
- derivation packet: afe1798ce77b74b79478d79553bd72323da8545b
- computational witness: 02e383c1ff0237199be5ac757c4aebdd4cb8e011
- reader manuscript: d2740a2d47c004dc48a0dc97ae0ebbb43d60707b
- source lock: f030acac3c8269ab6c3a4856c1ec53cc75cedee9
- Chapter Ledger: 2149fa3ae83e57fd46391e6b36a0af3931da5af0
- Source Register: 536349056012148899077b9d0d1f0badd18dd684
- transaction receipt: 0c94c9a90987f79960d6b3d89c3ad2316b3de75a

## 1. Hard prerequisites

PASS.

KRYLOV-001 is bound exactly:

- manuscript 59e169723ca068bef817e7bc9e28727d03b45f6a;
- source lock adbe97c750ed79d09462a5e867e5beb772ad72e2;
- AUDIT-039 03660b0dbd1d0604e943d0d09c7b52c6605b256c.

TRANSPORT-001 is bound exactly:

- manuscript 0a81b39a457384f7a265bbac2955ea282217bc3f;
- source lock 55fcd80bc3d94e3b270ddcf28873242ba21f823f;
- AUDIT-053 060d0b9dc320cd16fdcfe10b87484a3bbfda4c75.

No downstream chapter is used as hidden authority.

## 2. Source decision

PASS.

No new external academic source is added.

Classical Krylov/preconditioning authority remains governed by KRYLOV-001. Representation-map/local-Jacobian semantics remain governed by TRANSPORT-001. The new positive and failure witnesses are exact finite Atlas-owned linear algebra.

No learned nonlinear convergence theorem is imported by analogy.

## 3. Declared operator interface

PASS.

The chapter requires every Krylov construction to name the linear operator, starting vector/right-hand side, and preconditioner semantics.

A local Jacobian-derived or learned surrogate operator is kept distinct from the global nonlinear representation map.

## 4. Fixed left preconditioning

PASS.

The positive witness uses:

[
A=operatorname{diag}(1,4),qquad b=(1,1)^	op,
]

with fixed left preconditioner:

[
M=operatorname{diag}(1,2).
]

Therefore:

[
B=M^{-1}A=operatorname{diag}(1,2),
qquad
c=M^{-1}b=(1,1/2)^	op.
]

The exact solution remains:

[
x^star=(1,1/4)^	op.
]

## 5. One-dimensional Krylov minimizer

PASS.

For:

[
mathcal K_1(B,c)=operatorname{span}{c},
]

the transformed-residual minimizing scalar is exactly:

[
oxed{alpha=3/4}.
]

Thus:

[
x_1=(3/4,3/8)^	op.
]

Independent exact replay agrees.

## 6. Residual/error separation

PASS.

At (x_1):

- transformed residual squared: (1/8);
- original-system residual squared: (5/16);
- true solution error squared: (5/64).

The chapter correctly treats these as different metrics and states:

[
widehat r=M^{-1}r.
]

It does not identify residual norm with true error.

## 7. Two-dimensional exactness

PASS.

The vectors:

[
c=(1,1/2)^	op,
qquad
Bc=(1,1)^	op
]

have determinant:

[
1/2
eq0.
]

Hence:

[
mathcal K_2(B,c)=mathbb R^2.
]

The exact solution satisfies:

[
x^star=(3/2)c-(1/2)Bc.
]

Therefore an exact residual-minimizing solve over (mathcal K_2) can attain zero transformed residual, zero original residual, and zero true error.

## 8. Low-dimension failure control

PASS.

For:

[
B_{m bad}=operatorname{diag}(1,10),
qquad
c_{m bad}=(1,1)^	op,
]

the best one-dimensional residual scalar is:

[
alpha_{m bad}=11/101.
]

The residual is:

[
(90/101,-9/101)^	op,
]

with squared norm:

[
oxed{81/101}.
]

The chapter therefore correctly rejects low trial-space dimension as a convergence certificate.

## 9. Downstream readout firewall

PASS.

With:

[
w=(1,2)^	op,
]

the exact solution and non-exact one-step iterate both satisfy:

[
w^	op x=3/2.
]

Thus the downstream scalar readout is exact even though the one-step solve has nonzero residual and nonzero true error.

The manuscript correctly concludes that task/readout quality and solve quality are distinct objects.

## 10. Local/global nonlinear boundary

PASS.

A local Jacobian or explicitly declared local surrogate may define a Krylov operator.

The chapter does not identify that local operator with the global nonlinear representation map, and it explicitly blocks promotion from local Krylov improvement to global nonlinear convergence.

## 11. Preconditioner boundary

PASS.

The witness is fixed linear left preconditioning.

The chapter separately names right, flexible, learned, state-dependent, and nonlinear preconditioners as different semantics requiring separate analysis.

No fixed-linear guarantee is transferred to a learned/state-dependent preconditioner.

## 12. Matrix-free boundary

PASS.

Operator actions may be matrix-free, including JVP/VJP-style interfaces, but the operator itself still must be mathematically declared.

The manuscript does not use “matrix-free” as a substitute for operator identity.

## 13. Finite precision and restart

PASS.

The chapter preserves KRYLOV-001's exact-arithmetic versus floating-point boundary and states that restart/truncation can discard useful directions.

The finite witness itself shows horizon (m=1) misses a direction needed for the exact solve while (m=2) captures it.

No universal restart or horizon theorem is claimed.

## 14. Transaction-receipt provenance

PASS.

Every implementation artifact identity in governance/tranches/NEURALKRYLOV-001.md matches the exact protected implementation merge.

No post-receipt implementation repair occurred.

## 15. Repository integrity

PASS subject to audit-PR validation.

At the audited implementation merge:

- NEURALKRYLOV status is draft-v0.1;
- canonical specification/manuscript/derivation/source-lock/witness paths are populated;
- hard dependencies remain KRYLOV-001 and TRANSPORT-001;
- the source lock is registered;
- no new bibliography key or governed figure is required;
- exact implementation head passed GitHub Actions run 37547958975;
- protected implementation merge passed canonical repository validation;
- independent audit replay returned NEURALKRYLOV_AUDIT_WITNESS_OK.

## Final disposition

AUDIT-064 passes with no repair.

The durable NEURALKRYLOV rule is:

**short-horizon operator-generated computation can improve a declared local solve, but every guarantee is relative to an explicitly named linear operator, preconditioner, metric, and interface; classical Krylov convergence does not transfer to learned nonlinear representation transport by analogy.**
