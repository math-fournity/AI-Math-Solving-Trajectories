# Good Transversal Basis

## Answer

$$\boxed{\text{No}}$$

Not every hypergraph $H=(V,E)$ has a good transversal basis.

## Definitions and Interpretation

A set $B \subseteq V$ is a **transversal basis** if $B$ is a minimal hitting set (transversal) for the subfamily $I_B := \{e \in E : B \cap e \neq \emptyset\}$ of edges that $B$ actually intersects. Equivalently, $B$ is a transversal basis if for every $b \in B$, there exists an edge $e \in I_B$ such that $e \cap B = \{b\}$ (every element of $B$ is *essential*).

A transversal basis $B$ is **good** if $I_B$ is maximal by inclusion among $\{I_{B'} : B' \text{ is a transversal basis}\}$; that is, there is no transversal basis $B_1$ with $I_B \subsetneq I_{B_1}$.

## Finite Case: Yes

For a **finite** hypergraph $H=(V,E)$, the vertex set $V$ is finite, so the collection of all transversal bases is finite. Consequently $\{I_B : B \text{ is a transversal basis}\}$ is a finite subset of $2^E$, which always possesses a maximal element under inclusion. Any transversal basis $B$ achieving this maximal $I_B$ is good. Thus **every finite hypergraph has a good transversal basis**.

## Infinite Case: No (Counterexample)

We construct an infinite hypergraph with no good transversal basis.

**The hypergraph.** Let $V = \mathbb{N} = \{0, 1, 2, \ldots\}$ and $E = \{e_n : n \in \mathbb{N}\}$ where
$$e_n = \{m \in \mathbb{N} : m \geq n\} = \{n, n+1, n+2, \ldots\}.$$

**Claim.** The only transversal bases are the singletons $\{k\}$ for $k \in \mathbb{N}$.

*Proof of claim.* We analyze all possible $B \subseteq \mathbb{N}$:

**Case 1: $B = \{k\}$ (singleton).** Then $I_B = \{e_n : n \leq k\}$ since $k \geq n$ iff $n \leq k$. The set $\{k\}$ hits every $e_n$ with $n \leq k$, and removing $k$ hits nothing. So $\{k\}$ is a minimal hitting set for $I_B$. ✅ Transversal basis.

**Case 2: $B$ finite with $|B| \geq 2$.** Let $m = \max(B)$. Then $I_B = \{e_n : n \leq m\}$ (because $m \in e_n$ for all $n \leq m$). For any $b \in B \setminus \{m\}$, we have $b < m$, so for every $n \leq m$, both $b$ and $m$ belong to $e_n$ (since $m \geq n$ and $b \geq n$ when $n \leq b$, and when $n > b$, $b \notin e_n$ but $m \in e_n$). In either case, $e_n \cap B$ always contains $m$ whenever it contains $b$. Specifically, for $n \leq b$: $e_n \cap B \supseteq \{b, m\} \neq \{b\}$; for $b < n \leq m$: $b \notin e_n$, so no edge witnesses $b$ as essential. Thus $b$ is **not essential**, so $B$ is not a minimal hitting set for $I_B$. ❌ Not a transversal basis.

**Case 3: $B$ infinite.** Since $B \subseteq \mathbb{N}$, if $B$ is bounded then $B$ is finite (contradiction). So $B$ is unbounded, meaning for every $n \in \mathbb{N}$, $B \cap e_n \neq \emptyset$, hence $I_B = E$. For any $b \in B$ and any $n \leq b$, the set $e_n \cap B = \{b' \in B : b' \geq n\}$ is infinite (since $B$ is unbounded). Therefore $e_n \cap B \neq \{b\}$ for all $n$, so no element of $B$ is essential. ❌ Not a transversal basis.

This exhausts all cases, proving the claim. $\square$

**No good transversal basis exists.** The transversal bases are exactly $\{k\}$ for $k \in \mathbb{N}$, with
$$I_{\{k\}} = \{e_0, e_1, \ldots, e_k\}.$$
These form a strictly increasing chain:
$$I_{\{0\}} \subsetneq I_{\{1\}} \subsetneq I_{\{2\}} \subsetneq \cdots$$
since $e_{k+1} \in I_{\{k+1\}} \setminus I_{\{k\}}$. This chain has no maximal element, so there is no transversal basis $B$ with $I_B$ maximal. Equivalently, for every transversal basis $\{k\}$, the transversal basis $\{k+1\}$ satisfies $I_{\{k\}} \subsetneq I_{\{k+1\}}$, violating the goodness condition.

## Conclusion

Every **finite** hypergraph has a good transversal basis (by finiteness of the inclusion poset). However, **infinite** hypergraphs need not: the hypergraph $(\mathbb{N}, \{\{n, n+1, \ldots\} : n \in \mathbb{N}\})$ admits no good transversal basis. Therefore, not every hypergraph has a good transversal basis.

$$\boxed{\text{No}}$$
