# Proof: The limit $\lim_{x\to\infty} \frac{u(x)}{\pi(x)}$ exists

## Answer

$$\boxed{\lim_{x\to\infty} \frac{u(x)}{\pi(x)} = 0}$$

The limit exists and equals $0$.

---

## Definitions

- $\pi(x) = |\{p \le x : p \text{ prime}\}|$ is the prime counting function.
- $u(x) = |\{p \le x : p \text{ prime},\; s(p) \text{ prime}\}|$, where $s(n)$ denotes the sum of the (base-$10$) digits of $n$.

We prove $u(x)/\pi(x) \to 0$.

---

## Key tool: Mauduit–Rivat (2009)

**Theorem (Mauduit–Rivat, 2009).** *Sur un problème de Gelfond: la somme des chiffres des nombres premiers.* Let $s(n)$ be the sum of digits of $n$ in base $10$. For every $m \ge 2$ with $\gcd(m, 9) = 1$ and every residue $a \pmod{m}$,

$$\sum_{\substack{n \le N \\ s(n) \equiv a \!\!\pmod{m}}} \Lambda(n) \;=\; \frac{N}{m} + O\!\left(N^{1-\sigma}\right),$$

where $\sigma > 0$ is an absolute constant, and the estimate is uniform for $m = N^{o(1)}$.

**Reduction to prime counting.** The sum over $\Lambda(n)$ can be converted to a count over primes by standard partial summation. Indeed, writing the left side as

$$\sum_{\substack{p^k \le N \\ s(p^k) \equiv a \!\!\pmod{m}}} \log p,$$

the contribution of prime powers with $k \ge 2$ is $O(N^{1/2}\log N)$, which is absorbed into the error $O(N^{1-\sigma})$ (after possibly shrinking $\sigma$ by an absolute constant). The remaining sum over primes, weighted by $\log p$, is then converted to the unweighted count

$$\bigl|\{p \le N : s(p) \equiv a \pmod{m}\}\bigr| \;=\; \frac{\pi(N)}{m} + O\!\left(N^{1-\sigma'}\right)$$

by partial summation (Abel summation), for some absolute $\sigma' > 0$. This conversion costs only a constant factor in the error exponent, so the asymptotic structure is preserved.

---

## Proof

**Step 1: Setup.** Let $x$ be large and set $d = \lceil \log_{10} x \rceil$, so every $n \le x$ has at most $d$ digits and hence

$$s(n) \le 9d \qquad \text{for all } n \le x.$$

In particular $s(p) \le 9d$ for every prime $p \le x$.

**Step 2: Choice of modulus.** Let $m$ be the smallest prime number strictly greater than $9d$ with $m \neq 3$. Concretely, since $9d \ge 9$ for $d \ge 1$, we have $m > 9$, so $m \neq 3$ automatically and $\gcd(m, 9) = 1$ (as $m$ is a prime $> 9$, it is not $3$, and not divisible by $3$). By Bertrand's postulate, there is a prime between $9d$ and $2 \cdot 9d = 18d$, so

$$9d < m \le 18d.$$

Since $d \sim \frac{\ln x}{\ln 10}$, we have $m = \Theta(\ln x) = x^{o(1)}$, so the uniformity range $m = N^{o(1)}$ of the Mauduit–Rivat theorem is satisfied (with $N = x$).

**Step 3: Isolating each digit-sum value.** Because $m > 9d \ge s(p)$ for every prime $p \le x$, each possible digit-sum value $q \in \{0, 1, \dots, 9d\}$ occupies a *distinct* residue class modulo $m$. Therefore, for each such $q$,

$$s(p) = q \quad \Longleftrightarrow \quad s(p) \equiv q \pmod{m}.$$

**Step 4: Applying Mauduit–Rivat.** By the (reduced form of the) Mauduit–Rivat theorem, for each $q \in \{0, 1, \dots, 9d\}$,

$$\bigl|\{p \le x : s(p) = q\}\bigr| \;=\; \bigl|\{p \le x : s(p) \equiv q \pmod{m}\}\bigr| \;=\; \frac{\pi(x)}{m} + O\!\left(x^{1-\sigma'}\right).$$

**Step 5: Summing over prime digit-sums.** The digit sum $s(p)$ is prime only if $s(p) = q$ for some prime $q \le 9d$. (We also need $q \ge 2$, which is automatic for primes.) Summing over all primes $q \le 9d$:

$$u(x) \;=\; \sum_{\substack{q \le 9d \\ q \text{ prime}}} \bigl|\{p \le x : s(p) = q\}\bigr| \;=\; \sum_{\substack{q \le 9d \\ q \text{ prime}}} \left[\frac{\pi(x)}{m} + O\!\left(x^{1-\sigma'}\right)\right].$$

Let $\pi(9d)$ denote the number of primes up to $9d$. Then

$$u(x) \;=\; \frac{\pi(9d)}{m}\,\pi(x) \;+\; O\!\left(\pi(9d)\, x^{1-\sigma'}\right).$$

**Step 6: Estimating the main term.** By the prime number theorem,

$$\pi(9d) \sim \frac{9d}{\ln(9d)} \sim \frac{9d}{\ln d}, \qquad m = \Theta(d).$$

Hence

$$\frac{\pi(9d)}{m} \;=\; \Theta\!\left(\frac{d/\ln d}{d}\right) \;=\; \Theta\!\left(\frac{1}{\ln d}\right).$$

Since $d \sim \frac{\ln x}{\ln 10} \to \infty$ as $x \to \infty$,

$$\frac{\pi(9d)}{m} \;\longrightarrow\; 0.$$

**Step 7: Estimating the error term.** We have $\pi(9d) = O(d/\ln d) = O(\ln x / \ln\ln x)$ and $\pi(x) \sim x/\ln x$, so

$$\frac{\pi(9d)\, x^{1-\sigma'}}{\pi(x)} \;=\; O\!\left(\frac{(\ln x / \ln\ln x)\, x^{1-\sigma'}}{x / \ln x}\right) \;=\; O\!\left(\frac{(\ln x)^2}{\ln\ln x}\, x^{-\sigma'}\right) \;\longrightarrow\; 0.$$

**Step 8: Conclusion.** Dividing by $\pi(x)$,

$$\frac{u(x)}{\pi(x)} \;=\; \frac{\pi(9d)}{m} \;+\; O\!\left(\frac{\pi(9d)\, x^{1-\sigma'}}{\pi(x)}\right) \;\longrightarrow\; 0 + 0 \;=\; 0.$$

Therefore

$$\lim_{x \to \infty} \frac{u(x)}{\pi(x)} = 0. \qquad \blacksquare$$

---

## Remarks

- The proof relies on the **Mauduit–Rivat (2009)** theorem, a deep result resolving a conjecture of Gelfond concerning the distribution of digit sums of primes. No purely elementary proof is known.
- The key idea is to choose a modulus $m > 9d$ (so that each digit-sum value $q \le 9d$ occupies a *distinct* residue class mod $m$), with $\gcd(m,9)=1$ (so the theorem applies), and with $m = \Theta(\ln x)$ (so $m = x^{o(1)}$, within the uniform range). The equidistribution then gives each prime digit-sum value a $\sim 1/m$ share of all primes, and there are only $\sim 9d/\ln d$ prime values to sum over, yielding $\sim (\ln d)^{-1} \to 0$.
- A stronger result (Drmota–Mauduit–Rivat, 2011) shows that the digit sum of primes is *asymptotically normal* with mean $\frac{9}{2}d$ and variance $\frac{33}{4}d$, from which the same conclusion also follows, but the weaker 2009 equidistribution theorem suffices.
