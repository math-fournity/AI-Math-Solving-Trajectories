# Does every 4-manifold homeomorphic to $S^4$ admit positive scalar curvature?

## Answer

$$\boxed{\text{This is an open problem.}}$$

The question asks whether every smooth 4-manifold $M$ that is homeomorphic to $S^4$ admits a Riemannian metric with positive scalar curvature (psc), regardless of which differentiable structure is placed on the underlying topological manifold. We show that this problem is equivalent to a major open question in 4-dimensional differential topology, and that current mathematical knowledge is insufficient to resolve it.

---

## 1. Reduction to homotopy 4-spheres

**Definition.** A *homotopy 4-sphere* is a closed, smooth, simply connected 4-manifold homotopy equivalent to $S^4$.

**Proposition 1.** The problem is equivalent to: *Does every homotopy 4-sphere admit a psc metric?*

*Proof.* If $M$ is homeomorphic to $S^4$, then $M$ is simply connected and has the homology of $S^4$ (since homeomorphisms preserve homology). By Whitehead's theorem, $M$ is homotopy equivalent to $S^4$, so $M$ is a homotopy 4-sphere.

Conversely, by Freedman's classification theorem (1982), every homotopy 4-sphere is homeomorphic to $S^4$: a closed, simply connected, topological 4-manifold is determined up to homeomorphism by its intersection form and Kirby–Siebenmann invariant, and for a homotopy 4-sphere both are trivial (the intersection form is the zero form on $H_2 = 0$, and the Kirby–Siebenmann invariant vanishes for a smoothable manifold).

Thus "smooth structures on the topological $S^4$" correspond exactly to "homotopy 4-spheres up to diffeomorphism." $\square$

---

## 2. The standard $S^4$ admits psc

The round metric on $S^4 \subset \mathbb{R}^5$ has constant sectional curvature $+1$, hence constant scalar curvature $R = n(n-1) = 12 > 0$. So if the smooth Poincaré conjecture in dimension 4 is true (i.e., every homotopy 4-sphere is diffeomorphic to $S^4$), the answer is trivially **YES**.

The smooth Poincaré conjecture in dimension 4 is itself a famous open problem. Thus the interesting case is when exotic 4-spheres exist.

---

## 3. All known obstructions to psc fail for homotopy 4-spheres

We verify that every standard obstruction to the existence of psc metrics is inapplicable.

### 3.1 Lichnerowicz obstruction ($\hat{A}$-genus)

**Theorem (Lichnerowicz, 1963).** If $M$ is a spin manifold admitting a psc metric, then $\hat{A}(M) = 0$.

For a homotopy 4-sphere: $M$ is spin (since $H^2(M; \mathbb{Z}/2) = 0$, so $w_2 = 0$). The $\hat{A}$-genus in dimension 4 satisfies $\hat{A}(M) = -\sigma(M)/8$, where $\sigma$ is the signature of the intersection form. Since $H_2(M) = 0$, the intersection form is trivial and $\sigma = 0$, so $\hat{A}(M) = 0$.

**Conclusion:** The Lichnerowicz obstruction gives no information.

### 3.2 Seiberg–Witten obstruction

**Theorem (Witten, 1994; Taubes).** If $M$ is a closed symplectic 4-manifold with $b_2^+ \geq 1$, or more generally if $M$ has non-vanishing Seiberg–Witten invariants with $b_2^+ \geq 1$, then $M$ admits no psc metric.

For a homotopy 4-sphere: $b_2 = 0$, so $b_2^+ = 0$. The Seiberg–Witten invariants are not defined (or are trivially zero) when $b_2^+ = 0$.

**Conclusion:** The Seiberg–Witten obstruction does not apply.

### 3.3 Schoen–Yau minimal surface descent

**Theorem (Schoen–Yau, 1979–2017).** If $M^n$ ($n \leq 7$) admits a psc metric, then $M$ does not admit a map of non-zero degree to any aspherical $n$-manifold. Equivalently, if $M$ maps non-trivially to an aspherical manifold, then $M$ does not admit psc.

For a homotopy 4-sphere: $M$ is simply connected with $H_2 = 0$, so $M$ cannot map non-trivially to any aspherical manifold (any such map would be null-homotopic on $\pi_1$ and zero on $H_2$).

**Conclusion:** The Schoen–Yau obstruction does not apply.

### 3.4 Gromov–Lawson enlargeability

**Theorem (Gromov–Lawson, 1983).** If $M$ is enlargeable (admits a sequence of covers with non-zero degree maps to $S^n$ of arbitrarily small contractivity), then $M$ admits no psc metric.

For a homotopy 4-sphere: $M$ is simply connected, so its universal cover is itself. A simply connected manifold is trivially non-enlargeable.

**Conclusion:** The enlargeability obstruction does not apply.

### 3.5 Summary

No known obstruction prevents a homotopy 4-sphere from admitting psc. This is consistent with the answer being YES, but does not prove it.

---

## 4. The Gromov–Lawson–Stolz theorem and its failure in dimension 4

### 4.1 The theorem in dimensions $\geq 5$

**Theorem (Gromov–Lawson, 1980; Stolz, 1992).** Let $M$ be a closed, simply connected, smooth $n$-manifold with $n \geq 5$. Then $M$ admits a psc metric if and only if either:
- $M$ is non-spin, or
- $M$ is spin and $\hat{A}(M) = 0$.

The proof uses the **Gromov–Lawson surgery theorem**: psc metrics are preserved under surgeries of codimension $\geq 3$. One builds $M$ from a sphere (or a connected sum of spheres) by a sequence of surgeries, using the fact that in dimensions $\geq 5$, the Whitney trick allows cancellation of middle-dimensional handle pairs, yielding a handle decomposition with only handles of codimension $\geq 3$.

### 4.2 Surgery codimensions in dimension 4

A $k$-handle attachment in an $n$-manifold corresponds to surgery on $S^{k-1}$, with codimension $n - (k-1) = n - k + 1$.

For $n = 4$:

| Handle index $k$ | Surgery on $S^{k-1}$ | Codimension $= 4 - k + 1$ | Covered by Gromov–Lawson? |
|---|---|---|---|
| 1 | $S^0$ | 4 | Yes |
| 2 | $S^1$ | 3 | Yes |
| 3 | $S^2$ | 2 | **No** |
| 4 | $S^3$ | 1 | No |

**Key point:** In dimension 4, 3-handles correspond to codimension-2 surgery, which is **not** covered by the Gromov–Lawson surgery theorem. (Note: 2-handles, corresponding to codimension-3 surgery, *are* covered—a correction to the Round 1 analysis which incorrectly computed the codimension as $n - k - 1$.)

### 4.3 Why the surgery approach fails

**Proposition 2.** If a homotopy 4-sphere $M$ admits a handle decomposition with no 3-handles (equivalently, by duality, no 1-handles), then $M$ admits a psc metric.

*Proof.* If $M$ has no 1-handles and no 3-handles, its handle decomposition consists of 0-, 2-, and 4-handles only. The relative chain complex gives $H_2(M) = \mathbb{Z}^k / \text{im}(\partial_3) = \mathbb{Z}^k$ (since there are no 3-handles, $\partial_3 = 0$). But $H_2(M) = 0$, so $k = 0$: there are no 2-handles. Thus $M = B^4 \cup B^4 = S^4$.

More generally, if $M$ has no 3-handles (but may have 1-handles), we can build $M$ from $B^4$ by attaching 1-handles (codim 4, psc preserved) and 2-handles (codim 3, psc preserved), then capping with a 4-handle. Each step preserves psc by the Gromov–Lawson surgery theorem. $\square$

**Proposition 3.** If every homotopy 4-sphere admitted a handle decomposition with no 1-handles, then the smooth Poincaré conjecture in dimension 4 would be true.

*Proof.* By duality (reversing the handle decomposition), no 1-handles is equivalent to no 3-handles. By the argument in Proposition 2, a handle decomposition with no 1-handles and no 3-handles forces $M \cong S^4$. But handle trading—replacing 1-handles with 2-handles—requires geometric linking conditions that in dimension 4 depend on the Whitney trick. The smooth Whitney trick fails in dimension 4 (as demonstrated by Donaldson's work). Therefore, handle trading cannot always eliminate all 1-handles. $\square$

Since the smooth Poincaré conjecture in dimension 4 is open, we cannot guarantee the elimination of 1-handles (or, by duality, 3-handles). The Gromov–Lawson surgery approach therefore cannot be completed for a potentially exotic 4-sphere.

---

## 5. Other approaches and why they fail

### 5.1 Yamabe invariant

The Yamabe invariant $Y(M) > 0$ if and only if $M$ admits a psc metric. For $S^4$, $Y(S^4) = 8\pi\sqrt{6}$ (the maximum in dimension 4, by Obata's theorem). For a general homotopy 4-sphere $M$, $Y(M)$ is a smooth invariant, and determining its sign is equivalent to the original question—this is circular.

### 5.2 Ricci flow

In dimension 3, Perelman used Ricci flow to prove the Poincaré conjecture. In dimension 4, the Ricci flow with surgery is far less developed. Even if the flow converges, there is no guarantee it converges to a psc metric. Recent work by Bamler on 4-dimensional Ricci flow provides partial results but does not yield an existence theorem for psc metrics on homotopy 4-spheres.

### 5.3 Twisted sphere decomposition

A *twisted 4-sphere* is $B^4 \cup_f B^4$ for some diffeomorphism $f \in \text{Diff}(S^3)$. By the Smale conjecture (proved by Hatcher), $\text{Diff}(S^3) \simeq O(4)$, and every diffeomorphism of $S^3$ extends to $B^4$. Thus every twisted 4-sphere is diffeomorphic to $S^4$. Consequently, if exotic 4-spheres exist, they cannot be decomposed into two smooth 4-balls, and this approach cannot reach them.

### 5.4 h-cobordism reformulation

Removing two points from $M$ yields an h-cobordism $W = M \setminus \{p, q\}$ between two copies of $S^3$. If $W$ were diffeomorphic to $S^3 \times [0,1]$, then $M \cong S^4$. The smooth h-cobordism theorem fails in dimension 4 (even for simply connected cobordisms), so this reformulation does not resolve the question.

### 5.5 Gluing psc metrics on handlebodies

One might attempt to put psc metrics on each piece of a handle decomposition and glue. However, gluing psc metrics along a hypersurface requires matching conditions on the mean curvature (e.g., the boundary must have positive mean curvature with respect to both pieces). For arbitrary handle decompositions of a potentially exotic 4-sphere, these conditions cannot be guaranteed simultaneously.

### 5.6 Recent developments (2020–2025)

Recent work has produced new **non-existence** results for psc:
- **Chodosh–Li (2020–2023):** Certain aspherical 4-manifolds (e.g., certain torus bundles) admit no psc metric, extending Schoen–Yau-type obstructions.
- **Gromov (2019–2020):** New obstructions via waist inequalities and macroscopic scalar curvature bounds.

These are obstruction results, not existence theorems. No new existence theorem for psc on 4-manifolds with $b_2 = 0$ has been established.

---

## 6. The precise state of the problem

The problem sits at the intersection of two open issues:

1. **Existence of exotic 4-spheres** (smooth Poincaré conjecture in dimension 4): Open. If no exotic 4-spheres exist, the answer is trivially **YES**.

2. **psc on exotic 4-spheres** (if they exist): Open. No obstruction is known (Section 3), and no existence theorem extends to dimension 4 (Section 4). The Gromov–Lawson–Stolz theorem, which gives a complete answer in dimensions $\geq 5$, relies on the Whitney trick and cannot be extended to dimension 4.

The relationship between these two issues is:
- If the smooth Poincaré conjecture is true → answer is **YES**.
- If exotic 4-spheres exist AND all admit psc → answer is **YES**.
- If exotic 4-spheres exist AND some do not admit psc → answer is **NO** (this would require a new obstruction, unknown at present).

No current mathematical result distinguishes among these three possibilities. The problem is **open**.

---

## 7. Conclusion

The question of whether every 4-manifold homeomorphic to $S^4$ admits a Riemannian metric with positive scalar curvature is an **open problem** in differential geometry and topology. It is equivalent to asking whether every homotopy 4-sphere admits psc. While no obstruction is known (all standard obstructions—Lichnerowicz, Seiberg–Witten, Schoen–Yau, enlargeability—fail to apply), no existence theorem is available either: the Gromov–Lawson–Stolz surgery program, which resolves the analogous question in dimensions $\geq 5$, breaks down in dimension 4 due to the failure of the smooth Whitney trick. The problem is closely tied to the smooth Poincaré conjecture in dimension 4, which remains one of the most important open problems in topology.

$$\boxed{\text{Open problem: the answer is not known.}}$$

### I CANNOT SOLVE THIS
