# Proof: $A_p \to B_p$ is surjective (equivalent formulation)

## Statement

Let $A$ be a commutative ring, $U \subseteq \text{Spec}(A)$ an open subset, and $B = \mathcal{O}(U)$ the ring of sections of the structure sheaf over $U$. Given $s \in A$ with $D(s) \subseteq U$ and $f \in B$ such that $f|_{D(s)} = 0$, we show there exists an integer $N$ such that $s^N \cdot f = 0$ in $B$.

## Proof

**Step 1: Cover $U$ by finitely many distinguished opens.**

Since $\text{Spec}(A)$ is quasi-compact, every open subset is quasi-compact. The distinguished opens $\{D(t)\}_{t \in A}$ form a basis for the topology, so we can cover $U$ by distinguished opens and extract a finite subcover:

$$U = D(s_1) \cup D(s_2) \cup \cdots \cup D(s_n), \quad s_i \in A.$$

**Step 2: Express the restriction of $f$ to each $D(s_i)$.**

By the definition of the structure sheaf on an affine scheme, $\mathcal{O}(D(s_i)) = A_{s_i}$. Let

$$f_i := f|_{D(s_i)} \in A_{s_i}.$$

Write $f_i = a_i / s_i^{m_i}$ for some $a_i \in A$ and $m_i \geq 0$.

**Step 3: Use the hypothesis $f|_{D(s)} = 0$.**

Since $D(s) \subseteq U$, we have

$$D(s) = D(s) \cap U = \bigcup_{i=1}^{n} \bigl(D(s) \cap D(s_i)\bigr) = \bigcup_{i=1}^{n} D(s \cdot s_i).$$

The restriction of $f$ to $D(s)$ is $0$, so the restriction of $f_i$ to $D(s \cdot s_i)$ is $0$ for each $i$. In algebraic terms, the image of $f_i = a_i / s_i^{m_i}$ under the localization map

$$A_{s_i} \longrightarrow A_{s \cdot s_i}$$

is $0$. This means there exists an integer $k_i \geq 0$ such that

$$(s \cdot s_i)^{k_i} \cdot a_i = 0 \quad \text{in } A,$$

i.e., $s^{k_i} \cdot s_i^{k_i} \cdot a_i = 0$ in $A$.

**Step 4: Show $s^{k_i} \cdot f_i = 0$ in $A_{s_i}$.**

In $A_{s_i}$, consider $s^{k_i} \cdot f_i = s^{k_i} \cdot a_i / s_i^{m_i}$. This element is zero in $A_{s_i}$ if and only if there exists $\ell \geq 0$ with $s_i^{\ell} \cdot s^{k_i} \cdot a_i = 0$ in $A$. Taking $\ell = k_i$, we use the identity from Step 3:

$$s_i^{k_i} \cdot s^{k_i} \cdot a_i = s^{k_i} \cdot s_i^{k_i} \cdot a_i = 0.$$

Therefore $s^{k_i} \cdot f_i = 0$ in $A_{s_i}$ for each $i$.

**Step 5: Find a uniform exponent $N$.**

Set $N = \max(k_1, k_2, \ldots, k_n)$. Then for each $i$:

$$s^{N} \cdot f_i = s^{N - k_i} \cdot \underbrace{s^{k_i} \cdot f_i}_{=0} = 0 \quad \text{in } A_{s_i}.$$

**Step 6: Conclude $s^N \cdot f = 0$ in $B$ by the sheaf property.**

The element $s^N \cdot f \in B = \mathcal{O}(U)$ restricts to $s^N \cdot f_i = 0$ on each $D(s_i)$. Since $\{D(s_i)\}_{i=1}^{n}$ covers $U$, the **locality axiom** of the sheaf $\mathcal{O}$ states:

> If a section restricts to $0$ on every open in a cover, then the section is $0$.

Therefore $s^N \cdot f = 0$ in $B$. $\blacksquare$

## Why this implies $A_p \to B_p$ is surjective

The condition proved above — that the kernel of the restriction map $B \to \mathcal{O}(D(s)) = A_s$ is exactly the $s$-power-torsion submodule $\{f \in B : s^N f = 0 \text{ for some } N\}$ — is equivalent to saying that the natural map

$$B \otimes_A A_s \longrightarrow A_s$$

is an **isomorphism** for every $s$ with $D(s) \subseteq U$.

Now, $A_p = \varinjlim_{s \notin p} A_s$ and $B_p = B \otimes_A A_p = \varinjlim_{s \notin p} (B \otimes_A A_s)$. For any $s \notin p$, since $U$ is an open neighborhood of $p$, there exists $t \in A$ with $p \in D(t) \subseteq U$ (distinguished opens form a basis). Then $st \notin p$ (as $p$ is prime) and $D(st) \subseteq D(s) \cap D(t) \subseteq U$, so the directed system computing $A_p$ (resp. $B_p$) can be restricted to those $s$ with $D(s) \subseteq U$ without changing the colimit.

Since $B \otimes_A A_s \cong A_s$ for all such $s$, taking the colimit gives

$$B_p \cong A_p,$$

so the map $A_p \to B_p$ is an **isomorphism** (hence surjective). $\blacksquare$
