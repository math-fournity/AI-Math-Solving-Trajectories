# Proof: Graded algebra with $A_i A_{-i} = A_0$ is strongly graded

## Problem

Does there exist a graded algebra $A = \oplus_{i \in \mathbb{Z}} A_i$ such that $A_i \cdot A_{-i} = A_0$ for all $i \in \mathbb{Z}$, but the algebra is not strongly graded?

## Answer

$$\boxed{\text{No}}$$

No such algebra exists. The condition $A_i A_{-i} = A_0$ for all $i \in \mathbb{Z}$ forces $A$ to be strongly graded.

## Proof

We prove the following theorem (a standard form of Dade's theorem), which directly implies the answer.

**Theorem (Dade).** Let $G$ be a group and let $A = \oplus_{g \in G} A_g$ be a $G$-graded unital ring. Then $A$ is strongly graded (i.e., $A_g A_h = A_{gh}$ for all $g, h \in G$) if and only if $A_g A_{g^{-1}} = A_e$ for all $g \in G$, where $e \in G$ is the identity.

### Proof of the theorem

($\Rightarrow$) If $A$ is strongly graded, then $A_g A_{g^{-1}} = A_{g \cdot g^{-1}} = A_e$ for all $g \in G$. This direction is immediate.

($\Leftarrow$) Suppose $A_g A_{g^{-1}} = A_e$ for all $g \in G$. We must show $A_g A_h = A_{gh}$ for all $g, h \in G$.

**Step 1: The reverse inclusion is automatic.** By the definition of a graded ring, the product of a homogeneous element of degree $g$ and a homogeneous element of degree $h$ is homogeneous of degree $gh$. Therefore
$$
A_g \cdot A_h \subseteq A_{gh}
$$
holds for any graded ring, with no additional hypothesis.

**Step 2: The forward inclusion.** We must show $A_{gh} \subseteq A_g A_h$.

Apply the hypothesis with $g$ replaced by $h^{-1}$: we have $A_{h^{-1}} A_h = A_e$. Since $A$ is unital with $1 \in A_e$, we can write
$$
1 = \sum_{k=1}^{n} a_k \, b_k,
$$
where $a_k \in A_{h^{-1}}$ and $b_k \in A_h$ for each $k$.

Now let $x \in A_{gh}$ be an arbitrary homogeneous element. Then
$$
x = x \cdot 1 = x \sum_{k=1}^{n} a_k b_k = \sum_{k=1}^{n} (x \, a_k) \, b_k.
$$

We analyze the degrees of the factors in each summand:
- $x \in A_{gh}$ and $a_k \in A_{h^{-1}}$, so $x \, a_k \in A_{gh} \cdot A_{h^{-1}} \subseteq A_{gh \cdot h^{-1}} = A_g$.
- $b_k \in A_h$.

Therefore each summand $(x \, a_k) b_k \in A_g \cdot A_h$, and consequently
$$
x = \sum_{k=1}^{n} (x \, a_k) b_k \in A_g A_h.
$$

Since $x \in A_{gh}$ was arbitrary, we conclude
$$
A_{gh} \subseteq A_g A_h.
$$

**Step 3: Conclusion.** Combining Steps 1 and 2:
$$
A_g A_h \subseteq A_{gh} \quad \text{and} \quad A_{gh} \subseteq A_g A_h,
$$
so $A_g A_h = A_{gh}$ for all $g, h \in G$. $\quad \blacksquare$

### Application to the problem

Take $G = \mathbb{Z}$ (with additive notation, so the identity is $0$ and the inverse of $i$ is $-i$). The hypothesis of the problem is exactly
$$
A_i \cdot A_{-i} = A_0 \quad \text{for all } i \in \mathbb{Z},
$$
which is precisely the condition $A_g A_{g^{-1}} = A_e$ for all $g \in G$ in Dade's theorem. By the theorem, $A$ is strongly graded:
$$
A_i A_j = A_{i+j} \quad \text{for all } i, j \in \mathbb{Z}.
$$

Therefore, **no** graded algebra can satisfy $A_i A_{-i} = A_0$ for all $i \in \mathbb{Z}$ without being strongly graded.

### Remarks

1. **Unital assumption.** The proof uses $1 \in A_e$ to decompose $1 = \sum a_k b_k$ and to write $x = x \cdot 1$. This is the standard convention for "graded algebra" (a unital algebra graded by a group). Without a unit, the statement can fail, but this is outside the standard definition.

2. **Generality.** Dade's theorem holds for any group $G$, not just $\mathbb{Z}$. The proof above makes no use of commutativity or order structure of $\mathbb{Z}$.

3. **Why $A_0$ need not be a field.** The proof never requires $A_0$ to be commutative, a field, or a division ring. The key mechanism is purely the existence of a partition of unity $1 = \sum a_k b_k$ from $A_{h^{-1}} A_h = A_e$, which works over any unital base ring $A_0$. This is why all the attempted counterexamples with $A_0 = k \times k$, $A_0 = k[\epsilon]/(\epsilon^2)$, $A_0 = M_2(k)$, etc., necessarily fail: the theorem is base-ring-agnostic.

4. **Intuition.** The condition $A_i A_{-i} = A_0$ provides, for each $i$, a "partition of unity" $\sum a_k b_k = 1$ with $a_k \in A_i$, $b_k \in A_{-i}$. Multiplying any $x \in A_{i+j}$ on the right by this partition splits $x$ into a sum of elements of $A_i \cdot A_j$. This is the single mechanism that forces strong grading.

### PROOF COMPLETE
