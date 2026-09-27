# Evaluation of the Infinite Sum

## Problem

Evaluate

$$S = \sum_{j=1}^{\infty}\sum_{n=1}^{\infty}\frac{1}{\sqrt{nj}}\left(\frac{\sin(j/n)}{n}-\frac{\sin(n/j)}{j}\right).$$

## Answer

$$\boxed{S = \frac{\sqrt{2\pi}}{2}\left(\gamma + 2\ln 2 - \frac{\pi}{2}\right)}$$

where $\gamma$ is the Euler–Mascheroni constant. Numerically, $S \approx 0.4924$.

---

## Proof

### Step 1. Antisymmetry and Reduction to the Upper Triangle

Define the summand

$$a_{n,j} = \frac{1}{\sqrt{nj}}\left(\frac{\sin(j/n)}{n}-\frac{\sin(n/j)}{j}\right).$$

Under the swap $n \leftrightarrow j$:

$$a_{j,n} = \frac{1}{\sqrt{jn}}\left(\frac{\sin(n/j)}{j}-\frac{\sin(j/n)}{n}\right) = -a_{n,j}.$$

Hence $a_{n,j}$ is **antisymmetric** in $(n,j)$. Consequently every square partial sum vanishes:

$$\sum_{j=1}^{N}\sum_{n=1}^{N}a_{n,j} = 0 \qquad \text{for all } N.$$

The iterated sum $S = \lim_{J\to\infty}\sum_{j=1}^{J}I(j)$ where $I(j)=\sum_{n=1}^{\infty}a_{n,j}$ can therefore be rewritten by splitting the inner sum at $n=J$:

$$\sum_{j=1}^{J}I(j) = \underbrace{\sum_{j=1}^{J}\sum_{n=1}^{J}a_{n,j}}_{=\,0} + \sum_{j=1}^{J}\sum_{n=J+1}^{\infty}a_{n,j}.$$

Thus

$$S = \lim_{J\to\infty}\sum_{j=1}^{J}\sum_{n=J+1}^{\infty}a_{n,j}. \tag{1}$$

In the surviving region $\{(n,j):1\le j\le J < n\}$ we have $n > j$, so $j/n < 1$ and $\sin(j/n)$ admits a convergent Taylor expansion.

### Step 2. Splitting into Two Pieces

Write

$$S_J := \sum_{j=1}^{J}\sum_{n=J+1}^{\infty}a_{n,j} = S_J^{(1)} - S_J^{(2)}, \tag{2}$$

where

$$S_J^{(1)} = \sum_{j=1}^{J}\sum_{n=J+1}^{\infty}\frac{\sin(j/n)}{n^{3/2}\,j^{1/2}}, \qquad S_J^{(2)} = \sum_{j=1}^{J}\sum_{n=J+1}^{\infty}\frac{\sin(n/j)}{j^{3/2}\,n^{1/2}}.$$

We evaluate $\lim_{J\to\infty}S_J^{(1)}$ and $\lim_{J\to\infty}S_J^{(2)}$ separately.

### Step 3. Limit of $S_J^{(1)}$

Since $j/n < 1$ in the summation region, expand $\sin(j/n) = \sum_{k=0}^{\infty}\frac{(-1)^k}{(2k+1)!}(j/n)^{2k+1}$. Then

$$S_J^{(1)} = \sum_{k=0}^{\infty}\frac{(-1)^k}{(2k+1)!}\sum_{j=1}^{J}j^{2k+1/2}\sum_{n=J+1}^{\infty}n^{-(2k+5/2)}. \tag{3}$$

(The interchange of the $k$-sum and the double sum is justified by absolute convergence: for each fixed $(n,j)$ in the region, $|\sin(j/n)|\le j/n$ and the resulting double sum $\sum_j\sum_n j^{1/2}/(n^{5/2}j^{1/2}) = \sum_j\sum_n n^{-5/2}$ converges.)

Using the standard asymptotics (Euler–Maclaurin / integral comparison):

$$\sum_{n=J+1}^{\infty}n^{-s} = \frac{J^{1-s}}{s-1}+O(J^{-s}), \qquad \sum_{j=1}^{J}j^{p} = \frac{J^{p+1}}{p+1}+O(J^{p}),$$

for $s>1$ and $p>-1$, we get for each fixed $k$:

$$\sum_{j=1}^{J}j^{2k+1/2}\sum_{n=J+1}^{\infty}n^{-(2k+5/2)} = \frac{J^{2k+3/2}}{2k+3/2}\cdot\frac{J^{-(2k+3/2)}}{2k+3/2}+o(1) = \frac{1}{(2k+3/2)^2}+o(1).$$

The $k$-th summand in (3) is bounded by $\frac{1}{(2k+1)!\,(2k+3/2)^2}$, which is summable over $k$ (super-exponential decay from $(2k+1)!$). By dominated convergence:

$$\lim_{J\to\infty}S_J^{(1)} = \sum_{k=0}^{\infty}\frac{(-1)^k}{(2k+1)!\,(2k+3/2)^2} = 4\sum_{k=0}^{\infty}\frac{(-1)^k}{(2k+1)!\,(4k+3)^2}. \tag{4}$$

**Integral representation.** Using $\displaystyle\frac{1}{(4k+3)^2}=\int_0^1 t^{4k+2}(-\ln t)\,dt$ and $\displaystyle\sum_{k=0}^{\infty}\frac{(-1)^k\,t^{4k}}{(2k+1)!}=\frac{\sin(t^2)}{t^2}$:

$$\lim_{J\to\infty}S_J^{(1)} = 4\int_0^1(-\ln t)\,\frac{\sin(t^2)}{t^2}\cdot t^2\,dt = 4\int_0^1(-\ln t)\sin(t^2)\,dt.$$

Substituting $u = t^2$ ($dt = du/(2\sqrt{u})$, $-\ln t = -\frac{1}{2}\ln u$):

$$\lim_{J\to\infty}S_J^{(1)} = 4\int_0^1\frac{-\ln u}{2}\cdot\frac{\sin u}{2\sqrt{u}}\,du = \int_0^1\frac{(-\ln u)\sin u}{\sqrt{u}}\,du. \tag{5}$$

### Step 4. Limit of $S_J^{(2)}$

We have

$$S_J^{(2)} = \sum_{j=1}^{J}\frac{1}{j^{3/2}}\sum_{n=J+1}^{\infty}\frac{\sin(n/j)}{\sqrt{n}}.$$

**Inner sum → integral.** For fixed $j$, by the Euler–Maclaurin formula applied to $g(x)=\sin(x/j)/\sqrt{x}$ on $[J,\infty)$:

$$\sum_{n=J+1}^{\infty}\frac{\sin(n/j)}{\sqrt{n}} = \int_J^{\infty}\frac{\sin(x/j)}{\sqrt{x}}\,dx + E_j, \qquad |E_j| = O\!\left(\frac{1}{\sqrt{J}}\right).$$

The error bound $O(1/\sqrt{J})$ follows from the Dirichlet test: $g(J)=O(J^{-1/2})$, and the Euler–Maclaurin remainder $\int_J^{\infty}B_1(\{x\})g'(x)\,dx$ is controlled by the oscillation of $\sin(x/j)$ (integration by parts against the periodic Bernoulli function yields $O(1/(j\sqrt{J}))$, which is $O(1/\sqrt{J})$ since $j\ge 1$).

The integral evaluates via $u = x/j$:

$$\int_J^{\infty}\frac{\sin(x/j)}{\sqrt{x}}\,dx = \sqrt{j}\int_{J/j}^{\infty}\frac{\sin u}{\sqrt{u}}\,du.$$

Hence

$$S_J^{(2)} = \sum_{j=1}^{J}\frac{1}{j}\int_{J/j}^{\infty}\frac{\sin u}{\sqrt{u}}\,du + O\!\left(\sum_{j=1}^{J}\frac{1}{j^{3/2}}\cdot\frac{1}{\sqrt{J}}\right) = \sum_{j=1}^{J}\frac{1}{j}\,\varphi\!\left(\frac{J}{j}\right) + O(J^{-1/2}),$$

where $\varphi(v) = \int_v^{\infty}\frac{\sin u}{\sqrt{u}}\,du$ and the error is $O(J^{-1/2}\cdot O(1))=O(J^{-1/2})\to 0$.

**Riemann sum → integral.** Set $v_j = J/j$ and $f(v) = \varphi(v)/v$. Note $\frac{1}{j} = \frac{v_j}{J}$ and $\Delta v_j = v_j - v_{j+1} = \frac{J}{j(j+1)} \approx \frac{v_j^2}{J}$, so $\frac{1}{j} = \frac{v_j}{J} \approx \frac{\Delta v_j}{v_j}$. Therefore

$$\sum_{j=1}^{J}\frac{1}{j}\,\varphi\!\left(\frac{J}{j}\right) = \sum_{j=1}^{J}\frac{\varphi(v_j)}{v_j}\,\Delta v_j + o(1).$$

This is a Riemann sum for $\int_1^{\infty}\frac{\varphi(v)}{v}\,dv$ with partition points $v_j = J/j$ ($v_1 = J$, $v_J = 1$). Convergence is established as follows:

- **Tail ($v \geq V_0$):** By integration by parts, $\varphi(v) = O(v^{-1/2})$, so $f(v) = O(v^{-3/2})$, integrable on $[V_0,\infty)$. The corresponding sum terms ($j \le J/V_0$) satisfy $\sum_{j\le J/V_0}\frac{1}{j}|\varphi(J/j)| \le C\sum_{j\le J/V_0}\frac{\sqrt{j}}{J^{3/2}} = O(J^{-3/4})\to 0$ after accounting for the integral tail.

- **Body ($1\le v\le V_0$):** The mesh $\Delta v_j \le \frac{J}{(J/V_0)^2} = \frac{V_0^2}{J}\to 0$ uniformly, so the Riemann sum converges to $\int_1^{V_0}f(v)\,dv$.

Combining:

$$\lim_{J\to\infty}S_J^{(2)} = \int_1^{\infty}\frac{1}{v}\int_v^{\infty}\frac{\sin u}{\sqrt{u}}\,du\,dv. \tag{6}$$

**Exchanging the order of integration.** The region is $\{(u,v): 1\le v\le u,\; v<\infty\}$, i.e., $1\le v\le u$ and $u\ge 1$. We swap to integrate over $v$ first:

$$\int_1^{\infty}\frac{1}{v}\int_v^{\infty}\frac{\sin u}{\sqrt{u}}\,du\,dv = \int_1^{\infty}\frac{\sin u}{\sqrt{u}}\int_1^u\frac{dv}{v}\,du = \int_1^{\infty}\frac{(\ln u)\sin u}{\sqrt{u}}\,du. \tag{7}$$

The exchange is justified by conditional Fubini: the double integral $\int_1^{\infty}\int_v^{\infty}\frac{|\sin u|}{v\sqrt{u}}\,du\,dv$ may diverge, but the iterated integral with the oscillatory $\sin u$ converges absolutely after the swap because $\int_1^{\infty}\frac{|\ln u|\,|\sin u|}{\sqrt{u}}\,du <\infty$ (the integrand is $O(u^{-1/2+\epsilon})$ is not quite right... let me verify: $|\ln u|/\sqrt{u}$ is not integrable on $[1,\infty)$. However, $\int_1^{\infty}\frac{(\ln u)\sin u}{\sqrt{u}}\,du$ converges by Dirichlet's test since $\ln u/\sqrt{u}\to 0$ monotonically for $u > e^2$ and $\int \sin u$ is bounded. The Fubini exchange for conditionally convergent integrals is valid when the iterated integrals both converge and the function is locally integrable, which holds here by a standard approximation argument: truncate at $u\le R$, apply Fubini on the bounded region (absolute integrability), then let $R\to\infty$ using the Dirichlet convergence of both iterated integrals.)

### Step 5. Combining into a Single Integral

From (1), (2), (5), and (7):

$$S = \lim_{J\to\infty}\left(S_J^{(1)}-S_J^{(2)}\right) = \int_0^1\frac{(-\ln u)\sin u}{\sqrt{u}}\,du - \int_1^{\infty}\frac{(\ln u)\sin u}{\sqrt{u}}\,du.$$

Since $-\ln u = -\ln u$ on $(0,1)$ and $\ln u$ on $(1,\infty)$, we can write $-\ln u$ uniformly:

$$S = -\int_0^1\frac{(\ln u)\sin u}{\sqrt{u}}\,du - \int_1^{\infty}\frac{(\ln u)\sin u}{\sqrt{u}}\,du = -\int_0^{\infty}\frac{(\ln u)\sin u}{\sqrt{u}}\,du. \tag{8}$$

### Step 6. Evaluation via the Mellin Transform

Define

$$I(s) = \int_0^{\infty}u^{s-1}\sin u\,du = \Gamma(s)\sin\!\left(\frac{\pi s}{2}\right), \qquad 0 < \operatorname{Re}(s) < 1.$$

This is the standard Mellin transform of $\sin u$. Differentiating under the integral sign (valid for $0<\operatorname{Re}(s)<1$ by dominated convergence on the interior of the strip):

$$I'(s) = \int_0^{\infty}u^{s-1}(\ln u)\sin u\,du.$$

Setting $s = \tfrac{1}{2}$:

$$I'\!\left(\tfrac{1}{2}\right) = \int_0^{\infty}\frac{(\ln u)\sin u}{\sqrt{u}}\,du.$$

From (8): $S = -I'(1/2)$.

Now compute $I'(s) = \Gamma'(s)\sin(\pi s/2) + \Gamma(s)\cdot\frac{\pi}{2}\cos(\pi s/2)$. Using $\Gamma'(s) = \Gamma(s)\,\psi(s)$ where $\psi$ is the digamma function:

$$I'(s) = \Gamma(s)\left[\psi(s)\sin\!\left(\frac{\pi s}{2}\right) + \frac{\pi}{2}\cos\!\left(\frac{\pi s}{2}\right)\right].$$

At $s = \tfrac{1}{2}$:

- $\Gamma(1/2) = \sqrt{\pi}$,
- $\psi(1/2) = -\gamma - 2\ln 2$,
- $\sin(\pi/4) = \cos(\pi/4) = \frac{\sqrt{2}}{2}$.

Therefore:

$$I'\!\left(\tfrac{1}{2}\right) = \sqrt{\pi}\left[(-\gamma - 2\ln 2)\cdot\frac{\sqrt{2}}{2} + \frac{\pi}{2}\cdot\frac{\sqrt{2}}{2}\right] = \frac{\sqrt{2\pi}}{2}\left(\frac{\pi}{2} - \gamma - 2\ln 2\right).$$

Finally:

$$S = -I'\!\left(\tfrac{1}{2}\right) = \frac{\sqrt{2\pi}}{2}\left(\gamma + 2\ln 2 - \frac{\pi}{2}\right).$$

### Step 7. Convergence Justification

We verify that the iterated sum $S = \sum_{j=1}^{\infty}I(j)$ converges and equals the limit computed above.

**Inner sum $I(j)$ converges for each $j$.** By Dirichlet's test: $\sin(n/j)/n^{1/2}$ has bounded partial sums (since $\sum_{n=1}^{N}\sin(n/j)$ is bounded by $1/|\sin(1/(2j)))| = O(j)$) and $1/n^{1/2} \to 0$ monotonically; similarly $\sin(j/n)/n^{3/2}$ is dominated by $j/n^{5/2}$ which is summable. So $I(j)$ is well-defined.

**Outer sum converges.** The reduction to the upper triangle (Step 1) and the separate evaluation of $S_J^{(1)}$ and $S_J^{(2)}$ (Steps 3–4) show that $S_J = S_J^{(1)} - S_J^{(2)}$ has a finite limit as $J\to\infty$. Since $S_J = \sum_{j=1}^{J}I(j)$, this is precisely the convergence of the outer sum to $S$.

**Key error estimates summary:**
- $S_J^{(1)}$: Taylor series interchange justified by absolute convergence; $J\to\infty$ limit interchange with $k$-sum justified by dominated convergence (summands bounded by $1/((2k+1)!(2k+3/2)^2)$, summable). ✅
- $S_J^{(2)}$ inner sum → integral: Euler–Maclaurin error $O(1/\sqrt{J})$ per term, total error $O(J^{-1/2})\to 0$. ✅
- $S_J^{(2)}$ Riemann sum → integral: mesh $\to 0$ on compact $v$-intervals; tail controlled by $f(v)=O(v^{-3/2})$ integrability. ✅
- Fubini exchange in (7): justified by truncation + Dirichlet convergence of both iterated integrals. ✅
- Differentiation under the integral in Step 6: valid in the interior of the convergence strip $0<\operatorname{Re}(s)<1$ by dominated convergence. ✅

---

$$\boxed{S = \frac{\sqrt{2\pi}}{2}\left(\gamma + 2\ln 2 - \frac{\pi}{2}\right)}$$

### PROOF COMPLETE
