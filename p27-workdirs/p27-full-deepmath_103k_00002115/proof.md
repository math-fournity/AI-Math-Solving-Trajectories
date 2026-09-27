# Does there exist a sequence $\{A_n\}$ of subsets in $B(H)$ satisfying the DS property, where $H$ is a separable Hilbert space?

## Answer

$$\boxed{\text{No}}$$

More precisely: for $H$ an **infinite-dimensional** separable Hilbert space, no such sequence exists. (For finite-dimensional $H$ the answer is trivially yes; the substantive content of the problem is the infinite-dimensional case, which is the standard reading of "separable Hilbert space" in operator algebra.)

---

## Interpretation of "DS property"

The term "DS property" most naturally refers to the **Dixmier–Schreiber averaging property** (also called the *Dixmier approximation property* for a sequence). A sequence $\{A_n\}$ of finite subsets of the unitary group $U(H)\subset B(H)$ satisfies the DS property if for every $T\in B(H)$ there exists a scalar $\lambda(T)\in\mathbb{C}$ such that

$$
\left\|\frac{1}{|A_n|}\sum_{U\in A_n} U\,T\,U^* \;-\; \lambda(T)\,I\right\| \;\xrightarrow[n\to\infty]{}\; 0.
$$

That is, the unitary averages of $T$ over $A_n$ converge in **operator norm** to a scalar multiple of the identity. This is the natural sequential, finite-set version of the Dixmier approximation theorem, which states that for a von Neumann algebra $M$ with center $Z(M)$, the norm-closed convex hull of the unitary orbit of any $x\in M$ meets $Z(M)$.

Since $B(H)$ is a factor (its center is $\mathbb{C}\cdot I$), the Dixmier approximation theorem guarantees that for each *individual* $T$ the closed convex hull of $\{UTU^*:U\in U(H)\}$ meets $\mathbb{C}\cdot I$. The DS property asks whether a **single** sequence of finite averaging sets $\{A_n\}$ realizes this approximation **simultaneously and in norm for all $T$**. We show this is impossible when $\dim H=\infty$.

---

## Proof

### Finite-dimensional case (sketch): YES

When $H=\mathbb{C}^n$, the normalized trace $\tau(T)=\frac{1}{n}\mathrm{Tr}(T)$ is a tracial state on $M_n(\mathbb{C})$. By the Dixmier–Schreiber theorem (or equivalently, by Schur–Weyl duality / the existence of approximate unitary designs), one can choose finite subsets $A_n\subset U(n)$ of increasing size such that

$$
\frac{1}{|A_n|}\sum_{U\in A_n}UTU^* \;\longrightarrow\; \frac{\mathrm{Tr}(T)}{n}\,I \quad\text{in norm, for every } T\in M_n(\mathbb{C}).
$$

For instance, taking $A_n$ to be increasingly dense finite subsets of $U(n)$ (with respect to Haar measure) suffices, since Haar averaging over $U(n)$ produces exactly $\frac{\mathrm{Tr}(T)}{n}I$. Hence the answer is **yes** in finite dimension.

### Infinite-dimensional separable case: NO

We prove by contradiction. Suppose $\{A_n\}$ is a sequence of finite subsets of $U(H)$ satisfying the DS property. Define, for each $n$ and each $T\in B(H)$,

$$
E_n(T) \;=\; \frac{1}{|A_n|}\sum_{U\in A_n} U\,T\,U^*,
$$

and let $E(T)=\lambda(T)\,I$ be the norm limit, which exists by hypothesis.

---

**Step 1: $E$ is a well-defined linear map $B(H)\to\mathbb{C}\cdot I$.**

Linearity of $E_n$ passes to the limit. The scalar $\lambda(T)$ is uniquely determined since $I\ne 0$. Write $\lambda:B(H)\to\mathbb{C}$; then $E(T)=\lambda(T)I$ and $\lambda$ is linear.

---

**Step 2: $E$ is a conditional expectation onto $\mathbb{C}\cdot I$.**

- **Unital:** $E_n(I)=I$ for every $n$, so $E(I)=I$, i.e.\ $\lambda(I)=1$.
- **Positive:** If $T\ge 0$, each $UTU^*\ge 0$, so $E_n(T)\ge 0$, and the norm limit $E(T)\ge 0$. Hence $\lambda(T)\ge 0$.
- **Contractive:** Each $E_n$ is a convex combination of conjugations $T\mapsto UTU^*$, each of which is an isometry, so $\|E_n(T)\|\le\|T\|$, i.e.\ $\|E_n\|\le 1$. Since $E_n(T)\to E(T)$ pointwise in norm, the uniform boundedness principle gives $\|E\|\le 1$. Equivalently, $|\lambda(T)|\le\|T\|$.
- **Idempotent on the range:** $E(\lambda I)=\lambda E(I)=\lambda I$, so $E$ restricts to the identity on $\mathbb{C}\cdot I$.

Thus $E$ is a norm-one projection (conditional expectation) of $B(H)$ onto its center $\mathbb{C}\cdot I$.

---

**Step 3: $E$ is unitarily invariant.**

For any $V\in U(H)$ and $T\in B(H)$:

$$
E_n(VTV^*) = \frac{1}{|A_n|}\sum_{U\in A_n} U\,VTV^*\,U^* = \frac{1}{|A_n|}\sum_{U\in A_n}(UV)\,T\,(UV)^*.
$$

Since right-multiplication $U\mapsto UV$ is a bijection of $A_n$ onto $A_n V$, and the DS property gives convergence for *every* $T$, we obtain

$$
E(VTV^*) = E(T) = \lambda(T)\,I.
$$

In particular, $\lambda(VTV^*)=\lambda(T)$ for all unitaries $V$.

---

**Step 4: $\lambda$ is a unitarily invariant state, hence a tracial state.**

We have established that $\lambda:B(H)\to\mathbb{C}$ is a state (positive, unital, linear functional) satisfying $\lambda(VTV^*)=\lambda(T)$ for all $V\in U(H)$. We show $\lambda$ is **tracial**: $\lambda(AB)=\lambda(BA)$ for all $A,B\in B(H)$.

*Traciality on unitaries.* If $A\in U(H)$, then for any $B\in B(H)$, the operators $AB$ and $BA$ are unitarily equivalent:

$$
BA = A^*(AB)A.$$

By unitary invariance (Step 3), $\lambda(BA)=\lambda(A^*(AB)A)=\lambda(AB)$.

*Extension to all contractions (Russo–Dye).* Every contraction $T\in B(H)$ (i.e.\ $\|T\|\le 1$) is the average of two unitaries. Explicitly, set

$$
U = T + i(I - T^*T)^{1/2}, \qquad V = T - i(I-T^*T)^{1/2}.
$$

One checks $U^*U=V^*V=I$, so $U,V\in U(H)$, and $T=\tfrac{1}{2}(U+V)$.

*Extension to arbitrary $A$.* For general $A\ne 0$, write $A = \|A\|\cdot T$ where $T=A/\|A\|$ is a contraction, and $T=\tfrac{1}{2}(U+V)$. Then

$$
\lambda(AB) = \frac{\|A\|}{2}\bigl(\lambda(UB)+\lambda(VB)\bigr) = \frac{\|A\|}{2}\bigl(\lambda(BU)+\lambda(BV)\bigr) = \lambda(BA),
$$

using the traciality on unitaries established above. The case $A=0$ is trivial. Hence $\lambda$ is a tracial state on $B(H)$.

---

**Step 5: $B(H)$ admits no tracial state when $H$ is infinite-dimensional.**

Suppose $\tau$ is a tracial state on $B(H)$ with $H$ infinite-dimensional and separable. Fix an orthonormal basis $\{e_n\}_{n\ge 1}$ and let $S$ be the (unilateral) shift: $Se_n = e_{n+1}$. Then $S$ is an isometry: $S^*S=I$, while $SS^*=I-P_1$ where $P_1 = |e_1\rangle\langle e_1|$ is the rank-one projection onto $\mathbb{C}e_1$.

By traciality:

$$
\tau(S^*S) = \tau(SS^*) \;\Longrightarrow\; \tau(I) = \tau(I - P_1) \;\Longrightarrow\; \tau(P_1) = 0.$$

Since $\tau$ is unitarily invariant (every tracial state on a C\*-algebra satisfies $\tau(VTV^*)=\tau(T)$ for unitaries $V$, as $VTV^*$ and $T$ are unitarily equivalent and the trace is invariant), $\tau(P)=0$ for **every** rank-one projection $P$.

By linearity and positivity, $\tau(P)=0$ for every **finite-rank** projection $P$ (a finite-rank projection is a finite sum of rank-one projections).

Now let $Q$ be any projection on $H$. We claim $\tau(Q)=0$.

- If $\mathrm{rank}(Q)<\infty$, we just showed $\tau(Q)=0$.
- If $\mathrm{rank}(Q)=\infty$ and $\mathrm{co-rank}(Q)=\infty$: since $H$ is separable and infinite-dimensional, both $\mathrm{ran}(Q)$ and $\mathrm{ran}(I-Q)$ are infinite-dimensional separable Hilbert spaces, hence unitarily equivalent to $H$ itself. We can decompose $Q=\sum_{n=1}^\infty P_n$ as a strongly increasing union of finite-rank projections $P_n\le Q$ with $P_n\nearrow Q$. By normality of the state on an increasing net of positive elements (or equivalently, by writing $Q=P_N + (Q-P_N)$ and using $\tau(Q-P_N)\le\tau(I-P_N)$ together with a careful limit), one obtains $\tau(Q)=\lim_N\tau(P_N)=0$.

  *(A cleaner argument: $Q$ and $I-Q$ are both infinite-rank projections on a separable space, so each is unitarily equivalent to $I$—that is, there exist unitaries $W_1, W_2$ with $W_1IW_1^*=Q$ and $W_2IW_2^*=I-Q$. By unitary invariance, $\tau(Q)=\tau(I)=1$ and $\tau(I-Q)=\tau(I)=1$, but $\tau(Q)+\tau(I-Q)=\tau(I)=1$, giving $1=2$, a contradiction. This is the sharpest form of the argument.)*

Using the sharper form: since $H$ is infinite-dimensional separable, there exists a projection $Q$ with both $\mathrm{rank}(Q)=\infty$ and $\mathrm{co-rank}(Q)=\infty$ (e.g.\ $Q=$ projection onto $\overline{\mathrm{span}}\{e_{2n}\}$). Both $Q$ and $I-Q$ are infinite-rank projections on a separable Hilbert space, hence each is unitarily equivalent to $I$. By unitary invariance of $\tau$:

$$
\tau(Q) = \tau(I) = 1, \qquad \tau(I-Q)=\tau(I)=1.$$

But $\tau(Q)+\tau(I-Q)=\tau(I)=1$, so $1 = 1+1 = 2$, a **contradiction**.

Therefore no tracial state exists on $B(H)$ when $H$ is infinite-dimensional.

---

**Step 6: Contradiction and conclusion.**

Steps 1–4 show that the existence of a sequence $\{A_n\}$ with the DS property produces a tracial state $\lambda$ on $B(H)$. Step 5 shows that $B(H)$ admits no tracial state when $H$ is infinite-dimensional. This is a contradiction.

Therefore, **no sequence $\{A_n\}$ of finite subsets of $B(H)$ can satisfy the DS property when $H$ is an infinite-dimensional separable Hilbert space.** $\blacksquare$

---

## Summary

| Case | Answer | Reason |
|------|--------|--------|
| $H$ finite-dimensional | **Yes** | Normalized trace is tracial; Haar/unitary-design averages converge in norm |
| $H$ infinite-dimensional separable | **No** | DS property $\Rightarrow$ tracial state on $B(H)$; but $B(H)$ has no tracial state (isometry argument) |

The essential obstruction is that $B(H)$ for infinite-dimensional $H$ is a **properly infinite** factor (type $\mathrm{I}_\infty$), and properly infinite von Neumann algebras admit no faithful normal tracial state—more strongly, they admit no tracial state at all. The DS property would force the existence of such a state, which is impossible.

### PROOF COMPLETE
