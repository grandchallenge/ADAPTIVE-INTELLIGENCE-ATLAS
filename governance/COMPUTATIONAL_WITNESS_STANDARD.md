# Atlas Computational Witness Standard

**Standard ID:** `GCL-ATLAS-CW-001`  
**Status:** canonical project-local standard

## Definition

A computational witness is a reproducible symbolic, numerical, graphical, finite-search, simulation, or documentary computation that supports a bounded claim.

It is an evidence object, not an automatic proof object.

## Required record

A governed witness should record, where applicable:

1. **Witness identity** — stable Atlas ID.
2. **Chapter identity** — the chapter consuming it.
3. **Purpose** — the exact question being tested or reconstructed.
4. **Inputs** — exact parameters, matrices, datasets, candidate objects, seeds, or source revisions.
5. **Environment** — runtime, library/tool versions, architecture when material, and determinism assumptions.
6. **Mathematical convention** — norm, precision, branch convention, tolerance, units, coordinate convention, or domain.
7. **Method** — symbolic computation, finite search, simulation, numerical solve, replay, or other operation.
8. **Expected/result object** — values, files, inequalities, images, or states that constitute the witness result.
9. **Replay route** — command, notebook, Wolfram source, proof checker, or deterministic procedure.
10. **Identity checks** — hashes or immutable revisions where meaningful.
11. **Claim boundary** — what the witness establishes and what it does not.
12. **Figure relationship** — when a figure is derived from the witness, bind the figure generator and rendered artifact separately.

## Precision doctrine

Use exact arithmetic when it materially strengthens the claim and is computationally practical.

When floating-point arithmetic is used, record:

- precision;
- tolerance;
- norm;
- stopping criterion where applicable;
- whether displayed values are rounded;
- whether the conclusion is robust to the stated numerical uncertainty.

## Wolfram doctrine

Wolfram Language is preferred when it materially improves:

- symbolic derivation;
- exact matrix computation;
- high-precision numerics;
- eigensystems and pseudospectra;
- manifolds;
- phase portraits;
- stability regions;
- vector fields;
- implicit surfaces;
- parameter sweeps.

The rendered figure is not the witness by itself. The generator, parameters, and claim boundary are part of the witness.

## Replay doctrine

When a witness is meant to be executable replay evidence, prefer:

- immutable inputs;
- content digests;
- deterministic dependencies where practical;
- locked expected outputs;
- CI execution for small durable witnesses.

A random seed is not presumed to be a complete environment record.

## Failure discipline

A witness must not silently promote:

- finite verification to an infinite theorem;
- local linearization to global nonlinear behavior;
- one toy mechanism to empirical prevalence;
- reproduced bytes to correct semantics;
- internal replay to independent replication;
- green CI to institutional certification.

## Existing precedents

The first six keystone witnesses define the initial precedent set:

- sphere geometry;
- non-normal transient growth and pseudospectra;
- attention operator decomposition;
- optimizer-state transient amplification;
- boundary sensitivity;
- deterministic evidence replay.
