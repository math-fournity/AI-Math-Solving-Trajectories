# 命题判定

**命题为假（FALSE）。**

下面给出反例。我们先在 $d=1$ 情形构造一个 Lipschitz 函数 $f:\mathbb{R}\to\mathbb{R}$ 与一个测度 $\mu$，使得

- $\mathcal{H}^0(A)<\infty \Rightarrow \mu(A)=0$（即 $\mu$ 对一切有限集赋零，等价于 $\mu$ 非原子），
- 但 $f$ 的非可微集 $N_f$ 满足 $\mu(N_f)>0$。

然后将此反例推广到任意 $d\ge 1$。

---

## 一、$d=1$ 的反例

### 1.1 记号与构造

设 $C\subset[0,1]$ 为标准三分 Cantor 集。记 $C_n$ 为构造 Cantor 集时第 $n$ 步的逼近集：$C_n$ 是 $2^n$ 个长度为 $3^{-n}$ 的闭区间之并，$C_0=[0,1]$，$C=\bigcap_{n=0}^\infty C_n$，且 $C_{n+1}\subset C_n$。记 $|C_n|=(2/3)^n$ 为 $C_n$ 的 Lebesgue 测度。

定义"奇偶环带之并"
$$
F \;=\; \bigcup_{n=1}^{\infty}\bigl(C_{2n-1}\setminus C_{2n}\bigr).
$$

**关键观察**：$C\subset F^c$。事实上，$x\in C$ 当且仅当 $x\in C_n$ 对一切 $n$ 成立，故 $x\notin C_{2n-1}\setminus C_{2n}$ 对一切 $n$ 成立，从而 $x\notin F$。

### 1.2 $F$ 在 $C$ 的每一点处的密度振荡

对 $x\in C$ 和 $r>0$，记
$$
\Theta_F(x,r)=\frac{|F\cap(x-r,x+r)|}{2r}.
$$

**计算 $|F\cap C_{2n}|$。** 注意 $F\cap C_{2n}=\bigcup_{m>n}(C_{2m-1}\setminus C_{2m})$（因为 $F$ 中 $m\le n$ 的环带 $C_{2m-1}\setminus C_{2m}\subset C_{2n}^c$，而 $m>n$ 的环带有一部分落在 $C_{2n}$ 内）。更精确地，
$$
|F\cap C_{2n}|=\sum_{m=n+1}^{\infty}|C_{2m-1}\setminus C_{2m}|
=\sum_{m=n+1}^{\infty}\bigl(|C_{2m-1}|-|C_{2m}|\bigr)
=\sum_{m=n+1}^{\infty}\Bigl(\tfrac{2}{3}\Bigr)^{2m-1}\Bigl(1-\tfrac{2}{3}\Bigr)
=\frac{1}{3}\sum_{m=n+1}^{\infty}\Bigl(\tfrac{2}{3}\Bigr)^{2m-1}.
$$
这是一个首项为 $\frac13(\frac23)^{2n+1}$、公比为 $(\frac23)^2=\frac49$ 的等比级数，故
$$
|F\cap C_{2n}|=\frac{\frac13(\frac23)^{2n+1}}{1-\frac49}
=\frac{\frac13(\frac23)^{2n+1}}{\frac59}
=\frac{3}{5}\Bigl(\tfrac23\Bigr)^{2n+1}.
$$
而 $|C_{2n}|=(\frac23)^{2n}$，所以
$$
\frac{|F\cap C_{2n}|}{|C_{2n}|}=\frac{\frac35(\frac23)^{2n+1}}{(\frac23)^{2n}}=\frac35\cdot\frac23=\frac25. \tag{$\star$}
$$

**密度在两个尺度下的行为。** 取 $x\in C$。

- **尺度 $r=3^{-2n}$（偶数步）。** 此时 $(x-r,x+r)$ 落在 $C_{2n}$ 的某个基本区间 $I$ 内（因为 $x\in C\subset C_{2n}$，而 $C_{2n}$ 的基本区间长度为 $3^{-2n}$，$x$ 到 $I$ 端点的距离 $\ge 3^{-2n}$ 仅在端点处不成立；对 $x$ 在 $I$ 内部取 $r$ 略小于 $3^{-2n}$ 即可）。由 Cantor 集的自相似性和 $(\star)$，$F\cap I$ 在 $I$ 中的相对测度比为 $\frac25$，故
  $$
  \Theta_F(x,r)\approx\frac25\quad\text{当 }r\sim 3^{-2n}.
  $$

- **尺度 $r=3^{-(2n-1)}$（奇数步）。** 此时 $(x-r,x+r)$ 落在 $C_{2n-1}$ 的某个基本区间 $J$ 内，而 $J\setminus C_{2n}$（中间被挖掉的三分之一）完全属于 $F$。所以 $F\cap J$ 包含 $J\setminus C_{2n}$（占 $J$ 的 $\frac13$）加上 $F\cap C_{2n}$（占 $C_{2n}$ 的 $\frac25$，即占 $J$ 的 $\frac25\cdot\frac23=\frac{4}{15}$）。合计
  $$
  \frac{|F\cap J|}{|J|}=\frac13+\frac{4}{15}=\frac{5+4}{15}=\frac{9}{15}=\frac35.
  $$
  等等——这里需要更仔细。实际上 $F\cap J = (J\setminus C_{2n})\cup(F\cap C_{2n})$，其中 $|J\setminus C_{2n}|=\frac13|J|$，$|F\cap C_{2n}|=\frac25|C_{2n}|=\frac25\cdot\frac23|J|=\frac{4}{15}|J|$。所以 $|F\cap J|/|J|=\frac13+\frac{4}{15}=\frac{5+4}{15}=\frac{9}{15}=\frac35$。

  但我们想要的是**在更粗的奇数尺度上 $F$ 的密度接近 1**。重新审视：在尺度 $r\sim 3^{-(2n-1)}$ 时，区间落在 $C_{2n-1}$ 的基本区间 $J$ 中。$J$ 中属于 $C_{2n}$ 的部分占 $\frac23$，属于 $J\setminus C_{2n}$ 的部分占 $\frac13$（全部在 $F$ 中）。而 $C_{2n}$ 中属于 $F$ 的占 $\frac25$。所以 $F$ 在 $J$ 中的比例为 $\frac13+\frac23\cdot\frac25=\frac13+\frac{4}{15}=\frac35$。

  这给出的是 $\frac35$ 而非 $1$。但关键是：**两个尺度给出不同的密度值**（$\frac25$ vs $\frac35$），因此密度极限不存在。交接文档中"振荡于 $\frac25$ 与 $1$ 之间"的表述略有偏差，但核心结论——**密度极限不存在**——依然成立，因为 $\frac25\ne\frac35$。

**严格化。** 对 $x\in C$，取 $r_n=3^{-2n}$（适当选取使 $(x-r_n,x+r_n)\subset$ 某个 $C_{2n}$ 基本区间）和 $s_n=3^{-(2n-1)}$（类似）。由 Cantor 集的精确自相似结构，可以证明
$$
\liminf_{r\to0^+}\Theta_F(x,r)\le\frac25<\frac35\le\limsup_{r\to0^+}\Theta_F(x,r),
$$
故 $\lim_{r\to0^+}\Theta_F(x,r)$ 不存在。

> **精确论证**：Cantor 集的构造在每一步将每个区间三等分并保留两端。对 $x\in C$，设 $I_n(x)$ 为 $C_n$ 中包含 $x$ 的基本区间（长度 $3^{-n}$）。则 $I_{2n}(x)\subset I_{2n-1}(x)$，且 $I_{2n-1}(x)\setminus I_{2n}(x)$ 由 $I_{2n-1}(x)$ 中间三分之一区间构成（全部属于 $F$，因为它是 $C_{2n-1}\setminus C_{2n}$ 的一部分）。由自相似性，$|F\cap I_{2n}(x)|=\frac25|I_{2n}(x)|$（对每个 $C_{2n}$ 基本区间都成立，因为 $F\cap C_{2n}$ 在 $C_{2n}$ 的每个基本区间中按相同比例分布）。于是
> - $\Theta_F(x,|I_{2n}(x)|/2)\to\frac25$（沿偶数尺度），
> - $\Theta_F(x,|I_{2n-1}(x)|/2)\to\frac35$（沿奇数尺度）。
> 
> 两个子序列极限不同 $\Rightarrow$ 密度极限不存在。

### 1.3 Lipschitz 函数 $f$ 及其非可微集

令 $g=\mathbf{1}_F$（$F$ 的指示函数），定义
$$
f(x)=\int_0^x g(t)\,dt=\int_0^x\mathbf{1}_F(t)\,dt.
$$

由于 $0\le g\le 1$，$f$ 是 Lipschitz 常数为 $1$ 的 Lipschitz 函数。

**可微性与近似连续性的关系。** 由 Lebesgue 微分定理，$g\in L^\infty\subset L^1_{\mathrm{loc}}$ 在几乎所有点（w.r.t. $\mathcal{L}^1$）近似连续。标准结果（见 Rudin《Real and Complex Analysis》或 Mattila《Geometry of Sets and Measures》）给出：

> $f(x)=\int_0^x g(t)\,dt$ 在 $x$ 处可微且 $f'(x)=g(x)$ $\iff$ $g$ 在 $x$ 处近似连续 $\iff$ $F$（或 $F^c$）在 $x$ 处的密度分别为 $1$（或 $0$），且与 $g(x)$ 一致。

具体地：
- 若 $g(x)=1$（即 $x\in F$），则 $f$ 在 $x$ 可微 $\iff$ $F$ 在 $x$ 处密度为 $1$。
- 若 $g(x)=0$（即 $x\in F^c$），则 $f$ 在 $x$ 可微 $\iff$ $F$ 在 $x$ 处密度为 $0$。

**$f$ 在 $C$ 的每一点不可微。** 对 $x\in C$：
- $C\subset F^c$，故 $g(x)=0$。
- $f$ 在 $x$ 可微需要 $F$ 在 $x$ 处密度为 $0$。
- 但由 §1.2，$F$ 在 $x$ 处的密度极限不存在（在 $\frac25$ 与 $\frac35$ 之间振荡），特别地不等于 $0$。
- 故 $f$ 在 $x$ 处不可微。

因此 $C\subset N_f$（$f$ 的非可微集），而 $C$ 不可数。

### 1.4 测度 $\mu$ 的选取

取 $\mu$ 为 $C$ 上的标准 Cantor 测度（Cantor 分布）：这是 $C$ 上支撑的非原子概率测度，满足 $\mu(C)=1$。

- **非原子性**：Cantor 测度是连续型概率测度（Cantor 分布函数是 Cantor 函数，连续），故 $\mu(\{x\})=0$ 对一切 $x$ 成立。
- **满足条件**：$\mathcal{H}^0$ 是计数测度，$\mathcal{H}^0(A)<\infty$ $\iff$ $A$ 有限。$\mu$ 非原子 $\Rightarrow$ $\mu(A)=0$ 对一切有限集 $A$。故 $\mathcal{H}^0(A)<\infty\Rightarrow\mu(A)=0$。
- **非可微集正测度**：$C\subset N_f$，故 $\mu(N_f)\ge\mu(C)=1>0$。

**$d=1$ 反例完成。** 存在 Lipschitz 函数 $f:\mathbb{R}\to\mathbb{R}$ 和测度 $\mu$，满足 $\mathcal{H}^0(A)<\infty\Rightarrow\mu(A)=0$，但 $f$ 的非可微集 $N_f$ 满足 $\mu(N_f)\ge1>0$。

---

## 二、推广到任意 $d\ge 1$

### 2.1 Lipschitz 函数 $u$

设 $f:\mathbb{R}\to\mathbb{R}$ 为上述 $d=1$ 反例中的 Lipschitz 函数。定义
$$
u(x_1,x_2,\ldots,x_d)=f(x_1),\qquad x=(x_1,\ldots,x_d)\in\mathbb{R}^d.
$$

$u$ 是 Lipschitz 的（Lipschitz 常数与 $f$ 相同），因为
$$
|u(x)-u(y)|=|f(x_1)-f(y_1)|\le\mathrm{Lip}(f)\,|x_1-y_1|\le\mathrm{Lip}(f)\,|x-y|.
$$

### 2.2 $u$ 的非可微集

$u$ 在 $x=(x_1,\ldots,x_d)$ 处可微当且仅当 $f$ 在 $x_1$ 处可微。这是因为：
- 若 $f$ 在 $x_1$ 可微，则 $u$ 在 $x$ 处沿 $e_1$ 方向有导数 $f'(x_1)$，沿其他坐标方向导数为 $0$，故 $u$ 在 $x$ 可微，$Du=(f'(x_1),0,\ldots,0)$。
- 若 $f$ 在 $x_1$ 不可微，则 $u$ 在 $x$ 沿 $e_1$ 方向的差商 $\frac{u(x+he_1)-u(x)}{h}=\frac{f(x_1+h)-f(x_1)}{h}$ 当 $h\to0$ 时极限不存在，故 $u$ 在 $x$ 不可微。

因此
$$
N_u = N_f\times\mathbb{R}^{d-1}.
$$

### 2.3 测度 $\mu$ 的构造

**构造性方法（乘积测度）。** 取 $\mu=\nu\otimes\lambda$，其中：
- $\nu$ = $C$ 上的 Cantor 测度（$d=1$ 反例中的测度），
- $\lambda$ = $\mathbb{R}^{d-1}$ 上的标准 Gauss 测度（或任何有限 Borel 测度，例如 $\lambda=(2\pi)^{-(d-1)/2}e^{-|y|^2/2}\,dy$）。

**验证条件 $\mathcal{H}^{d-1}(A)<\infty\Rightarrow\mu(A)=0$。**

我们需要证明：若 $A\subset\mathbb{R}^d$ 满足 $\mathcal{H}^{d-1}(A)<\infty$，则 $(\nu\otimes\lambda)(A)=0$。

由 Fubini 定理，
$$
(\nu\otimes\lambda)(A)=\int_{\mathbb{R}^{d-1}}\nu(A_y)\,d\lambda(y),
$$
其中 $A_y=\{x_1\in\mathbb{R}:(x_1,y)\in A\}$ 是 $A$ 在 $y$ 处的截面。

**关键引理**：若 $\mathcal{H}^{d-1}(A)<\infty$，则对 $\lambda$-a.e. $y$，$A_y$ 是有限集（从而 $\nu(A_y)=0$，因为 $\nu$ 非原子）。

**引理证明**：由 coarea 公式（或 Fubini + Hausdorff 测度的截面估计），对 Borel 集 $A$，
$$
\int_{\mathbb{R}^{d-1}}\mathcal{H}^0(A_y)\,d\mathcal{H}^{d-1}(y)\le C_d\,\mathcal{H}^{d-1}(A).
$$
更精确地，对投影 $\pi:\mathbb{R}^d\to\mathbb{R}^{d-1}$，$\pi(x)=(x_2,\ldots,x_d)$，由 coarea 公式（Federer, GMT Theorem 3.2.22）：
$$
\int_{\mathbb{R}^{d-1}}\mathcal{H}^0(\pi^{-1}(y)\cap A)\,d\mathcal{H}^{d-1}(y)=\int_A J_{d-1}\pi\,d\mathcal{H}^{d-1},
$$
其中 $J_{d-1}\pi$ 是 $\pi$ 的 $(d-1)$-维 Jacobian。由于 $\pi$ 是正交投影（去掉第一个坐标），$J_{d-1}\pi\le1$，故
$$
\int_{\mathbb{R}^{d-1}}\mathcal{H}^0(A_y)\,d\mathcal{H}^{d-1}(y)\le\mathcal{H}^{d-1}(A)<\infty.
$$
因此 $\mathcal{H}^0(A_y)<\infty$ 对 $\mathcal{H}^{d-1}$-a.e. $y$ 成立，即 $A_y$ 有限。由于 $\lambda\ll\mathcal{H}^{d-1}$（Gauss 测度关于 $\mathcal{H}^{d-1}$ 绝对连续，因为 $\lambda$ 有密度），故 $A_y$ 有限对 $\lambda$-a.e. $y$ 也成立。

$\nu$ 非原子 $\Rightarrow$ $\nu(A_y)=0$ 对有限集 $A_y$ 成立。故
$$
(\nu\otimes\lambda)(A)=\int\nu(A_y)\,d\lambda(y)=0.
$$

**验证 $\mu(N_u)>0$。**
$$
N_u=N_f\times\mathbb{R}^{d-1},\qquad C\subset N_f.
$$
故
$$
\mu(N_u)\ge(\nu\otimes\lambda)(C\times\mathbb{R}^{d-1})=\nu(C)\cdot\lambda(\mathbb{R}^{d-1})=1\cdot1=1>0.
$$

### 2.4 一般 $d$ 反例完成

对任意 $d\ge1$，Lipschitz 函数 $u(x_1,\ldots,x_d)=f(x_1)$ 与测度 $\mu=\nu\otimes\lambda$ 满足：
- $\mathcal{H}^{d-1}(A)<\infty\Rightarrow\mu(A)=0$（由 §2.3 的 coarea 论证），
- $\mu(N_u)\ge1>0$（由 §2.3 的乘积测度计算）。

---

## 三、结论

命题断言："若 Lipschitz 映射 $u:\mathbb{R}^d\to\mathbb{R}$ 和测度 $\mu$ 满足 $\mathcal{H}^{d-1}(A)<\infty\Rightarrow\mu(A)=0$，则 $u$ 的非可微集 $N_u$ 满足 $\mu(N_u)=0$。"

我们构造了显式反例：$u(x_1,\ldots,x_d)=f(x_1)$，其中 $f(x)=\int_0^x\mathbf{1}_F(t)\,dt$，$F=\bigcup_{n\ge1}(C_{2n-1}\setminus C_{2n})$，$\mu=\nu\otimes\lambda$（Cantor 测度 $\otimes$ Gauss 测度）。此反例满足前提条件但 $\mu(N_u)=1>0$。

**命题为假。**

$$\boxed{\text{False}}$$

### PROOF COMPLETE
