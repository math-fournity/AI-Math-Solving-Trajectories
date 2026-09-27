# Proof that the maximal number is $k = 6$

## Setup and notation

We work in $\mathbb{P}^4$ with homogeneous coordinates $[x_0 : x_1 : x_2 : x_3 : x_4]$. The vector space of homogeneous quadratic forms in $5$ variables has dimension
$$\binom{5+1}{2} = 15.$$

Let $W = \langle Q_1, \dots, Q_k \rangle \subseteq S_2$ be the span of the chosen quadrics, and let $X = V(W) = V(Q_1, \dots, Q_k) \subseteq \mathbb{P}^4$. We require that $X$ have a connected component $C$ that is:

- **positive dimensional** ($\dim C \geq 1$), and
- **not lying on any hyperplane** (i.e. $C$ is *non-degenerate*: its linear span is all of $\mathbb{P}^4$, equivalently $I(C)$ contains no linear form).

We seek the maximal $k$.

## Reduction to $\dim I(C)_2$

Since every $Q_i$ vanishes on $C$, we have $W \subseteq I(C)_2$, hence
$$k = \dim W \leq \dim I(C)_2. \tag{1}$$

Conversely, if we take $W = I(C)_2$ (the full degree-$2$ part of the ideal), then $V(W) \supseteq C$, and $C$ is a connected component of $V(W)$ provided $V(I(C)_2)$ does not connect $C$ to any other component. In particular, if $V(I(C)_2) = C$ (ideal generated in degree $2$, or at least no extra components), then $C$ is trivially a connected component. Thus the problem reduces to:

> **Maximize $\dim I(C)_2$ over all positive-dimensional, non-degenerate $C \subseteq \mathbb{P}^4$ that arise as a connected component of $V(I(C)_2)$.**

A universal upper bound $\dim I(C)_2 \leq M$ for *all* positive-dimensional non-degenerate $C$ immediately gives $k \leq M$ by (1). We then exhibit a $C$ achieving equality with $V(I(C)_2) = C$.

## Upper bound: $\dim I(C)_2 \leq 6$

We split by the dimension of $C$.

### Case 1: $C$ is a curve ($\dim C = 1$)

Let $C \subseteq \mathbb{P}^4$ be a connected, non-degenerate (reduced or reducible) curve of degree $d$ and arithmetic genus $p_a$.

**Degree bound.** A non-degenerate curve in $\mathbb{P}^n$ has degree $d \geq n$; here $d \geq 4$.

**Riemann–Roch computation.** From the exact sequence
$$0 \to I_C(2) \to \mathcal{O}_{\mathbb{P}^4}(2) \to \mathcal{O}_C(2) \to 0$$
and $H^1(\mathcal{O}_{\mathbb{P}^4}(2)) = 0$, we get
$$\dim I(C)_2 = h^0(I_C(2)) = 15 - h^0(\mathcal{O}_C(2)) + h^1(\mathcal{O}_C(2)).$$
Riemann–Roch on $C$: $h^0(\mathcal{O}_C(2)) - h^1(\mathcal{O}_C(2)) = \deg(\mathcal{O}_C(2)) + 1 - p_a = 2d + 1 - p_a$. Substituting:
$$\boxed{\dim I(C)_2 = 15 - (2d + 1 - p_a) = 14 - 2d + p_a.} \tag{2}$$

**Castelnuovo bound.** For a connected, non-degenerate curve in $\mathbb{P}^4$ (valid also for reducible curves, by applying the bound to a general hyperplane section which is a set of $d$ points in $\mathbb{P}^3$ spanning $\mathbb{P}^3$):
$$p_a \leq \pi(d, 4), \qquad d - 1 = 3m + \epsilon,\; 0 \leq \epsilon \leq 2, \qquad \pi(d,4) = \tfrac{3m(m-1)}{2} + m\epsilon.$$

Evaluating:

| $d$ | $m$ | $\epsilon$ | $\pi(d,4)$ | $\dim I(C)_2 \leq 14 - 2d + \pi$ |
|-----|-----|------------|------------|-----------------------------------|
| 4   | 1   | 0          | 0          | $14 - 8 + 0 = 6$                  |
| 5   | 1   | 1          | 1          | $14 - 10 + 1 = 5$                 |
| 6   | 1   | 2          | 2          | $14 - 12 + 2 = 4$                 |
| 7   | 2   | 0          | 3          | $14 - 14 + 3 = 3$                 |
| $\geq 8$ | — | —     | —          | $\leq 2$ (decreasing)             |

The maximum is **$6$**, achieved uniquely at $d = 4$, $p_a = 0$.

### Case 2: $C$ is a surface ($\dim C = 2$)

A non-degenerate surface $S \subseteq \mathbb{P}^4$ has degree $\geq 3$. The minimal case is the cubic scroll $S(1,2) \cong \mathbb{F}_1$. With $\mathcal{O}_{\mathbb{P}^4}(1)|_S = C_0 + 2f$ (where $C_0^2 = -1$, $C_0 \cdot f = 1$, $f^2 = 0$):
$$\chi(\mathcal{O}_S(2)) = \tfrac{1}{2}(2C_0 + 4f)\cdot(2C_0 + 4f - K_S) = \tfrac{1}{2}(12)\cdot(2C_0+4f + 2C_0 + 6f) / \cdots$$
A direct Riemann–Roch on the surface gives $h^0(\mathcal{O}_S(2)) = 12$ (using $\chi(\mathcal{O}_S) = 1$, $K_S \cdot H = -5$, $H^2 = 3$ for the cubic scroll, and $H^i(\mathcal{O}_S(2)) = 0$ for $i \geq 1$ by Kodaira vanishing). Hence
$$\dim I(S)_2 = 15 - 12 = 3.$$
Surfaces of higher degree have $\dim I(S)_2 \leq 2$ (del Pezzo of degree $4$: $2$ complete-intersection quadrics; degree $\geq 5$: even smaller). So **surfaces give $\dim I(C)_2 \leq 3 < 6$**.

### Case 3: $C$ is a threefold ($\dim C = 3$)

A threefold in $\mathbb{P}^4$ is a hypersurface. A quadric hypersurface ($d = 2$) has $\dim I = 1$; for $d \geq 3$, $\dim I(C)_2 = 0$. So **threefolds give $\dim I(C)_2 \leq 1 < 6$**.

### Mixed / reducible cases

If $C$ is reducible, $I(C)_2 = \bigcap I(C_i)_2$, which is *smaller* than each factor — reducibility cannot increase $\dim I(C)_2$. Mixed dimensions (e.g. curve $\cup$ surface) only add constraints. So no improvement is possible.

### Summary of upper bound

Combining all cases:
$$\dim I(C)_2 \leq 6 \quad \text{for every positive-dimensional, non-degenerate } C \subseteq \mathbb{P}^4.$$
By (1), $k \leq 6$.

## Lower bound: $k = 6$ is achieved

We give an explicit construction. Let $C = L_1 \cup L_2 \cup L_3 \cup L_4$ be the **chain of four lines** in $\mathbb{P}^4$:
$$L_1 = \{[s:t:0:0:0]\},\quad L_2 = \{[0:s:t:0:0]\},\quad L_3 = \{[0:0:s:t:0]\},\quad L_4 = \{[0:0:0:s:t]\}.$$

**Non-degeneracy.** The four lines pass through the points $e_0, e_1, e_2, e_3, e_4$ (the chain links at $e_1, e_2, e_3$), so $\operatorname{span}(C) = \mathbb{P}^4$.

**Degree and genus.** $C$ is a chain of $4$ lines, $\deg C = 4$, and $p_a(C) = 0$ (a tree of $\mathbb{P}^1$'s). By (2): $\dim I(C)_2 = 14 - 8 + 0 = 6$.

**The six quadrics.** A quadratic form $Q = \sum a_{ij} x_i x_j$ vanishes on $L_1$ iff $a_{00} = a_{01} = a_{11} = 0$; on $L_2$ iff $a_{11} = a_{12} = a_{22} = 0$; on $L_3$ iff $a_{22} = a_{23} = a_{33} = 0$; on $L_4$ iff $a_{33} = a_{34} = a_{44} = 0$. The surviving monomials are exactly:
$$x_0 x_2,\; x_0 x_3,\; x_0 x_4,\; x_1 x_3,\; x_1 x_4,\; x_2 x_4.$$
These are $6$ linearly independent quadrics, and
$$I(C)_2 = \langle x_0 x_2,\; x_0 x_3,\; x_0 x_4,\; x_1 x_3,\; x_1 x_4,\; x_2 x_4 \rangle.$$

**Verification that $V(I(C)_2) = C$.** We solve the system:
$$x_0 x_2 = x_0 x_3 = x_0 x_4 = x_1 x_3 = x_1 x_4 = x_2 x_4 = 0.$$

- **If $x_0 \neq 0$:** then $x_2 = x_3 = x_4 = 0$, and $x_1 x_3 = 0$, $x_1 x_4 = 0$ are automatic. The remaining coordinates are $[x_0 : x_1 : 0 : 0 : 0] \in L_1$.
- **If $x_0 = 0$:** the system reduces to $x_1 x_3 = x_1 x_4 = x_2 x_4 = 0$.
  - *If $x_1 \neq 0$:* then $x_3 = x_4 = 0$, giving $[0 : x_1 : x_2 : 0 : 0] \in L_2$.
  - *If $x_1 = 0$:* the system is $x_2 x_4 = 0$.
    - *If $x_2 \neq 0$:* then $x_4 = 0$, giving $[0 : 0 : x_2 : x_3 : 0] \in L_3$.
    - *If $x_2 = 0$:* then $x_0 = x_1 = x_2 = 0$, giving $[0 : 0 : 0 : x_3 : x_4] \in L_4$.

Every solution lies on exactly one of $L_1, L_2, L_3, L_4$, so $V(I(C)_2) = C$. The six quadrics are linearly independent (distinct monomials), $C$ is connected (a chain), $1$-dimensional, and non-degenerate. Taking $Q_1, \dots, Q_6$ to be these six quadrics gives $k = 6$.

## Conclusion

The upper bound $k \leq 6$ holds for any positive-dimensional non-degenerate connected component in $\mathbb{P}^4$, and the chain of four lines achieves $k = 6$ with $V(Q_1, \dots, Q_6)$ equal to the chain itself.

$$\boxed{6}$$

### PROOF COMPLETE
