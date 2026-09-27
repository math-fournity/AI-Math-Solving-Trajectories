# Proof: Coefficients of monic factors are integral over $R_1$

**Problem.** Let $R_1 \subset R_2$ be two commutative rings with identity. Suppose $f \in R_1[x]$ factors as $f = gh$ with $g, h \in R_2[x]$, and both $g$ and $h$ are monic. Are the coefficients of $g$ and $h$ integral over $R_1$?

**Answer.** Yes. $\boxed{\text{Yes}}$

---

## Proof

### Step 1: $f$ is monic

Write
$$g = x^r + b_{r-1}x^{r-1} + \cdots + b_0, \qquad h = x^s + c_{s-1}x^{s-1} + \cdots + c_0,$$
with $b_i, c_j \in R_2$. Since $g$ and $h$ are both monic, the leading coefficient of $f = gh$ is $1 \cdot 1 = 1$. Hence $f$ is monic:
$$f = x^n + a_{n-1}x^{n-1} + \cdots + a_0 \in R_1[x], \qquad n = r + s.$$

### Step 2: The domain case

Assume first that $R_2$ is an integral domain. Let $K = \operatorname{Frac}(R_2)$ and let $\bar{K}$ be an algebraic closure of $K$. Over $\bar{K}[x]$ we may factor
$$g = \prod_{i=1}^{r}(x - \alpha_i), \qquad h = \prod_{j=1}^{s}(x - \beta_j),$$
so that
$$f = \prod_{i=1}^{r}(x - \alpha_i)\prod_{j=1}^{s}(x - \beta_j).$$

Each $\alpha_i$ and $\beta_j$ is a root of $f$. Since $f \in R_1[x]$ is monic, every root of $f$ is integral over $R_1$ (it satisfies the monic polynomial $f$). Thus each $\alpha_i, \beta_j$ is integral over $R_1$.

The coefficients of $g$ are the elementary symmetric polynomials in $\alpha_1, \ldots, \alpha_r$:
$$b_k = (-1)^{r-k}\, e_{r-k}(\alpha_1, \ldots, \alpha_r), \qquad k = 0, \ldots, r-1.$$
Since the set of elements of $\bar{K}$ integral over $R_1$ forms a subring (integrality is preserved under addition and multiplication), each $b_k$ is integral over $R_1$. The same argument applies to the coefficients $c_0, \ldots, c_{s-1}$ of $h$. This establishes the domain case.

### Step 3: Reduction to the domain case (key claim)

Now consider the general case (no assumption on $R_2$). Let $b$ be any coefficient of $g$ or $h$. Define the finitely generated $R_1$-subalgebra
$$R_2' = R_1[\,b_0, \ldots, b_{r-1},\, c_0, \ldots, c_{s-1}\,] \subseteq R_2,$$
and consider the evaluation homomorphism
$$\operatorname{ev}_b : R_1[t] \longrightarrow R_2', \qquad t \longmapsto b.$$
Let $I = \ker(\operatorname{ev}_b)$. Then $b$ is integral over $R_1$ if and only if $I$ contains a monic polynomial.

**Claim.** Every prime ideal $\mathfrak{P}$ of $R_1[t]$ containing $I$ contains a monic polynomial.

*Proof of Claim.* The ideal $\mathfrak{q} := \mathfrak{P}/I$ is a prime ideal of $R_1[t]/I \cong R_1[b] \subseteq R_2'$. Extend $\mathfrak{q}$ to a prime ideal $\mathfrak{q}'$ of $R_2'$ (every prime ideal extends to a prime ideal in an over-ring via Zorn's lemma / localization). Consider the integral domain
$$D := R_2'/\mathfrak{q}', \qquad \bar{b} := \text{image of } b \text{ in } D.$$

The factorization $f = gh$ descends to $D[x]$: writing $\bar{g}, \bar{h}$ for the images of $g, h$, we have $f = \bar{g}\bar{h}$ in $D[x]$, and $\bar{g}, \bar{h}$ remain monic. By the domain case (Step 2), $\bar{b}$ is integral over the image $\bar{R}_1 := R_1/(\mathfrak{q}' \cap R_1)$.

Hence there exist $\bar{a}_0, \ldots, \bar{a}_{m-1} \in \bar{R}_1$ such that
$$\bar{b}^{\,m} + \bar{a}_{m-1}\bar{b}^{\,m-1} + \cdots + \bar{a}_0 = 0 \quad \text{in } D.$$
Lifting to $R_1[t]$: there exist $a_0, \ldots, a_{m-1} \in R_1$ such that the monic polynomial
$$q(t) = t^m + a_{m-1}t^{m-1} + \cdots + a_0 \in R_1[t]$$
satisfies $q(b) \in \mathfrak{q}'$. Since $q(b) = \operatorname{ev}_b(q) \in \mathfrak{q}' \cap R_1[b] = \mathfrak{q}$, we have $q \in \mathfrak{P}$. Thus $\mathfrak{P}$ contains the monic polynomial $q$. $\square$

### Step 4: Conclusion via Zorn's lemma

Let $S \subseteq R_1[t]$ be the multiplicative set of all monic polynomials. Suppose for contradiction that $I \cap S = \emptyset$. Then in the localization $S^{-1}R_1[t]$, the ideal $S^{-1}I$ is proper. By Zorn's lemma, $S^{-1}I$ is contained in a maximal ideal $\mathfrak{m}$ of $S^{-1}R_1[t]$. The contraction
$$\mathfrak{P} := \mathfrak{m} \cap R_1[t]$$
is a prime ideal of $R_1[t]$ containing $I$ and disjoint from $S$ (i.e., containing no monic polynomial).

This contradicts the Claim of Step 3, which asserts that every prime ideal containing $I$ must contain a monic polynomial. Therefore $I \cap S \neq \emptyset$; that is, $I$ contains a monic polynomial, and $b$ is integral over $R_1$.

Since $b$ was an arbitrary coefficient of $g$ or $h$, **all coefficients of $g$ and $h$ are integral over $R_1$**. $\blacksquare$

### PROOF COMPLETE
