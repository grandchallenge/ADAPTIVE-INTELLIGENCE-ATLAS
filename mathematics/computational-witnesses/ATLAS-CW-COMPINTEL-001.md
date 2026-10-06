# ATLAS-CW-COMPINTEL-001 — Compression Probe Witness

**Chapter:** ATLAS-CH-COMPINTEL-001  
**Purpose:** exact replay of held-out codelength gain, matched failure control, and trivial-compressibility non-implication.

## W1. Held-out period-two probe

Training prefix:

\[
T=(0,1,0,1).
\]

Held-out structured continuation:

\[
H_s=(0,1,0,1).
\]

Matched held-out control:

\[
H_c=(0,0,1,1).
\]

The training prefix is identical in both cases.

## W2. Conditional prefix code

The decoder knows \(T\).

The code for a four-bit held-out sequence is:

- one-bit word \(1\): continue the period-two motif inferred from \(T\);
- five-bit word \(0b_1b_2b_3b_4\): literal fallback.

This code is prefix-free because the special word begins with \(1\), while every literal word begins with \(0\).

## W3. Structured held-out codelength

The inferred motif is

\[
(0,1).
\]

The structured continuation is exactly the next four motif bits.

Therefore

\[
\boxed{
L_C(H_s\mid T)=1.
}
\]

A fixed literal baseline requires

\[
L_0(H_s)=4.
\]

Hence

\[
\boxed{
\Delta_C(H_s)=4-1=3.
}
\]

## W4. Matched control codelength

The control sequence

\[
H_c=(0,0,1,1)
\]

does not continue the period-two motif.

Therefore the codec uses the literal fallback:

\[
\boxed{
L_C(H_c\mid T)=5.
}
\]

Against the same four-bit literal baseline,

\[
\boxed{
\Delta_C(H_c)=4-5=-1.
}
\]

Thus identical training exposure yields opposite held-out compression evidence.

## W5. What the witness shows

The witness establishes that a declared predictive regularity can reduce held-out codelength.

It also establishes that the same compressor can impose overhead when its inferred structure fails on held-out data.

This is stronger than reporting training fit.

## W6. Trivial-compressibility control

Let

\[
Z=(0,0,0,0,0,0,0,0).
\]

Define a second prefix code:

- one-bit word \(1\): eight zeros;
- nine-bit word \(0b_1\ldots b_8\): literal fallback.

For \(Z\),

\[
\boxed{
L_C(Z)=1.
}
\]

A literal baseline requires eight bits.

Thus

\[
\boxed{
\Delta_C(Z)=7.
}
\]

The sequence is highly compressible under this code.

Nothing in the witness contains:

- learning;
- adaptation;
- task transfer;
- agency;
- semantic understanding;
- general intelligence.

Therefore this is an exact counterexample to

\[
\text{large compression gain}
\Rightarrow
\text{intelligence}.
\]

## W7. Memorization control

A table that stores every label in \(T\) can reproduce \(T\) exactly.

That fact does not determine \(H\).

The period-two witness earns its gain only because the learned pattern predicts the untouched suffix.

The empirical analogue is mandatory:

> report codelength on untouched data, not only on examples used to fit the compressor or probe.

## W8. Codec-relativity control

The same all-zero object \(Z\) has:

- length \(1\) under the special zero-run code;
- length \(8\) under a fixed literal code.

Therefore codelength is incomplete without the code definition.

The correct conclusion is not that compression measurements are useless.

The correct conclusion is that comparisons must hold the relevant code semantics fixed or explicitly test code sensitivity.

## W9. Minimal exact replay code

    T = (0, 1, 0, 1)
    H_structured = (0, 1, 0, 1)
    H_control = (0, 0, 1, 1)

    def period2_prediction(train, n):
        motif = train[-2:]
        return tuple(motif[i % 2] for i in range(n))

    def conditional_length(train, heldout):
        predicted = period2_prediction(train, len(heldout))
        if tuple(heldout) == predicted:
            return 1
        return 1 + len(heldout)

    literal = 4

    assert period2_prediction(T, 4) == H_structured
    assert conditional_length(T, H_structured) == 1
    assert literal - conditional_length(T, H_structured) == 3

    assert conditional_length(T, H_control) == 5
    assert literal - conditional_length(T, H_control) == -1

    Z = (0,) * 8

    def zero_run_length(bits):
        if tuple(bits) == (0,) * 8:
            return 1
        return 1 + len(bits)

    assert zero_run_length(Z) == 1
    assert 8 - zero_run_length(Z) == 7

## W10. Probe-state separation

The replay has three distinct quantities:

\[
L_0(H),
\qquad
L_C(H\mid T),
\qquad
\Delta_C.
\]

They should not be collapsed.

A system can have:

- low codelength but poor retained behavior;
- good behavior but high codelength under a poor probe;
- positive gain under one code and weak gain under another.

The witness only verifies the arithmetic of the declared codes.

## Claim boundary

This witness does not establish:

- that period-two structure is intelligent;
- that one bit is a universal codelength for the structured suffix;
- that the selected codec is optimal;
- that compression gain identifies a unique representation or Residual;
- that a probe-accessible property is causally used by a model;
- that compression progress is sufficient or necessary for scientific discovery;
- that a larger compression gain means a more intelligent system.
