# Proof: Primitive element with conductor coprime to a given ideal

## Answer

**No**, in general such $\theta$ does not exist. We give an explicit counterexample.

## Key Observation

The existence of $\theta$ with $J + \mathfrak{f} = B$ requires, at each prime $\mathfrak{P} \mid J$, that $B_\mathfrak{P} = A_\mathfrak{p}[\theta]$ (where $\mathfrak{p} = \mathfrak{P} \cap A$). This is because:

$$\mathfrak{f} \not\subseteq \mathfrak{P} \iff \mathfrak{f}_\mathfrak{P} = B_\mathfrak{P} \iff B_\mathfrak{P} = A_\mathfrak{p}[\theta].$$

In turn, $B_\mathfrak{P} = A_\mathfrak{p}[\theta]$ implies (reducing modulo $\mathfrak{p}$):

$$\kappa(\mathfrak{P}) = B_\mathfrak{P}/\mathfrak{p}B_\mathfrak{P} = \kappa(\mathfrak{p})[\bar{\theta}],$$

so the residue field extension $\kappa(\mathfrak{P})/\kappa(\mathfrak{p})$ must be **simple**. If we can produce a separable extension $L/K$ where some prime $\mathfrak{P}$ has a non-simple residue field extension, then $B_\mathfrak{P}$ is not monogenic over $A_\mathfrak{p}$, and taking $J = \mathfrak{P}$ yields a counterexample.

## Counterexample

### Setup

Let $p$ be a prime. Set:
- $A = \mathbb{F}_p(u, v)[t]$, a PID (polynomial ring over a field), hence a Dedekind domain.
- $K = \operatorname{Frac}(A) = \mathbb{F}_p(u, v, t)$.
- $\alpha, \beta$ are roots of $f(X) = X^p + tX + u$ and $g(X) = X^p + tX + v$ respectively.
- $L = K(\alpha, \beta)$.

### Step 1: $L/K$ is finite separable

The derivatives $f'(X) = t \neq 0$ and $g'(X) = t \neq 0$ in $K$, so $\alpha$ is separable over $K$ and $\beta$ is separable over $K(\alpha)$. Thus $L/K$ is separable.

### Step 2: $[L:K] = p^2$

**$f(X) = X^p + tX + u$ is irreducible over $K$:** Its reduction modulo $\mathfrak{p} = (t)$ is $\bar{f}(X) = X^p + u$, which is irreducible over $\kappa(\mathfrak{p}) = \mathbb{F}_p(u, v)$ (since $u$ is not a $p$-th power in $\mathbb{F}_p(u,v)$, as $u, v$ are algebraically independent). Since $f$ is monic and its reduction is irreducible of the same degree, $f$ is irreducible over $K$ (Gauss's lemma + degree preservation for monic polynomials). So $[K(\alpha) : K] = p$.

**$g(X) = X^p + tX + v$ is irreducible over $K(\alpha)$:** In $K(\alpha)$, the prime $\mathfrak{p} = (t)$ extends to a prime $\mathfrak{P}'$ with residue field $\kappa(\mathfrak{P}') = \mathbb{F}_p(u^{1/p}, v)$ (since $\bar{\alpha}^p = u$, so $\bar{\alpha} = u^{1/p}$). The reduction of $g$ modulo $\mathfrak{P}'$ is $\bar{g}(X) = X^p + v$, irreducible over $\mathbb{F}_p(u^{1/p}, v)$ (since $v$ is not a $p$-th power in this field, as $v^{1/p} \notin \mathbb{F}_p(u^{1/p}, v)$). So $g$ is irreducible over $K(\alpha)$, giving $[L : K(\alpha)] = p$.

Therefore $[L:K] = p^2$.

### Step 3: Local structure at $\mathfrak{p} = (t)$

Over $\mathfrak{p} = (t)$:
- In $K(\alpha)/K$: $\bar{f} = X^p + u$ is irreducible, so there is a unique prime $\mathfrak{P}'$ over $\mathfrak{p}$ with $e(\mathfrak{P}'/\mathfrak{p}) = 1$, $f(\mathfrak{P}'/\mathfrak{p}) = p$.
- In $L/K(\alpha)$: $\bar{g} = X^p + v$ is irreducible over $\kappa(\mathfrak{P}')$, so there is a unique prime $\mathfrak{P}$ over $\mathfrak{P}'$ with $e(\mathfrak{P}/\mathfrak{P}') = 1$, $f(\mathfrak{P}/\mathfrak{P}') = p$.

Over $\mathfrak{p}$: $e(\mathfrak{P}/\mathfrak{p}) = 1$, $f(\mathfrak{P}/\mathfrak{p}) = p^2$.

The residue field is:
$$\kappa(\mathfrak{P}) = \mathbb{F}_p(u^{1/p}, v^{1/p}), \quad \kappa(\mathfrak{p}) = \mathbb{F}_p(u, v).$$

### Step 4: The residue field extension is not simple

For any $a \in \kappa(\mathfrak{P}) = \mathbb{F}_p(u^{1/p}, v^{1/p})$, write $a = \sum_{i,j \in \{0,1\}} c_{ij}\, u^{i/p} v^{j/p}$ with $c_{ij} \in \mathbb{F}_p(u, v)$. Then by the Frobenius (a ring homomorphism in characteristic $p$):

$$a^p = \sum_{i,j} c_{ij}^p\, u^i v^j \in \mathbb{F}_p(u^p, v^p) \subseteq \mathbb{F}_p(u, v) = \kappa(\mathfrak{p}).$$

So $a^p \in \kappa(\mathfrak{p})$ for every $a \in \kappa(\mathfrak{P})$, which means $[\kappa(\mathfrak{p})(a) : \kappa(\mathfrak{p})] \leq p$ (the minimal polynomial of $a$ divides $X^p - a^p$). Since $[\kappa(\mathfrak{P}) : \kappa(\mathfrak{p})] = p^2 > p$, **no single element generates** $\kappa(\mathfrak{P})$ over $\kappa(\mathfrak{p})$.

### Step 5: $B_\mathfrak{P}$ is not monogenic over $A_\mathfrak{p}$

Suppose for contradiction that $B_\mathfrak{P} = A_\mathfrak{p}[\theta]$ for some $\theta$. Since $e = 1$, we have $\mathfrak{p} B_\mathfrak{P} = \mathfrak{P}$, so:

$$\kappa(\mathfrak{P}) = B_\mathfrak{P}/\mathfrak{P} = B_\mathfrak{P}/\mathfrak{p}B_\mathfrak{P} = A_\mathfrak{p}[\theta]/\mathfrak{p}A_\mathfrak{p}[\theta] = \kappa(\mathfrak{p})[\bar{\theta}].$$

This would make $\kappa(\mathfrak{P})/\kappa(\mathfrak{p})$ a simple extension, contradicting Step 4. $\contradiction$

### Step 6: Taking $J = \mathfrak{P}$, no $\theta$ satisfies the conditions

For any $\theta \in B$ (primitive or not), since $B_\mathfrak{P} \neq A_\mathfrak{p}[\theta]$, the conductor satisfies $\mathfrak{f} \subseteq \mathfrak{P}$. Therefore:

$$J + \mathfrak{f} = \mathfrak{P} + \mathfrak{f} \subseteq \mathfrak{P} \subsetneq B.$$

So $J$ is **not** coprime to $\mathfrak{f}$, for every choice of $\theta$.

## Conclusion

The answer is $\boxed{No}$: in general, there does not exist such a $\theta$.

**Remark.** The answer becomes **Yes** under the additional hypothesis that all residue fields of $A$ are perfect (e.g., $A = \mathbb{Z}$, or $A = k[t]$ with $k$ perfect). In that case, every finite residue field extension is separable, hence simple (by the primitive element theorem), and the local monogenicity lemma goes through: one combines local generators via CRT, uses Nakayama's lemma to lift to $B_\mathfrak{P} = A_\mathfrak{p}[\theta]$, and uses the infinitude of $K$ (together with the finiteness of intermediate fields) to ensure primitivity. The counterexample shows this hypothesis cannot be dropped.

### PROOF COMPLETE
