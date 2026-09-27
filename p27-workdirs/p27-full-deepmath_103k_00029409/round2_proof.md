# Theorem

Let \(X\) be a 0-dimensional subset of \(\mathbb{R}^n\). If \(U = \mathbb{R}^n \setminus X\) is homeomorphic to \(\mathbb{R}^n\), then \(X\) is empty.

## Proof

Assume \(\mathbb{R}^n \setminus X \cong \mathbb{R}^n\), and let \(h: \mathbb{R}^n \to \mathbb{R}^n \setminus X\) be a homeomorphism. We treat the cases \(n \geq 1\) (the main argument) and \(n = 0\) (trivial) separately.

### Step 1. \(X\) is closed in \(\mathbb{R}^n\) (Invariance of Domain)

Viewing \(h\) as a continuous injective map \(\mathbb{R}^n \to \mathbb{R}^n\), the **Invariance of Domain** theorem implies that \(h(\mathbb{R}^n) = \mathbb{R}^n \setminus X\) is open in \(\mathbb{R}^n\). Consequently

\[
X = \mathbb{R}^n \setminus (\mathbb{R}^n \setminus X)
\]

is closed in \(\mathbb{R}^n\).

### Step 2. Pass to the one-point compactification

Let \(S^n = \mathbb{R}^n \cup \{\infty\}\) be the one-point compactification of \(\mathbb{R}^n\), and set

\[
X^* := X \cup \{\infty\} \subset S^n.
\]

Since \(X\) is closed in \(\mathbb{R}^n\), the complement

\[
S^n \setminus X^* = \mathbb{R}^n \setminus X
\]

is open in \(\mathbb{R}^n\), hence open in \(S^n\). Therefore \(X^*\) is closed in the compact space \(S^n\), so \(X^*\) is **compact**. Moreover, as a set (and in fact as a topological space),

\[
\mathbb{R}^n \setminus X = S^n \setminus X^*.
\]

### Step 3. \(X^*\) is 0-dimensional

We consider two cases.

- **\(X\) is compact (bounded).** Then \(\infty\) is an isolated point of \(X^*\) (since \(X\) is bounded, a neighborhood of \(\infty\) in \(S^n\) is disjoint from \(X\)). Thus \(X^* = X \sqcup \{\infty\}\) is a disjoint union of two 0-dimensional spaces, hence 0-dimensional.

- **\(X\) is unbounded.** Being closed in \(\mathbb{R}^n\), \(X\) is locally compact Hausdorff. A 0-dimensional locally compact Hausdorff space admits a basis of compact clopen sets. From this it follows that the one-point compactification \(X^+ = X \cup \{\infty\}\) is again 0-dimensional: every point of \(X\) has a compact clopen neighborhood in \(X\) (which remains clopen in \(X^+\)), and neighborhoods of \(\infty\) of the form \(X^+ \setminus K\) with \(K \subset X\) compact clopen are themselves clopen. Since \(X^* = X^+\) in this case, \(X^*\) is 0-dimensional.

In either case, \(X^*\) is a **compact, 0-dimensional** (hence totally disconnected) Hausdorff space.

### Step 4. Apply Alexander duality

By the **Alexander duality theorem** (with Čech cohomology on the right-hand side), for any compact subset \(K \subset S^n\),

\[
\widetilde{H}_i(S^n \setminus K;\, \mathbb{Z}) \;\cong\; \widetilde{H}^{\,n-i-1}(K;\, \mathbb{Z}) \qquad \text{for all } i.
\]

Apply this with \(K = X^*\). Since \(X^*\) is 0-dimensional and compact:

- \(\widetilde{H}^{\,j}(X^*) = 0\) for all \(j \geq 1\) (there are no cochains in positive degree on a 0-dimensional space),
- \(\widetilde{H}^{\,0}(X^*) \cong \mathbb{Z}^{\,c(X^*)-1}\), where \(c(X^*)\) denotes the number of connected components of \(X^*\).

(For a compact Hausdorff space, \(\widetilde{H}^0 = 0\) if and only if the space is connected — this holds regardless of whether the number of components is finite or infinite, since Čech \(\widetilde{H}^0\) vanishes exactly when every locally constant function is constant, i.e., when the space is connected.)

Therefore, with \(S^n \setminus X^* = \mathbb{R}^n \setminus X\):

\[
\widetilde{H}_{n-1}(\mathbb{R}^n \setminus X) \cong \widetilde{H}^{\,0}(X^*), \qquad
\widetilde{H}_i(\mathbb{R}^n \setminus X) = 0 \;\text{ for } i \neq n-1.
\]

### Step 5. Conclude \(X = \emptyset\)

By hypothesis \(\mathbb{R}^n \setminus X \cong \mathbb{R}^n\), and \(\mathbb{R}^n\) is contractible, so all reduced homology groups of \(\mathbb{R}^n \setminus X\) vanish. In particular,

\[
\widetilde{H}_{n-1}(\mathbb{R}^n \setminus X) = 0,
\]

which forces

\[
\widetilde{H}^{\,0}(X^*) = 0.
\]

As noted above, this means \(X^*\) is **connected**. But \(X^*\) is 0-dimensional and compact, hence **totally disconnected**. A space that is both connected and totally disconnected must be a single point. Since \(\infty \in X^*\), we conclude

\[
X^* = \{\infty\}, \qquad \text{and hence} \qquad X = \emptyset.
\]

### The case \(n = 0\)

\(\mathbb{R}^0\) is a single point. The only 0-dimensional subsets are \(\emptyset\) and \(\{\text{pt}\}\). We have \(\mathbb{R}^0 \setminus \emptyset = \{\text{pt}\} \cong \mathbb{R}^0\), while \(\mathbb{R}^0 \setminus \{\text{pt}\} = \emptyset \not\cong \mathbb{R}^0\). Hence \(X = \emptyset\) in this case as well. \(\blacksquare\)

## Answer

\[
\boxed{X = \emptyset}
\]

### PROOF COMPLETE
