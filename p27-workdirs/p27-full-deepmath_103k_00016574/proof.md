# Proof: Asymptotic expansion of $k\log x$ where $p_K(x) = \frac{1}{2}$

## Interpretation of $p_K$

We interpret $p_K(x) = x^K$, which is the cumulative distribution function of $M_K = \max(U_1, \dots, U_K)$, the maximum of $K$ independent $\mathrm{Uniform}(0,1)$ random variables. This is the standard notation in extreme value theory and order statistics, where $p_K$ denotes the CDF of the $K$-th order statistic (here the maximum).

## Solving $p_K(x) = \frac{1}{2}$

The equation $x^K = \frac{1}{2}$ gives the median of $M_K$:

$$x = 2^{-1/K} = e^{-\frac{\log 2}{K}}.$$

## Asymptotic expansion of $K \log x$

Substituting:

$$K \log x = K \log\!\left(e^{-\frac{\log 2}{K}}\right) = K \cdot \left(-\frac{\log 2}{K}\right) = -\log 2.$$

This holds **exactly** for every $K \geq 1$. Expanding $x$ in powers of $1/K$:

$$x = e^{-\frac{\log 2}{K}} = 1 - \frac{\log 2}{K} + \frac{(\log 2)^2}{2K^2} - \frac{(\log 2)^3}{6K^3} + \cdots,$$

so

$$K \log x = -\log 2 + \frac{(\log 2)^2}{2K} \cdot 0 + \cdots$$

More precisely, $\log x = -\frac{\log 2}{K}$ exactly, so:

$$K \log x = -\log 2 + 0 \cdot \frac{1}{K} + 0 \cdot \frac{1}{K^2} + \cdots$$

The asymptotic expansion is simply:

$$K \log x \sim -\log 2 \quad \text{as } K \to \infty.$$

## The constant coefficient

The asymptotic expansion of $K\log x$ as $K \to \infty$ is:

$$K \log x = c_0 + \frac{c_1}{K} + \frac{c_2}{K^2} + \cdots$$

where the **constant coefficient** (the $K^0$ term) is:

$$c_0 = -\log 2 \approx -0.6931.$$

## Answer

$$\boxed{-\log 2}$$

### PROOF COMPLETE
