# Proof: Cancellation for Abelian Varieties over $\mathbb{C}$

## Statement

Let $A, B, C, D$ be abelian varieties over $\mathbb{C}$ such that $A \times B \cong C \times D$ and $A \cong C$. Then $B \cong D$.

## Proof

The proof rests on the **Krull–Schmidt theorem for abelian varieties**, which we first establish and then apply.

### Step 1: The category of abelian varieties over $\mathbb{C}$ satisfies Krull–Schmidt

We verify the three hypotheses of the Krull–Schmidt–Azumaya theorem for the category $\mathcal{AV}_{\mathbb{C}}$ of abelian varieties over $\mathbb{C}$ (with morphisms being homomorphisms of abelian varieties).

**(a) $\mathcal{AV}_{\mathbb{C}}$ is an additive category with finite direct products.**

The set $\operatorname{Hom}(X, Y)$ of homomorphisms between two abelian varieties is an abelian group under pointwise addition. The zero morphism serves as the zero element, and the product $X \times Y$ (with the product group structure) serves as both the categorical product and coproduct. Composition is bilinear. Hence $\mathcal{AV}_{\mathbb{C}}$ is additive.

**(b) Idempotents split.**

Let $e \in \operatorname{End}(X)$ be an idempotent, i.e., $e^2 = e$. Set
$$Y = \ker(1 - e), \qquad Z = \ker(e).$$
Both $Y$ and $Z$ are abelian subvarieties of $X$ (kernels of endomorphisms are closed algebraic subgroups, and over the algebraically closed field $\mathbb{C}$, the connected component of the identity is an abelian subvariety; since $1-e$ and $e$ are idempotent, their kernels are already connected).

The map
$$\varphi: Y \times Z \longrightarrow X, \qquad (y, z) \longmapsto y + z$$
is a homomorphism of abelian varieties. It is an isomorphism: the inverse is $x \mapsto (e(x),\, x - e(x))$, since $e(x) \in Y$ (because $(1-e)(e(x)) = e(x) - e^2(x) = 0$) and $x - e(x) \in Z$ (because $e(x - e(x)) = e(x) - e^2(x) = 0$). Under this isomorphism, $e$ corresponds to the projection $Y \times Z \to Y$. Thus every idempotent splits.

**(c) Endomorphism rings are semiperfect (in fact, finitely generated free $\mathbb{Z}$-modules).**

For any abelian variety $X$ over $\mathbb{C}$, the endomorphism ring $\operatorname{End}(X)$ is a **free $\mathbb{Z}$-module of finite rank**. This is a classical result: $\operatorname{End}(X)$ embeds into $\operatorname{End}_{\mathbb{Z}}(H_1(X, \mathbb{Z}))$, which is a free $\mathbb{Z}$-module of rank $2\dim X$, and $\operatorname{End}(X)$ is a discrete subgroup of the finite-dimensional real vector space $\operatorname{End}(H_1(X, \mathbb{Z})) \otimes \mathbb{R}$, hence a finitely generated free $\mathbb{Z}$-module.

Since $\operatorname{End}(X)$ is a finitely generated $\mathbb{Z}$-module, it is a semiperfect ring (every finitely generated module over $\mathbb{Z}$ has a projective cover; equivalently, $\operatorname{End}(X)$ is semilocal modulo its Jacobson radical). More directly: $\mathbb{Z}$ is a semiperfect ring, and any finitely generated $\mathbb{Z}$-algebra is semiperfect.

**Conclusion of Step 1.** By the Krull–Schmidt–Azumaya theorem (which applies to any additive category in which idempotents split and whose endomorphism rings are semiperfect), every abelian variety $X$ over $\mathbb{C}$ admits a decomposition
$$X \cong X_1 \times X_2 \times \cdots \times X_n$$
where each $X_i$ is **indecomposable** (i.e., $\operatorname{End}(X_i)$ has no nontrivial idempotents), and this decomposition is **unique up to isomorphism and reordering of the factors**.

### Step 2: Applying Krull–Schmidt to deduce $B \cong D$

Decompose each abelian variety into indecomposable factors:
$$A \cong \prod_{i=1}^{r} A_i, \quad B \cong \prod_{j=1}^{s} B_j, \quad C \cong \prod_{k=1}^{t} C_k, \quad D \cong \prod_{\ell=1}^{u} D_\ell,$$
where each $A_i, B_j, C_k, D_\ell$ is indecomposable.

From $A \times B \cong C \times D$, the Krull–Schmidt uniqueness theorem gives:
$$\{A_1, \ldots, A_r, B_1, \ldots, B_s\} \cong \{C_1, \ldots, C_t, D_1, \ldots, D_u\}$$
as **multisets** (i.e., up to isomorphism and reordering). In particular, $r + s = t + u$.

From $A \cong C$, the Krull–Schmidt uniqueness theorem gives:
$$\{A_1, \ldots, A_r\} \cong \{C_1, \ldots, C_t\}$$
as multisets, so $r = t$ and (after reindexing) $A_i \cong C_i$ for each $i$.

Now, removing the common multiset $\{A_1, \ldots, A_r\} = \{C_1, \ldots, C_t\}$ from both sides of the equality
$$\{A_1, \ldots, A_r\} \cup \{B_1, \ldots, B_s\} = \{C_1, \ldots, C_t\} \cup \{D_1, \ldots, D_u\},$$
we obtain
$$\{B_1, \ldots, B_s\} \cong \{D_1, \ldots, D_u\}$$
as multisets, so $s = u$ and (after reindexing) $B_j \cong D_j$ for each $j$.

Therefore
$$B \cong \prod_{j=1}^{s} B_j \cong \prod_{j=1}^{s} D_j \cong D. \qquad \blacksquare$$

## Summary

The key structural fact is that the category of abelian varieties over $\mathbb{C}$ satisfies the Krull–Schmidt theorem: every abelian variety decomposes uniquely (up to isomorphism and reordering) into a product of indecomposable abelian varieties. This follows because (1) the category is additive, (2) idempotents split (via kernels of idempotent endomorphisms), and (3) endomorphism rings are finitely generated free $\mathbb{Z}$-modules, hence semiperfect. Given Krull–Schmidt, the cancellation $A \times B \cong C \times D,\ A \cong C \implies B \cong D$ is immediate: the indecomposable factors of $A$ and $C$ coincide, so removing them from both sides of the factorization of $A \times B \cong C \times D$ leaves $B \cong D$.

$$\boxed{B \cong D}$$
