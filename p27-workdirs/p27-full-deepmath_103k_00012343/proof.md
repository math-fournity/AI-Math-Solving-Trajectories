# Evaluation of $\limsup_{m \to \infty}\left(\limsup_{n \to \infty} \frac{\pi(n+m)-\pi(n)}{\pi(m)}\right)$

## Answer

$$\boxed{e^{-\gamma}}$$

where $\gamma \approx 0.5772$ is the Euler–Mascheroni constant, so $e^{-\gamma} \approx 0.5615$.

## Proof

### Step 1: Reformulation via admissible sets

Let $\pi(x)$ denote the prime counting function. The quantity $\pi(n+m) - \pi(n)$ counts the number of primes in the half-open interval $(n, n+m]$.

**Definition.** A set $S = \{a_1, \ldots, a_k\} \subset \mathbb{Z}$ is called *admissible* if for every prime $p$, the residues $\{a_1 \bmod p, \ldots, a_k \bmod p\}$ do not cover all of $\{0, 1, \ldots, p-1\}$.

**Definition.** Let $k(m) := \max\{ |S| : S \subseteq \{1, 2, \ldots, m\},\; S \text{ is admissible} \}$.

### Step 2: Upper bound — $\limsup_{n\to\infty}(\pi(n+m)-\pi(n)) \leq k(m)$

Suppose for some large $n$ we have $\pi(n+m) - \pi(n) = k$, with the primes being $n + a_1, \ldots, n + a_k$ where $1 \leq a_i \leq m$. We claim $\{a_1, \ldots, a_k\}$ is admissible.

For any prime $p \leq k$: since $n + a_i$ is prime and $n + a_i > n > k \geq p$ (for $n$ sufficiently large), we have $p \nmid (n + a_i)$, hence $a_i \not\equiv -n \pmod{p}$ for all $i$. Thus the set $\{a_1, \ldots, a_k\}$ misses the residue class $-n \pmod{p}$, so it does not cover all of $\mathbb{Z}/p\mathbb{Z}$.

For any prime $p > k$: the set has only $k < p$ elements, so it cannot cover all $p$ residue classes.

Therefore $\{a_1, \ldots, a_k\}$ is admissible, giving $k \leq k(m)$. Since this holds for all sufficiently large $n$:

$$\limsup_{n\to\infty}\bigl(\pi(n+m)-\pi(n)\bigr) \leq k(m).$$

### Step 3: Lower bound — $\limsup_{n\to\infty}(\pi(n+m)-\pi(n)) \geq k(m)$ (under prime $k$-tuple conjecture)

Let $S = \{a_1, \ldots, a_{k(m)}\} \subseteq \{1, \ldots, m\}$ be an admissible set of maximum size. By the **Hardy–Littlewood prime $k$-tuple conjecture** (a suitable generalization of the Bunyakovsky conjecture to systems of linear forms), there exist infinitely many integers $n$ such that all of $n + a_1, \ldots, n + a_{k(m)}$ are simultaneously prime.

For each such $n$, we have $\pi(n+m) - \pi(n) \geq k(m)$. Therefore:

$$\limsup_{n\to\infty}\bigl(\pi(n+m)-\pi(n)\bigr) \geq k(m).$$

Combining Steps 2 and 3:

$$\limsup_{n\to\infty}\bigl(\pi(n+m)-\pi(n)\bigr) = k(m).$$

### Step 4: Asymptotics of $k(m)$

We now determine $k(m)$ asymptotically as $m \to \infty$.

**Constructing a large admissible set.** For each prime $p \leq k$ (where $k = k(m)$ is the target size), exclude exactly one residue class modulo $p$. By the Chinese Remainder Theorem, the set of integers in $\{1, \ldots, m\}$ avoiding all excluded classes has size approximately

$$m \prod_{p \leq k}\left(1 - \frac{1}{p}\right).$$

By **Mertens' theorem**:

$$\prod_{p \leq k}\left(1 - \frac{1}{p}\right) \sim \frac{e^{-\gamma}}{\ln k} \quad \text{as } k \to \infty.$$

The resulting set is admissible (it misses one class per prime $p \leq k$, and for $p > k$ it has fewer than $p$ elements). So:

$$k(m) \geq m \cdot \frac{e^{-\gamma}}{\ln k(m)} \cdot (1 + o(1)).$$

**Optimality.** Conversely, any admissible set of size $k$ in $\{1, \ldots, m\}$ must miss at least one residue class per prime $p \leq k$. By the fundamental lemma of sieve theory, the count of such integers is at most

$$m \prod_{p \leq k}\left(1 - \frac{1}{p}\right) \cdot (1 + o(1)) \sim \frac{e^{-\gamma}\, m}{\ln k}.$$

Setting this equal to $k$:

$$k \sim \frac{e^{-\gamma}\, m}{\ln k}.$$

Since $k = \Theta(m / \ln m)$ (which we verify self-consistently), we have $\ln k \sim \ln m$, yielding:

$$k(m) \sim \frac{e^{-\gamma}\, m}{\ln m}.$$

### Step 5: Final computation

By the **Prime Number Theorem**:

$$\pi(m) \sim \frac{m}{\ln m}.$$

Therefore:

$$\limsup_{m\to\infty} \frac{k(m)}{\pi(m)} = \limsup_{m\to\infty} \frac{e^{-\gamma}\, m / \ln m}{m / \ln m} = e^{-\gamma}.$$

Substituting back:

$$\limsup_{m \to \infty}\left(\limsup_{n \to \infty} \frac{\pi(n+m)-\pi(n)}{\pi(m)}\right) = \limsup_{m\to\infty} \frac{k(m)}{\pi(m)} = e^{-\gamma}.$$

## Summary of key ingredients

| Ingredient | Role |
|---|---|
| Admissibility argument (Step 2) | Upper bound: primes in short intervals form admissible sets (unconditional) |
| Hardy–Littlewood prime $k$-tuple conjecture (Step 3) | Lower bound: admissible sets are realized as prime constellations (conjectural, = generalized Bunyakovsky) |
| Mertens' theorem (Step 4) | Asymptotic density of sifted sets: $\prod_{p\leq k}(1-1/p) \sim e^{-\gamma}/\ln k$ |
| Prime Number Theorem (Step 5) | $\pi(m) \sim m/\ln m$ |

The constant $e^{-\gamma}$ arises from the Mertens product, reflecting the maximal density of an admissible set relative to the density of primes.
