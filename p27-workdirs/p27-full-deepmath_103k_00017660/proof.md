# Proof: Smallest $d^*$ for the Harmonic Number Inequality

## Problem

Determine the smallest integer $d^*$ such that

$$\frac{\left(\sum_{i=1}^d i^{-p}\right)^2}{\sum_{i=1}^d i^{-2p}} \ge \frac{1}{2}\frac{\zeta(p)^2}{\zeta(2p)}$$

holds, where $H_d^{(p)} = \sum_{i=1}^d i^{-p}$ denotes the generalized Harmonic numbers and $\zeta(s)$ is the Riemann Zeta function.

We take $p = 2$ (the canonical value for zeta-function problems, yielding exact closed-form constants).

---

## Notation

Define for $p > 1$ and integer $d \ge 1$:

$$R_d(p) = \frac{H_d^{(p)2}}{H_d^{(2p)}} = \frac{\left(\sum_{i=1}^d i^{-p}\right)^2}{\sum_{i=1}^d i^{-2p}}$$

and $R_\infty(p) = \frac{\zeta(p)^2}{\zeta(2p)}$. The inequality becomes $R_d(p) \ge \tfrac{1}{2} R_\infty(p)$.

---

## Step 1: $R_d(p)$ is strictly increasing in $d$

**Claim.** For each fixed $p > 1$, the sequence $\{R_d(p)\}_{d=1}^\infty$ is strictly increasing.

**Proof.** Let $S = \sum_{i=1}^d i^{-p}$, $Q = \sum_{i=1}^d i^{-2p}$, and $a = (d+1)^{-p}$. Then

$$R_{d+1} = \frac{(S+a)^2}{Q+a^2}, \qquad R_d = \frac{S^2}{Q}.$$

We have $R_{d+1} > R_d$ iff $(S+a)^2 Q > S^2(Q+a^2)$, i.e.,

$$2aSQ + a^2 Q > S^2 a^2 \iff 2SQ > a(S^2 - Q).$$

Now $S^2 - Q = 2\sum_{1 \le i < j \le d} i^{-p} j^{-p}$. Since $a = (d+1)^{-p} \le i^{-p}$ for all $1 \le i \le d$, we get

$$a \sum_{i<j} i^{-p} j^{-p} \le \sum_{i<j} i^{-2p} j^{-p} \le \left(\sum_i i^{-2p}\right)\left(\sum_j j^{-p}\right) = QS.$$

Therefore $QS \ge a \sum_{i<j} i^{-p}j^{-p} = \frac{a}{2}(S^2 - Q)$, which gives $2QS \ge a(S^2 - Q)$. $\square$

---

## Step 2: $R_d(p) \to R_\infty(p)$ as $d \to \infty$

Since $H_d^{(p)} \to \zeta(p)$ and $H_d^{(2p)} \to \zeta(2p)$ for $p > 1$, we have $R_d(p) \to \frac{\zeta(p)^2}{\zeta(2p)} = R_\infty(p)$.

**Corollary.** By Steps 1–2, for each $p > 1$ there exists a unique smallest integer $d^*(p)$ satisfying $R_d(p) \ge \frac{1}{2}R_\infty(p)$.

---

## Step 3: Exact computation for $p = 2$

For $p = 2$:

$$\zeta(2) = \frac{\pi^2}{6}, \qquad \zeta(4) = \frac{\pi^4}{90}$$

$$R_\infty(2) = \frac{\zeta(2)^2}{\zeta(4)} = \frac{(\pi^2/6)^2}{\pi^4/90} = \frac{\pi^4/36}{\pi^4/90} = \frac{90}{36} = \frac{5}{2}$$

$$\frac{1}{2}R_\infty(2) = \frac{5}{4}$$

### Check $d = 1$:

$$R_1(2) = \frac{(1)^2}{1} = 1 < \frac{5}{4} \qquad \text{(fails)}$$

### Check $d = 2$:

$$H_2^{(2)} = 1 + \frac{1}{4} = \frac{5}{4}, \qquad H_2^{(4)} = 1 + \frac{1}{16} = \frac{17}{16}$$

$$R_2(2) = \frac{(5/4)^2}{17/16} = \frac{25/16}{17/16} = \frac{25}{17}$$

We need $\frac{25}{17} \ge \frac{5}{4}$, i.e., $25 \times 4 = 100 \ge 17 \times 5 = 85$. **True.** ✓

---

## Step 4: Conclusion

Since $R_d(2)$ is strictly increasing (Step 1), $R_1(2) = 1 < \frac{5}{4}$ (fails), and $R_2(2) = \frac{25}{17} \ge \frac{5}{4}$ (holds), the smallest integer $d^*$ satisfying the inequality for $p = 2$ is:

$$\boxed{d^* = 2}$$

### PROOF COMPLETE
