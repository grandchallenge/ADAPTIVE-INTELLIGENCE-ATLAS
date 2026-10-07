# LICENSE-SELECTION-001 — Repository Licensing Receipt

## Human Steward decision

Copyright holder:

**Grand Challenge Technologies Ltd.**

Selected repository licensing:

- **CC BY 4.0** for manuscript, chapter text, mathematical exposition, specifications, governance/documentation, diagrams, figures, and other non-software publication material;
- **MIT** for executable source code, scripts, validators, generators, computational tooling, workflow code, and other software/tooling;
- explicit file-specific notices take precedence;
- third-party and incorporated material subject to separate rights is not relicensed by the repository notice;
- generated build artifacts inherit the license applicable to their underlying source material.

## Protected baseline

- repository: `grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS`
- baseline protected main: `2d09774f0f29dc9c47e48fdfb410a3725def669a`
- implementation issue: #301
- implementation branch: `work/license-301`

## Canonical standard-text provenance

Source repository:

`spdx/license-list-data@31ba1a50e5397e00a304dbadc76531740e89ee48`

SPDX license-list build:

`3.29.0`

CC BY 4.0 source:

- path: `text/CC-BY-4.0.txt`
- source Git blob SHA-1: `13ca539f377dc705af32b8d2ce89262298ea2f06`
- Atlas path: `LICENSES/CC-BY-4.0.txt`
- Atlas Git blob SHA-1: `13ca539f377dc705af32b8d2ce89262298ea2f06`

The CC BY 4.0 text is byte-identical to the pinned SPDX canonical text.

MIT source template:

- path: `text/MIT.txt`
- source template Git blob SHA-1: `d817195dad53ec992418c28ffca5fbd1cd86502a`
- Atlas path: `LICENSES/MIT.txt`
- Atlas Git blob SHA-1 after standard copyright instantiation: `a431eb26664c286c260aa831d9a57adf32d303f0`

The only template substitution is:

`Copyright (c) <year> <copyright holders>`

to:

`Copyright (c) 2026 Grand Challenge Technologies Ltd.`

No other MIT license term is changed.

## Repository scope notice

The root `LICENSE` is a repository scope/precedence notice, not a rewritten substitute for either standard license.

It records:

- copyright © 2026 Grand Challenge Technologies Ltd.;
- CC-BY-4.0 scope;
- MIT scope;
- file-specific precedence;
- third-party-rights exclusion;
- generated-artifact inheritance;
- no endorsement/certification implication.

## Machine verification

`tools/check_release_readiness.py` now verifies:

- root license scope markers;
- absence of `LICENSE SELECTION PENDING`;
- exact CC BY 4.0 Git blob identity;
- exact instantiated MIT Git blob identity;
- canonical chapter lifecycle/readiness controls;
- citation/tag semantics;
- absence of substantive release artifacts unless explicit release authorization exists.

## Release authorization remains separate

This transaction discharges the **license-selection** gate only.

It does not:

- create a release candidate;
- create a substantive file under `releases/`;
- grant publication-ready or final-copy status;
- promote any chapter beyond `draft-v0.1`;
- authorize public release;
- certify any mathematical claim.

Substantive release artifacts remain prohibited unless:

`governance/RELEASE_AUTHORIZATION.yaml`

exists and records:

`public_release_authorized: true`.

## Remaining pre-release decisions

Still unresolved:

1. editorial treatment of `ATLAS-CH-MECHDIAG-001`;
2. intended release format or formats;
3. rendering-aware whole-corpus copy-edit;
4. release version/tag/date;
5. final rendered artifact generation and validation;
6. exact release artifact hashes and manifest;
7. release-candidate audit;
8. explicit public-release authorization.
