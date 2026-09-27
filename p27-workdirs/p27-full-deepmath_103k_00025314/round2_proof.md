# Riesz–Markov–Kakutani Representation Theorem

## Problem (interpreted)

Let $X$ be a compact Hausdorff space, $\Gamma = C(X)$ the space of continuous real-valued functions on $X$, $\Sigma = \mathcal{B}(X)$ the Borel $\sigma$-algebra, and $F : C(X) \to \mathbb{R}$ a positive linear functional with $F(\mathbf{1}) = 1$. Does there exist a unique probability measure $\mu$ on $\mathcal{B}(X)$ such that

$$F(f) = \int_X f \, d\mu \quad \text{for all } f \in C(X)?$$

**Answer: Yes.** There exists a unique regular Borel probability measure $\mu$ representing $F$.

---

## Part I — Uniqueness

**Theorem.** If $\mu_1, \mu_2$ are regular Borel probability measures on $X$ with $\int f \, d\mu_1 = \int f \, d\mu_2$ for all $f \in C(X)$, then $\mu_1 = \mu_2$.

*Proof.* Let $E \in \mathcal{B}(X)$ and $\varepsilon > 0$. By regularity of $\mu_1$ and $\mu_2$, there exist compact $K$ and open $U$ with $K \subseteq E \subseteq U$ and $\mu_i(U \setminus K) < \varepsilon$ for $i = 1, 2$.

Since $X$ is compact Hausdorff (hence normal), by Urysohn's lemma there exists $f \in C(X)$ with $0 \leq f \leq 1$, $f|_K = 1$, and $f|_{X \setminus U} = 0$.

For each $i$:
$$\mu_i(K) \leq \int f \, d\mu_i \leq \mu_i(U).$$

Since $\int f \, d\mu_1 = \int f \, d\mu_2$, we have:
$$\mu_1(E) \leq \mu_1(U) < \mu_1(K) + \varepsilon \leq \int f \, d\mu_1 + \varepsilon = \int f \, d\mu_2 + \varepsilon \leq \mu_2(U) < \mu_2(E) + 2\varepsilon.$$

By symmetry, $|\mu_1(E) - \mu_2(E)| < 2\varepsilon$. Since $\varepsilon > 0$ is arbitrary, $\mu_1(E) = \mu_2(E)$. $\square$

---

## Part II — Existence

We construct $\mu$ via the Riesz–Markov–Kakutani procedure (following Rudin, *Real and Complex Analysis*, Theorem 2.14).

### Step 1 — Definition on open sets

For $U \subseteq X$ open, define:
$$\mu(U) = \sup\{ F(f) : f \in C(X),\; 0 \leq f \leq \mathbf{1},\; \operatorname{supp}(f) \subseteq U \}.$$

We write $f \prec U$ to mean $f \in C(X)$, $0 \leq f \leq 1$, $\operatorname{supp}(f) \subseteq U$. Since $F$ is positive and $F(\mathbf{1}) = 1$, we have $0 \leq \mu(U) \leq 1$.

### Step 2 — Outer measure

For any $E \subseteq X$, define:
$$\mu^*(E) = \inf\{ \mu(U) : U \text{ open},\; E \subseteq U \}.$$

**Claim.** $\mu^*$ is an outer measure.

- $\mu^*(\emptyset) = 0$: Clear since $\mu(\emptyset) = 0$.
- Monotonicity: $E \subseteq F \Rightarrow \mu^*(E) \leq \mu^*(F)$. Clear from the definition.
- Countable subadditivity: Let $E \subseteq \bigcup_{i=1}^\infty E_i$. For each $i$, pick open $U_i \supseteq E_i$ with $\mu(U_i) < \mu^*(E_i) + \varepsilon/2^i$. Set $U = \bigcup U_i$ (open, $E \subseteq U$). For any $f \prec U$, $\operatorname{supp}(f)$ is compact and covered by $\{U_i\}$, so $\operatorname{supp}(f) \subseteq U_1 \cup \cdots \cup U_N$ for some $N$. By partition of unity subordinate to $\{U_1, \ldots, U_N\}$, write $f = \sum_{i=1}^N f \cdot \psi_i$ where $\psi_i \prec U_i$ and $\sum \psi_i = 1$ on $\operatorname{supp}(f)$. Then $f \cdot \psi_i \prec U_i$, so $F(f \cdot \psi_i) \leq \mu(U_i)$, giving $F(f) = \sum F(f \cdot \psi_i) \leq \sum_{i=1}^N \mu(U_i) \leq \sum_{i=1}^\infty \mu(U_i) < \sum \mu^*(E_i) + \varepsilon$. Taking sup over $f \prec U$: $\mu(U) \leq \sum \mu^*(E_i) + \varepsilon$, hence $\mu^*(E) \leq \sum \mu^*(E_i) + \varepsilon$. Let $\varepsilon \to 0$. $\square$

### Step 3 — Borel sets are $\mu^*$-measurable

By Carathéodory's theorem, it suffices to show that every closed set $C$ is measurable, i.e., for every $A \subseteq X$:
$$\mu^*(A) \geq \mu^*(A \cap C) + \mu^*(A \setminus C).$$

It suffices to show this for $A = U$ open (since $\mu^*$ is defined via open supersets). So we need:
$$\mu(U) \geq \mu(U \cap C) + \mu(U \setminus C).$$

Let $g \prec U \setminus C$ with $F(g) > \mu(U \setminus C) - \varepsilon/2$. Since $\operatorname{supp}(g)$ is compact and disjoint from the closed set $C$, by normality there exist disjoint open sets $W_1 \supseteq \operatorname{supp}(g)$ and $W_2 \supseteq C$.

Set $V = U \cap W_2$; this is open, contains $U \cap C$, and is disjoint from $\operatorname{supp}(g)$. For any $h \prec V$, we have $\operatorname{supp}(h) \cap \operatorname{supp}(g) = \emptyset$, so $g + h \prec U$ (the supports are disjoint, ensuring $g + h \leq 1$). Thus:
$$F(g) + F(h) = F(g + h) \leq \mu(U).$$

Taking sup over $h \prec V$: $F(g) + \mu(V) \leq \mu(U)$. Since $V \supseteq U \cap C$, $\mu(V) \geq \mu(U \cap C)$. Therefore:
$$\mu(U) \geq F(g) + \mu(U \cap C) > \mu(U \setminus C) - \varepsilon/2 + \mu(U \cap C).$$

Let $\varepsilon \to 0$. $\square$

### Step 4 — Key lemma

**Lemma.** Let $K$ be compact, $U$ open, $K \subseteq U$. If $h \in C(X)$ satisfies $K \prec h \prec U$ (i.e., $h = 1$ on $K$, $\operatorname{supp}(h) \subseteq U$, $0 \leq h \leq 1$), then:
$$\mu(K) \leq F(h) \leq \mu(U).$$

*Proof.* The upper bound $F(h) \leq \mu(U)$ is immediate from $h \prec U$.

For the lower bound, let $V = \{h > 1 - \varepsilon\}$ (open, contains $K$). For any $g \prec V$, we have $g \leq \mathbf{1}_V \leq \frac{h}{1-\varepsilon}$ (since $h > 1 - \varepsilon$ on $V$ and $g \leq 1$ with $\operatorname{supp}(g) \subseteq V$). By positivity: $F(g) \leq \frac{F(h)}{1-\varepsilon}$. Taking sup over $g \prec V$: $\mu(V) \leq \frac{F(h)}{1-\varepsilon}$, so $F(h) \geq (1-\varepsilon)\mu(V) \geq (1-\varepsilon)\mu(K)$ (since $V \supseteq K$). Let $\varepsilon \to 0$: $F(h) \geq \mu(K)$. $\square$

### Step 5 — Regularity

**Outer regularity**: For any Borel $E$, $\mu(E) = \inf\{\mu(U) : E \subseteq U, U \text{ open}\}$ by construction.

**Inner regularity**: For open $U$, $\mu(U) = \sup\{F(f) : f \prec U\}$. Each $f \prec U$ has $\operatorname{supp}(f)$ compact with $\operatorname{supp}(f) \subseteq U$, and $F(f) \leq \mu(\operatorname{supp}(f))$... actually, more directly: for $f \prec U$, let $K = \operatorname{supp}(f)$. Then $K \prec f$ (well, $f$ might not be exactly 1 on $K$, but we can use the lemma with a function that is 1 on $K$). The key point is that $\mu(U) = \sup\{\mu(K) : K \text{ compact}, K \subseteq U\}$, which follows from the sup definition and the lemma. For general Borel $E$ with $\mu(E) < \infty$ (which holds since $X$ is compact and $\mu(X) \leq 1$), inner regularity follows from outer regularity and the identity $\mu(E) = \mu(X) - \mu(X \setminus E)$, using outer regularity on $X \setminus E$ and compactness of closed subsets of $X$.

### Step 6 — The representation formula $\int f \, d\mu = F(f)$

We prove this first for $f \geq 0$, then extend by linearity.

#### Layer-cake representation

For $f \geq 0$ measurable, by Fubini's theorem:
$$\int_X f \, d\mu = \int_0^\infty \mu(\{f > t\}) \, dt.$$

(This follows from $f(x) = \int_0^{f(x)} dt = \int_0^\infty \mathbf{1}_{\{f > t\}}(x)\,dt$ and Fubini.)

Note: $\int_0^\infty \mu(\{f \geq t\})\,dt = \int_0^\infty \mu(\{f > t\})\,dt$ since $\{f \geq t\} \setminus \{f > t\} = \{f = t\}$ and $\{t : \mu(\{f = t\}) > 0\}$ is at most countable.

#### Upper bound: $F(f) \leq \int f \, d\mu$

Let $M = \|f\|_\infty$, $N$ a positive integer, $\delta = M/N$. Define:
- $K_k = \{f \geq k\delta\}$ for $k = 1, \ldots, N$ (compact, decreasing).
- $V_k = \{f > (k-1)\delta\}$ for $k = 1, \ldots, N$ (open, $K_k \subseteq V_k$).

By Urysohn's lemma, choose $h_k \in C(X)$ with $K_k \prec h_k \prec V_k$ (i.e., $h_k = 1$ on $K_k$, $\operatorname{supp}(h_k) \subseteq V_k$, $0 \leq h_k \leq 1$).

**Claim.** $f \leq \delta \sum_{k=1}^N h_k + \delta \cdot \mathbf{1}$.

*Proof of claim.* Fix $x \in X$, let $t = f(x) \geq 0$.
- If $t = 0$: $\delta \sum h_k(x) + \delta \geq \delta > 0 = t$. ✓
- If $t > 0$: let $j = \lfloor t/\delta \rfloor$, so $j\delta \leq t < (j+1)\delta$. For $k \leq j$, we have $f(x) = t \geq j\delta \geq k\delta$, so $x \in K_k$ and $h_k(x) = 1$. Thus $\delta \sum_{k=1}^N h_k(x) \geq j\delta \geq t - \delta$, giving $\delta \sum h_k(x) + \delta \geq t$. ✓

Applying $F$ (using positivity and linearity):
$$F(f) \leq \delta \sum_{k=1}^N F(h_k) + \delta \cdot F(\mathbf{1}) = \delta \sum_{k=1}^N F(h_k) + \delta.$$

By the Key Lemma, $F(h_k) \leq \mu(V_k) = \mu(\{f > (k-1)\delta\})$. So:
$$F(f) \leq \delta \sum_{k=1}^N \mu(\{f > (k-1)\delta\}) + \delta = \delta \sum_{k=0}^{N-1} \mu(\{f > k\delta\}) + \delta.$$

The sum $\delta \sum_{k=0}^{N-1} \mu(\{f > k\delta\})$ is the **left Riemann sum** for $g(t) = \mu(\{f > t\})$ on $[0, M]$ with uniform mesh $\delta$. Since $g$ is decreasing and non-negative:

$$\delta \sum_{k=0}^{N-1} g(k\delta) - \int_0^M g(t)\,dt = \sum_{k=0}^{N-1} \int_{k\delta}^{(k+1)\delta} [g(k\delta) - g(t)]\,dt \leq \sum_{k=0}^{N-1} \delta\,[g(k\delta) - g((k+1)\delta)] = \delta\,[g(0) - g(M)] \leq \delta \cdot g(0).$$

Since $g(0) = \mu(\{f > 0\}) \leq \mu(X) = 1$ (see Step 7 below), we get:
$$F(f) \leq \int_0^M \mu(\{f > t\})\,dt + \delta + \delta = \int f \, d\mu + 2\delta.$$

Letting $\delta \to 0$ (i.e., $N \to \infty$): $\boxed{F(f) \leq \int f \, d\mu}$.

#### Lower bound: $F(f) \geq \int f \, d\mu$

Using the same $K_k, V_k, h_k$ as above:

**Claim.** $\delta \sum_{k=1}^N h_k \leq f + \delta \cdot \mathbf{1}$.

*Proof of claim.* Fix $x \in X$, let $t = f(x) \geq 0$. If $h_k(x) > 0$ then $x \in V_k = \{f > (k-1)\delta\}$, so $t > (k-1)\delta$, i.e., $k < t/\delta + 1$. Thus the number of $k$ with $h_k(x) > 0$ is at most $\lfloor t/\delta \rfloor + 1$. Since $h_k \leq 1$:
$$\delta \sum_{k=1}^N h_k(x) \leq \delta\left(\lfloor t/\delta \rfloor + 1\right) \leq \delta \cdot (t/\delta + 1) = t + \delta.$$

So $f \geq \delta \sum h_k - \delta \cdot \mathbf{1}$. Applying $F$:
$$F(f) \geq \delta \sum_{k=1}^N F(h_k) - \delta.$$

By the Key Lemma, $F(h_k) \geq \mu(K_k) = \mu(\{f \geq k\delta\})$. So:
$$F(f) \geq \delta \sum_{k=1}^N \mu(\{f \geq k\delta\}) - \delta.$$

The sum $\delta \sum_{k=1}^N \mu(\{f \geq k\delta\})$ is the **right Riemann sum** for $\tilde{g}(t) = \mu(\{f \geq t\})$ on $[0, M]$ with uniform mesh $\delta$. Since $\tilde{g}$ is decreasing:

$$\int_0^M \tilde{g}(t)\,dt - \delta \sum_{k=1}^N \tilde{g}(k\delta) = \sum_{k=1}^N \int_{(k-1)\delta}^{k\delta} [\tilde{g}(t) - \tilde{g}(k\delta)]\,dt \leq \sum_{k=1}^N \delta\,[\tilde{g}((k-1)\delta) - \tilde{g}(k\delta)] = \delta\,[\tilde{g}(0) - \tilde{g}(M)] \leq \delta \cdot \tilde{g}(0) \leq \delta.$$

So $\delta \sum_{k=1}^N \mu(\{f \geq k\delta\}) \geq \int_0^M \mu(\{f \geq t\})\,dt - \delta = \int f \, d\mu - \delta$.

Therefore:
$$F(f) \geq \int f \, d\mu - \delta - \delta = \int f \, d\mu - 2\delta.$$

Letting $\delta \to 0$: $\boxed{F(f) \geq \int f \, d\mu}$.

#### Combining

For $f \geq 0$: $F(f) = \int f \, d\mu$.

For general $f \in C(X)$: write $f = f^+ - f^-$ with $f^+ = \max(f, 0)$, $f^- = \max(-f, 0)$, both continuous and non-negative. Then:
$$F(f) = F(f^+) - F(f^-) = \int f^+ \, d\mu - \int f^- \, d\mu = \int f \, d\mu. \quad \square$$

### Step 7 — $\mu$ is a probability measure

Taking $f = \mathbf{1}$ in the representation formula:
$$\mu(X) = \int \mathbf{1} \, d\mu = F(\mathbf{1}) = 1.$$

So $\mu$ is a probability measure. $\square$

---

## Conclusion

There exists a unique regular Borel probability measure $\mu$ on $X$ such that $F(f) = \int_X f \, d\mu$ for all $f \in C(X)$.

$$\boxed{\text{Yes}}$$

### PROOF COMPLETE
