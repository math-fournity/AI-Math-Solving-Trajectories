# Proof: $f(n) > n^2 \ln n$ eventually

## Problem

Let $(a_k)_{k \geq 1}$ be a positive sequence with $\sum_{k \geq 1} a_k = L < \infty$. Define $f(n) := \sum_{k=1}^n \frac{1}{a_k}$. Prove that there exists $n_0$ such that for all $n \geq n_0$, $f(n) > n^2 \ln n$.

## Answer

The proposition is **true**: such an $n_0$ exists.

## Proof

We prove by contradiction. Assume that $f(n) \leq n^2 \ln n$ for infinitely many $n$. Let $\mathcal{B} = \{n_1 < n_2 < n_3 < \cdots\}$ be the infinite set of indices where $f(n_i) \leq n_i^2 \ln n_i$.

We split into two complementary cases.

### Case 1: $n_{i+1} > 2n_i$ for infinitely many $i$.

Pass to a subsequence of $\mathcal{B}$, still denoted $(n_i)_{i \geq 1}$, such that $n_{i+1} > 2n_i$ for every $i$. (This is possible by selecting the indices where the condition holds; consecutive selected indices $i_j < i_{j+1}$ satisfy $n_{i_{j+1}} \geq n_{i_j + 1} > 2n_{i_j}$.)

For each $i$, define the interval $I_i := \bigl[\lfloor n_i / 2 \rfloor + 1,\; n_i\bigr]$, which has $|I_i| \geq n_i/3$ elements (for $n_i \geq 6$).

**Disjointness.** Since $n_{i+1} > 2n_i$, we have $\lfloor n_{i+1}/2 \rfloor \geq n_i$, so $I_{i+1}$ starts at $\lfloor n_{i+1}/2 \rfloor + 1 > n_i$, which is past the end of $I_i$. Thus the intervals $I_1, I_2, \ldots$ are pairwise disjoint.

**Lower bound on $\sum_{k \in I_i} a_k$.** Since $f$ is increasing and $f(\lfloor n_i/2 \rfloor) \geq 0$:

$$\sum_{k \in I_i} \frac{1}{a_k} = f(n_i) - f(\lfloor n_i/2 \rfloor) \leq f(n_i) \leq n_i^2 \ln n_i.$$

By the Cauchy–Schwarz inequality applied to the $|I_i|$ terms in $I_i$:

$$\left(\sum_{k \in I_i} a_k\right)\left(\sum_{k \in I_i} \frac{1}{a_k}\right) \geq |I_i|^2 \geq \frac{n_i^2}{9}.$$

Therefore:

$$\sum_{k \in I_i} a_k \geq \frac{n_i^2/9}{n_i^2 \ln n_i} = \frac{1}{9 \ln n_i}.$$

**Divergence.** Since $n_{i+1} > 2n_i$, we have $n_i > 2^{i-1} n_1$, so $\ln n_i > (i-1)\ln 2 + \ln n_1$. The intervals being disjoint:

$$\sum_{k=1}^{\infty} a_k \geq \sum_{i=1}^{\infty} \sum_{k \in I_i} a_k \geq \sum_{i=1}^{\infty} \frac{1}{9 \ln n_i} \geq \frac{1}{9} \sum_{i=1}^{\infty} \frac{1}{(i-1)\ln 2 + \ln n_1 + 1} = +\infty.$$

This contradicts $\sum a_k = L < \infty$.

### Case 2: $n_{i+1} \leq 2n_i$ for all sufficiently large $i$.

Let $I_0$ be such that $n_{i+1} \leq 2n_i$ for all $i \geq I_0$.

**Global bound on $f$.** For any $n \geq n_{I_0}$, let $i \geq I_0$ be the largest index with $n_i \leq n$. Then $n < n_{i+1} \leq 2n_i \leq 2n$, and since $f$ is increasing:

$$f(n) \leq f(n_{i+1}) \leq n_{i+1}^2 \ln n_{i+1} \leq (2n)^2 \ln(2n) = 4n^2 \ln(2n).$$

For $n \geq 3$, $\ln(2n) \leq 2\ln n$, so:

$$f(n) \leq 8\, n^2 \ln n \qquad \text{for all } n \geq \max(n_{I_0},\, 3). \tag{$\star$}$$

**Dyadic interval estimates.** Let $J_0$ be large enough that $2^{J_0} \geq \max(n_{I_0}, 3)$. For each $j \geq J_0$, consider the dyadic interval $D_j := \{2^j + 1, \ldots, 2^{j+1}\}$ of size $|D_j| = 2^j$.

From $(\star)$:

$$f(2^{j+1}) \leq 8 \cdot 4^{j+1} \cdot (j+1)\ln 2.$$

From Cauchy–Schwarz on $\{1, \ldots, 2^j\}$ (with $2^j$ terms):

$$f(2^j) \geq \frac{(2^j)^2}{\sum_{k=1}^{2^j} a_k} \geq \frac{4^j}{L}.$$

Therefore:

$$\sum_{k \in D_j} \frac{1}{a_k} = f(2^{j+1}) - f(2^j) \leq 8 \cdot 4^{j+1} \cdot (j+1)\ln 2.$$

Applying Cauchy–Schwarz to the $2^j$ terms in $D_j$:

$$\left(\sum_{k \in D_j} a_k\right)\left(\sum_{k \in D_j} \frac{1}{a_k}\right) \geq (2^j)^2 = 4^j.$$

Hence:

$$\sum_{k \in D_j} a_k \geq \frac{4^j}{8 \cdot 4^{j+1} \cdot (j+1)\ln 2} = \frac{1}{32\,(j+1)\ln 2}.$$

**Divergence.** The dyadic intervals $D_{J_0}, D_{J_0+1}, \ldots$ are pairwise disjoint, so:

$$\sum_{k=1}^{\infty} a_k \geq \sum_{j=J_0}^{\infty} \sum_{k \in D_j} a_k \geq \frac{1}{32\ln 2} \sum_{j=J_0}^{\infty} \frac{1}{j+1} = +\infty.$$

This again contradicts $\sum a_k = L < \infty$.

### Conclusion

Both cases lead to a contradiction. Therefore, our assumption was false: there are only finitely many $n$ with $f(n) \leq n^2 \ln n$. Equivalently, there exists $n_0$ such that for all $n \geq n_0$:

$$\boxed{f(n) > n^2 \ln n.}$$

### PROOF COMPLETE
