# Proof: Existence of a set $M$ of 1992 positive integers where every element and every subset sum is a perfect power

## Answer

$$\boxed{\text{Yes}}$$

## Construction

**Step 1: Choose a base set.** Let $S = \{1, 2, 3, \ldots, 1992\}$.

**Step 2: Enumerate all nonempty subset sums.** Let $\mathcal{F}$ be the collection of all nonempty subsets of $S$, so $|\mathcal{F}| = 2^{1992} - 1 = N$. For each $T \in \mathcal{F}$, define $t_T = \sum_{i \in T} i$.

**Step 3: Assign a distinct prime to each subset.** For each $T \in \mathcal{F}$, assign a distinct prime $p_T \geq 2$. This is possible since there are infinitely many primes and $\mathcal{F}$ is finite. The primes $\{p_T : T \in \mathcal{F}\}$ are pairwise coprime.

**Step 4: Construct the multiplier $C$ via CRT.** Let $q_1, q_2, \ldots, q_m$ be all the primes that divide at least one $t_T$. For each such prime $q_\ell$, consider the system of congruences:

$$g_{q_\ell} \equiv -v_{q_\ell}(t_T) \pmod{p_T} \quad \text{for all } T \in \mathcal{F}$$

where $v_{q_\ell}(t_T)$ denotes the $q_\ell$-adic valuation of $t_T$. Since the moduli $p_T$ are pairwise coprime, the Chinese Remainder Theorem guarantees a unique solution modulo $P = \prod_{T \in \mathcal{F}} p_T$. Take $g_{q_\ell}$ to be the smallest non-negative solution (so $0 \le g_{q_\ell} < P$).

Define:
$$C = \prod_{\ell=1}^{m} q_\ell^{g_{q_\ell}}$$

This is a well-defined positive integer (finite product over finitely many primes).

**Step 5: Define $M$.** Set $M = \{C, 2C, 3C, \ldots, 1992C\}$.

## Verification

**Distinctness:** The elements $C, 2C, \ldots, 1992C$ are 1992 distinct positive integers (since $C > 0$).

**Every element is a perfect power:** The element $iC$ corresponds to the singleton subset $T = \{i\}$, so $iC = C \cdot t_{\{i\}}$. By the argument below, this is a perfect power.

**Every nonempty subset sum is a perfect power:** Consider any nonempty subset $U \subseteq \{1, \ldots, 1992\}$. The corresponding sum is:

$$\sum_{i \in U} iC = C \cdot \sum_{i \in U} i = C \cdot t_U$$

We analyze the prime factorization of $C \cdot t_U$. For each prime $q_\ell$:

$$v_{q_\ell}(C \cdot t_U) = g_{q_\ell} + v_{q_\ell}(t_U)$$

By construction, $g_{q_\ell} \equiv -v_{q_\ell}(t_U) \pmod{p_U}$, so:

$$p_U \mid \bigl(g_{q_\ell} + v_{q_\ell}(t_U)\bigr)$$

This holds for **every** prime $q_\ell$ dividing $C \cdot t_U$. Therefore, every exponent in the prime factorization of $C \cdot t_U$ is divisible by $p_U \ge 2$.

**Case 1:** If $C \cdot t_U > 1$, then at least one exponent is positive, and all positive exponents share the common divisor $p_U \ge 2$. Hence $C \cdot t_U$ is a perfect $p_U$-th power (at least).

**Case 2:** If $C \cdot t_U = 1$, then $1 = 1^2$ is a perfect power.

In either case, $C \cdot t_U$ is expressible as $m^k$ with $m$ a positive integer and $k \ge 2$. $\checkmark$

## Conclusion

The set $M = \{C, 2C, 3C, \ldots, 1992C\}$ consists of exactly 1992 distinct positive integers, every element is a perfect power, and every nonempty subset sum is a perfect power. Therefore, such a set exists.

$$\boxed{\text{Yes}}$$

### PROOF COMPLETE
