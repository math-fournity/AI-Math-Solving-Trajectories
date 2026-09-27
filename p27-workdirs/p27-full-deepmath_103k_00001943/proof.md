# The Unit Ball of $D[0,1]^*$ is Weak* Separable

## Answer

$$\boxed{\text{Yes}}$$

The unit ball of $D[0,1]^*$ is separable in the weak* topology.

## Proof

Let $D[0,1]$ denote the Skorokhod space of càdlàg functions on $[0,1]$, equipped with the Skorokhod $J_1$ topology. Let $D[0,1]^*$ denote its continuous dual (the space of linear functionals continuous with respect to the Skorokhod topology), and let

$$B^* = \{f \in D[0,1]^* : |f(x)| \leq 1 \text{ for all } x \in D[0,1] \text{ with } \|x\|_\infty \leq 1\}$$

be the unit ball, where $\|\cdot\|_\infty$ is the supremum norm. We show that $B^*$ is separable in the weak* topology $\sigma(D[0,1]^*, D[0,1])$.

### Step 1: $D[0,1]$ is separable

This is a classical result. The set of piecewise constant càdlàg functions with rational jump locations and rational jump sizes is countable and dense in $D[0,1]$ under the Skorokhod $J_1$ metric (see Billingsley, *Convergence of Probability Measures*, or Ethier & Kurtz, *Markov Processes*). Hence $D[0,1]$ is a separable, completely metrizable topological vector space.

### Step 2: The Skorokhod topology agrees with the uniform topology near 0

The Skorokhod $J_1$ metric is:

$$d_S(x, y) = \inf_{\lambda \in \Lambda} \max\bigl(\|\lambda - \mathrm{id}\|_\infty,\; \|x - y \circ \lambda\|_\infty\bigr),$$

where $\Lambda$ is the set of strictly increasing continuous bijections $\lambda: [0,1] \to [0,1]$ with $\lambda(0)=0$, $\lambda(1)=1$.

Setting $y = 0$:

$$d_S(x, 0) = \inf_{\lambda \in \Lambda} \max\bigl(\|\lambda - \mathrm{id}\|_\infty,\; \|x\|_\infty\bigr) = \|x\|_\infty,$$

since $\|x\|_\infty$ is independent of $\lambda$ and $\inf_{\lambda} \|\lambda - \mathrm{id}\|_\infty = 0$ (take $\lambda = \mathrm{id}$).

Therefore the open balls around $0$ in the Skorokhod metric coincide with the open balls around $0$ in the supremum norm:

$$\{x \in D[0,1] : d_S(x, 0) < \varepsilon\} = \{x \in D[0,1] : \|x\|_\infty < \varepsilon\}.$$

In particular, the supremum-norm unit ball $U = \{x : \|x\|_\infty \leq 1\}$ is a closed neighborhood of $0$ in the Skorokhod topology.

### Step 3: $B^*$ is equicontinuous

A subset $H \subseteq D[0,1]^*$ is **equicontinuous** (with respect to the Skorokhod topology) if for every $\varepsilon > 0$ there exists a Skorokhod-neighborhood $V$ of $0$ such that $|f(x)| < \varepsilon$ for all $f \in H$ and $x \in V$.

By Step 2, $V_\varepsilon = \{x : \|x\|_\infty < \varepsilon\}$ is a Skorokhod-neighborhood of $0$. For any $f \in B^*$ and $x \in V_\varepsilon$, we have $|f(x)| \leq \|f\|_{\mathrm{op}} \cdot \|x\|_\infty \leq 1 \cdot \varepsilon = \varepsilon$. Hence $B^*$ is equicontinuous.

### Step 4: $B^*$ is weak* compact

The unit ball $B^*$ is the polar of the neighborhood $U$:

$$B^* = U^\circ = \{f \in D[0,1]^* : |f(x)| \leq 1 \text{ for all } x \in U\}.$$

Since $U$ is a neighborhood of $0$ in the locally convex space $(D[0,1], \tau_S)$, the Banach–Alaoglu theorem (in its locally convex form) asserts that $U^\circ$ is compact in the weak* topology $\sigma(D[0,1]^*, D[0,1])$.

### Step 5: $B^*$ is weak* metrizable

Since $D[0,1]$ is separable (Step 1), let $\{x_n\}_{n=1}^\infty$ be a countable dense subset. Define:

$$\rho(f, g) = \sum_{n=1}^\infty 2^{-n} \min\bigl(1, |f(x_n) - g(x_n)|\bigr), \qquad f, g \in B^*.$$

This is a pseudometric on $B^*$. We claim it is a metric that induces the weak* topology on $B^*$.

- **Separation**: If $\rho(f, g) = 0$, then $f(x_n) = g(x_n)$ for all $n$. Since $\{x_n\}$ is dense in $D[0,1]$ and $f, g$ are continuous, $f = g$ on all of $D[0,1]$.

- **Equivalence of topologies**: The weak* topology on $B^*$ is the topology of pointwise convergence on $D[0,1]$, i.e., the coarsest topology making each map $f \mapsto f(x)$ continuous. The metric $\rho$ makes each $f \mapsto f(x_n)$ continuous, so the $\rho$-topology is finer than the weak* topology restricted to the dense set. Conversely, by **equicontinuity** (Step 3), pointwise convergence on the dense set $\{x_n\}$ implies pointwise convergence on all of $D[0,1]$: if $f_k(x_n) \to f(x_n)$ for all $n$, then for any $x \in D[0,1]$ and $\varepsilon > 0$, pick $x_n$ with $d_S(x_n, x) < \delta$ (where $\delta$ comes from equicontinuity), and $|f_k(x) - f(x)| \leq |f_k(x) - f_k(x_n)| + |f_k(x_n) - f(x_n)| + |f(x_n) - f(x)| \to 0$. Hence the $\rho$-topology coincides with the weak* topology on $B^*$.

Therefore $(B^*, \rho)$ is a compact metrizable space.

### Step 6: Compact metrizable implies separable

Every compact metrizable space is separable: for each $n$, cover $B^*$ with finitely many balls of radius $1/n$ (possible by compactness); the union of the centers over all $n$ is a countable dense set.

### Conclusion

The unit ball $B^*$ of $D[0,1]^*$ is weak* compact (Banach–Alaoglu), weak* metrizable (by separability of $D[0,1]$ and equicontinuity of $B^*$), and therefore weak* separable.

$$\boxed{\text{Yes, the unit ball of } D[0,1]^* \text{ is separable in the weak* topology.}}$$

## Key Ingredients

| Step | Fact Used |
|------|-----------|
| 1 | $D[0,1]$ with Skorokhod $J_1$ topology is separable (classical) |
| 2 | Skorokhod distance to $0$ equals sup-norm: $d_S(x,0) = \|x\|_\infty$ |
| 3 | Equicontinuity of $B^*$ follows from Step 2 |
| 4 | Banach–Alaoglu (locally convex version): polar of a neighborhood is weak* compact |
| 5 | Separable domain + equicontinuity $\Rightarrow$ weak* metrizability of compact sets |
| 6 | Compact + metrizable $\Rightarrow$ separable |
