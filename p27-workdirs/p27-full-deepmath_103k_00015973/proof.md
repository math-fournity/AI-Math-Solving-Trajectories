# Proof

**Answer:** Yes. For every integer $n \ge 1$, at least one of $O^+(2n,2)$ or $O^-(2n,2)$ contains an element of order $2n+1$.

---

## Preliminaries

### Maximal tori of $O^\pm(2n,2)$

The maximal tori of the orthogonal groups $O^\pm(2n,q)$ (for $q$ even) are parametrized by **signed partitions** of $n$. A signed partition consists of:

- A partition $n = d_1 + d_2 + \cdots + d_k$ (with each $d_i \ge 1$),
- A sign $\epsilon_i \in \{+, -\}$ for each part $d_i$.

The corresponding torus is the product of cyclic groups:
$$T = \prod_{i=1}^{k} \mathbb{Z}/(2^{d_i} - \epsilon_i),$$
where a $-$ sign on part $d_i$ contributes a factor $\mathbb{Z}/(2^{d_i}-1)$ and a $+$ sign contributes $\mathbb{Z}/(2^{d_i}+1)$.

The sign parity determines which group the torus lies in:
- **$O^+(2n,2)$**: the number of $+$ signs is **even**.
- **$O^-(2n,2)$**: the number of $+$ signs is **odd**.

In particular:
- A single $-$ block of size $n$ (zero $+$ signs, even) gives the **split torus** $\mathbb{Z}/(2^n - 1) \le O^+(2n,2)$ — the *Singer cycle* of $O^+$.
- A single $+$ block of size $n$ (one $+$ sign, odd) gives the **non-split torus** $\mathbb{Z}/(2^n + 1) \le O^-(2n,2)$ — the *Singer cycle* of $O^-$.

### Element order in a torus

A finite abelian group $A = \prod_i \mathbb{Z}/a_i$ contains an element of order $m$ if and only if $m$ divides the **exponent** of $A$, which is $\operatorname{lcm}(a_1, \ldots, a_k)$. (This is a standard consequence of the structure theorem for finite abelian groups.)

In particular, a cyclic group $\mathbb{Z}/N$ contains an element of order $m$ iff $m \mid N$.

### A trivial block

A block of size $1$ with sign $-$ contributes $\mathbb{Z}/(2^1 - 1) = \mathbb{Z}/1$, the trivial group. This does not affect the exponent of the torus but does count as a $-$ sign for parity purposes. We use such trivial blocks to fill remaining space.

---

## Key Lemma

**Lemma.** Let $m \ge 3$ be an odd integer and let $D = \operatorname{ord}_m(2)$ be the multiplicative order of $2$ modulo $m$. If $D > \frac{m-1}{2}$, then $m = p^a$ for some odd prime $p$ and some $a \ge 1$. Consequently, $D = \phi(m)$ and $D$ is even.

**Proof.** Since $D = \operatorname{ord}_m(2)$, we have $D \mid \phi(m)$ (by Lagrange's theorem, as $2$ is an element of $(\mathbb{Z}/m\mathbb{Z})^*$). Also $\phi(m) \le m - 1$.

The hypothesis $D > \frac{m-1}{2} \ge \frac{\phi(m)}{2}$ (using $\phi(m) \le m-1$) together with $D \mid \phi(m)$ forces $D = \phi(m)$: the only divisor of $\phi(m)$ exceeding $\phi(m)/2$ is $\phi(m)$ itself.

Now $D = \phi(m)$ means that $2$ is a **primitive root** modulo $m$, i.e., $2$ generates the group $(\mathbb{Z}/m\mathbb{Z})^*$. This group must therefore be **cyclic**.

By the classical classification, $(\mathbb{Z}/m\mathbb{Z})^*$ is cyclic if and only if $m \in \{1, 2, 4, p^a, 2p^a\}$ for an odd prime $p$. Since $m$ is odd and $m \ge 3$, we conclude $m = p^a$ for some odd prime $p$.

Finally, $\phi(p^a) = p^{a-1}(p-1)$, and since $p$ is odd, $p - 1$ is even, so $D = \phi(m)$ is even. $\square$

**Corollary.** If $m = 2n+1$ is composite (i.e., has at least two distinct prime factors), then $\operatorname{ord}_m(2) \le n$.

**Proof.** This is the contrapositive of the Lemma: if $\operatorname{ord}_m(2) > n = \frac{m-1}{2}$, then $m = p^a$ (a prime power), contradicting the assumption that $m$ has at least two distinct prime factors. $\square$

---

## Main Proof

Let $n \ge 1$ and set $m = 2n + 1$ (which is odd and $\ge 3$). Let $D = \operatorname{ord}_m(2)$.

Since $D \mid \phi(m)$ and $\phi(m) \le m - 1 = 2n$, we have $D \le 2n$.

We consider two cases.

### Case 1: $D \le n$

Since $D = \operatorname{ord}_m(2)$, we have $m \mid 2^D - 1$.

Consider the signed partition of $n$ consisting of:
- One $-$ block of size $D$,
- $n - D$ trivial $-$ blocks of size $1$.

The number of $+$ signs is $0$ (even), so this torus lies in $O^+(2n, 2)$. The torus is:
$$T = \mathbb{Z}/(2^D - 1) \times \underbrace{\mathbb{Z}/1 \times \cdots \times \mathbb{Z}/1}_{n - D},$$
with exponent $2^D - 1$. Since $m \mid 2^D - 1$, the torus $T$ contains an element of order $m = 2n+1$.

### Case 2: $D > n$

By the Lemma, $m = p^a$ for some odd prime $p$, $D = \phi(m) = p^{a-1}(p-1)$, and $D$ is even.

Set $D' = D/2$. Since $D \le 2n$, we have $D' \le n$.

Since $m = p^a$ and $(\mathbb{Z}/p^a\mathbb{Z})^*$ is cyclic (as $p$ is an odd prime), the element $2^{D'}$ has order $2$ in $(\mathbb{Z}/p^a\mathbb{Z})^*$ (because $(2^{D'})^2 = 2^D \equiv 1 \pmod{p^a}$ and $2^{D'} \not\equiv 1 \pmod{p^a}$ since $D' < D = \operatorname{ord}_m(2)$). The unique element of order $2$ in a cyclic group is $-1$, so:
$$2^{D'} \equiv -1 \pmod{p^a},$$
which gives $m = p^a \mid 2^{D'} + 1$.

Consider the signed partition of $n$ consisting of:
- One $+$ block of size $D'$,
- $n - D'$ trivial $-$ blocks of size $1$.

The number of $+$ signs is $1$ (odd), so this torus lies in $O^-(2n, 2)$. The torus is:
$$T = \mathbb{Z}/(2^{D'} + 1) \times \underbrace{\mathbb{Z}/1 \times \cdots \times \mathbb{Z}/1}_{n - D'},$$
with exponent $2^{D'} + 1$. Since $m \mid 2^{D'} + 1$, the torus $T$ contains an element of order $m = 2n+1$.

---

## Conclusion

In both cases, we have exhibited a maximal torus in $O^+(2n,2)$ (Case 1) or $O^-(2n,2)$ (Case 2) whose exponent is divisible by $m = 2n+1$. Since a finite abelian group contains an element of order $m$ if and only if $m$ divides its exponent, the corresponding orthogonal group contains an element of order $2n+1$.

Therefore, for every integer $n \ge 1$, at least one of $O^+(2n,2)$ or $O^-(2n,2)$ contains an element of order $2n+1$.

$$\boxed{\text{Yes, for all } n \ge 1, \text{ at least one of } O^+(2n,2) \text{ or } O^-(2n,2) \text{ contains an element of order } 2n+1.}$$

### PROOF COMPLETE
