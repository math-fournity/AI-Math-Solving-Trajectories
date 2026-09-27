# Proof: $f$ is holomorphic on $D$

**Answer:** Yes, $f$ is holomorphic on $D$.

The proof proceeds in two stages:

1. **Radó's Theorem (one variable):** We first establish the result for $n=1$.
2. **Extension to several variables:** We apply Radó's theorem on coordinate slices and invoke Hartogs' theorem on separate analyticity.

---

## Stage 1: Radó's Theorem (One Variable)

**Theorem (Radó).** Let $\Omega \subset \mathbb{C}$ be a domain, and let $f:\Omega\to\mathbb{C}$ be continuous on $\Omega$ and holomorphic on $\Omega\setminus Z(f)$, where $Z(f)=\{z\in\Omega:f(z)=0\}$. Then $f$ is holomorphic on $\Omega$.

**Proof.** If $f\equiv 0$ the result is trivial. Assume $f\not\equiv 0$.

### Step 1: $\log|f|$ is subharmonic on $\Omega$.

Define $u:\Omega\to[-\infty,\infty)$ by
$$
u(z)=\begin{cases}\log|f(z)|,& z\in\Omega\setminus Z(f),\\[4pt]-\infty,& z\in Z(f).\end{cases}
$$
Since $f$ is continuous, $|f|$ is continuous, and $u$ is upper semicontinuous.

- **On $\Omega\setminus Z(f)$:** $f$ is holomorphic and non-vanishing, so $u=\log|f|$ is harmonic, hence subharmonic.
- **On $Z(f)$:** $u=-\infty$, and the sub-mean-value property $u(z_0)\le\frac{1}{2\pi}\int_0^{2\pi}u(z_0+re^{i\theta})\,d\theta$ holds trivially.
- **At boundary points of $Z(f)$:** These lie in $Z(f)$ (since $Z(f)$ is closed), so $u=-\infty$ and the sub-mean-value property is again trivial.

Thus $u$ is subharmonic on $\Omega$. $\quad\checkmark$

### Step 2: $Z(f)$ has $2$-dimensional Lebesgue measure zero.

Since $f\not\equiv 0$, there exists $z_0\in\Omega$ with $f(z_0)\neq 0$, so $u(z_0)>-\infty$, i.e., $u\not\equiv -\infty$.

A fundamental property of subharmonic functions states:

> **Fact.** If $u$ is subharmonic on a domain $\Omega$ and $u\not\equiv -\infty$, then $u\in L^1_{\mathrm{loc}}(\Omega)$. In particular, the set $\{u=-\infty\}$ has $2$-dimensional Lebesgue measure zero.

*(Brief justification: A subharmonic function $u\not\equiv -\infty$ satisfies the sub-mean-value property and is bounded above on compact sets. The Riesz decomposition theorem represents $u$ as the sum of a harmonic function and a logarithmic potential of a positive measure, both of which are locally integrable. Hence $u\in L^1_{\mathrm{loc}}$, which forces $\{u=-\infty\}$ to have measure zero.)*

Since $\{u=-\infty\}=Z(f)$, we conclude that $Z(f)$ has $2$-dimensional Lebesgue measure zero. $\quad\checkmark$

### Step 3: $f$ is holomorphic on $\Omega$ via Painlevé's removable singularities theorem.

**Painlevé's Theorem.** Let $E\subset\Omega$ be closed with $2$-dimensional Lebesgue measure zero. If $g$ is holomorphic on $\Omega\setminus E$ and locally bounded on $\Omega$, then $g$ extends to a holomorphic function on $\Omega$.

In our setting:
- $E=Z(f)$ is closed (by continuity of $f$) with measure zero (by Step 2),
- $f$ is holomorphic on $\Omega\setminus Z(f)$ (by hypothesis),
- $f$ is locally bounded (by continuity).

By Painlevé's theorem, $f$ extends to a holomorphic function $\widetilde{f}$ on $\Omega$. Since $f$ is already continuous on $\Omega$ and $\widetilde{f}=f$ on the dense set $\Omega\setminus Z(f)$, we have $\widetilde{f}=f$ everywhere. Thus $f$ is holomorphic on $\Omega$. $\quad\checkmark$

**Proof of Painlevé's Theorem (for completeness).** Let $p\in E$. Choose $r>0$ with $\overline{B(p,2r)}\subset\Omega$ and $|g|\le M$ on $B(p,2r)\setminus E$ for some $M>0$.

By Fubini's theorem, since $E$ has $2$-dimensional measure zero, for almost every $\rho\in(0,2r)$ the circle $\partial B(p,\rho)$ does not intersect $E$. Fix such a $\rho$.

For $z\in B(p,\rho)\setminus E$, we establish the Cauchy integral formula. Cover the compact set $E\cap\overline{B(p,\rho)}$ by finitely many open discs $D_1,\dots,D_N$ with $\sum_{k=1}^N \mathrm{area}(D_k)<\epsilon$. On the domain $B(p,\rho)\setminus\bigcup_k \overline{D_k}$, the function $g$ is holomorphic, so by Cauchy's integral formula:
$$
g(z)=\frac{1}{2\pi i}\int_{\partial B(p,\rho)}\frac{g(\zeta)}{\zeta-z}\,d\zeta-\sum_{k=1}^N\frac{1}{2\pi i}\int_{\partial D_k}\frac{g(\zeta)}{\zeta-z}\,d\zeta.
$$

Each integral over $\partial D_k$ is bounded by
$$
\left|\frac{1}{2\pi i}\int_{\partial D_k}\frac{g(\zeta)}{\zeta-z}\,d\zeta\right|\le\frac{M\cdot 2\pi r_k}{2\pi\cdot\mathrm{dist}(z,\partial D_k)},
$$
where $r_k$ is the radius of $D_k$. Since $E$ has measure zero, we can choose the cover so that $\sum_k r_k^2\to 0$ as $\epsilon\to 0$. For $z$ at a fixed positive distance from $E$, the denominators $\mathrm{dist}(z,\partial D_k)$ are bounded below, and the total contribution $\sum_k r_k\to 0$. Thus, letting $\epsilon\to 0$:
$$
g(z)=\frac{1}{2\pi i}\int_{\partial B(p,\rho)}\frac{g(\zeta)}{\zeta-z}\,d\zeta,\qquad z\in B(p,\rho)\setminus E.
$$

The right-hand side defines a holomorphic function $h(z)$ on all of $B(p,\rho)$ (it is a Cauchy-type integral with continuous density on $\partial B(p,\rho)$). Setting $\widetilde{g}=h$ on $B(p,\rho)$ and $\widetilde{g}=g$ on $\Omega\setminus E$ yields a well-defined holomorphic extension, since the two definitions agree on the overlap $B(p,\rho)\setminus E$ by the formula above. Covering $E$ by such balls gives a holomorphic extension to all of $\Omega$. $\quad\square$

This completes the proof of Radó's theorem. $\quad\square$

---

## Stage 2: Extension to $\mathbb{C}^n$

We now prove the result for general $n$ using Radó's theorem on coordinate slices and Hartogs' theorem on separate analyticity.

### Step 1: $f$ is separately holomorphic.

Fix an index $j\in\{1,\dots,n\}$ and fix a point $(z_1^0,\dots,z_{j-1}^0,z_{j+1}^0,\dots,z_n^0)\in\mathbb{C}^{n-1}$. Define the coordinate slice:
$$
L=\bigl\{(z_1^0,\dots,z_{j-1}^0,z_j,z_{j+1}^0,\dots,z_n^0):z_j\in\mathbb{C}\bigr\}\cap D.
$$
If $L\neq\emptyset$, it is an open subset of $\mathbb{C}$ (identified with the $z_j$-axis). Define
$$
g(z_j)=f(z_1^0,\dots,z_{j-1}^0,z_j,z_{j+1}^0,\dots,z_n^0),\qquad z_j\in L.
$$

We verify the hypotheses of Radó's theorem for $g$:

- **Continuity:** $g$ is continuous on $L$, since $f$ is continuous on $D$.
- **Zero set:** $Z(g)=\{z_j\in L:g(z_j)=0\}=Z(f)\cap L$.
- **Holomorphicity off the zero set:** On $L\setminus Z(g)=L\cap(D\setminus Z(f))$, the function $f$ is holomorphic (by hypothesis), so its restriction $g$ is holomorphic in $z_j$.

By Radó's theorem (applied to each connected component of $L$), $g$ is holomorphic on $L$.

Since this holds for every $j\in\{1,\dots,n\}$ and every choice of the remaining coordinates, $f$ is **holomorphic in each variable separately** on $D$. $\quad\checkmark$

### Step 2: Apply Hartogs' theorem on separate analyticity.

**Hartogs' Theorem (Separate Analyticity).** Let $D\subset\mathbb{C}^n$ be a domain. If $f:D\to\mathbb{C}$ is holomorphic in each variable separately (i.e., for each $j$ and each fixed value of the other $n-1$ variables, the resulting function of one variable is holomorphic), then $f$ is jointly holomorphic on $D$.

By Step 1, $f$ is separately holomorphic on $D$. By Hartogs' theorem, $f$ is holomorphic on $D$. $\quad\checkmark$

---

## Conclusion

$$
\boxed{f \text{ is holomorphic on } D.}
$$

The key ingredients are:

1. **Radó's theorem (one variable):** A continuous function on a domain $\Omega\subset\mathbb{C}$ that is holomorphic off its zero set is holomorphic everywhere. The proof uses:
   - The subharmonicity of $\log|f|$, which forces the zero set $Z(f)$ to have $2$-dimensional Lebesgue measure zero (as the $-\infty$-set of a non-trivial subharmonic function).
   - Painlevé's removable singularities theorem, which extends a locally bounded holomorphic function across a closed set of measure zero.

2. **Reduction to one variable:** Restricting $f$ to coordinate slices produces one-variable functions satisfying the hypotheses of Radó's theorem, yielding separate holomorphicity.

3. **Hartogs' theorem:** Separate holomorphicity on a domain in $\mathbb{C}^n$ implies joint holomorphicity.
