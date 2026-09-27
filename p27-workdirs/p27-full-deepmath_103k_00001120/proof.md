# Proof

## Problem Statement

Let $(x_n)$ be a monotonically decreasing sequence of positive real numbers that is summable. Let $(y_n)$ be a sequence of positive real numbers such that $\sum_n x_n y_n$ converges. Let $(z_n)$ be a monotonically increasing sequence of positive real numbers such that $\sum_n x_n z_n = \infty$. Assume that the sequences $y_n$ and $z_n$ are such that $2^{-\varepsilon y_n}$ and $2^{-\varepsilon z_n}$ are summable for every $\varepsilon > 0$.

**Question:** Does it follow that there exists a sequence $(w_n)$ with $y_n \leq w_n \leq z_n$ for all $n$ such that $\sum x_n w_n$ converges and $2^{-\varepsilon w_n}$ is summable for every $\varepsilon > 0$?

## Answer

$$\boxed{Yes}$$

## Proof

We construct $w_n$ explicitly and verify all required properties.

### Construction

Define
$$w_n = \min(y_n, z_n) \quad \text{for all } n \geq 1.$$

### Verification

We verify that $w_n$ satisfies all the required properties.

**Property 1: $w_n \leq z_n$ for all $n$.**

By definition, $w_n = \min(y_n, z_n) \leq z_n$ for every $n$.

**Property 2: $\sum_{n=1}^{\infty} x_n w_n < \infty$ (convergence).**

Since $w_n = \min(y_n, z_n) \leq y_n$ and $x_n > 0$ for all $n$:
$$\sum_{n=1}^{\infty} x_n w_n \leq \sum_{n=1}^{\infty} x_n y_n < \infty,$$
where the last inequality holds by assumption.

**Property 3: $\sum_{n=1}^{\infty} 2^{-\varepsilon w_n} < \infty$ for every $\varepsilon > 0$ (exponential summability).**

Since $w_n = \min(y_n, z_n)$, we have:
$$2^{-\varepsilon w_n} = 2^{-\varepsilon \min(y_n, z_n)} = \max\!\left(2^{-\varepsilon y_n},\; 2^{-\varepsilon z_n}\right).$$

Using the elementary inequality $\max(a, b) \leq a + b$ for non-negative $a, b$:
$$2^{-\varepsilon w_n} = \max\!\left(2^{-\varepsilon y_n},\; 2^{-\varepsilon z_n}\right) \leq 2^{-\varepsilon y_n} + 2^{-\varepsilon z_n}.$$

Summing over all $n$:
$$\sum_{n=1}^{\infty} 2^{-\varepsilon w_n} \leq \sum_{n=1}^{\infty} 2^{-\varepsilon y_n} + \sum_{n=1}^{\infty} 2^{-\varepsilon z_n} < \infty,$$
where both series on the right are finite by the assumption that $2^{-\varepsilon y_n}$ and $2^{-\varepsilon z_n}$ are summable for every $\varepsilon > 0$.

### Conclusion

The sequence $w_n = \min(y_n, z_n)$ satisfies:
- $w_n \leq z_n$ for all $n$ (bounded above by the divergent weight),
- $\sum x_n w_n \leq \sum x_n y_n < \infty$ (convergence, since $w_n \leq y_n$),
- $\sum 2^{-\varepsilon w_n} \leq \sum 2^{-\varepsilon y_n} + \sum 2^{-\varepsilon z_n} < \infty$ for every $\varepsilon > 0$ (exponential summability).

The key idea is that the pointwise minimum of $y_n$ and $z_n$ inherits the convergence property from $y_n$ (since $w_n \leq y_n$ implies $\sum x_n w_n \leq \sum x_n y_n$) and the exponential summability from both sequences (since $2^{-\varepsilon \min(y_n, z_n)} = \max(2^{-\varepsilon y_n}, 2^{-\varepsilon z_n})$ is controlled by the sum of two summable sequences).

Therefore, such a sequence $(w_n)$ exists. $\blacksquare$
