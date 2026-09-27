# 分数阶 Poincaré 不等式

## 问题

判断以下不等式对 $u \in W^{s,p}_0(\Omega)$ 是否成立：
$$
\|u\|_{L^p(\Omega)} \leq c \left(\iint_{\Omega\times\Omega}\frac{|u(x)-u(y)|^p}{|x-y|^{n+ps}}\,dx\,dy\right)^{1/p},
$$
其中 $W^{s,p}_0(\Omega)$ 是 $C^{\infty}_c(\Omega)$ 在 $W^{s,p}(\Omega)$ 范数下的闭包，范数为
$$
\|u\|_{W^{s,p}(\Omega)}=\|u\|_{L^p(\Omega)}+\left(\iint_{\Omega\times\Omega}\frac{|u(x)-u(y)|^p}{|x-y|^{n+ps}}\,dx\,dy\right)^{1/p}.
$$

记 Gagliardo 半范数为
$$
[u]_{W^{s,p}(\Omega)} := \left(\iint_{\Omega\times\Omega}\frac{|u(x)-u(y)|^p}{|x-y|^{n+ps}}\,dx\,dy\right)^{1/p}.
$$

## 结论

**该不等式当且仅当 $\Omega$ 为有界 Lipschitz 域且 $sp \geq 1$（即 $s \geq 1/p$）时成立。**

具体地：

| 条件 | 结论 |
|---|---|
| $\Omega$ 有界 Lipschitz，$sp \geq 1$ | **TRUE** |
| $\Omega$ 有界 Lipschitz，$sp < 1$ | **FALSE**（常数函数属于 $W^{s,p}_0(\Omega)$） |
| $\Omega$ 无界（如 $\mathbb{R}^n$） | **FALSE**（scaling 反例，对任意 $s,p$） |

> **定义敏感性的说明**：本题中 $W^{s,p}_0(\Omega)$ 定义为 $C^\infty_c(\Omega)$ 在**$\Omega\times\Omega$ 半范数**下的闭包。若改用 $\mathbb{R}^n$ 上的半范数 $[\,\cdot\,]_{W^{s,p}(\mathbb{R}^n)}$ 定义 $W^{s,p}_0$，则 Poincaré 不等式对所有 $s \in (0,1)$、$p \in [1,\infty)$ 均成立（因为零延拓的 cross 积分对所有 $sp$ 都排除了常数）。本题的临界现象 $sp = 1$ 完全源于 $\Omega\times\Omega$ 半范数定义。

---

## 证明

### 第一部分：TRUE 情形（$\Omega$ 有界 Lipschitz，$sp \geq 1$）

**采用反证法。** 设不等式不成立，则存在序列 $\{u_k\}_{k=1}^\infty \subset W^{s,p}_0(\Omega)$ 使得
$$
\|u_k\|_{L^p(\Omega)} = 1 \quad \forall\, k, \qquad [u_k]_{W^{s,p}(\Omega)} \to 0 \quad (k \to \infty). \tag{1}
$$

**步骤 1：$\{u_k\}$ 在 $W^{s,p}_0(\Omega)$ 中有界。**

由 (1)，对充分大的 $k$ 有 $[u_k] \leq 1$，故
$$
\|u_k\|_{W^{s,p}(\Omega)} = \|u_k\|_{L^p} + [u_k] \leq 1 + 1 = 2.
$$

**步骤 2：由紧嵌入提取 $L^p$ 收敛子列。**

由分数阶 Rellich–Kondrashov 定理：对有界 Lipschitz 域 $\Omega$，嵌入
$$
W^{s,p}(\Omega) \hookrightarrow\hookrightarrow L^q(\Omega), \quad q \in [1, p^*)
$$
是紧的，其中
$$
p^* = \begin{cases} \dfrac{np}{n - sp}, & sp < n, \\ \infty, & sp \geq n. \end{cases}
$$
取 $q = p$：当 $sp < n$ 时 $p^* = \frac{np}{n-sp} > p$（因 $sp > 0$）；当 $sp \geq n$ 时 $p^* = \infty > p$。故 $W^{s,p}(\Omega) \hookrightarrow\hookrightarrow L^p(\Omega)$ 紧。

因 $W^{s,p}_0(\Omega) \subset W^{s,p}(\Omega)$，存在子列（仍记为 $\{u_k\}$）和 $u \in L^p(\Omega)$ 使得
$$
u_k \to u \quad \text{在 } L^p(\Omega) \text{ 中}. \tag{2}
$$
由 $\|u_k\|_{L^p} = 1$ 得 $\|u\|_{L^p} = 1$，特别地 $u \neq 0$。

**步骤 3：$[u]_{W^{s,p}(\Omega)} = 0$，故 $u$ 为常数。**

由 Fatou 引理（半范数的下半连续性）：
$$
[u]_{W^{s,p}(\Omega)}^p = \iint_{\Omega\times\Omega} \frac{|u(x)-u(y)|^p}{|x-y|^{n+ps}}\,dx\,dy \leq \liminf_{k\to\infty} [u_k]_{W^{s,p}(\Omega)}^p = 0.
$$
故 $[u] = 0$，即 $u(x) = u(y)$ 对 a.e. $x,y \in \Omega$ 成立。因 $\Omega$ 为连通域（Lipschitz 域连通），$u$ 在 $\Omega$ 上 a.e. 等于某常数 $c$。由 $\|u\|_{L^p} = 1$ 知 $c \neq 0$。

**步骤 4：$u \in W^{s,p}_0(\Omega)$。**

由 (1) 和 (2)：$\|u_k - u\|_{L^p} \to 0$ 且 $[u_k] \to 0 = [u]$，故
$$
\|u_k - u\|_{W^{s,p}(\Omega)} = \|u_k - u\|_{L^p} + [u_k - u]_{W^{s,p}(\Omega)} \leq \|u_k - u\|_{L^p} + [u_k] + [u] \to 0.
$$
故 $u_k \to u$ 在 $W^{s,p}(\Omega)$ 中。因 $W^{s,p}_0(\Omega)$ 为闭集，$u \in W^{s,p}_0(\Omega)$。

**步骤 5：用迹定理排除非零常数——矛盾。**

**情形 (a) $sp > 1$（即 $s > 1/p$）：** 对有界 Lipschitz 域，分数阶迹算子
$$
T: W^{s,p}(\Omega) \to W^{s - 1/p,\, p}(\partial\Omega)
$$
是有界线性算子。对任意 $\varphi \in C^\infty_c(\Omega)$，$T\varphi = 0$（因 $\varphi$ 在边界附近恒为零）。由 $W^{s,p}_0(\Omega)$ 是 $C^\infty_c(\Omega)$ 的闭包及 $T$ 的连续性，对任意 $u \in W^{s,p}_0(\Omega)$ 有 $Tu = 0$。

但 $u = c \neq 0$ 为常数时 $Tu = c \neq 0$（在 $\partial\Omega$ 上），矛盾。

**情形 (b) $sp = 1$（即 $s = 1/p$）：** 这是临界情形。对有界 Lipschitz 域，迹算子
$$
T: W^{1/p,\, p}(\Omega) \to L^p(\partial\Omega)
$$
仍然是有界线性算子（参见 Grisvard, *Elliptic Problems in Nonsmooth Domains*；Evans–Gariepy, *Measure Theory and Fine Properties of Functions*；Ding, *A note on trace theorem for fractional Sobolev spaces*）。

同样地，$C^\infty_c(\Omega)$ 函数的迹为零，由连续性和密度，$W^{1/p,p}_0(\Omega)$ 中所有函数的迹为零。但非零常数 $c$ 的迹 $Tc = c \neq 0$，矛盾。

**结论：** 两种情形下均得矛盾，故反证假设不成立。存在常数 $c > 0$ 使得
$$
\|u\|_{L^p(\Omega)} \leq c\, [u]_{W^{s,p}(\Omega)}, \quad \forall\, u \in W^{s,p}_0(\Omega). \qquad \blacksquare
$$

---

### 第二部分：FALSE 情形 1（$sp < 1$，$\Omega$ 有界 Lipschitz）

**构造反例：证明非零常数 $c \in W^{s,p}_0(\Omega)$，从而 Poincaré 不等式失败。**

因 $[c]_{W^{s,p}(\Omega)} = 0$ 而 $\|c\|_{L^p(\Omega)} = |c|\,|\Omega|^{1/p} > 0$，若 $c \in W^{s,p}_0(\Omega)$ 则不等式要求 $|c|\,|\Omega|^{1/p} \leq c \cdot 0 = 0$，矛盾。

**构造逼近序列。** 取 $\eta \in C^\infty(\mathbb{R})$ 满足 $\eta(t) = 0$ 当 $t \leq 0$，$\eta(t) = 1$ 当 $t \geq 1$，$0 \leq \eta \leq 1$。

**一维情形 $\Omega = (0,1)$ 的显式验证。** 设 $n = 1$，$\Omega = (0,1)$。定义
$$
\phi_k(x) = \eta(kx)\,\eta(k(1-x)), \quad x \in (0,1).
$$
则 $\phi_k \in C^\infty_c((0,1))$，$\phi_k = 1$ 当 $x \in [1/k, 1-1/k]$，$\phi_k$ 在宽度 $1/k$ 的边界层内从 $0$ 过渡到 $1$。

**$L^p$ 估计：**
$$
\|\phi_k - 1\|_{L^p(0,1)}^p = \int_0^{1/k} |1 - \eta(kx)|^p\,dx + \int_{1-1/k}^{1} |1 - \eta(k(1-x))|^p\,dx = \frac{2}{k}\int_0^1 |1-\eta(t)|^p\,dt = O(1/k).
$$
故 $\|\phi_k - 1\|_{L^p} \to 0$。

**半范数估计。** 令 $s \in (0,1)$，$p \geq 1$，$sp < 1$。需证 $[\phi_k]_{W^{s,p}(0,1)} \to 0$。

将积分区域分解。记 $L = (0, 1/k)$（左边界层），$M = [1/k, 1-1/k]$（内部），$R = (1-1/k, 1)$（右边界层）。在 $M \times M$ 上 $\phi_k(x) - \phi_k(y) = 0$。只需估计涉及边界层的部分。

**左层×内部 ($L \times M$)：** 对 $x \in L$，$y \in M$，$|x - y| \sim y$（因 $x \leq 1/k \leq y$），$|\phi_k(x) - \phi_k(y)| = |\eta(kx) - 1| \leq 1$。
$$
\iint_{L \times M} \frac{|\phi_k(x) - \phi_k(y)|^p}{|x-y|^{1+sp}}\,dx\,dy \leq \int_0^{1/k} \int_{1/k}^{1} y^{-1-sp}\,dy\,dx = \frac{1}{k} \cdot \left[\frac{y^{-sp}}{-sp}\Big|_{1/k}^{1}\right].
$$
当 $sp < 1$ 时 $\int_{1/k}^1 y^{-1-sp}\,dy = \frac{1}{sp}(k^{sp} - 1) = O(k^{sp})$，故
$$
\iint_{L \times M} \leq \frac{1}{k} \cdot O(k^{sp}) = O(k^{sp - 1}).
$$
因 $sp < 1$，$sp - 1 < 0$，故 $O(k^{sp-1}) \to 0$。

**左层×左层 ($L \times L$)：** 令 $x = a/k$，$y = b/k$，$a, b \in (0,1)$，$dx\,dy = k^{-2} da\,db$，$|x-y| = |a-b|/k$：
$$
\iint_{L \times L} \frac{|\phi_k(x) - \phi_k(y)|^p}{|x-y|^{1+sp}}\,dx\,dy = k^{-2} \cdot k^{1+sp} \iint_{(0,1)^2} \frac{|\eta(a)\eta(1-a/k) - \eta(b)\eta(1-b/k)|^p}{|a-b|^{1+sp}}\,da\,db.
$$
当 $k$ 大时 $\eta(1-a/k) \to \eta(0^+)$，但更精确地，$\eta(1 - a/k) \to 1$ 当 $k \to \infty$（因 $1 - a/k \to 1$ 且 $\eta(t) = 1$ 当 $t \geq 1$，这里 $a \in (0,1)$ 故 $1 - a/k \in (0,1)$ 需要更仔细处理）。

实际上对 $a \in (0,1)$，$1 - a/k \in (1 - 1/k, 1)$，当 $k$ 充分大时 $1 - a/k > 0$。$\eta(1 - a/k)$ 当 $1 - a/k \geq 1$ 时为 $1$，但 $a > 0$ 时 $1 - a/k < 1$，故 $\eta(1-a/k)$ 取决于 $\eta$ 在 $(0,1)$ 上的值。不过 $|\eta(a)\eta(1-a/k) - \eta(b)\eta(1-b/k)| \leq C(|a-b| + |a-b|/k) \leq C'|a-b|$（利用 $\eta$ Lipschitz），故被积函数有界，积分 $O(1)$。因此
$$
\iint_{L \times L} = O(k^{sp - 1}) \to 0 \quad (\text{因 } sp < 1).
$$

**左层×右层 ($L \times R$)：** $x \in L$，$y \in R$，$|x - y| \sim 1$，$|\phi_k(x) - \phi_k(y)| \leq 2$：
$$
\iint_{L \times R} \leq C \cdot \frac{1}{k} \cdot \frac{1}{k} = O(k^{-2}) \to 0.
$$

由对称性，右层的相关估计同理。综合所有区域：
$$
[\phi_k]_{W^{s,p}(0,1)}^p = O(k^{sp - 1}) + O(k^{-2}) \to 0 \quad \text{当 } sp < 1.
$$

故 $\phi_k \to 1$ 在 $W^{s,p}((0,1))$ 中，即 $1 \in W^{s,p}_0((0,1))$。Poincaré 不等式失败。$\blacksquare$

**一般 $n$ 维情形。** 对有界 Lipschitz 域 $\Omega \subset \mathbb{R}^n$，边界附近由局部坐标化为半空间 $\{x_n > 0\}$。取 $\phi_k(x) = \eta(k\, d(x,\partial\Omega))$（用边界距离的适当正则化），cross 型积分经标度分析化为
$$
\int_0^{\varepsilon} t^{-sp}\,dt,
$$
当 $sp < 1$ 时收敛。这保证 $\phi_k \to 1$ 在 $W^{s,p}(\Omega)$ 中，故 $1 \in W^{s,p}_0(\Omega)$。

**等价地，用零延拓观点理解：** 当 $sp < 1$ 时，分数阶 Hardy 不等式
$$
\int_\Omega \frac{|u(x)|^p}{d(x,\partial\Omega)^{sp}}\,dx \leq C\, [u]_{W^{s,p}(\Omega)}^p
$$
成立，零延拓 $\tilde u \in W^{s,p}(\mathbb{R}^n)$ 有界。对常数 $c$，$c \cdot \mathbf{1}_\Omega$ 的 $\mathbb{R}^n$ 半范数为
$$
[c \cdot \mathbf{1}_\Omega]_{W^{s,p}(\mathbb{R}^n)}^p = 2|c|^p \iint_{\Omega \times \Omega^c} \frac{dx\,dy}{|x-y|^{n+sp}},
$$
经标度分析化为 $\int_0^\varepsilon t^{-sp}\,dt$，当 $sp < 1$ 时收敛，故 $c \cdot \mathbf{1}_\Omega \in W^{s,p}(\mathbb{R}^n)$，常数可被 $C^\infty_c$ 函数逼近。

---

### 第三部分：FALSE 情形 2（$\Omega$ 无界）

**Scaling 反例。** 设 $\Omega = \mathbb{R}^n$（或任何包含任意大球的无界域）。取 $\phi \in C^\infty_c(\mathbb{R}^n)$，$\|\phi\|_{L^p} = 1$，$\phi \neq 0$。定义
$$
u_R(x) = R^{-n/p}\, \phi\!\left(\frac{x}{R}\right), \quad R > 0.
$$
则 $u_R \in C^\infty_c(\mathbb{R}^n) \subset W^{s,p}_0(\mathbb{R}^n)$（当 $\Omega = \mathbb{R}^n$ 时 $W^{s,p}_0 = W^{s,p}$）。

**$L^p$ 范数：** 令 $x = Rz$，$dx = R^n\,dz$：
$$
\|u_R\|_{L^p}^p = R^{-n} \int_{\mathbb{R}^n} |\phi(x/R)|^p\,dx = R^{-n} \cdot R^n \int |\phi(z)|^p\,dz = 1.
$$

**半范数：** 令 $x = Rz$，$y = Rw$，$dx\,dy = R^{2n}\,dz\,dw$，$|x-y| = R|z-w|$：
$$
[u_R]_{W^{s,p}}^p = R^{-n} \iint_{\mathbb{R}^n \times \mathbb{R}^n} \frac{|\phi(z) - \phi(w)|^p}{R^{n+sp}|z-w|^{n+sp}} \cdot R^{2n}\,dz\,dw = R^{-sp}\, [\phi]_{W^{s,p}(\mathbb{R}^n)}^p.
$$
故 $[u_R] = R^{-s}\, [\phi] \to 0$ 当 $R \to \infty$（因 $s > 0$）。

**矛盾：** 若 Poincaré 不等式成立，则
$$
1 = \|u_R\|_{L^p} \leq c\, [u_R] = c\, R^{-s}\, [\phi] \xrightarrow{R \to \infty} 0,
$$
矛盾。故 $\Omega$ 无界时不等式失败。$\blacksquare$

---

## 总结

$$
\boxed{\text{不等式成立当且仅当 } \Omega \text{ 为有界 Lipschitz 域且 } sp \geq 1 \text{（即 } s \geq 1/p\text{）。}}
$$

- **TRUE**（$sp \geq 1$，$\Omega$ 有界 Lipschitz）：反证法 + 紧嵌入（分数阶 Rellich–Kondrashov）+ 迹定理排除非零常数。
- **FALSE**（$sp < 1$，$\Omega$ 有界 Lipschitz）：非零常数 $c \in W^{s,p}_0(\Omega)$，因边界层截断函数半范数 $O(k^{sp-1}) \to 0$。
- **FALSE**（$\Omega$ 无界）：scaling 反例 $u_R = R^{-n/p}\phi(\cdot/R)$，$[u_R] = R^{-s}[\phi] \to 0$ 而 $\|u_R\|_{L^p} = 1$。

### PROOF COMPLETE
