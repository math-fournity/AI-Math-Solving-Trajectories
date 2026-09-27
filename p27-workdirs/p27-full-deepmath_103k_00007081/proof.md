# Proof that $m_{a,b,c} = 0$ when $a, b, c$ are pairwise unequal nonnegative integers

## Setup

We study the coefficient $m_{a,b,c}$ of the monomial $x_1^{a+c+1}x_2^{a+b+1}x_3^{b+c+1}$ in the expansion of

$$f_{a,b,c}(x_1,x_2,x_3) = (x_1-x_2)^{2a+1}(x_2-x_3)^{2b+1}(x_3-x_1)^{2c+1}.$$

**Total degree check.** The polynomial $f_{a,b,c}$ has total degree $(2a+1)+(2b+1)+(2c+1) = 2a+2b+2c+3$. The target monomial has degree $(a+c+1)+(a+b+1)+(b+c+1) = 2a+2b+2c+3$. These match, so the coefficient is well-defined.

## Step 1: Reduction to two variables by homogeneity

Since $f_{a,b,c}$ is homogeneous of degree $2a+2b+2c+3$, we may set $x_3 = 1$. The coefficient $m_{a,b,c}$ equals the coefficient of $x_1^{a+c+1}x_2^{a+b+1}$ in

$$g(x_1, x_2) = (x_1 - x_2)^{2a+1}(x_2 - 1)^{2b+1}(1 - x_1)^{2c+1}.$$

## Step 2: Binomial expansion

Expand each factor:

$$(x_1 - x_2)^{2a+1} = \sum_{i=0}^{2a+1} \binom{2a+1}{i} x_1^i (-x_2)^{2a+1-i}$$

$$(x_2 - 1)^{2b+1} = \sum_{j=0}^{2b+1} \binom{2b+1}{j} x_2^j (-1)^{2b+1-j}$$

$$(1 - x_1)^{2c+1} = \sum_{k=0}^{2c+1} \binom{2c+1}{k} (-1)^k x_1^k$$

To obtain $x_1^{a+c+1}x_2^{a+b+1}$, we need:
- $i + k = a+c+1$ (power of $x_1$), so $k = a+c+1-i$,
- $(2a+1-i) + j = a+b+1$ (power of $x_2$), so $j = i - a + b$.

## Step 3: Deriving the sum formula

The coefficient of $x_1^{a+c+1}x_2^{a+b+1}$ in $g$ is:

$$m_{a,b,c} = \sum_i \binom{2a+1}{i}(-1)^{2a+1-i} \cdot \binom{2b+1}{i-a+b}(-1)^{2b+1-(i-a+b)} \cdot \binom{2c+1}{a+c+1-i}(-1)^{a+c+1-i}$$

**Sign computation.** The total sign exponent is:

$$(2a+1-i) + (2b+1-i+a-b) + (a+c+1-i) = 4a + b + c + 3 - 3i.$$

Since $4a$ is even, $(-1)^{4a+b+c+3-3i} = (-1)^{b+c+3-3i} = (-1)^{b+c+3}\cdot(-1)^{-3i} = -(-1)^{b+c}\cdot(-1)^{i}$.

Therefore:

$$m_{a,b,c} = -(-1)^{b+c} \sum_i \binom{2a+1}{i}\binom{2b+1}{i-a+b}\binom{2c+1}{a+c+1-i}(-1)^{i}.$$

**Substitution $i = a + t$.** Then $i - a + b = b + t$ and $a + c + 1 - i = c + 1 - t$:

$$m_{a,b,c} = -(-1)^{b+c} \sum_t \binom{2a+1}{a+t}\binom{2b+1}{b+t}\binom{2c+1}{c+1-t}(-1)^{a+t}$$

$$= -(-1)^{a+b+c} \sum_t (-1)^t \binom{2a+1}{a+t}\binom{2b+1}{b+t}\binom{2c+1}{c+1-t}.$$

**Symmetry of the binomial.** Using $\binom{n}{k} = \binom{n}{n-k}$:

$$\binom{2c+1}{c+1-t} = \binom{2c+1}{(2c+1)-(c+1-t)} = \binom{2c+1}{c+t}.$$

Therefore:

$$\boxed{m_{a,b,c} = -(-1)^{a+b+c} \cdot S}, \quad \text{where } S = \sum_t (-1)^t \binom{2a+1}{a+t}\binom{2b+1}{b+t}\binom{2c+1}{c+t}.$$

The sum ranges over all integers $t$ for which the binomial coefficients are nonzero, namely:

$$t \in [\max(-a,-b,-c),\; \min(a+1,\, b+1,\, c+1)].$$

## Step 4: The involution $t \mapsto 1-t$ proves $S = 0$

**Key observation.** Consider the map $\varphi: t \mapsto 1 - t$. This is a fixed-point-free involution on $\mathbb{Z}$ (since $t = 1-t$ implies $t = 1/2 \notin \mathbb{Z}$).

**The summation range is invariant.** The condition $0 \leq a + t \leq 2a+1$ is equivalent to $-a \leq t \leq a+1$. Under $t \mapsto 1-t$, this becomes $-a \leq 1-t \leq a+1$, i.e., $-a \leq t \leq a+1$ — the same range. The same holds for the $b$ and $c$ constraints. Therefore $\varphi$ permutes the summation range.

**The summand at $1-t$ is the negative of the summand at $t$.** We compute:

1. **Sign:** $(-1)^{1-t} = (-1)\cdot(-1)^{-t} = -(-1)^t$.

2. **Binomials:** Using $\binom{n}{k} = \binom{n}{n-k}$:
$$\binom{2a+1}{a+(1-t)} = \binom{2a+1}{a+1-t} = \binom{2a+1}{(2a+1)-(a+1-t)} = \binom{2a+1}{a+t}.$$
Similarly, $\binom{2b+1}{b+1-t} = \binom{2b+1}{b+t}$ and $\binom{2c+1}{c+1-t} = \binom{2c+1}{c+t}$.

Therefore, the summand at $1-t$ equals:

$$(-1)^{1-t}\binom{2a+1}{a+(1-t)}\binom{2b+1}{b+(1-t)}\binom{2c+1}{c+(1-t)} = -(-1)^t \binom{2a+1}{a+t}\binom{2b+1}{b+t}\binom{2c+1}{c+t},$$

which is exactly the **negative** of the summand at $t$.

**Conclusion.** Since $\varphi: t \mapsto 1-t$ is a fixed-point-free involution that preserves the summation range and sends each summand to its negative, the terms pair up and cancel:

$$S = \sum_t (-1)^t \binom{2a+1}{a+t}\binom{2b+1}{b+t}\binom{2c+1}{c+t} = 0.$$

Therefore $m_{a,b,c} = -(-1)^{a+b+c} \cdot 0 = 0$.

## Verification with examples

- **$a=0, b=1, c=2$ (pairwise distinct):** $S = \sum_{t \in \{0,1\}} (-1)^t \binom{1}{t}\binom{3}{1+t}\binom{5}{2+t} = 1\cdot1\cdot3\cdot10 - 1\cdot1\cdot3\cdot10 = 0$. ✓

- **$a=2, b=3, c=5$ (pairwise distinct):** Terms at $t$ and $1-t$ pair as $(-2,3), (-1,2), (0,1)$, each pair summing to zero. ✓

- **$a=1, b=1, c=0$ (not pairwise distinct):** $S = \sum_{t \in \{0,1\}} (-1)^t \binom{3}{1+t}^2 \binom{1}{t} = 9 - 9 = 0$. ✓ (The result holds for all nonneg integers, not just pairwise distinct ones.)

## Final Answer

$$\boxed{m_{a,b,c} = 0}$$

The coefficient $m_{a,b,c}$ is zero when $a, b, c$ are pairwise unequal nonnegative integers. The proof proceeds by:
1. Reducing to two variables via homogeneity ($x_3 = 1$),
2. Expanding all three factors via the binomial theorem and extracting the target coefficient as a signed sum $S$,
3. Applying the binomial symmetry $\binom{n}{k} = \binom{n}{n-k}$ to put the sum in the form $S = \sum_t (-1)^t \prod_{\alpha \in \{a,b,c\}} \binom{2\alpha+1}{\alpha+t}$,
4. Observing that the involution $t \mapsto 1-t$ is fixed-point-free, preserves the summation range, and sends each summand to its negative — forcing $S = 0$.

**Remark.** The argument does not use the pairwise-unequal hypothesis at all; the coefficient $m_{a,b,c} = 0$ for *all* nonnegative integers $a, b, c$.
