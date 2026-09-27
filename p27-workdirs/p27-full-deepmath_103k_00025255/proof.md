# Does there exist a distance metric for the $SE(3)$ group that satisfies the triangle inequality?

## Answer

$$\boxed{\text{No — there is no bi-invariant distance metric on } SE(3) \text{ satisfying the triangle inequality and inducing the manifold topology.}}$$

## Interpretation

A "distance metric for the $SE(3)$ group" is understood as a **bi-invariant** distance: one satisfying $d(gx, gy) = d(x, y)$ and $d(xg, yg) = d(x, y)$ for all $g, x, y \in SE(3)$, compatible with the group structure, inducing the manifold topology, and satisfying the triangle inequality. This is the standard meaning in robotics and geometric mechanics literature.

(Remark: a merely *left-invariant* Riemannian metric always exists on any Lie group and induces a distance satisfying the triangle inequality — so the question is only interesting in the bi-invariant setting.)

---

## Proof

### Setup

$SE(3) = SO(3) \ltimes \mathbb{R}^3$ is the group of rigid body motions. Elements are pairs $(R, t)$ with $R \in SO(3)$, $t \in \mathbb{R}^3$, and group law
$$(R_1, t_1)(R_2, t_2) = (R_1 R_2,\; R_1 t_2 + t_1).$$

The Lie algebra $\mathfrak{se}(3)$ consists of pairs $(\Omega, v) \in \mathbb{R}^3 \times \mathbb{R}^3$ with bracket
$$[(\Omega_1, v_1),\, (\Omega_2, v_2)] = (\Omega_1 \times \Omega_2,\; \Omega_1 \times v_2 - \Omega_2 \times v_1).$$

**Assume for contradiction** that there exists a bi-invariant distance $d$ on $SE(3)$ that satisfies the triangle inequality and induces the manifold topology.

### Step 1: Define $F$ and establish Ad-invariance

Define $F : \mathfrak{se}(3) \to [0, \infty)$ by
$$F(X) := d(e, \exp(X)).$$

Since $d$ is continuous (being a metric on a manifold) and $\exp$ is continuous, $F$ is continuous with $F(0) = 0$ and $F(X) > 0$ for $X$ near $0$, $X \neq 0$.

**Claim:** $F$ is $\operatorname{Ad}$-invariant, i.e., $F(\operatorname{Ad}_g X) = F(X)$ for all $g \in SE(3)$, $X \in \mathfrak{se}(3)$.

*Proof of claim:* By bi-invariance of $d$,
$$d(e,\, g \exp(X) g^{-1}) = d(g^{-1},\, \exp(X) g^{-1}) = d(g^{-1} g,\, g \exp(X) g^{-1} g) = d(e, \exp(X)).$$
More directly: $d(e, g \exp(X) g^{-1}) = d(g, g\exp(X)) = d(e, \exp(X))$, using left-invariance twice. Since $g \exp(X) g^{-1} = \exp(\operatorname{Ad}_g X)$, we obtain $F(\operatorname{Ad}_g X) = F(X)$. $\square$

### Step 2: $F(\Omega, v)$ depends only on $|\Omega|$ and $v \cdot \Omega$

The adjoint action of a pure translation $g = (I, s)$ on $(\Omega, v) \in \mathfrak{se}(3)$ is:
$$\operatorname{Ad}_{(I, s)}(\Omega, v) = (\Omega,\; v - s \times \Omega).$$

By Ad-invariance:
$$F(\Omega, v) = F(\Omega,\; v - s \times \Omega) \quad \text{for all } s \in \mathbb{R}^3.$$

As $s$ ranges over $\mathbb{R}^3$, the vector $s \times \Omega$ ranges over the plane $\Omega^\perp$ (all vectors perpendicular to $\Omega$). Therefore $F(\Omega, \cdot)$ is constant on each affine coset $v + \Omega^\perp$, which means:

$$F(\Omega, v) = \varphi\!\left(|\Omega|,\; v \cdot \widehat{\Omega}\right)$$

for some function $\varphi$, where $\widehat{\Omega} = \Omega / |\Omega|$ (for $\Omega \neq 0$). In particular, **$F(\Omega, v)$ does not depend on the component of $v$ perpendicular to $\Omega$.**

### Step 3: Construct the contradicting sequence

Define the sequence
$$g_n := \left(R_{1/n}^{z},\; (n,\, 0,\, 0)\right) \in SE(3), \qquad n = 1, 2, 3, \ldots$$

where $R_{1/n}^{z}$ is rotation by angle $1/n$ about the $z$-axis.

**The translation part of $g_n$ diverges:** $\|(n, 0, 0)\| = n \to \infty$, so $g_n$ does **not** converge to the identity $e = (I, 0)$ in the manifold topology of $SE(3)$.

**Compute $d(e, g_n)$:** Let $X_n = \log(g_n) \in \mathfrak{se}(3)$. Then $X_n = (\Omega_n, v_n)$ where:
- $\Omega_n = (0, 0, 1/n)$ (rotation vector, magnitude $1/n$),
- $v_n = A^{-1}(n, 0, 0)$ where $A$ is the Jacobian of the exponential map.

The **pitch** (component of translation along the rotation axis) is:
$$v_n \cdot \widehat{\Omega}_n = v_n \cdot (0, 0, 1) = 0,$$

since $A$ maps vectors perpendicular to $\Omega$ to vectors perpendicular to $\Omega$ (the exponential map preserves the screw structure), and $(n, 0, 0) \perp (0, 0, 1)$.

Therefore:
$$d(e, g_n) = F(X_n) = \varphi\!\left(\tfrac{1}{n},\; 0\right).$$

### Step 4: Show $d(e, g_n) \to 0$

Consider the element $h_n := (R_{1/n}^{z},\, 0) = \exp\!\big((0, 0, 1/n),\, (0, 0, 0)\big)$. Then:
$$d(e, h_n) = F\!\big((0, 0, 1/n),\, (0, 0, 0)\big) = \varphi\!\left(\tfrac{1}{n},\; 0\right).$$

Since $h_n = (R_{1/n}^{z}, 0) \to (I, 0) = e$ in the manifold topology (the rotation angle $1/n \to 0$ and translation is zero), and $d$ induces the manifold topology:
$$d(e, h_n) \to 0 \quad \text{as } n \to \infty.$$

But by Step 2, $F$ depends only on $(|\Omega|, v \cdot \widehat{\Omega})$, and both $g_n$ and $h_n$ have the same invariants $(1/n, 0)$:
$$d(e, g_n) = \varphi\!\left(\tfrac{1}{n}, 0\right) = d(e, h_n) \to 0.$$

### Step 5: Contradiction

We have established:
- $d(e, g_n) \to 0$ as $n \to \infty$,
- $g_n = (R_{1/n}^{z}, (n, 0, 0))$ does **not** converge to $e$ (since $\|(n, 0, 0)\| = n \to \infty$).

This directly contradicts the requirement that $d$ **induces the manifold topology**, which demands:
$$d(e, g_n) \to 0 \iff g_n \to e.$$

The contradiction shows that **no bi-invariant distance on $SE(3)$ can both satisfy the triangle inequality and induce the manifold topology.** $\blacksquare$

---

## Intuition

The root cause is that $SE(3) = SO(3) \ltimes \mathbb{R}^3$ is a **non-trivial semidirect product**. The adjoint action of translations on the Lie algebra creates a "shear" — it moves the translation component $v$ in directions perpendicular to $\Omega$ without changing the rotation. Bi-invariance forces the distance to be blind to this perpendicular translation (it can only see the pitch $v \cdot \Omega$), but the manifold topology requires the distance to detect *all* translation. These two requirements are incompatible.

This also explains why $SE(3)$ admits no bi-invariant *Riemannian* metric: a connected Lie group admits a bi-invariant Riemannian metric iff it is isomorphic to $K \times \mathbb{R}^n$ for compact $K$, and $SE(3)$ is not of this form. The argument above shows the obstruction is even stronger — it rules out *any* bi-invariant distance, not just Riemannian ones.
