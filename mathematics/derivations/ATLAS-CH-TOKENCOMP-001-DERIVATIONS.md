# ATLAS-CH-TOKENCOMP-001 — Derivation Packet

## D1. Token length

For tokenizer \(\tau\):

\[
L_\tau(x)=|\tau(x)|.
\]

This is a sequence-length quantity only.

## D2. Fixed-width token-ID length

Let:

\[
m=|V_\tau|\ge2.
\]

A declared fixed-width ID code requires:

\[
w_\tau=\lceil\log_2m\rceil
\]

bits per token ID.

Therefore:

\[
D_{\mathrm{fw}}(x;\tau)
=
L_\tau(x)\lceil\log_2|V_\tau|\rceil.
\]

Thus token count and vocabulary size jointly determine this toy ID-stream length.

## D3. Fixed-width and model-based code lengths differ

TOKEN-001 supplies:

\[
\ell_p(s)
=
-\sum_i\log_2p(v_i).
\]

Fixed-width coding instead uses:

\[
D_{\mathrm{fw}}=n\lceil\log_2m\rceil.
\]

Equality requires additional conditions.

Therefore:

\[
D_{\mathrm{fw}}
\neq
\ell_p
\]

in general.

## D4. Tokenizer-description overhead

If a tokenizer specification is not already shared, a complete transmitted representation can require:

\[
D_{\mathrm{total}}
=
D_{\mathrm{spec}}
+
D_{\mathrm{sequence}}
+
D_{\mathrm{framing}}.
\]

TOKENCOMP's exact finite witness compares only the sequence-ID component under shared specifications.

Hence it does not prove a complete compressor ordering.

## D5. Toy compute vector

For token length \(n\) and vocabulary size \(m\), define:

\[
K(n,m)
=
\left(
C_{\mathrm{pair}}(n),
C_{\mathrm{vocab}}(n,m)
\right)
=
(n^2,nm).
\]

These are declared exact proxies.

They are not measured runtime.

## D6. Witness tokenizer S

Let:

\[
x=\texttt{abababab}.
\]

Tokenizer S has:

\[
V_S=\{a,b\},
\qquad
m_S=2.
\]

Its token sequence is:

\[
[a,b,a,b,a,b,a,b].
\]

Therefore:

\[
n_S=8.
\]

Fixed-width ID width:

\[
w_S=\lceil\log_22\rceil=1.
\]

So:

\[
D_S=8.
\]

Compute vector:

\[
K_S=(8^2,8\cdot2)=(64,16).
\]

## D7. Witness tokenizer P

Let:

\[
V_P=\{a,b,ab,x,y,z,w,q\},
\qquad
m_P=8.
\]

Its token sequence is:

\[
[ab,ab,ab,ab].
\]

Therefore:

\[
n_P=4.
\]

Fixed-width ID width:

\[
w_P=\lceil\log_28\rceil=3.
\]

So:

\[
D_P=4\cdot3=12.
\]

Compute vector:

\[
K_P=(4^2,4\cdot8)=(16,32).
\]

## D8. Conflicting orderings

Token count:

\[
n_P<n_S.
\]

Pair proxy:

\[
C_{\mathrm{pair},P}<C_{\mathrm{pair},S}.
\]

But fixed-width ID stream:

\[
D_P>D_S.
\]

And dense-vocabulary proxy:

\[
C_{\mathrm{vocab},P}>C_{\mathrm{vocab},S}.
\]

Thus:

\[
\boxed{
n_P<n_S
\not\Rightarrow
D_P<D_S
}
\]

and:

\[
\boxed{
n_P<n_S
\not\Rightarrow
K_P\le K_S
\text{ componentwise}.
}
\]

The tokenizers are incomparable under the declared two-coordinate compute vector.

## D9. Pareto interpretation

Under objective vector:

\[
J_\tau=(D_{\mathrm{fw}},C_{\mathrm{pair}},C_{\mathrm{vocab}}),
\]

S gives:

\[
J_S=(8,64,16),
\]

while P gives:

\[
J_P=(12,16,32).
\]

Neither vector is componentwise smaller.

Therefore neither tokenizer Pareto-dominates the other in this toy objective space.

A scalar winner requires declared weights or a different objective.

## D10. Baseline-relative compression ratio

The ASCII byte string \(\texttt{abababab}\) contains 8 bytes, or 64 baseline bits.

Thus:

\[
R_S=8/64=1/8,
\]

\[
R_P=12/64=3/16.
\]

These are toy token-ID stream ratios under shared tokenizer specifications.

They do not include specification/dictionary cost.

## D11. Canonical-domain tokenizers

Let \(\mathcal X_c\) be a declared canonical byte-string domain.

For A and B:

\[
\tau_A:\mathcal X_c\to V_A^*,
\quad
\delta_A:V_A^*\to\mathcal X_c,
\]

\[
\tau_B:\mathcal X_c\to V_B^*,
\quad
\delta_B:V_B^*\to\mathcal X_c.
\]

Assume:

\[
\delta_A\circ\tau_A=\operatorname{id}_{\mathcal X_c},
\]

\[
\delta_B\circ\tau_B=\operatorname{id}_{\mathcal X_c}.
\]

## D12. Translation construction

Define:

\[
T_{A\to B}
=
\tau_B\circ\delta_A.
\]

For any \(x\in\mathcal X_c\):

\[
T_{A\to B}(\tau_A(x))
=
\tau_B(\delta_A(\tau_A(x)))
=
\tau_B(x).
\]

Then:

\[
\delta_B(T_{A\to B}(\tau_A(x)))
=
\delta_B(\tau_B(x))
=
x.
\]

Hence translation through the canonical domain is lossless on the declared domain.

## D13. Translation is not ID mapping

In general:

\[
T_{A\to B}
\]

need not act token-by-token.

One A token can become one or several B tokens, and several A tokens can become one B token.

Therefore a direct ID permutation is a strictly stronger condition than canonical decode-and-retokenize interoperability.

## D14. Interoperability does not imply behavioral equivalence

Suppose two model front ends use embedding tables \(E_A,E_B\).

Even when both decode to the same canonical bytes:

\[
\delta_A(s_A)=\delta_B(s_B)=x,
\]

the model inputs are:

\[
E_A(s_A)
\]

and:

\[
E_B(s_B).
\]

No equality follows without additional structure.

Thus:

\[
\boxed{
\text{lossless interface translation}
\not\Rightarrow
\text{equal internal representation or behavior}.
}
\]

## D15. Special-token boundary

A token stream may contain control/special tokens that have no ordinary canonical-byte decoding.

Such tokens lie outside the simple lossless translation theorem unless their transport semantics are separately specified.

This is a protocol boundary, not an implementation nuisance.

## D16. Version boundary

A tokenizer interface is versioned state.

If vocabulary, merge order, normalization, special-token IDs, or decoder rules change, an identical integer sequence may no longer denote the same representation.

Interoperability therefore requires exact tokenizer identity, not only a tokenizer family name.

## D17. Corpus scope

For corpus \(C\), comparison quantities such as:

\[
\mathbb E_{x\sim C}[L_\tau(x)]
\]

or:

\[
\mathbb E_{x\sim C}[D_{\mathrm{fw}}(x;\tau)]
\]

depend on \(C\).

No finite witness implies a universal ranking across languages or corpora.

## Durable propositions

1. Vocabulary size and sequence length jointly determine fixed-width token-ID stream length.
2. Fixed-width ID length and probability-model description length are distinct.
3. Shorter token sequences need not minimize a multi-coordinate compute model.
4. The exact witness produces conflicting compression and compute orderings.
5. A complete compressor comparison must account for tokenizer/specification overhead when it is not shared.
6. Lossless translation between tokenizer representations exists through a shared canonical domain under explicit round-trip assumptions.
7. Lossless translation does not imply token, embedding, semantic, probabilistic, or model-behavior equivalence.
8. A universal tokenizer lingua franca is not established.

## Claim boundary

This packet proves only the declared finite accounting and interoperability identities. It does not establish measured speedups, hardware costs, downstream accuracy, semantic equivalence, multilingual optimality, or a universal tokenizer standard.
