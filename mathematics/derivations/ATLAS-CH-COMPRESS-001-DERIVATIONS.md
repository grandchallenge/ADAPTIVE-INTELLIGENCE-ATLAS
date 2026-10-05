# Derivations — ATLAS-CH-COMPRESS-001

## Scope

This packet develops exact finite compression identities used by the chapter.

It does not establish that any one compression method preserves task quality universally or that compressibility implies interpretability.

## D1. Two-part description length

For a declared code C, model M, and data D, a two-part description length has the form

L_C(M,D)
=
L_C(M)
+
L_C(D|M).

The code C is part of the definition.

Two models can have the same parameter count and different code lengths.

Two models can have different parameter counts and the same code length.

Therefore parameter count and description length are not interchangeable.

## D2. MDL finite witness

Let two hypotheses have declared model-code lengths

L(H_A)=3,

L(H_B)=7.

Suppose the conditional data-code lengths are equal:

L(D|H_A)=L(D|H_B)=5.

Then

L(H_A,D)=3+5=8,

L(H_B,D)=7+5=12.

The shorter total description is H_A under this declared code.

The witness demonstrates two-part accounting only.

It does not establish the code lengths as universal or canonical.

## D3. Exact rank-one representation

Let

u=v=(1,1,1,1)^T.

Define

W=uv^T.

Then

W=
[[1,1,1,1],
 [1,1,1,1],
 [1,1,1,1],
 [1,1,1,1]].

Every column equals u, so rank(W)=1.

For every x in R^4,

Wx
=
u(v^T x).

Thus the factorized representation implements exactly the same linear map as the dense matrix.

## D4. Declared-code comparison

Assume:

- the 4 by 4 shape is known;
- dense entries are binary;
- rank-one factor entries are binary;
- one format bit distinguishes dense from factorized payloads.

Dense code length:

1 + 16 = 17 bits.

Factorized code length:

1 + 4 + 4 = 9 bits.

The exact same map therefore has different description lengths under the declared representation code.

The result depends on the declared codec.

## D5. Eckart–Young control

Let

A=diag(4,3,1).

Its singular values are

sigma_1=4,
sigma_2=3,
sigma_3=1.

The best rank-r Frobenius approximation keeps the largest r singular values.

For r=1,

A_1=diag(4,0,0).

Therefore

||A-A_1||_F^2
=
3^2+1^2
=
10.

For r=2,

A_2=diag(4,3,0),

and

||A-A_2||_F^2
=
1.

The rank-one representation is not exact because discarded singular values are nonzero.

## D6. Pruning can destroy function

Let

w=(1,1/8)^T,

x=(0,8)^T.

Then

w^T x
=
1*(0)+(1/8)*8
=
1.

Apply magnitude threshold tau=1/4.

Since |1/8|<1/4, prune the second component:

w_pruned=(1,0)^T.

Then

w_pruned^T x=0.

Thus small magnitude does not imply functional irrelevance on every input distribution.

## D7. Fixed-grid quantization

Let

w=(1/4,1/2,1/2,1/4).

Use fixed grid

Q={0,1/4,1/2,3/4}.

Each value of w belongs to Q exactly.

Thus the quantized vector equals w with zero parameter distortion.

If each raw value uses 8 bits, raw payload is

4*8=32 bits.

If grid indices use 2 bits, quantized payload is

4*2=8 bits.

Because the grid is fixed and known, there is no codebook payload in this witness.

## D8. Learned codebook accounting

If the same vector is represented by two learned centroids

c_0=1/4,
c_1=1/2,

and four one-bit indices, then with 8-bit centroids:

centroid payload=2*8=16 bits,

index payload=4 bits,

total=20 bits.

This is weight sharing.

All four connections remain represented.

## D9. Compression ratio

For original length L_orig and compressed length L_comp>0,

compression ratio
=
L_orig/L_comp.

For the fixed-grid witness:

32/8=4.

For the learned two-centroid witness:

32/20=8/5.

The larger ratio does not by itself establish higher retained accuracy.

## D10. Distortion measure

A lossy compression claim needs a declared distortion.

For parameter distortion one might use

||theta-theta_hat||.

For linear-map distortion one might use

||W-W_hat||.

For task distortion one might use a change in predictive loss or accuracy.

These measures can disagree.

Therefore "compression error" is incomplete unless the measured object is specified.

## D11. Distillation objective

Let teacher logits be z_T and student logits z_S.

At temperature T>0, define teacher and student distributions

p_T(i)
=
exp(z_T,i/T) / sum_j exp(z_T,j/T),

p_S(i)
=
exp(z_S,i/T) / sum_j exp(z_S,j/T).

A distillation term may minimize cross-entropy or KL divergence between these distributions.

This transfers predictive behavior under the declared objective.

It does not encode teacher parameters bit-for-bit.

## D12. Equal outputs do not imply equal internals

Suppose two models satisfy

f_A(x)=f_B(x)

for all x in a declared domain X.

Then they are functionally equivalent on X.

Their parameterizations, internal representations, computational costs, and code lengths can still differ.

Compression claims must state which equivalence is being preserved.

## D13. Structured parameterization

A dense matrix in R^(m by n) has mn free scalar entries.

A rank-r factorization UV^T with

U in R^(m by r),
V in R^(n by r)

has r(m+n) stored scalar entries before accounting for format metadata.

When

r(m+n)<mn,

the factorized parameterization uses fewer scalar slots.

This arithmetic does not guarantee faster execution or lower coded length after all metadata and implementation overhead are included.

## D14. Distillation versus exact compression

If a student reproduces teacher outputs only approximately on a training distribution, the student is not an exact compressed encoding of the teacher function.

Even exact agreement on a finite sample does not prove equality everywhere.

The correct object is behavioral approximation under a declared domain/objective.

## D15. Compression as probe

A successful compression can show that the declared behavior can be reproduced with a shorter representation under a declared codec and tolerance.

It does not by itself reveal why the behavior works.

Mechanistic conclusions require additional evidence.

## Claim boundary

Established here:

- two-part description accounting;
- exact dense-versus-rank-one code-length witness;
- exact low-rank approximation errors for the diagonal control;
- exact pruning failure control;
- exact fixed-grid and learned-codebook bit counts;
- mechanism distinction between pruning, quantization, sharing, low rank, and distillation.

Not established here:

- a universal optimal codec;
- universal task preservation under compression;
- a theorem that compressed models are more interpretable;
- a theorem that compressibility measures intelligence.
