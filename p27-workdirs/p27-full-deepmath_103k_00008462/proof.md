# Spectral Sequence of the Filtered Product Complex with Group Action

## Setup

Let $(A_1^\bullet, \partial_1)$ and $(A_2^\bullet, \partial_2)$ be complexes of $\mathbb{C}$-vector spaces, each with an action of a discrete group $G$ that preserves the grading and commutes with the differentials. Assume each $A_1^p$ is a free $\mathbb{C}[G]$-module.

The product complex $(A^\bullet, \partial)$ is defined by:
$$A^k = \bigoplus_{p+q=k} A_1^p \otimes_\mathbb{C} A_2^q, \qquad \partial = \partial_1 + (-1)^p\,\partial_2$$
(where the sign $(-1)^p$ is attached to the $A_1$-degree; equivalently $(-1)^q$ depending on convention — we use $(-1)^p\partial_2$ so that $\partial^2 = 0$).

The diagonal $G$-action on $A^k$ is $g\cdot(a_1\otimes a_2) = (g\cdot a_1)\otimes(g\cdot a_2)$, which preserves the total grading and commutes with $\partial$ (since $G$ commutes with both $\partial_1$ and $\partial_2$).

The **column filtration** is:
$$F^p A^k = \bigoplus_{\substack{p'+q=k\\p'\geqslant p}} A_1^{p'}\otimes_\mathbb{C} A_2^q.$$

## Goal

We prove that there is a first-quadrant spectral sequence
$$E_r^{p,q} \Rightarrow H^{p+q}\!\bigl((A^\bullet)^G\bigr)$$
with
$$E_1^{p,q} \cong A_1^p \otimes_{\mathbb{C}[G]} H^q(A_2^\bullet), \qquad E_2^{p,q} \cong H^p\!\bigl(A_1^\bullet \otimes_{\mathbb{C}[G]} H^q(A_2^\bullet)\bigr).$$

If moreover $A_1^\bullet$ is a projective resolution of the trivial $G$-module $\mathbb{C}$, then
$$E_2^{p,q} \cong H^p\!\bigl(G,\, H^q(A_2^\bullet)\bigr) \Rightarrow H^{p+q}\!\bigl(G,\, A_2^\bullet\bigr),$$
the **Cartan–Leray / hypercohomology spectral sequence**.

---

## Proof

### Step 1. The filtration is bounded and compatible with $\partial$

**Compatibility.** We check $\partial(F^p A^k) \subseteq F^p A^{k+1}$. An element of $F^p A^k$ lies in $\bigoplus_{p'\geqslant p} A_1^{p'}\otimes A_2^q$. Applying $\partial = \partial_1 + (-1)^{p'}\partial_2$:
- $\partial_1$ maps $A_1^{p'}\otimes A_2^q \to A_1^{p'+1}\otimes A_2^q$, and $p'+1 \geqslant p+1 > p$, so this lands in $F^{p+1}A^{k+1}\subseteq F^p A^{k+1}$. ✓
- $\partial_2$ maps $A_1^{p'}\otimes A_2^q \to A_1^{p'}\otimes A_2^{q+1}$, preserving $p'$, so this lands in $F^p A^{k+1}$. ✓

Hence $\partial(F^p)\subseteq F^p$ and the filtration is compatible.

**Boundedness.** If $A_1^\bullet$ and $A_2^\bullet$ are bounded below (say $A_1^p = 0$ for $p < 0$ and $A_2^q = 0$ for $q < 0$), then $F^p A^k = 0$ for $p > k$ and $F^0 A^k = A^k$, so the filtration is bounded:
$$0 = F^{k+1}A^k \subseteq F^k A^k \subseteq \cdots \subseteq F^0 A^k = A^k.$$
This ensures the spectral sequence converges strongly.

**$G$-compatibility.** Since $G$ preserves the $A_1$-grading, $G$ preserves $F^p$. Thus $F^p$ restricts to a filtration on the subcomplex of invariants $(A^\bullet)^G$:
$$F^p\bigl((A^\bullet)^G\bigr) = \bigl(F^p A^\bullet\bigr)^G.$$

### Step 2. The $E_0$ page

By definition of the spectral sequence of a filtered complex:
$$E_0^{p,q} = \frac{F^p (A^{p+q})^G}{F^{p+1}(A^{p+q})^G}.$$

Since $G$ preserves the bidegree, taking invariants commutes with taking the graded piece:
$$E_0^{p,q} = \left(\frac{F^p A^{p+q}}{F^{p+1} A^{p+q}}\right)^{\!G} = (A_1^p \otimes_\mathbb{C} A_2^q)^G.$$

**Key lemma (freeness).** *If $F$ is a free $\mathbb{C}[G]$-module (left) and $M$ is any left $\mathbb{C}[G]$-module, then with the diagonal $G$-action on $F\otimes_\mathbb{C} M$:*
$$(F\otimes_\mathbb{C} M)^G \cong F\otimes_{\mathbb{C}[G]} M.$$

*Proof of lemma.* It suffices to prove this for $F = \mathbb{C}[G]$ (then extend by direct sums). An element of $\mathbb{C}[G]\otimes_\mathbb{C} M$ is $\sum_g [g]\otimes m_g$. Under the diagonal action $h\cdot([g]\otimes m) = [hg]\otimes hm$, invariance requires $h\,m_{h^{-1}g} = m_g$ for all $g,h$. Setting $g=e$: $m_{h^{-1}} = h^{-1}m_e$, so $m_g = g^{-1}m$ where $m = m_e$. The map
$$\Phi: M \to (\mathbb{C}[G]\otimes_\mathbb{C} M)^G, \qquad m \mapsto \sum_{g\in G} [g]\otimes g^{-1}m$$
is an isomorphism of $\mathbb{C}$-vector spaces. Meanwhile $\mathbb{C}[G]\otimes_{\mathbb{C}[G]} M \cong M$ via $[g]\otimes_{\mathbb{C}[G]} m \mapsto g^{-1}m$ (or $gm$ depending on left/right convention). Composing gives the desired isomorphism. $\square$

Applying the lemma with $F = A_1^p$ and $M = A_2^q$:
$$\boxed{E_0^{p,q} \cong A_1^p \otimes_{\mathbb{C}[G]} A_2^q.}$$

The $d_0$ differential is the part of $\partial$ that preserves the filtration degree $p$, which is $(-1)^p\partial_2$ (acting on the $A_2$ factor). On the quotient $E_0^{p,q}$ this becomes:
$$d_0 = (-1)^p\,(\mathrm{id}\otimes \partial_2): A_1^p\otimes_{\mathbb{C}[G]} A_2^q \to A_1^p\otimes_{\mathbb{C}[G]} A_2^{q+1}.$$

### Step 3. The $E_1$ page

$$E_1^{p,q} = H^q\!\bigl(A_1^p \otimes_{\mathbb{C}[G]} A_2^\bullet,\; d_0\bigr) = H^q\!\bigl(A_1^p \otimes_{\mathbb{C}[G]} A_2^\bullet\bigr).$$

Since $A_1^p$ is a **free** $\mathbb{C}[G]$-module, it is in particular **flat** over $\mathbb{C}[G]$. Therefore tensoring with $A_1^p$ preserves cohomology:
$$H^q\!\bigl(A_1^p \otimes_{\mathbb{C}[G]} A_2^\bullet\bigr) \cong A_1^p \otimes_{\mathbb{C}[G]} H^q(A_2^\bullet).$$

$$\boxed{E_1^{p,q} \cong A_1^p \otimes_{\mathbb{C}[G]} H^q(A_2^\bullet).}$$

Here $H^q(A_2^\bullet)$ inherits a $G$-action (since $\partial_2$ commutes with $G$), making $A_1^p\otimes_{\mathbb{C}[G]} H^q(A_2)$ well-defined.

The $d_1$ differential is induced by $\partial_1$ (the part of $\partial$ that raises $p$ by 1):
$$d_1 = \partial_1 \otimes \mathrm{id}: A_1^p \otimes_{\mathbb{C}[G]} H^q(A_2) \to A_1^{p+1}\otimes_{\mathbb{C}[G]} H^q(A_2).$$

This is well-defined because $\partial_1$ commutes with the $G$-action and $\partial_1^2 = 0$.

### Step 4. The $E_2$ page

$$E_2^{p,q} = H^p\!\bigl(A_1^\bullet \otimes_{\mathbb{C}[G]} H^q(A_2^\bullet),\; d_1\bigr) = H^p\!\bigl(A_1^\bullet \otimes_{\mathbb{C}[G]} H^q(A_2^\bullet)\bigr).$$

$$\boxed{E_2^{p,q} \cong H^p\!\bigl(A_1^\bullet \otimes_{\mathbb{C}[G]} H^q(A_2^\bullet)\bigr).}$$

### Step 5. Identification with group cohomology (if $A_1^\bullet$ resolves $\mathbb{C}$)

If $A_1^\bullet$ is a projective (hence free) resolution of the trivial $G$-module $\mathbb{C}$:
$$\cdots \to A_1^1 \to A_1^0 \to \mathbb{C} \to 0,$$
then by definition of group cohomology:
$$H^p\!\bigl(A_1^\bullet \otimes_{\mathbb{C}[G]} M\bigr) = \mathrm{Tor}_p^{\mathbb{C}[G]}(\mathbb{C}, M) = H^p(G, M)$$
for any $\mathbb{C}[G]$-module $M$. Taking $M = H^q(A_2^\bullet)$:
$$\boxed{E_2^{p,q} \cong H^p\!\bigl(G,\, H^q(A_2^\bullet)\bigr).}$$

### Step 6. Convergence

The filtration $F^p$ on $(A^\bullet)^G$ is bounded (Step 1), so by the standard convergence theorem for spectral sequences of bounded filtered complexes (e.g., Weibel, Theorem 5.5.1; McCleary, Theorem 3.1), the spectral sequence converges strongly:
$$E_r^{p,q} \Rightarrow H^{p+q}\!\bigl((A^\bullet)^G\bigr).$$

When $A_1^\bullet$ is a resolution of $\mathbb{C}$, the total complex $(A^\bullet)^G = \mathrm{Tot}(A_1^\bullet \otimes_\mathbb{C} A_2^\bullet)^G \cong \mathrm{Tot}(A_1^\bullet \otimes_{\mathbb{C}[G]} A_2^\bullet)$ computes the hypercohomology $R\Gamma(G, A_2^\bullet)$, so:
$$\boxed{E_2^{p,q} \cong H^p\!\bigl(G,\, H^q(A_2^\bullet)\bigr) \Rightarrow H^{p+q}\!\bigl(G,\, A_2^\bullet\bigr).}$$

This is the **Cartan–Leray spectral sequence** (for hypercohomology).

---

## Summary

| Page | Term | Key ingredient used |
|------|------|---------------------|
| $E_0^{p,q}$ | $A_1^p \otimes_{\mathbb{C}[G]} A_2^q$ | Freeness: $(F\otimes M)^G \cong F\otimes_{\mathbb{C}[G]} M$ |
| $E_1^{p,q}$ | $A_1^p \otimes_{\mathbb{C}[G]} H^q(A_2)$ | Flatness of free modules |
| $E_2^{p,q}$ | $H^p(A_1^\bullet \otimes_{\mathbb{C}[G]} H^q(A_2))$ | Definition of derived functor |
| $E_2^{p,q}$ (if $A_1$ resolves $\mathbb{C}$) | $H^p(G, H^q(A_2))$ | Definition of group cohomology |
| Abutment | $H^{p+q}((A^\bullet)^G)$ | Bounded filtration → strong convergence |

The freeness of $A_1$ over $\mathbb{C}[G]$ is used in two places:
1. **$E_0$ page**: to identify $(A_1^p \otimes A_2^q)^G \cong A_1^p \otimes_{\mathbb{C}[G]} A_2^q$.
2. **$E_1$ page**: to ensure $A_1^p$ is flat over $\mathbb{C}[G]$, so $H^q(A_1^p \otimes_{\mathbb{C}[G]} A_2^\bullet) \cong A_1^p \otimes_{\mathbb{C}[G]} H^q(A_2^\bullet)$.
