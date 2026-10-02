# ADR-0002 — Stable Semantic Object Identifiers

## Status
Accepted for bootstrap.

## Decision
Use stable `ATLAS-*` identifiers for chapters, definitions, results, figures, allegories, and computational witnesses. Chapter numbers and paths are presentation coordinates only.

## Rationale
A long monograph will be reordered repeatedly. Provenance must survive moves, merges, and retitling.

## Consequences
Cross-references should target stable IDs. CI should reject duplicate identifiers and unresolved dependencies.
