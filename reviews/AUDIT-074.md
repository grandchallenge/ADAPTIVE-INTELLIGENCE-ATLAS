# AUDIT-074 — RELEASE-READINESS-001

## Disposition

**PASS WITH ONE TOOL-CONTRACT REPAIR**

RELEASE-READINESS-001 passes its mandatory fresh post-merge audit after one bounded repair to the working-assembly command-line contract.

No mathematical, lifecycle, citation, provenance, license, release-promotion, or publication-status defect requiring further repair was found.

No chapter is promoted beyond `draft-v0.1`. No public release, license grant, publication-ready status, final-copy status, or mathematical certification is created by this audit.

## Audited implementation

- implementation issue: #297
- implementation PR: #298
- protected baseline: `e22d9d383d048626797d7865bc7e9d3daebe1887`
- exact validated implementation head: `1dbf6f1d24a24566503ca478c06007dfd13d0649`
- GitHub Actions run: `37608881886` — success
- protected implementation merge: `b0d6034a76dac0e2444fd24b37bd381790995619`
- implementation merge tree has zero file differences from the exact validated head
- audit issue: #299
- audit branch: `audit/a299`
- bounded audit repair commit: `b53aeb88d826a5a04b2b1052ad2524bbe8bc8294`

## 1. Canonical release corpus

PASS.

The protected Chapter Ledger remains:

- 80 chapter nodes;
- 80 at `draft-v0.1`;
- 0 promoted beyond `draft-v0.1`;
- 80 unique canonical manuscript paths.

Canonical release membership is taken from `governance/CHAPTER_LEDGER.yaml`, not filesystem enumeration.

The two additional Markdown files under `manuscript/parts/` are preserved MECHDIAG historical/companion readers:

- `manuscript/parts/12-diagnostics-robustness-compression/_probe.md`;
- `manuscript/parts/12-diagnostics-robustness-compression/ATLAS-CH-DIAGREAD-001.md`.

They are not selected by the canonical assembly.

## 2. Deterministic working assembly

PASS AFTER REPAIR.

`tools/assemble_manuscript.py`:

- reads chapter membership and order from the Chapter Ledger;
- rejects missing or duplicate canonical reader paths;
- rejects canonical reader paths outside `manuscript/parts/`;
- emits exactly one assembly marker per canonical chapter;
- produces a machine-readable manifest containing stable chapter ID, Part ID, lifecycle state, path, and Git blob identity;
- records the source commit;
- labels the result as a non-promotional working assembly.

Positive replay on audit repair head `b53aeb88d826a5a04b2b1052ad2524bbe8bc8294` assembled exactly 80 canonical chapters.

## 3. Audit repair — `--check` contract

The implementation exposed one bounded tool-contract inconsistency.

The CLI declared:

`--check`

with help text saying that check mode writes only to explicitly supplied paths, but the implementation did not enforce explicit `--output` and `--manifest` arguments.

The CI invocation was already safe because it supplied explicit `/tmp` paths, so this was not an artifact-promotion or repository-mutation failure. It was nevertheless a false command-line contract.

### Repair

Audit commit `b53aeb88d826a5a04b2b1052ad2524bbe8bc8294` makes `--output` and `--manifest` optional at parse time and enforces:

- ordinary mode: defaults to `build/atlas-manuscript.md` and `build/atlas-manifest.json`;
- `--check` mode: both paths must be explicitly supplied.

Negative replay:

`python tools/assemble_manuscript.py --check`

now exits 1 with:

`--check requires explicit --output and --manifest paths`.

Positive replay with explicit temporary paths succeeds and assembles all 80 canonical chapters.

Disposition: repaired.

## 4. Release-readiness boundary checker

PASS.

`tools/check_release_readiness.py` independently enforces:

- exactly 80 canonical chapters;
- all remain `draft-v0.1`;
- canonical manuscript paths are unique, existing, and under `manuscript/parts/`;
- only the two named MECHDIAG companion files may remain outside ledger selection;
- `CITATION.cff` retains required book and commit/tag citation metadata;
- `LICENSE_SELECTION_PENDING` remains explicit;
- no substantive release artifact is committed under `releases/` while the license gate is active.

Protected implementation checker blob:

`338269c473a428e1c108d8370532421d7b09596a`.

## 5. License governance gate

PASS.

Protected license blob:

`383ba0cadbeb21255aeb5124e946167c0771bf79`.

It states:

`LICENSE SELECTION PENDING`

and requires explicit license selection before public release of substantive manuscript content.

RELEASE-READINESS-001 does not modify the license.

The readiness checker treats loss of that gate, before a separately governed release-promotion transaction, as an error.

## 6. Release-directory gate

PASS.

`releases/README.md` explicitly records that public release is unauthorized while the license remains pending.

The checker rejects substantive files in `releases/` while that gate is active.

No substantive release artifact is introduced by RELEASE-READINESS-001.

## 7. Build workspace semantics

PASS.

`build/README.md` records:

- build outputs are generated working artifacts;
- canonical membership/order comes from the Chapter Ledger;
- generated output does not change chapter lifecycle state;
- generated output does not imply release authorization or mathematical certification.

The tranche does not commit a generated manuscript bundle as a release artifact.

## 8. Citation/version readiness

PASS WITH DEFERRED RELEASE METADATA.

Protected `CITATION.cff` remains:

- CFF 1.2.0;
- type `book`;
- title `A Mathematical Atlas of Adaptive Intelligence`;
- author `Grand Challenge Labs`;
- repository identity;
- instruction to cite the specific tagged release or commit used.

No release version or release date is invented.

Those values must be bound to the exact protected release tag/commit in a later promotion transaction.

## 9. README phase semantics

PASS.

README now records:

- full first-draft corpus;
- release-readiness phase;
- 14 Parts;
- 80 stable chapter identities;
- 80/80 at `draft-v0.1`;
- global synthesis completed and independently audited;
- working assembly is non-promotional;
- public release remains blocked pending explicit Human Steward license selection.

No publication-ready or final-copy claim is made.

## 10. CI coverage

PASS.

The workflow is now named:

`Validate Atlas repository`.

Exact implementation head `1dbf6f1d24a24566503ca478c06007dfd13d0649` passed GitHub Actions run `37608881886`.

The workflow executes:

1. `python tools/validate_atlas.py`;
2. `python tools/check_release_readiness.py`;
3. `python tools/assemble_manuscript.py --output /tmp/atlas-manuscript.md --manifest /tmp/atlas-manifest.json --check`.

Thus CI exercises the actual assembly path without retaining a release artifact.

## 11. Editorial maturity warning

PASS AS EXPLICIT OPEN EDITORIAL ITEM.

The release-readiness scan reports approximately 199,638 words across the 80 canonical readers.

One material short-reader outlier remains:

- `ATLAS-CH-MECHDIAG-001`: approximately 236 words.

AUDIT-047 previously established its technical/documentary adequacy for the bounded chapter claim.

That does not establish publication-length maturity.

RELEASE-READINESS-001 correctly leaves the matter for explicit editorial adjudication instead of silently expanding claims or prose.

## 12. Copy-edit whitespace boundary

PASS.

A raw whitespace scan reports trailing spaces in many chapter readers, but this overlaps the established Markdown hard-break convention in metadata/status lines.

No mass whitespace rewrite is performed.

Any final copy-edit normalization must be rendering-aware.

## 13. Canonical Atlas validation after repair

PASS.

Linux replay on audit repair head reports:

`OK: 80 chapters, 126 hard edges, 1 root(s), 0 specification-ready keystones, 80 draft chapters, 18 rendered witnesses, 18 registered figures, 85 sources, 175 bibliography keys`.

Release-readiness replay reports:

`OK: release-readiness boundary intact; 80 canonical chapters, 2 preserved non-ledger companions, 199638 approximate words; LICENSE_SELECTION_PENDING blocks public release`.

The MECHDIAG length item is emitted as a warning, not a lifecycle mutation.

## 14. Remaining release-candidate requirements

The following remain open and are not silently discharged by this audit:

- Human Steward selects and records the repository license;
- editorial adjudication of MECHDIAG publication maturity;
- rendering-aware whole-corpus copy-edit;
- chosen release format or formats;
- release version/tag;
- `CITATION.cff` version/date bound to exact release identity;
- final rendered artifact generation;
- rendered-format verification of links, figures, equations, references, and typography;
- exact artifact hashes/release manifest;
- release-candidate audit;
- explicit public-release authorization.

## Promotion boundary

This audit does not authorize:

- license selection;
- release-candidate promotion;
- public release;
- publication-ready status;
- final-copy status;
- theorem certification;
- chapter promotion beyond `draft-v0.1`.

## Final disposition

**AUDIT-074: PASS WITH ONE TOOL-CONTRACT REPAIR**, subject only to full repository validation on the exact audit-record head before audit merge.

The durable result is:

**The Atlas now has a deterministic, ledger-driven 80-chapter working-build path and machine-enforced release gates. The repository is prepared for release-candidate work, but release promotion remains blocked by explicit Human Steward license selection and the remaining editorial/rendering requirements.**
