# CURRENT HANDOFF — Adaptive Intelligence Atlas

**Date:** 2026-10-07
**Recovery authority:** `governance/ACTIVE_TRANSACTION.yaml` on `state/atlas-controller`
**Current protected main:** `ab781fbf7861c36b7750a0ba2710a34ade625122`

## Restart rule

1. Read `governance/ACTIVE_TRANSACTION.yaml` first.
2. Read this handoff.
3. Fetch live `main`.
4. If live `main` differs from the recorded baseline, recompute release-configuration state.
5. Repository state overrides chat history.

## Current state

- controller state: `blocked-human-governance`;
- architecture drafting: complete;
- global synthesis: complete and audited;
- release readiness: complete and audited;
- repository rights selection: complete and audited;
- Chapter Ledger: 80/80 chapters remain `draft-v0.1`;
- release candidate: not yet instantiated;
- public release: not authorized.

## Completed rights-selection transaction

Implementation:

- issue #301 — closed completed;
- PR #302 — merged;
- exact validated head: `c8e51e1e1b7dc682926e116f58c59931e1211f01`;
- Actions run: `37611010380` — success;
- implementation merge: `22203b61b2d2264b11d43472c5d5ab6e393b9d83`.

Fresh audit:

- `AUDIT-075`;
- issue #303 — closed completed;
- PR #304 — merged;
- exact validated audit head: `907ecda1aea6c1544726490abff2f7a2cb69a0f4`;
- Actions run: `37611629107` — success;
- final protected merge: `ab781fbf7861c36b7750a0ba2710a34ade625122`;
- disposition: **PASS — NO REPAIR**.

Authoritative repository artifacts:

- `LICENSE`;
- `LICENSES/`;
- `governance/tranches/LICENSE-SELECTION-001.md`;
- `reviews/AUDIT-075.md`;
- `tools/check_release_readiness.py`.

These artifacts contain the exact Human Steward selection, copyright-holder identity, standard-text provenance, scope rules, and machine verification. Do not reconstruct those details from chat.

## Release authorization remains separate

The completed selection transaction does not create a release candidate or authorize publication.

Protected main contains no `governance/RELEASE_AUTHORIZATION.yaml` and no substantive release artifact.

## Release artifact hierarchy

Human Steward selection:

- **LaTeX** is the canonical source of truth for the release.
- **PDF** is the primary presentation artifact.
- **HTML** is the broader-accessibility artifact.

PDF and HTML must be generated from the exact canonical LaTeX release source and bound to the same protected release identity. Neither rendered artifact may become an independent editorial source of truth.

## Remaining Human Steward decision

One decision remains before `RELEASE-CANDIDATE-001`:

- choose the editorial treatment for `ATLAS-CH-MECHDIAG-001`.

MECHDIAG is approximately 236 words. `AUDIT-047` states that the concise reader is protocol-complete and binds the mature reader companion as part of the chapter packet. Global synthesis later made that audited companion the canonical reader.

Current recommendation, not yet a Human Steward decision:

- keep the audited content concise;
- typeset it in LaTeX as an intentional short interlude/bridge chapter;
- do not pad it merely to match neighboring chapter lengths;
- preserve its separate chapter identity and downstream handoff to `ATLAS-CH-SPECTRALDIAG-001`.

## Next transaction

After those two decisions, instantiate `RELEASE-CANDIDATE-001` from:

`ab781fbf7861c36b7750a0ba2710a34ade625122`.

Then:

1. construct the canonical LaTeX release source from the deterministic 80-chapter assembly;
2. implement the selected MECHDIAG treatment;
3. perform rendering-aware copy-edit in the LaTeX source of truth;
4. bind version/tag/date and citation metadata;
5. generate PDF and HTML from that exact LaTeX release source;
6. validate links, figures, equations, references, typography, and cross-format consistency;
7. generate exact hashes for the LaTeX source bundle, PDF, HTML artifact set, and release manifest;
8. run exact-head validation;
9. perform a fresh release-candidate audit;
10. stop before public release unless explicit public-release authorization is recorded.

## Legitimate stopping boundary

**Boundary name: HUMAN_STEWARD_RELEASE_CONFIGURATION.**
