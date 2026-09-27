# Proof: Generic Orbit Closure Dimension is $n - d$

## Answer

$$\boxed{\text{Yes}}$$

The dimension of the Zariski closure of the $G$-orbit is generically $n - d$.

---

## Setup and Notation

Let $K = \mathbb{C}(x_1, \ldots, x_n)$ where $x_1, \ldots, x_n$ are algebraically independent over $\mathbb{C}$. Let $G = \langle \sigma \rangle \cong \mathbb{Z}$ be a group of $\mathbb{C}$-automorphisms of $K$. The invariant field $K^G$ has $\operatorname{trdeg}(K^G / \mathbb{C}) = d$.

By the transcendence degree relation:
$$n = \operatorname{trdeg}(K/\mathbb{C}) = \operatorname{trdeg}(K^G/\mathbb{C}) + \operatorname{trdeg}(K/K^G) = d + \operatorname{trdeg}(K/K^G),$$
so $\operatorname{trdeg}(K/K^G) = n - d$.

The automorphism $\sigma$ sends each $x_i$ to a rational function $\sigma(x_i) \in K$, inducing a birational map $\Phi: \mathbb{A}^n \dashrightarrow \mathbb{A}^n$. For $a \in \mathbb{C}^n$ outside the indeterminacy locus, $\Phi(a) = (\sigma(x_1)(a), \ldots, \sigma(x_n)(a)) \in \mathbb{C}^n$.

For $a \in \mathbb{C}^n$, the $G$-orbit is $\mathcal{O}(a) = \{\Phi^k(a) : k \in \mathbb{Z}\}$ (when defined), and $V_a = \overline{\mathcal{O}(a)}^{\,\mathrm{Zar}}$ is its Zariski closure.

**Well-definedness of the orbit.** For each $k \in \mathbb{Z}$, the indeterminacy locus of $\Phi^k$ is a proper Zariski closed subset of $\mathbb{A}^n$ (since $\Phi$ is dominant). The union $\bigcup_{k \in \mathbb{Z}} \mathrm{Indet}(\Phi^k)$ is a countable union of proper closed subsets. By the Baire category theorem (applied to $\mathbb{C}^n$ with the usual topology, where proper Zariski closed sets are nowhere dense), this union is meager. Hence for a generic (comeager, in particular Zariski dense) set of $a$, the entire orbit $\mathcal{O}(a)$ is well-defined.

---

## Upper Bound: $\dim V_a \leq n - d$

Choose $d$ algebraically independent elements $f_1, \ldots, f_d \in K^G$ (a transcendence basis of $K^G$ over $\mathbb{C}$). Each $f_i$ is a rational function on $\mathbb{A}^n$, invariant under $G$.

For any $a \in \mathbb{C}^n$ and any $g \in G$:
$$f_i(g(a)) = g(f_i)(a) = f_i(a),$$
since $f_i$ is $G$-invariant. Therefore the entire orbit $\mathcal{O}(a)$ lies in the subvariety
$$W_a = V(f_1 - f_1(a), \, \ldots, \, f_d - f_d(a)) \subseteq \mathbb{A}^n.$$

Since $f_1, \ldots, f_d$ are algebraically independent, for generic $a$ the fiber $W_a$ has dimension $n - d$ (the generic fiber of the rational map $\pi = (f_1, \ldots, f_d): \mathbb{A}^n \dashrightarrow \mathbb{A}^d$ has the expected dimension). Thus:
$$\dim V_a \leq \dim W_a = n - d. \qquad \checkmark$$

---

## Lower Bound: $\dim V_a \geq n - d$

This is the substantive part. We must show that for generic $a$, the orbit is Zariski dense in $W_a$, i.e., $V_a = W_a$.

### Step 1: The Generic Orbit is Zariski Dense in the Generic Fiber

Let $F = \mathbb{C}(f_1, \ldots, f_d) \subseteq K^G$, so $F$ is a purely transcendental extension of $\mathbb{C}$ of degree $d$, and $K^G$ is algebraic over $F$.

The **generic fiber** $W_\eta$ is the variety over $F$ defined by $f_i = t_i$ (where $t_i$ are the indeterminates of $F$). Its function field over $F$ is $K$ (with $f_i$ identified with $t_i$), and $\dim W_\eta = n - d$.

The map $\Phi$ preserves the fibers of $\pi$ (since $\pi \circ \Phi = \pi$), so $\Phi$ restricts to a birational self-map $\phi: W_\eta \dashrightarrow W_\eta$ over $F$.

**Claim.** The orbit of the generic point of $W_\eta$ is Zariski dense in $W_\eta$ over $F$.

**Proof of Claim.** A closed subset of $W_\eta$ defined over $F$ is cut out by polynomials with coefficients in $F \subseteq K^G$. Let $P \in F[T_1, \ldots, T_n]$ vanish on the generic orbit, i.e., $P(\sigma^k(x)) = 0$ in $K$ for all $k \in \mathbb{Z}$.

Since the coefficients of $P$ lie in $F \subseteq K^G$ (fixed by $\sigma$):
$$P(\sigma^k(x)) = \sum_\alpha c_\alpha \, \sigma^k(x)^\alpha = \sigma^k\!\left(\sum_\alpha c_\alpha \, x^\alpha\right) = \sigma^k(P(x)).$$

So $P(\sigma^k(x)) = 0$ for all $k$ iff $\sigma^k(P(x)) = 0$ for all $k$, iff $P(x) = 0$ in $K$ (since $\sigma$ is an automorphism, $\sigma^k$ is injective).

Now, $P(x) = 0$ in $K$ means $P$ vanishes at the generic point of $W_\eta$, i.e., $P$ is in the ideal of $W_\eta$ in $F[T]$. In other words, $P$ vanishes on all of $W_\eta$.

Therefore, any polynomial over $F$ vanishing on the generic orbit vanishes on all of $W_\eta$. This means the generic orbit is Zariski dense in $W_\eta$ over $F$. $\quad \square$

**Key observation.** The above argument works because the coefficients of $P$ are in $F \subseteq K^G$ (fixed by $\sigma$), allowing us to pull $\sigma^k$ out. This is why we work over $F$ rather than over $K^G$ or $K$.

### Step 2: Specialization to Closed Points

We now transfer the generic density result to specific closed points $a \in \mathbb{C}^n$.

For a polynomial $P \in \mathbb{C}[T_1, \ldots, T_n]$ and $a \in \mathbb{C}^n$, we say $P$ is **non-trivial on $W_a$** if $P|_{W_a} \not\equiv 0$, i.e., $P \notin (f_1 - f_1(a), \ldots, f_d - f_d(a))$.

The orbit $\mathcal{O}(a)$ is Zariski dense in $W_a$ iff there is no $P \in \mathbb{C}[T] \setminus \{0\}$ that is non-trivial on $W_a$ and vanishes on $\mathcal{O}(a)$.

**Define the bad set.** For each degree bound $D \geq 1$ and each $N \geq 0$, let:
$$S_{D,N} = \left\{a \in \mathbb{A}^n : \exists\, P \in \mathbb{C}[T_1, \ldots, T_n]_{\leq D} \setminus \{0\},\; P|_{W_a} \not\equiv 0,\; P(\Phi^k(a)) = 0 \text{ for } k = 0, 1, \ldots, N \right\}.$$

This is a constructible subset of $\mathbb{A}^n$ (it is the projection of an incidence variety defined by algebraic conditions).

**The generic point is not in $S_{D,N}$.** We show $\eta \notin S_{D,N}$ for all $D, N$.

Recall that $P|_{W_\eta} \not\equiv 0$ for any $P \in \mathbb{C}[T] \setminus \{0\}$, because $(f_i - t_i) \cap \mathbb{C}[T] = \{0\}$ (a polynomial with $\mathbb{C}$-coefficients vanishing on the generic fiber $W_\eta$ must vanish on all of $\mathbb{A}^n$, hence is zero).

Now, if $P \in \mathbb{C}[T] \setminus \{0\}$, then $P(x) \neq 0$ in $K$ (since $x_i$ are algebraically independent over $\mathbb{C}$). Since $\sigma$ is a field automorphism:
$$P(\Phi^k(\eta)) = P(\sigma^k(x)) = \sigma^k(P(x)) \neq 0 \quad \text{for all } k.$$

So no non-zero $P \in \mathbb{C}[T]$ vanishes on even a single point of the generic orbit, let alone the first $N+1$ points. Hence $\eta \notin S_{D,N}$.

**$S_{D,N}$ is contained in a proper closed subset.** Since $S_{D,N}$ is constructible and does not contain the generic point of $\mathbb{A}^n$, it cannot contain any non-empty Zariski open set (any non-empty open set in an irreducible space contains the generic point). Therefore $S_{D,N}$ is contained in a proper Zariski closed subset of $\mathbb{A}^n$.

**Stabilization by Noetherianity.** For fixed $D$, the sets $S_{D,N}$ are descending in $N$ (more vanishing conditions = smaller set). Their closures $\overline{S_{D,N}}$ form a descending chain of closed subsets:
$$\overline{S_{D,0}} \supseteq \overline{S_{D,1}} \supseteq \overline{S_{D,2}} \supseteq \cdots$$

By the Noetherian property of $\mathbb{A}^n$, this chain stabilizes: there exists $N_0(D)$ such that $\overline{S_{D,N}} = \overline{S_{D,N_0(D)}}$ for all $N \geq N_0(D)$.

Define $S_D = \bigcap_{N \geq 0} S_{D,N}$ (the set of $a$ where some degree-$\leq D$ polynomial, non-trivial on $W_a$, vanishes on the **entire** orbit). Then:
$$S_D \subseteq S_{D,N_0(D)} \subseteq \overline{S_{D,N_0(D)}} \subsetneq \mathbb{A}^n.$$

So $S_D$ is contained in a proper closed subset for each $D$.

**Baire category argument.** The total bad set is:
$$\mathcal{B} = \bigcup_{D=1}^{\infty} S_D \subseteq \bigcup_{D=1}^{\infty} \overline{S_{D,N_0(D)}}.$$

This is a countable union of proper Zariski closed subsets of $\mathbb{A}^n(\mathbb{C})$. Each proper Zariski closed set is nowhere dense in the usual (Euclidean) topology on $\mathbb{C}^n$. By the Baire category theorem, $\mathcal{B} \neq \mathbb{C}^n$; in fact, $\mathbb{C}^n \setminus \mathcal{B}$ is comeager (and in particular Zariski dense).

### Step 3: Conclusion of the Lower Bound

For $a \in \mathbb{C}^n \setminus \mathcal{B}$ (a generic point), no polynomial $P \in \mathbb{C}[T] \setminus \{0\}$ that is non-trivial on $W_a$ vanishes on the entire orbit $\mathcal{O}(a)$. Therefore:
$$I(\mathcal{O}(a)) \subseteq (f_1 - f_1(a), \ldots, f_d - f_d(a)),$$
which gives $V_a = V(I(\mathcal{O}(a))) \supseteq W_a$. Combined with the upper bound $V_a \subseteq W_a$:
$$V_a = W_a, \qquad \dim V_a = \dim W_a = n - d.$$

---

## Final Answer

For a generic point $a \in \mathbb{C}^n$ (outside a countable union of proper Zariski closed subsets), the $G$-orbit $\{g(a)\}_{g \in G}$ is well-defined, contained in the fiber $W_a$ of dimension $n - d$, and Zariski dense in $W_a$. Therefore:

$$\dim \overline{\{g(a)\}_{g \in G}}^{\,\mathrm{Zar}} = n - d \quad \text{generically.}$$

$$\boxed{\text{Yes}}$$

### PROOF COMPLETE
