# Proof: The process $(S_1, S_2, \ldots)$ is necessarily recurrent

## Answer

$\boxed{\text{Yes}}$ — the process is necessarily recurrent. In fact, a stronger statement holds:

$$\liminf_{n\to\infty} |S_n| = 0 \quad \text{a.s.},$$

which immediately implies recurrence (take $M = 1$, or any $M > 0$).

---

## Setup

Since $(X_1, X_2, \ldots)$ is stationary and ergodic, there exists an ergodic measure-preserving transformation $T$ on a probability space $(\Omega, \mathcal{F}, \mathbb{P})$ and a function $f \in L^\infty(\mathbb{P})$ with $|f| \leq 1$ and $\mathbb{E}[f] = 0$, such that

$$X_n = f \circ T^{n-1}, \qquad S_n = \sum_{k=0}^{n-1} f \circ T^k.$$

We prove $\liminf_{n\to\infty} |S_n| = 0$ a.s.

---

## Proof (by contradiction)

### Step 1 — Negation hypothesis

Suppose $\liminf_{n\to\infty} |S_n| > 0$ on a set of positive measure. Then there exist $\epsilon > 0$ and a measurable set $A$ with $\mathbb{P}(A) > 0$ such that

$$\liminf_{n\to\infty} |S_n(\omega)| \geq 2\epsilon \quad \text{for all } \omega \in A.$$

### Step 2 — Extract a uniform set

Define $g_N(\omega) = \inf_{n \geq N} |S_n(\omega)|$. Then $g_N \nearrow \liminf |S_n|$ pointwise, so by monotone convergence there exist $N_0 \in \mathbb{N}$ and a set $B \subseteq A$ with $\mathbb{P}(B) > 0$ such that

$$|S_n(\omega)| \geq \epsilon \quad \text{for all } \omega \in B,\; n \geq N_0. \tag{1}$$

### Step 3 — Return times to $B$

By the Birkhoff ergodic theorem, for a.e. $\omega$ the orbit $\{T^m \omega\}_{m \geq 0}$ visits $B$ with asymptotic frequency $\mathbb{P}(B) > 0$. Fix such an $\omega$ and let

$$m_1 < m_2 < m_3 < \cdots$$

be the times $m \geq N_0$ with $T^m \omega \in B$.

### Step 4 — Cocycle identity

For the ergodic sum we have the cocycle identity

$$S_n(T^{m_k}\omega) = S_{m_k + n}(\omega) - S_{m_k}(\omega). \tag{2}$$

Since $T^{m_k}\omega \in B$, condition (1) gives $|S_n(T^{m_k}\omega)| \geq \epsilon$ for all $n \geq N_0$. Substituting (2):

$$|S_{m_k + n}(\omega) - S_{m_k}(\omega)| \geq \epsilon \quad \text{for all } n \geq N_0. \tag{3}$$

### Step 5 — Separation property

Set $c_k = S_{m_k}(\omega)$. We claim:

$$|c_j - c_k| \geq \epsilon \quad \text{whenever } |j - k| \geq N_0. \tag{4}$$

Indeed, if $j > k$ and $j - k \geq N_0$, then $m_j \geq m_k + N_0$ (since $m_{k+1}, \ldots, m_{k+N_0}$ are $N_0$ distinct integers all strictly greater than $m_k$, so the largest, $m_{k+N_0}$, satisfies $m_{k+N_0} \geq m_k + N_0$, and $m_j \geq m_{k+N_0}$). Thus $n := m_j - m_k \geq N_0$, and (3) yields $|c_j - c_k| \geq \epsilon$. The case $j < k$ is symmetric.

### Step 6 — Growth bound

By Birkhoff's theorem, $S_n(\omega)/n \to \mathbb{E}[f] = 0$ a.s. Also $m_k / k \to 1/\mathbb{P}(B)$. Hence for any $\delta > 0$, for all sufficiently large $k$:

$$|c_k| = |S_{m_k}(\omega)| \leq \delta \, m_k \leq \frac{2\delta}{\mathbb{P}(B)}\, k.$$

Set $\delta' = \frac{2\delta}{\mathbb{P}(B)}$, so $|c_k| \leq \delta' k$ for all large $k$.

### Step 7 — Counting argument (the contradiction)

Fix a large $J$ beyond which the growth bound holds, and let $K > J$ be arbitrary. The $K - J$ values $c_J, c_{k+1}, \ldots, c_{K-1}$ all lie in the interval $[-\delta' K,\, \delta' K]$, of length $2\delta' K$.

**Key observation:** By the separation property (4), any interval of length $\epsilon$ contains **at most $N_0$** of the $c_k$. (If two indices $j, k$ with $|j - k| \geq N_0$ both fell in the same $\epsilon$-interval, we would have $|c_j - c_k| < \epsilon$, contradicting (4). Hence all indices in a single $\epsilon$-interval are pairwise within distance $< N_0$, so there are at most $N_0$ of them.)

Covering $[-\delta' K,\, \delta' K]$ requires at most $\left\lceil \frac{2\delta' K}{\epsilon} \right\rceil + 1 \leq \frac{2\delta' K}{\epsilon} + 2$ intervals of length $\epsilon$. Therefore:

$$K - J \;\leq\; \left(\frac{2\delta' K}{\epsilon} + 2\right) N_0 \;=\; \frac{4\delta\, N_0}{\epsilon\, \mathbb{P}(B)}\, K + 2 N_0.$$

Now choose $\delta > 0$ small enough that $\frac{4\delta\, N_0}{\epsilon\, \mathbb{P}(B)} < \frac{1}{2}$. Then:

$$K - J \;\leq\; \frac{K}{2} + 2 N_0 \quad\Longrightarrow\quad K \;\leq\; 2J + 4 N_0.$$

But $K$ was arbitrary, so this is a **contradiction**.

### Conclusion

The assumption that $\liminf |S_n| > 0$ on a set of positive measure is false. Therefore

$$\liminf_{n\to\infty} |S_n| = 0 \quad \text{a.s.}$$

In particular, for $M = 1$ (indeed for any $M > 0$), the event $\{|S_n| \leq M\}$ occurs infinitely often almost surely. Hence $(S_1, S_2, \ldots)$ is recurrent. $\blacksquare$

---

## Remark

This is a from-scratch proof of **Atkinson's theorem** (G. Atkinson, "Recurrence of co-cycles and random walks," *J. London Math. Soc.*, 1976), specialized to the bounded case $|f| \leq 1$. The theorem in full generality states that for an ergodic measure-preserving $T$ and $f \in L^1$ with $\int f\,d\mathbb{P} = 0$, the Birkhoff sums $S_n f = \sum_{k=0}^{n-1} f \circ T^k$ satisfy $\liminf_{n\to\infty} |S_n f| = 0$ a.s.

### PROOF COMPLETE
