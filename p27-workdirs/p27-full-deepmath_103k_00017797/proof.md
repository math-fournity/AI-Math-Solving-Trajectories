# Can a continuous projection in a topological vector space be closed but not open?

**Answer:** $\boxed{\text{Yes}}$

---

## Setup and definitions

Let $X$ be a topological vector space (TVS) over $\mathbb{R}$ (the argument over $\mathbb{C}$ is identical). Recall:

- A **projection** is a continuous linear map $P:X\to X$ with $P^{2}=P$.
- $P$ is **closed** (as a map $X\to X$) if $P(F)$ is closed in $X$ for every closed $F\subseteq X$.
- $P$ is **open** (as a map $X\to X$) if $P(U)$ is open in $X$ for every open $U\subseteq X$.

We exhibit a concrete continuous projection that is closed but not open.

---

## The example

Take $X=\mathbb{R}$ with its usual (Hausdorff, non-discrete) topology, and let

$$
P:X\to X,\qquad P(x)=0\quad\text{for all }x\in X.
$$

### $P$ is a continuous projection

- **Linearity.** $P(\lambda x+\mu y)=0=\lambda P(x)+\mu P(y)$.
- **Idempotence.** $P^{2}(x)=P(P(x))=P(0)=0=P(x)$, so $P^{2}=P$.
- **Continuity.** $P$ is the constant zero map, hence continuous (the preimage of every open set is either $\emptyset$ or $X$, both open).

### $P$ is closed

Let $F\subseteq X$ be any closed set. Then

$$
P(F)=\{0\}.
$$

Since $X=\mathbb{R}$ is Hausdorff, the singleton $\{0\}$ is closed in $X$. Therefore $P(F)$ is closed for every closed $F$, and $P$ is a closed map.

### $P$ is not open

Let $U\subseteq X$ be any non-empty open set (such a set exists since $X$ is non-discrete, e.g. $U=X$ or $U=(-1,1)$). Then

$$
P(U)=\{0\}.
$$

Because $X=\mathbb{R}$ is **non-discrete**, the singleton $\{0\}$ is **not open** in $X$. Hence $P(U)$ is not open, and $P$ is not an open map.

---

## Conclusion

The zero projection $P=0$ on $X=\mathbb{R}$ (with the usual topology) is a continuous projection that is **closed but not open**. Therefore a continuous projection in a topological vector space **can** be closed but not open.

$$
\boxed{\text{Yes}}
$$

### PROOF COMPLETE
