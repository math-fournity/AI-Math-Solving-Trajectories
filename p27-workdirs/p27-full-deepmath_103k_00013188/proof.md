# Proof

**Answer: No.** There exists a compact LCA group $G$ and an open subset $F \subseteq G$ with $F + F = G$ such that $F - F \neq G$.

## Counterexample

Let $G = \mathbb{T} \times \mathbb{Z}/3\mathbb{Z}$, where $\mathbb{T} = \mathbb{R}/\mathbb{Z}$ is the circle group (compact) and $\mathbb{Z}/3\mathbb{Z}$ is given the discrete topology (hence compact, being finite). The product $G$ is a compact LCA group.

Define
$$
F = A \times \{0\} \;\cup\; B \times \{1\} \;\cup\; C \times \{2\},
$$
where
$$
A = B = (0,\, 0.4) \subseteq \mathbb{T}, \qquad C = (0.3,\, 0.7) \subseteq \mathbb{T}.
$$

Here intervals are taken in $\mathbb{T} = \mathbb{R}/\mathbb{Z}$, i.e., $q((0, 0.4))$ where $q: \mathbb{R} \to \mathbb{T}$ is the quotient map.

## Step 1: $F$ is open

Each of $A, B, C$ is open in $\mathbb{T}$ (as images of open intervals under the open quotient map $q$). Each singleton $\{0\}, \{1\}, \{2\}$ is open in the discrete group $\mathbb{Z}/3\mathbb{Z}$. Hence each piece $A \times \{0\}$, $B \times \{1\}$, $C \times \{2\}$ is open in the product topology, and $F$ is a union of three open sets. $\checkmark$

## Step 2: $F + F = G$

We must show that every $(t, n) \in \mathbb{T} \times \mathbb{Z}/3\mathbb{Z}$ can be written as $(a_1, i) + (a_2, j)$ with $(a_1, i), (a_2, j) \in F$, i.e., $a_1 + a_2 \equiv t \pmod{1}$ and $i + j \equiv n \pmod{3}$.

For each residue $n \in \mathbb{Z}/3\mathbb{Z}$, the set of pairs $(i, j)$ with $i + j \equiv n$ gives a union of interval sums in the $\mathbb{T}$-component. We compute:

**$n = 0$:** pairs $(0,0), (1,2), (2,1)$.
$$
(A+A) \cup (B+C) \cup (C+B) = q\big((0,0.8) \cup (0.3, 1.1)\big) = q\big((0, 1.1)\big) = \mathbb{T}.
$$
(Here $(0, 0.8) \cup (0.3, 1.1) = (0, 1.1)$ as subsets of $\mathbb{R}$, and $q((0,1.1)) = \mathbb{T}$ since every coset $t + \mathbb{Z}$ has a representative in $(0, 1.1)$: the representative in $(0,1)$ works, and $0 + \mathbb{Z}$ has representative $1 \in (0, 1.1)$.)

**$n = 1$:** pairs $(0,1), (1,0), (2,2)$.
$$
(A+B) \cup (C+C) = q\big((0, 0.8) \cup (0.6, 1.4)\big) = q\big((0, 1.4)\big) = \mathbb{T}.
$$

**$n = 2$:** pairs $(0,2), (1,1), (2,0)$.
$$
(A+C) \cup (B+B) = q\big((0.3, 1.1) \cup (0, 0.8)\big) = q\big((0, 1.1)\big) = \mathbb{T}.
$$

In all three cases the $\mathbb{T}$-component covers $\mathbb{T}$, so $F + F = G$. $\checkmark$

## Step 3: $F - F \neq G$

We claim $g = (0.5,\, 0) \notin F - F$.

The $\mathbb{Z}/3\mathbb{Z}$-component of $F - F$ at residue $0$ comes from pairs $(i, j)$ with $i - j \equiv 0 \pmod{3}$, namely $(0,0), (1,1), (2,2)$. The corresponding $\mathbb{T}$-components are:
$$
A - A = (0, 0.4) - (0, 0.4) = q((-0.4, 0.4)),
$$
$$
B - B = q((-0.4, 0.4)), \qquad C - C = (0.3, 0.7) - (0.3, 0.7) = q((-0.4, 0.4)).
$$

So the level-$0$ component of $F - F$ is
$$
q((-0.4, 0.4)) = \{0\} \cup (0, 0.4) \cup (0.6, 1) \subseteq \mathbb{T}.
$$

(The preimage under $q$ is $\bigcup_{n \in \mathbb{Z}}(n - 0.4, n + 0.4)$, which in $[0,1)$ gives $\{0\} \cup (0,0.4) \cup (0.6,1)$.)

Since $0.5 \notin \{0\} \cup (0, 0.4) \cup (0.6, 1)$, we have $(0.5, 0) \notin F - F$.

Therefore $F - F \neq G$. $\checkmark$

## Step 4: Direct verification that $(g + F) \cap F = \emptyset$

For $g = (0.5, 0)$:
$$
g + F = (0.5 + A) \times \{0\} \;\cup\; (0.5 + B) \times \{1\} \;\cup\; (0.5 + C) \times \{2\},
$$
where $0.5 + A = (0.5, 0.9)$, $0.5 + B = (0.5, 0.9)$, and $0.5 + C = q((0.8, 1.2)) = \{0\} \cup (0, 0.2) \cup (0.8, 1)$.

Checking each $\mathbb{Z}/3\mathbb{Z}$-level:

- **Level 0:** $(0.5, 0.9) \cap (0, 0.4) = \emptyset$. $\checkmark$
- **Level 1:** $(0.5, 0.9) \cap (0, 0.4) = \emptyset$. $\checkmark$
- **Level 2:** $\big(\{0\} \cup (0, 0.2) \cup (0.8, 1)\big) \cap (0.3, 0.7) = \emptyset$. $\checkmark$

Hence $(g + F) \cap F = \emptyset$, confirming $g \notin F - F$.

## Conclusion

The group $G = \mathbb{T} \times \mathbb{Z}/3\mathbb{Z}$ is a compact LCA group, $F$ is an open subset with $F + F = G$, yet $(g + F) \cap F = \emptyset$ for $g = (0.5, 0)$. Therefore $F - F \neq G$.

$$
\boxed{\text{No}}
$$

The statement "$F + F = G$ implies $F - F = G$" does **not** hold in general for compact LCA groups.
