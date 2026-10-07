# ATLAS-CW-TOKENCOMP-001 — Exact Compression, Compute, and Interface Witness

**Chapter:** ATLAS-CH-TOKENCOMP-001

## W1. Canonical byte string

Use ASCII/UTF-8 byte string:

\[
x=\texttt{abababab}.
\]

It contains:

- 8 bytes;
- 64 baseline bits.

## W2. Tokenizer S

Vocabulary:

\[
V_S=\{a,b\}.
\]

Tokenization:

\[
\tau_S(x)=[a,b,a,b,a,b,a,b].
\]

Exact values:

- vocabulary size: 2;
- token count: 8;
- fixed-width ID bits: \(\lceil\log_2 2\rceil=1\);
- fixed-width token-ID stream: 8 bits;
- pair proxy: \(8^2=64\);
- dense-vocabulary proxy: \(8\cdot2=16\).

## W3. Tokenizer P

Vocabulary:

\[
V_P=\{a,b,ab,x,y,z,w,q\}.
\]

Tokenization:

\[
\tau_P(x)=[ab,ab,ab,ab].
\]

Exact values:

- vocabulary size: 8;
- token count: 4;
- fixed-width ID bits: \(\lceil\log_2 8\rceil=3\);
- fixed-width token-ID stream: 12 bits;
- pair proxy: \(4^2=16\);
- dense-vocabulary proxy: \(4\cdot8=32\).

## W4. Conflicting order

P has fewer tokens:

\[
4<8.
\]

P has smaller pair proxy:

\[
16<64.
\]

But P has a larger fixed-width ID stream:

\[
12>8.
\]

And P has a larger dense-vocabulary proxy:

\[
32>16.
\]

Therefore no one-dimensional "shorter is better" ordering survives the declared objective vector.

## W5. Toy baseline ratios

Relative to the 64-bit byte baseline:

\[
R_S=8/64=1/8,
\]

\[
R_P=12/64=3/16.
\]

These ratios count only token IDs under already-shared tokenizer specifications.

## W6. Exact canonical translation

Both tokenizers use concatenation as decoder on this declared witness domain.

Thus:

\[
\delta_S(\tau_S(x))=x,
\]

\[
\delta_P(\tau_P(x))=x.
\]

Define:

\[
T_{S\to P}=\tau_P\circ\delta_S.
\]

Then:

\[
T_{S\to P}(\tau_S(x))
=
\tau_P(x)
=
[ab,ab,ab,ab].
\]

Reverse translation:

\[
T_{P\to S}=\tau_S\circ\delta_P
\]

returns:

\[
[a,b,a,b,a,b,a,b].
\]

Both directions preserve the canonical byte string.

## W7. Token identity is not preserved

The S representation contains only tokens \(a,b\).

The P representation used for the witness contains token \(ab\).

Thus lossless canonical translation does not preserve token identities or sequence length.

## W8. Minimal replay code

    import math

    x = "abababab"
    baseline_bits = len(x.encode("utf-8")) * 8

    V_S = ("a", "b")
    s_S = ("a", "b", "a", "b", "a", "b", "a", "b")

    V_P = ("a", "b", "ab", "x", "y", "z", "w", "q")
    s_P = ("ab", "ab", "ab", "ab")

    def width(vocab):
        return math.ceil(math.log2(len(vocab)))

    def fixed_bits(vocab, tokens):
        return width(vocab) * len(tokens)

    def pair_proxy(tokens):
        return len(tokens) ** 2

    def vocab_proxy(vocab, tokens):
        return len(tokens) * len(vocab)

    D_S = fixed_bits(V_S, s_S)
    D_P = fixed_bits(V_P, s_P)

    assert baseline_bits == 64
    assert len(s_S) == 8
    assert len(s_P) == 4
    assert width(V_S) == 1
    assert width(V_P) == 3
    assert D_S == 8
    assert D_P == 12
    assert pair_proxy(s_S) == 64
    assert pair_proxy(s_P) == 16
    assert vocab_proxy(V_S, s_S) == 16
    assert vocab_proxy(V_P, s_P) == 32

    assert len(s_P) < len(s_S)
    assert pair_proxy(s_P) < pair_proxy(s_S)
    assert D_P > D_S
    assert vocab_proxy(V_P, s_P) > vocab_proxy(V_S, s_S)

    def decode(tokens):
        return "".join(tokens)

    def tok_S(text):
        assert set(text) <= {"a", "b"}
        return tuple(text)

    def tok_P(text):
        assert text == x
        return ("ab",) * 4

    assert decode(s_S) == x
    assert decode(s_P) == x
    assert tok_P(decode(s_S)) == s_P
    assert tok_S(decode(s_P)) == s_S

    print("TOKENCOMP_EXACT_WITNESS_OK")

Expected output:

    TOKENCOMP_EXACT_WITNESS_OK

## Claim boundary

This witness proves only the declared fixed-width ID accounting, toy compute proxies, and canonical-string translation. It excludes tokenizer-specification transmission cost, entropy coding, real model FLOPs, measured runtime, special-token transport, semantics, downstream quality, and multilingual generalization.
