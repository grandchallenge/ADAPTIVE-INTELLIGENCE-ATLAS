# BOUNDARYPROBE-001 — Boundary Probes

## Identity

- chapter: `ATLAS-CH-BOUNDARYPROBE-001`
- issue: #116
- baseline: `c82f61da1ca457b9670273669c04fe3fd5459652`
- branch: `work/boundaryprobe-001`
- hard prerequisites:
  - `ATLAS-CH-LINALG-001`
  - `ATLAS-CH-NETNUM-001`

Exact prerequisite binds:

- LINALG manuscript: `e7fcf56322f26d232d3a3043038d9850792b4bde`
- Foundation audit: `948f76b3f86d27fa4830efc30d8ef0135134256e`
- LINALG source lock: `f24e93ee0c2496ca0b9d71f6f824b0d13dbdc08e`
- NETNUM manuscript: `cbaf0b96c996c821df50f985075f64028459c587`
- NETNUM audit: `746e0c297e4ddf29122d4735108becc33e599030`
- NETNUM source lock: `02bbe77d19da4a6a123e430f8aae058d666c4e35`

## Central objects

- JVP: `J_F(x)v`
- VJP: `J_F(x)^T w`
- local Euclidean gain: `sigma_max(J_F(x))`
- power probe on `J^T J`
- boundary-probe contract:
  `B=(F,X,Y,O,U,N_X,N_Y,P,E,tau)`

## Exact witness

For

`F(x1,x2)=(x1^2+x2,x1+2x2)`

at `x0=(1,1)`:

- `J=[[2,1],[1,2]]`
- singular values: `3,1`
- JVP at `v=(1,1)`: `(3,3)`
- VJP at `w=(1,2)`: `(4,5)`
- pairing identity: `9=9`
- mixed-start power iteration gives Rayleigh values `365/41`, `29525/3281` approaching `9`
- start `(1,-1)` remains in the weak eigenspace and reports `1` forever despite true norm `3`

Thus finite power iteration is an estimator, not an automatic upper certificate.

## Durable distinctions

- JVP versus VJP;
- forward versus reverse derivative propagation;
- local sensitivity versus global nonlinear behavior;
- mathematical operator norm versus finite estimator;
- probe initialization/iteration metadata versus bare scalar output;
- numerical interface sensitivity versus semantic compatibility.

## Remaining gates

Validate, merge implementation, run bounded audit, repair and validate audit, merge, verify closure, recompute frontier, reset controller.
