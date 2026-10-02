# FOUNDATION-001 — Reader Spine Through Representation

## Status

**Tranche state:** implemented on branch pending merge validation.

## Baseline

- synthesis integrity merge: `3f74175d14e587d2567140025a79bfa78eefd125`;
- issue: `#19`;
- starting architecture: 80 chapters / 126 hard dependency edges;
- six audited keystones at `draft-v0.1`.

## Objective

Backfill the smallest reader-facing dependency spine required to make Representation executable from the root of the Atlas:

1. `ATLAS-CH-THESIS-001` — The Adaptive-System Thesis;
2. `ATLAS-CH-OBJECTS-001` — States, Operators, Flows, and Interfaces;
3. `ATLAS-CH-LINALG-001` — Linear Maps and Decompositions;
4. `ATLAS-CH-INFO-001` — Probability, Information, and Statistical Structure;
5. `ATLAS-CH-REP-001` — Representations and Invariants.

The already-drafted Geometry keystone supplies Representation's second hard prerequisite.

## A. Thesis

### Epistemic class

Atlas Synthesis.

The chapter states the governing thesis:

> Adaptive intelligence is more usefully studied here as organized computation over states, operators, dynamics, memory, interfaces, evidence, and governance than as a catalogue of model classes.

The source lock binds this only to Atlas project scope and doctrine. It is not presented as an externally established theorem.

### Durable objects

- specification: `manuscript/specifications/ATLAS-CH-THESIS-001.md`;
- source lock: `sources/source-locks/ATLAS-CH-THESIS-001.yaml`;
- documentary packet: `mathematics/derivations/ATLAS-CH-THESIS-001-DERIVATIONS.md`;
- manuscript: `manuscript/parts/01-orientation/ATLAS-CH-THESIS-001.md`.

## B. States, Operators, Flows, and Interfaces

### Epistemic class

Atlas Synthesis with standard mathematical instances.

The chapter freezes the project-local four-role vocabulary and teaches category-error avoidance:

- state;
- operator;
- flow/dynamics;
- interface/contract.

It explicitly states that the taxonomy is explanatory rather than universal.

### Durable objects

- specification: `manuscript/specifications/ATLAS-CH-OBJECTS-001.md`;
- source lock: `sources/source-locks/ATLAS-CH-OBJECTS-001.yaml`;
- derivation/object-role packet: `mathematics/derivations/ATLAS-CH-OBJECTS-001-DERIVATIONS.md`;
- manuscript: `manuscript/parts/01-orientation/ATLAS-CH-OBJECTS-001.md`.

## C. Linear Maps and Decompositions

### Sources

Source-locks:

- Trefethen–Bau 1997;
- Horn–Johnson 2012;
- Golub–Van Loan 2013.

### Exact witness

For

[
A=
egin{pmatrix}
1&1\
0&1
end{pmatrix},
]

the repeated eigenvalue is (1), while the singular values are

[
rac{1+sqrt5}{2},
qquad
rac{sqrt5-1}{2}.
]

For

[
D=operatorname{diag}(1,1/100),
]

[
kappa_2(D)=100.
]

The witness also checks projection idempotence and the rank-one approximation error.

### Figure

`ATLAS-FIG-LINALG-001`

- source blob: `94450cbddb6c10c06d61f758454ef0aa0090caf8`;
- rendered blob: `d861c038e841450ccfabb8f0709e161d6a555450`;
- rendered bytes: 41,238.

### Durable objects

- specification;
- source lock;
- derivation packet;
- computational witness;
- complete manuscript draft;
- registered rendered figure.

## D. Probability, Information, and Statistical Structure

### Sources

Source-locks:

- Cover–Thomas 2006;
- Wainwright–Jordan 2008;
- Vershynin 2018.

### Exact witness

For

[
P_{XY}
=
egin{pmatrix}
3/8&1/8\
1/8&3/8
end{pmatrix},
]

with uniform marginals,

[
I(X;Y)
=
rac{log(27/16)}{log16}
approx
0.1887218755408671
]

bits.

The chapter explicitly preserves:

- KL is not a metric;
- support mismatch can make KL infinite;
- mutual information is dependence, not causal direction;
- sufficient statistics are relative to a statistical family.

### Figure

`ATLAS-FIG-INFO-001`

- source blob: `9b4feabb9f0413dd3fa499b8353e84e405391da4`;
- rendered blob: `46ac60a0ff3c0b14fa81bf970e8307f182442d08`;
- rendered bytes: 21,815.

## E. Representations and Invariants

### Sources

Source-locks:

- Bengio–Courville–Vincent 2013;
- Cohen–Welling 2016;
- Locatello et al. 2019;
- Olshausen–Field 1996;
- Elhage et al. 2022, explicitly as non-peer-reviewed toy-model/research evidence.

### Exact witness

Reflection:

[
G=operatorname{diag}(-1,1),
qquad
x=(2,3),
]

gives an equivariant vector representation and invariant squared norm

[
|x|_2^2=|Gx|_2^2=13.
]

Invertible recoding:

[
T=
egin{pmatrix}
1&1\
0&1
end{pmatrix}
]

with transformed readout

[
	ilde w=T^{-	op}w
]

preserves the declared linear output exactly.

### Figure

`ATLAS-FIG-REP-001`

- source blob: `9aad5571d51fd9c8dcfc08dfebd300c3758c5a2a`;
- rendered blob: `e14a1b9738190ed9b5930657c82dbe3c8ea21492`;
- rendered bytes: 44,643.

The figure is classed schematic because the recoding layout is presentation geometry even though all displayed numeric relations are exact.

## F. Source discipline

The bibliography was expanded with canonical references for the foundation spine.

The Representation chapter preserves a strict source boundary:

- peer-reviewed sources support representation learning, equivariance, identifiability limits, and sparse coding;
- the superposition source is explicitly non-peer-reviewed toy-model research evidence;
- broader representation-equivalence synthesis is Atlas-owned.

## G. Chapter Ledger

These five nodes are promoted to:

`draft-v0.1`.

Each records:

- specification path;
- manuscript path;
- derivation/documentary path;
- source-lock path;
- computational witness path where material;
- figure IDs where material.

No other architecture node is promoted by this tranche.

## H. Validator extension

The validator is generalized so every `draft-v0.1` chapter, not only keystones, must have:

- specification;
- manuscript;
- derivation/documentary packet;
- source lock.

A computational witness is checked when declared.

Existing citation closure, figure registry, DAG, replay, and control-character checks remain active.

## Epistemic boundaries

This tranche preserves:

[
	ext{Atlas thesis}

eq
	ext{externally established theorem}.
]

[
	ext{coordinates}

eq
	ext{operator or semantic identity}.
]

[
	ext{mutual information}

eq
	ext{causal direction}.
]

[
	ext{invariance}

eq
	ext{equivariance}.
]

[
	ext{task-preserving recoding}

eq
	ext{universal semantic equivalence}.
]

[
	ext{toy superposition evidence}

eq
	ext{universal empirical prevalence}.
]

## Next step after merge

Run a bounded FOUNDATION-001 audit over all five reader-spine chapters before drafting normalized or quotient representations.

The audit should independently check:

- source/citation closure;
- linear-algebra exact witnesses;
- information-theory exact witness;
- representation invariance/equivariance and recoding algebra;
- figure generator/master/manifest identity;
- source-scope boundaries;
- dependency closure;
- no epistemic promotion beyond `draft-v0.1`.
