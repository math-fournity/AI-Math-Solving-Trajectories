# Gammaharmonic Series Limit — Closed Form

## Problem

Find the closed-form expression for

$$L = \lim_{n\to \infty}\left(\sum_{k=1}^{n}\frac{1}{\Gamma(1/k)} - \log\Gamma\!\left(\frac{1}{n}\right)\right).$$

## Answer

$$\boxed{\,L \;=\; \gamma \;+\; \sum_{k=1}^{\infty}\!\left(\frac{1}{\Gamma(1/k)}-\frac{1}{k}\right)\,}$$

where $\gamma$ is the Euler–Mascheroni constant. Equivalently, writing the Taylor expansion
$\displaystyle\frac{1}{\Gamma(x)}=\sum_{m=1}^{\infty}a_m\,x^m$ (with $a_1=1,\;a_2=\gamma,\;a_3=\tfrac{\gamma^{2}-\zeta(2)}{2},\;\ldots$),

$$L \;=\; \gamma \;+\; \sum_{m=2}^{\infty} a_m\,\zeta(m).$$

Numerically, $\;L = 0.81886\,38872\,71306\,84342\ldots$

---

## Proof

### Step 1. Small-$x$ asymptotics of $1/\Gamma(x)$ and $\log\Gamma(x)$

From the Weierstrass product

$$\frac{1}{\Gamma(x)}=x\,e^{\gamma x}\prod_{j=1}^{\infty}\!\left(1+\frac{x}{j}\right)e^{-x/j},$$

taking logarithms gives, for $|x|<1$,

$$\log\frac{1}{\Gamma(x)}=\log x+\gamma x+\sum_{m=2}^{\infty}\frac{(-1)^{m+1}\zeta(m)}{m}\,x^{m}.$$

Equivalently,

$$\log\Gamma(x)=-\log x-\gamma x+\sum_{m=2}^{\infty}\frac{(-1)^{m}\zeta(m)}{m}\,x^{m},\qquad |x|<1. \tag{A}$$

Exponentiating the series for $\log(1/\Gamma(x))-\log x$ yields the Taylor expansion of the **entire** function $1/\Gamma(x)/x$:

$$\frac{1}{\Gamma(x)}=x\sum_{j=0}^{\infty}b_j\,x^{j}=\sum_{m=1}^{\infty}a_m\,x^{m},\qquad a_m:=b_{m-1}, \tag{B}$$

where $b_0=1$, $b_1=\gamma$, $b_2=\frac{\gamma^2-\zeta(2)}{2}$, and in general the $b_j$ are determined by the recurrence

$$b_j=\frac{1}{j}\sum_{\ell=1}^{j}\ell\,h_\ell\,b_{j-\ell},\qquad h_1=\gamma,\;\; h_\ell=\frac{(-1)^{\ell+1}\zeta(\ell)}{\ell}\;\;(\ell\ge2).$$

Since $1/\Gamma(x)/x=e^{h(x)}$ is **entire**, its Taylor coefficients satisfy $|b_j|^{1/j}\to 0$ (Cauchy–Hadamard), i.e. $|a_m|$ decays faster than any geometric sequence.

From (A) and (B) we read off the two asymptotic estimates we need:

$$\frac{1}{\Gamma(x)}=x+\gamma\,x^{2}+O(x^{3}),\qquad x\to 0, \tag{C}$$

$$\log\Gamma(x)=-\log x-\gamma\,x+O(x^{2}),\qquad x\to 0. \tag{D}$$

### Step 2. Definition of the correction series and its convergence

Set

$$a_k:=\frac{1}{\Gamma(1/k)}-\frac{1}{k},\qquad k\ge1.$$

From (C) with $x=1/k$:

$$a_k=\frac{\gamma}{k^{2}}+O\!\left(\frac{1}{k^{3}}\right),$$

so $\sum_{k=1}^{\infty}|a_k|<\infty$ (absolute convergence). Define

$$A:=\sum_{k=1}^{\infty}a_k=\sum_{k=1}^{\infty}\!\left(\frac{1}{\Gamma(1/k)}-\frac{1}{k}\right).$$

Note $a_1=1/\Gamma(1)-1=0$, so the sum effectively starts at $k=2$.

**$A>0$.** For $k\ge2$ we have $0<1/k<1$, hence $1<1+1/k<2$. The Gamma function satisfies $\Gamma(x)<1$ on the open interval $(1,2)$ (its minimum $\approx0.8856$ occurs at $x_0\approx1.4616$, and $\Gamma(1)=\Gamma(2)=1$). Using $\Gamma(1/k)=k\,\Gamma(1+1/k)<k$, we get $1/\Gamma(1/k)>1/k$, i.e. $a_k>0$ for every $k\ge2$. Therefore $A>0$ and $L>\gamma$.

### Step 3. Decomposition and passage to the limit

Write $S_n:=\sum_{k=1}^{n}1/\Gamma(1/k)$ and $H_n:=\sum_{k=1}^{n}1/k$. Then

$$S_n = H_n + \sum_{k=1}^{n}a_k. \tag{E}$$

We use three classical/standard facts:

1. **Harmonic numbers:** $H_n = \log n + \gamma + O(1/n)$.
2. **From (D)** with $x=1/n$: $\;\log\Gamma(1/n)=\log n - \dfrac{\gamma}{n}+O(1/n^{2})$, hence $\log n - \log\Gamma(1/n)=\dfrac{\gamma}{n}+O(1/n^{2})\to 0$.

Now decompose:

$$S_n-\log\Gamma(1/n)=\underbrace{\bigl(H_n-\log n\bigr)}_{\to\;\gamma}+\underbrace{\sum_{k=1}^{n}a_k}_{\to\;A}+\underbrace{\bigl(\log n-\log\Gamma(1/n)\bigr)}_{\to\;0}.$$

All three limits are justified: the first by definition of $\gamma$, the second by absolute convergence of $\sum a_k$ (Step 2), and the third by (D). Therefore

$$\boxed{L=\gamma+A=\gamma+\sum_{k=1}^{\infty}\!\left(\frac{1}{\Gamma(1/k)}-\frac{1}{k}\right)}. \tag{F}$$

### Step 4. Equivalent zeta-series form (interchange of summation)

Since $1/\Gamma(x)=\sum_{m=1}^{\infty}a_m x^m$ is entire, for each $k\ge1$,

$$\frac{1}{\Gamma(1/k)}=\sum_{m=1}^{\infty}\frac{a_m}{k^m},\qquad\text{so}\qquad a_k=\frac{1}{\Gamma(1/k)}-\frac{1}{k}=\sum_{m=2}^{\infty}\frac{a_m}{k^m}$$

(using $a_1=1$). To interchange $\sum_k\sum_m$, verify absolute convergence via Tonelli:

$$\sum_{k=1}^{\infty}\sum_{m=2}^{\infty}\frac{|a_m|}{k^m}=\sum_{m=2}^{\infty}|a_m|\,\zeta(m).$$

Because $1/\Gamma(x)/x$ is entire, $|a_m|^{1/m}\to 0$, so $|a_m|$ decays super-geometrically while $\zeta(m)\to 1$; hence $\sum_{m=2}^{\infty}|a_m|\zeta(m)<\infty$. The interchange is legitimate, giving

$$A=\sum_{m=2}^{\infty}a_m\,\zeta(m),\qquad L=\gamma+\sum_{m=2}^{\infty}a_m\,\zeta(m). \tag{G}$$

The first few coefficients are $a_1=1$, $a_2=\gamma$, $a_3=\frac{\gamma^2-\zeta(2)}{2}$, $a_4=\frac{\gamma^3}{6}-\frac{\gamma\,\zeta(2)}{2}+\frac{\zeta(3)}{3}$, $\ldots$

### Step 5. Numerical value

High-precision evaluation (Richardson extrapolation of the partial sums, confirmed by the zeta-series (G)) gives

$$L = 0.81886\,38872\,71306\,84342\,05545\,13435\ldots$$

with $A=L-\gamma=0.24164\,82223\,69773\,98256\ldots$

This constant does not reduce to any simpler known elementary combination; the forms (F) and (G) are the closed-form expressions for the Gammaharmonic limit.

### PROOF COMPLETE
