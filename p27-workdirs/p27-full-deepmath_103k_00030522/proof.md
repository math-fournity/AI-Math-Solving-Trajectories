# Proof: Existence of a Finite-Index Two-Sided Ideal

**Problem.** Let $R$ be a (not necessarily commutative) ring with a subring $S$ of finite additive index, i.e., $[R:S] < \infty$. Show that there exists a two-sided ideal $I$ of $S$ such that $[R:I] < \infty$.

**Answer:** Yes, such an ideal always exists.

---

## Proof

Since $[R:S] = n < \infty$, the additive quotient $R/S$ is a finite abelian group of order $n$. Let $\{r_1 + S, \dots, r_n + S\}$ denote its elements.

### Step 1: Two well-defined action maps

Because $S$ is a **subring** (closed under multiplication), left and right multiplication by elements of $S$ descend to well-defined maps on $R/S$:

- **Left action.** For each $s \in S$, define
$$\alpha_s : R/S \to R/S, \qquad \alpha_s(r_j + S) = s\,r_j + S.$$
This is well-defined: if $r_j + S = r_k + S$, then $r_j - r_k \in S$, so $s(r_j - r_k) \in S$ (since $s \in S$ and $S$ is multiplicatively closed), giving $sr_j + S = sr_k + S$. Moreover $\alpha_s$ is a group endomorphism of the finite abelian group $R/S$.

- **Right action.** For each $s \in S$, define
$$\beta_s : R/S \to R/S, \qquad \beta_s(r_j + S) = r_j\,s + S.$$
Well-definedness is identical: $r_j - r_k \in S \Rightarrow (r_j - r_k)s \in S$. This too is a group endomorphism of $R/S$.

### Step 2: The kernels and their intersection

The maps $s \mapsto \alpha_s$ and $s \mapsto \beta_s$ are group homomorphisms from $(S,+)$ into $\operatorname{End}(R/S)$, the endomorphism ring of the **finite** group $R/S$. Since $|R/S| = n$, the ring $\operatorname{End}(R/S)$ is finite (it has at most $n^n$ elements).

Define:
$$K_L = \ker(s \mapsto \alpha_s) = \{s \in S : sR \subseteq S\},$$
$$K_R = \ker(s \mapsto \beta_s) = \{s \in S : Rs \subseteq S\},$$
$$I = K_L \cap K_R = \{s \in S : sR \subseteq S \text{ and } Rs \subseteq S\}.$$

Since each homomorphism maps into a **finite** ring, each kernel has **finite index** in $S$:
$$[S : K_L] \leq |\operatorname{End}(R/S)| < \infty, \qquad [S : K_R] \leq |\operatorname{End}(R/S)| < \infty.$$

By the standard group-theoretic inequality for intersections of finite-index subgroups:
$$[S : I] = [S : K_L \cap K_R] \leq [S:K_L]\cdot[S:K_R] < \infty.$$

### Step 3: $I$ is a two-sided ideal of $S$

- **Additive subgroup.** If $s_1, s_2 \in I$, then $R(s_1 - s_2) \subseteq Rs_1 - Rs_2 \subseteq S$ and $(s_1-s_2)R \subseteq s_1 R - s_2 R \subseteq S$, so $s_1 - s_2 \in I$.

- **Left ideal.** If $s \in I$ and $t \in S$:
  - $R(ts) = (Rt)s \subseteq Rs \subseteq S$ (since $Rt \subseteq R$ and $Rs \subseteq S$),
  - $(ts)R = t(sR) \subseteq tS \subseteq S$ (since $sR \subseteq S$ and $t \in S$).
  
  Hence $ts \in I$.

- **Right ideal.** If $s \in I$ and $t \in S$:
  - $R(st) = (Rs)t \subseteq St \subseteq S$ (since $Rs \subseteq S$ and $t \in S$),
  - $(st)R = s(tR) \subseteq sR \subseteq S$ (since $tR \subseteq R$ and $sR \subseteq S$).
  
  Hence $st \in I$.

Therefore $I$ is a two-sided ideal of $S$.

### Step 4: Finite index of $I$ in $R$

Since $I \subseteq S \subseteq R$ (all as additive subgroups), multiplicativity of the index gives:
$$[R : I] = [R : S]\cdot[S : I] = n \cdot [S:I] < \infty.$$

---

## Conclusion

For any ring $R$ with a subring $S$ of finite additive index, the ideal
$$I = \{s \in S : sR \subseteq S \text{ and } Rs \subseteq S\}$$
is a two-sided ideal of $S$ with $[R:I] < \infty$.

$$\boxed{\text{Yes. Such a two-sided ideal } I \text{ always exists.}}$$
