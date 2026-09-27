# Proof: Every open affine subscheme of an algebraic $k$-variety is an affine $k$-variety

## Answer

$\boxed{\text{Yes}}$

## Theorem

Let $X$ be an algebraic $k$-variety (a separated scheme of finite type over a field $k$). If $U = \operatorname{Spec} B$ is an affine open subscheme of $X$, then $B$ is a finitely generated $k$-algebra. Consequently, $U$ is itself an affine $k$-variety.

## Proof

The proof proceeds in two stages: (1) an algebraic lemma that constitutes the core argument, and (2) a geometric reduction from the general case to the algebraic lemma.

### Stage 1: Algebraic Lemma

**Lemma.** Let $k$ be a field, $B$ a $k$-algebra, and $h_1, \ldots, h_n \in B$ elements that generate the unit ideal. Suppose each localization $B_{h_i}$ is a finitely generated $k$-algebra. Then $B$ is a finitely generated $k$-algebra.

**Proof of Lemma.**

**Step 1: Construct a finitely generated subalgebra $B' \subseteq B$ with $(B')_{h_i} = B_{h_i}$.**

Since $1/h_i \in B_{h_i}$ and $B_{h_i}$ is the localization of $B$ at $h_i$, there exist $b_i \in B$ and $m_i \geq 0$ such that
$$
h_i^{m_i+1} b_i = h_i^{m_i} \quad \text{in } B,
$$
so that $b_i$ maps to $1/h_i$ under $B \to B_{h_i}$.

Since each $B_{h_i}$ is finitely generated over $k$, write
$$
B_{h_i} = k\!\left[\frac{\alpha_{i1}}{h_i^{e_{i1}}}, \ldots, \frac{\alpha_{is_i}}{h_i^{e_{is_i}}}\right]
$$
with $\alpha_{ij} \in B$ and $e_{ij} \geq 0$.

Define
$$
B' = k\big[\, b_1, \ldots, b_n,\; \alpha_{ij} \text{ for all } i, j \,\big] \subseteq B.
$$
This is a finitely generated $k$-algebra (finitely many generators). Since $k$ is a field (hence noetherian), $B'$ is a **noetherian ring**.

We claim $(B')_{h_i} = B_{h_i}$ for every $i$. The inclusion $(B')_{h_i} \subseteq B_{h_i}$ is clear since $B' \subseteq B$. For the reverse inclusion: $b_i \in B'$ and $h_i \cdot b_i = 1$ in $(B')_{h_i}$ (because $h_i^{m_i+1} b_i = h_i^{m_i}$ implies $h_i b_i = 1$ after inverting $h_i$), so $1/h_i \in (B')_{h_i}$. Then each generator $\alpha_{ij}/h_i^{e_{ij}} = \alpha_{ij} \cdot (1/h_i)^{e_{ij}} = \alpha_{ij} \cdot b_i^{e_{ij}}$ lies in $(B')_{h_i}$ (since $\alpha_{ij} \in B'$). Hence $B_{h_i} \subseteq (B')_{h_i}$, proving the claim. $\checkmark$

**Step 2: Show that $h_1, \ldots, h_n$ generate the unit ideal in $B'$.**

Let $I = (h_1, \ldots, h_n) B'$. We prove $I = B'$.

Since $B'$ is noetherian, the descending chain $I \supseteq I^2 \supseteq I^3 \supseteq \cdots$ stabilizes: there exists $N \geq 1$ with $I^N = I^{N+1}$. Set $J = I^N$. Then $J = I \cdot J$ and $J$ is a finitely generated $B'$-module (since $B'$ is noetherian).

By the **determinant trick** (a consequence of the Cayley–Hamilton theorem): since $J = IJ$ and $J$ is finitely generated, there exists $\epsilon \in I$ such that
$$
(1 - \epsilon)\, J = 0.
$$

Now $\epsilon \in I$ implies $\epsilon^N \in I^N = J$. From $(1-\epsilon)J = 0$ we get $(1-\epsilon)\epsilon^N = 0$, i.e., $\epsilon^N = \epsilon^{N+1}$. Set $e = \epsilon^N$. Then:
- $e^2 = \epsilon^{2N} = \epsilon^N = e$ (since $\epsilon^N = \epsilon^{N+k}$ for all $k \geq 0$), so **$e$ is idempotent**.
- $e = \epsilon^N \in I^N \subseteq I$.
- $(1-e)J = (1 - \epsilon^N)J = (1-\epsilon)(1 + \epsilon + \cdots + \epsilon^{N-1})J = 0$.

**Key step: $e = 1$ in $B'$.** We use the inclusion $B' \hookrightarrow B$ (which is injective by construction) and the fact that $h_1, \ldots, h_n$ generate the unit ideal in $B$.

In the localization $(B')_{h_i} = B_{h_i}$, the element $h_i$ is a unit. Since $e \in I = (h_1, \ldots, h_n)B'$, the image of $e$ in $(B')_{h_i}$ lies in $I \cdot (B')_{h_i} = (B')_{h_i}$ (because $h_i$ is a unit, so $I$ generates the unit ideal in $(B')_{h_i}$). Thus $e$ maps to an idempotent that is also a unit in $(B')_{h_i}$, forcing $e = 1$ in $(B')_{h_i}$.

Since $(B')_{h_i} = B_{h_i}$, the image of $e$ in $B_{h_i}$ is $1$ for every $i$. Now, because $h_1, \ldots, h_n$ generate the unit ideal in $B$, the canonical map
$$
B \longrightarrow \prod_{i=1}^n B_{h_i}
$$
is **injective** (this is the standard fact that the localizations at a set of elements generating the unit ideal are jointly faithful). Since $e$ maps to $1$ in each $B_{h_i}$, we conclude $e = 1$ in $B$.

Finally, since $B' \hookrightarrow B$ is injective and $e$ maps to $1 \in B$, we conclude $e = 1$ in $B'$.

Since $e \in I$ and $e = 1$, we have $I = B'$. $\checkmark$

**Step 3: Conclude $B = B'$.**

Since $I = B'$, the elements $h_1, \ldots, h_n$ generate the unit ideal in $B'$. For any $b \in B$, since $b \in B_{h_i} = (B')_{h_i}$, there exists an integer $m \geq 0$ (chosen uniformly over all $i$) such that $h_i^m \, b \in B'$ for every $i$.

Since $h_1, \ldots, h_n$ generate the unit ideal in $B'$, so do $h_1^m, \ldots, h_n^m$ (indeed, if $1 = \sum h_i a_i$ then $1 = (\sum h_i a_i)^{(n-1)m+1}$, and each term contains some $h_i^m$ as a factor, so $1 \in (h_1^m, \ldots, h_n^m)$). Write
$$
1 = \sum_{i=1}^n h_i^m \, a_i, \qquad a_i \in B'.
$$
Then
$$
b = \sum_{i=1}^n a_i \, (h_i^m \, b) \in B',
$$
since $a_i \in B'$ and $h_i^m b \in B'$. This shows $B \subseteq B'$, hence $B = B'$.

Since $B'$ is finitely generated over $k$, so is $B$. $\square$

### Stage 2: Geometric Reduction

Let $X$ be an algebraic $k$-variety (separated, finite type over $k$) and $U = \operatorname{Spec} B$ an affine open subscheme.

**Step 1: Cover $U$ by principal opens of affine charts of $X$.**

Since $X$ is of finite type over $k$, it is noetherian; hence every open subset of $X$ is quasi-compact. Cover $X$ by finitely many affine opens $V_1, \ldots, V_m$ with $V_j = \operatorname{Spec} A_j$, where each $A_j$ is a finitely generated $k$-algebra.

Then $U = \bigcup_{j=1}^m (U \cap V_j)$. Each $U \cap V_j$ is an open subset of $V_j = \operatorname{Spec} A_j$ and is quasi-compact (being open in the noetherian space $X$). Hence
$$
U \cap V_j = \bigcup_{a} D(f_{ja}), \qquad f_{ja} \in A_j,
$$
a finite union of principal opens. Each $D(f_{ja}) = \operatorname{Spec} (A_j)_{f_{ja}}$ is the spectrum of a finitely generated $k$-algebra (localization of a f.g. $k$-algebra).

**Step 2: Refine to principal opens of $U = \operatorname{Spec} B$.**

Each $D(f_{ja})$ is an open subscheme of $U = \operatorname{Spec} B$ and is quasi-compact (open in the noetherian space $X$). Hence
$$
D(f_{ja}) = \bigcup_{l} D(h_{jal}), \qquad h_{jal} \in B,
$$
a finite union of principal opens of $\operatorname{Spec} B$.

Since $D(h_{jal}) \subseteq D(f_{ja}) = \operatorname{Spec}(A_j)_{f_{ja}}$, the open $D(h_{jal})$ is the principal open of $\operatorname{Spec}(A_j)_{f_{ja}}$ cut out by the restriction $\bar{h}_{jal} \in (A_j)_{f_{ja}}$. Therefore
$$
B_{h_{jal}} = \big((A_j)_{f_{ja}}\big)_{\bar{h}_{jal}},
$$
which is a localization of the finitely generated $k$-algebra $(A_j)_{f_{ja}}$, hence itself a finitely generated $k$-algebra.

**Step 3: Apply the Algebraic Lemma.**

Collecting all the $h_{jal}$ as $h_1, \ldots, h_n \in B$, we have:
- $U = \bigcup_{i=1}^n D(h_i)$, so $h_1, \ldots, h_n$ generate the unit ideal in $B$.
- Each $B_{h_i}$ is a finitely generated $k$-algebra.

By the Algebraic Lemma (Stage 1), $B$ is a finitely generated $k$-algebra. $\square$

### Conclusion

The affine open subscheme $U = \operatorname{Spec} B$ has $B$ finitely generated over $k$, so $U$ is the spectrum of a finitely generated $k$-algebra — that is, $U$ is an affine $k$-variety.

$$
\boxed{\text{Yes, every open affine subscheme of an algebraic } k\text{-variety is an affine } k\text{-variety.}}
$$

### PROOF COMPLETE
