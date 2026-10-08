# ATLAS RC2 — semantic alternative-text reconciliation

Programme: EDITORIAL-REVIEW-001 (#314), accessibility task #325.
Role: ACCESSIBILITY_IMPLEMENTER. Candidate source predecessor: PR #320 at 21712c24955cbcbff86f11b2eb929563dca7411b.
Disposition: 18/18 source-to-HTML semantic alt transportation mechanically verified; final accessibility acceptance remains open.

## Diagnosed defect

Canonical corrected-edition LaTeX contains 18 Pandoc image directives with detailed `alt={...}` descriptions of mathematics, components, quantities, and relationships. Existing `tools/release_add_alt.py` replaces these with the visible figure captions in embedded HTML. A count of 18 nonempty caption-derived alt attributes was therefore insufficient to check semantic accessibility. Historical v0.1.0 publishing scripts must not be silently changed.

## Corrected-edition repair

Add `tools/editorial_export_figure_alts.py`, separate from the historical release pipeline:

- Parse 18 LaTeX `\includegraphics[...alt={...}]{path}` fields with balanced TeX braces.
- Bind each stable figure ID, source semantic alt and actual source PNG by its SHA-256 binary hash, not ordinal or caption text.
- Decode 18 embedded HTML PNG byte streams, look up each digest, and replace caption-derived alt with the corresponding source description; keep all visible captions unchanged.
- Reject missing/duplicate images, unknown image content, short/invalid source descriptions, and incomplete coverage.
- Leave the historical release, masters, manifests, image bytes and citations unchanged.

Reproduction on a diagnostic HTML built from candidate RC2:

```sh
python tools/editorial_export_figure_alts.py
python tools/editorial_export_figure_alts.py --html /tmp/atlas-rc.html --write
python tools/editorial_export_figure_alts.py --html /tmp/atlas-rc.html --verify
python -m unittest discover -s tests -p test_atlas_semantic_alt.py -v
```

Prior steps assemble RC2, normalize the 18 image directives using `tools/release_tex_for_html.py`, and generate embedded standalone HTML with Pandoc. These legacy preparation steps remain separate. The actual corrected-edition HTML conversion was replayed with all 18/18 images carrying semantically specific source alt. The follow-up --verify passed on the same embedded PNG bytes.

## Checks and boundary

Five adversarial tests exercise all-figure coverage, correct exact-PNG mapping, wrong prior alt, duplicate image and missing image. Source-only validation is added to candidate PR CI; no 5MB HTML file is committed. This is **not** a WCAG/screen-reader, contrast, layout, reading-order or print-scale certification. Visual P2 issues and corrected MANIFOLD/PSPECTRUM figure checks continue through #323–#325. Role independence means separate evidenced agent work, not GitHub account inequality.
