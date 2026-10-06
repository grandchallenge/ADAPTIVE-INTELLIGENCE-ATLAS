# Chapter Specification — ATLAS-CH-TRANSPORT-001

## Identity

**Title:** Representation as Transport  
**Part:** Neural Computation as Dynamics  
**Status:** specification-ready.  
**Epistemic class:** established manifold/dynamical mathematics + audited prerequisite inheritance + Atlas synthesis.

## Chapter contract

Synthesize geometry, residual computation, and constrained motion into a transport view of representation updates.

The chapter must make the transport language precise enough to be useful while refusing four common conflations:

- representation-state transport is not vector transport;
- representation-state transport is not parallel transport;
- representation-state transport is not optimal transport;
- a finite learned composition is not automatically an exact ODE flow.

## Hard prerequisites

- \`ATLAS-CH-NORMREP-001\` / \`AUDIT-005\`;
- \`ATLAS-CH-SPLIT-001\` / \`AUDIT-036\`.

Exact prerequisite identities and source authority are locked in:

\`sources/source-locks/ATLAS-CH-TRANSPORT-001.yaml\`.

## Reader outcome

A reader should be able to:

1. model a representation trajectory as a sequence of declared state maps;
2. distinguish discrete stage index from physical or continuous time;
3. distinguish unconstrained residual motion from constraint-preserving motion;
4. explain why a tangent vector belongs to a tangent space at a specified base point;
5. distinguish retraction, exponential map, vector transport, and parallel transport;
6. explain how stage ordering can change a constrained representation path;
7. identify when an ODE interpretation is explicit and when it is only an analogy;
8. state what information is lost when a constraint such as unit norm is imposed;
9. hand a well-defined transport operator/interface to the downstream Neural Krylov chapter.

## Formal spine

Let representation state at stage \(k\) be

\[
z_k\in\mathcal Z_k.
\]

A general stage map is

\[
z_{k+1}=\Phi_k(z_k).
\]

When all stages share one state space \(\mathcal Z\), the depth-\(K\) representation is

\[
z_K=(\Phi_{K-1}\circ\cdots\circ\Phi_0)(z_0).
\]

This finite composition is the primary transport object.

A residual stage has the form

\[
\Phi_k(z)=z+F_k(z),
\]

or, with explicit step scale,

\[
\Phi_{k,h}(z)=z+hF_k(z).
\]

Neither formula by itself proves the existence of a unique continuous-time generator.

### Constrained state

For a manifold \(M\subseteq\mathbb R^n\), a constrained update should distinguish:

- a tangent proposal \(\xi_k\in T_{z_k}M\);
- an endpoint map such as a retraction

\[
z_{k+1}=R_{z_k}(\xi_k)\in M.
\]

For the sphere,

\[
R_u(\xi)=\frac{u+\xi}{\|u+\xi\|_2},
\qquad
u^\top\xi=0.
\]

### Tangent-data transport

A tangent vector

\[
v_k\in T_{z_k}M
\]

is attached to the base point \(z_k\). After moving to \(z_{k+1}\), simply reusing the same ambient coordinates need not produce an element of \(T_{z_{k+1}}M\).

A vector transport, projection, or parallel-transport rule is an additional object. It is not supplied automatically by the state update.

## Exact finite witnesses

### Witness A — retraction versus exponential map

On \(S^1\), take

\[
u=(1,0),
\qquad
\xi=(0,1).
\]

The normalized retraction gives

\[
R_u(\xi)=\frac{(1,1)}{\sqrt2},
\]

whose angular displacement is \(\pi/4\).

The unit-speed exponential/geodesic endpoint for tangent vector \(\xi\) at unit time is

\[
\operatorname{Exp}_u(\xi)=(\cos 1,\sin 1),
\]

whose angular displacement is \(1\) radian.

Thus

\[
R_u(\xi)\neq \operatorname{Exp}_u(\xi).
\]

Both endpoints lie on the sphere. Feasibility does not identify the path construction.

### Witness B — old tangent data becomes non-tangent

At

\[
u_0=(1,0),
\qquad
v_0=(0,1),
\]

we have \(u_0^\top v_0=0\).

After retraction with the same increment,

\[
u_1=\frac{(1,1)}{\sqrt2}.
\]

Then

\[
u_1^\top v_0=\frac1{\sqrt2}\neq0.
\]

So \(v_0\notin T_{u_1}S^1\).

Its orthogonal tangent projection is

\[
P_{u_1}v_0
=
v_0-(u_1^\top v_0)u_1
=
\left(-\frac12,\frac12\right).
\]

This is a finite witness that moving state and moving tangent information are different operations.

### Witness C — constrained stage order changes the endpoint

On \(S^2\), start at

\[
u_0=(1,0,0),
\]

with ambient increments

\[
a=(0,1,0),
\qquad
b=(0,0,1).
\]

Both are tangent at \(u_0\), and each remains tangent after the other first step in this witness.

Define normalized retraction

\[
R_u(\xi)=\frac{u+\xi}{\|u+\xi\|}.
\]

Apply \(a\) then \(b\):

\[
u_a=\frac{(1,1,0)}{\sqrt2},
\]

\[
u_{ab}=R_{u_a}(b)
=
\left(\frac12,\frac12,\frac1{\sqrt2}\right).
\]

Reverse the order:

\[
u_b=\frac{(1,0,1)}{\sqrt2},
\]

\[
u_{ba}=R_{u_b}(a)
=
\left(\frac12,\frac1{\sqrt2},\frac12\right).
\]

Hence

\[
u_{ab}\neq u_{ba}.
\]

Both paths remain on \(S^2\). Constraint preservation does not make staged transport order-independent.

Their inner product is

\[
u_{ab}^\top u_{ba}
=
\frac14+\frac1{\sqrt2}.
\]

## Continuous-depth boundary

An explicit Neural ODE specifies

\[
\frac{dz}{dt}=f(z,t;\theta)
\]

and defines finite-time state transport through its flow/numerical solution.

A residual stack instead directly specifies a finite composition.

The chapter may compare the two, but must not infer:

\[
\text{residual stack}
\Rightarrow
\text{unique exact ODE}.
\]

If \(\Phi_k\) changes with \(k\), a continuous analogy is naturally nonautonomous/stage-dependent unless additional structure is proved.

## Information boundary

If transport includes normalization,

\[
z\mapsto \frac{z}{\|z\|},
\]

radial information is removed unless represented elsewhere.

A feasible constrained trajectory can therefore be non-invertible and information-losing.

Constraint preservation is not information preservation.

## Principal pedagogical device

### Allegory: moving a state versus carrying a local compass

Moving a point across a curved surface is one problem. Carrying a tangent arrow or local coordinate frame along the route is another.

Structural correspondence:

- moving point ↔ representation-state update;
- tangent arrow ↔ local differential/optimizer/history information;
- route ↔ ordered composition of stage maps;
- keeping point on surface ↔ constraint preservation;
- carrying arrow consistently ↔ vector/parallel transport.

Limit:

This is geometry language. It does not imply that a learned network literally lives on a smooth manifold or follows a Levi-Civita connection.

## Failure boundaries

- state transport != vector transport;
- vector transport != parallel transport;
- representation transport != optimal transport;
- retraction != exponential map;
- feasible endpoint != geodesic endpoint;
- residual stage != exact flow map;
- finite stack != unique ODE;
- shared map != layer-varying map;
- constraint preservation != invertibility;
- constraint preservation != information preservation;
- order-sensitive witness != universal noncommutation theorem;
- local tangent coordinates cannot be silently reused after the base point moves.

## Downstream handoff

Direct consumer:

- \`ATLAS-CH-NEURALKRYLOV-001\`.

NEURALKRYLOV may inherit:

- the declared state-transport map \(\Phi_k\);
- the distinction between finite composition and exact continuous flow;
- tangent/base-point ownership;
- the constrained retraction witness;
- the order-sensitive two-stage constrained witness;
- autonomous versus stage-dependent transport semantics.

NEURALKRYLOV must independently establish any Krylov subspace, projection, residual, preconditioning, or convergence claim. No classical Krylov guarantee transfers merely because a representation update is described as transport.

## Sources

- [@Lee2018Riemannian]
- [@AbsilMahonySepulchre2008]
- [@HeZhangRenSun2016]
- [@ChenRubanovaBettencourtDuvenaud2018]
- [@HaberRuthotto2018]

Exact source authority and claim boundaries are locked in:

\`sources/source-locks/ATLAS-CH-TRANSPORT-001.yaml\`.
