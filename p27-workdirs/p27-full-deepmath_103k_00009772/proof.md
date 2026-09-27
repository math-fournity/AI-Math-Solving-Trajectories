# Proof

**Answer:** Yes, such measures exist.

---

## Construction

Let $M \geq 2$ be an integer. Define two Borel probability measures $\mu$ and $\nu$ on $\mathbb{R}$ as the distributions of the following independent random series:

$$S = \sum_{n=1}^{\infty} \frac{X_n}{M^{2n}}, \qquad T = \sum_{n=1}^{\infty} \frac{Y_n}{M^{2n-1}},$$

where $\{X_n\}_{n \geq 1}$ and $\{Y_n\}_{n \geq 1}$ are independent families of i.i.d. random variables, each uniformly distributed on $\{0, 1, \ldots, M-1\}$. Set $\mu = \mathrm{Law}(S)$ and $\nu = \mathrm{Law}(T)$.

---

## Step 1: $\mu$ and $\nu$ are finite complex measures with compact support

Both $\mu$ and $\nu$ are probability measures (total mass $1$), hence finite positive (and thus complex) measures.

**Compact support of $\mu$:** Since $0 \leq X_n \leq M-1$,

$$0 \leq S \leq \sum_{n=1}^{\infty} \frac{M-1}{M^{2n}} = \frac{M-1}{M^2 - 1} = \frac{1}{M+1}.$$

So $\mu$ is supported on $\left[0, \frac{1}{M+1}\right]$.

**Compact support of $\nu$:** Similarly,

$$0 \leq T \leq \sum_{n=1}^{\infty} \frac{M-1}{M^{2n-1}} = \frac{(M-1) \cdot M^{-1}}{1 - M^{-2}} = \frac{M}{M+1}.$$

So $\nu$ is supported on $\left[0, \frac{M}{M+1}\right]$.

---

## Step 2: $\mu$ is singular with respect to Lebesgue measure

The support of $\mu$ is the self-similar set

$$E = \left\{\sum_{n=1}^{\infty} \frac{x_n}{M^{2n}} : x_n \in \{0, 1, \ldots, M-1\}\right\} \subseteq \left[0, \frac{1}{M+1}\right].$$

We show $E$ has Lebesgue measure zero by a covering argument. For each $N \geq 1$ and each digit string $(x_1, \ldots, x_N) \in \{0, \ldots, M-1\}^N$, define the interval

$$I_{x_1, \ldots, x_N} = \left[\sum_{n=1}^{N} \frac{x_n}{M^{2n}},\; \sum_{n=1}^{N} \frac{x_n}{M^{2n}} + \sum_{n=N+1}^{\infty} \frac{M-1}{M^{2n}}\right].$$

Every point of $E$ lies in one of these $M^N$ intervals. The length of each interval is

$$\sum_{n=N+1}^{\infty} \frac{M-1}{M^{2n}} = \frac{(M-1) \cdot M^{-2(N+1)}}{1 - M^{-2}} = \frac{M^{-2N}}{M+1}.$$

The total covering length is therefore

$$M^N \cdot \frac{M^{-2N}}{M+1} = \frac{M^{-N}}{M+1} \xrightarrow{N \to \infty} 0.$$

Hence $|E| = 0$. Since $\mu$ is supported on $E$, $\mu$ is singular with respect to Lebesgue measure. $\checkmark$

---

## Step 3: $\nu$ is singular with respect to Lebesgue measure

The support of $\nu$ is the self-similar set

$$F = \left\{\sum_{n=1}^{\infty} \frac{y_n}{M^{2n-1}} : y_n \in \{0, 1, \ldots, M-1\}\right\} \subseteq \left[0, \frac{M}{M+1}\right].$$

By the identical covering argument (at level $N$, cover $F$ by $M^N$ intervals each of length $\frac{M^{-(2N-1)}}{M+1} \cdot M^{-1}$; more precisely, each interval has length $\sum_{n>N} (M-1)/M^{2n-1} = \frac{M^{-(2N-1)}}{M+1}$), the total covering length is

$$M^N \cdot \frac{M^{-(2N-1)}}{M+1} = \frac{M^{-N+1}}{M+1} \xrightarrow{N \to \infty} 0.$$

Hence $|F| = 0$, and $\nu$ is singular with respect to Lebesgue measure. $\checkmark$

---

## Step 4: $\mu * \nu$ is absolutely continuous (in fact, equals Lebesgue measure on $[0,1]$)

Since $S$ and $T$ are independent, $\mu * \nu$ is the law of $S + T$. We compute:

$$S + T = \sum_{n=1}^{\infty} \frac{X_n}{M^{2n}} + \sum_{n=1}^{\infty} \frac{Y_n}{M^{2n-1}} = \sum_{k=1}^{\infty} \frac{Z_k}{M^k},$$

where the $\{Z_k\}$ are defined by interleaving:

$$Z_{2n-1} = Y_n, \qquad Z_{2n} = X_n, \qquad n = 1, 2, 3, \ldots$$

Since all the $X_n$ and $Y_n$ are independent and uniformly distributed on $\{0, 1, \ldots, M-1\}$, the $\{Z_k\}_{k \geq 1}$ are i.i.d. uniform on $\{0, 1, \ldots, M-1\}$.

The random variable $\sum_{k=1}^{\infty} Z_k / M^k$ with i.i.d. uniform $M$-adic digits is the standard representation of a random variable uniformly distributed on $[0, 1]$. (The set of real numbers with non-unique $M$-adic expansions—those with a trailing string of $(M-1)$'s—is countable, hence has measure zero, and does not affect the distribution.)

**Verification via Fourier transform (optional check):** The Fourier transform of $\mu * \nu$ is

$$\widehat{\mu * \nu}(t) = \hat\mu(t) \cdot \hat\nu(t) = \prod_{n=1}^{\infty} \hat\mu_n(t) \cdot \prod_{n=1}^{\infty} \hat\nu_n(t),$$

where $\hat\mu_n(t) = \frac{1}{M}\sum_{j=0}^{M-1} e^{2\pi i j t / M^{2n}}$ and $\hat\nu_n(t) = \frac{1}{M}\sum_{j=0}^{M-1} e^{2\pi i j t / M^{2n-1}}$. Combining,

$$\widehat{\mu * \nu}(t) = \prod_{k=1}^{\infty} \frac{1}{M} \cdot \frac{1 - e^{2\pi i t / M^{k-1}}}{1 - e^{2\pi i t / M^k}}.$$

This product telescopes:

$$\widehat{\mu * \nu}(t) = \lim_{N \to \infty} \frac{1}{M^N} \cdot \frac{1 - e^{2\pi i t}}{1 - e^{2\pi i t / M^N}} = \frac{e^{2\pi i t} - 1}{2\pi i t},$$

which is the Fourier transform of the Lebesgue measure on $[0, 1]$ (with density $\mathbf{1}_{[0,1]}$). By uniqueness of the Fourier transform for finite measures, $\mu * \nu = \mathbf{1}_{[0,1]} \, dx$.

Therefore $\mu * \nu$ is absolutely continuous with respect to Lebesgue measure, with density $\mathbf{1}_{[0,1]} \in L^1(\mathbb{R})$, which is nonzero. $\checkmark$

---

## Conclusion

We have constructed two finite (probability) measures $\mu$ and $\nu$ with compact supports on $\mathbb{R}$, both singular with respect to Lebesgue measure (each supported on a set of Hausdorff dimension $\log M / \log M^2 = 1/2$), such that $\mu * \nu$ is the Lebesgue measure on $[0, 1]$, which is purely absolutely continuous and nonzero.

$$\boxed{\text{Yes}}$$

### PROOF COMPLETE
