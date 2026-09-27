Let me start by reading the analysis notes file to understand the problem and current state.Let me understand the task:

**Problem**: Let $B$ be a fractional Brownian motion with Hurst parameter $H \in (0,1)$, and $Z = \int_0^1 B_s^4 \, ds$. Does $Z$ have a density with respect to Lebesgue measure?

**Answer**: Yes — for every $H \in (0,1)$, the density exists.

**Route**: Malliavin derivative non-degenerate + Bouleau–Hirsch criterion.

The proof chain:
1. **Malliavin smoothness**: $Z \in \mathbb{D}^{1,p}$ for all $p < \infty$. Moment estimates: $\|DZ\| \le 4\int_0^1 |B_t|^3 t^H dt$... wait, actually let me think. The derivative is $D_s Z = 4\int_0^1 B_t^3 \tilde{1}_{[0,s]}(t) dt$ where $\tilde 1_{[0,t]}(s) = 1_{s \le t}$. So as an element of $\mathcal{H}_H$: $DZ = 4m$ where $m = \int_0^1 B_t^3 \tilde 1_{[0,t]} dt$.

Wait, actually the norm bound: $\|DZ\|_{\mathcal H} \le 4\int_0^1 |B_t|^3 \|\tilde 1_{[0,t]}\|_{\mathcal H} dt$ by triangle inequality, and $\|\tilde 1_{[0,t]}\|_{\mathcal H}^2 = t^{2H}$, so $\|DZ\| \le 4\int_0^1 |B_t|^3 t^H dt$. Then $\mathbb E|B_t|^k \le C_k t^{kH}$. Good, this gives $Z \in \mathbb D^{1,p}$ for all $p$.

2. **Derivative explicit formula**: $D_s Z = 4 \int_0^1 B_t^3 \tilde 1_{[0,s]}(t) dt$, i.e., $D_s B_t = \tilde 1_{[0,t]}(s) = 1_{s \le t}$. For BM case: $D_s Z = 4\int_s^1 B_t^3 dt$ which matches classical.

So $\|DZ\|_{\mathcal H}^2 = 16 Q(B^3)$ where $Q(g) := \langle m_g, m_g\rangle = \iint g(s) g(t) R_H(s,t) ds dt$ with $m = \int_0^1 g(t) \tilde 1_{[0,t]} dt$, and $R_H(s,t) = \langle \tilde 1_{[0,s]}, \tilde 1_{[0,t]}\rangle_{\mathcal H} = \frac12(|s|^{2H} + |t|^{2H} - |s-t|^{2H})$.

Hmm wait: $\langle \tilde 1_{[0,s]}, \tilde 1_{[0,t]}\rangle_{\mathcal H_H} = \int_0^1 \tilde 1_{[0,s]}(u)\tilde 1_{[0,t]}(u) du + ...$ Actually the Cameron-Martin space of fBm is $\mathcal H_H = \{h: h' \text{ exists a.e.}, h' \in L^2 \text{ weighted}\}$... Let me recall the standard setup.

For fBm with Hurst parameter $H$, there are two common frameworks:

(a) **Abstract Wiener space setting**: The Hilbert space $\mathcal H$ is the closure of the linear span of $\{\delta x : x \in [0,T]\}$ under the inner product induced by covariance: $\langle \delta_x, \delta_y \rangle_{\mathcal H} = R_H(x,y)$ where $R_H(x,y) = \frac{1}{2}(x^{2H} + y^{2H} - |x-y|^{2H})$. Then $\mathbb D^{1,2}(\mathcal H)$ etc.

In this setting, for $F = \int_0^T u_t dB_t$ (Wiener integral), $D F = u$ viewed in $\mathcal L^2([0,T]; \mathcal H)$. And $\|D F\|^2_{\mathcal L^2([0,T],\mathcal H)} = \iint u_s u_t R_H(s,t) dsdt$.

(b) There's also a formulation via an isonormal process on $\mathcal H$ itself.

The notes use the convention: $D_s B_t = \tilde 1_{[0,t]}(s) = 1_{s\le t}$. Hmm wait, actually let me recheck. In Nualart's book (fBm chapter, or general), if $B_t = W(\delta_t)$ hmm...

Actually in Nualart's book framework: Let $\mathcal H$ be the Hilbert space from the covariance kernel. $B_t = \langle \cdot, 1_{[0,t]}\rangle_{\mathcal H}$ where $1_{[0,t]}$ is viewed as element of $\mathcal H$. Then $D_s B_t = 1_{[0,t]}(s) = 1_{s \le t}$ (as element of $\mathcal H$ indexed by $s$). 

Then $D_s Z = \int_0^1 4B_t^3 D_s B_t dt = 4\int_0^1 B_t^3 1_{[0,t]}(s) dt = 4\int_s^1 B_t^3 dt$ (pointwise in $s$).

And $\|DZ\|^2_\mathcal H = \langle DZ, DZ\rangle_\mathcal H = 16 \iint_{[0,1]^2} \left(\int_s^1...\right)$... hmm wait no. $D Z \in L^2(\Omega \times [0,1])$-valued in $\mathcal H$? Let me redo: $DZ = \{(D_s Z)\}_{s\in[0,1]}$, and its $\mathcal H$-norm squared is

$\|DZ\|^2_{\mathcal H} = \iint (D_s Z)(D_t Z) R_H(ds, dt)$? No...

OK here's the cleanest way: $DZ \in L^2(\Omega; \mathcal H)$ where $\mathcal H$ here means the Hilbert space over which the Gaussian field lives. In Nualart's notation for fBm: $\mathfrak H = L^2([0,T])$ hmm, there are two conventions again.

Convention in Nualart's book Chapter 5 (fBm): The isonormal Gaussian process $W = \{W(h): h \in \mathcal H\}$ where $\mathcal H = L^2([0,T])$ hmm no. Let me recall precisely.

Nualart 2006, Chapter 5: "the process $B = \{B_t, t\ge0\}$ can be expressed as $B_t = W(1_{[0,t]})$" hmm, where $W$ is an isonormal process over $\mathcal H$ and $\mathcal H$ is the completion of the set of step functions with inner product $\langle 1_{[0,s]}, 1_{[0,t]}\rangle_{\mathcal H} = R_H(s,t)$. Yes that's convention (a).

Then for $F \in \mathbb D^{1,2}$, $DF \in L^2(\Omega;\mathcal H)$, i.e., $DF = \{D_\rho F: \rho \ge 0\}$ where each $D_\rho F \in \mathcal H$. And $\|DF\|^2_\mathcal H = \|DF\|^2_{L^2(\Omega;\mathcal H)}$ pointwise in $\omega$.

Chain rule: $D_s Z = \int_0^1 4 B_t^3 D_s B_t \, dt$ where now $D_s B_t = 1_{[0,t]}(s) \in \mathcal H$ (as a function of the first variable... wait I need to be careful about which slot indexes what).

Standard: $D_s B_t$ means $(D B_t)_s$, the derivative of the random variable $B_t$ evaluated at parameter $s$. Since $B_t = W(1_{[0,t]})$, we get $D_s B_t = 1_{[0,t]}(s)$ — as an element of $\mathcal H$ in the $s$-slot it's the function $s \mapsto 1_{s\le t}$, i.e., $\tilde 1_{[0,t]}$ in the notes' notation (tilde to emphasize it's the $\mathcal H$-element, not a scalar function... well it IS a function but lives in $\mathcal H$).

So $D_s Z = 4\int_0^1 B_t^3 \cdot 1_{s \le t}\, dt$ — for fixed $\omega$ and fixed $s$, this is a number: $4\int_s^1 B_t^3(\omega) dt$. And as a function of $s$, $D Z = (s \mapsto 4\int_s^1 B_t^3 dt)$. Hmm wait, but then the notes say "$D_s Z = 4\int_0^1 B_t^3 \tilde 1_{[0,s]}(t) dt$". Note $\tilde 1_{[0,s]}(t) = 1_{t \le s}$?? That would give $D_s Z = 4\int_0^s B_t^3 dt$, contradicting BM check $D_s Z = 4\int_s^1 B_t^3 dt$.

Hold on. The notes say at line 26: "导数显式式：$D_sZ=4\int_0^1 B_t^3\,\tilde1_{[0,s]}(t)\,dt$，即作为 $\mathcal H_H$ 元素 $DZ=4m$，其中 $m=\int_0^1 B_t^3\,\tilde1_{[0,t]}\,dt$（Bochner 积分）。"

Hmm, so they define $D_s Z = 4 \int_0^1 B_t^3 \tilde 1_{[0,s]}(t) dt$. If $\tilde 1_{[0,s]}(t) = 1_{t \le s}$ then $D_s Z = 4\int_0^s B_t^3 dt$. But then the BM check says "BM 情形 $D_sZ=4\int_s^1B_t^3dt$". These are inconsistent unless... hmm.

Wait, maybe there's a subtlety: perhaps in their convention $D_s B_t = \tilde 1_{[0,t]}(s) = 1_{s\le t}$, so $D_s Z = 4\int_0^1 B_t^3 1_{s\le t} dt = 4\int_s^1 B_t^3 dt$. And separately, as an element of $\mathcal H$, $DZ = 4\int_0^1 B_t^3 \tilde 1_{[0,t]} dt$ (Bochner integral over $t$ of $\mathcal H$-elements $\tilde 1_{[0,t]}$).

Then evaluating this $\mathcal H$-element at $s$: $\left(\int_0^1 B_t^3 \tilde 1_{[0,t]} dt\right)(s) = \int_0^1 B_t^3 1_{s\le t} dt = \int_s^1 B_t^3 dt$. Consistent! So the first displayed formula in line 26 has a typo (should be $\tilde 1_{[0,t]}(s)$ not $\tilde 1_{[0,s]}(t)$), OR their convention is $\tilde 1_{[0,s]}(t) = 1_{s \le t}$?? That seems weird notation-wise. Anyway, the note itself says "约定复核已做（@41856）：正确方向是 $D_sB_t=\tilde1_{[0,t]}(s)$ 即 $D_sB_t=1_{s\le t}$，BM 情形 $D_sZ=4\int_s^1B_t^3dt$ 与经典一致。轮次3 中途一度搞反后自行纠正，最终链条验证自洽。"

So the final convention: $D_s B_t = 1_{\{s \le t\}}$, hence
$$D_s Z = 4\int_s^1 B_t^3\,dt.$$

And as an $\mathcal H$-valued random variable,
$$DZ = 4\int_0^1 B_t^3\,\tilde 1_{[0,t]}\,dt =: 4m,$$
where $m(\cdot) = \int_0^1 B_t^3 \tilde 1_{[0,t]}(\cdot)\,dt$, i.e., $m(s) = \int_s^1 B_t^3\,dt$.

Then
$$\|DZ\|^2_{\mathcal H} = 16\langle m, m\rangle_{\mathcal H} = 16 \iint_{[0,1]^2} B_s^3 B_t^3 R_H(s,t)\,ds\,dt = 16\,Q(B^3),$$
where $R_H(s,t) = \langle \tilde 1_{[0,s]}, \tilde 1_{[0,t]}\rangle_{\mathcal H} = \tfrac12(s^{2H} + t^{2H} - |s-t|^{2H})$.

Good. Now the event $E = \{\|DZ\|_{\mathcal H} = 0\}$. On $E$, $m = 0$ in $\mathcal H$. Since $\tilde 1_{[0,t]}$ is a continuous curve in $\mathcal H$ ($\|\tilde 1_{[0,t]} - \tilde 1_{[0,t']}\|^2 = |t - t'|^{2H}$), the Bochner integral commutes with continuous linear functionals: for all $t$, 
$$U(t) := \langle m, \tilde 1_{[0,t]}\rangle_{\mathcal H} = 0.$$
Now compute $U(t)$ explicitly: 
$$U(t) = \int_0^1 B_u^3 R_H(u, t)\,du.$$
Indeed $\langle m, \tilde 1_{[0,t]}\rangle = \int_0^1 B_u^3 \langle \tilde 1_{[0,u]}, \tilde 1_{[0,t]}\rangle du = \int_0^1 B_u^3 R_H(u,t) du$.

On $E$: $g(t) := B_t^3(\omega)$ (continuous function of $t$ for fixed $\omega$) satisfies
$$U_g(t) := \int_0^1 g(u) R_H(u,t)\,du \equiv 0 \quad \forall t \in [0,1].$$

Now expand $R_H(u,t) = \frac12(u^{2H} + t^{2H} - |u-t|^{2H})$:
$$U_g(t) = \frac12\left[\int g(u)u^{2H}du + t^{2H}\int g(u)du - \int g(u)|u-t|^{2H}du\right] \equiv 0.$$

Define $A = \int_0^1 g$, $C = \int_0^1 t^{2H} g(t) dt$, and $\mathcal V(t) = \int_0^1 |t-u|^{2H} g(u) du$. Then the equation says:
$$\mathcal V(t) = C + A t^{2H} \quad \forall t\in[0,1].$$

(The notes write $As^{2H} + D$ with $D = C - 2c$; slight difference because maybe they had $U_g \equiv c$ rather than $\equiv 0$. Fine.)

Lemma A: If $g \in C([0,1])$ and $\mathcal V(t) = \int_0^1 |t-u|^{2H} g(u)du$ coincides with $A t^{2H} + C$ on $[0,1]$ (polynomial of degree ≤ 2 in... well, $At^{2H} + C$, non-smooth at 0 unless $A=0$), then $g \equiv 0$.

Three-step proof:
- Step 1: $A = 0$. Via differentiating twice repeatedly ("阶梯求导" ladder differentiation).
- Step 2: Energy identity pure algebra: multiply potential equation by $g$ and integrate:
$$\mathcal E_{2H}(g) := \iint g(s)g(t)|s-t|^{2H}\,ds\,dt = A(C+D)$$ hmm with their constants. With my normalization $\mathcal V(t) = At^{2H} + C$: multiply by $g(t)$ integrate: $\iint g(t)g(u)|t-u|^{2H}dudt = A\int t^{2H}g(t)dt + C\int g = AC + CA = 2AC$. Wait: $\int \mathcal V(t) g(t) dt = \iint g(u)g(t)|t-u|^{2H} dudt = A C + C A = 2AC$. So $\mathcal E = 2AC$. With $A = 0$: $\mathcal E = 0$.
- Step 3: For zero-mean $g$, $\mathcal E_{2H}(g) = c_H \int |\hat g(\xi)|^2 |\xi|^{-1-2H} d\xi \ge 0$ with equality iff $\hat g \equiv 0$ iff $g \equiv 0$. Since $A = 0$, $\hat g(0) = 0$ and the representation holds (no atom issue at 0 since $A^2 = 0$ kills the singular term).

Actually more carefully: $|x|^\alpha$ with $\alpha = 2H \in (0,2)$ has Fourier transform (as tempered distribution) $-\frac{2\Gamma(\alpha+1)\sin(\pi\alpha/2)}{|\xi|^{1+\alpha}} \cdot$(const)... Let me recall exactly. For $0 < \alpha < 2$:
$$\mathcal F[|x|^{-\alpha}](\xi) = c(\alpha)|\xi|^{\alpha-1},$$
or dually $|x|^{\alpha} = c'_\alpha \int (1-\cos(\xi x))|\xi|^{-1-\alpha} d\xi$ hmm. The standard identity: for $0<\alpha<2$,
$$|x|^\alpha = C_\alpha \, \mathrm{PV}\!\int_{\mathbb R} \frac{e^{i\xi x}-1}{|\xi|^{1+\alpha}}\,d\xi$$ 
with $C_\alpha > 0$. Equivalently $|x|^\alpha = \frac{C_\alpha}{2}\int (2 - e^{i\xi x} - e^{-i\xi x})|\xi|^{-1-\alpha}d\xi = C_\alpha\int(1-\cos(\xi x))|\xi|^{-1-\alpha}d\xi$.

With $g$ compactly supported (support in [0,1]), $\hat g$ entire. Then
$$\mathcal E_\alpha(g) = C_\alpha\int (1-\cos(\xi\cdot))|\xi|^{-1-\alpha} \widehat{g\ast\tilde g}... $$

More concretely: $\mathcal E_\alpha(g)=\iint g(s)g(t)|s-t|^\alpha dsdt$. Using $|s-t|^\alpha = C_\alpha\int (1-\cos(\xi(s-t)))|\xi|^{-1-\alpha}d\xi$:
$$\mathcal E = C_\alpha\int |\xi|^{-1-\alpha}\left[A^2 - |\hat g(\xi)|^2\right]d\xi$$
where $\hat g(\xi) = \int g(t)e^{i\xi t}dt$ (real part matters since cos; and $|\hat g(\xi)|^2 = \hat g(\xi)\overline{\hat g(\xi)}$, with $g$ real, $\Re$ stuff — anyway standard). When $A = 0$, the integrand near $\xi=0$: $|\hat g(\xi)|^2 = O(\xi^2) \cdot (\int |tg|)^2$-ish, so $\xi^{-1-\alpha}|\hat g(\xi)|^2 \sim |\xi|^{1-\alpha}$ integrable near 0 since $1 - \alpha > -1$ iff $\alpha < 2$. Good. At infinity, $\hat g$ bounded, $|\xi|^{-1-\alpha}$ integrable since $\alpha > 0$. So the integral converges absolutely when $A=0$, and equals $\mathcal E$ by Fubini (need care: the double integral isn't absolutely convergent before subtracting; standard trick: truncate $|\xi|\le M$, use dominated convergence / monotone convergence with $A^2 - |\hat g(\xi)|^2 \geq 0$... hmm, actually $A^2 - |\hat g(\xi)|^2 \ge 0$ always? By triangle inequality yes! $|\hat g(\xi)| \le \|g\|_1 = A$ if $g\ge0$... no wait $A = \int g$ could be negative. Hmm, $|\hat g(\xi)| = |\int g e^{i\xi t}| \le \int |g|$, and $A^2 = (\int g)^2 \le (\int|g|)^2$. So $A^2 - |\hat g|^2$ is NOT automatically nonnegative. OK so Fubini needs justification differently — do it for smooth approximations or use the distributional Fourier transform directly. Alternatively justify via truncation and limit using the fact that everything is finite and the integrand is dominated appropriately after subtracting. This is a standard computation; I'll handle it carefully in the proof, e.g., by writing $\mathcal E = C_\alpha\lim_{M\to\infty}\int_{|\xi|\le M}...$ justified by Fubini–Tonelli on the truncated kernel $K_M(x) = |x|^\alpha \wedge$ something... Actually simplest rigorous route: approximate $g$ by $C_c^\infty$ functions, or directly note that for the truncated integral Fubini applies since $\int_{|\xi|\le M}(1-\cos(\xi(s-t)))|\xi|^{-1-\alpha}d\xi$ is bounded uniformly in $(s,t)$ (it grows like $|s-t|$ hmm, $\int_{|\xi|\le M}(1-\cos(\xi x))|\xi|^{-1-\alpha}d\xi = |x|^\alpha \int_{|y|\le M|x|}(1-\cos y)|y|^{-1-\alpha}dy \le C|x|^\alpha (M|x|)^{... }$ hmm for small $|x|$, $\le C'|x|^2 M^{1-\alpha}$; for large $|x|$, bounded by const). On compact support both fine, so truncated Fubini is fine, then take $M\to\infty$ with the RHS converging by dominated conv given $A = 0$ and the LHS being constant. Good.

Then $\mathcal E = 0$ forces $\hat g(\xi) = 0$ for a.e. $\xi$; $\hat g$ is entire (continuous + compact support), so $\hat g \equiv 0$, so $g \equiv 0$. Hence $B_t^3(\omega) \equiv 0$ on $E$, i.e., $B_t(\omega)\equiv 0$, so $E \subseteq \{B \equiv 0\} \subseteq \{B_1 = 0\}$, and $P(B_1 = 0) = 0$ since $B_1 \sim N(0, 1)$ (for fBm, $B_1 \sim N(0,1)$ regardless of $H$). Therefore $P(E) = 0$.

By Bouleau–Hirsch criterion (Nualart, Thm 2.1.3 in 2nd ed): if $F \in \mathbb D^{1,2}$ and $P(\|DF\|_{\mathcal H} > 0) = 1$, then the law of $F$ is absolutely continuous w.r.t. Lebesgue measure. Done.

Now Step 1 details (ladder differentiation): We have $\mathcal V(t) = At^{2H} + C$ for $t \in [0,1]$ where $\mathcal V(t) = \int_0^1 |t-u|^{2H}g(u)du$. Write $\beta = 2H \in (0,2)$.

Key mechanism: differentiate twice; each differentiation lowers the exponent of the kernel singularity by 2 but the new kernel remains integrable as long as exponent $> -1$... wait: differentiating $|t-u|^\beta$ twice in $t$ gives $\beta(\beta-1)|t-u|^{\beta-2}$, which is integrable in $u$ iff $\beta - 2 > -1$, i.e., $\beta > 1$. Each round lowers $\beta$ by 2. So:

Round structure: start with $\beta_0 = 2H$. While $\beta_k > 2$... hmm wait $\beta_0 < 2$ already. Hmm, so actually we differentiate at most... let me think again.

$\beta \in (0, 2)$. First derivative: $\partial_t |t-u|^\beta = \beta\,\mathrm{sgn}(t-u)|t-u|^{\beta-1}$, defined classically away from $t=u$; the function $t\mapsto \mathcal V(t)$ is $C^1$? For $\beta > 1$: yes, $\mathcal V \in C^1$ with $\mathcal V'(t) = \beta\int \mathrm{sgn}(t-u)|t-u|^{\beta-1}g(u)du$. For $\beta \le 1$: $\mathcal V$ needn't be $C^1$... but the RHS $A\beta t^{\beta-1}$ blows up at $t\to 0^+$ if $A \neq 0$ and $\beta < 1$. That's the "blow-up" argument.

The notes describe: "每微分两次指数降 2（新核仍可积当指数 >1），落到 $(-1,1]$ 后按正负分支处理：负指数直接 $s\to0^+$ 右端爆破而左端有限；$(0,1]$ 先再微分一次化为单侧负指数方程再爆破。"

Translation: Differentiate twice per round, exponent drops by 2 (new kernel still integrable when exponent > 1... hmm "可积当指数>1" probably means the second-differentiated kernel $|t-u|^{\beta-2}$ needs $\beta - 2 > -1$). After finitely many rounds the residual exponent lands in $(-1, 1]$, then two cases:
- Negative exponent ($-1 < \beta_k < 0$): the equation reads $\mathcal V^{(k)}(t) = $ const·$t^{\beta_k - k'}$-ish... the RHS has negative power of $t$ which blows up as $t \to 0^+$ while the LHS stays bounded. Contradiction unless coefficient zero.
- Exponent in $(0,1]$: differentiate once more to get a one-sided negative-exponent equation, then blow up.

Let me work this out concretely. Set $\beta_0 = 2H \in (0,2)$.

Case analysis on fractional part: Let me just do the general scheme. Define $\mathcal V_j$ = j-th derivative of $\mathcal V$ (where valid). 

General principle: $\frac{d}{dt}|t-u|^\gamma$ (classical, away from diagonal) $= \gamma\,\mathrm{sgn}(t-u)|t-u|^{\gamma-1}$ for $\gamma \ne 0$; second derivative $= \gamma(\gamma-1)|t-u|^{\gamma-2}$.

If $\beta > 1$: $\mathcal V \in C^2$? Second derivative kernel $|t-u|^{\beta-2}$ with $\beta - 2 \in (-1, 0)$: $\mathcal V''(t) = \beta(\beta-1)\int|t-u|^{\beta-2}g(u)du$ exists for all $t$ (integrable singular), and $\mathcal V''$ is continuous. RHS: $\frac{d^2}{dt^2}[At^\beta + C] = A\beta(\beta-1)t^{\beta-2}$ for $t > 0$. So
$$\int_0^1 |t-u|^{\beta-2}g(u)du = A t^{\beta-2} \quad (t>0).$$
New exponent $\beta_1 = \beta - 2 \in (-1, 0)$: negative branch → blow up at $t \to 0^+$: RHS $\to \pm\infty$ if $A \ne 0$, LHS: $\left|\int|t-u|^{\beta-2}g(u)du\right| \le \|g\|_\infty \sup_t \int_0^1 |t-u|^{\beta-2}du \le \|g\|_\infty \cdot \frac{2}{\beta-1}$ bounded. So $A = 0$. 

If $\beta = 1$: $\mathcal V'(t) = \int \mathrm{sgn}(t-u)g(u)du$ (kernel $|t-u|^0$, sgn; derivative exists, $\mathcal V' = G(t) - G(1-t)$-ish, continuous piecewise... actually $\mathcal V'(t) = \int_0^t g - \int_t^1 g$ is continuous, even Lipschitz). $\mathcal V'' (t)= 2g(t)$ a.e. RHS: $A t^{\beta-2} = A t^{-1}$ for $t>0$ — blow up unless $A=0$ (LHS $\mathcal V''$ locally bounded a.e.). Actually simpler: for $\beta = 1$, compare behavior: $\mathcal V(t) = \int|t-u|g = \int_0^t(t-u)g + \int_t^1(u-t)g = tG(t) - \int_0^t ug + \int_t^1ug - t(G - G(t))$ where $G = \int_0^1 g$. As $t \to 0^+$: $\mathcal V(t) \to \int_0^1 ug\,du$ hmm wait: $tG(t) \to 0$, $-\int_0^t ug \to 0$, $\int_t^1 ug \to \int_0^1 ug$, $-t(G-G(t)) \to 0$. So $\mathcal V(t) \to C'$ finite. RHS $At + C$ fine. Hmm, that doesn't immediately kill it. Use the second-derivative route: $\mathcal V \in W^{2,\infty}_{loc}$, $\mathcal V'' = 2g$ a.e.; RHS $At^{-1} + 0$. If $A \neq 0$, RHS not in $L^1_{loc}(0,1)$... but $\mathcal V'' = 2g \in L^\infty$. Contradiction. Clean.

If $\beta < 1$: $\mathcal V$ may fail to be differentiable at interior points, but we can still use: $\mathcal V(t) - \mathcal V(t_0) = \int_0^1 [|t-u|^\beta - |t_0-u|^\beta]g(u)du$. Hmm, the notes' approach: "负指数直接 $s\to0^+$" — for $\beta<1$, consider the equation $\mathcal V(t) = At^\beta + C$ as $t \to 0^+$: LHS $\to \int_0^1 u^\beta g(u)du =: v_0$ (finite, by continuity & boundedness). RHS: if $A\neq0$ and... $At^\beta + C \to C$. Both finite! No contradiction yet. So must differentiate once: 

For $\beta \in (0,1)$: Consider $\mathcal V'(t)$ for $t \notin \{u\}$... hmm. Alternative: difference quotient. $\frac{\mathcal V(t+h)-\mathcal V(t)}{h}$ as $h\to0$... The classical trick: for $\beta\in(0,1)$, the function $t \mapsto \mathcal V(t)$ is Hölder-$\beta$; the RHS is $At^\beta + C$; equating doesn't immediately give contradiction.

Better approach following notes: differentiate once in a generalized sense. Define $W(t) := \int_0^1 \mathrm{sgn}(t-u)|t-u|^{\beta-1}\beta g(u)\,du$ — this is an actual $L^1_{loc}$ function of $t$ (since $\beta - 1 > -1$), and $\mathcal V(t) = \mathcal V(0) + \int_0^t W(s)ds$. Indeed: $\int_0^t \mathrm{sgn}(s-u)|s-u|^{\beta-1}\beta\,ds = |t-u|^\beta - |u|^\beta$ (check: for $s<u$: $\frac{d}{ds}[-(u-s)^\beta]\cdot$something... let me verify: $\frac{d}{ds}|s-u|^\beta = \beta\,\mathrm{sgn}(s-u)|s-u|^{\beta-1}$. Yes.) So $\mathcal V(t) - \mathcal V(0) = \int_0^t \beta\int \mathrm{sgn}(s-u)|s-u|^{\beta-1}g(u)duds$. 

RHS of equation: $At^\beta + C - C = At^\beta$. So
$$\int_0^t W(s)ds = At^\beta, \quad t\in[0,1],$$
with $W \in L^1(0,1)$ (actually $L^\infty$ if $g$ bounded: $|W| \le \beta\|g\|_\infty\int_0^1|s-u|^{\beta-1}du < \infty$). But $t \mapsto At^\beta$ is not an indefinite integral of an $L^1$ function unless $A = 0$... why: if $A \ne 0$, $t^\beta$ with $\beta<1$ is not absolutely continuous on $[0,\epsilon]$: indeed any indefinite integral of $L^1$ is absolutely continuous, hence uniformly continuous with modulus controlled; but more directly, absolute continuity fails: $t^\beta = o(...)$... Simplest: absolutely continuous functions have derivative a.e., and $\frac{d}{dt}At^\beta = A\beta t^{\beta-1} \notin L^1_{loc}$ when... hmm, actually a.e.-derivative existing isn't enough. Cleanest: AC functions satisfy $|f(y)-f(x)| = |\int_x^y f'| \le \int_x^y|f'|$ and $\int_0^\epsilon |f'| < \infty$. Suppose $At^\beta = \int_0^t W$. Take partition $t_k = (k/n)^\mu$ hmm. Alternative clean argument: $\int_0^t W(s)ds$ is AC, so $t\mapsto At^\beta$ extends to an AC function on $[0,1]$; but AC functions are exactly those of bounded variation with measure-valued derivative absolutely continuous wrt Lebesgue; $t^\beta$ ($0<β<1$) has variation $O(1)$ on $[0,\delta]$: total variation of $t^\beta$ on $[0,1]$ is 1, finite. BV fine. Hmm, so need the right invariant: AC ⟺ BV + derivative ∈ L¹ + f(t) = f(0)+∫f′. $t^\beta$ IS BV. Its a.e. derivative is $\beta t^{\beta-1} \notin L^1(0,\epsilon)$. If it were AC then $t^\beta - t^\beta(0)= t^\beta = \int_0^t \beta s^{\beta-1}ds$ would require $\beta s^{\beta-1} \in L^1$, false. But how do I know the a.e. derivative computed classically off 0 is THE derivative appearing in the AC decomposition? Because if $f \in AC$ then $f' $ (classical a.e.) $= $ the $L^1$ rep. And classically, for $t>0$, $\frac{d}{dt}t^\beta = \beta t^{\beta-1}$. So $f' = \beta t^{\beta-1}$ a.e. on $(0,1)$, which is not integrable near 0, contradicting AC. Solid. So $A = 0$.

Hmm wait, but actually for $\beta \in (0,1)$ I could ALSO just use the same trick as $\beta>1$ but only differentiating once and getting one-sided kernels... The notes say for $(0,1]$: "先再微分一次化为单侧负指数方程再爆破" (differentiate once more to reduce to one-sided negative exponent equation, then blow up). Let me see: for $\beta \in (0,1)$: differentiate once: $W(t) = \beta\int\mathrm{sgn}(t-u)|t-u|^{\beta-1}g(u)du = A\beta t^{\beta-1}$ for a.e./all $t>0$ (W continuous? $|t-u|^{\beta-1}$ integrable uniformly, and W is continuous in t by dominated conv; and $\mathcal V' = W$ everywhere since $\mathcal V(t) - \mathcal V(0) = \int_0^t W$ and W continuous ⟹ V is C¹). RHS $A\beta t^{\beta-1} \to \pm\infty$ as $t\to0^+$ if $A \ne 0$ (since $\beta - 1 < 0$), while LHS $W(0) = \beta\int\mathrm{sgn}(-u)u^{\beta-1}g(u)du$ finite. Contradiction. 

That's the "one-sided negative exponent blow-up": after differentiating once, the equation $W(t) = A\beta t^{\beta-1}$ has negative exponent on the right. Same for $\beta = 1$: $W(t) = A$, no info... wait for $\beta=1$: $\mathcal V'(t) = \int \mathrm{sgn}(t-u)g = A$?? RHS $A\cdot 1\cdot t^0 = A$. So $W(t) \equiv A$ where $W(t) = \int_0^t g - \int_t^1 g$; then $g = \frac12 W' = 0$?? Wait: $W'(t) = g(t)+g(t) = 2g(t)$, and if $W \equiv A$ then $g \equiv 0$ directly! Interesting — for $\beta = 1$ (which corresponds to $H = 1/2$, Brownian motion), the potential equation alone gives $g \equiv 0$. Nice, consistent with known results (this is the classical case).

Hmm wait, but hold on: for β=1, does the argument give $g≡0$ without needing Steps 2–3? $W ≡ A$ means $\int_0^t g = \int_t^1 g$ for all t, differentiating: $g = -g$, so $g ≡ 0$. Yes! For H = 1/2, Lemma A is immediate. But note the general chain still covers it via steps 2–3 (with $A=0$ obtained from... hmm, for β=1, how do we get $A = 0$ in the general scheme? From $W ≡ A$ and integrating: $W(1^-) = \int_0^1 g - 0 = A$ ✓ consistent, no contradiction. So the ladder gives nothing for β=1; instead we directly get $g≡0$. Fine — handle β=1 separately or note that steps 2–3 with A unknown still work: energy identity $\mathcal E_1(g) = 2AC$ where... hmm with A possibly nonzero. But actually for β=1 we've shown $g≡0$ directly. Also note: for β=1, $\mathcal E_1(g) = \iint g(s)g(t)|s-t|dsdt = \int |\hat g|^2 \cdot c|\xi|^{-2}$-ish, and $\mathcal E_1(g) \ge 0$ always (it's $\int\int (g\otimes g)|s-t|$ — positive definite kernel $|x|$? $|x|$ is conditionally negative definite, so $-|x|$ is PD... wait. Hmm: $|x|^\alpha$ for $\alpha \in (0,2]$ is conditionally negative definite (CND); for $\alpha\in(0,2)$ strictly CND; $\alpha = 2$ gives $|x|^2$ which is CND too (quadratic). So $\mathcal E_\alpha(g) \le 0$?? Let me recheck sign!

CRITICAL SIGN CHECK. Schoenberg: $|x|^\alpha$, $\alpha \in (0,2)$, is conditionally negative definite: $\sum c_i c_j |x_i - x_j|^\alpha \le 0$ whenever $\sum c_i = 0$. So for zero-mean $g$: $\mathcal E_\alpha(g) = \iint g(s)g(t)|s-t|^\alpha \le 0$!! 

But the notes say $\mathcal E_{2H}(g) = c_H\int\xi^{-1-2H}(A^2 - |\hat g(\xi)|^2)d\xi$ — with $A=0$: $= -c_H\int\xi^{-1-2H}|\hat g(\xi)|^2d\xi \le 0$. Yes! Negative. And $\mathcal E = 0$ iff $\hat g \equiv 0$. Sign consistent with CND. Good, the notes' formula has the right sign ($A^2 - |\hat g|^2$). I mis-wrote above ("≥0") — correct statement: $\mathcal E_{2H}(g) = -c_H\int |\hat g(\xi)|^2|\xi|^{-1-2H}d\xi \le 0$ for zero-mean $g$, with equality iff $g\equiv0$. 

And Step 2: $\mathcal E = 2AC$; with $A=0$, $\mathcal E = 0$; combined with strict negativity on zero-mean class: $g \equiv 0$. All consistent.

Also verify Step 2 algebra independently: $\mathcal V(t) = \int_0^1|t-u|^\beta g(u)du = At^\beta + C$ for all $t$. Multiply by $g(t)$, integrate over $t$: $\iint g(t)g(u)|t-u|^\beta du\,dt = A\int t^\beta g(t)dt + C\int g(t)dt = AC + C\cdot A = 2AC$. ✓. (Notes wrote it as $A(C+D)$ with their shifted constants; same thing.)

Sanity check of Lemma A conclusion with a concrete example: BM case ($\beta = 1$): shown $g≡0$ directly. Another check: try $g$ = nonzero with $\int g = A \neq 0$ — could $\mathcal V(t) - At^\beta$ be constant? E.g. $g \equiv 1$: $\mathcal V(t) = \int_0^1|t-u|^\beta du = \frac{t^{\beta+1}+(1-t)^{\beta+1}}{\beta+1}$. Is that $= At^\beta + C$ with $A = 1$? $t^{\beta+1}$ vs $t^\beta$: no. ✓ not a solution.

Numerical verification will be done via Python: discretize, build matrix $K_{ij} = |t_i - t_j|^\beta$, solve least squares / nullspace: find $g$ with $Kg = At + c$ — check nullspace dimension numerically. Also sympy check of energy identity for polynomial test functions: compute $\iint g(s)g(t)|s-t|^\beta$ symbolically vs $2AC$ given $\mathcal V = At^\beta + C$... but polynomial g won't satisfy the potential equation exactly; instead verify the *identity* $\iint g\otimes g|s-t|^\beta = \int g(t)[At^\beta + C](t)dt$ holds whenever $\mathcal V \equiv At^\beta+C$ — that's trivially true. Better symbolic check: verify that for specific functions, $\mathcal V(t) \ne At^\beta + C$; and verify the Fourier/Laplace representation constant numerically: check $|x|^\alpha \stackrel{?}{=} C_\alpha\int(1-\cos(\xi x))|\xi|^{-1-\alpha}d\xi$ numerically for sample values.

Let me recall the exact constant: For $0<\alpha<2$,
$$\int_{\mathbb R}(1-\cos(\xi x))\frac{d\xi}{|\xi|^{1+\alpha}} = \frac{2\Gamma(1-\alpha)\sin(\pi\alpha/2)}{\alpha}|x|^\alpha \cdot(-1)?$$ 
Known: $\int_0^\infty \frac{1-\cos(\xi x)}{\xi^{1+\alpha}}d\xi = \frac{-\Gamma(-\alpha)\cos(\pi\alpha/2)}{} |x|^\alpha$ hmm let me just derive numerically in Python. Standard result: $\int_0^\infty\frac{1-\cos t}{t^{1+\alpha}}dt = \frac{\pi}{2\Gamma(1+\alpha)\sin(\pi\alpha/2)}$ for $0<\alpha<2$. Then substituting $\xi x$: $\int_0^\infty\frac{1-\cos(\xi x)}{\xi^{1+\alpha}}d\xi = |x|^\alpha\int_0^\infty\frac{1-\cos y}{y^{1+\alpha}}dy = \frac{\pi|x|^\alpha}{2\Gamma(1+\alpha)\sin(\pi\alpha/2)}$.

So $|x|^\alpha = \frac{2\Gamma(1+\alpha)\sin(\pi\alpha/2)}{\pi}\int_0^\infty\frac{1-\cos(\xi x)}{\xi^{1+\alpha}}d\xi = c_\alpha'\int_\mathbb R(1-\cos(\xi x))|\xi|^{-1-\alpha}d\xi$ with $c_\alpha' = \frac{\Gamma(1+\alpha)\sin(\pi\alpha/2)}{\pi}$.

Check α=1: $\int_0^\infty\frac{1-\cos y}{y^2}dy = \pi/2$. Formula: $\frac{\pi}{2\Gamma(2)\sin(\pi/2)} = \pi/2$ ✓. And $c_1' = \Gamma(2)\sin(\pi/2)/\pi = 1/\pi$; then $|x| = \frac1\pi\int_\mathbb R(1-\cos\xi x)\frac{d\xi}{\xi^2}$ ✓ (known identity). Good.

Now the full Fourier identity for the energy: for $g \in L^1 \cap$ nice, zero mean:
$$\mathcal E_\alpha(g) = \iint g(s)g(t)|s-t|^\alpha dsdt = c_\alpha'\int_\mathbb R\big[(\hat g(0))^2 - |\hat g(\xi)|^2\big]|\xi|^{-1-\alpha}d\xi.$$
where $\hat g(\xi) = \int g(t)e^{-i\xi t}dt$. Check: $\iint g(s)g(t)c\int(1-\cos(\xi(s-t)))|\xi|^{-1-\alpha}d\xi dsdt = c\int|\xi|^{-1-\alpha}[A^2 - \Re\iint g_sg_te^{i\xi(s-t)}] = c\int|\xi|^{-1-\alpha}[A^2 - |\hat g(\xi)|^2]$ ✓ (with $\hat g(\xi)=\int g e^{-i\xi t}$, $\Re\iint g(s)g(t)e^{i\xi(s-t)}dsdt = |\hat g(\xi)|^2$ for real $g$ ✓).

Justification of swapping: for zero-mean $g$, integrand $[A^2 - |\hat g|^2]|\xi|^{-1-\alpha}$: near 0, $|\hat g(\xi)|^2 = |\int g(e^{-i\xi t}-1)|^2 \le \xi^2(\int|tg|)^2$, so integrand $\lesssim |\xi|^{1-\alpha}$, integrable since $\alpha<2$ ✓; at ∞, bounded by $(A^2 + \|g\|_1^2)|\xi|^{-1-\alpha}$, integrable since $\alpha>0$ ✓. Absolute convergence of the ξ-integral ✓. To exchange ∬ and ∫ rigorously: apply Tonelli to truncated $\psi_M(x) := (1-\cos(\xi x))$ cutoff... The cleanest: define $I_M = \int_{|\xi|\le M}$. Then $\iint g_sg_t I_M(s-t) dsdt = \int_{|\xi|\le M}|\xi|^{-1-\alpha}[A^2-|\hat g|^2]d\xi$ by Fubini (all bounded on compacts: $|1-\cos(\xi x)| \le \min(2, \xi^2x^2/2) \le 2$, and $\int_{|\xi|\le M}|\xi|^{-1-\alpha} < \infty$; kernel $x \mapsto \int_{|\xi|\le M}(1-\cos\xi x)|\xi|^{-1-\alpha}d\xi$ is bounded continuous on supp of $g\otimes g$, i.e., on $[-1,1]$ ✓). Then $M\to\infty$: LHS → $\mathcal E$ provided $\int_{|\xi|\le M}(1-\cos(\xi x))|\xi|^{-1-\alpha}d\xi \to |x|^\alpha/c_\alpha'$ pointwise AND dominated on $x\in[-1,1]$: dominated by $\min(C|x|^2M^{1-\alpha}, C')$... hmm need domination independent of M. Pointwise limit known. Domination: for $x \in [-1,1]$, $\int_{|\xi|\le M}(1-\cos(\xi x))|\xi|^{-1-\alpha}d\xi \le \int_{\mathbb R}(1-\cos(\xi x))|\xi|^{-1-\alpha}d\xi = |x|^\alpha/c_\alpha' \le 1/c_\alpha'$ ✓ (all terms nonneg!). Monotone convergence even. So LHS → $c_\alpha'^{-1}\cdot$ wait careful: $\lim_M \int_{|\xi|\le M}(1-\cos(\xi x))|\xi|^{-1-\alpha}d\xi = |x|^\alpha / c_\alpha'$, and by monotone convergence applied to $\iint g_sg_t[\cdots]$ — but $g_sg_t$ changes sign! MCT doesn't directly apply. Use dominated convergence: the partial kernels are dominated by $|x|^\alpha/c_\alpha'$ on $[-1,1]^2$ ✓ (since partial sums of nonneg terms increase to the full integral). DCT works ✓. RHS → the full integral by monotone/dominated conv on the ξ-side given $A^2 - |\hat g|^2$ might be negative... hmm. $A^2 - |\hat g(\xi)|^2$ can be negative for some ξ (if $g$ changes sign, $\hat g$ can exceed $A$ in magnitude... e.g. $g = 1_{[0,1/2]} - 1_{[1/2,1]}$, $A = 0$, fine that's zero-mean. For zero-mean $g$, $A = 0$ and integrand is $-|\hat g|^2|\xi|^{-1-\alpha} \le 0$, increasing in magnitude — apply dominated convergence to $|\hat g|^2|\xi|^{-1-\alpha}$ truncated: $|\hat g|^2 \le \|g\|_1^2$, tail dominated ✓, near-zero part: $|\hat g(\xi)|^2|\xi|^{-1-\alpha} \le \xi^2(\int|tg|)^2\xi^{-1-\alpha} = C\xi^{1-\alpha} \le C$ on $(0,1]$ ✓. DCT fine ✓.)

Great, fully rigorous. Since in our application $A = 0$ (from Step 1), we only need the zero-mean version. 

But WAIT — there's an ordering subtlety: Step 1 gives $A = 0$ for ALL $\beta \in (0,2)$ including $\beta = 1$ (via the direct $g≡0$ or via... hmm for β=1 the ladder gave $g≡0$ directly, even better). Actually let me re-examine: for β=1, Step 1's goal is $A=0$; we showed stronger: $g≡0$. Fine. For β≠1, ladder gives $A=0$; then Steps 2–3 give $g≡0$. Unified conclusion ✓.

Hmm wait, actually for β=1, let me redo within the general framework to keep the proof uniform: β=1: $\mathcal V(t) = At + C$. $\mathcal V'(t) = \int\mathrm{sgn}(t-u)g(u)du = A$ for all $t$ (V is C¹ here). Differentiate: $2g(t) = 0$ ⟹ done. So for β=1 skip to conclusion. For β∈(0,1)∪(1,2): ladder ⟹ A=0 ⟹ energy ⟹ g≡0. Uniform enough.

Alternatively for β=1 treat via the SAME two-case machinery: β=1 falls in "(0,1]" branch: differentiate once: $W(t) = A\cdot 1\cdot t^{0} = A$ — exponent 0, no blow-up. Then differentiate again: $W'(t) = 2g(t)$, RHS derivative 0 ⟹ $g≡0$. That's the "$(0,1]$ 先再微分一次" branch: after differentiating once you get exponent $\beta - 1 = 0 \in (0,1]$... then differentiate once more to get negative single-sided exponent? $W'(t) = 2g$, RHS $= 0$. Hmm the notes' description: "(0,1] 先再微分一次化为单侧负指数方程再爆破" — differentiate once more to reach a one-sided negative-exponent equation. For β=1: after two differentiations, exponent $-1$: $\mathcal V''(t) = 2g(t)$ vs RHS $A\beta(\beta-1)t^{-1} = 0$ (coefficient vanishes!). So actually the coefficient $\beta(\beta-1) = 0$ makes RHS zero, giving $g ≡ 0$ directly. Either way β=1 is easy. I'll present it cleanly.

Hmm, actually wait. Let me reconsider whether for β ∈ (0,1), ONE differentiation suffices, making the whole thing cleaner:

β ∈ (0,1): $\mathcal V \in C^1$? Is it? $\mathcal V(t) = \int_0^1|t-u|^\beta g(u)du$. Kernel $|x|^\beta$ with β∈(0,1) is C¹ off 0 with derivative $\beta\,\mathrm{sgn}(x)|x|^{\beta-1}$, which near 0 behaves like $|x|^{\beta-1}$, integrable (index $\beta - 1 > -1$) ✓. So $\mathcal V'(t) = \beta\int_0^1 \mathrm{sgn}(t-u)|t-u|^{\beta-1}g(u)du$ EXISTS for every t and is CONTINUOUS (dominated conv, kernel integrable uniformly in t: $\sup_t\int_0^1|t-u|^{\beta-1}du \le \frac{2}{\beta}$ ✓). So $\mathcal V \in C^1([0,1])$ and the equation differentiates:
$$\beta\int_0^1\mathrm{sgn}(t-u)|t-u|^{\beta-1}g(u)du = A\beta t^{\beta-1}, \quad t\in(0,1].$$
As $t\to0^+$: RHS $\sim A\beta t^{\beta-1} \to \operatorname{sgn}(A)\infty$ if $A\neq0$ (since β−1<0). LHS at $t=0$: $\beta\int_0^1(-u^{\beta-1})g(u)du$, FINITE (bounded by $\beta\|g\|_\infty\cdot\frac{1}{\beta} = \|g\|_\infty$). Continuity of LHS ⟹ bounded near 0. Contradiction ⟹ $A = 0$. ✓✓ So for β∈(0,1): ONE differentiation. 

For β∈(1,2): TWO differentiations: $\mathcal V \in C^2$ (second kernel $|t-u|^{\beta-2}$, exponent ∈(−1,0), integrable, V″ continuous), 
$$\int_0^1|t-u|^{\beta-2}g(u)du = A t^{\beta-2},\quad t\in(0,1],$$
(coefficient β(β−1) cancels, β≠0,1). As $t\to0^+$: RHS blows up if $A\neq0$; LHS bounded ($\sup_t \int_0^1|t-u|^{\beta-2}du < \infty$ since β−2>−1 ✓). ⟹ $A=0$ ✓.

For β=1: shown $g\equiv0$ directly.

BEAUTIFUL — the "ladder" collapses: since $\beta = 2H \in (0,2)$ always, we NEVER need more than two differentiations! The multi-round ladder in the notes was for safety; actually one round suffices: β∈(0,1): 1 deriv; β∈{1}: trivial; β∈(1,2): 2 derivs. The reason the notes had a ladder: they considered iterating because after 2 derivations the new equation (exponent β−2 ∈ (−1,0)) could itself be differentiated further — unnecessary. One round suffices. 

So Lemma A proof:
Given: $g\in C([0,1])$, $\exists A, C\in\mathbb R$: $\int_0^1|t-u|^\beta g(u)du = At^\beta + C$ ∀t∈[0,1].

- Case β∈(0,1)∪(1,2): differentiate (once if β<1, twice if β>1) to obtain $\Phi(t) = At^{\beta-1}$ resp. $At^{\beta-2}$ where Φ is continuous on [0,1] (bounded); RHS unbounded near 0⁺ unless A=0; hence A=0.
- Case β=1: differentiate once: $\int\mathrm{sgn}(t-u)g = A$; differentiate again: $2g(t)=0$; g≡0. (Done, skip rest.)
- Now A=0. Energy: $\mathcal E_\beta(g) = \iint g_sg_t|s-t|^\beta = 2AC = 0$ (multiply potential eq. by g, integrate).
- Laplace/Fourier: zero-mean ⟹ $\mathcal E_\beta(g) = -c_\beta'\int|\hat g(\xi)|^2|\xi|^{-1-\beta}d\xi$. Zero ⟹ $\hat g\equiv0$ a.e. ⟹ (continuity of ĝ) $\hat g\equiv0$ everywhere ⟹ $g\equiv0$. □

Note: for the case β∈(0,1), after getting A=0 we don't even need the differentiated equation anymore; energy identity uses the ORIGINAL potential equation ✓ valid.

Double-check the energy identity derivation once more: potential eq: $\mathcal V(t) = \int_0^1|t-u|^\beta g(u)du = A t^\beta + C$. Multiply both sides by $g(t)$ and integrate t∈[0,1]:
LHS $= \int_0^1\int_0^1 g(t)g(u)|t-u|^\beta\,du\,dt = \mathcal E_\beta(g)$.
RHS $= A\int_0^1 t^\beta g(t)dt + C\int_0^1g(t)dt = A\cdot C' + CA$ where $C' := \int t^\beta g(t)dt$. 

WAIT. Is $C' = C$? In the potential equation, what is C? It's just some constant such that $\mathcal V - At^\beta \equiv C$. From the original problem: $U_g(t)\equiv0$ expands to $\mathcal V(t) = \frac12[C' + At^{2H}\cdot...]$ hmm let me redo. Original: $\int_0^1 g(u)R_H(u,t)du \equiv 0$ with $R_H(u,t) = \frac12(u^{2H} + t^{2H} − |u−t|^{2H})$:
$$\frac12\Big[\underbrace{\int g(u)u^{2H}du}_{=:C'} + t^{2H}\underbrace{\int g(u)du}_{=:A} − \mathcal V(t)\Big] \equiv 0$$
⟹ $\mathcal V(t) = C' + A t^{2H}$. So in our Lemma A hypothesis, $C = C' = \int t^\beta g(t)dt$ and $A = \int g$. THEN: RHS of multiplied eq $= AC + CA = 2AC$ ✓ where indeed $C = \int t^\beta g$. 

So in the application, the constant C is FORCED to equal $\int t^\beta g(t)dt$ — good, that's why the identity is exactly $2AC$. In abstract Lemma A, should I assume C arbitrary or $C = \int t^\beta g$? Note: IF $\mathcal V(t) = At^\beta + C$ for all t, then plugging t=0: $\mathcal V(0) = \int u^\beta g(u)du = C$ automatically (since $A\cdot0^\beta = 0$)! So $C = \int t^\beta g$ is automatic ✓. Great — so Lemma A can state: if $\mathcal V(t) − At^\beta$ is constant on [0,1], then g≡0. Clean.

Energy identity: $\mathcal E_\beta(g) = 2AC$ where $A=\int g$, $C=\int t^\beta g$. With $A=0$: $\mathcal E = 0$ ✓.

Everything checks. Now assemble the FULL PROOF.

---

## Full proof structure for proof.md

**Theorem.** Let $B$ be fBm with Hurst $H\in(0,1)$ on $[0,1]$, $Z=\int_0^1B_s^4ds$. Then the law of $Z$ is absolutely continuous w.r.t. Lebesgue measure.

**Proof.**

**Setup/Notation.** fBm: centered Gaussian, $R_H(s,t)=\mathbb E[B_sB_t]=\frac12(s^{2H}+t^{2H}−|s−t|^{2H})$, continuous paths, self-similarity $B_{ct}\stackrel d=c^HB_t$. Hilbert space $\mathcal H$: completion of step functions under $\langle1_{[0,s]},1_{[0,t]}\rangle_{\mathcal H}=R_H(s,t)$; canonical isonormal $W(f)$ hmm — actually $B_t = W(1_{[0,t]})$ where $W$ isonormal on $\mathcal H$; $\|1_{[0,t]}\|^2 = t^{2H}$, $\|1_{[0,s]}−1_{[0,t]}\|^2=|s−t|^{2H}$.

**Step 1 (Z ∈ 𝔻^{1,p}).** $f(x)=x^4$: $|f(x)|\le x^4$, $|f'(x)|=4|x|^3$. Chain rule for $F = \int u\,dB$ type... Actually $Z = \int_0^1 B_t^4 dt$ is a pathwise Lebesgue integral of the process $t\mapsto B_t^4 \in \mathbb D^{1,p}$ hmm. Standard result (Nualart Prop 5.2.1-ish for fBm / general: if $u\in L^p([0,1]\times\Omega)$ with $u_t \in \mathbb D^{1,q}$ suitably and measurable versions, then $\int u_tdt\in\mathbb D^{1,q}$ and $D_s\int u = \int D_su$): 

Moments: $\mathbb E|B_t|^k \le C_k t^{kH}$ (scaling: $B_t \stackrel d = t^HB_1$, $N(0,1)$ moments). $\mathbb E\int_0^1|B_t|^{4p}dt = \int\mathbb E|B_t|^{4p} \le C\int t^{4pH}dt < \infty$ ⟹ $Z\in L^p$, and $B^4_t\in\mathbb D^{1,p}$ with $D_sB_t^4 = 4B_t^31_{\{s\le t\}}$, $\mathbb E\int_0^1\|DB_t^4\|^p_{\mathcal H}dt$: $\|DB_t^4\|_{\mathcal H} = 4|B_t|^3\|1_{[0,t]}\| = 4|B_t|^3t^H$, $\mathbb E|B_t|^{3p}t^{Hp} \le Ct^{Hp+3pH}$, integrable ✓. So $Z\in\mathbb D^{1,p}$ ∀p<∞ and 
$$D_sZ = 4\int_0^1B_t^3\,1_{\{s\le t\}}\,dt = 4\int_s^1B_t^3\,dt.$$
(Nualart Thm 3.2.6 / Prop 3.2.7-type: chain rule + differentiation under the integral; conditions verified via moment bounds. I'll cite Nualart 2006 Prop 3.2.7 hmm, actually the relevant one: Prop 3.2.7 is about $F=\varphi(W(h_1),...,)$; for integrals: Proposition 3.2.8? Or in Ch.5 fBm section 5.2... The generic statement: if $F\in\mathbb D^{1,p}$ and $\varphi$ smooth bounded... For our purposes: cite "Nualart (2006), Proposition 3.2.7 & the chain rule", plus localness/smooth approximation for $x^4$ — or simply state: $B_t^4 = f(B_t)$, $f$ polynomial, chain rule Prop 3.2.7 hmm wait actually I realize the cleanest citation: Nualart Prop 3.2.7: if $F_i\in\mathbb D^{1,p}_\text{loc}$ hmm. Polynomial chain rule is standard: $\mathbb D^{1,2}$ is closed under polynomials with $DP(F) = P'(F)DF$ — that's in Nualart §3.2 basic properties (Prop 3.2.7 in 2nd ed? I believe Prop 3.2.7 is exactly "let φ ∈ C¹ with bounded derivative..." and there's a remark extending to polynomials). Fine—I'll phrase citations generically-but-correctly: "Nualart (2006), Section 3.2 (chain rule)".)

**Step 2 (‖DZ‖² formula).** As computed:
$$\|DZ\|^2_{\mathcal H}=16\iint_{[0,1]^2}B_s^3B_t^3\,R_H(s,t)\,ds\,dt =:16\,Q(B^3).$$
Derivation: $\|DZ\|^2 = \langle 4m,4m\rangle$, $m = \int_0^1 B_t^3\,\tilde1_{[0,t]}\,dt$ Bochner in $\mathcal H$ hmm — actually simpler: $\|DZ\|^2_{\mathcal H}$ where $DZ\in L^2(\Omega;\mathcal H)$, and $\langle DZ,DZ\rangle_\mathcal H = \iint (DsZ)(DtZ)\langle\tilde1_{?}...\rangle$... Let me do it cleanly:

$D_sZ = 4\int_s^1B_t^3dt$ is a scalar function of $s$; but elements of $\mathcal H$ ARE equivalence classes of functions (completion of step functions embeds into... hmm, actually the map step-func ↦ its function may not be injective on the completion — the classic subtlety!). The safe computation: $\|DZ\|^2_{\mathcal H} = \langle DZ, DZ\rangle$ where $DZ = D(Z) \in L^2(\Omega;\mathcal H)$. Compute via duality with step functions: $\langle DZ, 1_{[a,b]}\rangle = ?$ Hmm. Cleanest: use the chain rule directly on $Z$ as a functional:

Alternative clean route: $D_s Z = 4\int_0^1 B_t^3 1_{\{s\le t\}}dt$ — for each fixed $s$, this is a NUMBER; the map $s\mapsto D_sZ$ defines the representative. Then formally $\|DZ\|^2_{\mathcal H} = \iint D_sZ\,D_tZ\,R_H(ds,dt)$?? No wait — that's mixing conventions badly. UGH. Let me fix conventions ONCE.

**Nualart's fBm convention (Ch. 5, 2nd ed.)**: $\mathcal H$ = completion of step functions w.r.t. $\langle 1_{[0,s]},1_{[0,t]}\rangle_\mathcal H := R_H(s,t)$. Isonormal $W$ on $\mathcal H$: $B_t = W(1_{[0,t]})$. Malliavin: $D: L^2(\Omega)\to L^2(\Omega\times[0,1])$-ish — NO: $DF\in L^2(\Omega;\mathcal H)$, written $DF = \{D_\rho F\}_{\rho}$ with $D_\rho F \in \mathcal H$. For $F = W(h)$: $D_\rho F = h$ (∈𝓗) ∀ρ. Chain rule: $D_\rho F = \sum \partial_i\varphi\, D_\rho F_i$ where $D_\rho F_i \in \mathcal H$.

So: $D_\rho B_t = 1_{[0,t]} \in\mathcal H$ (constant in ρ!). $D_\rho Z = \int_0^1 4B_t^3\cdot D_\rho B_t\,dt = 4\int_0^1B_t^3\,1_{[0,t]}\,dt$ — a Bochner integral in $\mathcal H$, INDEPENDENT of ρ! Indeed: $Z$ depends on the whole path, and $D_\rho Z\in\mathcal H$ is the "sensitivity direction"... interesting, in this convention EVERY $D_\rho Z$ is the same $\mathcal H$-element. Then
$$\|DZ\|^2_{L^2(\Omega;\mathcal H)}\ \widehat{=}\ \int_0^1\|D_\rho Z\|^2_{\mathcal H}\,d\rho = \int_0^1 16\Big\|\int_0^1B_t^3\,1_{[0,t]}dt\Big\|^2_{\mathcal H}d\rho = 16\Big\|\int_0^1B_t^3\,1_{[0,t]}dt\Big\|^2_{\mathcal H}.$$
Hmm wait, is the norm in the BH criterion $\|DF\|^2_{\mathcal H} := \int_0^1\|D_\rho F\|^2_{\mathcal H}d\rho$? YES — in Nualart Ch.5 (fBm), the BH-type criterion is stated as: if $\int_0^1\|D_\rho F\|^2_\mathcal H d\rho > 0$ a.s. then law is AC. Hmm, actually I recall in Nualart's book, Theorem 5.2.? hmm. Let me think about what's actually true and citable.

Actually hold on. I recall the standard treatment (e.g., Nualart's book, or Hu–Nualart "Some results on fractional Brownian motion...", or Alos–Mazet–Nualart 2001 "Stochastic calculus with respect to Gaussian processes"): For a Gaussian process $X$ with covariance RKHS $\mathcal H$, $F\in\mathbb D^{1,2}$, the criterion is $P(\|DF\|_{\mathcal H}>0)>0$ hmm, where $\|DF\|^2_{\mathcal H} = \int_0^T \|D_\rho F\|^2_{\mathcal H}d\rho$ in the "two-slot" convention. The event $\{\|DF\|=0\} = \{$all $D_\rho F = 0\}$.

Either way: $\|DF\| = 0$ ⟺ $D_\rho Z = 0$ (as 𝓗-element) for a.e./all ρ ⟺ $m:=\int_0^1B_t^3 1_{[0,t]}dt = 0$ in 𝓗. Same reduction. ✓.

So: **Event reduction**: $E:=\{\|DZ\|_{\mathcal H}=0\} = \{m = 0\}$, and on $E$: for all $t\in[0,1]$ (by continuity of $t\mapsto 1_{[0,t]}$ in 𝓗 and commuting ⟨m,·⟩):
$$0=\langle m,1_{[0,t]}\rangle_\mathcal H = \int_0^1B_u^3\,\langle 1_{[0,u]},1_{[0,t]}\rangle\,du = \int_0^1B_u^3\,R_H(u,t)\,du.$$
✓ matches notes.

**Step 3 (Lemma A)** as above ⟹ on $E$, $B_u^3(\omega)\equiv0$ ⟹ $B\equiv0$ ⟹ $E\subseteq\{B_1=0\}$, $\mathbb P(E)\le\mathbb P(B_1=0)=0$ (since $B_1\sim N(0,1)$).

**Step 4 (BH criterion)** ⟹ law of Z is AC. ∎

Now — citations. The Bouleau–Hirsch criterion in the Gaussian-process/fBm setting. Standard references:
- Bouleau & Hirsch (1991) "Dirichlet Forms and Analysis on the Wiener Space".
- Nualart (2006) "The Malliavin Calculus and Related Topics", 2nd ed.: Proposition 2.1.? hmm — I recall: **Proposition 2.1.3**? The observer's notes say "Nualart 2006 二版 Thm 2.1.3". Hmm, in Nualart 2nd ed., §2.1.2 "absolute continuity": Proposition 2.1.3 states: "Let F ∈ 𝔻^{1,2}. Then the law of F is absolutely continuous w.r.t. Lebesgue measure iff... " hmm no. Let me recall: There's the result: **Prop 2.1.3** hmm I genuinely am unsure between Prop 2.1.3 and Thm 2.1.3; the notes say Thm 2.1.3. I'll cite it as "Nualart (2006), Theorem 2.1.3 (Bouleau–Hirsch criterion)" hmm — risk: if it's actually Prop 2.1.3. Hmm. I remember clearly that in Nualart 2nd edition, Section 2.1.2 contains:
- Proposition 2.1.1 (density via integration by parts / divergence)
- Proposition 2.1.2 (?)
- Theorem 2.1.3: "The law of F is absolutely continuous provided F∈𝔻^{1,p}, p>1, and P(‖DF‖>0)>0." — I believe THIS is right: Thm 2.1.3 requires p>1 and P(‖DF‖>0)>0 (positive probability, not necessarily 1!), and gives AC of the regular part... Actually I recall: Theorem 2.1.3: "Suppose F ∈ 𝔻^{1,2}. Then the measure µ ◦ F^{-1} decomposes as µ_a + µ_s with µ_s ⊥ Leb and µ_s supported on {‖DF‖=0}; in particular if P(‖DF‖>0)>0 then µ has AC component; if =1 then AC." Something like: "P{‖DF‖>0}>0 implies the law has an absolutely continuous component"? Hmm. The precise statement I'm fairly confident about: Nualart 2006, Theorem 2.1.3: "If F ∈ 𝔻^{1,p} for some p ≥ 1 and P[‖DF‖_{H} > 0] > 0, then the law of F has an absolutely continuous component." And Corollary/if P=1: law is AC. Hmm, alternatively there's Prop 2.1.3?? 

Since I cannot browse (well — CAN I search? The instructions say 禁止搜索题目文本本身 — searching for the exact theorem NUMBER in Nualart's book is not searching the problem text; it's verifying a reference. The constraint: "禁止搜索题目文本本身。若接触相关内容须声明。" Searching for "Nualart Theorem 2.1.3 Bouleau Hirsch criterion" is about the TOOL/reference, not the problem text. I think that's allowed and prudent. But hmm, do I have web access tools here? I have webfetch. The AGENTS.md provides curl-based search. Given 最高指示第一条 requires verifying technical decisions via search... but the core math is already settled; the only external fact is the citation. I could do a quick search to pin the exact numbering. Let me try webfetch on some source. Actually, let me be careful about time/token budget. The key deliverable is the proof. I can cite conservatively: "Nualart, *The Malliavin Calculus and Related Topics*, 2nd ed., Theorem 2.1.3" — hmm, but if wrong it's embarrassing. Alternative: cite BOTH the original BH monograph and state the criterion precisely, citing "see e.g. Nualart 2006, §2.1.2". That's safe regardless of exact numbering. I'll do a quick search attempt to confirm; if inconclusive, use §2.1.2-style citation.

Actually, let me plan the formal verification FIRST (required!), then write proof.md, then run verifications, then finalize.

## Formalization/verification plan (MANDATORY per instructions)

The instruction: the WHOLE solution chain must be checked by formal means; mark in proof.md which steps are machine-verified. Components:

1. **Sympy symbolic checks**:
   a. Covariance expansion: $\langle 1_{[0,u]},1_{[0,t]}\rangle = R_H(u,t) = \frac12(u^{2H}+t^{2H}−|u−t|^{2H})$ — verify $\mathbb E[B_sB_t]$ formula consistency: check that $R_H(s,t)$ defined thus satisfies positive-definiteness (numerically, eigenvalues of discretized kernel ≥ 0) and matches known cases (H=1/2: min(s,t) ✓ symbolic).
   b. Potential-equation expansion: from $U_g\equiv0$ to $\mathcal V(t)=C'+At^{2H}$ — pure algebra, trivial, but include as symbolic manipulation sanity check.
   c. Energy identity: for several concrete $g$ (polynomials on [0,1]): verify numerically/symbolically that IF $\mathcal V(t) = At^\beta + C$ held then $\mathcal E = 2AC$ — this is trivial algebra; better: verify the IDENTITY $\mathcal E_\beta(g) - [\int g(t)\mathcal V_g(t)dt] = 0$ definitionally, AND verify for candidate counterexample searches that no nonzero g solves potential eq.
   d. Verify $C = \int t^\beta g$ automatic from t=0 substitution (trivial).
   e. Laplace representation constant: numerically verify $\int_0^\infty(1-\cos y)y^{-1-\beta}dy = \frac{\pi}{2\Gamma(1+\beta)\sin(\pi\beta/2)}$ for several β via high-precision quadrature (mpmath), AND verify $c_\beta'$ formula reproduces $|x|^\beta$ at sample points.
   f. Symbolic verification that $\hat g(\xi) = O(\xi)$ as ξ→0 when A=0, ensuring integrability (sympy series).

2. **Nullspace search (numerical)**: Discretize operator $T: g \mapsto \mathcal V(t) − At^\beta − C$ on fine grid, build matrix M (rows: grid points t_i; columns: g values at u_j) augmented to enforce the two constraints; find smallest singular values / nullspace dim via SVD. Expect: nullspace ≈ {0} up to numerical noise, for various β = 2H ∈ {0.2, 0.5, 0.9, 1.0, 1.3, 1.7}. This validates Lemma A globally (no missed branches).

3. **Random polynomial search**: solve constrained LSQ: minimize ‖Kg − At^β − C‖ over (g,A,C) with ‖g‖_∞≤1 normalization; check min ≈ 0 only for g≈0.

4. **Verify the Malliavin-convention consistency**: BM special case H=1/2: $D_sZ = 4\int_s^1B_t^3dt$ — matches textbook ✓ (analytical remark, plus Monte-Carlo sanity: simulate BM paths, compute empirical variance of Z... not needed for density existence; skip heavy MC; maybe quick check that $\mathbb E[Z] = \int \mathbb E B_t^4 = 3\int t^2 dt = 1$ for H=1/2 and $\mathbb E[Z]=3\int t^{4H} = \frac{3}{4H+1}$ generally — numeric check trivially).

5. **Check the blow-up arguments numerically?** They're analytic; formal check: plot/verify that for β<1, $t^{\beta-1}$ unbounded — trivial. Skip.

6. **End-to-end Monte Carlo validation of the CONCLUSION** (density existence is qualitative; but we can validate the mechanism): simulate fBm paths (Cholesky), compute Z samples, histogram — shows spread (consistent with continuous density); more meaningfully, verify $P(\|DZ\|=0)$ empirically = 0: compute $\|DZ\|^2_{\mathcal H} = 16\iint B_s^3B_t^3R_H(s,t)dsdt$ on simulated paths, check >0 always. This directly tests the KEY claim $P(E)=0$. DO IT for several H including edge values. 

7. Optionally Lean: too heavy for this session; Python coverage suffices given the mandate lists options ("包括但不限于").

Also verify the claim $P(B\equiv0)=0$: $E⊆\{B_1=0\}$, $B_1~N(0,1)$ ✓ analytic.

One more mathematical detail to nail down: **Step 1 chain rule / D^{1,p} regularity details**:

We need: (a) $B_t\in\mathbb D^{1,q}$ ∀ q, with $D_\rho B_t = 1_{[0,t]}$; (b) $B_t^4\in\mathbb D^{1,q}$ with $D_\rho B_t^4 = 4B_t^3 1_{[0,t]}$ (chain rule; $x^4$ is C¹ with polynomial growth — the chain rule in Nualart Prop 3.2.7 hmm requires φ ∈ C¹ with bounded φ′; for polynomials use localization or the standard extension: if F∈𝔻^{1,q}∩L^∞... $B_t^4\notin L^\infty$. Standard workaround: truncate $x^4\wedge n$... Actually the cleanest standard fact: 𝔻^{1,p} contains all smooth cylindrical functionals; for $F\in\mathbb D^{1,p}$ and φ∈C¹ with φ′ of at most polynomial growth (or φ Lipschitz), φ(F)∈𝔻^{1,p} with Dφ(F)=φ′(F)DF — TRUE, standard (can cite Nualart Prop 3.2.7 + remark, or prove by approximation: φ_n = smooth truncation, pass limits using φ_n(F)→φ(F) in L^p and φ_n′(F)DF→φ′(F)DF in L^p by polynomial growth + moment bounds). I'll include a short lemma with proof-by-approximation sketch. Actually for FULL rigor I'll write it out: 

**Lemma (chain rule for polynomial growth).** If $F\in\mathbb D^{1,p}$ and $\varphi\in C^1(\mathbb R)$ with $|\varphi(x)|+|\varphi'(x)|\le K(1+|x|^r)$, then $\varphi(F)\in\mathbb D^{1,p}$ and $D\varphi(F)=\varphi'(F)DF$. Proof: take $\eta\in C_c^\infty$, $\eta\equiv1$ on [−1,1], $\varphi_n = \eta(\cdot/n)(\varphi\ast\rho_{1/n})$ hmm — smoother: $\varphi_n := \varphi\chi_n$ where χ_n smooth cutoff equal to 1 on [−n,n]: φ_n∈C¹_b, φ_n→φ pointwise, φ_n′→φ′ pointwise, with |φ_n|+|φ_n′| ≤ C(1+|x|^r) uniform in n (needs care: φ_n′ = φ′χ_n + φχ_n′; χ_n′ supported on annulus n≤|x|≤2n, |χ_n′| ≤ C/n, and |φ(x)|χ_n′(x)/n ≤ C(1+n^r)/n·1_{n≤|x|≤2n} ≤ C|x|^{r−1}·... hmm r≥1 needed; for r=3 (φ=x⁴, φ′=4x³): |φ(x)|/n ≤ C n³·1_{annulus}... |x|^{r}·1_{|x|≥n}/n = |x|^{r-1}·(|x|/n) ≤ 2|x|^{r-1}·... fine ≤ C(1+|x|^{r-1})·hmm |x|^{r-1}·1_{|x|≥n} ≤ (1+|x|^r)/1 ok whatever: |φχ_n′| ≤ sup|χ_n′|·|φ|·1_annulus ≤ (C/n)·C(1+|x|^r)·1_{|x|≥n} ≤ C'|x|^{r-1}1_{|x|≥n} ≤ C''(1+|x|^{r-1}) ≤ C'''(1+|x|^r). ✓ uniform domination.) Then φ_n(F)→φ(F) in L^p (poly growth + F∈L^p... need φ_n(F)→φ(F) dominated: ✓ by uniform poly growth), Dφ_n(F)=φ_n′(F)DF→φ′(F)DF in L^p(Ω;𝓗) ✓. Since D closed in 𝔻^{1,p} ✓. ∎ 

(c) $Z = \int_0^1 B_t^4\,dt \in \mathbb D^{1,p}$ with $D_\rho Z = \int_0^1 D_\rho B_t^4\,dt$: need the theorem "differentiation commutes with Lebesgue integration": if $u:[0,1]\times\Omega\to\mathbb R$ measurable, $u_t\in\mathbb D^{1,p}$, $\mathbb E\int|u_t|^p dt<∞$ and $\mathbb E\int\|Du_t\|^p_{\mathcal H}dt<∞$ hmm plus existence of suitable versions — then $\int u_tdt\in\mathbb D^{1,p}$ and $D\int u = \int Du_t\,dt$ (Bochner/Riemann). Standard (Nualart Prop 3.2.8? hmm — I think there's such a statement around Prop 3.2.8/Exercise; in fBm chapter it's used freely). Conditions: $\mathbb E\int_0^1|B_t^4|^pdt = \int\mathbb E|B_t|^{4p} \le C_p\int t^{4pH}<∞$ ✓; $\mathbb E\int_0^1\|D B_t^4\|^p_{\mathcal H}dt = \int 4^p t^{Hp}\mathbb E|B_t|^{3p}dt \le C\int t^{Hp(1+3H)}dt<∞$ ✓. And measurability/versions: $D_\rho B_t = 1_{\rho\le t}$ is product-measurable ✓, $D_\rho(B_t^4)$ jointly measurable ✓. Fine — cite as standard (Nualart 2006, cf. proof technique of Prop 3.2.8 / Section 3.2; or Alos–Mazet–Nualart). I'll state it as a quoted standard fact with precise hypotheses verified inline.

Hmm — actually, I want to double-check the exact statement in Nualart 2nd ed: I'm fairly sure **Proposition 3.2.8** hmm... I really can't be 100% sure of numbers. Strategy: cite with descriptive titles + book sections rather than betting on exact proposition numbers where uncertain, EXCEPT the ones I'm confident about:
- Nualart 2006, Theorem 2.1.3: I'm ~85% confident this is the BH absolute-continuity criterion ("If F∈𝔻^{1,p}, p>1... hmm or 𝔻^{1,2}"). Hmm. Honestly, let me just try to verify via web search quickly — allowed since it's not the problem text. If no access, cite "§2.1.2".

Let me also double check the fBm Malliavin derivative convention citation: Nualart Ch.5 §5.2: "Proposition 5.2.1: Assume H>1/2... B^{1/2,...}" hmm no. The general facts: $D_sB_t = 1_{[0,t]}(s)$ appears in Nualart 2nd ed. §5.2.1 (Equation (5.2.x)). Again cite descriptively.

OK here's another thought — maybe I should ALSO provide an alternative self-contained proof of the BH criterion usage? The notes explicitly warn: DO NOT attempt to reprove BH (that's what starved round 3). Just cite. ✓ Will cite.

Now, let me also double-check Step "event reduction" details once more:

$m = \int_0^1B_u^3\,1_{[0,u]}\,du$ — Bochner integral in $\mathcal H$: need $B_u^3 1_{[0,u]}$ Bochner-integrable: $\int_0^1\|B_u^3\,1_{[0,u]}\|_\mathcal H du = \int|B_u|^3u^Hdu$ finite a.s.? $\int_0^1|B_u|^3u^Hdu \le \sup|B|^3\cdot\int u^H < ∞$ ✓ a.s. (continuous paths). And the map $u\mapsto B_u^3\,1_{[0,u]}$ is a.s. continuous into 𝓗: $\|(B_u^3 1_{[0,u]}) - (B_v^3 1_{[0,v]})\| \le |B_u^3−B_v^3|\,v^H + |B_u|^3\|1_{[0,u]}−1_{[0,v]}\|$ → 0 by continuity of B and $\|1_{[0,u]}−1_{[0,v]}\|^2 = |u−v|^{2H}$ ✓. So m well-defined a.s. ✓. And $D_\rho Z = 4m$ — from differentiating under the integral ✓ (same integrability conditions as above, in 𝓗-norm).

Event: $E = \{‖DZ‖_{𝓗}=0\} = \{m=0\}$ ✓ (scalar factor 16 irrelevant).

Commuting ⟨·,·⟩ with Bochner integral: for each $t$: $\langle m,1_{[0,t]}\rangle = \int_0^1B_u^3\langle1_{[0,u]},1_{[0,t]}\rangle du = \int_0^1B_u^3R_H(u,t)du$ ✓ (linear functional applied to Bochner integral = integral of scalar function ✓).

On E: $\int_0^1 B_u^3 R_H(u,t)du = 0\ \forall t$ ✓. Expand:
$\int g(u)\frac12(u^{2H}+t^{2H}−|u−t|^{2H})du = 0$ ⟹ $\mathcal V_g(t) = \int g(u)|u−t|^{2H}du = \int g(u)u^{2H}du + t^{2H}\int g(u)du = C' + A t^{2H}$ ✓.

Lemma A (with β = 2H) ⟹ $g\equiv0$ on [0,1] ⟹ $B_u^3\equiv0$ ⟹ $B\equiv0$ (path continuous, $B_0=0$ anyway) ⟹ $ω∈E ⟹ B_1(ω)=0$ ⟹ $\mathbb P(E) \le \mathbb P(B_1=0) = 0$ ✓.

BH ⟹ Z AC ✓.

Also should double check: does BH criterion need $Z\in\mathbb D^{1,2}$ only, with $P(‖DZ‖>0)=1$? Yes: Nualart Thm 2.1.3 (2nd ed): "Let $F\in\mathbb D^{1,2}$ be such that $P(\|DF\|_\mathcal H>0)>0$..." hmm the version I want: if P(‖DF‖>0)=1 then law AC. I'm confident SOME standard statement gives: {law of F} = AC + singular part carried by {‖DF‖=0}. So P=1 ⟹ fully AC. ✓.

Hmm, one subtle point: in the fBm literature the criterion is often written with the norm $\|DF\|^2_{\mathcal H} = \int_0^T\|D_\theta F\|^2_{\mathcal H}d\theta$ (because DF ∈ L²(Ω×[0,T];𝓗)). Event {∫‖D_θF‖²dθ=0} = ∩{D_θF=0} ✓ same thing. ✓.

Now — additional rigor check on Lemma A Step "differentiate the potential equation":

Case β∈(1,2), claim: $\mathcal V\in C^2([0,1])$ and $\mathcal V''(t) = \beta(\beta−1)\int_0^1|t−u|^{\beta−2}g(u)du$.
- First derivative: $\mathcal V'(t) = \beta\int_0^1\mathrm{sgn}(t−u)|t−u|^{\beta−1}g(u)du$ — exists everywhere, continuous (kernel $|t−u|^{\beta−1}$, exponent ∈(0,1), bounded by... $\sup_t\int_0^1|t−u|^{\beta−1}du \le 2\max(1,\frac{1}{\beta})$-ish finite ✓; dominated conv for continuity ✓). Also need: $\mathcal V$ is the integral of $\mathcal V'$: $\int_a^b\mathcal V'(s)ds = \mathcal V(b)−\mathcal V(a)$ — by Fubini: $\int_a^b\beta\,\mathrm{sgn}(s−u)|s−u|^{\beta−1}ds = |b−u|^\beta−|a−u|^\beta$ ✓ (check both sides u<a, u∈[a,b], u>b ✓). So $\mathcal V(b)−\mathcal V(a) = \int_a^b\mathcal V'(s)ds$ ✓ FTC valid.
- Second: similarly with kernel exponent β−2∈(−1,0): integrable, $\mathcal V''$ continuous, $\mathcal V'(b)−\mathcal V'(a) = \int_a^b\mathcal V''$ ✓.
- RHS $At^\beta + C$ is $C^\infty$ on $(0,1]$, so for $t\in(0,1]$: $\beta(\beta−1)\int|t−u|^{\beta−2}g = A\beta(\beta−1)t^{\beta−2}$; divide β(β−1)≠0: $\int_0^1|t−u|^{\beta−2}g(u)du = A\,t^{\beta−2}$ for $t\in(0,1]$.
- LHS bounded on (0,1]: $|\int|t−u|^{\beta−2}g| ≤ ‖g‖_∞\int_0^1|t−u|^{\beta−2}du ≤ ‖g‖_∞\cdot\frac{2}{\beta−1}$ ✓ (compute: $\int_0^t(t−u)^{\beta−2}du = \frac{t^{\beta−1}}{\beta−1} \le \frac1{\beta−1}$; $\int_t^1(u−t)^{\beta−2}du = \frac{(1−t)^{\beta−1}}{\beta−1} \le \frac1{\beta−1}$ ✓).
- RHS: $|A|t^{\beta−2}\to∞$ as $t↓0$ if A≠0 (β−2∈(−1,0)) ⟹ A=0 ✓.

Case β∈(0,1): $\mathcal V\in C^1$, $\mathcal V'(t) = \beta\int\mathrm{sgn}(t−u)|t−u|^{\beta−1}g$, LHS bounded: $|\mathcal V'(t)| ≤ β‖g‖_∞\int_0^1|t−u|^{\beta−1}du ≤ β‖g‖_∞\cdot\frac{2}{\beta} = 2‖g‖_∞$ ✓. Equation: $\mathcal V'(t) = A\beta t^{\beta−1}$ on (0,1] (both sides C¹... wait need RHS differentiable: $At^\beta$ C¹ on (0,1] ✓, and $\mathcal V$ C¹ ✓, so differentiate the IDENTITY: $\mathcal V'(t) = A\beta t^{\beta−1}$ ✓). Blow-up ⟹ A=0 ✓.

Case β=1: $\mathcal V(t) = \int_0^1|t−u|g(u)du = \int_0^t(t−u)g+\int_t^1(u−t)g$. $\mathcal V'(t) = \int_0^tg−\int_t^1g$ (valid, kernel Lipschitz) and equation $\mathcal V'(t) = A$ ∀t. Differentiate: $2g(t)=0$ ∀t ✓ DONE (even stronger).

All good. Note for β=1 we never needed A=0 — direct finish.

Hmm wait, in case β∈(0,1): I should double-check $\mathcal V'$ formula validity at ALL t including where... kernel $\mathrm{sgn}(t−u)|t−u|^{\beta−1}$ is integrable in u uniformly ✓ and the identity $\mathcal V(t)−\mathcal V(0) = \int_0^t\mathcal V'(s)ds$ holds by Fubini ✓ ⟹ $\mathcal V\in C^1$ with derivative $\mathcal V'$ ✓ (continuity shown). ✓.

And in the application, is $g$ continuous? $g(u) = B_u^3(\omega)$ — yes, continuous paths ✓. ‖g‖_∞ < ∞ a.s. ✓.

NOW — one more consideration: the notes mention Step 1 concluded "A = 0 for all β∈(0,2)" — matches ✓. And they used a longer ladder; mine is shorter (one/two derivatives max). My simplification is sound; I derived it fresh and verified. Good — but let me double-check against possible subtlety: for β∈(0,1), is it legitimate to differentiate the identity $\mathcal V(t) = At^\beta + C$ at points $t\in(0,1]$? $\mathcal V$ is C¹ on ALL of [0,1] (shown); $t\mapsto At^\beta+C$ is C¹ on (0,1]; identity holds on [0,1] hence on (0,1]; differentiating: $\mathcal V'(t) = A\beta t^{\beta−1}$ for t∈(0,1] ✓ legit.

Edge: β∈(0,1): as t→0⁺, LHS → 𝒱′(0) = β∫sgn(−u)u^{β−1}g(u)du = −β∫₀¹u^{β−1}g(u)du, finite ✓; RHS: Aβt^{β−1} diverges unless A=0 ✓.

PERFECT. Lemma A fully rigorous and SIMPLE. 

Now Step 2–3 (energy + Fourier) — restate cleanly:

Given A=0 (cases β≠1) — wait, for β=1 we're already done, so Steps 2–3 only needed for β≠1, where A=0 established.

Multiply potential identity by g, integrate: $\mathcal E_\beta(g) := \iint_{[0,1]^2}g(s)g(t)|s−t|^\beta dsdt = A\int t^\beta g(t)dt + C\int g = AC + CA = 2AC = 0$.

Fourier: for zero-mean g (A=0): $\mathcal E_\beta(g) = −\frac{\Gamma(1+\beta)\sin(\pi\beta/2)}{\pi}\int_\mathbb R\frac{|\hat g(\xi)|^2}{|\xi|^{1+\beta}}d\xi = 0$.

⟹ $|\hat g(\xi)|^2|\xi|^{−1−\beta} = 0$ a.e. ξ (nonneg integrand, zero integral) ⟹ $\hat g(\xi)=0$ a.e. ⟹ everywhere (ĝ continuous) ⟹ g≡0 (uniqueness of Fourier transform on e.g. L¹/Schwartz distributions — g∈C[0,1]⊂L¹, extend by 0 to ℝ; injectivity of FT on L¹ ✓).

∎ Lemma A.

Constants: $c_\beta' := \frac{\Gamma(1+\beta)\sin(\pi\beta/2)}{\pi}$ — VERIFY NUMERICALLY.

Hmm, also double check the sign convention: $|x|^\beta = c_\beta'\int_\mathbb R(1−\cos(\xi x))|\xi|^{−1−\beta}d\xi$ with $c_\beta' = \frac{\Gamma(1+\beta)\sin(\pi\beta/2)}{\pi}$. Test β=1: $c_1' = \frac{\Gamma(2)\sin(\pi/2)}{\pi} = \frac1\pi$; known: $\int_\mathbb R(1−\cos(\xi x))/\xi^2 d\xi = \pi|x|$ ✓ ⟹ $|x| = \frac1\pi\cdot\pi|x|$ ✓✓.

Test β→0⁺... skip, numerical check will do.

So $\mathcal E_\beta(g) = c_\beta'\int|\xi|^{−1−\beta}[A^2 − |\hat g(\xi)|^2]d\xi$ (general A, when convergent), and with A=0: $\mathcal E = −c_\beta'\int|\xi|^{−1−\beta}|\hat g|^2 \le 0$, =0 iff ĝ≡0 ✓.

Also worth noting the connection: this is exactly "strict conditional negative definiteness of $|x|^\beta$" ✓ consistent with round-1's observation.

NOW, the remaining pieces to verify/cite for the main theorem:

(A) fBm basics: continuous modification exists ∀H∈(0,1) ✓ standard (Kolmogorov: $\mathbb E|B_t−B_s|^q ≤ C_q|t−s|^{qH}$, take q>1/H). $B_1\sim N(0,1)$ ✓ ($\mathbb EB_1^2 = R_H(1,1) = 1$ ✓ — CHECK: $\frac12(1+1−0)=1$ ✓).

(B) Malliavin machinery in fBm setting — cite Nualart ch.5 setup + ch.2–3 general theory.

(C) BH criterion — cite.

(D) Lemma A — proved above, machine-verifiable components.

Potential objection someone might raise: **is $\mathbb D^{1,p}$ chain rule applicable with $u_t = B_t^4$ needing JOINT measurability of $(ρ,t)↦D_ρB_t^4$?** $D_ρB_t^4 = 4B_t^3 1_{ρ≤t}$ jointly measurable ✓.

Another potential gap: the theorem "differentiation under Lebesgue integral" — precise hypotheses in Nualart: Proposition (Nualart 2006, Prop 3.2.8?? hmm). I recall EXACTLY this kind of statement: "If $u = \{u_t, t∈[0,1]\}$ is measurable, $u_t∈𝔻^{1,p}$, and $\mathbb E[\int_0^1|u_t|^pdt] + \mathbb E[\int_0^1\|Du_t\|^p dt] < ∞$, then $F = \int_0^1u_tdt ∈ 𝔻^{1,p}$ and $D_tF = \int_0^1D_su_t\,dt$." — hmm, I believe this might require additionally that $Du$ has a jointly measurable version. It's standard; I'll cite as "cf. Nualart 2006, Proposition 3.2.8" hmm... risk. ALTERNATIVELY, avoid citing: prove it directly via mollification of the integrand? That's work. OR use a slicker route: 

Slicker: $Z = \int_0^1B_t^4dt$. Approximate by Riemann sums $Z_N = \frac1N\sum B_{t_i}^4 ∈ 𝔻^{1,p}$ with $D_ρZ_N = \frac1N\sum 4B_{t_i}^3 1_{ρ≤t_i}$. Show $Z_N→Z$ in $L^p$ ✓ (continuity) and $DZ_N → $ candidate in $L^p(Ω×[0,1];𝓗)$: $\|D_ρZ_N − 4\int_0^1B_t^3 1_{[0,t]}dt\|_𝓗 = \|\frac1N\sum 4B_{t_i}^3 1_{[0,t_i]} − \int 4B_t^3 1_{[0,t]}dt\|_𝓗$ → 0 a.s. (Bochner-Riemann sums, integrand a.s. continuous into 𝓗 ✓ shown earlier!) and dominated in L^p: $\|\cdot\|_𝓗 ≤ \frac1N\sum 4|B_{t_i}|^3 t_i^H + \int 4|B_t|^3t^Hdt$, $\mathbb E(\sup\text{-ish})^p$: bound by $(4\sup_t|B_t|^3\int_0^1t^Hdt)^p$, $\mathbb E\sup|B|^3 < ∞$ ✓ (continuous Gaussian). DCT in L^p(Ω;𝓗) after integrating over ρ (note: independent of ρ, so $\mathbb E\int_0^1\|·\|^pdρ$ same) ✓. Closedness of D ⟹ $Z∈𝔻^{1,p}$ with $D_ρZ = 4m$ ∀ρ ✓. 

This avoids needing the general theorem — SELF-CONTAINED, only uses: (i) D closed (standard property of 𝔻^{1,p}, Nualart Prop 3.2.?-ish but very basic), (ii) chain rule for $x^4$ applied to $B_{t_i}$ (standard, provable via the polynomial-growth chain rule lemma I sketched), (iii) moment bounds. I'll present this Riemann-sum argument — it's clean and reduces citation load to: definition of 𝔻^{1,p}, closedness of D, chain rule, BH criterion. 

Similarly the chain rule for polynomials: $B_t∈𝔻^{1,p}$ with $D_ρB_t = 1_{ρ≤t}$ — for Gaussian W(h): $D(W(h)) = h$ DEFINITIONAL (𝔻^{1,2} contains W(h) ✓); $B_t = W(1_{[0,t]})$ ✓ so $D_ρB_t = 1_{[0,t]}$ ✓ definitional. Chain rule $x↦x^4$: via the polynomial-growth lemma (prove it: approximation argument, ~10 lines) — include as Lemma 2 with short proof. ✓ Self-contained modulo basics.

Moment computations:
- $\mathbb E|B_t|^q = t^{qH}\mathbb E|B_1|^q = t^{qH}\mathbb E|N(0,1)|^q = C_qt^{qH}$ ✓.
- Fernikesque for sup: $\mathbb E[\sup_{t∈[0,1]}|B_t|^q] ≤ C_q$ — standard (Dudley/Borell; or elementary: sup ≤ ... use $\mathbb E\sup ≤ K\int_0^1\sqrt{\log(1/t^H)}... $ whatever, standard fact, cite Fernique or Borell; simplest: Fernique ⟹ $\sup_t|B_t|$ has all exponential moments ✓ cite Fernique's theorem).

Everything solid. Let me also prepare the H=1/2 sanity: β=1 case handled inside Lemma A ✓ (gives g≡0 directly) — so no separate treatment needed; but mention BM-classical crosscheck $D_sZ = 4\int_s^1B_t^3dt$ ✓ consistent.

Hmm hold on, wait. Let me reconsider the claim $\|1_{[0,s]}−1_{[0,t]}\|^2_𝓗 = |s−t|^{2H}$. $\|1_{[0,s]}−1_{[0,t]}\|^2 = R(s,s)+R(t,t)−2R(s,t) = \frac12(s^{2H}+s^{2H}) +\frac12(t^{2H}+t^{2H}) −2·\frac12(s^{2H}+t^{2H}−|s−t|^{2H}) = |s−t|^{2H}$ ✓.

And $R_H(s,t)$ PSD ✓ (it's a covariance). Positive definiteness of the kernel on step functions: $\|\sum a_i1_{[0,t_i]}\|^2 = \sum a_ia_jR(t_i,t_j) = \mathbb E[W(\sum a_i1_{[0,t_i]})]^2 ≥ 0$ — well, 𝓗 is DEFINED as completion, so PSD by construction ✓; degenerate elements: $\|\sum a_i1_{[0,t_i]}\|=0$ ⟹ the corresponding Gaussian combo has variance 0 — fine, that's why 𝓗-elements are equivalence classes; the FUNCTION representatives may coincide... The subtlety: distinct step-functions-in-L² can map to same 𝓗 class?? For fBm with H<1/2 hmm: known fact — the natural map L²→𝓗... For H ≥ 1/2: 𝓗 embeds... hmm honestly: the map from indicators to 𝓗 classes: is $1_{[0,s]}↦$ class injective as function of s? $\|1_{[0,s]}−1_{[0,t]}\|^2 = |s−t|^{2H} > 0$ for s≠t ✓ INJECTIVE in s ✓. That's all we need (the curve t↦1_{[0,t]} is continuous & non-degenerate) ✓. And ⟨m,1_{[0,t]}⟩ well-defined for m∈𝓗 ✓.

Do we ever need that 𝓗 elements are honest functions? NO — we only pair with $1_{[0,t]}$ ✓. 

One more check — **the Bochner-integral commutation**: $\langle m, 1_{[0,t]}\rangle_𝓗 = \int_0^1B_u^3\langle1_{[0,u]},1_{[0,t]}\rangle_𝓗 du$: since $φ_m: h↦\langle m,h\rangle$ continuous linear, $φ_m(\int f_u du) = \int φ_m(f_u)du$ ✓ (property of Bochner integral) ✓.

And $D_ρZ = 4m$: Riemann-sum argument ✓.

**Event reduction completeness**: $E = \{‖DZ‖=0\}$. $‖DZ‖^2 = \int_0^1‖D_ρZ‖^2dρ = 16‖m‖²$ ⟹ E={m=0} ✓. On E: ∀t: $\langle m,1_{[0,t]}\rangle=0$ ✓ ⟹ potential equation ✓.

So the FINAL LOGICAL CHAIN:
1. fBm def + basics (continuous paths, scaling, $B_1∼N(0,1)$).
2. 𝓗, isonormal W, $B_t=W(1_{[0,t]})$, 𝔻^{1,p} basics.
3. Lemma 2 (poly-growth chain rule) ⟹ $B_t^4∈𝔻^{1,p}$, $D_ρB_t^4 = 4B_t^3 1_{[0,t]}$.
4. Riemann-sum lemma ⟹ $Z∈𝔻^{1,p}$ ∀p, $D_ρZ = 4m$ with $m=\int_0^1B_t^3 1_{[0,t]}dt$ (Bochner).
5. Norm: $\|DZ\|² = 16‖m‖² = 16\iint B_s^3B_t^3R_H(s,t)dsdt$.
6. Reduction: on E={m=0}: ∀t: $\int_0^1B_u^3R_H(u,t)du=0$.
7. Expansion ⟹ potential equation $\mathcal V_g(t) = C'+At^{2H}$, $g=B^3$ continuous.
8. Lemma A ⟹ g≡0 ⟹ E⊆{B₁=0} ⟹ P(E)=0.
9. BH ⟹ law of Z AC. ∎

Machine verification plan mapping to chain:
- Step 5 formula: numerically verify on simulated paths that $\|m\|²_𝓗$ computed via double integral of R_H matches Gram-matrix computation ✓ (consistency of conventions).
- Step 6–7: symbolic/numeric trivial ✓.
- Step 8 (Lemma A): 
  - SVD nullspace test for various β ✓;
  - sympy: verify energy identity $2AC$ for trial functions SATISFYING nothing — hmm the energy identity is conditional. Instead: verify for MANY random continuous g that $\mathcal V_g(t) − At^\beta − C ≠ 0$ (i.e., no accidental solutions) — covered by SVD test;
  - verify Fourier constant via mpmath quadrature ✓;
  - verify the differentiated-equation claims: for random g, check numerically that $\mathcal V'(t)$ formula matches finite differences (validates the differentiation identities incl. coefficients β, β(β−1)) ✓;
  - verify blow-up: trivial analytic.
  - verify strict negative definiteness: for random ZERO-MEAN g: compute $\mathcal E_\beta(g) < 0$ ✓ and match against $−c_\beta'\int|\hat g|²|ξ|^{−1−β}dξ$ (numerical FT) ✓ — this validates Step 2+3 formula end-to-end!
- Step 9/conclusion: Monte Carlo: simulate fBm (several H), compute $Y = \|DZ\|²/16 = \iint B_s^3B_t^3R_H(s,t)$ per path; check Y>0 for ALL sampled paths (thousands) ✓; also check Z varies continuously (histogram) — supporting evidence for density.
- Cross-checks: $\mathbb E[Z] = 3/(4H+1)$ via MC ✓; BM case H=1/2 known results.

Also verify $R_H(u,t)$ expansion identity used in step 7 symbolically ✓ trivial.

Additionally, to be extra careful about the Fourier-representation Fubini subtleties, my proof will present Step 3 via the standard route with full justification as analyzed above (truncate, monotone/DCT). Machine check: numerical agreement of both sides for random zero-mean g ✓.

Alright — also the question asks "问 Z 是否有关于 Lebesgue 测度的密度" — answer: 是 (yes), for every H∈(0,1).

Extra flourish (optional, brief): the density is actually strictly positive? Not required. Skip. Maybe mention $Z>0$ a.s. and $\mathbb E Z = 3/(4H+1)$, and that density smoothness (C^∞? positivity?) could follow from higher-order criteria — NOT claimed, just remark? Better keep minimal claims. Maybe one remark: since $Z∈𝔻^{1,p}$∀p and ‖DZ‖>0 a.s., one gets density; smoothness would need more (e.g., $Z∈𝔻^{k,p}$∀k — plausible but not proven here; DON'T claim). Keep scope tight.

Language: The user prompt is Chinese; AGENTS.md demands 人话 style for user-facing text. proof.md — mathematical document; I'll write it in Chinese prose with LaTeX, clear narrative style (人话铁律 applies to explanations). The final chat response should be concise.

Plan of action:
1. Read 分析笔记.md ✓ (done).
2. Write working notes incrementally to 工作笔记.md as I go (requirement!). Start it now with the plan, append after each block.
3. Do the math (mostly done in head — capture in notes).
4. Run Python verifications (sympy/mpmath/numpy/MC).
5. Write proof.md with verification annotations.
6. Final boxed answer.

Let me also decide on git: directory — is it a repo? Env says "Is directory a git repo: no". AGENTS.md git protocol applies to repos; no repo here, so no commits (can't commit outside repo; initializing one wasn't requested). I'll note that. Actually the global rules say files changed should be committed... but no repo exists. Creating a repo proactively = surprising side effect; skip, mention nothing (or one line). The trajectory-based workflow (rounds/, .work_rN dirs) suggests parent dirs managed externally. Skip git.

Token budget consideration: be efficient. Write 工作笔记.md first (concise skeleton + key derivations), then run verification scripts, then proof.md.

Let me draft the verification script content mentally:

```python
# verify.py parts
import numpy as np
from mpmath import mp, quad, gamma, sin, pi, cos, inf, mpf

mp.dps = 30

# 1. Laplace constant check
def laplace_const(beta):
    # int_0^inf (1-cos y)/y^{1+beta} dy
    # split: [0, big] quadrature + tail asymptotic? integrand ~ 1/y^{1+beta} oscillatory...
    # use mpmath quadosc or split at zeros of cos
    ...
```

mpmath quadosc needs zeros; alternative: use known formula check via computing $\int_0^\infty(1−\cos y)y^{−1−β}dy$ with `quad` over [0,∞) using transformation... Simpler: verify the CONSTANT indirectly: pick β, x; compute $c_\beta'\int_{-M}^{M}(1−\cos(\xi x))|\xi|^{−1−β}dξ$ for large M and compare to $|x|^β$. Tail error: $\int_M^\infty 2|\xi|^{−1−β}dξ = \frac{2M^{−β}}{β}$ — controllable. Use scipy.integrate.quad on [0,M] ×2 (symmetry) with points. Good.

Even better/simpler: verify the ENERGY identity numerically end-to-end (which is what matters): for random zero-mean g on [0,1]:
- LHS: $\mathcal E_\beta(g) = \iint g(s)g(t)|s−t|^\beta$ (2D quad / matrix).
- RHS: $−c_\beta'\int|\hat g(ξ)|²|ξ|^{−1−β}dξ$ — compute ĝ by quadrature, integrate with tail control.
Match to high precision ⟹ validates constant + Fubini + sign simultaneously ✓.

- SVD nullspace test: grid n=400; K[i,j] = |t_i−u_j|^β; want: Kg = A·t^β + C·1. Matrix M = [K | −t^β | −1] ((n)×(n+2)); smallest singular values of M; expect σ_min ~ 0 only for trivial... hmm careful: (g,A,C)=(0,0,C) ANY C solves?? Kg − At^β − C·1 = −C·1 = 0 requires C=0. So nullspace should be {0}: expect σ_min distinctly positive relative to σ_max. Compare across β. ALSO: the TRUE theorem says nullspace = 0 in CONTINUOUS setting; discrete approx should show σ_min/σ_max ratio stable as n grows (not collapsing like 1/n^k). Report ratios for n = 100..800 few values. Note: for small β, kernel nearly singular (|s−t|^β ≈ 1 for most pairs) — σ_min may scale oddly; interpret carefully: augment with normalization ‖g‖=1 constraint: minimize ‖Kg−At^β−C‖ s.t. ‖g‖₂=1: compute smallest singular value of M restricted... eh — simpler: project out span{t^β, 1}: Let P = projector orthogonal to span{1, t^β} in ℝ^n (discrete L²). Solve: does there exist g with Pg = g (zero-mean-ish and orthogonal to t^β... hmm not exactly the right constraint: A and C free, so constraint is: ∃A,C: Kg = At^β+C1 ⟺ P(Kg) = 0 where P projects out span{1,t^β}. So look for g with PKg = 0, g≠0: nullspace of PK (n×n). Expect dim 0: smallest SV of PK positive & stable. ✓ DO THAT.

- MC fBm simulation: Cholesky of R_H on grid (n=256), 500 paths per H ∈ {0.3,0.5,0.7,0.9}; compute Z̄, Y=∬g⊗g R (matrix ops), check min Y > 0; report min/max. Also E[Z] check.

- Differentiation-identity check: for random smooth g (e.g., trig polynomial), numerically differentiate $\mathcal V_g(t)$ and compare with formulas β∫sgn|t−u|^{β−1}g and β(β−1)∫|t−u|^{β−2}g — validates the calculus lemmas' constants ✓.

- Sympy extras: verify $\mathcal E_\beta$ vs $2AC$ relationship can't be tested unconditionally; skip; but DO verify: for g solving NOTHING, identity $\int g(t)\mathcal V_g(t)dt = \mathcal E_\beta(g)$ (definitionally true — trivial, skip). Verify expansion $R_H$ ⟹ potential equation symbolically with sympy simplify ✓ cheap.

- Also verify claim $\|1_{[0,t]}\|² = t^{2H}$: from R ✓ trivial symbolic.

- Verify $\hat g(ξ) = O(ξ)$ for zero-mean: symbolic with sympy series for polynomial g ✓ cheap.

Edge scrutiny — anything the chain relies on that could secretly FAIL?

(i) For H<1/2, is $Z∈𝔻^{1,p}$ still fine? Yes — argument didn't use H>1/2 anywhere ✓. (Common pitfall in fBm papers: 𝔻^{1,2} ⊂ things differ by H, but basic chain rule universal ✓.)

(ii) BH criterion applicability in fBm setting: standard, used ubiquitously (e.g., in proving densities of fBm functionals). Citation fine.

(iii) The event reduction used pairing ONLY with $1_{[0,t]}$, t∈[0,1] — sufficient ✓.

(iv) Lemma A assumes g continuous ✓ (paths continuous).

(v) Subtle: $E$ defined via ‖DZ‖=0; BH needs P(‖DZ‖₊>0)=1 — we have P(E)=0 ✓.

(vi) Does the theorem need Z real-valued ✓ obviously.

(vii) H→edge cases: H∈(0,1) open — fine. H=1 excluded (not asked).

(viii) One more: in Lemma A case β∈(0,1), we used $\mathcal V∈C¹$ — requires g merely bounded/continuous ✓; and identity $\mathcal V(t)−\mathcal V(0)=\int_0^t\mathcal V'(s)ds$ via Fubini — kernel manipulations: $\int_0^t\int_0^1 β\,\mathrm{sgn}(s−u)|s−u|^{β−1}g(u)duds$; absolute integrability: $\int_0^t\int_0^1|s−u|^{β−1}|g(u)|duds ≤ ‖g‖_∞\int_0^1\int_0^1|s−u|^{β−1}dsdu = ‖g‖_∞\cdot\frac{2}{β(β+1)} < ∞$ ✓ Tonelli legit ✓.

(ix) Similarly β∈(1,2) second derivative Fubini: $\int\int|s−u|^{β−2}$: $= \frac{2}{(β−1)β}<∞$ ✓.

(x) The energy-identity multiplication: $\int_0^1 g(t)\mathcal V(t)dt = \int g(t)[At^\beta + C]dt$: both sides finite ✓ trivially.

(xi) Fourier side: g extended by 0 to ℝ, $\hat g$ entire ✓; integral convergence argued ✓; uniqueness of FT on L¹ ✓.

(xii) $c_\beta' > 0$ for β∈(0,2) ✓ (sin(πβ/2)>0).

All airtight. Also the notes ask patch (iii): constant $c_H$ formula — covered ✓.

Now let me ALSO reconcile with the notes' Step 2 formula "$\mathcal E_{2H}(g)=A(C+D)$, $D=C−2c$" — theirs came from $U_g\equiv c$ general form; ours from $U_g\equiv0$: $\mathcal V = C' + At^{2H}$, multiply: $\mathcal E = AC' + C'A = 2AC'$ ✓ same structure. ✓.

Write-up order in proof.md:
- Title, statement, answer.
- §0 Overview (route map).
- §1 Preliminaries: fBm, 𝓗, 𝔻 basics (with citations), needed facts F1–F5.
- §2 Regularity of Z & explicit derivative (Lemmas + proofs).
- §3 Non-degeneracy reduction (event E, potential equation).
- §4 Lemma A (deterministic) with three cases + energy + Fourier.
- §5 Conclusion via BH.
- §6 Formal verification report (what was checked by which script, results).
- §7 Remarks (H=1/2 classical consistency; what's NOT claimed—smoothness).
- Boxed answer.

Citations list:
- Nualart, D. (2006). The Malliavin Calculus and Related Topics, 2nd ed. Springer. [𝔻 definitions §2.2 hmm — actually §2.2? In 2nd ed: §2.1 isonormal + derivatives... Let me be careful: 2nd ed: Chapter 2: §2.1 (isonormal process, derivative operator, 𝔻^{1,p}), §2.1.2 absolute continuity (BH criterion Thm 2.1.3?), ... Chapter 5: §5.2 fBm.] I'll cite sections not exact prop numbers except Thm 2.1.3 which I'll flag as the BH criterion. Let me quickly try to verify Thm 2.1.3 via webfetch (allowed: tool verification, not problem text). Try fetching a source quoting it. E.g., search "Nualart" "Theorem 2.1.3" "absolutely continuous". Let me do that during execution (cheap, one fetch). Per 最高指示第一条, verifying the citation is due diligence. Also verify "Prop 5.2.1"-style derivative formula? Eh — one fetch attempt, else fall back to section-level citation.

- Bouleau, N., Hirsch, F. (1991). Dirichlet Forms and Analysis on the Wiener Space. de Gruyter.
- Fernique / standard Gaussian facts — can cite generically.
- Hu, Y., Nualart, D. (2005) "Hermite criteria..." hmm the relevant: Hu–Nualart, "Some nonlinear stochastic integral..." Actually the known related result: for H>1/2? There's a paper by Hu & Nualart: "Renormalized self-intersection local time..." The relevant known result: density of $\int_0^T B_t^p dt$ hmm — I recall a paper: "Density of double integrals..." eh. There IS a known result that $\int_0^T u_s dB_s$ etc. For our purpose optional; mention only if certain. SKIP optional lit.

Let me also double-check the BH criterion statement form I'll rely on:

**BH criterion (as cited)**: Let $F\in\mathbb D^{1,2}$ (real). Decompose law: $\mu\circ F^{−1} = \mu_{ac} + \mu_s$ w.r.t. Lebesgue with $\mu_s(\mathbb R\setminus N)=0$-ish supported on critical set... The usable corollary: **if $\mathbb P(\|DF\|_\mathcal H>0)=1$ then $F$ has a density.** This is definitely a standard corollary (often quoted as "Bouleau–Hirsch criterion"). ✓.

Alright — also I want to double check the claim "$D_ρZ$ is the same for all ρ" doesn't break the DEFINITION of the Malliavin norm in the fBm chapter: In Nualart's fBm chapter, for $F∈𝔻^{1,2}$, one writes $\|DF\|^2_\mathcal H := \int_0^1\|D_θF\|^2_\mathcal H dθ$. Hmm wait — actually now I doubt: in Ch.5 he often uses the operator δ and the pseudo-norm $\|DF\|_\mathcal H$ treating DF as function of θ valued in 𝓗... The BH-type result in fBm context (used e.g. in Alos–Mazet–Nualart 2000, or in Nualart's survey "Malliavin calculus and stochastic integral representation of fractional Brownian motion"): Theorem: if $F∈𝔻^{1,2}$ and $\mathbb P(\int_0^T\|D_θF\|^2_\mathcal H dθ > 0) = 1$ hmm... OR some treatments use the derivative $D F$ as element of $L^2([0,T];\mathcal H)$ and the criterion on its norm. Either way OUR object: $D_θZ = 4m$ ∀θ ⟹ $\int_0^1\|D_θZ\|²dθ = 16‖m‖²$ ✓ and the event is the same either convention ✓. In proof.md I'll define $\|DZ\|^2_{\mathcal L^{inv}} := \int_0^1\|D_θZ\|^2_\mathcal H dθ$ explicitly to dodge convention ambiguity. ✓.

Hmm, hmm — actually WAIT. Now I need to double-check the chain rule in the fBm convention: $D_θB_t = 1_{[0,t]}(θ)$ — as an element of 𝓗 in the θ-variable. Then $D_θ(B_t^4) = 4B_t^3 1_{[0,t]}$ ✓. Then $D_θZ = \int_0^1 4B_t^3 1_{[0,t]} dt$ — Bochner in 𝓗 ✓ INDEPENDENT of θ ✓. Then $\|D_θZ\|_\mathcal H = 4‖m‖$ ∀θ ✓. Great consistent.

But CAREFUL: is it true that for fBm, $B_t = W(1_{[0,t]})$ with the SAME 𝓗-inner product $R_H$? YES by construction (𝓗 defined via covariance; isonormal W extends the map $1_{[0,t]}↦B_t$; well-defined since $\langle1_{[0,s]},1_{[0,t]}\rangle = R_H(s,t) = \mathbb E[B_sB_t]$ ✓).

Definition of derivative: $D$ is the closure of $\varphi(W(h_1),…)\mapsto\sum\partial_i\varphi\,h_i$. For $F=W(h)$: $DF = h$ (𝓗-valued, no θ-dependence!). AH WAIT — in the GENERAL isonormal setting, $DF ∈ L²(Ω;𝓗)$ — there's no θ slot at all! The "D_θF" notation with θ-slot appears only in the WIENER-space convention where 𝓗=L²[0,T]. In the fBm/abstract convention: $DF = $ single 𝓗-element. Then $D(B_t) = 1_{[0,t]}$ (one element, no θ). $D(B_t^4) = 4B_t^3\cdot 1_{[0,t]}$ ✓. $DZ = \int_0^1 4B_t^3\cdot1_{[0,t]}\,dt = 4m$ — SINGLE 𝓗-element ✓✓. And $\|DZ\|_\mathcal H = 4‖m‖$ ✓. CLEANER — no θ-slot ambiguity at all! The notes' convention matches this (they say "作为 𝓗 元素 DZ=4m"). ✓✓ 

So in the abstract-isonormal convention: $D_sB_t$ notation in notes = "$\langle DB_t\rangle$ evaluated..." hmm whatever — the clean presentation: $DF∈𝓗$; $DB_t = 1_{[0,t]}$; $DZ = 4m$. The "D_sB_t = 1_{s≤t}" is the coordinate representation pairing with $1_{[0,s]}$: $\langle DB_t, 1_{[0,s]}\rangle_𝓗 = R_H(s,t) = \mathbb E[B_sB_t]$... and the BM-limit check: for H=1/2, 𝓗≅L²[0,1] hmm: for BM, $\langle f,g\rangle_{𝓗} = \int fg$; $DB_t = 1_{[0,t]}$ as L²-function ✓; $DZ = 4m$, $m(s) = \int_s^1B_t^3dt$ ✓ matches classical $D_sZ$ ✓✓. 

So final convention in proof.md: abstract isonormal; $DZ = 4m ∈ 𝓗$; norm $‖m‖²_𝓗 = \iint B_s^3B_t^3R_H(s,t)dsdt$ ✓; BH criterion: $F∈𝔻^{1,2}$, $\mathbb P(‖DF‖_𝓗>0)=1$ ⟹ AC ✓ (exact form of Nualart Thm 2.1.3 corollary / BH).

This also resolves the notes' line-26 typo question definitively: $DZ = 4\int_0^1B_t^3\,\tilde1_{[0,t]}\,dt$ ✓ (their formula was RIGHT in Bochner form; the "D_sZ=" prefix was loose notation).

NOW — one more deep check of Lemma A application: we need the potential identity for ALL t∈[0,1] INCLUDING t=0: $\langle m,1_{[0,0]}\rangle$: note $1_{[0,0]}$ = indicator of {0}: $\|1_{[0,0]}\|² = R(0,0) = 0$ — degenerate! Pairing gives $\int B_u^3R(u,0)du = \int B_u^3\frac12(u^{2H}+0−u^{2H})du = 0$ trivially. So t=0 gives nothing — fine, we use t∈(0,1] and continuity extends to 0 harmlessly (potential eq. at 0 holds vacuously/trivially: both sides... $\mathcal V_g(0) = \int|u|^{2H}g(u)du$ and $C