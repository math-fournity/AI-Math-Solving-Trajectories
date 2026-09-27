# Convergence of $\sum_{n=1}^{\infty} g_n z^n$

**Problem.** Let $g_n$ denote the number of isomorphism classes of groups of order $n$. Determine the values of $z$ for which the generating function $\sum_{n=1}^{\infty} g_n z^n$ converges.

**Answer.** The series converges if and only if $|z| < 1$.

---

## Proof

We determine the radius of convergence $R$ via the Cauchy–Hadamard formula:

$$\frac{1}{R} = \limsup_{n \to \infty} g_n^{1/n}.$$

We show that $\lim_{n\to\infty} g_n^{1/n} = 1$, which gives $R = 1$. We then check the boundary $|z| = 1$.

### Step 1: Lower bound $g_n^{1/n} \geq 1$

For every $n \geq 1$, the cyclic group $\mathbb{Z}/n\mathbb{Z}$ is a group of order $n$, so $g_n \geq 1$. Hence

$$g_n^{1/n} \geq 1 \quad \text{for all } n \geq 1,$$

which gives $\limsup_{n\to\infty} g_n^{1/n} \geq 1$.

### Step 2: Upper bound — groups of prime-power order

The dominant contribution to $g_n$ comes from prime-power orders. We use the following classical result:

> **Theorem (Higman 1960, Sims 1965).** The number of groups of order $p^k$ (for prime $p$) satisfies
> $$g_{p^k} = p^{\,\frac{2}{27}k^3 + O(k^{8/3})},$$
> where the implied constant is absolute (independent of $p$ and $k$).

Setting $n = p^k$, so $k = \log_p n$, we compute:

$$\log g_{p^k} = \left(\frac{2}{27}k^3 + O(k^{8/3})\right)\log p = \frac{2}{27}\frac{(\log n)^3}{(\log p)^2} + O\!\left(\frac{(\log n)^{8/3}}{(\log p)^{5/3}}\right).$$

Since $n = p^k$, the ratio $\frac{\log g_{p^k}}{n} = \frac{\log g_{p^k}}{p^k} \to 0$ as $k \to \infty$ (the numerator is polynomial in $k$ while the denominator is exponential in $k$). Therefore

$$g_{p^k}^{1/p^k} = e^{\,\log g_{p^k}\,/\,p^k} \to e^0 = 1 \quad \text{as } k \to \infty.$$

### Step 3: Upper bound — general $n$

For general $n$, write the prime factorization $n = p_1^{a_1} \cdots p_r^{a_r}$ and let $\mu(n) = \max_i a_i$ denote the largest exponent. We use:

> **Theorem (Pyber, 1993).** The number of groups of order $n$ satisfies
> $$g_n \leq n^{\,\left(\frac{2}{27} + o(1)\right)\mu(n)^2},$$
> where the $o(1)$ term tends to $0$ as $\mu(n) \to \infty$.

Since $\mu(n) \leq \log_2 n$ (because $2^{\mu(n)} \leq n$), we obtain:

$$g_n \leq n^{\,C(\log n)^2}$$

for some absolute constant $C > 0$ and all sufficiently large $n$. Taking logarithms:

$$\log g_n \leq C\,(\log n)^3.$$

Therefore

$$\frac{\log g_n}{n} \leq \frac{C\,(\log n)^3}{n} \to 0 \quad \text{as } n \to \infty,$$

which gives

$$g_n^{1/n} = e^{\,\log g_n\,/\,n} \leq e^{\,C(\log n)^3\,/\,n} \to 1 \quad \text{as } n \to \infty.$$

### Step 4: Radius of convergence

Combining Steps 1 and 3:

$$1 \leq \liminf_{n\to\infty} g_n^{1/n} \leq \limsup_{n\to\infty} g_n^{1/n} \leq 1,$$

so $\lim_{n\to\infty} g_n^{1/n} = 1$. By the Cauchy–Hadamard formula, the radius of convergence is

$$R = \frac{1}{\limsup_{n\to\infty} g_n^{1/n}} = 1.$$

The series converges absolutely for $|z| < 1$ and diverges for $|z| > 1$.

### Step 5: Boundary $|z| = 1$

When $|z| = 1$, we have $|g_n z^n| = g_n \geq 1$ for all $n \geq 1$. Since the terms of the series do not tend to zero, the series diverges (the necessary condition for convergence, $g_n z^n \to 0$, fails).

### Conclusion

The generating function $\sum_{n=1}^{\infty} g_n z^n$ converges if and only if $|z| < 1$.

$$\boxed{|z| < 1}$$
