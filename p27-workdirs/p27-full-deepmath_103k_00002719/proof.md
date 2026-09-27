# Proof: Open atlas representable by affine

**Question.** Given a scheme $S$, does there exist an open atlas for $S$ consisting only of morphisms representable by an affine?

**Answer.** $\boxed{\text{No}}$.

---

## 1. Terminology and reformulation

**Open atlas.** An open atlas for a scheme $S$ is an open cover $\{f_i: U_i \hookrightarrow S\}_{i\in I}$ by affine open subschemes $U_i$, where each $f_i$ is an open immersion. (This is the standard meaning for schemes: a scheme is defined by gluing affine schemes along open subsets, and its "atlas" is the collection of affine charts.)

**Representable by an affine.** A morphism $f: X \to Y$ of schemes is *representable by affine schemes* if for every affine scheme $T$ and every morphism $T \to Y$, the fiber product $X \times_Y T$ is an affine scheme.

**Lemma 1.** *For a morphism of schemes $f: X \to Y$, "representable by affine schemes" is equivalent to "$f$ is an affine morphism."*

*Proof.* ($\Rightarrow$) Suppose $f$ is representable by affine. Let $V \subseteq Y$ be any affine open subscheme. The open immersion $V \hookrightarrow Y$ gives a morphism from an affine scheme to $Y$, so $X \times_Y V$ is affine. But $X \times_Y V = f^{-1}(V)$. Hence $f^{-1}(V)$ is affine for every affine open $V \subseteq Y$, which is the definition of an affine morphism.

($\Leftarrow$) Suppose $f$ is an affine morphism. For any affine $T$ and $T \to Y$, the base change $X \times_Y T \to T$ is an affine morphism (affine morphisms are stable under base change). Since $T$ is affine, $X \times_Y T$ is affine. $\square$

**Reformulation.** The question asks: does every scheme $S$ admit an affine open cover $\{U_i\}$ such that each open immersion $U_i \hookrightarrow S$ is an affine morphism? Equivalently: for every affine open $V \subseteq S$ and every $U_i$ in the cover, $U_i \cap V$ is affine.

---

## 2. The separated case: Yes

If $S$ is separated, then any affine open cover works.

*Proof.* Let $\{U_i\}$ be any affine open cover of $S$ (which exists by definition of a scheme). For any affine open $V \subseteq S$ and any $i$, $U_i \cap V$ is the intersection of two affine open subschemes of a separated scheme, hence affine (separatedness is equivalent to the diagonal being closed, which is equivalent to intersections of affine opens being affine). So each $U_i \hookrightarrow S$ is an affine morphism. $\square$

---

## 3. The counterexample: affine plane with doubled origin

### 3.1 Construction

Let $k$ be a field. Define $S$ as follows:

- $V_0 = \operatorname{Spec} k[x,y] = \mathbb{A}^2_k$,
- $V_1 = \operatorname{Spec} k[x,y] = \mathbb{A}^2_k$,
- Glue $V_0$ and $V_1$ along the open subset $U_{01} = \mathbb{A}^2_k \setminus \{(0,0)\}$ via the identity map.

The resulting scheme $S$ is the *affine plane with doubled origin*. It is a non-separated, non-affine scheme. The two copies of the origin $O_0 \in V_0$ and $O_1 \in V_1$ are distinct points of $S$, while all other points are identified. We have $S = V_0 \cup V_1$ and $V_0 \cap V_1 = U_{01}$.

### 3.2 Affine open subschemes of $S$

**Lemma 2.** *The affine open subschemes of $S$ are exactly:*
1. *Affine open subschemes of $V_0$ (these do not contain $O_1$),*
2. *Affine open subschemes of $V_1$ (these do not contain $O_0$).*

*In particular, no affine open subscheme of $S$ contains both $O_0$ and $O_1$.*

*Proof.* Since $S \setminus \{O_1\} = V_0$ and $S \setminus \{O_0\} = V_1$, any open subscheme of $S$ containing $O_0$ but not $O_1$ is contained in $V_0$, and any open containing $O_1$ but not $O_0$ is contained in $V_1$.

Now suppose $U \subseteq S$ is an open subscheme containing both $O_0$ and $O_1$. Then $U \cap V_0$ is an open in $V_0 = \mathbb{A}^2$ containing $(0,0)$, and $U \cap V_1$ is an open in $V_1 = \mathbb{A}^2$ containing $(0,0)$. Since $U \cap V_0$ and $U \cap V_1$ agree on $U_{01}$ (i.e., $(U \cap V_0) \setminus \{(0,0)\} = (U \cap V_1) \setminus \{(0,0)\}$) and both contain $(0,0)$, we have $U \cap V_0 = U \cap V_1 =: W$, an open in $\mathbb{A}^2$ containing $(0,0)$.

The scheme $U$ is obtained by gluing two copies of $W$ along $W \setminus \{(0,0)\}$. Its ring of global sections is:
$$\Gamma(U, \mathcal{O}_U) = \Gamma(W, \mathcal{O}) \times_{\Gamma(W \setminus \{(0,0)\},\, \mathcal{O})} \Gamma(W, \mathcal{O}).$$

Since $W$ is a non-empty open of $\mathbb{A}^2 = \operatorname{Spec} k[x,y]$ (which is normal and noetherian of dimension 2) and $(0,0)$ is a closed point of codimension 2, the Hartogs extension theorem gives $\Gamma(W \setminus \{(0,0)\}, \mathcal{O}) = \Gamma(W, \mathcal{O})$. Therefore:
$$\Gamma(U, \mathcal{O}_U) = \Gamma(W, \mathcal{O}) \times_{\Gamma(W, \mathcal{O})} \Gamma(W, \mathcal{O}) = \Gamma(W, \mathcal{O}).$$

If $U$ were affine, then $U = \operatorname{Spec} \Gamma(W, \mathcal{O})$. But $U$ has two points lying over $(0,0)$ (namely $O_0$ and $O_1$), while $\operatorname{Spec} \Gamma(W, \mathcal{O})$ — which is the canonical affine envelope of $W$ — has only one. This is a contradiction. Hence $U$ is not affine. $\square$

### 3.3 No affine open containing $O_0$ gives an affine morphism

**Lemma 3.** *Let $U$ be an affine open subscheme of $S$ with $O_0 \in U$. Then the open immersion $U \hookrightarrow S$ is **not** an affine morphism.*

*Proof.* By Lemma 2, $U$ does not contain $O_1$, so $U \subseteq V_0$. Thus $U$ is an affine open subscheme of $V_0 = \mathbb{A}^2_k$ containing the point $(0,0)$.

Since $U \subseteq V_0$ and $V_1 \cap V_0 = U_{01} = \mathbb{A}^2 \setminus \{(0,0)\}$, we have:
$$U \cap V_1 = U \cap U_{01} = U \setminus \{(0,0)\}.$$

For $U \hookrightarrow S$ to be an affine morphism, $U \cap V_1$ must be affine (since $V_1$ is an affine open of $S$).

Now, $U$ is a non-empty open subscheme of the irreducible scheme $\mathbb{A}^2_k$, so $\dim U = 2$. The point $(0,0)$ is a closed point of $U$ of codimension 2 (its local ring is $k[x,y]_{(x,y)}$, which has dimension 2). Since $U$ is an open subscheme of $\mathbb{A}^2_k = \operatorname{Spec} k[x,y]$, it is normal (as $k[x,y]$ is integrally closed and normality is preserved under localization).

By the **Hartogs extension theorem** for normal noetherian schemes: if $X$ is a normal noetherian scheme and $Z \subseteq X$ is a closed subset of codimension $\geq 2$, then the restriction map $\Gamma(X, \mathcal{O}_X) \to \Gamma(X \setminus Z, \mathcal{O}_X)$ is an isomorphism.

Applying this with $X = U$ and $Z = \{(0,0)\}$ (codimension 2):
$$\Gamma(U \setminus \{(0,0)\}, \mathcal{O}) = \Gamma(U, \mathcal{O}).$$

If $U \setminus \{(0,0)\}$ were affine, then $U \setminus \{(0,0)\} = \operatorname{Spec} \Gamma(U, \mathcal{O})$. But $U$ is affine, so $U = \operatorname{Spec} \Gamma(U, \mathcal{O})$. This would give $U \setminus \{(0,0)\} = U$, contradicting $(0,0) \in U$ but $(0,0) \notin U \setminus \{(0,0)\}$.

Hence $U \setminus \{(0,0)\}$ is **not** affine, so $U \cap V_1$ is not affine, and $U \hookrightarrow S$ is not an affine morphism. $\square$

**Remark.** By symmetry (swapping $V_0 \leftrightarrow V_1$ and $O_0 \leftrightarrow O_1$), the same conclusion holds for any affine open $U$ containing $O_1$.

### 3.4 No atlas exists for $S$

**Theorem.** *The affine plane with doubled origin $S$ admits no open atlas consisting of morphisms representable by affine.*

*Proof.* Suppose for contradiction that $\{U_i \hookrightarrow S\}_{i \in I}$ is such an atlas: each $U_i$ is an affine open subscheme of $S$, and each $U_i \hookrightarrow S$ is an affine morphism.

Since the atlas covers $S$, there exists some $i_0$ with $O_0 \in U_{i_0}$. By Lemma 2, $U_{i_0}$ is an affine open subscheme of $S$ containing $O_0$. By Lemma 3, the immersion $U_{i_0} \hookrightarrow S$ is not an affine morphism. This contradicts the assumption that every morphism in the atlas is representable by affine.

Similarly, $O_1$ must be covered by some $U_{j_0}$, and the same argument gives a contradiction.

Therefore, no such atlas exists. $\square$

---

## 4. Conclusion

The answer is $\boxed{\text{No}}$: not every scheme $S$ admits an open atlas consisting only of morphisms representable by affine. The affine plane with doubled origin provides an explicit counterexample: the non-separatedness at the doubled origin forces any affine open neighborhood of either origin to have a non-affine intersection with the other affine chart, violating the affine morphism condition.

### PROOF COMPLETE
