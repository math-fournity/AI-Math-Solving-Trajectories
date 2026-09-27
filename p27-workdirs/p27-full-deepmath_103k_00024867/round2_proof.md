# Non-vanishing of $H^1_{\text{cont}}(\operatorname{Gal}(L/K), L^\times)$ for Infinite Algebraic Extensions

## Answer

$$\boxed{H^1_{\text{cont}}(\operatorname{Gal}(L/K),\, L^\times) \neq 0 \text{ in general. It vanishes for finite Galois extensions but can be nonzero for infinite Galois extensions } L/K \text{ of } \mathbb{Q}_p.}$$

## Proof

### Step 1: Finite Galois extensions — $H^1 = 0$ (Hilbert 90)

Let $L/K$ be a **finite** Galois extension with $G = \operatorname{Gal}(L/K)$. Since $G$ is finite, it carries the discrete topology. A $1$-cocycle $f: G \to L^\times$ has finite image (as $G$ is finite), hence is automatically continuous regardless of the topology on $L^\times$. Therefore:

$$H^1_{\text{cont}}(G, L^\times) = H^1(G, L^\times) = 0$$

by Hilbert's Theorem 90. $\checkmark$

### Step 2: Infinite Galois extensions — the key obstruction

For an **infinite** Galois extension $L/K$ with $G = \operatorname{Gal}(L/K)$ profinite, the situation differs fundamentally depending on the topology:

- **Discrete topology on $L^\times$**: A continuous cocycle $f: G \to L^\times_{\text{disc}}$ must be locally constant, hence factors through some finite quotient $G/N$. By Hilbert 90 for the finite subextension $L^N/K$, the cocycle is a coboundary. So $H^1_{\text{cont}}(G, L^\times_{\text{disc}}) = 0$.

- **$p$-adic topology on $L^\times$**: Continuity is a **weaker** condition (the $p$-adic topology is coarser than the discrete topology), so there are **more** continuous cocycles. The factoring-through-finite-quotients argument fails, and indeed $H^1$ can be nonzero.

### Step 3: Counterexample — the $\mathbb{Z}_p$-extension

Let $K = \mathbb{Q}_p$ and let $L$ be the (unique) $\mathbb{Z}_p$-extension of $K$, i.e., the unique Galois extension $L/K$ with $\operatorname{Gal}(L/K) \cong \mathbb{Z}_p$. (This exists by local class field theory; for $p$ odd it is the subextension of $\mathbb{Q}_p(\mu_{p^\infty})$ fixed by the prime-to-$p$ torsion in $\mathbb{Z}_p^\times$.) Write $L = \bigcup_{n \geq 0} L_n$ where $[L_n : K] = p^n$ and $\operatorname{Gal}(L_n/K) \cong \mathbb{Z}/p^n\mathbb{Z}$.

Set $G = \operatorname{Gal}(L/K) \cong \mathbb{Z}_p$ and fix a topological generator $\gamma$ (so $\chi: G \xrightarrow{\;\sim\;} \mathbb{Z}_p$ with $\chi(\gamma) = 1$).

**Choice of element.** Let $e = 1$ if $p$ is odd, and $e = 2$ if $p = 2$. Set $u = 1 + p^e \in K^\times$. Note:
- $u \in 1 + p^e \mathbb{Z}_p \setminus \{1\}$,
- $u$ is **not** a root of unity in $\mathbb{Q}_p$ (the only roots of unity in $\mathbb{Q}_p$ are $\mu_{p-1}$ for $p$ odd, and $\{\pm 1\}$ for $p = 2$; in either case $u \neq 1$ and $u$ is not a root of unity).

**Construction of the cocycle.** Define $f: G \to L^\times$ by

$$f(\sigma) = u^{\chi(\sigma)} := \exp\!\bigl(\chi(\sigma) \cdot \log_p(u)\bigr),$$

where $\log_p$ is the $p$-adic logarithm and $\exp$ is the $p$-adic exponential.

**Continuity.** Since $u = 1 + p^e$, we have $v_p(\log_p(u)) = e$. For $p$ odd ($e=1$), $\exp$ converges on $p\mathbb{Z}_p$ and $\chi(\sigma)\log_p(u) \in p\mathbb{Z}_p$ for all $\sigma \in \mathbb{Z}_p$. For $p = 2$ ($e = 2$), $\exp$ converges on $4\mathbb{Z}_2$ and $\chi(\sigma)\log_p(u) \in 4\mathbb{Z}_2$. In both cases, $f: \mathbb{Z}_p \to 1 + p^e\mathbb{Z}_p \subset K^\times \subset L^\times$ is a well-defined continuous map (composition of continuous maps $\chi$, scalar multiplication, $\exp$). $\checkmark$

**Cocycle condition.** Since $u \in K^\times$, every $\sigma \in G$ acts trivially on $u$: $\sigma(u) = u$. Therefore $\sigma(f(\tau)) = \sigma(u^{\chi(\tau)}) = u^{\chi(\tau)} = f(\tau)$. The cocycle condition becomes:

$$f(\sigma\tau) = u^{\chi(\sigma\tau)} = u^{\chi(\sigma) + \chi(\tau)} = u^{\chi(\sigma)} \cdot u^{\chi(\tau)} = f(\sigma) \cdot \sigma(f(\tau)). \quad \checkmark$$

**Not a coboundary.** Suppose for contradiction that $f$ is a coboundary: $f(\sigma) = \sigma(b)/b$ for some $b \in L^\times$. Since $L = \bigcup_n L_n$, we have $b \in L_m^\times$ for some $m \geq 0$.

Restricting to $G_m = \operatorname{Gal}(L_m/K) \cong \mathbb{Z}/p^m\mathbb{Z}$: for every $\sigma \in G_m$,

$$\frac{\sigma(b)}{b} = f(\sigma) = u^{\chi_m(\sigma)},$$

where $\chi_m: G_m \to \mathbb{Z}/p^m\mathbb{Z}$ is the reduction of $\chi$. Taking the norm $N_{L_m/K}$ of both sides:

$$1 = N_{L_m/K}\!\left(\frac{\sigma(b)}{b}\right) = N_{L_m/K}\!\left(u^{\chi_m(\sigma)}\right) = u^{[L_m:K]\cdot \chi_m(\sigma)} = u^{p^m \cdot \chi_m(\sigma)}.$$

Since $\chi_m$ is surjective onto $\mathbb{Z}/p^m\mathbb{Z}$, we may choose $\sigma$ with $\chi_m(\sigma) = 1$, yielding:

$$u^{p^m} = 1 \quad \text{in } K^\times = \mathbb{Q}_p^\times.$$

But $u = 1 + p^e$ is **not a root of unity** in $\mathbb{Q}_p$, so $u^{p^m} \neq 1$ for any $m \geq 0$. **Contradiction.** $\checkmark$

### Step 4: Valuation argument (why the cocycle lands in units)

For completeness, we verify that **any** continuous cocycle $f: G \to L^\times$ (with $p$-adic topology) automatically takes values in $\mathcal{O}_L^\times$, confirming that the obstruction lies entirely in the unit group.

The valuation $v_L: L^\times \to \mathbb{R}$, $v_L(x) = -\log_p |x|_p$, is continuous for the $p$-adic topology on $L^\times$ and the usual topology on $\mathbb{R}$. Since $v_L$ is $G$-equivariant (Galois automorphisms preserve the valuation) with trivial $G$-action on the target, the composition $v_L \circ f: G \to \mathbb{R}$ is a **continuous group homomorphism** from the compact group $G$ to $\mathbb{R}$. The image is a compact subgroup of $\mathbb{R}$, hence $\{0\}$. So $v_L(f(\sigma)) = 0$ for all $\sigma$, i.e., $f$ takes values in $\mathcal{O}_L^\times$.

This shows $H^1_{\text{cont}}(G, L^\times) \cong H^1_{\text{cont}}(G, \mathcal{O}_L^\times)$, and the nonvanishing comes from the profinite (inverse-limit) structure of $\mathcal{O}_L^\times$ under the $p$-adic topology, which prevents the direct-limit argument used in the discrete case.

### Conclusion

- For **finite** Galois $L/K$: $H^1_{\text{cont}}(\operatorname{Gal}(L/K), L^\times) = 0$ (Hilbert 90).
- For **infinite** Galois $L/K$: $H^1_{\text{cont}}(\operatorname{Gal}(L/K), L^\times)$ **can be nonzero**. Explicitly, for the $\mathbb{Z}_p$-extension $L/\mathbb{Q}_p$, the cocycle $f(\sigma) = (1+p^e)^{\chi(\sigma)}$ defines a nontrivial class.

The essential difference from the classical (discrete topology) Hilbert 90 is that the $p$-adic topology permits continuous cocycles that do **not** factor through any finite quotient of $G$, and the $p$-adic exponential provides a mechanism to construct such cocycles from elements of $1 + p^e\mathbb{Z}_p$ that are not roots of unity.

$$\boxed{H^1_{\text{cont}}(\operatorname{Gal}(L/K),\, L^\times) \text{ does not vanish in general for algebraic extensions } L/K \text{ of } \mathbb{Q}_p.}$$
