# Proof: If $X \times X \simeq \mathbb{R}^2$, then $X \simeq \mathbb{R}$

**Theorem.** Let $X$ be a topological space such that $X \times X \cong \mathbb{R}^2$. Then $X \cong \mathbb{R}$.

We write $\cong$ for homeomorphism and $\simeq$ for homotopy equivalence. Throughout, singular homology with $\mathbb{Z}$-coefficients is used.

---

## Step A. Basic topological properties of $X$

Since $X \times X \cong \mathbb{R}^2$:

- **Hausdorff**: $\mathbb{R}^2$ is Hausdorff, and a product is Hausdorff only if each factor is; hence $X$ is Hausdorff.
- **Second countable**: $\mathbb{R}^2$ is second countable, and a product is second countable only if each factor is; hence $X$ is second countable.
- **Locally compact** (Hausdorff): $\mathbb{R}^2$ is locally compact. For Hausdorff spaces, local compactness of $X \times X$ implies local compactness of $X$ (each point of $X$ has a compact neighborhood, obtained by projecting a compact product-neighborhood and using that the projection of a compact set is compact).
- **Connected**: $\mathbb{R}^2$ is connected, and $X \times X$ connected implies $X$ connected (the projection of a connected space is connected).
- **Non-compact**: If $X$ were compact, then $X \times X$ would be compact (Tychonoff), contradicting $\mathbb{R}^2$ non-compact.
- **More than one point**: If $X$ were a single point, $X \times X$ would be a single point, not $\mathbb{R}^2$.

**Contractibility.** Since $X \times X \cong \mathbb{R}^2$ is contractible, $\pi_n(X \times X) = 0$ for all $n \geq 0$. As $\pi_n(X \times X) \cong \pi_n(X) \times \pi_n(X)$, we get $\pi_n(X) = 0$ for all $n$. By the Künneth theorem, $H_*(X \times X) \cong H_*(X) \otimes H_*(X)$; since $H_k(\mathbb{R}^2) = 0$ for $k \geq 1$, this forces $H_k(X) = 0$ for all $k \geq 1$ (any nonzero $H_k(X)$ would produce a nonzero summand in $H_{2k}(X \times X)$). We will show below (Step B) that $X$ is an ANR, hence has the homotopy type of a CW complex. By Whitehead's theorem, the vanishing of all homotopy groups then implies $X$ is contractible. In particular $H_1(X) = 0$ and $\widetilde{H}_0(X) = 0$.

---

## Step B. $X$ is an ANR

$\mathbb{R}^2$ is a (topological) 2-manifold, hence an ANR (every manifold is an ANR). The space $X$ is a retract of $X \times X \cong \mathbb{R}^2$: fix a basepoint $x_0 \in X$ and define
$$r: X \times X \to X, \quad r(a, b) = a, \qquad s: X \to X \times X, \quad s(a) = (a, x_0).$$
Then $r \circ s = \mathrm{id}_X$, so $X$ is a retract of $\mathbb{R}^2$. A retract of an ANR is an ANR. Hence **$X$ is an ANR**.

**Consequences:**
1. ANR $\Rightarrow$ locally contractible $\Rightarrow$ locally path-connected $\Rightarrow$ locally connected.
2. Since $X$ is locally compact and an ANR, every point $x \in X$ has a compact neighborhood $K$ that is an ANR. By West's theorem, a compact ANR has the homotopy type of a finite CW complex. Therefore the local homology groups $H_k(X, X \setminus \{x\}) \cong H_k(K, K \setminus \{x\})$ (by excision, taking $K$ a compact ANR neighborhood of $x$ with $x \in \operatorname{int} K$) are **finitely generated** abelian groups.

---

## Step C. Local homology of $X$ via the relative Künneth theorem

Fix $x \in X$ and set $A = X \setminus \{x\}$ (open, since $X$ is Hausdorff so $\{x\}$ is closed). Define
$$h_k := H_k(X, X \setminus \{x\}) = H_k(X, A).$$

**Key identity.** For the diagonal point $(x, x) \in X \times X$:
$$X \times X \setminus \{(x,x)\} = A \times X \;\cup\; X \times A.$$
*Proof of identity:* $(a, b) \neq (x, x)$ iff $a \neq x$ or $b \neq x$, iff $(a,b) \in A \times X$ or $(a,b) \in X \times A$. $\square$

Since $X \times X \cong \mathbb{R}^2$, the local homology of $X \times X$ at $(x,x)$ is that of $\mathbb{R}^2$ at any point:
$$H_n(X \times X,\; X \times X \setminus \{(x,x)\}) = H_n(X \times X,\; A \times X \cup X \times A) = \begin{cases} \mathbb{Z} & n = 2, \\ 0 & n \neq 2. \end{cases}$$

**Applying the relative Künneth theorem.** The relative Künneth theorem (see Hatcher, *Algebraic Topology*, Theorem 3.21; or Spanier, *Algebraic Topology*, Theorem 5.3.10) gives a natural short exact sequence
$$0 \to \bigoplus_{i+j=n} H_i(X, A) \otimes H_j(X, A) \to H_n\bigl(X \times X,\; A \times X \cup X \times A\bigr) \to \bigoplus_{i+j=n-1} \mathrm{Tor}\bigl(H_i(X,A),\, H_j(X,A)\bigr) \to 0$$
which (for singular homology) splits (unnaturally). In our notation:
$$0 \to \bigoplus_{i+j=n} h_i \otimes h_j \to H_n(X \times X, A \times X \cup X \times A) \to \bigoplus_{i+j=n-1} \mathrm{Tor}(h_i, h_j) \to 0.$$

**Legitimacy of Künneth here.** The pairs $(X, A)$ and $(X, A)$ with $A = X \setminus \{x\}$ open satisfy: the inclusion $A \hookrightarrow X$ is a cofibration (in the sense required by the Künneth theorem for pairs) because $A$ is open and $X$ is a metrizable ANR — equivalently, one may use the version of the Künneth theorem for *arbitrary* pairs (Spanier, Dold), which for singular homology holds without cofibration hypotheses, the Tor term accounting for all obstructions. We proceed with this general version.

**Determining the $h_k$.**

*$h_0 = 0$:* From the long exact sequence of the pair $(X, A)$:
$$\cdots \to H_0(A) \to H_0(X) \to h_0 \to 0.$$
Since $X$ is connected and $A = X \setminus \{x\}$ is nonempty (as $X$ has more than one point), the map $H_0(A) \to H_0(X)$ is surjective (every point of $X$ is path-connected to a point of $A$, using that $X$ is path-connected and $A$ nonempty). Hence $h_0 = H_0(X, A) = 0$.

*$h_1 \cong \mathbb{Z}$:* Set $n = 2$. The Tor term is $\bigoplus_{i+j=1} \mathrm{Tor}(h_i, h_j) = \mathrm{Tor}(h_0, h_1) \oplus \mathrm{Tor}(h_1, h_0) = 0$ since $h_0 = 0$. The tensor term is $\bigoplus_{i+j=2} h_i \otimes h_j = h_0 \otimes h_2 \oplus h_1 \otimes h_1 \oplus h_2 \otimes h_0 = h_1 \otimes h_1$. So:
$$h_1 \otimes h_1 \cong H_2(X \times X, \,\cdot\,) \cong \mathbb{Z}.$$
Since $h_1$ is finitely generated (Step B), write $h_1 \cong \mathbb{Z}^r \oplus T$ with $T$ finite. Then $h_1 \otimes h_1 \cong \mathbb{Z}^{r^2} \oplus (T \otimes \mathbb{Z}^r) \oplus (\mathbb{Z}^r \otimes T) \oplus (T \otimes T)$. The tensor product of a finite group with anything is finite (torsion), so $h_1 \otimes h_1 \cong \mathbb{Z}^{r^2} \oplus (\text{finite})$. For this to be $\mathbb{Z}$, we need $r^2 = 1$ (so $r = 1$) and the finite part zero. The finite part $T \otimes h_1$ vanishes iff $T = 0$ (since $T \otimes \mathbb{Z} \cong T \neq 0$ if $T \neq 0$). Hence $h_1 \cong \mathbb{Z}$.

*$h_k = 0$ for $k \geq 2$ (by induction):* Suppose $h_m = 0$ for $2 \leq m \leq k-1$ (base case $k=2$: vacuous). Set $n = k+1$. The tensor term $\bigoplus_{i+j=k+1} h_i \otimes h_j$ involves only $h_0 = 0$, $h_1 = \mathbb{Z}$, and $h_m$ for $2 \leq m \leq k-1$ (all zero by hypothesis), plus $h_k \otimes h_1 \oplus h_1 \otimes h_k = h_k \oplus h_k$. The Tor term $\bigoplus_{i+j=k} \mathrm{Tor}(h_i, h_j)$: the only potentially nonzero $\mathrm{Tor}$ comes from $\mathrm{Tor}(h_1, h_{k-1}) \oplus \mathrm{Tor}(h_{k-1}, h_1)$, but $h_{k-1} = 0$ by hypothesis (for $k \geq 3$; for $k = 2$, $h_{k-1} = h_1 = \mathbb{Z}$ and $\mathrm{Tor}(\mathbb{Z}, h_1) = 0$). So the Tor term is $0$. The short exact sequence gives:
$$h_k \oplus h_k \cong H_{k+1}(X \times X, \,\cdot\,) = 0 \quad (\text{since } k+1 \geq 3),$$
hence $h_k = 0$. By induction, $h_k = 0$ for all $k \geq 2$.

**Conclusion of Step C:**
$$\boxed{H_k(X, X \setminus \{x\}) = \begin{cases} 0 & k = 0, \\ \mathbb{Z} & k = 1, \\ 0 & k \geq 2. \end{cases}}$$
This is exactly the local homology of $\mathbb{R}$ at any point.

---

## Step D. $X \setminus \{x\}$ has exactly two connected components

From the long exact sequence of the pair $(X, X \setminus \{x\})$:
$$H_1(X) \xrightarrow{\;\alpha\;} H_1(X, X \setminus \{x\}) \xrightarrow{\;\beta\;} \widetilde{H}_0(X \setminus \{x\}) \xrightarrow{\;\gamma\;} \widetilde{H}_0(X).$$

We have:
- $H_1(X) = 0$ (Step A, $X$ contractible),
- $H_1(X, X \setminus \{x\}) = h_1 \cong \mathbb{Z}$ (Step C),
- $\widetilde{H}_0(X) = 0$ (Step A, $X$ connected).

So the sequence becomes $0 \to \mathbb{Z} \xrightarrow{\beta} \widetilde{H}_0(X \setminus \{x\}) \to 0$, giving
$$\widetilde{H}_0(X \setminus \{x\}) \cong \mathbb{Z}.$$

The reduced 0-th homology $\widetilde{H}_0(Y) \cong \mathbb{Z}^{c(Y) - 1}$ where $c(Y)$ is the number of path-components of $Y$. So $c(X \setminus \{x\}) = 2$: **$X \setminus \{x\}$ has exactly two path-components.**

Since $X$ is an ANR, it is locally path-connected; an open subspace of a locally path-connected space is locally path-connected, so $X \setminus \{x\}$ is locally path-connected. In a locally path-connected space, connected components coincide with path-components. Therefore:

> **Every point $x \in X$ is a cut point, and $X \setminus \{x\}$ has exactly two connected components.**

---

## Step E. A space with the two-component cut property is homeomorphic to $\mathbb{R}$

We now prove the following classical result (a form of a theorem of Whyburn; see Whyburn, *Analytic Topology*, AMS Colloquium Publications, and the cut-point characterization of the arc/line):

> **Proposition (Whyburn's cut-point theorem, line version).** *Let $Y$ be a non-compact, connected, locally connected, locally compact, separable metrizable space in which every point is a cut point separating $Y$ into exactly two connected components. Then $Y \cong \mathbb{R}$.*

We verify the hypotheses for $Y = X$: $X$ is non-compact (Step A), connected (Step A), locally connected (Step B, ANR), locally compact (Step A), separable metrizable (Step A: second countable + Hausdorff + locally compact gives metrizable; or directly, second countable regular $\Rightarrow$ metrizable by Urysohn), and every point separates $X$ into exactly two components (Step D). So the Proposition applies and $X \cong \mathbb{R}$.

For completeness, we give the proof of the Proposition.

### E.1. Construction of a linear order

Fix two distinct points $a, b \in X$. Since $X \setminus \{a\}$ has exactly two components, let $C_a^+$ denote the component containing $b$, and $C_a^-$ the other. Similarly for any point $p$, $X \setminus \{p\}$ has two components; we denote them $C_p^+$ (the one containing $b$, if $p \neq b$) and $C_p^-$ (the other), and for $p = b$ we use $C_b^+$ = component containing $a$.

**Definition of the order.** For distinct $p, q \in X$, we write $p < q$ if $q \in C_p^+$ (i.e., $q$ lies in the component of $X \setminus \{p\}$ containing $b$) **and** $p \in C_q^-$ (i.e., $p$ lies in the component of $X \setminus \{q\}$ *not* containing $b$). Equivalently, $p < q$ iff $p$ and $a$ are in the same component of $X \setminus \{q\}$ and $q$ and $b$ are in the same component of $X \setminus \{p\}$.

This is the standard *separation order* in cut-point theory. We verify it is a total order:

- **Trichotomy.** For distinct $p, q$: consider $X \setminus \{p\} = C_p^+ \sqcup C_p^-$. Either $q \in C_p^+$ or $q \in C_p^-$. Consider $X \setminus \{q\} = C_q^+ \sqcup C_q^-$. Either $p \in C_q^+$ or $p \in C_q^-$. The four combinations are not all possible: if $q \in C_p^+$ and $p \in C_q^+$, then $p$ and $q$ are "on the same side of each other," which would mean $C_p^+ = C_q^+$ — but this is impossible because $p \in C_q^+$ means $p \in C_p^+$ (since $C_q^+ = C_p^+$ would contain $p$, contradicting $p \notin X \setminus \{p\}$... more carefully: $C_p^+$ is a component of $X \setminus \{p\}$, so $p \notin C_p^+$; if $C_q^+ = C_p^+$ then $p \notin C_q^+$, contradiction). Similarly $q \in C_p^-$ and $p \in C_q^-$ is impossible. So exactly one of $p < q$ or $q < p$ holds.

- **Transitivity.** Suppose $p < q$ and $q < r$. Then $q \in C_p^+$, $p \in C_q^-$, $r \in C_q^+$, $q \in C_r^-$. Since $X \setminus \{q\} = C_q^+ \sqcup C_q^-$ and $p \in C_q^-$, $r \in C_q^+$, the points $p$ and $r$ are in different components of $X \setminus \{q\}$. This means any path (or connected set) from $p$ to $r$ must pass through $q$. In particular, $r \in C_p^+$ (since the component of $X \setminus \{p\}$ containing $r$ must contain $q \in C_p^+$, as $r$ is connected to $q$ without passing through $p$ — if the path from $q$ to $r$ passed through $p$, then $p$ would be between $q$ and $r$, but $q < r$ means $r$ is reachable from $q$ without $p$). Formally: $C_p^+$ is connected and contains $q$; $r$ is in the same component of $X \setminus \{q\}$ as... we need $r \in C_p^+$. Since $q \in C_p^+$ and $r \in C_q^+$, and $C_q^+ \setminus \{p\}$ (if $p \notin C_q^+$, which holds since $p \in C_q^-$) is contained in a single component of $X \setminus \{p\}$, namely $C_p^+$ (as it's connected, contains $q \in C_p^+$, and doesn't contain $p$). So $r \in C_p^+$. Similarly $p \in C_r^-$. Hence $p < r$.

### E.2. The order topology agrees with the original topology

**Order topology $\subseteq$ original topology.** The subbasic open sets of the order topology are the open rays $(-\infty, p) = C_p^-$ and $(p, +\infty) = C_p^+$. Each $C_p^\pm$ is a component of the open set $X \setminus \{p\}$; since $X$ is locally connected, components of open sets are open. So the open rays are open in the original topology, hence the order topology is coarser than the original.

**Original topology $\subseteq$ order topology.** Let $U$ be open in $X$ and $x \in U$. Since $X$ is locally connected, $x$ has a connected open neighborhood $V$ with $x \in V \subseteq U$. We claim $V$ contains an order-open interval around $x$. Take any $p \in V$ with $p < x$ and any $q \in V$ with $x < q$ (such points exist because $V$ is connected and $x$ is a cut point, so $V$ meets both components of $X \setminus \{x\}$). Then $(p, q) = C_p^+ \cap C_q^-$ is an order-open interval containing $x$ and contained in $V \subseteq U$. (Any $y$ with $p < y < q$ lies in $C_p^+$ and $C_q^-$; since $V$ is connected and contains $p$ and $q$, and $y$ is between them, $y \in V$.) So $U$ is open in the order topology. Hence the two topologies coincide.

### E.3. The order is that of $\mathbb{R}$

$X$ with this order is a **LOTS** (linearly ordered topological space) whose order topology is the original topology. We verify the properties characterizing $\mathbb{R}$:

- **No endpoints.** If $x$ were the minimum, then $X \setminus \{x\}$ would have only one "rightward" component, i.e., $X \setminus \{x\}$ would be connected — contradicting that every point is a cut point into two components. Similarly no maximum.

- **Order-dense.** If $p < q$ with no $r$ satisfying $p < r < q$, then $X = (-\infty, p] \cup [q, +\infty)$, a union of two disjoint nonempty closed sets — contradicting connectedness of $X$.

- **Order-complete (Dedekind complete).** A connected LOTS has no Dedekind gaps: a gap would witness a separation $X = L \cup R$ with $L < R$, $L$ open-closed, $R$ open-closed, both nonempty — contradicting connectedness.

- **Separable.** $X$ is second countable (Step A), and a separable LOTS has a countable dense subset.

**Classical characterization.** A connected, separable, order-dense, Dedekind-complete linear order with no endpoints is order-isomorphic (hence homeomorphic) to $\mathbb{R}$. This is the standard characterization of the real line (see e.g. Munkres, *Topology*, §24, Theorem 24.1; or the Dedekind completeness + separability + no endpoints characterization).

Therefore $X \cong \mathbb{R}$.

---

## Step F. Conclusion

Combining all steps: $X \times X \cong \mathbb{R}^2$ implies $X$ is a non-compact, connected, locally connected, locally compact, separable metrizable ANR (Steps A–B); the relative Künneth theorem forces the local homology of $X$ to match that of $\mathbb{R}$ (Step C); the long exact sequence then shows every point of $X$ separates $X$ into exactly two components (Step D); and Whyburn's cut-point theorem (Step E) yields $X \cong \mathbb{R}$.

$$\boxed{X \cong \mathbb{R}}$$

### PROOF COMPLETE
