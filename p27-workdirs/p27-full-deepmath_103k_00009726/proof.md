# Proof: Bijective Enumeration of Rationals with Finite Square-Variation Energy

## Problem

Does there exist a bijective enumeration of the rationals in $[0,1]$, denoted $q_1, q_2, \ldots$, such that $\sum_{i=1}^{\infty} (q_i - q_{i-1})^2 < \infty$?

**Answer: Yes.** We set $q_0 = 0$ (any fixed value in $[0,1]$ works; the first term is bounded by 1 and does not affect convergence).

---

## Construction

### Farey sequences

Recall the **Farey sequence** of order $n$, denoted $F_n$: the elements of $[0,1]$ that are rationals $p/q$ in lowest terms with $1 \leq q \leq n$, arranged in increasing order. Standard properties:

- If $a/b < c/d$ are consecutive in $F_n$, then $bc - ad = 1$ and $b + d > n$.
- The gap $c/d - a/b = 1/(bd) \leq 1/n$, with equality at the endpoints $0/1, 1/n$.
- The **mediant** $(a+c)/(b+d)$ satisfies $a/b < (a+c)/(b+d) < c/d$ and has denominator $b+d$.

### Geometric growth schedule

Set $n_k = 2^k$ for $k = 0, 1, 2, \ldots$ (so $n_0=1, n_1=2, n_2=4, n_3=8, \ldots$). Note $n_k = 2\,n_{k-1}$.

Define the **layers**:
$$A_0 = F_{n_0} = F_1 = \{0,\, 1\}, \qquad A_k = F_{n_k} \setminus F_{n_{k-1}} \quad (k \geq 1).$$

Each $A_k$ consists of rationals $p/q \in [0,1]$ in lowest terms with $n_{k-1} < q \leq n_k$.

### Enumeration rule

Visit the layers in order $A_0, A_1, A_2, \ldots$. Within each layer, visit elements in **sorted order**, **alternating direction**:

- **Even $k$** (including $k=0$): left $\to$ right (increasing order).
- **Odd $k$**: right $\to$ left (decreasing order).

This produces the sequence $q_1, q_2, q_3, \ldots$

---

## Bijectivity

Every rational $r = p/q \in [0,1]$ in lowest terms has a unique denominator $q \geq 1$. Since $n_k = 2^k \to \infty$, there is a unique $k \geq 1$ with $n_{k-1} < q \leq n_k$ (or $q = 1$ giving $k=0$). Thus $r \in A_k$ for exactly one $k$. Within $A_k$, each element is listed exactly once. Therefore the enumeration is a **bijection** $\mathbb{N} \to \mathbb{Q} \cap [0,1]$. $\checkmark$

---

## Key Lemma: Max Gap in $A_k$

**Lemma.** For $k \geq 1$, the maximum gap between consecutive elements of $A_k$ (in sorted order) is at most $2/n_{k-1}$.

**Proof.** Since $n_k = 2\,n_{k-1}$, every gap of $F_{n_{k-1}}$ contains at least one element of $A_k$:

> If $a/b < c/d$ are consecutive in $F_{n_{k-1}}$, then $b + d > n_{k-1}$ (Farey property) and $b + d \leq 2\,n_{k-1} = n_k$ (since $b, d \leq n_{k-1}$). The mediant $\frac{a+c}{b+d}$ has denominator $b+d \in (n_{k-1},\, n_k]$, so it lies in $F_{n_k} \setminus F_{n_{k-1}} = A_k$, and falls strictly between $a/b$ and $c/d$.

Now let $r_1 < r_2$ be two consecutive elements of $A_k$ (sorted). We claim at most **one** element of $F_{n_{k-1}}$ lies in the open interval $(r_1, r_2)$.

Suppose for contradiction that $s_i < s_{i+1}$ are two consecutive elements of $F_{n_{k-1}}$ both lying in $(r_1, r_2)$. By the argument above, the mediant of $s_i, s_{i+1}$ is an element of $A_k$ lying in $(s_i, s_{i+1}) \subset (r_1, r_2)$. But $r_1, r_2$ are consecutive in $A_k$, so no element of $A_k$ lies between them—contradiction.

Therefore at most one $F_{n_{k-1}}$ element $s$ lies between $r_1$ and $r_2$.

- **Case 1** (no $F_{n_{k-1}}$ element between them): Both $r_1, r_2$ lie in the same gap $(a/b, c/d)$ of $F_{n_{k-1}}$, so $r_2 - r_1 \leq c/d - a/b = 1/(bd) \leq 1/n_{k-1} \leq 2/n_{k-1}$.

- **Case 2** (exactly one $F_{n_{k-1}}$ element $s$ between them): $r_1$ lies in some gap $(a/b, s)$ and $r_2$ lies in the adjacent gap $(s, c/d)$ of $F_{n_{k-1}}$. Then
$$r_2 - r_1 = (s - r_1) + (r_2 - s) \leq \frac{1}{n_{k-1}} + \frac{1}{n_{k-1}} = \frac{2}{n_{k-1}}.$$

In both cases, $r_2 - r_1 \leq 2/n_{k-1}$. $\square$

---

## Energy Analysis

### Intra-sweep energy

For sweep $k \geq 1$, let the sorted elements of $A_k$ be $r_1 < r_2 < \cdots < r_m$. The intra-sweep energy (same regardless of traversal direction) is:

$$E_k^{\text{intra}} = \sum_{j=1}^{m-1} (r_{j+1} - r_j)^2 \leq \bigl(\max_j (r_{j+1} - r_j)\bigr) \cdot \sum_{j=1}^{m-1} (r_{j+1} - r_j).$$

By the Lemma, $\max_j (r_{j+1} - r_j) \leq 2/n_{k-1}$. The telescoping sum $\sum (r_{j+1} - r_j) = r_m - r_1 \leq 1$. Therefore:

$$E_k^{\text{intra}} \leq \frac{2}{n_{k-1}} = \frac{2}{2^{k-1}} = 2^{2-k} \qquad (k \geq 1).$$

For sweep $0$: $A_0 = \{0, 1\}$, so $E_0^{\text{intra}} = (1 - 0)^2 = 1$.

### Inter-sweep energy

We track the endpoints of each sweep:

- **Even $k$** (left $\to$ right): starts at $\min(A_k)$, ends at $\max(A_k)$.
- **Odd $k$** (right $\to$ left): starts at $\max(A_k)$, ends at $\min(A_k)$.

The minimum element of $A_k$ (for $k \geq 1$) is $1/n_k$ (the rational with denominator $n_k > n_{k-1}$, smallest value). The maximum is $(n_k - 1)/n_k = 1 - 1/n_k$.

**Transition from sweep $k$ to sweep $k+1$:**

- **$k$ even, $k+1$ odd**: Sweep $k$ ends at $1 - 1/n_k$; sweep $k+1$ starts at $1 - 1/n_{k+1}$.
  $$\text{Jump} = \left|\frac{1}{n_k} - \frac{1}{n_{k+1}}\right| \leq \frac{1}{n_k}.$$

- **$k$ odd, $k+1$ even**: Sweep $k$ ends at $1/n_k$; sweep $k+1$ starts at $1/n_{k+1}$.
  $$\text{Jump} = \left|\frac{1}{n_k} - \frac{1}{n_{k+1}}\right| \leq \frac{1}{n_k}.$$

In both cases, the inter-sweep jump is at most $1/n_k$, so:

$$E_k^{\text{inter}} \leq \frac{1}{n_k^2} = \frac{1}{4^k} \qquad (k \geq 0).$$

(The transition from $q_0 = 0$ to the start of sweep $0$ gives a jump of $|0 - 0| = 0$.)

### Total energy

$$\sum_{i=1}^{\infty} (q_i - q_{i-1})^2 = \underbrace{\sum_{k=0}^{\infty} E_k^{\text{intra}}}_{\text{intra-sweep}} + \underbrace{\sum_{k=0}^{\infty} E_k^{\text{inter}}}_{\text{inter-sweep}}.$$

**Intra-sweep total:**
$$1 + \sum_{k=1}^{\infty} \frac{2}{n_{k-1}} = 1 + 2\sum_{k=0}^{\infty} \frac{1}{2^k} = 1 + 2 \cdot 2 = 5.$$

**Inter-sweep total:**
$$\sum_{k=0}^{\infty} \frac{1}{4^k} = \frac{1}{1 - 1/4} = \frac{4}{3}.$$

**Grand total:**
$$\sum_{i=1}^{\infty} (q_i - q_{i-1})^2 \leq 5 + \frac{4}{3} = \frac{19}{3} < \infty.$$

---

## Conclusion

The geometric-growth Farey sweep construction produces a bijective enumeration of $\mathbb{Q} \cap [0,1]$ with total squared-variation energy at most $19/3 < \infty$.

$$\boxed{\text{Yes}}$$

### PROOF COMPLETE
