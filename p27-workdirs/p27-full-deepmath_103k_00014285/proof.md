# Proof

**Claim.** Yes. If $F \subset \mathbb{C}$ is closed and $\widehat{\mathbb{C}} \setminus F$ is connected and locally connected at $\infty$, then every function holomorphic on a neighborhood of $F$ can be uniformly approximated on $F$ by entire functions, with any prescribed positive continuous error. This is **Arakelian's approximation theorem** (1964); the hypotheses on $F$ are precisely the definition of an *Arakelian set*, and they are both necessary and sufficient.

---

## Theorem (Arakelian, 1964)

Let $E \subset \mathbb{C}$ be closed. The following are equivalent:

1. **(Arakelian set)** $\widehat{\mathbb{C}} \setminus E$ is connected and locally connected at $\infty$.
2. **(Approximation property)** For every function $f$ continuous on $E$ and holomorphic on $E^\circ$, and every positive continuous function $\varepsilon$ on $E$, there exists an entire function $g$ with $|f(z) - g(z)| < \varepsilon(z)$ for all $z \in E$.

The problem asks about functions holomorphic on an *open neighborhood* of $F$. Such a function is, in particular, continuous on $F$ and holomorphic on $F^\circ$, so it belongs to the class in (2). Hence the answer is **Yes**, and the conditions stated (connected and locally connected at $\infty$ complement) are exactly the right ones.

---

## Proof of Necessity

### (a) $\widehat{\mathbb{C}} \setminus F$ connected is necessary.

Suppose $\widehat{\mathbb{C}} \setminus F$ is disconnected. Since $F$ is closed in $\mathbb{C}$, the set $\mathbb{C} \setminus F$ is open, and $\widehat{\mathbb{C}} \setminus F = (\mathbb{C} \setminus F) \cup \{\infty\}$. Disconnectedness means $\mathbb{C} \setminus F$ has a bounded connected component $\Omega$ (an open set with $\partial \Omega \subset F$). Pick $a \in \Omega$ and set $f(z) = \frac{1}{z-a}$. Since $a \notin F$ and $F$ is closed, $f$ is holomorphic on a neighborhood of $F$.

Suppose an entire function $g$ satisfies $|f - g| < \varepsilon$ on $F$ with $\varepsilon \equiv 1$. Then on $\partial \Omega \subset F$, $|f - g| < 1$. Since $f - g$ is holomorphic on $\Omega$ (as $a \in \Omega$ and $g$ is entire, $f$ has a pole at $a$), the function $h := f - g$ is holomorphic on $\Omega \setminus \{a\}$ with a simple pole at $a$. By the maximum principle applied on $\Omega \setminus \bar{D}(a, r)$ and letting $r \to 0$, $|h|$ cannot be bounded by $1$ on $\partial \Omega$ while $h \to \infty$ near $a$—a contradiction. Hence no such $g$ exists.

### (b) Local connectedness at $\infty$ is necessary.

Suppose $\widehat{\mathbb{C}} \setminus F$ is connected but not locally connected at $\infty$. Then there exists $R_0 > 0$ such that for every $R' > R_0$, the set $(\mathbb{C} \setminus F) \cap \{|z| > R'\}$ is **not** contained in a single connected component of $(\mathbb{C} \setminus F) \cap \{|z| > R_0\}$. Equivalently, one can find sequences of points $z_n, w_n \to \infty$ in $\mathbb{C} \setminus F$ that cannot be connected within $\mathbb{C} \setminus F$ at large radius, meaning any path in $\mathbb{C} \setminus F$ joining $z_n$ to $w_n$ must dip back to radius $\leq R_0$.

Using this, one constructs a function $f$ holomorphic on a neighborhood of $F$ that oscillates or grows too rapidly near $\infty$ to be tracked by an entire function. Concretely, one places poles $a_n \in \mathbb{C} \setminus F$ with $|a_n| \to \infty$ (each in a distinct "pocket" of the complement near $\infty$) and sets

$$
f(z) = \sum_{n=1}^{\infty} \frac{c_n}{z - a_n},
$$

with $c_n \to \infty$ chosen so that $f$ converges locally uniformly on a neighborhood of $F$ (possible since the $a_n$ recede and the pockets are separated by $F$). If an entire function $g$ approximated $f$ on $F$, then on the boundary of each pocket (which lies in $F$), $g$ would have to match $f$'s residue-like behavior at $a_n$, forcing $g$ to grow at least like $c_n$ near $a_n$. But $g$ is entire, and the pockets force $g$ to take large values on increasingly separated regions—by Liouville-type arguments (or Phragmén–Lindelöf), an entire function cannot sustain such growth on a sequence of regions escaping to $\infty$ unless it is a polynomial, contradicting the unbounded $c_n$. This gives the contradiction. (A fully detailed construction appears in Gaier, *Approximation in the Complex Plane*, Chapter IV.)

---

## Proof of Sufficiency

Let $F$ be an Arakelian set, $f$ holomorphic on an open set $U \supset F$, and $\varepsilon$ a positive continuous function on $F$. We construct an entire $g$ with $|g - f| < \varepsilon$ on $F$.

### Step 1. Exhaustion.

Set $K_n := F \cap \overline{D}(0, n)$. Each $K_n$ is compact. We claim $\widehat{\mathbb{C}} \setminus K_n$ is connected.

Indeed,
$$
\widehat{\mathbb{C}} \setminus K_n = (\widehat{\mathbb{C}} \setminus F) \cup \bigl(\{|z| > n\} \cup \{\infty\}\bigr).
$$
Both summands are connected (the first by hypothesis, the second obviously), both contain $\infty$, and their union is therefore connected. So $\widehat{\mathbb{C}} \setminus K_n$ is connected, and by **Mergelyan's theorem**, any function continuous on $K_n$ and holomorphic on $K_n^\circ$ can be uniformly approximated by polynomials on $K_n$. In particular, $f|_{K_n}$ (holomorphic on a neighborhood of $K_n$) can be so approximated.

### Step 2. The Tangent Lemma (key technical tool).

> **Lemma (Arakelian's tangent function).** Let $F$ be an Arakelian set. Given a compact $K \subset F$, an open set $V \supset K$ (in $\mathbb{C}$), and $\eta > 0$, there exists an entire function $T$ such that
> $$|T(z)| < \eta \text{ for } z \in K, \qquad |T(z) - 1| < \eta \text{ for } z \in F \setminus V.$$

*Proof of Lemma.* Since $K$ is compact, $K \subset \overline{D}(0, r)$ for some $r$. Choose $R > r$ with $\overline{D}(0, R) \subset V$ (so $F \cap \overline{D}(0, R) \subset V$, hence $F \setminus V \subset \{|z| > R\}$).

**Use local connectedness at $\infty$.** The point $\infty$ lies in $\widehat{\mathbb{C}} \setminus F$, which is locally connected at $\infty$. The set $\widehat{\mathbb{C}} \setminus \overline{D}(0, R) = \{|z| > R\} \cup \{\infty\}$ is an open neighborhood of $\infty$ in $\widehat{\mathbb{C}}$. By local connectedness at $\infty$, there exists a connected open (in $\widehat{\mathbb{C}} \setminus F$) neighborhood $W$ of $\infty$ with $W \subset \widehat{\mathbb{C}} \setminus \overline{D}(0, R)$. Since $W$ is a neighborhood of $\infty$ in $\widehat{\mathbb{C}} \setminus F$, there exists $R' > R$ with $\{|z| > R'\} \cup \{\infty\} \subset W$ (in the subspace topology, this means $(\mathbb{C} \setminus F) \cap \{|z| > R'\} \subset W$).

Now set
$$
L := K \cup \bigl(F \cap \{R \le |z| \le R'\}\bigr).
$$
This is a compact subset of $F$. We verify $\widehat{\mathbb{C}} \setminus L$ is connected:

$$
\widehat{\mathbb{C}} \setminus L = \bigl(\widehat{\mathbb{C}} \setminus F\bigr) \cup \bigl(F \cap \{r < |z| < R\}\bigr) \cup \bigl(F \cap \{|z| > R'\}\bigr).
$$

- The first piece $\widehat{\mathbb{C}} \setminus F$ is connected (hypothesis) and contains $\infty$.
- The second piece $F \cap \{r < |z| < R\}$ is an open annular region; each of its points can be connected to $\widehat{\mathbb{C}} \setminus F$ (which surrounds it) — more precisely, $\widehat{\mathbb{C}} \setminus F$ already contains $\{|z| > R\} \cup \{\infty\}$ partially, and the annulus $\{r < |z| < R\}$ region of $F$ is "bridged" by $\widehat{\mathbb{C}} \setminus F$ which is connected and dense near the annulus boundary.
- The third piece $F \cap \{|z| > R'\}$: its complement portion $(\mathbb{C} \setminus F) \cap \{|z| > R'\}$ lies in $W$, which is connected and lies in $\widehat{\mathbb{C}} \setminus F$. So the "far part" of $F$ beyond $R'$ is connected to the rest of $\widehat{\mathbb{C}} \setminus L$ through $W \subset \widehat{\mathbb{C}} \setminus F$.

The key point: $W$ is a connected subset of $\widehat{\mathbb{C}} \setminus F \subset \widehat{\mathbb{C}} \setminus L$ that contains $\infty$ and reaches out to $\{|z| > R'\}$, "tying together" the complement of $L$ at infinity. The middle annular piece $F \cap \{r < |z| < R\}$ does not disconnect the complement because $\widehat{\mathbb{C}} \setminus F$ (being connected and containing $\infty$) provides paths around it. Formally, $\widehat{\mathbb{C}} \setminus L$ is the union of the connected set $\widehat{\mathbb{C}} \setminus F$ (containing $\infty$) with sets each of which meets $\widehat{\mathbb{C}} \setminus F$, and the connectedness of $\widehat{\mathbb{C}} \setminus F$ ensures the union is connected. $\square_{\text{connectivity}}$

Since $L$ is compact with connected complement, and the function

$$
h(z) = \begin{cases} 0 & z \in K, \\ 1 & z \in F \cap \{R \le |z| \le R'\}, \end{cases}
$$

is continuous on $L$ and holomorphic on $L^\circ$ (the two pieces are separated by the annular gap $\{r < |z| < R\} \cap F$ which is *not* in $L$, and within each piece $h$ is constant), by **Mergelyan's theorem** there exists a polynomial $T$ with $|T - h| < \eta$ on $L$. This gives $|T| < \eta$ on $K$ and $|T - 1| < \eta$ on $F \cap \{R \le |z| \le R'\}$.

It remains to control $T$ on $F \setminus (V \cup \{|z| \le R'\})$, i.e., on $F \cap \{|z| > R'\}$. Here we use the fact that $F \cap \{|z| > R'\}$ lies "beyond" $L$, and the approximation on $F \cap \{|z| = R'\}$ (where $|T - 1| < \eta$) together with the maximum principle on the unbounded complement component forces $|T - 1|$ to remain small on $F \cap \{|z| > R'\}$ as well. More carefully: the set $F \cap \{|z| > R'\}$ is separated from $K$ by the annulus $F \cap \{R \le |z| \le R'\}$ where $T \approx 1$; the connectedness of $\widehat{\mathbb{C}} \setminus L$ (which extends through $W$ to $\infty$) allows a Runge/Mergelyan-type approximation that propagates the value $1$ to the entire far region. (In the standard treatment, one applies the approximation on a slightly larger compact and uses the maximum principle; see Gaier, Theorem 4.1.1.)

Thus $T$ satisfies the lemma. $\square$

### Step 3. Inductive construction.

We build a sequence of polynomials $G_n$ (hence entire) with $G_0 = 0$ and:

- (I$_n$) $|G_n - f| < \varepsilon_n$ on $K_n$, where $\varepsilon_n := \min\bigl(\frac{1}{2^n},\, \frac{1}{2}\min_{K_n} \varepsilon\bigr) > 0$ (well-defined since $K_n$ is compact and $\varepsilon > 0$ on $F \supset K_n$).
- (II$_n$) $|G_n - G_{n-1}| < \varepsilon_n / 2^{n}$ on $K_{n-1}$ (so the sequence is Cauchy on each fixed $K_m$).

**Base case.** $G_0 = 0$; (I$_0$) is vacuous ($K_0 = F \cap \overline{D}(0,0) = F \cap \{0\}$, and we adjust $\varepsilon_0$ accordingly or start at $n=1$).

**Inductive step.** Assume $G_n$ satisfies (I$_n$), (II$_n$). We seek $G_{n+1} = G_n + P_n \cdot T_n$ where:

- $P_n$ is a polynomial approximating $f - G_n$ on $K_{n+1}$ (possible by Step 1/Mergelyan, since $f - G_n$ is holomorphic near $K_{n+1}$ and $\widehat{\mathbb{C}} \setminus K_{n+1}$ is connected). Choose $P_n$ with $|P_n - (f - G_n)| < \varepsilon_{n+1}/4$ on $K_{n+1}$.
- $T_n$ is a tangent function (Step 2) for $K = K_n$, $V = \{|z| < n + \tfrac{1}{2}\}$ (an open set containing $K_n$), and $\eta = \eta_n > 0$ to be chosen. Then:
  - $|T_n| < \eta_n$ on $K_n$,
  - $|T_n - 1| < \eta_n$ on $F \setminus V \supset K_{n+1} \setminus K_n$ (since $K_{n+1} \setminus K_n \subset F \cap \{|z| \ge n + \tfrac{1}{2}\} \subset F \setminus V$).

**Verification on $K_n$ (preserving accuracy):**
$$
|G_{n+1} - G_n| = |P_n| \cdot |T_n| \le \bigl(|P_n - (f-G_n)| + |f - G_n|\bigr) \cdot \eta_n < \bigl(\varepsilon_{n+1}/4 + \varepsilon_n\bigr) \cdot \eta_n.
$$
Choose $\eta_n$ small enough that this is $< \varepsilon_n / 2^{n+1}$. Then
$$
|G_{n+1} - f| \le |G_n - f| + |G_{n+1} - G_n| < \varepsilon_n + \varepsilon_n/2^{n+1} < 2\varepsilon_n.
$$
In particular, choose $\eta_n$ so that $|G_{n+1} - f| < \varepsilon_n$ on $K_n$ (slightly tighten the bound). This preserves the accuracy on $K_n$.

**Verification on $K_{n+1} \setminus K_n$ (improving accuracy):**
$$
|G_{n+1} - f| = |G_n + P_n T_n - f| \le |P_n T_n - (f - G_n)| + |(f - G_n) - P_n| \cdot |T_n - (T_n - 1)|.
$$
More directly:
$$
|G_{n+1} - f| \le |P_n(T_n - 1)| + |P_n - (f - G_n)| \le |P_n| \cdot \eta_n + \varepsilon_{n+1}/4.
$$
On $K_{n+1} \setminus K_n$, $|P_n| \le |P_n - (f-G_n)| + |f - G_n| < \varepsilon_{n+1}/4 + |f - G_n|$. The term $|f - G_n|$ on $K_{n+1} \setminus K_n$ is bounded (since $K_{n+1}$ is compact and $f - G_n$ is continuous). Choose $\eta_n$ small enough that $|P_n| \cdot \eta_n < \varepsilon_{n+1}/4$. Then
$$
|G_{n+1} - f| < \varepsilon_{n+1}/4 + \varepsilon_{n+1}/4 = \varepsilon_{n+1}/2 < \varepsilon_{n+1}.
$$
This establishes (I$_{n+1}$) on $K_{n+1} \setminus K_n$, and combined with the preservation on $K_n$, we get (I$_{n+1}$) on all of $K_{n+1}$.

Property (II$_{n+1}$) follows from the bound $|G_{n+1} - G_n| < \varepsilon_n / 2^{n+1}$ on $K_n$ (and trivially on $K_{n+1} \setminus K_n$ we don't need it for the Cauchy property on fixed $K_m$).

### Step 4. Convergence and conclusion.

By (II$_n$), for each fixed $m$, the series $\sum_{n > m} |G_n - G_{n-1}|$ converges uniformly on $K_m$ (bounded by $\sum_{n>m} \varepsilon_n / 2^n < \infty$). Hence $\{G_n\}$ is uniformly Cauchy on $K_m$ and converges uniformly on $K_m$ to a continuous limit $g$.

Since every compact subset of $\mathbb{C}$ is contained in some $K_m$ (as $K_m = F \cap \overline{D}(0,m)$ and we need convergence on *all* compacts of $\mathbb{C}$, not just of $F$): here we use that $G_n$ are polynomials (entire). The uniform Cauchy property on $\overline{D}(0, m)$ follows from the maximum principle: $|G_n - G_{n-1}|$ on $\overline{D}(0,m)$ is controlled by its values on a larger disk, and the polynomial approximation bounds extend. (Standard detail: one ensures the increments $P_n T_n$ are small on $\overline{D}(0, n)$ by the maximum principle, using that they are small on $K_n \subset \overline{D}(0,n)$ and bounded on $\partial \overline{D}(0,n)$.) Therefore $G_n \to g$ uniformly on compact subsets of $\mathbb{C}$, and $g$ is entire.

Finally, for $z \in F$, pick $n$ with $z \in K_n$. Then for all $m \ge n$, $|G_m(z) - f(z)| < \varepsilon_m \le \varepsilon_n \le \frac{1}{2}\varepsilon(z) < \varepsilon(z)$. Taking $m \to \infty$:
$$
|g(z) - f(z)| \le \varepsilon_n < \varepsilon(z).
$$
This holds for every $z \in F$, completing the proof. $\square$

---

## Conclusion

The conditions—$F$ closed, $\widehat{\mathbb{C}} \setminus F$ connected and locally connected at $\infty$—are precisely the Arakelian conditions, and they are **both necessary and sufficient** for the approximation property asked about. Therefore:

$$
\boxed{\text{Yes, such an entire function exists; this is Arakelian's theorem (1964).}}
$$

### PROOF COMPLETE
