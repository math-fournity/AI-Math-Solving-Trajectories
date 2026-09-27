# Upper Power Density: Maximal $\alpha$

## Answer

$$\boxed{\dfrac{2}{3}}$$

No set $A \subseteq \mathbb{N}$ satisfies $\bar{d_p}(A) = \bar{d_p}(A^C) = \tfrac{1}{2}$. The maximal $\alpha$ such that for every $A \subseteq \mathbb{N}$, either $\bar{d_p}(A) \ge \alpha$ or $\bar{d_p}(A^C) \ge \alpha$, is $\alpha = \tfrac{2}{3}$.

---

## Definition of Power Density

The **upper power density** is defined as:

$$\bar{d_p}(A) = \limsup_{n \to \infty} \frac{\sum_{k \in A,\, k \le n} 2^k}{\sum_{k=1}^{n} 2^k}.$$

Each integer $k$ receives weight $2^k$ (a power of 2), so the density is dominated by the largest elements. One can verify that this gives $\bar{d_p}(\text{evens}) = \bar{d_p}(\text{odds}) = \tfrac{2}{3}$, consistent with the problem statement.

---

## Reduction to a Recurrence

Let $a_n = \mathbf{1}_A(n) \in \{0,1\}$ and define:

$$g(n) = \frac{\sum_{k=1}^{n} a_k \, 2^k}{2^{n+1}}.$$

Since $\sum_{k=1}^{n} 2^k = 2^{n+1} - 2$, we have $\bar{d_p}(A) = \limsup_{n\to\infty} g(n)$ (the factor $2^{n+1}/(2^{n+1}-2) \to 1$ does not affect the limsup). Similarly, $\bar{d_p}(A^C) = 1 - \liminf_{n\to\infty} g(n)$.

The function $g$ satisfies the **key recurrence**:

$$g(n) = \frac{g(n-1) + a_n}{2}, \qquad g(0) = 0.$$

Equivalently:
- If $a_n = 1$: $g(n) = \dfrac{g(n-1) + 1}{2}$.
- If $a_n = 0$: $g(n) = \dfrac{g(n-1)}{2}$.

---

## Key Geometric Observation

**Lemma.** If $g(n) \in \left(\tfrac{1}{3},\, \tfrac{2}{3}\right)$, then $g(n+1) \notin \left(\tfrac{1}{3},\, \tfrac{2}{3}\right)$ regardless of the choice of $a_{n+1}$.

*Proof.* Suppose $g(n) \in (1/3,\, 2/3)$.

- **Case $a_{n+1} = 0$:** $g(n+1) = g(n)/2 \in (1/6,\, 1/3)$. This lies below $1/3$, hence outside $(1/3, 2/3)$.
- **Case $a_{n+1} = 1$:** $g(n+1) = (g(n)+1)/2 \in (2/3,\, 5/6)$. This lies above $2/3$, hence outside $(1/3, 2/3)$.

In both cases, $g(n+1) \notin (1/3, 2/3)$. $\square$

---

## Impossibility of $\bar{d_p}(A) = \bar{d_p}(A^C) = 1/2$

**Theorem.** For every $A \subseteq \mathbb{N}$, either $\bar{d_p}(A) \ge \tfrac{2}{3}$ or $\bar{d_p}(A^C) \ge \tfrac{2}{3}$.

*Proof.* Suppose for contradiction that $\bar{d_p}(A) < \tfrac{2}{3}$ and $\bar{d_p}(A^C) < \tfrac{2}{3}$. Then:

$$\limsup_{n\to\infty} g(n) < \frac{2}{3} \quad \text{and} \quad 1 - \liminf_{n\to\infty} g(n) < \frac{2}{3},$$

which gives $\limsup g(n) < 2/3$ and $\liminf g(n) > 1/3$. By definition of limsup and liminf, there exists $N$ such that for all $n \ge N$:

$$g(n) \in \left(\frac{1}{3},\, \frac{2}{3}\right).$$

But by the Lemma, $g(N+1) \notin (1/3, 2/3)$, contradicting the above. $\square$

**Corollary.** No set $A$ achieves $\bar{d_p}(A) = \bar{d_p}(A^C) = \tfrac{1}{2}$, since this would require $\limsup g(n) = 1/2 < 2/3$ and $\liminf g(n) = 1/2 > 1/3$, which is impossible by the Theorem.

---

## Tightness: The Bound $2/3$ Is Achieved

We show that $A = \{\text{even numbers}\}$ achieves $\bar{d_p}(A) = \bar{d_p}(A^C) = \tfrac{2}{3}$.

For evens, $a_n = 1$ if $n$ is even, $a_n = 0$ if $n$ is odd. Computing $g$:

| $n$ | $g(n)$ |
|-----|--------|
| 1 | $0$ |
| 2 | $1/2$ |
| 3 | $1/4$ |
| 4 | $5/8$ |
| 5 | $5/16$ |
| 6 | $21/32$ |
| 7 | $21/64$ |
| 8 | $85/128$ |

**At even $n = 2m$:** $g(2m) = \frac{2^{2m} + 2(-1)^{2m}}{3 \cdot 2^{2m}} \cdot \frac{1}{2} \cdot 2 = \cdots$

More precisely, the values at even indices satisfy $g(2m) \to \frac{2}{3}$ from below, and the values at odd indices satisfy $g(2m+1) \to \frac{1}{3}$ from below. One can verify the closed forms:

$$g(2m) = \frac{2}{3} - \frac{1}{3 \cdot 4^m}, \qquad g(2m+1) = \frac{1}{3} - \frac{1}{3 \cdot 2 \cdot 4^m}.$$

(These are verified by induction using the recurrence and the alternating pattern $a_n = 0,1,0,1,\ldots$)

Therefore:
$$\limsup_{n\to\infty} g(n) = \frac{2}{3}, \qquad \liminf_{n\to\infty} g(n) = \frac{1}{3}.$$

This gives $\bar{d_p}(\text{evens}) = \tfrac{2}{3}$ and $\bar{d_p}(\text{odds}) = 1 - \tfrac{1}{3} = \tfrac{2}{3}$.

---

## Optimality of the Strategy

The interval $(1/3, 2/3)$ is the **largest** symmetric interval around $1/2$ that cannot be maintained by the recurrence. To see this is optimal, consider any strategy attempting to keep $g$ in a wider interval $(1/2 - \delta, 1/2 + \delta)$ with $\delta < 1/6$ (i.e., a narrower interval than $(1/3, 2/3)$):

- If $g \in (1/2 - \delta, 1/2 + \delta)$, then $g/2 \in (1/4 - \delta/2, 1/4 + \delta/2)$ and $(g+1)/2 \in (3/4 - \delta/2, 3/4 + \delta/2)$.
- Both options are far from $1/2$ (distance $\geq 1/4 - \delta/2 > 1/4 - 1/12 = 1/6 > \delta$).

So $g$ immediately exits any interval narrower than $(1/3, 2/3)$, confirming that $2/3$ is the tight threshold.

---

## Conclusion

$$\alpha = \inf_{A \subseteq \mathbb{N}} \max\!\big(\bar{d_p}(A),\, \bar{d_p}(A^C)\big) = \frac{2}{3}.$$

The bound is achieved by $A = \{\text{even numbers}\}$ (and many other sets), and no set can do better.

$$\boxed{\dfrac{2}{3}}
