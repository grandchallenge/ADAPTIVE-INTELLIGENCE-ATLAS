# Chapter Specification — ATLAS-CH-SPECTRALSHAPE-001

## Identity

**Title:** Spectral Shaping  
**Part:** Optimization  
**Status target:** draft-v0.1  
**Implementation issue:** #272  
**Protected baseline:** c17966203c5a3d7c5bbb629caa2d3b2ae87d81e0

## Hard prerequisites

### ATLAS-CH-MATRIXOPT-001 / AUDIT-046

May inherit:

- SVD and polar-factor language;
- rectangular semi-orthogonality;
- matrix-aware update geometry;
- norm-dependent steepest directions;
- exact-versus-approximate singular-value transformations;
- the distinction between singular-value flattening and general spectral shaping.

May not inherit the claim that a flat spectrum is universally optimal.

### ATLAS-CH-NONNORMAL-001 / AUDIT-001

May inherit:

- normal versus non-normal operator distinctions;
- exact transient-growth witnesses;
- resolvent and pseudospectral language;
- matched-eigenvalue controls.

May not infer finite-horizon behavior from eigenvalues alone.

Exact prerequisite identities and claim boundaries are frozen in:

sources/source-locks/ATLAS-CH-SPECTRALSHAPE-001.yaml

## Core interface

For a full-rank matrix update

\[
G=U\Sigma V^\top,
\]

with

\[
\Sigma=\operatorname{diag}(\sigma_1,\dots,\sigma_r),
\]

define a singular-value shaping map

\[
T_f(G)
=
U f(\Sigma)V^\top,
\]

where

\[
f(\Sigma)
=
\operatorname{diag}
(
f(\sigma_1),\dots,f(\sigma_r)
).
\]

The map \(f\) must be declared.

Different choices correspond to different operations.

## Four distinct operations

The chapter must distinguish:

1. scalar normalization;
2. clipping/conditioning;
3. polar flattening;
4. explicit non-flat target shaping.

These may all alter the spectrum while serving different objectives.

## Exact conditioning witness

Use

\[
G=
\begin{pmatrix}
4&0\\
0&1
\end{pmatrix}.
\]

Its singular values are

\[
(4,1),
\]

so

\[
\boxed{
\kappa_2(G)=4.
}
\]

### Scalar normalization

Normalize by the operator norm:

\[
T_{\rm scale}(G)
=
\frac{G}{\|G\|_2}
=
\begin{pmatrix}
1&0\\
0&1/4
\end{pmatrix}.
\]

Its singular values are

\[
(1,1/4),
\]

and therefore

\[
\boxed{
\kappa_2(T_{\rm scale}(G))=4.
}
\]

Global scale changed.

Conditioning did not.

### Upper clipping

Use

\[
f_{\rm clip}(\sigma)=\min(\sigma,2).
\]

Then

\[
T_{\rm clip}(G)
=
\begin{pmatrix}
2&0\\
0&1
\end{pmatrix}.
\]

Its condition number is

\[
\boxed{
\kappa_2(T_{\rm clip}(G))=2.
}
\]

This improves the singular-value ratio without flattening it.

### Polar flattening

For positive singular values, define

\[
f_{\rm polar}(\sigma)=1.
\]

Then

\[
T_{\rm polar}(G)=I_2.
\]

Hence

\[
\boxed{
\kappa_2(T_{\rm polar}(G))=1.
}
\]

All nonzero singular values are flattened.

### Explicit non-flat target profile

Declare target singular values

\[
\tau=(3,2).
\]

Then

\[
T_\tau(G)
=
\begin{pmatrix}
3&0\\
0&2
\end{pmatrix},
\]

with

\[
\boxed{
\kappa_2(T_\tau(G))=\frac32.
}
\]

This is intentional spectral shaping without flattening.

## Non-equivalence theorem for the witness

For the same \(G\),

\[
\boxed{
\text{normalization}
\neq
\text{clipping}
\neq
\text{polar flattening}
\neq
\text{non-flat target shaping}.
}
\]

They produce different singular-value profiles:

\[
(1,1/4),
\qquad
(2,1),
\qquad
(1,1),
\qquad
(3,2).
\]

## Conditioning is not scale

Scalar multiplication by any nonzero \(c\) sends

\[
\sigma_i\mapsto |c|\sigma_i.
\]

Therefore:

\[
\kappa_2(cG)
=
\frac{|c|\sigma_{\max}}{|c|\sigma_{\min}}
=
\kappa_2(G).
\]

Thus global normalization cannot improve a full-rank matrix's condition number merely by rescaling it.

## Clipping is not flattening

Upper clipping preserves smaller singular values below the threshold.

Polar flattening replaces every positive singular value by one.

Therefore:

\[
\boxed{
f_{\rm clip}
\neq
f_{\rm polar}.
}
\]

Their equality on some accidental finite input would not make the maps identical.

## Non-flat targets are legitimate objects

A target spectrum can encode a desired relative weighting among directions.

For example:

\[
(3,2)
\]

retains directional anisotropy.

The chapter must not claim that this target is universally desirable.

Target choice is problem-relative.

## Condition number scope

The standard spectral condition number

\[
\kappa_2(G)
=
\frac{\sigma_{\max}(G)}
{\sigma_{\min}(G)}
\]

is finite only when the relevant full-rank object has positive smallest singular value.

Rank-deficient cases require explicit support restriction, pseudoinverse conventions, regularization, or another declared metric.

## Non-normal control

Use

\[
A=
\begin{pmatrix}
1/2&2\\
0&1/2
\end{pmatrix},
\qquad
N=
\frac12 I_2.
\]

Both have eigenvalues

\[
\{1/2,1/2\}.
\]

But for

\[
e_2=
\begin{pmatrix}
0\\1
\end{pmatrix},
\]

we have

\[
Ae_2=
\begin{pmatrix}
2\\1/2
\end{pmatrix},
\]

so

\[
\boxed{
\|Ae_2\|_2^2=\frac{17}{4}.
}
\]

For the normal control,

\[
Ne_2=
\begin{pmatrix}
0\\1/2
\end{pmatrix},
\]

so

\[
\boxed{
\|Ne_2\|_2^2=\frac14.
}
\]

Equal eigenvalues do not imply equal finite-horizon response.

## Exact pseudospectral separation

For the upper-triangular family inherited from NONNORMAL,

\[
A=
\begin{pmatrix}
a&K\\
0&a
\end{pmatrix},
\]

the closed 2-norm \(\varepsilon\)-pseudospectral boundary is

\[
|z-a|^2
=
\varepsilon(\varepsilon+K).
\]

Set

\[
a=\frac12,
\qquad
K=2,
\qquad
\varepsilon=\frac14.
\]

Then the non-normal pseudospectral radius around \(a\) is

\[
\sqrt{
\frac14
\left(
\frac14+2
\right)
}
=
\sqrt{\frac9{16}}
=
\boxed{\frac34}.
\]

For

\[
N=\frac12I,
\]

the corresponding normal pseudospectral radius is

\[
\boxed{\frac14}.
\]

Thus matched eigenvalues coexist with different perturbation sensitivity.

## Why this matters for spectral shaping

If a matrix-aware optimizer shapes the singular spectrum of an instantaneous update, that does not automatically specify:

- the state-transition Jacobian;
- the optimizer-state map;
- the linearized training dynamics;
- the pseudospectrum of those dynamics.

Therefore:

\[
\boxed{
\text{instantaneous update spectrum}
\not\Rightarrow
\text{training-dynamics spectrum}.
}
\]

## Stateful optimizer boundary

A stateful optimizer has coupled state:

\[
S_{t+1}
=
\Phi(S_t,G_t),
\]

and update:

\[
\Delta_t
=
\Psi(S_{t+1},G_t).
\]

The spectral shape of \(\Delta_t\) at one step does not identify the spectrum of the joint-state Jacobian.

That belongs to optimizer-state dynamics.

## Convergence boundary

A lower condition number for an update or preconditioned matrix can be a useful local numerical diagnostic.

But:

\[
\boxed{
\text{better instantaneous conditioning}
\not\Rightarrow
\text{faster nonlinear optimizer convergence}.
}
\]

A convergence claim needs the actual optimization problem, update law, state, step size, geometry, and assumptions.

## Task-quality boundary

A spectrally shaped update can improve one matrix metric while harming a downstream objective.

Conversely, a task can improve despite a less favorable singular-value ratio.

Thus:

\[
\boxed{
\text{spectral-shape quality}
\not\Rightarrow
\text{task quality}.
}
\]

## Direction preservation

A shaping map of the form

\[
U f(\Sigma)V^\top
\]

preserves the singular-vector frames \(U,V\) while changing singular values.

A more general matrix transform may also change singular vectors.

The chapter must state which object is being shaped.

## Sign and rank boundaries

For rectangular or signed matrices, polar factors and SVDs require the usual support/rank conventions inherited from MATRIXOPT.

Zero singular values cannot be turned into exact invertibility without adding regularization or altering rank.

Any such operation must be explicit.

## Spectral shaping as design

The chapter may frame spectral shaping as choosing a target function:

\[
f:\sigma\mapsto f(\sigma).
\]

Possible design goals include:

- global scale control;
- cap large directions;
- lift small directions;
- flatten nonzero singular values;
- impose a target anisotropy;
- preserve a desired band.

These are design choices, not synonyms.

## Required non-implications

The manuscript must explicitly reject:

\[
\text{normalization}
\not\Rightarrow
\text{better conditioning},
\]

\[
\text{conditioning}
\not\Rightarrow
\text{flattening},
\]

\[
\text{flat spectrum}
\not\Rightarrow
\text{universal optimizer quality},
\]

\[
\text{better update condition number}
\not\Rightarrow
\text{faster nonlinear convergence},
\]

\[
\text{instantaneous update spectrum}
\not\Rightarrow
\text{optimizer-state dynamics},
\]

\[
\text{eigenvalue shape}
\not\Rightarrow
\text{non-normal transient control},
\]

and:

\[
\text{spectral-shape quality}
\not\Rightarrow
\text{task quality}.
\]

## Reader outcomes

A reader should be able to:

1. define a singular-value shaping map;
2. distinguish scale normalization from conditioning;
3. reproduce the exact \(G=\operatorname{diag}(4,1)\) witness;
4. compute condition numbers \(4,4,2,1,3/2\);
5. distinguish clipping from polar flattening;
6. explain a non-flat target spectrum;
7. reproduce the exact non-normal interface-response control;
8. reproduce the \(\varepsilon=1/4\) pseudospectral radii \(3/4\) and \(1/4\);
9. explain why update spectra do not identify optimizer-state dynamics;
10. state the convergence/task-quality boundaries.

## Required artifacts

- source lock;
- specification;
- derivation packet;
- exact computational witness;
- reader manuscript;
- Chapter Ledger promotion;
- Source Register entry;
- transaction receipt;
- mandatory post-draft audit.

## References used in this chapter

No new external academic authority is added.

Matrix-update and polar/SVD authority is inherited through audited ATLAS-CH-MATRIXOPT-001.

Non-normal transient-growth and pseudospectral authority is inherited through audited ATLAS-CH-NONNORMAL-001.

Exact prerequisite identities and claim boundaries are recorded in:

sources/source-locks/ATLAS-CH-SPECTRALSHAPE-001.yaml
