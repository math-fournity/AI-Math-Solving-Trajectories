# Proof

**Answer: Yes, $E$ is norming.**

## Setup

Let $F$ be a Banach space with closed unit ball $B = \{f \in F : \|f\| \leq 1\}$. Let $E \subset F^*$ be a total subspace (i.e., $E$ separates points of $F$). Define

$$|||f||| = \sup_{e \in E,\, e \neq 0} \frac{|\langle f, e\rangle|}{\|e\|}.$$

**Hypothesis:** $B$ is complete with respect to $|||\cdot|||$.

**Goal:** Show there exists $r > 0$ such that $|||f||| \geq r\|f\|$ for all $f \in F$.

## Step 1: Basic properties of $|||\cdot|||$

Since $E \subset F^*$, for any $e \in E$ we have $|\langle f, e\rangle| \leq \|f\|\|e\|$, so

$$|||f||| \leq \|f\| \quad \text{for all } f \in F. \tag{1}$$

Since $E$ is total, $|||\cdot|||$ is a genuine norm on $F$ (not merely a seminorm): if $|||f||| = 0$, then $\langle f, e\rangle = 0$ for all $e \in E$, which forces $f = 0$ by totality.

## Step 2: $(F, |||\cdot|||)$ is complete

Let $\widetilde{F}$ denote the completion of $(F, |||\cdot|||)$. We view $F$ as a dense subspace of $\widetilde{F}$.

**Each $nB$ is closed in $\widetilde{F}$.** Since $B$ is complete under $|||\cdot|||$ (by hypothesis) and scaling preserves completeness, each $nB = \{f : \|f\| \leq n\}$ is complete under $|||\cdot|||$. A complete subset of a complete metric space is closed, so $nB$ is closed in $\widetilde{F}$.

**Baire category argument.** We have

$$F = \bigcup_{n=1}^{\infty} nB \subset \widetilde{F},$$

and $F$ is dense in $\widetilde{F}$. Since $\widetilde{F}$ is a complete metric space, the Baire category theorem implies that some $nB$ has nonempty interior in $\widetilde{F}$. That is, there exist $h \in nB$ and $\delta > 0$ such that

$$\{x \in \widetilde{F} : |||x - h||| < \delta\} \subset nB. \tag{2}$$

**The ball around $0$ is contained in $F$.** Take any $x \in \widetilde{F}$ with $|||x||| < \delta$. Then:
- $h + x \in nB$ (since $|||(h+x) - h||| = |||x||| < \delta$, by (2)),
- $h \in nB$ (given),
- $-h \in nB$ (since $B$ is symmetric, $B = -B$).

By convexity of $nB$:

$$\frac{(h+x) + (-h)}{2} = \frac{x}{2} \in nB \subset F.$$

Since $F$ is a vector space, $x = 2 \cdot \frac{x}{2} \in F$. Therefore

$$\{x \in \widetilde{F} : |||x||| < \delta\} \subset F. \tag{3}$$

**$F = \widetilde{F}$.** $F$ is a vector subspace of $\widetilde{F}$ containing the open ball of radius $\delta$ around $0$. For any $y \in \widetilde{F}$ with $y \neq 0$, the element $\frac{\delta}{2|||y|||}\, y$ satisfies $|||\frac{\delta}{2|||y|||}\, y||| = \frac{\delta}{2} < \delta$, so it lies in $F$ by (3). Since $F$ is a vector space, $y = \frac{2|||y|||}{\delta} \cdot \frac{\delta}{2|||y|||}\, y \in F$. Hence $F = \widetilde{F}$, and $(F, |||\cdot|||)$ is a Banach space.

## Step 3: Closed graph theorem

Consider the identity map

$$\mathrm{id} : (F, |||\cdot|||) \to (F, \|\cdot\|), \quad f \mapsto f.$$

Both $(F, |||\cdot|||)$ and $(F, \|\cdot\|)$ are Banach spaces (Step 2 and hypothesis respectively).

**The graph is closed.** Suppose $f_n \to f$ in $|||\cdot|||$ and $f_n \to g$ in $\|\cdot\|$. By (1), $|||\cdot||| \leq \|\cdot\|$, so $\|f_n - g\| \to 0$ implies $|||f_n - g||| \to 0$, hence $f_n \to g$ in $|||\cdot|||$. By uniqueness of limits (since $|||\cdot|||$ is a norm), $f = g$.

By the **closed graph theorem**, $\mathrm{id}$ is continuous, so there exists $C > 0$ such that

$$\|f\| \leq C\, |||f||| \quad \text{for all } f \in F.$$

## Conclusion

Setting $r = 1/C > 0$, we obtain

$$|||f||| \geq r\,\|f\| \quad \text{for all } f \in F.$$

Therefore $E$ is norming.

$$\boxed{\text{Yes, } E \text{ is norming: there exists } r > 0 \text{ such that } |||f||| \geq r\|f\| \text{ for all } f \in F.}$$
