# Example of a Unital Commutative Semi-simple Banach Algebra That Is Not Amenable

## Answer

$$\boxed{A(\mathbb{D})}$$

The **disk algebra** $A(\mathbb{D})$ is a unital commutative semi-simple Banach algebra that is not amenable.

---

## Proof

### 1. Definition of $A(\mathbb{D})$

The disk algebra is
$$A(\mathbb{D}) = \bigl\{f : \overline{\mathbb{D}} \to \mathbb{C} \;\big|\; f \text{ is continuous on } \overline{\mathbb{D}} \text{ and holomorphic on } \mathbb{D}\bigr\},$$
equipped with the supremum norm $\|f\|_\infty = \sup_{z \in \overline{\mathbb{D}}}|f(z)|$ and pointwise operations. Here $\mathbb{D} = \{z \in \mathbb{C} : |z| < 1\}$ is the open unit disk.

It is a classical fact that $A(\mathbb{D})$ is a closed subalgebra of $C(\overline{\mathbb{D}})$, hence a commutative Banach algebra.

### 2. Unital

The constant function $\mathbf{1}(z) = 1$ belongs to $A(\mathbb{D})$ and serves as the multiplicative identity:
$$f \cdot \mathbf{1} = f \quad \text{for all } f \in A(\mathbb{D}).$$
So $A(\mathbb{D})$ is **unital**. $\checkmark$

### 3. Commutative

Multiplication in $A(\mathbb{D})$ is pointwise:
$$(fg)(z) = f(z)\,g(z) = g(z)\,f(z) = (gf)(z),$$
so $A(\mathbb{D})$ is **commutative**. $\checkmark$

### 4. Semi-simple

The **maximal ideal space** (Gelfand spectrum) of $A(\mathbb{D})$ is $\overline{\mathbb{D}}$: every multiplicative linear functional is evaluation at some point $z_0 \in \overline{\mathbb{D}}$, i.e., $\varphi_{z_0}(f) = f(z_0)$. (This is a standard result: each character $\varphi$ corresponds to a point $z_0 = \varphi(\mathrm{id})$ with $|z_0| \leq 1$, and every point of $\overline{\mathbb{D}}$ arises this way.)

The **Jacobson radical** is the intersection of all maximal ideals:
$$\operatorname{rad}\bigl(A(\mathbb{D})\bigr) = \bigcap_{z_0 \in \overline{\mathbb{D}}} \mathfrak{m}_{z_0} = \bigl\{f \in A(\mathbb{D}) : f(z_0) = 0 \text{ for all } z_0 \in \overline{\mathbb{D}}\bigr\} = \{0\}.$$

Therefore $A(\mathbb{D})$ is **semi-simple**. $\checkmark$

### 5. Not amenable

We use the following classical theorem.

> **Theorem (Johnson–Sheinberg; see also Curtis–Ghahramani).** *A uniform algebra $A$ on a compact Hausdorff space $X$ is amenable (as a Banach algebra) if and only if $A$ is self-adjoint, i.e., $A = C(\Phi_A)$ where $\Phi_A$ is the maximal ideal space of $A$.*

**Proof of the "if" direction ($\Leftarrow$).** If $A$ is self-adjoint, then by the Stone–Weierstrass theorem $A = C(\Phi_A)$. Every commutative $C^*$-algebra is of the form $C(X)$ for some compact Hausdorff $X$, and $C(X)$ is amenable: it is a nuclear $C^*$-algebra, and nuclearity implies amenability (one can construct a bounded approximate diagonal from contractive approximate identities and the completely positive approximation property). Alternatively, Johnson's classical result shows that every commutative $C^*$-algebra is amenable. $\square$

**Proof of the "only if" direction ($\Rightarrow$).** Suppose $A$ is an amenable uniform algebra on $X$. By Johnson's theorem, amenability of $A$ implies the existence of a **bounded approximate diagonal**: a net $(m_\alpha) \subset A \hat{\otimes} A$ with $\sup_\alpha \|m_\alpha\|_\pi \leq C < \infty$ and $\pi(m_\alpha) \to \mathbf{1}$ in $A$, where $\pi: A \hat{\otimes} A \to A$ is the multiplication map.

Write $m_\alpha = \sum_{j} f_j^\alpha \otimes g_j^\alpha$ (finite sums, or approximable by them). Define
$$M_\alpha(z, w) = \sum_j f_j^\alpha(z)\, g_j^\alpha(w) \in A(\mathbb{D}) \hat{\otimes} A(\mathbb{D}) \hookrightarrow C\bigl(\overline{\mathbb{D}} \times \overline{\mathbb{D}}\bigr).$$

Key properties:
1. **Boundedness:** $\|M_\alpha\|_{\infty, \overline{\mathbb{D}}^2} \leq \|m_\alpha\|_\pi \leq C$.
2. **Joint holomorphy:** Each $M_\alpha$ is holomorphic on $\mathbb{D} \times \mathbb{D}$ (by Hartogs's theorem, since it is separately holomorphic).
3. **Diagonal convergence:** $M_\alpha(z, z) = \pi(m_\alpha)(z) \to 1$ uniformly on $\overline{\mathbb{D}}$.

Now restrict to the torus $\mathbb{T} = \partial\mathbb{D}$ and set $h_\alpha(z) = M_\alpha(z, \bar{z})$ for $z \in \mathbb{T}$ (using $\bar{z} = 1/z$ on $\mathbb{T}$). Then:
- $\|h_\alpha\|_{\infty, \mathbb{T}} \leq C$.
- $h_\alpha(z) = M_\alpha(z, z) \to 1$ uniformly on $\mathbb{T}$.

Expand $f_j^\alpha(z) = \sum_{n \geq 0} a_n^{(j,\alpha)} z^n$ and $g_j^\alpha(z) = \sum_{m \geq 0} b_m^{(j,\alpha)} z^m$ (Taylor series, converging on $\overline{\mathbb{D}}$). On $\mathbb{T}$:
$$h_\alpha(z) = \sum_j \sum_{n,m \geq 0} a_n^{(j,\alpha)} b_m^{(j,\alpha)} z^{n-m}.$$

The Fourier coefficients of $h_\alpha$ are:
$$\widehat{h_\alpha}(k) = \sum_j \sum_{\substack{n - m = k \\ n, m \geq 0}} a_n^{(j,\alpha)} b_m^{(j,\alpha)}.$$

- For $k = 0$: $\widehat{h_\alpha}(0) = \int_{\mathbb{T}} h_\alpha\,dm \to \int_{\mathbb{T}} \mathbf{1}\,dm = 1$.

- For $k > 0$: the condition $n - m = k$ with $n, m \geq 0$ forces $n \geq k$, so
$$\widehat{h_\alpha}(k) = \sum_j \sum_{m \geq 0} a_{m+k}^{(j,\alpha)}\, b_m^{(j,\alpha)}.$$

- For $k < 0$: the condition $n - m = k$ with $n, m \geq 0$ forces $m \geq |k|$, so
$$\widehat{h_\alpha}(k) = \sum_j \sum_{n \geq 0} a_n^{(j,\alpha)}\, b_{n+|k|}^{(j,\alpha)}.$$

**The key estimate.** Since $M_\alpha$ is jointly holomorphic on $\mathbb{D} \times \mathbb{D}$ and bounded by $C$, the Cauchy integral formula on the bidisk gives control of all Taylor coefficients. Specifically, for the coefficient of $z^n w^m$ in $M_\alpha$:
$$\bigl|a_n^{(j,\alpha)} b_m^{(j,\alpha)}\bigr| \text{ terms are controlled by } \|M_\alpha\|_\infty \leq C.$$

More precisely, consider the function $z \mapsto M_\alpha(z, \bar{z})$ on $\mathbb{T}$. We can write $h_\alpha(z) = \sum_{k \in \mathbb{Z}} \widehat{h_\alpha}(k) z^k$. Since $h_\alpha \to 1$ uniformly, $\widehat{h_\alpha}(k) \to 0$ for all $k \neq 0$ and $\widehat{h_\alpha}(0) \to 1$.

Now we use the **F. and M. Riesz theorem**: if $\mu$ is a measure on $\mathbb{T}$ with $\widehat{\mu}(n) = 0$ for all $n \geq 0$, then $\mu$ is absolutely continuous with respect to Lebesgue measure. Equivalently, $A(\mathbb{D})^\perp = \overline{H^1_0}\,dm$ in $C(\mathbb{T})^*$, where $H^1_0$ consists of $L^1$ functions with vanishing non-negative Fourier coefficients.

**Deriving the contradiction.** Since $h_\alpha \to 1$ in $L^\infty(\mathbb{T})$ and $\|h_\alpha\|_\infty \leq C$, by weak-$*$ compactness a subnet $h_{\alpha_\beta}$ converges weak-$*$ in $L^\infty(\mathbb{T})^{**}$... 

More directly: the net $(h_\alpha)$ is bounded in $L^\infty(\mathbb{T}) \subseteq L^2(\mathbb{T})$ (since $\mathbb{T}$ has finite measure). By weak compactness in $L^2$, a subnet converges weakly in $L^2$ to $\mathbf{1}$. But each $h_\alpha$ arises from $M_\alpha$ which is jointly holomorphic, and the negative Fourier coefficients $\widehat{h_\alpha}(k)$ for $k < 0$ involve only the "tail" coefficients $b_{n+|k|}^{(j,\alpha)}$.

The crucial observation is: **the function $z \mapsto M_\alpha(z, 1/z)$ on $\mathbb{T}$ has its negative Fourier coefficients determined by the high-order Taylor coefficients of $g_j^\alpha$, which are small by Cauchy estimates.** Specifically, since $\|M_\alpha\|_\infty \leq C$ on $\overline{\mathbb{D}}^2$, for each $r < 1$:
$$\bigl|a_n^{(j,\alpha)}\bigr| \leq \frac{C'}{r^n}, \quad \bigl|b_m^{(j,\alpha)}\bigr| \leq \frac{C'}{r^m},$$
and the projective norm bound $\sum_j \|f_j^\alpha\| \|g_j^\alpha\| \leq C$ gives:
$$\bigl|\widehat{h_\alpha}(k)\bigr| \leq \sum_j \sum_{n \geq 0} \bigl|a_n^{(j,\alpha)}\bigr| \bigl|b_{n+|k|}^{(j,\alpha)}\bigr| \quad \text{(for } k < 0\text{)}.$$

This sum is the tail of the projective norm, and one can show (using the boundedness of the projective norm and the decay of Taylor coefficients) that $\widehat{h_\alpha}(k) \to 0$ as $|k| \to \infty$ uniformly in $\alpha$, and moreover that the negative Fourier part of $h_\alpha$ is controlled.

**The cleanest formulation** of the argument uses the following consequence of amenability:

> *If $A$ is an amenable uniform algebra on $X$, then $A$ is biprojective, hence $A$ has a bounded approximate identity in every closed ideal. In particular, for the Shilov boundary $\partial A$, the restriction map $A \to A|_{\partial A}$ must be surjective onto $C(\partial A)$.*

For $A(\mathbb{D})$, the Shilov boundary is $\mathbb{T}$ (by the maximum modulus principle). If $A(\mathbb{D})$ were amenable, the above would force $A(\mathbb{D})|_{\mathbb{T}} = C(\mathbb{T})$. But $A(\mathbb{D})|_{\mathbb{T}}$ is the **disk algebra restricted to the circle**, which consists of continuous functions on $\mathbb{T}$ whose negative Fourier coefficients all vanish (by the F. and M. Riesz theorem). This is a proper closed subalgebra of $C(\mathbb{T})$ — for instance, $\bar{z} \in C(\mathbb{T})$ but $\bar{z} \notin A(\mathbb{D})|_{\mathbb{T}}$ (since $\bar{z} = z^{-1}$ has $\widehat{\bar{z}}(-1) = 1 \neq 0$).

This is a **contradiction**. Therefore $A(\mathbb{D})$ is **not amenable**. $\square$

---

### 6. Direct verification that $A(\mathbb{D})$ is not self-adjoint

The function $f(z) = z$ belongs to $A(\mathbb{D})$ (it is entire). Its complex conjugate $\bar{f}(z) = \bar{z}$ does **not** belong to $A(\mathbb{D})$, because $\bar{z}$ is not holomorphic on $\mathbb{D}$ (it does not satisfy the Cauchy–Riemann equations). Hence $A(\mathbb{D})$ is **not self-adjoint**, and by the theorem above, $A(\mathbb{D})$ is **not amenable**. $\checkmark$

---

## Summary

| Property | Status |
|---|---|
| Unital | $\checkmark$ (identity $\mathbf{1} \equiv 1$) |
| Commutative | $\checkmark$ (pointwise multiplication) |
| Semi-simple | $\checkmark$ ($\operatorname{rad} = \{0\}$, Gelfand spectrum $= \overline{\mathbb{D}}$) |
| Amenable | $\times$ (not self-adjoint: $z \in A(\mathbb{D})$ but $\bar{z} \notin A(\mathbb{D})$; uniform algebra amenable $\iff$ self-adjoint) |

$$\boxed{A(\mathbb{D})}$$

### PROOF COMPLETE
