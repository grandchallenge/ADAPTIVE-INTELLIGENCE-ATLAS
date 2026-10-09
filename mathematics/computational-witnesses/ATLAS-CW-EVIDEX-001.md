# ATLAS-CW-EVIDEX-001 — Source Identity and Replay Ambiguity

**Chapter:** ATLAS-CH-EVIDEX-001  
**Witness class:** exact finite provenance/replay computation

## Purpose

Show that identical returned evidence bytes do not determine which mutable source version produced them, while an exact source-version identity can remove that ambiguity in a finite candidate set.

## Candidate sources

All three source versions are presented under the same human pathname:

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

Version v3 bytes:

    a=1
    b=4

SHA-256:

    af3f00343ac49267cd0a4519d85ade7d6c3857725f45454b12dbf556cf224c2d

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

All of v1, v2 and v3 satisfy that pathname label.

Candidate source count:

    3

Replay outcomes:

- v1 -> result=5
- v2 -> result=6
- v3 -> result=5

Even assuming the declared deterministic procedure and exact candidate enumeration, the returned value only rules out v2. Two different versions (v1 and v3) remain output-consistent:

    output_consistent_candidates=2

The result bytes therefore do not uniquely determine the source version in this repaired finite construction.

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
    v3 = b"a=1\nb=4\n"
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
        sha256(v3): v3,
    }

    target_hash = sha256(v1)
    output_consistent = {h: src for h, src in candidates.items()
                         if compute(src) == returned}
    hash_consistent = {h: src for h, src in candidates.items()
                       if h == target_hash}

    assert len(candidates) == 3
    assert len(output_consistent) == 2
    assert set(output_consistent) == {sha256(v1), sha256(v3)}
    assert len(hash_consistent) == 1
    assert next(iter(hash_consistent.values())) == v1
    assert compute(v1) == compute(v3) == returned
    assert compute(v2) != returned

    print("v1_sha256=" + sha256(v1))
    print("v2_sha256=" + sha256(v2))
    print("v3_sha256=" + sha256(v3))
    print("returned_sha256=" + sha256(returned))
    print("pathname_candidates=" + str(len(candidates)))
    print("output_consistent_candidates=" + str(len(output_consistent)))
    print("hash_candidates=" + str(len(hash_consistent)))
    print("v1_replay=" + compute(v1).decode().strip())
    print("v2_replay=" + compute(v2).decode().strip())
    print("v3_replay=" + compute(v3).decode().strip())

Expected output:

    v1_sha256=b64a71cff6737624915d32f719c1c6957c60cfb0b286eb9d0b5d3741f26b1265
    v2_sha256=c572528f7b0e700de0fd7bf2f3b7144a68f671ee0ed4b9d47943d9b489fe9844
    v3_sha256=af3f00343ac49267cd0a4519d85ade7d6c3857725f45454b12dbf556cf224c2d
    returned_sha256=ccdc6ccf3d8b13ef2de8739e91bacbe75d8f29b5c5a4dba8da5ac49881617d2f
    pathname_candidates=3
    output_consistent_candidates=2
    hash_candidates=1
    v1_replay=result=5
    v2_replay=result=6
    v3_replay=result=5

## What the witness establishes

For this finite candidate set:

- a mutable/human pathname leaves three admissible source versions;
- matching the returned value after exact deterministic replay still leaves two versions, v1 and v3;
- the exact v1 content hash selects one asserted source version;
- replay of the selected version reproduces the returned value.

This does not independently verify the producer's source-use claim: the fingerprint is meaningful because the handoff explicitly declares and binds it. The result is exact relative to the candidate set and declared deterministic procedure.

This is an identity and replay-disambiguation result.

## Claim boundary

The witness does not establish that SHA-256 provides semantic authority, that all provenance problems reduce to content hashes, that replayed results are scientifically correct, or that a matching source hash is sufficient to reproduce computations whose environment or nondeterminism also matters.
