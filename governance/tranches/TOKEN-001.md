# TOKEN-001 Transaction Receipt

Stable chapter ID: ATLAS-CH-TOKEN-001  
Issue: #207  
Baseline: b4e3d2e12841a2185bd66c04b0ef79244922fbbd  
Work branch: work/token-207  
Source-lock checkpoint: a5a70df71b6287b21f34819ed95a26513aca1389

## Prerequisite binds

Information:
- manuscript: 0fca10cbc7476c5b729ee15dfad0dec563665821
- source lock: ea5a1b0db3aadf052fc0b749d7e813bb0ca5d43c
- AUDIT-004: 948f76b3f86d27fa4830efc30d8ef0135134256e

Representations:
- manuscript: 6109e6ac9505a339cb8bc2dd85a8b9bc882f72bb
- source lock: dfe9176c458a56ca5cda5f258c440aea52f9b9fa
- AUDIT-004: 948f76b3f86d27fa4830efc30d8ef0135134256e

## Implementation artifact identities

- specification: f87dce93093efe26e2483195f294e98c7016adf6
- manuscript: 07c1edd5103ff179bbb3727ede9c4e15f2ec949a
- derivation: 0161b85fda989ac828ff968b6edb44ad4c4f7fa4
- witness: f8004ba6abf348a001fbdb918bfaac3bb1452e21
- source lock: 616c92bb63ed33e5c5587b3fe4491ae21a0eba54
- Chapter Ledger: 0f7f83a0dc5664fecec910c6c4210e271153a206
- Source Register: ae57731f36bc10b9c0c718b06b800e7fbc0e00cc
- bibliography: d162e7ba05c510a6d1580bbfec714141d9325f62

## Exact witnesses

- NFC `é`: 1 codepoint, 2 UTF-8 bytes;
- decomposed `e` + combining acute: 2 codepoints, 3 UTF-8 bytes;
- unigram segmentation probabilities for `abab`: `(64/81, 8/81, 8/81, 1/81)`;
- two-token declared code length: 8 bits; three-token declared code length: 3 bits;
- toy fertility: 2.5 versus 1.0.

## Durable boundaries

- byte != codepoint != grapheme != subword != token ID != embedding;
- token count != entropy or description length;
- BPE != unigram segmentation;
- vocabulary != complete tokenizer procedure;
- fertility != language complexity;
- morphology alignment != model-quality theorem;
- multilingual tokenizer adequacy is multi-factor and corpus-scoped.

## Completion rule

Implementation merge requires exact-head canonical validation. A fresh post-draft audit must recheck prerequisite identities, source scope, all finite witnesses, fertility/morphology/multilingual boundaries, reader maturity, provenance, and TOKENCOMP handoff before transaction completion.
