# ATLAS-CW-RESEARCHSM-001 — Finite Research-State Witness

## Evidence identity

Fix dispatch `d=17` and result identity `r_A=(17,A)`. With `E_0=empty`, first capture gives `E_1={r_A}`, so `|E_1|=1`.

## Exact retry

Receiving the same identity again gives `E_2=E_1 union {r_A}=E_1`, so `|E_2|=1`. Attempt history may still record both arrivals.

## Distinct result

Let `r_B=(17,B)` with `B!=A`. This is not an exact duplicate of `r_A`. Preserving both gives `E_3={r_A,r_B}`, so `|E_3|=2`.

## Claim boundary

The witness is limited to the finite identity-count calculations above.
