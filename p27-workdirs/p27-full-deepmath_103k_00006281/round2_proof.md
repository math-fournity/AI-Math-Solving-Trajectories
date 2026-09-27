# Supremum of $f(x)/g(x)$

## Setup

Let
$$
G(x) := \int_{-\infty}^{x} \exp\!\left(-\frac{(t-\mu)^2}{2\sigma^2}\right) dt
\qquad\text{(unnormalized Gaussian CDF, dummy variable } t\text{)}.
$$

Then the given function is
$$
f(x) = \frac{\beta\, e^{-\beta x}\, G(x)}{\displaystyle\int_{-\infty}^{\infty}\beta\, e^{-\beta x}\,dx \;\cdot\; G(x)}.
$$

## Step 1 — The Gaussian factor cancels

The factor $G(x)$ appears **identically** in the numerator and in the denominator (both are $\int_{-\infty}^{x} e^{-(t-\mu)^2/(2\sigma^2)}\,dt$, with the same upper limit $x$ and the same integrand). For all $x$ where $G(x)>0$ (which holds for every finite $x$ since the Gaussian integrand is strictly positive), we may cancel:

$$
f(x) = \frac{\beta\, e^{-\beta x}}{\displaystyle\int_{-\infty}^{\infty}\beta\, e^{-\beta x}\,dx}.
$$

The parameters $\mu, \sigma$ disappear entirely — they only appeared inside the canceling factor.

## Step 2 — Normalization of the exponential

The integral $\int_{-\infty}^{\infty} \beta\, e^{-\beta x}\,dx$ converges only when the exponential is supported on $[0,\infty)$ (the standard exponential distribution with rate $\beta>0$):

$$
\int_{0}^{\infty} \beta\, e^{-\beta x}\,dx = 1.
$$

Hence $f(x) = \beta\, e^{-\beta x}$ for $x \in [0,\infty)$ (and $f(x)=0$ for $x<0$). This is exactly the $\mathrm{Exp}(\beta)$ density.

## Step 3 — Form the ratio

With $g(x) = e^{-x}$, on the support $[0,\infty)$:

$$
\frac{f(x)}{g(x)} = \frac{\beta\, e^{-\beta x}}{e^{-x}} = \beta\, e^{(1-\beta)x}, \qquad x \ge 0.
$$

## Step 4 — Take the supremum

Let $h(x) = \beta\, e^{(1-\beta)x}$ on $[0,\infty)$.

- **If $\beta \ge 1$:** then $(1-\beta)\le 0$, so $h$ is non-increasing. The maximum is attained at $x=0$:
  $$
  \sup_{x\ge 0} h(x) = h(0) = \beta.
  $$

- **If $\beta < 1$:** then $(1-\beta)>0$, so $h(x)\to\infty$ as $x\to\infty$, and the supremum is $+\infty$.

For the problem to have a finite supremum we require $\beta \ge 1$.

## Conclusion

$$
\boxed{\sup_{x}\frac{f(x)}{g(x)} = \beta}
$$

(assuming $\beta \ge 1$; the Gaussian parameters $\mu,\sigma$ cancel and do not affect the result).
