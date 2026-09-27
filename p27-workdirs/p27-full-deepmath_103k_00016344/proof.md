# 最大线性无关二次型数 $k$ 的确定

**问题.** 确定 $\mathbb{C}$ 上五个变量的线性无关齐次二次型 $Q_1, \dots, Q_k$ 的最大个数 $k$，使得 $V(Q_1) \cap \dots \cap V(Q_k) \subseteq \mathbb{P}^4$ 包含一个正维数且不位于任何超平面内的连通分量。

**答案：$k = 6$。**

---

## 记号与框架

设 $S = \mathbb{C}[x_0, \dots, x_4]$，$\dim S_2 = \binom{5+1}{2} = 15$。

设 $X = V(Q_1) \cap \dots \cap V(Q_k)$，$C \subseteq X$ 为一个正维数、非退化（不包含于任何超平面）的连通分量。因 $C \subseteq V(Q_i)$ 对每个 $i$，所有 $Q_i$ 在 $C$ 上恒为零，即 $Q_i \in I_C(2)$。由 $Q_1, \dots, Q_k$ 线性无关，

$$
k \leq \dim I_C(2) = 15 - h_C(2),
$$

其中 $h_C(2) = \dim (S/I_C)_2$ 是 $C$ 在度 $2$ 的 Hilbert 函数。**最大化 $k$ 等价于最小化 $h_C(2)$**，其中 $C$ 取遍 $\mathbb{P}^4$ 中的非退化正维数簇。

---

## 上界：$k \leq 6$

### 关键工具：超平面截面正合列

设 $C \subseteq \mathbb{P}^4$ 为非退化正维数簇，$L \in S_1$ 为一般线性形式（定义超平面 $H = V(L) \cong \mathbb{P}^3$）。

**正合性条件.** $C$ 是 $X$ 的连通分量，故 $I_C$ 是根式理想（radical ideal）。$\mathbb{P}^4$ 中的根式理想是 unmixed 的（无嵌入素理想），因此 $S/I_C$ 是 Cohen–Macaulay 的在"无嵌入素"意义下——具体地，一般线性形式 $L$ 不属于 $I_C$ 的任何结合素理想，故 $L$ 是 $S/I_C$ 上的非零因子。由此得正合列：

$$
0 \to (S/I_C)(-1) \xrightarrow{\,\cdot L\,} S/I_C \to S/(I_C + (L)) \to 0.
$$

记 $\Gamma = C \cap H$，$I_\Gamma = I_C + (L)$，则

$$
h_C(m) = h_C(m-1) + h_\Gamma(m). \tag{$\star$}
$$

### 情形 1：$C$ 是曲线（$\dim C = 1$）

$\Gamma = C \cap H$ 是 $\mathbb{P}^3$ 中的有限点集。

- $h_C(0) = 1$，$h_C(1) = 5$（$C$ 非退化，故 $I_C(1) = 0$）。
- 由 $(\star)$ 在 $m=1$：$h_\Gamma(1) = h_C(1) - h_C(0) = 5 - 1 = 4$，即 $\Gamma$ 在 $\mathbb{P}^3$ 中非退化。
- **有限点集的 Hilbert 函数非递减**：对有限点集 $\Gamma$，一般线性形式 $L'$ 不在 $\Gamma$ 的任一点消失，故 $L'$ 是 $S/I_\Gamma$ 上的非零因子，给出注入 $(S/I_\Gamma)_m \hookrightarrow (S/I_\Gamma)_{m+1}$，即 $h_\Gamma(m+1) \geq h_\Gamma(m)$。
- 因此 $h_\Gamma(2) \geq h_\Gamma(1) = 4$。
- 由 $(\star)$ 在 $m=2$：$h_C(2) = h_C(1) + h_\Gamma(2) \geq 5 + 4 = 9$。

$$
\boxed{k \leq 15 - 9 = 6.}
$$

**注.** 此论证仅用非退化性与点集 Hilbert 函数的非递减性，不依赖度数、不可约性或 ACM 性质，适用于任意非退化曲线（可约或不可约）。

### 情形 2：$C$ 是曲面（$\dim C = 2$）

迭代应用 $(\star)$。设 $H, H'$ 为两个一般超平面。

- $\Gamma_1 = C \cap H$ 是 $\mathbb{P}^3$ 中的非退化曲线，$h_{\Gamma_1}(1) = 4$。
- $\Gamma_2 = \Gamma_1 \cap H'$ 是 $\mathbb{P}^2$ 中的非退化有限点集，$h_{\Gamma_2}(1) = 3$，$h_{\Gamma_2}(2) \geq 3$（非递减性）。
- $h_{\Gamma_1}(2) = h_{\Gamma_1}(1) + h_{\Gamma_2}(2) \geq 4 + 3 = 7$。
- $h_C(2) = h_C(1) + h_{\Gamma_1}(2) \geq 5 + 7 = 12$。

$$
k \leq 15 - 12 = 3.
$$

### 情形 3：$C$ 是三维簇（$\dim C = 3$）

$\mathbb{P}^4$ 中的非退化 $3$-fold 是超曲面（由单个方程定义），$h_C(1) = 5$。继续迭代：

- $h_C(2) \geq 5 + 9 = 14$（第二层截面回到曲线情形）。

$$
k \leq 15 - 14 = 1.
$$

### 综合上界

| $\dim C$ | $h_C(2)$ 下界 | $k$ 上界 |
|:---:|:---:|:---:|
| 1（曲线） | $\geq 9$ | $\leq 6$ |
| 2（曲面） | $\geq 12$ | $\leq 3$ |
| 3（3-fold） | $\geq 14$ | $\leq 1$ |

**对任意非退化正维数连通分量 $C$，$k \leq 6$。**

---

## 下界：$k = 6$ 可达

### 构造：4 次有理正规曲线

设 $C \subseteq \mathbb{P}^4$ 为 **4 次有理正规曲线**，参数化为

$$
\varphi : \mathbb{P}^1 \to \mathbb{P}^4, \quad [s:t] \mapsto [s^4 : s^3 t : s^2 t^2 : s t^3 : t^4].
$$

### 理想与生成二次型

$C$ 的理想 $I_C$ 由 catalecticant 矩阵

$$
M = \begin{pmatrix} x_0 & x_1 & x_2 & x_3 \\ x_1 & x_2 & x_3 & x_4 \end{pmatrix}
$$

的全体 $2 \times 2$ 子式生成。这给出 $6$ 个线性无关的二次型：

$$
\begin{aligned}
Q_1 &= x_0 x_2 - x_1^2, \\
Q_2 &= x_0 x_3 - x_1 x_2, \\
Q_3 &= x_0 x_4 - x_1 x_3, \\
Q_4 &= x_1 x_3 - x_2^2, \\
Q_5 &= x_1 x_4 - x_2 x_3, \\
Q_6 &= x_2 x_4 - x_3^2.
\end{aligned}
$$

### 验证

1. **Hilbert 函数.** 有理正规曲线 $C$ 的 Hilbert 函数为 $h_C(m) = 4m + 1$（$I_C$ 由 $2 \times 2$ 子式生成，$C$ 是 arithmetically Cohen–Macaulay，$h$-向量为 $(1, 4, 0, 0, \dots)$）。故 $h_C(2) = 9$，$\dim I_C(2) = 15 - 9 = 6$。上述 $6$ 个二次型线性无关且张成 $I_C(2)$。

2. **理想由二次型生成.** $C$ 是 ACM 的，$I_C$ 恰由这 $6$ 个二次型生成。因此

$$
V(Q_1) \cap \dots \cap V(Q_6) = V(I_C) = C.
$$

3. **连通性.** $C \cong \mathbb{P}^1$ 是光滑不可约曲线，故连通。

4. **正维数.** $\dim C = 1 > 0$。

5. **非退化.** 参数化 $[s^4 : s^3 t : s^2 t^2 : s t^3 : t^4]$ 用到全部 $5$ 个坐标，$C$ 不包含于任何超平面：$h_C(1) = 5 = \dim S_1$，即 $I_C(1) = 0$。

**因此 $k = 6$ 可达。**

---

## 结论

上界 $k \leq 6$（对任意非退化正维数连通分量）与下界 $k = 6$（由 4 次有理正规曲线实现）结合，得

$$
\boxed{k = 6}.
$$

### PROOF COMPLETE
