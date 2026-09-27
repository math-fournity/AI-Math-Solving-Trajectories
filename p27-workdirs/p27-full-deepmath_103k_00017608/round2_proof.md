# Rank of $y^2 = x^3 + p^3 x$ for $p \equiv 7 \pmod{16}$

## Answer

$$\boxed{0}$$

## Proof

Let $p$ be a prime with $p \equiv 7 \pmod{16}$, and let $E: y^2 = x^3 + p^3 x$. We compute the rank of $E(\mathbb{Q})$ via 2-isogeny descent.

### Step 1: Setup

The curve $E: y^2 = x^3 + p^3 x = x(x^2 + p^3)$ has a rational 2-torsion point $T = (0,0)$. Since $x^2 + p^3 = 0$ has no rational solutions ($p^3 > 0$), we have
$$E(\mathbb{Q})[2] = \{O, (0,0)\}, \quad |E(\mathbb{Q})[2]| = 2.$$

The 2-isogeny $\phi: E \to E'$ with kernel $\{O, (0,0)\}$ maps to
$$E': y^2 = x^3 - 4p^3 x, \quad b' = -4p^3.$$
Explicitly, $\phi(x,y) = \left(\frac{y^2}{x^2},\, \frac{-y(x^2 - p^3)}{x^2}\right)$ for $x \neq 0$.

The 2-torsion of $E'$: $x(x^2 - 4p^3) = 0$ gives $x = 0$ or $x = \pm 2p\sqrt{p}$, which is irrational. So
$$E'(\mathbb{Q})[2] = \{O, (0,0)\}, \quad |E'(\mathbb{Q})[2]| = 2.$$

### Step 2: The descent maps

**For $\hat\phi$-descent** (on $E$, with $b = p^3$): the map $\alpha: E(\mathbb{Q}) \to \mathbb{Q}^*/(\mathbb{Q}^*)^2$ is
- $\alpha(O) = 1$, $\alpha((0,0)) = b = p^3 \equiv p \pmod{(\mathbb{Q}^*)^2}$, $\alpha((x,y)) = x$ for $x \neq 0$.

The homogeneous space for squarefree $d \mid b$ is $C_d: N^2 = dM^4 + (b/d)e^4 = dM^4 + (p^3/d)e^4$.

The squarefree divisors of $p^3$ (up to sign) are $d \in \{1, -1, p, -p\}$.

**For $\phi$-descent** (on $E'$, with $b' = -4p^3$): the map $\alpha': E'(\mathbb{Q}) \to \mathbb{Q}^*/(\mathbb{Q}^*)^2$ is
- $\alpha'(O) = 1$, $\alpha'((0,0)) = b' = -4p^3 \equiv -p \pmod{(\mathbb{Q}^*)^2}$, $\alpha'((x,y)) = x$ for $x \neq 0$.

The homogeneous space for squarefree $d \mid b'$ is $C'_d: N^2 = dM^4 + (b'/d)e^4 = dM^4 + (-4p^3/d)e^4$.

The squarefree divisors of $-4p^3 = -2^2 p^3$ are $d \in \{\pm 1, \pm 2, \pm p, \pm 2p\}$.

### Step 3: Computing $S^{(\hat\phi)}$

We check local solubility of $C_d: N^2 = dM^4 + (p^3/d)e^4$ for each $d$.

- **$d = 1$**: Always in $S^{(\hat\phi)}$ (corresponds to $O$). ✓
- **$d = -1$**: $N^2 = -M^4 - p^3 e^4 < 0$ over $\mathbb{R}$ for $Me \neq 0$. ✗
- **$d = -p$**: $N^2 = -pM^4 - p^2 e^4 < 0$ over $\mathbb{R}$ for $Me \neq 0$. ✗
- **$d = p$**: $C_p: N^2 = pM^4 + p^2 e^4$.
  - **Over $\mathbb{R}$**: RHS $> 0$ for $Me \neq 0$. ✓
  - **Over $\mathbb{Q}_p$**: Take $v_p(M) \geq 1$, $v_p(e) = 0$. Then $v_p(\text{RHS}) = 2$, so $N = pN'$, and $N'^2 = M^4/p + e^4 \equiv e^4 \pmod{p}$, which is a nonzero square mod $p$. By Hensel's lemma, this lifts. ✓
  - **Over $\mathbb{Q}_2$**: Take $M = 2$, $e = 1$. Then $N^2 = 16p + p^2 = p(16 + p)$. Since $p \equiv 7 \pmod{16}$, we have $16 + p \equiv 7 \pmod{16}$, so $v_2(p(16+p)) = 0$ and $p(16+p) \equiv 7 \cdot 7 = 49 \equiv 1 \pmod{8}$. A 2-adic unit $\equiv 1 \pmod{8}$ is a square. ✓
  - **Other primes $\ell \neq 2, p$**: Good reduction, local solubility automatic. ✓

Therefore $S^{(\hat\phi)} = \{1, p\}$ and $|S^{(\hat\phi)}| = 2$.

### Step 4: Computing $S^{(\phi)}$

We check $C'_d: N^2 = dM^4 + (-4p^3/d)e^4$ for each $d \in \{\pm 1, \pm 2, \pm p, \pm 2p\}$.

- **$d = 1$**: Always in $S^{(\phi)}$ (corresponds to $O$). ✓
- **$d = -p$**: Always in $S^{(\phi)}$ (corresponds to $(0,0) \in E'$, since $\alpha'((0,0)) = -p$). ✓
- **$d = -1$**: $C'_{-1}: N^2 = -M^4 + 4p^3 e^4$. Over $\mathbb{Q}_p$ with $v_p(M) = v_p(e) = 0$: $N^2 \equiv -M^4 \pmod{p}$. Since $p \equiv 7 \pmod{16} \equiv 3 \pmod{4}$, we have $\left(\frac{-1}{p}\right) = -1$, so $-M^4$ is not a QR mod $p$. ✗
- **$d = 2$**: $C'_2: N^2 = 2(M^4 - p^3 e^4)$. Over $\mathbb{Q}_2$: for any parity of $M, e$, either $v_2(\text{RHS})$ is odd (not a square) or the unit part is $\equiv 5 \pmod{8}$ (not a square). Specifically, with $M, e$ both odd: $M^4 - p^3 e^4 \equiv 1 - 7 = -6 \equiv 10 \pmod{16}$, so $v_2 = 1$, $v_2(N^2) = 2$, and $(M^4 - p^3 e^4)/2 \equiv 5 \pmod{8}$, not a square. Other parities give $v_2(N^2) = 1$, odd. ✗
- **$d = -2$**: $C'_{-2}: N^2 = 2(p^3 e^4 - M^4)$. Over $\mathbb{Q}_2$ with $M, e$ odd: $p^3 e^4 - M^4 \equiv 7 - 1 = 6 \pmod{16}$, $v_2 = 1$, $v_2(N^2) = 2$, unit part $\equiv 3 \pmod{8}$, not a square. ✗
- **$d = p$**: $C'_p: N^2 = p(M^4 - 4pe^4)$. Over $\mathbb{Q}_p$ with $v_p(M) = 0, v_p(e) = 0$: $v_p(\text{RHS}) = 1$, odd. With $v_p(M) \geq 1, v_p(e) = 0$: $v_p(\text{RHS}) = 2$, $N = pN'$, $N'^2 \equiv -4e^4 \pmod{p}$. Since $\left(\frac{-4}{p}\right) = \left(\frac{-1}{p}\right) = -1$ (as $p \equiv 3 \pmod 4$), this is not a QR. ✗
- **$d = 2p$**: $C'_{2p}: N^2 = 2p(M^4 - pe^4)$. Over $\mathbb{Q}_p$ with $v_p(M) \geq 1, v_p(e) = 0$: $N'^2 \equiv -2e^4 \pmod{p}$. Since $\left(\frac{-2}{p}\right) = \left(\frac{-1}{p}\right)\left(\frac{2}{p}\right) = (-1)(1) = -1$ (using $p \equiv 7 \pmod 8$ so $\left(\frac{2}{p}\right) = 1$, and $p \equiv 3 \pmod 4$ so $\left(\frac{-1}{p}\right) = -1$), not a QR. ✗
- **$d = -2p$**: $C'_{-2p}: N^2 = 2p(pe^4 - M^4)$. Over $\mathbb{Q}_p$ with $v_p(M) \geq 1, v_p(e) = 0$: $N'^2 \equiv 2e^4 \pmod{p}$, which is a QR ($\left(\frac{2}{p}\right) = 1$). Passes $p$-adic. ✓ But over $\mathbb{Q}_2$ with $M, e$ odd: $pe^4 - M^4 \equiv 6 \pmod{16}$, $v_2 = 1$, $v_2(N^2) = 2$, unit part $\equiv 5 \pmod{8}$, not a square. ✗

Therefore $S^{(\phi)} = \{1, -p\}$ and $|S^{(\phi)}| = 2$.

### Step 5: Determining the rank

The image of $\alpha$ always contains $\{1, p\}$ (from $O$ and $(0,0)$), so
$$|E(\mathbb{Q})/\hat\phi(E'(\mathbb{Q}))| \geq 2 = |S^{(\hat\phi)}|.$$
Since the image is a subgroup of $S^{(\hat\phi)}$, we get $|E(\mathbb{Q})/\hat\phi(E'(\mathbb{Q}))| = 2$ and $|\text{Sha}[\hat\phi]| = 1$.

Similarly, the image of $\alpha'$ always contains $\{1, -p\}$ (from $O$ and $(0,0)$), so
$$|E'(\mathbb{Q})/\phi(E(\mathbb{Q}))| = 2 = |S^{(\phi)}|,$$
and $|\text{Sha}[\phi]| = 1$.

**Key identity.** Since $\hat\phi \circ \phi = [2]$, we have $2E(\mathbb{Q}) = \hat\phi(\phi(E(\mathbb{Q}))) \subseteq \hat\phi(E'(\mathbb{Q})) \subseteq E(\mathbb{Q})$, so
$$[E(\mathbb{Q}) : 2E(\mathbb{Q})] = [E(\mathbb{Q}) : \hat\phi(E'(\mathbb{Q}))] \cdot [\hat\phi(E'(\mathbb{Q})) : 2E(\mathbb{Q})].$$

By the homomorphism theorem, $\hat\phi(E'(\mathbb{Q}))/\hat\phi(\phi(E(\mathbb{Q}))) \cong E'(\mathbb{Q})/(\phi(E(\mathbb{Q})) \cdot E'(\mathbb{Q})[\hat\phi])$.

We check that $(0,0) \notin \phi(E(\mathbb{Q}))$: if $\phi(P) = (0,0)$ for $P = (x,y)$ with $x \neq 0$, then $y^2/x^2 = 0$ forces $y = 0$, hence $x(x^2 + p^3) = 0$ gives $x = 0$, contradiction. And $\phi(O) = \phi((0,0)) = O \neq (0,0)$. So $(0,0) \notin \phi(E(\mathbb{Q}))$, meaning $E'(\mathbb{Q})[\hat\phi] \cap \phi(E(\mathbb{Q})) = \{O\}$, and thus
$$[\hat\phi(E'(\mathbb{Q})) : 2E(\mathbb{Q})] = [E'(\mathbb{Q}) : \phi(E(\mathbb{Q}))]/2.$$

Combining:
$$[E(\mathbb{Q}) : 2E(\mathbb{Q})] = [E(\mathbb{Q}) : \hat\phi(E'(\mathbb{Q}))] \cdot [E'(\mathbb{Q}) : \phi(E(\mathbb{Q}))] / 2.$$

Since $|E(\mathbb{Q})[2]| = 2$, we have $[E(\mathbb{Q}) : 2E(\mathbb{Q})] = 2^{r+1}$ where $r = \operatorname{rank} E(\mathbb{Q})$. Substituting:
$$2^{r+1} = 2 \cdot 2 / 2 = 2,$$
$$r + 1 = 1, \qquad r = 0.$$

### Conclusion

The rank of the elliptic curve $y^2 = x^3 + p^3 x$ for a prime $p \equiv 7 \pmod{16}$ is

$$\boxed{0}.$$

The Mordell-Weil group is $E(\mathbb{Q}) = \{O, (0,0)\} \cong \mathbb{Z}/2\mathbb{Z}$, with no points of order 4 (since $2P = (0,0)$ requires $x^2 = p^3$, which has no rational solution).
