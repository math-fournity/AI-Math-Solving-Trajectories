# Proof

**Claim.** There exists a left-Ore ring that does not have the invariant basis number (IBN) property. The answer is **Yes**.

We exhibit an explicit example: $R = \operatorname{End}_k(V)$, the ring of $k$-linear endomorphisms of an infinite-dimensional vector space $V$ over a field $k$.

---

## Step 1. $R = \operatorname{End}_k(V)$ is a left-Ore ring

Recall that a ring $R$ is a **left-Ore ring** if its set of regular elements (non-zero-divisors) $S = R^{\mathrm{reg}}$ satisfies the left Ore condition:

> For every $r \in R$ and $s \in S$, there exist $r' \in R$ and $s' \in S$ with $s' r = r' s$,

together with the invertibility condition $rs = 0,\; s \in S \Rightarrow r = 0$.

**Lemma 1.1.** In $R = \operatorname{End}_k(V)$ with $\dim_k V = \infty$, the regular elements are exactly the units (automorphisms of $V$).

*Proof.* Let $\varphi \in R$.

- ($\Leftarrow$) If $\varphi$ is a unit (bijective), then $\varphi$ is clearly not a left or right zero-divisor.

- ($\Rightarrow$, contrapositive) Suppose $\varphi$ is not a unit.

  - If $\varphi$ is not injective, pick $0 \neq v \in \ker\varphi$. Define $\psi \in R$ with $\psi(V) \subseteq k\cdot v \subseteq \ker\varphi$ and $\psi \neq 0$ (e.g., $\psi(w) = \lambda(w) v$ for some nonzero linear functional $\lambda$). Then $\varphi \circ \psi = 0$ with $\psi \neq 0$, so $\varphi$ is a **left** zero-divisor.

  - If $\varphi$ is injective but not surjective (so not a unit), then $\operatorname{im}\varphi \subsetneq V$. Define $\psi \in R$ with $\ker\psi \supseteq \operatorname{im}\varphi$ and $\psi \neq 0$ (possible since $\operatorname{im}\varphi \neq V$; extend a basis of $\operatorname{im}\varphi$ to $V$ and let $\psi$ be nonzero on the complement). Then $\psi \circ \varphi = 0$ with $\psi \neq 0$, so $\varphi$ is a **right** zero-divisor.

  In either case a non-unit is a zero-divisor. $\square$

So $S = R^\times$ (the group of units) in $R$.

**Lemma 1.2.** $R$ is a left-Ore ring.

*Proof.* The Ore condition is trivially satisfied when $S = R^\times$: given $r \in R$ and $s \in S$ (a unit), set $s' = s \in S$ and $r' = s r s^{-1} \in R$. Then
$$s'\, r = s\, r = (s r s^{-1})\, s = r'\, s. \quad\checkmark$$
The invertibility condition also holds trivially: if $rs = 0$ with $s$ a unit, then $r = r s s^{-1} = 0$. $\square$

Since every regular element is already invertible, localizing at $S = R^\times$ changes nothing: the classical left ring of quotients is $Q = R$ itself.

---

## Step 2. $R = \operatorname{End}_k(V)$ does not have IBN

Recall that $R$ has **IBN** (invariant basis number) if $R^m \cong R^n$ as left $R$-modules implies $m = n$. Equivalently, there do **not** exist an $n \times m$ matrix $A$ and an $m \times n$ matrix $B$ over $R$ with $AB = I_n$ and $BA = I_m$ for $m \neq n$.

We show $R^1 \cong R^2$ as left $R$-modules, violating IBN.

**Construction.** Since $V$ is infinite-dimensional, $V \cong V \oplus V$ as $k$-vector spaces. Fix a $k$-linear isomorphism
$$\varphi : V \xrightarrow{\;\sim\;} V \oplus V,$$
with inverse $\psi = \varphi^{-1} : V \oplus V \to V$. Let $\iota_i : V \to V \oplus V$ be the $i$-th coordinate injection and $\pi_i : V \oplus V \to V$ the $i$-th coordinate projection ($i = 1, 2$). Define
$$a_i = \psi \circ \iota_i \;\in R, \qquad b_i = \pi_i \circ \varphi \;\in R, \qquad i = 1, 2.$$

**Verification.** We use the standard identities in $\operatorname{End}(V \oplus V)$:
$$\pi_i \circ \iota_j = \delta_{ij}\,\mathrm{id}_V, \qquad \iota_1 \circ \pi_1 + \iota_2 \circ \pi_2 = \mathrm{id}_{V \oplus V}.$$

**(a)** For all $i, j \in \{1,2\}$:
$$b_i \circ a_j = \pi_i \circ \varphi \circ \psi \circ \iota_j = \pi_i \circ \mathrm{id}_{V\oplus V} \circ \iota_j = \pi_i \circ \iota_j = \delta_{ij}\,\mathrm{id}_V.$$

**(b)** 
$$a_1 \circ b_1 + a_2 \circ b_2 = \psi \circ \iota_1 \circ \pi_1 \circ \varphi + \psi \circ \iota_2 \circ \pi_2 \circ \varphi = \psi \circ (\iota_1 \pi_1 + \iota_2 \pi_2) \circ \varphi = \psi \circ \mathrm{id}_{V\oplus V} \circ \varphi = \psi \circ \varphi = \mathrm{id}_V.$$

**Matrix interpretation.** An $R$-module homomorphism $f : R^m \to R^n$ is given by left-multiplication by an $n \times m$ matrix (acting on column vectors). Set
$$A = \begin{pmatrix} a_1 \\ a_2 \end{pmatrix} \in M_{2 \times 1}(R), \qquad B = \begin{pmatrix} b_1 & b_2 \end{pmatrix} \in M_{1 \times 2}(R).$$

- $A$ defines $f : R^1 \to R^2$, $\;x \mapsto Ax = \begin{pmatrix} a_1 x \\ a_2 x \end{pmatrix}$.
- $B$ defines $g : R^2 \to R^1$, $\;\begin{pmatrix} y_1 \\ y_2 \end{pmatrix} \mapsto b_1 y_1 + b_2 y_2$.

From (a): $BA = b_1 a_1 + b_2 a_2 = \delta_{11} + \delta_{22} = 1 + 1 = 2$... 

— *Correction*: we must be careful. $BA = \sum_i b_i a_i$ is a $1 \times 1$ matrix, and from (a) with $i = j$: $b_1 a_1 = \mathrm{id}_V$, $b_2 a_2 = \mathrm{id}_V$, so $BA = 2\,\mathrm{id}_V$. This is **not** $I_1$ in general (it is $2\,\mathrm{id}$, which equals $\mathrm{id}$ only if $\operatorname{char} k = 2$).

The correct IBN-witnessing identities come from re-reading (a) and (b) as matrix products in the **other** direction. The map $R^2 \to R^1$ given by $(y_1, y_2) \mapsto a_1 y_1 + a_2 y_2$ is encoded by the $1 \times 2$ matrix $A' = (a_1\;\; a_2)$, and the map $R^1 \to R^2$ given by $x \mapsto (b_1 x,\, b_2 x)^T$ is encoded by the $2 \times 1$ matrix $B' = \begin{pmatrix} b_1 \\ b_2 \end{pmatrix}$.

Then:
- $A' B' = a_1 b_1 + a_2 b_2 = \mathrm{id}_V = I_1$ (by (b)),
- $B' A' = \begin{pmatrix} b_1 a_1 & b_1 a_2 \\ b_2 a_1 & b_2 a_2 \end{pmatrix} = \begin{pmatrix} \mathrm{id}_V & 0 \\ 0 & \mathrm{id}_V \end{pmatrix} = I_2$ (by (a)).

Thus $A' \in M_{1 \times 2}(R)$ and $B' \in M_{2 \times 1}(R)$ satisfy $A' B' = I_1$ and $B' A' = I_2$, witnessing $R^1 \cong R^2$ as left $R$-modules with $1 \neq 2$. Therefore $R$ does **not** have IBN. $\square$

---

## Conclusion

The ring $R = \operatorname{End}_k(V)$, where $V$ is an infinite-dimensional vector space over a field $k$, is:

1. a **left-Ore ring** (its regular elements are exactly its units, so the Ore condition holds trivially), and
2. **without IBN** (since $V \cong V \oplus V$ yields $R^1 \cong R^2$).

Hence there exists a left-Ore ring that does not have the invariant basis number property.

$$\boxed{\text{Yes. } R = \operatorname{End}_k(V) \text{ (} V \text{ infinite-dimensional over } k\text{) is a left-Ore ring without IBN.}}$$

### PROOF COMPLETE
