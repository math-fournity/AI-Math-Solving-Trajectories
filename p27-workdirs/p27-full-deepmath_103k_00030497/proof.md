# Proof: A countable set can be given a topology homeomorphic to $\mathbb{Q}^2$

## Answer

$$\boxed{\text{Yes}}$$

It is possible to define a topology on a countable set that is homeomorphic to $\mathbb{Q}^2$.

---

## Justification

### Step 1. The trivial observation

$\mathbb{Q}^2 = \mathbb{Q} \times \mathbb{Q}$ is itself countable (a product of two countable sets is countable), and equipped with the subspace topology inherited from $\mathbb{R}^2$, it is homeomorphic to itself. So the answer is trivially "yes" if we take the countable set to be $\mathbb{Q}^2$ itself.

The interesting content of the question is whether a *more familiar* countable set — in particular $\mathbb{Q}$ with its usual topology — can be homeomorphic to $\mathbb{Q}^2$. The answer is still **yes**, by a classical theorem of Sierpiński.

### Step 2. Sierpiński's characterization theorem (1920)

> **Theorem (Sierpiński).** *Every countable, metrizable topological space with no isolated points is homeomorphic to $\mathbb{Q}$ (with its usual topology).*

Equivalently: up to homeomorphism, $\mathbb{Q}$ is the **unique** countable metrizable space without isolated points.

### Step 3. $\mathbb{Q}^2$ satisfies the three hypotheses

We verify that $\mathbb{Q}^2$ (with the subspace topology from $\mathbb{R}^2$) satisfies all three conditions of Sierpiński's theorem.

**(a) Countable.** $\mathbb{Q}$ is countable, and a finite Cartesian product of countable sets is countable, so $\mathbb{Q}^2 = \mathbb{Q} \times \mathbb{Q}$ is countable.

**(b) Metrizable.** $\mathbb{R}^2$ with the Euclidean metric is a metric space, and any subspace of a metrizable space is metrizable (by restricting the metric). Hence $\mathbb{Q}^2$ is metrizable.

**(c) No isolated points.** Let $(p, q) \in \mathbb{Q}^2$ and let $\varepsilon > 0$. Choose a rational $\delta$ with $0 < \delta < \varepsilon$ (possible since $\mathbb{Q}$ is dense in $\mathbb{R}$). Then $(p + \delta, q) \in \mathbb{Q}^2$, and
$$d\bigl((p,q),\, (p+\delta, q)\bigr) = |\delta| < \varepsilon,$$
so $(p+\delta, q) \in B\bigl((p,q), \varepsilon\bigr) \cap \mathbb{Q}^2$ and $(p+\delta, q) \neq (p,q)$. Thus no point of $\mathbb{Q}^2$ is isolated.

### Step 4. Conclusion via Sierpiński's theorem

By Steps 2 and 3, $\mathbb{Q}^2$ is homeomorphic to $\mathbb{Q}$:
$$\mathbb{Q}^2 \cong \mathbb{Q}.$$

Since $\mathbb{Q}$ is a countable set equipped with a topology (its usual topology) that makes it homeomorphic to $\mathbb{Q}^2$, the answer to the question is **yes**.

---

## Sketch of Sierpiński's theorem (for completeness)

The theorem is proved by a **back-and-forth (zig-zag) argument**. Let $X$ be any countable metrizable space with no isolated points, and let $Y = \mathbb{Q}$. Enumerate $X = \{x_1, x_2, \dots\}$ and $Y = \{q_1, q_2, \dots\}$.

**Key lemma.** *In a countable metrizable space with no isolated points, every non-empty open set is infinite.*

*Proof of lemma.* Let $U$ be a non-empty open set and pick $x \in U$. Since $x$ is not isolated, $U$ contains some $y \neq x$. Since the space is metrizable (hence $T_1$), we can separate $x$ and $y$ by an open neighborhood of $x$ inside $U$ that excludes $y$; this neighborhood contains a third point (again because no point is isolated). Iterating produces infinitely many distinct points in $U$. $\square$

**Construction.** We build a partial bijection $f : A \to B$ (with $A \subseteq X$, $B \subseteq Y$) in stages $n = 1, 2, 3, \dots$:

- **Odd stage $n = 2k-1$:** Ensure $x_k$ enters the domain. If $x_k \notin A$ already, find the smallest "cell" (a basic open set in $X$ determined by the current partial map) containing $x_k$, and pick a point $q \in Y$ in the corresponding cell of $Y$ that has not yet been used. Set $f(x_k) = q$.
- **Even stage $n = 2k$:** Ensure $q_k$ enters the range, symmetrically.

At each stage, we refine the partition into smaller cells (using radii $\leq 2^{-n}$) so that:

1. **Cell preservation invariant:** for every previously assigned point $a \in A$, the new point lies in the same cell of $X$ as $a$ if and only if its image lies in the corresponding cell of $Y$. This guarantees $f$ preserves the "closeness" structure.

2. **Nested radii $\to 0$:** the cell containing each point $a$ shrinks (diameter $\leq 2^{-n}$) at each subsequent stage. This ensures **continuity**: for any $\varepsilon > 0$, choose $n$ with $2^{-n} < \varepsilon$; then for all $x$ sufficiently close to $a$ (inside the stage-$n$ cell), $d_Y(f(x), f(a)) < 2^{-n} < \varepsilon$.

3. **Complement stays non-empty:** when a new point falls outside all existing cells (the "complement case"), the complement is an open set (complement of a finite union of closed cells). By the key lemma, this open set is infinite, so we can place a new small cell inside it without exhausting it — choosing the new radius $< \frac{1}{4}\operatorname{diam}(\text{complement})$ keeps the complement non-empty.

The back-and-forth ensures $\bigcup A = X$ and $\bigcup B = Y$, so $f$ is a bijection. The cell-preservation invariant plus nested radii give that both $f$ and $f^{-1}$ are continuous. Hence $f$ is a homeomorphism $X \cong \mathbb{Q}$. $\square$

---

## Final answer

$$\boxed{\text{Yes}}$$

$\mathbb{Q}^2$ is countable, metrizable, and has no isolated points, so by Sierpiński's theorem it is homeomorphic to $\mathbb{Q}$. Therefore the countable set $\mathbb{Q}$, equipped with its usual topology, is homeomorphic to $\mathbb{Q}^2$.

### PROOF COMPLETE
