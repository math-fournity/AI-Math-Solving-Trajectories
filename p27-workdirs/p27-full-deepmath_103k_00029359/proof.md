# Proof: Faithful Normal State Controls SOT Convergence of Projections

## Theorem

Let $\omega$ be a faithful normal state on a von Neumann algebra $R$, and let $P_1, P_2, \ldots$ be projections in $R$ with $\omega(P_n) \to 0$. Then $P_n \to 0$ in the strong operator topology (SOT).

## Answer

$$\boxed{\text{Yes, } P_n \text{ must converge to } 0 \text{ in SOT.}}$$

---

## Proof

### Step 1: Reduction — For projections, SOT convergence to 0 equals WOT convergence to 0

Since each $P_n$ is a projection ($P_n = P_n^* = P_n^2$), for any vector $\xi$ in the Hilbert space $H$ on which $R$ acts:

$$\|P_n \xi\|^2 = \langle P_n \xi, P_n \xi \rangle = \langle \xi, P_n^* P_n \xi \rangle = \langle \xi, P_n \xi \rangle.$$

Therefore:
- $P_n \to 0$ in SOT $\iff$ $\|P_n \xi\| \to 0$ for all $\xi$ $\iff$ $\langle \xi, P_n \xi \rangle \to 0$ for all $\xi$.

By the polarization identity (applied to the self-adjoint operators $P_n$), $\langle \xi, P_n \xi \rangle \to 0$ for all $\xi$ implies $\langle \eta, P_n \xi \rangle \to 0$ for all $\eta, \xi$, i.e., $P_n \to 0$ in the weak operator topology (WOT). The converse is immediate.

Since the WOT on a von Neumann algebra coincides with the $\sigma$-weak topology, $P_n \to 0$ in WOT iff $\varphi(P_n) \to 0$ for every normal linear functional $\varphi$ on $R$. By the Jordan decomposition, it suffices to check positive normal functionals:

$$P_n \to 0 \text{ in SOT} \iff \varphi(P_n) \to 0 \text{ for every positive normal functional } \varphi. \tag{$\star$}$$

### Step 2: Key sub-lemma — Approximation by functionals dominated by $\omega$

**Sub-lemma.** *Let $\omega$ be a faithful normal state on $R$ and let $\varphi$ be a positive normal functional on $R$. For every $\varepsilon > 0$, there exist positive normal functionals $\varphi_1, \varphi_2$ on $R$ and a constant $C > 0$ such that:*
1. $\varphi = \varphi_1 + \varphi_2$,
2. $\varphi_1 \leq C \cdot \omega$ (i.e., $\varphi_1(x) \leq C\,\omega(x)$ for all $x \in R_+$),
3. $\|\varphi_2\| < \varepsilon$.

**Proof of Sub-lemma.**

Work in the standard form $(R, H, J, \mathcal{P})$ of $R$, where $\mathcal{P}$ is the natural positive cone. Let $\Omega \in \mathcal{P}$ be the cyclic and separating vector representing $\omega$, so $\omega(x) = \langle \Omega, x\Omega\rangle$ for $x \in R$.

Every positive normal functional $\varphi$ on $R$ corresponds to a unique vector $\xi_\varphi \in \mathcal{P}$ with $\varphi(x) = \langle \xi_\varphi, x\,\xi_\varphi\rangle$ for all $x \in R$.

**The spatial derivative.** Define the *spatial derivative* $h := d\varphi/d\omega$ as the positive self-adjoint operator on $H$ determined by:

$$h(x\Omega) = x\,\xi_\varphi, \quad x \in R.$$

This is well-defined: if $x\Omega = 0$, then $\omega(x^*x) = \|x\Omega\|^2 = 0$, and faithfulness of $\omega$ gives $x = 0$, hence $x\,\xi_\varphi = 0$.

**$h$ is affiliated with $R'$ (the commutant).** For $y \in R$ and $x \in R$:

$$h\,y(x\Omega) = h(yx\Omega) = yx\,\xi_\varphi = y \cdot h(x\Omega).$$

Since $R\Omega$ is dense in $H$ (cyclicity of $\Omega$), $h$ commutes with every $y \in R$, so $h$ is affiliated with $R'$.

**Key relation:** $h\Omega = \xi_\varphi$ (taking $x = 1$ in the definition).

**Spectral decomposition.** Let $h = \int_0^\infty \lambda\, dE(\lambda)$ be the spectral decomposition, with spectral projections $E(\lambda) \in R'$ (since $h$ is affiliated with $R'$). For $N > 0$, set $E_N := E([0,N]) \in R'$.

**Decomposition of $\varphi$.** Write $\xi_\varphi = E_N\,\xi_\varphi + (1 - E_N)\,\xi_\varphi =: \eta_N + \zeta_N$. Since $E_N \in R'$, for any $x \in R$ the cross terms vanish:

$$\langle \eta_N, x\,\zeta_N\rangle = \langle E_N\xi_\varphi,\, x(1-E_N)\xi_\varphi\rangle = \langle \xi_\varphi,\, E_N\, x\,(1-E_N)\,\xi_\varphi\rangle = \langle \xi_\varphi,\, x\, E_N(1-E_N)\,\xi_\varphi\rangle = 0,$$

using $E_N x = x E_N$ (since $E_N \in R'$) and $E_N(1-E_N) = 0$. Similarly $\langle \zeta_N, x\,\eta_N\rangle = 0$.

Therefore:

$$\varphi(x) = \langle \xi_\varphi, x\,\xi_\varphi\rangle = \langle \eta_N, x\,\eta_N\rangle + \langle \zeta_N, x\,\zeta_N\rangle =: \varphi_1(x) + \varphi_2(x).$$

Both $\varphi_1$ and $\varphi_2$ are positive normal functionals (vector functionals).

**Bounding $\varphi_1$.** Note $\eta_N = E_N\,\xi_\varphi = E_N\, h\,\Omega$. The operator $T_N := E_N\, h$ is bounded (since $E_N$ projects onto the spectral subspace where $h \leq N$) with $\|T_N\| \leq N$, and $T_N \in R'$. Then:

$$\varphi_1(x) = \langle T_N\Omega,\, x\, T_N\Omega\rangle = \langle \Omega,\, T_N^*\, x\, T_N\, \Omega\rangle = \langle \Omega,\, x\, T_N^* T_N\, \Omega\rangle,$$

where the last step uses $T_N \in R'$ (so $T_N^*$ commutes with $x$). Now:

$$T_N^* T_N = (E_N h)^*(E_N h) = h\, E_N\, h = h^2\, E_N \in R'_+,$$

and $h^2 E_N \leq N^2\, E_N \leq N^2 \cdot \mathbf{1}$ (as operators in $R'$). For $x \in R_+$, since $x \in R_+$ and $h^2 E_N \in R'_+$ commute, their product is positive and:

$$x \cdot h^2 E_N \leq N^2\, x.$$

Hence:

$$\varphi_1(x) = \langle \Omega,\, x\, h^2 E_N\, \Omega\rangle \leq N^2 \langle \Omega,\, x\,\Omega\rangle = N^2\, \omega(x).$$

So $\varphi_1 \leq N^2\, \omega$ with $C = N^2$.

**Bounding $\varphi_2$.** We have:

$$\|\varphi_2\| = \varphi_2(\mathbf{1}) = \|\zeta_N\|^2 = \|(1-E_N)\,\xi_\varphi\|^2 = \langle \xi_\varphi,\, (1-E_N)\,\xi_\varphi\rangle = \langle h\Omega,\, (1-E_N)\, h\Omega\rangle = \langle \Omega,\, h^2(1-E_N)\,\Omega\rangle.$$

Let $\mu$ be the spectral measure of $h$ at $\Omega$: $\mu(B) = \langle \Omega, E(B)\Omega\rangle$. Then:

$$\|\varphi_2\| = \int_N^\infty \lambda^2\, d\mu(\lambda), \qquad \|\varphi\| = \varphi(\mathbf{1}) = \|\xi_\varphi\|^2 = \|h\Omega\|^2 = \int_0^\infty \lambda^2\, d\mu(\lambda) < \infty.$$

Since $\int_0^\infty \lambda^2\, d\mu(\lambda) < \infty$, the tail integral $\int_N^\infty \lambda^2\, d\mu(\lambda) \to 0$ as $N \to \infty$.

Choose $N$ large enough that $\int_N^\infty \lambda^2\, d\mu(\lambda) < \varepsilon$. Then $\|\varphi_2\| < \varepsilon$ and $\varphi_1 \leq N^2\, \omega$. $\blacksquare$

### Step 3: Completing the proof

Let $\varphi$ be any positive normal functional on $R$ and $\varepsilon > 0$. By the sub-lemma, decompose $\varphi = \varphi_1 + \varphi_2$ with $\varphi_1 \leq C\,\omega$ and $\|\varphi_2\| < \varepsilon$.

Since $P_n \geq 0$:

$$\varphi(P_n) = \varphi_1(P_n) + \varphi_2(P_n) \leq C\,\omega(P_n) + |\varphi_2(P_n)| \leq C\,\omega(P_n) + \|\varphi_2\| \cdot \|P_n\| \leq C\,\omega(P_n) + \varepsilon.$$

Taking $\limsup_{n \to \infty}$ and using $\omega(P_n) \to 0$:

$$\limsup_{n\to\infty} \varphi(P_n) \leq \varepsilon.$$

Since $\varepsilon > 0$ is arbitrary, $\limsup_{n\to\infty} \varphi(P_n) \leq 0$. But $\varphi(P_n) \geq 0$ (as $\varphi$ is positive and $P_n \geq 0$), so:

$$\lim_{n\to\infty} \varphi(P_n) = 0.$$

This holds for every positive normal functional $\varphi$. By the reduction $(\star)$, $P_n \to 0$ in SOT. $\blacksquare$

---

## Summary of the argument

1. **Reduction**: For projections, SOT convergence to 0 is equivalent to WOT convergence to 0 (because $\|P_n\xi\|^2 = \langle \xi, P_n\xi\rangle$), which is equivalent to $\varphi(P_n) \to 0$ for all positive normal functionals $\varphi$.

2. **Sub-lemma (Sakai–Radon–Nikodym / spatial derivative)**: Every positive normal functional $\varphi$ can be decomposed as $\varphi = \varphi_1 + \varphi_2$ where $\varphi_1 \leq C\omega$ and $\|\varphi_2\|$ is arbitrarily small. The proof uses the spatial derivative $h = d\varphi/d\omega$, which is a positive self-adjoint operator **affiliated with $R'$** (the commutant), with spectral projections $E_N \in R'$. The spectral truncation $E_N$ decomposes $\xi_\varphi$ into a part controlled by $\omega$ (via $h^2 E_N \leq N^2$) and a part with arbitrarily small norm (via the tail of the spectral integral $\int_N^\infty \lambda^2\, d\mu \to 0$).

3. **Conclusion**: $\varphi(P_n) \leq C\,\omega(P_n) + \varepsilon \to \varepsilon$, and $\varepsilon$ arbitrary gives $\varphi(P_n) \to 0$ for all positive normal $\varphi$, hence $P_n \to 0$ in SOT.

### PROOF COMPLETE
