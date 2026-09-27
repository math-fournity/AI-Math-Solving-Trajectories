# Hecke L-Functions with Unit-Root Local Eigenvalues are Artin L-Functions

## Statement

Let $L(s, \chi)$ be a Hecke $L$-function attached to a Hecke character (Größencharakter) $\chi$ of a number field $K$. If all local eigenvalues (Satake parameters at every place, including archimedean ones) are roots of unity, then $L(s, \chi)$ is an Artin $L$-function.

**Answer:** $\boxed{\text{Yes — a Hecke } L\text{-function whose local eigenvalues are all roots of unity is an Artin } L\text{-function.}}$

---

## Proof

### Step 1: Artin $L$-functions always have unit-root local eigenvalues

Let $L/F$ be a finite Galois extension with $G = \mathrm{Gal}(L/F)$, and let $\rho: G \to \mathrm{GL}_n(\mathbb{C})$ be a representation. The Artin $L$-function is

$$L(s, \rho) = \prod_{\mathfrak{p}} \det\!\Big(I - \rho(\mathrm{Frob}_{\mathfrak{p}})\, N(\mathfrak{p})^{-s}\Big)^{-1},$$

where the product runs over primes of $F$ unramified in $L$.

Since $G$ is **finite**, every $g \in G$ has finite order: $g^m = 1$ for some $m \mid |G|$. Hence $\rho(g)^m = I$, so every eigenvalue $\lambda$ of $\rho(g)$ satisfies $\lambda^m = 1$, i.e., $\lambda$ is an $m$-th root of unity. In particular, the eigenvalues of $\rho(\mathrm{Frob}_{\mathfrak{p}})$ — the Satake parameters — are roots of unity at every unramified prime.

At archimedean places, the local factor of an Artin $L$-function is a product of $\Gamma_{\mathbb{R}}(s+\mu_i)$ or $\Gamma_{\mathbb{C}}(s+\mu_i)$ factors with $\mu_i \in \mathbb{Z}_{\geq 0}$ arising from the Hodge structure of the finite-order representation; the associated "eigenvalues" are $\pm 1$ (roots of unity).

Thus: **every Artin $L$-function has all local eigenvalues being roots of unity.** ✓

### Step 2: The "all eigenvalues are roots of unity" condition forces $\chi$ to be of finite order

A Hecke character $\chi: \mathbb{A}_K^{\times} / K^{\times} \to \mathbb{C}^{\times}$ decomposes into local components $\chi = \prod_v \chi_v$. At each place $v$:

- **Finite place $\mathfrak{p}$ (unramified):** the Satake parameter is
$$\alpha_{\mathfrak{p}} = \chi(\varpi_{\mathfrak{p}}) = \prod_{v} \chi_v(\varpi_{\mathfrak{p}}),$$
where $\varpi_{\mathfrak{p}}$ is viewed as an idele that is a uniformizer at $\mathfrak{p}$ and a unit elsewhere.

- **Archimedean place $v$:** writing $K_v \cong \mathbb{R}$ or $\mathbb{C}$, the local character has the form
$$\chi_v(x) = x^{a_v} \bar{x}^{\,b_v}\, |x|^{2it_v}, \qquad a_v, b_v \in \mathbb{Z},\; t_v \in \mathbb{R},$$
where $(a_v, b_v)$ is the **infinity type** and $t_v$ is the **norm character exponent**.

The Satake parameter at a finite prime $\mathfrak{p}$ then satisfies:

$$\alpha_{\mathfrak{p}} = \chi_{\mathfrak{p}}(\varpi_{\mathfrak{p}}) \cdot \prod_{v \mid \infty} \sigma_v(\varpi_{\mathfrak{p}})^{a_v} \overline{\sigma_v(\varpi_{\mathfrak{p}})}^{\,b_v} \cdot |N_{K/\mathbb{Q}}(\varpi_{\mathfrak{p}})|^{it},$$

where $t = \sum_{v \mid \infty} t_v$ and $\sigma_v$ are the archimedean embeddings.

**Claim:** If every $\alpha_{\mathfrak{p}}$ is a root of unity, then:
1. $t = 0$ (the norm exponent vanishes), and
2. the infinity type $(a_v, b_v) = (0, 0)$ for all $v \mid \infty$.

**Proof of the claim:**

**(a) Vanishing of $t$.** Suppose $t \neq 0$. Then $|\alpha_{\mathfrak{p}}| = N(\mathfrak{p})^{t}$ (up to a unit-modulus factor from the finite part, which has $|\chi_{\mathfrak{p}}(\varpi_{\mathfrak{p}})| = 1$ for unramified $\mathfrak{p}$, and the infinity-type part has $|\sigma_v(\varpi_{\mathfrak{p}})^{a_v}\overline{\sigma_v(\varpi_{\mathfrak{p}})}^{b_v}| = N(\mathfrak{p})^{(a_v+b_v)/2}$). More directly, the norm contribution gives $|\alpha_{\mathfrak{p}}| = N(\mathfrak{p})^{t + \text{(type contribution)}}$. For $\alpha_{\mathfrak{p}}$ to be a root of unity we need $|\alpha_{\mathfrak{p}}| = 1$ for all $\mathfrak{p}$. Since $N(\mathfrak{p})$ takes arbitrarily large values (over all primes), the only way $N(\mathfrak{p})^t = 1$ for all $\mathfrak{p}$ is $t = 0$.

**(b) Vanishing of the infinity type.** Suppose some $(a_{v_0}, b_{v_0}) \neq (0,0)$. Then the Satake parameter contains the factor $\sigma_{v_0}(\varpi_{\mathfrak{p}})^{a_{v_0}} \overline{\sigma_{v_0}(\varpi_{\mathfrak{p}})}^{\,b_{v_0}}$, whose argument varies continuously with the prime $\mathfrak{p}$ (via the embedding $\sigma_{v_0}$). By Chebotarev-type equidistribution (or more elementarily, by the density of primes with prescribed splitting behavior), the arguments of these factors are equidistributed on the circle. A root of unity has argument in $\frac{2\pi}{m}\mathbb{Z}$ for some fixed $m$; an equidistributed continuous family cannot lie entirely in such a discrete set unless the exponent is zero. Hence $a_{v_0} = b_{v_0} = 0$.

Therefore $\chi$ has **trivial infinity type** and **zero norm exponent**, meaning $\chi$ is a **finite-order** (type $A_0$) Hecke character: $\chi^m = 1$ for some $m \geq 1$.

### Step 3: Finite-order Hecke characters give Artin $L$-functions

By **class field theory** (the Artin reciprocity map), a finite-order Hecke character $\chi$ of $K$ factors through the abelianization of the Galois group:

$$\chi: \mathbb{A}_K^{\times}/K^{\times} \twoheadrightarrow \mathrm{Gal}(K^{\mathrm{ab}}/K)^{\mathrm{ab}} \to \mathbb{C}^{\times}.$$

Concretely, there exists a finite abelian extension $L/K$ with $\mathrm{Gal}(L/K) \cong \Delta$ and a character $\tilde{\chi}: \Delta \to \mathbb{C}^{\times}$ such that the diagram commutes:

$$\chi = \tilde{\chi} \circ \mathrm{rec}_K,$$

where $\mathrm{rec}_K: \mathbb{A}_K^{\times}/K^{\times} \to \mathrm{Gal}(K^{\mathrm{ab}}/K)$ is the Artin reciprocity map.

The Hecke $L$-function then satisfies:

$$L(s, \chi) = \prod_{\mathfrak{p}} \big(1 - \chi(\varpi_{\mathfrak{p}})\, N(\mathfrak{p})^{-s}\big)^{-1} = \prod_{\mathfrak{p}} \big(1 - \tilde{\chi}(\mathrm{Frob}_{\mathfrak{p}})\, N(\mathfrak{p})^{-s}\big)^{-1} = L(s, \tilde{\chi}),$$

where the last expression is the **Artin $L$-function** of the one-dimensional representation $\tilde{\chi}$ of $\mathrm{Gal}(L/K)$.

The archimedean local factors also match: since $\chi$ has trivial infinity type, the Hecke $L$-function's $\Gamma$-factors are $\Gamma_{\mathbb{R}}(s)$ or $\Gamma_{\mathbb{C}}(s)$ (the "unramified" archimedean factors), which are exactly the $\Gamma$-factors of the Artin $L$-function for a finite-order character.

### Conclusion

We have shown:

$$\boxed{\text{If all local eigenvalues of a Hecke } L\text{-function } L(s,\chi) \text{ are roots of unity, then } L(s,\chi) \text{ is an Artin } L\text{-function.}}$$

The argument proceeds in three steps:
1. The unit-root condition forces the Hecke character $\chi$ to have trivial infinity type and zero norm exponent (Step 2), making $\chi$ a finite-order character.
2. By class field theory, a finite-order Hecke character corresponds to a character of the Galois group (Step 3).
3. The Hecke $L$-function of such a character coincides with the Artin $L$-function of the corresponding Galois character.

The converse (Artin $\Rightarrow$ unit-root eigenvalues) holds by Step 1, since the Galois group is finite. Hence the condition is both necessary and sufficient.
