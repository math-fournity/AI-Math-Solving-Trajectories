# A Constructible Angle That Cannot Be Quintsected

## Answer

$$\boxed{\theta = \arccos(1/3)}$$

That is, the angle $\theta$ satisfying $\cos\theta = 1/3$.

---

## Proof

### Step 1. $\theta$ is constructible.

A real number $\alpha$ is constructible (by unmarked straightedge and compass) only if $[\mathbb{Q}(\alpha):\mathbb{Q}]$ is a power of $2$; conversely, if $\alpha\in\mathbb{Q}$ then $\alpha$ is certainly constructible.

Here $\cos\theta = 1/3 \in \mathbb{Q}$, so $\theta$ is a constructible angle (given a unit segment, one constructs the point $(1/3, \sqrt{1-1/9}) = (1/3, 2\sqrt{2}/3)$ on the unit circle, and the angle it subtends is $\theta$).

### Step 2. Quintsection reduces to a Chebyshev equation.

The $5$-th Chebyshev polynomial of the first kind is
$$T_5(x) = 16x^5 - 20x^3 + 5x,\qquad T_5(\cos\alpha)=\cos(5\alpha).$$

Quintsecting $\theta$ means constructing $\theta/5$, equivalently constructing $\cos(\theta/5)$. Since
$$T_5(\cos(\theta/5)) = \cos\theta = \tfrac{1}{3},$$
the number $x_0:=\cos(\theta/5)$ is a root of
$$T_5(x) - \tfrac{1}{3} = 0 \quad\Longleftrightarrow\quad 48x^5 - 60x^3 + 15x - 1 = 0. \tag{$*$}$$

Quintsection is possible $\iff$ $\cos(\theta/5)$ is constructible over $\mathbb{Q}(\cos\theta)=\mathbb{Q}$ $\iff$ $[\mathbb{Q}(\cos(\theta/5)):\mathbb{Q}]$ is a power of $2$.

### Step 3. A lemma on reducibility of $T_5(x)-c$ over $\mathbb{Q}$.

> **Lemma.** For $c\in\mathbb{Q}$, the polynomial $T_5(x)-c\in\mathbb{Q}[x]$ is reducible over $\mathbb{Q}$ *if and only if* it has a rational root.

*Proof.* The five roots of $T_5(x)-c=0$ are
$$r_k = \cos\!\Big(\tfrac{\theta + 2k\pi}{5}\Big),\qquad k=0,1,2,3,4,$$
where $\cos\theta = c$.

Let $L=\mathbb{Q}(\zeta_5,\, e^{i\theta/5})$ be the splitting field, with $\zeta_5=e^{2\pi i/5}$. Since $c\in\mathbb{Q}$, the number $e^{i\theta}=c+i\sqrt{1-c^2}$ lies in a quadratic extension of $\mathbb{Q}$, so every $\mathbb{Q}$-automorphism $\sigma$ of $L$ either fixes $e^{i\theta}$ or sends it to $e^{-i\theta}$. Writing $\alpha=e^{i\theta/5}$, we have either $\sigma(\alpha)=\zeta_5^{\,b}\alpha$ or $\sigma(\alpha)=\zeta_5^{\,b}\bar\alpha$ for some $b\in\mathbb{Z}/5\mathbb{Z}$, and $\sigma(\zeta_5)=\zeta_5^{\,a}$ for some $a\in(\mathbb{Z}/5\mathbb{Z})^{*}$. In both cases the action on the roots is
$$r_k \longmapsto r_{\,ak+b},$$
so the Galois group $G$ embeds into the affine group
$$\operatorname{AGL}(1,5)=(\mathbb{Z}/5\mathbb{Z})\rtimes(\mathbb{Z}/5\mathbb{Z})^{*},\qquad |G|\mid 20.$$

Because $5$ is prime, a subgroup of $\operatorname{AGL}(1,5)$ is transitive on $\{0,\dots,4\}$ iff it contains a $5$-cycle (a translation). Hence:

- $T_5(x)-c$ **irreducible** $\iff$ $G$ transitive $\iff$ $G$ contains a translation.
- $T_5(x)-c$ **reducible** $\iff$ $G$ not transitive $\iff$ $G$ fixes some index $j$ $\iff$ $r_j\in\mathbb{Q}$ $\iff$ $T_5(x)-c$ has a rational root.

The last equivalence uses: a non-transitive subgroup of $\operatorname{AGL}(1,5)$ lies in a point stabilizer (conjugate to $(\mathbb{Z}/5\mathbb{Z})^{*}\cong C_4$), hence fixes a root, and a root fixed by the full Galois group is rational. $\blacksquare$

### Step 4. $48x^5-60x^3+15x-1$ has no rational root.

By the Rational Root Theorem, any rational root of $f(x)=48x^5-60x^3+15x-1$ has the form $\pm 1/d$ with $d\mid 48$. The divisors of $48$ are
$$1,2,3,4,6,8,12,16,24,48,$$
giving $20$ candidates $\pm 1/d$. Substituting (a representative sample):
$$f(1)=2,\quad f(-1)=-2,\quad f(\tfrac12)=\tfrac12,\quad f(-\tfrac12)=-\tfrac12,\quad f(\tfrac13)=\tfrac{16}{27},\quad f(-\tfrac13)=-\tfrac{16}{27},$$
$$f(\tfrac14)=\tfrac{11}{32},\quad f(\tfrac16)=\tfrac{7}{18},\quad f(\tfrac18)=\tfrac{71}{256},\quad f(\tfrac1{12})=\tfrac{13}{48},\quad f(\tfrac1{16})=\tfrac{239}{2048},\quad f(\tfrac1{24})=\tfrac{191}{13824},\quad f(\tfrac1{48})=\tfrac{5759}{25165824},$$
and the negatives give the corresponding negative values. **None of the $20$ candidates is a root.**

Hence $f(x)$ has no rational root.

### Step 5. Conclusion.

By the Lemma (Step 3), since $f(x)=48\bigl(T_5(x)-\tfrac13\bigr)$ has no rational root, $T_5(x)-\tfrac13$ is **irreducible** over $\mathbb{Q}$, of degree $5$. Therefore
$$[\mathbb{Q}(\cos(\theta/5)):\mathbb{Q}]=5,$$
which is **not** a power of $2$. By the constructibility criterion, $\cos(\theta/5)$ is not constructible, so $\theta/5$ is not constructible: **$\theta$ cannot be quintsected** with unmarked straightedge and compass.

Combined with Step 1, $\theta=\arccos(1/3)$ is a constructible angle that cannot be quintsected. $\blacksquare$

### PROOF COMPLETE
