# Proof

**Question.** Does there exist an infinite sequence of distinct primes $(q)$, with $p \neq q$, such that the modular product $\prod_{q \leq Q} q \pmod{p}$ asymptotically stays in a small subset of $\{1, 2, \dots, p-1\}$ as $Q$ increases, say a subset of size $\delta p$ for some small constant $\delta > 0$?

**Answer.** $\boxed{\text{Yes}}$.

---

## Construction

Fix a prime $p$. Consider the sequence of all primes $q$ (in increasing order) satisfying
$$
q \equiv 1 \pmod{p}, \qquad q \neq p.
$$

By **Dirichlet's theorem on primes in arithmetic progressions**, since $\gcd(1, p) = 1$, the arithmetic progression $1 \pmod{p}$ contains infinitely many primes. Hence this sequence is infinite and consists of distinct primes, none equal to $p$ (since $p \equiv 0 \pmod{p}$, not $1$).

## Partial products stay in $\{1\}$

For any cutoff $Q$, let $N(Q) = \#\{q \leq Q : q \text{ prime}, \ q \equiv 1 \pmod{p}\}$. The partial product is
$$
\prod_{\substack{q \leq Q \\ q \equiv 1 \pmod{p}}} q \equiv \prod_{i=1}^{N(Q)} 1 \equiv 1 \pmod{p}.
$$

Thus the partial product is **identically** $1 \pmod{p}$ for every $Q$. It stays in the singleton subset $\{1\} \subset \{1, 2, \dots, p-1\}$, which has size $1$.

## Satisfying the $\delta p$ bound

For any $\delta > 0$ and any prime $p > 1/\delta$, we have $1 \leq \delta p$, so the subset $\{1\}$ has size at most $\delta p$. Hence the construction satisfies the required bound for all sufficiently large $p$ (namely $p > 1/\delta$).

## Generalization (optional): subgroups of controlled size

More generally, let $g$ be a primitive root modulo $p$, so $(\mathbb{Z}/p\mathbb{Z})^{*} = \langle g \rangle$ is cyclic of order $p-1$. Fix any $d \in \{1, \dots, p-1\}$ and consider the sequence of all primes $q$ satisfying
$$
q \equiv g^{d} \pmod{p}.
$$

Since $\gcd(g^{d} \bmod p, \, p) = 1$, Dirichlet's theorem again guarantees infinitely many such primes. For this sequence, every factor contributes a factor of $g^{d}$, so the partial product is
$$
\prod_{\substack{q \leq Q \\ q \equiv g^{d} \pmod{p}}} q \equiv (g^{d})^{N(Q)} \pmod{p},
$$
which lies in the cyclic subgroup $\langle g^{d} \rangle \subseteq (\mathbb{Z}/p\mathbb{Z})^{*}$ of order
$$
\frac{p-1}{\gcd(d,\, p-1)}.
$$

By choosing $d$ with $\gcd(d, p-1)$ large, this subgroup can be made as small as desired. Concretely, for any $\delta > 0$, choosing $d = p-1$ gives the trivial subgroup $\{1\}$ of size $1 \leq \delta p$ (for $p > 1/\delta$), and choosing $d = (p-1)/k$ for any divisor $k$ of $p-1$ with $k \leq \delta p$ gives a subgroup of size $k \leq \delta p$.

## Conclusion

The sequence of all primes $q \equiv 1 \pmod{p}$ (with $q \neq p$) is an infinite sequence of distinct primes whose partial products modulo $p$ remain identically equal to $1$, hence stay in a subset of $\{1, \dots, p-1\}$ of size $1 \leq \delta p$ for every $\delta > 0$ and every prime $p > 1/\delta$.

### PROOF COMPLETE
