# Proof: Can $u$ have a discontinuous level curve?

**Answer: No.** Every level curve $f_c$ of $u$ is continuous.

---

## Setup and notation

Let $I := u(\mathbb{R}^2)$ be the range of $u$. For each $c \in I$, write the level curve $\{u = c\}$ as the graph of $f_c : \mathbb{R} \to \mathbb{R}$, i.e.

$$
\{(x,y) \in \mathbb{R}^2 : u(x,y) = c\} = \{(x, f_c(x)) : x \in \mathbb{R}\}.
$$

For fixed $x$, define $g_x(y) := u(x,y)$.

---

## Lemma 1 (Slice bijection)

For every $x \in \mathbb{R}$, $g_x : \mathbb{R} \to I$ is a bijection.

*Proof.* Fix $x$. For every $c \in I$, the level curve $\{u = c\}$ is the graph of $f_c$, so there is exactly one $y$ with $u(x,y) = c$, namely $y = f_c(x)$. Hence $g_x$ is a bijection $\mathbb{R} \to I$. $\square$

---

## Lemma 2 (Slice continuity)

For every $x \in \mathbb{R}$, $g_x$ is continuous. Consequently $I$ is an interval and $g_x$ is strictly monotone.

*Proof.* Fix $x_0$ and write $g = g_{x_0}$. For any $c \in I$:

- $\{y : g(y) \le c\} = \{y : u(x_0, y) \le c\}$ is the slice of the closed set $\{u \le c\}$ at $x = x_0$, hence closed.
- $\{y : g(y) \ge c\} = \{y : u(x_0, y) \ge c\}$ is the slice of the closed set $\{u \ge c\}$ at $x = x_0$, hence closed.

Therefore $\{y : g(y) < c\}$ and $\{y : g(y) > c\}$ are open for every $c \in I$. For any open $O \subseteq \mathbb{R}$, the preimage $g^{-1}(O) = g^{-1}(O \cap I)$ is a union of sets of the form $\{g > a\} \cap \{g < b\}$ (with $a, b \in I$), hence open. So $g$ is continuous.

Since $g$ is a continuous injection $\mathbb{R} \to \mathbb{R}$, it is strictly monotone. Since $I = g(\mathbb{R})$ is the continuous image of the connected set $\mathbb{R}$, $I$ is an interval. $\square$

Define the **monotonicity sign**

$$
\sigma(x) := \begin{cases} +1 & \text{if } g_x \text{ is strictly increasing}, \\ -1 & \text{if } g_x \text{ is strictly decreasing}. \end{cases}
$$

Key consequence: for $c \in I$ and any $x$,

- if $\sigma(x) = +1$: $\{y : u(x,y) \le c\} = (-\infty, f_c(x)]$ and $\{y : u(x,y) \ge c\} = [f_c(x), +\infty)$;
- if $\sigma(x) = -1$: $\{y : u(x,y) \le c\} = [f_c(x), +\infty)$ and $\{y : u(x,y) \ge c\} = (-\infty, f_c(x)]$.

---

## Lemma 3 (Closed graph)

For every $c \in I$, the graph of $f_c$ is closed in $\mathbb{R}^2$.

*Proof.* $\{u = c\} = \{u \le c\} \cap \{u \ge c\}$, the intersection of two closed sets. $\square$

---

## Lemma 4 (Closed-graph dichotomy)

If $f_c$ has closed graph and $x_n \to x_0$ with $f_c(x_n) \to y_0 \in \mathbb{R}$ (finite), then $y_0 = f_c(x_0)$.

*Proof.* $(x_n, f_c(x_n)) \in \{u = c\}$ and $(x_n, f_c(x_n)) \to (x_0, y_0)$. Since $\{u = c\}$ is closed, $(x_0, y_0) \in \{u = c\}$, so $y_0 = f_c(x_0)$. $\square$

So the only way $f_c$ can be discontinuous at $x_0$ is if some sequence $x_n \to x_0$ has $|f_c(x_n)| \to \infty$.

---

## Main Theorem

**For every $c \in I$, $f_c$ is continuous.**

*Proof.* Fix $c \in I$ and $x_0 \in \mathbb{R}$. Suppose $x_n \to x_0$. We show $f_c(x_n) \to f_c(x_0)$.

By Lemma 4, it suffices to rule out $f_c(x_n) \to +\infty$ and $f_c(x_n) \to -\infty$ (along subsequences). We treat the case $f_c(x_n) \to +\infty$; the case $-\infty$ is symmetric (flip all inequalities).

**Case A: $\sigma(x_0) = +1$** ($g_{x_0}$ strictly increasing).

Pick $y^\star > f_c(x_0)$. Then $u(x_0, y^\star) > c$, so $(x_0, y^\star) \notin \{u \le c\}$.

- **Subcase A1: $\sigma(x_n) = +1$ for infinitely many $n$.** Pass to that subsequence. For large $n$, $f_c(x_n) > y^\star$, and since $\sigma(x_n) = +1$ we have $u(x_n, y^\star) \le c$ (because $y^\star \le f_c(x_n)$ and $g_{x_n}$ increasing). So $(x_n, y^\star) \in \{u \le c\}$. By closedness, $(x_0, y^\star) \in \{u \le c\}$, i.e. $u(x_0, y^\star) \le c$—**contradiction**.

- **Subcase A2: $\sigma(x_n) = -1$ for all large $n$.** Pick $y_\star < f_c(x_0)$. Then $u(x_0, y_\star) < c$, so $(x_0, y_\star) \notin \{u \ge c\}$. For large $n$, $f_c(x_n) > y_\star$ and $\sigma(x_n) = -1$, so $g_{x_n}(y_\star) \ge c$ (because $y_\star \le f_c(x_n)$ and $g_{x_n}$ decreasing). Thus $(x_n, y_\star) \in \{u \ge c\}$. By closedness, $(x_0, y_\star) \in \{u \ge c\}$, i.e. $u(x_0, y_\star) \ge c$—**contradiction**.

Subcases A1 and A2 are exhaustive (either $+1$ occurs infinitely often, or $-1$ holds eventually). Contradiction in both.

**Case B: $\sigma(x_0) = -1$** ($g_{x_0}$ strictly decreasing).

Pick $y^\star > f_c(x_0)$. Then $u(x_0, y^\star) < c$ (decreasing $g_{x_0}$), so $(x_0, y^\star) \notin \{u \ge c\}$.

- **Subcase B1: $\sigma(x_n) = -1$ for infinitely many $n$.** Pass to that subsequence. For large $n$, $f_c(x_n) > y^\star$ and $\sigma(x_n) = -1$, so $u(x_n, y^\star) \ge c$ (because $y^\star \le f_c(x_n)$ and $g_{x_n}$ decreasing). Thus $(x_n, y^\star) \in \{u \ge c\}$. By closedness, $(x_0, y^\star) \in \{u \ge c\}$—**contradiction**.

- **Subcase B2: $\sigma(x_n) = +1$ for all large $n$.** Pick $y_\star < f_c(x_0)$. Then $u(x_0, y_\star) > c$ (decreasing $g_{x_0}$), so $(x_0, y_\star) \notin \{u \le c\}$. For large $n$, $f_c(x_n) > y_\star$ and $\sigma(x_n) = +1$, so $g_{x_n}(y_\star) \le c$ (because $y_\star \le f_c(x_n)$ and $g_{x_n}$ increasing). Thus $(x_n, y_\star) \in \{u \le c\}$. By closedness, $(x_0, y_\star) \in \{u \le c\}$—**contradiction**.

Again A1/A2 (here B1/B2) are exhaustive. Contradiction in both.

This rules out $f_c(x_n) \to +\infty$. The argument for $f_c(x_n) \to -\infty$ is identical with all inequality signs reversed (swap the roles of $y^\star > f_c(x_0)$ and $y_\star < f_c(x_0)$, and swap $\{u \le c\} \leftrightarrow \{u \ge c\}$).

Having ruled out escape to $\pm\infty$, every subsequential limit of $f_c(x_n)$ is finite and—by Lemma 4—equals $f_c(x_0)$. Hence $f_c(x_n) \to f_c(x_0)$, and $f_c$ is continuous at $x_0$. Since $x_0$ was arbitrary, $f_c$ is continuous on $\mathbb{R}$. $\square$

---

## Conclusion

No level curve of $u$ can be discontinuous.

$$
\boxed{\text{No}}
$$

### PROOF COMPLETE
