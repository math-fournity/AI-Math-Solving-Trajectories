# Proof: $\dim H^{(0,1)}(B(2) - B(1)) = \infty$

## Setup

Let $B(r) = \{z \in \mathbb{C}^2 : |z_1|^2 + |z_2|^2 < r^2\}$ be the open ball of radius $r$ in $\mathbb{C}^2$. We interpret $B(2) - B(1)$ as the open spherical shell

$$\Omega = B(2) \setminus \overline{B(1)} = \{z \in \mathbb{C}^2 : 1 < |z_1|^2 + |z_2|^2 < 4\},$$

which is an open Reinhardt domain in $\mathbb{C}^2$ (invariant under the torus action $(z_1, z_2) \mapsto (e^{i\theta_1} z_1, e^{i\theta_2} z_2)$).

## Step 1: Dolbeault Theorem Reduction

By the Dolbeault theorem, $H^{(0,q)}(\Omega) \cong H^q(\Omega, \mathcal{O})$ for all $q \geq 0$, where $\mathcal{O}$ is the sheaf of holomorphic functions. In particular:

$$H^{(0,1)}(\Omega) \cong H^1(\Omega, \mathcal{O}).$$

## Step 2: The Standard Cover and Its Acyclicity

Define the standard Reinhardt cover $\mathcal{U} = \{U_1, U_2\}$ where

$$U_i = \{z \in \Omega : z_i \neq 0\}, \quad i = 1, 2.$$

**Claim:** $U_1 \cup U_2 = \Omega$.

*Proof.* If $z \in \Omega$ and $z_1 = 0$ and $z_2 = 0$, then $|z|^2 = 0 < 1$, contradicting $z \in \Omega$. So at least one coordinate is nonzero, hence $z \in U_1 \cup U_2$. $\square$

**Claim:** Each $U_I$ (for $I \subseteq \{1,2\}$, $I \neq \emptyset$) is a domain of holomorphy, hence Stein.

*Proof.* We handle each case:

- **$U_1 = \Omega \cap \{z_1 \neq 0\}$:** The function $f(z) = 1/z_1$ is holomorphic on $U_1$. The boundary $\partial U_1 \setminus \partial \Omega$ consists of points $\{(0, z_2) : 1 < |z_2| < 2\}$. At any such point $p = (0, z_2^0)$, the function $1/z_1$ blows up, so it cannot be extended to any neighborhood of $p$. Therefore $U_1$ is a domain of holomorphy.

- **$U_2 = \Omega \cap \{z_2 \neq 0\}$:** By the same argument with $1/z_2$.

- **$U_{12} = U_1 \cap U_2 = \Omega \cap \{z_1 \neq 0\} \cap \{z_2 \neq 0\}$:** The function $1/(z_1 z_2)$ is holomorphic on $U_{12}$ and blows up at any boundary point where $z_1 = 0$ or $z_2 = 0$. So $U_{12}$ is a domain of holomorphy.

By the Cartan–Thullen theorem, every domain of holomorphy in $\mathbb{C}^n$ is Stein. $\square$

**Corollary:** The cover $\mathcal{U}$ is Leray (acyclic): $H^q(U_I, \mathcal{O}) = 0$ for all $q \geq 1$ and all $U_I$.

*Proof.* Each $U_I$ is Stein, so by Cartan's Theorem B, $H^q(U_I, \mathcal{O}) = 0$ for $q \geq 1$. $\square$

By Leray's theorem, the Čech cohomology of this cover computes the sheaf cohomology:

$$\check{H}^q(\mathcal{U}, \mathcal{O}) \cong H^q(\Omega, \mathcal{O}) \quad \text{for all } q \geq 0.$$

## Step 3: Weight Space (Laurent) Decomposition

Since $\Omega$ is a Reinhardt domain, every holomorphic function on a Reinhardt open subset $V \subseteq \Omega$ admits a unique Laurent expansion $f = \sum_{\alpha \in \mathbb{Z}^2} c_\alpha z^\alpha$, where $z^\alpha = z_1^{\alpha_1} z_2^{\alpha_2}$. The sheaf $\mathcal{O}$ decomposes as a direct sum of weight space sheaves:

$$\mathcal{O} = \bigoplus_{\alpha \in \mathbb{Z}^2} \mathcal{O}_\alpha,$$

where $\mathcal{O}_\alpha(V) = \mathbb{C} \cdot z^\alpha$ if $z^\alpha$ is holomorphic on $V$, and $\mathcal{O}_\alpha(V) = 0$ otherwise. Since sheaf cohomology is additive over direct sums of sheaves of vector spaces:

$$H^q(\Omega, \mathcal{O}) = \bigoplus_{\alpha \in \mathbb{Z}^2} H^q(\Omega, \mathcal{O}_\alpha).$$

## Step 4: Holomorphic Monomials on Each $U_I$

We determine which monomials $z^\alpha$ are holomorphic on each open set:

- **$U_1 = \{1 < |z|^2 < 4,\ z_1 \neq 0\}$:** Since $z_1 \neq 0$, any power $z_1^{\alpha_1}$ ($\alpha_1 \in \mathbb{Z}$) is holomorphic. Since $z_2 = 0$ is in $U_1$ (e.g., $z = (z_1, 0)$ with $1 < |z_1| < 2$), we need $\alpha_2 \geq 0$. So:
  $$\mathcal{O}(U_1) = \bigoplus_{\alpha_1 \in \mathbb{Z},\, \alpha_2 \geq 0} \mathbb{C} \cdot z_1^{\alpha_1} z_2^{\alpha_2}.$$

- **$U_2 = \{1 < |z|^2 < 4,\ z_2 \neq 0\}$:** By symmetry:
  $$\mathcal{O}(U_2) = \bigoplus_{\alpha_1 \geq 0,\, \alpha_2 \in \mathbb{Z}} \mathbb{C} \cdot z_1^{\alpha_1} z_2^{\alpha_2}.$$

- **$U_{12} = \{1 < |z|^2 < 4,\ z_1 \neq 0,\ z_2 \neq 0\}$:** Both coordinates are nonzero, so all monomials are holomorphic:
  $$\mathcal{O}(U_{12}) = \bigoplus_{\alpha \in \mathbb{Z}^2} \mathbb{C} \cdot z^\alpha.$$

## Step 5: Čech Computation by Weight Space

The Čech complex for the cover $\mathcal{U} = \{U_1, U_2\}$ with coefficients in $\mathcal{O}$ is:

$$0 \to \mathcal{O}(U_1) \oplus \mathcal{O}(U_2) \xrightarrow{\delta} \mathcal{O}(U_{12}) \to 0,$$

where $\delta(f_1, f_2) = f_2|_{U_{12}} - f_1|_{U_{12}}$.

This decomposes by weight space $\alpha = (\alpha_1, \alpha_2) \in \mathbb{Z}^2$ into the direct sum of the following four cases:

| Case | Condition on $\alpha$ | $\mathcal{O}_\alpha(U_1)$ | $\mathcal{O}_\alpha(U_2)$ | $\mathcal{O}_\alpha(U_{12})$ | $\delta_\alpha$ | $H^1_\alpha$ |
|------|----------------------|---------------------------|---------------------------|------------------------------|-----------------|-------------|
| 1 | $\alpha_1 \geq 0,\ \alpha_2 \geq 0$ | $\mathbb{C}$ | $\mathbb{C}$ | $\mathbb{C}$ | $(c_1, c_2) \mapsto c_2 - c_1$ (surjective) | $0$ |
| 2 | $\alpha_1 < 0,\ \alpha_2 \geq 0$ | $\mathbb{C}$ | $0$ | $\mathbb{C}$ | $c_1 \mapsto -c_1$ (surjective) | $0$ |
| 3 | $\alpha_1 \geq 0,\ \alpha_2 < 0$ | $0$ | $\mathbb{C}$ | $\mathbb{C}$ | $c_2 \mapsto c_2$ (surjective) | $0$ |
| 4 | $\alpha_1 < 0,\ \alpha_2 < 0$ | $0$ | $0$ | $\mathbb{C}$ | $0 \mapsto 0$ (not surjective) | $\mathbb{C}$ |

**Explanation of each case:**

- **Case 1** ($\alpha_1 \geq 0, \alpha_2 \geq 0$): $z^\alpha$ is holomorphic on both $U_1$ and $U_2$ (and on $\Omega$). The map $\delta: \mathbb{C}^2 \to \mathbb{C}$ is surjective, so $H^1_\alpha = 0$. The kernel is 1-dimensional (the diagonal), giving $H^0_\alpha = \mathbb{C}$.

- **Case 2** ($\alpha_1 < 0, \alpha_2 \geq 0$): $z^\alpha$ is holomorphic on $U_1$ (where $z_1 \neq 0$) but not on $U_2$ (where $z_1 = 0$ is possible, and $z_1^{\alpha_1}$ would blow up). So $\mathcal{O}_\alpha(U_1) = \mathbb{C}$, $\mathcal{O}_\alpha(U_2) = 0$, and $\delta: \mathbb{C} \to \mathbb{C}$ is $c_1 \mapsto -c_1$, which is surjective. So $H^1_\alpha = 0$.

- **Case 3** ($\alpha_1 \geq 0, \alpha_2 < 0$): By symmetry with Case 2, $H^1_\alpha = 0$.

- **Case 4** ($\alpha_1 < 0, \alpha_2 < 0$): $z^\alpha$ is holomorphic on $U_{12}$ (where both $z_1, z_2 \neq 0$) but on neither $U_1$ nor $U_2$ (since $z_2 = 0 \in U_1$ and $z_1 = 0 \in U_2$ would cause blow-up). So $\mathcal{O}_\alpha(U_1) = 0$, $\mathcal{O}_\alpha(U_2) = 0$, and $\delta: 0 \to \mathbb{C}$ is the zero map, which is not surjective. Thus $H^1_\alpha = \mathbb{C}$.

## Step 6: Assembling the Result

From the weight space decomposition:

$$H^0(\Omega, \mathcal{O}) = \bigoplus_{\alpha_1 \geq 0,\, \alpha_2 \geq 0} \mathbb{C} \cdot z^\alpha = \mathcal{O}(\Omega),$$

which is the space of holomorphic functions on $\Omega$ (all non-negative monomials). This is consistent with the Hartogs extension phenomenon: since $n = 2 \geq 2$, every holomorphic function on the shell $\Omega$ extends to the ball $B(2)$, so $\mathcal{O}(\Omega) \cong \mathcal{O}(B(2))$.

For the first cohomology:

$$H^1(\Omega, \mathcal{O}) = \bigoplus_{\substack{\alpha_1 < 0 \\ \alpha_2 < 0}} \mathbb{C} \cdot z^\alpha = \bigoplus_{k \geq 1,\, l \geq 1} \mathbb{C} \cdot z_1^{-k} z_2^{-l}.$$

The index set $\{(k, l) \in \mathbb{Z}^2 : k \geq 1, l \geq 1\}$ is countably infinite, so:

$$\dim H^1(\Omega, \mathcal{O}) = \aleph_0 = \infty.$$

A basis is given by the Čech cocycles $\{z_1^{-k} z_2^{-l}\}_{k,l \geq 1}$, each representing the class of the monomial $z_1^{-k} z_2^{-l}$ viewed as a section of $\mathcal{O}$ over $U_1 \cap U_2$ that cannot be expressed as a difference of sections over $U_1$ and $U_2$.

## Step 7: Verification of Non-triviality (Case 4)

To confirm that the classes in Case 4 are genuinely non-trivial, suppose for contradiction that $z_1^{-k} z_2^{-l} = f_1 - f_2$ on $U_{12}$ for some $f_1 \in \mathcal{O}(U_1)$ and $f_2 \in \mathcal{O}(U_2)$. Expanding in Laurent series on $U_{12}$ (where all monomials are holomorphic):

- $f_1 = \sum_{\alpha_1 \in \mathbb{Z},\, \alpha_2 \geq 0} c_\alpha z^\alpha$ (only non-negative $\alpha_2$ terms, since $f_1$ is holomorphic on $U_1$ where $z_2 = 0$ is possible).
- $f_2 = \sum_{\alpha_1 \geq 0,\, \alpha_2 \in \mathbb{Z}} d_\alpha z^\alpha$ (only non-negative $\alpha_1$ terms).

The coefficient of $z_1^{-k} z_2^{-l}$ (with $k, l \geq 1$) in $f_1 - f_2$ is $c_{(-k,-l)} - d_{(-k,-l)}$. But $c_{(-k,-l)} = 0$ (since $\alpha_2 = -l < 0$ is not allowed in $f_1$) and $d_{(-k,-l)} = 0$ (since $\alpha_1 = -k < 0$ is not allowed in $f_2$). So the coefficient is $0 \neq 1$, a contradiction.

Moreover, classes for distinct $(k,l)$ are linearly independent since they lie in different weight spaces (the decomposition is direct).

## Conclusion

By the Dolbeault theorem and the Čech–Leray computation:

$$\dim H^{(0,1)}(B(2) - B(1)) = \dim H^1(\Omega, \mathcal{O}) = \left|\{(k, l) \in \mathbb{Z}^2 : k \geq 1,\, l \geq 1\}\right| = \aleph_0 = \infty.$$

$$\boxed{\infty}$$

### PROOF COMPLETE
