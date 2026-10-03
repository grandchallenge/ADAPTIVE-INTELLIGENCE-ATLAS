# ATLAS-CW-OPTBASE-001 — First-Order Optimization Witness

**Chapter:** \`ATLAS-CH-OPTBASE-001\`  
**Runtime:** Wolfram Language service, 2026-10-03

## Purpose

Replay the exact calibration objects used by the chapter:

- finite unbiased SGD;
- Adam first-step bias correction;
- global norm clipping;
- coupled versus decoupled decay under adaptive scaling;
- scalar quadratic amplification;
- initialization second-moment formulas.

## Unbiased SGD

Sample gradients:

\[
g_1=x-1,
\qquad
g_2=x+1.
\]

Uniform expectation:

\[
\frac12(g_1+g_2)=x.
\]

Variance:

\[
\frac12[(g_1-x)^2+(g_2-x)^2]=1.
\]

## Adam first step

Parameters:

\[
g_1=3,
\quad
\beta_1=9/10,
\quad
\beta_2=99/100.
\]

With zero initial moments:

\[
m_1=3/10,
\qquad
v_1=9/100.
\]

Bias-corrected:

\[
\hat m_1=3,
\qquad
\hat v_1=9.
\]

At \(\varepsilon=0\):

\[
\hat m_1/\sqrt{\hat v_1}=1.
\]

## Gradient clipping

For

\[
g=(3,4),
\quad
\tau=2,
\]

the exact result is

\[
g_{\rm clip}
=
(6/5,8/5),
\]

with norm

\[
2.
\]

## Coupled versus decoupled decay

Use:

\[
\theta=2,
\quad
g=3,
\quad
p=1/2,
\quad
\eta=1/10,
\quad
\lambda=1/5.
\]

Wolfram returns:

\[
\theta_{\rm c}^+=183/100,
\]

\[
\theta_{\rm d}^+=181/100,
\]

and

\[
\theta_{\rm c}^+-\theta_{\rm d}^+=1/50.
\]

## Initialization

Under the declared independence/zero-mean assumptions,

\[
\mathbb E[z^2]
=
n\sigma_w^2q.
\]

For symmetric preactivation and ReLU,

\[
\mathbb E[\operatorname{ReLU}(z)^2]
=
\frac12n\sigma_w^2q.
\]

## Replay expression

\`\`\`wolfram
g1=x-1;
g2=x+1;
eg=FullSimplify[(g1+g2)/2];
var=FullSimplify[
 ((g1-eg)^2+(g2-eg)^2)/2
];

beta1=9/10;
beta2=99/100;
grad=3;

m1=(1-beta1) grad;
v1=(1-beta2) grad^2;
mhat=FullSimplify[m1/(1-beta1)];
vhat=FullSimplify[v1/(1-beta2)];

gv={3,4};
tau=2;
ng=Sqrt[gv.gv];
gclip=FullSimplify[
 gv Min[1,tau/ng]
];

th=2;
gg=3;
pp=1/2;
lr=1/10;
l2=1/5;

coupled=FullSimplify[
 th-lr pp (gg+l2 th)
];

decoupled=FullSimplify[
 (1-lr l2) th-lr pp gg
];

{
 eg,
 var,
 m1,
 v1,
 mhat,
 vhat,
 FullSimplify[mhat/Sqrt[vhat]],
 ng,
 gclip,
 FullSimplify[Sqrt[gclip.gclip]],
 coupled,
 decoupled,
 FullSimplify[coupled-decoupled],
 1-eta lam,
 n sigw^2 q,
 n sigw^2 q/2
}
\`\`\`

## Actual replay output

\[
\{
x,\,
1,\,
3/10,\,
9/100,\,
3,\,
9,\,
1,\,
5,\,
(6/5,8/5),\,
2,\,
183/100,\,
181/100,\,
1/50,\,
1-\eta\lambda,\,
nq\sigma_w^2,\,
nq\sigma_w^2/2
\}.
\]

## Claim boundary

This witness checks exact toy algebra only.

It does not establish empirical optimizer superiority, convergence of Adam on arbitrary objectives, unbiasedness after clipping, or distributional preservation in deep nonlinear networks.
