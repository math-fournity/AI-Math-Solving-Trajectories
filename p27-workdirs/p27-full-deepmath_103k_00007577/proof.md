# Proof

## Answer

For $n = 1$: **Yes** (trivially). For $n \geq 2$: **No**.

$$\boxed{\text{No (for } n \geq 2\text{)}}$$

---

## Clarification of "asymptotically nilpotent"

A matrix $A \in \mathbf{Mat}_n(\mathbb{R})$ is **asymptotically nilpotent** if $\lim_{k\to\infty} A^k = 0$. By the spectral radius formula (Gelfand), this is equivalent to $\rho(A) < 1$, where $\rho(A) = \max_i |\lambda_i(A)|$ is the spectral radius. We denote $U := \{A \in \mathbf{Mat}_n(\mathbb{R}) : \rho(A) < 1\}$.

**Remark.** We interpret "asymptotically nilpotent" as $\rho(A) < 1$ (i.e., $A^k \to 0$), not as $\rho(A) = 0$ (classical nilpotency). The latter would make the word "asymptotically" redundant with "nilpotent."

---

## Case $n = 1$: Trivially Yes

All matrices are scalars, the Lie bracket is identically zero, so every subset is bracket-closed. The unique maximal subset of asymptotically nilpotent matrices is $(-1, 1)$, so $\mathcal{A} = \mathcal{B} = (-1,1)$ and $P = 1$ works.

---

## Case $n = 2$: Counterexample (two non-conjugate maximal sets)

We construct two maximal bracket-closed subsets $\mathcal{A}_1, \mathcal{A}_2 \subset U$ that are not conjugate.

### Construction of $\mathcal{A}_1$: upper-triangular small-diagonal set

Define
$$
\mathcal{A}_1 = \left\{ \begin{pmatrix} a & b \\ 0 & d \end{pmatrix} : |a| < 1,\; |d| < 1,\; b \in \mathbb{R} \right\}.
$$

**All elements are asymptotically nilpotent.** The eigenvalues of an upper-triangular matrix are its diagonal entries $a, d \in (-1,1)$, so $\rho < 1$. ✓

**Bracket-closed.** For $A = \begin{pmatrix} a & b \\ 0 & d \end{pmatrix}$, $A' = \begin{pmatrix} a' & b' \\ 0 & d' \end{pmatrix}$ in $\mathcal{A}_1$:
$$
[A, A'] = \begin{pmatrix} 0 & (a-d)b' - (a'-d')b \\ 0 & 0 \end{pmatrix},
$$
which is strictly upper-triangular (diagonal entries $0 \in (-1,1)$), hence in $\mathcal{A}_1$. ✓

**Maximality.** Suppose $\mathcal{A}_1 \cup \{M\}$ is bracket-closed and contained in $U$, with $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \notin \mathcal{A}_1$. Then either $c \neq 0$, or $c = 0$ but $|a| \geq 1$ or $|d| \geq 1$.

- If $|a| \geq 1$ or $|d| \geq 1$: $M \notin U$, contradiction.
- If $c \neq 0$: For every $t \in \mathbb{R}$, the matrix $t E_{12} = \begin{pmatrix} 0 & t \\ 0 & 0 \end{pmatrix}$ is nilpotent ($\rho = 0 < 1$), so $t E_{12} \in \mathcal{A}_1$. Bracket-closedness requires $[M, tE_{12}] \in U$. Compute:
$$
[M, tE_{12}] = t \begin{pmatrix} -c & a - d \\ 0 & c \end{pmatrix},
$$
which is upper-triangular with eigenvalues $-tc$ and $tc$. Its spectral radius is $|t| \cdot |c|$. For $|t| > 1/|c|$, this exceeds $1$, so $[M, tE_{12}] \notin U$. Contradiction. ✓

Therefore $\mathcal{A}_1$ is maximal.

**Span.** $\operatorname{span}(\mathcal{A}_1)$ is the Borel subalgebra (all upper-triangular $2 \times 2$ matrices), which has dimension $3$.

### Construction of $\mathcal{A}_2$: Zorn maximal extension of a small ball

Let $c \leq 1/2$ and define the open operator-norm ball
$$
B_c^{\mathrm{op}} = \{ A \in \mathbf{Mat}_2(\mathbb{R}) : \|A\|_{\mathrm{op}} < c \}.
$$

**Contained in $U$.** $\rho(A) \leq \|A\|_{\mathrm{op}} < c \leq 1/2 < 1$. ✓

**Bracket-closed.** $\|[A, B]\|_{\mathrm{op}} \leq 2\|A\|_{\mathrm{op}}\|B\|_{\mathrm{op}} < 2c^2 \leq c$ (using $c \leq 1/2$), so $[A, B] \in B_c^{\mathrm{op}}$. ✓

**Span.** $B_c^{\mathrm{op}}$ is an open ball centered at the origin, containing matrices in every direction, so $\operatorname{span}(B_c^{\mathrm{op}}) = \mathbf{Mat}_2(\mathbb{R}) = \mathfrak{gl}_2$, dimension $4$.

**Maximal extension exists.** Consider the poset of bracket-closed subsets of $U$ that contain $B_c^{\mathrm{op}}$, ordered by inclusion. For any chain $\{S_\alpha\}$, the union $S = \bigcup_\alpha S_\alpha$ is bracket-closed (if $A, B \in S$, then $A \in S_\alpha$, $B \in S_\beta$ for some $\alpha, \beta$; one contains the other, so both in some $S_\gamma$, hence $[A,B] \in S_\gamma \subseteq S$) and contained in $U$. By Zorn's lemma, there exists a maximal element $\mathcal{A}_2$.

Since $\mathcal{A}_2 \supseteq B_c^{\mathrm{op}}$, we have $\operatorname{span}(\mathcal{A}_2) \supseteq \operatorname{span}(B_c^{\mathrm{op}}) = \mathfrak{gl}_2$, so $\operatorname{span}(\mathcal{A}_2) = \mathfrak{gl}_2$, dimension $4$.

### Non-conjugacy

Suppose for contradiction that $P \mathcal{A}_1 P^{-1} = \mathcal{A}_2$ for some $P \in \mathrm{GL}_2(\mathbb{R})$. Conjugation by $P$ is a linear map, so it maps $\operatorname{span}(\mathcal{A}_1)$ to $\operatorname{span}(\mathcal{A}_2)$:
$$
P \operatorname{span}(\mathcal{A}_1) P^{-1} = \operatorname{span}(\mathcal{A}_2).
$$
The left side has dimension $\dim \operatorname{span}(\mathcal{A}_1) = 3$ (Borel subalgebra), while the right side has dimension $\dim \operatorname{span}(\mathcal{A}_2) = 4$ ($\mathfrak{gl}_2$). Conjugation preserves dimension, so $3 = 4$, a contradiction.

Therefore no such $P$ exists.

---

## Conclusion

- For $n = 1$: Yes, trivially.
- For $n = 2$: No — the maximal bracket-closed sets $\mathcal{A}_1$ (upper-triangular, spanning a 3-dimensional Borel subalgebra) and $\mathcal{A}_2$ (Zorn extension of a small ball, spanning the 4-dimensional $\mathfrak{gl}_2$) are not conjugate.
- For $n \geq 2$: No. The $n = 2$ counterexample already refutes the universal statement. (One can also embed the $2 \times 2$ construction into larger matrices via block-diagonal extension with zero blocks, yielding non-conjugate maximal sets for any $n \geq 2$.)

$$\boxed{\text{No}}$$

### PROOF COMPLETE
