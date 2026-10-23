# ATLAS-CH-SYNTHESIS-001 — Transaction Receipt

## Identity
- chapter: ATLAS-CH-SYNTHESIS-001
- implementation issue: #276
- protected baseline: 4c038e50f91e152e8139fc0dd412587d02f620fb
- branch: work/synthesis-276

## Hard prerequisites
FRONTIER-001:
- reader e1a692a7e6406041a6e4395c0e23a0732fb5b4e3
- source lock 84b4b3f80a5daf5a557b29c1f0ea0f7991c7dd63
- AUDIT-043 4ea9811d0e9c184b2e1aa223091332e356c77056

POLITY-001:
- manuscript fa1cb3dad381ddbcbd7e4725a87ce42c77a03948
- source lock ee898fbbafc58a4f6322a7c65ef571c9a084bc35
- AUDIT-048 8b04e42fecca8a361c929dc68ead4441a4f592cd

## Source decision
No new external academic source added. New systems witness is Atlas-owned exact finite logic over audited prerequisites.

## Implementation artifacts
- specification b654fade91567c1a2d940c766bf75e0729b7a504
- derivations f2b0fed22d025ba33c3e10e61cd61887da7d9452
- witness e9ffd717f2568259aca8fdc3bd3913d11fb814ec
- manuscript 1196cd0495bda0cc63515dbc46c127577c937f2e
- source lock 32f4c6b53797bbbd9ae3b9694b5f68d246ef0f3a
- Chapter Ledger 112d7e3ecc4ce9e1e6ba1c033c05ad98f8d8b65a
- Source Register 36b5c66c314f7f792e9053dfd6d9016573b70acd

## Notation regression correction: issue #280 (current candidate)

The identities in **Implementation artifacts** above describe the original historical implementation; preserve them for provenance. The current correction restores the damaged mathematical display on the then-protected baseline `49d576a4b89ab671fdb6d8e6b3d49cfe05146294` by comparing it with the already-merged historical source repair [PR #360](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/pull/360), merge `a810c4b5f8e9803a54fcfeab434212e62622f2b3`.

- historical damaged derivation blob: `f2b0fed22d025ba33c3e10e61cd61887da7d9452`;
- current corrected derivation blob: `aecd9fcd8f4a208e2517326ad773f8418d0ab5cf`;
- historical damaged computational-witness blob: `e9ffd717f2568259aca8fdc3bd3913d11fb814ec`;
- current corrected computational-witness blob: `0541ab6dfb65eeb86b43f7b0e38d46810321a8b2`;
- **Renderer replay:** 33 derivation and four witness display blocks round-trip through Arithmatex HTML with no leaked delimiters; all 37 source formulas compile under `pdflatex` (`amsmath,amssymb`) into formula-only PDF SHA-256 `0f2ce7eb979513b026af9ebf814100d4404e9db3a85ede647e71ca4769f76628`. This is source-document proof, **not** inspection of the whole published Atlas PDF or HTML. The PDF replay exposed and fixed four internal paragraph breaks and one unescaped `validator\_accept` identifier.
- correction preserves the original Python witness source and its claim boundary; it restores paired display mathematics and legible source/task notation and corrects `V(c_{\\mathrm{bad}})`.
- original manuscript, computational model, seven-category status grammar and source locks remain unaffected.

The candidate remains subject to fresh repository validation, independent witness replay, review and protected-main readback. A successful typesetting repair does not constitute an Atlas-wide chapter acceptance or mathematical certification.

## Full witness
- task accuracy 2/2
- validated commit coverage 2/2
- persistent recall coverage 2/2
- unauthorized commits 0

## Ablations
- broken router -> task and commit coverage 1/2
- validator removed with governance unchanged -> transient answers 2/2, authorized commits 0/2
- memory removed -> persistent recall 0/2
- governance bypass -> rejected bad-source candidate can be written

## Status grammar preserved
AUDIT_BOUND_SUBSTRATE; DRAFT_SUBSTRATE; BOUNDED_EVIDENCE; ARCHITECTURE_STAGE; OPEN_PROOF_OBLIGATION; OPEN_EXPERIMENT_OBLIGATION; CONJECTURAL_CONNECTION.

## Durable boundaries
Component count does not imply composition quality; answer capability does not imply authorized durable state; evidence does not imply authority; memory persistence does not imply truth; adaptation does not imply permission; distributed does not imply superior; open FRONTIER obligations remain open.

## Validation gate
Merge requires exact-head canonical repository validation, independent exact witness replay, exact-head GitHub Actions success, and a fresh post-draft audit.
