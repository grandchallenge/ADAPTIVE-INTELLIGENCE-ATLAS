# ATLAS-CH-VARIOPT-001 — Transaction Receipt

## Identity

- chapter: ATLAS-CH-VARIOPT-001
- implementation issue: #289
- protected baseline: 77946bcbe595f88c0fe446f6d0dfc9868267da00
- branch: work/variopt-289

## Hard prerequisites

NUMERICS-001:
- manuscript a719a16e86d1feb76679e1f1cda2d9d3393d2e42
- source lock 7feea1c8ca3026fa1f61f35b87281b4afe9ccd8d
- AUDIT-009 2bbb1b7687d6c4b8c0bfeed5206de836dac92dca

MANOPT-001:
- manuscript 62ded6bc72c980feb96dff2c77c122141171f64f
- source lock e98e655839f521250d25350c33006c9eed60e23c
- AUDIT-045 f6663dde7a93c9ca7a471e3e272759c9c337dfd6

## Established external authority

- Bregman (1967), DOI 10.1016/0041-5553(67)90040-7
- Marsden and West (2001), DOI 10.1017/S096249290100006X
- Wibisono, Wilson, and Jordan (2016), DOI 10.1073/pnas.1614734113

## GCL programme evidence

Protected MODULUS snapshot:
- repository: grandchallenge/MODULUS
- commit: 7ca4ffcdace32d5ff79c27ad557bfb690fac0af3
- motivation/context blob: 73af647840f07aa527e98998e0397de240d34e7c
- Hyperball implementation blob: 88b5e2b4c9abe760b8670f7fd2691fee25587b17
- Hyperball test blob: 105d6b4e38fe6d71bef8e7ec28c2f05a5ce08434

GCL repository-profile authority:
- grandchallenge/gcl-standards@b89fc0ab807e69a255760c11ce85b1048d329c81
- MODULUS profile blob: 6d52d66cbc11478c0f0a8872c19160d572dc4396
- authority: versioned implementation, benchmark, and empirical evidence; no claim-promotion or certification authority.

## Implementation artifacts

- specification 9023f94675ad4d0144f9b074877c82f62c84909a
- derivation packet 0862c95b24ea66ca6a6a6d4f1d9d3c031af1354b
- computational witness 82ac7737ac0718c83db48face1e5fb9d402aebcb
- reader manuscript 57751af058ee5885e7478e1aa74c1cc50aa2f463
- source lock 1e20f98009b8828963c9d26aa87323292d6f99b3
- Chapter Ledger 09a07425e69f67d1113f037aaf62f60fa769dd39
- Source Register 1910bb5a199cb976b0821e9a1c9d5158556db53d

## Exact divergence witness

For phi(x)=exp(x):
- D(1,0)=e-2
- D(0,1)=1
- therefore the divergence is asymmetric.

At x=0:
- D(delta,0)=exp(delta)-1-delta
- local expansion begins delta^2/2.

## Exact mirror-step witness

For phi(x)=x log x-x:
- grad phi(x)=log x
- x0=1
- eta=1
- g=log 2
- exact mirror update x1=1/2.

## Exact non-descent control

For:
- f(x)=1/2(x-2)^2
- x0=0
- Euclidean Bregman generator
- eta=3

the divergence-derived first-order update gives:
- x1=6
- f(x0)=2
- f(x1)=8

so derivation from a convex divergence does not itself imply descent.

## Exact discrete-variational witness

Discrete Lagrangian:

L_d(q_k,q_{k+1};h)
=
(q_{k+1}-q_k)^2/(2h)
-
h q_k^2/2.

Discrete Euler-Lagrange stationarity gives:

q_{k+1}
=
(2-h^2)q_k-q_{k-1}.

With p_k=(q_k-q_{k-1})/h:

p_{k+1}=p_k-hq_k,

q_{k+1}=q_k+h p_{k+1}.

The exact state matrix is:

M_h =
[[1-h^2,h],[-h,1]],

with:
- det(M_h)=1;
- M_h^T J M_h=J.

## Exact symplectic controls

At:
- h=1/2
- (q0,p0)=(0,1)

the update gives:
- p1=1
- q1=1/2.

For H(q,p)=1/2(q^2+p^2):
- H0=1/2
- H1=5/8

so exact symplecticity does not imply exact energy conservation.

For F(q)=1/2 q^2:
- F(q0)=0
- F(q1)=1/8

so exact symplecticity does not imply objective descent.

## Exact MODULUS programme witness

Using the protected Hyperball geometry:
- w=(1,0)
- base proposal u=(1,1)
- tangent projection u_perp=(0,1)
- radius=1
- target-angle programme parameter alpha=1

the sphere retraction gives:

w_plus=(1,1)/sqrt(2).

The exact finite angle is:

theta=pi/4,

not 1 radian.

For unit w and unit tangent v, the exact finite relation is:

theta=arctan(alpha).

Thus the current target-angle branch is first-order angular control through tangent-update norm, not exact finite exponential-map angle control.

## Independent replay

All exact finite and symbolic checks return:

VARIOPT_EXACT_WITNESS_OK

## Durable boundaries

- divergence != metric;
- local Hessian geometry != global distance;
- divergence-derived update != automatic descent;
- action stationarity != objective stationarity;
- variational derivation != accuracy or stability;
- symplecticity != exact energy conservation;
- symplecticity != objective descent;
- constraint preservation != convergence or global optimality;
- Bregman-Lagrangian source theory != arbitrary discretization theorem;
- MODULUS Hyperball != established universal variational theory;
- programme target-angle parameter != exact finite geodesic angle under the current retraction.

## Validation gate

Merge requires independent exact witness replay and full repository GitHub Actions validation on the exact implementation head, followed by a fresh post-draft audit.
