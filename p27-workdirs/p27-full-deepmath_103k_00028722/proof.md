# Proof

**Problem.** Find the minimum number of integer lattice points contained in a centrally symmetric convex subset of $\mathbb{R}^N$ with a volume that is not an integer multiple of $2^N$.

**Answer:** $\boxed{3}$.

We interpret "centrally symmetric convex subset" as a convex body symmetric about the origin (the standard convention in the geometry of numbers). The condition "volume is not an integer multiple of $2^N$" places us in the Minkowski regime: since $\operatorname{vol}(K) = k \cdot 2^N$ is excluded for every non-negative integer $k$, and the problem is non-trivial precisely when $\operatorname{vol}(K) > 2^N$ (volumes in $(0, 2^N)$ trivially contain only the origin), we seek the minimum of $|K \cap \mathbb{Z}^N|$ over all centrally symmetric convex bodies $K \subset \mathbb{R}^N$ (symmetric about the origin) with $\operatorname{vol}(K) > 2^N$ and $\operatorname{vol}(K)/2^N \notin \mathbb{Z}$.

## Lower Bound: $|K \cap \mathbb{Z}^N| \geq 3$

Let $K \subset \mathbb{R}^N$ be a closed convex body, centrally symmetric about the origin (i.e., $K = -K$), with $\operatorname{vol}(K) > 2^N$.

**Step 1: The origin is a lattice point in $K$.**

Since $K = -K$ and $K$ is convex, for any $x \in K$, we have $-x \in K$ and $\frac{x + (-x)}{2} = 0 \in K$. Thus $0 \in K \cap \mathbb{Z}^N$.

**Step 2: Minkowski's theorem gives a nonzero lattice point.**

Consider the set $K/2 = \{x/2 : x \in K\}$. This is a convex body symmetric about the origin with $\operatorname{vol}(K/2) = \operatorname{vol}(K)/2^N > 1$.

Project $K/2$ onto the torus $\mathbb{R}^N / \mathbb{Z}^N$ (the unit fundamental domain, volume $1$). Since $\operatorname{vol}(K/2) > 1 = \operatorname{vol}(\mathbb{R}^N / \mathbb{Z}^N)$, by the pigeonhole principle (Blichfeldt's theorem), there exist two distinct points $u, v \in K/2$ such that $u - v \in \mathbb{Z}^N \setminus \{0\}$.

Since $u \in K/2$, we have $2u \in K$. Since $v \in K/2$ and $K/2$ is symmetric about the origin, $-v \in K/2$, so $-2v \in K$. By convexity of $K$:

$$\frac{2u + (-2v)}{2} = u - v \in K.$$

Since $u - v \in \mathbb{Z}^N \setminus \{0\}$, we have found a nonzero lattice point $w := u - v \in K \cap \mathbb{Z}^N$.

**Step 3: Symmetry gives the third lattice point.**

Since $K = -K$ and $w \in K$, we have $-w \in K$. Since $w \neq 0$, we have $-w \neq w$, so $-w$ is a distinct lattice point. Thus:

$$\{0, w, -w\} \subseteq K \cap \mathbb{Z}^N,$$

and these three points are distinct. Therefore $|K \cap \mathbb{Z}^N| \geq 3$.

## Upper Bound: Construction Achieving Exactly 3

We construct, for every $N \geq 1$, a centrally symmetric convex body $K$ with $\operatorname{vol}(K) > 2^N$, $\operatorname{vol}(K)/2^N \notin \mathbb{Z}$, and $|K \cap \mathbb{Z}^N| = 3$.

**Construction.** Let $\epsilon \in (0, 1)$ and $\delta \in (0, 1)$ be parameters to be chosen. Define:

$$K = [-1-\epsilon,\; 1+\epsilon] \times [-\delta,\; \delta]^{N-1}.$$

This is a closed rectangular box, hence convex and centrally symmetric about the origin.

**Volume.** The volume is:

$$\operatorname{vol}(K) = 2(1+\epsilon) \cdot (2\delta)^{N-1} = 2^N (1+\epsilon)\,\delta^{N-1}.$$

We need $(1+\epsilon)\,\delta^{N-1} > 1$ (so that $\operatorname{vol}(K) > 2^N$) and $(1+\epsilon)\,\delta^{N-1} \notin \mathbb{Z}$ (so that $\operatorname{vol}(K)$ is not a multiple of $2^N$).

**Choosing parameters.** Set $\epsilon = \frac{1}{2}$. We need $\frac{3}{2}\,\delta^{N-1} \in (1, 2) \setminus \mathbb{Z}$, i.e., $\delta^{N-1} \in \bigl(\frac{2}{3},\, \frac{4}{3}\bigr)$ with $\frac{3}{2}\delta^{N-1} \notin \mathbb{Z}$.

- For $N = 1$: the condition is simply $\frac{3}{2} \in (1,2) \setminus \mathbb{Z}$, which holds. ✓
- For $N \geq 2$: choose any $\delta \in \bigl(\max\{(\frac{2}{3})^{1/(N-1)},\, 0\},\; 1\bigr)$ such that $\frac{3}{2}\delta^{N-1} \notin \mathbb{Z}$. Such $\delta$ exists because the interval $\bigl((\frac{2}{3})^{1/(N-1)},\, 1\bigr)$ is non-empty (since $(\frac{2}{3})^{1/(N-1)} < 1$) and the set of $\delta$ with $\frac{3}{2}\delta^{N-1} \in \mathbb{Z}$ is finite (at most one value in the interval for each integer). ✓

**Lattice point count.** A point $(x_1, x_2, \ldots, x_N) \in \mathbb{Z}^N$ belongs to $K$ if and only if:

- $|x_1| \leq 1 + \epsilon = \frac{3}{2}$, so $x_1 \in \{-1, 0, 1\}$ (since $x_1$ is an integer and $\frac{3}{2} < 2$).
- $|x_i| \leq \delta < 1$ for $i = 2, \ldots, N$, so $x_i = 0$ (since $x_i$ is an integer).

Therefore:

$$K \cap \mathbb{Z}^N = \{(-1, 0, \ldots, 0),\; (0, 0, \ldots, 0),\; (1, 0, \ldots, 0)\},$$

which has exactly $3$ elements.

## Conclusion

We have shown:
- **Lower bound:** Every centrally symmetric convex body $K$ (about the origin) with $\operatorname{vol}(K) > 2^N$ contains at least $3$ lattice points (by Minkowski's theorem and symmetry).
- **Upper bound:** For every $N \geq 1$, there exists such a body with $\operatorname{vol}(K)/2^N \notin \mathbb{Z}$ containing exactly $3$ lattice points.

Therefore, the minimum number of integer lattice points is:

$$\boxed{3}.$$

### PROOF COMPLETE
