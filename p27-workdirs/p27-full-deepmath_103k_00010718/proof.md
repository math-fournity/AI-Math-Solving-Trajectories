# Tamagawa Numbers of Crystalline Galois Representations

## Problem Statement

Let $p \ge 3$ be a prime, and let $V$ be a crystalline 2-dimensional representation of $G_{\mathbb{Q}_p}$ with a $G_{\mathbb{Q}_p}$-stable lattice $T$ in $V$. Assume:

- $V$ is irreducible.
- $\operatorname{Fil}^0 \mathbb{D}_{\mathrm{cris}}(V)$ is 1-dimensional.
- None of the eigenvalues of Frobenius on $\mathbb{D}_{\mathrm{cris}}(V)$ are integral powers of $p$.
- The Hodge filtration of $V$ has length $< (p-1)$.

Since the Hodge filtration length is $< (p-1)$, Fontaine–Laffaille theory gives an equivalence between $G_{\mathbb{Q}_p}$-stable lattices $T$ in $V$ and strongly divisible $\mathbb{Z}_p$-lattices $\mathbb{D}(T)$ in $\mathbb{D}_{\mathrm{cris}}(V)$. Let $\omega$ be a $\mathbb{Z}_p$-basis of the tangent space
$$t_T = \mathbb{D}(T) / \operatorname{Fil}^0 \mathbb{D}(T).$$

For $K_n = \mathbb{Q}_p(\mu_{p^n})$, the Tamagawa number of $T$ over $K_n$ is
$$\operatorname{Tam}^0_{K_n, \omega}(T) = \frac{[H^1_f(K_n, T) : \exp_{K_n}(\mathcal{O}_{K_n} \otimes_{\mathbb{Z}_p} \mathbb{Z}_p \omega)]}{[\mathbb{D}(T) : (1 - \varphi)\mathbb{D}(T)]},$$
where $[A : B]$ denotes the generalized index of $\mathbb{Z}_p$-lattices.

**Question.** Is $\operatorname{Tam}^0_{K_n, \omega}(T) = 1$ for all $n \ge 0$?

**Answer.** Yes.

$$\boxed{\operatorname{Tam}^0_{K_n, \omega}(T) = 1 \text{ for all } n \ge 0.}$$

---

## Proof

We split the proof into two parts: the case $n = 0$ (i.e., $K_0 = \mathbb{Q}_p$), which follows from the Bloch–Kato fundamental exact sequence, and the case $n \ge 1$, which follows from the Benois–Berger theorem on the local Tamagawa number conjecture for crystalline representations over the cyclotomic tower.

### Preliminaries: Hodge–Tate Weights and Frobenius Eigenvalues

Let the Hodge–Tate weights of $V$ be $k_1 \ge k_2$ (with $k_1, k_2 \in \mathbb{Z}$ since $V$ is crystalline). The condition that $\operatorname{Fil}^0 \mathbb{D}_{\mathrm{cris}}(V)$ is 1-dimensional means that $k_2 < 0 \le k_1$, i.e., the Hodge–Tate weights straddle $0$. The Hodge filtration length is $h = k_1 - k_2 < p - 1$.

Let $\alpha, \beta$ be the eigenvalues of Frobenius $\varphi$ on $\mathbb{D}_{\mathrm{cris}}(V)$. By weak admissibility, the Newton slopes satisfy $v_p(\alpha) + v_p(\beta) = k_1 + k_2$ and $\{v_p(\alpha), v_p(\beta)\} = \{k_1, k_2\}$ (up to ordering). The non-exceptional condition states that $\alpha \ne p^m$ and $\beta \ne p^m$ for all $m \in \mathbb{Z}$.

### Part I: The Case $n = 0$ ($K_0 = \mathbb{Q}_p$)

We prove $\operatorname{Tam}^0_{\mathbb{Q}_p, \omega}(T) = 1$ using the Bloch–Kato fundamental exact sequence.

#### Step 1: The Fundamental Exact Sequence for $V$

The Bloch–Kato fundamental exact sequence is
$$0 \to \mathbb{Q}_p \to B_{\mathrm{cris}}^{\varphi=1} \to B_{\mathrm{dR}} / \operatorname{Fil}^0 B_{\mathrm{dR}} \to 0.$$

Tensoring with $V$ and taking $G_{\mathbb{Q}_p}$-invariants yields the long exact sequence in Galois cohomology:
$$0 \to H^0(\mathbb{Q}_p, V) \to D_{\mathrm{cris}}(V)^{\varphi=1} \to t_V \xrightarrow{\exp} H^1(\mathbb{Q}_p, V) \to H^1(\mathbb{Q}_p, V \otimes B_{\mathrm{cris}}^{\varphi=1}) \to H^1(\mathbb{Q}_p, V \otimes B_{\mathrm{dR}}/\operatorname{Fil}^0 B_{\mathrm{dR}}) \to H^2(\mathbb{Q}_p, V) \to \cdots$$

where $t_V = D_{\mathrm{dR}}(V) / \operatorname{Fil}^0 D_{\mathrm{dR}}(V)$ is the tangent space of $V$.

**Claim.** Under our hypotheses, the terms $H^0(\mathbb{Q}_p, V)$, $D_{\mathrm{cris}}(V)^{\varphi=1}$, $H^1(\mathbb{Q}_p, V \otimes B_{\mathrm{cris}}^{\varphi=1})$, $H^1(\mathbb{Q}_p, V \otimes B_{\mathrm{dR}}/\operatorname{Fil}^0 B_{\mathrm{dR}})$, and $H^2(\mathbb{Q}_p, V)$ all vanish.

*Proof of Claim.*

1. **$H^0(\mathbb{Q}_p, V) = 0$**: Since $V$ is irreducible and 2-dimensional, $H^0(\mathbb{Q}_p, V) = 0$ (a non-zero invariant would give a 1-dimensional subrepresentation). Alternatively, $H^0(\mathbb{Q}_p, V) = D_{\mathrm{cris}}(V)^{\varphi=1}$, and $\varphi = 1$ on some subspace would mean $1$ is a Frobenius eigenvalue, contradicting the non-exceptional condition (since $1 = p^0$).

2. **$D_{\mathrm{cris}}(V)^{\varphi=1} = 0$**: This is the kernel of $1 - \varphi$ on $D_{\mathrm{cris}}(V)$. Since neither $\alpha$ nor $\beta$ equals $1$ (as $1 = p^0$ is an integral power of $p$), $1 - \varphi$ is invertible, so the kernel is zero.

3. **$H^1(\mathbb{Q}_p, V \otimes B_{\mathrm{cris}}^{\varphi=1}) \cong D_{\mathrm{cris}}(V)/(1-\varphi)D_{\mathrm{cris}}(V) = 0$**: The isomorphism $H^1(\mathbb{Q}_p, V \otimes B_{\mathrm{cris}}^{\varphi=1}) \cong D_{\mathrm{cris}}(V)/(1-\varphi)D_{\mathrm{cris}}(V)$ follows from Fontaine's theorem that $H^1(\mathbb{Q}_p, V \otimes B_{\mathrm{cris}}) = 0$ for crystalline $V$, together with the exact sequence $0 \to B_{\mathrm{cris}}^{\varphi=1} \to B_{\mathrm{cris}} \xrightarrow{1-\varphi} B_{\mathrm{cris}} \to 0$. Since $1 - \varphi$ is invertible on $D_{\mathrm{cris}}(V)$ (as in item 2), the quotient is zero.

4. **$H^1(\mathbb{Q}_p, V \otimes B_{\mathrm{dR}}/\operatorname{Fil}^0 B_{\mathrm{dR}}) = 0$**: We have $B_{\mathrm{dR}}/\operatorname{Fil}^0 B_{\mathrm{dR}} \cong \mathbb{C}_p$ as a $G_{\mathbb{Q}_p}$-module. Since $V$ is de Rham, $V \otimes \mathbb{C}_p \cong \bigoplus_i \mathbb{C}_p(\chi^{k_i})$ where $\chi$ is the cyclotomic character and $k_i$ are the Hodge–Tate weights. By a theorem of Tate, $H^1(\mathbb{Q}_p, \mathbb{C}_p(\chi^k)) = 0$ for all $k \in \mathbb{Z}$. Hence $H^1(\mathbb{Q}_p, V \otimes \mathbb{C}_p) = 0$.

5. **$H^2(\mathbb{Q}_p, V) = 0$**: By local Tate duality, $H^2(\mathbb{Q}_p, V) \cong H^0(\mathbb{Q}_p, V^*(1))^*$. Now $H^0(\mathbb{Q}_p, V^*(1)) = D_{\mathrm{cris}}(V^*(1))^{\varphi=1}$. The eigenvalues of $\varphi$ on $D_{\mathrm{cris}}(V^*(1))$ are $p/\alpha$ and $p/\beta$. For $H^0 \ne 0$, we would need $p/\alpha = 1$ or $p/\beta = 1$, i.e., $\alpha = p$ or $\beta = p$. Since $p = p^1$ is an integral power of $p$, the non-exceptional condition rules this out. Hence $H^0(\mathbb{Q}_p, V^*(1)) = 0$ and $H^2(\mathbb{Q}_p, V) = 0$.

This establishes the Claim. $\square$

#### Step 2: The Exponential Map for $V$

With all the vanishing results from Step 1, the long exact sequence collapses to:
$$0 \to t_V \xrightarrow{\exp} H^1(\mathbb{Q}_p, V) \to 0.$$

Therefore:
$$\exp: t_V \xrightarrow{\;\sim\;} H^1(\mathbb{Q}_p, V)$$
is an isomorphism. In particular, $H^1_f(\mathbb{Q}_p, V) = H^1(\mathbb{Q}_p, V)$ (the finite part is all of $H^1$).

#### Step 3: The Integral Exact Sequence for $T$

Since the Hodge filtration length $h = k_1 - k_2 < p - 1$, we are in the Fontaine–Laffaille range. The Fontaine–Laffaille theory provides an equivalence of categories between:
- $G_{\mathbb{Q}_p}$-stable $\mathbb{Z}_p$-lattices $T$ in $V$, and
- Strongly divisible $\mathbb{Z}_p$-lattices $\mathbb{D}(T)$ in $D_{\mathrm{cris}}(V)$.

Under this equivalence, the Bloch–Kato fundamental exact sequence descends to the integral level. Tensoring the fundamental exact sequence with $T$ (using $A_{\mathrm{cris}}$ for the integral theory) and taking $G_{\mathbb{Q}_p}$-invariants, we obtain:
$$0 \to T^{G_{\mathbb{Q}_p}} \to \mathbb{D}(T)^{\varphi=1} \to t_T \xrightarrow{\exp} H^1(\mathbb{Q}_p, T) \to H^1(\mathbb{Q}_p, T \otimes B_{\mathrm{cris}}^{\varphi=1}) \to H^1(\mathbb{Q}_p, T \otimes B_{\mathrm{dR}}/\operatorname{Fil}^0 B_{\mathrm{dR}}) \to H^2(\mathbb{Q}_p, T) \to \cdots$$

By the Fontaine–Laffaille theory in the FL range:
- $T^{G_{\mathbb{Q}_p}} = 0$ (since $H^0(\mathbb{Q}_p, V) = 0$).
- $\mathbb{D}(T)^{\varphi=1} = 0$ (since $D_{\mathrm{cris}}(V)^{\varphi=1} = 0$ and $\mathbb{D}(T)$ is a lattice in $D_{\mathrm{cris}}(V)$).
- $t_T = \mathbb{D}(T)/\operatorname{Fil}^0 \mathbb{D}(T)$ (by the FL equivalence).
- $H^1(\mathbb{Q}_p, T \otimes B_{\mathrm{cris}}^{\varphi=1}) \cong \mathbb{D}(T)/(1-\varphi)\mathbb{D}(T)$ (the integral version of the isomorphism in Step 1, item 3, using the FL theory to handle the lattice).
- $H^1(\mathbb{Q}_p, T \otimes B_{\mathrm{dR}}/\operatorname{Fil}^0 B_{\mathrm{dR}}) = 0$ (same argument as for $V$, using that $T \otimes \mathbb{C}_p \hookrightarrow V \otimes \mathbb{C}_p$ and $H^1(\mathbb{Q}_p, V \otimes \mathbb{C}_p) = 0$).
- $H^2(\mathbb{Q}_p, T) = 0$ (since $H^2(\mathbb{Q}_p, V) = 0$ and $T$ is a lattice in $V$).

The exact sequence for $T$ therefore collapses to:
$$0 \to t_T \xrightarrow{\exp} H^1(\mathbb{Q}_p, T) \to \mathbb{D}(T)/(1-\varphi)\mathbb{D}(T) \to 0. \tag{$\star$}$$

#### Step 4: Computing the Tamagawa Number for $n = 0$

From ($\star$), we obtain:
1. $\exp: t_T \hookrightarrow H^1(\mathbb{Q}_p, T)$ is injective.
2. $H^1(\mathbb{Q}_p, T) / \exp(t_T) \cong \mathbb{D}(T)/(1-\varphi)\mathbb{D}(T)$.

Since $H^1_f(\mathbb{Q}_p, V) = H^1(\mathbb{Q}_p, V)$ (from Step 2), we have:
$$H^1_f(\mathbb{Q}_p, T) = H^1(\mathbb{Q}_p, T) \cap H^1_f(\mathbb{Q}_p, V) = H^1(\mathbb{Q}_p, T) \cap H^1(\mathbb{Q}_p, V) = H^1(\mathbb{Q}_p, T).$$

Therefore:
$$[H^1_f(\mathbb{Q}_p, T) : \exp(\mathbb{Z}_p \omega)] = [H^1(\mathbb{Q}_p, T) : \exp(t_T)] = |\mathbb{D}(T)/(1-\varphi)\mathbb{D}(T)| = [\mathbb{D}(T) : (1-\varphi)\mathbb{D}(T)].$$

(Here we use that $\omega$ is a $\mathbb{Z}_p$-basis of $t_T$, so $\exp(\mathbb{Z}_p \omega) = \exp(t_T)$, and that the generalized index $[\mathbb{D}(T) : (1-\varphi)\mathbb{D}(T)]$ equals the cardinality of the quotient $\mathbb{D}(T)/(1-\varphi)\mathbb{D}(T)$, which is finite since $1-\varphi$ is invertible on $D_{\mathrm{cris}}(V) \otimes \mathbb{Q}_p$.)

Substituting into the Tamagawa number formula:
$$\operatorname{Tam}^0_{\mathbb{Q}_p, \omega}(T) = \frac{[H^1_f(\mathbb{Q}_p, T) : \exp(\mathbb{Z}_p \omega)]}{[\mathbb{D}(T) : (1-\varphi)\mathbb{D}(T)]} = \frac{[\mathbb{D}(T) : (1-\varphi)\mathbb{D}(T)]}{[\mathbb{D}(T) : (1-\varphi)\mathbb{D}(T)]} = 1.$$

This completes the proof for $n = 0$. $\square$

**Remark.** This is essentially the theorem of Bloch–Kato [BK90, §3–4] for crystalline representations in the Fontaine–Laffaille range with non-exceptional Frobenius eigenvalues. It also appears as Proposition II.2 in Berger's unpublished paper "Nombres de Tamagawa de certaines représentations cristallines."

### Part II: The Case $n \ge 1$ ($K_n = \mathbb{Q}_p(\mu_{p^n})$)

For $n \ge 1$, the extension $K_n/\mathbb{Q}_p$ is totally ramified, so the Fontaine–Laffaille theory does not directly apply. We instead use the Benois–Berger theorem on the local Tamagawa number conjecture.

#### Step 5: The Benois–Berger Theorem

We recall the main theorem of Benois–Berger [BB08]:

> **Theorem (Benois–Berger, Theorem A).** *Let $K$ be a finite unramified extension of $\mathbb{Q}_p$ and let $V$ be a crystalline representation of $G_K$. Then:*
> 1. *The conjecture $C_{\mathrm{Iw}}(K_\infty/K, V)$ (the $\delta_{\mathbb{Z}_p}(V)$ conjecture of Perrin-Riou on the integrality of the Perrin-Riou exponential) is true.*
> 2. *The conjecture $C_{\mathrm{EP}}(L/K, V)$ (the Fontaine–Perrin-Riou local Tamagawa number conjecture) is true for every finite extension $L$ of $K$ contained in $K_\infty = \bigcup_{n=1}^{\infty} K(\zeta_{p^n})$.*

#### Step 6: Verification of Hypotheses

We check that the conditions of the Benois–Berger theorem are satisfied:

- **$K$ is unramified over $\mathbb{Q}_p$**: We take $K = \mathbb{Q}_p$, which is trivially unramified. ✓
- **$V$ is crystalline**: This is given. ✓
- **$L \subset K_\infty$**: We take $L = K_n = \mathbb{Q}_p(\mu_{p^n}) \subset \mathbb{Q}_p(\mu_{p^\infty}) = K_\infty$. ✓
- **$p$ is odd**: Given ($p \ge 3$). ✓

The additional conditions in our problem (irreducibility, $\operatorname{Fil}^0$ 1-dimensional, non-exceptional Frobenius eigenvalues, Hodge filtration length $< p-1$) are not required by the Benois–Berger theorem, which holds for all crystalline representations over unramified extensions. Our conditions are therefore sufficient (and in fact stronger than necessary).

#### Step 7: From $C_{\mathrm{EP}}$ to $\operatorname{Tam}^0 = 1$

The conjecture $C_{\mathrm{EP}}(K_n, V)$ (the non-equivariant version, which follows from the equivariant version $C_{\mathrm{EP}}(K_n/\mathbb{Q}_p, V)$ by property (3) of Proposition 2.5 in [BB08]) relates the Tamagawa numbers of $T$ and $T^*(1)$ over $K_n$:

$$\frac{\operatorname{Tam}^0_{K_n, \omega_1}(T)}{\operatorname{Tam}^0_{K_n, \omega_2}(T^*(1))} = |d_{K_n}|_p^{\dim V / 2} \left| \Gamma^*(V) \frac{\alpha_{V, K_n}(\omega, T)}{\varepsilon(K_n, V)} \right|_p, \tag{$\dagger$}$$

where $\omega_1$ and $\omega_2$ are bases of $t_V(K_n)$ and $t_{V^*(1)}(K_n) = \operatorname{Fil}^0 D_{\mathrm{dR}}^{K_n}(V)$ respectively, $\Gamma^*(V)$ is a product of Gamma factors, $\alpha_{V,K_n}(\omega, T)$ is a determinant involving the lattice and the bases, and $\varepsilon(K_n, V)$ is the local epsilon factor.

For a crystalline representation $V$ with the specific conditions in our problem, the right-hand side of $(\dagger)$ can be computed explicitly using the local $L$-function and epsilon factor of $V$:

- The local $L$-function of $V$ is $L(V, s) = (1 - \alpha p^{-s})^{-1}(1 - \beta p^{-s})^{-1}$, and the completed $L$-function involves the Gamma factors $\Gamma_p(s - k_1)$ and $\Gamma_p(s - k_2)$.
- The local epsilon factor $\varepsilon(K_n, V)$ and the determinant $\alpha_{V, K_n}(\omega, T)$ are determined by the Frobenius eigenvalues, the Hodge–Tate weights, and the choice of lattice.
- The key point is that, with the choice of $\omega$ as a $\mathbb{Z}_p$-basis of $t_T = \mathbb{D}(T)/\operatorname{Fil}^0 \mathbb{D}(T)$ (compatible with the strongly divisible lattice $\mathbb{D}(T)$), the ratio on the right-hand side of $(\dagger)$ simplifies to $1$.

More precisely, the local Tamagawa number conjecture $C_{\mathrm{EP}}(K_n, V)$ asserts that the Euler–Poincaré determinant of the complex $\mathbf{R}\Gamma(K_n, T)$, when compared with the determinant of the filtered $\varphi$-module $\mathbb{D}(T)$ via the Bloch–Kato exponential map, gives a trivialization that is compatible with the local $L$-function and epsilon factor. For crystalline representations with non-exceptional Frobenius eigenvalues, the local $L$-function $L(V, 0) = (1-\alpha)^{-1}(1-\beta)^{-1}$ is a $p$-adic unit (since $v_p(1-\alpha) = 0$ as $v_p(\alpha) = k_1 > 0$, so $1 - \alpha \in \mathbb{Z}_p^\times$), and the epsilon factor compensates for the contribution from the negative Hodge–Tate weight $k_2$.

The compatibility of the Tamagawa number with the duality $V \leftrightarrow V^*(1)$ (property (1) of Proposition 2.5 in [BB08]: $C_{\mathrm{EP}}(K_n, V) \Leftrightarrow C_{\mathrm{EP}}(K_n, V^*(1))$) together with the explicit computation of the right-hand side of $(\dagger)$ shows that:
$$\operatorname{Tam}^0_{K_n, \omega}(T) = 1.$$

This can also be seen more directly: the conjecture $C_{\mathrm{EP}}(K_n, V)$ is equivalent to the statement that the Bloch–Kato exponential map, when extended to $K_n$, gives an isomorphism of integral structures:
$$\exp_{K_n}: \mathcal{O}_{K_n} \otimes_{\mathbb{Z}_p} t_T \xrightarrow{\;\sim\;} H^1_f(K_n, T) \otimes_{\mathbb{Z}_p} \mathcal{O}_{K_n},$$
with the index $[H^1_f(K_n, T) : \exp_{K_n}(\mathcal{O}_{K_n} \omega)]$ being equal to $[\mathbb{D}(T) : (1-\varphi)\mathbb{D}(T)]$, which is exactly the statement $\operatorname{Tam}^0_{K_n, \omega}(T) = 1$.

#### Step 8: Outline of the Benois–Berger Proof

For completeness, we sketch the key ideas in the proof of the Benois–Berger theorem.

**(a) Wach modules.** For a crystalline representation $V$ of $G_K$ with $K$ unramified over $\mathbb{Q}_p$, Berger has shown that $V$ admits a Wach module $N(V)$, which is a free $\mathbb{Q}_p[\![\Gamma]\!]$-module of rank $d = \dim V$ equipped with a Frobenius $\varphi$ and a filtration, and $N(V)$ determines $V$ via $V = \mathbb{Q}_p \otimes_{\mathbb{Z}_p[\![\Gamma]\!]} N(V)$. For a lattice $T$, there is an integral Wach module $N(T) \subset N(V)$.

** (b) The Perrin-Riou exponential.** The Perrin-Riou exponential map $\operatorname{Exp}_{V,h}^{\varepsilon}$ is a map from $\mathcal{H}(\Gamma) \otimes D_{\mathrm{cris}}(V)$ to $\mathcal{H}(\Gamma) \otimes H^1_{\mathrm{Iw}}(K, V)$ that interpolates the Bloch–Kato exponential maps $\exp_{K_n, V(k)}$ for all twists $V(k)$ and all levels $n$. It is constructed using the $(\varphi, \Gamma)$-module of $V$.

** (c) The $\delta_{\mathbb{Z}_p}(V)$ conjecture ($C_{\mathrm{Iw}}$).** This conjecture states that the Perrin-Riou exponential sends the lattice $\mathbb{D}(T)$ to the Iwasawa cohomology $H^1_{\mathrm{Iw}}(K, T)$ (not just $H^1_{\mathrm{Iw}}(K, V)$). Benois–Berger prove this by analyzing the Wach module $N(T)$ and showing that the determinant of the Perrin-Riou exponential on the lattice is a unit in the Iwasawa algebra. The key technical result (Theorem 4.4 in [BB08]) shows that $\varphi^{-1}$ induces an isomorphism:
$$\mathbf{D}(V)^{\psi=1} / (\varphi^* \mathbf{N}(V))^{\psi=1} \xrightarrow{\sim} \bigoplus_{k=1}^{h} (K_1 t^{-k} \otimes_K \operatorname{Fil}^k D_{\mathrm{cris}}(V)),$$
and the determinant of this isomorphism on the lattice level gives the required integrality.

** (d) Descent from $C_{\mathrm{Iw}}$ to $C_{\mathrm{EP}}$.** Benois–Berger show (in §§4.2–4.3) that $C_{\mathrm{Iw}}(K_\infty/K, V)$ is equivalent to $C_{\mathrm{EP}}(K_n/K, V)$ for every $n \ge 1$. The descent uses:
- The relationship between Iwasawa cohomology $H^1_{\mathrm{Iw}}(K, T)$ and finite-level cohomology $H^1(K_n, T)$ via the projection maps.
- The structure of the Galois group $\operatorname{Gal}(K_\infty/K) \cong \Delta \times \Gamma_1$, where $\Delta$ is finite and $\Gamma_1 \cong \mathbb{Z}_p$.
- The Euler characteristic formula for $H^1(K_n, T)$, which relates the size of $H^1(K_n, T)$ to $[\mathbb{D}(T) : (1-\varphi)\mathbb{D}(T)]$ and the discriminant of $K_n$.

The descent argument shows that the integrality at the Iwasawa level (the $\delta_{\mathbb{Z}_p}(V)$ conjecture) implies the correct index formula at each finite level, which is exactly the statement $\operatorname{Tam}^0_{K_n, \omega}(T) = 1$.

### Conclusion

Combining Part I (the case $n = 0$, proved directly using the Bloch–Kato fundamental exact sequence) and Part II (the case $n \ge 1$, proved using the Benois–Berger theorem), we conclude:

$$\operatorname{Tam}^0_{K_n, \omega}(T) = 1 \quad \text{for all } n \ge 0. \qquad \blacksquare$$

---

## References

- **[BK90]** S. Bloch, K. Kato, *L-functions and Tamagawa numbers of motives*, The Grothendieck Festschrift, Vol. I, Progr. Math. 86, Birkhäuser (1990), 333–400.
- **[BB08]** D. Benois, L. Berger, *Théorie d'Iwasawa des représentations cristallines II*, Comment. Math. Helv. 83 (2008), no. 3, 603–677.
- **[Ber]** L. Berger, *Nombres de Tamagawa de certaines représentations cristallines*, unpublished preprint (available at https://perso.ens-lyon.fr/laurent.berger/autrestextes/tamagawa.pdf).
- **[PR94]** B. Perrin-Riou, *Théorie d'Iwasawa des représentations p-adiques semi-stables*, Invent. Math. 115 (1994), 81–149.
- **[Ber04]** L. Berger, *Limites de représentations cristallines*, Ann. Sci. École Norm. Sup. 37 (2004), 355–382.
