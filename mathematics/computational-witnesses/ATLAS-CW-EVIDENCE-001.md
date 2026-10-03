# ATLAS-CW-EVIDENCE-001 — Finite Witness versus Universal Claim

**Chapter:** ATLAS-CH-EVIDENCE-001  
**Witness class:** exact finite computation  
**Purpose:** make the boundary between an exact computational witness and a universal theorem explicit.

## Question

Compare two claims.

Finite claim:

For every integer n in the declared set {-10,-9,...,10}, the product n(n-1) is even.

Universal claim:

For every integer n, the product n(n-1) is even.

## Inputs

The exact integer domain is:

-10 through 10 inclusive.

No floating-point arithmetic is used.

## Deterministic replay procedure

The following Python procedure uses only exact integer arithmetic.

    values = list(range(-10, 11))
    residues = [(n * (n - 1)) % 2 for n in values]
    print("count=" + str(len(values)))
    print("all_even=" + str(all(r == 0 for r in residues)))

Expected output:

    count=21
    all_even=True

## Result

The exact finite witness establishes the finite claim for all 21 declared inputs.

It does not, by enumeration alone, establish the universal claim over all integers.

## Separate universal proof

Let n be an arbitrary integer.

The integers n and n-1 are consecutive. Exactly one of two consecutive integers is even. Therefore their product n(n-1) has an even factor and is even.

Because n was arbitrary, the universal claim follows.

The proof and the finite computation agree on the 21 tested cases, but they have different logical scope.

## Why this witness belongs in the chapter

The example separates four objects that are often blurred:

1. the finite claim;
2. the universal claim;
3. the exact computational witness;
4. the general proof.

Exactness of the computation strengthens confidence in what was computed. It does not enlarge the quantifier of the claim.

## Claim boundary

This witness establishes only the exact finite enumeration result and illustrates the difference between finite verification and general proof.

The universal parity statement is established by the separate elementary argument, not by the 21-case enumeration.

The witness says nothing about empirical machine-learning behavior, numerical approximation, model mechanisms, or scientific reproducibility outside this toy example.
