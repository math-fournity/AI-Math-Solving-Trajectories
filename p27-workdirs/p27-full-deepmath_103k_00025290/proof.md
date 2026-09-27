# Proof: Cofinal $T \subseteq [\kappa]^{<\omega}$ contains an antichain of size $\kappa$

**Answer: YES.**

## Step 1. $|T| = \kappa$

**Lower bound.** Since $T$ is cofinal in $P = [\kappa]^{<\omega}$, for every $\alpha < \kappa$ (taking $s = \{\alpha\} \in P$) there exists $t \in T$ with $\{\alpha\} \subseteq t$, i.e. $\alpha \in t$. Hence
$$\kappa \subseteq \bigcup_{t \in T} t, \qquad \text{so } \left|\bigcup T\right| \ge \kappa.$$
Each $t \in T$ is finite, so $|\bigcup T| \le |T| \cdot \omega$. Because $\kappa$ is uncountable, $|T| \cdot \omega \ge \kappa$ forces $|T| \ge \kappa$.

**Upper bound.** $T \subseteq [\kappa]^{<\omega}$ and $|[\kappa]^{<\omega}| = \kappa^{<\omega} = \sup_{n<\omega} \kappa^n = \kappa$ (since $\kappa^n = \kappa$ for every finite $n \ge 1$ and $\kappa$ is infinite). Hence $|T| \le \kappa$.

Combining, $|T| = \kappa$.

## Step 2. $\Delta$-system lemma for uncountable $\kappa$

**Lemma.** Let $\kappa$ be an uncountable cardinal and let $\mathcal{F}$ be a family of finite sets with $|\mathcal{F}| = \kappa$. Then $\mathcal{F}$ contains a $\Delta$-subfamily $\mathcal{D} \subseteq \mathcal{F}$ of size $\kappa$ (i.e. there is a finite "root" $R$ such that $D_1 \cap D_2 = R$ for all distinct $D_1, D_2 \in \mathcal{D}$).

*Proof.* Thinning $\mathcal{F}$, we may assume every $F \in \mathcal{F}$ has the same size $n$ for some fixed $n < \omega$. We argue by induction on $n$.

- $n = 0$: all sets are $\emptyset$; take $\mathcal{D} = \mathcal{F}$, $R = \emptyset$.
- $n = 1$: all sets are singletons, already pairwise disjoint; take $R = \emptyset$.

For $n \ge 2$, split into two cases.

**Case A — some element $x$ belongs to $\kappa$ many members of $\mathcal{F}$.** Let $\mathcal{F}' = \{F \in \mathcal{F} : x \in F\}$, so $|\mathcal{F}'| = \kappa$. Apply the induction hypothesis to $\{F \setminus \{x\} : F \in \mathcal{F}'\}$ (sets of size $n-1$) to get a $\Delta$-subfamily of size $\kappa$ with root $R'$. Re-attaching $x$ gives a $\Delta$-subfamily of $\mathcal{F}$ of size $\kappa$ with root $R = R' \cup \{x\}$.

**Case B — every element belongs to $< \kappa$ members of $\mathcal{F}$.** We build a pairwise disjoint subfamily $\{F_\alpha : \alpha < \kappa\}$ by transfinite recursion. At stage $\alpha < \kappa$, suppose $\{F_\beta : \beta < \alpha\}$ have been chosen and are pairwise disjoint. Let
$$W_\alpha = \bigcup_{\beta < \alpha} F_\beta, \qquad |W_\alpha| \le |\alpha| \cdot n < \kappa.$$
A set $F \in \mathcal{F}$ is *blocked* at stage $\alpha$ if $F \cap W_\alpha \ne \emptyset$. The number of blocked sets is at most
$$\sum_{w \in W_\alpha} |\{F \in \mathcal{F} : w \in F\}| \le |W_\alpha| \cdot \sup_{w} |\{F \in \mathcal{F} : w \in F\}|.$$
Both factors are $< \kappa$; the second is $< \kappa$ by the Case B hypothesis, and the first satisfies $|W_\alpha| < \kappa$. **Key cardinal-arithmetic fact:** for any uncountable $\kappa$ (regular or singular) and any two infinite cardinals $\mu, \nu < \kappa$,
$$\mu \cdot \nu = \max(\mu, \nu) < \kappa.$$
(Indeed $\max(\mu,\nu) < \kappa$ because $\kappa$ is a cardinal, and the product of two infinite cardinals equals their maximum.) If one factor is finite the product is still $< \kappa$. Hence the number of blocked sets is $< \kappa = |\mathcal{F}|$, so some $F \in \mathcal{F}$ is unblocked; pick it as $F_\alpha$.

This produces $\{F_\alpha : \alpha < \kappa\}$ pairwise disjoint, a $\Delta$-system with root $R = \emptyset$. $\square$

## Step 3. Apply the lemma to $T$

$T$ is a family of finite sets with $|T| = \kappa$ (Step 1) and $\kappa$ is uncountable. By the lemma, $T$ has a $\Delta$-subfamily $\mathcal{D} \subseteq T$ of size $\kappa$ with root $R$:
$$D_1 \cap D_2 = R \quad \text{for all distinct } D_1, D_2 \in \mathcal{D}.$$

## Step 4. $\mathcal{D}$ (or $\mathcal{D} \setminus \{R\}$) is an antichain

Suppose $D_1, D_2 \in \mathcal{D}$ with $D_1 \subseteq D_2$ and $D_1 \ne D_2$. Then
$$D_1 = D_1 \cap D_2 = R,$$
so $D_1 = R$. Therefore the only possible comparable pair in $\mathcal{D}$ involves the root $R$ itself (and only if $R \in \mathcal{D}$, in which case $R \subseteq D$ for every $D \in \mathcal{D}$).

- If $R \notin \mathcal{D}$: $\mathcal{D}$ has no comparable pairs, so $\mathcal{D}$ is an antichain of size $\kappa$.
- If $R \in \mathcal{D}$: $\mathcal{D} \setminus \{R\}$ has no comparable pairs (removing $R$ removes the only element that could be below others), and $|\mathcal{D} \setminus \{R\}| = \kappa$ (removing one element from an infinite set of cardinality $\kappa$ does not change the cardinality). So $\mathcal{D} \setminus \{R\}$ is an antichain of size $\kappa$.

In either case, $T$ contains an antichain of size $\kappa$.

## Conclusion

$$\boxed{\text{Yes, } T \text{ contains an antichain of size } \kappa.}$$

### PROOF COMPLETE
