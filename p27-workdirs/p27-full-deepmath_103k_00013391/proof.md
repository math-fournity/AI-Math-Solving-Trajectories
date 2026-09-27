# Proof: Existence of $uL$ with no nonzero $p$-algebraic elements and infinite global dimension

**Answer:** $\boxed{\text{Yes}}$

## Construction

Let $k$ be a field of characteristic $p > 0$. We construct an (infinite-dimensional) abelian restricted Lie algebra $L$ over $k$ as follows.

- **Underlying vector space:** $L$ has $k$-basis $\{e_n : n \geq 1\}$.
- **Lie bracket:** $[e_m, e_n] = 0$ for all $m, n$ (i.e., $L$ is abelian).
- **$p$-operation:** $e_n^{[p]} = e_{2n}$ for all $n \geq 1$, extended $p$-semilinearly:
$$\left(\sum_{n} a_n e_n\right)^{[p]} = \sum_{n} a_n^p\, e_{2n}.$$

## Verification that $L$ is a restricted Lie algebra

For an abelian Lie algebra, the restricted Lie algebra axioms reduce to:

1. **$p$-semilinearity:** $(\alpha x)^{[p]} = \alpha^p x^{[p]}$ for $\alpha \in k$, $x \in L$. This holds by definition: $(\alpha \sum a_n e_n)^{[p]} = \sum (\alpha a_n)^p e_{2n} = \alpha^p \sum a_n^p e_{2n} = \alpha^p (\sum a_n e_n)^{[p]}$.

2. **Additivity:** $(x + y)^{[p]} = x^{[p]} + y^{[p]}$. This follows from the Freshman's dream identity $(a + b)^p = a^p + b^p$ in characteristic $p$:
$$\left(\sum (a_n + b_n) e_n\right)^{[p]} = \sum (a_n + b_n)^p e_{2n} = \sum (a_n^p + b_n^p) e_{2n} = \left(\sum a_n e_n\right)^{[p]} + \left(\sum b_n e_n\right)^{[p]}.$$

3. **Compatibility:** $[x^{[p]}, y] = \operatorname{ad}(x)^p(y)$. Since $L$ is abelian, both sides are $0$. ✓

4. **Closure:** $e_{2n} \in L$ for all $n \geq 1$ since $2n \geq 1$. ✓

Hence $L$ is a well-defined restricted Lie algebra.

## $L$ has no nonzero $p$-algebraic elements

**Definition.** An element $x \in L$ is *$p$-algebraic* if the sequence $x, x^{[p]}, x^{[p]^2}, \ldots$ is linearly dependent over $k$.

**Claim.** Every nonzero element of $L$ is not $p$-algebraic.

*Proof.* Let $x = \sum_{i=1}^{N} a_i e_i \in L$ be nonzero, with $a_N \neq 0$ (so $N$ is the largest index with a nonzero coefficient). We compute the iterated $p$-powers:

$$x^{[p]^n} = \sum_{i=1}^{N} a_i^{p^n}\, e_{2^n i}.$$

The **leading term** of $x^{[p]^n}$ (the term with the largest basis index) is $a_N^{p^n}\, e_{2^n N}$, with coefficient $a_N^{p^n} \neq 0$ (since $k$ is a field, $a_N \neq 0$ implies $a_N^{p^n} \neq 0$).

Now consider any linear combination $\sum_{n=0}^{M} c_n\, x^{[p]^n} = 0$ with $c_n \in k$. Look at the coefficient of the basis element $e_{2^M N}$ (the largest index appearing). This basis element appears **only** in $x^{[p]^M}$ (since $2^M N > 2^n N$ for $n < M$, and $2^M N > 2^M i$ for $i < N$). Its coefficient is $c_M\, a_N^{p^M}$.

For the linear combination to be zero, we need $c_M\, a_N^{p^M} = 0$. Since $a_N^{p^M} \neq 0$, we get $c_M = 0$. By induction backward on $M$, all $c_n = 0$.

Therefore $x, x^{[p]}, x^{[p]^2}, \ldots$ are linearly independent, so $x$ is not $p$-algebraic. $\square$

## Computation of $uL$

Since $L$ is abelian, the ordinary universal enveloping algebra is the symmetric algebra:
$$UL = S(L) = k[e_1, e_2, e_3, \ldots]$$
(the polynomial ring in countably many variables).

The restricted universal enveloping algebra is:
$$uL = UL \big/ \left(e_n^p - e_n^{[p]} : n \geq 1\right) = k[e_1, e_2, e_3, \ldots] \big/ \left(e_n^p - e_{2n} : n \geq 1\right).$$

**Rewriting system.** The relations $e_{2n} = e_n^p$ allow us to eliminate every even-indexed variable:
- $e_{2m} = e_m^p$ for all $m \geq 1$.
- Iterating: $e_{2^k m} = e_m^{p^k}$ for all $k \geq 0$, $m \geq 1$.

Every positive integer $n$ has a unique factorization $n = 2^k m$ where $m$ is odd and $k \geq 0$. Thus every variable $e_n$ can be expressed as $e_m^{p^k}$ where $m$ is odd.

**The independent generators** are $\{e_m : m \text{ odd}, m \geq 1\} = \{e_1, e_3, e_5, e_7, \ldots\}$, which is an infinite set.

**Claim.** $uL \cong k[\{x_m : m \geq 1 \text{ odd}\}]$, the polynomial ring in countably infinitely many variables.

*Proof.* Define a $k$-algebra homomorphism
$$\psi: k[e_1, e_2, e_3, \ldots] \to k[\{x_m : m \text{ odd}\}]$$
by $\psi(e_n) = x_m^{p^k}$ where $n = 2^k m$ with $m$ odd. Then:
$$\psi(e_n^p) = x_m^{p^{k+1}} = \psi(e_{2n})$$
since $2n = 2^{k+1} m$. So $\psi$ vanishes on the ideal $(e_n^p - e_{2n})$ and descends to a homomorphism $\bar{\psi}: uL \to k[\{x_m : m \text{ odd}\}]$.

**Surjectivity:** $\bar{\psi}(e_m) = x_m$ for each odd $m$, so all generators of the target are in the image.

**Injectivity:** Any element of $uL$ can be represented (after applying the rewriting rules $e_{2n} \to e_n^p$ repeatedly) as a polynomial $f$ in the odd-indexed variables $\{e_m : m \text{ odd}\}$. If $\bar{\psi}(f) = 0$, then $f$ (viewed as a polynomial in the algebraically independent variables $\{x_m\}$) must be zero. Hence $f = 0$ in $uL$.

The rewriting system is confluent: the only overlap occurs when $e_{2n}$ itself has an even index (i.e., $n$ is even, say $n = 2m$), giving $e_{2(2m)} = e_{4m}$, which rewrites to $e_{2m}^p = (e_m^p)^p = e_m^{p^2}$. Directly, $e_{4m} \to e_{2m}^p \to (e_m^p)^p = e_m^{p^2}$, and there is only one reduction path. So the system is confluent (no critical pairs), and the normal form is unique.

Therefore $uL \cong k[\{x_m : m \geq 1 \text{ odd}\}]$. $\square$

## Global dimension of $uL$ is infinite

$uL \cong k[x_1, x_3, x_5, \ldots]$ is a polynomial ring in countably infinitely many variables over $k$.

**Claim.** $\operatorname{gldim}(uL) = \infty$.

*Proof.* For each $n \geq 1$, let $R_n = k[x_1, x_3, x_5, \ldots, x_{2n-1}]$ be the polynomial subring in the first $n$ odd-indexed variables. Then $R_n \subset uL$ is a polynomial extension (hence flat), and:
- $\operatorname{gldim}(R_n) = n$ (global dimension of a polynomial ring in $n$ variables over a field).
- The residue field $k = R_n / (x_1, x_3, \ldots, x_{2n-1})$ has $\operatorname{pd}_{R_n}(k) = n$ (via the Koszul resolution).

Since $uL$ is flat over $R_n$, we have $uL \otimes_{R_n} k \cong k$ (as an $uL$-module), and by flat base change:
$$\operatorname{pd}_{uL}(k) \geq \operatorname{pd}_{R_n}(k) = n.$$

This holds for every $n \geq 1$, so $\operatorname{pd}_{uL}(k) = \infty$, which implies $\operatorname{gldim}(uL) = \infty$. $\square$

## Conclusion

We have constructed a restricted Lie algebra $L$ over $k$ (of any characteristic $p > 0$) such that:

1. **$L$ has no nonzero $p$-algebraic elements** (proved in §3 via the leading-term argument), and
2. **$\operatorname{gldim}(uL) = \infty$** (proved in §5, since $uL$ is a polynomial ring in countably many variables).

Therefore, such an $L$ exists.

$$\boxed{\text{Yes}}$$

### PROOF COMPLETE
