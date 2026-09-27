# Coulomb Energy of a Compactly Supported Signed Measure is Non-Negative

**Problem.** Suppose $\nu$ is a compactly supported signed measure in $\mathbb{R}^{n}$, $n \geq 3$. Is the Coulomb energy
$$
I(\nu) = \iint \frac{1}{\|x-y\|^{n-2}}\,d\nu(x)\,d\nu(y)
$$
always $\geq 0$?

**Answer: Yes.** Whenever the energy is well-defined (i.e., does not involve an $\infty - \infty$ indeterminacy), it is non-negative.

$$\boxed{\text{Yes, } \iint \frac{d\nu(x)\,d\nu(y)}{\|x-y\|^{n-2}} \geq 0 \text{ whenever the integral is well-defined.}}$$

---

## Proof

### Setup

Let $\nu$ be a compactly supported signed (Borel) measure on $\mathbb{R}^n$, $n \geq 3$, with Jordan decomposition $\nu = \nu^+ - \nu^-$. Set
$$
K(x) = |x|^{2-n}, \qquad x \in \mathbb{R}^n \setminus \{0\}.
$$
The Coulomb energy is
$$
I(\nu) = \iint K(x-y)\,d\nu(x)\,d\nu(y) = A - 2B + C,
$$
where
$$
A = \iint K(x-y)\,d\nu^+(x)\,d\nu^+(y), \quad
B = \iint K(x-y)\,d\nu^+(x)\,d\nu^-(y), \quad
C = \iint K(x-y)\,d\nu^-(x)\,d\nu^-(y),
$$
each taking values in $[0, +\infty]$.

### Key Fact: Fourier Transform of the Kernel

With the convention $\widehat{f}(\xi) = \int_{\mathbb{R}^n} e^{-2\pi i\, x\cdot\xi}\,f(x)\,dx$, the distributional Fourier transform of $K(x) = |x|^{2-n}$ is
$$
\widehat{K}(\xi) = \frac{4\pi^{n/2}}{\Gamma\!\left(\frac{n-2}{2}\right)}\,\frac{1}{|\xi|^2}.
$$
This follows from the standard Riesz potential formula: $I_\alpha(x) = c_{\alpha,n}|x|^{\alpha-n}$ with $c_{\alpha,n} = \frac{\Gamma((n-\alpha)/2)}{\pi^{n/2}\,2^\alpha\,\Gamma(\alpha/2)}$ and $\widehat{I_\alpha}(\xi) = |\xi|^{-\alpha}$; setting $\alpha = 2$ and solving for $\widehat{|x|^{2-n}}$.

**Non-negativity.** The constant $\frac{4\pi^{n/2}}{\Gamma((n-2)/2)}$ is positive since $n \geq 3 \Rightarrow (n-2)/2 > 0 \Rightarrow \Gamma((n-2)/2) > 0$, and $|\xi|^{-2} \geq 0$. Hence
$$
\widehat{K}(\xi) \geq 0 \quad \text{for all } \xi \neq 0.
$$

**Local integrability.** Near $\xi = 0$, $|\xi|^{-2}$ has singularity $r^{-2}$ with volume element $r^{n-1}\,dr$, giving integrand $r^{n-3}$, which is integrable iff $n - 3 > -1$, i.e., $n > 2$. Since $n \geq 3$, $\widehat{K} \in L^1_{\mathrm{loc}}(\mathbb{R}^n)$. $\checkmark$

### Regularization

For $\varepsilon > 0$, define
$$
K_\varepsilon(x) = K(x)\,e^{-\pi\varepsilon|x|^2} = |x|^{2-n}\,e^{-\pi\varepsilon|x|^2}.
$$
Then $K_\varepsilon \in L^1(\mathbb{R}^n) \cap C_0(\mathbb{R}^n)$ (the Gaussian decay dominates the polynomial singularity at infinity, and the singularity at $0$ is locally integrable since $n \geq 3$). By the convolution theorem for Fourier transforms,
$$
\widehat{K_\varepsilon}(\xi) = (\widehat{K} * g_\varepsilon)(\xi), \qquad g_\varepsilon(\xi) = \varepsilon^{-n/2}\,e^{-\pi|\xi|^2/\varepsilon} \geq 0,
$$
where $g_\varepsilon$ is the Fourier transform of $e^{-\pi\varepsilon|x|^2}$. Since $\widehat{K} \geq 0$ and $g_\varepsilon \geq 0$, their convolution satisfies
$$
\widehat{K_\varepsilon}(\xi) \geq 0 \quad \text{for all } \xi \in \mathbb{R}^n. \quad \checkmark
$$

### Non-Negativity of the Regularized Energy

Since $K_\varepsilon$ is bounded and continuous, Fubini's theorem applies to the signed measure $\nu$, giving
$$
\iint K_\varepsilon(x-y)\,d\nu(x)\,d\nu(y) = \int_{\mathbb{R}^n} \widehat{K_\varepsilon}(\xi)\,|\widehat{\nu}(\xi)|^2\,d\xi, \qquad (\star)
$$
where $\widehat{\nu}(\xi) = \int e^{-2\pi i\,x\cdot\xi}\,d\nu(x)$ is the Fourier–Stieltjes transform. (This identity follows from writing $K_\varepsilon(x-y) = \int \widehat{K_\varepsilon}(\xi)\,e^{2\pi i(x-y)\cdot\xi}\,d\xi$ and applying Fubini, justified by $K_\varepsilon \in L^1$ and $\nu$ having finite total variation.)

Since $\widehat{K_\varepsilon} \geq 0$ and $|\widehat{\nu}(\xi)|^2 \geq 0$, the right-hand side of $(\star)$ is $\geq 0$. Therefore
$$
\iint K_\varepsilon(x-y)\,d\nu(x)\,d\nu(y) \geq 0 \quad \text{for all } \varepsilon > 0. \quad \checkmark
$$

### Passage to the Limit

As $\varepsilon \searrow 0$, we have $e^{-\pi\varepsilon|x|^2} \nearrow 1$ for every $x$, so $K_\varepsilon(x) \nearrow K(x)$ pointwise (monotone increasing, since the exponential factor increases toward $1$).

Decompose $\nu = \nu^+ - \nu^-$ and define the three regularized double integrals:
$$
A_\varepsilon = \iint K_\varepsilon\,d\nu^+\,d\nu^+, \quad
B_\varepsilon = \iint K_\varepsilon\,d\nu^+\,d\nu^-, \quad
C_\varepsilon = \iint K_\varepsilon\,d\nu^-\,d\nu^-.
$$
Each integrand $K_\varepsilon(x-y)$ is non-negative and increases monotonically to $K(x-y)$, so by the **Monotone Convergence Theorem** (applied to the product measures $\nu^+\otimes\nu^+$, $\nu^+\otimes\nu^-$, $\nu^-\otimes\nu^-$),
$$
A_\varepsilon \nearrow A, \qquad B_\varepsilon \nearrow B, \qquad C_\varepsilon \nearrow C, \qquad A, B, C \in [0, +\infty].
$$

From $(\star)$ and the decomposition, the regularized energy satisfies
$$
A_\varepsilon - 2B_\varepsilon + C_\varepsilon = \iint K_\varepsilon\,d\nu\,d\nu \geq 0,
$$
which rearranges to
$$
A_\varepsilon + C_\varepsilon \geq 2B_\varepsilon \quad \text{for all } \varepsilon > 0. \qquad (\star\star)
$$

#### Case 1: $B < \infty$.

Taking $\varepsilon \to 0$ in $(\star\star)$: the left side $A_\varepsilon + C_\varepsilon$ increases to $A + C$ (monotone convergence), and the right side $2B_\varepsilon$ increases to $2B < \infty$. Hence
$$
A + C \geq 2B.
$$
Therefore
$$
I(\nu) = A - 2B + C = (A + C) - 2B \geq 0. \quad \checkmark
$$

#### Case 2: $B = +\infty$.

From $(\star\star)$, $A_\varepsilon + C_\varepsilon \geq 2B_\varepsilon \to +\infty$, so $A + C = +\infty$. The energy $I(\nu) = A - 2B + C$ then involves the indeterminate form $+\infty - \infty$ and is **not well-defined**.

Moreover, the scenario "$B = \infty$ but $A, C < \infty$" is **impossible**: it would contradict $(\star\star)$ in the limit, since $A_\varepsilon + C_\varepsilon \leq A + C < \infty$ could not dominate $2B_\varepsilon \to \infty$. Hence whenever $B = \infty$, at least one of $A, C$ is also $+\infty$, confirming the $\infty - \infty$ indeterminacy.

### Conclusion

The Coulomb energy $I(\nu) = \iint \frac{d\nu(x)\,d\nu(y)}{|x-y|^{n-2}}$ is well-defined (avoids $\infty - \infty$) precisely when $B < \infty$, and in that case
$$
I(\nu) = A - 2B + C \geq 0.
$$

Therefore, **whenever the Coulomb energy of a compactly supported signed measure in $\mathbb{R}^{n\geq 3}$ is well-defined, it is non-negative.** $\blacksquare$

---

### Remark (Physical Intuition)

The kernel $\Phi(x) = c_n|x|^{2-n}$ with $c_n = \frac{1}{(n-2)\omega_n} > 0$ is the Newtonian potential, satisfying $-\Delta\Phi = \delta_0$. Setting $u = \Phi * \nu$, we have $-\Delta u = \nu$ in the distributional sense, and formally
$$
I(\nu) = \frac{1}{c_n}\iint \Phi(x-y)\,d\nu(x)\,d\nu(y) = \frac{1}{c_n}\int_{\mathbb{R}^n} |\nabla u|^2\,dx \geq 0,
$$
i.e., the Coulomb energy equals (up to a positive constant) the Dirichlet energy of the potential — the $H^1$ seminorm squared — which is manifestly non-negative. The Fourier regularization argument above makes this rigorous for arbitrary compactly supported signed measures.
