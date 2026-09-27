# Proof

**Statement.** Let $k$ be a field of characteristic zero and size $\le\mathfrak{c}$. If $X$ is a $k$-variety, then to any pair of embeddings $\sigma,\tau:k\hookrightarrow\mathbb{C}$ we can associate a homotopy class of homotopy equivalences $\varphi_{\sigma,\tau}:X\times_\sigma\operatorname{Spec}\mathbb{C}\to X\times_\tau\operatorname{Spec}\mathbb{C}$ (analytic topologies) satisfying the cocycle conditions $\varphi_{\sigma,\upsilon}=\varphi_{\tau,\upsilon}\circ\varphi_{\sigma,\tau}$ and $\varphi_{\sigma,\sigma}=\mathrm{Id}$.

**Answer: TRUE.**

---

## Step 0: The condition $|k|\le\mathfrak{c}$

This condition guarantees that embeddings $k\hookrightarrow\mathbb{C}$ exist. Since $k$ has characteristic zero, it contains $\mathbb{Q}$. The transcendence degree of $k$ over $\mathbb{Q}$ is at most $|k|\le\mathfrak{c}$. Since $\mathbb{C}$ is algebraically closed with transcendence degree $\mathfrak{c}$ over $\mathbb{Q}$, any field of characteristic zero with transcendence degree $\le\mathfrak{c}$ over $\mathbb{Q}$ admits an embedding into $\mathbb{C}$.

---

## Step 1: Reduction to $k$ finitely generated over $\mathbb{Q}$

Since $X$ is a $k$-variety (finite type $k$-scheme), it is defined by finitely many equations with coefficients in $k$, involving only finitely many elements of $k$. Thus $X$ is defined over some finitely generated subfield $k_0\subset k$ (over $\mathbb{Q}$).

Any embedding $\sigma:k\hookrightarrow\mathbb{C}$ restricts to $\sigma_0=\sigma|_{k_0}:k_0\hookrightarrow\mathbb{C}$, and since $X$ is defined over $k_0$:
$$X\times_\sigma\operatorname{Spec}\mathbb{C}\cong X\times_{\sigma_0}\operatorname{Spec}\mathbb{C}=:X_{\sigma_0}.$$

If we construct $\varphi_{\sigma_0,\tau_0}$ for all pairs of embeddings of $k_0$ satisfying the cocycle conditions, then defining $\varphi_{\sigma,\tau}:=\varphi_{\sigma_0,\tau_0}$ gives a valid system for $k$ (the cocycle conditions for $\sigma,\tau,\upsilon:k\hookrightarrow\mathbb{C}$ follow from those for $\sigma_0,\tau_0,\upsilon_0:k_0\hookrightarrow\mathbb{C}$, since $X_\sigma=X_{\sigma_0}$ etc.).

**Henceforth, assume $k$ is finitely generated over $\mathbb{Q}$.**

---

## Step 2: The compositum $L=k\cdot\bar{\mathbb{Q}}$

Fix an embedding $\iota:k\hookrightarrow\mathbb{C}$ and form the compositum $L=k\cdot\bar{\mathbb{Q}}$ inside $\mathbb{C}$ (via $\iota$).

**Claim:** $L$ is finitely generated over $\bar{\mathbb{Q}}$ and is a regular extension of $\bar{\mathbb{Q}}$.

*Proof.* Since $k$ is finitely generated over $\mathbb{Q}$, say $k=\mathbb{Q}(x_1,\dots,x_n)$ (as a field), we have $L=\bar{\mathbb{Q}}(x_1,\dots,x_n)$, which is finitely generated over $\bar{\mathbb{Q}}$. Since $\bar{\mathbb{Q}}$ is algebraically closed, $L$ is automatically linearly disjoint from $\bar{\mathbb{Q}}$ over $\bar{\mathbb{Q}}$ (trivially), and $L$ is separable over $\bar{\mathbb{Q}}$ (characteristic zero). Hence $L$ is a regular extension of $\bar{\mathbb{Q}}$. $\square$

Since $X$ is defined over $k\subset L$, it is also defined over $L$.

---

## Step 3: Spreading out over a geometrically irreducible $\bar{\mathbb{Q}}$-variety

Since $L$ is finitely generated over $\bar{\mathbb{Q}}$ and regular over $\bar{\mathbb{Q}}$, there exists a **geometrically irreducible** $\bar{\mathbb{Q}}$-variety $T$ with function field $L$. (Take $T=\operatorname{Spec} B$ where $B$ is a finitely generated $\bar{\mathbb{Q}}$-algebra with $\operatorname{Frac}(B)=L$; geometric irreducibility follows from regularity of $L/\bar{\mathbb{Q}}$.)

Spread $X$ out to a family $\mathcal{X}\to T$ (over a dense open subscheme of $T$, which we again denote $T$ for convenience). This is a finite type morphism of $\bar{\mathbb{Q}}$-schemes.

**Key consequence:** $T_\mathbb{C}=T\times_{\bar{\mathbb{Q}}}\mathbb{C}$ is irreducible (geometric irreducibility), so $T(\mathbb{C})$ is connected in the analytic topology.

---

## Step 4: Thom isotopy lemma

**Theorem (Thom–Mather first isotopy lemma).** For a finite type morphism $f:\mathcal{X}\to T$ of complex algebraic varieties, there exists a Whitney stratification of $T$ such that $f$ is a topological fiber bundle over each stratum. The strata are locally closed algebraic subsets defined over the same field as $f$.

Since $f:\mathcal{X}\to T$ is defined over $\bar{\mathbb{Q}}$, the stratification is defined over $\bar{\mathbb{Q}}$. Let $V\subset T_\mathbb{C}$ be the open stratum (the stratum containing the generic point). Then:

- $V$ is a dense open subscheme of $T_\mathbb{C}$ (since $T_\mathbb{C}$ is irreducible).
- The boundary $\partial V = T_\mathbb{C}\setminus V$ is a proper $\bar{\mathbb{Q}}$-closed subvariety of $T_\mathbb{C}$.
- $\mathcal{X}|_V \to V$ is a topological fiber bundle (hence a Serre fibration, since $V(\mathbb{C})$ is paracompact, being a complex analytic space).

---

## Step 5: Very general point argument

Let $B$ be the coordinate ring of $T$ (a finitely generated $\bar{\mathbb{Q}}$-algebra with $\operatorname{Frac}(B)=L$). A $\mathbb{C}$-point $t\in T(\mathbb{C})$ corresponds to a $\bar{\mathbb{Q}}$-algebra homomorphism $\varphi_t:B\to\mathbb{C}$.

**Claim:** For any embedding $\tilde{\sigma}:L\hookrightarrow\mathbb{C}$, the corresponding point $t_{\tilde{\sigma}}\in T(\mathbb{C})$ lies in $V(\mathbb{C})$.

*Proof.* The point $t_{\tilde{\sigma}}$ lies in $\partial V$ iff $\tilde{\sigma}(f)=0$ for all $f$ in the ideal $I(\partial V)\subset B$. Since $\partial V$ is a proper $\bar{\mathbb{Q}}$-closed subvariety, $I(\partial V)$ contains a nonzero element $f\in B\setminus\{0\}$. Since $f\in B\subset L$ and $f\neq 0$, and $\tilde{\sigma}:L\hookrightarrow\mathbb{C}$ is a **field embedding (injective)**, we have $\tilde{\sigma}(f)\neq 0$. Hence $t_{\tilde{\sigma}}\notin\partial V$, i.e., $t_{\tilde{\sigma}}\in V(\mathbb{C})$. $\square$

---

## Step 6: Path connectivity and transport

**$V(\mathbb{C})$ is path-connected.** Since $V$ is a dense open of the irreducible $\mathbb{C}$-variety $T_\mathbb{C}$, $V$ is irreducible. The $\mathbb{C}$-points of an irreducible $\mathbb{C}$-variety are connected in the analytic topology (the smooth locus is connected, and the singular locus has real codimension $\ge 2$). Since $V(\mathbb{C})$ is locally path-connected (it is a complex analytic space), connected implies path-connected.

**Extension of embeddings.** Any embedding $\sigma:k\hookrightarrow\mathbb{C}$ extends to an embedding $\tilde{\sigma}:L=k\cdot\bar{\mathbb{Q}}\hookrightarrow\mathbb{C}$. (Since $\mathbb{C}$ is algebraically closed, any embedding of $k$ extends to the algebraic extension $L/k$; this uses Zorn's lemma but is standard field theory.)

For each such $\tilde{\sigma}$, the point $t_{\tilde{\sigma}}\in V(\mathbb{C})$ (by Step 5), and the fiber $\mathcal{X}_{t_{\tilde{\sigma}}}=X\times_{k,\sigma}\mathbb{C}=:X_\sigma$ (since $\tilde{\sigma}|_k=\sigma$).

---

## Step 7: Construction of $\varphi_{\sigma,\tau}$ and cocycle conditions

**Construction.** Fix a base point $t_0\in V(\mathbb{C})$. For each embedding $\sigma:k\hookrightarrow\mathbb{C}$:

1. Choose an extension $\tilde{\sigma}:L\hookrightarrow\mathbb{C}$.
2. Choose a path $\gamma_\sigma:[0,1]\to V(\mathbb{C})$ from $t_0$ to $t_{\tilde{\sigma}}$ (possible by path-connectivity).

Since $\mathcal{X}|_V\to V$ is a Serre fibration, the homotopy lifting property gives a **parallel transport** along any path in $V(\mathbb{C})$, yielding a homotopy equivalence between the fibers over the endpoints. The homotopy class of this equivalence depends only on the homotopy class of the path (relative endpoints).

Define:
$$\varphi_{\sigma,\tau}:=\text{transport along } \gamma_\tau\cdot\gamma_\sigma^{-1},$$
where $\gamma_\sigma^{-1}$ is the reverse path (from $t_{\tilde{\sigma}}$ to $t_0$) and $\gamma_\tau\cdot\gamma_\sigma^{-1}$ denotes path concatenation (first $\gamma_\sigma^{-1}$, then $\gamma_\tau$). This is a homotopy equivalence $X_\sigma\to X_\tau$.

**Unit condition.** $\varphi_{\sigma,\sigma}$ = transport along $\gamma_\sigma\cdot\gamma_\sigma^{-1}$ = transport along the null-homotopic loop at $t_0$ = $\mathrm{Id}_{X_\sigma}$. $\checkmark$

**Cocycle condition.** For embeddings $\sigma,\tau,\upsilon:k\hookrightarrow\mathbb{C}$:
- $\varphi_{\sigma,\upsilon}$ = transport along $\gamma_\upsilon\cdot\gamma_\sigma^{-1}$.
- $\varphi_{\tau,\upsilon}\circ\varphi_{\sigma,\tau}$ = (transport along $\gamma_\upsilon\cdot\gamma_\tau^{-1}$) $\circ$ (transport along $\gamma_\tau\cdot\gamma_\sigma^{-1}$) = transport along $(\gamma_\upsilon\cdot\gamma_\tau^{-1})\cdot(\gamma_\tau\cdot\gamma_\sigma^{-1})$ = transport along $\gamma_\upsilon\cdot\gamma_\sigma^{-1}$ = $\varphi_{\sigma,\upsilon}$. $\checkmark$

(The composition of transports along concatenated paths equals the transport along the concatenation, by the homotopy lifting property of the fibration.)

---

## Step 8: Remarks on generality

**Non-smooth $X$.** The Thom–Mather isotopy lemma applies to arbitrary finite type morphisms (not only smooth ones), producing a Whitney stratification of the target over which the morphism is a topological fibration. Hence the proof works for any $k$-variety $X$ (smooth or singular).

**Why spreading out over $\bar{\mathbb{Q}}$ rather than $\mathbb{Q}$.** If one spreads out over a $\mathbb{Q}$-variety $S$ with function field $k$, the base $S_\mathbb{C}$ may fail to be irreducible when $k$ is not a regular extension of $\mathbb{Q}$ (i.e., when $\bar{\mathbb{Q}}\cap k\neq\mathbb{Q}$). In that case, different embeddings $\sigma,\tau$ may land in different connected components of $S(\mathbb{C})$, and the path-connectivity argument breaks down. By passing to the compositum $L=k\cdot\bar{\mathbb{Q}}$, which is always a regular extension of $\bar{\mathbb{Q}}$, we guarantee that the base $T_\mathbb{C}$ is irreducible (hence $V(\mathbb{C})$ is connected), so **all** embedding-points lie in the same connected component. This is the key idea that makes the proof work uniformly for all pairs of embeddings.

---

$$\boxed{\text{True}}$$

### PROOF COMPLETE
