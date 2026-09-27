# Proof: Map from a Bounded Region in $\mathbb{R}^2$ to $S^2$ with Jacobian Bounded Away from Zero and Infinity

## Answer

**Yes**, it is possible.

## Proof

We construct an explicit map with the desired property using **stereographic projection**.

### Construction

Let $\Omega = \{(x, y) \in \mathbb{R}^2 : x^2 + y^2 \leq 1\}$ be the closed unit disk, which is a bounded region in $\mathbb{R}^2$.

Define $f: \Omega \to S^2$ by stereographic projection from the north pole $N = (0, 0, 1)$:

$$f(x, y) = \left(\frac{2x}{1 + x^2 + y^2},\; \frac{2y}{1 + x^2 + y^2},\; \frac{x^2 + y^2 - 1}{1 + x^2 + y^2}\right).$$

This map is smooth on $\Omega$ (the denominator $1 + x^2 + y^2 \geq 1 > 0$ everywhere) and maps into $S^2 \setminus \{N\} \subset S^2$.

### Computing the Jacobian

Stereographic projection is a **conformal** map with conformal factor

$$\lambda(x, y) = \frac{2}{1 + x^2 + y^2}.$$

The induced metric (pullback of the round metric on $S^2$) is $g = \lambda^2 (dx^2 + dy^2)$, so the area distortion factor (Jacobian determinant) is:

$$J_f(x, y) = \lambda^2 = \frac{4}{(1 + x^2 + y^2)^2}.$$

**Derivation of the conformal factor.** Writing $r^2 = x^2 + y^2$ and $D = 1 + r^2$, we compute the partial derivatives:

$$\frac{\partial f}{\partial x} = \left(\frac{2(D - 2x^2)}{D^2},\; \frac{-4xy}{D^2},\; \frac{4x}{D^2}\right), \qquad \frac{\partial f}{\partial y} = \left(\frac{-4xy}{D^2},\; \frac{2(D - 2y^2)}{D^2},\; \frac{4y}{D^2}\right).$$

The coefficients of the first fundamental form are:

$$E = \left\|\frac{\partial f}{\partial x}\right\|^2 = \frac{4}{D^2}, \qquad F = \left\langle \frac{\partial f}{\partial x}, \frac{\partial f}{\partial y} \right\rangle = 0, \qquad G = \left\|\frac{\partial f}{\partial y}\right\|^2 = \frac{4}{D^2}.$$

(One verifies $E = G$ and $F = 0$ by direct computation, confirming conformality.) Therefore:

$$J_f = \sqrt{EG - F^2} = \sqrt{\frac{16}{D^4}} = \frac{4}{(1 + x^2 + y^2)^2}.$$

### Bounding the Jacobian on $\Omega$

On the closed unit disk $\Omega$, we have $0 \leq x^2 + y^2 \leq 1$, so:

$$1 \leq 1 + x^2 + y^2 \leq 2.$$

Squaring: $1 \leq (1 + x^2 + y^2)^2 \leq 4$. Taking reciprocals (all positive):

$$\frac{1}{4} \leq \frac{1}{(1 + x^2 + y^2)^2} \leq 1.$$

Multiplying by 4:

$$\boxed{1 \leq J_f(x, y) \leq 4 \quad \text{for all } (x, y) \in \Omega.}$$

Thus $J_f$ is bounded below by $c = 1 > 0$ and above by $C = 4 < \infty$ on $\Omega$.

### Geometric Interpretation

The map $f$ sends the unit disk $\Omega$ onto the **closed southern hemisphere** of $S^2$:
- The origin $(0,0)$ maps to the south pole $(0, 0, -1)$.
- The boundary circle $x^2 + y^2 = 1$ maps to the equator $(\cdot, \cdot, 0)$.
- The Jacobian equals 1 at the origin (no distortion at the south pole) and equals $1/4 \cdot 4 = 1$... 

Actually, at the origin: $J_f(0,0) = 4/(1+0)^2 = 4$. At the boundary: $J_f = 4/(1+1)^2 = 4/4 = 1$. So the distortion ranges from 1 (at the equator) to 4 (at the south pole), both finite and positive.

### Conclusion

The stereographic projection $f: \Omega \to S^2$, restricted to the closed unit disk $\Omega$, is a smooth map from a bounded region in $\mathbb{R}^2$ to $S^2$ whose Jacobian determinant satisfies $1 \leq J_f \leq 4$, hence is bounded away from both zero and infinity.

$$\boxed{\text{Yes}}$$

## Remark (Surjective Case)

If one additionally requires the map to be **surjective** onto $S^2$, then no such map exists:

- If $|J_f|$ is bounded away from zero, then $f$ is a local diffeomorphism.
- If $\Omega$ is compact (closed and bounded) and $f$ is surjective, then $f$ is a **covering map**.
- Since $S^2$ is simply connected, any covering map to $S^2$ is a homeomorphism.
- But no subset of $\mathbb{R}^2$ is homeomorphic to $S^2$ (e.g., $H_2(\Omega) = 0$ for any $\Omega \subset \mathbb{R}^2$, while $H_2(S^2) = \mathbb{Z}$; or by invariance of domain).

If $\Omega$ is open and bounded, then a surjective local diffeomorphism $f: \Omega \to S^2$ would make $\Omega$ a covering space of the compact space $S^2$, forcing $\Omega$ to be compact — contradicting openness.

Thus the surjective version is impossible, but the non-surjective version (as stated) is possible.
