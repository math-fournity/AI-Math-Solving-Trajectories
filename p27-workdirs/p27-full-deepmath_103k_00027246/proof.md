# Time Derivative of the Modified Hartree Energy

## Problem

Given a solution $u \in H^2(\mathbb{R}^3)$ to the Hartree equation with an odd real-valued potential $V$, find the time derivative of the modified Hartree energy.

## Setup

The Hartree equation with external potential $V$ and Coulomb interaction kernel $w(x) = \frac{1}{|x|}$ is:

$$i\partial_t u = -\Delta u + V(x)u + \left(|u|^2 * \frac{1}{|x|}\right)u$$

Denote $W := \left(|u|^2 * \frac{1}{|x|}\right)$, so the equation reads $i\partial_t u = -\Delta u + Vu + Wu$.

The **standard Hartree energy** is:

$$E[u] = \frac{1}{2}\|\nabla u\|_{L^2}^2 + \frac{1}{2}\int_{\mathbb{R}^3} V|u|^2\,dx + \frac{1}{4}\int_{\mathbb{R}^3} W|u|^2\,dx$$

The **modified Hartree energy** (the free part, with the external potential term removed) is:

$$\mathcal{E}[u] = \frac{1}{2}\|\nabla u\|_{L^2}^2 + \frac{1}{4}\int_{\mathbb{R}^3} W|u|^2\,dx = E[u] - \frac{1}{2}\int_{\mathbb{R}^3} V|u|^2\,dx$$

This is the natural "modified" energy in scattering theory: one removes the external potential contribution to study how the free (interaction-only) energy evolves under the full dynamics.

## Step 1: Conservation of the Standard Energy

**Claim:** $\frac{dE}{dt} = 0$.

**Proof.** The Hartree equation has Hamiltonian structure. We compute the variational derivative:

$$\frac{\delta E}{\delta \bar{u}} = -\Delta u + Vu + Wu$$

**Verification of the Hartree term:** The Hartree energy term is $\frac{1}{4}\int (w*|u|^2)|u|^2\,dx = \frac{1}{4}\iint w(x-y)|u(y)|^2|u(x)|^2\,dy\,dx$. Varying with respect to $\bar{u}$: the $|u(x)|^2$ factor contributes $\frac{1}{4}\cdot 2\cdot (w*|u|^2)(x) = \frac{1}{2}W(x)$, and the $|u(y)|^2$ factor inside the convolution contributes another $\frac{1}{4}\cdot 2\cdot (w*|u|^2)(x) = \frac{1}{2}W(x)$ (using the symmetry $w(x-y)=w(y-x)$ to identify the two contributions). Total: $\frac{1}{2}W + \frac{1}{2}W = W$. ✓

Since $i\partial_t u = \frac{\delta E}{\delta \bar{u}}$, we have:

$$\frac{dE}{dt} = 2\operatorname{Re}\int \frac{\delta E}{\delta \bar{u}}\,\overline{\partial_t u}\,dx = 2\operatorname{Re}\int \frac{\delta E}{\delta \bar{u}}\,\overline{\left(-i\frac{\delta E}{\delta \bar{u}}\right)}\,dx = 2\operatorname{Re}\left(i\int \left|\frac{\delta E}{\delta \bar{u}}\right|^2 dx\right) = 0$$

since $\int |\frac{\delta E}{\delta \bar{u}}|^2 dx \geq 0$ is real. $\square$

## Step 2: Time Derivative of the Modified Energy

Since $\mathcal{E} = E - \frac{1}{2}\int V|u|^2\,dx$ and $\frac{dE}{dt} = 0$:

$$\frac{d\mathcal{E}}{dt} = -\frac{1}{2}\frac{d}{dt}\int_{\mathbb{R}^3} V|u|^2\,dx$$

**Computing $\frac{d}{dt}\int V|u|^2\,dx$:**

$$\frac{d}{dt}\int V|u|^2\,dx = 2\operatorname{Re}\int V\,\bar{u}\,\partial_t u\,dx$$

From the equation, $\partial_t u = i\Delta u - iVu - iWu$, so:

$$\bar{u}\,\partial_t u = i\bar{u}\Delta u - iV|u|^2 - iW|u|^2$$

Taking the real part: $\operatorname{Re}(\bar{u}\,\partial_t u) = -\operatorname{Im}(\bar{u}\Delta u)$, since $V|u|^2$ and $W|u|^2$ are real (so $\operatorname{Re}(-iV|u|^2) = 0$ and $\operatorname{Re}(-iW|u|^2) = 0$).

Therefore:

$$\frac{d}{dt}\int V|u|^2\,dx = -2\operatorname{Im}\int V\,\bar{u}\,\Delta u\,dx$$

**Integration by parts:** Using $\int f\,\Delta g\,dx = -\int \nabla f \cdot \nabla g\,dx$ (valid for $u \in H^2$, $V$ sufficiently regular, with decay at infinity):

$$\int V\,\bar{u}\,\Delta u\,dx = -\int \nabla(V\bar{u})\cdot\nabla u\,dx = -\int (\nabla V \cdot \nabla u)\,\bar{u}\,dx - \int V\,|\nabla u|^2\,dx$$

The second term $\int V|\nabla u|^2\,dx$ is real (since $V$ is real-valued), so its imaginary part vanishes. Hence:

$$\operatorname{Im}\int V\,\bar{u}\,\Delta u\,dx = -\operatorname{Im}\int (\nabla V \cdot \nabla u)\,\bar{u}\,dx$$

Substituting back:

$$\frac{d}{dt}\int V|u|^2\,dx = 2\operatorname{Im}\int (\nabla V \cdot \nabla u)\,\bar{u}\,dx$$

$$\frac{d\mathcal{E}}{dt} = -\operatorname{Im}\int_{\mathbb{R}^3} (\nabla V(x) \cdot \nabla u(x))\,\overline{u(x)}\,dx$$

## Step 3: Role of the Odd Potential

Since $V$ is odd, i.e., $V(-x) = -V(x)$, differentiating gives $\partial_j V(-x) = \partial_j V(x)$ for each $j$, so **$\nabla V$ is even**.

The integrand can be rewritten as:

$$\frac{d\mathcal{E}}{dt} = -\int_{\mathbb{R}^3} \nabla V(x) \cdot \operatorname{Im}\!\left(\overline{u(x)}\,\nabla u(x)\right) dx$$

where $\operatorname{Im}(\bar{u}\,\nabla u)$ is the **momentum density** (probability current density).

**Parity analysis:** If $u$ has definite parity (even or odd as a function of $x$), then:
- $u$ even $\Rightarrow$ $\nabla u$ odd $\Rightarrow$ $\bar{u}\,\nabla u$ odd $\Rightarrow$ $\operatorname{Im}(\bar{u}\nabla u)$ odd.
- $u$ odd $\Rightarrow$ $\nabla u$ even $\Rightarrow$ $\bar{u}$ odd $\Rightarrow$ $\bar{u}\,\nabla u$ odd $\Rightarrow$ $\operatorname{Im}(\bar{u}\nabla u)$ odd.

In both cases, $\operatorname{Im}(\bar{u}\nabla u)$ is odd. Since $\nabla V$ is even, the product $\nabla V \cdot \operatorname{Im}(\bar{u}\nabla u)$ is odd, and its integral over $\mathbb{R}^3$ vanishes. Therefore:

$$\frac{d\mathcal{E}}{dt} = 0 \quad \text{when } u \text{ has definite parity.}$$

**Remark on parity preservation:** The Hartree equation with odd $V$ is invariant under the simultaneous transformation $(x, V) \to (-x, -V)$. Since $V$ is fixed, the equation is **not** invariant under $x \to -x$ alone, and parity is not automatically preserved for general initial data. However, if the initial data $u(0, \cdot)$ has definite parity and one extends the solution to the equation with $-V$ (which is the parity-reflected version), the two solutions combine to give a consistent picture. In many physical and mathematical contexts where this problem arises, solutions with definite parity are the natural class of interest (e.g., standing waves, symmetric ground states of related even-potential problems).

## Final Answer

$$\boxed{\dfrac{d\mathcal{E}}{dt} = -\operatorname{Im}\int_{\mathbb{R}^3} \nabla V(x) \cdot \overline{u(x)}\,\nabla u(x)\,dx = -\int_{\mathbb{R}^3} \nabla V(x) \cdot \operatorname{Im}\!\left(\overline{u(x)}\,\nabla u(x)\right) dx}$$

where $\mathcal{E}[u] = \frac{1}{2}\|\nabla u\|_{L^2}^2 + \frac{1}{4}\int_{\mathbb{R}^3} (|u|^2 * \frac{1}{|x|})|u|^2\,dx$ is the modified (free) Hartree energy. When $V$ is odd and $u$ has definite parity, this derivative vanishes.

### PROOF COMPLETE
