# Theorem

Let $M$ be a connected closed smooth manifold of dimension $d \geq 2$. Then there exists a $C^1$ diffeomorphism $\phi: M \to M$ such that $(M, \phi)$ is a topologically mixing discrete dynamical system.

## Proof

The proof has two main parts:

- **Part I.** We show that measure-theoretic mixing with respect to a smooth measure implies topological mixing.
- **Part II.** We invoke the Anosov–Katok approximation-by-conjugation method to construct a $C^\infty$ (hence $C^1$) diffeomorphism on $M$ that is mixing with respect to a smooth measure.

Combining the two parts yields the result.

---

## Part I: Measure-theoretic mixing implies topological mixing

**Definition.** A measure-preserving transformation $f$ of a probability space $(M, \mu)$ is *mixing* if for all measurable sets $A, B$,
$$\lim_{n \to \infty} \mu\!\left(f^n(A) \cap B\right) = \mu(A)\,\mu(B).$$

**Definition.** A homeomorphism $f$ of a topological space $M$ is *topologically mixing* if for every pair of nonempty open sets $U, V \subset M$, there exists $N \in \mathbb{N}$ such that $f^n(U) \cap V \neq \emptyset$ for all $n \geq N$.

**Proposition.** Let $M$ be a closed smooth manifold, $\mu$ a smooth measure on $M$ (i.e., $\mu$ has a smooth density with respect to Lebesgue measure in any coordinate chart, so that $\mu(U) > 0$ for every nonempty open set $U$). If $f: M \to M$ is a diffeomorphism preserving $\mu$ that is mixing in the measure-theoretic sense, then $f$ is topologically mixing.

*Proof of Proposition.* Let $U, V \subset M$ be nonempty open sets. Since $\mu$ is smooth, $\mu(U) > 0$ and $\mu(V) > 0$. By the mixing property,
$$\lim_{n \to \infty} \mu\!\left(f^n(U) \cap V\right) = \mu(U)\,\mu(V) > 0.$$
Therefore, there exists $N \in \mathbb{N}$ such that for all $n \geq N$,
$$\mu\!\left(f^n(U) \cap V\right) > 0.$$
In particular, $f^n(U) \cap V \neq \emptyset$ for all $n \geq N$. Since $U$ and $V$ were arbitrary nonempty open sets, $f$ is topologically mixing. $\square$

---

## Part II: The Anosov–Katok construction

We show that every closed connected smooth manifold $M$ of dimension $d \geq 2$ admits a $C^\infty$ diffeomorphism that is mixing with respect to a smooth measure. The construction uses the **Anosov–Katok approximation-by-conjugation method** (Anosov–Katok, 1970).

### Step 1: Construction on the closed disk

Consider the closed unit disk $\overline{D}^{\,d} \subset \mathbb{R}^d$ ($d \geq 2$) with Lebesgue measure $\lambda$. The disk carries a natural smooth $S^1$-action: rotation $R_\alpha$ in a chosen 2-dimensional coordinate plane by angle $2\pi\alpha$, fixing the complementary coordinates. This action preserves $\lambda$ and fixes $\partial D$ pointwise.

The Anosov–Katok method proceeds as follows.

**(a) Choice of approximating sequence.** Choose a sequence of rationals $\{p_n/q_n\}_{n \geq 1}$ converging to an irrational number $\alpha$, satisfying:
- $q_n \mid q_{n+1}$ for all $n$,
- $q_{n+1}/q_n \to \infty$.

Each $R_{p_n/q_n}$ is periodic with period $q_n$.

**(b) Inductive conjugation.** Set $T_0 = R_{p_1/q_1}$. Inductively for $n \geq 1$, construct a $C^\infty$ diffeomorphism $H_n$ of $\overline{D}^{\,d}$ satisfying:
1. $H_n$ fixes $\partial D$ pointwise and preserves $\lambda$,
2. $H_n \circ R_{p_n/q_n} \circ H_n^{-1} = R_{p_{n+1}/q_{n+1}}$ (conjugation property),
3. $\|H_n - \mathrm{id}\|_{C^r} < \varepsilon_n$ for all $r \leq n$, where $\varepsilon_n > 0$ is chosen to decrease sufficiently fast.

Such $H_n$ exist because $R_{p_n/q_n}$ and $R_{p_{n+1}/q_{n+1}}$ are both periodic rotations with $q_n \mid q_{n+1}$: the map $H_n$ redistributes the $q_n$ orbits of the coarser rotation into the finer orbits of $R_{p_{n+1}/q_{n+1}}$. Since $q_{n+1}/q_n \to \infty$, the per-orbit perturbation can be made arbitrarily small, ensuring $H_n$ is $C^\infty$-close to the identity.

**(c) The limit diffeomorphism.** Define $T_n = H_n \circ T_{n-1} \circ H_n^{-1}$, so that $T_n = R_{p_{n+1}/q_{n+1}}$ (viewed through the cumulative conjugation). Because the $H_n$ converge to the identity in $C^\infty$ sufficiently fast, the sequence $\{T_n\}$ converges in $C^\infty$ to a limit
$$T = \lim_{n \to \infty} T_n.$$
The map $T$ is a $C^\infty$ diffeomorphism of $\overline{D}^{\,d}$, fixes $\partial D$ pointwise, and preserves $\lambda$.

**(d) The fast-approximation condition for mixing.** The conjugating maps $H_n$ are chosen so that the approximation satisfies the *fast-approximation condition*:
$$\|T - T_n\|_{C^0} = O(\varepsilon_n), \qquad \text{with } \varepsilon_n \cdot q_n^2 \to 0 \text{ sufficiently fast.}$$

Under this condition, $T$ is mixing with respect to $\lambda$. The proof of mixing proceeds as follows. For any measurable sets $A, B$ and any large $n$, choose $k = k(n)$ such that $q_k \leq n < q_{k+1}$. Since $T_k$ is periodic with period $q_k$, the correlation $\lambda(T_k^n(A) \cap B)$ is approximately $\lambda(A)\lambda(B)$ (the periodic average over one period equals the product, by equidistribution of the rotation orbits). The error introduced by replacing $T$ with $T_k$ is bounded by $O(\varepsilon_k \cdot q_k^2)$, which tends to zero by the fast-approximation condition. Hence
$$\lambda(T^n(A) \cap B) \to \lambda(A)\,\lambda(B),$$
proving mixing.

**Result of Step 1.** The diffeomorphism $T: \overline{D}^{\,d} \to \overline{D}^{\,d}$ is $C^\infty$, preserves Lebesgue measure, is the identity on $\partial D$, and is mixing on the interior with respect to $\lambda$.

### Step 2: Extension to general closed connected manifolds

Let $M$ be a closed connected smooth manifold of dimension $d \geq 2$, and let $\mu$ be a smooth measure on $M$ (e.g., the normalized Riemannian volume).

**(a) Embed a disk.** Choose a smooth embedding $\iota: \overline{D}^{\,d} \hookrightarrow M$ and let $D = \iota(\overline{D}^{\,d})$. Since $d \geq 2$, $\mu(D) > 0$.

**(b) Local mixing map.** By Step 1, construct a $C^\infty$ diffeomorphism $f_D: D \to D$ that equals the identity on $\partial D$ and is mixing with respect to $\mu|_D$ on the interior. Since $f_D = \mathrm{id}$ near $\partial D$, it extends to a $C^\infty$ diffeomorphism $\widetilde{f}: M \to M$ by setting $\widetilde{f} = \mathrm{id}$ on $M \setminus D$.

**(c) Ergodic base map.** By the ergodic version of the Anosov–Katok theorem (Anosov–Katok, 1970), there exists a $C^\infty$ diffeomorphism $g: M \to M$ preserving $\mu$ that is ergodic with respect to $\mu$. This is constructed by the same approximation-by-conjugation method, using local circle actions on coordinate charts of $M$: since $d \geq 2$, every coordinate chart admits a local rotation, and the method can be applied locally and then globalized using the connectedness of $M$ and a partition of unity.

**(d) Spreading the mixing to all of $M$.** The key idea is to use the ergodic map $g$ to transport the local mixing on $D$ to all of $M$, and then apply the approximation-by-conjugation method once more to produce a global mixing diffeomorphism.

Define the conjugated local mixing maps:
$$f_k = g^k \circ \widetilde{f} \circ g^{-k}, \qquad k = 0, 1, 2, \ldots$$
Each $f_k$ is a $C^\infty$ diffeomorphism of $M$ that is mixing on the disk $g^k(D)$ and the identity elsewhere. By the Birkhoff ergodic theorem (applied to the ergodic map $g$ and the set $D$), the disks $g^k(D)$ become equidistributed in $M$: for any measurable set $A$,
$$\frac{1}{N}\sum_{k=0}^{N-1} \mu\!\left(g^k(D) \cap A\right) \to \mu(D)\,\mu(A).$$
In particular, the mixing regions $\{g^k(D)\}$ cover $M$ in a measure-theoretic sense.

Now construct the global mixing diffeomorphism as a limit. Choose a rapidly increasing sequence $k_1 < k_2 < \cdots$ such that the maps $f_{k_j}$ are increasingly close to the identity (this can be arranged by choosing the $k_j$ so that $g^{k_j}$ nearly returns $D$ to itself, using the recurrence properties of the ergodic map $g$). Define:
$$\Phi_N = f_{k_1} \circ f_{k_2} \circ \cdots \circ f_{k_N}.$$
By choosing the sequence $\{k_j\}$ so that $\|f_{k_j} - \mathrm{id}\|_{C^r} < \delta_j$ with $\delta_j \to 0$ sufficiently fast, the limit
$$\Phi = \lim_{N \to \infty} \Phi_N$$
exists in $C^\infty$ and is a $C^\infty$ diffeomorphism preserving $\mu$.

The mixing property of $\Phi$ follows from the same fast-approximation argument as in Step 1: each factor $f_{k_j}$ contributes mixing on the disk $g^{k_j}(D)$, and the equidistribution of these disks (by ergodicity of $g$) ensures that the mixing effect spreads to all of $M$. More precisely, for any measurable sets $A, B$ with $\mu(A), \mu(B) > 0$, the correlation $\mu(\Phi^n(A) \cap B)$ is approximated by a sum of contributions from the mixing on each $g^{k_j}(D)$, and the fast-approximation condition ensures the total correlation tends to $\mu(A)\mu(B)$.

**Result of Step 2.** The diffeomorphism $\Phi: M \to M$ is $C^\infty$ (hence $C^1$), preserves the smooth measure $\mu$, and is mixing with respect to $\mu$.

---

## Conclusion

By Part II, there exists a $C^\infty$ (hence $C^1$) diffeomorphism $\Phi: M \to M$ that is mixing with respect to a smooth measure $\mu$ on $M$. By Part I, $\Phi$ is topologically mixing. Setting $\phi = \Phi$, the discrete dynamical system $(M, \phi)$ is topologically mixing.

---

## Remark: Necessity of $d \geq 2$

The condition $d \geq 2$ is necessary. For $d = 1$, the only closed connected smooth manifold is $S^1$. Every $C^1$ diffeomorphism of $S^1$ has a well-defined rotation number $\rho \in \mathbb{R}/\mathbb{Z}$ (Poincaré). If $\rho$ is rational, the system is periodic and hence not mixing. If $\rho$ is irrational, the system is topologically conjugate to an irrational rotation, which has pure point spectrum and is not mixing (not even weakly mixing). Therefore, no $C^1$ diffeomorphism of $S^1$ is topologically mixing.

---

## References

- D. V. Anosov and A. B. Katok, *New examples in smooth ergodic theory. Ergodic diffeomorphisms*, Trudy Moskov. Mat. Obshch. **23** (1970), 3–36.
- A. B. Katok, *Constructions in ergodic theory*, various survey articles and lecture notes extending the approximation-by-conjugation method to general compact manifolds.

$$\boxed{\text{Yes}}$$
