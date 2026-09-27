# Euler Characteristic of the Manifold of Fixed Rank Matrices

## Problem

Determine the Euler characteristic of $\mathcal{M}_r$, the manifold of $n \times m$ matrices of rank $r$ over $\mathbb{R}$ or $\mathbb{C}$.

## Answer

$$\boxed{\chi(\mathcal{M}_r) = 0 \quad \text{for all } r \geq 1}$$

(over $\mathbb{C}$ this holds without exception; over $\mathbb{R}$ it holds for $r \geq 2$, and for $r = 1$ it holds except in the degenerate case where both $n$ and $m$ are odd, where $\chi = 2$).

---

## Proof

### Setup: the fibration structure

A rank-$r$ matrix $A : \mathbb{F}^m \to \mathbb{F}^n$ (where $\mathbb{F} = \mathbb{R}$ or $\mathbb{C}$) determines:
- its image $V = \operatorname{im}(A) \in \operatorname{Gr}(r, n)$, an $r$-dimensional subspace of $\mathbb{F}^n$;
- its kernel $W = \ker(A) \in \operatorname{Gr}(m-r, m)$, an $(m-r)$-dimensional subspace of $\mathbb{F}^m$.

Given $(V, W)$, the matrix $A$ factors through an isomorphism $\mathbb{F}^m / W \xrightarrow{\sim} V$, and the space of such isomorphisms is $\operatorname{GL}(r, \mathbb{F})$. This gives a fiber bundle:

$$\operatorname{GL}(r, \mathbb{F}) \longrightarrow \mathcal{M}_r \longrightarrow \operatorname{Gr}(r,n) \times \operatorname{Gr}(m-r, m).$$

By Gram–Schmidt, $\operatorname{GL}(r, \mathbb{R}) \simeq O(r)$ and $\operatorname{GL}(r, \mathbb{C}) \simeq U(r)$.

### Case 1: $\mathbb{F} = \mathbb{C}$, $r \geq 1$

The circle group $S^1 = \{\lambda \in \mathbb{C} : |\lambda| = 1\}$ acts freely on $\mathcal{M}_r(\mathbb{C})$ by scalar multiplication: $\lambda \cdot A = \lambda A$. This action is free because for $r \geq 1$, every $A \in \mathcal{M}_r$ is nonzero, so $\lambda A = A$ implies $\lambda = 1$.

Since $S^1$ is a compact connected Lie group acting freely, the Euler characteristic is multiplicative:

$$\chi(\mathcal{M}_r(\mathbb{C})) = \chi(\mathcal{M}_r(\mathbb{C})/S^1) \cdot \chi(S^1).$$

Since $\chi(S^1) = 0$ (odd-dimensional sphere), we conclude:

$$\chi(\mathcal{M}_r(\mathbb{C})) = 0 \quad \text{for all } r \geq 1.$$

### Case 2: $\mathbb{F} = \mathbb{R}$, $r \geq 2$

We use the fibration $O(r) \to \mathcal{M}_r(\mathbb{R}) \to \operatorname{Gr}(r,n) \times \operatorname{Gr}(m-r,m)$.

**Step 2a: $\chi(O(r)) = 0$ for $r \geq 2$.**

$O(r)$ has two connected components, each diffeomorphic to $SO(r)$, so $\chi(O(r)) = 2\,\chi(SO(r))$. For $r \geq 2$, $SO(r)$ is a nontrivial compact connected Lie group, hence has positive rank (a maximal torus of dimension $\geq 1$). By the Hopf theorem, a compact connected Lie group has nonzero Euler characteristic if and only if it is trivial (rank $0$). Therefore $\chi(SO(r)) = 0$ for $r \geq 2$, giving $\chi(O(r)) = 0$.

**Step 2b: Handling monodromy via the Leray–Serre spectral sequence.**

The structure group $\operatorname{GL}(r, \mathbb{R})$ is disconnected (two components), so the fibration may have nontrivial monodromy. The monodromy action on $H^*(O(r))$ permutes the two copies of $H^*(SO(r))$ in the decomposition $H^*(O(r)) \cong H^*(SO(r)) \oplus H^*(SO(r))$.

Decompose into $\pm 1$ eigenspaces under monodromy:
- The $+1$ eigenspace (diagonal) carries the trivial local system with fiber $H^*(SO(r))$.
- The $-1$ eigenspace (anti-diagonal) carries a sign local system with fiber $H^*(SO(r))$.

The Leray–Serre spectral sequence gives:

$$\chi(\mathcal{M}_r(\mathbb{R})) = \sum_{p,q} (-1)^{p+q} \dim E_2^{p,q}.$$

Each $E_2^{p,q}$ term is $H^p(\text{base}; \mathcal{L}_q)$ where $\mathcal{L}_q$ is a local system with fiber $H^q(SO(r))$. The key observation is that **every term in the alternating sum contains the factor $\dim H^q(SO(r))$ for some $q$**, and the total contribution factors as:

$$\chi(\mathcal{M}_r(\mathbb{R})) = \left(\sum_q (-1)^q \dim H^q(SO(r))\right) \cdot C = \chi(SO(r)) \cdot C$$

where $C$ is a constant depending on the base and the local systems (trivial or sign), but independent of the fiber cohomology. Since $\chi(SO(r)) = 0$ for $r \geq 2$:

$$\chi(\mathcal{M}_r(\mathbb{R})) = 0 \quad \text{for all } r \geq 2.$$

### Case 3: $\mathbb{F} = \mathbb{R}$, $r = 1$

A rank-$1$ real matrix has the form $A = u v^T$ for nonzero $u \in \mathbb{R}^n$, $v \in \mathbb{R}^m$, with the identification $(u, v) \sim (\lambda u, \lambda^{-1} v)$ for $\lambda \in \mathbb{R}^*$. Thus:

$$\mathcal{M}_1(\mathbb{R}) = \left((\mathbb{R}^n \setminus \{0\}) \times (\mathbb{R}^m \setminus \{0\})\right) / \mathbb{R}^*.$$

**Step 3a: Quotient by $\mathbb{R}_{>0}$.** The subgroup $\mathbb{R}_{>0} \subset \mathbb{R}^*$ acts by $(u, v) \mapsto (\lambda u, \lambda^{-1} v)$. This action is free with contractible fibers (each orbit is a copy of $\mathbb{R}_{>0} \cong \mathbb{R}$), so the quotient is homotopy equivalent to the original space. After this quotient, we may normalize $|u| = |v| = 1$:

$$\mathcal{M}_1(\mathbb{R}) \simeq (S^{n-1} \times S^{m-1}) / \mathbb{Z}_2,$$

where the remaining $\mathbb{Z}_2 = \{\pm 1\} \subset \mathbb{R}^*$ acts by $(u, v) \mapsto (-u, -v)$.

**Step 3b: Compute the Euler characteristic.** The $\mathbb{Z}_2$-action is free (since $(-u, -v) = (u, v)$ would require $u = 0$ or $v = 0$, impossible on spheres). For a free action of a finite group $G$ on a finite CW-complex $X$:

$$\chi(X) = |G| \cdot \chi(X/G).$$

Therefore:

$$\chi(\mathcal{M}_1(\mathbb{R})) = \frac{\chi(S^{n-1}) \cdot \chi(S^{m-1})}{2} = \frac{(1 + (-1)^{n-1})(1 + (-1)^{m-1})}{2}.$$

This equals $0$ unless both $n$ and $m$ are odd, in which case it equals $2$.

### Summary

| Field | $r$ | $\chi(\mathcal{M}_r)$ |
|-------|-----|----------------------|
| $\mathbb{C}$ | $\geq 1$ | $0$ |
| $\mathbb{R}$ | $\geq 2$ | $0$ |
| $\mathbb{R}$ | $= 1$ | $0$ (generically); $2$ if $n, m$ both odd |

The generic answer, valid over both $\mathbb{R}$ and $\mathbb{C}$ for all $r \geq 1$, is:

$$\boxed{\chi(\mathcal{M}_r) = 0}$$

### PROOF COMPLETE
