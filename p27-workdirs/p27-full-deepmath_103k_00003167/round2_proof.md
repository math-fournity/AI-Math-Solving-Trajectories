# The natural map $A \circledast_C B \to A *_C B$ is not always injective

**Answer:** $\boxed{No}$ — the natural map from the purely algebraic pushout (algebraic amalgamated free product) to the C*-algebraic amalgamated free product is **not** injective in general. We give an explicit counterexample with unital C*-algebras and unital (even injective) *-homomorphisms.

---

## Setup

Let

- $C = \mathbb{C}^2$ (the C*-algebra of pairs $(\lambda,\mu)$ with pointwise operations),
- $A = M_2(\mathbb{C})$, $B = M_2(\mathbb{C})$,

and define unital *-homomorphisms

$$
\phi : C \longrightarrow A, \qquad \phi(\lambda,\mu) = \begin{pmatrix} \lambda & 0 \\ 0 & \mu \end{pmatrix},
$$

$$
\psi : C \longrightarrow B, \qquad \psi(\lambda,\mu) = \begin{pmatrix} \mu & 0 \\ 0 & \lambda \end{pmatrix}.
$$

Both $\phi$ and $\psi$ are unital and injective. Note the **swap**: $\phi$ sends $(1,0)\mapsto e_{11}^A$ while $\psi$ sends $(1,0)\mapsto e_{22}^B$.

Let $A \circledast_C B$ denote the algebraic amalgamated free product (pushout in the category of unital *-algebras) and $A *_C B$ the C*-algebraic amalgamated free product (pushout in the category of unital C*-algebras, obtained by completing $A \circledast_C B$ with respect to the maximal C*-seminorm and quotienting its kernel).

The **natural map** is

$$
\pi : A \circledast_C B \longrightarrow A *_C B, \qquad x \longmapsto \text{image of } x \text{ in the C*-completion}.
$$

Its kernel is $\{x \in A \circledast_C B : \|x\|_{\max} = 0\}$, where $\|x\|_{\max} = \sup_{\rho} \|\rho(x)\|$ over all *-representations $\rho$ of $A \circledast_C B$.

---

## The counterexample element

Denote by $e_{ij}^A$ and $e_{ij}^B$ the standard matrix units in $A$ and $B$ respectively. In the pushout, the amalgamation relations give:

$$
e_{11}^A = \phi(1,0) = \psi(1,0) = e_{22}^B, \qquad e_{22}^A = \phi(0,1) = \psi(0,1) = e_{11}^B.
$$

Set $p := e_{11}^A = e_{22}^B$ (a projection in the pushout) and $q := 1 - p = e_{22}^A = e_{11}^B$.

**Define**

$$
y := e_{12}^A \cdot e_{21}^B \;\in\; A \circledast_C B.
$$

### $y$ is nonzero in $A \circledast_C B$

The image $\phi(C) \subset A$ is the diagonal subalgebra of $M_2(\mathbb{C})$, and likewise $\psi(C) \subset B$ is the diagonal subalgebra. The element $e_{12}^A = \begin{pmatrix}0&1\\0&0\end{pmatrix}$ is off-diagonal, hence $e_{12}^A \notin \phi(C)$; similarly $e_{21}^B \notin \psi(C)$. Therefore $y = e_{12}^A \cdot e_{21}^B$ is a **reduced word** of length 2 in the algebraic amalgamated free product, and reduced words are linearly independent. Hence

$$
y \neq 0 \quad \text{in } A \circledast_C B.
$$

---

## Computation: $yy^* = 0$ and $y^*y = 0$ in $A \circledast_C B$

### Compute $yy^*$

$$
yy^* = e_{12}^A \cdot e_{21}^B \cdot (e_{21}^B)^* \cdot (e_{12}^A)^* = e_{12}^A \cdot e_{21}^B \cdot e_{12}^B \cdot e_{21}^A.
$$

The middle product $e_{21}^B \cdot e_{12}^B$ is a product **within** $B$:

$$
e_{21}^B \cdot e_{12}^B = e_{22}^B = p.
$$

So

$$
yy^* = e_{12}^A \cdot p \cdot e_{21}^A.
$$

Now use the $A$-structure: $p = e_{11}^A$, and

$$
e_{12}^A \cdot e_{11}^A = 0 \qquad \text{(matrix multiplication: } e_{12}\,e_{11} = 0\text{)}.
$$

Therefore

$$
yy^* = 0 \cdot e_{21}^A = 0.
$$

### Compute $y^*y$

$$
y^*y = e_{12}^B \cdot e_{21}^A \cdot e_{12}^A \cdot e_{21}^B.
$$

The middle product $e_{21}^A \cdot e_{12}^A$ is a product **within** $A$:

$$
e_{21}^A \cdot e_{12}^A = e_{22}^A = q = 1 - p.
$$

So

$$
y^*y = e_{12}^B \cdot (1-p) \cdot e_{21}^B.
$$

Now use the $B$-structure: $1 - p = q = e_{11}^B$, and

$$
e_{12}^B \cdot e_{11}^B = 0 \qquad \text{(matrix multiplication: } e_{12}\,e_{11} = 0\text{)}.
$$

Therefore

$$
y^*y = 0.
$$

---

## $y$ lies in the kernel of the natural map

Let $\rho : A \circledast_C B \to \mathcal{B}(H)$ be any *-representation. From $yy^* = 0$ we get

$$
\rho(y)\,\rho(y)^* = \rho(yy^*) = 0,
$$

which forces $\rho(y) = 0$ (since $\|\rho(y)\|^2 = \|\rho(y)\rho(y)^*\| = 0$ in the C*-algebra $\mathcal{B}(H)$).

Since $\rho(y) = 0$ for **every** *-representation $\rho$,

$$
\|y\|_{\max} = \sup_{\rho} \|\rho(y)\| = 0.
$$

Hence $y \in \ker(\pi)$, i.e., $y$ maps to $0$ in $A *_C B$.

---

## Conclusion

We have exhibited:

- unital C*-algebras $A = B = M_2(\mathbb{C})$, $C = \mathbb{C}^2$,
- unital injective *-homomorphisms $\phi : C \to A$ and $\psi : C \to B$,
- an element $y = e_{12}^A \cdot e_{21}^B \in A \circledast_C B$ with $y \neq 0$ (it is a reduced word),

such that $yy^* = 0$ in $A \circledast_C B$, which forces $\rho(y) = 0$ for every *-representation $\rho$, hence $\|y\|_{\max} = 0$, hence $\pi(y) = 0$ in $A *_C B$.

Therefore the natural map

$$
\pi : A \circledast_C B \longrightarrow A *_C B
$$

is **not injective** in general.

$$
\boxed{No}
$$

---

### Remark on the mechanism

The failure of injectivity stems from the **swap** in the amalgamation: $\phi$ and $\psi$ send the same minimal projection of $C = \mathbb{C}^2$ to *complementary* projections in $A$ and $B$. This creates an algebraic element $y = e_{12}^A\, e_{21}^B$ that is a perfectly valid nonzero reduced word algebraically, but which satisfies $yy^* = 0$ — a relation that is algebraically consistent yet forces $y = 0$ in any C*-representation by the C*-identity $\|y\|^2 = \|yy^*\|$. The algebraic pushout has no way to "see" this positivity obstruction; it only manifests upon passage to the C*-completion.
