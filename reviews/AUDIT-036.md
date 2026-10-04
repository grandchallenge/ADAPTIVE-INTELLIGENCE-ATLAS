# AUDIT-036 — Split-Operator Networks

## Disposition

**PASS AFTER FOUR PRECISION/NOTATION REPAIRS**

`ATLAS-CH-SPLIT-001` remains at `draft-v0.1`.

The implementation correctly established the finite-dimensional Lie/Strang witness, the commutator-controlled order effect, the commuting control, the additive-versus-sequential distinction, and the central firewall between exact-flow theory and neural architectural synthesis.

AUDIT-036 found four in-scope defects:

1. matrix-product labels were occasionally described as chronological execution order even though column-vector products act right-to-left;
2. the neural Strang analogy used half-step language before defining a step-parameterized learned-map family with a meaningful half-stage;
3. the nonlinear/Jacobian discussion did not distinguish the derivative of the nonlinear composition defect from a same-state algebraic Jacobian commutator;
4. several inline TeX delimiters were malformed by the implementation write and required documentary repair.

All four defects were repaired on the audit branch. No prerequisite edge, source authority, Chapter Ledger status, finite witness arithmetic, or downstream dependency required reversal.

## Audited baseline

- implementation merge:
  `2776a2d77fff39e90bd58a866b0275d946909fa9`;
- implementation PR:
  #142;
- implementation issue:
  #141;
- audit issue:
  #143;
- chapter:
  `ATLAS-CH-SPLIT-001`.

Merged implementation artifact blobs before audit repair:

- specification:
  `8e5c37f84c70e6e8921d8bd3927f568c5521fe7b`;
- derivation packet:
  `0a0ca84d8c8106e1f994a582347a8b40d3a06d40`;
- computational witness:
  `82eed25dd3d719ec0d7ba95d304350e2ec07a292`;
- manuscript:
  `e05fec9d5f61ced2e045066cf48ba8d8ea5f8ad5`;
- source lock:
  `6642e3d299cfa53efcd87225a932e40f065b9102`.

Repaired audit-head artifact blobs:

- specification:
  `124bcef76fe7f6f8bdc58dd9a561bbf7912e6ae9`;
- derivation packet:
  `64dab4d0d497ac8990724e1366ed6610b317137f`;
- computational witness:
  `7216d90a84c3197ec646d19e3c3a6e88f43241ef`;
- manuscript:
  `bcaf1db6b1fc7144e2472ff2725f7ff561fe7fc0`;
- source lock:
  `afb84e2f3ebb941f320c52693b088b0eb078b8ce`.

## 1. Hard prerequisites

PASS.

The source lock binds exactly to the audited prerequisites at the protected implementation baseline.

### Discretization, Stability, and Splitting

- manuscript blob:
  `a719a16e86d1feb76679e1f1cda2d9d3393d2e42`;
- AUDIT-009 blob:
  `2bbb1b7687d6c4b8c0bfeed5206de836dac92dca`;
- source-lock blob:
  `7feea1c8ca3026fa1f61f35b87281b4afe9ccd8d`.

### The Transformer as Baseline Object

- manuscript blob:
  `197b74ffd40fe54b79ca15ab731b73538aada494`;
- AUDIT-011 blob:
  `e8bfa9b062b4b80bd0cccd49f168f99c40843f71`;
- source-lock blob:
  `dec885c68a9afb439aed9af5ca35b998519722bc`.

No downstream Composition or Transport chapter is used as hidden prerequisite authority.

## 2. External source scope

PASS.

The source lock uses:

- McLachlan and Quispel (2002) for splitting/composition, commutators, and order;
- Hairer, Lubich, and Wanner (2006) for geometric/composition-method boundaries and structure-preserving semantics;
- Vaswani et al. (2017) for baseline Transformer sublayer anatomy.

The neural split-operator interpretation remains Atlas synthesis.

The chapter does not claim that arbitrary learned blocks inherit exact-flow, second-order, reversibility, symplecticity, or convergence properties from those sources.

## 3. Product order versus chronological order

PASS AFTER REPAIR.

For column-vector states, a product

[
S_{AB}(h)=e^{hA}e^{hB}
]

acts right-to-left: the (B) subflow acts first and the (A) subflow second.

The original derivation called this the “A-then-B” composition, which was an execution-order ambiguity.

The repaired specification, derivation, witness, manuscript, and source-lock rule now state explicitly that:

- (S_{AB}) and (S_{BA}) are product-order labels;
- chronological A-then-B corresponds to (e^{hB}e^{hA});
- product subscripts are not used as ambiguous execution-order prose.

The matrix formulas themselves were already correct.

## 4. Lie commutator derivation

PASS.

For constant finite-dimensional matrices,

[
e^{hA}e^{hB}
-
e^{h(A+B)}
=
rac{h^2}{2}[A,B]+O(h^3),
]

while

[
e^{hB}e^{hA}
-
e^{h(A+B)}
=
-rac{h^2}{2}[A,B]+O(h^3).
]

Thus the leading product-order asymmetry is

[
e^{hA}e^{hB}-e^{hB}e^{hA}
=
h^2[A,B]+O(h^3).
]

The chapter correctly bounds this statement to the declared analytic finite-dimensional setting.

## 5. Exact noncommuting witness

PASS.

For

[
A=
egin{pmatrix}
0&1\
0&0
end{pmatrix},
qquad
B=
egin{pmatrix}
0&0\
1&0
end{pmatrix},
]

the witness has

[
A^2=B^2=0,
]

[
AB=
egin{pmatrix}
1&0\
0&0
end{pmatrix},
qquad
BA=
egin{pmatrix}
0&0\
0&1
end{pmatrix},
]

and

[
[A,B]=
egin{pmatrix}
1&0\
0&-1
end{pmatrix}.
]

The exact Lie-product difference is

[
e^{hA}e^{hB}-e^{hB}e^{hA}
=
h^2[A,B].
]

No audit repair changed this arithmetic.

## 6. Exact combined flow

PASS.

Since

[
(A+B)^2=I,
]

the exact combined flow is

[
e^{h(A+B)}
=
egin{pmatrix}
cosh h&sinh h\
sinh h&cosh h
end{pmatrix}.
]

At (h=1/2), independent replay reproduces the recorded Frobenius error of either Lie product:

[
|L-E|_F
approx
0.1793148493970293.
]

The numeric value is correctly treated as a bounded witness checkpoint rather than the source of the asymptotic order claim.

## 7. Strang witness

PASS.

The exact symmetric product is

[
S_{ABA}(h)
=
e^{hA/2}e^{hB}e^{hA/2}
=
egin{pmatrix}
1+h^2/2&h+h^3/4\
h&1+h^2/2
end{pmatrix}.
]

Comparison with the exact combined-flow series shows an (O(h^3)) local defect in the declared witness.

At (h=1/2), independent replay reproduces

[
|S_{ABA}-E|_F
approx
0.02370487546729764.
]

The chapter correctly states that this one smaller numeric error is not the proof of second-order convergence.

## 8. Neural half-step semantics

PASS AFTER REPAIR.

The implementation used a palindromic neural expression suggestive of

[
A/2	o B	o A/2
]

without first defining what “half of” a learned neural map means.

The repaired artifacts require a declared step-parameterized family

[
Psi_A(h),
qquad
Psi_B(h),
]

with a meaningful half-stage (Psi_A(h/2)) before forming a neural analogue

[
Psi_A(h/2)
circ
Psi_B(h)
circ
Psi_A(h/2).
]

The chapter now states that:

- duplicating a learned block is not automatically a half-flow;
- halving a residual coefficient is a new design choice unless a step semantics is declared;
- palindromic layout alone does not inherit Strang order.

## 9. Commuting control

PASS.

For

[
A_c=operatorname{diag}(1,2),
qquad
B_c=operatorname{diag}(3,4),
]

the commutator vanishes and

[
e^{hA_c}e^{hB_c}
=
e^{hB_c}e^{hA_c}
=
e^{h(A_c+B_c)}
]

exactly.

This correctly blocks the overstatement that every split composition is order-sensitive.

## 10. Additive versus sequential residual composition

PASS.

For

[
F_A(x)=hAx,
qquad
F_B(x)=hBx,
]

the additive update is

[
(I+h(A+B))x.
]

Chronological A-then-B sequential residual application is

[
(I+hB)(I+hA)x
=
(I+h(A+B)+h^2BA)x.
]

Reversing chronology gives the (h^2AB) cross term.

The chapter correctly uses this as a finite architectural distinction, not as a general convergence theorem.

## 11. Exact-flow versus neural-submap boundary

PASS.

The chapter defines actual learned submaps, for example,

[
Psi_A(H)=H+F_A(N_A(H)),
]

[
Psi_B(H)=H+F_B(N_B(H)).
]

It states that ordinary learned-map composition remains valid even when no exact continuous reference exists.

It does not replace those submaps by (e^{hA}) and (e^{hB}) unless exact-flow semantics have separately been established.

## 12. Normalization and effective submaps

PASS.

Normalization, masking, gating, clipping, routing, residual scaling, stochasticity when active, and data-dependent control flow are treated as part of the effective executed submap.

The chapter correctly states that dropping them changes the mathematical object unless an explicit approximation supports the omission.

## 13. Symmetric ordering versus invertibility

PASS.

The repaired manuscript distinguishes:

- palindromic/symmetric ordering;
- self-adjoint composition under a declared numerical-flow model;
- exact invertibility;
- practical reconstruction;
- reversible-network implementation.

A symmetric sequence of non-invertible learned maps is not promoted to an invertible network.

## 14. Shared versus layer-varying suboperators

PASS.

A repeated fixed pair (A,B) admits an autonomous reference interpretation.

Layer-dependent (A_k,B_k) instead requires a stage-dependent/nonautonomous reading.

A local commutator ([A_k,B_k]) is not silently promoted to one global autonomous commutator for the network.

## 15. Nonlinear composition defect and Jacobian diagnostics

PASS AFTER REPAIR.

For nonlinear learned maps, the repaired derivation defines the direct composition defect

[
C_Psi(x)
=
Psi_B(Psi_A(x))
-
Psi_A(Psi_B(x)).
]

When differentiable,

[
DC_Psi(x)
=
J_B(Psi_A(x))J_A(x)
-
J_A(Psi_B(x))J_B(x).
]

This is generally distinct from the same-state algebraic Jacobian commutator

[
J_B(x)J_A(x)-J_A(x)J_B(x).
]

The latter is now described only as a possible local diagnostic unless an additional approximation or theorem connects it to the nonlinear composition defect.

## 16. Error taxonomy

PASS.

The chapter keeps separate:

- splitting/discretization error relative to a declared reference flow;
- learned-function approximation error;
- finite-data estimation error;
- optimization error;
- stochastic run variation;
- finite-precision and implementation error.

Classical splitting order is allowed to govern only the first category under its assumptions.

## 17. Mathematical typography and documentary integrity

PASS AFTER REPAIR.

The implementation write contained malformed inline TeX delimiters, including escaped function arguments such as `\Psi_A\(H\)` and malformed `O\(h^4\)` terms.

The repaired specification, derivation, witness, and manuscript now use valid function arguments and valid inline/display delimiters.

A second targeted integrity scan found no remaining repair-generated escaped function-parenthesis defects.

## 18. Repository integrity

PASS subject to audit-PR validation.

At the repaired audit head:

- Chapter Ledger blob:
  `ef587a76bacb4c662b73f82a69615a580f35e1c5`;
- Source Register blob:
  `0b15a3ccdef193b26f4a27a15517f304dadec3d2`.

The Chapter Ledger retains SPLIT-001 at `draft-v0.1`.

The Source Register retains `ATLAS-SRC-SPLIT-LOCK-001`.

The manuscript retains the required epistemic marker, references section, and explicit source-lock path.

No governed figure is required for this tranche.

## 19. Downstream handoff

PASS.

After audit, Composition may inherit:

- additive versus sequential composition;
- explicit product-order semantics;
- finite-dimensional commutator order effects;
- the requirement that effective submaps include normalization/routing/masking semantics;
- the distinction between direct nonlinear composition defects and local Jacobian diagnostics.

Transport may inherit:

- staged composition as a transport interpretation only after the stage maps are declared;
- the distinction between exact flows and generic learned residual maps;
- the autonomous versus layer-varying/nonautonomous distinction.

Neither downstream chapter may inherit:

- exact-flow semantics for arbitrary Transformer sublayers;
- automatic Strang order for palindromic neural blocks;
- global reversibility from symmetry;
- a global noncommutation theorem from one local Jacobian diagnostic.

## Final disposition

AUDIT-036 passes after four repairs.

The durable split-operator layer is:

**declared submaps + explicit product/execution order + commutator-controlled exact reference mathematics + bounded symmetric-composition semantics + a strict firewall between numerical splitting error and learned neural approximation.**
