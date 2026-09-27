# Proof: Density of $C_c^\infty(\Omega)$ in $W^{1,p}(\Omega) \cap C_0(\Omega)$

**Answer: YES.** $C_c^\infty(\Omega)$ is dense in $W^{1,p}(\Omega) \cap C_0(\Omega)$ equipped with the norm $\|\cdot\|_{W^{1,p}} + \|\cdot\|_{L^\infty}$, for every bounded open set $\Omega \subset \mathbb{R}^N$ and $1 \leq p < \infty$.

---

## Key Idea

The standard approach of multiplying by a smooth cutoff $\eta_\epsilon$ (with $\eta_\epsilon = 1$ away from $\partial\Omega$ and $\eta_\epsilon = 0$ near $\partial\Omega$) requires controlling $\|u\,\nabla\eta_\epsilon\|_{L^p}$, which depends on the geometry of $\partial\Omega$ and fails for irregular domains.

Instead, we use **truncation by level sets**: define $u_\epsilon = (|u| - \epsilon)^+\operatorname{sgn}(u)$. This exploits the fact that $u \in C_0(\Omega)$ (so $|u| \leq \epsilon$ near $\partial\Omega$, giving compact support) and the Stampacchia chain rule (so $\nabla u = 0$ a.e. on $\{u = 0\}$, giving $W^{1,p}$ convergence). No geometric assumptions on $\Omega$ are needed.

---

## Proof

Let $u \in W^{1,p}(\Omega) \cap C_0(\Omega)$. We construct a sequence $\{v_n\} \subset C_c^\infty(\Omega)$ with $\|v_n - u\|_{W^{1,p}} + \|v_n - u\|_{L^\infty} \to 0$.

### Step 1: Truncation by level sets

For $\epsilon > 0$, define
$$u_\epsilon(x) := \bigl(|u(x)| - \epsilon\bigr)^+ \operatorname{sgn}(u(x)),$$
where $f^+ = \max(f, 0)$ and $\operatorname{sgn}(t) = \mathbf{1}_{t>0} - \mathbf{1}_{t<0}$.

**Claim 1a:** $u_\epsilon \in C_c(\Omega)$ (continuous with compact support in $\Omega$).

*Proof.* The map $t \mapsto (|t|-\epsilon)^+\operatorname{sgn}(t)$ is continuous, so $u_\epsilon \in C(\overline{\Omega})$. Since $u \in C_0(\Omega)$, we have $u = 0$ on $\partial\Omega$, and by continuity there exists $\delta > 0$ such that $|u(x)| < \epsilon$ whenever $\operatorname{dist}(x, \partial\Omega) < \delta$. On this neighborhood, $u_\epsilon = 0$, so $\operatorname{supp}(u_\epsilon) \subset \{x \in \Omega : \operatorname{dist}(x, \partial\Omega) \geq \delta\} \subset\subset \Omega$. $\square$

**Claim 1b:** $u_\epsilon \in W^{1,p}(\Omega)$ and $\nabla u_\epsilon = \mathbf{1}_{\{|u| > \epsilon\}} \nabla u$ a.e.

*Proof.* The function $\phi(t) = (|t|-\epsilon)^+\operatorname{sgn}(t)$ is Lipschitz with $\phi'(t) = \mathbf{1}_{\{|t|>\epsilon\}} \operatorname{sgn}(t)$. By the Stampacchia chain rule for Sobolev functions, $u_\epsilon = \phi(u) \in W^{1,p}(\Omega)$ and
$$\nabla u_\epsilon = \phi'(u)\,\nabla u = \mathbf{1}_{\{|u|>\epsilon\}}\,\nabla u \quad \text{a.e.}$$
$\square$

**Claim 1c:** $\|u_\epsilon - u\|_{L^\infty} \leq \epsilon$.

*Proof.* Pointwise, $|u_\epsilon(x) - u(x)| = \bigl|||u(x)|-\epsilon)^+ \operatorname{sgn}(u(x)) - u(x)\bigr| = \min(|u(x)|, \epsilon) \leq \epsilon$. $\square$

**Claim 1d:** $\|u_\epsilon - u\|_{W^{1,p}} \to 0$ as $\epsilon \to 0$.

*Proof.* 
- **$L^p$ convergence:** $|u_\epsilon - u| \leq \epsilon$ pointwise, so $\|u_\epsilon - u\|_{L^p} \leq \epsilon\,|\Omega|^{1/p} \to 0$.
- **Gradient convergence:** From Claim 1b, $\nabla u_\epsilon - \nabla u = -\mathbf{1}_{\{|u| \leq \epsilon\}}\,\nabla u$, so
$$\|\nabla u_\epsilon - \nabla u\|_{L^p}^p = \int_{\{|u| \leq \epsilon\}} |\nabla u|^p\,dx.$$
As $\epsilon \to 0$, the sets $\{|u| \leq \epsilon\}$ decrease to $\{u = 0\}$. By the **Stampacchia theorem** (applied to $f(t) = t^+$ and $f(t) = (-t)^+$), $\nabla u = 0$ a.e. on $\{u = 0\}$. Therefore $|\nabla u|^p \cdot \mathbf{1}_{\{|u| \leq \epsilon\}} \to 0$ a.e., and by dominated convergence (dominated by $|\nabla u|^p \in L^1(\Omega)$):
$$\int_{\{|u| \leq \epsilon\}} |\nabla u|^p\,dx \;\longrightarrow\; \int_{\{u=0\}} |\nabla u|^p\,dx = 0. \quad\square$$

### Step 2: Mollification of $u_\epsilon$

Fix $\epsilon > 0$. Since $u_\epsilon \in C_c(\Omega) \cap W^{1,p}(\Omega)$ with $\operatorname{supp}(u_\epsilon) \subset\subset \Omega$, extend by zero to $\tilde{u}_\epsilon \in C_c(\mathbb{R}^N) \cap W^{1,p}(\mathbb{R}^N)$.

Let $\rho_\delta$ be a standard mollifier and set $v_{\epsilon,\delta} = \rho_\delta * \tilde{u}_\epsilon$.

**Claim 2a:** For $\delta < \operatorname{dist}(\operatorname{supp}(u_\epsilon), \partial\Omega)$, we have $v_{\epsilon,\delta} \in C_c^\infty(\Omega)$.

*Proof.* $\operatorname{supp}(v_{\epsilon,\delta}) \subset \operatorname{supp}(\tilde{u}_\epsilon) + \overline{B(0,\delta)} \subset \Omega$ for $\delta$ small enough. $\square$

**Claim 2b:** $\|v_{\epsilon,\delta} - u_\epsilon\|_{L^\infty} \to 0$ and $\|v_{\epsilon,\delta} - u_\epsilon\|_{W^{1,p}} \to 0$ as $\delta \to 0$.

*Proof.* 
- **$L^\infty$:** $\tilde{u}_\epsilon \in C_c(\mathbb{R}^N)$ is uniformly continuous, so $\rho_\delta * \tilde{u}_\epsilon \to \tilde{u}_\epsilon$ uniformly on $\mathbb{R}^N$.
- **$W^{1,p}$:** Standard property of mollification: $\rho_\delta * \tilde{u}_\epsilon \to \tilde{u}_\epsilon$ in $W^{1,p}(\mathbb{R}^N)$, hence also in $W^{1,p}(\Omega)$. $\square$

### Step 3: Diagonal argument

For each $n \geq 1$:
1. Set $\epsilon_n = \frac{1}{2n}$ and form $u_{\epsilon_n}$ as in Step 1.
2. Choose $\delta_n > 0$ small enough that:
   - $\delta_n < \operatorname{dist}(\operatorname{supp}(u_{\epsilon_n}), \partial\Omega)$ (so $v_n := v_{\epsilon_n, \delta_n} \in C_c^\infty(\Omega)$),
   - $\|v_n - u_{\epsilon_n}\|_{L^\infty} < \frac{1}{2n}$,
   - $\|v_n - u_{\epsilon_n}\|_{W^{1,p}} < \frac{1}{n}$.

Then $v_n \in C_c^\infty(\Omega)$ and by the triangle inequality:

$$\|v_n - u\|_{L^\infty} \leq \|v_n - u_{\epsilon_n}\|_{L^\infty} + \|u_{\epsilon_n} - u\|_{L^\infty} < \frac{1}{2n} + \frac{1}{2n} = \frac{1}{n} \to 0,$$

$$\|v_n - u\|_{W^{1,p}} \leq \|v_n - u_{\epsilon_n}\|_{W^{1,p}} + \|u_{\epsilon_n} - u\|_{W^{1,p}} \to 0 + 0 = 0.$$

Therefore $\|v_n - u\|_{W^{1,p}} + \|v_n - u\|_{L^\infty} \to 0$, proving density. $\blacksquare$

---

## Why the smooth-cutoff approach fails but truncation succeeds

The standard cutoff approach multiplies $u$ by $\eta_\epsilon$ (smooth, $\eta_\epsilon = 1$ on $\{d \geq 2\epsilon\}$, $\eta_\epsilon = 0$ on $\{d \leq \epsilon\}$), producing the error term $\|u\,\nabla\eta_\epsilon\|_{L^p} \sim \omega(\epsilon)\,m(\epsilon)^{1/p}/\epsilon$ where $\omega(\epsilon) = \sup_{\{d \leq C\epsilon\}} |u|$ and $m(\epsilon) = |\{d \leq C\epsilon\}|$. For irregular domains, $m(\epsilon)$ may decay slower than $\epsilon$, so this term need not vanish.

The truncation approach sidesteps this entirely: it does not introduce any $\nabla\eta_\epsilon$ factor. Instead, it uses the **intrinsic level-set structure** of $u$:
- Compact support comes from $u \in C_0$ (not from an external cutoff).
- $W^{1,p}$ convergence comes from $\nabla u = 0$ a.e. on $\{u = 0\}$ (Stampacchia), not from geometric estimates on $\partial\Omega$.

This is why the result holds for **all** bounded open sets, without any regularity assumption on $\partial\Omega$.

---

## Conclusion

$$\boxed{\text{Yes, } C_c^\infty(\Omega) \text{ is dense in } W^{1,p}(\Omega) \cap C_0(\Omega) \text{ for every bounded open } \Omega \subset \mathbb{R}^N \text{ and } 1 \leq p < \infty.}$$

### PROOF COMPLETE
