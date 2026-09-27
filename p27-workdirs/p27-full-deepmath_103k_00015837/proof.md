# Problem

Consider algebraically independent irreducible homogeneous polynomials $P_1, P_2, \ldots, P_k$ in $n$ variables over the complex numbers. If the variety defined by the ideal $I=(P_1, \ldots, P_k)$ is reducible, determine whether there exists a point $b = (b_1, b_2, \ldots, b_n)$ such that $P_i(b) = 0$ for all $i \in [k]$ and the rank of the Jacobian matrix of $P_1, P_2, \ldots, P_k$ at $b$ is $k$. Provide a justification for your answer.

## Answer

$$\boxed{\text{No, such a point need not exist.}}$$

The answer is **not necessarily**: there exist choices of $P_1, \ldots, P_k$ satisfying all the hypotheses for which the Jacobian of $(P_1, \ldots, P_k)$ has rank strictly less than $k$ at *every* point of $V(I)$. We prove this by an explicit counterexample.

## Counterexample

Take $n = 3$, $k = 2$, and work in $R = \mathbb{C}[x, y, z]$. Set

$$P_1 = x^2 + yz, \qquad P_2 = x^2 + 2yz.$$

### Step 1. The $P_i$ are homogeneous and irreducible

Both $P_1$ and $P_2$ are homogeneous of degree $2$.

A quadratic form over $\mathbb{C}$ in $m$ variables is reducible (factors into two linear forms) if and only if its associated symmetric matrix has rank $\leq 2$ when $m \geq 3$; equivalently, a quadratic form in $3$ variables is reducible iff its matrix has rank $\leq 2$.

The symmetric matrix of $P_1 = x^2 + yz$ is

$$M_1 = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & \tfrac{1}{2} \\ 0 & \tfrac{1}{2} & 0 \end{pmatrix}, \qquad \det(M_1) = -\tfrac{1}{4} \neq 0,$$

so $P_1$ has rank $3$ and is irreducible over $\mathbb{C}$.

The symmetric matrix of $P_2 = x^2 + 2yz$ is

$$M_2 = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix}, \qquad \det(M_2) = -1 \neq 0,$$

so $P_2$ has rank $3$ and is irreducible over $\mathbb{C}$.

(One may also verify directly: if $x^2 + yz = (ax + by + cz)(dx + ey + fz)$, comparing coefficients forces $ad = 1$, $be = cf = 0$, $af + cd = 0$, $ae + bd = 0$, $bf + ce = 1$. From $ad = 1$ both $a, d \neq 0$, so $f = c = 0$ from the cross terms, but then $bf + ce = 0 \neq 1$, a contradiction.)

### Step 2. The $P_i$ are algebraically independent

Observe

$$P_2 - P_1 = yz, \qquad P_1 - (P_2 - P_1) = 2x^2 - P_2 + P_1 \;\Longrightarrow\; x^2 = P_1 - yz = P_1 - (P_2 - P_1) = 2P_1 - P_2.$$

So $\{P_1, P_2\}$ and $\{x^2, yz\}$ are related by an invertible linear change:

$$\begin{pmatrix} P_1 \\ P_2 \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix} \begin{pmatrix} x^2 \\ yz \end{pmatrix}, \qquad \det\begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix} = 1 \neq 0.$$

Algebraic independence is preserved by invertible linear combinations, so it suffices to check that $x^2$ and $yz$ are algebraically independent. Suppose $F \in \mathbb{C}[T_1, T_2]$ satisfies $F(x^2, yz) = 0$ in $\mathbb{C}[x,y,z]$. Write $F = \sum_{i,j} c_{ij} T_1^i T_2^j$. Then

$$\sum_{i,j} c_{ij}\, x^{2i}\, y^j z^j = 0 \quad \text{in } \mathbb{C}[x,y,z].$$

The monomials $x^{2i} y^j z^j$ are pairwise distinct (distinct triples $(2i, j, j)$ of exponents), hence linearly independent over $\mathbb{C}$. Therefore every $c_{ij} = 0$, i.e. $F = 0$. So $x^2, yz$ are algebraically independent, and hence $P_1, P_2$ are algebraically independent.

### Step 3. The variety $V(I)$ is reducible

From $P_2 - P_1 = yz \in I$ and $2P_1 - P_2 = x^2 \in I$, we get

$$I = (P_1, P_2) = (x^2, yz).$$

Therefore

$$V(I) = V(x^2, yz) = V(x, yz) = V(x, y) \cup V(x, z),$$

the union of the two coordinate lines $\{(0, 0, t) : t \in \mathbb{C}\}$ and $\{(0, t, 0) : t \in \mathbb{C}\}$. This is reducible. ✓

(For completeness: the minimal primes of $I = (x^2, yz)$ are $(x, y)$ and $(x, z)$, both of height $2 = k$, so $\operatorname{ht}(I) = k$ and $R/I$ is Cohen–Macaulay, equidimensional, with no embedded primes. This is consistent with the hypotheses but does not prevent the phenomenon below.)

### Step 4. The Jacobian has rank $< k$ at every point of $V(I)$

The Jacobian matrix of $(P_1, P_2)$ with respect to $(x, y, z)$ is

$$J = \begin{pmatrix} \partial_x P_1 & \partial_y P_1 & \partial_z P_1 \\ \partial_x P_2 & \partial_y P_2 & \partial_z P_2 \end{pmatrix} = \begin{pmatrix} 2x & z & y \\ 2x & z & 2y \end{pmatrix}.$$

We evaluate $J$ on each irreducible component of $V(I)$:

- **On $V(x, y) = \{(0, 0, t)\}$**: here $x = 0$, $y = 0$, so

$$J\big|_{V(x,y)} = \begin{pmatrix} 0 & t & 0 \\ 0 & t & 0 \end{pmatrix},$$

which has rank $\leq 1 < 2 = k$ (rank $1$ when $t \neq 0$, rank $0$ when $t = 0$).

- **On $V(x, z) = \{(0, t, 0)\}$**: here $x = 0$, $z = 0$, so

$$J\big|_{V(x,z)} = \begin{pmatrix} 0 & 0 & t \\ 0 & 0 & 2t \end{pmatrix},$$

which has rank $\leq 1 < 2 = k$ (rank $1$ when $t \neq 0$, rank $0$ when $t = 0$).

- **At the origin** $(0,0,0)$ (the intersection of the two components): $J = 0$, rank $0$.

Since $V(I) = V(x,y) \cup V(x,z)$, we have exhausted all points of $V(I)$. **At every point $b \in V(I)$, the Jacobian has rank $\leq 1 < 2 = k$.** Hence no point $b \in V(I)$ exists at which the Jacobian has rank $k$.

## Why this happens (mechanism)

The Jacobian criterion tests *scheme-theoretic* smoothness of $\operatorname{Spec}(R/I)$, using the generators of $I$ itself (not of $\sqrt{I}$). Here

$$I = (x^2, yz), \qquad \sqrt{I} = (x, yz) = (x, y) \cap (x, z), \qquad I \subsetneq \sqrt{I},$$

so $I$ is **not radical**. The underlying reduced variety $V(\sqrt{I}) = V(x,y) \cup V(x,z)$ is geometrically smooth away from the origin (each component is a line), but the scheme $\operatorname{Spec}(R/I)$ carries the non-reduced structure $x^2 = 0$, which makes every point singular scheme-theoretically.

Concretely, at the smooth geometric point $b = (0, 0, 1) \in V(x, y)$:

$$\left(R/I\right)_{\mathfrak{m}_b} = \mathbb{C}[x,y,z]_{(x,y,z-1)}/(x^2, yz) \cong \mathbb{C}[x, y]_{(x,y)}/(x^2, y) \cong \mathbb{C}[x]_{(x)}/(x^2),$$

which has Krull dimension $0$ but embedding dimension $1$ (the cotangent space is spanned by $x$), so it is **not a regular local ring**. The Jacobian rank $n - \dim - \text{emb. dim. correction}$ detects exactly this: rank $1 < 2 = k$ reflects the embedded tangent direction coming from $x^2 = 0$.

## Contrast: the point can exist in other examples

To confirm the answer is "not necessarily" rather than "never", consider $P_1 = x$, $P_2 = x^2 + y^2 + z^2$ in $\mathbb{C}[x,y,z]$. These are algebraically independent, irreducible, and homogeneous; $V(I) = V(x, y^2 + z^2) = V(x, y + iz) \cup V(x, y - iz)$ is reducible. At $b = (0, 1, i) \in V(x, y + iz)$:

$$J(b) = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 2 & 2i \end{pmatrix}, \qquad \operatorname{rank} = 2 = k.$$

Here $I = (x, y^2 + z^2) = (x, (y+iz)(y-iz))$ is again non-radical, but $P_1 = x$ is linear and cuts out a radical piece, leaving a Jacobian that is full rank at the smooth points of each component. The difference is that in the counterexample *both* generators contribute non-reduced structure ($x^2$ and $yz$), so no point escapes the singularity.

## Conclusion

The counterexample $P_1 = x^2 + yz,\; P_2 = x^2 + 2yz \in \mathbb{C}[x, y, z]$ satisfies all hypotheses (algebraically independent, irreducible, homogeneous, $V(I)$ reducible), yet the Jacobian of $(P_1, P_2)$ has rank $\leq 1 < 2 = k$ at **every** point of $V(I)$. Therefore such a point $b$ **need not exist**.

$$\boxed{\text{No. Such a point } b \text{ does not necessarily exist.}}$$

### PROOF COMPLETE
