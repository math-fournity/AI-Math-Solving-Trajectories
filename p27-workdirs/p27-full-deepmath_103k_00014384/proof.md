# Fourier Inversion for $L^1$ Functions — Symmetric Partial Integrals

## Answer

$$\boxed{\text{No}}$$

The Fourier inversion theorem in the stated form does **not** hold for every $f\in L^1(\mathbb{R})$. There exist functions $f$ with $\int_{-\infty}^{\infty}|f(x)|\,dx<\infty$ for which the symmetric partial integrals $\int_{-R}^{R}\hat{f}(w)\,e^{2\pi i xw}\,dw$ **diverge** on a set of positive measure (even almost everywhere).

The correct inversion for general $L^1$ functions requires a **summability kernel** (Cesàro/Fejér or Abel/Poisson), not the raw Dirichlet partial integral.

---

## Setup and Notation

We use the convention
$$\hat{f}(w)=\int_{-\infty}^{\infty}f(x)\,e^{-2\pi i xw}\,dx,\qquad f\in L^1(\mathbb{R}).$$

The **symmetric partial integral** is
$$S_R f(x):=\int_{-R}^{R}\hat{f}(w)\,e^{2\pi i xw}\,dw.$$

## Step 1 — $S_R f$ is a convolution with the Dirichlet kernel

By Fubini's theorem (justified since $f\in L^1$ and $e^{-2\pi i tw}$ has modulus 1 on the finite interval $[-R,R]$):

$$
S_R f(x)=\int_{-R}^{R}\left(\int_{-\infty}^{\infty}f(t)\,e^{-2\pi i tw}\,dt\right)e^{2\pi i xw}\,dw
=\int_{-\infty}^{\infty}f(t)\left(\int_{-R}^{R}e^{2\pi i (x-t)w}\,dw\right)dt.
$$

The inner integral evaluates to
$$
\int_{-R}^{R}e^{2\pi i (x-t)w}\,dw=\frac{\sin(2\pi R(x-t))}{\pi(x-t)}=:D_R(x-t),
$$
where $D_R(s)=\frac{\sin(2\pi Rs)}{\pi s}$ is the **Dirichlet kernel** (with $D_R(0)=2R$ by continuity). Thus

$$\boxed{S_R f(x)=(f*D_R)(x)=\int_{-\infty}^{\infty}f(t)\,D_R(x-t)\,dt.}$$

## Step 2 — The Dirichlet kernel is NOT an approximation to the identity

A family $\{K_R\}_{R>0}$ is an **approximation to the identity** if:
1. $\int K_R = 1$ for all $R$,
2. $\sup_R\|K_R\|_{L^1}<\infty$,
3. For every $\delta>0$, $\int_{|s|>\delta}|K_R(s)|\,ds\to 0$ as $R\to\infty$.

The Dirichlet kernel satisfies condition 1 ($\int_{-\infty}^{\infty}D_R(s)\,ds=1$ by the Fourier inversion of the rectangular window), but **fails** condition 2:

$$
\|D_R\|_{L^1}=\int_{-\infty}^{\infty}\left|\frac{\sin(2\pi Rs)}{\pi s}\right|ds
=2\int_0^{\infty}\frac{|\sin(2\pi Rs)|}{\pi s}\,ds
=\frac{2}{\pi}\int_0^{2\pi R}\frac{|\sin u|}{u}\,du.
$$

Since $\int_0^N\frac{|\sin u|}{u}\,du\sim\frac{2}{\pi}\log N$ as $N\to\infty$ (the average of $|\sin u|$ is $2/\pi$), we obtain

$$\|D_R\|_{L^1}\sim\frac{4}{\pi^2}\log(2\pi R)\xrightarrow[R\to\infty]{}\infty.$$

**The $L^1$ norm of the Dirichlet kernel grows logarithmically**, so $\{D_R\}$ is not an approximation to the identity. Consequently, the general theorem "$f*K_R\to f$ a.e. for all $f\in L^1$" does **not** apply.

## Step 3 — The Kolmogorov counterexample: $L^1$ divergence

### Fourier series analogue

**Kolmogorov (1923).** There exists $g\in L^1([0,2\pi])$ such that the symmetric partial sums of its Fourier series
$$S_N g(x)=\sum_{n=-N}^{N}\hat{g}(n)\,e^{inx}$$
**diverge for every** $x\in[0,2\pi]$.

The mechanism: the partial sum operator $S_N$ is convolution with the discrete Dirichlet kernel $D_N^{\text{disc}}(x)=\sum_{n=-N}^{N}e^{inx}=\frac{\sin((N+1/2)x)}{\sin(x/2)}$, whose $L^1([0,2\pi])$ norm grows like $\log N$. The unboundedness of the maximal operator $\sup_N|S_N g|$ on $L^1$ allows construction of an $L^1$ function with everywhere divergence.

### Transfer to the Fourier transform on $\mathbb{R}$

We transfer the counterexample from the torus $\mathbb{T}=[0,2\pi]$ to $\mathbb{R}$.

**Construction.** Let $g\in L^1([0,1])$ be a Kolmogorov-type function whose Fourier series diverges a.e. on $[0,1]$. Define $f:\mathbb{R}\to\mathbb{C}$ by
$$f(x)=g(x)\cdot\mathbf{1}_{[0,1]}(x).$$
Then $f\in L^1(\mathbb{R})$ with $\|f\|_{L^1}=\|g\|_{L^1([0,1])}<\infty$.

The Fourier transform of $f$ is
$$\hat{f}(w)=\int_0^1 g(t)\,e^{-2\pi i tw}\,dt.$$

The symmetric partial integral at $x\in(0,1)$ is
$$S_R f(x)=\int_{-\infty}^{\infty}f(t)\,D_R(x-t)\,dt=\int_0^1 g(t)\,\frac{\sin(2\pi R(x-t))}{\pi(x-t)}\,dt.$$

**Relation to Fourier series.** The Fourier partial sum of $g$ (periodized to $[0,1]$) at $x$ is
$$S_N^{\text{series}}g(x)=\int_0^1 g(t)\sum_{n=-N}^{N}e^{2\pi i n(x-t)}\,dt=\int_0^1 g(t)\,\frac{\sin(\pi(2N+1)(x-t))}{\sin(\pi(x-t))}\,dt.$$

The continuous partial integral $S_R f(x)$ replaces the discrete kernel $\frac{\sin(\pi(2N+1)(x-t))}{\sin(\pi(x-t))}$ with the continuous kernel $\frac{\sin(2\pi R(x-t))}{\pi(x-t)}$.

**Key observation.** Both kernels share the same pathology: their $L^1$ norms grow logarithmically. The continuous Dirichlet maximal operator
$$\mathcal{C}f(x)=\sup_{R>0}|S_R f(x)|=\sup_{R>0}\left|\int_{-\infty}^{\infty}f(t)\,\frac{\sin(2\pi R(x-t))}{\pi(x-t)}\,dt\right|$$
is the **Carleson maximal operator** on $\mathbb{R}$.

**Carleson–Hunt theorem (1966–1968).** $\mathcal{C}$ is bounded on $L^p(\mathbb{R})$ for $1<p<\infty$, and consequently $S_R f(x)\to f(x)$ a.e. for $f\in L^p(\mathbb{R})$, $1<p<\infty$.

**Failure at $p=1$.** The operator $\mathcal{C}$ is **not** bounded from $L^1$ to weak-$L^1$. This follows from the same mechanism as on the torus: the logarithmic growth of $\|D_R\|_{L^1}$ implies, via the uniform boundedness principle, that the operators $S_R:L^1\to L^0$ (convergence in measure) cannot all be uniformly controlled. More precisely:

Consider the linear functionals on $L^1(\mathbb{R})$ defined by $T_R(f)=S_R f(x_0)$ for a fixed Lebesgue point $x_0$. Each $T_R$ has operator norm $\|D_R\|_\infty=2R$, but the relevant quantity for a.e. convergence is the maximal operator. By the Stein uniform boundedness principle for symmetric diffusion semigroups (or directly), if $S_R f\to f$ a.e. for all $f\in L^1$, then $\mathcal{C}$ would be weak-type $(1,1)$, which contradicts the logarithmic growth of $\|D_R\|_{L^1}$.

**Explicit counterexample.** Using the transfer from the torus: there exists $f\in L^1(\mathbb{R})$, supported on $[0,1]$, such that $S_R f(x)$ diverges for a.e. $x\in[0,1]$ (in fact, the construction can be made to diverge everywhere on a set of positive measure). This is achieved by the same transference principle that carries Kolmogorov's $L^1(\mathbb{T})$ counterexample to $L^1(\mathbb{R})$: the restriction of the continuous Dirichlet kernel to $[0,1]$ majorizes (up to constants) the discrete Dirichlet kernel, so the divergence of the discrete partial sums implies divergence of the continuous partial integrals.

## Step 4 — Conclusion

For a general $f\in L^1(\mathbb{R})$:

- $\hat{f}$ is well-defined, continuous, bounded, and $\hat{f}(w)\to 0$ as $|w|\to\infty$ (Riemann–Lebesgue).
- The symmetric partial integral $S_R f(x)=(f*D_R)(x)$ is well-defined for all $x$ and $R>0$.
- **However**, $S_R f(x)\to f(x)$ a.e. is **not guaranteed**. The Dirichlet kernel is not an approximation to the identity ($\|D_R\|_{L^1}\to\infty$), and the Carleson maximal operator is unbounded on $L^1$.
- There exist $f\in L^1(\mathbb{R})$ for which $S_R f(x)$ diverges on a set of positive measure.

Therefore, the stated formula
$$f(x)=\lim_{R\to+\infty}\int_{-R}^{R}\hat{f}(w)\,e^{2\pi i xw}\,dw$$
does **not** hold for almost every $x$ for every $f\in L^1(\mathbb{R})$.

$$\boxed{\text{No}}$$

---

## Remark — The Correct Inversion for $L^1$

What **does** hold for every $f\in L^1(\mathbb{R})$ is inversion via a **summability kernel** (approximation to the identity):

**Fejér (Cesàro) inversion.** At every Lebesgue point $x$ of $f$:
$$f(x)=\lim_{R\to\infty}\int_{-\infty}^{\infty}\left(1-\frac{|w|}{R}\right)_+\hat{f}(w)\,e^{2\pi i xw}\,dw
=\lim_{R\to\infty}(f*F_R)(x),$$
where $F_R(s)=R\left(\frac{\sin(\pi Rs)}{\pi Rs}\right)^2$ is the **Fejér kernel**, satisfying $\|F_R\|_{L^1}=1$ and $F_R\geq 0$ (hence an approximation to the identity).

**Abel (Poisson) inversion.** At every Lebesgue point $x$:
$$f(x)=\lim_{\epsilon\to 0^+}\int_{-\infty}^{\infty}e^{-2\pi\epsilon|w|}\hat{f}(w)\,e^{2\pi i xw}\,dw
=\lim_{\epsilon\to 0^+}(f*P_\epsilon)(x),$$
where $P_\epsilon(s)=\frac{1}{\pi}\frac{\epsilon}{\epsilon^2+s^2}$ is the **Poisson kernel**.

**Inversion when $\hat{f}\in L^1$.** If additionally $\hat{f}\in L^1(\mathbb{R})$, then $f$ has a continuous representative and
$$f(x)=\int_{-\infty}^{\infty}\hat{f}(w)\,e^{2\pi i xw}\,dw\quad\text{for all }x,$$
with the integral converging absolutely (no principal value needed).

The crucial distinction: the Fejér and Poisson kernels are **non-negative** approximations to the identity with bounded $L^1$ norm, while the Dirichlet kernel oscillates and has unbounded $L^1$ norm. This is why summability methods succeed for all $L^1$ functions where the raw partial integral fails.
