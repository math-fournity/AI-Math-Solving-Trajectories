# 行列式恒为零的证明

## 题目

判断以下行列式是否对任意 $C^3$ 函数 $\phi: \mathbb{R}^n \rightarrow \mathbb{R}^{n-2}$ 恒为零：

$$\begin{bmatrix} \frac{\partial }{\partial x_1} & \frac{\partial\phi_2 }{\partial x_1} & \dots & \frac{\partial \phi_{n-1} }{\partial x_1} \\
\frac{\partial }{\partial x_n} & \frac{\partial\phi_2 }{\partial x_n} & \dots & \frac{\partial \phi_{n-1} }{\partial x_n} \end{bmatrix}$$

## 答案

$$\boxed{\text{YES, 行列式恒等于零}}$$

---

## 维度说明

$\phi = (\phi_2, \dots, \phi_{n-1})$ 共 $n-2$ 个分量。矩阵第一列为微分算子 $\frac{\partial}{\partial x_i}$，其余 $n-2$ 列为 $\frac{\partial \phi_j}{\partial x_i}$，故矩阵共 $n-1$ 列。题目只显示了首末两行（$x_1$ 与 $x_n$），由"determinant"一词知矩阵应为方阵，即 $(n-1) \times (n-1)$（行对应 $x_1, \dots, x_{n-1}$，末行 $x_n$ 为 $x_{n-1}$ 的索引约定差异）。更一般地，若矩阵为 $n \times (n-1)$（含全部 $n$ 行），则所有 $(n-1) \times (n-1)$ 极大子式均恒为零。下面给出一般情形的证明。

---

## 主证明（微分形式法）

设 $m = n-1$，行索引 $i = 1, \dots, m$。在 $\mathbb{R}^m$ 上考虑 $(m-1)$-形式

$$\omega = d\phi_2 \wedge d\phi_3 \wedge \cdots \wedge d\phi_{m}$$

（这里 $m = n-1$，$\phi$ 的分量为 $\phi_2, \dots, \phi_m$，共 $m-1 = n-2$ 个，与题目一致。）

### 第一步：$d\omega = 0$

由分级 Leibniz 法则，

$$d\omega = \sum_{j=2}^{m} (-1)^{j-2}\, d\phi_2 \wedge \cdots \wedge \underbrace{d(d\phi_j)}_{=\,0} \wedge \cdots \wedge d\phi_m$$

由于 $\phi \in C^3 \Rightarrow \phi \in C^2$，由 **Clairaut 定理**（混合偏导对称性），$d(d\phi_j) = 0$（即 $d^2 = 0$）。因此每一项均为零，

$$\boxed{d\omega = 0}$$

### 第二步：$\omega$ 的坐标展开

将 $d\phi_j = \sum_{i=1}^{m} \frac{\partial \phi_j}{\partial x_i}\, dx_i$ 代入并展开，$\omega$ 是 $(m-1)$-形式，故可写为

$$\omega = \sum_{i=1}^{m} J_i\, dx_1 \wedge \cdots \wedge \widehat{dx_i} \wedge \cdots \wedge dx_m$$

其中 $J_i$ 是从 Jacobian 矩阵 $\left(\frac{\partial \phi_j}{\partial x_k}\right)$ 中删去第 $i$ 行后所得 $(m-1)\times(m-1)$ 子式的行列式（带适当符号），$\widehat{dx_i}$ 表示 $dx_i$ 被省略。

### 第三步：$d\omega$ 的坐标展开

对 $\omega$ 取外微分，

$$d\omega = \sum_{i=1}^{m} dJ_i \wedge dx_1 \wedge \cdots \wedge \widehat{dx_i} \wedge \cdots \wedge dx_m$$

由于 $dJ_i = \sum_{k=1}^{m} \frac{\partial J_i}{\partial x_k}\, dx_k$，而 $dx_k \wedge dx_1 \wedge \cdots \wedge \widehat{dx_i} \wedge \cdots \wedge dx_m$ 仅当 $k = i$ 时非零（否则 $dx_k$ 重复出现），此时需将 $dx_i$ 移过 $i-1$ 个位置，故

$$d\omega = \sum_{i=1}^{m} (-1)^{i-1} \frac{\partial J_i}{\partial x_i}\, dx_1 \wedge \cdots \wedge dx_m$$

### 第四步：识别 $D$ 为 $d\omega$ 的系数

题目中的行列式 $D$ 是 $(m \times m)$ 矩阵，其第一列为算子 $\frac{\partial}{\partial x_i}$，其余列为 $\frac{\partial \phi_j}{\partial x_k}$。按第一列（算子列）Laplace 展开：

$$D = \sum_{i=1}^{m} (-1)^{i+1} \frac{\partial J_i}{\partial x_i}$$

由于 $(-1)^{i+1} = (-1)^{i-1}$（两者差 $(-1)^2 = 1$），

$$D = \sum_{i=1}^{m} (-1)^{i-1} \frac{\partial J_i}{\partial x_i}$$

这**恰好是 $d\omega$ 中 $dx_1 \wedge \cdots \wedge dx_m$ 的系数**。

### 第五步：结论

由第一步 $d\omega = 0$，其每一个坐标分量系数均为零，特别地

$$D = \sum_{i=1}^{m} (-1)^{i-1} \frac{\partial J_i}{\partial x_i} = 0$$

因此行列式恒等于零。$\blacksquare$

---

## 验证：$n = 3$ 情形

$\phi: \mathbb{R}^3 \to \mathbb{R}^1$，$\phi = (\phi_2)$，矩阵为 $2 \times 2$：

$$D = \det\begin{pmatrix} \frac{\partial}{\partial x_1} & \frac{\partial \phi_2}{\partial x_1} \\[4pt] \frac{\partial}{\partial x_3} & \frac{\partial \phi_2}{\partial x_3} \end{pmatrix} = \frac{\partial^2 \phi_2}{\partial x_1 \partial x_3} - \frac{\partial^2 \phi_2}{\partial x_3 \partial x_1} = 0$$

由 Clairaut 定理（$\phi \in C^3 \Rightarrow C^2$）。此时 $\omega = d\phi_2$，$d\omega = d^2\phi_2 = 0$，$D$ 即 $d\omega$ 中 $dx_1 \wedge dx_3$ 的系数。✓

---

## 验证：$n = 4$ 情形

$\phi: \mathbb{R}^4 \to \mathbb{R}^2$，$\phi = (\phi_2, \phi_3)$，矩阵为 $3 \times 3$，按第一列 Laplace 展开：

$$D = \frac{\partial}{\partial x_1}\!\left(\phi_{2,2}\phi_{3,3}-\phi_{2,3}\phi_{3,2}\right) - \frac{\partial}{\partial x_2}\!\left(\phi_{2,1}\phi_{3,3}-\phi_{2,3}\phi_{3,1}\right) + \frac{\partial}{\partial x_3}\!\left(\phi_{2,1}\phi_{3,2}-\phi_{2,2}\phi_{3,1}\right)$$

其中 $\phi_{j,ab} := \frac{\partial^2 \phi_j}{\partial x_a \partial x_b}$。展开后用 Clairaut 对称性 $\phi_{j,ab} = \phi_{j,ba}$ 配对消去，全部 6 类项成对抵消，$D = 0$。✓

此时 $\omega = d\phi_2 \wedge d\phi_3$，$d\omega = d^2\phi_2 \wedge d\phi_3 - d\phi_2 \wedge d^2\phi_3 = 0$。✓

---

## 推广：$n \times (n-1)$ 情形

若矩阵包含全部 $n$ 行（$n \times (n-1)$），则 $\omega$ 是 $\mathbb{R}^n$ 上的 $(n-2)$-形式，$d\omega = 0$ 意味着 $d\omega$ 在**每一个** $(n-1)$-形式基元素 $dx_{i_1} \wedge \cdots \wedge dx_{i_{n-1}}$ 上的系数均为零。每个系数恰对应一个由行 $\{i_1, \dots, i_{n-1}\}$ 选出的 $(n-1) \times (n-1)$ 子式。因此**所有极大子式恒为零**，特别地题目显示的 $\{x_1, x_n\}$（$n=3$）或任意 $n-1$ 行的子式均为零。

---

## 核心机制总结

| 要素 | 内容 |
|---|---|
| 关键定理 | Clairaut 定理（$C^2$ 混合偏导对称性），等价于 $d^2 = 0$ |
| 正则性条件 | $\phi \in C^3 \Rightarrow \phi \in C^2$，条件充分 |
| 证明结构 | $D$ = $d\omega$ 的坐标系数；$d\omega = 0$；故 $D = 0$ |
| 适用范围 | 任意 $n \geq 3$，方阵情形或 $n \times (n-1)$ 全部极大子式情形 |

### PROOF COMPLETE
