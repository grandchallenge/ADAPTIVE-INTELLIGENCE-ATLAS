# ATLAS-CH-TOKENCOMP-001 — Transaction Receipt

## Identity

- chapter: ATLAS-CH-TOKENCOMP-001
- implementation issue: #285
- protected baseline: fdaa7ec148e607654c88dfabe710ebf95f628599
- branch: work/tokencomp-285

## Hard prerequisite

TOKEN-001:
- manuscript 07c1edd5103ff179bbb3727ede9c4e15f2ec949a
- source lock 616c92bb63ed33e5c5587b3fe4491ae21a0eba54
- AUDIT-052 7c279eef5c55ea026fe965e18f696b62adad624e

## Source decision

No new external academic source is added.

TOKEN-001 already supplies audited tokenizer mechanisms, probability-model code length, multilingual scope, and representation-interface boundaries. TOKENCOMP adds exact Atlas-owned fixed-width ID accounting, declared compute proxies, Pareto controls, and a canonical lossless interoperability theorem.

## Implementation artifacts

- specification 7910cfe70266e23eab3e2acbb67bbad1af9e9fe1
- derivation packet 8a00dabe255901309f29650c7e082201f632e45a
- computational witness ec40dea6e29b772962ff3aded130a6cbbcabdb14
- reader manuscript 59cd3d63baa653975b0398f1fbdb635b54667cc4
- source lock 2022fae0751eda9408e77de2e02c42c1e437601e
- Chapter Ledger 72654340f6943e41ccc7068d16997a015d2d5bb9
- Source Register cff81d8047f5a28f21afcc83ff8fb7dce9776543

## Exact trade-off witness

Canonical byte string:
- x = abababab
- 8 bytes
- 64 baseline bits

Tokenizer S:
- vocabulary size 2
- token count 8
- fixed-width ID width 1 bit
- fixed-width token-ID stream 8 bits
- pair proxy 64
- dense-vocabulary proxy 16

Tokenizer P:
- vocabulary size 8
- token count 4
- fixed-width ID width 3 bits
- fixed-width token-ID stream 12 bits
- pair proxy 16
- dense-vocabulary proxy 32

Therefore the shorter sequence improves the pair proxy while worsening both fixed-width ID length and the dense-vocabulary proxy. Neither tokenizer Pareto-dominates the other in the declared objective vector.

## Exact interoperability witness

Both witness tokenizers detokenize to the same canonical byte string.

Translation by decode-to-canonical-bytes then retokenize is lossless in both directions on the declared witness domain.

This preserves the byte string but not:
- token identities;
- token count;
- embeddings;
- probability models;
- downstream behavior;
- semantics beyond the declared byte identity.

Independent replay result:

TOKENCOMP_EXACT_WITNESS_OK

## Durable boundaries

- token count != description length;
- fixed-width ID length != probability-model code length;
- ID-stream length != complete compressor size;
- token length != compute;
- shorter sequence != lower cost under every compute model;
- lossless translation != token/embedding/model-behavior equivalence;
- canonical transport interface != universal tokenizer standard;
- finite corpus witness != multilingual or universal optimum;
- toy compute proxy != measured runtime.

## Validation gate

Merge requires exact-head canonical repository validation, independent witness replay, exact-head GitHub Actions success, and a fresh post-draft audit.
