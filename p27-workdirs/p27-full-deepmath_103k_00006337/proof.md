# Proof that $\mu = \mu'$

## Setup

Let $r = d\mu'/d\mu$ be the Radon–Nikodym derivative. Since both $\mu$ and $\mu'$ assign measure $0$ to all and only $\lambda$-null sets, we have $\mu \sim \lambda$ and $\mu' \sim \lambda$, hence $\mu \sim \mu'$. Thus $r$ exists, is positive $\mu$-a.e., and satisfies $\int_0^1 r\,d\mu = \mu'([0,1]) = 1$.

Both $\mu$ and $\mu'$ are non-atomic (since $\lambda$ is, and $\mu \sim \lambda$).

**Interpretation of $\mu_X$.** We interpret $\mu_X$ as the conditional probability measure:
$$\mu_X(A) = \frac{\mu(A \cap X)}{\mu(X)}, \qquad A \in \Sigma.$$
This is the only interpretation under which the hypothesis is non-vacuous: if $\mu_X$ were the restricted measure $\mu|_X$, then $\mu_X(X) = \mu(X)$ and $\mu_{\overline{X}}(\overline{X}) = \mu(\overline{X})$ would need to be equal for a measure-preserving bijection to exist, forcing $\mu(X) = 1/2$ for all $X$—impossible for a non-atomic measure.

## Step 1: Pushforward conditions

For a partition $X, \overline{X} = [0,1]\setminus X$ with $0 < \lambda(X) < 1$, the hypothesis gives a measurable $f: X \to \overline{X}$ with $f_*(\mu_X) = \mu_{\overline{X}}$ and $f_*(\mu'_X) = \mu'_{\overline{X}}$.

Since $\mu_X = \mu|_X / \mu(X)$ and $\mu_{\overline{X}} = \mu|_{\overline{X}} / \mu(\overline{X})$, the first condition becomes:
$$f_*(\mu|_X) = \frac{\mu(X)}{\mu(\overline{X})}\,\mu|_{\overline{X}} = \alpha\,\mu|_{\overline{X}}, \qquad \alpha := \frac{\mu(X)}{\mu(\overline{X})}.$$

Similarly, writing $\beta := \mu'(X)/\mu'(\overline{X})$:
$$f_*(\mu'|_X) = \beta\,\mu'|_{\overline{X}}.$$

Since $\mu' = r\,\mu$, we have $\mu'|_X = r|_X \cdot \mu|_X$ and $\mu'|_{\overline{X}} = r|_{\overline{X}} \cdot \mu|_{\overline{X}}$.

## Step 2: Conditional expectation relation

The Radon–Nikodym derivative of $f_*(r|_X \cdot \mu|_X)$ with respect to $f_*(\mu|_X)$ is the conditional expectation $E_{\mu|_X}[r \mid f = y]$. The Radon–Nikodym derivative of $\beta\, r|_{\overline{X}} \cdot \mu|_{\overline{X}}$ with respect to $\alpha\, \mu|_{\overline{X}}$ is $(\beta/\alpha)\,r(y)$.

Since $f_*(r|_X \cdot \mu|_X) = \beta\, r|_{\overline{X}} \cdot \mu|_{\overline{X}}$ and $f_*(\mu|_X) = \alpha\, \mu|_{\overline{X}}$:

$$\boxed{E_{\mu|_X}[r \mid f = y] = \frac{\beta}{\alpha}\,r(y) \quad \text{for } \mu\text{-a.e. } y \in \overline{X}.} \tag{1}$$

## Step 3: Jensen's inequality

By Jensen's inequality for conditional expectations, $E[r^2 \mid f = y] \geq (E[r \mid f = y])^2$. Using (1):

$$E[r^2 \mid f = y] \geq \left(\frac{\beta}{\alpha}\right)^2 r(y)^2.$$

Integrating against $f_*(\mu|_X) = \alpha\,\mu|_{\overline{X}}$:

$$\int_X r^2\,d\mu = \alpha\int_{\overline{X}} E[r^2 \mid f=y]\,d\mu(y) \geq \alpha\left(\frac{\beta}{\alpha}\right)^2 \int_{\overline{X}} r^2\,d\mu = \frac{\beta^2}{\alpha}\int_{\overline{X}} r^2\,d\mu. \tag{$\star$}$$

## Step 4: Symmetry forces equality

Set $A := \int_0^1 r^2\,d\mu$, $S_X := \int_X r^2\,d\mu$, $S_{\overline{X}} := A - S_X$.

Inequality $(\star)$ reads $S_X \geq \frac{\beta^2}{\alpha}\,S_{\overline{X}}$, i.e.,
$$S_X \geq \frac{\beta^2}{\alpha + \beta^2}\,A. \tag{2}$$

Applying the same argument to the swapped partition $\overline{X}, X$ (which also satisfies $0 < \lambda(\overline{X}) < 1$), with $\alpha' = 1/\alpha$, $\beta' = 1/\beta$:
$$S_{\overline{X}} \geq \frac{\alpha}{\beta^2}\,S_X \implies S_X \leq \frac{\beta^2}{\alpha + \beta^2}\,A. \tag{3}$$

Combining (2) and (3):

$$\boxed{S_X = A \cdot \frac{\beta^2}{\alpha + \beta^2} = A \cdot \frac{\mu'(X)^2\,\mu(\overline{X})}{\mu'(\overline{X})^2\,\mu(X) + \mu'(X)^2\,\mu(\overline{X})}} \tag{$\star\star\star$}$$

for **every** $X \in \Sigma$ with $0 < \lambda(X) < 1$.

**Equality in Jensen** means $r$ is $\sigma(f)$-measurable (constant on $f$-fibers) for each such $X$.

## Step 5: $A$ is finite

If $A = \infty$, then ($\star\star\star$) gives $S_X = \infty$ for every $X$ with $0 < \mu(X) < 1$. But for $X_N := \{r \leq N\}$ (which has $0 < \mu(X_N) < 1$ for suitable $N$ since $r < \infty$ a.e. and $\int r\,d\mu = 1$):
$$S_{X_N} = \int_{\{r \leq N\}} r^2\,d\mu \leq N\int_{\{r \leq N\}} r\,d\mu \leq N < \infty,$$
contradicting $S_{X_N} = \infty$. Hence $A < \infty$, i.e., $r \in L^2(\mu)$.

## Step 6: Shrinking to a point — proving $A = 1$

Fix $x_0 \in (0,1)$ and let $X_n = (x_0 - 1/n,\, x_0 + 1/n) \cap [0,1]$ for $n$ large enough that $0 < \lambda(X_n) < 1$.

Set $p_n = \mu(X_n) \to 0$, $m_n = \mu'(X_n) \to 0$. By the Lebesgue differentiation theorem (applied to the Radon measure $\mu \sim \lambda$), for $\mu$-a.e. $x_0$:
$$\frac{m_n}{p_n} = \frac{\int_{X_n} r\,d\mu}{\mu(X_n)} \to r(x_0), \qquad \frac{S_{X_n}}{p_n} = \frac{\int_{X_n} r^2\,d\mu}{\mu(X_n)} \to r(x_0)^2.$$

Also $\mu(\overline{X_n}) \to 1$ and $\mu'(\overline{X_n}) \to 1$.

From ($\star\star\star$), dividing both sides by $p_n$:
$$\frac{S_{X_n}}{p_n} = A \cdot \frac{(m_n/p_n)^2\,(1 - p_n)}{(1 - m_n)^2 + (m_n/p_n)^2\,p_n\,(1 - p_n)}.$$

As $n \to \infty$: the numerator $\to r(x_0)^2 \cdot 1$; the denominator $\to 1 + r(x_0)^2 \cdot 0 \cdot 1 = 1$. So:
$$r(x_0)^2 = A \cdot r(x_0)^2.$$

Since $r(x_0) > 0$ for $\mu$-a.e. $x_0$, we conclude:
$$\boxed{A = \int_0^1 r^2\,d\mu = 1.}$$

## Step 7: Conclusion

We have:
- $\int_0^1 r\,d\mu = 1$ (since $\mu'$ is a probability measure),
- $\int_0^1 r^2\,d\mu = 1$ (from Step 6).

Therefore:
$$\int_0^1 (r - 1)^2\,d\mu = \int_0^1 r^2\,d\mu - 2\int_0^1 r\,d\mu + \int_0^1 1\,d\mu = 1 - 2 + 1 = 0.$$

Since $(r-1)^2 \geq 0$ and $\int (r-1)^2\,d\mu = 0$, we get $r = 1$ $\mu$-a.e., hence $\mu' = \mu$.

$$\boxed{\mu = \mu'}$$

### PROOF COMPLETE
