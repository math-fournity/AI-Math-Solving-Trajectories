# Can exotic $\mathbb{R}^4$ admit a metric such that its Riemann tensor is zero everywhere?

**Answer: $\boxed{\text{Yes}}$**

---

## Proof

We interpret the question as asking whether *there exists* an exotic $\mathbb{R}^4$ (a smooth 4-manifold homeomorphic but not diffeomorphic to standard $\mathbb{R}^4$) that admits a Riemannian metric $g$ with $\mathrm{Rm}(g) \equiv 0$. We show the answer is **yes** by exhibiting an explicit construction using *small exotic $\mathbb{R}^4$'s*.

### 1. The complete case is impossible (preliminary observation)

Let $M$ be an exotic $\mathbb{R}^4$. Since $M$ is homeomorphic to $\mathbb{R}^4$, it is simply connected. Suppose $M$ admitted a **complete** flat Riemannian metric $g$. By the Killing–Hopf theorem (the flat case of the Cartan–Hadamard / space-form classification), a complete, simply connected, flat Riemannian $n$-manifold is isometric to $(\mathbb{R}^n, g_0)$ with the standard Euclidean metric. An isometry is in particular a diffeomorphism, so $M$ would be diffeomorphic to standard $\mathbb{R}^4$ — contradicting the definition of exotic $\mathbb{R}^4$.

Hence **no exotic $\mathbb{R}^4$ admits a complete flat metric**. The key subtlety is that the question only requires the Riemann tensor to vanish; it does **not** require completeness.

### 2. Small exotic $\mathbb{R}^4$'s exist as open subsets of $\mathbb{R}^4$

A **small exotic $\mathbb{R}^4$** is a smooth 4-manifold $U$ such that:

- $U$ is an open subset of $\mathbb{R}^4$ (with the standard smooth structure inherited as an open submanifold),
- $U$ is homeomorphic to $\mathbb{R}^4$,
- $U$ is **not** diffeomorphic to $\mathbb{R}^4$.

The existence of such manifolds is a celebrated consequence of the interplay between Freedman's and Donaldson's work in the 1980s:

- **Freedman** (1982) proved that the topological $h$-cobordism theorem holds in dimension 4, providing the topological classification of simply connected closed 4-manifolds.
- **Donaldson** (1983) showed that a smooth 4-manifold admitting a definite intersection form must have a diagonalizable form, ruling out certain smooth structures that are topologically admissible.
- Combining these, **Freedman, Gompf, Taubes, and others** constructed open subsets $U \subset \mathbb{R}^4$ that are homeomorphic to $\mathbb{R}^4$ (by Freedman's topological tools) but cannot be diffeomorphic to $\mathbb{R}^4$ (by Donaldson-type smooth obstructions, e.g., the failure of the smooth $h$-cobordism theorem in dimension 4).

These $U$ are precisely the small exotic $\mathbb{R}^4$'s. Their existence is well-established in the literature (see e.g. Gompf, *An infinite set of exotic $\mathbb{R}^4$'s*, J. Differential Geom. 1983; Taubes, *Gauge theory on asymptotically periodic 4-manifolds*, J. Differential Geom. 1987).

### 3. The Euclidean metric restricted to $U$ is flat

Let $U \subset \mathbb{R}^4$ be a small exotic $\mathbb{R}^4$ as above, and let $g_0$ denote the standard Euclidean metric on $\mathbb{R}^4$. Since $U$ is an open subset, the tangent bundle $TU$ is the restriction $T\mathbb{R}^4|_U$, and the restriction

$$g := g_0\big|_U$$

is a well-defined Riemannian metric on $U$.

The Riemann curvature tensor is a **local** tensor: it is computed pointwise from the metric and its derivatives in any local coordinate chart. Since $g = g_0|_U$ agrees with $g_0$ in the standard coordinates of $\mathbb{R}^4$ (which are also coordinates on $U$ as an open submanifold), and since $\mathrm{Rm}(g_0) \equiv 0$ on $\mathbb{R}^4$, we have

$$\mathrm{Rm}(g) = \mathrm{Rm}(g_0)\big|_U \equiv 0.$$

Equivalently, restricting a flat metric to an open subset does not change the curvature tensor — it remains identically zero.

### 4. Conclusion

We have produced a smooth 4-manifold $U$ that is:

- **homeomorphic to $\mathbb{R}^4$** but **not diffeomorphic to $\mathbb{R}^4$** (hence an exotic $\mathbb{R}^4$), and
- equipped with a Riemannian metric $g = g_0|_U$ whose Riemann tensor vanishes everywhere.

Therefore, an exotic $\mathbb{R}^4$ **can** admit a metric with zero Riemann tensor.

$$\boxed{\text{Yes}}$$

### 5. Remarks

- The metric $g = g_0|_U$ is **incomplete** (in general, $U$ is a proper open subset of $\mathbb{R}^4$, so geodesics can exit $U$ in finite time). This is necessarily the case: as shown in §1, a *complete* flat metric on an exotic $\mathbb{R}^4$ would force a diffeomorphism to standard $\mathbb{R}^4$, a contradiction.
- The argument relies crucially on the existence of **small** exotic $\mathbb{R}^4$'s — those that embed as open subsets of standard $\mathbb{R}^4$. **Large** exotic $\mathbb{R}^4$'s (those that cannot embed in $\mathbb{R}^4$) are not addressed by this construction; whether every exotic $\mathbb{R}^4$ admits a flat (necessarily incomplete) metric is a more delicate question. The question as stated only asks whether *some* exotic $\mathbb{R}^4$ admits such a metric, and the small exotic $\mathbb{R}^4$ construction gives an affirmative answer.

### PROOF COMPLETE
