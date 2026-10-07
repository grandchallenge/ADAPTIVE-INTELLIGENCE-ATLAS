# CURRENT HANDOFF — Adaptive Intelligence Atlas

**Date:** 2026-10-07
**Recovery authority:** `governance/ACTIVE_TRANSACTION.yaml` on `state/atlas-controller`
**Current protected main:** `2d09774f0f29dc9c47e48fdfb410a3725def669a`

## Restart rule

1. Read `governance/ACTIVE_TRANSACTION.yaml` first.
2. Read this handoff.
3. Fetch live `main`.
4. If live `main` differs from the recorded baseline, recompute lifecycle and release-readiness state.
5. Repository state overrides chat history.

## Current state

- controller state: `blocked-human-governance`;
- architecture drafting frontier: exhausted;
- first bounded global synthesis: complete and audited;
- non-promotional release readiness: complete and audited;
- Chapter Ledger: 80 chapters at `draft-v0.1`;
- canonical working release corpus: exactly 80 ledger-selected readers;
- public-release promotion: blocked by explicit Human Steward license selection;
- no publication-ready, final-copy, certified, release-candidate, or released status has been granted.

## RELEASE-READINESS-001 — completed

Implementation:

- issue: #297 — closed completed;
- PR: #298 — merged;
- protected baseline: `e22d9d383d048626797d7865bc7e9d3daebe1887`;
- exact validated implementation head: `1dbf6f1d24a24566503ca478c06007dfd13d0649`;
- GitHub Actions run: `37608881886` — success;
- implementation merge: `b0d6034a76dac0e2444fd24b37bd381790995619`;
- implementation merge tree has zero file differences from the validated implementation head.

Audit:

- `AUDIT-074`;
- audit issue: #299 — closed completed;
- audit PR: #300 — merged;
- bounded audit repair commit: `b53aeb88d826a5a04b2b1052ad2524bbe8bc8294`;
- exact validated audit head: `63b837e2250ebe36362f8a7532961600867091a4`;
- GitHub Actions run: `37609300522` — success;
- final audit merge / current protected main: `2d09774f0f29dc9c47e48fdfb410a3725def669a`;
- audit merge tree has zero file differences from the validated audit head;
- disposition: **PASS WITH ONE TOOL-CONTRACT REPAIR**.

## Durable release-readiness result

The Atlas now has a deterministic working-build boundary.

`tools/assemble_manuscript.py`:

- uses `governance/CHAPTER_LEDGER.yaml` as the sole canonical chapter membership/order authority;
- assembles exactly 80 canonical readers;
- rejects duplicate, missing, or non-`manuscript/parts/` canonical paths;
- emits one marker per canonical chapter;
- emits a machine-readable manifest containing stable chapter ID, Part ID, lifecycle state, path, Git blob identity, and source commit;
- marks generated output as non-promotional working material.

The 82 Markdown files under `manuscript/parts/` are intentionally not treated as 82 release chapters.

The two preserved non-ledger MECHDIAG files are:

- `manuscript/parts/12-diagnostics-robustness-compression/_probe.md`;
- `manuscript/parts/12-diagnostics-robustness-compression/ATLAS-CH-DIAGREAD-001.md`.

They remain historical/companion material and are excluded from the canonical assembly.

## Release-boundary enforcement

`tools/check_release_readiness.py` enforces:

- exactly 80 canonical chapters;
- all remain `draft-v0.1`;
- unique existing canonical manuscript paths under `manuscript/parts/`;
- only the two named MECHDIAG non-ledger companion files;
- required `CITATION.cff` book/commit-tag metadata;
- explicit `LICENSE_SELECTION_PENDING`;
- no substantive committed release artifact under `releases/` while the license gate is active.

The GitHub Actions workflow is now named:

`Validate Atlas repository`.

It executes:

1. `python tools/validate_atlas.py`;
2. `python tools/check_release_readiness.py`;
3. `python tools/assemble_manuscript.py --output /tmp/atlas-manuscript.md --manifest /tmp/atlas-manifest.json --check`.

The assembly path is therefore exercised in CI without retaining or publishing a release artifact.

## AUDIT-074 repair

The audit found one bounded command-line contract defect.

Implementation help text said `--check` required explicit temporary output paths, but the implementation did not enforce that condition.

Audit repair commit:

`b53aeb88d826a5a04b2b1052ad2524bbe8bc8294`.

After repair:

- `python tools/assemble_manuscript.py --check` exits 1;
- it reports that explicit `--output` and `--manifest` paths are required;
- explicit temporary paths succeed and assemble all 80 canonical chapters.

## Current corpus metrics

Release-readiness scan:

- canonical chapters: 80;
- approximate canonical-reader words: 199,638;
- median chapter length: approximately 2,550 words;
- canonical readers under 1,000 words: one.

The material outlier is:

- `ATLAS-CH-MECHDIAG-001`: approximately 236 words.

AUDIT-047 established the chapter's bounded technical/documentary adequacy. It did not establish publication-length maturity.

No automatic expansion was performed.

## Open editorial decision — MECHDIAG

Before final release packaging, explicitly choose whether `ATLAS-CH-MECHDIAG-001` should:

1. remain intentionally concise;
2. be expanded editorially without strengthening its claims;
3. be presented together with adjacent diagnostic material;
4. receive another explicitly documented editorial treatment.

This is an editorial judgment boundary, not a mathematical defect.

## Copy-edit boundary

A raw whitespace scan finds trailing spaces in many chapter readers, but these overlap established Markdown hard-break formatting.

No mass whitespace rewrite was performed.

Final copy-edit must be rendering-aware; blind stripping is not authorized as a correctness repair.

## Citation/version state

`CITATION.cff` currently records:

- CFF 1.2.0;
- type: book;
- title: *A Mathematical Atlas of Adaptive Intelligence*;
- author: Grand Challenge Labs;
- repository identity;
- instruction to cite the specific tagged release or commit used.

Release version and release date are intentionally absent.

They must be bound to the exact protected release tag/commit during a future release-candidate transaction.

## Explicit governance gate — LICENSE_SELECTION_PENDING

Protected `LICENSE` blob remains:

`383ba0cadbeb21255aeb5124e946167c0771bf79`.

It states:

`LICENSE SELECTION PENDING`

and requires explicit license selection before public release of substantive manuscript content.

The assistant is not authorized to choose that license on behalf of the Human Steward.

This is the named governance boundary preventing the next release-promotion action.

## Release formats are not yet selected

Before final packaging, select the intended release format or formats, for example:

- Markdown/source bundle;
- PDF;
- HTML;
- EPUB;
- a deliberately scoped combination.

Rendered-format verification depends on this choice.

## Remaining requirements before public release

- [ ] Human Steward selects and records repository license;
- [ ] Human Steward/editorial decision on MECHDIAG treatment;
- [ ] release format(s) selected;
- [ ] rendering-aware whole-corpus copy-edit;
- [ ] release version/tag chosen;
- [ ] `CITATION.cff` version/date bound to exact release identity;
- [ ] final artifact(s) generated from the ledger-driven assembly;
- [ ] rendered links, figures, equations, references, and typography verified;
- [ ] exact artifact hashes and release manifest produced;
- [ ] release-candidate audit completed;
- [ ] explicit public-release authorization.

## Next transaction after Human Steward decisions

Instantiate `RELEASE-CANDIDATE-001` from exact protected main:

`2d09774f0f29dc9c47e48fdfb410a3725def669a`.

The transaction should:

1. apply the selected license;
2. implement the selected MECHDIAG editorial treatment;
3. bind release format(s);
4. perform rendering-aware copy-edit;
5. choose and bind version/tag/date metadata;
6. generate final rendered artifacts from the deterministic 80-chapter assembly;
7. verify rendered output;
8. generate exact artifact hashes and release manifest;
9. run exact-head repository validation;
10. undergo a fresh release-candidate audit;
11. stop before public release unless explicit public-release authorization is present.

## Legitimate stopping boundary

**Boundary name: HUMAN_STEWARD_RELEASE_GOVERNANCE.**

The bounded RELEASE-READINESS-001 transaction is complete.

The next release-promotion transaction is blocked until the Human Steward makes the required license decision. Release format and MECHDIAG editorial treatment should be resolved at the same handoff if possible.
