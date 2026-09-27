# Proof: Rank of $E: Y^2 = X^3 + p^2X$ for $p \equiv 5 \pmod{8}$

## Setup

Let $p$ be a prime with $p \equiv 5 \pmod{8}$. We prove that the elliptic curve
$$E: y^2 = x^3 + p^2 x$$
has rank $0$ over $\mathbb{Q}$, using a $2$-isogeny descent.

**Key number-theoretic facts** (all from $p \equiv 5 \pmod{8}$):
- $p \equiv 1 \pmod{4}$, so $\left(\frac{-1}{p}\right) = 1$.
- $\left(\frac{2}{p}\right) = (-1)^{(p^2-1)/8} = -1$.
- $p - 1 = 4m$ with $m$ odd, so $z^4 \equiv -1 \pmod{p}$ has no solution (since $-1 = g^{2m}$ in $(\mathbb{Z}/p\mathbb{Z})^*$ requires $4j \equiv 2m \pmod{4m}$, i.e., $j = m/2$, but $m$ is odd).

## The 2-Isogeny

The curve $E: y^2 = x^3 + p^2 x$ (with $a = 0$, $b = p^2$) has a $2$-isogeny
$$\varphi: E \to E', \qquad E': y^2 = x^3 - 4p^2 x$$
with kernel $E[\varphi] = \{O, (0,0)\}$. The dual isogeny $\hat{\varphi}: E' \to E$ has kernel $E'[\hat{\varphi}] = \{O, (0,0)'\}$, and $\hat{\varphi} \circ \varphi = [2]_E$.

**Rational $2$-torsion:**
- $E(\mathbb{Q})[2] = \{O, (0,0)\}$, order $2$ (since $x^2 + p^2$ has no rational root).
- $E'(\mathbb{Q})[2] = \{O, (0,0)', (2p, 0), (-2p, 0)\}$, order $4$ (since $x^3 - 4p^2 x = x(x-2p)(x+2p)$ splits completely over $\mathbb{Q}$).

**No $4$-torsion on $E$:** The point $(0,0) \in E(\mathbb{Q})$ is not divisible by $2$. Indeed, $[2]P = (0,0)$ requires $x(P) = \pm p$ (from the duplication formula $x([2]P) = (x^2 - p^2)^2/(4x(x^2+p^2))$, setting this equal to $0$ gives $x = \pm p$). But $x = p$ gives $y^2 = 2p^3$ (requires $2p$ to be a square, impossible) and $x = -p$ gives $y^2 = -2p^3 < 0$ (no real solution).

## Descent Maps and Homogeneous Spaces

Following the standard $2$-isogeny descent (Silverman, *Arithmetic of Elliptic Curves*, Ch. X; Washington, *Elliptic Curves*, Ch. 4):

**Descent map $\alpha: E(\mathbb{Q}) \to \mathbb{Q}^*/(\mathbb{Q}^*)^2$** with $\ker(\alpha) = \hat{\varphi}(E'(\mathbb{Q}))$:
$$\alpha(O) = 1, \quad \alpha((0,0)) = b = p^2 \equiv 1, \quad \alpha((x,y)) = x \pmod{\text{squares}}.$$

Homogeneous spaces $C_d: d w^2 = d^2 + p^2 z^4$ for squarefree $d \mid p^2$, i.e., $d \in \{1, p, -1, -p\}$.

**Descent map $\alpha': E'(\mathbb{Q}) \to \mathbb{Q}^*/(\mathbb{Q}^*)^2$** with $\ker(\alpha') = \varphi(E(\mathbb{Q}))$:
$$\alpha'(O) = 1, \quad \alpha'((0,0)') = b' = -4p^2 \equiv -1, \quad \alpha'((x,y)) = x \pmod{\text{squares}}.$$

Homogeneous spaces $C'_d: d w^2 = d^2 - 4p^2 z^4$ for squarefree $d \mid (-4p^2)$, i.e., $d \in \{\pm 1, \pm 2, \pm p, \pm 2p\}$.

## Computing $\text{Sel}_{\hat{\varphi}}$ (bounds $E(\mathbb{Q})/\hat{\varphi}(E'(\mathbb{Q}))$)

Check local solubility of $C_d: dw^2 = d^2 + p^2 z^4$:

- **$d = 1$:** $w^2 = 1 + p^2 z^4$. Point $(w,z) = (1,0)$. ✓
- **$d = p$:** $w^2 = p(1 + z^4)$. At $p$: if $v_p(z) = 0$, then $v_p(\text{RHS}) = 1$ (odd) since $z^4 \equiv -1 \pmod{p}$ has no solution. If $v_p(z) \geq 1$, then $v_p(1+z^4) = 0$, so $v_p(\text{RHS}) = 1$ (odd). No $p$-adic solution. ✗
- **$d = -1$:** $w^2 = -(1 + p^2 z^4) < 0$ over $\mathbb{R}$. ✗
- **$d = -p$:** $w^2 = -p(1 + z^4) < 0$ over $\mathbb{R}$. ✗

$$\boxed{\text{Sel}_{\hat{\varphi}} = \{1\}, \quad |\text{Sel}_{\hat{\varphi}}| = 1.}$$

## Computing $\text{Sel}_{\varphi}$ (bounds $E'(\mathbb{Q})/\varphi(E(\mathbb{Q}))$)

Check local solubility of $C'_d: dw^2 = d^2 - 4p^2 z^4$:

- **$d = 1$:** $w^2 = 1 - 4p^2 z^4$. Point $(w,z) = (1,0)$. ✓
- **$d = -1$:** $w^2 = 4p^2 z^4 - 1$. The affine part fails at $2$ ($w^2 \equiv 3$ or $7 \pmod{8}$, neither a square mod $8$). However, the smooth projective model has a rational point at infinity corresponding to $(0,0)' \in E'(\mathbb{Q})$ with $\alpha'((0,0)') = -1$. ✓
- **$d = 2$:** $w^2 = 2(1 - p^2 z^4)$. At $p$ with $z = 0$: $w^2 = 2$, requiring $\left(\frac{2}{p}\right) = 1$. But $\left(\frac{2}{p}\right) = -1$. ✗
- **$d = -2$:** $w^2 = 2(p^2 z^4 - 1)$. At $p$ with $z = 0$: $w^2 = -2$, requiring $\left(\frac{-2}{p}\right) = 1$. But $\left(\frac{-2}{p}\right) = \left(\frac{-1}{p}\right)\left(\frac{2}{p}\right) = 1 \cdot (-1) = -1$. ✗
- **$d = p$:** $w^2 = p(1 - 4z^4)$. At $p$: $v_p(\text{RHS}) = 1$ (odd) since $1 - 4z^4 \not\equiv 0 \pmod{p}$ for all $z$ (as $z^4 \equiv 1/4 \pmod{p}$ has no solution, which follows from $2^{2m} \equiv -1 \pmod{p}$). ✗
- **$d = -p$:** $w^2 = -p(1 - 4z^4)$. Same odd valuation at $p$. ✗
- **$d = 2p$:** $w^2 = 2p(1 - z^4)$. Point $(z,w) = (1,0)$, which is smooth ($\partial/\partial z$ of $2p(z^4-1) - w^2$ at $(1,0)$ is $8p \neq 0$). ✓
- **$d = -2p$:** $w^2 = 2p(z^4 - 1)$. Point $(z,w) = (1,0)$, smooth. ✓

$$\boxed{\text{Sel}_{\varphi} = \{1, -1, 2p, -2p\}, \quad |\text{Sel}_{\varphi}| = 4.}$$

## Determining the Quotient Groups

**$E'(\mathbb{Q})/\varphi(E(\mathbb{Q}))$:** The four $2$-torsion points of $E'$ map under $\alpha'$ to four distinct classes:
$$\alpha'(O) = 1, \quad \alpha'((0,0)') = -1, \quad \alpha'((2p,0)) = 2p, \quad \alpha'((-2p,0)) = -2p.$$

We verify none of the non-trivial $2$-torsion points lie in $\varphi(E(\mathbb{Q}))$:

- If $(0,0)' = \varphi(P)$, then $[2]P = \hat{\varphi}((0,0)') = O$, so $P \in E[2] = \{O, (0,0)\}$. But $\varphi(O) = \varphi((0,0)) = O \neq (0,0)'$. Contradiction.
- If $(2p,0) = \varphi(P)$, then $[2]P = \hat{\varphi}((2p,0)) = (0,0)$ (using the explicit dual isogeny formula). But $(0,0)$ is not $2$-divisible in $E(\mathbb{Q})$. Contradiction.
- Similarly $(-2p,0) \notin \varphi(E(\mathbb{Q}))$.

Therefore $|E'(\mathbb{Q})/\varphi(E(\mathbb{Q}))| \geq 4$. Since $|\text{Sel}_{\varphi}| = 4$ and $E'(\mathbb{Q})/\varphi(E(\mathbb{Q})) \hookrightarrow \text{Sel}_{\varphi}$, we get
$$|E'(\mathbb{Q})/\varphi(E(\mathbb{Q}))| = 4, \quad |\text{Ш}(E/\mathbb{Q})[\varphi]| = 1.$$

**$E(\mathbb{Q})/\hat{\varphi}(E'(\mathbb{Q}))$:** Since $\alpha((0,0)) = p^2 \equiv 1$, the point $(0,0)$ lies in $\ker(\alpha) = \hat{\varphi}(E'(\mathbb{Q}))$. Together with $O$, if $E(\mathbb{Q}) = \{O, (0,0)\}$ (rank $0$), then $E(\mathbb{Q}) = \hat{\varphi}(E'(\mathbb{Q}))$ and $|E(\mathbb{Q})/\hat{\varphi}(E'(\mathbb{Q}))| = 1 = |\text{Sel}_{\hat{\varphi}}|$. We verify this is self-consistent below.

## The Rank Formula

We use the factorization $[2]_E = \hat{\varphi} \circ \varphi$ and the tower
$$E(\mathbb{Q}) \supseteq \hat{\varphi}(E'(\mathbb{Q})) \supseteq \hat{\varphi}(\varphi(E(\mathbb{Q}))) = 2E(\mathbb{Q}).$$

By the tower law:
$$|E(\mathbb{Q})/2E(\mathbb{Q})| = |E(\mathbb{Q})/\hat{\varphi}(E'(\mathbb{Q}))| \cdot |\hat{\varphi}(E'(\mathbb{Q}))/\hat{\varphi}(\varphi(E(\mathbb{Q})))|.$$

For the second factor, $\hat{\varphi}: E'(\mathbb{Q}) \to \hat{\varphi}(E'(\mathbb{Q}))$ has kernel $\{O, (0,0)'\}$, and
$$|\hat{\varphi}(E'(\mathbb{Q}))/\hat{\varphi}(\varphi(E(\mathbb{Q})))| = \frac{|E'(\mathbb{Q})/\varphi(E(\mathbb{Q}))|}{|\ker(\hat{\varphi})/(\ker(\hat{\varphi}) \cap \varphi(E(\mathbb{Q})))|} = \frac{4}{2} = 2,$$
since $(0,0)' \notin \varphi(E(\mathbb{Q}))$ so $\ker(\hat{\varphi}) \cap \varphi(E(\mathbb{Q})) = \{O\}$.

Therefore:
$$|E(\mathbb{Q})/2E(\mathbb{Q})| = 1 \cdot 2 = 2.$$

Since $E(\mathbb{Q}) \cong \mathbb{Z}^r \oplus E(\mathbb{Q})_{\text{tors}}$ and $|E(\mathbb{Q})[2]| = 2$:
$$2^r = \frac{|E(\mathbb{Q})/2E(\mathbb{Q})|}{|E(\mathbb{Q})[2]|} = \frac{2}{2} = 1.$$

## Conclusion

$$r = \log_2(1) = 0.$$

The rank of $E: y^2 = x^3 + p^2 x$ over $\mathbb{Q}$ for $p \equiv 5 \pmod{8}$ is:

$$\boxed{0}$$

### PROOF COMPLETE