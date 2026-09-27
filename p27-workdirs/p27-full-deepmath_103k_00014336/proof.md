# Maximum Modulus Principle on Connected Analytic Subsets with Singularities

## Theorem

Let $U \subset \mathbb{C}^n$ be a domain, $X \subset U$ a connected analytic subset, and $f : U \to \mathbb{C}$ a holomorphic function. If $|f|$ attains its maximum on $X$, i.e. there exists $p \in X$ with
$$
|f(p)| = \max_{x \in X} |f(x)|,
$$
then $f$ is constant on $X$.

**Answer: $\boxed{\text{Yes}}$** — the maximum modulus principle holds for connected analytic subsets even in the presence of singularities.

---

## Proof

We proceed by induction on $d := \dim X$.

### Base case: $d = 0$

A $0$-dimensional analytic set is discrete. Since $X$ is connected, $X$ is a single point, and the claim is trivial.

### Inductive step

Assume the result holds for every connected analytic subset of dimension $< d$, with $d \geq 1$. Let $X$ be a connected analytic subset of dimension $d$, and let $f : U \to \mathbb{C}$ be holomorphic with $|f|$ attaining its maximum $M := \max_X |f|$ at some $p \in X$.

If $M = 0$, then $f \equiv 0$ on $X$ and we are done. Hence assume $M > 0$.

Define the **level set**
$$
S := \{x \in X : f(x) = f(p)\}.
$$
Since $f$ is continuous, $S$ is closed in $X$. We will show $S$ is also open in $X$; by connectedness of $X$ this forces $S = X$, i.e. $f \equiv f(p)$ on $X$.

It suffices to show: for every $q \in S$, the set $S$ contains a neighborhood of $q$ in $X$.

Fix $q \in S$, so $f(q) = f(p)$ and $|f(q)| = M$.

---

#### Case A: $q \in X_{\mathrm{reg}}$ (regular point)

Near $q$, the set $X$ is a $d$-dimensional complex submanifold of $U$. The restriction $f|_X$ is holomorphic on this submanifold, and $|f|$ attains its local maximum at $q$. By the classical maximum modulus principle on complex manifolds, $f$ is constant in a neighborhood of $q$ in $X$. Hence $S$ contains a neighborhood of $q$ in $X$.

---

#### Case B: $q \in X_{\mathrm{sing}}$ (singular point)

We handle the singular point in two sub-steps.

**Step B1 — The singular locus.** The singular locus $X_{\mathrm{sing}}$ is a proper analytic subset of $X$, hence
$$
\dim X_{\mathrm{sing}} < d.
$$
Let $Z$ be the connected component of $X_{\mathrm{sing}}$ containing $q$. The restriction $f|_{X_{\mathrm{sing}}}$ is holomorphic and $|f|$ attains its maximum on $Z$ at $q$. Since $\dim Z < d$, the **induction hypothesis** applies, giving $f \equiv f(q)$ on $Z$. Thus $Z \subset S$.

**Step B2 — Regular branches accumulating at $q$.** In a small neighborhood $\Omega$ of $q$ in $U$, the regular part $X_{\mathrm{reg}} \cap \Omega$ has finitely many connected components $C_1, \dots, C_m$ whose closures contain $q$. Each $C_i$ is a $d$-dimensional complex submanifold. We claim $f \equiv f(q)$ on $C_i$ near $q$ for every $i$.

Fix $C_i$. Since $f$ is continuous on $U$ and $q \in \overline{C_i}$,
$$
\lim_{\substack{x \to q \\ x \in C_i}} f(x) = f(q), \qquad |f(q)| = M.
$$

We now use a **graph parametrization** near $q$.

- The **tangent cone** $T_q C_i$ is a $d$-dimensional complex cone (closed under multiplication by $e^{i\theta}$, $\theta \in \mathbb{R}$), spanning a $d$-dimensional complex linear subspace $L \subset \mathbb{C}^n$.

- Choose coordinates so that $q = 0$ and $L = \{z_{d+1} = \cdots = z_n = 0\}$. Write $z = (z', z'')$ with $z' = (z_1, \dots, z_d)$, $z'' = (z_{d+1}, \dots, z_n)$.

- By the local parametrization theorem for analytic sets, after shrinking $\Omega$, the branch $C_i$ is a **graph** over a punctured neighborhood of $0 \in \mathbb{C}^d$:
  $$
  z'' = \psi(z'), \qquad \psi = (\psi_{d+1}, \dots, \psi_n),
  $$
  where each $\psi_j$ is holomorphic on a punctured ball $B^*_\varepsilon(0) \subset \mathbb{C}^d$.

- Because $C_i$ is tangent to $L$ at $q$ (the tangent cone spans $L$), we have
  $$
  |\psi_j(z')| = o(|z'|) \quad \text{as } z' \to 0, \quad j = d+1, \dots, n.
  $$
  In particular each $\psi_j$ is **bounded** near $0$.

- **Removable singularity / Hartogs extension.**
  - If $d = 1$: each $\psi_j$ is a bounded holomorphic function on a punctured disk, so by the **removable singularity theorem** (Riemann), $\psi_j$ extends holomorphically across $0$.
  - If $d \geq 2$: each $\psi_j$ is a bounded holomorphic function on $B^*_\varepsilon(0) \subset \mathbb{C}^d$, so by the **Hartogs extension theorem**, $\psi_j$ extends holomorphically to $B_\varepsilon(0)$.

  In both cases, $\psi_j$ extends holomorphically to $0$, with $\psi_j(0) = 0$ (from $|\psi_j(z')| = o(|z'|)$).

- Define
  $$
  G(z') := f\bigl(z',\, \psi(z')\bigr), \qquad z' \in B_\varepsilon(0).
  $$
  Then $G$ is holomorphic on $B_\varepsilon(0)$, $G(0) = f(q)$, and
  $$
  |G(z')| = |f(z', \psi(z'))| \leq M = |G(0)| \quad \text{for all } z' \in B_\varepsilon(0).
  $$
  By the **classical maximum modulus principle** on $\mathbb{C}^d$, $G$ is constant on $B_\varepsilon(0)$, so $G \equiv f(q)$. Consequently $f \equiv f(q)$ on $C_i \cap \Omega$.

Since this holds for every branch $C_i$, and combined with Step B1 ($f \equiv f(q)$ on $Z \subset X_{\mathrm{sing}}$), we conclude that $f \equiv f(q)$ on a full neighborhood of $q$ in $X$. Hence $S$ contains a neighborhood of $q$ in $X$.

---

### Conclusion

We have shown $S = \{x \in X : f(x) = f(p)\}$ is both **closed** (by continuity of $f$) and **open** (Cases A and B) in $X$. Since $X$ is **connected** and $S \neq \emptyset$ (it contains $p$), we obtain
$$
S = X.
$$
Therefore $f \equiv f(p)$ on $X$; that is, $f$ is constant on $X$. $\blacksquare$

---

### Key ingredients

| Tool | Role |
|---|---|
| Induction on $\dim X$ | Reduces the singular case to lower-dimensional analytic sets |
| Classical MMP on complex manifolds | Handles regular points directly |
| $\dim X_{\mathrm{sing}} < \dim X$ | Makes the induction hypothesis applicable on the singular locus |
| Tangent cone is a complex cone spanning a $d$-plane | Justifies the graph parametrization tangent to $L$ |
| Removable singularity theorem ($d=1$) / Hartogs theorem ($d \geq 2$) | Extends the graph parametrization across the singular point |
| Classical MMP on $\mathbb{C}^d$ | Forces the composed function $G$ to be constant |

### PROOF COMPLETE
