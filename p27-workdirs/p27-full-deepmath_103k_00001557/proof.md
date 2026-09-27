# Problem

Let $A \subset \mathbb{R}^N \setminus \{0\}$ be a closed symmetric set (i.e., $x \in A \Rightarrow -x \in A$) such that $A$ is homeomorphic to a sphere $S^n$, where $n \leq N$. Is it possible to construct an odd homeomorphism $F: A \to S^n$ (i.e., $F(-x) = -F(x)$)?

## Answer

$$\boxed{\text{No, in general it is not possible.}}$$

---

## Proof

We interpret the question in the universal sense: "Is it **always** possible, for every such $A$, to construct an odd homeomorphism $F: A \to S^n$?" We show the answer is **No** by exhibiting, for certain values of $n$, a closed symmetric set $A \subset \mathbb{R}^N \setminus \{0\}$ homeomorphic to $S^n$ that admits no odd homeomorphism onto $S^n$.

### Step 1: Reduction to a Conjugacy Problem for Free Involutions

Let $\sigma: A \to A$ denote the negation map $\sigma(x) = -x$. Since $0 \notin A$ and $A$ is symmetric, $\sigma$ is a **free** $\mathbb{Z}_2$-action on $A$ (i.e., $\sigma$ is a fixed-point-free involution).

Choose any homeomorphism $h: S^n \to A$. Transport $\sigma$ to $S^n$ via $h$:
$$\tau := h^{-1} \circ \sigma \circ h : S^n \to S^n.$$
Then $\tau$ is a free involution on $S^n$.

**Claim:** An odd homeomorphism $F: A \to S^n$ exists if and only if $\tau$ is **conjugate** to the antipodal map $\alpha: S^n \to S^n$, $\alpha(p) = -p$ (i.e., there exists a homeomorphism $\varphi: S^n \to S^n$ with $\varphi \circ \tau = \alpha \circ \varphi$).

*Proof of Claim:* 
- ($\Rightarrow$) If $F: A \to S^n$ is an odd homeomorphism, set $\varphi = F \circ h: S^n \to S^n$. Then:
$$\varphi \circ \tau = F \circ h \circ h^{-1} \circ \sigma \circ h = F \circ \sigma \circ h.$$
Since $F$ is odd, $F \circ \sigma = F(-\,\cdot\,) = -F(\,\cdot\,) = \alpha \circ F$, so:
$$\varphi \circ \tau = \alpha \circ F \circ h = \alpha \circ \varphi. \quad \checkmark$$

- ($\Leftarrow$) If $\varphi \circ \tau = \alpha \circ \varphi$ for some homeomorphism $\varphi$, set $F = \varphi \circ h^{-1}: A \to S^n$. Then $F$ is a homeomorphism, and:
$$F \circ \sigma = \varphi \circ h^{-1} \circ \sigma = \varphi \circ \tau \circ h^{-1} = \alpha \circ \varphi \circ h^{-1} = \alpha \circ F,$$
so $F$ is odd. $\square$

### Step 2: Conjugacy $\iff$ Quotient Homeomorphism

**Claim:** The free involution $\tau$ on $S^n$ is conjugate to the antipodal map $\alpha$ if and only if the quotient space $S^n / \tau$ is homeomorphic to $\mathbb{R}P^n$.

*Proof of Claim:*
- ($\Rightarrow$) If $\varphi \circ \tau = \alpha \circ \varphi$, then $\varphi$ descends to a homeomorphism $\bar{\varphi}: S^n/\tau \to S^n/\alpha = \mathbb{R}P^n$.

- ($\Leftarrow$) Suppose $\bar{\psi}: S^n/\tau \xrightarrow{\cong} \mathbb{R}P^n$ is a homeomorphism. Both $S^n \to S^n/\tau$ and $S^n \to \mathbb{R}P^n$ are universal covering maps (since $n \geq 2$, $\pi_1(S^n) = 0$ and the quotients have $\pi_1 = \mathbb{Z}_2$; for $n=1$ the argument is elementary). By the unique lifting property of universal covers, $\bar{\psi}$ lifts to a homeomorphism $\psi: S^n \to S^n$ satisfying $\psi \circ \tau = \alpha \circ \psi$ (using that $\alpha$ is an involution, so $\alpha = \alpha^{-1}$). $\square$

**Summary so far:** An odd homeomorphism $F: A \to S^n$ exists $\iff$ $S^n/\tau \cong \mathbb{R}P^n$ (as topological spaces).

### Step 3: Existence of Exotic Free Involutions

We now show that for $n = 4k + 3$ with $k \geq 1$ (i.e., $n = 7, 11, 15, \ldots$), there exist free involutions $\tau$ on $S^n$ that are **not** conjugate to the antipodal map.

**Construction via exotic projective spaces.** By the surgery exact sequence in topological surgery theory (Wall, *Surgery on Compact Manifolds*), the topological structure set $\mathcal{S}^{\mathrm{Top}}(\mathbb{R}P^n)$ fits into the exact sequence:
$$\cdots \to L_{n+1}(\mathbb{Z}[\mathbb{Z}_2]) \to \mathcal{S}^{\mathrm{Top}}(\mathbb{R}P^n) \to [\mathbb{R}P^n, G/\mathrm{Top}] \to L_n(\mathbb{Z}[\mathbb{Z}_2]) \to \cdots$$

For $n = 4k+3$ with $k \geq 1$, this structure set is **nontrivial**. Concretely, for $n = 7$:

- The group $bP_8$ of homotopy $7$-spheres bounding parallelizable $8$-manifolds is $\mathbb{Z}_{28}$ (Kervaire–Milnor).
- The relevant surgery obstruction groups and normal invariants yield $\mathcal{S}^{\mathrm{Top}}(\mathbb{R}P^7) \neq 0$.

A nontrivial element of $\mathcal{S}^{\mathrm{Top}}(\mathbb{R}P^n)$ corresponds to a closed topological $n$-manifold $M$ that is **homotopy equivalent** to $\mathbb{R}P^n$ but **not homeomorphic** to it. 

Since $M \simeq \mathbb{R}P^n$, we have $\pi_1(M) \cong \mathbb{Z}_2$ and the universal cover $\widetilde{M}$ is a simply connected homology $n$-sphere. By the **Generalized Poincaré Conjecture** (Smale for $n \geq 5$; Freedman for $n = 4$; Perelman for $n = 3$), $\widetilde{M}$ is homeomorphic to $S^n$. The deck transformation group $\mathbb{Z}_2$ acts freely on $\widetilde{M} \cong S^n$, giving a free involution $\tau: S^n \to S^n$ with $S^n / \tau \cong M$.

Since $M \not\cong \mathbb{R}P^n$, by Step 2, $\tau$ is **not** conjugate to the antipodal map. Moreover, by Kirby–Siebenmann theory and the fact that these exotic elements can be represented by smooth manifolds (for $n = 7$, the relevant surgery can be performed in the smooth category), $\tau$ can be taken to be a **smooth** free involution.

### Step 4: Realizing the Exotic Involution as Negation on a Symmetric Set

We now show that any smooth free involution $\tau$ on $S^n$ can be realized as the negation map on some closed symmetric set $A \subset \mathbb{R}^N \setminus \{0\}$ with $A \cong S^n$.

**Construction.** Let $g: S^n \to \mathbb{R}^M$ be a **generic** smooth embedding, with $M \geq 2n + 1$ (such embeddings exist by the Whitney Embedding Theorem; genericity is with respect to the transversality conditions below). Define:
$$f: S^n \to \mathbb{R}^M, \qquad f(x) = g(x) - g(\tau(x)).$$

Set $A = f(S^n) \subset \mathbb{R}^M$ and $N = M$.

**Verification of properties:**

1. **$f$ is odd with respect to $\tau$:** $f(\tau(x)) = g(\tau(x)) - g(\tau^2(x)) = g(\tau(x)) - g(x) = -f(x)$. $\checkmark$

2. **$f(x) \neq 0$ for all $x$:** Since $g$ is injective and $\tau$ is free ($\tau(x) \neq x$), we have $g(x) \neq g(\tau(x))$, so $f(x) \neq 0$. Thus $A \subset \mathbb{R}^M \setminus \{0\}$. $\checkmark$

3. **$A$ is closed and symmetric:** $A = f(S^n)$ is compact (continuous image of compact set), hence closed. Symmetry: if $y = f(x) \in A$, then $-y = f(\tau(x)) \in A$. $\checkmark$

4. **$f$ is injective (hence $A \cong S^n$):** We must show $f(x) = f(y) \Rightarrow x = y$.
   - If $y = \tau(x)$: $f(y) = -f(x) = f(x)$ would imply $f(x) = 0$, contradicting (2). So $y \neq \tau(x)$.
   - If $y \neq x$ and $y \neq \tau(x)$: $f(x) = f(y)$ means $g(x) - g(\tau(x)) = g(y) - g(\tau(y))$, i.e., $\Phi(x,y) := g(x) - g(y) - g(\tau(x)) + g(\tau(y)) = 0$. The map $\Phi$ is defined on the open set $D = \{(x,y) \in S^n \times S^n : x \neq y,\; x \neq \tau(y)\}$, which has dimension $2n$. By the **Parametric Transversality Theorem**, for a generic embedding $g$, the map $\Phi: D \to \mathbb{R}^M$ is transverse to $\{0\}$. Since $\dim D = 2n < M$ (as $M \geq 2n+1$), the preimage $\Phi^{-1}(0)$ has negative dimension, hence is empty. So $f(x) \neq f(y)$. $\checkmark$

5. **$f$ is an immersion (hence a smooth embedding):** The derivative is $df_x(v) = dg_x(v) - dg_{\tau(x)}(d\tau_x(v))$. The condition $df_x(v) = 0$ gives $M$ equations. The space of pairs $(x, v)$ with $v \in T_x S^n$ (up to scaling) has dimension $2n - 1$. For generic $g$, by transversality, $M > 2n - 1$ (satisfied since $M \geq 2n + 1$) ensures no nontrivial kernel. So $f$ is an immersion. Combined with injectivity and compactness of $S^n$, $f$ is a smooth embedding. $\checkmark$

6. **Condition $n \leq N$:** We have $N = M \geq 2n + 1 \geq n$. $\checkmark$

**Key property:** Under the homeomorphism $f: S^n \to A$, the negation map $\sigma$ on $A$ corresponds to $\tau$ on $S^n$:
$$\sigma(f(x)) = -f(x) = f(\tau(x)) = (f \circ \tau \circ f^{-1})(f(x)),$$
so $\sigma = f \circ \tau \circ f^{-1}$, i.e., the transported involution (Step 1) is exactly $\tau$.

### Step 5: Contradiction and Conclusion

Take $n = 7$ and let $\tau$ be an exotic smooth free involution on $S^7$ (not conjugate to the antipodal map), as constructed in Step 3. By Step 4, there exists a closed symmetric set $A \subset \mathbb{R}^{15} \setminus \{0\}$ with $A \cong S^7$, such that the negation map on $A$ corresponds to $\tau$ under this homeomorphism.

**Suppose**, for contradiction, that an odd homeomorphism $F: A \to S^7$ exists. By Step 1, $\tau$ would be conjugate to the antipodal map $\alpha$ on $S^7$. By Step 2, this would mean $S^7/\tau \cong \mathbb{R}P^7$. But $\tau$ was chosen to be exotic (not conjugate to $\alpha$), i.e., $S^7/\tau \not\cong \mathbb{R}P^7$. **Contradiction.**

Therefore, no odd homeomorphism $F: A \to S^7$ exists for this particular $A$.

### Remark on Low Dimensions

For completeness, we note that for $n \leq 3$, the answer is **Yes** (an odd homeomorphism always exists):
- **$n = 1$:** Every free involution on $S^1$ is conjugate to rotation by $\pi$ (the antipodal map); the quotient is always $S^1 \cong \mathbb{R}P^1$.
- **$n = 2$:** The quotient $S^2/\tau$ is a closed surface with $\pi_1 = \mathbb{Z}_2$ and universal cover $S^2$; by the classification of surfaces, it must be $\mathbb{R}P^2$.
- **$n = 3$:** The quotient $S^3/\tau$ is a closed $3$-manifold with $\pi_1 = \mathbb{Z}_2$ and universal cover $S^3$; by geometrization (Perelman), it must be $\mathbb{R}P^3 \cong SO(3)$, and the covering is equivalent to the standard one.

For $n = 4k + 3$ with $k \geq 1$ (i.e., $n = 7, 11, 15, \ldots$), the answer is **No**, as demonstrated above. $\blacksquare$

### PROOF COMPLETE
