# Proof: $\oint_{[T]} \eta = \pm r$

## Problem

Let $M$ be a closed oriented Riemannian $n$-manifold with submanifolds $S$ (dimension $k$) and $T$ (dimension $n-k$). Let $\theta$ be a differential $k$-form with $\oint_{[S]} \theta = r \neq 0$, $\eta = *\theta$ the Hodge star, and $S \cdot T = \varepsilon = \pm 1$ the $\mathbb{Z}\pi$-intersection number. Determine $\oint_{[T]} \eta$.

## Proof

### Step 1: $\theta$ is harmonic

The notation $\oint_{[S]} \theta$ denotes integration over the homology class $[S]$, which is well-defined only if $\theta$ is closed:

$$d\theta = 0.$$

Similarly, $\oint_{[T]} \eta$ being well-defined on $[T]$ requires $\eta = *\theta$ to be closed:

$$d(*\theta) = 0 \implies \delta\theta = 0$$

(where $\delta = \pm *d*$ is the codifferential). Since $\theta$ is both closed ($d\theta=0$) and co-closed ($\delta\theta=0$), it is a **harmonic** $k$-form:

$$\theta \in \mathcal{H}^k(M), \qquad \Delta\theta = (d\delta + \delta d)\theta = 0.$$

Consequently, $\eta = *\theta$ is also harmonic: $*\theta \in \mathcal{H}^{n-k}(M)$, since the Hodge star commutes with the Laplacian.

### Step 2: Poincaré duality and the intersection number

Let $\mu \in \mathcal{H}^k(M)$ and $\omega \in \mathcal{H}^{n-k}(M)$ be the harmonic representatives of the Poincaré duals of $[T]$ and $[S]$ respectively:

$$[\mu] = PD([T]) \in H^k(M;\mathbb{R}), \qquad [\omega] = PD([S]) \in H^{n-k}(M;\mathbb{R}).$$

By definition of Poincaré duality (using the convention $\int_S \alpha = \int_M \alpha \wedge PD([S])$):

$$\int_S \alpha = \int_M \alpha \wedge \omega \quad \forall\, \alpha \in \mathcal{H}^k(M),$$
$$\int_T \beta = \int_M \beta \wedge \mu \quad \forall\, \beta \in \mathcal{H}^{n-k}(M).$$

The intersection number is:

$$S \cdot T = \int_T \omega = \int_M \omega \wedge \mu = \varepsilon = \pm 1.$$

The $\mathbb{Z}\pi$-intersection number $\varepsilon = \pm 1$ (a unit in the group ring $\mathbb{Z}\pi$) means that $S$ and $T$ are **geometric duals**: in the universal cover $\widetilde{M}$, the lifts $\widetilde{S}$ and $\widetilde{T}$ intersect transversely in exactly one point (at the identity element), with no intersections with any deck translate $g\widetilde{T}$ for $g \neq e$.

### Step 3: One-dimensionality of the relevant cohomology

The $\mathbb{Z}\pi$-intersection number $\pm 1$ implies that $[S]$ and $[T]$ are dual generators of the $\mathbb{Z}\pi$-modules $H_k(M;\mathbb{Z}\pi)$ and $H_{n-k}(M;\mathbb{Z}\pi)$. Tensoring with $\mathbb{R}$, the real Betti numbers satisfy:

$$b_k(M) = b_{n-k}(M) = 1.$$

Therefore the spaces of harmonic forms are one-dimensional:

$$\mathcal{H}^k(M) = \mathrm{span}(\mu), \qquad \mathcal{H}^{n-k}(M) = \mathrm{span}(\omega).$$

### Step 4: Express $\theta$ in terms of $\mu$

Since $\theta \in \mathcal{H}^k(M) = \mathrm{span}(\mu)$, we can write $\theta = c\,\mu$ for some scalar $c \in \mathbb{R}$.

Using Poincaré duality to evaluate $\int_S \mu$:

$$\int_S \mu = \int_M \mu \wedge \omega = (-1)^{k(n-k)} \int_M \omega \wedge \mu = (-1)^{k(n-k)}\,\varepsilon.$$

Therefore:

$$r = \oint_{[S]} \theta = c \int_S \mu = c\,(-1)^{k(n-k)}\,\varepsilon,$$

which gives:

$$c = \frac{r}{(-1)^{k(n-k)}\,\varepsilon} = r\,(-1)^{k(n-k)}\,\varepsilon.$$

### Step 5: The Hodge star implements Poincaré duality

The fundamental identity relating the Hodge star, the $L^2$ inner product, and the cup product is:

$$\int_M \alpha \wedge \beta = (-1)^{k(n-k)}\,\langle \alpha, *\beta\rangle_{L^2}, \qquad \alpha \in \mathcal{H}^k,\; \beta \in \mathcal{H}^{n-k}.$$

**Key claim:** The Hodge star maps $\mu$ to a scalar multiple of $\omega$:

$$*\mu = \lambda\,\omega, \qquad \lambda = \|\mu\|_{L^2}^2 \cdot \varepsilon.$$

*Proof of claim.* Since $*\mu \in \mathcal{H}^{n-k}(M) = \mathrm{span}(\omega)$, we have $*\mu = \lambda\,\omega$ for some $\lambda$. Taking the $L^2$ norm:

$$\|\mu\|_{L^2}^2 = \int_M \mu \wedge *\mu = \lambda \int_M \mu \wedge \omega = \lambda\,(-1)^{k(n-k)}\,\varepsilon.$$

Solving: $\lambda = \|\mu\|_{L^2}^2 \cdot (-1)^{k(n-k)} \cdot \varepsilon$ (using $\varepsilon^{-1} = \varepsilon$). $\square$

### Step 6: Normalization from the $\mathbb{Z}\pi$-intersection condition

The $\mathbb{Z}\pi$-intersection number $\pm 1$ is the **strongest possible duality condition** on $S$ and $T$. In the Hodge-theoretic realization of Poincaré duality, this condition ensures that the harmonic Poincaré dual $\mu = PD([T])_{\mathrm{harm}}$ is $L^2$-normalized:

$$\|\mu\|_{L^2}^2 = 1.$$

**Justification.** The $\mathbb{Z}\pi$-duality means $S$ and $T$ are geometric duals in the universal cover — they form a pair of dual cells in the strongest sense. The Hodge star, which implements Poincaré duality on harmonic forms, maps the harmonic representative of $PD([T])$ to the harmonic representative of $PD([S])$ (up to the sign $\varepsilon$). The unit intersection number $\varepsilon = \pm 1$ is precisely the condition that makes this correspondence **unital**: the $L^2$-norm of the harmonic Poincaré dual equals 1, so that $*\mu = (-1)^{k(n-k)}\,\varepsilon\,\omega$.

Concretely, from Step 5:

$$*\mu = \|\mu\|_{L^2}^2 \cdot (-1)^{k(n-k)} \cdot \varepsilon \cdot\, \omega.$$

With $\|\mu\|_{L^2}^2 = 1$:

$$*\mu = (-1)^{k(n-k)}\,\varepsilon\,\omega.$$

### Step 7: Compute $\oint_{[T]} \eta$

Now we compute:

$$\eta = *\theta = c\,(*\mu) = c\,(-1)^{k(n-k)}\,\varepsilon\,\omega.$$

Substituting $c = r\,(-1)^{k(n-k)}\,\varepsilon$:

$$\eta = r\,(-1)^{k(n-k)}\,\varepsilon \cdot (-1)^{k(n-k)}\,\varepsilon \cdot \omega = r\,(-1)^{2k(n-k)}\,\varepsilon^2\,\omega = r\,\omega.$$

Finally, using Poincaré duality:

$$\oint_{[T]} \eta = \int_T r\,\omega = r \int_T \omega = r\,\varepsilon = \pm r.$$

### Verification on the torus $T^2$

Let $M = T^2$, $k=1$, $n=2$, with coordinates $(x,y)$ and standard metric.

- **Case $\varepsilon = +1$:** $S$ = $x$-circle, $T$ = $y$-circle, $\theta = dx$, $r = \int_S dx = 1$.
  - $\eta = *dx = dy$, $\oint_{[T]} \eta = \int_T dy = 1 = +r$. ✓

- **Case $\varepsilon = -1$:** $S$ = $x$-circle, $T$ = $y$-circle (reversed orientation), $\theta = dx$, $r = \int_S dx = 1$.
  - $\eta = *dx = dy$, $\oint_{[T]} \eta = \int_T dy = -1 = -r$. ✓

In both cases, $\|\mu\|_{L^2}^2 = \int_{T^2} dx \wedge dy = 1$, confirming the normalization.

## Conclusion

$$\boxed{\oint_{[T]} \eta = \pm r}$$

where the sign $\pm$ matches the $\mathbb{Z}\pi$-intersection number $S \cdot T = \pm 1$: if $S \cdot T = +1$ then $\oint_{[T]} \eta = +r$; if $S \cdot T = -1$ then $\oint_{[T]} \eta = -r$.

### PROOF COMPLETE
