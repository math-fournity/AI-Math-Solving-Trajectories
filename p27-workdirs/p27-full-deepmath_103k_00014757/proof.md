# Proof: Bisection by all hyperplanes through the origin implies central symmetry

**Claim.** Let $U \subset \mathbb{R}^n$ be a bounded open convex set such that every hyperplane passing through the origin divides $U$ into two sets of equal $n$-dimensional Lebesgue volume. Then $U = -U$.

**Answer:** $\boxed{\text{Yes, } U = -U.}$

---

## Step 0: The cases $n = 1$ and $n = 2$

### $n = 1$

$U = (a, b)$ is a bounded open interval. The only "hyperplane through the origin" is $\{0\}$. The bisection condition gives $|a| = |b|$, i.e. $a = -b$, so $U = -U$.

### $n = 2$

We treat $n = 2$ separately because the Gegenbauer parameter $\lambda = (n-2)/2 = 0$ causes the Rodrigues formula (used below for $n \geq 3$) to degenerate.

Once Step 1 (showing $0 \in U$) is established, define the radial function $\rho(\alpha) = \max\{r > 0 : r(\cos\alpha, \sin\alpha) \in U\}$ for $\alpha \in [0, 2\pi)$. Then

$$\mathrm{Vol}(U) = \tfrac{1}{2}\int_0^{2\pi} \rho(\alpha)^2\, d\alpha.$$

Set $g(\alpha) = \rho(\alpha)^2$ and $h(\alpha) = g(\alpha) - g(\alpha + \pi)$. Then $h$ is $\pi$-**anti-periodic**: $h(\alpha + \pi) = -h(\alpha)$. The bisection condition for the line through the origin at angle $\beta$ reads

$$\int_{\beta - \pi/2}^{\beta + \pi/2} h(\alpha)\, d\alpha = 0 \qquad \forall\, \beta.$$

This is a convolution $(h * \mathbf{1}_{[-\pi/2,\, \pi/2]})(\beta) = 0$. Taking Fourier coefficients:

$$\hat{h}(k) \cdot \widehat{\mathbf{1}}_{[-\pi/2,\, \pi/2]}(k) = 0 \qquad \forall\, k \in \mathbb{Z},$$

where $\widehat{\mathbf{1}}_{[-\pi/2,\, \pi/2]}(k) = \frac{\sin(k\pi/2)}{k\pi}$ for $k \neq 0$ and $= 1/2$ for $k = 0$. This kernel coefficient vanishes for even $k \neq 0$ and is nonzero for all odd $k$ (and for $k = 0$).

The $\pi$-anti-periodicity of $h$ forces $\hat{h}(k) = 0$ for all **even** $k$ (including $k = 0$, since $e^{i \cdot 0 \cdot \pi} = 1 \neq -1$). The convolution condition then forces $\hat{h}(k) = 0$ for all **odd** $k$. Hence $\hat{h}(k) = 0$ for every $k$, so $h \equiv 0$, giving $\rho(\alpha) = \rho(\alpha + \pi)$ and $U = -U$.

---

## Step 1: The origin lies in $U$ (all $n \geq 1$)

We show $0 \in U$ by ruling out $0 \notin \overline{U}$ and $0 \in \partial U$.

**Case 1: $0 \notin \overline{U}$.** Since $\overline{U}$ is compact and convex, the (strict) separation theorem gives a unit vector $v$ with $v \cdot x > 0$ for all $x \in \overline{U}$. Then the hyperplane $H_v = \{x : v \cdot x = 0\}$ has $U$ entirely on one side, so it does not bisect $U$—contradiction.

**Case 2: $0 \in \partial U$.** By the supporting hyperplane theorem, there exists a unit vector $v$ with $v \cdot x \geq 0$ for all $x \in \overline{U}$. We claim in fact $v \cdot x > 0$ for all $x \in U$. Suppose for contradiction that some $x_0 \in U$ satisfies $v \cdot x_0 = 0$. Since $U$ is open, a small ball $B(x_0, \varepsilon) \subset U$ exists, and it contains points $x_0 - \delta\, v$ (for small $\delta > 0$) with $v \cdot (x_0 - \delta v) = -\delta < 0$, contradicting $v \cdot x \geq 0$ on $\overline{U}$. Hence $v \cdot x > 0$ on all of $U$, so $H_v$ does not bisect $U$—contradiction.

Therefore $0 \in \overline{U} \setminus \partial U = \mathrm{int}(\overline{U})$. Since $U$ is open and convex, $\mathrm{int}(\overline{U}) = U$, so $0 \in U$.

---

## Step 2: Radial-function reduction (all $n \geq 1$)

Since $0 \in U$ and $U$ is open, the **radial function**

$$\rho(\theta) = \max\{r > 0 : r\theta \in U\}, \qquad \theta \in S^{n-1},$$

is well defined, finite (by boundedness), and **continuous** (by convexity of $U$; the boundary of a convex body is continuous in every direction). In polar coordinates,

$$\mathrm{Vol}(U) = \frac{1}{n}\int_{S^{n-1}} \rho(\theta)^n\, d\sigma(\theta),$$

where $d\sigma$ is the surface measure on $S^{n-1}$. Set $g(\theta) = \rho(\theta)^n$ (continuous, nonneg.) and

$$h(\theta) = g(\theta) - g(-\theta).$$

Then $h$ is **continuous** and **odd**: $h(-\theta) = -h(\theta)$, so $\int_{S^{n-1}} h\, d\sigma = 0$.

For a unit vector $v$, the hyperplane $\{x : v \cdot x = 0\}$ splits $U$ into the two halves $\{v \cdot x > 0\} \cap U$ and $\{v \cdot x < 0\} \cap U$. In polar coordinates the volume of the positive half is $\frac{1}{n}\int_{\{v \cdot \theta > 0\}} g(\theta)\, d\sigma$ and similarly for the negative half. The bisection condition is therefore

$$\int_{\{v \cdot \theta > 0\}} g(\theta)\, d\sigma = \int_{\{v \cdot \theta < 0\}} g(\theta)\, d\sigma \qquad \forall\, v \in S^{n-1}.$$

Subtracting and using the substitution $\theta \mapsto -\theta$ on the negative hemisphere,

$$\int_{\{v \cdot \theta > 0\}} \bigl[g(\theta) - g(-\theta)\bigr]\, d\sigma(\theta) = \int_{H_v} h(\theta)\, d\sigma(\theta) = 0 \qquad \forall\, v \in S^{n-1},$$

where $H_v = \{\theta \in S^{n-1} : v \cdot \theta > 0\}$ is the open hemisphere centered at $v$.

**It remains to prove:** if $h \in C(S^{n-1})$ is odd and $\int_{H_v} h\, d\sigma = 0$ for every $v$, then $h \equiv 0$.

---

## Step 3: Reduction to a zonal convolution operator via Funk–Hecke (for $n \geq 3$)

Define the **hemisphere transform**

$$\mathcal{H}[h](v) = \int_{H_v} h(\theta)\, d\sigma(\theta) = \int_{\{v \cdot \theta > 0\}} h(\theta)\, d\sigma(\theta).$$

Since $h$ is odd, $\int_{S^{n-1}} h\, d\sigma = 0$, and we may write

$$\mathcal{H}[h](v) = \frac{1}{2}\int_{S^{n-1}} h(\theta)\, \operatorname{sgn}(v \cdot \theta)\, d\sigma(\theta) = \frac{1}{2}\, T[h](v),$$

where $T$ is the zonal convolution operator with kernel $K(v, \theta) = \operatorname{sgn}(v \cdot \theta)$, which depends only on $v \cdot \theta$. By the **Funk–Hecke theorem**, $T$ is diagonalized by spherical harmonics: if $Y_\ell^m$ is a spherical harmonic of degree $\ell$,

$$T[Y_\ell^m](v) = \lambda_\ell\, Y_\ell^m(v),$$

with eigenvalue (independent of $m$)

$$\lambda_\ell = |S^{n-2}| \int_{-1}^{1} \operatorname{sgn}(t)\, \frac{C_\ell^\lambda(t)}{C_\ell^\lambda(1)}\, (1 - t^2)^{\lambda - 1/2}\, dt, \qquad \lambda = \frac{n-2}{2}.$$

(Here $C_\ell^\lambda$ is the Gegenbauer polynomial and $|S^{n-2}|$ the area of the $(n{-}2)$-sphere; the factor $(1-t^2)^{\lambda-1/2}$ is the standard weight in the Funk–Hecke formula.)

Since $\operatorname{sgn}(t)$ is an **odd** function of $t$, the integrand is odd when $\ell$ is even (then $C_\ell^\lambda$ is even) and even when $\ell$ is odd (then $C_\ell^\lambda$ is odd). Therefore

$$\lambda_\ell = 0 \quad \text{for even } \ell, \qquad \lambda_\ell = \frac{2\,|S^{n-2}|}{C_\ell^\lambda(1)} \int_0^1 C_\ell^\lambda(t)\, (1 - t^2)^{\lambda - 1/2}\, dt \quad \text{for odd } \ell.$$

Denote $I_\ell := \int_0^1 C_\ell^\lambda(t)\, (1 - t^2)^{\lambda - 1/2}\, dt$ for odd $\ell$.

Now expand $h$ (which is odd, so only odd-degree harmonics appear):

$$h = \sum_{\ell \text{ odd}} \sum_{m} a_\ell^m\, Y_\ell^m.$$

The condition $\mathcal{H}[h] = 0$ becomes $\lambda_\ell\, a_\ell^m = 0$ for every odd $\ell$ and every $m$. **If $\lambda_\ell \neq 0$ for every odd $\ell \geq 1$, then every $a_\ell^m = 0$, hence $h \equiv 0$.**

So the entire proof reduces to showing:

> **Key Lemma.** For every odd $\ell \geq 1$ and every $\lambda > 0$ (i.e. $n \geq 3$), $I_\ell \neq 0$.

---

## Step 4: The Key Lemma — $I_\ell \neq 0$ for odd $\ell$ and $\lambda > 0$

We use the **Rodrigues formula** for Gegenbauer polynomials:

$$C_\ell^\lambda(t) = \frac{(-1)^\ell\, (2\lambda)_\ell}{2^\ell\, \ell!\, (\lambda + 1/2)_\ell}\, (1 - t^2)^{1/2 - \lambda}\, \frac{d^\ell}{dt^\ell}\, (1 - t^2)^{\ell + \lambda - 1/2},$$

where $(a)_\ell = a(a+1)\cdots(a+\ell-1)$ is the Pochhammer symbol. Set

$$f(t) = (1 - t^2)^{\ell + \lambda - 1/2}, \qquad \alpha := \ell + \lambda - \tfrac{1}{2}.$$

Substituting the Rodrigues formula into $I_\ell$:

$$I_\ell = \frac{(-1)^\ell\, (2\lambda)_\ell}{2^\ell\, \ell!\, (\lambda + 1/2)_\ell} \int_0^1 \frac{d^\ell f}{dt^\ell}(t)\, dt = \frac{(-1)^\ell\, (2\lambda)_\ell}{2^\ell\, \ell!\, (\lambda + 1/2)_\ell}\, \Bigl[\, f^{(\ell-1)}(1) - f^{(\ell-1)}(0)\,\Bigr].$$

### (a) $f^{(\ell-1)}(1) = 0$

Near $t = 1$, $f(t) = (1-t^2)^\alpha \sim (2(1-t))^\alpha$, i.e. $f(t) \sim c\,(1-t)^\alpha$ with $\alpha = \ell + \lambda - 1/2$. The $(\ell-1)$-st derivative of $(1-t)^\alpha$ at $t = 1$ is a constant times $(1-t)^{\alpha - (\ell-1)}$, which vanishes at $t=1$ provided $\alpha - (\ell - 1) > 0$, i.e. $\lambda + 1/2 > 0$, which holds since $\lambda > 0$. Hence $f^{(\ell-1)}(1) = 0$.

### (b) $f^{(\ell-1)}(0) \neq 0$

$f(t) = (1 - t^2)^\alpha$ is an **even** function, so $f^{(k)}(0) = 0$ for odd $k$ and $f^{(k)}(0) \neq 0$ (generically) for even $k$. Since $\ell$ is odd, $\ell - 1$ is **even**, so $f^{(\ell-1)}(0)$ is the derivative of even order and need not vanish. Concretely, expand $f(t) = (1 - t^2)^\alpha = \sum_{j \geq 0} \binom{\alpha}{j}(-1)^j t^{2j}$. The coefficient of $t^{\ell-1}$ (with $\ell - 1 = 2j$, so $j = (\ell-1)/2$) is

$$\binom{\alpha}{j}(-1)^j, \qquad j = \frac{\ell - 1}{2}, \quad \alpha = \ell + \lambda - \frac{1}{2}.$$

Thus $f^{(\ell-1)}(0) = (\ell - 1)!\, \binom{\alpha}{j}\, (-1)^j$. The generalized binomial coefficient is

$$\binom{\alpha}{j} = \frac{\alpha(\alpha-1)\cdots(\alpha - j + 1)}{j!}.$$

Every factor in the numerator is positive: the smallest is $\alpha - j + 1 = \bigl(\ell + \lambda - \tfrac{1}{2}\bigr) - \tfrac{\ell-1}{2} + 1 = \tfrac{\ell}{2} + \lambda + \tfrac{1}{2} > 0$ (since $\lambda > 0$). Hence $\binom{\alpha}{j} > 0$, and

$$f^{(\ell-1)}(0) = (\ell-1)!\, \binom{\alpha}{j}\, (-1)^{(\ell-1)/2} \neq 0.$$

### (c) Closed form and conclusion

Combining (a) and (b):

$$I_\ell = \frac{(-1)^\ell\, (2\lambda)_\ell}{2^\ell\, \ell!\, (\lambda + 1/2)_\ell}\, \Bigl(0 - f^{(\ell-1)}(0)\Bigr) = \frac{(-1)^{\ell+1}\, (2\lambda)_\ell}{2^\ell\, \ell!\, (\lambda + 1/2)_\ell}\, f^{(\ell-1)}(0).$$

Writing $f^{(\ell-1)}(0)$ out explicitly via the gamma function (using $\binom{\alpha}{j} = \frac{\Gamma(\alpha+1)}{\Gamma(j+1)\,\Gamma(\alpha - j + 1)}$ with $\alpha + 1 = \ell + \lambda + 1/2$, $j + 1 = (\ell+1)/2$, $\alpha - j + 1 = \ell/2 + \lambda + 1$):

$$I_\ell = (-1)^{(\ell-1)/2}\, \frac{(2\lambda)_\ell\, (\ell-1)!}{2^\ell\, \ell!\, (\lambda + 1/2)_\ell}\, \frac{\Gamma(\ell + \lambda + 1/2)}{\Gamma\bigl((\ell+1)/2\bigr)\, \Gamma(\ell/2 + \lambda + 1)}.$$

**Every factor in this expression is strictly positive** (for $\lambda > 0$):
- $(2\lambda)_\ell > 0$ since $2\lambda > 0$;
- $(\ell-1)!,\; \ell!,\; 2^\ell,\; (\lambda+1/2)_\ell$ all positive;
- all gamma-function arguments are positive, so the gamma ratio is positive.

The **only** sign contribution is $(-1)^{(\ell-1)/2} = \pm 1$. Therefore

$$|I_\ell| = \frac{(2\lambda)_\ell\, (\ell-1)!}{2^\ell\, \ell!\, (\lambda + 1/2)_\ell}\, \frac{\Gamma(\ell + \lambda + 1/2)}{\Gamma\bigl((\ell+1)/2\bigr)\, \Gamma(\ell/2 + \lambda + 1)} > 0.$$

Hence $I_\ell \neq 0$ for every odd $\ell \geq 1$ and every $\lambda > 0$. $\quad\blacksquare$

### Sanity checks

- **$\ell = 1$:** $C_1^\lambda(t) = 2\lambda\, t$, so $I_1 = 2\lambda \int_0^1 t\,(1-t^2)^{\lambda-1/2}\, dt = 2\lambda \cdot \frac{1}{2\lambda+1} = \frac{2\lambda}{2\lambda+1} > 0$. ✓
- **$\ell = 3$:** $C_3^\lambda(t) = \frac{2\lambda(\lambda+1)}{3}\,(4t^3 - 3t)\cdot\frac{3}{2\lambda+2}\cdots$; direct computation gives $I_3 = -\frac{\lambda(\lambda+1)}{3(\lambda + 3/2)} < 0$, matching $(-1)^{(3-1)/2} = -1$. ✓

---

## Step 5: Completion of the proof ($n \geq 3$)

From Step 4, $\lambda_\ell = \frac{2\,|S^{n-2}|}{C_\ell^\lambda(1)}\, I_\ell \neq 0$ for every odd $\ell \geq 1$ (note $C_\ell^\lambda(1) > 0$). The condition $\mathcal{H}[h] = 0$ gives $\lambda_\ell\, a_\ell^m = 0$ for all odd $\ell$, all $m$, forcing $a_\ell^m = 0$ for all coefficients. Since $h$ is odd, it has no even-degree component, so

$$h \equiv 0.$$

Therefore $g(\theta) = g(-\theta)$ for all $\theta$, i.e. $\rho(\theta)^n = \rho(-\theta)^n$, and since $\rho \geq 0$,

$$\rho(\theta) = \rho(-\theta) \qquad \forall\, \theta \in S^{n-1}.$$

Now $x \in U \iff x = r\theta$ with $0 \leq r < \rho(\theta)$ for some $\theta \in S^{n-1}$. Then $-x = r(-\theta)$ with $0 \leq r < \rho(\theta) = \rho(-\theta)$, so $-x \in U$. Hence $U = -U$.

---

## Conclusion

For every $n \geq 1$, a bounded open convex set $U \subset \mathbb{R}^n$ that is bisected by every hyperplane through the origin must satisfy $U = -U$.

$$\boxed{U = -U}$$

### PROOF COMPLETE
