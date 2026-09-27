# Proof: The condition does not imply $g(x) = x$ a.e.

## Answer

$$\boxed{\text{No}}$$

The condition $\int_0^\infty g(ax)\,f(x)\,dx = a$ for all $a > 0$ does **not** imply $g(x) = x$ almost everywhere. We construct an explicit counterexample.

---

## Setup and Key Transformation

Given $f > 0$ with $\int_0^\infty f(x)\,dx = 1$ and $\int_0^\infty x\,f(x)\,dx = 1$, and $g \geq 0$ nonconstant with $\int_0^\infty g(ax)\,f(x)\,dx = a$ for all $a > 0$.

**Substitution.** In the condition $\int_0^\infty g(ax)\,f(x)\,dx = a$, let $u = ax$:

$$\frac{1}{a}\int_0^\infty g(u)\,f(u/a)\,du = a \quad\Longrightarrow\quad \int_0^\infty g(u)\,f(u/a)\,du = a^2. \tag{1}$$

Now set $u = e^v$, $a = e^s$, and define $\tilde{f}(v) = f(e^v)\,e^v$ (a probability density on $\mathbb{R}$ since $\int \tilde{f} = 1$). Then (1) becomes:

$$\int_{-\infty}^{\infty} g(e^v)\,f(e^{v-s})\,e^v\,dv = e^{2s}.$$

Since $f(e^{v-s}) = \tilde{f}(v-s)\,e^{s-v}$, this simplifies to:

$$\int_{-\infty}^{\infty} \bar{g}(v+s)\,\tilde{f}(v)\,dv = e^s, \tag{2}$$

where $\bar{g}(v) = g(e^v)$. Equation (2) is a cross-correlation. Defining $\tilde{f}^-(w) = \tilde{f}(-w)$, it becomes the **convolution equation**:

$$(\bar{g} * \tilde{f}^-)(s) = e^s \quad \text{for all } s \in \mathbb{R}. \tag{3}$$

---

## Particular Solution: $g(x) = x$

If $g(x) = x$, then $\bar{g}(v) = e^v$, and:

$$(\bar{g} * \tilde{f}^-)(s) = \int e^{s-w}\,\tilde{f}(-w)\,dw = e^s \int e^{-w}\,\tilde{f}(-w)\,dw = e^s \int e^v\,\tilde{f}(v)\,dv = e^s \int_0^\infty x\,f(x)\,dx = e^s. \quad\checkmark$$

---

## Finding Other Solutions

Write $\bar{g}(v) = e^v + h(v)$. Substituting into (3) and using the particular solution:

$$(h * \tilde{f}^-)(s) = 0 \quad \text{for all } s. \tag{4}$$

**Mellin transform condition.** Taking Fourier transforms of (4) (in the sense of distributions / for suitable $h$):

$$\hat{h}(\omega) \cdot \widehat{\tilde{f}^-}(\omega) = 0.$$

Since $\widehat{\tilde{f}^-}(\omega) = \overline{\hat{\tilde{f}}(\omega)}$ and $\hat{\tilde{f}}(\omega) = \int_0^\infty x^{-i\omega}\,f(x)\,dx = \hat{f}(1-i\omega)$ (Mellin transform of $f$), a nonzero $h$ exists when $\hat{f}(1-i\omega_0) = 0$ for some $\omega_0 \neq 0$.

**Choosing $h$.** Try $h(v) = \epsilon\, e^v \cos(\omega_0 v)$ for small $\epsilon > 0$, giving:

$$g(x) = x\bigl(1 + \epsilon \cos(\omega_0 \ln x)\bigr). \tag{5}$$

**Direct verification.** We compute $\int_0^\infty g(ax)\,f(x)\,dx$:

$$= a\underbrace{\int_0^\infty x\,f(x)\,dx}_{=\,1} + \epsilon a \int_0^\infty x\cos(\omega_0 \ln(ax))\,f(x)\,dx.$$

Expanding $\cos(\omega_0 \ln a + \omega_0 \ln x)$:

$$= a + \epsilon a\Bigl[\cos(\omega_0 \ln a)\,\operatorname{Re}\hat{f}(2{+}i\omega_0) - \sin(\omega_0 \ln a)\,\operatorname{Im}\hat{f}(2{+}i\omega_0)\Bigr].$$

For this to equal $a$ for **all** $a > 0$, we need $\hat{f}(2 + i\omega_0) = 0$.

**Reconciling with the convolution approach.** With $h(v) = \epsilon e^v \cos(\omega_0 v)$:

$$(h * \tilde{f}^-)(s) = \epsilon e^s \int e^{-w}\cos(\omega_0(s{-}w))\,\tilde{f}(-w)\,dw.$$

The integral $\int e^{-w} e^{i\omega_0 w}\tilde{f}(-w)\,dw = \int e^v e^{-i\omega_0 v}\tilde{f}(v)\,dv = \hat{f}(2 - i\omega_0)$.

So the correct condition from both approaches is:

$$\boxed{\hat{f}(2 + i\omega_0) = 0 \quad \text{for some } \omega_0 \neq 0.} \tag{$\star$}$$

---

## Constructing $f$ Satisfying $(\star)$

We need a strictly positive $f$ with $\int f = 1$, $\int x f = 1$, and $\hat{f}(2+i\omega_0) = 0$ for some $\omega_0 \neq 0$.

**Construction.** Let $\tilde{f}(v) = f(e^v)\,e^v = C\bigl(\alpha_1\, e^{-(v-b_1)^2} + \alpha_2\, e^{-(v-b_2)^2}\bigr)$ with $\alpha_1, \alpha_2 > 0$ and $b_1 \neq b_2$. This is strictly positive (sum of positive Gaussians).

**Mellin transform computation.**

$$\hat{f}(2+i\omega) = \int e^{(1+i\omega)v}\,\tilde{f}(v)\,dv = C\sqrt{\pi}\,e^{1/4 - \omega^2/4}\,e^{i\omega/2}\bigl[\alpha_1 e^{b_1}\,e^{i\omega b_1} + \alpha_2 e^{b_2}\,e^{i\omega b_2}\bigr].$$

Setting $\alpha_1 e^{b_1} = \alpha_2 e^{b_2} = K$ (equal weights in the Mellin domain):

$$\hat{f}(2+i\omega) = C\sqrt{\pi}\,e^{1/4-\omega^2/4}\,e^{i\omega/2}\,K \cdot 2\,e^{i\omega(b_1+b_2)/2}\cos\!\Bigl(\frac{\omega(b_1 - b_2)}{2}\Bigr).$$

This vanishes when $\omega(b_1 - b_2)/2 = \pi/2 + k\pi$, i.e., $\omega_0 = \frac{(2k+1)\pi}{b_1 - b_2} \neq 0$. $\checkmark$

**Normalization.** $\int \tilde{f}\,dv = C\sqrt{\pi}(\alpha_1 + \alpha_2) = 1$, so $C = \frac{1}{\sqrt{\pi}(\alpha_1 + \alpha_2)}$.

**Mean condition.** $\int e^v \tilde{f}(v)\,dv = C\sqrt{\pi}\,e^{1/4}(\alpha_1 e^{b_1} + \alpha_2 e^{b_2}) = \frac{e^{1/4} \cdot 2K}{\alpha_1 + \alpha_2} = 1$.

With $\alpha_j = K e^{-b_j}$, we get $\alpha_1 + \alpha_2 = K(e^{-b_1} + e^{-b_2})$, so the mean condition becomes:

$$e^{-b_1} + e^{-b_2} = 2\,e^{1/4}. \tag{6}$$

**Solving (6) with $b_1 \neq b_2$.** Set $b_1 = 0$: then $e^{-b_2} = 2e^{1/4} - 1 \approx 1.568$, giving $b_2 = -\ln(2e^{1/4}-1) \approx -0.449 \neq 0 = b_1$. $\checkmark$

With this choice:
- $f$ is strictly positive (sum of Gaussians). $\checkmark$
- $\int_0^\infty f(x)\,dx = 1$. $\checkmark$
- $\int_0^\infty x\,f(x)\,dx = 1$. $\checkmark$
- $\hat{f}(2 + i\omega_0) = 0$ for $\omega_0 = \frac{\pi}{b_1 - b_2} \neq 0$. $\checkmark$

---

## The Counterexample

With the $f$ constructed above and $\omega_0 = \pi/(b_1 - b_2)$, define for any $0 < \epsilon \leq 1$:

$$g(x) = x\bigl(1 + \epsilon\cos(\omega_0 \ln x)\bigr), \quad x > 0.$$

**Verification of all conditions:**

1. **$g \geq 0$:** Since $x > 0$ and $1 + \epsilon\cos(\cdot) \geq 1 - \epsilon \geq 0$. $\checkmark$

2. **$g$ nonconstant:** $\epsilon > 0$ and $\cos(\omega_0 \ln x)$ is not identically zero. $\checkmark$

3. **$g \neq x$ a.e.:** $g(x) - x = \epsilon\, x\cos(\omega_0 \ln x)$, which is nonzero on a set of positive measure. $\checkmark$

4. **Integral condition:** As computed above,

$$\int_0^\infty g(ax)\,f(x)\,dx = a + \epsilon a\Bigl[\cos(\omega_0 \ln a)\,\operatorname{Re}\hat{f}(2{+}i\omega_0) - \sin(\omega_0 \ln a)\,\operatorname{Im}\hat{f}(2{+}i\omega_0)\Bigr] = a + 0 = a,$$

since $\hat{f}(2+i\omega_0) = 0$. $\checkmark$

5. **Convergence:** $|g(ax)| \leq ax(1+\epsilon)$ and $\int_0^\infty x\,f(x)\,dx = 1 < \infty$, so the integral converges. $\checkmark$

---

## Conclusion

We have constructed a strictly positive probability density $f$ with mean $1$ and a nonnegative nonconstant function $g \neq x$ such that $\int_0^\infty g(ax)\,f(x)\,dx = a$ for all $a > 0$. Therefore, the condition does **not** imply $g(x) = x$ almost everywhere.

$$\boxed{\text{No}}$$

---

## Remark: When Uniqueness Does Hold

For certain special choices of $f$, the solution **is** unique. For example, if $f(x) = e^{-x}$ (exponential distribution), the condition becomes the Laplace transform equation $\mathcal{L}[g](1/a) = a^2$, i.e., $\mathcal{L}[g](s) = 1/s^2$. By uniqueness of the Laplace transform, $g(x) = x$ a.e. is the only solution. This corresponds to $\hat{f}(2+i\omega) = \Gamma(2+i\omega) \neq 0$ for all real $\omega$ (the Gamma function has no zeros), so condition $(\star)$ is never satisfied.

The key insight is that uniqueness holds if and only if the Mellin transform $\hat{f}(2 + i\omega)$ has **no real zeros** — a condition that fails for general $f$ but holds for specific densities like the exponential.
