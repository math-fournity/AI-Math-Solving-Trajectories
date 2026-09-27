# Proof

**Answer: Yes.** If $F_{\vec p} \cong F_{\vec q}$ as topological groups, then $\vec p = \vec q$.

---

## Setup

Let $G = \prod_{k \in \omega} F_{p_k}$ with the product topology (each $F_{p_k}$ discrete), where $\vec p = (p_k)$ is an increasing sequence of primes. Let $\pi_i : G \to F_{p_i}$ denote the $i$-th projection.

We recover $\vec p$ from the topological group structure of $G$.

---

## Lemma 1 (Surjections to free groups factor through one coordinate)

**Claim.** Any continuous surjection $\phi : G = \prod_k F_{p_k} \to F_n$ with $n \geq 2$ factors as
$$G \xrightarrow{\pi_j} F_{p_j} \xrightarrow{\sigma} F_n$$
for some index $j$ and some surjection $\sigma : F_{p_j} \to F_n$. In particular $p_j \geq n$.

**Proof.** Since $F_n$ is discrete and $\phi$ is continuous, $\ker(\phi)$ is open, so $\ker(\phi) \supseteq \prod_{k \geq N} F_{p_k}$ for some $N$. Thus $\phi$ factors through the finite product $\prod_{k < N} F_{p_k}$, giving a surjection
$$\tilde\phi : \prod_{k < N} F_{p_k} \to F_n.$$
This is determined by homomorphisms $\phi_k : F_{p_k} \to F_n$ ($k < N$) whose images $H_k = \operatorname{im}(\phi_k)$ pairwise commute (since the factors commute in the product) and generate $F_n$.

Since the $H_k$ pairwise commute and generate $F_n$, each $H_k$ is normal in $F_n$: for any $g \in F_n = \langle H_1, \dots, H_{N-1}\rangle$ and $h \in H_k$, write $g = h_1 \cdots h_{N-1}$ with $h_i \in H_i$; then $g h g^{-1} = h_i h h_i^{-1}$ (other factors commute with $h$) $= h$ if $i \neq k$, and $= h_k h h_k^{-1} \in H_k$ if $i = k$. More precisely, $g h g^{-1} \in H_k$ since $H_k$ commutes with all $H_i$ ($i \neq k$) and is normalized by $H_k$ itself. So $H_k \trianglelefteq F_n$.

The $H_k$ are pairwise commuting normal subgroups generating $F_n$, so $F_n$ is the internal direct product $H_0 \times H_1 \times \cdots \times H_{N-1}$.

**Key fact:** $F_n$ ($n \geq 2$) is *directly indecomposable*: if $F_n = A \times B$ with $A, B$ normal, then $A$ and $B$ commute, so every element of $A$ commutes with every element of $B$. But the center of $F_n$ is trivial ($n \geq 2$), and the centralizer of any nontrivial element in a free group is cyclic. If both $A$ and $B$ are nontrivial, pick $a \in A \setminus\{e\}$, $b \in B \setminus\{e\}$; then $ab = ba$, so $b \in C_{F_n}(a)$, which is cyclic, hence $\langle a, b \rangle$ is cyclic, hence abelian — but $F_n$ contains no non-cyclic abelian subgroup that is a direct factor... More directly: $A$ and $B$ commuting and both normal means $F_n = A \times B$; but a free group of rank $\geq 2$ cannot be a nontrivial direct product (this is a classical result: any two nontrivial normal subgroups of $F_n$ have nontrivial intersection, since $F_n$ is torsion-free and its normal subgroups are free of rank $\geq 2$ when of finite index, and in general a direct product decomposition would make $F_n$ have nontrivial center, contradiction).

Therefore exactly one $H_k$ is nontrivial, and it equals $F_n$. So $\tilde\phi$ factors through the single coordinate $k = j$, giving $\phi = \sigma \circ \pi_j$ with $\sigma : F_{p_j} \to F_n$ surjective. $\square$

---

## Lemma 2 (Structure of open normal subgroups with free quotient)

The open normal subgroups $N \trianglelefteq G$ with $G/N \cong F_n$ for some $n \geq 2$ are exactly the subgroups of the form
$$N = \pi_i^{-1}(M), \quad \text{where } p_i \geq n,\; M \trianglelefteq F_{p_i},\; F_{p_i}/M \cong F_n.$$

**Proof.** ($\Leftarrow$) Clear: $G/\pi_i^{-1}(M) \cong F_{p_i}/M \cong F_n$, and $\pi_i^{-1}(M)$ is open (preimage of an open subgroup under a continuous map).

($\Rightarrow$) If $G/N \cong F_n$ ($n \geq 2$), the quotient map $\phi : G \to G/N \cong F_n$ is a continuous surjection. By Lemma 1, $\phi = \sigma \circ \pi_j$ for some $j$ and surjection $\sigma : F_{p_j} \to F_n$. Then $N = \ker(\phi) = \pi_j^{-1}(\ker(\sigma))$, and $F_{p_j}/\ker(\sigma) \cong F_n$, with $p_j \geq n$. $\square$

---

## Lemma 3 (Incomparability between different coordinates)

Let $N_1 = \pi_i^{-1}(M_1)$ with $G/N_1 \cong F_{n_1}$ ($n_1 \geq 2$) and $N_2 = \pi_j^{-1}(M_2)$ with $G/N_2 \cong F_{n_2}$ ($n_2 \geq 2$), where $i \neq j$. Then $N_1$ and $N_2$ are **incomparable** (neither contains the other).

**Proof.** Suppose $N_1 \subseteq N_2$. Take $g \in G$ with $\pi_i(g) \in M_1$ (so $g \in N_1 \subseteq N_2$) but $\pi_j(g) \notin M_2$. This is possible because $\pi_i$ and $\pi_j$ are independent projections ($i \neq j$): we can choose $g$ freely in each coordinate. But $g \in N_2$ requires $\pi_j(g) \in M_2$, contradiction — unless $M_2 = F_{p_j}$, which would make $G/N_2$ trivial, contradicting $n_2 \geq 2$. $\square$

---

## Lemma 4 (Incomparability within a coordinate, same quotient)

Let $N_1 = \pi_i^{-1}(M_1)$ and $N_2 = \pi_i^{-1}(M_2)$ with $F_{p_i}/M_1 \cong F_{p_i}/M_2 \cong F_n$ ($n \geq 2$). If $N_1 \subseteq N_2$ then $N_1 = N_2$.

**Proof.** $N_1 \subseteq N_2$ gives $M_1 \subseteq M_2$, hence a surjection $F_{p_i}/M_1 \twoheadrightarrow F_{p_i}/M_2$, i.e., $F_n \twoheadrightarrow F_n$. Free groups of finite rank are **Hopfian**: every surjective endomorphism is an automorphism. So this surjection is an isomorphism, giving $M_1 = M_2$. $\square$

---

## Theorem (Main result)

If $G = \prod_k F_{p_k}$ and $G' = \prod_k F_{q_k}$ are topologically isomorphic, then $\vec p = \vec q$.

**Proof.** Define the **lattice** $\mathcal{L}(G)$: the set of all open normal subgroups $N \trianglelefteq G$ such that $G/N \cong F_n$ for some $n \geq 2$, partially ordered by inclusion $\subseteq$.

**$\mathcal{L}(G)$ is a topological group invariant.** A topological group isomorphism $\Phi : G \to G'$ maps open normal subgroups to open normal subgroups, preserves quotients ($G/N \cong G'/\Phi(N)$), and preserves inclusion. So $\mathcal{L}(G) \cong \mathcal{L}(G')$ as posets.

**Decomposition into columns.** By Lemma 2, every element of $\mathcal{L}(G)$ is $\pi_i^{-1}(M)$ for a unique coordinate $i$ (uniqueness follows from Lemma 3: an element cannot belong to two different coordinates). Define the **column** $C_i$ as the set of all elements of $\mathcal{L}(G)$ of the form $\pi_i^{-1}(M)$.

Consider the **comparability graph** on $\mathcal{L}(G)$: two elements are adjacent if one contains the other.

- **Between columns** ($i \neq j$): by Lemma 3, no element of $C_i$ is comparable with any element of $C_j$. So there are no edges between different columns.
- **Within a column** $C_i$: the element $\ker(\pi_i) = \pi_i^{-1}(\{e\})$ belongs to $\mathcal{L}(G)$ (since $G/\ker(\pi_i) \cong F_{p_i}$ and $p_i \geq 2$) and is contained in every element of $C_i$ (since $\{e\} \subseteq M$ for all $M$). So $\ker(\pi_i)$ is comparable with every element of $C_i$, making $C_i$ connected in the comparability graph.

Therefore the connected components of the comparability graph are exactly the columns $\{C_i\}_{i \in \omega}$.

**Each column has a unique minimal element.** The element $\ker(\pi_i)$ is the minimum of $C_i$ (it is contained in every element of $C_i$). By Lemma 4, no two distinct elements of $C_i$ with the same quotient are comparable, so the only element that can be below everything is $\ker(\pi_i)$, which is indeed unique.

**Recovering $p_i$.** The quotient $G/\ker(\pi_i) \cong F_{p_i}$. The abelianization of $F_{p_i}$ is $\mathbb{Z}^{p_i}$, a free abelian group of rank $p_i$. The rank $p_i$ is an isomorphism invariant of the quotient group. Since the quotient groups (as abstract groups, determined up to isomorphism by the poset structure via the labeling) are recoverable from $\mathcal{L}(G)$, the value $p_i$ is determined for each column.

**Recovering the multiset.** The columns are the connected components of $\mathcal{L}(G)$, which is a topological group invariant. Each column determines its $p_i$ via the abelianization rank of the minimal element's quotient. Therefore the multiset $\{p_k : k \in \omega\}$ (with multiplicities) is a topological group invariant.

**Recovering the sequence.** Since $\vec p = (p_k)$ is an increasing sequence of primes, the multiset $\{p_k\}$ uniquely determines the sequence:
- If "increasing" means strictly increasing: each prime appears at most once, so the multiset determines the sequence by ordering.
- If "increasing" means non-decreasing: the multiset (with multiplicities) determines the sequence by ordering.

In either case, $\vec p$ is determined by the multiset, hence by the topological group structure.

**Conclusion.** If $F_{\vec p} \cong F_{\vec q}$ as topological groups, then $\mathcal{L}(F_{\vec p}) \cong \mathcal{L}(F_{\vec q})$, so the multisets $\{p_k\} = \{q_k\}$, hence $\vec p = \vec q$.

$$\boxed{\text{Yes}}$$

### PROOF COMPLETE
