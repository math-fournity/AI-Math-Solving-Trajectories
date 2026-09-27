# Proof: Minimum of $\prod_{i=1}^{n} \frac{A - a_i}{d_i D_i}$

## Answer

$$\boxed{(n-1)^n}$$

achieved when $a_1 = a_2 = \cdots = a_n = 1$.

---

## Setup and Notation

Let $a_1, a_2, \ldots, a_n$ be pairwise coprime positive integers ($n \geq 2$), $A = \sum_{i=1}^n a_i$, $d_i = \gcd(A, a_i)$, and $D_i = \gcd(\{a_j : j \neq i\})$.

Define $g_i = d_i = \gcd(A, a_i)$ and $f_i = \frac{A - a_i}{g_i}$.

---

## Step 1: The case $n = 2$

When $n = 2$: $D_1 = \gcd(a_2) = a_2$, $D_2 = \gcd(a_1) = a_1$. Since $\gcd(a_1, a_2) = 1$:

$$d_1 = \gcd(a_1 + a_2,\, a_1) = \gcd(a_2, a_1) = 1, \quad d_2 = 1.$$

$$\prod_{i=1}^{2} \frac{A - a_i}{d_i D_i} = \frac{a_2}{1 \cdot a_2} \cdot \frac{a_1}{1 \cdot a_1} = 1 = (2-1)^2.$$

So the product is identically $1 = (n-1)^n$ for all valid inputs when $n = 2$. ✓

---

## Step 2: Simplification for $n \geq 3$ — $D_i = 1$

**Claim:** For $n \geq 3$, $D_i = 1$ for all $i$.

**Proof:** $D_i = \gcd(a_1, \ldots, a_{i-1}, a_{i+1}, \ldots, a_n)$. Since $n \geq 3$, this gcd is taken over at least $2$ numbers. If a prime $p$ divides $D_i$, then $p \mid a_j$ and $p \mid a_k$ for two distinct $j, k \neq i$, contradicting pairwise coprimality. $\square$

So for $n \geq 3$, the product simplifies to:

$$\prod_{i=1}^{n} \frac{A - a_i}{d_i D_i} = \prod_{i=1}^{n} \frac{A - a_i}{g_i} = \prod_{i=1}^{n} f_i.$$

---

## Step 3: Key properties of $g_i$

Since $g_i = \gcd(A, a_i)$:

1. **$g_i \mid a_i$**, so $a_i \geq g_i$ (as $a_i \geq 1$ and $g_i$ is a positive divisor of $a_i$).

2. **$g_i \mid (A - a_i)$**, since $g_i \mid A$ and $g_i \mid a_i$.

3. **The $g_i$ are pairwise coprime:** if prime $p \mid g_i$ and $p \mid g_j$ ($i \neq j$), then $p \mid a_i$ and $p \mid a_j$, contradicting $\gcd(a_i, a_j) = 1$.

4. **$\gcd(g_i, a_j) = 1$ for $j \neq i$:** since $g_i \mid a_i$ and $\gcd(a_i, a_j) = 1$.

---

## Step 4: Lower bound on each $f_i$

Since $g_i \mid a_i$ and $a_i \geq 1$, we have $a_i \geq g_i$ for every $i$. Therefore:

$$A - a_i = \sum_{j \neq i} a_j \geq \sum_{j \neq i} g_j.$$

Dividing by $g_i$ (which divides $A - a_i$):

$$f_i = \frac{A - a_i}{g_i} \geq \frac{\sum_{j \neq i} g_j}{g_i}.$$

---

## Step 5: The key inequality via AM-GM

**Theorem.** For any positive reals $g_1, g_2, \ldots, g_n$:

$$\prod_{i=1}^{n} \frac{\sum_{j \neq i} g_j}{g_i} \geq (n-1)^n.$$

**Proof.** By the AM-GM inequality applied to the $n-1$ positive numbers $\{g_j : j \neq i\}$:

$$\sum_{j \neq i} g_j \geq (n-1)\left(\prod_{j \neq i} g_j\right)^{\!1/(n-1)}.$$

Therefore:

$$\prod_{i=1}^{n} \frac{\sum_{j \neq i} g_j}{g_i} \geq \prod_{i=1}^{n} \frac{(n-1)\left(\prod_{j \neq i} g_j\right)^{1/(n-1)}}{g_i} = (n-1)^n \cdot \frac{\prod_{i=1}^{n}\left(\prod_{j \neq i} g_j\right)^{1/(n-1)}}{\prod_{i=1}^{n} g_i}.$$

**Computing the numerator:** In $\prod_{i=1}^{n}\left(\prod_{j \neq i} g_j\right)^{1/(n-1)}$, each $g_k$ appears in $\prod_{j \neq i} g_j$ for every $i \neq k$ (that is, $n-1$ times), each time with exponent $\frac{1}{n-1}$. The total exponent of $g_k$ is:

$$(n-1) \times \frac{1}{n-1} = 1.$$

Hence:

$$\prod_{i=1}^{n}\left(\prod_{j \neq i} g_j\right)^{1/(n-1)} = \prod_{k=1}^{n} g_k.$$

Substituting back:

$$\prod_{i=1}^{n} \frac{\sum_{j \neq i} g_j}{g_i} \geq (n-1)^n \cdot \frac{\prod_{k=1}^n g_k}{\prod_{i=1}^n g_i} = (n-1)^n. \qquad \square$$

---

## Step 6: Combining the bounds

From Step 4 and Step 5:

$$\prod_{i=1}^{n} f_i \geq \prod_{i=1}^{n} \frac{\sum_{j \neq i} g_j}{g_i} \geq (n-1)^n.$$

---

## Step 7: Equality analysis

Equality in Step 5 (AM-GM) requires all $g_j$ ($j \neq i$) to be equal for each $i$, which means all $g_i$ are equal: $g_1 = g_2 = \cdots = g_n = g$.

Equality in Step 4 requires $a_j = g_j$ for all $j$, i.e., $a_i = g_i = g$ for all $i$.

With all $a_i = g$: $A = ng$, and $g_i = \gcd(ng, g) = g$. ✓

But pairwise coprimality requires $\gcd(a_i, a_j) = \gcd(g, g) = g = 1$.

So equality holds if and only if $g = 1$, i.e., $a_1 = a_2 = \cdots = a_n = 1$, giving $A = n$ and:

$$\prod_{i=1}^{n} \frac{A - a_i}{g_i} = \prod_{i=1}^{n} \frac{n - 1}{1} = (n-1)^n.$$

---

## Step 8: Verification for $n = 2$ consistency

For $n = 2$, the formula gives $(2-1)^2 = 1$, matching the direct computation in Step 1. ✓

---

## Conclusion

For all $n \geq 2$ and all pairwise coprime positive integers $a_1, \ldots, a_n$:

$$\prod_{i=1}^{n} \frac{A - a_i}{d_i D_i} \geq (n-1)^n,$$

with equality if and only if $a_1 = a_2 = \cdots = a_n = 1$ (for $n \geq 3$; for $n = 2$ equality holds for all valid inputs, and the value is always $1 = (n-1)^n$).

$$\boxed{(n-1)^n}$$
