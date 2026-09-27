# 逆命题是否成立？

**问题**：设 $f \in C^\infty(\mathbb{R})$，$A(f) := \bigcup_{n=0}^{\infty} \text{Graph}(f^{(n)})$。已知 $g = f^{(n)} \Rightarrow A(g) \subset A(f)$。问：$A(g) \subset A(f) \Rightarrow g = f^{(n)}$ 对某个 $n \geq 0$？

**答案**：逆命题**不成立**。下面给出反例。

---

## 反例构造

令平函数
$$
\alpha(x) = \begin{cases} e^{-1/x^2}, & x \neq 0, \\ 0, & x = 0. \end{cases}
$$
熟知 $\alpha \in C^\infty(\mathbb{R})$ 且 $\alpha^{(n)}(0) = 0$ 对所有 $n \geq 0$，$\alpha$ 在 $\mathbb{R}\setminus\{0\}$ 上实解析，且为偶函数。

定义
$$
f(x) = \cosh(x) + \alpha(x),
$$
$$
g(x) = \begin{cases} f(x), & x \leq 0, \\ f''(x), & x > 0. \end{cases}
$$

---

## 验证

### (1) $f \in C^\infty(\mathbb{R})$

$\cosh \in C^\infty$，$\alpha \in C^\infty$，故 $f \in C^\infty$。✓

### (2) 导数在 $0$ 处周期为 2

对任意 $n \geq 0$：
$$
f^{(n)}(0) = \cosh^{(n)}(0) + \alpha^{(n)}(0) = \cosh^{(n)}(0) + 0.
$$
$\cosh^{(n)}(0) = 1$（$n$ 偶），$0$（$n$ 奇）。故
$$
f^{(n)}(0) = f^{(n+2)}(0), \quad \forall\, n \geq 0. \tag{$\ast$}
$$

### (3) $g \in C^\infty(\mathbb{R})$

在 $x \neq 0$ 处 $g$ 显然 $C^\infty$。在 $x = 0$ 处，需验证左右各阶导数匹配。

- 左导数：$g^{(k)}(0^-) = f^{(k)}(0)$（因 $x \leq 0$ 时 $g = f$）。
- 右导数：$g^{(k)}(0^+) = (f'')^{(k)}(0) = f^{(k+2)}(0)$（因 $x > 0$ 时 $g = f''$）。

由 $(\ast)$，$f^{(k+2)}(0) = f^{(k)}(0)$，故 $g^{(k)}(0^-) = g^{(k)}(0^+)$ 对所有 $k \geq 0$。因此 $g \in C^\infty(\mathbb{R})$。✓

### (4) $A(g) \subset A(f)$

$A(g) = \bigcup_{k=0}^{\infty} \text{Graph}(g^{(k)})$。需证对每个 $k$ 和每个 $x$，$(x, g^{(k)}(x)) \in A(f)$。

- **$x \leq 0$**：$g^{(k)}(x) = f^{(k)}(x)$，故 $(x, g^{(k)}(x)) \in \text{Graph}(f^{(k)}) \subset A(f)$。✓
- **$x > 0$**：$g^{(k)}(x) = (f'')^{(k)}(x) = f^{(k+2)}(x)$，故 $(x, g^{(k)}(x)) \in \text{Graph}(f^{(k+2)}) \subset A(f)$。✓
- **$x = 0$**：$g^{(k)}(0) = f^{(k)}(0)$（由 (3)），故 $(0, g^{(k)}(0)) \in \text{Graph}(f^{(k)}) \subset A(f)$。✓

因此 $A(g) \subset A(f)$。✓

### (5) $g \neq f^{(n)}$ 对所有 $n \geq 0$

分四种情形：

**情形 (i)：$n = 0$。** 需证 $g \neq f$。在 $x = 1 > 0$ 处 $g(1) = f''(1)$。计算
$$
f(1) - f''(1) = \alpha(1) - \alpha''(1).
$$
$\alpha'(x) = \frac{2}{x^3}e^{-1/x^2}$，$\alpha''(x) = \left(\frac{4}{x^6} - \frac{6}{x^4}\right)e^{-1/x^2}$。故
$$
\alpha(1) - \alpha''(1) = \left(1 - 4 + 6\right)e^{-1} = 3e^{-1} \neq 0.
$$
因此 $g(1) = f''(1) \neq f(1)$，即 $g \neq f$。✗

**情形 (ii)：$n = 2$。** 需证 $g \neq f''$。在 $x = -1 \leq 0$ 处 $g(-1) = f(-1)$。因 $\alpha$ 为偶函数，
$$
f(-1) - f''(-1) = \alpha(-1) - \alpha''(-1) = \alpha(1) - \alpha''(1) = 3e^{-1} \neq 0.
$$
因此 $g(-1) = f(-1) \neq f''(-1)$，即 $g \neq f''$。✗

**情形 (iii)：$n$ 为奇数。** $g(0) = f(0) = \cosh(0) + 0 = 1$。而 $f^{(n)}(0) = \cosh^{(n)}(0) = 0$（$n$ 奇）。故 $g(0) = 1 \neq 0 = f^{(n)}(0)$，即 $g \neq f^{(n)}$。✗

**情形 (iv)：$n$ 为偶数，$n \geq 4$。** 需证 $g \neq f^{(n)}$。在 $(-\infty, 0]$ 上 $g = f$，故需证 $f^{(n)} \neq f$ 在 $(-\infty, 0)$ 上。因 $n$ 偶，$\cosh^{(n)} = \cosh$，故
$$
f^{(n)} - f = \alpha^{(n)} - \alpha.
$$

**引理**：对 $n \geq 1$，$\alpha^{(n)} \neq \alpha$ 在 $(-\infty, 0)$ 上。

*证明*：在 $\mathbb{R}\setminus\{0\}$ 上，$\alpha^{(n)}(x) = e^{-1/x^2} P_n(1/x)$，其中 $P_n$ 为多项式，满足递推
$$
P_0(t) = 1, \quad P_{n+1}(t) = 2t^3 P_n(t) - t^2 P_n'(t).
$$
- $P_0 = 1$（次数 $0$）。
- $P_1(t) = 2t^3$（次数 $3$）。
- 一般地，若 $\deg P_n = d_n$，则 $2t^3 P_n$ 次数为 $d_n + 3$，$t^2 P_n'$ 次数为 $d_n + 1$。故 $\deg P_{n+1} = d_n + 3$。

因此对 $n \geq 1$，$\deg P_n \geq 3 > 0$，故 $P_n \not\equiv 1$。

$\alpha^{(n)} - \alpha$ 在 $(-\infty, 0)$ 上实解析（$\alpha$ 在 $\mathbb{R}\setminus\{0\}$ 实解析）。若 $\alpha^{(n)} = \alpha$ 在 $(-\infty, 0)$ 上，则
$$
e^{-1/x^2} P_n(1/x) = e^{-1/x^2}, \quad \forall\, x < 0,
$$
即 $P_n(1/x) = 1$ 对所有 $x < 0$，亦即 $P_n(t) = 1$ 对所有 $t < 0$。由多项式身份定理（非常多项式不可能在无穷多个点取常值），$P_n \equiv 1$，与 $\deg P_n \geq 3$ 矛盾。

故 $\alpha^{(n)} \neq \alpha$ 在 $(-\infty, 0)$ 上，即存在 $x_0 < 0$ 使 $f^{(n)}(x_0) \neq f(x_0) = g(x_0)$。因此 $g \neq f^{(n)}$。✗

**综合**：对所有 $n \geq 0$，$g \neq f^{(n)}$。✓

---

## 结论

存在 $f \in C^\infty(\mathbb{R})$ 和 $g \in C^\infty(\mathbb{R})$ 满足 $A(g) \subset A(f)$，但 $g \neq f^{(n)}$ 对任何 $n \geq 0$。因此逆命题**不成立**。

$$
\boxed{\text{No, the converse is false.}}
$$

### PROOF COMPLETE
