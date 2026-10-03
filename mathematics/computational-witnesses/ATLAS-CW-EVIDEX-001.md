# ATLAS-CW-EVIDEX-001 — Source Identity and Replay Ambiguity

**Chapter:** ATLAS-CH-EVIDEX-001  
**Witness class:** exact finite provenance/replay computation

## Purpose

Show that identical returned evidence bytes do not determine which mutable source version produced them, while an exact source-version identity can remove that ambiguity in a finite candidate set.

## Candidate sources

Both source versions are presented under the same human pathname:

inputs.txt

Version v1 bytes:

    a=2
    b=3

SHA-256:

    b64a71cff6737624915d32f719c1c6957c60cfb0b286eb9d0b5d3741f26b1265

Version v2 bytes:

    a=2
    b=4

SHA-256:

    c572528f7b0e700de0fd7bf2f3b7144a68f671ee0ed4b9d47943d9b489fe9844

## Declared procedure

Parse integers a and b and return:

    result=a+b

## Returned evidence bytes

    result=5

SHA-256:

    ccdc6ccf3d8b13ef2de8739e91bacbe75d8f29b5c5a4dba8da5ac49881617d2f

The evidence payload is held fixed in both handoff cases.

## Handoff A — pathname only

Provenance field:

    source_path=inputs.txt

Both v1 and v2 satisfy that pathname label.

Candidate source count:

    2

Replay outcomes:

- v1 -> result=5
- v2 -> result=6

Therefore the returned bytes do not uniquely determine the source version.

## Handoff B — pathname plus exact source hash

Provenance fields:

    source_path=inputs.txt
    source_sha256=b64a71cff6737624915d32f719c1c6957c60cfb0b286eb9d0b5d3741f26b1265

Exactly one candidate matches.

Candidate source count:

    1

Replay outcome:

    result=5

Thus exact source-version identity removes the finite ambiguity in this witness.

## Replay procedure

    import hashlib

    v1 = b"a=2\nb=3\n"
    v2 = b"a=2\nb=4\n"
    returned = b"result=5\n"

    def sha256(x):
        return hashlib.sha256(x).hexdigest()

    def compute(src):
        values = {}
        for line in src.decode().strip().splitlines():
            k, v = line.split("=")
            values[k] = int(v)
        return f"result={values['a'] + values['b']}\n".encode()

    candidates = {
        sha256(v1): v1,
        sha256(v2): v2,
    }

    target_hash = sha256(v1)

    print("v1_sha256=" + sha256(v1))
    print("v2_sha256=" + sha256(v2))
    print("returned_sha256=" + sha256(returned))
    print("pathname_candidates=" + str(len(candidates)))
    print("hash_candidates=" + str(sum(h == target_hash for h in candidates)))
    print("v1_replay=" + compute(v1).decode().strip())
    print("v2_replay=" + compute(v2).decode().strip())

Expected output:

    v1_sha256=b64a71cff6737624915d32f719c1c6957c60cfb0b286eb9d0b5d3741f26b1265
    v2_sha256=c572528f7b0e700de0fd7bf2f3b7144a68f671ee0ed4b9d47943d9b489fe9844
    returned_sha256=ccdc6ccf3d8b13ef2de8739e91bacbe75d8f29b5c5a4dba8da5ac49881617d2f
    pathname_candidates=2
    hash_candidates=1
    v1_replay=result=5
    v2_replay=result=6

## What the witness establishes

For this finite candidate set:

- a mutable/human pathname alone leaves two admissible source versions;
- the exact v1 content hash selects one source version;
- replay of that selected source reproduces the returned value.

This is an identity and replay-disambiguation result.

## Claim boundary

The witness does not establish that SHA-256 provides semantic authority, that all provenance problems reduce to content hashes, that replayed results are scientifically correct, or that a matching source hash is sufficient to reproduce computations whose environment or nondeterminism also matters.
