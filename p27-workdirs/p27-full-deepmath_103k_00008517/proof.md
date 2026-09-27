# Proof: If $(Ke_i, e_j) \to 0$ for every Hilbert basis, then $K$ is compact

## Answer

Yes, $K$ must be compact.

$$\boxed{K \text{ is compact}}$$

## Proof

We assume $K$ is a bounded linear operator on a separable Hilbert space $H$. (The condition that $(Ke_i, e_j)$ is well-defined for every basis element $e_i$ requires $K$ to be everywhere defined; the standard setting for compact operators is bounded operators.)

**Trivial direction.** If $K$ is compact, then for any orthonormal basis $\{e_i\}$, since $e_i \to 0$ weakly, compactness gives $\|Ke_i\| \to 0$. Hence $|(Ke_i, e_j)| \leq \|Ke_i\| \to 0$ as $i \to \infty$ (uniformly in $j$), so the condition holds.

**Converse (main proof).** We prove the contrapositive: if $K$ is bounded and **not** compact, then there exists an orthonormal basis $\{e_i\}$ such that $(Ke_i, e_j) \not\to 0$ as $i, j \to \infty$.

Since $K$ is not compact, there exists an orthonormal sequence $\{f_n\}_{n=1}^\infty$ and $\epsilon > 0$ such that
$$\|Kf_n\| \geq \epsilon \quad \text{for all } n.$$
(This is a standard characterization: $K$ is compact iff $\|Kf_n\| \to 0$ for every orthonormal sequence $\{f_n\}$.)

Set $u_n = Kf_n / \|Kf_n\|$, so $\|u_n\| = 1$ and
$$(Kf_n, u_n) = \|Kf_n\| \geq \epsilon.$$
Since $f_n \to 0$ weakly and $K$ is bounded (hence weak-to-weak continuous), $u_n \to 0$ weakly.

Let $M = \overline{\operatorname{span}}\{f_n\}$ and let $P_M$ denote the orthogonal projection onto $M$. We consider two cases.

---

### Case 1: $\|P_{M^\perp} Kf_n\| \geq \epsilon/2$ for infinitely many $n$.

Passing to a subsequence (still denoted $\{f_n\}$), assume $\|P_{M^\perp} Kf_n\| \geq \epsilon/2$ for all $n$. Define
$$v_n = \frac{P_{M^\perp} Kf_n}{\|P_{M^\perp} Kf_n\|} \in M^\perp, \quad \|v_n\| = 1.$$
Then $(Kf_n, v_n) = \|P_{M^\perp} Kf_n\| \geq \epsilon/2$, and $v_n \to 0$ weakly (since $Kf_n \to 0$ weakly and $P_{M^\perp}$ is weak-continuous).

Since $v_n \to 0$ weakly, by the Bessaga–Pełczyński selection principle, we extract a subsequence $\{v_{n_k}\}$ that is a basic sequence equivalent to an orthonormal sequence. Applying Gram–Schmidt, we obtain an orthonormal sequence $\{w_k\} \subset M^\perp$ with $\|w_k - v_{n_k}\| \to 0$ (by choosing the subsequence so that off-diagonal inner products decay sufficiently fast). For large $k$,
$$|(Kf_{n_k}, w_k)| \geq |(Kf_{n_k}, v_{n_k})| - \|K\|\|w_k - v_{n_k}\| \geq \frac{\epsilon}{2} - \frac{\epsilon}{4} = \frac{\epsilon}{4}.$$

**Key observation:** $\{f_{n_k}\} \subset M$ and $\{w_k\} \subset M^\perp$, so these two sequences are **automatically orthogonal** to each other. Since each is orthonormal, the interleaved sequence
$$e_1 = f_{n_1},\ e_2 = w_1,\ e_3 = f_{n_2},\ e_4 = w_2,\ \ldots$$
is **orthonormal** without any further Gram–Schmidt needed. Extend it to an orthonormal basis of $H$.

In this basis, $|(Ke_{2k-1}, e_{2k})| = |(Kf_{n_k}, w_k)| \geq \epsilon/4$ for all large $k$, while $2k-1, 2k \to \infty$. The condition fails. $\checkmark$

---

### Case 2: $\|P_M Kf_n\| \geq \epsilon/2$ for all sufficiently large $n$.

Passing to a subsequence, assume $\|P_M Kf_n\| \geq \epsilon/2$ for all $n$. Define
$$g_n = \frac{P_M Kf_n}{\|P_M Kf_n\|} \in M, \quad \|g_n\| = 1.$$
Then $(Kf_n, g_n) = \|P_M Kf_n\| \geq \epsilon/2$, and $g_n \to 0$ weakly.

We split into two sub-cases.

#### Sub-case 2a: $|(Kf_n, f_n)| \geq \epsilon/2$ for infinitely many $n$.

Extend $\{f_n\}$ to an orthonormal basis of $H$. In this basis, the diagonal entries $(Kf_n, f_n)$ satisfy $|(Kf_n, f_n)| \geq \epsilon/2$ for infinitely many $n \to \infty$. Taking $i = j = n \to \infty$, the condition fails. $\checkmark$

#### Sub-case 2b: $(Kf_n, f_n) \to 0$ (after passing to a subsequence).

Then $(f_n, g_n) = \overline{(Kf_n, f_n)} / \|P_M Kf_n\| \to 0$ (since $|(Kf_n, f_n)| \to 0$ and $\|P_M Kf_n\| \geq \epsilon/2$).

For each $n$, define $b_n$ to be the normalized component of $g_n$ orthogonal to $f_n$:
$$b_n = \frac{g_n - (g_n, f_n) f_n}{\|g_n - (g_n, f_n) f_n\|}.$$
For large $n$, $|(g_n, f_n)| < 1/2$, so $b_n$ is well-defined, $\|b_n\| = 1$, $b_n \perp f_n$, and $\{f_n, b_n\}$ is an orthonormal basis of $W_n := \operatorname{span}\{f_n, g_n\}$.

**Compute $(Kf_n, b_n)$:**
$$
(Kf_n, b_n) = \frac{(Kf_n, g_n) - (g_n, f_n)(Kf_n, f_n)}{\sqrt{1 - |(g_n, f_n)|^2}}.
$$
The numerator satisfies $(Kf_n, g_n) \geq \epsilon/2$ and $|(g_n, f_n)(Kf_n, f_n)| \to 0$, so for large $n$ the numerator is $\geq \epsilon/3$. The denominator $\to 1$. Hence
$$|(Kf_n, b_n)| \geq \frac{\epsilon}{4} \quad \text{for all large } n.$$

**Inductive block construction.** We construct a subsequence $\{n_k\}$ and the corresponding blocks $\{a_k, b_k'\} = \{f_{n_k}, b_{n_k}\}$ inductively.

At step $k$, choose $n_k$ large enough that:
1. $|(Kf_{n_k}, f_{n_k})|$ is small enough that $|(Kf_{n_k}, b_{n_k})| \geq \epsilon/4$;
2. $|(f_{n_k}, a_j)|, |(f_{n_k}, b_j')|, |(g_{n_k}, a_j)|, |(g_{n_k}, b_j')| < \delta_k$ for all $j < k$, where $\delta_k = \delta / 2^k$ for a small $\delta > 0$ to be chosen.

Condition 2 is achievable because $f_n \to 0$ weakly and $g_n \to 0$ weakly, so inner products with any fixed finite set of vectors tend to 0.

Set $a_k = f_{n_k}$ and $b_k' = b_{n_k}$. Then $\{a_k, b_k'\}$ is an orthonormal pair in $W_{n_k}$, and the cross-block inner products satisfy: for $j \neq k$,
$$|(a_k, a_j)|, |(a_k, b_j')|, |(b_k', a_j)|, |(b_k', b_j')| < \max(\delta_k, \delta_j) = \delta_{\min(k,j)} \leq \delta / 2^{\min(k,j)}.$$

**Gram–Schmidt orthonormalization.** Apply Gram–Schmidt to the sequence $a_1, b_1', a_2, b_2', \ldots$ to obtain an orthonormal sequence $e_1, e_2, e_3, e_4, \ldots$.

For each vector $v$ in the sequence, the $\ell^2$-norm of its cross-block inner products with all other vectors is:
$$
\sum_{\text{cross}} |(v, v')|^2 \leq \sum_{j < k} 4\delta_k^2 + \sum_{j > k} 4\delta_j^2 = \frac{4(k-1)\delta^2}{4^k} + \frac{4\delta^2}{3 \cdot 4^k} \leq \frac{C_0 \delta^2}{4^k}
$$
for some constant $C_0$. For large $k$, this is $< \delta^2$. By the standard Gram–Schmidt perturbation estimate, for large $k$:
$$\|e_{2k-1} - a_k\| \leq C_1 \delta / 2^k, \qquad \|e_{2k} - b_k'\| \leq C_1 \delta / 2^k$$
for some constant $C_1$ depending only on the geometry.

**Estimate $(Ke_{2k-1}, e_{2k})$:**
$$
|(Ke_{2k-1}, e_{2k}) - (Ka_k, b_k')| \leq \|K\|\bigl(\|e_{2k-1} - a_k\| + \|e_{2k} - b_k'\|\bigr) \leq \frac{2C_1 \|K\| \delta}{2^k}.
$$
Since $(Ka_k, b_k') = (Kf_{n_k}, b_{n_k}) \geq \epsilon/4$, for large $k$:
$$|(Ke_{2k-1}, e_{2k})| \geq \frac{\epsilon}{4} - \frac{2C_1 \|K\| \delta}{2^k} \geq \frac{\epsilon}{8}.$$

Extend $\{e_k\}$ to an orthonormal basis of $H$. Then $|(Ke_{2k-1}, e_{2k})| \geq \epsilon/8$ for all large $k$, with $2k-1, 2k \to \infty$. The condition fails. $\checkmark$

---

### Conclusion

In all cases, if $K$ is bounded and not compact, we can construct an orthonormal basis where $(Ke_i, e_j) \not\to 0$ as $i, j \to \infty$. By contraposition, if the condition holds for **every** orthonormal basis, then $K$ must be compact.

$$\boxed{K \text{ is compact}}$$
