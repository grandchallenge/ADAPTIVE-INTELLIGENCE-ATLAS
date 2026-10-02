# ADR-0004 — Dependency Semantics

## Status

Accepted for the keystone specification tranche.

## Context

Atlas v0.1 records one untyped `dependencies` list per chapter. That is sufficient to guarantee a directed acyclic architecture, but it does not distinguish a true reading prerequisite from a useful cross-link or from a later synthesis relationship. For a long monograph, that distinction matters: otherwise a reader cannot tell what must be understood first, an author cannot tell which definitions may be assumed, and a global synthesis pass cannot tell whether two chapter families merely refer to one another or actually depend on one another.

The v0.1 graph contains 80 chapter nodes and 126 hard edges. It is acyclic and has one root, `ATLAS-CH-THESIS-001`.

## Decision

Maintain two graph layers.

### 1. Hard dependency DAG

The existing `CHAPTER_LEDGER.yaml:dependencies` remains the canonical hard prerequisite relation.

A hard edge (A \to B) means that chapter (B) may assume a concept, notation, result, or framing established in (A). Hard dependencies must remain acyclic.

Hard dependencies are further described, when useful, by one of these semantic roles:

- `formal` — definitions, notation, or mathematical results are directly consumed;
- `conceptual` — a viewpoint or object taxonomy is consumed;
- `methodological` — an evidentiary, experimental, or procedural discipline is consumed;
- `synthesis` — the target chapter explicitly composes two or more mature streams.

The role annotation explains an existing hard edge; it does not create a second source of truth for adjacency.

### 2. Soft cross-links

A soft cross-link connects chapters that illuminate one another but do not impose reading order. Soft links may be cyclic. They are recorded in `governance/DEPENDENCY_GRAPH.yaml`.

Examples include:

- geometry ↔ information geometry;
- non-normality ↔ optimizer dynamics;
- operator splitting ↔ boundary contracts;
- replayable evidence ↔ formal methods.

Soft links are editorial navigation, not prerequisites.

## Keystone dependency cones

Each keystone specification must declare:

- immediate hard prerequisites;
- inherited prerequisite cone;
- the concepts it is permitted to assume;
- downstream chapters that rely materially on it;
- soft cross-links that should become reader-facing bridges.

This turns a chapter specification into a local contract against the global DAG.

## Change control

Changing a chapter’s hard prerequisite set changes the executable reading architecture and must update:

1. `CHAPTER_LEDGER.yaml`;
2. `DEPENDENCY_GRAPH.yaml`;
3. any affected keystone specifications;
4. validation tests.

Adding or removing a soft cross-link requires only `DEPENDENCY_GRAPH.yaml` and any relevant prose cross-reference.

## Consequence

The Atlas can now distinguish “read this first” from “this will help you see the same structure elsewhere.” That is essential to preserving rigor without forcing every chapter into one linear reading order.
