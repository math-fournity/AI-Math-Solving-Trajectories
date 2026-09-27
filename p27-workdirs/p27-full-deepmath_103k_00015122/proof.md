# Calculation of $\int_T db \wedge dt$

## Setup

We work in $\mathbb{R}^5$ with coordinates $(p_1, q_1, p_2, q_2, t)$. We are given
$$db = dp_1 \wedge dp_2, \qquad T = \{\, t \in [0,1],\; p_1^2 + q_1^2 = p_2^2 + q_2^2 \leq t^2 \,\}.$$

Since $db \wedge dt = dp_1 \wedge dp_2 \wedge dt$ is a **3-form**, the domain $T$ must be a 3-dimensional manifold (with boundary). The equality constraint $p_1^2 + q_1^2 = p_2^2 + q_2^2$ is one equation in $\mathbb{R}^5$, giving a 4-dimensional set; the inequality $\leq t^2$ bounds it. The natural 3-dimensional interpretation that makes the integral well-posed is to take the **boundary surface** where the inequality is saturated:
$$T = \{\, p_1^2 + q_1^2 = p_2^2 + q_2^2 = t^2,\; t \in [0,1] \,\}.$$

We show $\int_T db \wedge dt = 0$ by two independent methods.

---

## Method 1: Direct computation via parametrization

### Parametrization

For each $t \in (0,1]$, the conditions $p_1^2 + q_1^2 = t^2$ and $p_2^2 + q_2^2 = t^2$ describe two circles of radius $t$. We parametrize $T$ (for $t > 0$) by
$$\Phi(t, \theta_1, \theta_2) = (t\cos\theta_1,\; t\sin\theta_1,\; t\cos\theta_2,\; t\sin\theta_2,\; t),$$
with $t \in (0,1]$, $\theta_1, \theta_2 \in [0, 2\pi)$. The point $t = 0$ collapses to the origin and contributes nothing to a 3-dimensional integral.

### Pullback of the 3-form

Compute the pullbacks of the coordinate 1-forms:
$$\Phi^*(dp_1) = \cos\theta_1\, dt - t\sin\theta_1\, d\theta_1,$$
$$\Phi^*(dp_2) = \cos\theta_2\, dt - t\sin\theta_2\, d\theta_2,$$
$$\Phi^*(dt) = dt.$$

Now compute the wedge product:
$$\Phi^*(dp_1 \wedge dp_2) = (\cos\theta_1\, dt - t\sin\theta_1\, d\theta_1) \wedge (\cos\theta_2\, dt - t\sin\theta_2\, d\theta_2).$$

Expanding, the term $\cos\theta_1\cos\theta_2\, dt \wedge dt = 0$. The cross terms $\cos\theta_1\, dt \wedge (-t\sin\theta_2\, d\theta_2)$ and $(-t\sin\theta_1\, d\theta_1)\wedge \cos\theta_2\, dt$ each contain a $dt$ that will vanish when we wedge with $\Phi^*(dt) = dt$ (since $dt \wedge dt = 0$). The only surviving term is:
$$\Phi^*(dp_1 \wedge dp_2) = t^2 \sin\theta_1 \sin\theta_2\, d\theta_1 \wedge d\theta_2 + (\text{terms involving } dt).$$

Wedging with $\Phi^*(dt) = dt$, all terms already containing $dt$ vanish, leaving:
$$\Phi^*(dp_1 \wedge dp_2 \wedge dt) = t^2 \sin\theta_1 \sin\theta_2\, d\theta_1 \wedge d\theta_2 \wedge dt.$$

Reordering to the standard orientation $dt \wedge d\theta_1 \wedge d\theta_2$ requires two swaps ($d\theta_1 \wedge d\theta_2 \wedge dt \to dt \wedge d\theta_1 \wedge d\theta_2$), contributing $(-1)^2 = +1$, so:
$$\Phi^*(dp_1 \wedge dp_2 \wedge dt) = t^2 \sin\theta_1 \sin\theta_2\, dt \wedge d\theta_1 \wedge d\theta_2.$$

### Evaluation

The integral separates:
$$\int_T db \wedge dt = \int_0^1 t^2\, dt \cdot \int_0^{2\pi} \sin\theta_1\, d\theta_1 \cdot \int_0^{2\pi} \sin\theta_2\, d\theta_2.$$

Each angular integral vanishes:
$$\int_0^{2\pi} \sin\theta\, d\theta = \big[-\cos\theta\big]_0^{2\pi} = -\cos(2\pi) + \cos(0) = -1 + 1 = 0.$$

Therefore:
$$\int_T db \wedge dt = \frac{1}{3} \cdot 0 \cdot 0 = 0.$$

---

## Method 2: Stokes' theorem

### The 3-form is exact

Choose the 2-form $b = p_1\, dp_2$, so that $db = dp_1 \wedge dp_2$ as required. Then:
$$d(b \wedge dt) = db \wedge dt + (-1)^{\deg b}\, b \wedge d(dt) = db \wedge dt + (-1)^2\, b \wedge 0 = db \wedge dt,$$
using $d^2 = 0$ (so $d(dt) = 0$) and $\deg b = 2$. Thus $db \wedge dt = d(p_1\, dp_2 \wedge dt)$ is **exact**.

### Applying Stokes' theorem

By Stokes' theorem:
$$\int_T db \wedge dt = \int_T d(p_1\, dp_2 \wedge dt) = \int_{\partial T} p_1\, dp_2 \wedge dt.$$

The boundary $\partial T$ consists of two pieces:

1. **$t = 0$ slice**: The condition $p_1^2 + q_1^2 = p_2^2 + q_2^2 = 0$ forces $p_1 = q_1 = p_2 = q_2 = 0$, so this is the single point $(0,0,0,0,0)$. A 2-form integrated over a 0-dimensional set gives $0$.

2. **$t = 1$ slice**: This is the 2-torus $\{p_1^2 + q_1^2 = p_2^2 + q_2^2 = 1,\; t = 1\}$. Here $t$ is constant, so $dt = 0$ on this slice, and the integrand $p_1\, dp_2 \wedge dt = 0$ identically.

Both boundary pieces contribute $0$, hence:
$$\int_{\partial T} p_1\, dp_2 \wedge dt = 0.$$

---

## Conclusion

Both the direct parametrization computation and Stokes' theorem yield the same result:

$$\boxed{\int_T db \wedge dt = 0}$$

### PROOF COMPLETE
