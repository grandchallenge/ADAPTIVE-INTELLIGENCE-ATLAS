# LOCALGLOBAL-001 — Local-to-Global Mathematics

## Identity

- chapter: `ATLAS-CH-LOCALGLOBAL-001`
- issue: #125
- baseline: `ed3f07a2531c520e0fad43f072340f8099448098`
- branch: `work/localglobal-001`
- hard prerequisite:
  - `ATLAS-CH-OBJECTS-001`

Exact prerequisite binds:

- Objects manuscript: `6e8bd13b7d7ec7337e14135f8e9cf0a7fc415054`
- AUDIT-004: `948f76b3f86d27fa4830efc30d8ef0135134256e`
- Objects source lock: `805b06978f08c7efa7add3f36fca0301dca7047b`

## Central local-to-global structure

- local section spaces `F(U)`;
- restriction maps `rho^U_V:F(U)->F(V)`;
- matching families on overlaps;
- gluing existence;
- gluing uniqueness;
- overlap discrepancy/obstruction.

For the finite two-set cover, the exact algebra is:

`R:R^3->R^4`,
`R(x,y,z)=(x,y,y,z)`;

`Delta:R^4->R`,
`Delta(u_a,u_b,v_b,v_c)=u_b-v_b`.

The witness proves:

`R` is injective;

`im(R)=ker(Delta)`.

## Exact witness

Compatible local data:

- U section `(1,2)`;
- V section `(2,4)`;
- overlap discrepancy `0`;
- unique global glue `(1,2,4)`.

Incompatible local data:

- U section `(1,2)`;
- V section `(3,4)`;
- overlap discrepancy `-1`;
- no global glue.

## Durable distinctions

- graph/cover incidence versus data and maps carried over it;
- local section versus global section;
- presheaf restriction structure versus sheaf unique-gluing property;
- gluing existence versus gluing uniqueness;
- exact matching versus approximate fusion;
- consistency versus factual truth or semantic adequacy;
- explicit obstruction versus vague global failure.

## Remaining gates

Validate, merge implementation, run bounded audit, repair and validate audit, merge, verify closure, recompute frontier, reset controller.
