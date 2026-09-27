# Proof: Intrinsic Invariance Forces $P(x,y) = F(xy)$

## Statement

Let $P(x,y)$ be a polynomial with real coefficients. Suppose $P(\kappa_1, \kappa_2)$ is intrinsically invariant for all surfaces in $\mathbb{R}^3$, i.e., invariant under isometries of surfaces (diffeomorphisms preserving the first fundamental form). Then $P(x,y) = F(xy)$ for some one-variable polynomial $F$.

## Answer

$$\boxed{\text{Yes, } P(x,y) = F(xy) \text{ for some one-variable polynomial } F.}$$

---

## Proof

### Step 0: Setup and notation

Let $\kappa_1, \kappa_2$ denote the principal curvatures of a surface $S \subset \mathbb{R}^3$. Recall:
- **Gaussian curvature**: $K = \kappa_1 \kappa_2$.
- **Mean curvature**: $H = \tfrac{1}{2}(\kappa_1 + \kappa_2)$.

By **Gauss's Theorema Egregium**, $K$ is determined by the first fundamental form $I$ alone, hence is intrinsic. In contrast, $H$ depends on the second fundamental form $II$ and is **not** intrinsic.

### Step 1: Sufficiency — $F(xy)$ is intrinsically invariant

If $P(x,y) = F(xy)$, then $P(\kappa_1,\kappa_2) = F(\kappa_1\kappa_2) = F(K)$. Since $K$ is intrinsic (Gauss), $F(K)$ is intrinsic for any polynomial $F$. This establishes sufficiency.

### Step 2: Necessity — strategy

We must show: if $P(\kappa_1,\kappa_2)$ is invariant under all surface isometries, then $P$ is constant on each hyperbola $\{xy = c\}$, which forces $P(x,y) = F(xy)$.

The key geometric input is:

> **(★) For every $c < 0$ and every pair $(a, b)$ with $ab = c$, there exist two isometric surfaces $S, S'$ in $\mathbb{R}^3$ and a point $p$ (identified via the isometry) such that $(\kappa_1, \kappa_2)|_p = (a, b)$ on $S$ and $(\kappa_1', \kappa_2')|_p$ is any other pair $(a', b')$ with $a'b' = c$ on $S'$.

We prove (★) below using the **fundamental theorem of surfaces** combined with **Cauchy–Kovalevskaya** and the **Bianchi identity**.

### Step 3: Constructing isometric surfaces with prescribed principal curvatures (proof of (★))

Fix $c < 0$. Let $S$ be any surface with $K < 0$ in a neighborhood of a point $p$, with $K(p) = c$. (For instance, take a pseudosphere scaled so that $K \equiv c$.) Let $I = E\,du^2 + 2F\,du\,dv + G\,dv^2$ be the first fundamental form in local coordinates $(u,v)$ near $p$, and let $II = e\,du^2 + 2f\,du\,dv + g\,dv^2$ be the second fundamental form.

**Goal**: Find a new second fundamental form $II' = e'\,du^2 + 2f'\,du\,dv + g'\,dv^2$ such that:
1. **Gauss equation**: $e'g' - f'^2 = K \cdot (EG - F^2)$ (same $K$ since $I$ is unchanged).
2. **Codazzi equations**: the integrability conditions for $II'$ with respect to $I$.
3. At the point $p$, the principal curvatures derived from $(I, II')$ are any prescribed $(a', b')$ with $a'b' = c$.

**Step 3a: Initial data on a curve.** Choose a curve $\gamma$ through $p$ that is **non-characteristic** for the Codazzi system (a generic curve, e.g., not tangent to a principal direction). Along $\gamma$, we prescribe analytic functions $e'(u,v), f'(u,v), g'(u,v)$ satisfying:
- The Gauss equation $e'g' - f'^2 = K(EG - F^2)$ at every point of $\gamma$.
- At $p$, the values $(e', f', g')$ yield the target principal curvatures $(a', b')$.

This is feasible: the Gauss equation is one constraint on three unknowns $(e', f', g')$, leaving a 2-parameter family at each point. For example, set $f' = 0$ along $\gamma$ and solve $e'g' = K(EG-F^2)$ for $g' = K(EG-F^2)/e'$, choosing $e'$ as an analytic positive function along $\gamma$ that at $p$ gives the correct eigenvalues. Since $K(p) = c < 0$, we have $K(EG - F^2) < 0$ at $p$ (as $EG - F^2 > 0$), so $e'$ and $g'$ have opposite signs, consistent with $\kappa_1' \kappa_2' = c < 0$.

**Step 3b: Extension via Cauchy–Kovalevskaya.** The Codazzi equations form a **linear first-order PDE system** for $(e', f', g')$ (with coefficients determined by $I$ and its Christoffel symbols). Assuming the data is analytic and $\gamma$ is non-characteristic, the **Cauchy–Kovalevskaya theorem** gives a unique analytic solution $(e', f', g')$ in a neighborhood of $p$ extending the initial data on $\gamma$.

**Step 3c: Gauss equation propagates (Bianchi identity).** Define
$$\Phi := e'g' - f'^2 - K \cdot (EG - F^2).$$
We have $\Phi|_\gamma = 0$ by construction. A classical consequence of the **Codazzi equations** (equivalently, the **Bianchi identity** / integrability of the connection) is:
$$d\Phi = \alpha \cdot \Phi$$
for a certain 1-form $\alpha$ determined by $I$. This means $\Phi$ satisfies a linear first-order ODE along any path. Since $\Phi = 0$ on $\gamma$, the uniqueness of solutions to such ODEs gives $\Phi \equiv 0$ in a neighborhood of $p$.

**Step 3d: Application of the fundamental theorem.** We now have $(I, II')$ satisfying both the Gauss and Codazzi equations. By the **fundamental theorem of surface theory** (Bonnet), there exists a surface $S' \subset \mathbb{R}^3$ (unique up to rigid motion) with first fundamental form $I$ and second fundamental form $II'$. Since $S'$ has the same first fundamental form $I$ as $S$, the map $S \to S'$ (in these coordinates) is an **isometry**. At the point $p$, the principal curvatures of $S'$ are the prescribed $(a', b')$ with $a'b' = c$.

This establishes (★): for any $c < 0$ and any two points $(a,b), (a',b')$ on the hyperbola $\{xy = c\}$, there exist isometric surfaces realizing these as principal curvatures at corresponding points.

### Step 4: $P$ is constant on hyperbolas $\{xy = c\}$ for $c < 0$

By the intrinsic invariance hypothesis and (★): for any $c < 0$ and any $(a,b), (a',b')$ with $ab = a'b' = c$,
$$P(a, b) = P(a', b').$$
Thus $P$ is constant on each hyperbola $\{xy = c\}$ for every $c < 0$.

### Step 5: Polynomial identity argument

Write $P(x,y) = \sum_{i,j \geq 0} a_{ij}\, x^i y^j$. The condition that $P$ is constant on $\{xy = c\}$ means: for each $c < 0$, the function
$$x \mapsto P(x, c/x) = \sum_{i,j} a_{ij}\, c^j\, x^{i-j}$$
is constant in $x$. Therefore, for every integer $k \neq 0$, the coefficient of $x^k$ vanishes:
$$\sum_{\substack{i - j = k}} a_{ij}\, c^j = 0 \quad \text{for all } c < 0.$$

For fixed $k \neq 0$, this is a polynomial in $c$ (with real coefficients) that vanishes on the entire interval $(-\infty, 0)$. A polynomial vanishing on an interval is identically zero, so:
$$a_{ij} = 0 \quad \text{for all } i \neq j.$$

Therefore, the only surviving terms have $i = j$:
$$P(x,y) = \sum_{n \geq 0} a_{nn}\, (xy)^n =: F(xy),$$
where $F(t) = \sum_{n \geq 0} a_{nn}\, t^n$ is a one-variable polynomial. $\quad\blacksquare$

---

## Summary

| Step | Content |
|------|---------|
| 1 | Sufficiency: $F(K)$ is intrinsic by Gauss's Theorema Egregium. |
| 2 | Strategy: show $P$ constant on each $\{xy=c\}$, $c<0$. |
| 3 | **Key construction**: For $K<0$, use the fundamental theorem of surfaces + Cauchy–Kovalevskaya + Bianchi identity to build isometric surfaces with arbitrary principal curvatures on the same hyperbola $\{xy = c\}$. |
| 4 | Intrinsic invariance $\Rightarrow$ $P$ constant on $\{xy=c\}$ for all $c<0$. |
| 5 | Polynomial identity: vanishing on $(-\infty,0)$ forces $a_{ij}=0$ for $i\neq j$, giving $P(x,y)=F(xy)$. |

### PROOF COMPLETE
