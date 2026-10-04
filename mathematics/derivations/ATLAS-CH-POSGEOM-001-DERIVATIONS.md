# Derivations — ATLAS-CH-POSGEOM-001

## Scope

This packet develops the exact positional algebra used by the chapter.

It proves the finite rotation identities and witness arithmetic.

It does not prove that a trained language model will extrapolate reliably to arbitrary context length.

## D1. Rotation block

Define

R(phi) =
[[cos(phi), -sin(phi)],
 [sin(phi),  cos(phi)]].

Then

R(phi)^T = R(-phi).

Therefore

R(phi)^T R(psi)
=
R(-phi)R(psi)
=
R(psi-phi).

This is the basic group identity.

## D2. Position-indexed rotations

For fixed frequency omega, define

R_m = R(m omega).

Then

R_m^T R_n
=
R((n-m)omega).

Thus for query/key subvectors q,k,

(R_m q)^T(R_n k)
=
q^T R_m^T R_n k
=
q^T R((n-m)omega) k.

The dot product depends on m,n only through the relative offset n-m once q,k and omega are fixed.

## D3. Multi-frequency block diagonal form

For even dimension d=2h, let

R_m =
diag(
R(m omega_1),
...,
R(m omega_h)
).

Each block is orthogonal.

Therefore R_m is orthogonal and

R_m^T R_n
=
diag(
R((n-m)omega_1),
...,
R((n-m)omega_h)
).

The relative-offset identity holds independently in every frequency block.

## D4. Connection to additive sinusoids

For one frequency omega, define the additive sinusoidal position vector

p_m =
[sin(m omega), cos(m omega)]^T.

Using angle-addition identities,

p_(m+delta)
=
A_delta p_m,

where

A_delta =
[[ cos(delta omega),  sin(delta omega)],
 [-sin(delta omega),  cos(delta omega)]].

So a fixed position offset is represented by a linear rotation of the 2-vector.

This is an exact trigonometric identity.

It does not make additive sinusoidal encoding identical to rotary query/key transformation.

## D5. Exact same-offset witness

Choose

theta=pi/6,

q=k=(1,0)^T.

For m=0,n=2,

score_(0,2)
=
q^T R(2 theta)k
=
cos(pi/3)
=
1/2.

For m=3,n=5,

score_(3,5)
=
q^T R(2 theta)k
=
1/2.

The absolute positions differ, but n-m=2 in both cases.

## D6. Generic-vector replay

Let

q=(1,2)^T,

k=(3,-1)^T,

theta=pi/6,

m=2,

n=5.

Then n-m=3 and

R(3 theta)=R(pi/2)
=
[[0,-1],[1,0]].

Therefore

R(pi/2)k
=
(1,3)^T,

and

q^T R(pi/2)k
=
1+6
=
7.

By D2,

(R(2 theta)q)^T(R(5 theta)k)=7.

This verifies the identity on a non-axis-aligned pair.

## D7. Non-orthogonal control

Define

S_m =
diag(2^m,1).

Then

S_m^T S_n
=
diag(2^(m+n),1).

This depends on m+n, not only n-m.

For q=k=(1,0)^T,

(S_m q)^T(S_n k)
=
2^(m+n).

Equal-offset pairs:

(0,2) gives 4.

(3,5) gives 256.

Thus same relative offset does not determine the score.

The missing property is the position-indexed orthogonal/group action satisfying T_m^T T_n=T_(n-m).

## D8. A stronger algebraic condition

Suppose position transforms T_m satisfy

T_m^T T_n = G_(n-m)

for some family G_delta.

Then transformed inner products obey

(T_m q)^T(T_n k)
=
q^T G_(n-m)k.

RoPE realizes this with

T_m=R_m

and

G_delta=R_delta.

Orthogonality plus the additive phase representation supplies this relation.

The chapter does not claim this condition is unique.

## D9. Multidimensional product action

Let 2D positions be

p=(u,v),

q=(u',v').

Define

R_p
=
diag(
R(u omega_x),
R(v omega_y)
).

Then

R_p^T R_q
=
diag(
R((u'-u)omega_x),
R((v'-v)omega_y)
).

Hence transformed inner products depend on the coordinate-wise relative displacement

q-p=(u'-u,v'-v).

This is the direct-product version of the 1D identity.

## D10. Translation of all positions

Let every position shift by c:

m -> m+c,

n -> n+c.

Then

(n+c)-(m+c)=n-m.

Therefore the rotary inner-product kernel is invariant under a common translation of position indices:

R_(m+c)^T R_(n+c)
=
R_(n-m).

This is an exact algebraic translation-invariance statement for the rotary score contribution.

It is not a statement that the full model is translation invariant, because content, masking, boundaries, and other position-dependent operations can break that symmetry.

## D11. Frequency schedule

For h blocks, the relative contribution is

sum_j q_j^T R((n-m)omega_j) k_j.

Different omega_j produce different phase rates.

Therefore the frequency schedule determines how offsets are represented across blocks.

Changing base frequencies or rescaling positions changes this phase map.

Frequency scaling and index scaling can sometimes produce related phase effects, but they are distinct interventions and must be stated explicitly.

## D12. Position Interpolation

Suppose a pretrained model used position index m in an original range [0,L).

To map a target range [0,L') with L'>L into the original coordinate scale, Position Interpolation uses a rescaled position approximately

m_tilde = m L/L'.

The rotary phase becomes

m_tilde omega

rather than m omega.

This keeps the evaluated phases in a range closer to the pretrained regime.

The paper provides model-scoped theoretical/empirical evidence for this strategy.

The present derivation does not turn that evidence into a universal theorem.

## D13. Extrapolation versus exact algebra

The identity

R_m^T R_n=R_(n-m)

continues algebraically for all integer or real m,n.

However a trained model has learned weights under a finite distribution of phases and offsets.

Therefore exact continuation of the positional formula does not imply that the learned attention computation behaves usefully outside the training regime.

This is the central algebra-versus-generalization boundary.

## D14. Mask interaction

A causal mask changes admissible attention support.

The rotary identity affects the score between an admissible query-key pair.

The mask determines whether that pair is allowed to contribute at all.

Thus positional score geometry and attention support constraints are distinct components.

## Claim boundary

Established here:

- exact 2D rotation-group identity;
- exact relative-offset query-key inner-product identity;
- multi-frequency block extension;
- common-translation invariance of the rotary score contribution;
- additive-sinusoid fixed-offset linear relation;
- multidimensional product-group identity;
- exact same-offset and non-orthogonal-control witnesses.

Not established here:

- universal long-context extrapolation;
- task-quality preservation under arbitrary scaling;
- superiority of one frequency schedule for all tasks;
- downstream RPO frequency-mode/DC/head-specialization claims.
