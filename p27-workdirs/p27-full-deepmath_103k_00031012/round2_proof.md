# Proof

## Problem

Determine the number of positive integers, each with exactly $2^{2005}$ digits, where each digit is either 7 or 8, such that among any two chosen integers, at most half of their corresponding digits are the same.

We seek the maximum size of a set of such integers satisfying the pairwise condition. Let $n = 2^{2005}$.

## Step 1: Reduction to Binary Coding Theory

Map each digit to a binary value: $7 \mapsto 0$, $8 \mapsto 1$. Each integer becomes a binary string of length $n$. For two strings $c, c'$, the number of positions where they have the same digit equals the number of positions where they agree, which is $n - d(c, c')$, where $d(c, c')$ is the Hamming distance.

The condition "at most half of their corresponding digits are the same" becomes:

$$n - d(c, c') \leq \frac{n}{2} \iff d(c, c') \geq \frac{n}{2}.$$

Thus the problem asks for $A(n, n/2)$: the maximum size of a binary code of length $n$ with minimum distance $\geq n/2$.

## Step 2: Lower Bound via Hadamard Code — $A(n, n/2) \geq 2n$

Since $n = 2^{2005}$ is a power of 2, the Sylvester Hadamard matrix $H_n$ of order $n$ exists, constructed recursively by $H_1 = [1]$ and $H_{2k} = \begin{pmatrix} H_k & H_k \\ H_k & -H_k \end{pmatrix}$.

The rows of $H_n$ are $n$ vectors $h_0, h_1, \ldots, h_{n-1} \in \{+1, -1\}^n$ satisfying:
- $\langle h_a, h_a \rangle = n$ (each entry is $\pm 1$),
- $\langle h_a, h_b \rangle = 0$ for $a \neq b$ (orthogonality of Hadamard matrix rows).

**Construction**: Form the set of $2n$ vectors
$$\mathcal{C} = \{h_a : 0 \leq a \leq n-1\} \cup \{-h_a : 0 \leq a \leq n-1\}.$$

**Verification of pairwise distances**: In the $\{+1, -1\}$ representation, the number of positions where two vectors $u, v$ agree is $a(u,v) = \frac{n + \langle u, v \rangle}{2}$, and the Hamming distance is $d(u,v) = \frac{n - \langle u, v \rangle}{2}$.

- For $h_a, h_b$ with $a \neq b$: $\langle h_a, h_b \rangle = 0$, so $d = n/2$. ✓
- For $h_a, -h_a$: $\langle h_a, -h_a \rangle = -n$, so $d = n$. ✓
- For $h_a, -h_b$ with $a \neq b$: $\langle h_a, -h_b \rangle = 0$, so $d = n/2$. ✓

All pairwise Hamming distances are $\geq n/2$. Converting back to digits ($+1 \mapsto 7$, $-1 \mapsto 8$), we obtain $2n = 2^{2006}$ valid integers. Therefore:

$$A(n, n/2) \geq 2n = 2^{2006}.$$

## Step 3: Upper Bound via Delsarte LP Bound — $A(n, n/2) \leq 2n$

We use the Delsarte linear programming bound for binary codes.

### Setup

Let $C \subseteq \{0,1\}^n$ be a binary code with $|C| = M$ and minimum distance $d = n/2$. Define the distance distribution:

$$A_i = \frac{1}{M} \cdot |\{(c, c') \in C \times C : d(c, c') = i\}|, \quad i = 0, 1, \ldots, n.$$

This distribution satisfies:
- $A_0 = 1$,
- $A_i \geq 0$ for all $i$,
- $A_i = 0$ for $1 \leq i < d = n/2$,
- $\sum_{i=0}^n A_i = M$.

### Krawtchouk Polynomials

The binary Krawtchouk polynomials are defined by:

$$K_k(x) = \sum_{j=0}^{k} (-1)^j \binom{x}{j} \binom{n-x}{k-j}, \quad k = 0, 1, \ldots, n.$$

Key instances:
- $K_0(x) = 1$,
- $K_1(x) = n - 2x$,
- $K_2(x) = \frac{(n-2x)^2 - n}{2}$.

### Delsarte Inequalities

The Delsarte inequalities state that for any binary code:

$$B_k := \sum_{i=0}^{n} A_i \, K_k(i) \geq 0, \quad k = 0, 1, \ldots, n.$$

Note that $B_0 = \sum_i A_i = M$.

### Delsarte LP Bound (Dual Form)

**Theorem (Delsarte)**: If $f(x) = \sum_{k=0}^{n} f_k \, K_k(x)$ is a polynomial satisfying:
1. $f_0 > 0$,
2. $f_k \geq 0$ for $k = 1, \ldots, n$,
3. $f(i) \leq 0$ for $i = d, d+1, \ldots, n$,

then $M \leq \frac{f(0)}{f_0}$.

**Proof of the bound**: We compute $\sum_{i=0}^n A_i \, f(i)$ in two ways.

*First way* (using Krawtchouk expansion):
$$\sum_i A_i \, f(i) = \sum_i A_i \sum_k f_k K_k(i) = \sum_k f_k \underbrace{\left(\sum_i A_i K_k(i)\right)}_{B_k \geq 0} \geq f_0 B_0 = f_0 \cdot M,$$
since $f_k \geq 0$ and $B_k \geq 0$ for all $k$.

*Second way* (using the support of $A_i$):
$$\sum_i A_i \, f(i) = A_0 \, f(0) + \sum_{i \geq d} A_i \, f(i) \leq f(0),$$
since $A_0 = 1$, $A_i = 0$ for $1 \leq i < d$, $A_i \geq 0$, and $f(i) \leq 0$ for $i \geq d$.

Combining: $f_0 \cdot M \leq f(0)$, hence $M \leq \frac{f(0)}{f_0}$. $\square$

### Constructing the Dual Polynomial

We claim that the polynomial

$$f(x) = 1 + K_1(x) + \frac{2}{n} K_2(x)$$

satisfies all the conditions and gives $f(0) = 2n$.

**Coefficients**: $f_0 = 1$, $f_1 = 1$, $f_2 = 2/n > 0$, and $f_k = 0$ for $k \geq 3$. All $f_k \geq 0$. ✓

**Explicit form**: Substituting the Krawtchouk polynomials:

$$f(x) = 1 + (n - 2x) + \frac{2}{n} \cdot \frac{(n-2x)^2 - n}{2} = 1 + (n-2x) + \frac{(n-2x)^2 - n}{n}.$$

Simplifying:

$$f(x) = (n - 2x) + \frac{(n-2x)^2}{n} = (n-2x)\left(1 + \frac{n-2x}{n}\right) = \frac{(n-2x)(2n - 2x)}{n} = \frac{2(n-2x)(n-x)}{n}.$$

**Evaluation at $x = 0$**:

$$f(0) = \frac{2 \cdot n \cdot n}{n} = 2n. \quad \checkmark$$

**Sign condition for $i \geq n/2$**: For $n/2 \leq i \leq n$:
- $n - 2i \leq 0$ (since $i \geq n/2$),
- $n - i \geq 0$ (since $i \leq n$).

Therefore $f(i) = \frac{2(n-2i)(n-i)}{n} \leq 0$ for all $i \in [n/2, n]$. ✓

### Applying the Bound

All conditions of the Delsarte LP bound are satisfied with $f_0 = 1$ and $f(0) = 2n$. Therefore:

$$M \leq \frac{f(0)}{f_0} = \frac{2n}{1} = 2n = 2^{2006}.$$

## Step 4: Conclusion

Combining the lower bound (Step 2) and the upper bound (Step 3):

$$A(n, n/2) = 2n = 2 \cdot 2^{2005} = 2^{2006}.$$

The maximum number of positive integers, each with exactly $2^{2005}$ digits, where each digit is either 7 or 8, such that among any two chosen integers at most half of their corresponding digits are the same, is:

$$\boxed{2^{2006}}$$

### PROOF COMPLETE
