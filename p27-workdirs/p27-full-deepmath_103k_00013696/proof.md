# Proof: Ratio of Trees with a Perfect Matching Converges to Zero

## Problem

As $n \to \infty$, does the ratio of the number of trees of order $2n$ with a perfect matching to the total number of trees of order $2n$ converge to zero?

**Answer: Yes.** We prove this for both labeled and unlabeled trees.

---

## Part I: Labeled Trees (Elementary Proof)

### Setup

- **Total labeled trees** on $2n$ vertices: $(2n)^{2n-2}$ (Cayley's formula).
- We seek an upper bound on the number of labeled trees on $[2n] = \{1, 2, \ldots, 2n\}$ that admit a perfect matching.

### Contraction Argument

**Key observation.** Let $T$ be a labeled tree on $[2n]$ with a perfect matching $M$ (a set of $n$ disjoint edges covering all $2n$ vertices). Contract each edge of $M$ to a single "super-vertex." Since $T$ has $2n$ vertices and $2n-1$ edges, and we contract $n$ edges, the result is a tree $S$ on $n$ super-vertices with $n-1$ edges.

**Reconstruction.** Conversely, given:
1. A perfect matching $M$ on $[2n]$ (a partition into $n$ pairs), and
2. A labeled tree $S$ on $n$ vertices (the super-vertices, labeled by their pairs),

we can reconstruct a tree $T$ on $[2n]$ containing $M$ as follows: for each edge $(v_i, v_j)$ of $S$ (where $v_i$ corresponds to pair $\{a_i, b_i\}$ and $v_j$ to pair $\{a_j, b_j\}$), we choose which endpoint of pair $i$ connects to which endpoint of pair $j$. There are $2 \times 2 = 4$ choices per edge.

**Validity.** The result always has $2n$ vertices (the original labels) and $n + (n-1) = 2n - 1$ edges (the $n$ matching edges plus $n-1$ inter-pair edges). It is connected (since $S$ is connected and each super-vertex is internally connected by its matching edge), hence it is a tree. Different choices yield different trees, and different super-trees yield different trees.

### Counting (Tree, Perfect Matching) Pairs

For a **fixed** perfect matching $M$ on $[2n]$:
- Number of labeled trees on $n$ super-vertices: $n^{n-2}$ (Cayley).
- Number of endpoint choices: $4^{n-1}$.

So the number of labeled trees on $[2n]$ containing $M$ is $n^{n-2} \cdot 4^{n-1}$.

The number of perfect matchings on $[2n]$ is $(2n-1)!! = \frac{(2n)!}{2^n \, n!}$.

The total number of pairs $(T, M)$ where $T$ is a labeled tree on $[2n]$ and $M$ is a perfect matching of $T$ is:

$$N_{\text{pairs}} = \frac{(2n)!}{2^n \, n!} \cdot n^{n-2} \cdot 4^{n-1}.$$

### Upper Bound on Trees with a Perfect Matching

Every tree with at least one perfect matching contributes at least one pair, so:

$$\#\{T \text{ with PM}\} \leq N_{\text{pairs}} = \frac{(2n)!}{2^n \, n!} \cdot n^{n-2} \cdot 4^{n-1}.$$

### Asymptotic Ratio

The ratio is bounded above by:

$$R_n = \frac{N_{\text{pairs}}}{(2n)^{2n-2}} = \frac{(2n)! \cdot n^{n-2} \cdot 4^{n-1}}{2^n \, n! \cdot (2n)^{2n-2}}.$$

Simplify using $(2n)^{2n-2} = 2^{2n-2} \cdot n^{2n-2}$ and $4^{n-1} = 2^{2n-2}$:

$$R_n = \frac{(2n)!}{2^n \, n! \, n^n}.$$

By Stirling's approximation, $(2n)! \sim \sqrt{4\pi n} \left(\frac{2n}{e}\right)^{2n}$ and $n! \sim \sqrt{2\pi n} \left(\frac{n}{e}\right)^n$:

$$R_n \sim \frac{\sqrt{4\pi n} \cdot (2n)^{2n} / e^{2n}}{2^n \cdot \sqrt{2\pi n} \cdot n^n / e^n \cdot n^n} = \sqrt{2} \cdot \frac{2^{2n} \cdot n^{2n} / e^{2n}}{2^n \cdot n^{2n} / e^n} = \sqrt{2} \cdot \left(\frac{2}{e}\right)^n.$$

Since $\frac{2}{e} \approx 0.736 < 1$, we have $R_n \to 0$ as $n \to \infty$.

---

## Part II: Unlabeled Trees (Generating Function Proof)

### Generating Functions

Let $T(x) = \sum_{n \geq 1} t_n^{(r)} x^n$ be the generating function for **rooted unlabeled trees**, satisfying:

$$T(x) = x \exp\!\left(\sum_{k \geq 1} \frac{T(x^k)}{k}\right).$$

Let $P(x) = \sum_{n \geq 1} p_n^{(r)} x^{2n}$ be the generating function for **rooted unlabeled trees with a perfect matching** (rooted at a vertex matched to one of its children).

**Structural decomposition.** A rooted tree with a perfect matching has:
- A root $r$, matched to exactly one "special" child $c$.
- The special child $c$ has a multiset of children, each being a rooted tree with a perfect matching.
- The root's other children form a multiset of rooted trees with perfect matchings.

Using the multiset operator $\mathcal{M}(A) = \exp\!\left(\sum_{k \geq 1} \frac{A(x^k)}{k}\right)$:

$$P(x) = x^2 \cdot \mathcal{M}(P)^2 = x^2 \exp\!\left(2\sum_{k \geq 1} \frac{P(x^k)}{k}\right).$$

### Comparison: $P(x) < T(x)$ for $x \in (0, \rho_T)$

We prove by induction (on coefficients) that $P(x) < T(x)$ for all $x \in (0, \rho_T)$, where $\rho_T$ is the radius of convergence of $T$.

**Base case:** $T(x) = x + \cdots$ and $P(x) = x^2 + \cdots$, so $P(x) < T(x)$ for small $x > 0$.

**Inductive step:** Suppose $P(y) < T(y)$ for all $y \in (0, x]$ with $x < \rho_T$. Then $P(x^k) < T(x^k)$ for all $k \geq 1$ (since $x^k \leq x$), so:

$$\sum_{k \geq 1} \frac{P(x^k)}{k} < \sum_{k \geq 1} \frac{T(x^k)}{k}.$$

Therefore:

$$P(x) = x^2 \exp\!\left(2\sum_{k \geq 1} \frac{P(x^k)}{k}\right) < x^2 \exp\!\left(2\sum_{k \geq 1} \frac{T(x^k)}{k}\right) = T(x)^2.$$

Since $T(x) < 1$ for $x \in (0, \rho_T)$ (as $T(\rho_T) = 1$ and $T$ is increasing), we get $T(x)^2 < T(x)$, hence $P(x) < T(x)$. $\checkmark$

### $P(x)$ Is Analytic at $x = \rho_T$

Rewrite the functional equation as:

$$P \, e^{-2P} = x^2 \, e^{g(x)}, \quad \text{where } g(x) = 2\sum_{k \geq 2} \frac{P(x^k)}{k}.$$

The function $g(x)$ is analytic near $x = \rho_T$ (since it depends on $P(x^k)$ for $k \geq 2$, and $\rho_T^k \leq \rho_T^2 < \rho_T$ for $k \geq 2$, where $P$ is analytic).

The function $h(P) = P \, e^{-2P}$ has a unique maximum at $P = \frac{1}{2}$, where $h\!\left(\frac{1}{2}\right) = \frac{1}{2e}$.

**$P(x)$ has a singularity at $x = \rho_P$ only if** $\rho_P^2 \, e^{g(\rho_P)} = \frac{1}{2e}$.

At $x = \rho_T$, the value $\rho_T^2 \, e^{g(\rho_T)}$ determines whether $P$ is singular:

$$\rho_T^2 \, e^{g(\rho_T)} < \frac{1}{2e} \iff P \text{ is analytic at } \rho_T \iff \rho_P > \rho_T.$$

We verify this inequality. Since $P(x) < T(x)$ for $x \in (0, \rho_T)$:

$$g(\rho_T) = 2\sum_{k \geq 2} \frac{P(\rho_T^k)}{k} < 2\sum_{k \geq 2} \frac{T(\rho_T^k)}{k} = 2f(\rho_T),$$

where $f(x) = \sum_{k \geq 2} \frac{T(x^k)}{k}$ is the "correction" term in the functional equation for $T$.

From the functional equation for $T$, the singularity condition gives $T(\rho_T) = 1$ and $\rho_T = e^{-(1 + f(\rho_T))}$, so $\rho_T^2 = e^{-2(1 + f(\rho_T))}$.

We need:

$$\rho_T^2 \, e^{g(\rho_T)} < \frac{1}{2e} \iff e^{-2(1 + f(\rho_T)) + g(\rho_T)} < \frac{1}{2e} \iff g(\rho_T) - 2f(\rho_T) < 1 - \ln 2.$$

Since $g(\rho_T) < 2f(\rho_T)$, we have $g(\rho_T) - 2f(\rho_T) < 0 < 1 - \ln 2$ (as $\ln 2 \approx 0.693 < 1$). $\checkmark$

Therefore $P(x)$ is analytic at $x = \rho_T$, which means $\rho_P > \rho_T$.

### Exponential Growth Rate Comparison

The number of rooted unlabeled trees of order $n$ grows as $\sim C_T \, \alpha_T^n \, n^{-5/2}$ where $\alpha_T = 1/\rho_T \approx 2.9558$ (Otter's constant).

The number of rooted unlabeled trees with a perfect matching of order $2n$ grows as $\sim C_P \, \alpha_P^{2n} \, (2n)^{-5/2}$ where $\alpha_P = 1/\rho_P$.

Since $\rho_P > \rho_T$, we have $\alpha_P < \alpha_T$.

By Otter's dissymmetry theorem, unrooted trees have the same exponential growth rate as rooted trees, so the number of unrooted trees of order $2n$ with a perfect matching grows as $\alpha_P^{2n}$, while the total grows as $\alpha_T^{2n}$.

The ratio:

$$\frac{\#\{\text{unlabeled trees of order } 2n \text{ with PM}\}}{\#\{\text{unlabeled trees of order } 2n\}} \sim \frac{C_P}{C_T} \cdot \left(\frac{\alpha_P}{\alpha_T}\right)^{2n} \to 0$$

since $\alpha_P / \alpha_T < 1$. $\blacksquare$

---

## Conclusion

In both the labeled and unlabeled cases, the ratio of the number of trees of order $2n$ with a perfect matching to the total number of trees of order $2n$ converges to zero as $n \to \infty$.

$$\boxed{\text{Yes, the ratio converges to zero.}}$$
