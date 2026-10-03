# EVIDEX-001 — Evidence Exchange and Zero-Context Work

## Status

**Tranche state:** implemented on branch pending merge validation.

## Baseline

- baseline: ffca5ab3dbc75ef0b3ce0ff5afe13d86f32ae75e;
- issue: #92;
- hard prerequisites:
  - ATLAS-CH-COORD-001 at audited draft-v0.1;
  - ATLAS-CH-EVIDENCE-001 at audited draft-v0.1.

## Objective

Define a portable evidence-handoff interface that does not depend on hidden conversational state.

## Central objects

Dispatch:

D = (delta, Q, B, Sigma, C, Lambda, Gamma, rho).

Return:

R = (delta, chi, K, Pi, V, Delta).

Zero-context sufficiency is defined relative to a declared actor class by invariance of the reconstructed task contract under admissible hidden histories.

## Exact witness

Two source versions share the pathname inputs.txt.

- v1 SHA-256:
  b64a71cff6737624915d32f719c1c6957c60cfb0b286eb9d0b5d3741f26b1265
- v2 SHA-256:
  c572528f7b0e700de0fd7bf2f3b7144a68f671ee0ed4b9d47943d9b489fe9844

The same returned bytes result=5 are ambiguous under pathname-only provenance but replay uniquely under the exact v1 hash within the declared finite candidate set.

## External basis

- W3C PROV-DM;
- FAIR Guiding Principles.

## Bounded GCL project evidence

Exact public MATHSOLVE commit 1273b75457f42da62a8af4c69493d44d293d4567:

- zero-context CEI dispatch template;
- RESULT/1 grammar;
- independent_blind ZERO_CONTEXT adversarial packet.

These demonstrate one implementation and are not promoted into universal standards.

## Figure decision

No governed figure is added in v0.1.

The dispatch/return tuples and exact provenance-ambiguity witness carry the semantics directly.

## Durable objects

- sources/source-locks/ATLAS-CH-EVIDEX-001.yaml;
- manuscript/specifications/ATLAS-CH-EVIDEX-001.md;
- mathematics/derivations/ATLAS-CH-EVIDEX-001-DERIVATIONS.md;
- mathematics/computational-witnesses/ATLAS-CW-EVIDEX-001.md;
- manuscript/parts/13-agents-systems-hardware/ATLAS-CH-EVIDEX-001.md;
- Chapter Ledger promotion;
- Source Register entry.

## Next step after merge

Run a bounded post-draft audit of source identity, zero-context semantics, provenance/truth separation, exact witness hashes, receipt/acceptance/promotion boundaries, GCL project-evidence scope, and downstream handoffs.
