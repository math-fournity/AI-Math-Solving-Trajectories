# Proof

**Claim.** If $A$ and $B$ are two $C^{*}$-algebras such that their minimal tensor product $A \otimes_{\min} B$ is a $Z^{*}$-algebra, then both $A$ and $B$ are $Z^{*}$-algebras (in particular, $A$ or $B$ is a $Z^{*}$-algebra).

We prove a stronger lemma from which the claim follows immediately.

---

## Lemma. Every unital $C^{*}$-algebra is a $Z^{*}$-algebra.

Recall that a unital $C^{*}$-algebra $\mathcal{A}$ is a $Z^{*}$-algebra if every element of $\mathcal{A}$ is a $\mathbb{Z}$-linear combination of unitaries, i.e., $\mathcal{A} = \mathbb{Z}\text{-span}(\mathcal{U}(\mathcal{A}))$.

### Step 1. Every self-adjoint element of norm $\leq 1$ is the average of two unitaries.

Let $a \in \mathcal{A}$ be self-adjoint with $\|a\| \leq 1$. By the continuous functional calculus, we may apply any continuous function on $[-1,1]$ to $a$. Define

$$
\theta := \arccos(a) \in \mathcal{A},
$$

which is self-adjoint since $\arccos$ is real-valued on $[-1,1]$. Set

$$
u := e^{i\theta} \in \mathcal{A}.
$$

Since $\theta$ is self-adjoint, $u$ is unitary: $u^{*}u = e^{-i\theta}e^{i\theta} = 1$ and $uu^{*} = 1$. Moreover, by the functional calculus,

$$
u + u^{*} = e^{i\theta} + e^{-i\theta} = 2\cos(\theta) = 2\cos(\arccos(a)) = 2a.
$$

Hence $2a = u + u^{*}$, i.e., $a = \tfrac{1}{2}(u + u^{*})$. In particular, $a$ is a $\mathbb{Z}$-linear combination of unitaries **provided we can clear the factor of $2$**, which we handle by scaling in Step 2.

### Step 2. Every self-adjoint element is a $\mathbb{Z}$-linear combination of unitaries.

Let $a \in \mathcal{A}$ be self-adjoint (with arbitrary norm). Choose $n \in \mathbb{N}$ such that $2n \geq \|a\|$, so that $\|a/(2n)\| \leq 1$. Applying Step 1 to the self-adjoint element $a/(2n)$, there exists a unitary $u \in \mathcal{A}$ with

$$
2 \cdot \frac{a}{2n} = u + u^{*}, \qquad \text{i.e.,} \qquad \frac{a}{n} = u + u^{*}.
$$

Therefore

$$
a = n \cdot u + n \cdot u^{*},
$$

which is a $\mathbb{Z}$-linear combination of the unitaries $u$ and $u^{*}$ (with coefficients $n$ and $n$).

### Step 3. Every element is a $\mathbb{Z}$-linear combination of unitaries.

Let $a \in \mathcal{A}$ be arbitrary. Decompose $a$ into its self-adjoint parts:

$$
a = b + ic, \qquad b = \frac{a + a^{*}}{2}, \quad c = \frac{a - a^{*}}{2i},
$$

where $b$ and $c$ are self-adjoint. By Step 2, there exist unitaries $u_j, v_k \in \mathcal{A}$ and integers $n_j, m_k \in \mathbb{Z}$ such that

$$
b = \sum_j n_j \, u_j, \qquad c = \sum_k m_k \, v_k.
$$

**Key observation:** if $v$ is unitary, then $iv$ is also unitary, since

$$
(iv)^{*}(iv) = (-i)v^{*} \cdot (iv) = v^{*}v = 1, \qquad (iv)(iv)^{*} = (iv)(-i)v^{*} = vv^{*} = 1.
$$

Therefore

$$
a = b + ic = \sum_j n_j \, u_j + \sum_k m_k \, (i \, v_k),
$$

which is a $\mathbb{Z}$-linear combination of unitaries (the $u_j$'s and the $iv_k$'s). This completes the proof of the Lemma. $\blacksquare$

---

## Proof of the Claim.

Suppose $A \otimes_{\min} B$ is a $Z^{*}$-algebra.

1. **$A \otimes_{\min} B$ is unital.** By definition, a $Z^{*}$-algebra is a unital $C^{*}$-algebra in which every element is a $\mathbb{Z}$-linear combination of unitaries. The existence of unitaries requires a unit, so $A \otimes_{\min} B$ is unital.

2. **$A$ and $B$ are unital.** The minimal tensor product $A \otimes_{\min} B$ is unital if and only if both $A$ and $B$ are unital, with unit $1_{A \otimes_{\min} B} = 1_A \otimes 1_B$.

3. **$A$ and $B$ are $Z^{*}$-algebras.** By the Lemma, every unital $C^{*}$-algebra is a $Z^{*}$-algebra. Since $A$ and $B$ are unital $C^{*}$-algebras, both are $Z^{*}$-algebras.

Therefore, if $A \otimes_{\min} B$ is a $Z^{*}$-algebra, then **both** $A$ and $B$ are $Z^{*}$-algebras. In particular, $A$ or $B$ is a $Z^{*}$-algebra.

$$
\boxed{\text{Yes}}
$$

### PROOF COMPLETE
