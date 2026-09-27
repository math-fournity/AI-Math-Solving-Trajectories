# Proof: $E_p \cdot \sigma_{p,q} = 1$

## Setup

Let $\pi: Y \to \mathbb{P}^3$ be the composition of two blow-ups:
1. **First blow-up** $\pi_1: X \to \mathbb{P}^3$: blow up $p$ and $q$, yielding exceptional divisors $E_{p,X}, E_{q,X} \cong \mathbb{P}^2$.
2. **Second blow-up** $\rho: Y \to X$: blow up the strict transform $\tilde{L}$ of $L$, yielding exceptional divisor $F = E_{p,q}$.

The divisors on $Y$ are $H, E_p, E_q, F$ where $H = \pi^*(\text{hyperplane})$, $E_p = \rho^*E_{p,X}$, $E_q = \rho^*E_{q,X}$ (strict transforms, since $\tilde{L} \not\subset E_{p,X}, E_{q,X}$), and $F = E_{p,q}$.

## Key geometric facts

### The normal bundle of $\tilde{L}$ in $X$

In $\mathbb{P}^3$, $N_{L/\mathbb{P}^3} \cong \mathcal{O}(1) \oplus \mathcal{O}(1)$. Blowing up two points $p, q$ on $L$ modifies the normal bundle of the strict transform:
$$N_{\tilde{L}/X} = N_{L/\mathbb{P}^3} \otimes \mathcal{O}_L(-p-q) = \mathcal{O}(1) \oplus \mathcal{O}(1) \otimes \mathcal{O}(-2) = \mathcal{O}(-1) \oplus \mathcal{O}(-1).$$

### Structure of $E_{p,q}$

The exceptional divisor is $F = E_{p,q} = \mathbb{P}(N_{\tilde{L}/X}) = \mathbb{P}(\mathcal{O}(-1) \oplus \mathcal{O}(-1))$. Since tensoring by a line bundle does not change projectivization:
$$E_{p,q} \cong \mathbb{P}(\mathcal{O} \oplus \mathcal{O}) \cong \mathbb{P}^1 \times \mathbb{P}^1.$$

The projection $E_{p,q} \to \tilde{L} \cong \mathbb{P}^1$ gives one ruling (the **fiber** ruling $f_{p,q}$); these fibers are contracted by $\pi$ (each maps to a point on $L$). The other ruling consists of **sections** $\sigma_{p,q}$, each isomorphic to $\mathbb{P}^1$ and mapping isomorphically to $L$ under $\pi$ — hence **not contracted**.

### Structure of $E_p$

After the second blow-up, $E_p$ is the blow-up of $E_{p,X} \cong \mathbb{P}^2$ at the point where $\tilde{L}$ meets it (the point corresponding to the tangent direction of $L$ at $p$). Thus $E_p \cong \mathbb{F}_1$ (the first Hirzebruch surface), confirming the problem statement.

### The intersection $E_p \cap E_{p,q}$

The curve $\tilde{L}$ meets $E_{p,X}$ at exactly one point (the direction of $L$ at $p$). When we blow up $\tilde{L}$, the preimage of this point in $E_{p,q}$ is the fiber of $E_{p,q} \to \tilde{L}$ over that point. This fiber is:
- In $E_p \cong \mathbb{F}_1$: the $(-1)$-section $s_p$ (the exceptional curve of the blow-up of $\mathbb{P}^2$ at a point).
- In $E_{p,q} \cong \mathbb{P}^1 \times \mathbb{P}^1$: a fiber $f_{p,q}$ of the projection $E_{p,q} \to \tilde{L}$ (the **contracted** ruling).

So $E_p \cap E_{p,q} = s_p = f_{p,q}$ (the same curve, viewed in two surfaces).

## Computation of $E_p \cdot \sigma_{p,q}$

The intersection $E_p \cdot \sigma_{p,q}$ is the intersection of the divisor $E_p$ with the curve $\sigma_{p,q}$ in the 3-fold $Y$.

**Step 1:** The curve $\sigma_{p,q}$ lies entirely in $E_{p,q}$. The divisor $E_p$ intersects $E_{p,q}$ along the curve $f_{p,q} = E_p \cap E_{p,q}$ (a fiber of $E_{p,q} \to \tilde{L}$).

**Step 2:** Since $\sigma_{p,q}$ lies in $E_{p,q}$, the intersection $E_p \cdot \sigma_{p,q}$ equals the intersection of $f_{p,q}$ with $\sigma_{p,q}$ **inside the surface** $E_{p,q} \cong \mathbb{P}^1 \times \mathbb{P}^1$.

**Step 3:** In $E_{p,q} \cong \mathbb{P}^1 \times \mathbb{P}^1$:
- $f_{p,q}$ is a fiber of the first projection $E_{p,q} \to \tilde{L}$ (the contracted ruling).
- $\sigma_{p,q}$ is a section of this projection, i.e., a fiber of the second projection (the non-contracted ruling).

These are the two complementary rulings of $\mathbb{P}^1 \times \mathbb{P}^1$, and their intersection number is:
$$f_{p,q} \cdot \sigma_{p,q} = 1.$$

**Conclusion:**
$$E_p \cdot \sigma_{p,q} = 1.$$

## Verification via triple intersections

As a consistency check, we verify using the intersection theory of blow-ups along curves.

The normal bundle $N_{\tilde{L}/X} = \mathcal{O}(-1) \oplus \mathcal{O}(-1)$ has $\deg(N_{\tilde{L}/X}) = -2$.

For the blow-up $\rho: Y \to X$ along $\tilde{L}$ with exceptional divisor $F$:
- $F^3 = \deg(N_{\tilde{L}/X}) = -2$.
- $\rho^*D \cdot F^2 = -(D \cdot \tilde{L})$ for any divisor $D$ on $X$.

Computing $D \cdot \tilde{L}$ for each divisor on $X$:
- $H_X \cdot \tilde{L} = 1$ (hyperplane meets line in 1 point).
- $E_{p,X} \cdot \tilde{L} = 1$ ($\tilde{L}$ meets $E_{p,X}$ at the tangent direction of $L$ at $p$).
- $E_{q,X} \cdot \tilde{L} = 1$ (similarly).

So:
- $H \cdot F^2 = -1$, $E_p \cdot F^2 = -1$, $E_q \cdot F^2 = -1$, $F^3 = -2$.

The curve $\sigma_{p,q}$ is a section of $F \to \tilde{L}$ corresponding to a quotient $N_{\tilde{L}/X} \to \mathcal{O}(-1)$. The intersection numbers with $\sigma_{p,q}$ are:
- $H \cdot \sigma_{p,q} = \deg(H|_{\sigma_{p,q}}) = \deg(\mathcal{O}_{\tilde{L}}(1)) = 1$.
- $E_p \cdot \sigma_{p,q} = \deg(E_p|_{\sigma_{p,q}}) = \deg(\mathcal{O}_{\tilde{L}}(1)) = 1$ (since $E_{p,X}|_{\tilde{L}} = \mathcal{O}(1)$, the point where $\tilde{L}$ meets $E_{p,X}$).
- $E_q \cdot \sigma_{p,q} = 1$ (similarly).
- $F \cdot \sigma_{p,q} = \deg(F|_{\sigma_{p,q}}) = \deg(\mathcal{O}_F(-1)|_{\sigma_{p,q}}) = \deg(\mathcal{O}(1)) = 1$ (since $\sigma_{p,q}^*\mathcal{O}_F(-1) = \mathcal{O}(-1)^\vee = \mathcal{O}(1)$).

All methods confirm: $E_p \cdot \sigma_{p,q} = 1$. $\blacksquare$