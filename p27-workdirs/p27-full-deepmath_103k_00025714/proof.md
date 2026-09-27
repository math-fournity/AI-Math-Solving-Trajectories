# Codimension of the Commutator Ideal of $\mathfrak{gl}(V)$ for Infinite-Dimensional $V$

## Answer

$$\boxed{0}$$

That is, $[\mathfrak{gl}(V), \mathfrak{gl}(V)] = \mathfrak{gl}(V)$ when $V$ is infinite-dimensional: every endomorphism is a commutator, so the commutator ideal is the entire algebra and has codimension $0$.

---

## Proof

### Step 1: Finite-dimensional contrast

When $\dim V = n < \infty$, the trace map $\operatorname{tr} \colon \mathfrak{gl}(V) \to k$ satisfies $\operatorname{tr}([A,B]) = 0$ for all $A, B$, while $\operatorname{tr}(I_V) = n \neq 0$. Hence $I_V \notin [\mathfrak{gl}(V), \mathfrak{gl}(V)]$, and in fact $[\mathfrak{gl}(V), \mathfrak{gl}(V)] = \mathfrak{sl}(V)$ (the traceless endomorphisms), giving codimension $1$.

The obstruction is purely the trace: it is a nonzero Lie algebra homomorphism $\mathfrak{gl}(V) \to k$ that vanishes on all commutators.

### Step 2: The trace obstruction vanishes for infinite-dimensional $V$

For infinite-dimensional $V$, there is no nonzero trace on $\mathfrak{gl}(V) = \operatorname{End}(V)$ in the purely algebraic setting. (A trace is a linear functional $\phi$ with $\phi(AB) = \phi(BA)$ for all $A, B$; such a $\phi$ must vanish on every commutator. We will show indirectly that the only trace is zero by showing every element is a commutator.)

### Step 3: Block decomposition of $V$

Let $\kappa = \dim V$ be an infinite cardinal. Since $\aleph_0 \cdot \kappa = \kappa$ for every infinite cardinal $\kappa$, we can decompose

$$V \cong \bigoplus_{n \in \mathbb{Z}} V_n, \qquad V_n \cong V \text{ for each } n \in \mathbb{Z}.$$

Concretely, fix a basis $\mathcal{B}$ of $V$ and partition $\mathcal{B}$ into countably many subsets $\mathcal{B}_n$ ($n \in \mathbb{Z}$), each of cardinality $\kappa$. Set $V_n = \operatorname{span}(\mathcal{B}_n)$.

### Step 4: The block shift operator

Define the **block shift** $S \in \operatorname{End}(V)$ as follows: for each $n \in \mathbb{Z}$, choose an isomorphism $\sigma_n \colon V_n \xrightarrow{\sim} V_{n+1}$, and set

$$S|_{V_n} = \sigma_n \colon V_n \to V_{n+1}.$$

This is a well-defined endomorphism of $V$ (each basis vector maps to a single vector).

### Step 5: Block matrix representation

Under the decomposition $V = \bigoplus_{n \in \mathbb{Z}} V_n$, every $T \in \operatorname{End}(V)$ is represented by a **block matrix** $(T_{mn})_{m,n \in \mathbb{Z}}$ where $T_{mn} \in \operatorname{Hom}(V_n, V_m)$, and the matrix is **column-finite**: for each fixed $n$, only finitely many $T_{mn}$ (as $m$ ranges over $\mathbb{Z}$) are nonzero. This is because $T(v)$ is a finite linear combination of basis vectors for each $v \in V_n$.

Similarly, $S$ has block matrix $S_{m,n} = \delta_{m,n+1} \cdot \sigma_n$ (i.e., $S_{n+1,n} = \sigma_n$ and all other entries zero).

### Step 6: Computing $[S, B]$ in block form

For $B = (B_{mn})$, the products are:

$$(SB)_{mn} = \sum_k S_{mk} B_{kn} = S_{m,\,m-1}\, B_{m-1,\,n} = \sigma_{m-1} \circ B_{m-1,\,n},$$

$$(BS)_{mn} = \sum_k B_{mk} S_{kn} = B_{m,\,n+1}\, S_{n+1,\,n} = B_{m,\,n+1} \circ \sigma_n.$$

To simplify, we may absorb the isomorphisms $\sigma_n$ into the block entries (i.e., identify all $V_n$ with $V$ via fixed isomorphisms, so $\sigma_n = \mathrm{id}$). Then:

$$[S, B]_{mn} = B_{m-1,\,n} - B_{m,\,n+1}.$$

### Step 7: Solving $[S, B] = T$ by recursion

We seek $B$ such that $B_{m-1,\,n} - B_{m,\,n+1} = T_{mn}$ for all $m, n \in \mathbb{Z}$.

**Initial condition:** Set $B_{m,\,0} = 0$ for all $m \in \mathbb{Z}$.

**Forward recursion** ($n \geq 0$): Define

$$B_{m,\,n+1} = B_{m-1,\,n} - T_{mn}.$$

Unrolling:

$$B_{m,\,n} = -\sum_{k=0}^{n-1} T_{m-n+1+k,\; k}, \qquad n > 0.$$

**Backward recursion** ($n < 0$): From $B_{m-1,\,n} = B_{m,\,n+1} + T_{mn}$, setting $n \to n-1$:

$$B_{m,\,n-1} = B_{m+1,\,n} + T_{m+1,\,n-1}.$$

Starting from $B_{m,\,0} = 0$:

$$B_{m,\,-1} = B_{m+1,\,0} + T_{m+1,\,-1} = T_{m+1,\,-1},$$

$$B_{m,\,-2} = B_{m+1,\,-1} + T_{m+1,\,-2} = T_{m+2,\,-1} + T_{m+1,\,-2},$$

and in general:

$$B_{m,\,-p} = \sum_{k=1}^{p} T_{m+k,\; -p+k-1}, \qquad p > 0.$$

### Step 8: Verification of the recursion

We verify $B_{m-1,\,n} - B_{m,\,n+1} = T_{mn}$ in each case.

**Case $n = 0$:** $B_{m-1,\,0} - B_{m,\,1} = 0 - (-T_{m,0}) = T_{m,0}$. ✓

**Case $n > 0$:**

$$B_{m-1,\,n} - B_{m,\,n+1} = \left(-\sum_{k=0}^{n-1} T_{m-1-n+1+k,\; k}\right) - \left(-\sum_{k=0}^{n} T_{m-n+k,\; k}\right)$$

$$= -\sum_{k=0}^{n-1} T_{m-n+k,\; k} + \sum_{k=0}^{n} T_{m-n+k,\; k} = T_{m-n+n,\; n} = T_{m,\,n}. \quad ✓$$

**Case $n = -1$:**

$$B_{m-1,\,-1} - B_{m,\,0} = T_{m,\,-1} - 0 = T_{m,\,-1}. \quad ✓$$

**Case $n = -p$, $p \geq 1$:**

$$B_{m-1,\,-p} - B_{m,\,-p+1} = \sum_{k=1}^{p} T_{m-1+k,\; -p+k-1} - \sum_{k=1}^{p-1} T_{m+k,\; -p+k}$$

Reindex the first sum with $j = k-1$ (so $k = j+1$, $j$ from $0$ to $p-1$):

$$= \sum_{j=0}^{p-1} T_{m+j,\; -p+j} - \sum_{k=1}^{p-1} T_{m+k,\; -p+k}$$

The $j=0$ term is $T_{m,\,-p}$. The remaining terms ($j=1$ to $p-1$) cancel with the second sum ($k=1$ to $p-1$). Result: $T_{m,\,-p} = T_{m,\,n}$. ✓

### Step 9: $B$ is a well-defined endomorphism (column-finiteness)

We must show that for each fixed $n$, only finitely many $B_{m,\,n}$ (as $m$ varies over $\mathbb{Z}$) are nonzero.

**Column $n = 0$:** $B_{m,\,0} = 0$ for all $m$. ✓

**Column $n > 0$:** $B_{m,\,n} = -\sum_{k=0}^{n-1} T_{m-n+1+k,\; k}$. This is a sum over $k \in \{0, 1, \ldots, n-1\}$ (finitely many terms). For each fixed $k$, the column $\{T_{j,\,k}\}_{j \in \mathbb{Z}}$ is column-finite (only finitely many nonzero $T_{j,k}$). So for each $k$, only finitely many values of $m$ make $T_{m-n+1+k,\; k}$ nonzero. The union of finitely many finite sets (over $k = 0, \ldots, n-1$) is finite. Hence only finitely many $B_{m,\,n}$ are nonzero. ✓

**Column $n = -p < 0$:** $B_{m,\,-p} = \sum_{k=1}^{p} T_{m+k,\; -p+k-1}$. Same argument: finitely many $k$ values, each contributing finitely many nonzero terms. ✓

Therefore $B \in \operatorname{End}(V)$.

### Step 10: Conclusion

For every $T \in \operatorname{End}(V) = \mathfrak{gl}(V)$, we have constructed $B \in \operatorname{End}(V)$ such that

$$[S, B] = T.$$

Hence every element of $\mathfrak{gl}(V)$ is a commutator (in fact, a single commutator with the fixed operator $S$). Therefore

$$[\mathfrak{gl}(V),\, \mathfrak{gl}(V)] = \mathfrak{gl}(V),$$

and the codimension of the commutator ideal in $\mathfrak{gl}(V)$ is

$$\boxed{0}.$$

### Remark: the Eilenberg swindle

A particularly elegant special case is $T = I_V$ (the identity). Using the same decomposition $V \cong \bigoplus_{n \in \mathbb{Z}} V_n$, define $S$ as the block shift and $D$ as the weighted block backward shift $D|_{V_n} = n \cdot \sigma_{n-1}^{-1} \colon V_n \to V_{n-1}$. Then for $v \in V_n$:

$$[S, D](v) = S(D(v)) - D(S(v)) = S(n \cdot \sigma_{n-1}^{-1}(v)) - D(\sigma_n(v)) = n \cdot v - (n+1) \cdot v = -v.$$

So $[S, D] = -I_V$, i.e., $I_V = [D, S]$ is a commutator. This is the classical Eilenberg swindle, which exploits the infinite direct sum decomposition to make the "trace" $\sum_n n - \sum_n (n+1)$ telescope to $-1$.

However, the identity being a commutator alone does not suffice (the commutator subspace is a Lie ideal, not an associative ideal). The full strength of Step 7's construction—showing **every** $T$ is a commutator—is what gives codimension $0$.

### PROOF COMPLETE
