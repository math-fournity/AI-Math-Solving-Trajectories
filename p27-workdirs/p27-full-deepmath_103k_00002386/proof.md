# Proof: Characteristic function convergence does NOT imply merging for BUC functions

## Answer

$$\boxed{\text{No}}$$

The pointwise convergence $f_n(t) - g_n(t) \to 0$ for all $t$ does **not** imply that $P_n$ and $Q_n$ merge with respect to bounded uniformly continuous functions.

## Counterexample

Define:
- $P_n$ = uniform (Lebesgue) probability measure on $[0, n]$, i.e., $dP_n = \frac{1}{n}\mathbf{1}_{[0,n]}\,dx$.
- $Q_n$ = uniform probability measure on $[n, 2n]$, i.e., $dQ_n = \frac{1}{n}\mathbf{1}_{[n,2n]}\,dx$.
- Test function: $h(x) = \sin(\log(1+|x|))$.

We will show:
1. $\hat{P}_n(t) - \hat{Q}_n(t) \to 0$ for every $t \in \mathbb{R}$.
2. $h$ is bounded and uniformly continuous.
3. $\int h\,dP_n - \int h\,dQ_n \not\to 0$.

## Step 1: Characteristic functions converge pointwise

For $t \neq 0$:
$$\hat{P}_n(t) = \frac{1}{n}\int_0^n e^{itx}\,dx = \frac{e^{itn} - 1}{itn}, \qquad \hat{Q}_n(t) = \frac{1}{n}\int_n^{2n} e^{itx}\,dx = \frac{e^{i2tn} - e^{itn}}{itn} = e^{itn}\cdot\hat{P}_n(t).$$

Therefore:
$$\hat{P}_n(t) - \hat{Q}_n(t) = \hat{P}_n(t)\bigl(1 - e^{itn}\bigr).$$

Since $|\hat{P}_n(t)| = \left|\frac{\sin(tn/2)}{tn/2}\right| \leq \frac{2}{|t|\,n} \to 0$ and $|1 - e^{itn}| \leq 2$:
$$\bigl|\hat{P}_n(t) - \hat{Q}_n(t)\bigr| \leq \frac{4}{|t|\,n} \longrightarrow 0.$$

For $t = 0$: $\hat{P}_n(0) = \hat{Q}_n(0) = 1$, so the difference is $0$.

Thus $f_n(t) - g_n(t) \to 0$ for all $t \in \mathbb{R}$. $\checkmark$

## Step 2: $h$ is bounded and uniformly continuous

**Boundedness**: $|h(x)| = |\sin(\log(1+|x|))| \leq 1$ for all $x$. $\checkmark$

**Uniform continuity**: Write $h = \sin \circ\, \varphi$ where $\varphi(x) = \log(1+|x|)$. We have:
$$|\varphi(x) - \varphi(y)| = \left|\log\frac{1+|x|}{1+|y|}\right| \leq \frac{\bigl||x|-|y|\bigr|}{1+\min(|x|,|y|)} \leq |x - y|,$$
so $\varphi$ is Lipschitz with constant $1$. Since $\sin$ is also Lipschitz with constant $1$, the composition $h$ is Lipschitz with constant $1$, hence uniformly continuous. $\checkmark$

**$h$ is not almost periodic**: For $a > 0$, consider the translate $h(\cdot + a)$. At $x = 0$:
$$h(a) - h(0) = \sin(\log(1+a)) - \sin(0) = \sin(\log(1+a)).$$
Since $\sin(\log(1+a))$ does not converge as $a \to \infty$ (it oscillates), the translates $\{h(\cdot + a)\}_{a \geq 0}$ are not totally bounded in $L^\infty$. Hence $h \notin AP(\mathbb{R})$. $\checkmark$

## Step 3: The integral difference does not converge to zero

We compute:
$$D_n := \int h\,dP_n - \int h\,dQ_n = \frac{1}{n}\int_0^n \sin(\log(1+x))\,dx - \frac{1}{n}\int_n^{2n} \sin(\log(1+x))\,dx.$$

**Antiderivative.** Using the substitution $u = 1+x$ and the identity:
$$\int \sin(\log u)\,du = \frac{u}{2}\bigl(\sin(\log u) - \cos(\log u)\bigr) + C,$$
we define $F(u) = \frac{u}{2}(\sin(\log u) - \cos(\log u))$, so $F'(u) = \sin(\log u)$.

**Exact expression.** Then:
$$\frac{1}{n}\int_0^n \sin(\log(1+x))\,dx = \frac{F(n+1) - F(1)}{n} = \frac{n+1}{2n}\bigl(\sin\log(n+1) - \cos\log(n+1)\bigr) + \frac{1}{2n},$$

$$\frac{1}{n}\int_n^{2n} \sin(\log(1+x))\,dx = \frac{F(2n+1) - F(n+1)}{n} = \frac{2n+1}{2n}\bigl(\sin\log(2n+1) - \cos\log(2n+1)\bigr) - \frac{n+1}{2n}\bigl(\sin\log(n+1) - \cos\log(n+1)\bigr).$$

Adding these:
$$D_n = \frac{n+1}{n}\bigl(\sin\log(n+1) - \cos\log(n+1)\bigr) - \frac{2n+1}{2n}\bigl(\sin\log(2n+1) - \cos\log(2n+1)\bigr) + \frac{1}{2n}.$$

**Asymptotic analysis.** Since $\log(n+1) = \log n + O(1/n)$ and $\log(2n+1) = \log n + \log 2 + O(1/n)$, and $\sin, \cos$ are Lipschitz:

$$D_n = \bigl(\sin\theta_n - \cos\theta_n\bigr) - \bigl(\sin(\theta_n + c) - \cos(\theta_n + c)\bigr) + O(1/n),$$

where $\theta_n = \log n \to \infty$ and $c = \log 2 \neq 0$.

**Simplification.** Using sum-to-product formulas:
$$\sin\theta - \sin(\theta+c) = -2\sin(c/2)\cos(\theta + c/2),$$
$$\cos(\theta+c) - \cos\theta = -2\sin(c/2)\sin(\theta + c/2).$$

Therefore:
$$D_n = -2\sin(c/2)\bigl[\cos(\theta_n + c/2) + \sin(\theta_n + c/2)\bigr] + O(1/n) = -2\sqrt{2}\sin(c/2)\sin\!\left(\theta_n + \frac{c}{2} + \frac{\pi}{4}\right) + O(1/n).$$

**Non-convergence.** The leading term has amplitude:
$$A = 2\sqrt{2}\,\bigl|\sin(\log 2 / 2)\bigr| \approx 0.961 \neq 0.$$

Since $\theta_n = \log n \to \infty$, the oscillating term $\sin(\log n + \log 2/2 + \pi/4)$ does not converge. To see this explicitly, take two subsequences:

- $n_k = \left\lfloor e^{2\pi k - \log 2/2 - \pi/4}\right\rfloor$: then $\sin(\log n_k + \log 2/2 + \pi/4) \approx \sin(2\pi k) = 0$... 

Actually, more directly: choose $n_k' = \lfloor e^{\pi/2 + 2\pi k - \log 2/2 - \pi/4}\rfloor$ so that the sine term $\approx \sin(\pi/2) = 1$, giving $D_{n_k'} \approx -A$; and $n_k'' = \lfloor e^{3\pi/2 + 2\pi k - \log 2/2 - \pi/4}\rfloor$ so that the sine term $\approx \sin(3\pi/2) = -1$, giving $D_{n_k''} \approx +A$.

Since $A \neq 0$, the two subsequential limits differ, so $D_n$ does not converge. In particular, $D_n \not\to 0$. $\checkmark$

## Conclusion

We have constructed probability measures $P_n$ (uniform on $[0,n]$) and $Q_n$ (uniform on $[n,2n]$) on $\mathbb{R}$ such that:

1. $\hat{P}_n(t) - \hat{Q}_n(t) \to 0$ for every $t \in \mathbb{R}$, yet
2. For the bounded uniformly continuous function $h(x) = \sin(\log(1+|x|))$, the difference $\int h\,dP_n - \int h\,dQ_n$ oscillates with amplitude $\approx 0.96$ and does not converge to zero.

Therefore, **pointwise convergence of characteristic functions does not imply merging with respect to bounded uniformly continuous functions**.

$$\boxed{\text{No}}$$

## Intuition

The key mechanism is that both $P_n$ and $Q_n$ "escape to infinity" — their mass moves to ever-larger regions of $\mathbb{R}$. In the Bohr compactification $b\mathbb{R}$, both push forward to the Haar measure (the "uniform distribution at infinity"), so their characteristic functions agree asymptotically. However, the function $h(x) = \sin(\log(1+|x|))$ varies on the logarithmic scale: its "local frequency" at $x$ is $\sim 1/x$, which decreases as $x \to \infty$. The two measures $P_n$ and $Q_n$ sample $h$ at different logarithmic phases ($\log n$ vs.\ $\log n + \log 2$), and this phase difference is detected by $h$ but is invisible to the characters $e^{itx}$ (which are almost periodic and only see the Bohr compactification, not the finer structure of the $BUC$ compactification).
