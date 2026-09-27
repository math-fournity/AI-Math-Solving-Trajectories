# Proof: Exceptional divisor of a 3-fold divisorial terminal contraction is irreducible

## Theorem

Let $X$ be a 3-fold, and $f: Y \rightarrow X$ a birational $\mathbb{Q}$-factorial divisorial terminal contraction (of relative Picard number one) contracting a divisor $E \subset Y$ to a point $p \in X$. Then the exceptional divisor $E$ is necessarily irreducible.

## Proof

We argue by contradiction. Suppose $E$ is reducible, so $E = E_1 + E_2 + \cdots + E_n$ with $n \geq 2$, where each $E_i$ is a distinct prime divisor on $Y$. It suffices to derive a contradiction from any two components; we work with $E_1$ and $E_2$.

### Step 1: Setup and numerical proportionality

Since $f$ is a birational extremal contraction with $\rho(Y/X) = 1$, the relative Néron–Severi space $N^1(Y/X)$ is a one-dimensional real vector space. Each $E_i$ is $f$-exceptional (its image under $f$ is the point $p$), so its class $[E_i] \in N^1(Y/X)$ is nonzero. Because $Y$ is $\mathbb{Q}$-factorial, each $E_i$ is $\mathbb{Q}$-Cartier, so $[E_i]$ lies in the $\mathbb{Q}$-vector subspace $N^1(Y/X)_{\mathbb{Q}}$, which is one-dimensional over $\mathbb{Q}$. Therefore there exists $\lambda \in \mathbb{Q}_{>0}$ such that

$$E_1 \equiv \lambda \, E_2 \quad \text{over } X,$$

i.e., $E_1 - \lambda E_2$ is $f$-numerically trivial. (The ratio $\lambda$ is rational because both $[E_1]$ and $[E_2]$ lie in the same one-dimensional $\mathbb{Q}$-vector space.)

Set $D = E_1 - \lambda E_2$. This is a $\mathbb{Q}$-Cartier divisor on $Y$ (since $Y$ is $\mathbb{Q}$-factorial and $\lambda \in \mathbb{Q}$) that is $f$-numerically trivial.

### Step 2: Upgrading numerical triviality to ℚ-linear triviality over $X$

We claim that $D \sim_{\mathbb{Q}} f^*\Delta$ for some $\mathbb{Q}$-Cartier divisor $\Delta$ on $X$.

We verify the hypotheses of the **relative basepoint-free theorem** (Kollár–Mori, *Birational Geometry of Algebraic Varieties*, Theorem 3.3):

1. **$f: Y \to X$ is a proper morphism of normal varieties.** ✓ ( $f$ is a birational morphism of varieties.)

2. **$(Y, 0)$ is klt.** ✓ ( $Y$ has terminal singularities, and terminal $\Rightarrow$ klt, since terminal requires all discrepancies $a_i > 0$ while klt requires $a_i > -1$.)

3. **$D$ is $f$-nef.** ✓ ( $D$ is $f$-numerically trivial, so $D \cdot C = 0$ for every curve $C$ contracted by $f$.)

4. **$D - K_Y$ is $f$-nef and $f$-big.** Since $D \equiv 0$ over $X$, we have $D - K_Y \equiv -K_Y$ over $X$. Because $f$ is a $K_Y$-negative extremal contraction (the contraction of a $K_Y$-negative extremal ray $R$ with $\rho(Y/X)=1$), the divisor $-K_Y$ is positive on $N^1(Y/X)$, hence $-K_Y$ is $f$-ample. In particular, $-K_Y$ is $f$-nef and $f$-big. ✓

By the basepoint-free theorem, $D$ is $f$-semiample: there exists $m > 0$ such that $mD$ is Cartier and the linear system $|mD|$ is basepoint-free over $X$, defining a morphism $g: Y \to W$ over $X$ with $mD \sim g^*H$ for some ample divisor $H$ on $W$.

Since $D$ is $f$-numerically trivial, $mD \cdot C = 0$ for every curve $C$ contracted by $f$. Thus $g$ contracts every curve that $f$ contracts. Because $\rho(Y/X) = 1$, the contracted curves of $f$ span the unique extremal ray, so $g$ factors through $f$:

$$g = h \circ f \quad \text{for some morphism } h: X \to W.$$

Therefore

$$mD \sim g^*H = f^*(h^*H) = f^*A,$$

where $A = h^*H$ is a Cartier divisor on $X$. Setting $\Delta = \frac{1}{m}A$, we obtain

$$D \sim_{\mathbb{Q}} f^*\Delta,$$

with $\Delta$ a $\mathbb{Q}$-Cartier divisor on $X$. This establishes the claim.

### Step 3: The divisor comparison argument

Choose $m > 0$ sufficiently divisible so that $mD$ and $mf^*\Delta$ are both Cartier divisors and $mD \sim mf^*\Delta$. Then there exists a rational function $\phi \in K(Y)^*$ such that

$$\operatorname{div}_Y(\phi) = mD - mf^*\Delta = mE_1 - m\lambda E_2 - mf^*\Delta. \tag{$\star$}$$

Since $f: Y \to X$ is birational, $K(Y) \cong K(X)$, so $\phi$ is also a rational function on $X$.

**Key observation:** $f$ is an isomorphism on $Y \setminus \operatorname{Supp}(E) \to X \setminus \{p\}$, because the exceptional locus of $f$ is exactly $\operatorname{Supp}(E)$, which maps to the single point $p$.

Restricting $(\star)$ to $Y \setminus \operatorname{Supp}(E)$: the divisors $E_1$, $E_2$, and the exceptional part of $f^*\Delta$ are all supported on $\operatorname{Supp}(E)$, so

$$\operatorname{div}_Y(\phi)\big|_{Y \setminus \operatorname{Supp}(E)} = -mf^*\Delta\big|_{Y \setminus \operatorname{Supp}(E)} = -m\Delta\big|_{X \setminus \{p\}}.$$

Via the isomorphism $Y \setminus \operatorname{Supp}(E) \xrightarrow{\sim} X \setminus \{p\}$, this gives

$$\operatorname{div}_X(\phi)\big|_{X \setminus \{p\}} = -m\Delta\big|_{X \setminus \{p\}}.$$

Now, $X$ is a 3-fold and $p$ is a point, so $\operatorname{codim}_X(p) = 3$. A prime divisor on $X$ has codimension 1, so no prime divisor is supported at $\{p\}$. Therefore, a Weil divisor on $X$ is completely determined by its restriction to $X \setminus \{p\}$. Since $m\Delta$ is Cartier (hence a Weil divisor), we conclude

$$\operatorname{div}_X(\phi) = -m\Delta \quad \text{as Cartier divisors on } X.$$

### Step 4: Deriving the contradiction

Pulling back the equality $\operatorname{div}_X(\phi) = -m\Delta$ via the birational morphism $f$, and using the standard fact that for a rational function $\phi$ on $X$ viewed on $Y$ via the birational identification, $\operatorname{div}_Y(\phi) = f^*\operatorname{div}_X(\phi)$, we obtain

$$\operatorname{div}_Y(\phi) = f^*(-m\Delta) = -mf^*\Delta. \tag{$\star\star$}$$

Comparing $(\star)$ and $(\star\star)$:

$$mE_1 - m\lambda E_2 - mf^*\Delta = -mf^*\Delta,$$

which yields

$$mE_1 - m\lambda E_2 = 0, \quad \text{i.e.,} \quad E_1 = \lambda E_2 \quad \text{as } \mathbb{Q}\text{-divisors}.$$

But $E_1$ and $E_2$ are **distinct prime divisors** (distinct irreducible reduced integral divisors). The equality $E_1 = \lambda E_2$ as $\mathbb{Q}$-divisors requires that $E_1$ and $E_2$ have the same support (i.e., $E_1 = E_2$ as sets) and that $\lambda = 1$ (matching the coefficients of the unique prime component). This contradicts the assumption that $E_1 \neq E_2$.

Therefore, $E$ cannot be reducible. $\blacksquare$

## Summary of key ingredients

| Step | Tool used | Why it applies |
|------|-----------|----------------|
| Numerical proportionality $E_1 \equiv \lambda E_2$ over $X$ | $\rho(Y/X) = 1$ + $\mathbb{Q}$-factoriality of $Y$ | $N^1(Y/X) \cong \mathbb{R}$ is 1-dim; $[E_i] \neq 0$; $\lambda \in \mathbb{Q}$ from the lattice structure |
| Numerical $\Rightarrow$ $\mathbb{Q}$-linear equivalence over $X$ | Relative basepoint-free theorem | $(Y,0)$ klt (terminal $\Rightarrow$ klt); $D$ $f$-nef (numerically trivial); $D - K_Y \equiv -K_Y$ is $f$-ample ($K_Y$-negative contraction) |
| Divisor comparison | $f$ isomorphism on $Y \setminus E \to X \setminus \{p\}$ + $\operatorname{codim}_X(p) = 3$ | Divisors determined by restriction away from codim $\geq 2$ subset; $\operatorname{div}_Y(\phi) = f^*\operatorname{div}_X(\phi)$ for birational $f$ |
| Contradiction | $E_1, E_2$ distinct prime divisors | $E_1 = \lambda E_2$ forces $E_1 = E_2$ and $\lambda = 1$ |

**Remark.** The proof uses only the properties of $Y$ ($\mathbb{Q}$-factoriality and terminality) and of the contraction $f$ ($K_Y$-negative, $\rho(Y/X) = 1$, divisorial to a point). It does **not** require $X$ to be $\mathbb{Q}$-factorial, thereby avoiding any circular dependence between the $\mathbb{Q}$-factoriality of $X$ and the irreducibility of $E$.

$$\boxed{Yes, \text{ the exceptional divisor } E \text{ is necessarily irreducible.}}$$
