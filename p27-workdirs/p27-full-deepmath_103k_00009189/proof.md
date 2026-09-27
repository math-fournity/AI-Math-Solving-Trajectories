# 计算 $\lambda$：复合态射 $\pi_{n+1}(S^{n+1}) \to \pi_n(SO_{n+1}) \to \pi_n(S^n)$ 的乘数

## 问题

求整数 $\lambda$，使得复合同态
$$
\mathbb{Z} \cong \pi_{n+1}(S^{n+1}) \xrightarrow{\;\partial\;} \pi_n(SO_{n+1}) \xrightarrow{\;\alpha_*\;} \pi_n(S^n) \cong \mathbb{Z}
$$
为乘以 $\lambda$。其中 $\partial$ 是纤维化 $SO_{n+1} \hookrightarrow SO_{n+2} \to S^{n+1}$ 的连接同态，$\alpha:SO_{n+1}\to S^n$ 为矩阵乘法映射（取定单位向量 $v$，$A\mapsto Av$，即取矩阵的某一列）。

## 答案

$$
\boxed{\,\lambda = 1 + (-1)^{n+1}\,}
$$

即 $n$ 为奇数时 $\lambda = 2$，$n$ 为偶数时 $\lambda = 0$。等价地 $\lambda = \chi(S^{n+1})$。

## 证明

### 步骤 1：纤维化是切丛的标架主丛

由 $S^{n+1} = SO(n+2)/SO(n+1)$，投影 $\pi:SO(n+2)\to S^{n+1}$（$A\mapsto A\cdot e_{n+2}$）以 $SO(n+1)$（固定 $e_{n+2}$ 的旋转）为纤维。这是 $S^{n+1}$ 切丛 $TS^{n+1}$ 的标架主丛：在 $p\in S^{n+1}$ 处，纤维 $\pi^{-1}(p)$ 由把 $e_{n+2}$ 送到 $p$ 的正交标架组成，等价于 $T_pS^{n+1}$ 的正定向正交标架。故伴随丛 $SO(n+2)\times_{SO(n+1)}\mathbb{R}^{n+1}\cong TS^{n+1}$。

### 步骤 2：连接同态给出切换函数

取 $\pi_{n+1}(S^{n+1})$ 的生成元 $[id]$（恒等映射）。将 $S^{n+1}$ 分为北半球 $D_+$、南半球 $D_-$，赤道 $S^n$。恒等映射 $id:S^{n+1}\to S^{n+1}$ 在每个闭半球上提升到 $SO(n+2)$：
- 北半球：$s_+(x)=$ 把 $e_{n+2}$ 沿测地线旋转到 $x$ 的旋转（北极平凡化）；
- 南半球：$s_-(x)=$ 把 $-e_{n+2}$ 沿测地线旋转到 $x$ 的旋转（南极平凡化）。

在赤道 $p\in S^n$ 上，两个提升之差 $g(p)=s_-(p)^{-1}s_+(p)\in SO(n+1)$（固定 $e_{n+2}$ 的子群）就是 $TS^{n+1}$ 的切换函数。连接同态
$$
\partial([id]) = [g] \in \pi_n(SO(n+1)).
$$

### 步骤 3：Euler 类 $=$ $\alpha_*$ 作用于切换函数

**关键事实**（见 Milnor–Stasheff《Characteristic Classes》§9，或 Husemoller《Fibre Bundles》）：设 $\xi$ 是 $S^k$ 上秩 $k$ 的定向向量丛，切换函数 $f:S^{k-1}\to SO(k)$，则其 Euler 类满足
$$
e(\xi) = \alpha_*([f]) \in \pi_{k-1}(S^{k-1})\cong\mathbb{Z},
$$
其中 $\alpha:SO(k)\to S^{k-1}$ 取列投影（取最后一列或第一列，二者给出同一类，因为 $SO(k)$ 连通且两投影相差一个固定旋转的同伦）。

**符号锚定**（$k=2$）：$TS^2$ 的切换函数为 $\theta\mapsto$ 旋转 $2\theta$，$\alpha_*$ 给出 degree $2 = \chi(S^2)$，确认 $\alpha_*([f])=+e(\xi)$，无额外符号因子。

### 步骤 4：复合态射 $=$ Euler 类 $=$ 示性数

由步骤 2、3，
$$
\alpha_*\circ\partial([id]) = \alpha_*([g]) = e(TS^{n+1}).
$$
对切丛有经典关系 $e(TS^{n+1}) = \chi(S^{n+1})\cdot[S^{n+1}]^*\in H^{n+1}(S^{n+1};\mathbb{Z})$（Gauss–Bonnet / Poincaré–Hopf）。$S^{n+1}$ 的胞腔结构为一个 $0$ 胞腔加一个 $(n+1)$ 胞腔，故
$$
\chi(S^{n+1}) = 1 + (-1)^{n+1}.
$$
因此
$$
\lambda = \alpha_*\circ\partial([id]) = 1 + (-1)^{n+1}.
$$

### 步骤 5：直接度数计算（独立验证）

取 $\alpha$ 取最后一列的约定。切换函数经定向修正后为 $c(p)=r_p\circ r_{e_1}$（$r_p$ 为在 $p^\perp$ 内的反射，复合固定反射 $r_{e_1}$ 修正 $\det$ 到 $+1$）。复合 $\alpha\circ c:S^n\to S^n$ 给出
$$
h(x) = e_{n+1} - 2x_{n+1}\,x.
$$
取正则值 $-e_{n+1}$，原像为 $\{e_{n+1},-e_{n+1}\}$：
- 在 $e_{n+1}$ 处：$dh$ 在 $\mathrm{span}(e_1,\dots,e_n)$ 上为 $-2I$。考虑源点 $e_{n+1}$ 处切空间正定向基相对标准基的符号 $(-1)^n$、靶点 $-e_{n+1}$ 处的符号 $(-1)^{n+1}$，正定向基下行列式符号为 $(-1)^{n+1}$，local degree $=(-1)^{n+1}$。
- 在 $-e_{n+1}$ 处：$dh=2I$，源靶同点符号相同，local degree $=+1$。

总 degree $= 1 + (-1)^{n+1}$，与步骤 4 一致。取 $\alpha$ 取第一列的约定同样给出 $1+(-1)^{n+1}$。

### 步骤 6：特例验证

- $n=1$（$S^2$）：$\chi(S^2)=2$，切换函数 $\theta\mapsto 2\theta$，degree $2$ ✓
- $n=2$（$S^3$）：$S^3$ 是李群，$TS^3$ 平凡，切换函数零伦，degree $0=\chi(S^3)$ ✓
- $n=3$（$S^4$）：$\chi(S^4)=2$，公式给 $2$ ✓

## 结论

$$
\boxed{\,\lambda = 1 + (-1)^{n+1}\,}
$$

### PROOF COMPLETE
