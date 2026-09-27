# Proof: $C_p([0,1])$ is not a continuous image of $\mathbb{R}$

## Answer

$$\boxed{\text{No}}$$

$C_p([0,1])$ is **not** a continuous image of $\mathbb{R}$.

---

## Proof

We show that every continuous image of $\mathbb{R}$ is $\sigma$-compact, and then that $C_p([0,1])$ is not $\sigma$-compact.

### Step 1. Every continuous image of $\mathbb{R}$ is $\sigma$-compact.

Write $\mathbb{R} = \bigcup_{n=1}^{\infty} [-n, n]$, where each $[-n,n]$ is compact. If $\varphi: \mathbb{R} \to Y$ is a continuous surjection, then

$$Y = \varphi(\mathbb{R}) = \bigcup_{n=1}^{\infty} \varphi([-n,n]),$$

and each $\varphi([-n,n])$ is compact (continuous image of a compact set). Hence $Y$ is $\sigma$-compact. $\checkmark$

### Step 2. Characterization of compact subsets of $C_p([0,1])$.

Recall that $C_p([0,1])$ carries the subspace topology inherited from the product $\mathbb{R}^{[0,1]}$ (topology of pointwise convergence). A subset $K \subseteq C_p([0,1])$ is compact if and only if:

- $K$ is **closed in** $\mathbb{R}^{[0,1]}$ (not merely in $C_p([0,1])$), and
- $K$ is **pointwise bounded**: for each $x \in [0,1]$, the set $\pi_x(K) = \{f(x) : f \in K\}$ is bounded in $\mathbb{R}$.

*Justification.* If $K$ is compact in $C_p([0,1])$, then $K$ is compact as a subset of the Hausdorff space $\mathbb{R}^{[0,1]}$, hence closed in $\mathbb{R}^{[0,1]}$. Each projection $\pi_x : \mathbb{R}^{[0,1]} \to \mathbb{R}$ is continuous, so $\pi_x(K)$ is compact in $\mathbb{R}$, hence bounded. Conversely, if $K$ is closed in $\mathbb{R}^{[0,1]}$ and pointwise bounded, then $K \subseteq \prod_{x \in [0,1]} \overline{\pi_x(K)}$, a product of compact intervals (hence compact by Tychonoff), and $K$ is a closed subset of this compact product, so $K$ is compact. $\checkmark$

### Step 3. Each compact $K \subseteq C_p([0,1])$ is closed in the sup-norm topology.

Let $\|\cdot\|_\infty$ denote the sup-norm on $C([0,1])$. Suppose $(f_\alpha)$ is a net in $K$ with $\|f_\alpha - f\|_\infty \to 0$ for some $f \in C([0,1])$. Uniform convergence implies pointwise convergence, so $f_\alpha \to f$ in $\mathbb{R}^{[0,1]}$. Since $K$ is closed in $\mathbb{R}^{[0,1]}$ (Step 2), we have $f \in K$. Thus $K$ is closed in the sup-norm topology. $\checkmark$

### Step 4. Each compact $K \subseteq C_p([0,1])$ has empty interior in the sup-norm topology.

Suppose for contradiction that $K$ contains a sup-norm open ball:

$$B_\infty(f_0, r) = \{f \in C([0,1]) : \|f - f_0\|_\infty < r\} \subseteq K$$

for some $f_0 \in C([0,1])$ and $r > 0$. Since $K$ is closed in $\mathbb{R}^{[0,1]}$ (Step 2), $K$ contains the closure of $B_\infty(f_0, r)$ in $\mathbb{R}^{[0,1]}$.

We claim this closure contains a **discontinuous** function. Define

$$g(x) = \begin{cases} f_0(x) + r & \text{if } x = \tfrac{1}{2}, \\ f_0(x) & \text{if } x \neq \tfrac{1}{2}. \end{cases}$$

Then $g$ is discontinuous (at $x = 1/2$) and $|g(x) - f_0(x)| \leq r$ for all $x$.

To show $g \in \overline{B_\infty(f_0, r)}^{\mathbb{R}^{[0,1]}}$: let $U$ be any basic neighborhood of $g$ in $\mathbb{R}^{[0,1]}$, specified by finitely many points $x_1, \dots, x_k \in [0,1]$ and $\varepsilon > 0$:

$$U = \{h \in \mathbb{R}^{[0,1]} : |h(x_i) - g(x_i)| < \varepsilon, \; i = 1, \dots, k\}.$$

We construct a continuous $f \in B_\infty(f_0, r) \cap U$:

- **If $1/2 \notin \{x_1, \dots, x_k\}$**: Take $f = f_0$. Then $\|f - f_0\|_\infty = 0 < r$ and $|f(x_i) - g(x_i)| = 0 < \varepsilon$ for all $i$. $\checkmark$

- **If $1/2 = x_j$ for some $j$**: Set $f(1/2) = f_0(1/2) + r - \varepsilon/2$ and $f(x_i) = f_0(x_i) = g(x_i)$ for $i \neq j$. Extend $f$ to a continuous function on $[0,1]$ by piecewise linear interpolation through the prescribed points $\{(x_i, f(x_i))\} \cup \{(1/2, f(1/2))\}$, ensuring $\|f - f_0\|_\infty \leq r - \varepsilon/2 < r$ (this is possible since all prescribed values of $f - f_0$ lie in $[-(r - \varepsilon/2),\, r - \varepsilon/2]$, and piecewise linear interpolation preserves this bound). Then $f \in B_\infty(f_0, r)$ and $|f(x_i) - g(x_i)| < \varepsilon$ for all $i$. $\checkmark$

So $g \in \overline{B_\infty(f_0, r)}^{\mathbb{R}^{[0,1]}} \subseteq K$. But $g$ is discontinuous, contradicting $K \subseteq C([0,1])$. $\checkmark$

### Step 5. $C_p([0,1])$ is not $\sigma$-compact.

Suppose for contradiction that

$$C_p([0,1]) = \bigcup_{n=1}^{\infty} K_n,$$

where each $K_n$ is compact in $C_p([0,1])$. By Steps 3 and 4, each $K_n$ is **closed** in the sup-norm topology and has **empty interior** in the sup-norm topology.

Now, $C([0,1])$ equipped with the sup-norm $\|\cdot\|_\infty$ is a Banach space (complete normed vector space), hence a **Baire space**. By the Baire Category Theorem, a countable union of closed sets with empty interior in a Baire space has empty interior. Therefore

$$\bigcup_{n=1}^{\infty} K_n$$

has empty interior in $(C([0,1]), \|\cdot\|_\infty)$. But this union equals $C([0,1])$, which has nonempty interior (it is the entire space). **Contradiction.**

Therefore $C_p([0,1])$ is not $\sigma$-compact. $\checkmark$

### Step 6. Conclusion.

By Step 1, every continuous image of $\mathbb{R}$ is $\sigma$-compact. By Step 5, $C_p([0,1])$ is not $\sigma$-compact. Therefore, there is no continuous surjection $\mathbb{R} \to C_p([0,1])$.

$$\boxed{C_p([0,1]) \text{ is not a continuous image of } \mathbb{R}.}$$

### PROOF COMPLETE
