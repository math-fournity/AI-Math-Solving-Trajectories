# Is there a Hausdorff compactification of the irrational numbers with its usual topology such that the remainder is a discrete space?

**Answer: No.** There is no Hausdorff compactification of the irrational numbers $\mathbb{P} = \mathbb{R}\setminus\mathbb{Q}$ whose remainder is a discrete space.

---

## Proof

We argue by contradiction. We use three standard lemmas, each proved below.

### Lemma 1 (The irrationals are nowhere locally compact)

$\mathbb{P}$ is nowhere locally compact: no point of $\mathbb{P}$ has a compact neighborhood in $\mathbb{P}$.

*Proof.* Let $x\in\mathbb{P}$ and let $U$ be any neighborhood of $x$ in $\mathbb{P}$. Pick $\varepsilon>0$ with $(x-\varepsilon, x+\varepsilon)\cap\mathbb{P}\subseteq U$, and let $C = [x-\varepsilon, x+\varepsilon]\cap\mathbb{P}$. Then $C$ is closed in $\mathbb{P}$ and contains a relative neighborhood of $x$, so it suffices to show $C$ is not compact. The set $C$ is not closed in $\mathbb{R}$ (its closure in $\mathbb{R}$ is $[x-\varepsilon,x+\varepsilon]$, which contains rationals), hence $C$ is not a closed subset of the compact set $[x-\varepsilon,x+\varepsilon]$, and so $C$ is not compact. By Heine–Borel, equivalently, $C$ is a closed-and-bounded subset of $\mathbb{R}$ only if it is closed in $\mathbb{R}$, which it is not. Thus no point of $\mathbb{P}$ has a compact neighborhood. $\square$

### Lemma 2 (Open subsets inherit nowhere local compactness)

If $Y$ is nowhere locally compact and $U\subseteq Y$ is a non-empty open subset, then $U$ is not locally compact.

*Proof.* Suppose $U$ were locally compact. Then some $x\in U$ has a compact neighborhood $C\subseteq U$ (compact in the subspace topology of $U$, hence in $Y$). So there is a set $O$, open in $U$ with $x\in O\subseteq C$. Since $U$ is open in $Y$, the set $O$ is also open in $Y$. Hence $x\in\operatorname{int}_Y(C)$, i.e. $x$ has a compact neighborhood in $Y$ — contradicting $Y$ being nowhere locally compact. $\square$

### Lemma 3 (Open subsets of "compact Hausdorff minus a point" are locally compact)

Let $L$ be a compact Hausdorff space and $r\in L$. Then $L\setminus\{r\}$ is locally compact, and every open subset of $L\setminus\{r\}$ is locally compact.

*Proof.* $L\setminus\{r\}$ is an open subset of the compact Hausdorff (hence locally compact) space $L$, and an open subspace of a locally compact Hausdorff space is locally compact. Moreover, an open subspace of a locally compact Hausdorff space is again locally compact Hausdorff, so its open subspaces are locally compact as well. $\square$

### Main argument

Suppose for contradiction that $K$ is a Hausdorff compactification of $\mathbb{P}$ with remainder $R = K\setminus\mathbb{P}$ discrete.

- $R\neq\emptyset$, since $\mathbb{P}$ is not compact while $K$ is.
- $K$ is compact Hausdorff, hence regular.

Fix any $r\in R$. Since $R$ is discrete, there exists an open set $V_r$ in $K$ with $V_r\cap R = \{r\}$. By regularity of $K$, choose an open set $W_r$ in $K$ with
$$r \in W_r \subseteq \operatorname{cl}_K(W_r) \subseteq V_r.$$
Then
$$\operatorname{cl}_K(W_r)\cap R \subseteq V_r\cap R = \{r\}.$$

**Claim.** $W_r\cap\mathbb{P}$ is a non-empty open subset of $\mathbb{P}$.

*Proof of claim.* $W_r$ is open in $K$ and contains $r\in R$. Since $\mathbb{P}$ is dense in $K$ (it is the dense embedded copy in the compactification), every non-empty open subset of $K$ meets $\mathbb{P}$. As $W_r\neq\emptyset$, we have $W_r\cap\mathbb{P}\neq\emptyset$. Moreover,
$$W_r\cap\mathbb{P} = W_r\setminus R = W_r\setminus\{r\},$$
which is open in $K\setminus\{r\}$, hence open in $\mathbb{P}$ (as a subspace of $K\setminus\{r\}$, since $\mathbb{P}\subseteq K\setminus\{r\}$). $\square$

**Two contradictory conclusions about $W_r\cap\mathbb{P}$:**

1. *$W_r\cap\mathbb{P}$ is locally compact.* Indeed,
$$W_r\cap\mathbb{P} = W_r\setminus\{r\} = W_r \cap (K\setminus\{r\}),$$
an open subset of $K\setminus\{r\}$. But $\operatorname{cl}_K(W_r)\setminus\{r\}$ is an open subset of the compact Hausdorff space $\operatorname{cl}_K(W_r)$ (open because $\{r\}$ is closed), hence is locally compact by Lemma 3. The set $W_r\cap\mathbb{P} = W_r\setminus\{r\}$ is an open subset of $\operatorname{cl}_K(W_r)\setminus\{r\}$, hence is itself locally compact (open subspace of locally compact Hausdorff).

2. *$W_r\cap\mathbb{P}$ is not locally compact.* By Lemma 1, $\mathbb{P}$ is nowhere locally compact. By Lemma 2, every non-empty open subset of $\mathbb{P}$ is not locally compact. By the Claim, $W_r\cap\mathbb{P}$ is a non-empty open subset of $\mathbb{P}$, so it is not locally compact.

This is a contradiction. Therefore no such compactification exists. $\square$

---

### Remark

The argument uses only that $\mathbb{P}$ is a nowhere locally compact Tychonoff space. Hence the same conclusion holds for any nowhere locally compact Tychonoff space $X$: there is no Hausdorff compactification of $X$ with discrete remainder.

### PROOF COMPLETE
