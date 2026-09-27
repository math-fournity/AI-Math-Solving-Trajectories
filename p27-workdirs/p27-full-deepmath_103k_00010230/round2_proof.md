# Solution

## Answer

Such a linear hypergraph exists **if and only if $\alpha$ is finite** (i.e., $\alpha \in \omega \setminus \{0,1,2\}$, meaning $\alpha \geq 3$ is a finite ordinal). For $\alpha = \omega$, no such hypergraph exists.

$$\boxed{\text{Yes for finite } \alpha \geq 3;\ \text{No for } \alpha = \omega.}$$

---

## Proof

### Part 1: Finite $\alpha \geq 3$ — Yes

**Claim.** For every finite $\alpha \geq 3$, there exists a linear $\alpha$-uniform hypergraph $H = (\omega, E)$ with $\chi(H) = \aleph_0$.

**Construction.** We use the following classical fact:

> **Fact (Erdős–Hajnal, 1966).** For every finite $n \geq 2$, every $k \geq 1$, and every $g \geq 1$, there exists a finite $n$-uniform hypergraph with girth $> g$ and chromatic number $> k$.

*Sketch of the fact.* Consider the random $n$-uniform hypergraph on $N$ vertices where each $n$-element subset is included as an edge independently with probability $p = N^{-n+1-\varepsilon}$ for small $\varepsilon > 0$. The expected number of edges is $\binom{N}{n}p \sim N^{1+\varepsilon}/n!$. The expected number of pairs of edges sharing $\geq 2$ vertices is $O(N^{2n-2}p^2) = O(N^{-\varepsilon})$, which is $< 1$ for large $N$. Thus with positive probability the hypergraph is linear (girth $> 2$) and has $\Omega(N^{1+\varepsilon})$ edges. Meanwhile, the expected number of independent sets of size $m$ is $\binom{N}{m}(1-p)^{\binom{m}{n}}$, which is $< 1$ for $m = N^{1-\delta}$ (with appropriate $\delta > 0$ depending on $\varepsilon, n$). Hence the independence number is $o(N)$, giving $\chi = \Omega(N^{\delta}) \to \infty$ as $N \to \infty$. $\square$

A hypergraph with girth $> 2$ is linear: if two distinct edges share two vertices $a, b$, then $a, e_1, b, e_2, a$ is a cycle of length 2, contradicting girth $> 2$.

Now, for each $k \in \omega$, apply the fact with $n = \alpha$, $g = 2$, and chromatic number $> k$ to obtain a finite $\alpha$-uniform linear hypergraph $H_k = (V_k, E_k)$ with $\chi(H_k) > k$.

Since each $H_k$ is finite, we can place the vertex sets $V_0, V_1, V_2, \ldots$ on pairwise disjoint subsets of $\omega$ (using the fact that a countable union of finite sets can be embedded in $\omega$). Define:

$$V = \bigcup_{k \in \omega} V_k \subseteq \omega, \qquad E = \bigcup_{k \in \omega} E_k.$$

Since the $V_k$ are pairwise disjoint, $E$ is $\alpha$-uniform and the hypergraph $H = (V, E)$ is linear (edges from different $H_k$ are on disjoint vertex sets, hence disjoint; edges within the same $H_k$ satisfy linearity by construction). Extend $H$ to all of $\omega$ by leaving vertices in $\omega \setminus V$ isolated (not in any edge).

**Chromatic number.** Any coloring of $H$ restricts to a coloring of each $H_k$, so $\chi(H) \geq \chi(H_k) > k$ for every $k$, giving $\chi(H) \geq \aleph_0$. Since $|V| \leq \aleph_0$, we have $\chi(H) \leq \aleph_0$. Therefore $\chi(H) = \aleph_0$. $\blacksquare$

---

### Part 2: $\alpha = \omega$ — No

**Claim.** For every linear hypergraph $H = (\omega, E)$ with $E \subseteq [\omega]^\omega$, we have $\chi(H) \leq 2 < \aleph_0$.

The proof has two steps.

#### Step 1: $|E| \leq \aleph_0$ (any linear family of countably infinite subsets of $\omega$ is countable).

For each edge $e \in E$, consider the set of unordered pairs:
$$\binom{e}{2} = \bigl\{\{a, b\} : a, b \in e,\ a \neq b\bigr\} \subseteq \binom{\omega}{2}.$$

Since $|e| = \aleph_0$, we have $\left|\binom{e}{2}\right| = \aleph_0$.

**Linearity implies disjointness of pair sets.** If $e \neq f$ are edges and $\{a, b\} \in \binom{e}{2} \cap \binom{f}{2}$, then $a, b \in e \cap f$ with $a \neq b$, so $|e \cap f| \geq 2$, contradicting linearity. Hence:
$$\binom{e}{2} \cap \binom{f}{2} = \emptyset \quad \text{for all distinct } e, f \in E.$$

The total set of pairs satisfies $\left|\binom{\omega}{2}\right| = \aleph_0$. Since $\left\{\binom{e}{2} : e \in E\right\}$ is a family of pairwise disjoint subsets of $\binom{\omega}{2}$, each of cardinality $\aleph_0$, we have:
$$|E| \cdot \aleph_0 \leq \aleph_0,$$
which forces $|E| \leq \aleph_0$.

#### Step 2: A countable family of infinite sets can be 2-split (diagonalization).

Since $|E| \leq \aleph_0$, enumerate $E = \{e_0, e_1, e_2, \ldots\}$ (if $E$ is finite, the argument is even simpler). We construct a 2-coloring $c: \omega \to \{0, 1\}$ such that no edge is monochromatic.

**Construction.** Initialize all vertices as uncolored. At step $n$ (for $n = 0, 1, 2, \ldots$):
- The edge $e_n$ is infinite, and at most $2n$ vertices have been colored in steps $0, \ldots, n-1$.
- So $e_n$ contains infinitely many uncolored vertices. Pick two distinct uncolored vertices $u_n, v_n \in e_n$.
- Set $c(u_n) = 0$ and $c(v_n) = 1$.

After all steps, color any remaining uncolored vertices as $c(w) = 0$.

**Verification.** For each $n$, the edge $e_n$ contains $u_n$ (color 0) and $v_n$ (color 1), so $e_n$ is not monochromatic. Hence no edge is monochromatic, and $\chi(H) \leq 2$.

Since $2 < \aleph_0$, we conclude $\chi(H) < \aleph_0$ for every linear hypergraph $H = (\omega, E)$ with $E \subseteq [\omega]^\omega$. $\blacksquare$

---

### Conclusion

Combining both parts:

| $\alpha$ | Exists? | Reason |
|---|---|---|
| Finite $\alpha \geq 3$ | **Yes** | Erdős–Hajnal: finite linear $\alpha$-uniform hypergraphs with arbitrarily large $\chi$; disjoint union on $\omega$ gives $\chi = \aleph_0$ |
| $\alpha = \omega$ | **No** | Linear family of infinite subsets of $\omega$ is countable (pair-counting); countable family of infinite sets is 2-splitable (diagonalization); so $\chi \leq 2$ |

The answer is: **such a hypergraph exists if and only if $\alpha$ is finite** (i.e., $\alpha \in \omega \setminus \{0,1,2\}$).
