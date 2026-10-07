# AUDIT-075 — LICENSE-SELECTION-001

## Disposition

**PASS — NO REPAIR**

LICENSE-SELECTION-001 correctly implements the Human Steward licensing decision and preserves the separate release-authorization boundary.

This audit is a repository-governance and provenance audit. It does not purport to replace jurisdiction-specific legal advice.

## Audited implementation

- implementation issue: #301
- implementation PR: #302
- protected baseline: `2d09774f0f29dc9c47e48fdfb410a3725def669a`
- exact validated implementation head: `c8e51e1e1b7dc682926e116f58c59931e1211f01`
- GitHub Actions run: `37611010380` — success
- protected implementation merge: `22203b61b2d2264b11d43472c5d5ab6e393b9d83`
- implementation merge tree has zero file differences from the exact validated head
- audit issue: #303
- audit branch: `audit/a303`

## 1. Human Steward decision

PASS.

Copyright holder:

**Grand Challenge Technologies Ltd.**

Selected repository policy:

- CC BY 4.0 for manuscript, exposition, documentation, figures, specifications, governance material, and other non-software publication material;
- MIT for executable code, scripts, validators, generators, workflows, computational tooling, and other software/tooling;
- file-specific notices take precedence;
- third-party material subject to separate rights is not relicensed;
- generated artifacts inherit the license applicable to their underlying source material.

## 2. Repository scope notice

PASS.

Protected root `LICENSE` blob:

`ab037f45624441002a3d0fae5aa746dce0a383c8`.

It records:

- `Copyright © 2026 Grand Challenge Technologies Ltd.`;
- CC BY 4.0 / `CC-BY-4.0` publication scope;
- MIT software/tooling scope;
- exact standard-text paths;
- file-specific precedence;
- third-party-rights exclusion;
- generated-artifact inheritance;
- no endorsement/certification implication.

`LICENSE SELECTION PENDING` is absent.

## 3. CC BY 4.0 standard text

PASS.

Pinned source:

- repository: `spdx/license-list-data`;
- commit: `31ba1a50e5397e00a304dbadc76531740e89ee48`;
- path: `text/CC-BY-4.0.txt`;
- source Git blob SHA-1: `13ca539f377dc705af32b8d2ce89262298ea2f06`.

Atlas path:

`LICENSES/CC-BY-4.0.txt`.

Protected Atlas Git blob SHA-1:

`13ca539f377dc705af32b8d2ce89262298ea2f06`.

Independent protected-state comparison confirms byte identity with the pinned SPDX text.

No CC license term is modified.

## 4. MIT standard text

PASS.

Pinned source template:

- repository: `spdx/license-list-data`;
- commit: `31ba1a50e5397e00a304dbadc76531740e89ee48`;
- path: `text/MIT.txt`;
- source template Git blob SHA-1: `d817195dad53ec992418c28ffca5fbd1cd86502a`.

Atlas path:

`LICENSES/MIT.txt`.

Protected Atlas Git blob SHA-1:

`a431eb26664c286c260aa831d9a57adf32d303f0`.

Independent comparison confirms that the Atlas text equals the pinned SPDX MIT template after exactly one standard template substitution:

`Copyright (c) <year> <copyright holders>`

becomes:

`Copyright (c) 2026 Grand Challenge Technologies Ltd.`

No other MIT license term changes.

## 5. Third-party and file-specific rights

PASS.

The root scope notice explicitly states that:

- explicit file-specific license notices control where present;
- quoted, reproduced, incorporated, data, code, figures, or other third-party material subject to separate rights is not relicensed;
- source/citation/provenance records remain relevant to rights determination.

The selected repository license therefore does not silently overwrite separately governed third-party rights.

## 6. Machine verification

PASS.

Protected `tools/check_release_readiness.py` blob:

`4fcb95944269cbd53aa0324f18826694bd81bab7`.

It now verifies:

- selected root-license scope markers;
- copyright holder;
- absence of pending-selection state;
- exact CC BY 4.0 Git blob identity;
- exact instantiated MIT Git blob identity;
- canonical chapter lifecycle and path boundaries;
- citation/tag semantics;
- explicit release authorization before substantive release artifacts may exist.

## 7. Release authorization remains separate

PASS.

No `governance/RELEASE_AUTHORIZATION.yaml` exists on protected main.

Protected release directory contains only:

- `releases/.gitkeep`;
- `releases/README.md`.

No substantive release artifact exists.

The release README explicitly states that license selection alone does not authorize public release.

The validator rejects substantive release artifacts unless governance state contains:

`public_release_authorized: true`.

Thus:

[
	ext{license selected}

otRightarrow
	ext{public release authorized}.
]

## 8. Lifecycle and certification boundaries

PASS.

Protected Chapter Ledger remains:

- 80 chapter nodes;
- 80 at `draft-v0.1`;
- 0 promoted by this transaction.

No publication-ready, final-copy, released, or mathematical-certification state is introduced.

The root license notice also denies any implication that licensing confers endorsement, validation, or mathematical certification.

## 9. Public documentation

PASS.

README now records the scoped CC BY 4.0 + MIT policy and the Grand Challenge Technologies Ltd. copyright holder.

It explicitly preserves a separate release-candidate/publication-promotion transaction.

`releases/README.md` likewise preserves:

- release version/tag binding;
- selected release format;
- rendering-aware validation;
- artifact hashing;
- release-candidate audit;
- explicit public-release authorization.

## 10. Durable provenance receipt

PASS.

Protected receipt:

`governance/tranches/LICENSE-SELECTION-001.md`

Git blob:

`6441c9696fdc3f798f1ca9e20c406b7318c37fb9`.

It records the Human Steward decision, pinned standard-text provenance, exact Atlas license identities, scope/precedence rules, machine verification, and remaining release gates.

## 11. Exact-head validation

PASS.

Exact implementation head:

`c8e51e1e1b7dc682926e116f58c59931e1211f01`.

GitHub Actions run:

`37611010380`.

Conclusion:

**success**.

The workflow passed:

1. canonical Atlas validation;
2. release-readiness and selected-license validation;
3. deterministic 80-chapter working assembly.

The protected merge is file-identical to that validated head.

## Remaining governance boundary

The licensing decision is discharged.

The remaining pre-release Human Steward/editorial choices are:

1. intended release format or formats;
2. editorial treatment of `ATLAS-CH-MECHDIAG-001`.

A later release-candidate transaction must additionally bind:

- release version/tag/date;
- rendering-aware copy-edit;
- rendered artifact validation;
- exact artifact hashes/manifest;
- release-candidate audit;
- explicit public-release authorization.

## Final disposition

**AUDIT-075: PASS — NO REPAIR**, subject only to repository validation on the exact audit-record head before audit merge.

Durable result:

**Grand Challenge Technologies Ltd. has selected scoped CC BY 4.0 licensing for Atlas publication material and MIT licensing for Atlas software/tooling; the standard license texts and provenance are locked, while release authorization remains independently governed.**
