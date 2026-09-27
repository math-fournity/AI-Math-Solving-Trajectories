Let me start by reading the analysis notes file to understand the current state of the problem.Let me understand the task:

**Problem**: Let $B$ be a fractional Brownian motion (fBm) with Hurst parameter $H \in (0,1)$, and $Z = \int_0^1 B_s^4 \, ds$. Question: Does $Z$ have a density with respect to Lebesgue measure?

**Strategy**: Malliavin/Bouleau–Hirsch criterion. Show $\|DZ\|_{\mathcal H}^2 = 16 Q(B^3) > 0$ a.s., where $Q(g) := \iint_{[0,1]^2} g(s)g(t) R_H(s,t) \, ds \, dt$.

Key reduction: On the event $\{Q(B^3) = 0\}$, we have $m_g := \int g(t) \tilde 1_{[0,t]} dt = 0 \in \mathcal H$, which implies $U_g(s) = \int_0^1 g(t) R_H(s,t) dt$ is constant, hence $U_g \equiv 0$. Then by a deterministic lemma (Lemma A), $g \equiv 0$, i.e., $B \equiv 0$. But $\{B \equiv 0\}$ has probability zero. So $\{\|DZ\| = 0\}$ is null, and Bouleau-Hirsch gives absolute continuity.

**Lemma A(H)**: If $g \in C([0,1])$ and $U_g(s) \equiv \text{const}$ on $[0,1]$, then $g \equiv 0$.

Equivalent form: $\int_0^1 |s-t|^{2H} g(t) dt = A s^{2H} + D$ for all $s \in [0,1]$, where $A = \int g$, $D = C - 2c$, $C = \int t^{2H} g(t) dt$.

Wait let me redo this. $R_H(s,t) = \frac{1}{2}(s^{2H} + t^{2H} - |s-t|^{2H})$. 

$U_g(s) = \int_0^1 g(t) R_H(s,t) dt = \frac{1}{2}\left[ s^{2H} A + C - \mathcal V(s) \right]$ where $A = \int_0^1 g$, $C = \int_0^1 t^{2H} g(t) dt$, $\mathcal V(s) = \int_0^1 |s-t|^{2H} g(t) dt$.

If $U_g(s) \equiv c$ then $\mathcal V(s) = s^{2H} A + C - 2c =: As^{2H} + D$.

**Assembly plan**:
- (d) Ladder differentiation ⟹ $A = 0$: Differentiate the potential equation. $V'(s) = 2H[\int_0^s (s-t)^{2H-1} g(t) dt - \int_s^1 (t-s)^{2H-1} g(t) dt]$. Each further double differentiation reduces exponent by 2 ($\partial_s^2 |s-t|^\beta = \beta(\beta-1)|s-t|^{\beta-2}$, valid as long as current exponent $\beta > 1$ so new kernel is integrable). Ladder down until exponent falls in $(-1, 1]$:
  - If lands in $(-1, 0]$: Let $s \to 0^+$; RHS $As^\beta \to \pm\infty$ while $V^{(k)}(0^+)$ finite (g bounded, exponent > -1 integrable), forcing $A = 0$.
  - If lands in $(0, 1]$: First differentiate once (one-sided kernel still integrable), get one-sided equation with exponent $\beta - 1 \in (-1, 0]$, then same blow-up argument forces $A = 0$.

- (a) Energy identity with $A = 0$: $Q(g) = AC - \frac{1}{2}\mathcal E_{2H}(g)$. Hmm wait, actually the energy identity is about $Q$, but here in Lemma A we work with $\mathcal E_{2H}$. Let me re-read.

Actually wait. In the assembly plan: "Lemma A 的闭合 = (d) 的 $A=0$ + (a) 取 $A=0$ 得 $\mathcal E_{2H}(g)=2AC=0$" — hmm, that seems garbled. Let me think again.

From (b): $U_g \equiv c \Rightarrow Q(g) = 0$.

From (a): $Q(g) = AC - \frac{1}{2}\mathcal E_{2H}(g)$.

So if $U_g \equiv c$, then $Q(g) = 0$, i.e., $AC = \frac12 \mathcal E_{2H}(g)$.

With $A = 0$ from (d): $\mathcal E_{2H}(g) = 2AC = 0$.

Then from (c): zero-mean strictly negative definite — when $A = 0$ and $g \not\equiv 0$, $\mathcal E_{2H}(g) < 0$ strictly. Since $\mathcal E_{2H}(g) = 0$, we conclude $g \equiv 0$. 

That's the chain. Now I need to write this rigorously:

1. Setup: potential equation, smoothness of $V$.
2. Ladder differentiation: careful justification of differentiating under the integral with weak kernels, order of differentiation legality.
3. Case analysis on where $2H \bmod 2$ lands.
4. Blow-up argument at $s \to 0^+$ to force $A = 0$.
5. Energy identity derivation: $Q(g) = AC - \frac12 \mathcal E_{2H}(g)$.

Wait, actually let me verify the energy identity myself since it's crucial.

$Q(g) = \iint g(s)g(t) R_H(s,t) dsdt = \frac12 \iint g(s)g(t)[s^{2H} + t^{2H} - |s-t|^{2H}] dsdt$

$= \frac12[A C + C A - \mathcal E_{2H}(g)] = AC - \frac12 \mathcal E_{2H}(g)$.

Yes! Because $\iint g(s)g(t)s^{2H} ds dt = (\int g(s) s^{2H} ds)(\int g(t) dt) = CA$ and symmetrically. Good.

6. Zero-mean strict negative definiteness via Laplace representation:

$|x|^{2H} = c_H \int_0^\infty (1 - \cos(tx)) |t|^{-1-2H} dt$ for some constant $c_H > 0$.

Then $\mathcal E_{2H}(g) = c_H \int_0^\infty \xi^{-1-2H} [\ldots] d\xi$. Let me compute:

$\mathcal E_{2H}(g) = \iint g(s)g(t) |s-t|^{2H} dsdt = c_H \iint g(s)g(t) \int_0^\infty (1 - \cos(\xi(s-t))) \xi^{-1-2H} d\xi \, dsdt$

$= c_H \int_0^\infty \xi^{-1-2H} \left[ A^2 - \iint g(s)g(t)\cos(\xi(s-t)) dsdt \right] d\xi$.

Now $\iint g(s)g(t)\cos(\xi(s-t))dsdt = |\hat g(\xi)|^2$ where $\hat g(\xi) = \int g(u) \cos(\xi u) du$ (for real g; more precisely $\iint g(s)g(t)\cos(\xi(s-t)) = (\int g\cos\xi s)^2 + (\int g \sin \xi s)^2 = |\hat g_e(\xi)|^2$, the squared modulus of the even extension's Fourier transform... anyway).

So $\mathcal E_{2H}(g) = c_H \int_0^\infty \xi^{-1-2H}[A^2 - |\hat g(\xi)|^2] d\xi \le c_H A^2 \int_0^\infty \xi^{-1-2H}[\text{something bounded}]$...

Hmm wait, need care: $\int_0^\infty \xi^{-1-2H}(1-\cos(\xi x))d\xi = |x|^{2H}/c_H$ converges at both ends: near 0 integrand ~ $\xi^{1-2H}$ (fine since $2H < 2$... wait $1 - 2H > -1$ iff $H < 1$, yes fine), at infinity integrand ~ $\xi^{-1-2H}$ with $2H > 0$, fine.

But interchanging $\iint$ with the $\xi$ integral requires absolute convergence or Fubini-Tonelli care. For continuous $g$ on compact, everything is bounded except potentially the tails. Actually the standard approach: use the representation with a cutoff, or note that for the difference $A^2 - |\hat g|^2$, hmm.

Actually there's a cleaner way for the strict negativity when $A = 0$:

When $A = 0$: $\mathcal E_{2H}(g) = -c_H \int_0^\infty \xi^{-1-2H} |\hat g(\xi)|^2 d\xi \cdot$ ... wait no. With $A= 0$: $\mathcal E_{2H}(g) = -c_H\int_0^\infty \xi^{-1-2H}|\hat g(\xi)|^2 d\xi$? Let me redo: $\mathcal E = c_H\int \xi^{-1-2H}[A^2 - |\hat g|^2]d\xi$. With $A = 0$, $\mathcal E = -c_H \int \xi^{-1-2H}|\hat g(\xi)|^2 d\xi < 0$ provided $\hat g \not\equiv 0$ on $(0,\infty)$, which holds iff $g \not\equiv 0$ (if all Fourier cosine/sine data vanishes on $(0,\infty)$, then g = 0). And the integral is well-defined (possibly infinite)? No wait, we need it to be a proper negative number. Since $\hat g(\xi)$ is bounded and decays, $\int \xi^{-1-2H}|\hat g(\xi)|^2 d\xi$: near 0, $\hat g(\xi) \approx \hat g(0) = \int g = 0 = A$... hmm interesting, if $A = 0$ then $\hat g(\xi) = O(\xi)$ near 0 (since $\int g = 0$, the cosine transform starts at second order... let me think: $\hat g_c(\xi) = \int g(u)\cos(\xi u)du = \int g(u)(1 - \xi^2u^2/2 + \ldots) du = 0 - \xi^2/2 \int u^2 g + \ldots = O(\xi^2)$; $\hat g_s(\xi) = \int g(u)\sin(\xi u) du = \xi \int ug(u)du + O(\xi^3) = O(\xi)$.) So $\xi^{-1-2H}|\hat g|^2 = O(\xi^{1-2H})$ or $O(\xi^{2 - 4H}\cdot$...)— anyway integrable near 0 since $1 - 2H > -1$. At infinity, $|\hat g|^2 \le \|g\|_1^2$, and $\int^\infty \xi^{-1-2H}d\xi < \infty$. So the integral is finite. 

But hold on—the issue is whether the Fubini interchange is justified to get $\mathcal E = c_H\int \xi^{-1-2H}[A^2 - |\hat g|^2]$ as an honest identity of finite quantities. The individual pieces: $\iint |g(s)g(t)| \cdot \int \xi^{-1-2H}|1-\cos(\xi(s-t))| d\xi dsdt = \iint |g(s)g(t)||s-t|^{2H}/c_H \, dsdt < \infty$ since $|s-t|^{2H} \le 1$ and g bounded. Oh nice—since $|s - t| \le 1$, we have $\int_0^\infty \xi^{-1-2H}(1-\cos(\xi x)) d\xi \le \int_0^\infty \min(\xi^{1-2H}, 2\xi^{-1-2H}) d\xi \le C|x|^{2H}$... wait actually the exact formula gives $\int_0^\infty \xi^{-1-2H}(1-\cos(\xi x))d\xi = C_H |x|^{2H}$, and $1 - \cos \geq 0$, so the absolute value of the whole thing is exactly $C_H|x|^{2H} \le C_H$. So Tonelli applies directly: 

$\mathcal E_{2H}(g) = \iint g(s)g(t)|s-t|^{2H}dsdt = c_H\iint g(s)g(t)\left[\int_0^\infty \xi^{-1-2H}(1-\cos(\xi(s-t)))d\xi\right]dsdt$

and since $g(s)g(t)(1-\cos(\cdot)) \geq$ hmm, sign issues: $g(s)g(t)$ can be negative, but Tonelli works with $|g(s)g(t)|(1-\cos(\xi(s-t)))$ whose integral equals $C_H \iint |g(s)g(t)||s-t|^{2H} dsdt < \infty$. Great, so Fubini is fully justified by Tonelli applied to the absolute values. Then

$\mathcal E_{2H}(g) = c_H\int_0^\infty \xi^{-1-2H}\left[(\textstyle\int g)^2 - \left(\textstyle\int g\cos\right)^2 - \left(\textstyle\int g \sin\right)^2\right]d\xi$.

Hmm wait: $\iint g(s)g(t)\cos(\xi(s-t))dsdt$. Expand: $\cos(\xi s - \xi t) = \cos\xi s\cos \xi t + \sin\xi s \sin \xi t$. So $\iint g(s)g(t)\cos(\xi(s-t)) = (\int g\cos\xi u du)^2 + (\int g \sin\xi u du)^2 = |\hat g(\xi)|^2$ where $\hat g(\xi) = \int_0^1 g(u)e^{-i\xi u}du$. Yes.

And $\iint g(s)g(t) dsdt = A^2$.

So $\mathcal E_{2H}(g) = c_H\int_0^\infty \xi^{-1-2H}(A^2 - |\hat g(\xi)|^2)d\xi$, as an absolutely convergent integral (both parts finite by the bounds above; when $A = 0$ shown above; general case also fine since $|A^2 - |\hat g|^2|$ bounded and $\int \xi^{-1-2H}$ diverges at 0! Wait: $\int_0^1 \xi^{-1-2H} d\xi = \infty$. So need cancellation near 0: $A^2 - |\hat g(\xi)|^2 = O(\xi)$? Hmm: $|\hat g(\xi)|^2 = |A + O(\xi)|^2 = A^2 + O(\xi)$, so $A^2 - |\hat g(\xi)|^2 = O(\xi)$, integrable against $\xi^{-1-2H}$ iff $O(\xi^{1-2H})$ with $1 - 2H > -1$ ✓. OK so the combined integral converges; to justify splitting, integrate over $[\epsilon, \infty)$ first (all fine) then take $\epsilon \to 0$ using the cancellation bound. That works.)

For strict negativity when $A = 0$ and $g \not\equiv 0$: $\hat g$ is (restriction to ℝ of) entire function (compact support), not identically zero; its zero set is discrete, so $\hat g(\xi) \ne 0$ for a.e. ξ, in particular on a set of positive measure in $(0,\infty)$. Hence $\int \xi^{-1-2H}|\hat g(\xi)|^2 d\xi > 0$, giving $\mathcal E_{2H}(g) = -c_H \cdot (\text{positive}) < 0$. 

7. Now the ladder differentiation part (d) in detail. This is the trickiest rigorous bit. Let me carefully work through it.

Setup: $V(s) = \int_0^1 |s-t|^{2H}g(t)dt = As^{2H} + D$ for all $s\in[0,1]$, $g \in C([0,1])$.

Goal: show $A = 0$, then $\mathcal E_{2H}(g) = 2AC$... wait no. Hold on. Where does $\mathcal E_{2H}(g) = 0$ come from?

Chain again: Assume $U_g \equiv c$ (constant). 
- From (b): $Q(g) = 0$. [This requires the Malliavin-space argument: $m_g = 0 \in \mathcal H$ implies $Q(g) = \|m_g\|^2 = 0$.]
- From (a): $Q(g) = AC - \frac12 \mathcal E_{2H}(g)$, so $\mathcal E_{2H}(g) = 2AC$.
- From (d): $A = 0$. Hence $\mathcal E_{2H}(g) = 2AC = 0$.
- From (c): $A = 0$ and $g \not\equiv 0$ ⟹ $\mathcal E_{2H}(g) < 0$. Contradiction unless $g \equiv 0$. ∎

Alternatively, purely deterministically: can we avoid (b)/(a) and get directly from the potential equation? The potential equation alone says $\mathcal V(s) = As^{2H}+D$; plugging into the energy identity doesn't directly give $\mathcal E_{2H}(g)$ without knowing $Q$. Hmm, but actually there might be a direct way: multiply $\mathcal V(s) = As^{2H} + D$ by $g(s)$ and integrate:

$\iint |s-t|^{2H}g(t)g(s)dtds = A\int s^{2H}g(s)ds + D\int g(s)ds = AC + DA$.

So $\mathcal E_{2H}(g) = A(C + D)$. Interesting! So if we can show $A = 0$ AND $D = 0$... hmm, but with $A = 0$ this gives $\mathcal E_{2H}(g) = 0$ directly, without needing (b) and (a)! 

Wait: if $A = 0$, RHS $= 0 \cdot (C+D) = 0$. So $\mathcal E_{2H}(g) = 0$. Combined with (c): $g \equiv 0$. 

Oh nice, this is cleaner—it avoids the stochastic-space argument (b) entirely within Lemma A. The chain becomes:

Lemma A: Suppose $g \in C([0,1])$ and $U_g(s) \equiv c$ const on $[0,1]$. Equivalently $\mathcal V(s) = As^{2H} + D$ where $\mathcal V(s) = \int|s-t|^{2H}g(t)dt$, $A = \int g$, $D = C - 2c$, $C = \int t^{2H}g(t)dt$.

Step 1 (ladder): $A = 0$.
Step 2: Multiply the equation by $g$ and integrate: $\mathcal E_{2H}(g) = A(C+D) = 0$.
Step 3 (Laplace/negative-definiteness): $A = 0$, $\mathcal E_{2H}(g) = 0$ ⟹ $g \equiv 0$.

Beautiful. This makes Lemma A purely deterministic real analysis, and the only stochastic input is the reduction (event $\{Q = 0\}$ ⟹ $U_{B^3}$ constant) and Bouleau–Hirsch.

Hmm wait, but actually do we even need (b) then? The reduction was: on $\{Q(B^3) = 0\}$, $m_{B^3} = 0 \in \mathcal H$, hence $-\int \varphi' U_g = 0$ for all smooth φ, hence $U_g$ constant. So we still need (b)'s direction "$m_g = 0$ ⟹ $U_g$ constant" (the easy direction: pairing with test functions), but NOT the converse direction nor the claim $Q(g) = \|m_g\|^2$... wait actually we DO need $Q(g) = \|m_g\|^2$? No wait.

Let me re-examine the overall structure:

$\|DZ\|^2_{\mathcal H} = 16 Q(B^3)$ where $Q(g) = \langle m_g, m_g\rangle_{\mathcal H}$ with $m_g = \int_0^1 g(t)\tilde 1_{[0,t]}dt$. Indeed $D Z_s$... $D_sZ = 4\int_s^1 B_t^3 D_s B_t dt = 4\int_s^1 B_t^3 (D_sB_t)dt$. And $\langle D_s B, D_tB\rangle_{\mathcal H} = R_H(s,t) = \langle \tilde 1_{[0,s]}, \tilde 1_{[0,t]}\rangle$. So $\|DZ\|^2_{\mathcal H} = 16\iint_{s,t: ?} B_s^3B_t^3 \langle D_sB, D_tB\rangle_H dsdt$. Careful: $D_sZ = 4\int_s^1 B_t^3 \tilde 1_{[0,s]}(t)$? Hmm, let me just write $D_s Z = 4\int_0^1 B_t^3 D_s B_t dt = 4\int_0^1 B_t^3 \tilde1_{[0,s]}(t)dt = 4 m_{B^3}(s)$ where $m_g = \int g(t)\tilde 1_{[0,s]}$... indices: $m_g(s) := \int_0^1 g(t)\tilde 1_{[0,s]}(t)dt$. Hmm, $\tilde 1_{[0,s]}$ is the element of $\mathcal H$ with $\langle h, \tilde 1_{[0,s]}\rangle_\mathcal H = \int_0^s h\,du$. Then $D_sB_t = \tilde 1_{[0,s]}(t)$ meaning $\langle D_sB_t, \cdot\rangle$... Standard: $D_s B = \tilde 1_{[0,s]} \in \mathcal H$, viewed as function of $t$: $D_s B_t = \tilde 1_{[0,s]}(t)$, and $\langle D_sB, D_{s'}B\rangle_{\mathcal H} = \langle \tilde1_{[0,s]}, \tilde 1_{[0,s']}\rangle_\mathcal H = R_H(s,s')$. ✓.

So $D_sZ = 4\int_0^1 B_t^3 \tilde 1_{[0,s]}(t)dt$, thus
$\|DZ\|^2_\mathcal H = 16\int_0^1\!\!\int_0^1 B_s^3B_t^3\langle\tilde1_{[0,s]},\tilde1_{[0,t]}\rangle_\mathcal H dsdt = 16\iint B_s^3B_t^3R_H(s,t)dsdt = 16 Q(B^3)$. ✓ matches the notes.

Now, $Q(g) = \langle m_g,m_g\rangle_\mathcal H$ where $m_g = \int_0^1 g(t)\tilde 1_{[0,t]}dt$ (Malliavin-type integral of an adapted-ish process; here $g(t) = B_t^3$ is adapted, square-integrable, fine).

On event $E = \{Q(B^3) = 0\}$: $m_g = 0$ in $\mathcal H$. Then for any smooth φ: $\langle m_g, \varphi\rangle_\mathcal H = 0$. Compute: $\langle \tilde 1_{[0,t]}, \varphi\rangle_\mathcal H = \int_0^t \varphi'(u)du$? Hmm: $\langle h, \varphi\rangle_\mathcal H$ for nice $h$: integration by parts in the Cameron-Martin/fBm kernel space. For fBm, $\mathcal H_H$ is the completion of $C^\infty$-type functions w.r.t. inner product $\langle f,g\rangle_H = H(2H-1)\int\int f(s)g(t)|s-t|^{2H-2}dsdt$ for $H>1/2$; for $H<1/2$ it's defined via fractional calculus operators. The standard fact: $\langle \tilde 1_{[0,t]}, \varphi \rangle_\mathcal H = \varphi(t)$ for smooth φ. Indeed because $\tilde 1_{[0,t]}$ is $D_tB$, and $\langle D_tB, D\varphi(B)\rangle$... simpler: $\varphi(B_t) - \varphi(B_0) = \int_0^t \varphi'(B_u)\delta B_u$ hmm. Cleanest: $\langle \tilde1_{[0,t]},\varphi\rangle_\mathcal H = \int_0^1 \tilde 1_{[0,t]}(u)\, d\varphi^H(u)$... Let me instead use the defining property: $\langle h, \varphi\rangle_\mathcal H$ should equal $\int_0^1 \varphi'(u)\left(\int_0^u h(v)dv\right)$... 

Actually the notes say: $\langle m_g, \varphi\rangle_\mathcal H = -\int \varphi'(s)U_g(s)ds$ where $U_g(s) = \int_0^1 g(t)R_H(s,t)dt$. Let me verify: $\langle m_g,\varphi\rangle = \int_0^1 g(t)\langle \tilde 1_{[0,t]},\varphi\rangle dt$. And $\langle \tilde 1_{[0,t]},\varphi\rangle_\mathcal H$: since $\tilde 1_{[0,t]} = K\delta_t$ hmm. Use: $\langle \tilde 1_{[0,t]}, \varphi\rangle_\mathcal H = \langle \delta_t, K^*\varphi\rangle_{L^2}$? The fBm transfer operator: $\tilde 1_{[0,t]} = K 1_{[0,t]}$ where $K$ maps indicator functions; $\langle Kh_1, h_2\rangle_\mathcal H = \langle h_1, K^*h_2\rangle_{L^2[0,1]}$. So $\langle \tilde 1_{[0,t]},\varphi\rangle_\mathcal H = \langle 1_{[0,t]}, K^*\varphi\rangle_{L^2} = \int_0^t (K^*\varphi)(u)du$. For fBm, $(K^*\varphi)(u) = \frac{d}{du}\int_u^1 \varphi'(r)\frac{\partial R}{\partial r}(r,u)dr$-ish... This is getting complicated; but the upshot in both regimes is known: $\langle \tilde 1_{[0,t]},\varphi\rangle_\mathcal H = \varphi(t)$ (this is the reproducing kernel property in the appropriate sense—for Cameron–Martin space of Brownian motion $\langle 1_{[0,t]},\varphi\rangle_{CM} = \int_0^t \varphi'(u)du = \varphi(t)-\varphi(0)$; for fBm the analogous statement holds: the RKHS element $\tilde 1_{[0,t]}$ pairs with φ to give φ(t)... let me sanity check with $R_H$: define $\Phi(s) := U_\varphi$-like object... 

Alternative clean approach avoiding these RKHS subtleties: work with $U_g$ directly!

$Q(g) = \iint g(s)g(t)R_H(s,t)dsdt$. Integrate by parts / rewrite: 

$Q(g) = \int_0^1 g(t)\left[\int_0^1 g(s)R_H(s,t)ds\right]dt = \int_0^1 g(t)U_g(t)dt$.

And note $U_g(t) = \int_0^1 g(s)R_H(s,t)ds = \int_0^1 g(s)\langle \tilde 1_{[0,s]},\tilde 1_{[0,t]}\rangle ds = \langle \int_0^1 g(s)\tilde1_{[0,s]}ds, \tilde 1_{[0,t]}\rangle = \langle m_g, \tilde 1_{[0,t]}\rangle_\mathcal H$.

Also define $F_g(t) := \int_0^t g(s)ds$ hmm. Note $\langle m_g, \tilde 1_{[0,t]}\rangle = \frac{d}{dt}Q$-ish... Actually here's a classical trick: $Q(g) = \int_0^1 g(t) U_g(t) dt$ and also consider $W(t) := \int_0^1 g(s)R_H(\min(s,t),\max)...$. Hmm.

Cleaner: Let me use the standard identity $\langle \tilde 1_{[0,t]}, \varphi\rangle_\mathcal H = \varphi(t)$ for $\varphi \in C^1$ hmm is that right? Check H = 1/2: $\langle 1_{[0,t]},\varphi\rangle_{L^2} = \int_0^t\varphi = \ne \varphi(t)$. ✗!! 

Right, wrong. For BM: $\langle 1_{[0,t]},\varphi\rangle_{CM} = \int_0^1 1_{[0,t]}(u)\varphi'(u)du$? CM inner product: $\langle f,g\rangle_{CM} = \int f'g'du$. $\langle 1_{[0,t]},\varphi\rangle_{CM} = \int_0^t \varphi'(u)du = \varphi(t) - \varphi(0)$. So $\langle \tilde 1_{[0,t]},\varphi\rangle = \varphi(t) - \varphi(0)$ for BM. OK so for fBm analogously $\langle \tilde 1_{[0,t]},\varphi\rangle_\mathcal H = \varphi(t) - \varphi(0)$ presumably. Fine—doesn't matter, constants wash out. The notes' computation: $\langle m_g,\varphi\rangle = -\int\varphi' U_g$: 

$\langle m_g,\varphi\rangle = \int_0^1 g(t)[\varphi(t)-\varphi(0)]dt$. Hmm, and how does that equal $-\int\varphi'(s)U_g(s)ds$? We'd want $\int g(t)(\varphi(t)-\varphi(0))dt = \int_0^1\varphi'(s)\left[-\int_s^1 g(t)dt\right]ds$ — that's plain integration by parts with $\Phi(s) = -\int_s^1 g$, $\Phi' = g$: $\int_0^1 \varphi'(s)\Phi(s)ds + \int \varphi g = [\varphi\Phi]_0^1 = \varphi(1)\Phi(1) - \varphi(0)\Phi(0) = 0 - \varphi(0)(-\int_0^1g) = \varphi(0)A$. Hmm: $\int_0^1 \varphi'(s)\Phi(s)ds = [\varphi\Phi]_0^1 - \int_0^1\varphi(s)g(s)ds = \varphi(0)A - \int\varphi g$. So $\int \varphi g = \varphi(0)A - \int\varphi'\Phi$, giving $\int g(t)(\varphi(t)-\varphi(0))dt = -\int_0^1 \varphi'(s)\Phi(s)ds$ where $\Phi(s) = -\int_s^1g$. OK so indeed $\langle m_g,\varphi\rangle = -\int\varphi'(s)\left(-\int_s^1 g\right)ds$ for H=1/2. And the claim is the analogous formula with $U_g(s) = \int g(t)R_H(s,t)dt$ replacing $-\int_s^1 g$:

Claim: $\langle m_g,\varphi\rangle_\mathcal H = -\int_0^1\varphi'(s)U_g(s)ds$ for all smooth φ, all H.

Proof sketch: suffices to check for $m_g = \tilde 1_{[0,t]}$ (density argument): $\langle \tilde 1_{[0,t]},\varphi\rangle = ?$ vs $-\int \varphi'(s)R_H(s,t)ds$. Compute RHS: $-\int_0^1\varphi'(s)R_H(s,t)ds = -[\varphi R_H]_0^1 + \int_0^1\varphi(s)\partial_sR_H(s,t)ds = -\varphi(1)R_H(1,t) + \varphi(0)\underbrace{R_H(0,t)}_{=0} + \int_0^1\varphi(s)\partial_sR_H(s,t)ds$. Hmm and LHS should be $\varphi(t)-\varphi(0)$. Is $\langle\tilde 1_{[0,t]},\varphi\rangle_\mathcal H = -\int\varphi'R_H(\cdot,t)$? For BM: LHS $=\varphi(t)-\varphi(0)$; RHS: $-\int\varphi'(s)(s\wedge t)ds = -[\varphi(s)(s\wedge t)]_0^1 + \int\varphi(s)1_{s<t}ds = -\varphi(1)t+\int_0^t\varphi$. These are equal iff $\varphi(t)-\varphi(0) = -t\varphi(1)+\int_0^t\varphi(s)ds$?? Not generally. Hmm! So something's off. Let me recompute.

BM case, direct: $m_g(s) = \int_0^1 g(t)1_{[0,t]}(s)dt = \int_s^1 g(t)dt$. $\langle m_g,\varphi\rangle_{CM} = \int_0^1 m_g'(s)\varphi'(s)ds = \int_0^1(-g(s))\varphi'(s)ds = -\int g\varphi'$. ✓ matches notes' formula with $U_g(s) = \int_0^1 g(t)R(s,t)dt = \int_0^1 g(t)(s\wedge t)dt = \int_s^1g(t)\cdot s\,dt + \int_0^s g(t)t\,dt$. Wait that's not $m_g(s) = \int_s^1g$. Hmm, but $-\int\varphi'(s)m_g(s)ds = -\int\varphi'(s)\int_s^1g(t)dt\,ds$. And via my formula above: $-\int\varphi'(s)U_g(s)ds$ where $U_g(s) = \int_0^1g(t)(s\wedge t)dt = s\int_s^1 g + \int_0^s tg(t)dt$. Are these the same modulo integration by parts? $-\int\varphi'(s)[s\int_s^1g(t)dt]\,ds = -[s\varphi(s)\int_s^1g]_0^1 + \int s\varphi(s)\cdot(-g(s))ds\cdot(-1)$... let me be careful:

$\int_0^1\varphi'(s)\,s\,G(s)ds$ with $G(s) = \int_s^1g$. IBP: $= [s\varphi(s)G(s)]_0^1 - \int_0^1 G(s)[\varphi(s) + s\varphi'(s)]ds$. At $s=1$: $G(1) = 0$; at $s=0$: term is 0. So $= -\int_0^1\varphi(s)G(s)ds - \int_0^1 s\varphi'(s)G(s)ds$. Hence $\int\varphi'\cdot sG = -\int\varphi G - \int s\varphi' G$, i.e., $\int\varphi'[sG + \int_0^s tg(t)dt]ds = -\int \varphi G + \int\varphi'\int_0^stg - ...$ hmm I'm making errors. Let me just directly verify the claimed identity differently.

We want: $\langle m_g, \varphi\rangle_\mathcal H = -\int_0^1\varphi'(s)U_g(s)ds$ where $U_g(s) = \langle m_g, \tilde 1_{[0,s]}\rangle$.

Since $U_g(s) = \langle m_g,\tilde1_{[0,s]}\rangle$, and if we knew $\langle h, \varphi\rangle_\mathcal H = -\int\varphi'(s)\langle h,\tilde 1_{[0,s]}\rangle ds$ for all $h \in \mathcal H$ smooth-ish (this is an abstract integration-by-parts identity of the RKHS), then done. Verify for BM: $\langle h,\varphi\rangle_{CM} = \int h'\varphi'$. RHS: $-\int\varphi'(s)\frac{d}{ds}\langle h,\int_0^\cdot 1\rangle$... For BM, $\langle h, 1_{[0,s]}\rangle_{CM} = \int_0^s h'(u)du = h(s) - h(0)$. So RHS $= -\int\varphi'(s)(h(s)-h(0))ds = -\int\varphi' h + h(0)\int\varphi' = -\int\varphi'h + h(0)(\varphi(1)-\varphi(0))$. IBP: $\int \varphi'h = [\varphi h]_0^1 - \int \varphi h' = \varphi(1)h(1) - \varphi(0)h(0) - \int\varphi h'$. So RHS $= -\varphi(1)h(1) + \varphi(0)h(0) + \int\varphi h' + h(0)\varphi(1) - h(0)\varphi(0) = \int\varphi h' + h(0)(\varphi(1)-\varphi(0)) - \varphi(1)(h(1)-h(0))$. Hmm, that's $\int\varphi h'$ plus boundary junk. Not equal to $\int h'\varphi'$ in general. ✗?!

Hmm wait, maybe the correct identity has different boundary terms, or maybe the right statement uses $\varphi(1) = 0$ test functions, or the identity is $\langle h,\varphi\rangle = -\int \varphi'(s)\langle h, \tilde1_{[0,s]}\rangle ds + $ correction. Hmm. But wait—for our purposes what matters is: IF $\langle m_g, \varphi\rangle_\mathcal H = 0$ for all φ in a dense class, THEN $m_g = 0$, THEN $U_g(\cdot) = \langle m_g, \tilde 1_{[0,\cdot]}\rangle \equiv 0$. The direction we need is: $m_g = 0$ ⟹ $U_g \equiv 0$, which is TRIVIAL since $U_g(s) = \langle m_g, \tilde 1_{[0,s]}\rangle_\mathcal H$! 

Oh wait, but that requires $U_g(s) = \langle m_g,\tilde 1_{[0,s]}\rangle$, i.e., $\int_0^1 g(t)\langle\tilde 1_{[0,t]},\tilde 1_{[0,s]}\rangle dt = \langle \int g\tilde1_{[0,t]}dt, \tilde1_{[0,s]}\rangle$, which is just continuity of inner product—valid as long as $m_g = \int g\tilde 1_{[0,t]}dt$ exists in $\mathcal H$ (Bochner integral), which it does ($g$ bounded, $\sup_t\|\tilde1_{[0,t]}\|^2 = R_H(t,t) = t^{2H}\le1$). ✓✓

And conversely, to apply Lemma A we need: $m_g = 0$ ⟹ $U_g$ constant — actually we get $U_g \equiv 0$ directly, even better than constant. Wait, but the notes say the reduction goes through "$m_g = 0$ ⟹ pairing with all smooth φ vanishes ⟹ $-\int\varphi'U_g = 0$ ∀φ ⟹ $U_g$ const". That route needs the integration-by-parts identity. But the direct route $U_g(s) = \langle m_g,\tilde 1_{[0,s]}\rangle_\mathcal H = 0$ avoids ALL RKHS subtleties! Much cleaner. 

So the actual logical flow needed:

(i) $\|DZ\|^2_\mathcal H = 16Q(B^3)$, $Q(g) = \iint g(s)g(t)R_H(s,t)dsdt = \int g(t)U_g(t)dt$ where $U_g(t) = \int g(s)R_H(s,t)ds$.

(ii) On $E = \{Q = 0\}$: $m_{B^3} = 0$ in $\mathcal H$ [since $Q = \|m\|^2$], hence $U_{B^3}(s) = \langle m,\tilde1_{[0,s]}\rangle = 0$ for all s. Pathwise deterministic statement now: the path $g := (B_t^3)_t$ satisfies $U_g \equiv 0$ on $E$.

(iii) Deterministic Lemma A: $g\in C$, $U_g\equiv0$ ⟹ $g\equiv0$. [Note: $U_g \equiv 0$ is the special case of the notes' "$U_g$ constant" with $c = 0$; and actually for Lemma A we may as well prove: $U_g \equiv c$ ⟹ $g ≡ 0$.]

(iv) $P(E) \le P(B\equiv 0) = 0$. Hence $\|DZ\|_\mathcal H > 0$ a.s.

(v) Bouleau–Hirsch / Nualart Thm: non-degenerate Malliavin covariance in probability ⟹ law of Z has density wrt Lebesgue. Need $Z \in \mathbb D^{1,p}$ for some $p > 1$ (actually $p>4$? For density existence criterion need $E[\|DZ\|^p]<\infty$ hmm, Nualart Prop 2.1.1/(Thm 2.1.3): if $F\in\mathbb D^{1,p}, p>1$ hmm wait for the criterion "$\|DF\| > 0$ a.s." we typically need... Nualart's book Theorem 2.1.3 ("Bouleau–Hirsch"): Let $F \in \mathbb D_{loc}^{1,p}$, $p>1$ hmm, actually the criterion: if $P(\|DF\|_H > 0) = 1$ then the law of F is absolutely continuous. There are versions requiring $F\in\mathbb D^{1,p}$ globally with the set $\{\|DF\|=0\}$ null: then density exists. Some versions give density in $L^p$ etc. We'll cite appropriately.)

For $Z \in \mathbb D^{1,p}$: $Z = \int_0^1B_s^4ds$; $DZ_s = 4\int_s^1B_t^3D_sB_tdt$ hmm as computed $= 4m_{B^3}(s)$. Moments: $E\|DZ\|^2_\mathcal H \le 16\int_0^1\int_0^1(E B_s^6B_t^6)^{1/2}$... fBm has Gaussian moments, $E|B_s|^k \le C_k s^{kH}$, so all moments finite, dominated convergence gives $Z\in\mathbb D^{1,p}\forall p<\infty$. Standard.

Also need chain rule validity: $Z = \int B_s^4 ds$, $B^4 \in \mathbb D^{1,p}$ locally... $B_s$ is Gaussian so $B_s^4\in\mathbb D^{1,p}$, and $s\mapsto B_s^4$ continuous in $\mathbb D^{1,p}$ a.s.? Need Bochner integrability: $E\int_0^1(|B_s|^4 + s^{2H}|B_s|^2)^{p/2}$ hmm wait $\|D(B_s^4)\| = 4|B_s|^3\|D B_s\| = 4|B_s|^3 s^H$. All finite moments. Fine.

So the ONLY genuinely hard piece is Lemma A. And within Lemma A, the plan:

Lemma A: $g \in C([0,1])$, $U_g(s) := \int_0^1 g(t)R_H(s,t)dt \equiv c$ (constant) on $[0,1]$. Show $g \equiv 0$.

Step 0: Convert to potential equation. $U_g(s) \equiv c$ ⟺ $\frac12[s^{2H}A + C - \mathcal V(s)] = c$ ⟺ $\mathcal V(s) = As^{2H} + D$, $D := C - 2c$ const, where $\mathcal V(s) = \int_0^1|s-t|^{2H}g(t)dt$.

Step 1 (ladder): Show $A = \int g = 0$.

Step 2: Pair with g: $\mathcal E_{2H}(g) = \int g(s)\mathcal V(s)ds = A\int s^{2H}g(s)ds + D\int g(s)ds = AC + DA$. With $A=0$: $\mathcal E_{2H}(g) = 0$.

Step 3: Laplace rep: $A = 0, \mathcal E = 0, g$ continuous ⟹ $g\equiv 0$.

Now Step 1 in detail. Write $\beta = 2H \in (0,2)$.

$V(s) = \int_0^1|s-t|^\beta g(t)dt = As^\beta + D$.

First derivative: $V'(s) = \beta\int_0^1 \text{sgn}(s-t)|s-t|^{\beta-1}g(t)dt = \beta[J_+(s) - J_-(s)]$ where $J_+(s) = \int_0^s(s-t)^{\beta-1}g(t)dt$, $J_-(s) = \int_s^1(t-s)^{\beta-1}g(t)dt$.

Legality: need $V \in C^1$ with this formula. Since $g$ continuous: near $t=s$, $|s-t|^{\beta-1}g(t)$ integrable iff $\beta - 1 > -1$ ✓ (β>0). Dominated convergence on compact subintervals away from diagonal is trivial; across diagonal: $|V(s+h)-V(s)|/h$ analysis. Standard result: $s\mapsto\int|s-t|^\beta g(t)dt$ is $C^1$ when $\beta>1$... wait no: when β ∈ (0,1], $V$ is Hölder but is it $C^1$? $V(s+h)-V(s) = \int[|s+h-t|^\beta - |s-t|^\beta]g(t)dt$. The difference quotient: $\frac{|x+h|^\beta-|x|^\beta}{h}$, dominated pointwise by... for β∈(0,1): sup over h of $|\cdot|/h \le C|h|^{\beta-1}$ which blows up near x=0 but is integrable in x for β>0 (since β-1 > -1). So DCT works: $V'(s) = \int\partial_s|s-t|^\beta g(t)dt$ with domination $C\|g\|_\infty\int|s-t|^{\beta-1}dt < \infty$. ✓ So $V\in C^1$ for all β>0, and moreover $V'$ is continuous (similar domination). ✓ Matches "@62500 已验证 $C^1$ 性".

Second derivative: $V''(s) = \beta(\beta-1)\int_0^1|s-t|^{\beta-2}g(t)dt$ — integrable iff $\beta-2>-1$ iff β>1. For β≤1 must stop.

General ladder: define $k^* = $ number of times we can differentiate twice. Exponent after j double-differentials: $\beta_j = \beta - 2j$. Can differentiate twice while $\beta_j > 1$, i.e., $j < (\beta-1)/2$.

Case analysis. Let me parametrize: β = 2H ∈ (0,2).

After $j := \lfloor (\beta-1)/2 \rfloor$ double-differentiations (j ≥ 0), exponent $\beta_j = \beta - 2j \in (1, 3]$.

- If $\beta_j > 2$: can double-differentiate once more? Condition β_j > 1 allows one more double-diff giving β_j − 2 ∈ (−1, 1]. Hmm wait condition for differentiating twice is current exponent > 1. Let me recount: we start with exponent β. Double-diff allowed iff current exponent > 1 (new kernel exponent = old − 2 > −1, integrable). 

Let me define the sequence: e_0 = β. While e_k > 1: e_{k+1} = e_k − 2. Stop at first k with e_k ≤ 1. Then e_k ∈ (−1, 1].

Given β ∈ (0,2): e_1 = β−2 ∈ (−2, 0). So k ∈ {0, 1}: if β > 1, stop at k=1 with e_1 = β−2 ∈ (−1, 0); if β ≤ 1, stop at k=0 with e_0 = β ∈ (0,1].

Subcase β ∈ (0,1] (H ≤ 1/2): We have $V = As^\beta + D$ with V ∈ C^1, $V' = \beta[J_+ - J_-]$ where $J_\pm$ involve kernel exponent β−1 ∈ (−1,0]. 

Now differentiate once more? $V''$ involves $|s-t|^{\beta-2}$, exponent ∈ (−2,−1]: NOT locally integrable across diagonal. Instead, handle one-sided: $J_+(s) = \int_0^s(s-t)^{\beta-1}g(t)dt$ is (fractional-integral-like) differentiable from... hmm. Alternative per the notes: don't differentiate again; instead use behavior as $s\to0^+$.

As $s\to0^+$: 
$J_+(s) = \int_0^s(s-t)^{\beta-1}g(t)dt \le \|g\|_\infty s^\beta/\beta \to 0$. 
$J_-(s) = \int_s^1(t-s)^{\beta-1}g(t)dt \to \int_0^1 t^{\beta-1}g(t)dt =: M_1$ (finite since β>0, g bounded). 
So $V'(0^+) = -\beta M_1$ exists as limit, i.e., $V'$ extends continuously to $0^+$.

Meanwhile RHS: $\frac{d}{ds}[As^\beta + D] = \beta As^{\beta-1}$. 

Two cases:
- If β < 1: as $s\to0^+$, $\beta As^{\beta-1} \to \pm\infty$ if $A\ne0$ (sign of A), while LHS → finite $-\beta M_1$. Contradiction ⟹ $A = 0$. ✓ (This is the @39800 argument.)
- If β = 1 (H = 1/2): handled separately classically anyway; but also fits: $V' = A$ const; $V'(s) = J_+-J_-$, as $s\to0^+$: $J_+\to0$, $J_-\to\int t^0 g = A$. So $A = -A$?? wait $V'(0^+) = -\beta M_1 = -M_1 = -\int g = -A$, and RHS limit is A·β·s^0 = A. So $A = -A$, $A=0$. ✓ Works too. Actually clean.

Subcase β ∈ (1,2) (H > 1/2): $e_1 = β−2 ∈ (−1,0)$. $V''(s) = \beta(\beta-1)\int_0^1|s-t|^{\beta-2}g(t)dt = \beta(\beta-1)[K_+(s)+K_-(s)]$ where $K_+(s) = \int_0^s(s-t)^{\beta-2}g(t)dt$, $K_-(s) = \int_s^1(t-s)^{\beta-2}g(t)dt$, kernels exponent β−2 ∈ (−1,0), locally integrable ✓. Legality of $V''$: $V'$ given by $\beta[J_+-J_-]$, each $J_\pm$ differentiable: $J_+'(s) = (s-s)^{\beta-1}g(s) + \int_0^s(\beta-1)(s-t)^{\beta-2}g(t)dt = \int_0^s(\beta-1)(s-t)^{\beta-2}g(t)dt$ (boundary term: $(s-t)^{\beta-1}$ at t=s is 0 since β>1 ✓). Domination for DCT: $C\int_0^s(s-t)^{\beta-2}dt = Cs^{\beta-1}$ finite ✓. Similarly $J_-'(s) = -(t-s)^{\beta-1}|_{t=s}\cdot g(s) - \int_s^1(\beta-1)(t-s)^{\beta-2}g(t)dt$ wait: $J_-(s) = \int_s^1(t-s)^{\beta-1}g(t)dt$, $\partial_s = -(t-s)^{\beta-1}g(t)|_{t=s} + \int_s^1-(\beta-1)(t-s)^{\beta-2}g(t)dt = -(\beta-1)K_-(s)$ (boundary term vanishes since exponent β−1>0). ✓ So $V'' = \beta(\beta-1)[K_+ + K_-] = \beta(\beta-1)\int_0^1|s-t|^{\beta-2}g(t)dt$ ✓ and $V''$ continuous similarly. Meanwhile RHS: $\beta(\beta-1)As^{\beta-2}$.

As $s\to0^+$: $K_+(s)\to0$ (bound $\|g\|_\infty s^{\beta-1}/(\beta-1)\to0$), $K_-(s)\to\int_0^1t^{\beta-2}g(t)dt =: M_2$ finite (exponent > −1 ✓). So $V''(0^+) = \beta(\beta-1)M_2$ finite. RHS: $\beta(\beta-1)As^{\beta-2}$ with $\beta-2\in(-1,0)$: blows up unless $A=0$. ⟹ $A=0$. ✓

So uniformly: **A = 0 for all β ∈ (0,2)**, with the two cases (differentiate twice if β>1, else once; then blow-up at origin). Also note for β exactly... covered. What about the notes' sub-case "lands in (0,1]: differentiate once more to reach (−1,0]"? That would be for β ∈ (2,3) i.e. H>1, outside range. Our β∈(0,2) means the ladder is at most: β→β−2. Simple!

Wait, but hold on: the notes describe a longer ladder because they considered general exponents, but since 2H ∈ (0,2), the ladder has length at most 1 (one double-differentiation). 

Hmm wait, actually I realize we should double check whether we can shortcut Step 1 entirely. Alternative: evaluate the potential equation at special points? $V(0) = D$ (since $0^\beta = 0$): $\int t^\beta g(t)dt = D = C - 2c$, consistent, no info. Hmm, no shortcut visible; ladder it is. Actually wait — there might be an even slicker route for Step 1: the equation $\mathcal V(s) = As^\beta + D$; apply $\partial_s$ once: $\beta[J_+-J_-] = \beta As^{\beta-1}$. Set $s=0$: LHS → $-\beta M_1$, RHS → 0 if β>1, ±∞ if β<1&A≠0, A if β=1. For β>1: get $M_1 = 0$?? wait: $-\beta M_1 = \lim_{s\to0}\beta As^{\beta-1} = 0$ (β>1) ⟹ $M_1 = \int t^{\beta-1}g = 0$. Interesting, extra info but not yet A=0. Then differentiate again as above. Fine—stick with the plan.

Hmm, wait. Actually, let me reconsider: is there an issue with the case β ∈ (0,1] regarding whether $V'$ formula holds AT $s=0$ or only on $(0,1]$? We only use limits $s\to0^+$, fine.

But actually hold on, for β ∈ (0,1], I want to double-check the claim "$V'(s) = \beta[J_+(s) - J_-(s)]$ on (0,1]". Yes since $V \in C^1((0,1])$... on all of [0,1] including 0? At s=0: $V'(0)$: difference quotient $\frac{V(h)-V(0)}{h} = \frac{\int(|h-t|^\beta - t^\beta)g(t)dt}{h}$. For t>h: $t^\beta - (t-h)^\beta \sim \beta ht^{\beta-1}$; contribution $\to -\beta M_1$. For t<h: $(h-t)^\beta - t^\beta$, contribution: $\int_0^h[(h-t)^\beta - t^\beta]g(t)dt/h$, magnitude $\le \|g\|_\infty h^\beta/h\cdot h\cdot\frac{2}{\beta+1}$/h hmm $\int_0^h h^\beta dt/h = h^\beta\to0$ ✓. So $V'(0) = -\beta M_1$ genuinely exists. Even better. But we don't even need continuity at 0; limits suffice.

OK so Step 1 is solid and quite simple. Let me now also double check Step 2 and Step 3.

Step 2: $\mathcal E_{2H}(g) := \int_0^1\!\!\int_0^1 g(s)g(t)|s-t|^\beta dsdt$. Using $\mathcal V(s) = As^\beta+D$: $\mathcal E = \int_0^1 g(s)\mathcal V(s)ds = A\int s^\beta g(s)ds + D\int g = AC + DA$. With A=0: $\mathcal E = 0$. ✓ (Justified: ordinary integral manipulation, everything absolutely convergent.)

Step 3: Laplace representation. For $0<\gamma<2$ ($\gamma := \beta$): 
$$|x|^\gamma = c_\gamma\int_0^\infty(1-\cos(\xi x))\xi^{-1-\gamma}d\xi,$$
$c_\gamma = \left[\int_0^\infty(1-\cos u)u^{-1-\gamma}du\right]^{-1} > 0$.

Check: substitute u = ξ|x|: $\int_0^\infty(1-\cos(\xi x))\xi^{-1-\gamma}d\xi = |x|^\gamma\int_0^\infty(1-\cos u)u^{-1-\gamma}du$ for x≠0 ✓.

Then for $g\in C([0,1])$ extended by 0 to ℝ (or just work on [0,1]):
$\mathcal E = c_\gamma\int_0^\infty\xi^{-1-\gamma}\left[A^2 - |\hat g(\xi)|^2\right]d\xi$
where $\hat g(\xi) = \int_0^1g(u)e^{-iu\xi}du$, justified by Tonelli (absolute version finite as computed: $\iint|g(s)g(t)|\cdot C|s-t|^\gamma <\infty$).

With A=0: $\mathcal E = -c_\gamma\int_0^\infty\xi^{-1-\gamma}|\hat g(\xi)|^2d\xi$.

Convergence: near 0: $|\hat g(\xi)|^2 \le (\int|g|)^2$ but need integrability: $|\hat g(\xi)| = |\int_0^1 g(u)(e^{-iu\xi}-1)du| \le \xi\int_0^1u|g|du \le C\xi$, so $\xi^{-1-\gamma}\xi^2 = \xi^{1-\gamma}$, integrable near 0 iff γ<2 ✓. Near ∞: $|\hat g|\le\|g\|_1$, $\int_1^\infty\xi^{-1-\gamma}d\xi<\infty$ ✓.

If $g\not\equiv0$: $\hat g$ is holomorphic (entire) on ℂ, not identically zero (e.g., its restriction to ℝ... if $\hat g\equiv0$ on ℝ then g=0 a.e. by injectivity of Fourier transform on L¹, contradicting continuity + g≢0). Zeroes of nonzero holomorphic function are isolated, so $|\hat g(\xi)|^2>0$ except on a discrete subset of (0,∞); hence $\int_0^\infty\xi^{-1-\gamma}|\hat g|^2d\xi>0$. Therefore $\mathcal E < 0$, contradicting $\mathcal E=0$. Hence $g\equiv0$. ∎

All three steps are clean. Also should handle: what if $c \ne 0$, does anything change? Step 0 conversion handles arbitrary c via D. Steps 1–3 never used c or D beyond constancy. ✓

Edge consideration: the problem says H ∈ (0,1). H = 1/2 included (β=1 case worked above; also classical independent treatment available). 

Now assemble the full solution:

**Theorem**: For every H ∈ (0,1), $Z=\int_0^1B_s^4ds$ has a density wrt Lebesgue measure.

**Proof structure**:
1. Malliavin smoothness: $Z\in\mathbb D^{1,p}\ \forall p<\infty$; $D_sZ = 4\int_0^1B_t^3\tilde 1_{[0,s]}(t)dt$.
2. $\|DZ\|_\mathcal H^2 = 16\,\mathbb E$-pathwise $16\iint B_s^3B_t^3R_H(s,t)dsdt = 16\,Q(B^3)$.
   Define $m(s) := \int_0^1 B_t^3\tilde1_{[0,s]}(t)dt \in \mathcal H$ (a.s. well-defined Bochner integral), so $\|DZ\|^2 = 16\|m\|^2_\mathcal H$ and $U(t) := \int_0^1B_s^3R_H(s,t)ds = \langle m,\tilde1_{[0,t]}\rangle_\mathcal H$.
3. Event $E:=\{\|DZ\| = 0\} = \{m=0\}$. On E: $U\equiv0$ pathwise.
4. Lemma A ⟹ on E: $B^3\equiv0$ ⟹ $B\equiv0$. $P(E) \le P(B\equiv0)=0$.
5. Bouleau–Hirsch: $Z\in\mathbb D^{1,p}$, p>1 (say p=2), $\|DZ\|>0$ a.s. ⟹ law of Z abs. cont.

Wait, subtle point in step 3: on E, $m = 0$ as an $\mathcal H$-element. Then $U(t) = \langle m, \tilde 1_{[0,t]}\rangle_\mathcal H = 0$. ✓. And $U$ defined by the explicit integral $\int_0^1B_s^3R_H(s,t)ds$: equality with the inner product holds always (continuity of inner product under Bochner integration), not just on E. ✓.

Another subtlety in step 3: Lemma A concludes from $U_g\equiv0$ that $g\equiv0$ where $g(t)=B_t^3$. Conclude $B_t=0\ \forall t$ (cube injective). ✓.

$P(B\equiv0)=0$: fBm is Gaussian, non-degenerate: e.g., $P(B_1 = 0) = 0$ suffices: $\{B\equiv0\}\subseteq\{B_1=0\}$, and $B_1\sim N(0,1)$. ✓.

Step 5 details: Nualart, Theorem 2.1.3 (2nd ed.): "Let $F\in\mathbb D_{loc}^{1,p}$, $p>1$, and suppose $\|DF\|_H \ne 0$ a.s. hmm precisely: P(\|DF\|_H = 0) = 0. Then the law of F is absolutely continuous w.r.t. Lebesgue measure." Something like that. We can state: By the Bouleau–Hirsch criterion (Nualart 2006, Thm 2.1.3), since $Z\in\mathbb D^{1,2}$ and $P(\|DZ\|_\mathcal H>0)=1$, the law of Z admits a density. ✓

Also worth adding: quantitative regularity could be obtained (density in $L^p$ etc.) but not required.

Now — formal verification requirements. I must verify computationally:

1. **Numerical Monte-Carlo verification**: simulate fBm paths, compute $Q(B^3)$ along paths, check it's rarely/never near 0 relative to scale; estimate density of Z empirically (histogram smoothness) — weak but supportive. Better: numerically test Lemma A itself: pick random smooth-ish functions g, compute $U_g$, check that $U_g$ close to constant only when g≈0. Actually Lemma A is deterministic—can verify by discretization: solve for g such that $U_g$ ≈ constant on a grid (linear algebra) and observe the solution collapses to ≈0. That's a strong numerical check: the operator $T: g\mapsto U_g$ restricted... Take grid n=100, build matrix $M_{ij} = R_H(s_i,t_j)w_j$ (quadrature weights), find null space / smallest singular vectors of "deviation from constants": i.e., project: does there exist g ≠ 0 with $Mg \in \text{span}(1)$? Solve constrained least squares minimizing ‖Mg − c·1‖² subject to ‖g‖=1, check minimum is bounded away from 0. Do for various H. 

2. **Symbolic verification of key identities** with sympy:
   - Energy identity $Q(g) = AC − ½\mathcal E$ — trivial algebra, can verify symbolically with polynomial test g's and generic H (or specific H values).
   - The ladder differentiation formulas (kernel derivatives) — symbolic.
   - The Laplace representation constant: verify numerically $\int_0^\infty(1-\cos u)u^{-1-\gamma}du = \pi/(\Gamma(\gamma+1)\sin(\pi\gamma/2))$ for sample γ, and that $c_\gamma|s-t|^\gamma$ matches $|s-t|^\gamma$ numerically at sample points.
   - Strict negativity: random zero-mean g's, compute $\mathcal E_{2H}(g) < 0$ numerically. ✓

3. **Verify the blow-up argument's content**: for β∈(0,1): construct candidate solutions with A≠0 of discretized equation and confirm contradiction appears (numerically the LSQ will just fail) — covered by #1.

4. Possibly verify the full Malliavin chain by MC: estimate P(Q(B³) < ε·scale) → small; estimate density of Z via kernel smoothing for a couple of H values; also verify $\|DZ\|^2 = 16Q$ identity numerically pathwise (compute both sides: LHS via $\int\int D_sZ D_tZ R$ hmm that IS Q; instead verify $D_sZ = 4\int_0^1B_t^3\tilde1_{[0,s]}(t)dt$ numerically? For H=1/2, $D_sZ = 4\int_s^1B_t^3dt$, and $\|DZ\|^2 = 16\int\int_{s<t}... $ hmm, for H=1/2: $\|DZ\|^2_{CM} = 16\int_0^1(\int_s^1B_t^3dt)^2ds$. Compare with $16Q$: $Q = \iint B_s^3B_t^3(s\wedge t)dsdt$. Identity: $\int_0^1G(s)^2ds$ where $G(s)=\int_s^1B_t^3dt$ equals $\iint B_s^3B_t^3(s\wedge t)dsdt$? $\int_0^1\int_s^1\int_s^1B_u^3B_v^3dudvds = \iint B_u^3B_v^3\int_0^{\min(u,v)}ds\,dudv = \iint B_u^3B_v^3\min(u,v)dudv$ ✓. Numerically verify pathwise equality. ✓)

5. SageMath/Lean: probably Python+sympy+mpmath suffice. Lean for Lemma A would be a big lift (fractional kernels, integration by parts); I'll rely on Python verification + declare scope honestly.

Also: the problem statement asks specifically "does Z have a density" — answer YES for all H∈(0,1). Also mention H=1/2 explicitly (classical). Perhaps remark on stronger statements (smoothness of density? Known results: for H>1/6 or so, density is smooth by higher-order Malliavin calculus — Cheridito–Nualart type results. Actually known literature: Berruiati? The known result: $Z=\int B^4$ hmm. There's literature on densities of polynomials of fBm; e.g., Hu–Nualart. Smoothness: $\|DZ\|^{-p}$ integrability conditions relate to H > 1/8? Not needed. Keep answer minimal: existence.)

One more check — the reduction step needs $m(s)$-Bochner integral: $m = \int_0^1B_t^3\tilde1_{[0,t]}dt$ — note the integrand process $t\mapsto B_t^3\tilde1_{[0,t]}$ hmm wait indices: $D_sZ = 4\int_0^1 B_t^3 D_sB_t dt$; $D_sB_t = \tilde1_{[0,s]}(t)$, so $D_sZ = 4\int_0^1B_t^3\tilde 1_{[0,s]}(t)dt = 4\int_0^s B_t^3dt$?? NO WAIT. $\tilde 1_{[0,s]}$ as a function of t: it's the RKHS element associated to indicator of [0,s]; as an actual function (for H≥1/2) $\tilde 1_{[0,s]}(t) = 1_{t\le s}$. So $D_sZ = 4\int_0^sB_t^3dt$?? That contradicts the classical $D_sZ = 4\int_s^1B_t^3dt$ for BM!

Let me recheck. For BM, $D_sB_t = 1_{[0,s]}(t)$, i.e., $D_sB_t = 1$ if $t \le s$ (the noise enters up to time s). Chain rule: $D_s(B_t^4) = 4B_t^31_{t\le s}$. Then $D_sZ = \int_0^1 4B_t^31_{t\le s}dt = 4\int_0^sB_t^3dt$. Hmm! But classical result for $Z=\int_0^1B_s^4ds$ (BM): $D_sZ = 4\int_s^1B_t^3dt$?? Which is right??

$Z = \int_0^1 f(B_t)dt$, $D_sZ = \int_0^1f'(B_t)D_sB_tdt = \int_0^1 4B_t^3\cdot1_{t\le s}dt = 4\int_0^sB_t^3dt$. 

Hmm, so which convention: $D_sB_t = 1_{t\le s}$ or $1_{t\ge s}$? Definition: $B_t = \int_0^t dB$, $D_sB_t = 1_{[0,t]}(s) = 1$ if $s\le t$. So $D_sB_t = 1_{s\le t}$. Then $D_sZ = \int_0^14B_t^31_{s\le t}dt = 4\int_s^1B_t^3dt$. ✓ Classical. I confused myself: $\tilde 1_{[0,t]}$ evaluated at s: $\tilde1_{[0,t]}(s)=1_{s\le t}$. So $D_sB_t = \tilde1_{[0,t]}(s)$. Good: $D_sZ = 4\int_s^1B_t^3\,\tilde1$-weighted $= 4m(s)$ with $m(s):=\int_s^1B_t^3dt$ (BM case). In general fBm: $D_sZ = 4\int_0^1B_t^3(D_sB_t)dt = 4\int_0^1B_t^3\tilde 1_{[0,t]}(s)dt$, i.e., as an element of $\mathcal H$: $DZ = 4\int_0^1B_t^3\tilde1_{[0,t]}dt = 4m$ where $m:=\int_0^1B_t^3\tilde1_{[0,t]}dt\in\mathcal H$. ✓ (matches notes: $m_g=\int g(t)\tilde1_{[0,t]}dt$, $g=B^3$.)

$\|DZ\|^2 = 16\langle m,m\rangle = 16\int\int B_s^3B_t^3\langle\tilde1_{[0,s]},\tilde1_{[0,t]}\rangle dsdt = 16\iint B_s^3B_t^3R_H(s,t)dsdt = 16Q$. ✓✓

And $U(t) := \int_0^1B_s^3R_H(s,t)ds = \langle m,\tilde1_{[0,t]}\rangle_\mathcal H$. ✓ (inner product in first slot variable s: $\langle\tilde1_{[0,s]},\tilde1_{[0,t]}\rangle = R_H(s,t)$ ✓.)

Great, the chain is consistent. Note the earlier confusion resolved: on E={m=0}: $U(t) = \langle m,\tilde1_{[0,t]}\rangle = 0$ ∀t. Then Lemma A with $g = B^3$: $g\equiv0$ ⟹ $B\equiv0$. ✓

Also should double-check Lemma A hypothesis: g continuous — yes, B has continuous paths (H>0), so $B^3$ continuous. ✓

Also, in Lemma A I should allow the weaker hypothesis "$U_g$ constant" (not necessarily 0) since on E we derived $U\equiv0$ directly—but proving the more general statement costs nothing (same proof). Fine either way; I'll prove the general one.

Potential subtlety: On E, m=0 as element of $\mathcal H_H$. The map t ↦ ⟨m, \tilde1_{[0,t]}⟩ — fine. But is it legitimate that $U(t)$ (defined as an ordinary Lebesgue integral $\int_0^1 B_s^3R_H(s,t)ds$) equals $\langle m,\tilde1_{[0,t]}\rangle_H$? Justification: $t\mapsto\tilde1_{[0,t]}$ is continuous $\mathcal H$-valued (‖\tilde1_{[0,t]}−\tilde1_{[0,t']}‖² = R(t,t)+R(t',t')−2R(t,t') = ½|t−t'|^{2H}·2... let me compute: R(s,s)=s^{2H}; ‖\tilde1_{[0,t]}−\tilde1_{[0,t']}‖² = t^{2H}+t'^{2H}−2R(t,t') = |t−t'|^{2H}. ✓ continuous). Bochner integral commutes with continuous linear functionals: ⟨∫φ_tdt, v⟩ = ∫⟨φ_t,v⟩dt. ✓ So $U(t)=⟨m,\tilde1_{[0,t]}⟩$ always. ✓

Now the density-of-smooth-functions-in-$\mathcal H$ question (patch #3 in notes) — turns out NOT needed anymore since we bypassed the test-function pairing! Nice simplification. The only analytic facts about $\mathcal H_H$ needed:
- It's a Hilbert space with $\langle\tilde1_{[0,s]},\tilde1_{[0,t]}\rangle=R_H(s,t)$ — true by construction (RKHS of fBm; completion of span of indicators).
- Continuity of t↦\tilde1_{[0,t]} — shown above.
That's all! The proof never needs density of smooth functions, nor explicit descriptions of $\mathcal H_H$ in either regime. Excellent — much more robust than round 1's approach.

Bouleau–Hirsch criterion also only needs abstract $\mathbb D^{1,p}$ theory. For the Malliavin derivative of fBm: $D_sB_t = \tilde1_{[0,s]}(t)$ — standard (Nualart Ch. 5). Chain rule for $B_t^3$: $D_sb_t^3 = 3B_t^2\tilde1_{[0,t]}(s)$ hmm wait $D_s(B_t^3) = 3B_t^2D_sB_t = 3B_t^2\tilde1_{[0,t]}(s)$. Then $D_sZ = \int_0^1 4B_t^3\tilde1_{[0,t]}(s)dt$. To justify interchange of Malliavin derivative and dt-integral: standard dominated convergence in $\mathbb D^{1,p}$: $E\int_0^1\|D(B_t^4)\|^p_Hdt <\infty$ etc. Fine.

Let me also double check $R_H(0,t)=0$: $R_H(0,t) = ½(0+t^{2H}−t^{2H}) = 0$ ✓.

Now, one more important check on Step 1 (ladder) — the case β ∈ (0,1] more carefully. We have V ∈ C¹([0,1]), V(s) = As^β + D on [0,1]. V'(s) = βAs^{β−1} on (0,1]. Also V'(s) = β[J₊(s)−J₋(s)]. As s→0⁺: J₊→0 monotonically-ish (bound ‖g‖∞s^β/β), J₋→M₁:=∫₀¹t^{β−1}g(t)dt (finite: |g|≤G, ∫₀¹t^{β−1}dt = 1/β). So lim V' = −βM₁. If β<1: βAs^{β−1}→±∞ unless A=0; if A≠0 contradiction with finite limit. If β=1: V'(s) = A for all s; limit s→0⁺ of J₊−J₄... J₊(s)→0, J₋(s)→∫₀¹g = A, so A = V'/β = (J₊−J₋)|_{0⁺}·(1/1)... V'(0⁺)=−A, but V'≡A, so A=−A, A=0 ✓.

Case β∈(1,2): V∈C², V''(s) = β(β−1)As^{β−2} on (0,1], and V''(s) = β(β−1)[K₊+K₋]; s→0⁺: K₊→0, K₋→M₂:=∫₀¹t^{β−2}g(t)dt finite (β−2∈(−1,0)). If A≠0: RHS→±∞ ≠ β(β−1)M₂ finite. Contradiction ⟹ A=0 ✓.

All good. Also note: we should make sure the differentiation-under-integral claims are airtight, including at every s∈(0,1] and the DCT dominators. Will write carefully in the proof.

Additionally, I realize there might be an even more elementary finish for Step 3 avoiding Laplace transforms: With A=0, we have $\mathcal V(s) = D$ constant... wait no! With A=0 the original equation reads $\mathcal V(s) = D$, i.e., the Riesz-type potential of g is CONSTANT. Hmm, and then $\mathcal E = \int g\mathcal V = D\cdot A = 0$ ✓ consistent. Is there a direct proof that $\mathcal V \equiv D$, g continuous ⟹ g≡0? Fourier: $\widehat{|x|^\beta g}$... On the line: extend g by 0; $\hat{\mathcal V}(\xi) = \hat g(\xi)\cdot\widehat{|x|^\beta}(\xi)$ (distributionally; $\widehat{|x|^\beta} = c|\xi|^{-1-\beta}$ distribution). $\mathcal V \equiv D$ on (0,1) but g supported in [0,1] so $\mathcal V$ compactly supported... $\mathcal V\equiv D$ on [0,1] and outside? $\mathcal V(x)$ for x>1: $\int_0^1(x-t)^\beta g(t)dt$ — not constant out there. Messy; Laplace route is clean enough. Alternatively use the strict conditional negative definiteness as the notes did. Same thing. Keep Laplace.

Alternative cleaner Step 3 (avoid distributions): already have it. Good.

Now, ANOTHER alternative for Step 3 that's even more elementary — energy/positive-definiteness trick: Consider $g_\lambda(x) = g(x) - \lambda$... no, keep Laplace.

Let me also sanity-check the Laplace-representation-based identity numerically later.

Also, potential objection: In Step 3, we need $A=0$ AND $\mathcal E=0$. Both established. And strict negativity needs $g\not\equiv0$ ⟹ ∫ξ^{-1-γ}|\hat g|²>0 over (0,∞). Shown via holomorphy + isolation of zeros. Solid. (Even simpler: $\hat g$ real-analytic on ℝ; if it vanished on a set of positive measure it'd vanish identically; injectivity of FT ⟹ g≡0.) ✓

Now let me also think about whether the theorem statement needs "for all H∈(0,1)" — the analysis notes said the problem's exact quantification is uncertain but round 1 proceeded with "all H∈(0,1)". I'll answer: YES for every H∈(0,1). This matches known literature (e.g., Hu–Nualart 2005-ish results on $\int B^4$; actually there IS literature: "Density of the integral of fBm powers"... I recall Nualart–Üstünel? Anyway, self-contained proof stands on its own).

Extra rigor points to include:
- $Z\in\mathbb D^{1,p}$: show $E\|DZ\|^{p} < \infty$: $\|DZ\| \le 4\int_0^1|B_t|^3\|\tilde1_{[0,t]}\|dt \le 4\int_0^1|B_t|^3t^Hdt$; $E|B_t|^{3p}\le Ct^{3Hp}$; ∫₀¹ t^{3Hp}·... fine.
- Chain rule application pointwise in t then Fubini—use local property/DCT in D^{1,p}; cite Nualart Prop 2.1.10 hmm whatever, present cleanly.
- Gaussian moment fact: $B$ centered Gaussian family ⇒ $E|B_t|^k \le C_k t^{kH}$ (since Var(B_t)=t^{2H}). ✓

Verification plan (Python):
A. Symbolic (sympy):
 1. Energy identity with polynomial test functions & several rational H (H=1/4,1/2,3/4 → γ=1/2,1,3/2): compute Q, A, C, E symbolically via exact integration of polynomials × |s−t|^γ — hmm |s−t|^γ symbolic integration with fractional γ: sympy can do ∫∫ over triangle splitting s<t: polynomial × (t−s)^γ integrable symbolically for rational γ. Doable: split domain, integrate. Or numerically high precision (mpmath 50 digits) comparing both sides — safer. I'll do high-precision numeric checks for identities, and exact symbolic where easy.
 2. Ladder formulas: verify $V'(s) = \beta\int sgn·|s−t|^{β−1}g$ numerically vs finite differences for random g, various β. And second derivative similarly for β>1.
B. Lemma A end-to-end numerical test (discretized): grid n=200, Clenshaw/trapezoid quadrature, matrix T_ij = R_H(s_i,t_j)w_j; minimize ‖Tg − mean(Tg)·1‖ over unit-norm g (smallest singular value of centered operator); check σ_min > 0 substantially for many H; ALSO check with the pure potential operator |s−t|^γ mod span{s^γ,1}. Expect smallest singular value comfortably positive (~O(n^{-something})) — just need clearly nonzero vs machine noise.
C. Strict negativity: random smooth g with A=0 (project: g ← g − mean), compute $\mathcal E_{2H}(g)$ by quadrature, verify < 0 for many draws & many H. Also verify the Laplace identity numerically.
D. Stochastic MC: simulate fBm (Cholesky, n=512) for several H, N=2000 paths; pathwise compute $Q(B^3)$; report min/Q·scale; verify $\|DZ\|^2 = 16Q$ identity pathwise for H=1/2 (where both sides computable independently); histogram of Z showing smooth-looking empirical density; two-sample check maybe unnecessary.
E. Optional: sympy check that for H=1/2 the classical argument's identity holds.

Also verify Step 2 consequence numerically: for discretized Lemma A solutions with A forced... skip, B covers.

Let me also decide the final answer format: full proof.md with:
- Statement, answer boxed: YES for all H∈(0,1).
- Proof Part 0: setup & notation.
- Part 1: Malliavin machinery & reduction (steps 1–5 as above).
- Part 2: Lemma A with full details (Steps 0–3).
- Part 3: conclusion.
- Verification section listing all computational checks with scripts/results.
- Remarks: H=1/2 classical special case; stronger smoothness known but not needed; comparison to round-1 plan (assembled as instructed).

Before writing, run the verifications. Let me start coding.

Plan the code:

```python
# check1_laplace.py
import mpmath as mp
mp.mp.dps = 50
for gamma in [0.25, 0.5, 1.0, 1.5, 1.75]:
    c = 1/mp.quad(lambda u: (1-mp.cos(u))*u**(-1-gamma), [0, 1, mp.inf])
    # check |x|^gamma = c * int_0^inf (1-cos(xi x)) xi^{-1-gamma} dxi
    for x in [0.3, 0.7, 1.3]:
        val = c*mp.quad(lambda xi: (1-mp.cos(xi*x))*xi**(-1-gamma), [0,1,mp.inf])
        print(gamma, x, float(val - abs(x)**gamma))
```

```python
# check2_energy_identity.py: Q(g) = A*C - 0.5*E2 for random polys g, several H (high-precision quadrature)
```

```python
# check3_ladder.py: random C^1-ish g (polys), beta in {0.3,0.7,1.0,1.3,1.9}: 
#   V(s)=∫|s-t|^β g; compare derivative formulas with high-order finite differences;
#   also verify V'(0+), V''(0+) limits equal -β M1, β(β-1) M2.
```

```python
# check4_lemmaA_discrete.py: 
for H in np.linspace(0.05,0.95,19):
    n=300 grid, weights trapezoid; T[i,j]=R_H(si,tj)*wj
    center: S = T - row_means? We want inf over g≠0 of ||Tg - c1|| minimized: 
    equivalent: smallest singular value of P T where P projects orthogonal to span{1}.
    sigma_min = svd(P T)[1][-1]; record. Expect >> 1e-10.
```

Also potential-only version: T2[i,j]=|si−tj|^γ wj, project against span{1, s^γ}.

```python
# check5_negative_definite.py:
rng draws g = random smooth combos; enforce mean zero; compute E2 = ∫∫ g g |s−t|^γ via 2D quadrature (n=400, use symmetry & matrix ops); assert < −tol.
```

```python
# check6_fbm_mc.py: Cholesky fBm sim, H in {0.3,0.5,0.7}; N=3000 paths n=256.
# pathwise Q(B^3) via Riemann; report min over paths, ratio to typical scale;
# for H=0.5 also compute LHS = ∫ (∫_s^1 B^3)^2 ds *16 and compare to 16Q (identity check);
# histogram Z.
```

Also a check for the reduction's pathwise claim "on {Q=0}, U≡0": trivially linear algebra (U = T g_row...). Skip—logic, not numerics.

Let me also double check the claim $\langle\tilde 1_{[0,t]}-\tilde1_{[0,s]},\cdot\rangle$... done above: norm² = |t−s|^{2H}. ✓

One more theoretical detail: Bouleau–Hirsch precise statement to cite: Nualart (2006) Theorem 2.1.3: Let $F = (F^1,...,F^d)$ ... for d=1: "Assume $F\in\mathbb D^{1,p}$, p>2? ..." Hmm versions vary: The common criterion (Nualart Thm 2.1.3): If $F\in\mathbb D_{loc}^{1,p}$ for some p>1 and $P[\|DF\|_H=0]=0$... hmm actually I recall: Theorem 2.1.3 in Nualart's book (2nd ed): "Let $F_i \in \mathbb D_{loc}^{1,p}$... suppose det Γ_F > 0 a.s. Then law has density..." — that's the local criterion. And there's an earlier global one (Prop 2.1.1?): hmm. There are two standard statements:
(a) If $F\in\mathbb D^{1,p}$, p>1, and $E[\|DF\|_H^p]>0$... no.
(b) Bouleau–Hirsch: $F\in\mathbb D^{1,p}$, p>1, then the measure $P_F\circ\|DF\|^{-1}$... The cleanest citable: Nualart, The Malliavin Calculus, Proposition 2.1.1: hmm not sure of numbers. Safer: state the criterion generically: "Bouleau–Hirsch criterion (see Nualart, The Malliavin Calculus and Related Topics, 2nd ed., Thm 2.1.3; or Nualart, Stochastic Process. Appl. 120 (2010) survey): if $F\in\mathbb D^{1,p}$ for some p>1 and $P(\|DF\|_{\mathcal H}>0)=1$, then the law of F is absolutely continuous w.r.t. Lebesgue measure." This is definitely a true standard theorem. To be safe I can sketch its proof briefly: $1_{\{|F|\le R\}}$... the standard trick: for a.e. path, consider $\theta_\epsilon(F)$... Actually the standard proof: Let φ ∈ C_c^∞. Then $E[\varphi'(F)] = E[\langle DF, -\ldots\rangle]$... The classic: choose $\psi_\epsilon$ approximating $1/\|DF\|^2$ truncated; then density formula $E[\varphi(F)] = E[\varphi'(F)\|DF\|^2\cdot\frac{1}{\|DF\|^2}]$... I'll include a short proof of the criterion for completeness (it's short):

Criterion proof sketch (global version): Suppose $F\in\mathbb D^{1,p}$, p>1, and $\|DF\|>0$ a.s. Define for ε∈(0,1): $\Psi_\epsilon = \|DF\|^2(\|DF\|^2+\epsilon)^{-1}$ hmm. Standard approach: Let $\alpha(x) = (|x|^2+\epsilon)^{-1}$... We want to show: for every φ∈C_c^∞(ℝ), $|E[\varphi(F)]| \le C_\varphi\cdot Leb(\text{supp}\varphi)$-ish implying density. Standard argument: for interval [a,b], $E[1_{[a,b]}(F)]$... hmm the cleanest: 

Take φ∈C_c^∞. Integration by parts (duality relation): $E[\varphi(F)\|DF\|^2\alpha(F)]$ hmm. Let me recall the textbook proof of Thm 2.1.3-style global criterion:

For $F\in\mathbb D^{1,2}$ with $\|DF\|>0$ a.s.: define $G_\epsilon = F$-independent? No—define $h_\epsilon = \|DF\|^2(\|DF\|^2\vee\epsilon)^{-1}$... Actually here's the standard one (from Nualart's book, proof of Thm 2.1.3): Set $\alpha_\epsilon(x)=(x^2+\epsilon)^{-1}$. Then consider $\varphi\in C_c^\infty$, and
$E[\varphi(F)] = E[\varphi(F)\|DF\|^2\alpha_\epsilon(\|DF\|)] + E[\varphi(F)\epsilon\alpha_\epsilon(\|DF\|)]$.
First term: duality: $= E[\varphi'(F)\cdot(\text{stuff})]\le\|\varphi'\|_\infty E[\|DF\|\alpha_\epsilon(\|DF\|)\cdot\|DF\|]$... hmm getting the bound independent of ε: $E[\|DF\|^2\alpha_\epsilon(\|DF\|)]\le 1$. So first term ≤ ‖φ'‖∞. Second term: $E[\varphi(F)\epsilon\alpha_\epsilon(\|DF\|)] \to 0$ as ε→0 by dominated convergence (pointwise →φ(F)·1_{\|DF\|>0}=φ(F)·1... wait εα_ε(x) = ε/(x²+ε) → 0 pointwise, dominated by |φ(F)|·ε/x²... hmm domination: ε/(x²+ε) ≤ 1, so dominated by |φ(F)| ✓, pointwise limit 0 since x>0 a.s.). So $|E[\varphi(F)]|\le\|\varphi'\|_\infty$. Hmm that shows the law has "bounded variation dual"? Actually $|E[\varphi(F)]|\le\|\varphi'\|_\infty$ implies the law of F is absolutely continuous with density in BV? Precisely: the map φ↦E[φ(F)] extends to a bounded functional on W^{1,∞}_0... Standard conclusion: μ law of F satisfies |μ̂-type bound|... The implication: for any interval I=(a,b): approximate 1_I by φ_n with φ_n'=n on I shrinking... gives μ(I) ≤ |b−a|·sup-density... Actually simplest: |E[φ]|≤‖φ'‖_1? Let me redo: we got |E[φ(F)]| ≤ ‖φ'‖_∞. Take φ = smoothed indicator of (a,b) with Lipschitz const 1/(b−a): then μ((a,b)) ≤ 1 + ... hmm yields μ(I) ≤ C|I| + o? Let me instead do it properly: the inequality |E[φ(F)]| ≤ ‖φ'‖∞ for all φ∈C_c^∞ implies (by taking φ approximating sign-changed... ) that μ has finite total variation as a distribution, i.e., μ is a signed measure — it already is (probability). Hmm, the right conclusion: For any open set O = ∪I_k disjoint intervals: μ(O) ≤ Σ μ(I_k); and μ(I) ≤ inf{‖φ'‖∞ : φ=1 on I} = 1/|I|?? That gives μ(I) ≤ 1/|I| — useless for small intervals... 

Hold on, I think the standard proof gives |E[φ′... let me look at it again. Actually the correct standard statement & proof (Nualart Thm 2.1.3 in 1st ed / Thm 2.1.2 2nd ed?) is for the LOCAL criterion with det Γ > 0 off a set. The GLOBAL criterion usually stated: If $E[\|DF\|^2] > 0$... no.

Hmm, let me recall properly. The cleanest global criterion with proof I'm confident about:

**Proposition**: Let F ∈ 𝔻^{1,p} for some p>1 (say p=2), with P(‖DF‖>0)=1. Then F has a density.

Proof: Fix φ∈C_c^∞. For ε>0 set $H_\epsilon := \frac{\|DF\|^2}{\|DF\|^2+\epsilon}$. By the duality relation,
$$E[\varphi(F)H_\epsilon] = E[\varphi'(F)\,?]$$ 
no wait. Duality: $E[\langle DF, D(\varphi(F)h)\rangle]$ hmm. Let me use the divergence formulation: For any r.v. G in 𝔻^{1,2}... The standard trick (Nualart's book, proof of his Thm 2.1.3, which I've definitely seen): 

$E[\varphi(F)] = E\left[\varphi(F)\frac{\|DF\|^2}{\|DF\|^2+\epsilon}\right] + E\left[\varphi(F)\frac{\epsilon}{\|DF\|^2+\epsilon}\right]$.

Second term → 0 (DCT, since ‖DF‖>0 a.s.).

First term: apply duality with $D(\varphi(F)) = \varphi'(F)DF$: Write $\varphi(F)H_\epsilon = \varphi(F)\|DF\|^2\alpha_\epsilon(\|DF\|)$ where α_ε(x)=(x²+ε)^{-1}. Hmm, duality relates E[⟨DF, DV⟩] = E[Vδ(DF)]... δ(DF) isn't defined for general F∈𝔻^{1,2} (need F∈𝔻^{1,4}-ish for δ(DF)... Skorohod integral δ(DF) exists when F∈𝔻^{1,2} and E‖DF‖²<∞? δ(u) defined for u∈L²(Ω;H); δ(u) exists iff E[δ...] hmm, δ(u) requires u ∈ Dom δ ⊇ {u ∈ 𝕃^{1,2}}. For u = DF with F ∈ 𝔻^{2,2}... we only have 𝔻^{1,p}. Hmm!)

OK here's the resolution: the standard criterion (Bouleau–Hirsch 1991; Nualart book Thm 2.1.3 2nd edition) is stated for $F\in\mathbb D_{loc}^{1,p}$, p>1, and the proof uses localization + the technique with $F_\epsilon := F\cdot$hmm. Let me just remember the ACTUAL statement in Nualart 2nd ed:

**Theorem 2.1.3** (Nualart 2nd ed.): Let $F=(F^1,\dots,F^d)$ be a random vector satisfying: (i) $F^i \in \mathbb D_{loc}^{1,p}$ for some p>d... hmm I genuinely don't recall exactly; alternatives: Theorem 2.1.3: "Assume F ∈ 𝔻^{1,p}, p ≥ 2? and that ‖DF‖ > 0 a.s. Then the law of F is absolutely continuous and the density belongs to L^p..." 

There's also the widely-used **Proposition 2.1.1** hmm.

Rather than misquote numbering, I'll state the criterion by NAME with a self-contained proof. Let me construct the proof carefully with minimal hypotheses (F ∈ 𝔻^{1,p}, p>1, ‖DF‖>0 a.s.):

Standard proof (as in Bouleau–Hirsch book, Prop... and reproduced in many papers): For simplicity assume p≥1... Let φ∈C_c^∞(ℝ), and let ε∈(0,1). Put $\psi_\epsilon(x) = \frac{x}{x^2+\epsilon}$ hmm. Here's a clean version I'm confident in (used in e.g. Cheridito–Kronmal? or in Petrou 2008, "On the regularity of the distribution of generalized Wiener functionals"—Petrou's Prop 2.1? Petrou states: F∈𝔻^{1,p}, p>1... hmm Petrou needs higher for smoothness).

Cleanest rigorous route with F ∈ 𝔻^{1,p} for ALL p (which we have!): use the divergence-based IBP:

Since F ∈ 𝔻^{1,p} ∀p<∞, we have u := DF/F-factor... Define $v := DF\cdot\alpha_\epsilon(\|DF\|)$ where α_ε(x)=(x²+ε)^{-1}. Then v ∈ 𝕃^{1,q} ∀q. Claim: δv exists. Indeed sufficient condition: u ∈ 𝕃^{1,2} (i.e., E[∫∫ ... ] finite) — for the general Malliavin calculus over Hilbert space H, δ is defined on the closure of smooth cylindrical gradients in 𝕃²(Ω;H); membership: v is L²(Ω;H) ✓ bounded even. Existence of δ(v): v ∈ Dom δ if v ∈ 𝕃^{1,2} (isomorphic image). Is every L²(Ω;H) rv in Dom δ? NO—Dom δ ⊊ L²(Ω;H). BUT: v = DF·α_ε: there's the classical result: if F∈𝔻^{1,r} for r>2? hmm: DF ∈ Dom δ whenever F ∈ 𝔻^{1,p} with p>2? The known result: for F ∈ 𝔻^{1,p}, p>2 hmm... Actually: **if F ∈ 𝔻^{1,p} for some p>2, then DF ∈ Dom δ and δ(DF) = ... ** hmm is that right? The standard sufficient condition: u ∈ 𝕃^{1,2} means E[δ(u)²]... circular. The real standard: if u ∈ 𝕃^{1,2} (norm: E[‖u‖² + ‖Du‖_{HS}²]) then u∈Domδ. For u = DFα_ε(‖DF‖): Du involves D²F — not available.

Alternative standard approach avoiding δ: **the "substitution"/Cameron–Martin-free IBP via the criterion's own classical proof**: Bouleau–Hirsch's actual argument uses the characterization of absolute continuity via $P(F\in dx)$ and Steen's lemma? Their book "Malliavin Calculus with respect to Lévy..." no—"Analysis on Wiener space" hmm. 

Honestly the most practical citation-safe approach: **strengthen our hypotheses**: we can easily show Z ∈ 𝔻^{1,p} ∀p AND in fact Z ∈ 𝔻^{2,p}? Z = ∫B⁴: D²Z involves products B²·R̃ — fine, Z ∈ 𝔻^{2,p}∀p, even 𝔻^{∞} (Malliavin-smooth: all derivatives exist, polynomial growth). Indeed B is infinitely Malliavin-differentiable (DB_t = 1̃_{[0,t]}, D²B_t = 0!), so B_t^4 ∈ 𝔻^∞ with uniform-in-t bounds; Z ∈ 𝔻^{k,p}∀k,p. THEN the standard **Nualart Theorem 2.1.3 (2nd ed.)** hmm which needs... you know what, the cleanest fully-standard reference statement I'm 100% sure of:

**Nualart, The Malliavin Calculus and Related Topics, 2nd ed., Theorem 2.1.3**: "Let F = (F¹,…,F^d) be a random vector whose components belong to 𝔻^{1,p} for some p> d... hmm no.

Let me instead cite the criterion as commonly used in the fBm literature, e.g., in papers on densities of fBm functionals: "**By the Bouleau–Hirsch criterion (cf. Nualart (2006), Theorem 2.1.3), since Z ∈ 𝔻^{1,2} and P(‖DZ‖_H = 0) = 0, the law of Z is absolutely continuous with respect to Lebesgue measure.**" — This usage pattern appears in dozens of papers; Theorem 2.1.3 in Nualart 2nd ed. is indeed (I'm now fairly confident) the criterion "If F ∈ 𝔻_{loc}^{1,p}, p>1, and P(‖DF‖_H = 0) = 0, then the law of F is absolutely continuous w.r.t. Lebesgue measure" — hmm, actually I recall Thm 2.1.3 being stated for random vectors with the condition on the determinant of the covariance matrix being ≠ 0 a.s., concluding density. Either way, both forms are TRUE theorems in that vicinity; and to be maximally safe I'll provide a complete self-contained proof of the 1-D global criterion I need. Let me nail such a proof NOW (important to get right):

**Lemma (IBP/density criterion).** Let F ∈ 𝔻^{1,p} for all p < ∞ (more than enough), with ‖DF‖_H > 0 a.s. Then law of F has a density; moreover density ∈ L^p ∀p? (won't claim more than existence + maybe L¹... claim existence.)

**Proof**: Step A: reduce to bounded F: replace F by ρ(F) hmm or just work with truncations: fix R>0 and let η_R ∈ C_c^∞, η_R = 1 on [−R,R]. Consider F_R = Fη_R(F)?? Simpler: prove the IBP formula for test φ and then conclude.

Core IBP claim: for every φ ∈ C_c^∞(ℝ):
$$\big|E[\varphi(F)]\big| \;\le\; \|\varphi'\|_\infty \; E\big[\|DF\|\,\big] \quad??? $$
Hmm that would need the duality with a bounded inverse-gradient factor, requiring δ. Let me think about the actual mechanism used in proofs of Thm 2.1.3-type results WITHOUT δ:

The trick in Nualart's book (proof of Thm 2.1.3, 2nd ed. — now I really do recall this): he considers $F \in 𝔻^{1,p}$, p>1 hmm, and proves: the measure μ∘F⁻¹ assigns to sets... He uses the auxiliary random variable $G = F$ and the function... AH WAIT. I remember now! The proof of the 1-D criterion in Nualart's book (Thm 2.1.3, and similarly in Sanz-Solé's lectures) goes through the **characteristic-function / Fourier** route OR through the following **"sweeping" argument**:

For a.e. ω with ‖DF(ω)‖>0, consider the map... no.

THE STANDARD PROOF (I'm reconstructing from Petrou (2008) SPA paper, Prop. 2.1, which follows Nualart Thm 2.1.3): 

Let φ∈C_c^∞. For ε∈(0,1), define $F_\epsilon := F + \epsilon\langle DF/\|DF\|, W\rangle$?? no...

Hmm, alternatively the **finite-dimensional projection argument** (Bouleau–Hirsch style): Work on Wiener chaos expansion... 

You know what — there's a MUCH simpler classical device for our SPECIFIC situation, avoiding the general criterion entirely: 

**Direct IBP via Malliavin integration by parts with a cleverly built auxiliary variable.** We know Z ∈ 𝔻^{n,p} for ALL n,p (infinitely smooth in Malliavin sense). Then the FULL Nualart machinery applies: if additionally $E[\|DZ\|^{-q}]<∞$ for some q... but we DON'T have control of negative moments of ‖DZ‖ (that's the hard part in general!). However—for mere EXISTENCE of a density (no smoothness claim), the criterion needs no negative moments. 

OK here is a fully self-contained, elementary proof of the existence criterion that I can write with confidence, using only: F ∈ 𝔻^{1,2}... hmm, actually here's one I'm sure about — the **add-one-parameter / Gaussian-shift ("Blumenthal–Getoor–McKean / Bismut–Elworthy–Kunita") method**, specialized to Wiener space with H = the Cameron–Martin space. But for fBm, the underlying isocameration is Brownian; F = Z is a functional of the Brownian path too? fBm with H≠1/2 is NOT a functional of BM over fixed horizon in an obvious way... Volterra: B_t = ∫W K(t,u)du — yes! fBm IS a (Volterra) functional of Brownian motion: $B_t = \int_0^t K(t,s)dW_s$. So the whole system lives on classical Brownian Wiener space (Ω, W), and Malliavin derivative w.r.t. W: $D^W_rB_t = K(t,r)1_{r≤t}$, and $D^W_s Z = \int_0^1 4B_t^3 D^W_sB_tdt = 4\int_s^1 B_t^3K(t,s)dt$. And ‖D^WZ‖_{L²[0,1]} ≥ ... related to ‖DZ‖_H: indeed D^WZ = K*DZ-ish: $\|DZ\|_{\mathcal H_H} = \|K^{-1}DZ\|$... and ‖D^WF‖_{L²} = ‖D F‖_{𝓗_H} when K is an isometry-ish: $\langle K h_1, Kh_2\rangle_{L²}$ hmm: 𝓗_H = K(L²[0,1]) with ‖Kh‖_𝓗 = ‖h‖_{L²}. And D^W_sF = ∫... relationship: D^WF = K(K^{-1}DF)?? Standard: $D^W F = K^*{}^{-1}$... For F = f(B): D_FB = K as operator: D_F B_t = K(·,t) as function of the W-variable r: D^W_rB_t = K(t,r)1_{r≤t}. Then ‖D^WF‖²_{L²(dr)} = ‖D_FF‖²_{𝓗_H} — is this exactly true? For F=f(B_{t₁}): D^W_rF = f'K(t₁,r); ‖·‖²_{L²} = f'²∫K(t₁,r)²dr; ‖D_FF‖_𝓗 = |f'|‖K 1_{[0,t₁]}... ‖·‖_𝓗 = |f'|·‖tilde1_{[0,t₁]}‖ = |f'|t₁^H. And ∫K(t₁,r)²dr = t₁^{2H} = variance of B_{t₁} ✓ EQUAL. In general for multiple t's: ‖D^WF‖² = aᵀ𝕂ᵀ𝕂a where 𝕂_{ij}... = ‖ΣaᵢK(tᵢ,·)‖²_{L²}; ‖D_FF‖²_𝓗 = ‖Σaᵢtilde1_{[0,tᵢ]}‖²_𝓗 = ΣaᵢaⱼR(tᵢ,tⱼ) = ‖K(a)‖²_𝓗 where (Ka)(t) = Σaᵢ... and 𝕂ᵀ𝕂 vs R: R(s,t) = ∫K(s,r)K(t,r)dr (Volterra rep!) ✓ so EQUAL. Great: ‖D^WF‖_{L²(W-dr)} = ‖D_FF‖_{𝓗_H} for all cylinder F, extends by closure. 

So: **P(‖D^WZ‖_{L²} = 0) = P(‖DZ‖_𝓗 = 0) = 0.**

NOW apply the classical **Bismut–Elworthy–Li / Gaussian perturbation IBP on Brownian Wiener space** — but BE–Li needs directional derivative flows (SDEs). For general Wiener functionals, the right elementary tool is the **classical Malliavin–Stroock IBP with the Ornstein–Uhlenbeck... ** hmm still needs δ.

SIMPLEST CORRECT ELEMENTARY PROOF of existence criterion on CLASSICAL Wiener space, using only 𝔻^{1,2} + Gaussian shifts — the **"Gauss–Green on finite-dimensional projections"** method (this IS essentially Bouleau–Hirsch's argument; I can reconstruct it cleanly):

Setup: W = standard BM on [0,1], Ω = Wiener space. Malliavin derivative D (classical, L²[0,1]-valued). F ∈ 𝔻^{1,2}, θ := ‖DF‖ > 0 a.s. Goal: law of F ac.

Finite-dim approximation: For n, let π_n be projection onto first n chaos?? no—onto coordinates: identify W with (ξ₁,ξ₂,...) via Karhunen–Loève: W_t = Σ√λₖξₖeₖ(t), ξₖ iid N(0,1). Then F = f(ξ) a.s. for a measurable f: ℝ^ℕ→ℝ. Malliavin derivative ↔ gradient in Gaussian Sobolev sense: D_kF = ∂-weak-ξₖ. The Malliavin criterion says: if the "infinite-dimensional gradient" never vanishes, then distribution is ac.

Concrete elementary proof via **finite-dimensional conditioning + Fubini ("sweeping with one coordinate")** — the classical proof of Bouleau–Hirsch Thm (their Annales ENS 1981 paper? or their book with Hirsch, "Dirichlet Forms and Analysis on the Wiener Space", Prop. I.1.? — the KEY lemma is often called **"Steen's lemma"** or the **"integration by parts with respect to a one-dimensional projection"**):

Lemma (1-d sweeping): Let F ∈ 𝔻^{1,2}(ℝ^ℕ-Gaussian space), let u ∈ L²(Ω;H) hmm...

Honestly, let me just go with citing the criterion + giving the proof that's easiest to make airtight HERE. I think the cleanest airtight elementary proof for OUR case uses the **Fourier/characteristic function route with the Laplace-transform identity we ALREADY proved** — wait, actually, here's a thought: we've already done all the hard analysis in Lemma A. The remaining step is genuinely just quoting a standard theorem. Every serious reference (Nualart's book Thm 2.1.3; Cheridito–Nualart 2005?; Hu–Nualart; Petrou) states: **F ∈ 𝔻^{1,p}, p>1, P(‖DF‖=0)=0 ⟹ F has a density.** I am confident this is a true, standard theorem (it's Theorem 2.1.3 combined with the discussion in Nualart's book; also appears as Prop 5.5? in various lecture notes; also Bouleau–Hirsch book Theorem... ). For the writeup I'll:

- State the criterion precisely.
- Give a proof sketch with the main mechanism (the standard one): For φ∈C_c^∞(ℝ) and ε>0, set $G_\epsilon := \varphi(F)\,\theta_\epsilon$ where θ_ε = ‖DF‖²(‖DF‖²+ε)^{-1} ∈ [0,1]. Using the duality relation E⟨DG, DF⟩ = E[Gδ(DF)] — requires δ(DF) to exist: **justified because we may take F ∈ 𝔻^{1,p} ∀p and in fact we can invoke the standard result: DF ∈ Dom δ whenever F ∈ 𝔻^{1,p} for some p>2** — hmm, is THAT standard? The known result: **if u ∈ 𝕃^{1,2} then u ∈ Dom δ**; applying to u = DF: need F ∈ 𝔻^{2,2}. WE HAVE Z ∈ 𝔻^{2,2} easily (indeed 𝔻^{2,p}∀p)! So: restrict criterion to F ∈ 𝔻^{2,2}: then DF ∈ 𝕃^{1,2}, δ(DF) exists, and the duality E[⟨DF, DG⟩] = E[G·δ(DF)] holds for G ∈ 𝔻^{1,2} bounded-ish. 

Then the standard argument: 
E[φ(F)] = E[φ(F)(θ_ε + (1−θ_ε))] where 1−θ_ε = ε(‖DF‖²+ε)^{-1}.
Term2 = E[φ(F)ε/(θ²+ε)] → 0 by DCT (pointwise: since θ>0 a.s.; domination |φ(F)|). ✓
Term1: E[φ(F)θ_ε] = E[φ(F)‖DF‖²α_ε] where α_ε := (‖DF‖²+ε)^{-1} ≤ 1/ε bounded, and α_ε depends on DF... Apply duality with G := φ(F)‖DF‖α_ε hmm: want E[⟨D(φ(F)), DF·α_ε·‖DF‖⟩]... Let me define G_ε := φ(F)·β_ε where β_ε := ‖DF‖(‖DF‖²+ε)^{-1/2}·... I'll do it cleanly:

Set $Y_\epsilon := \varphi(F)\,\frac{\|DF\|^2}{\|DF\|^2+\epsilon}$. Then ⟨DY_ε, DF⟩ = φ'(F)⟨DF,DF⟩·θ_ε + φ(F)·⟨Dθ_ε, DF⟩. Messy but bounded: |⟨Dθ_ε,DF⟩| ≤ ... θ_ε = ψ(‖DF‖²), ψ(u)=u/(u+ε), ψ'(u) = ε/(u+ε)², D‖DF‖² = 2⟨DF,D·DF⟩, so |⟨Dθ_ε,DF⟩| ≤ [ε/(‖DF‖²+ε)²]·2‖DF‖‖D²F‖_HS·‖DF‖ ≤ 2‖D²F‖_HS·[ε‖DF‖²/(‖DF‖²+ε)²] ≤ 2‖D²F‖_HS/4 hmm ε·u/(u+ε)² ≤ 1/4. So |⟨Dθ_ε,DF⟩| ≤ ½‖D²F‖_HS. Fine—all terms controlled since Z ∈ 𝔻^{2,2} with bounded moments. 

Duality: E[Y_ε·δ(DF)] = E[⟨DY_ε, DF⟩]. So E[Y_ε·δ(DF)] = E[φ'(F)‖DF‖²θ_ε + φ(F)⟨Dθ_ε,DF⟩].
Thus E[φ(F)‖DF‖²θ_ε] = E[(δ(DF)−⟨Dθ_ε,DF⟩)·φ(F)] hmm wait rearrange:
E[φ'(F)‖DF‖²θ_ε] = E[Y_ε δ(DF)] − E[φ(F)⟨Dθ_ε,DF⟩].
And E[φ(F)‖DF‖²θ_ε] = E[φ(F)‖DF‖²] − E[φ(F)‖DF‖²(1−θ_ε)] = E[φ(F)‖DF‖²] − E[φ(F)‖DF‖²ε/(‖DF‖²+ε)]; the subtracted term → 0 (DCT, |dominator| ≤ ‖φ(F)‖·‖DF‖² bounded by integrable). 

Hmm, this is getting somewhere but the δ(DF) term isn't obviously harmless (δ(DF) is some L² rv, fine, but I need to bound E[φ(F)δ(DF)]-ish uniformly in ε...). Let me simplify: rather than θ_ε, use the DIRECT approach with α_ε = (‖DF‖²+ε)^{-1}:

Define $G_\epsilon := \varphi(F)\,\alpha_\epsilon\,\|DF\|^2 = Y_\epsilon$ same thing. OK alternative cleaner standard presentation (this is EXACTLY the proof of Nualart Prop. 2.1.1?? hmm). 

You know what, let me look at this from a totally different angle: **there is a beautifully elementary proof of the existence-criterion via characteristic functions using the Gaussian integration-by-parts on FINITE-DIMENSIONAL projections + monotone passage**. This is Bouleau–Hirsch's actual method ("Corollaire de densité" via "lemme de Steen"?). Reconstruction:

Identify Ω ≅ ℝ^ℕ (iid Gaussians ξₖ) as above; F = f(ξ). Malliavin derivative: DF = (D_kF)_k, D_kF = weak partials in the Gaussian-Sobolev sense, Σ D_kF² = ‖DF‖² a.s.

Claim: if Σ_k(D_kf)² > 0 a.s. then f's law is ac. 

Proof idea: For n ≥ 1, decompose ξ = (ξ', η) with ξ' = first n coords, η = rest. Conditional on ξ': F = f(ξ',·) as function of η — hard to say anything (depends on η in unknown way). The BH trick instead: **perturb along ONE well-chosen direction in the η-coordinates**: Since Σ_k D_kF² > 0 a.s., for each ω there EXISTS k with |D_kF(ω)| > 0. Define random index... measurability issues (choosing k depending on ω breaks independence). BH's actual trick ("épuisement"): none needed—here's the CLEANEST modern reconstruction, the **"random direction" trick**: 

Let Θ be an RV independent of ξ, uniform on the sphere S^{n−1}... but D_kF involves all k. Hmm, truncate: θ_n² := Σ_{k≤n}D_kF² ↑ ‖DF‖² > 0 a.s. For FIXED n: consider the directional derivative along Θ_n (uniform on S^{n−1}, independent): G_n := Σ_{k≤n}ΘₖD_kF. E[G_n² | F-part] = θ_n²/n. So P(G_n ≠ 0 | ...) ≥ ... For fixed n, consider the map T_n: ξ ↦ ξ + tΘ_n e (adding t in direction Θ_n of the first n coords): Gaussianity: ξ + tΘ_ne ~ still iid N(0,1) vector (rotation of first n coords preserves the law!). So for any bounded measurable h: E[h(f(ξ₁,...,ξₙ,ξₙ₊₁...))] = E[h(f((ξ+tΘ)₁..ₙ, ξₙ₊₁,...))] — i.e., the law is invariant under the rotation-mix. Then differentiate in t at t=0?? Requires differentiability of f along that direction — only a.e./weak available. The Gaussian IBP saves us: for smooth cylinder h... 

This is the actual BH mechanism ("méthode de l'isocamération"): rotate within the first n coordinates by angle proportional to... The conclusion they draw: the law of F restricted to... they prove: for a.e. finite-dim projection... 

I've spent long enough reconstructing from memory. DECISION: In proof.md, state the Bouleau–Hirsch existence criterion as a cited theorem (Nualart 2006, Thm 2.1.3 — this citation is extremely common in the fBm literature for exactly this use; e.g., "by the criterion of Bouleau–Hirsch (see Nualart, Thm 2.1.3)"), and include a **complete proof of a slightly stronger hypothesis version that I CAN make airtight**: since we have Z ∈ 𝔻^{n,p} ∀n,p, I can prove existence of density via the **standard IBP formula** route:

**Self-contained criterion (strong-hypothesis version).** Suppose F ∈ 𝔻^{1,p} ∀p<∞ and moreover DF ∈ Dom δ with E[|δ(DF)|^p]<∞ ∀p (automatic if F ∈ 𝔻^{2,p} ∀p, since then DF ∈ 𝕃^{1,p}∀p and Dom δ ⊇ 𝕃^{1,2}... careful: 𝕃^{1,2}-membership of DF means E[‖DF‖² + ‖D²F‖²_HS] < ∞ ✓ we have it). Then P(‖DF‖>0)=1 ⟹ density exists.

**Proof**: Fix φ ∈ C_c^∞(ℝ). For ε ∈ (0,1), set α_ε := (‖DF‖² + ε)^{-1} (bounded, and α_ε → 1/‖DF‖² a.s.), and note α_ε ∈ 𝔻^{1,q} ∀q with ‖Dα_ε‖ ≤ 2‖DF‖·‖D²F‖_HS/ε²·... |Dα_ε| = |ψ'(‖DF‖²)|·2|⟨DF,D‖DF‖... |: ψ(u) = (u+ε)^{-1}, ψ'(u) = −(u+ε)^{-2}, so ‖Dα_ε‖ ≤ 2‖DF‖‖D²F‖/(‖DF‖²+ε)² ≤ 2‖DF‖‖D²F‖/ε² — fine, all moments finite (using F∈𝔻^{2,p}∀p and ‖DF‖ ≤ 1/√ε bounded... even simpler: α_ε ≤ 1/ε so everything bounded by powers of 1/ε — finiteness uniform enough for the limit argument below? The limit argument takes ε→0 at the END with dominating rv independent of ε — need care: terms like E[|⟨Dα_ε,DF⟩||φ(F)|] ≤ (2/ε²)E[‖DF‖²‖D²F‖|φ(F)|] — blows as ε→0! Bad domination. FIX: use the standard trick of bounding BEFORE taking limits differently: 

Standard resolution (as in Nualart's actual proof of Thm 2.1.3 — NOW I remember the mechanism! He uses the LOCAL version with the open sets where ‖DF‖ stays away from 0, plus a covering argument): 

**Localization**: Let A_m := {‖DF‖ > 1/m}. These increase to a full-measure set. On A_m, define α_{ε} with ε = 1/m² say: β_m := (‖DF‖² + m^{-2})^{-1}1_{A_m}... and use the LOCAL criterion: E[φ(F)1_{A_m}·stuff]. The cleanest: prove: **μ(F ∈ dx ∩ A_m-event...)**: For each m: |E[φ(F)1_{A_m}]| ≤ C_m‖φ'‖_∞ where C_m = E[1_{A_m}·(1 + |δ(DF)|·...)]. Then since 1_{A_m}↑1: |E[φ(F)]| ≤ C_m‖φ'‖_∞ for EVERY m, and letting m→∞ needs sup_m C_m < ∞ — NOT guaranteed a priori... BUT actually C_m → E[stuff on full set] by monotone/bounded conv: C_m = E[1_{A_m}W] with W := (1 + |δ(DF)|)·(1 + ‖D²F‖) integrable, so C_m ↑ E[W] < ∞. ✓✓ THAT WORKS. Let me execute:

For m ≥ 1 define β_m := 1_{A_m}·(‖DF‖² + 1/m²)^{-1}·‖DF‖² hmm. Let me define things to make the IBP clean. GOAL inequality: |E[φ(F)1_{A_m}]| ≤ C_m‖φ'‖_∞ with C_m = E[1_{A_m}(1+|δ(DF)| + |⟨D log-stuff...⟩|)]... 

Cleanest execution: On A_m, let γ_m := 1_{A_m}(‖DF‖²+1/m²)^{-1}. Note γ_m ≤ m², γ_m ∈ 𝔻^{1,q}∀q, Dγ_m = −1_{A_m}2⟨DF, D²F(·,·)⟩(‖DF‖²+1/m²)^{-2} + (gradient of indicator—ZERO a.e.-wise? 1_{A_m} has distributional derivative supported on ∂A_m; messy!). AVOID differentiating indicators: use smooth θ_m(x) = χ(m x) with χ: [0,∞)→[0,1], χ=0 on [0,1/2], χ=1 on [1,∞), smooth. Set γ_m := θ_m(‖DF‖²)·(‖DF‖²+1/m²)^{-1}. Then: γ_m ∈ 𝔻^{1,q}∀q (chain rule, smooth θ_m, F∈𝔻^{2,q}); γ_m = (‖DF‖²+1/m²)^{-1} on {‖DF‖²≥1/m²} =: B_m; γ_m = 0 on {‖DF‖²≤ 1/(2m²)}. 

Now the IBP: for φ ∈ C_c^∞:
E[φ(F)γ_m‖DF‖²] =: T.
Write φ(F)γ_m‖DF‖² = φ(F)γ_m(‖DF‖²+1/m²) − φ(F)γ_m m²... hmm (‖DF‖²+1/m²)γ_m: on B_m equals ‖DF‖²; off B_m: (small)·γ_m ≤ (1/m²)·(2/m²)^{-1}·... |‖DF‖²+1/m²|·γ_m ≤ 1 everywhere (check on complement of B_m: γ_m = θ_m·(...)⁻¹ ≤ (‖DF‖²+1/m²)^{-1} so product ≤ 1 ✓; on B_m: = ‖DF‖²·(‖DF‖²+1/m²)^{-1} ≤ 1 ✓). So φγ_m‖DF‖² = φγ_m(‖DF‖²+1/m²) − φγ_m m²... wait: γ_m‖DF‖² = γ_m(‖DF‖²+1/m²) − γ_m/m². So
T = E[φ(F)·γ_m(‖DF‖²+1/m²)] − E[φ(F)γ_m/m²].

First piece via duality with V_m := φ(F)γ_m: E[φγ_m(‖DF‖²+1/m²)] hmm duality gives E[⟨DV_m, DF⟩] = E[V_mδ(DF)], i.e., E[⟨DF, D(φγ_m)⟩] = E[φγ_mδ(DF)]. And ⟨DF, D(φγ_m)⟩ = φ'(F)‖DF‖²γ_m + φ(F)⟨DF,Dγ_m⟩. So:
E[φ'(F)γ_m‖DF‖²] = E[φ(F)γ_mδ(DF)] − E[φ(F)⟨DF,Dγ_m⟩]. (*)

Also E[φγ_m(‖DF‖²+1/m²)] = E[φ'(F)·0...] hmm I wanted to convert E[φγ_m(‖DF‖²+1/m²)] into a φ'-term: apply (*) with γ̃_m := γ_m(‖DF‖²+1/m²)/‖DF‖²?? getting messy. ALTERNATIVE cleaner: directly bound |E[φ(F)]| via decomposition:

E[φ(F)] = E[φ(F)χ_m] + E[φ(F)(1−χ_m)] where χ_m := θ_m(‖DF‖²) ∈ [0,1], χ_m = 1 when ‖DF‖² ≥ 1/m², = 0 when ≤ 1/(2m²). Second term → 0 by DCT (pointwise → φ(F)1_{‖DF‖>0} = φ(F) a.s.). First term: 
E[φ(F)χ_m] = E[φ(F)χ_m·‖DF‖²·(‖DF‖²+1/m²)^{-1}(‖DF‖²+1/m²)/‖DF‖²]... I keep going in circles. FINAL CLEAN DESIGN — mimic the classic proof of Nualart Thm 2.1.3 EXACTLY as I best recall (his proof of the local criterion, which I do remember structurally): he shows for the local set A: |E[φ(F)1_A]| ≤ ‖φ'‖_∞·E[1_A·(1+|δ(...)|+...)] via considering the functional φ(F)G where G := 1_A‖DF‖^{-2}‖DF‖²-trick... 

His actual trick (Thm 2.1.3 proof, 2nd ed., I'm now ~90% sure): Set G = 1_A · ‖DF‖^{-2}·hmm he defines the matrix Γ^{-1} localized smoothly and computes E[⟨DF, D(φ(F)·Ψ)⟩] where Ψ = 1_AΓ^{-1} smoothly localized; LHS: E[φ'(F)⟨DF,DF⟩Ψ + φ(F)⟨DF,DΨ⟩] = E[φ'(F)1_A·(localized Γ^{-1}Γ ≈ 1) + error]; RHS: E[φ(F)Ψδ(DF)] hmm wait duality: E[⟨D(φΨ), DF⟩] = E[φΨδ(DF)]. So:
E[φ'(F)·1_A·c_m + err] = E[φ(F)Ψ_mδ(DF)], where c_m := ⟨DF,DF⟩Ψ_m = 1 on A (with smooth localization: on A_m, Ψ_mΓ = 1 exactly). Hence
E[φ(F)1_{A_m}] = E[φ'(F)(1_{A_m} − Ψ_mΓ)] + E[φ(F)⟨DF,DΨ_m⟩] + E[φ(F)Ψ_mδ(DF)]
and |1_{A_m} − Ψ_mΓ| ≤ C/m (since off A_m, |Ψ_mΓ| ≤ small; on A_m it's exactly 1... with smooth θ: |1 − θ_m(u)u(u+1/m²)^{-1}|: on u≥1/m²: = |1−θ_m(u)·u/(u+1/m²)| ≤ |1−θ_m| + θ_m·(1/m²)/u ≤ 0 + (1/m²)/(1/m²)=1 hmm not small. Adjust: use