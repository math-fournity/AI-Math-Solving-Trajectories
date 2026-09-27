# Proof

**Answer: Yes, $f$ has a (unique) fixed point.**

## Key consequence of the $\alpha$ condition

The hypothesis "$\alpha(t_n) \to 1 \Rightarrow t_n \to 0$" is equivalent to:

$$\forall \varepsilon > 0, \quad \rho_\varepsilon := \sup_{t \geq \varepsilon} \alpha(t) < 1.$$

Indeed, if $\sup_{t \geq \varepsilon} \alpha(t) = 1$ for some $\varepsilon > 0$, we could find a sequence $t_n \geq \varepsilon$ with $\alpha(t_n) \to 1$, but $t_n \geq \varepsilon > 0$ so $t_n \not\to 0$, contradicting the hypothesis.

## Step 1: Picard iteration and $d_n \to 0$

Pick $x_0 \in X$ and define $x_{n+1} = f(x_n)$. Let $d_n = d(x_n, x_{n+1})$. If $d_n = 0$ for some $n$, then $x_n$ is a fixed point and we are done. Assume $d_n > 0$ for all $n$.

Since $\alpha(d_n) < 1$, we have $d_{n+1} \leq \alpha(d_n)\, d_n < d_n$, so $\{d_n\}$ is strictly decreasing and bounded below by $0$, hence converges to some $L \geq 0$.

If $L > 0$, then $d_n \geq L$ for all $n$, so $\alpha(d_n) \leq \rho_L < 1$, giving $d_{n+1} \leq \rho_L\, d_n$, hence $d_n \leq \rho_L^n\, d_0 \to 0$ — contradicting $L > 0$. Therefore $L = 0$.

## Step 2: $\{x_n\}$ is Cauchy

Suppose for contradiction that $\{x_n\}$ is not Cauchy. Then there exists $\varepsilon > 0$ such that for every $N$, there exist $m > n \geq N$ with $d(x_n, x_m) \geq \varepsilon$.

Construct subsequences $\{n_k\}, \{m_k\}$ as follows. For each $k$, choose $n_k \geq k$ and let $m_k > n_k$ be the **smallest** index such that $d(x_{n_k}, x_{m_k}) \geq \varepsilon$. Then:

$$d(x_{n_k}, x_{m_k - 1}) < \varepsilon.$$

By the triangle inequality:

$$d(x_{n_k}, x_{m_k}) \leq d(x_{n_k}, x_{m_k - 1}) + d(x_{m_k - 1}, x_{m_k}) < \varepsilon + d_{m_k - 1}.$$

Since $d_n \to 0$ and $m_k \to \infty$ (as $n_k \to \infty$ forces $m_k \to \infty$), we have $d_{m_k - 1} \to 0$, so:

$$\lim_{k \to \infty} d(x_{n_k}, x_{m_k}) = \varepsilon. \tag{1}$$

Now apply the contractive property. Since $d(x_{n_k}, x_{m_k}) \geq \varepsilon$, we have $\alpha(d(x_{n_k}, x_{m_k})) \leq \rho_\varepsilon < 1$, so:

$$d(x_{n_k + 1}, x_{m_k + 1}) \leq \alpha(d(x_{n_k}, x_{m_k})) \cdot d(x_{n_k}, x_{m_k}) \leq \rho_\varepsilon \cdot d(x_{n_k}, x_{m_k}).$$

Taking limsup and using (1):

$$\limsup_{k \to \infty} d(x_{n_k + 1}, x_{m_k + 1}) \leq \rho_\varepsilon \cdot \varepsilon < \varepsilon. \tag{2}$$

On the other hand, by the triangle inequality:

$$d(x_{n_k + 1}, x_{m_k + 1}) \geq d(x_{n_k}, x_{m_k}) - d(x_{n_k}, x_{n_k + 1}) - d(x_{m_k}, x_{m_k + 1}) = d(x_{n_k}, x_{m_k}) - d_{n_k} - d_{m_k}.$$

Since $d_{n_k} \to 0$ and $d_{m_k} \to 0$, taking liminf and using (1):

$$\liminf_{k \to \infty} d(x_{n_k + 1}, x_{m_k + 1}) \geq \varepsilon - 0 - 0 = \varepsilon. \tag{3}$$

Combining (2) and (3):

$$\varepsilon \leq \liminf \leq \limsup \leq \rho_\varepsilon \cdot \varepsilon < \varepsilon,$$

a contradiction. Therefore $\{x_n\}$ is Cauchy.

## Step 3: Existence of the fixed point

Since $X$ is complete and $\{x_n\}$ is Cauchy, there exists $x^* \in X$ with $x_n \to x^*$.

The map $f$ is continuous because it is $1$-Lipschitz:

$$d(f(x), f(y)) \leq \alpha(d(x, y))\, d(x, y) \leq d(x, y).$$

By continuity, $f(x_n) \to f(x^*)$. But $f(x_n) = x_{n+1} \to x^*$. By uniqueness of limits, $f(x^*) = x^*$.

## Step 4: Uniqueness

Suppose $x^*, y^* \in X$ are both fixed points. If $d(x^*, y^*) > 0$, then:

$$d(x^*, y^*) = d(f(x^*), f(y^*)) \leq \alpha(d(x^*, y^*))\, d(x^*, y^*) < d(x^*, y^*),$$

a contradiction. Hence $d(x^*, y^*) = 0$, i.e., $x^* = y^*$.

## Conclusion

$f$ has a unique fixed point.

$$\boxed{\text{Yes, } f \text{ has a (unique) fixed point.}}$$

### PROOF COMPLETE
