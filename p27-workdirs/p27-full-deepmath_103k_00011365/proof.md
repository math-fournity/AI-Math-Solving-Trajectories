# Proof: Is every simply-connected nilpotent Lie group algebraic?

**Answer: Yes.**

## Proof

Let $N$ be a simply-connected nilpotent Lie group with Lie algebra $\mathfrak{n}$ of dimension $d$ and nilpotency class $c$.

### Step 1: The exponential map is a global diffeomorphism

Since $N$ is simply-connected and nilpotent, the exponential map
$$\exp : \mathfrak{n} \longrightarrow N$$
is a global diffeomorphism (this is a standard theorem for simply-connected nilpotent Lie groups). We use $\exp$ to identify $N$ with $\mathfrak{n} \cong \mathbb{R}^d$ as smooth manifolds.

### Step 2: The group law is polynomial (Baker–Campbell–Hausdorff)

Under this identification, the group multiplication on $N$ is given by the Baker–Campbell–Hausdorff formula:
$$X \cdot Y = \mathrm{BCH}(X, Y) = X + Y + \frac{1}{2}[X, Y] + \frac{1}{12}[X, [X, Y]] - \frac{1}{12}[Y, [Y, X]] + \cdots$$

Since $\mathfrak{n}$ is nilpotent of class $c$, every iterated commutator of length $> c$ vanishes. Therefore the BCH series **terminates after finitely many terms**. Each term is a polynomial function of $X$ and $Y$ (with coefficients that are universal rational numbers times the structure constants of $\mathfrak{n}$). Hence the multiplication map
$$\mu : \mathbb{R}^d \times \mathbb{R}^d \longrightarrow \mathbb{R}^d, \quad (X, Y) \mapsto X \cdot Y$$
is a **polynomial map**.

Similarly, the inversion map $X \mapsto X^{-1}$ is given by a terminating series (obtained from $\mathrm{BCH}(X, -X)$), and is therefore also polynomial.

### Step 3: $N$ is an affine algebraic group over $\mathbb{R}$

The triple $(\mathbb{R}^d, \mu, \iota)$ where $\mu$ is polynomial multiplication and $\iota$ is polynomial inversion defines an **affine algebraic group over $\mathbb{R}$**. The underlying algebraic variety is the affine space $\mathbb{A}^d_{\mathbb{R}}$, and the group operations are morphisms of algebraic varieties.

Concretely, $N$ is a **unipotent** algebraic group: the group law has the form $X \cdot Y = X + Y + (\text{terms of degree} \geq 2)$, so the group is built from nilpotent operations. The adjoint action of $N$ on $\mathfrak{n}$ is by nilpotent endomorphisms (since $\mathrm{ad}(X)$ is nilpotent for every $X \in \mathfrak{n}$), confirming unipotence.

### Step 4: Realization as a closed subgroup of $\mathrm{GL}_m$

By a theorem of Chevalley, every affine algebraic group over $\mathbb{R}$ is isomorphic to a closed (Zariski-closed) subgroup of $\mathrm{GL}_m$ for some $m$. Alternatively, by the Ado–Iwasawa theorem, the nilpotent Lie algebra $\mathfrak{n}$ admits a faithful representation $\rho : \mathfrak{n} \to \mathfrak{gl}_m(\mathbb{R})$ by nilpotent endomorphisms. The induced group homomorphism
$$\Phi : N \longrightarrow \mathrm{GL}_m(\mathbb{R}), \quad \Phi(\exp(X)) = \exp(\rho(X))$$
is faithful, and its image consists of unipotent matrices. The image $\Phi(N)$ is a connected, simply-connected unipotent subgroup of $\mathrm{GL}_m(\mathbb{R})$.

Let $H = \overline{\Phi(N)}^{\mathrm{Zar}}$ be the Zariski closure of $\Phi(N)$ in $\mathrm{GL}_m$. Then $H$ is a connected unipotent algebraic $\mathbb{R}$-subgroup of $\mathrm{GL}_m$. Since unipotent groups over $\mathbb{R}$ are isomorphic to affine space, $H(\mathbb{R})$ is connected and simply-connected. Now:
- $\Phi(N) \subseteq H(\mathbb{R})$ (both are the $\mathbb{R}$-points containing the image),
- $\mathrm{Lie}(H) = \mathrm{Lie}(\Phi(N)) = \rho(\mathfrak{n})$ (the Zariski closure of a connected unipotent subgroup has the same Lie algebra),
- Both $\Phi(N)$ and $H(\mathbb{R})$ are connected Lie groups of the same dimension.

Therefore $\Phi(N)$ is an open subgroup of $H(\mathbb{R})$. Since $H(\mathbb{R})$ is connected, $\Phi(N) = H(\mathbb{R})$.

### Conclusion

We have shown $N \cong H(\mathbb{R})$ where $H$ is a unipotent algebraic group defined over $\mathbb{R}$. Therefore $N$ is algebraic.

$$\boxed{\text{Yes}}$$

## Remark on the Malcev lattice theorem

The Malcev lattice theorem states that a simply-connected nilpotent Lie group $N$ admits a **lattice** (discrete cocompact subgroup) if and only if its Lie algebra $\mathfrak{n}$ admits a $\mathbb{Q}$-structure (a basis with rational structure constants). This is a statement about **arithmetic** properties (definability over $\mathbb{Q}$), not about algebraicity over $\mathbb{R}$.

The existence of a $\mathbb{Q}$-structure is a strictly stronger condition than algebraicity over $\mathbb{R}$:
- **Algebraic over $\mathbb{R}$**: always true for simply-connected nilpotent Lie groups (by the BCH argument above).
- **Defined over $\mathbb{Q}$** (equivalently, admits a lattice): true if and only if $\mathfrak{n}$ has a $\mathbb{Q}$-structure.

Not every simply-connected nilpotent Lie group admits a lattice (there exist nilpotent Lie algebras without $\mathbb{Q}$-structure, as can be shown by a counting argument: algebras with $\mathbb{Q}$-structure form a countable set, while real nilpotent Lie algebras form an uncountable set in sufficiently high dimension). But every simply-connected nilpotent Lie group is nonetheless algebraic over $\mathbb{R}$.

The key distinction is that the BCH formula has **rational** universal coefficients, so even when the structure constants of $\mathfrak{n}$ are irrational, the resulting group law is still polynomial over $\mathbb{R}$ — it is an algebraic group over $\mathbb{R}$, just not necessarily defined over $\mathbb{Q}$.
