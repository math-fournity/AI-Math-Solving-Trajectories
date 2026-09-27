# Proof: Existence of a meager set $S$ with $G_S$ connected and infinite diameter

## Answer

**Yes**, such a set exists. We construct $S = \{2^k,\; 2^k+1 : k \geq 1\}$ and verify all three required properties.

**Interpretation of "meager."** We interpret "meager" as *asymptotic density zero*: $d(S) = \lim_{N\to\infty} \frac{|S \cap [1,N]|}{N} = 0$. This is the natural reading, since in the discrete topology on $\mathbb{N}$ every nonempty set is open (hence not nowhere-dense), so the only topologically meager set is $\emptyset$, which cannot yield a connected graph.

We take $\mathbb{N} = \{1, 2, 3, \ldots\}$. The sum-graph is $G_S = (\mathbb{N}, E)$ with $E = \bigl\{\{a,b\} : a \neq b,\; a+b \in S\bigr\}$.

---

## 1. $S$ is meager (density zero)

For $N \geq 2$, the elements of $S$ up to $N$ are among $\{2^k : 1 \leq k \leq \lfloor\log_2 N\rfloor\} \cup \{2^k+1 : 1 \leq k \leq \lfloor\log_2(N-1)\rfloor\}$, so

$$|S \cap [1,N]| \;\leq\; 2\lfloor \log_2 N \rfloor + 2.$$

Therefore

$$\frac{|S \cap [1,N]|}{N} \;\leq\; \frac{2\log_2 N + 2}{N} \;\xrightarrow{N\to\infty}\; 0.$$

Hence $d(S) = 0$; $S$ is meager. $\checkmark$

---

## 2. $G_S$ is connected

We use a general sufficient condition.

> **Lemma (Connectivity criterion).** *If $S \subseteq \mathbb{N}$ satisfies $S \cap (n,\, 2n) \neq \emptyset$ for every $n \geq 2$, then $G_S$ is connected.*

*Proof of Lemma.* For any $n \geq 2$, pick $s \in S \cap (n, 2n)$. Set $m = s - n$. Then:
- $m > 0$ since $s > n$,
- $m < n$ since $s < 2n$,
- $m \neq n$ since $s \neq 2n$ (as $s < 2n$),
- $n + m = s \in S$, so $\{n, m\} \in E$.

Thus every vertex $n \geq 2$ is adjacent to a strictly smaller positive vertex $m < n$. By induction, every vertex has a path to vertex $1$. Since the graph is undirected, $1$ is connected to every vertex. $\square$

**Verification for our $S$.** Let $n \geq 2$ and set $k = \lfloor \log_2 n \rfloor$, so $2^k \leq n < 2^{k+1}$.

- **Case $n = 2^k$:** Then $2^k + 1 \in S$ and $2^k < 2^k + 1 < 2^{k+1} = 2n$, so $2^k+1 \in S \cap (n, 2n)$. $\checkmark$

- **Case $2^k < n < 2^{k+1}$:** Then $2^{k+1} \in S$. We have $n < 2^{k+1}$ (so $2^{k+1} > n$) and $2n > 2 \cdot 2^k = 2^{k+1}$ (so $2^{k+1} < 2n$). Hence $2^{k+1} \in S \cap (n, 2n)$. $\checkmark$

The criterion applies, so $G_S$ is connected. $\checkmark$

---

## 3. $\operatorname{diam}(G_S) = \infty$

Since $G_S$ is connected, it suffices to show that distances from vertex $1$ are unbounded: $\sup_{v \in \mathbb{N}} d(1, v) = \infty$.

### 3.1. The block-count invariant

For a positive integer $n$, let $\operatorname{blocks}(n)$ denote the number of **maximal runs of consecutive 1s** in the binary representation of $n$.

*Examples:* $\operatorname{blocks}(2^k) = 1$, $\operatorname{blocks}(2^k - 1) = 1$, $\operatorname{blocks}(5) = \operatorname{blocks}(101_2) = 2$, $\operatorname{blocks}(21) = \operatorname{blocks}(10101_2) = 3$.

> **Lemma 1 (Reflection bound).** *For any positive integer $v$ and any $k$ with $2^k > v$,*
> $$\operatorname{blocks}(2^k - v) \;\leq\; \operatorname{blocks}(v) + 1.$$

*Proof.* Write $v$ in $k$ bits (padding with leading zeros): $v = (b_{k-1} \cdots b_0)_2$ with $b_{k-1} = \cdots = b_\ell = 0$ and $b_{\ell-1} = 1$ where $\ell = \lfloor \log_2 v \rfloor + 1$.

**Step 1: Complement.** The bitwise complement in $k$ bits is $\overline{v} = 2^k - 1 - v = (1-b_{k-1}) \cdots (1-b_0)_2$. The top $k - \ell$ bits of $\overline{v}$ are all $1$, and bit $\ell - 1$ of $\overline{v}$ is $0$ (since $b_{\ell-1} = 1$). So the leading $k-\ell$ ones form one complete block.

The remaining $\ell$ bits of $\overline{v}$ are the complement of $v$'s $\ell$-bit representation. The number of 1-blocks in this complement equals the number of 0-blocks in $v$'s $\ell$-bit representation. Since $v$'s representation starts with $1$ (bit $\ell - 1$):

- If $v$ is **odd** ($b_0 = 1$): $v$'s bits start and end with $1$, so 0-blocks $=$ 1-blocks $- 1 = \operatorname{blocks}(v) - 1$. Thus $\operatorname{blocks}(\overline{v}) = 1 + (\operatorname{blocks}(v) - 1) = \operatorname{blocks}(v)$.
- If $v$ is **even** ($b_0 = 0$): $v$'s bits start with $1$, end with $0$, so 0-blocks $=$ 1-blocks $= \operatorname{blocks}(v)$. Thus $\operatorname{blocks}(\overline{v}) = 1 + \operatorname{blocks}(v)$.

**Step 2: Add 1.** We have $2^k - v = \overline{v} + 1$. Adding $1$ to any non-negative integer $w$ changes $\operatorname{blocks}(w)$ by at most $+1$: if $w$ has $t \geq 0$ trailing 1s, then $w+1$ flips them to $0$ and sets bit $t$ to $1$; this destroys one trailing 1-block and creates at most one new block, so the net increase is at most $1$ (achieved only when $t = 0$, i.e., $w$ is even).

- If $v$ is **odd**: $\overline{v}$ is **even** (last bit $1 - 1 = 0$), so adding $1$ can increase blocks by at most $1$: $\operatorname{blocks}(2^k - v) \leq \operatorname{blocks}(v) + 1$. $\checkmark$
- If $v$ is **even**: $\overline{v}$ is **odd** (last bit $1 - 0 = 1$), so $t \geq 1$ and adding $1$ does **not** increase blocks: $\operatorname{blocks}(2^k - v) \leq \operatorname{blocks}(\overline{v}) = \operatorname{blocks}(v) + 1$. $\checkmark$

In both cases, $\operatorname{blocks}(2^k - v) \leq \operatorname{blocks}(v) + 1$. $\square$

> **Lemma 2 (Shifted reflection bound).** *For any positive integer $v$ and any $k$ with $2^k + 1 > v$,*
> $$\operatorname{blocks}(2^k + 1 - v) \;\leq\; \operatorname{blocks}(v) + 2.$$

*Proof.* Set $w = 2^k - v$. By Lemma 1, $\operatorname{blocks}(w) \leq \operatorname{blocks}(v) + 1$. Since $2^k + 1 - v = w + 1$ and adding $1$ increases blocks by at most $1$:

$$\operatorname{blocks}(2^k + 1 - v) \leq \operatorname{blocks}(w) + 1 \leq \operatorname{blocks}(v) + 2. \quad\square$$

### 3.2. Bounding blocks along paths

A path of length $d$ from vertex $1$ to vertex $v$ is a sequence $1 = u_0, u_1, \ldots, u_d = v$ where each $\{u_{i-1}, u_i\} \in E$, meaning $u_{i-1} + u_i = s_i \in S$ for some $s_i \in \{2^{k_i},\, 2^{k_i}+1\}$. Thus $u_i = s_i - u_{i-1}$.

By Lemmas 1 and 2, each step increases the block count by at most $2$:

$$\operatorname{blocks}(u_i) \leq \operatorname{blocks}(u_{i-1}) + 2.$$

Since $\operatorname{blocks}(1) = 1$, by induction:

$$\operatorname{blocks}(v) = \operatorname{blocks}(u_d) \leq 1 + 2d.$$

Therefore, any vertex $v$ with $\operatorname{blocks}(v) = M$ satisfies $d(1, v) \geq \frac{M - 1}{2}$.

### 3.3. Vertices with arbitrarily many blocks

For each $M \geq 1$, define

$$v_M \;=\; \sum_{j=0}^{M-1} 4^j \;=\; \frac{4^M - 1}{3}.$$

In binary, $v_M = \underbrace{10\,10\,10 \cdots 10\,1}_{M \text{ ones}}{}_2$: the bits at positions $0, 2, 4, \ldots, 2(M-1)$ are $1$ and all others are $0$. Each $1$ is an isolated block, so

$$\operatorname{blocks}(v_M) = M.$$

By the bound above:

$$d(1,\, v_M) \;\geq\; \frac{M - 1}{2}.$$

As $M \to \infty$, $d(1, v_M) \to \infty$. Since $\operatorname{diam}(G_S) \geq d(1, v_M)$ for every $M$:

$$\operatorname{diam}(G_S) = \infty. \quad\checkmark$$

---

## Conclusion

The set $S = \{2^k,\; 2^k + 1 : k \geq 1\}$ satisfies all three required properties:

1. **$S$ is meager**: $|S \cap [1,N]| = O(\log N)$, so $d(S) = 0$.
2. **$G_S$ is connected**: $S \cap (n, 2n) \neq \emptyset$ for all $n \geq 2$, so the connectivity criterion applies.
3. **$\operatorname{diam}(G_S) = \infty$**: the block-count invariant gives $d(1, v_M) \geq (M-1)/2 \to \infty$.

$$\boxed{\text{Yes, such a set } S \text{ exists.}}$$

### PROOF COMPLETE
