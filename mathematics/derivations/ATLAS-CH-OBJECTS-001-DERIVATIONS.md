# ATLAS-CH-OBJECTS-001 — Object-Role Packet

## D1. State

A state is an information-bearing value

[
xinmathcal X.
]

Its array representation does not determine its semantic role.

## D2. Operator

An operator is a transformation

[
F:mathcal X	omathcal Y.
]

If (Ainmathbb R^{n	imes n}), the same stored array may represent:

- a state whose entries are data;
- a linear operator (xmapsto Ax).

The distinction is semantic and operational.

## D3. Flow

A flow is a parameterized family

[
Phi_t:mathcal X	omathcal X
]

with composition law

[
Phi_{t+s}=Phi_tcircPhi_s
]

when a true flow structure is present.

A depth-indexed neural computation may be flow-like without satisfying an exact continuous-time group law.

## D4. Interface

An interface declaration states what one object exposes to another.

A shape signature is weaker than a semantic contract.

The Boundary Contracts keystone later refines this distinction.

## D5. Category-error examples

1. A square matrix used as a covariance state is not thereby an operator.
2. One residual block is not the same object as the entire depth-indexed evolution.
3. A tensor shape contract does not imply semantic compatibility.
4. An evidence record describing an operator is not the operator.

## Claim boundary

The four roles are Atlas explanatory categories. They are not a universal ontology, and a concrete object may occupy different roles under different modeling choices.
