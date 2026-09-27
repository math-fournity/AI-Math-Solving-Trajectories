# Problem

Let $k$ be a field, $K/k$ a separable quadratic extension, and $D/K$ a central division algebra of dimension $r^2$ over $K$ with an involution $\sigma$ of the second kind (i.e., $\sigma$ acts non-trivially on $K$ and trivially on $k$). Does there exist a field extension $F/k$ such that $L := K \otimes_k F$ is a field, and $D \otimes_K L$ splits (i.e., is isomorphic to the matrix algebra $M_r(L)$ over $L$)?

## Answer

$$\boxed{\text{Yes}}$$

## Proof

Let $\tau = \sigma|_K \in \mathrm{Gal}(K/k)$ be the non-trivial automorphism of $K/k$.

### Step 1. Reformulation

Since $K/k$ is separable (hence Galois of degree 2), for any extension $F/k$ we have
$$L = K \otimes_k F \text{ is a field} \iff K \text{ and } F \text{ are linearly disjoint over } k \iff K \cap F = k.$$
When this holds, $L = K \cdot F$ (compositum), with $[L:K] = [F:k]$ and $[L:F] = 2$, and $\tau$ extends to $\tilde\tau = \tau \otimes \mathrm{id}_F \in \mathrm{Gal}(L/F)$.

Also,
$$D \otimes_K L = D \otimes_K (K \otimes_k F) \cong D \otimes_k F,$$
so "$D \otimes_K L$ splits over $L$" is equivalent to "$L$ splits $D$", i.e. $[D] \mapsto 0$ in $\mathrm{Br}(L)$.

A sufficient condition: if $E \supset K$ is a **maximal subfield** of $D$ (so $[E:K]=r$ and $D \otimes_K E \cong M_r(E)$), then $L = E$ splits $D$. So it suffices to find a maximal subfield $E \supset K$ of $D$ such that, setting $F := E^{\langle \sigma|_E \rangle}$ (the fixed field of the involution restricted to $E$), we have $K \cap F = k$ and $K \cdot F = E$.

### Step 2. Reduction to a $\sigma$-stable maximal subfield

Suppose $D$ admits a **$\sigma$-stable** maximal subfield $E$ (i.e. $\sigma(E) = E$). Then:

- $\sigma|_E$ is an involution of $E$ extending $\tau$ on $K$. Since $E$ is commutative, $\sigma|_E$ is a genuine automorphism of order 2, non-trivial (because $\sigma|_K = \tau \neq \mathrm{id}$).
- By Artin's theorem, $F := E^{\langle \sigma|_E \rangle}$ is a field with $[E:F] = 2$ and $[F:k] = [E:k]/2 = (2r)/2 = r$.
- $K^\sigma = K^\tau = k$, so $K \cap F \supset k$. Since $[K \cdot F : k] \le [K:k][F:k] = 2r = [E:k]$ and $K \cdot F \subset E$, in fact $K \cdot F = E$, forcing $K \cap F = k$.
- $K/k$ Galois and $K \cap F = k$ $\Rightarrow$ $K \otimes_k F$ is a field, equal to $K \cdot F = E$.
- $E$ maximal subfield $\Rightarrow$ $D \otimes_K E \cong M_r(E)$, i.e. $L = E$ splits $D$. ✓

So the problem reduces to:

> **Does $D$ admit a $\sigma$-stable maximal subfield?**

### Step 3. The unitary group and its maximal torus

Define the **unitary group** of $(D, \sigma)$:
$$G := U(D, \sigma) := \{g \in D^\times : \sigma(g)\, g = 1\}.$$
This is a reductive $k$-group (an outer form of $\mathrm{GL}_{r,K}$). Indeed, base-changing to $K$:
- $K \otimes_k K \cong K \times K$ via $a \otimes b \mapsto (ab, a\tau(b))$.
- $\mathrm{Res}_{K/k}(\mathrm{GL}_1(D))_K \cong \mathrm{GL}_1(D) \times_K \mathrm{GL}_1({}^\tau D)$, and $\sigma$ swaps the two factors.
- The unitary condition $\sigma(g)g = 1$ then identifies $G_K \cong \mathrm{GL}_1(D)$.

So $G$ is a $k$-form of $\mathrm{GL}_1(D)$, hence reductive, and $G_K \cong \mathrm{GL}_1(D)$.

### Step 4. Maximal tori exist

**Case 1: $k$ finite.** Then $K$ is finite, so $\mathrm{Br}(K) = 0$ by Wedderburn's little theorem, hence $D = K$ and $r = 1$. Take $F = k$, $L = K$: $D \otimes_K L = K = M_1(K)$. ✓

**Case 2: $k$ infinite.** A reductive group over an infinite field possesses a maximal torus (Grothendieck–Chevalley–Tits): regular semisimple elements are Zariski-dense, and the identity component of their centralizer is a maximal torus defined over $k$. Hence $G = U(D, \sigma)$ has a maximal $k$-torus $T$.

### Step 5. From maximal torus to $\sigma$-stable maximal subfield

Base-change to $K$: $T_K$ is a maximal $K$-torus of $G_K \cong \mathrm{GL}_1(D)$. The maximal $K$-tori of $\mathrm{GL}_1(D)$ are exactly the groups $\mathrm{Res}_{E/K}(\mathbb{G}_m)$ where $E$ ranges over the maximal subfields of $D$ (with $[E:K] = r$). So there is a maximal subfield $E \supset K$ of $D$ with $T_K = \mathrm{Res}_{E/K}(\mathbb{G}_m)$.

Since $T$ is defined over $k$ and $\sigma$ is the $k$-structure involution of $G$, we have $\sigma(T) = T$, hence $\sigma(T_K) = T_K$, i.e. $\sigma(E) = E$. This is precisely the $\sigma$-stability required in Step 2.

### Step 6. Conclusion

With $E$ the $\sigma$-stable maximal subfield from Step 5 and $F = E^{\langle \sigma|_E \rangle}$:

- $L := K \otimes_k F = K \cdot F = E$ is a field (Step 2).
- $D \otimes_K L = D \otimes_K E \cong M_r(E) = M_r(L)$, so $D \otimes_K L$ splits.

Therefore such an $F/k$ always exists. $\blacksquare$

### PROOF COMPLETE
