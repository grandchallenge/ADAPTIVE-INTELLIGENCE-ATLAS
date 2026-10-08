# Spectral Shaping
<!-- ATLAS-CH-SPECTRALSHAPE-001 -->

**Epistemic status:** audited Matrix-Aware Optimization and Non-normality substrates + Atlas-owned exact finite spectral-shaping witnesses.  
**Specification:** manuscript/specifications/ATLAS-CH-SPECTRALSHAPE-001.md  
**Derivation packet:** mathematics/derivations/ATLAS-CH-SPECTRALSHAPE-001-DERIVATIONS.md  
**Computational witness:** mathematics/computational-witnesses/ATLAS-CW-SPECTRALSHAPE-001.md  
**Source lock:** sources/source-locks/ATLAS-CH-SPECTRALSHAPE-001.yaml

Spectral manipulation is often discussed as though it were one operation.

It is not.

A matrix update can be:

- normalized;
- clipped;
- conditioned;
- flattened;
- or deliberately reshaped toward a non-flat target.

Those operations can have different mathematical meanings even when they all alter singular values.

The governing rule is:

\[
\boxed{
\text{declare the target spectral map before interpreting the result}.
}
\]

## 1. The handoff from Matrix-Aware Optimization

MATRIXOPT already gives the Atlas:

- SVD language;
- polar factors;
- rectangular semi-orthogonality;
- matrix preconditioning;
- exact-versus-approximate singular-value transformations;
- the key boundary that polar flattening is not all spectral shaping.

SPECTRALSHAPE starts where that chapter deliberately stopped.

## 2. The handoff from Non-normality

NONNORMAL adds a second constraint.

Even if eigenvalues look benign, finite-horizon behavior can be very different when the operator is non-normal.

Therefore an instantaneous update spectrum cannot be promoted directly into a dynamical guarantee.

## 3. A general shaping map

Let

\[
G=U\Sigma V^\top,
\]

with singular values

\[
\sigma_1,\dots,\sigma_r.
\]

A singular-value shaping rule has the form

\[
T_f(G)
=
U f(\Sigma)V^\top,
\]

where \(f\) acts on the singular values. When \(G\) is rank-deficient, the map must specify its behavior on zero singular directions. Taking \(f(0)=0\) leaves those directions zero and yields an SVD-independent singular-value transform. If \(f(0)\ne0\), a rule also needs a declared pairing of the left and right nullspaces; the zero-singular-vector choices in an SVD of \(G\) are not unique.

As a counterexample, let \(G=\operatorname{diag}(1,0)\) and \(f(1)=f(0)=1\). Two valid SVDs are \(U=V=I_2\) and \(U=\operatorname{diag}(1,-1),V=I_2\), both with \(\Sigma=\operatorname{diag}(1,0)\). They give different transformed matrices, \(I_2\) and \(\operatorname{diag}(1,-1)\). Hence a rank-increasing rule requires extra structure. The full-rank witnesses below are unaffected.

Different well-defined \(f\) give different update geometries.

## 4. Exact witness matrix

Use

\[
G=
\begin{pmatrix}
4&0\\
0&1
\end{pmatrix}.
\]

Its singular values are:

\[
(4,1).
\]

Hence:

\[
\boxed{
\kappa_2(G)=4.
}
\]

This one matrix is enough to distinguish four common operations.

## 5. Scalar normalization changes scale

Normalize by the operator norm:

\[
G_{\rm scale}
=
\frac{G}{\|G\|_2}
=
\begin{pmatrix}
1&0\\
0&1/4
\end{pmatrix}.
\]

The condition number remains:

\[
\boxed{
\kappa_2(G_{\rm scale})=4.
}
\]

So:

\[
\boxed{
\text{normalization}
\not\Rightarrow
\text{better conditioning}.
}
\]

A global scalar multiplies every singular value by the same amount.

Their ratio is unchanged.

## 6. Clipping can change conditioning

Now cap singular values at \(2\):

\[
f_{\rm clip}(\sigma)
=
\min(\sigma,2).
\]

Then:

\[
G_{\rm clip}
=
\begin{pmatrix}
2&0\\
0&1
\end{pmatrix}.
\]

Thus:

\[
\boxed{
\kappa_2(G_{\rm clip})=2.
}
\]

The spectrum is still non-flat.

Only the large mode was clipped.

## 7. Polar flattening is stronger

For a full-rank square positive diagonal matrix, the polar factor replaces every nonzero singular value by one.

Thus:

\[
G_{\rm polar}=I_2.
\]

Hence:

\[
\boxed{
\kappa_2(G_{\rm polar})=1.
}
\]

This is complete nonzero singular-value flattening.

## 8. A non-flat target is another operation

Suppose we deliberately choose target singular values:

\[
(3,2).
\]

Then:

\[
G_\tau
=
\begin{pmatrix}
3&0\\
0&2
\end{pmatrix}.
\]

Its condition number is:

\[
\boxed{
\kappa_2(G_\tau)=\frac32.
}
\]

This is neither normalization, clipping, nor flattening.

It is explicit spectral design.

## 9. The four maps are not synonyms

For the same input \(G\), the shaped spectra are:

\[
(1,1/4),
\]

\[
(2,1),
\]

\[
(1,1),
\]

and

\[
(3,2).
\]

Therefore:

\[
\boxed{
\text{scale control}
\neq
\text{clipping}
\neq
\text{flattening}
\neq
\text{target shaping}.
}
\]

## 10. Better condition number is not automatically better optimization

On this witness, the condition numbers are:

\[
4,\quad4,\quad2,\quad1,\quad3/2.
\]

That is an exact matrix statement.

It is not a universal optimizer ranking.

A nonlinear optimizer also depends on:

- objective geometry;
- step size;
- optimizer state;
- stochasticity;
- parameterization;
- update interaction across steps.

## 11. Flat is not automatically best

The polar spectrum:

\[
(1,1)
\]

is maximally flat.

But there may be reasons to preserve anisotropy.

A target:

\[
(3,2)
\]

retains directional preference.

The Atlas therefore treats the target spectrum as a design object rather than an article of faith.

## 12. Conditioning is only one objective

Possible spectral goals include:

- cap large modes;
- raise small modes;
- reduce condition number;
- preserve relative scale in a band;
- remove scale entirely;
- impose a desired anisotropy.

These objectives need not agree.

## 13. Rank matters

If a singular value is zero, the standard full-space condition number is infinite.

Changing a zero singular value to a positive one changes rank.

That is no longer mere rescaling.

It is a structural intervention and must be declared as such.

## 14. Singular vectors matter too

A map

\[
U f(\Sigma)V^\top
\]

changes singular values while retaining the singular-vector frames.

A more general transform can also rotate \(U\) or \(V\).

Two matrices with the same singular values can therefore still behave differently relative to a particular interface.

Spectral shape is not the whole operator.

## 15. Non-normality supplies the dynamical warning

Consider:

\[
A=
\begin{pmatrix}
1/2&2\\
0&1/2
\end{pmatrix},
\qquad
N=
\frac12I.
\]

Both have eigenvalues:

\[
\{1/2,1/2\}.
\]

If eigenvalues were the whole story, their short-time behavior would look alike.

It does not.

## 16. Same eigenvalues, different one-step response

Probe both matrices with:

\[
e_2=(0,1)^\top.
\]

Then:

\[
Ae_2=(2,1/2)^\top,
\]

so:

\[
\boxed{
\|Ae_2\|_2^2=\frac{17}{4}.
}
\]

But:

\[
Ne_2=(0,1/2)^\top,
\]

so:

\[
\boxed{
\|Ne_2\|_2^2=\frac14.
}
\]

Equal eigenvalues do not imply equal interface response.

## 17. Pseudospectra separate them further

For the upper-triangular non-normal family inherited from NONNORMAL, the exact closed 2-norm \(\varepsilon\)-pseudospectral radius around the repeated eigenvalue is:

\[
r_A
=
\sqrt{\varepsilon(\varepsilon+K)}.
\]

Set:

\[
K=2,
\qquad
\varepsilon=\frac14.
\]

Then:

\[
\boxed{
r_A=\frac34.
}
\]

For the normal scalar matrix:

\[
\boxed{
r_N=\frac14.
}
\]

Matched eigenvalues coexist with a threefold difference in this pseudospectral radius.

## 18. Why that matters for optimizer updates

Suppose an optimizer shapes the singular spectrum of an instantaneous update matrix:

\[
\Delta_t.
\]

That says something about \(\Delta_t\).

It does not automatically say anything about the spectrum or pseudospectrum of the optimizer's joint state transition.

Those are different operators.

## 19. Stateful optimizers enlarge the object

A stateful optimizer has:

\[
S_{t+1}
=
\Phi(S_t,G_t),
\]

and perhaps:

\[
W_{t+1}
=
W_t+\Psi(S_{t+1},G_t).
\]

The relevant local dynamical operator is then a Jacobian on the coupled state:

\[
(W,S).
\]

The singular values of one instantaneous parameter update are not that Jacobian.

## 20. Spectral shaping is not optimizer-state dynamics

Therefore:

\[
\boxed{
\text{instantaneous update spectrum}
\not\Rightarrow
\text{optimizer-state dynamics}.
}
\]

This boundary is mandatory.

It prevents a useful matrix diagnostic from becoming an unsupported dynamical theorem.

## 21. Better conditioning is not convergence

Even if a spectral map reduces:

\[
\kappa_2(G),
\]

the nonlinear training trajectory may improve, worsen, or remain unchanged.

A convergence theorem needs the actual update law and assumptions.

So:

\[
\boxed{
\text{better update condition number}
\not\Rightarrow
\text{faster nonlinear convergence}.
}
\]

## 22. Task quality is another layer

A shaped update can have:

- a lower condition number;
- a flatter spectrum;
- smaller operator norm;

and still harm the downstream objective.

Conversely, task quality can improve without a flatter update spectrum.

Thus:

\[
\boxed{
\text{spectral-shape quality}
\not\Rightarrow
\text{task quality}.
}
\]

## 23. A practical reporting protocol

For a spectral-shaping method, report separately:

1. the matrix/operator being shaped;
2. the SVD or spectral object being used;
3. the shaping function \(f\);
4. the target spectrum or clipping rule;
5. condition number before/after;
6. rank changes, if any;
7. singular-vector changes, if any;
8. optimizer-state semantics;
9. dynamical diagnostics;
10. downstream task metrics.

This prevents one spectral statistic from impersonating the entire optimization process.

## 24. What a flat spectrum actually certifies

For a full-rank square matrix, flattening the nonzero singular values to one certifies:

\[
\kappa_2=1.
\]

It does not certify:

- minimum training loss;
- good generalization;
- stable coupled dynamics;
- absence of non-normality elsewhere;
- correct task behavior.

The certificate is exactly the matrix property it proves.

## 25. What a non-flat target actually certifies

A target such as:

\[
(3,2)
\]

certifies only that the chosen singular-value profile has been imposed.

Whether this geometry is useful is an empirical or theoretical question about the downstream problem.

## 26. Atlas non-implications

SPECTRALSHAPE rejects:

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
\text{better update conditioning}
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

## 27. Atlas connections

**Matrix-Aware Optimization.**  
Supplies SVD/polar update geometry and the exact flattening boundary.

**Normality, Pseudospectra, and Transient Growth.**  
Supplies the warning that spectral eigenvalue information may be insufficient for finite-horizon dynamics.

**Optimizer-State Dynamics.**  
Owns the coupled model–optimizer state and its Jacobian.

**Spectral and Operator Diagnostics.**  
Can diagnose operator behavior but does not convert a spectral signature into mechanistic evidence.

## 28. Closing view

Spectral shaping is best understood as an explicit design map:

\[
\boxed{
G
\mapsto
U f(\Sigma)V^\top.
}
\]

The important question is not:

> did the spectrum change?

It is:

> which spectrum, by what map, toward what target, for what objective, and with what separate evidence about dynamics and task behavior?

The exact witness gives four different answers from one input matrix.

That is the point.

## References used in this chapter

No new external academic authority is added.

Matrix-update and SVD/polar authority is inherited through audited ATLAS-CH-MATRIXOPT-001.

Non-normal transient-growth and pseudospectral authority is inherited through audited ATLAS-CH-NONNORMAL-001.

Exact prerequisite identities and claim boundaries are recorded in:

sources/source-locks/ATLAS-CH-SPECTRALSHAPE-001.yaml
