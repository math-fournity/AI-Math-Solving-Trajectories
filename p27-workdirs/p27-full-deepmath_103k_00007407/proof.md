# Solution

## Answer

$$\boxed{\text{No in general (for } n \geq 2\text{). Yes for } n = 1.}$$

For $n \geq 2$, there exist open covers $\{U_\lambda\}$ of $\mathbb{R}^n$ and function families $\{f_\lambda\}$ satisfying the given conditions for which no global $f$ exists. For $n = 1$, such an $f$ always exists.

---

## Part I: Counterexample for $n \geq 2$

We construct an explicit counterexample on $\mathbb{R}^2$. The construction extends to $\mathbb{R}^n$ for $n \geq 2$ by taking products with $\mathbb{R}^{n-2}$.

### 1. The open cover

Fix $\epsilon \in (0, 1/2)$. Use polar coordinates $(r, \theta)$ on $\mathbb{R}^2$.

**Three arcs on $S^1$.** Define open arcs (in degrees):
$$A_1 = (-10°, 130°), \quad A_2 = (110°, 250°), \quad A_3 = (230°, 370°).$$

These satisfy:
- $A_1 \cup A_2 \cup A_3 = S^1$ (every angle is covered),
- $A_i \cap A_j \neq \emptyset$ for each pair (non-empty open arc),
- $A_1 \cap A_2 \cap A_3 = \emptyset$ (no angle lies in all three).

**Four open sets.** Define:
$$U_i = \bigl\{(r\cos\theta,\, r\sin\theta) : \theta \in A_i,\; r \in (1-\epsilon,\, 1+\epsilon)\bigr\}, \quad i = 1, 2, 3,$$
$$U_4 = \bigl\{(x,y) : x^2 + y^2 < (1-\epsilon)^2\bigr\} \cup \bigl\{(x,y) : x^2 + y^2 > (1+\epsilon)^2\bigr\}.$$

**Properties:**
- **Open:** Each $U_i$ is open in $\mathbb{R}^2$ (polar coordinate map is a local diffeomorphism for $r > 0$, and $\epsilon < 1/2$ ensures $r > 0$). $U_4$ is a union of two open sets.
- **Cover:** Any point has $r \in [0, \infty)$. If $r \in (1-\epsilon, 1+\epsilon)$, its angle $\theta$ lies in some $A_i$, so it is in $U_i$. If $r < 1-\epsilon$ or $r > 1+\epsilon$, it is in $U_4$. Hence $U_1 \cup U_2 \cup U_3 \cup U_4 = \mathbb{R}^2$.
- **Each $U_i$ ($i \leq 3$) is connected:** $U_i \cong A_i \times (1-\epsilon, 1+\epsilon)$, a product of connected sets.
- **$U_4$ has two connected components:** the inner disk $D_{\text{in}} = \{r < 1-\epsilon\}$ and the outer region $D_{\text{out}} = \{r > 1+\epsilon\}$.
- **Pairwise intersections among $U_1, U_2, U_3$:** $U_i \cap U_j = \{(r\cos\theta, r\sin\theta) : \theta \in A_i \cap A_j,\; r \in (1-\epsilon, 1+\epsilon)\}$, which is connected (non-empty open arc $\times$ interval). There are three such: $U_{12}, U_{13}, U_{23}$.
- **$U_i \cap U_4 = \emptyset$ for $i = 1, 2, 3$:** $U_i$ has $r \in (1-\epsilon, 1+\epsilon)$ while $U_4$ has $r < 1-\epsilon$ or $r > 1+\epsilon$. Disjoint.
- **Triple intersection $U_1 \cap U_2 \cap U_3 = \emptyset$:** follows from $A_1 \cap A_2 \cap A_3 = \emptyset$.
- **All other triple intersections empty:** any triple involving $U_4$ is empty since $U_4 \cap U_i = \emptyset$.

### 2. The Čech cohomology computation

Since all $U_i$ ($i \leq 3$) are connected and $U_4$ has 2 components, and all non-empty pairwise intersections are connected, and all triple intersections are empty:

$$\check{C}^0 = \underline{\mathbb{R}}(U_1) \oplus \underline{\mathbb{R}}(U_2) \oplus \underline{\mathbb{R}}(U_3) \oplus \underline{\mathbb{R}}(U_4) = \mathbb{R} \oplus \mathbb{R} \oplus \mathbb{R} \oplus \mathbb{R}^2 = \mathbb{R}^5,$$

$$\check{C}^1 = \underline{\mathbb{R}}(U_{12}) \oplus \underline{\mathbb{R}}(U_{13}) \oplus \underline{\mathbb{R}}(U_{23}) = \mathbb{R}^3 \quad (\text{only non-empty pairwise intersections}),$$

$$\check{C}^2 = 0 \quad (\text{all triple intersections empty}).$$

The differential $\delta^0: \check{C}^0 \to \check{C}^1$ sends $(c_1, c_2, c_3, d_1, d_2)$ to $(c_2 - c_1,\; c_3 - c_1,\; c_3 - c_2)$. The components $d_1, d_2$ (from $U_4$) do not appear since $U_4$ intersects no other set. The image is:
$$\operatorname{im}(\delta^0) = \{(a, b, c) \in \mathbb{R}^3 : a - b + c = 0\} \cong \mathbb{R}^2.$$

Since $\check{C}^2 = 0$, we have $\ker(\delta^1) = \check{C}^1 = \mathbb{R}^3$. Therefore:
$$\check{H}^1\bigl(\{U_\lambda\},\, \underline{\mathbb{R}}\bigr) = \mathbb{R}^3 / \mathbb{R}^2 \cong \mathbb{R} \neq 0.$$

### 3. The function family (non-trivial cocycle)

Define $f_\lambda: U_\lambda \to \mathbb{R}$ (arbitrary functions, not required to be continuous):

$$f_1 \equiv 0 \text{ on } U_1, \qquad f_2 \equiv 0 \text{ on } U_2, \qquad f_4 \equiv 0 \text{ on } U_4,$$

$$f_3(p) = \begin{cases} -1 & \text{if } p \in U_1 \cap U_3, \\ \phantom{-}0 & \text{if } p \in U_3 \setminus (U_1 \cap U_3). \end{cases}$$

This is well-defined since $U_1 \cap U_3$ and $U_3 \setminus (U_1 \cap U_3)$ partition $U_3$.

**Verification that $f_\lambda - f_\mu$ is constant on each $U_\lambda \cap U_\mu$:**

| Intersection | Computation | Constant |
|---|---|---|
| $U_1 \cap U_2$ | $f_1 - f_2 = 0 - 0 = 0$ | $0$ ✓ |
| $U_1 \cap U_3$ | $f_1 - f_3 = 0 - (-1) = 1$ | $1$ ✓ |
| $U_2 \cap U_3$ | $f_2 - f_3 = 0 - 0 = 0$ (since $U_2 \cap U_3 \subset U_3 \setminus U_{13}$, as $U_{23} \cap U_{13} = U_{123} = \emptyset$) | $0$ ✓ |
| $U_i \cap U_4$ | empty | vacuous ✓ |

### 4. Non-existence of global $f$

Suppose for contradiction that $f: \mathbb{R}^2 \to \mathbb{R}$ exists with $f - f_\lambda = c_\lambda$ (constant) on $U_\lambda$.

- **On $U_1 \cap U_2$:** $f = f_1 + c_1 = c_1$ and $f = f_2 + c_2 = c_2$, so $c_1 = c_2$.
- **On $U_2 \cap U_3$:** $f = f_2 + c_2 = c_2$ and $f = f_3 + c_3 = 0 + c_3 = c_3$, so $c_2 = c_3$.
- **On $U_1 \cap U_3$:** $f = f_1 + c_1 = c_1$ and $f = f_3 + c_3 = -1 + c_3$, so $c_1 = c_3 - 1$, i.e., $c_3 - c_1 = 1$.

From the first two: $c_1 = c_2 = c_3$. From the third: $c_3 - c_1 = 1$, giving $0 = 1$. **Contradiction.** $\square$

### 5. Extension to $\mathbb{R}^n$ for $n > 2$

For $n > 2$, write $\mathbb{R}^n = \mathbb{R}^2 \times \mathbb{R}^{n-2}$ and set $U_i' = U_i \times \mathbb{R}^{n-2}$. Since $\mathbb{R}^{n-2}$ is connected, the connectedness properties of all sets and intersections are preserved, the nerve is unchanged, and the Čech complex is identical. The same function family (extended trivially) and the same contradiction apply.

---

## Part II: The case $n = 1$ (answer is YES)

For $n = 1$, such an $f$ **always exists**.

**Key fact:** Every open subset of $\mathbb{R}$ is a disjoint union of open intervals, each contractible. Therefore, for any open $V \subseteq \mathbb{R}$, the sheaf cohomology $H^p(V, \underline{\mathbb{R}}) = 0$ for all $p \geq 1$ (the constant sheaf on a disjoint union of contractible sets is acyclic).

**Leray's theorem:** If every finite intersection $U_{\lambda_0 \cdots \lambda_p}$ is acyclic for the sheaf $\underline{\mathbb{R}}$ (i.e., $H^q(U_{\lambda_0 \cdots \lambda_p}, \underline{\mathbb{R}}) = 0$ for $q \geq 1$), then the fixed-cover Čech cohomology equals the sheaf cohomology:
$$\check{H}^p(\mathcal{U}, \underline{\mathbb{R}}) \cong H^p(\mathbb{R}, \underline{\mathbb{R}}).$$

For $\mathbb{R}$: every finite intersection of open sets is open, hence a disjoint union of intervals, hence acyclic. So Leray's theorem applies to **every** open cover of $\mathbb{R}$, giving:
$$\check{H}^1(\mathcal{U}, \underline{\mathbb{R}}) \cong H^1(\mathbb{R}, \underline{\mathbb{R}}) = 0$$
since $\mathbb{R}$ is contractible. The obstruction group vanishes, so the global $f$ always exists. $\square$

---

## Part III: Conceptual framework (summary)

The problem is equivalent to a Čech 1-cocycle question. Setting $c_{\lambda\mu} = f_\lambda - f_\mu$ (constant on $U_\lambda \cap U_\mu$), the existence of $f$ with $f - f_\lambda = c_\lambda$ requires $c_{\lambda\mu} = c_\mu - c_\lambda$, i.e., the cocycle $\{c_{\lambda\mu}\}$ must be a coboundary. The obstruction lies in $\check{H}^1(\{U_\lambda\}, \underline{\mathbb{R}})$.

For $n \geq 2$, open subsets of $\mathbb{R}^n$ can have non-trivial topology (e.g., non-contractible connected sets), so Leray's theorem does not apply to all covers, and $\check{H}^1$ can be non-zero — as our counterexample demonstrates.

For $n = 1$, all open subsets are acyclic for the constant sheaf, so Leray's theorem forces $\check{H}^1 = 0$ for every cover.

### PROOF COMPLETE
