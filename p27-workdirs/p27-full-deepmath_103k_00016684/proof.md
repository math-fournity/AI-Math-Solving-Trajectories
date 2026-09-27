# Proof

**Answer: No.** In general, contractibility of the interior region does *not* imply that $S$ is diffeomorphic to a sphere. A counterexample exists for $N \geq 6$.

## Step 1. Setup and notation

Let $U$ be the interior region of $S$, i.e. the bounded connected component of $\mathbb{R}^N \setminus S$, and let $M = \overline{U} = U \cup S$. Then $M$ is a compact smooth $N$-manifold with boundary $\partial M = S$.

**Key fact.** A compact manifold with boundary is homotopy equivalent to its interior: using a collar neighborhood $\partial M \times [0,1) \hookrightarrow M$ one pushes $M$ into $\operatorname{int}(M) = U$ by an inward deformation retraction. Hence
$$
M \simeq U.
$$
Since $U$ is contractible by hypothesis, $M$ is contractible.

## Step 2. $S$ is an integral homology $(N{-}1)$-sphere

Consider the long exact sequence of the pair $(M, S)$:
$$
\cdots \to H_i(S) \to H_i(M) \to H_i(M, S) \to H_{i-1}(S) \to \cdots
$$
By Poincaré–Lefschetz duality for the compact orientable manifold $M$ with boundary,
$$
H_i(M, S) \cong H^{N-i}(M).
$$
Since $M$ is contractible, $H^{N-i}(M) = 0$ for $N - i \geq 1$ (i.e. $i \leq N-1$) and $H^0(M) \cong \mathbb{Z}$.

From the long exact sequence:
- For $1 \leq i \leq N-2$: both $H_i(M) = 0$ and $H_i(M,S) = 0$, so $H_i(S) = 0$.
- $H_{N-1}(S) \cong H_{N-1}(M, S) \cong H^0(M) \cong \mathbb{Z}$.
- $H_0(S) \cong \mathbb{Z}$ (since $S$ is connected, being the boundary of a compact manifold).

Therefore
$$
H_*(S;\,\mathbb{Z}) \cong H_*(S^{N-1};\,\mathbb{Z}),
$$
i.e. $S$ is an integral homology $(N{-}1)$-sphere.

## Step 3. Low-dimensional cases ($N \leq 3$): the answer is Yes

- **$N = 1$:** $S$ is a finite set of points; the bounded component is an interval (contractible) only when $S$ consists of two points, so $S \cong S^0$.
- **$N = 2$:** $S$ is a smooth simple closed curve. By the smooth Jordan–Schoenflies theorem, $S$ is diffeomorphic to $S^1$.
- **$N = 3$:** $S$ is a homology $2$-sphere, i.e. a closed orientable surface with $H_1 = 0$. By the classification of compact surfaces, the only such surface is $S^2$, and the unique smooth structure on $S^2$ is the standard one. So $S \cong S^2$.

These cases do not settle the general question, which is asked for arbitrary $N$.

## Step 4. Counterexample for $N \geq 6$

We construct a smooth compact hypersurface $S \subset \mathbb{R}^N$ with contractible interior that is **not** diffeomorphic to $S^{N-1}$.

### 4a. A non-simply-connected homology sphere

By a theorem of Kervaire (*Smooth homology spheres and their fundamental groups*, 1969):

> **Theorem (Kervaire).** For $n \geq 5$, every finitely presented superperfect group $G$ (i.e. $H_1(G) = H_2(G) = 0$) arises as the fundamental group of a homology $n$-sphere.

Take $G$ to be the **binary icosahedral group** $2I$ of order $120$: this is the fundamental group of the Poincaré homology $3$-sphere and is superperfect ($H_1(2I) = H_2(2I) = 0$). For $N \geq 6$ (so $n = N-1 \geq 5$), Kervaire's theorem gives a smooth homology $(N{-}1)$-sphere $\Sigma$ with
$$
\pi_1(\Sigma) \cong 2I \neq 0.
$$
In particular $\Sigma$ is **not** diffeomorphic (not even homeomorphic) to $S^{N-1}$.

### 4b. $\Sigma$ bounds a contractible $N$-manifold

A second part of Kervaire's theorem states:

> **Theorem (Kervaire).** For $n \geq 5$, every homology $n$-sphere bounds a contractible $(n{+}1)$-manifold.

**Construction sketch.** Start with $\Sigma \times [0,1]$. Attach $2$-handles to $\Sigma \times \{1\}$ along generators of $\pi_1(\Sigma)$ to kill the fundamental group; this produces an $h$-cobordism from $\Sigma$ to $S^n$ (valid for $n \geq 5$ by general-position and handle-trading arguments). Capping off the $S^n$ boundary component with $B^{n+1}$ yields a homology $(n{+}1)$-ball $W_0$ with $\partial W_0 = \Sigma$. The interior $1$-surgery needed to kill $\pi_1(W_0)$ is performed along embedded circles of codimension $\geq 5$ (here $n+1 \geq 6$), so the attaching spheres $S^{n-1}$ are simply connected and introduce no new fundamental group. The result $W$ is a simply connected homology $(n{+}1)$-ball, hence contractible by Whitehead's theorem. We have $\partial W = \Sigma$.

### 4c. $W$ embeds in $\mathbb{R}^N$

After handle trading, $W$ admits a handle decomposition using only $0$-, $1$-, and $2$-handles. We embed this handlebody into $S^N$ (and hence into $\mathbb{R}^N$ by removing a point away from the image):

- The $0$-handle is a copy of $B^N$.
- Each $1$-handle $D^1 \times D^{N-1}$ is embedded as a "tube" in $S^N \setminus \operatorname{int}(B^N)$ connecting two $(N{-}1)$-disks on $\partial B^N$; the normal bundle of rank $N-1$ is ample.
- Each $2$-handle $D^2 \times D^{N-2}$ has core $D^2 \times \{0\}$, a $2$-disk. To embed the cores disjointly in the $N$-manifold $S^N \setminus \operatorname{int}(M_{\mathrm{current}})$ we use general position: a $2$-disk in an $N$-manifold can be made disjoint from another $2$-disk (and from the existing $1$-skeleton) provided
$$
2 + 2 = 4 < N,
$$
which holds for $N \geq 5$, and in particular for $N \geq 6$. The framing of each $2$-handle (a trivialization of the normal $D^{N-2}$-bundle over $S^1$) extends over the embedded core disk since $\pi_1(SO(N-2))$ presents no obstruction for $N - 2 \geq 4$.

Hence for $N \geq 6$ the entire handlebody $W$ embeds smoothly into $S^N$, and removing a point of $S^N$ not in the image gives a smooth embedding $W \hookrightarrow \mathbb{R}^N$.

### 4d. The counterexample

Set $S := \partial W = \Sigma \subset \mathbb{R}^N$. Then:

- $S$ is a smooth, compact, boundaryless hypersurface in $\mathbb{R}^N$ (by Jordan–Brouwer it separates $\mathbb{R}^N$).
- Its interior region is $\operatorname{int}(W)$, and $\operatorname{int}(W) \simeq W$ is contractible.
- $\pi_1(S) \cong 2I \neq 0$, so $S$ is **not** diffeomorphic to $S^{N-1}$.

This is the desired counterexample.

## Step 5. Conclusion

For $N \geq 6$ there exists a smooth compact hypersurface $S \subset \mathbb{R}^N$ without boundary whose interior is contractible but which is not diffeomorphic to a sphere. Therefore the answer to the question, asked for general $N$, is:

$$
\boxed{\text{No}}
$$

### PROOF COMPLETE
