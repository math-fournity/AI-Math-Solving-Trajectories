# Answer: No

## Counterexample

Let $A = k[x,y]$ be the polynomial ring in two variables over a field $k$, with field of fractions $K = k(x,y)$. Let $\mathfrak{p} = (x,y)$, the maximal ideal, and define the fractional ideal

$$I = \frac{1}{x}(x,y) = \left(1,\, \frac{y}{x}\right).$$

### Verification that $I$ is a non-zero fractional $A$-ideal

$I$ is non-zero (it contains $1$), and $x \cdot I = (x,y) \subseteq A$, so $I$ is a fractional $A$-ideal.

### Computation of $I^{-1}$

$$I^{-1} = \{a \in K \mid aI \subseteq A\} = \left\{a \in K \;\middle|\; a \cdot 1 \in A,\; a \cdot \frac{y}{x} \in A\right\}.$$

The condition $a \in A$ and $\frac{ay}{x} \in A$ means $x \mid ay$ in $A = k[x,y]$. Since $\gcd(x,y) = 1$ in the UFD $k[x,y]$, this forces $x \mid a$. Therefore:

$$I^{-1} = xA = (x).$$

### Verification of $II^{-1} \subseteq \mathfrak{p}$

$$II^{-1} = \left(1, \frac{y}{x}\right) \cdot (x) = (x, y) = \mathfrak{p} \subseteq \mathfrak{p}. \quad \checkmark$$

### Localization

Since $1 \in I$, we have $I \not\subseteq \mathfrak{p}$. The element $1$ is a unit in $A_\mathfrak{p}$, so:

$$IA_\mathfrak{p} = A_\mathfrak{p}.$$

Therefore:

$$(IA_\mathfrak{p})^{-1} = (A_\mathfrak{p})^{-1} = A_\mathfrak{p}.$$

On the other hand:

$$I^{-1}A_\mathfrak{p} = xA \cdot A_\mathfrak{p} = xA_\mathfrak{p}.$$

Since $x \in \mathfrak{p}$, $x$ is not a unit in $A_\mathfrak{p}$, so $xA_\mathfrak{p} \subsetneq A_\mathfrak{p}$.

### The counterexample element

Take $a = y \in K$. Then:

- $a(IA_\mathfrak{p}) = y \cdot A_\mathfrak{p} = yA_\mathfrak{p} \subseteq A_\mathfrak{p}$ (since $y \in A \subseteq A_\mathfrak{p}$). In fact $yA_\mathfrak{p} \subsetneq A_\mathfrak{p}$ since $y \in \mathfrak{p}A_\mathfrak{p}$ is not a unit.
- $a = y \notin I^{-1}A_\mathfrak{p} = xA_\mathfrak{p}$, because $y \in xA_\mathfrak{p}$ would require $\frac{y}{x} \in A_\mathfrak{p}$, but $\frac{y}{x} \notin k[x,y]$ and cannot be written as $\frac{f}{g}$ with $g \notin \mathfrak{p} = (x,y)$ (the denominator $x$ lies in $\mathfrak{p}$).

Thus $a(IA_\mathfrak{p}) \subset A_\mathfrak{p}$ but $a \notin I^{-1}A_\mathfrak{p}$.

## Key Observation

The condition $II^{-1} \subseteq \mathfrak{p}$ with $\mathfrak{p}$ prime implies (since $II^{-1} \subseteq \mathfrak{p}$ and $\mathfrak{p}$ is prime) that either $I \subseteq \mathfrak{p}$ or $I^{-1} \subseteq \mathfrak{p}$.

When $I^{-1} \subseteq \mathfrak{p}$ and $I \not\subseteq \mathfrak{p}$ (which can occur for fractional ideals that are not integral ideals), $IA_\mathfrak{p} = A_\mathfrak{p}$ (since $I$ contains a unit of $A_\mathfrak{p}$), so $(IA_\mathfrak{p})^{-1} = A_\mathfrak{p}$, while $I^{-1}A_\mathfrak{p} \subseteq \mathfrak{p}A_\mathfrak{p} \subsetneq A_\mathfrak{p}$. This gap provides the counterexample.

$$\boxed{No}$$
