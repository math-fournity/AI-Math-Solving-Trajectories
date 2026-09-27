# Proof

## Setup

Let $\pi$ be a smooth admissible cuspidal representation of $\operatorname{GSp}_4(\mathbb{A}^{(\infty)})$ of dominant weight $(k_1, k_2)$ with $k_1 \geq k_2 \geq 1$, satisfying the multiplicity one hypothesis. The attached $p$-adic Galois representation $\rho: G_{\mathbb{Q}} \to \operatorname{GL}_4(\overline{\mathbb{Q}}_p)$ occurs in $H^3_{\text{ét}}$ of the Siegel threefold (the Siegel modular variety of genus 2, which has complex dimension 3).

Complex conjugation $c \in \operatorname{Gal}(\mathbb{C}/\mathbb{R})$ acts on the 4-dimensional space $V_\rho$ with $c^2 = 1$, so its eigenvalues are $\pm 1$. We must determine the number of $-1$ eigenvalues.

## Step 1: The $\pi$-isotypic component is a sub-Hodge structure of $H^3$

The Siegel threefold $X$ is defined over $\mathbb{Q}$ (the reflex field for $\operatorname{GSp}_4$ is $\mathbb{Q}$). The Hecke algebra acts on $H^3_{\text{ét}}(X_{\overline{\mathbb{Q}}}, \overline{\mathbb{Q}}_p)$ by algebraic correspondences defined over $\mathbb{Q}$. By the multiplicity one hypothesis, the $\pi$-isotypic component $V_\pi \subset H^3_{\text{ét}}$ is 4-dimensional, and it is simultaneously:

- a sub-$G_{\mathbb{Q}}$-representation (stable under Galois), and
- a sub-Hodge structure of $H^3_{\text{B}}(X(\mathbb{C}), \mathbb{Q})$ (stable under the Hodge decomposition),

since the Hecke correspondences preserve both structures. Under the comparison isomorphism $H^3_{\text{ét}}(X_{\mathbb{C}}, \overline{\mathbb{Q}}_p) \cong H^3_{\text{B}}(X(\mathbb{C}), \mathbb{Q}) \otimes \overline{\mathbb{Q}}_p$, the action of $c$ on $V_\pi$ corresponds to the action of complex conjugation on the Betti cohomology.

## Step 2: Hodge types of $V_\pi$

The Hodge–Tate weights of $\rho$ are $\{k_1+k_2-3,\; k_1-2,\; k_2-1,\; 0\}$. Since $V_\pi$ appears in $H^3$ (middle cohomology of a 3-fold), the purity weight is $w = 3$, giving $k_1 + k_2 = 6$. The Hodge types $(p, q)$ with $p + q = 3$ are:

$$
(3, 0), \quad (k_1-2,\; k_2-1), \quad (k_2-1,\; k_1-2), \quad (0, 3),
$$

each with multiplicity 1. (One checks $(k_1-2)+(k_2-1) = k_1+k_2-3 = 3$.) Since $k_1+k_2 = 6$ forces $k_1-2 \neq k_2-1$ for integer weights (that would require $k_1 = k_2+1$ and $k_2 = 5/2$, which is not an integer), the two middle Hodge types are distinct.

**Crucially, since $w = 3$ is odd, every Hodge type $(p,q)$ has $p \neq q$.** There are no $(p,p)$ types.

## Step 3: Trace of complex conjugation on odd-degree cohomology

Complex conjugation $c$ acts on $H^3_{\text{B}}(X(\mathbb{C}), \mathbb{C}) = \bigoplus_{p+q=3} H^{p,q}$ as a $\mathbb{C}$-anti-linear involution ($c^2 = \mathrm{id}$) that sends $H^{p,q}$ to $H^{q,p}$.

As a $\mathbb{R}$-linear map on the real cohomology $H^3_{\text{B}}(X(\mathbb{C}), \mathbb{R})$:

- **On each pair $H^{p,q} \oplus H^{q,p}$ with $p \neq q$:** $c$ swaps the two summands (anti-linearly). As an $\mathbb{R}$-linear map, this swap has **trace $0$**. (The $+1$ and $-1$ eigenspaces each have real dimension $2h^{p,q}$, contributing equally.)

- **On $H^{p,p}$ (diagonal types):** $c$ acts as an $\mathbb{R}$-linear involution whose trace depends on the specific real structure of the variety.

Since $w = 3$ is **odd**, there are **no** $(p,p)$ Hodge types in $H^3$. Therefore:

$$
\operatorname{Tr}(c \mid H^3_{\text{B}}(X(\mathbb{C}), \mathbb{R})) = \sum_{\substack{p+q=3 \\ p \neq q}} 0 + \sum_{\substack{p+q=3 \\ p = q}} (\text{trace on } H^{p,p}) = 0 + 0 = 0.
$$

This is a **general fact for odd-degree cohomology**: the trace of complex conjugation is always $0$, independent of the specific real structure, because there are no diagonal Hodge types. (The K3 counterexample from Round 1 involved $H^2$ — an even degree — where the $(1,1)$ part exists and the trace depends on the real structure. That counterexample does not apply to odd degree.)

## Step 4: Trace on the $\pi$-isotypic component

The same argument applies to the 4-dimensional sub-Hodge structure $V_\pi$. Its Hodge types are $(3,0)$, $(k_1-2, k_2-1)$, $(k_2-1, k_1-2)$, $(0,3)$ — all with $p \neq q$ (since $p + q = 3$ is odd). Complex conjugation swaps:

- $(3,0) \leftrightarrow (0,3)$: contributes trace $0$ (one $+1$, one $-1$ eigenvalue).
- $(k_1-2, k_2-1) \leftrightarrow (k_2-1, k_1-2)$: contributes trace $0$ (one $+1$, one $-1$ eigenvalue).

Therefore:

$$
\operatorname{Tr}(c \mid V_\pi) = 0.
$$

## Step 5: Conclusion

Let $a$ be the number of $+1$ eigenvalues and $b$ the number of $-1$ eigenvalues of $c$ on $V_\pi$. Then:

$$
a + b = 4, \qquad a - b = \operatorname{Tr}(c) = 0.
$$

Solving: $a = 2$, $b = 2$.

**Consistency check (determinant):** $\det(\rho) = \chi_{\mathrm{cyc}}^{2w} \cdot \varepsilon$ with $w = 3$, so $\det(\rho(c)) = (-1)^6 \cdot \varepsilon(c) = \varepsilon(c)$. With $b = 2$, $\det(\rho(c)) = (-1)^2 = 1$, giving $\varepsilon(c) = 1$. This is consistent with the nebentypus constraint for representations arising from $H^3$ of the Siegel threefold, and imposes no contradiction.

$$
\boxed{2}
$$

### PROOF COMPLETE
