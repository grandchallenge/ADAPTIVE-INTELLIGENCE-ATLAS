# ATLAS-CH-REP-001 — Derivation Packet

## D1. Representation map

A representation is modeled as

[
r:mathcal X\tomathcal Z.
]

The coordinates in (mathcal Z) are not themselves the semantics.

## D2. Invariance and equivariance

Let a group element (g) act on inputs and let (\rho(g)) act on the representation space.

Invariance:

[
r(gcdot x)=r(x).
]

Equivariance:

[
r(gcdot x)=\rho(g)r(x).
]

For reflection

[
G=
\begin{pmatrix}
-1&0\
0&1
end{pmatrix},
]

the identity representation (r(x)=x) is equivariant under (\rho(G)=G).

The scalar representation

[
r_{\rm inv}(x)=|x|_2^2
]

is invariant under this reflection.

For

[
x=(2,3),
]

both (x) and (Gx=(-2,3)) have invariant value (13).

## D3. Equivalent recoding with transformed readout

Let

[
zinmathbb R^2,
qquad
\tilde z=Tz,
]

with invertible

[
T=
\begin{pmatrix}
1&1\
0&1
end{pmatrix}.
]

A linear readout

[
y=w^\top z
]

is preserved by choosing

[
\tilde w=T^{-\top}w.
]

Then

[
\tilde w^\top\tilde z
=
w^\top z.
]

For

[
z=(2,3),
qquad
w=(4,-1),
]

the original output is (5).

The transformed objects are

[
\tilde z=(5,3),
qquad
\tilde w=(4,-5),
]

and the output remains (5).

Thus coordinate identity is not required for task-preserving equivalence.

## D4. Identifiability warning

If latent variables are transformed by an invertible mixing (T) and the decoder is transformed by (T^{-1}), observable data can remain unchanged.

Additional assumptions are therefore needed to identify a preferred latent coordinate system. This is consistent with the unsupervised-disentanglement limitations discussed by Locatello et al. [@LocatelloEtAl2019].

## D5. Sparsity and superposition

Sparse coding represents an input using relatively few active dictionary coefficients.

Superposition, as used in the cited toy-model research, studies regimes in which more features than available representational dimensions are encoded non-orthogonally.

The Atlas does not promote that toy-model mechanism to a universal theorem about learned networks.

## Claim boundary

This packet establishes exact invariance/equivariance and invertible-recoding examples. Broader claims about semantic equivalence, sparse features, or superposition remain model- and evidence-dependent.
