# Proof: $\lim_{t\to+\infty}\int_0^{+\infty}\frac{dx}{e^x+\sin(tx)}=\frac{\pi}{2}$

## Step 1. Well-definedness

For $x>0$: $e^x\ge 1$ and $\sin(tx)\ge -1$, so $e^x+\sin(tx)\ge e^x-1>0$. Near $x=0$: $e^x+\sin(tx)\approx 1+(1+t)x$, so the integrand $\sim 1/(1+(1+t)x)$ is integrable. For large $x$: $e^x+\sin(tx)\ge e^x-1\ge \frac{1}{2}e^x$ (for $x$ large), so the integrand $\le 2e^{-x}$, integrable. Hence the integral is finite for every $t>0$.

## Step 2. Fourier expansion of $\frac{1}{a+\sin\theta}$

**Claim.** For $a>1$, with $\alpha:=a+\sqrt{a^2-1}>1$,

$$\frac{1}{a+\sin\theta}=\frac{1}{\sqrt{a^2-1}}\left(1+2\sum_{n=1}^{\infty}\frac{\cos\!\bigl(n(\theta+\pi/2)\bigr)}{\alpha^n}\right), \qquad \theta\in\mathbb{R}.$$

*Proof.* The constant term is the classical integral

$$\frac{1}{2\pi}\int_0^{2\pi}\frac{d\theta}{a+\sin\theta}=\frac{1}{2\pi}\int_0^{2\pi}\frac{d\phi}{a+\cos\phi}=\frac{1}{\sqrt{a^2-1}},$$

where we set $\phi=\theta-\pi/2$ and used the standard result $\int_0^{2\pi}\frac{d\phi}{a+\cos\phi}=\frac{2\pi}{\sqrt{a^2-1}}$ for $a>1$.

For the $n$-th Fourier coefficient ($n\ge 1$), set $z=e^{i\theta}$, $\sin\theta=(z-z^{-1})/(2i)$:

$$c_n=\frac{1}{2\pi}\int_0^{2\pi}\frac{e^{-in\theta}\,d\theta}{a+\sin\theta}=\frac{1}{2\pi i}\oint_{|z|=1}\frac{2iz^{-n}\,dz}{z^2+2iaz-1}.$$

The denominator factors as $(z-z_1)(z-z_2)$ with $z_1=i(-a+\sqrt{a^2-1})$ (inside $|z|=1$) and $z_2=i(-a-\sqrt{a^2-1})=-i\alpha$ (outside). For $n\ge 1$, $z^{-n}$ has an $n$-th order pole at $z=0$. Computing residues at $z_1$ and $z=0$ (they combine to give the exterior pole contribution), one obtains

$$c_n=\frac{z_2^{-n}}{\sqrt{a^2-1}}=\frac{i^n}{\alpha^n\sqrt{a^2-1}}.$$

By reality, $c_{-n}=\overline{c_n}$, so the $n$-th harmonic is $c_ne^{in\theta}+\overline{c_n}e^{-in\theta}=\frac{2\cos(n\theta+n\pi/2)}{\alpha^n\sqrt{a^2-1}}=\frac{2\cos(n(\theta+\pi/2))}{\alpha^n\sqrt{a^2-1}}$. $\square$

## Step 3. Exchange on $[\delta,\infty)$: Riemann–Lebesgue

Set $a=e^x>1$ (for $x>0$), $\theta=tx$, and $\alpha(x)=e^x+\sqrt{e^{2x}-1}$. Then

$$\frac{1}{e^x+\sin(tx)}=\frac{1}{\sqrt{e^{2x}-1}}+\frac{2}{\sqrt{e^{2x}-1}}\sum_{n=1}^{\infty}\frac{\cos\!\bigl(n(tx+\pi/2)\bigr)}{\alpha(x)^n}. \tag{$\star$}$$

On $[\delta,\infty)$ with $\delta>0$: $\alpha(x)\ge\alpha_\delta:=e^\delta+\sqrt{e^{2\delta}-1}>1$, so the series converges absolutely and uniformly (in $x$ and $t$). Integrating term-by-term:

$$\int_\delta^\infty\frac{dx}{e^x+\sin(tx)}=\int_\delta^\infty\frac{dx}{\sqrt{e^{2x}-1}}+\sum_{n=1}^{\infty}\underbrace{\int_\delta^\infty\frac{2\cos(n(tx+\pi/2))}{\alpha(x)^n\sqrt{e^{2x}-1}}\,dx}_{=:A_n(t)}.$$

**Each $A_n(t)\to 0$ as $t\to\infty$** by the Riemann–Lebesgue lemma, since the amplitude $\frac{2}{\alpha(x)^n\sqrt{e^{2x}-1}}\in L^1[\delta,\infty)$ (bounded by $\frac{2\alpha_\delta^{-n}}{\sqrt{e^{2\delta}-1}}\cdot\int_\delta^\infty\frac{dx}{\sqrt{e^{2x}-1}}<\infty$).

**Exchange of $\lim_{t\to\infty}$ and $\sum_n$:** We have $|A_n(t)|\le M\alpha_\delta^{-n}$ where $M:=2\int_\delta^\infty\frac{dx}{\sqrt{e^{2x}-1}}<\infty$. Since $\sum_n M\alpha_\delta^{-n}<\infty$ (geometric, ratio $\alpha_\delta^{-1}<1$), the dominated convergence theorem (for counting measure) gives $\sum_{n=1}^\infty A_n(t)\to 0$. Therefore

$$\lim_{t\to\infty}\int_\delta^\infty\frac{dx}{e^x+\sin(tx)}=\int_\delta^\infty\frac{dx}{\sqrt{e^{2x}-1}}. \tag{1}$$

## Step 4. Uniform bound on $[0,\delta]$

**Lemma.** There exists $C>0$ such that for all $t\ge 1$ and $\delta\in(0,1]$,

$$\int_0^\delta\frac{dx}{e^x+\sin(tx)}\le C\,\delta^{1/3}.$$

*Proof.* Since $e^x\ge 1+x$, we have $e^x+\sin(tx)\ge (1+\sin(tx))+x$. Substituting $u=tx$:

$$\int_0^\delta\frac{dx}{e^x+\sin(tx)}\le\frac{1}{t}\int_0^{t\delta}\frac{du}{(1+\sin u)+u/t}. \tag{2}$$

**Quadratic lower bound on $1+\sin u$.** Since $1+\sin u=2\sin^2\!\bigl(\tfrac{u}{2}+\tfrac{\pi}{4}\bigr)$ and the zeros of $1+\sin u$ are $u_k=\tfrac{3\pi}{2}+2k\pi$ ($k\in\mathbb{Z}$), using $|\sin x|\ge\frac{2|x|}{\pi}$ for $|x|\le\frac{\pi}{2}$ and $d(u):=\min_k|u-u_k|\le\pi$:

$$1+\sin u\ge\frac{2}{\pi^2}\,d(u)^2\qquad\forall\,u\in\mathbb{R}. \tag{3}$$

**Weighted AM–GM.** For $a,b>0$ and $\alpha\in[0,1]$: $a^\alpha b^{1-\alpha}\le\alpha a+(1-\alpha)b\le a+b$, hence

$$\frac{1}{a+b}\le\frac{1}{a^\alpha\,b^{1-\alpha}}. \tag{4}$$

Apply (4) with $a=1+\sin u$, $b=u/t$, $\alpha=\tfrac{1}{3}$ (so $2\alpha=\tfrac{2}{3}<1$, ensuring integrability near zeros):

$$\frac{1}{(1+\sin u)+u/t}\le\frac{t^{2/3}}{(1+\sin u)^{1/3}\,u^{2/3}}\le\frac{C\,t^{2/3}}{d(u)^{2/3}\,u^{2/3}},$$

using (3): $(1+\sin u)^{1/3}\ge c\,d(u)^{2/3}$. Substituting into (2):

$$\int_0^\delta\frac{dx}{e^x+\sin(tx)}\le\frac{C}{t^{1/3}}\int_0^{t\delta}\frac{du}{d(u)^{2/3}\,u^{2/3}}. \tag{5}$$

**Bounding the integral in (5).** Split $[0,t\delta]$ into the intervals $J_k:=[u_k-\pi,\,u_k+\pi]$ (which tile $\mathbb{R}$ up to endpoints, since $u_{k+1}-u_k=2\pi$) and intersect with $[0,t\delta]$.

*Case $k\ge 1$ ($u_k\ge\frac{7\pi}{2}$, so $u\ge\frac{5\pi}{2}$ on $J_k$):* On $J_k$, $d(u)=|u-u_k|$ and $u\ge u_k-\pi$, so

$$\int_{J_k}\frac{du}{d(u)^{2/3}\,u^{2/3}}\le\frac{1}{(u_k-\pi)^{2/3}}\int_{-\pi}^{\pi}\frac{dv}{|v|^{2/3}}=\frac{C_1}{(u_k-\pi)^{2/3}}\le\frac{C_2}{k^{2/3}}.$$

Summing over $k=1,\ldots,K$ where $K\le\frac{t\delta}{2\pi}+1$:

$$\sum_{k=1}^{K}\le C_2\sum_{k=1}^{K}\frac{1}{k^{2/3}}\le C_3\,K^{1/3}\le C_4\,(t\delta)^{1/3}.$$

*Case $k=0$ ($u_0=\frac{3\pi}{2}$):* On $J_0\cap[0,t\delta]\subseteq[0,\frac{5\pi}{2}]$, both $u^{-2/3}$ (near $u=0$) and $d(u)^{-2/3}=|u-\frac{3\pi}{2}|^{-2/3}$ (near $u=\frac{3\pi}{2}$) are integrable (exponent $\frac{2}{3}<1$), so

$$\int_{J_0\cap[0,t\delta]}\frac{du}{d(u)^{2/3}\,u^{2/3}}\le C_5.$$

*Region $[0,\pi/2]$ (before $J_0$ starts at $\pi/2$):* Here $\sin u\ge 0$ so $d(u)=\frac{3\pi}{2}-u\ge\pi$, giving $d(u)^{-2/3}\le\pi^{-2/3}$ and $\int_0^{\min(\pi/2,\,t\delta)}u^{-2/3}\,du\le C_6$. So this part is $\le C_7$.

**Combining.** The integral in (5) is $\le C_4(t\delta)^{1/3}+C_8$, so

$$\int_0^\delta\frac{dx}{e^x+\sin(tx)}\le C\,\delta^{1/3}+\frac{C_8}{t^{1/3}}. \tag{6}$$

When $t\delta\ge\frac{\pi}{2}$ (so $J_0$ is relevant), $t\ge\frac{\pi}{2\delta}$, hence $t^{-1/3}\le\bigl(\frac{2\delta}{\pi}\bigr)^{1/3}=O(\delta^{1/3})$. When $t\delta<\frac{\pi}{2}$, the entire interval $[0,t\delta]$ has $\sin u\ge 0$, so $1+\sin u\ge 1$ and the original integral is $\le\frac{1}{t}\cdot t\delta=\delta\le\delta^{1/3}$. In either case, (6) gives $\le C\,\delta^{1/3}$. $\square$

## Step 5. Squeeze argument

For any $\delta>0$, split $I(t):=\int_0^\infty\frac{dx}{e^x+\sin(tx)}=\int_0^\delta+\int_\delta^\infty$.

**Upper bound.** By the Lemma and (1):

$$\limsup_{t\to\infty}I(t)\le C\delta^{1/3}+\int_\delta^\infty\frac{dx}{\sqrt{e^{2x}-1}}.$$

**Lower bound.** The integrand is non-negative, so $\int_0^\delta\ge 0$. By (1):

$$\liminf_{t\to\infty}I(t)\ge\int_\delta^\infty\frac{dx}{\sqrt{e^{2x}-1}}.$$

Writing $\int_\delta^\infty=\int_0^\infty-\int_0^\delta$ and noting $\int_0^\delta\frac{dx}{\sqrt{e^{2x}-1}}\le\int_0^\delta\frac{dx}{\sqrt{2x}}=\sqrt{2\delta}\to 0$:

$$\frac{\pi}{2}-\sqrt{2\delta}\le\liminf_{t\to\infty}I(t)\le\limsup_{t\to\infty}I(t)\le\frac{\pi}{2}+C\delta^{1/3}.$$

Letting $\delta\to 0^+$: $\lim_{t\to\infty}I(t)=\int_0^\infty\frac{dx}{\sqrt{e^{2x}-1}}$.

## Step 6. Evaluation of $\int_0^\infty\frac{dx}{\sqrt{e^{2x}-1}}$

Substitute $u=e^x$, $dx=du/u$:

$$\int_1^\infty\frac{du}{u\sqrt{u^2-1}}.$$

Substitute $u=\sec\theta$, $du=\sec\theta\tan\theta\,d\theta$, $\sqrt{u^2-1}=\tan\theta$:

$$\int_0^{\pi/2}\frac{\sec\theta\tan\theta\,d\theta}{\sec\theta\cdot\tan\theta}=\int_0^{\pi/2}d\theta=\frac{\pi}{2}.$$

## Conclusion

$$\boxed{\lim_{t\to+\infty}\int_0^{+\infty}\frac{dx}{e^x+\sin(tx)}=\frac{\pi}{2}}.$$

### PROOF COMPLETE
