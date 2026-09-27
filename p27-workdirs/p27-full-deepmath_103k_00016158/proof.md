# Proof

## Answer

**No.** There is no universal constant $C$ (independent of $J$, $K$, and $\epsilon$) such that the stated conclusion holds under the one-sided hypothesis $K \subset V_\epsilon(J)$.

$$\boxed{\text{No}}$$

## Setup and Key Observation

The hypothesis is **one-sided**: $K \subset V_\epsilon(J)$, meaning every point of $K$ is within distance $\epsilon$ of *some* point of $J$. This does **not** imply that every point of $J$ is close to $K$. In particular, $d(J, K) := \sup_{x \in J} \inf_{y \in K} |x - y|$ can be arbitrarily large relative to $\epsilon$.

The conclusion requires $|j(\xi) - k(\xi)| < C\epsilon$ for **all** $\xi \in T$. Since $j: T \to J$ is surjective, for every $x \in J$ there exists $\xi$ with $j(\xi) = x$, and then $|j(\xi) - k(\xi)| \geq d(x, K)$. Therefore the conclusion forces

$$\sup_{x \in J} d(x, K) \leq C\epsilon.$$

So a necessary condition is $d(J,K) \leq C\epsilon$. We show this can fail with arbitrarily large ratio $d(J,K)/\epsilon$.

## Counterexample

**The curve $J$.** Let $J$ be the ellipse with semi-axes $a$ and $b$, where $a \gg b > 0$:
$$J = \{(a\cos t,\; b\sin t) : t \in [0, 2\pi)\}.$$

**The parameter $\epsilon$.** Set $\epsilon = b + \delta$ for a small $\delta > 0$ (e.g., $\delta = 0.01\, b$, so $\epsilon = 1.01\, b$).

**The curve $K$.** Let $K$ be the circle of radius $r$ centered at the point $p = (a, 0) \in J$, where $r = \delta/2 < \delta < \epsilon$:
$$K = \{p + r(\cos t, \sin t) : t \in [0, 2\pi)\}.$$

### Verification that $K \subset V_\epsilon(J)$

Every point $y \in K$ satisfies $|y - p| = r < \delta < \epsilon$, and $p = (a, 0) \in J$. Hence $d(y, J) \leq |y - p| < \epsilon$ for all $y \in K$, so $K \subset V_\epsilon(J)$. ✓

### Verification that $K$ is a Jordan curve

$K$ is a circle, hence a Jordan curve. ✓

### The distance $d(J, K)$ is large

Consider the point $x_0 = (-a, 0) \in J$ (the leftmost point of the ellipse). For any $y \in K$,
$$|x_0 - y| \geq |x_0 - p| - |p - y| = 2a - r.$$
Therefore
$$d(x_0, K) = \inf_{y \in K} |x_0 - y| = 2a - r = 2a - \delta/2.$$

### No universal $C$ can work

Suppose parametrizations $j: T \to J$ and $k: T \to K$ exist with $|j(\xi) - k(\xi)| < C\epsilon$ for all $\xi$. Since $j$ is surjective, there exists $\xi_0 \in T$ with $j(\xi_0) = x_0 = (-a, 0)$. Then
$$|j(\xi_0) - k(\xi_0)| \geq d(x_0, K) = 2a - \delta/2.$$
The required bound gives
$$2a - \delta/2 \leq |j(\xi_0) - k(\xi_0)| < C\epsilon = C(b + \delta).$$
Thus
$$C > \frac{2a - \delta/2}{b + \delta}.$$

As $a/b \to \infty$ (with $\delta$ fixed, say $\delta = 0.01\, b$), the right-hand side grows like $2a/b \to \infty$. Therefore **no universal constant $C$** (independent of $J$, $K$, $\epsilon$) can satisfy the conclusion.

### Concrete numbers

- $a = 100, b = 1, \delta = 0.01, \epsilon = 1.01, r = 0.005$: requires $C > 199.995 / 1.01 \approx 198$.
- $a = 10^6, b = 1, \delta = 0.01, \epsilon = 1.01$: requires $C > 2 \times 10^6$.

The required $C$ grows without bound, so no fixed universal constant suffices. $\blacksquare$

## Remark on the two-sided (Hausdorff) variant

If the hypothesis were strengthened to the **two-sided** Hausdorff condition $d_H(J, K) \leq \epsilon$ (i.e., both $K \subset V_\epsilon(J)$ and $J \subset V_\epsilon(K)$), then the necessary condition $d(J,K) \leq \epsilon$ is automatically satisfied, and the question becomes whether one can extract a *homeomorphism* $\phi: J \to K$ with $|x - \phi(x)| \leq C\epsilon$ for a universal $C$. That is a substantially different (and deeper) question. Under the literal one-sided reading of the problem as stated, the answer is **No**.

### PROOF COMPLETE
