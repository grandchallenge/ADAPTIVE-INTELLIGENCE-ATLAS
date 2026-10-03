# COORD-001 — Coordination Architectures

## Status

**Tranche state:** implemented on branch pending merge validation.

## Baseline

- baseline: 79a066f9e4c22022f09a03fda7945264ef10619b;
- issue: #76;
- hard prerequisite:
  - ATLAS-CH-AGENTS-001 at draft-v0.1;
  - AUDIT-015 PASS.

## Objective

Establish the coordination layer required when several bounded agent loops communicate, synchronize, share state, retry, or act on common resources.

## Central object

C = (I, {A_i}, {X_i}, S, K, ≺, T, F).

The chapter separates actors, local state, shared coordination state, channels/operations, causal ordering, transaction semantics, and failure/retry policy.

## Architecture families

The manuscript develops:

- direct message passing;
- rendezvous;
- blackboards;
- Linda-style tuple spaces;
- event-driven / append-only coordination;
- transactions.

No family is presented as universally superior.

## Exact witness

ATLAS-CW-COORD-001 exhaustively enumerates the six legal interleavings of two non-atomic read-modify-write increments.

Results:

- 2 schedules finish at x=2;
- 4 schedules finish at x=1.

Two atomic increment transactions finish at x=2 in either transaction order.

## GCL example

Exact public AETHER artifacts at commit 74b2e322a4453f1665a076bc0682adcd0c5cfb44 are used as bounded project evidence for one event/provenance-oriented coordination design.

## Figure decision

No governed figure is added in v0.1.

The architecture table, causal-order notation, and complete interleaving witness carry the semantics directly.

## Durable objects

The branch contains:

- sources/source-locks/ATLAS-CH-COORD-001.yaml;
- manuscript/specifications/ATLAS-CH-COORD-001.md;
- mathematics/derivations/ATLAS-CH-COORD-001-DERIVATIONS.md;
- mathematics/computational-witnesses/ATLAS-CW-COORD-001.md;
- manuscript/parts/13-agents-systems-hardware/ATLAS-CH-COORD-001.md;
- Chapter Ledger promotion to draft-v0.1;
- Source Register entry.

## Next step after merge

Run a bounded post-draft audit of mechanism identities, causal-order semantics, lost-update enumeration, delivery/effect distinctions, transaction boundaries, AETHER claim scope, and downstream handoffs.
