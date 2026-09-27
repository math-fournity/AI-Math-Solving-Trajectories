# Hilbert Symbol under Restriction — Proof that $(a,b)_p = 1$ over $E$

## Answer

$$\boxed{(a,b)_p \text{ calculated over } E \text{ is necessarily equal to } 1.}$$

---

## Setup

Let $p$ be an odd prime, $E/\mathbb{Q}_p$ a finite extension with $\zeta_p \in E$ but $\zeta_{p^2} \notin E$. Let $a, b \in E^*$ with $[E : \mathbb{Q}_p(a,b,\zeta_p)] = p^m$, $m \geq 1$.

Define $F := \mathbb{Q}_p(a, b, \zeta_p)$. Since $a, b \in E^*$ and $\zeta_p \in E$, we have $F \subseteq E$, so $F$ is a subfield of $E$ with $[E:F] = p^m$.

Key observations:
- $a, b \in F^*$ and $\zeta_p \in F$.
- $[E:F] = p^m$ with $m \geq 1$, so $p \mid [E:F]$.

The Hilbert symbol $(a,b)_p$ over a field $K \supseteq \zeta_p$ is the $p$-th power Hilbert symbol, taking values in $\mu_p \cong \mathbb{Z}/p\mathbb{Z}$ (equivalently, in $\operatorname{Br}(K)[p]$).

---

## Step 1: Hilbert symbol commutes with restriction

**Claim.** $(a,b)_E = \operatorname{res}_{F \to E}\bigl((a,b)_F\bigr)$.

**Proof.** The $p$-th Hilbert symbol over a field $K \supseteq \zeta_p$ admits a cohomological description via Kummer theory. The Kummer class $[a]_K \in H^1(G_K, \mu_p)$ is defined by the cocycle $\sigma \mapsto \sigma(\sqrt[p]{a})/\sqrt[p]{a}$. The Hilbert symbol is the cup product:

$$(a,b)_K = [a]_K \cup [b]_K \in H^2(G_K, \mu_p^{\otimes 2}).$$

Using $\zeta_p \in K$ to identify $\mu_p \cong \mathbb{Z}/p\mathbb{Z}$ (as a $G_K$-module with trivial action), we get $H^2(G_K, \mu_p) \cong \operatorname{Br}(K)[p]$, and the Hilbert symbol lands in $\operatorname{Br}(K)[p]$.

Since $a, b \in F \subseteq E$, the Kummer class $[a]_F$ restricts to $[a]_E$ under $\operatorname{res}_{F \to E}: H^1(G_F, \mu_p) \to H^1(G_E, \mu_p)$ (the element $a$ is the same; we are just restricting the Galois group). Cup products commute with restriction:

$$\operatorname{res}_{F \to E}([a]_F \cup [b]_F) = [a]_E \cup [b]_E.$$

Therefore $(a,b)_E = \operatorname{res}_{F \to E}\bigl((a,b)_F\bigr)$. $\square$

---

## Step 2: The Brauer group of a local field

For any local field $K$ (finite extension of $\mathbb{Q}_p$), local class field theory gives:

$$\operatorname{Br}(K) \cong \mathbb{Q}/\mathbb{Z}.$$

The isomorphism is given by the **Hasse invariant** $\operatorname{inv}_K: \operatorname{Br}(K) \xrightarrow{\sim} \mathbb{Q}/\mathbb{Z}$.

The $p$-torsion subgroup is:

$$\operatorname{Br}(K)[p] = \{x \in \operatorname{Br}(K) : px = 0\} \cong \tfrac{1}{p}\mathbb{Z}/\mathbb{Z} \cong \mathbb{Z}/p\mathbb{Z}.$$

In particular, $|\operatorname{Br}(K)[p]| = p$, and every element $\alpha \in \operatorname{Br}(K)[p]$ satisfies $p \cdot \alpha = 0$.

Since $(a,b)_F \in \operatorname{Br}(F)[p]$, we have $p \cdot (a,b)_F = 0$ in $\operatorname{Br}(F)$.

---

## Step 3: Hasse invariant and the restriction formula

**Key formula.** For any finite extension $L/K$ of local fields:

$$\operatorname{inv}_L \circ \operatorname{res}_{K \to L} = [L:K] \cdot \operatorname{inv}_K. \tag{$\star$}$$

Equivalently, under the identification $\operatorname{Br}(K) \cong \mathbb{Q}/\mathbb{Z}$ and $\operatorname{Br}(L) \cong \mathbb{Q}/\mathbb{Z}$ via Hasse invariants, the restriction map $\operatorname{res}_{K \to L}: \operatorname{Br}(K) \to \operatorname{Br}(L)$ corresponds to multiplication by $[L:K]$ on $\mathbb{Q}/\mathbb{Z}$.

**Proof of $(\star)$.** This is a standard result in local class field theory. We verify it via the compatibility with corestriction. The composition $\operatorname{cor}_{L \to K} \circ \operatorname{res}_{K \to L} = [L:K] \cdot \operatorname{id}$ is a standard fact from Galois cohomology (valid for any finite extension, not necessarily Galois). The Hasse invariant satisfies $\operatorname{inv}_K \circ \operatorname{cor}_{L \to K} = \operatorname{inv}_L$ (corestriction preserves the invariant — this follows from the compatibility of invariant maps with norm maps in local CFT). Combining:

$$\operatorname{inv}_K \circ \operatorname{cor}_{L \to K} \circ \operatorname{res}_{K \to L} = \operatorname{inv}_L \circ \operatorname{res}_{K \to L},$$

$$[L:K] \cdot \operatorname{inv}_K = \operatorname{inv}_L \circ \operatorname{res}_{K \to L}. \quad \square$$

**Concrete verification via cyclic algebras.** As a sanity check: take $K = \mathbb{Q}_p(\zeta_p)$, $L = K(\sqrt[p]{\pi})$ (totally ramified, degree $p$), and the cyclic algebra $A = (L/K, \sigma, u)$ with $u \notin N_{L/K}(L^*)$. Then $\operatorname{inv}_K(A) = k/p \neq 0$ for some $k \in \{1,\dots,p-1\}$. Since $L$ is a maximal subfield of $A$ (degree $p$ CSA), $A \otimes_K L \cong M_p(L)$ by the double centralizer theorem, so $\operatorname{res}_{K \to L}(A) = 0$ and $\operatorname{inv}_L(\operatorname{res}(A)) = 0$. Formula $(\star)$ gives $p \cdot (k/p) = k = 0 \in \mathbb{Q}/\mathbb{Z}$, which is consistent. This rules out the alternative formula $\operatorname{inv}_L \circ \operatorname{res} = \operatorname{inv}_K$ (which would give $k/p \neq 0$, a contradiction).

---

## Step 4: Restriction kills $p$-torsion

Apply formula $(\star)$ with $K = F$ and $L = E$:

$$\operatorname{inv}_E \circ \operatorname{res}_{F \to E} = [E:F] \cdot \operatorname{inv}_F = p^m \cdot \operatorname{inv}_F.$$

Since $\operatorname{inv}_F: \operatorname{Br}(F) \xrightarrow{\sim} \mathbb{Q}/\mathbb{Z}$ is an isomorphism, this means $\operatorname{res}_{F \to E}$ acts as multiplication by $p^m$ on $\mathbb{Q}/\mathbb{Z}$.

Now restrict to $p$-torsion. For $\alpha \in \operatorname{Br}(F)[p] \cong \tfrac{1}{p}\mathbb{Z}/\mathbb{Z}$, we have $p \cdot \alpha = 0$. Since $m \geq 1$:

$$\operatorname{res}_{F \to E}(\alpha) = p^m \cdot \alpha = p^{m-1} \cdot (p \cdot \alpha) = p^{m-1} \cdot 0 = 0.$$

Therefore $\operatorname{res}_{F \to E} = 0$ on $\operatorname{Br}(F)[p]$.

---

## Step 5: Conclusion

From Step 1: $(a,b)_E = \operatorname{res}_{F \to E}\bigl((a,b)_F\bigr)$.

From Step 2: $(a,b)_F \in \operatorname{Br}(F)[p]$.

From Step 4: $\operatorname{res}_{F \to E} = 0$ on $\operatorname{Br}(F)[p]$.

Therefore:

$$(a,b)_E = \operatorname{res}_{F \to E}\bigl((a,b)_F\bigr) = 0 \in \operatorname{Br}(E)[p],$$

which means $(a,b)_p = 1$ when calculated over $E$.

$$\boxed{(a,b)_p = 1}$$

---

## Remark on the hypotheses

- **$\zeta_p \in E$**: Required for the $p$-th Hilbert symbol to be defined (Kummer theory needs $\zeta_p$).
- **$\zeta_{p^2} \notin E$**: Not strictly necessary for the proof. The argument only uses $[E:F] = p^m$ with $m \geq 1$ (so $p \mid [E:F]$) and $\zeta_p \in F$. The condition $\zeta_{p^2} \notin E$ is part of the problem's structural setup but does not affect the core argument. The conclusion holds for any finite extension $E/\mathbb{Q}_p$ containing $\zeta_p$ with $[E:\mathbb{Q}_p(a,b,\zeta_p)]$ divisible by $p$.
- **$m \geq 1$**: Crucial — this ensures $p \mid [E:F]$, which is what makes the restriction vanish on $p$-torsion. If $m = 0$ (i.e., $E = F$), the restriction is the identity and $(a,b)_E = (a,b)_F$ need not be $1$.

### PROOF COMPLETE
