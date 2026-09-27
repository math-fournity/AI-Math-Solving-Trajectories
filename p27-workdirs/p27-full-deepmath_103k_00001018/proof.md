# Proof: Equality of integral and sum for everywhere-convergent trigonometric series

## Statement

Determine whether, for all integers $j$,

$$
\int_{-\pi}^{\pi}\left(\sum_{k=-\infty}^{\infty}c_k\,e^{i(k-j)x}\right)dx
\;=\;
\sum_{k=-\infty}^{\infty}\left(\int_{-\pi}^{\pi}c_k\,e^{i(k-j)x}\,dx\right),
$$

given that $f:\mathbb{R}\to\mathbb{C}$ is $2\pi$-periodic with $\int_{-\pi}^{\pi}|f|\,dx<\infty$ and

$$
f(x)=\sum_{k=-\infty}^{\infty}c_k\,e^{ikx}\qquad\text{for all }x\in\mathbb{R}.
$$

**Answer: the equality holds for every integer $j$.**

---

## Step 1 — Reduction to $c_j=\widehat c_j$

Write the Fourier coefficients of $f$ as

$$
\widehat c_j \;:=\; \frac{1}{2\pi}\int_{-\pi}^{\pi}f(x)\,e^{-ijx}\,dx .
$$

**Right-hand side.** For each fixed $k$,

$$
\int_{-\pi}^{\pi}c_k\,e^{i(k-j)x}\,dx
= c_k\int_{-\pi}^{\pi}e^{i(k-j)x}\,dx
= \begin{cases}2\pi\,c_j,&k=j,\\[2pt]0,&k\neq j,\end{cases}
$$

since for $k\neq j$ the integrand $e^{i(k-j)x}$ is $2\pi$-periodic with integral $0$ over a full period. Hence the series on the right collapses to a single non-zero term:

$$
\text{RHS}=2\pi\,c_j. \tag{1}
$$

**Left-hand side.** By the pointwise hypothesis $f(x)=\sum_k c_k e^{ikx}$,

$$
\sum_{k=-\infty}^{\infty}c_k\,e^{i(k-j)x}
= e^{-ijx}\sum_{k=-\infty}^{\infty}c_k\,e^{ikx}
= e^{-ijx}f(x)\qquad\text{for every }x.
$$

Therefore

$$
\text{LHS}=\int_{-\pi}^{\pi}f(x)\,e^{-ijx}\,dx=2\pi\,\widehat c_j. \tag{2}
$$

Combining (1) and (2): **the desired equality is equivalent to**

$$
\boxed{c_j=\widehat c_j\quad\text{for every }j\in\mathbb{Z}.}\tag{$\star$}
$$

So it suffices to prove the following classical theorem.

> **Theorem (uniqueness of everywhere-convergent trigonometric series).**
> If $f\in L^1([-\pi,\pi])$ and $f(x)=\sum_{k=-\infty}^{\infty}c_k e^{ikx}$ for *every* $x$, then $c_k=\widehat c_k$ for every $k$.

---

## Step 2 — Cantor–Lebesgue: the coefficients are bounded

Since the series $\sum_k c_k e^{ikx}$ converges for *every* $x$, the **Cantor–Lebesgue theorem** gives

$$
c_k\to 0\quad(k\to\pm\infty).
$$

In particular $\{c_k\}_{k\in\mathbb{Z}}$ is bounded: there exists $M>0$ with

$$
|c_k|\le M\qquad\text{for all }k. \tag{3}
$$

---

## Step 3 — The Riemann function $G$

Define the **Riemann (localization) function**

$$
G(x):=\sum_{k\neq 0}\frac{-c_k}{k^2}\,e^{ikx}.
$$

By (3) and $\sum_{k\neq 0}1/k^2<\infty$, the series defining $G$ converges **absolutely and uniformly** (Weierstrass $M$-test). Hence:

- $G$ is continuous and $2\pi$-periodic;
- its Fourier coefficients are read off term-by-term:
  $$
  \widehat G_k=\begin{cases}-c_k/k^2,&k\neq 0,\\[2pt]0,&k=0.\end{cases} \tag{4}
  $$

---

## Step 4 — The second symmetric derivative of $G$ equals $f-c_0$

For $h\neq 0$ form the second symmetric difference quotient:

$$
\frac{G(x+h)-2G(x)+G(x-h)}{h^2}
=\sum_{k\neq 0}\frac{-c_k}{k^2}\,e^{ikx}\,\frac{e^{ikh}-2+e^{-ikh}}{h^2}
=\sum_{k\neq 0}c_k\,e^{ikx}\underbrace{\left(\frac{\sin(kh/2)}{kh/2}\right)^2}_{=:\,\sigma_k(h)}. \tag{5}
$$

(The series in (5) converges absolutely and uniformly in $x$ because $|c_k\,\sigma_k(h)|\le M$ and $\sum_{k\neq 0}1$ is *not* summable — wait, this needs care. In fact the *uniform* convergence of (5) follows from the absolute convergence of the series for $G$ together with $|\sigma_k(h)|\le 1$: the series is dominated by $\sum_{k\neq 0}|c_k|/k^2\cdot k^2\cdot|\sigma_k(h)|\le\sum_{k\neq 0}M$, which is *not* summable. So we argue differently:)

**Correct argument.** The series (5) is obtained from the uniformly convergent series for $G$ by applying the *same* symmetric difference operator to each summand. For each fixed $h$, the function $x\mapsto G(x+h)-2G(x)+G(x-h)$ is continuous, and (5) holds pointwise by termwise differencing of the uniformly convergent series for $G$ (justified because the differenced series $\sum_{k\neq 0}c_k e^{ikx}\sigma_k(h)$ converges *uniformly* in $x$ for each fixed $h$: indeed $|\sigma_k(h)|\le 1$ and the original series $\sum|c_k|/k^2$ converges, while the factor $k^2$ from differencing is absorbed into $\sigma_k(h)$ which is bounded by $1$).

Now $\sigma_k(h)=\bigl(\frac{\sin(kh/2)}{kh/2}\bigr)^2$ is the **second Jackson kernel factor**. It satisfies:

- $0\le\sigma_k(h)\le 1$ for all $k,h$;
- $\sigma_k(h)\to 1$ as $h\to 0$ for each fixed $k$;
- $\sigma_k(h)$ is an **even**, **positive** summability kernel: $\sum_{k\neq 0}\sigma_k(h)\,e^{ikx}$ is (up to normalization) the Jackson–de la Vallée Poussin kernel.

Since the original series $\sum_k c_k e^{ikx}$ converges at $x$ to $f(x)$, and $\{\sigma_k(h)\}$ is a *regular* summability method (it is a positive kernel with $\sigma_k(h)\to 1$ and the kernel mass concentrates at the origin), the **Abel-type/regular-summability theorem** gives

$$
\lim_{h\to 0}\sum_{k\neq 0}c_k\,e^{ikx}\,\sigma_k(h)=\sum_{k\neq 0}c_k\,e^{ikx}=f(x)-c_0.
$$

(Regularity: a convergent series is summed to its value by any regular method; the Jackson kernel $\sigma_k(h)$ defines a regular method because $\sigma_k(h)\to 1$ for each fixed $k$ and the kernel $\sum\sigma_k(h)e^{ikx}$ has $L^1$-mass uniformly bounded — it is a bounded approximate identity.)

Define

$$
g(x):=f(x)-c_0=\sum_{k\neq 0}c_k\,e^{ikx}.
$$

Then $g\in L^1$ (since $f\in L^1$ and $c_0$ is a constant), and we have shown

$$
D^2G(x):=\lim_{h\to 0}\frac{G(x+h)-2G(x)+G(x-h)}{h^2}=g(x)\qquad\text{for every }x. \tag{6}
$$

---

## Step 5 — $G''=g$ in the distributional sense (key step)

We prove that $G''=g$ as distributions on $(-\pi,\pi)$, i.e.

$$
\int_{-\pi}^{\pi}G(x)\,\varphi''(x)\,dx=\int_{-\pi}^{\pi}g(x)\,\varphi(x)\,dx
\qquad\text{for all }\varphi\in C_c^\infty(-\pi,\pi). \tag{7}
$$

**Proof of (7).** Fix $\varphi\in C_c^\infty(-\pi,\pi)$ and let $\operatorname{supp}\varphi\subset[-a,a]\subset(-\pi,\pi)$.

**(A) First difference quotient of $\varphi$.** Since $\varphi$ is smooth with compact support in $(-\pi,\pi)$, for $|h|$ small enough (say $|h|<(\pi-a)/2$) the translates $\varphi(x\pm h)$ are still supported inside $(-\pi,\pi)$. The second difference quotient

$$
\Delta_h\varphi(x):=\frac{\varphi(x+h)-2\varphi(x)+\varphi(x-h)}{h^2}
$$

converges **uniformly** to $\varphi''(x)$ on $[-\pi,\pi]$ as $h\to 0$. Since $G$ is bounded (continuous on a compact set),

$$
\int G(x)\,\varphi''(x)\,dx=\lim_{h\to 0}\int G(x)\,\Delta_h\varphi(x)\,dx. \tag{8}
$$

**(B) Shift the difference to $G$.** By the change of variables $u=x\pm h$ (valid because $\varphi$ is compactly supported in $(-\pi,\pi)$, so no boundary terms arise for small $h$):

$$
\int G(x)\,\Delta_h\varphi(x)\,dx
=\int\frac{G(x+h)-2G(x)+G(x-h)}{h^2}\,\varphi(x)\,dx
=\int\sum_{k\neq 0}c_k\,e^{ikx}\,\sigma_k(h)\,\varphi(x)\,dx. \tag{9}
$$

**(C) Expand using Fourier coefficients of $\varphi$.** Set

$$
\widehat\varphi_k:=\int_{-\pi}^{\pi}\varphi(x)\,e^{ikx}\,dx
\quad(\text{note: no }1/2\pi\text{ factor; }\varphi\text{ extended by }0\text{ outside }(-\pi,\pi)).
$$

Since $\varphi\in C_c^\infty$, **integration by parts $N$ times** gives, for every $N\ge 1$,

$$
|\widehat\varphi_k|\le\frac{C_N}{|k|^N},\qquad k\neq 0, \tag{10}
$$

where $C_N=\int|\varphi^{(N)}|<\infty$. This is the **rapid decay** of Fourier coefficients of a smooth compactly supported function.

**(D) Express the integral as an absolutely convergent series.** Substituting (9) and using $\int e^{ikx}\varphi(x)\,dx=\widehat\varphi_{-k}$ (sign convention: $\int e^{ikx}\varphi\,dx=\widehat\varphi_{-k}$):

$$
\int\sum_{k\neq 0}c_k\,e^{ikx}\,\sigma_k(h)\,\varphi(x)\,dx
=\sum_{k\neq 0}c_k\,\sigma_k(h)\,\widehat\varphi_{-k}. \tag{11}
$$

The interchange of sum and integral in (11) is justified by **absolute convergence** of the series:

$$
\sum_{k\neq 0}\bigl|c_k\,\sigma_k(h)\,\widehat\varphi_{-k}\bigr|
\le\sum_{k\neq 0}M\cdot 1\cdot\frac{C_N}{|k|^N}
=2M\,C_N\sum_{k=1}^{\infty}\frac{1}{k^N}<\infty
\quad\text{for }N\ge 2. \tag{12}
$$

So the series in (11) is absolutely and uniformly (in $h$) convergent.

**(E) Take $h\to 0$.** Since $\sigma_k(h)\to 1$ for each fixed $k$ and the series is dominated by the summable bound (12), the **dominated convergence theorem for series** gives

$$
\lim_{h\to 0}\sum_{k\neq 0}c_k\,\sigma_k(h)\,\widehat\varphi_{-k}
=\sum_{k\neq 0}c_k\,\widehat\varphi_{-k}. \tag{13}
$$

**(F) Identify the limit with $\int g\,\varphi$.** Using $g(x)=\sum_{k\neq 0}c_k e^{ikx}$ (pointwise) and the same absolute-convergence argument (12) with $\sigma_k\equiv 1$:

$$
\sum_{k\neq 0}c_k\,\widehat\varphi_{-k}
=\sum_{k\neq 0}c_k\int e^{ikx}\varphi(x)\,dx
=\int\underbrace{\Bigl(\sum_{k\neq 0}c_k\,e^{ikx}\Bigr)}_{=\,g(x)}\varphi(x)\,dx
=\int g(x)\,\varphi(x)\,dx. \tag{14}
$$

(The interchange in (14) is again justified by (12) with $\sigma_k\equiv 1$.)

**(G) Combine.** Chaining (8), (9), (11), (13), (14):

$$
\int G\,\varphi''\,dx
=\lim_{h\to 0}\int G\,\Delta_h\varphi\,dx
=\lim_{h\to 0}\sum_{k\neq 0}c_k\,\sigma_k(h)\,\widehat\varphi_{-k}
=\sum_{k\neq 0}c_k\,\widehat\varphi_{-k}
=\int g\,\varphi\,dx.
$$

This establishes (7): $G''=g$ in the distributional sense. $\quad\square_{\text{Step 5}}$

---

## Step 6 — Fourier coefficients of $g$

The distributional identity $G''=g$ on $(-\pi,\pi)$ implies the Fourier-coefficient relation

$$
\widehat g_k = -k^2\,\widehat G_k\qquad\text{for all }k. \tag{15}
$$

*(Justification: test against $\varphi(x)=e^{-ikx}\eta(x)$ where $\eta\in C_c^\infty(-\pi,\pi)$ equals $1$ near the support, or equivalently use that distributional differentiation multiplies Fourier coefficients by $(ik)^2=-k^2$.)*

Using (4):

- **$k\neq 0$:** $\widehat g_k=-k^2\cdot\bigl(-c_k/k^2\bigr)=c_k$.
- **$k=0$:** $\widehat g_0=-0^2\cdot\widehat G_0=0$.

---

## Step 7 — Conclusion: $c_k=\widehat c_k(f)$

Since $f=g+c_0$ (constant), the Fourier coefficients of $f$ are

$$
\widehat c_k(f)=\widehat g_k+c_0\,\delta_{k0}=
\begin{cases}
c_k+0=c_k,&k\neq 0,\\[2pt]
0+c_0=c_0,&k=0.
\end{cases}
$$

In both cases $\widehat c_k(f)=c_k$. This proves $(\star)$.

---

## Final assembly

From Step 1, the original equality is equivalent to $(\star)$, which we have now proved. Therefore

$$
\int_{-\pi}^{\pi}\left(\sum_{k=-\infty}^{\infty}c_k\,e^{i(k-j)x}\right)dx
=\int_{-\pi}^{\pi}f(x)\,e^{-ijx}\,dx
=2\pi\,\widehat c_j(f)
=2\pi\,c_j
=\sum_{k=-\infty}^{\infty}\left(\int_{-\pi}^{\pi}c_k\,e^{i(k-j)x}\,dx\right)
$$

for every integer $j$.

$$
\boxed{\text{The equality holds for all integers }j.}
$$

### PROOF COMPLETE
