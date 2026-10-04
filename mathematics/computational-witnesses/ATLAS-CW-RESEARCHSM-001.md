# ATLAS-CW-RESEARCHSM-001 — Finite Research-State Witness

## Evidence identity

Fix dispatch `d=17` and result identity `r_A=(17,A)`. With `E_0=empty`, first capture gives `E_1={r_A}`, so `|E_1|=1`.

## Exact retry

Receiving the same identity again gives `E_2=E_1 union {r_A}=E_1`, so `|E_2|=1`. Attempt history may still record both arrivals.

## Distinct result

Let `r_B=(17,B)` with `B!=A`. This is not an exact duplicate of `r_A`. Preserving both gives `E_3={r_A,r_B}`, so `|E_3|=2`.

## Advancement gate

Use:

`G_adv(b)=b1*b2*b3*b4*b5`.

For:

`b=(1,1,1,1,0)`,

we obtain:

`G_adv(b)=0`.

For:

`b'=(1,1,1,1,1)`,

we obtain:

`G_adv(b')=1`.

A missing required replay/check example is:

`b_R=(1,1,0,1,1)`,

which also gives:

`G_adv(b_R)=0`.

## Idempotent advancement

Let `K_adv` be the canonical set of advanced evidence identities.

If `m` is already admitted under a true guard, then:

`(K_adv union {m}) union {m}=K_adv union {m}`.

Thus repeating the same exact advancement event does not multiply the canonical advancement effect.

History may still record the repeated attempt.

## Actor-separation counterexample

For a policy that requires producer/reviewer identity separation, define:

`Sep(a_prod,a_rev)=1{a_prod != a_rev}`.

Then:

`Sep(A,A)=0`.

So a same-actor review fails that declared separation predicate.

For distinct identities:

`Sep(A,B)=1`.

This establishes identity separation only; it does not prove stronger independence.

## Safety without liveness

Take a blocked state in which:

- all evidence identities are preserved;
- every invalid guarded transition remains blocked;
- no duplicate canonical effect occurs;
- certification remains unchanged;
- advancement disposition stays false forever.

If the only repeated future event is an idempotent retry, all listed safety invariants continue to hold while the evidence identity never enters `K_adv`.

Therefore the finite execution is safe under the declared invariants but not live with respect to eventual advancement.

## Claim boundary

This witness proves only the exact finite identity, Boolean-guard, actor-identity-separation, idempotence, and safety/liveness statements above.

It does not prove that the five-factor gate is universally correct; that distinct actors are epistemically independent; that workflow conformance proves mathematical truth; that blocked work should always advance; or that one lifecycle should govern all research programmes.
