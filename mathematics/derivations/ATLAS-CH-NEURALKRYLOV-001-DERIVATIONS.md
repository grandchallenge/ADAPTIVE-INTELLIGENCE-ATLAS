# ATLAS-CH-NEURALKRYLOV-001 — Derivation Packet

## Scope

This packet proves the exact fixed-left-preconditioned finite witness used by NEURALKRYLOV-001 and the low-dimension failure control.

It does not prove convergence of arbitrary learned nonlinear transport mechanisms.

## D1. Original local solve

Use

\[
A=
\begin{pmatrix}
1&0\\
0&4
\end{pmatrix},
\qquad
b=
\begin{pmatrix}
1\\1
\end{pmatrix}.
\]

The exact solution is

\[
x^\star=A^{-1}b
=
\begin{pmatrix}
1\\1/4
\end{pmatrix}.
\]

## D2. Fixed left preconditioner

Let

\[
M=
\begin{pmatrix}
1&0\\
0&2
\end{pmatrix},
\qquad
M^{-1}=
\begin{pmatrix}
1&0\\
0&1/2
\end{pmatrix}.
\]

Left preconditioning gives

\[
M^{-1}Ax=M^{-1}b.
\]

Define

\[
B=M^{-1}A=
\begin{pmatrix}
1&0\\
0&2
\end{pmatrix},
\]

and

\[
c=M^{-1}b=
\begin{pmatrix}
1\\1/2
\end{pmatrix}.
\]

The exact solution is unchanged:

\[
Bx^\star=c.
\]

## D3. First Krylov space

With \(x_0=0\),

\[
\mathcal K_1(B,c)=\operatorname{span}\{c\}.
\]

Restrict candidate solutions to

\[
x=\alpha c.
\]

The transformed residual is

\[
\widehat r(\alpha)=c-\alpha Bc.
\]

Since

\[
Bc=
\begin{pmatrix}
1\\1
\end{pmatrix},
\]

we obtain

\[
\widehat r(\alpha)
=
\begin{pmatrix}
1-\alpha\\
1/2-\alpha
\end{pmatrix}.
\]

## D4. Best transformed-residual scalar

Minimize

\[
f(\alpha)
=
(1-\alpha)^2+(1/2-\alpha)^2.
\]

Differentiate:

\[
f'(\alpha)
=
2(\alpha-1)+2(\alpha-1/2)
=
4\alpha-3.
\]

Thus

\[
\boxed{
\alpha^\star=\frac34.
}
\]

The second derivative is positive:

\[
f''(\alpha)=4.
\]

Hence this is the unique minimizer.

## D5. One-step approximation

The best \(\mathcal K_1\) point is

\[
x_1
=
\frac34 c
=
\begin{pmatrix}
3/4\\
3/8
\end{pmatrix}.
\]

Its transformed residual is

\[
\widehat r_1
=
c-Bx_1
=
\begin{pmatrix}
1/4\\
-1/4
\end{pmatrix}.
\]

Therefore

\[
\boxed{
\|\widehat r_1\|_2^2
=
\frac1{16}+\frac1{16}
=
\frac18.
}
\]

## D6. Original residual

The original residual is

\[
r_1=b-Ax_1.
\]

Since

\[
Ax_1
=
\begin{pmatrix}
3/4\\
3/2
\end{pmatrix},
\]

we obtain

\[
r_1
=
\begin{pmatrix}
1/4\\
-1/2
\end{pmatrix}.
\]

Hence

\[
\boxed{
\|r_1\|_2^2
=
\frac1{16}+\frac14
=
\frac5{16}.
}
\]

Also

\[
\widehat r_1=M^{-1}r_1,
\]

as required.

## D7. True error

The exact error is

\[
e_1=x^\star-x_1
=
\begin{pmatrix}
1/4\\
-1/8
\end{pmatrix}.
\]

Thus

\[
\boxed{
\|e_1\|_2^2
=
\frac1{16}+\frac1{64}
=
\frac5{64}.
}
\]

And indeed

\[
Ae_1=r_1.
\]

Residual and error remain distinct.

## D8. Second Krylov space

Now

\[
\mathcal K_2(B,c)
=
\operatorname{span}\{c,Bc\}.
\]

The two generating columns are

\[
\begin{pmatrix}
1\\1/2
\end{pmatrix},
\qquad
\begin{pmatrix}
1\\1
\end{pmatrix}.
\]

Their determinant is

\[
1-\frac12
=
\boxed{\frac12}.
\]

Therefore they are linearly independent and

\[
\boxed{
\mathcal K_2(B,c)=\mathbb R^2.
}
\]

## D9. Exact solution in the second space

Solve

\[
x^\star=\beta c+\gamma Bc.
\]

The equations are

\[
\beta+\gamma=1,
\]

\[
\frac12\beta+\gamma=\frac14.
\]

Subtracting gives

\[
\frac12\beta=\frac34,
\]

hence

\[
\beta=\frac32,
\qquad
\gamma=-\frac12.
\]

Therefore

\[
\boxed{
x^\star
=
\frac32 c
-
\frac12 Bc.
}
\]

Thus the exact solution lies in \(\mathcal K_2\).

## D10. Exact two-step solve

Because the exact solution is available in the trial space, a residual-minimizing solve over \(\mathcal K_2\) can attain:

\[
\widehat r_2=0.
\]

Then:

\[
r_2=0,
\]

and because \(A\) is invertible:

\[
e_2=0.
\]

Thus:

\[
\boxed{
\|\widehat r_2\|_2^2
=
\|r_2\|_2^2
=
\|e_2\|_2^2
=
0.
}
\]

## D11. Strict short-horizon improvement

At horizon one:

\[
\|r_1\|_2^2=\frac5{16},
\qquad
\|e_1\|_2^2=\frac5{64}.
\]

At horizon two:

\[
\|r_2\|_2^2=0,
\qquad
\|e_2\|_2^2=0.
\]

Hence:

\[
\boxed{
\text{one additional operator-generated direction strictly improves the declared solve}.
}
\]

This is a finite witness, not a dimension-independent rate theorem.

## D12. Exact task-readout firewall

Define

\[
w=
\begin{pmatrix}
1\\2
\end{pmatrix}.
\]

For the exact solution:

\[
w^\top x^\star
=
1+2(1/4)
=
\frac32.
\]

For the non-exact one-step approximation:

\[
w^\top x_1
=
\frac34+2\frac38
=
\frac34+\frac34
=
\frac32.
\]

Therefore

\[
\boxed{
w^\top x_1=w^\top x^\star
}
\]

while

\[
r_1\neq0
\]

and

\[
e_1\neq0.
\]

Thus exact downstream readout does not imply exact linear solve.

## D13. Bad low-dimension control

Use

\[
B_{\rm bad}
=
\begin{pmatrix}
1&0\\
0&10
\end{pmatrix},
\qquad
c_{\rm bad}
=
\begin{pmatrix}
1\\1
\end{pmatrix}.
\]

Again:

\[
\mathcal K_1(B_{\rm bad},c_{\rm bad})
=
\operatorname{span}\{c_{\rm bad}\}.
\]

Restrict:

\[
x=\alpha c_{\rm bad}.
\]

Then:

\[
B_{\rm bad}c_{\rm bad}
=
\begin{pmatrix}
1\\10
\end{pmatrix}.
\]

The residual is

\[
r(\alpha)
=
\begin{pmatrix}
1-\alpha\\
1-10\alpha
\end{pmatrix}.
\]

## D14. Bad-control best scalar

Minimize:

\[
g(\alpha)
=
(1-\alpha)^2+(1-10\alpha)^2.
\]

Differentiate:

\[
g'(\alpha)
=
2(\alpha-1)+20(10\alpha-1)
=
202\alpha-22.
\]

Thus:

\[
\boxed{
\alpha_{\rm bad}
=
\frac{11}{101}.
}
\]

## D15. Bad-control residual

Substitution gives:

\[
r_{\rm bad}
=
\begin{pmatrix}
1-11/101\\
1-110/101
\end{pmatrix}
=
\begin{pmatrix}
90/101\\
-9/101
\end{pmatrix}.
\]

Therefore:

\[
\|r_{\rm bad}\|_2^2
=
\frac{8100+81}{10201}
=
\frac{8181}{10201}
=
\boxed{
\frac{81}{101}
}.
\]

This remains large despite the one-dimensional trial space.

Hence:

\[
\boxed{
\text{low Krylov dimension}
\not\Rightarrow
\text{small residual}.
}
\]

## D16. Local linearization boundary

Suppose a representation map is

\[
z^+=\Phi(z).
\]

At base state \(z_0\), the Jacobian

\[
J_\Phi(z_0)
\]

is a local differential object.

If a chapter defines

\[
A_{z_0}=I-J_\Phi(z_0),
\]

then a Krylov space built from \(A_{z_0}\) is a Krylov space for that declared linear operator.

It is not a Krylov space for the nonlinear map \(\Phi\) itself.

## D17. State-dependent operator boundary

If the representation changes to \(z_1\) and one recomputes:

\[
A_{z_1},
\]

then generally:

\[
A_{z_1}\neq A_{z_0}.
\]

A sequence of directions generated under changing operators is not automatically one classical Krylov sequence:

\[
\operatorname{span}
\{r,Ar,A^2r,\ldots\}.
\]

Any flexible/nonstationary method requires separate semantics.

## D18. Preconditioner boundary

For fixed left preconditioner \(M\),

\[
\widehat r=M^{-1}r.
\]

If \(M\) becomes learned or state-dependent:

\[
M=M_\theta(z),
\]

then the effective transformed operator can change with the state.

Fixed-preconditioner identities must not be transferred without proving the needed hypotheses.

## D19. Metric separation

The exact witness contains four distinct numerical facts:

- transformed residual squared \(=1/8\);
- original residual squared \(=5/16\);
- true error squared \(=5/64\);
- downstream readout error \(=0\).

Therefore no pair of these metrics can be silently identified.

A representation-level metric would be yet another declared object.

## D20. Finite-precision and restart boundary

The exact witness uses exact rational arithmetic.

A practical implementation may lose basis orthogonality or linear independence in floating point.

Likewise, truncation/restart can discard useful directions.

The positive witness already shows that truncating at \(m=1\) loses a direction needed for the exact solve, while \(m=2\) recovers it.

No universal restart rule follows.

## Durable propositions

1. The exact fixed-left-preconditioned witness has a unique best \(K_1\) transformed-residual scalar \(\alpha=3/4\).
2. At \(K_1\), transformed residual squared is \(1/8\), original residual squared is \(5/16\), and true error squared is \(5/64\).
3. \(K_2(B,c)=\mathbb R^2\).
4. The exact solution is \((3/2)c-(1/2)Bc\).
5. A two-dimensional residual-minimizing solve can therefore be exact.
6. The bad one-dimensional control has minimum residual squared \(81/101\).
7. Low trial-space dimension alone is not a convergence certificate.
8. The one-step positive witness has exact downstream readout \(w^\top x\) despite nonzero solve residual/error.
9. A local Jacobian-derived Krylov construction is not a global nonlinear convergence theorem.
10. Learned/state-dependent preconditioners require separate analysis.

## Claim boundary

This packet proves only exact finite linear-algebra identities for the declared operators and readout. It does not establish that a real learned representation operator has these matrices, that a learned Krylov block converges globally, or that reducing linear-solve residual necessarily improves representation or task quality.
