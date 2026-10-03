# MEMTAX-001 — A Taxonomy of Machine Memory

## Status

**Tranche state:** implemented on branch pending merge validation.

## Baseline

- baseline: 9a00ed8fc6b0ca160a9b7e1fb4deef7c078f69cf;
- issue: #88;
- hard prerequisite:
  - ATLAS-CH-REP-001 at audited draft-v0.1.

## Objective

Define a machine-memory taxonomy by engineering role rather than biological analogy.

## Central object

M = (L, W, R, T, A, U, P, S).

Coordinates:
- locus;
- write path;
- read path;
- lifetime;
- addressability;
- mutability;
- provenance;
- sharing/synchronization.

## Six roles

- parametric;
- working;
- episodic;
- semantic;
- associative;
- external persistent.

The roles overlap and do not form a scalar hierarchy.

## Exact witness

One immutable three-record store is queried through:
- exact key;
- nearest-vector association;
- event-time/recency filtering.

The store is unchanged while memory behavior changes with the read contract.

## Source basis

- Baddeley-Hitch;
- Tulving;
- Hopfield;
- Memory Networks;
- Neural Turing Machines;
- Differentiable Neural Computer;
- Neural Episodic Control;
- parametric-knowledge evidence in language models.

Cognitive sources provide terminology lineage only.

## Figure decision

No governed figure is added in v0.1.

The coordinate taxonomy and exact multi-access witness carry the semantics directly.

## Durable objects

- sources/source-locks/ATLAS-CH-MEMTAX-001.yaml;
- manuscript/specifications/ATLAS-CH-MEMTAX-001.md;
- mathematics/derivations/ATLAS-CH-MEMTAX-001-DERIVATIONS.md;
- mathematics/computational-witnesses/ATLAS-CW-MEMTAX-001.md;
- manuscript/parts/09-memory-beyond-weights/ATLAS-CH-MEMTAX-001.md;
- Chapter Ledger promotion;
- Source Register entry.

## Next step after merge

Run a bounded post-draft audit of category overlap, terminology scope, source identity, exact witness arithmetic, storage/access separation, persistence/provenance boundaries, and downstream handoffs.
