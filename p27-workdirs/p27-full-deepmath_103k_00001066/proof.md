# 证明：$S_\omega$ 的极小生成集存在性

## 问题

判定是否存在子集 $M \subseteq S_\omega$，使得 $\langle M \rangle = S_\omega$，且对每个 $m \in M$，都有 $\langle M \setminus \{m\} \rangle \neq S_\omega$。

## 答案

**存在。** 取 $M = \{(i\;\; i+1) : i \in \mathbb{N},\; i \geq 1\}$ 为所有相邻对换的集合。

## 证明

### 预备知识

$S_\omega$ 是 $\mathbb{N}$ 上所有**有限支撑**置换构成的群，即仅移动有限多个元素的置换全体。它可表示为递增链

$$S_\omega = \bigcup_{n=1}^{\infty} S_n,$$

其中 $S_n$ 嵌入 $S_{n+1}$ 为固定 $n+1$ 的子群。$S_\omega$ 是可数群，且非有限生成（任何有限生成子群必包含于某个 $S_n$ 中）。

### 第一步：$M$ 生成 $S_\omega$

**断言：** $\langle M \rangle = S_\omega$。

$S_\omega$ 由所有对换生成（任意有限支撑置换可分解为有限个对换的乘积）。而任意对换 $(i\;\; j)$（$i < j$）可由相邻对换表出：

$$(i\;\; j) = (i\;\; i{+}1)(i{+}1\;\; i{+}2)\cdots(j{-}1\;\; j)\cdots(i{+}1\;\; i{+}2)(i\;\; i{+}1),$$

即先用相邻对换将 $i$ 逐步移到 $j$ 的位置，再将"空位"逐步移回。因此所有相邻对换生成 $S_\omega$，即 $\langle M \rangle = S_\omega$。$\checkmark$

### 第二步：去掉任意一个元素后不再生成 $S_\omega$

**断言：** 对任意 $k \geq 1$，$\langle M \setminus \{(k\;\; k{+}1)\} \rangle \neq S_\omega$。

设 $T_k = M \setminus \{(k\;\; k{+}1)\}$。将 $T_k$ 分为两部分：

- **左部：** $L = \{(i\;\; i{+}1) : 1 \leq i \leq k-1\}$，这些对换仅移动 $\{1, 2, \ldots, k\}$ 中的元素，生成 $S_{\{1, \ldots, k\}}$（在 $\{1,\ldots,k\}$ 上的对称群，固定 $\{k+1, k+2, \ldots\}$ 中的所有元素）。
- **右部：** $R = \{(i\;\; i{+}1) : i \geq k+1\}$，这些对换仅移动 $\{k+1, k+2, \ldots\}$ 中的元素，生成 $S_\omega(\{k+1, k+2, \ldots\})$（在 $\{k+1, k+2, \ldots\}$ 上的有限支撑对称群，固定 $\{1, \ldots, k\}$ 中的所有元素）。

由于 $L$ 的生成元和 $R$ 的生成元作用在**不相交**的子集上，它们生成的群是直积：

$$\langle T_k \rangle = S_{\{1, \ldots, k\}} \times S_\omega(\{k+1, k+2, \ldots\}).$$

这个群的每个元素 $\sigma$ 都满足：$\sigma(\{1, \ldots, k\}) = \{1, \ldots, k\}$，即保持划分 $\{1,\ldots,k\} \cup \{k+1, k+2, \ldots\}$ 不变。

然而对换 $(1\;\; k{+}1) \in S_\omega$ 不保持此划分（它将 $1 \in \{1,\ldots,k\}$ 映到 $k+1 \notin \{1,\ldots,k\}$），故

$$(1\;\; k{+}1) \notin \langle T_k \rangle.$$

因此 $\langle T_k \rangle \subsetneq S_\omega$。$\checkmark$

### 结论

$M = \{(i\;\; i{+}1) : i \geq 1\}$ 满足：

1. $\langle M \rangle = S_\omega$（第一步），
2. 对每个 $m = (k\;\; k{+}1) \in M$，$\langle M \setminus \{m\} \rangle \neq S_\omega$（第二步）。

故这样的子集 $M$ 存在。

$$\boxed{\text{存在}}$$
