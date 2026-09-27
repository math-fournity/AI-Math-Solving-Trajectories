# Proof: Compactness via Truncation in $L^p$

## Problem Statement

Let $f_n:[a,b]\to\mathbb{R}$, $n\in\mathbb{N}$, be a sequence of $L^p$ functions for some $p\in(1,\infty)$. For every fixed $m\in\mathbb{N}^*$, suppose the sequence $\{f_n\,\psi_m(f_n)\}_{n\in\mathbb{N}}$ has a strongly convergent subsequence in $L^p([a,b])$, where $\psi_m$ is smooth with

$$
\psi_m(f)=\begin{cases}1 & \text{if } |f|\ge 1/m,\\ 0 & \text{if } |f|\le 1/(2m),\end{cases}\qquad 0\le\psi_m\le 1.
$$

**Claim:** $\{f_n\}$ has a strongly convergent subsequence in $L^p([a,b])$.

---

## Proof

### Step 1: Key Decomposition

For every $n$ and $m$, write

$$
f_n = f_n\,\psi_m(f_n) + f_n\,(1-\psi_m(f_n)). \tag{1}
$$

We estimate the second term. By definition of $\psi_m$:

- Where $\psi_m(f_n)=1$ (i.e., $|f_n|\ge 1/m$): the factor $(1-\psi_m(f_n))=0$, so $f_n(1-\psi_m(f_n))=0$.
- Where $\psi_m(f_n)=0$ (i.e., $|f_n|\le 1/(2m)$): $|f_n(1-\psi_m(f_n))|=|f_n|\le 1/(2m)$.
- Where $0<\psi_m(f_n)<1$ (i.e., $1/(2m)<|f_n|<1/m$): $|f_n(1-\psi_m(f_n))|\le |f_n|<1/m$.

In all cases, $|f_n(1-\psi_m(f_n))|\le 1/m$ pointwise. Therefore

$$
\|f_n(1-\psi_m(f_n))\|_{L^p} \le \frac{1}{m}\,(b-a)^{1/p}. \tag{2}
$$

### Step 2: Diagonal Subsequence Extraction

For each $m\in\mathbb{N}^*$, by hypothesis, $\{f_n\,\psi_m(f_n)\}_n$ has a convergent subsequence in $L^p$. We extract nested subsequences:

- **$m=1$:** There exists a subsequence $\{n^{(1)}_k\}_{k\ge1}$ of $\mathbb{N}$ such that $\{f_{n^{(1)}_k}\,\psi_1(f_{n^{(1)}_k})\}_k$ converges in $L^p$.
- **$m=2$:** From $\{n^{(1)}_k\}_k$, extract a further subsequence $\{n^{(2)}_k\}_k$ such that $\{f_{n^{(2)}_k}\,\psi_2(f_{n^{(2)}_k})\}_k$ converges in $L^p$.
- **Inductively, $m=j$:** From $\{n^{(j-1)}_k\}_k$, extract a further subsequence $\{n^{(j)}_k\}_k$ such that $\{f_{n^{(j)}_k}\,\psi_j(f_{n^{(j)}_k})\}_k$ converges in $L^p$.

Define the **diagonal subsequence** $n_k := n^{(k)}_k$.

**Key property:** For every fixed $m$, the tail $\{n_k\}_{k\ge m}$ is a subsequence of $\{n^{(m)}_j\}_{j\ge1}$.

*Proof of key property:* Since $\{n^{(j)}_k\}_k$ is a subsequence of $\{n^{(j-1)}_k\}_k$ for each $j$, by transitivity $\{n^{(k)}_k\}_{k\ge m}$ is a subsequence of $\{n^{(m)}_j\}_{j\ge1}$ (each $n^{(k)}_k$ for $k\ge m$ appears in $\{n^{(m)}_j\}$ at an increasing index position). $\square$

Consequently, for every fixed $m$, the sequence $\{f_{n_k}\,\psi_m(f_{n_k})\}_{k\ge1}$ converges in $L^p$ (its tail is a subsequence of a convergent sequence).

### Step 3: The Diagonal Subsequence is Cauchy in $L^p$

Let $g_k := f_{n_k}$. We show $\{g_k\}$ is Cauchy in $L^p$.

Fix $\varepsilon>0$. Choose $m$ large enough so that

$$
\frac{2}{m}(b-a)^{1/p} < \frac{\varepsilon}{2}. \tag{3}
$$

(This is possible since $(b-a)^{1/p}$ is a fixed constant and $1/m\to 0$.)

For this fixed $m$, the sequence $\{g_k\,\psi_m(g_k)\}_k$ converges in $L^p$, hence is Cauchy. So there exists $K$ such that for all $j,k\ge K$,

$$
\|g_j\,\psi_m(g_j) - g_k\,\psi_m(g_k)\|_{L^p} < \frac{\varepsilon}{2}. \tag{4}
$$

Now, using the decomposition (1) for both $g_j$ and $g_k$:

$$
g_j - g_k = \bigl[g_j\,\psi_m(g_j) - g_k\,\psi_m(g_k)\bigr] + \bigl[g_j(1-\psi_m(g_j)) - g_k(1-\psi_m(g_k))\bigr].
$$

By the triangle inequality and the estimate (2):

$$
\|g_j - g_k\|_{L^p} \le \|g_j\,\psi_m(g_j) - g_k\,\psi_m(g_k)\|_{L^p} + \|g_j(1-\psi_m(g_j))\|_{L^p} + \|g_k(1-\psi_m(g_k))\|_{L^p}.
$$

Applying (2) and (4) for $j,k\ge K$:

$$
\|g_j - g_k\|_{L^p} < \frac{\varepsilon}{2} + \frac{1}{m}(b-a)^{1/p} + \frac{1}{m}(b-a)^{1/p} = \frac{\varepsilon}{2} + \frac{2}{m}(b-a)^{1/p} < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon.
$$

Thus $\{g_k\}=\{f_{n_k}\}$ is Cauchy in $L^p([a,b])$.

### Step 4: Conclusion

Since $L^p([a,b])$ is a Banach space (complete) for $p\in(1,\infty)$, every Cauchy sequence converges. Therefore $\{f_{n_k}\}$ converges strongly in $L^p([a,b])$.

This proves that $\{f_n\}$ has a strongly convergent subsequence in $L^p([a,b])$. $\blacksquare$

---

## Summary of the Argument

| Step | Content |
|------|---------|
| Decomposition | $f_n = f_n\psi_m(f_n) + f_n(1-\psi_m(f_n))$, with the second term $\le 1/m$ pointwise |
| Diagonal extraction | Nested subsequences for each $m$; diagonal subsequence converges for all $m$ simultaneously |
| Cauchy estimate | For large $m$, the truncation error is $O(1/m)$; for fixed $m$, the truncated sequence is Cauchy |
| Completeness | $L^p$ is complete, so Cauchy $\Rightarrow$ convergent |

The essential idea: the truncation $\psi_m$ separates $f_n$ into a "large-value part" (which is precompact by hypothesis) and a "small-value part" (which is uniformly small in $L^p$ norm, of order $1/m$). The diagonal argument extracts a subsequence where all large-value parts converge simultaneously, and the small-value parts vanish as $m\to\infty$.
