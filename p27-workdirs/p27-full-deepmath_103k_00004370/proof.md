# Proof: Genus Bound for Curves on del Pezzo Surfaces

## Problem

Let $X$ be a del Pezzo surface over $\mathbb{C}$, obtained by blowing up $\mathbb{P}^2$ at $r$ points ($0 \le r \le 8$) in general position. Let $H$ be the hyperplane class of $\mathbb{P}^2$, and $\pi: X \to \mathbb{P}^2$ the blow-up map. Let $\Sigma$ be a smooth, irreducible curve on $X$ satisfying

$$-K_X \cdot \Sigma > \tfrac{1}{2}\,\Sigma \cdot \Sigma + \pi^*H \cdot \Sigma.$$

**Question:** Is the genus of such curves bounded above?

**Answer:** $\boxed{\text{Yes, the genus is bounded above by } 1.}$

---

## Setup and Notation

Let $L = \pi^*H$ and $E_1, \dots, E_r$ be the exceptional divisors. Any curve class on $X$ can be written as

$$\Sigma \equiv d\,L - \sum_{i=1}^r m_i\, E_i, \qquad d \ge 0,\; m_i \ge 0.$$

Set $s = \sum_{i=1}^r m_i$ and $q = \sum_{i=1}^r m_i^2$. The standard intersection numbers on a del Pezzo surface give:

| Intersection | Value |
|---|---|
| $L \cdot L = 1$ | $L \cdot E_i = 0$ |
| $E_i \cdot E_j = -\delta_{ij}$ | $-K_X = 3L - \sum E_i$ |

From these:

- $\pi^*H \cdot \Sigma = d$,
- $-K_X \cdot \Sigma = 3d - s$,
- $\Sigma^2 = d^2 - q$,
- **Genus (adjunction):** $\displaystyle g = 1 + \frac{\Sigma^2 + \Sigma \cdot K_X}{2} = 1 + \frac{d^2 - q - 3d + s}{2}$.

---

## Step 1: Reformulating the Inequality

Substituting into the given inequality $-K_X \cdot \Sigma > \frac{1}{2}\Sigma^2 + \pi^*H \cdot \Sigma$:

$$3d - s > \tfrac{1}{2}(d^2 - q) + d.$$

Multiplying by 2:

$$6d - 2s > d^2 - q + 2d \implies q > d^2 - 4d + 2s. \tag{$\star$}$$

Now rewrite using the genus formula. From $2g - 2 = d^2 - q - 3d + s$, we get $q = d^2 - 3d + s - 2g + 2$. Substituting into $(\star)$:

$$d^2 - 3d + s - 2g + 2 > d^2 - 4d + 2s,$$

which simplifies to:

$$\boxed{d - s > 2g - 2.} \tag{$\star\star$}$$

Equivalently, $g < 1 + \frac{d - s}{2}$.

We also record the equivalent form of $(\star)$ using $(m_i - 1)^2 = m_i^2 - 2m_i + 1$:

$$\sum_{i=1}^r (m_i - 1)^2 = q - 2s + r > d^2 - 4d + r. \tag{$\star\star\star$}$$

---

## Step 2: Key Lemma — Maximizing $\sum(m_i-1)^2$ Under a Sum Constraint

**Lemma.** *Let $m_1, \dots, m_r$ be non-negative integers with $\sum m_i = s$. Then*

$$\sum_{i=1}^r (m_i - 1)^2 \le (s-1)^2 + (r-1).$$

*Equality holds when $m_1 = s$ and $m_2 = \cdots = m_r = 0$.*

**Proof.** The function $f(x) = (x-1)^2$ is convex. By the extremal principle for convex functions under a sum constraint with non-negativity, the maximum of $\sum f(m_i)$ is achieved at an extreme point of the feasible region, i.e., when the mass is concentrated: one $m_i = s$ and the rest are $0$. This gives $(s-1)^2 + (r-1) \cdot 1 = (s-1)^2 + r - 1$. $\square$

---

## Step 3: Main Argument — Ruling Out $g \ge 2$

**Theorem.** *If $\Sigma$ is a smooth irreducible curve on a del Pezzo surface $X$ satisfying $-K_X \cdot \Sigma > \frac{1}{2}\Sigma^2 + \pi^*H \cdot \Sigma$, then $g(\Sigma) \le 1$.*

**Proof.** Suppose for contradiction that $g \ge 2$.

**From $(\star\star)$:** $d - s > 2g - 2 \ge 2$, so

$$s \le d - 3. \tag{1}$$

**From $(\star\star\star)$ and the Lemma:**

$$d^2 - 4d + r < \sum_{i=1}^r (m_i - 1)^2 \le (s-1)^2 + (r-1). \tag{2}$$

We now bound $(s-1)^2$ using (1). Since $0 \le s \le d-3$, the value $(s-1)^2$ is maximized at the endpoints of $[0, d-3]$:

- At $s = 0$: $(s-1)^2 = 1$.
- At $s = d-3$: $(s-1)^2 = (d-4)^2$.

**Case A: $d \ge 5$.** Then $(d-4)^2 \ge 1$, so $(s-1)^2 \le (d-4)^2 = d^2 - 8d + 16$. Substituting into (2):

$$d^2 - 4d + r < d^2 - 8d + 16 + r - 1 = d^2 - 8d + 15 + r,$$

which gives $-4d + 15 > 0$, i.e., $d < \frac{15}{4} = 3.75$. This contradicts $d \ge 5$.

**Case B: $d = 4$.** Then $s \le 1$.

- If $s = 0$: all $m_i = 0$, so $\sum(m_i-1)^2 = r$. Inequality $(\star\star\star)$: $r > 16 - 16 + r = r$, i.e., $r > r$. Contradiction.
- If $s = 1$: one $m_i = 1$, rest $0$. Then $\sum(m_i-1)^2 = 0 + (r-1) = r-1$. Inequality: $r - 1 > r$, i.e., $-1 > 0$. Contradiction.

**Case C: $d \le 3$.** From (1), $s \le d - 3 \le 0$, so $s = 0$ and all $m_i = 0$. The genus formula gives:

$$g = 1 + \frac{d^2 - 0 - 3d + 0}{2} = 1 + \frac{d(d-3)}{2}.$$

For $d = 3$: $g = 1 + 0 = 1$. For $d = 2$: $g = 1 + (-1) = 0$. For $d = 1$: $g = 1 + (-1) = 0$. For $d = 0$: $g = 1 + 0 = 1$ (but $d = 0$ gives $\Sigma \equiv 0$, not a curve).

In all subcases with $d \le 3$, we get $g \le 1$, contradicting $g \ge 2$.

**Conclusion:** All cases lead to contradiction. Therefore $g \le 1$. $\square$

---

## Step 4: Sharpness — $g = 1$ Is Achieved

Take $r = 0$ (i.e., $X = \mathbb{P}^2$), $d = 3$: a smooth plane cubic $\Sigma$. Then:

- $\pi^*H \cdot \Sigma = 3$,
- $\Sigma^2 = 9$,
- $-K_X \cdot \Sigma = 9$,
- $g = 1$.

The inequality: $9 > \frac{1}{2} \cdot 9 + 3 = 7.5$. ✓

More generally, for any $r \le 8$, the class $\Sigma \equiv 3L$ (pullback of a smooth plane cubic avoiding the blown-up points) gives $g = 1$ and satisfies the inequality: $9 > 4.5 + 3 = 7.5$. ✓

For $g = 0$ examples with unbounded $d$: on the del Pezzo surface of degree 8 ($r = 1$), the class $\Sigma \equiv dL - (d-1)E_1$ for any $d \ge 1$ gives $g = 0$ and satisfies the inequality (since $(d-2)^2 > d^2 - 4d + 1 \iff 1 < 4$). This shows $d$ can be unbounded while $g = 0$, confirming that the bound is on genus, not on degree.

---

## Summary

The inequality $-K_X \cdot \Sigma > \frac{1}{2}\Sigma^2 + \pi^*H \cdot \Sigma$ is equivalent to $d - s > 2g - 2$. Assuming $g \ge 2$ forces $s \le d - 3$, which combined with the convexity-based upper bound $\sum(m_i-1)^2 \le (s-1)^2 + (r-1)$ and the inequality $\sum(m_i-1)^2 > d^2 - 4d + r$, yields $d < 15/4$ (for $d \ge 5$, contradiction) or direct contradictions (for $d = 4$), ultimately forcing $d \le 3$ and $s = 0$, which gives $g \le 1$—contradicting $g \ge 2$.

$$\boxed{\text{Yes, the genus is bounded above (by } g \le 1\text{).}}$$

### PROOF COMPLETE
