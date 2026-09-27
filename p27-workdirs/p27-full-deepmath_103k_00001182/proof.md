# Proof: Galois Group of Q(α)/Q is S₃

## Setup

Let $\alpha$ be a root of $h(X) = X^3 + 3X + \sqrt{3} \in \mathbb{Q}(\sqrt{3})[X]$, and set $K = \mathbb{Q}(\sqrt{3})$.

## Step 1: The minimal polynomial of $\alpha$ over $\mathbb{Q}$

Define the conjugate polynomial $h^*(X) = X^3 + 3X - \sqrt{3}$ (obtained by $\sqrt{3} \mapsto -\sqrt{3}$). Then

$$f(X) = h(X) \cdot h^*(X) = (X^3 + 3X)^2 - 3 = X^6 + 6X^4 + 9X^2 - 3 \in \mathbb{Q}[X].$$

**$f$ is irreducible over $\mathbb{Q}$** by Eisenstein's criterion at $p = 3$: the coefficients $a_5 = 0,\ a_4 = 6,\ a_3 = 0,\ a_2 = 9,\ a_1 = 0,\ a_0 = -3$ are all divisible by $3$, the leading coefficient $a_6 = 1$ is not divisible by $3$, and $a_0 = -3$ is not divisible by $9$.

Since $f(\alpha) = 0$ and $f$ is irreducible of degree $6$, we have $[\mathbb{Q}(\alpha) : \mathbb{Q}] = 6$ and $f$ is the minimal polynomial of $\alpha$ over $\mathbb{Q}$.

## Step 2: $K = \mathbb{Q}(\sqrt{3})$ is a subfield of $\mathbb{Q}(\alpha)$

From $h(\alpha) = 0$ we get $\alpha^3 + 3\alpha + \sqrt{3} = 0$, hence

$$\sqrt{3} = -\alpha^3 - 3\alpha \in \mathbb{Q}(\alpha).$$

Therefore $K \subset \mathbb{Q}(\alpha)$, and $[\mathbb{Q}(\alpha) : K] = [\mathbb{Q}(\alpha) : \mathbb{Q}] / [K : \mathbb{Q}] = 6/2 = 3$.

## Step 3: $h$ is irreducible over $K$

Since $[\mathbb{Q}(\alpha) : K] = 3$ and $\alpha$ is a root of $h$ (which has degree $3$), $h$ must be the minimal polynomial of $\alpha$ over $K$. Hence $h$ is irreducible over $K$.

## Step 4: The discriminant of $h$ over $K$

For a cubic $X^3 + pX + q$, the discriminant is $\Delta = -4p^3 - 27q^2$. Here $p = 3$ and $q = \sqrt{3}$, so

$$\Delta = -4(3)^3 - 27(\sqrt{3})^2 = -108 - 81 = -189 = -3^3 \cdot 7.$$

## Step 5: $\Delta = -189$ is not a square in $K$

The field $K = \mathbb{Q}(\sqrt{3})$ is a subfield of $\mathbb{R}$ (since $\sqrt{3} > 0$ is real). Since $\Delta = -189 < 0$, it cannot be a square in any subfield of $\mathbb{R}$.

(Equivalently: if $(a + b\sqrt{3})^2 = -189$ with $a, b \in \mathbb{Q}$, then $a^2 + 3b^2 + 2ab\sqrt{3} = -189$, requiring $2ab = 0$ and $a^2 + 3b^2 = -189$, which is impossible since $a^2 + 3b^2 \geq 0$.)

## Step 6: The Galois group is $S_3$, not $C_6$

The extension $\mathbb{Q}(\alpha)/\mathbb{Q}$ has degree $6$ with intermediate field $K = \mathbb{Q}(\sqrt{3})$ satisfying $[K:\mathbb{Q}] = 2$ and $[\mathbb{Q}(\alpha):K] = 3$. The two candidate groups of order $6$ are $C_6$ (cyclic) and $S_3$ (symmetric).

**Key criterion.** For an irreducible cubic over a field, the Galois group is $C_3$ (cyclic) if and only if the discriminant is a square in the base field; otherwise it is $S_3$.

- If $\operatorname{Gal}(\mathbb{Q}(\alpha)/\mathbb{Q}) \cong C_6$ (cyclic), then the unique subgroup of order $3$ corresponds to $K$, and $\mathbb{Q}(\alpha)/K$ would be a **cyclic** Galois extension of degree $3$. This requires $h$ to have cyclic Galois group $C_3$ over $K$, which in turn requires $\Delta$ to be a square in $K$.

- If $\operatorname{Gal}(\mathbb{Q}(\alpha)/\mathbb{Q}) \cong S_3$, then the normal subgroup $A_3 \cong C_3$ corresponds to $K$, and $\mathbb{Q}(\alpha)/K$ has Galois group $C_3$. The full group $S_3$ (rather than $C_6$) arises precisely when the cubic $h$ over $K$ has non-square discriminant, giving $\operatorname{Gal}(h/K) \cong S_3$.

Since $\Delta = -189$ is **not** a square in $K$ (Step 5), the cubic $h$ has Galois group $S_3$ over $K$, ruling out the cyclic case $C_6$.

## Conclusion

The Galois group of $\mathbb{Q}(\alpha)/\mathbb{Q}$ is isomorphic to $S_3$.

$$\boxed{S_3}$$

### PROOF COMPLETE
