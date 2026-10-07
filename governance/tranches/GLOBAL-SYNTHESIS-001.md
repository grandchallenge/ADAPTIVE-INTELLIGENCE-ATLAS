# GLOBAL-SYNTHESIS-001 — Full-Manuscript Coherence Pass

## Status

Bounded global-synthesis implementation record.

## Identity

- issue: #293
- protected baseline: `c62320923c40e8c7c941fd551a26459f8d38b4d9`
- branch: `synthesis/global-293`
- scope: manuscript-wide coherence and documentary reconciliation after exhaustion of the architecture drafting frontier
- promotion authority: none

## Baseline inventory

At the protected baseline:

- 14 Parts;
- 80 stable chapter nodes;
- 80 chapters at `draft-v0.1`;
- 0 chapters at `architecture`;
- 126 hard prerequisite edges;
- one dependency root;
- 18 registered rendered-witness figures;
- 85 Source Register entries.

The canonical validator reports the hard dependency graph as acyclic.

## Governing doctrine

This pass is required by:

- `governance/ATLAS_EDITORIAL_PROFILE.md`;
- `governance/CHAPTER_FAMILY_ROLLOUT.md`;
- `governance/CHAPTER_COMPOSITION_PROTOCOL.md`;
- `governance/EPISTEMIC_STATUS.yaml`;
- `governance/MATHEMATICAL_LEXICON.yaml`;
- `governance/DEPENDENCY_GRAPH.md`.

The governing composition sequence is:

`architecture -> dependency graph -> keystone chapters -> six-keystone synthesis -> chapter families -> global synthesis`.

## Finding 1 — public phase state was stale

The repository README still described the project as an "architecture bootstrap" and described the architecture release as a future target.

That was inconsistent with the protected Chapter Ledger, which now records all 80 chapter nodes at `draft-v0.1` and zero at `architecture`.

### Repair

The README now states:

- full first-draft corpus;
- global synthesis in progress;
- 80/80 chapters at `draft-v0.1`;
- no publication, certification, or final-copy promotion.

No chapter lifecycle state was changed by this repair.

## Finding 2 — rollout plan was being read as current state

`governance/CHAPTER_FAMILY_ROLLOUT.md` correctly recorded its original six-keystone baseline and 74 undrafted chapters, but did not say that the plan had now been executed to completion.

### Repair

The rollout document is retained as historical execution rationale and now explicitly records:

- original baseline: six audited keystones;
- original remaining chapters: 74;
- current phase: 80/80 draft-v0.1, architecture frontier exhausted, global synthesis active;
- current lifecycle authority: Chapter Ledger and controller state.

The historical family sequence itself is unchanged.

## Finding 3 — editorial profile lagged the project phase

The editorial profile still identified itself as "post six-keystone synthesis."

### Repair

The profile now records the global-synthesis phase and freezes three distinctions:

1. `CHAPTER_LEDGER.yaml` is authoritative for chapter lifecycle state;
2. `Status: specification-ready` inside a specification file describes that specification artifact and does not override ledger lifecycle state;
3. stable chapter IDs and ledger `part_id` values carry semantic identity, while filesystem paths remain presentation coordinates.

No upstream authority was enlarged.

## Finding 4 — FRONTIER reader had a noncanonical live path

The ledger-selected `ATLAS-CH-FRONTIER-001` reader was stored at:

`governance/tranches/CH171-READER.md`.

AUDIT-043 explicitly accepted this as a recoverable connector-path workaround, not a governance relaxation.

### Repair

A canonical reader copy now exists at:

`manuscript/parts/14-scientific-method-governed-adaptation/ATLAS-CH-FRONTIER-001.md`.

Before ledger rebinding, the two files were verified byte-identical:

`e1a692a7e6406041a6e4395c0e23a0732fb5b4e3`.

The original historical artifact remains preserved. The ledger now points to the canonical manuscript location.

### Historical-status boundary

FRONTIER's references to "architecture-stage" programmes are part of its exact source-locked programme snapshot at the chapter's historical baseline. They are not silently rewritten into current lifecycle assertions.

Current chapter lifecycle state is governed by the protected Chapter Ledger.

## Finding 5 — MECHDIAG ledger selected the minimal probe rather than its audited mature reader

The ledger selected:

`manuscript/parts/12-diagnostics-robustness-compression/_probe.md`.

AUDIT-047 explicitly bound the mature reader companion:

`manuscript/parts/12-diagnostics-robustness-compression/ATLAS-CH-DIAGREAD-001.md`.

### Repair

A canonical chapter reader now exists at:

`manuscript/parts/12-diagnostics-robustness-compression/ATLAS-CH-MECHDIAG-001.md`.

Before ledger rebinding, it was verified byte-identical to the AUDIT-047 mature reader companion:

`8275d106f3960eb21e385b3d9130b3cb7686fec0`.

The original probe and companion remain preserved. The ledger now points to the canonical mature reader.

## Finding 6 — legacy directory numbering is not chapter identity

Some earlier chapter files retain directory names from earlier editorial coordinates, including optimization material under a legacy `05-optimization` path and two legacy Part-7 directory labels.

The Atlas editorial profile already states that filesystem location is a presentation coordinate rather than stable identity.

### Disposition

No mass path migration is performed.

The stable chapter ID, ledger `part_id`, dependency graph, and Atlas Map determine semantic identity and Part membership.

Moving source-locked historical files solely to normalize directory prefixes would create provenance churn without strengthening the mathematics.

## Finding 7 — epistemic and dependency controls remain coherent

The global pass found no reason to alter:

- the 126 hard dependency edges;
- the one-root acyclic dependency structure;
- the canonical epistemic vocabulary;
- the Mathematical Lexicon notation contract;
- any source lock;
- any computational witness;
- any figure manifest;
- any mathematical claim;
- any chapter status.

Historical transaction receipts and audits retain the state they recorded at their own baselines. They are not rewritten to mimic current state.

## Reader-path closure after repair

After the two path normalizations:

- all 80 ledger chapters have a manuscript path;
- all 80 manuscript paths exist;
- all 80 ledger manuscript paths are under `manuscript/parts/`;
- the Chapter Ledger remains 80/80 `draft-v0.1`.

## Validation

A Windows-native execution of `tools/validate_atlas.py` produced only a raw-byte replay mismatch caused by CRLF stdout translation.

The same checked-out tree was then replayed under Linux/WSL, matching the GitHub Actions newline environment:

`OK: 80 chapters, 126 hard edges, 1 root(s), 0 specification-ready keystones, 80 draft chapters, 18 rendered witnesses, 18 registered figures, 85 sources, 175 bibliography keys`

Exact GitHub Actions validation is still required on the final pushed synthesis head before merge.

## Promotion boundary

This synthesis pass does not:

- promote any chapter beyond `draft-v0.1`;
- certify any mathematical result;
- convert a programme claim into established theory;
- grant publication-ready or final-copy status;
- authorize a release candidate.

Those are separate governed transitions.

## Remaining synthesis boundary

This bounded pass establishes repository-level lifecycle, reader-path, dependency, and documentary coherence.

It does not claim that every sentence across all 80 chapters has undergone final copy-editing or that all cross-chapter exposition is publication-ready.

Any release-candidate transaction must separately address release governance, licensing, final build/copy-edit, and publication promotion requirements.
