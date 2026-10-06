# COMPINTEL-001 — Transaction Receipt

## Identity
- chapter: ATLAS-CH-COMPINTEL-001
- implementation issue: #227
- protected baseline: 21597e4f2bb7af5312dc9967417a60dc3d8dc0f5
- branch: work/compintel-227

## Hard prerequisites
COMPRESS-001:
- manuscript e8db79df51b64cfd4d5ef6957d4d10313886b6f4
- source lock 156cd6afe1a06b49d2761b54d32b586fe5d23cec
- AUDIT-042 677efa90a2d606c0400b8e471465278d19857393

RESIDUAL-001:
- manuscript 02b0886a87e1e17c749e15349e14f43674c3d1ff
- source lock 6e6a25c4b4e01475e68a6c616eefb6ba7b039341
- AUDIT-006 b24ef782bedfe76a4c52d832562a0dd29d2a64a9

## Implementation artifacts
- specification f3143c5b63537696e327f15aa1ef041f3f075482
- derivations a05602c16c82587170c5b57e44cc4c5033d89bac
- witness fb6f398987666794ba7520d2045982421b6f58c6
- manuscript e6396abb339b8ccc14d1cb54b9c89eb982937d1e
- source lock fbd6948afb38648697f0173aa25fbbe6a32b76ba
- Chapter Ledger 7d6e77ecd71ed76c1141a2fe39349e5dcdef8490
- Source Register 7b17cc17785312012761626688bac44238c67af3
- bibliography db440c3ea184780c4eb669609887dcc9ef6fac62

## Durable substrate
- codelength is code-relative;
- held-out codelength is stronger evidence than training fit;
- Delta_C compares held-out codelength against a declared baseline;
- Gamma_t measures longitudinal held-out codelength progress under fixed semantics;
- codec, random-label, shuffle, random-representation, memorization, capacity, task-distortion, and recoding controls are mandatory;
- economical recoverability is distinct from causal use;
- codelength ranking is distinct from the Residual factorization preorder;
- compression is not promoted to a definition of intelligence.

## Exact witness
For T=(0,1,0,1), the declared period-two conditional code gives:
- H=(0,1,0,1): 1 bit versus 4-bit literal baseline, gain +3;
- H=(0,0,1,1): 5 bits versus 4-bit literal baseline, gain -1.

For eight zeros, the declared run code gives 1 bit versus 8-bit literal baseline, gain +7; this is a trivial-compressibility control, not an intelligence result.

## Validation gate
Merge requires exact-head canonical validation, exact witness replay, exact-head GitHub Actions success, and a fresh post-draft audit.
