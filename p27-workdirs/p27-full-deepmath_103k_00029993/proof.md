# Proof: Expectation Convergence for Positive Recurrent Chains with Finite Invariant Mean

## Answer

$$\boxed{NO}$$

There is **no** irreducible, aperiodic, positive recurrent Markov chain on $\mathbb{N}$ with finite invariant mean $E_\mu[X] < \infty$ for which $E_{k_0}[M_n]$ fails to converge to $E_\mu[X]$. For every such chain and every initial state $k_0$, we have $E_{k_0}[M_n] \to E_\mu[X]$.

## Proof

### Setup

Let $(M_n)_{n \geq 0}$ be an irreducible, aperiodic, positive recurrent Markov chain on $\mathbb{N} = \{0, 1, 2, \ldots\}$ with transition matrix $P$ and unique invariant distribution $\mu = (\mu_k)_{k \geq 0}$. Assume $E_\mu[X] = \sum_{k=0}^\infty k\,\mu_k < \infty$. Fix any initial state $k_0 \in \mathbb{N}$.

### Step 1: Renewal Decomposition at $k_0$

Let $T_{k_0} = \inf\{n \geq 1 : M_n = k_0\}$ be the first return time to $k_0$. Define:

- $u_n := P^n(k_0, k_0) = P_{k_0}(M_n = k_0)$ — the $n$-step return probability.
- $g(t) := E_{k_0}\!\bigl[M_t \cdot \mathbf{1}_{\{T_{k_0} > t\}}\bigr]$ for $t \geq 1$ — the expected state at time $t$ during an excursion from $k_0$.

By the **renewal decomposition** (conditioning on the last visit to $k_0$ before or at time $n$), for any $k \neq k_0$:

$$P^n(k_0, k) = \sum_{t=1}^{n} u_{n-t} \cdot q_t(k), \qquad q_t(k) := P_{k_0}(M_t = k,\; T_{k_0} > t).$$

Since $T_{k_0} > t$ implies $M_t \neq k_0$, we have $q_t(k_0) = 0$ for $t \geq 1$. Therefore:

$$E_{k_0}[M_n] = \sum_{k=0}^{\infty} k\, P^n(k_0, k) = k_0\, u_n + \sum_{t=1}^{n} u_{n-t} \cdot g(t). \tag{1}$$

### Step 2: Convergence of Return Probabilities

By the **Markov chain convergence theorem** (irreducibility + aperiodicity + positive recurrence):

$$u_n = P^n(k_0, k_0) \longrightarrow \mu_{k_0} = \frac{1}{E_{k_0}[T_{k_0}]} > 0. \tag{2}$$

In particular, $(u_n)$ is bounded: $0 \leq u_n \leq 1$.

### Step 3: Integrability of the Excursion Profile (Kac's Formula)

By **Kac's formula** (the cycle formula for positive recurrent chains), for any non-negative function $f$:

$$E_{k_0}\!\left[\sum_{t=1}^{T_{k_0}} f(M_t)\right] = \frac{E_\mu[f]}{\mu_{k_0}}.$$

Applying this with $f(k) = k$ and using $E_\mu[X] < \infty$:

$$E_{k_0}\!\left[\sum_{t=1}^{T_{k_0}} M_t\right] = \frac{E_\mu[X]}{\mu_{k_0}} < \infty. \tag{3}$$

Now decompose the cycle sum. Since $\mathbf{1}_{\{T_{k_0} \geq t\}} = \mathbf{1}_{\{T_{k_0} > t-1\}}$ and $M_t = k_0$ when $T_{k_0} = t$:

$$E_{k_0}\!\left[\sum_{t=1}^{T_{k_0}} M_t\right] = \sum_{t=1}^{\infty} E_{k_0}\!\bigl[M_t \cdot \mathbf{1}_{\{T_{k_0} \geq t\}}\bigr] = \sum_{t=1}^{\infty} E_{k_0}\!\bigl[M_t \cdot \mathbf{1}_{\{T_{k_0} > t-1\}}\bigr].$$

For $t \geq 2$, split on whether $T_{k_0} = t-1$ (meaning $M_{t-1} = k_0$ but $M_t$ may or may not be $k_0$) vs $T_{k_0} > t-1$:

$$E_{k_0}\!\bigl[M_t \cdot \mathbf{1}_{\{T_{k_0} > t-1\}}\bigr] = \underbrace{E_{k_0}\!\bigl[M_t \cdot \mathbf{1}_{\{T_{k_0} > t\}}\bigr]}_{= g(t)} + \underbrace{E_{k_0}\!\bigl[M_t \cdot \mathbf{1}_{\{T_{k_0} = t\}}\bigr]}_{= k_0 \cdot P_{k_0}(T_{k_0} = t)}.$$

For $t = 1$: $E_{k_0}[M_1 \cdot \mathbf{1}_{\{T_{k_0} > 0\}}] = E_{k_0}[M_1]$ (since $T_{k_0} \geq 1$ always), and $g(1) = E_{k_0}[M_1 \cdot \mathbf{1}_{\{T_{k_0} > 1\}}]$, and $E_{k_0}[M_1 \cdot \mathbf{1}_{\{T_{k_0} = 1\}}] = k_0 \cdot P_{k_0}(T_{k_0} = 1)$.

Summing over all $t \geq 1$:

$$\frac{E_\mu[X]}{\mu_{k_0}} = \sum_{t=1}^{\infty} g(t) + k_0 \sum_{t=1}^{\infty} P_{k_0}(T_{k_0} = t) = \sum_{t=1}^{\infty} g(t) + k_0. \tag{4}$$

Therefore:

$$\sum_{t=1}^{\infty} g(t) = \frac{E_\mu[X]}{\mu_{k_0}} - k_0 < \infty. \tag{5}$$

Since $M_t \geq 0$ and $\mathbf{1}_{\{T_{k_0} > t\}} \geq 0$, we have $g(t) \geq 0$, so $g \in \ell^1(\mathbb{N})$.

### Step 4: Decomposition of the Deviation

From (1) and the identity $E_\mu[X] = \mu_{k_0}\bigl(\sum_{t=1}^{\infty} g(t) + k_0\bigr)$ (equation (4)):

$$E_{k_0}[M_n] - E_\mu[X] = \underbrace{k_0\bigl(u_n - \mu_{k_0}\bigr)}_{\text{(I)}} + \underbrace{\sum_{t=1}^{n} \bigl(u_{n-t} - \mu_{k_0}\bigr)\, g(t)}_{\text{(II)}} - \underbrace{\mu_{k_0} \sum_{t=n+1}^{\infty} g(t)}_{\text{(III)}}. \tag{6}$$

### Step 5: Each Term Vanishes

**Term (I):** $k_0(u_n - \mu_{k_0}) \to 0$ by (2).

**Term (III):** $\mu_{k_0} \sum_{t=n+1}^{\infty} g(t) \to 0$ because $g \in \ell^1$ by (5) (the tail of a convergent series vanishes).

**Term (II):** This is a discrete convolution $(a * g)(n)$ where $a_s := u_s - \mu_{k_0} \to 0$ (by (2)) and $g \in \ell^1$ (by (5)). We show this convolution vanishes.

**Convolution Lemma.** *If $(a_s)_{s \geq 0}$ is bounded with $a_s \to 0$, and $(g(t))_{t \geq 1} \in \ell^1$, then $\sum_{t=1}^{n} a_{n-t}\, g(t) \to 0$ as $n \to \infty$.*

*Proof of Lemma.* Let $A := \sup_s |a_s| < \infty$ and $G := \sum_{t=1}^{\infty} |g(t)| < \infty$. Split the sum at $t = \lfloor n/2 \rfloor$:

$$\left|\sum_{t=1}^{n} a_{n-t}\, g(t)\right| \leq \underbrace{\sum_{t=1}^{\lfloor n/2 \rfloor} |a_{n-t}|\, |g(t)|}_{\text{(a)}} + \underbrace{\sum_{t=\lfloor n/2 \rfloor + 1}^{n} |a_{n-t}|\, |g(t)|}_{\text{(b)}}.$$

- **(a):** For $t \leq \lfloor n/2 \rfloor$, we have $n - t \geq \lceil n/2 \rceil$, so $|a_{n-t}| \leq \sup_{s \geq \lceil n/2 \rceil} |a_s|$. Thus:
$$\text{(a)} \leq \sup_{s \geq \lceil n/2 \rceil} |a_s| \cdot G \longrightarrow 0 \cdot G = 0,$$
  since $a_s \to 0$.

- **(b):** $|a_{n-t}| \leq A$, so:
$$\text{(b)} \leq A \sum_{t=\lfloor n/2 \rfloor + 1}^{\infty} |g(t)| \longrightarrow A \cdot 0 = 0,$$
  since $g \in \ell^1$ (tail of absolutely convergent series vanishes).

Both parts go to 0, so the convolution vanishes. $\square$

Applying the lemma with $a_s = u_s - \mu_{k_0}$ (bounded by 1, converging to 0 by (2)) and $g$ (in $\ell^1$ by (5)), Term (II) $\to 0$.

### Step 6: Conclusion

All three terms in (6) vanish as $n \to \infty$, so:

$$E_{k_0}[M_n] \longrightarrow E_\mu[X] = \sum_{k=0}^{\infty} k\,\mu_k.$$

This holds for **every** irreducible, aperiodic, positive recurrent Markov chain on $\mathbb{N}$ with finite invariant mean, and for **every** initial state $k_0$. Therefore, no such chain exists for which the convergence fails.

### Why the Intuition "TV Convergence ≠ Unbounded Expectation Convergence" Does Not Apply

It is true in general that total variation convergence $P_n \to \mu$ does not imply $\int f\, dP_n \to \int f\, d\mu$ for unbounded $f$. However, the distributions $P^n(k_0, \cdot)$ are not arbitrary — they are constrained by the **renewal structure** of the Markov chain. Specifically:

1. The renewal decomposition (Step 1) expresses $E_{k_0}[M_n]$ as a **convolution** of the return probabilities $u_n$ with the excursion profile $g(t)$.

2. The finite invariant mean condition (Step 3) is **exactly equivalent** to $g \in \ell^1$, via Kac's formula.

3. The convolution of a bounded sequence converging to 0 with an $\ell^1$ sequence always converges to 0 (Step 5).

Thus, the Markov chain structure provides the uniform integrability that arbitrary sequences of distributions lack. The finite invariant mean condition $E_\mu[X] < \infty$ is precisely the right condition to ensure $E_{k_0}[M_n] \to E_\mu[X]$.

### Key Ingredients Used

- **Renewal decomposition**: Standard for countable-state Markov chains (see Norris, *Markov Chains*, Theorem 1.3.5; or Meyn-Tweedie, *Markov Chains and Stochastic Stability*).
- **Markov chain convergence theorem**: Irreducibility + aperiodicity + positive recurrence $\Rightarrow$ $P^n(i,j) \to \mu_j$ (Norris, Theorem 1.8.3).
- **Kac's formula** (cycle formula): $E_i\!\left[\sum_{t=1}^{T_i} f(M_t)\right] = E_\mu[f]/\mu_i$ for positive recurrent chains (Norris, Theorem 1.10.2).
- **Convolution lemma**: Standard analysis result; $\ell^1 * c_0 \subseteq c_0$.

### PROOF COMPLETE
