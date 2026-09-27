# Proof

**Answer:** No. There does not necessarily exist such an $r_0$.

We exhibit a surjective entire function $f$ for which $f^{-1}(D(0,r))$ is disconnected for **every** $r > 0$.

---

## The counterexample

Let
$$f(z) = e^z + z.$$

## Step 1. $f$ is surjective

We prove that for every $w \in \mathbb{C}$, the equation $e^z + z = w$ has a solution.

Fix $w \in \mathbb{C}$ and set $g(z) = e^z + z - w$. For a positive integer $N$, consider the rectangle
$$R_N = \{z = x + iy : -N \le x \le N+1,\; -(2N+1)\pi \le y \le (2N+1)\pi\}.$$
We count the zeros of $g$ in $R_N$ via the argument principle, showing the count tends to infinity.

**Right edge** ($x = N+1$, $|y| \le (2N+1)\pi$): Here $|e^z| = e^{N+1}$, while $|z - w| \le |z| + |w| \le (N+1) + (2N+1)\pi + |w| = O(N)$. For $N$ large, $e^{N+1} \gg O(N)$, so $g(z) = e^z(1 + (z-w)/e^z)$ and $\arg g(z) \approx \arg e^z = y$ winds approximately $2(2N+1)$ times (the factor of 2 accounts for the full $2\pi$ range of $y$ over height $2(2N+1)\pi$). More precisely, $g$ is homotopic to $e^z$ on this edge, contributing argument change $\approx 2(2N+1)\pi$.

**Left edge** ($x = -N$, $|y| \le (2N+1)\pi$): Here $|e^z| = e^{-N} \to 0$, while $|z - w| \ge |z| - |w| \ge N - |w| > 0$ for $N$ large. So $g(z) \approx z - w$, and the argument change is that of $z - w$ along a vertical segment of length $2(2N+1)\pi$, which is $\approx 0$ (the segment is nearly vertical through $z = w$-shifted, contributing $O(1)$ net change). The contribution is $O(1)$.

**Top and bottom edges** ($y = \pm(2N+1)\pi$, $-N \le x \le N+1$): On these edges $e^z = e^x \cdot e^{\pm i(2N+1)\pi} = -e^x$ (since $e^{i(2N+1)\pi} = -1$). So $g(z) = -e^x + x \pm i(2N+1)\pi - w$. As $x$ ranges over $[-N, N+1]$, the real part $-e^x + x - \operatorname{Re} w$ is a continuous function going from $-e^{-N} + (-N) - \operatorname{Re} w \to -\infty$ to $-e^{N+1} + (N+1) - \operatorname{Re} w \to -\infty$ (both ends negative, with a maximum in between). The imaginary part is $\pm(2N+1)\pi - \operatorname{Im} w$, which is large and approximately constant. So the argument on each horizontal edge stays near $\pm \pi/2$ (sign matching the edge), contributing $O(1)$ net change each.

**Total argument change:** The dominant contribution is from the right edge, giving $\approx 2(2N+1)\pi$. By the argument principle, the number of zeros of $g$ in $R_N$ is
$$\frac{1}{2\pi} \Delta_{\partial R_N} \arg g \approx 2(2N+1) \xrightarrow{N \to \infty} \infty.$$

Since the zero count in $R_N$ tends to infinity, for every $w$ there exists $N$ with at least one zero in $R_N$. Hence $f$ is surjective. $\square$

*(Remark: this is the classical result that $e^z + az + b$ is surjective for every $a \neq 0$.)*

## Step 2. The critical values of $f$ are unbounded

$$f'(z) = e^z + 1 = 0 \implies z = (2k+1)\pi i, \quad k \in \mathbb{Z}.$$
The critical values are
$$f\big((2k+1)\pi i\big) = e^{(2k+1)\pi i} + (2k+1)\pi i = -1 + (2k+1)\pi i,$$
which lie on the line $\operatorname{Re} = -1$ and satisfy $|f((2k+1)\pi i)| \to \infty$ as $|k| \to \infty$. So the critical values are unbounded.

## Step 3. $f$ has infinitely many zeros tending to infinity

The zeros of $f$ satisfy $e^z = -z$, i.e., $z = -W_k(1)$ where $W_k$ denotes the $k$-th branch of the Lambert $W$-function. There are infinitely many zeros $z_k$ ($k \in \mathbb{Z}$), and their asymptotics are
$$z_k \approx -2k\pi i + \log(2k\pi) + \frac{i\pi}{2} \quad (k \to +\infty),$$
so $|z_k| \to \infty$ and the spacing between consecutive zeros satisfies $|z_{k+1} - z_k| \to 2\pi$.

## Step 4. Each sufficiently large zero lies in an isolated small component of $f^{-1}(D(0,r))$

Fix $r > 0$. We show that for $|z_k|$ large enough, the connected component of $f^{-1}(D(0,r))$ containing $z_k$ is confined to a small disk around $z_k$, disjoint from the components of neighboring zeros.

**Local linearization.** Since $f(z_k) = 0$ and $f'(z_k) = e^{z_k} + 1 = -z_k + 1$, for $z$ near $z_k$:
$$f(z) = f'(z_k)(z - z_k) + \frac{f''(z_k)}{2}(z - z_k)^2 + \cdots$$
where $f''(z_k) = e^{z_k} = -z_k$. So
$$f(z) = (-z_k + 1)(z - z_k) - \frac{z_k}{2}(z - z_k)^2 + O(|z_k|\,|z - z_k|^3).$$

**Estimate on a circle.** Set $\rho = 2r / |z_k|$ and consider the circle $|z - z_k| = \rho$. For $|z_k|$ large (so $\rho$ is small):
$$|f(z)| \ge |f'(z_k)|\,\rho - \frac{|z_k|}{2}\rho^2 - C|z_k|\rho^3$$
$$\ge (|z_k| - 1)\cdot\frac{2r}{|z_k|} - \frac{|z_k|}{2}\cdot\frac{4r^2}{|z_k|^2} - C|z_k|\cdot\frac{8r^3}{|z_k|^3}$$
$$= 2r - \frac{2r}{|z_k|} - \frac{2r^2}{|z_k|} - \frac{8Cr^3}{|z_k|^2}.$$

For $|z_k| > \max(4r + 4r^2 + 1,\; 8Cr)$ this gives $|f(z)| > 2r - r/2 - r/2 = r$ (with room to spare). More concretely, for $|z_k|$ sufficiently large (depending on $r$ and the constant $C$), we have $|f(z)| > r$ on $|z - z_k| = \rho$.

**Conclusion of isolation.** Since $|f| > r$ on the circle $|z - z_k| = \rho$ and $|f(z_k)| = 0 < r$, the component of $f^{-1}(D(0,r))$ containing $z_k$ is contained in the disk $|z - z_k| < \rho = 2r/|z_k|$.

**Disjointness.** The spacing between consecutive zeros tends to $2\pi$. For $|z_k| > r/\pi$ we have $\rho = 2r/|z_k| < 2\pi$, so for $|z_k|$ large enough the disks $|z - z_k| < \rho$ and $|z - z_{k+1}| < \rho$ are disjoint (since $|z_{k+1} - z_k| \to 2\pi > 2\rho$). Moreover, the barrier between consecutive zeros is real: at the midpoint $z_m \approx z_k - \pi i$ between $z_k$ and $z_{k+1}$,
$$e^{z_m} = e^{z_k} \cdot e^{-\pi i} = -e^{z_k} = z_k, \qquad f(z_m) = z_k + (z_k - \pi i) = 2z_k - \pi i,$$
so $|f(z_m)| \approx 2|z_k| \gg r$, confirming no path within $f^{-1}(D(0,r))$ connects the two components.

## Step 5. Conclusion

For any $r > 0$, there are infinitely many zeros $z_k$ with $|z_k|$ exceeding the thresholds of Step 4. Each such zero lies in its own connected component of $f^{-1}(D(0,r))$, and these components are pairwise disjoint. Therefore $f^{-1}(D(0,r))$ has infinitely many connected components, hence is **disconnected**, for every $r > 0$.

Consequently, no $r_0 > 0$ exists for this surjective entire function $f$.

$$\boxed{\text{No. Such } r_0 \text{ need not exist; } f(z)=e^z+z \text{ is a counterexample.}}$$

### PROOF COMPLETE
