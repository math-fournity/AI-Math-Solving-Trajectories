# Proof

## Answer

We exhibit the lens space $L(p,1)$ for any integer $p \geq 2$; in particular $L(2,1) \cong \mathbb{RP}^3$ is a concrete example. We verify that $L(p,1)$ is a smooth, closed, orientable 3-manifold, that $\pi_1(L(p,1)) \cong \mathbb{Z}/p\mathbb{Z}$ contains non-trivial torsion, and that $L(p,1)$ embeds smoothly in $\mathbb{R}^4$.

$$\boxed{L(2,1)\cong\mathbb{RP}^3}$$

---

## Step 1. $L(p,1)$ is a smooth, closed, orientable 3-manifold

Recall the standard definition. Let $\omega = e^{2\pi i/p}$ be a primitive $p$-th root of unity and let $\mathbb{Z}/p\mathbb{Z}$ act on $S^3 \subset \mathbb{C}^2$ by
$$
k\cdot (z_1, z_2) = (\omega^k z_1,\, \omega^k z_2), \qquad k \in \mathbb{Z}/p\mathbb{Z}.
$$
This action is free: if $(\omega^k z_1, \omega^k z_2) = (z_1, z_2)$ with $(z_1,z_2) \in S^3$, then either $\omega^k = 1$ (so $k \equiv 0$) or $(z_1,z_2) = (0,0)$, which is impossible on $S^3$. The action is also orientation-preserving, since it is the restriction of a complex-linear (hence orientation-preserving) map of $\mathbb{C}^2 \cong \mathbb{R}^4$.

By the quotient manifold theorem, the quotient
$$
L(p,1) := S^3 / (\mathbb{Z}/p\mathbb{Z})
$$
is a smooth closed 3-manifold. Since the action preserves orientation, $L(p,1)$ is orientable.

---

## Step 2. $\pi_1(L(p,1))$ has non-trivial torsion

Because $S^3$ is simply connected and the $\mathbb{Z}/p\mathbb{Z}$-action is free and properly discontinuous, the quotient map $S^3 \to L(p,1)$ is the universal covering, with deck group $\mathbb{Z}/p\mathbb{Z}$. Hence
$$
\pi_1(L(p,1)) \cong \mathbb{Z}/p\mathbb{Z}.
$$
For $p \geq 2$, every non-identity element has order $p$, so $\pi_1(L(p,1))$ contains non-trivial torsion.

---

## Step 3. $L(p,1)$ embeds smoothly in $\mathbb{R}^4$

We use the description of $L(p,1)$ as **Dehn surgery on the unknot** and realize the surgery inside $S^4$, then pass to $\mathbb{R}^4$.

### 3.1. Dehn surgery description

Let $U \subset S^3$ be the unknot and let $N(U) \cong S^1 \times D^2$ be a tubular neighborhood. On $T = \partial N(U)$ let $\mu$ be the meridian (the curve bounding a disk in $N(U)$) and $\lambda$ the preferred longitude (the curve bounding a disk in $S^3 \setminus \operatorname{int} N(U)$, i.e. linking $U$ zero times). It is classical (see e.g. Rolfsen, *Knots and Links*) that $L(p,1)$ is obtained from $S^3$ by $p/1$ Dehn surgery on $U$:
$$
L(p,1) = \bigl(S^3 \setminus \operatorname{int} N(U)\bigr) \;\cup_{\varphi}\; V,
$$
where $V \cong S^1 \times D^2$ is a solid torus and the gluing map $\varphi : \partial V \to T$ sends the meridian $m_V = \{\mathrm{pt}\}\times \partial D^2$ of $V$ to the curve $p\mu + \lambda$ on $T$.

### 3.2. The curve $p\mu + \lambda$ is an unknot

The curve $p\mu + \lambda$ on $T = \partial N(U)$ is, by definition, the $(p,1)$-torus knot $T(p,1)$ on the boundary of the tubular neighborhood of the unknot. The genus of the $(p,q)$-torus knot is
$$
g\bigl(T(p,q)\bigr) = \frac{|pq| - |p| - |q| + 1}{2}.
$$
For $q = 1$:
$$
g\bigl(T(p,1)\bigr) = \frac{p - p - 1 + 1}{2} = 0.
$$
A knot of genus $0$ is the unknot. Hence **$p\mu + \lambda$ is an unknot in $S^3$**, and in particular it bounds a smoothly embedded disk $D \subset S^3$.

### 3.3. Realizing the surgery inside $S^4$

Write $S^4 = D^4_+ \cup_{S^3} D^4_-$ as the union of two 4-balls glued along their common boundary $S^3$ (the "equator"). Place the unknot $U$ in this equatorial $S^3$.

- **The exterior $E := S^3 \setminus \operatorname{int} N(U)$** is a solid torus. We leave it untouched inside the equatorial $S^3 \subset S^4$.

- **The new solid torus $V$** must be embedded in $D^4_+$ so that $\partial V = T = \partial N(U) \subset S^3 = \partial D^4_+$ and so that a meridian disk of $V$ has boundary $p\mu + \lambda$.

  Since $p\mu + \lambda$ is an unknot in $S^3$, it bounds a smooth disk $D_0 \subset S^3$. Push the interior of $D_0$ slightly into the interior of $D^4_+$ to obtain a smooth properly embedded disk $D_+ \subset D^4_+$ with $\partial D_+ = p\mu + \lambda \subset S^3$. A regular neighborhood of $D_+$ in $D^4_+$ is a 2-handle $D^2 \times D^2$; its boundary contribution to $\partial D^4_+ = S^3$ is a tubular neighborhood of $p\mu + \lambda$ in $S^3$. Attaching to this 2-handle a 1-handle (a small $D^1 \times D^3$) running along the remaining direction of $T$ produces a solid torus $V \subset D^4_+$ with
  $$
  \partial V = T, \qquad \text{meridian of } V = p\mu + \lambda.
  $$
  Concretely: the core circle of $V$ (the $S^1$-factor) runs once along $\lambda$; the meridian disk of $V$ is the pushed-in disk $D_+$ whose boundary is $p\mu + \lambda$. This is exactly the gluing data of $p/1$ surgery.

- **Gluing.** The exterior $E \subset S^3$ and the new torus $V \subset D^4_+$ share the common boundary $T \subset S^3 = \partial D^4_+$. After a small collar smoothing (standard in differential topology; the two pieces meet along a clean common boundary and are smoothed in a bicollar neighborhood of $T$), their union
  $$
  M := E \cup_T V \;\subset\; S^3 \cup D^4_+ = D^4_+ \cup_{S^3} D^4_+ \;\subset\; S^4
  $$
  is a smoothly embedded closed 3-manifold. By the surgery description of §3.1, $M \cong L(p,1)$.

  (Equivalently and more compactly: the 4-dimensional 2-handlebody $D^4_+ \cup (\text{2-handle along } p\mu+\lambda)$ has boundary $L(p,1)$; this boundary sits inside $S^4$ as the interface between the handlebody and its complementary piece $D^4_- \cup (\text{dual 2-handle})$.)

### 3.4. Passing from $S^4$ to $\mathbb{R}^4$

We have produced a smooth embedding $L(p,1) \hookrightarrow S^4$. Choose a point $q \in S^4 \setminus L(p,1)$ (possible since $L(p,1)$ is a compact 3-dimensional subset of the 4-manifold $S^4$). Stereographic projection from $q$ gives a diffeomorphism
$$
S^4 \setminus \{q\} \;\xrightarrow{\;\cong\;}\; \mathbb{R}^4,
$$
and restricting to $L(p,1) \subset S^4 \setminus \{q\}$ yields a smooth embedding
$$
L(p,1) \;\hookrightarrow\; \mathbb{R}^4.
$$

---

## Conclusion

For any $p \geq 2$, the lens space $L(p,1)$ is:

1. **smooth and closed**, being the quotient of $S^3$ by a free smooth $\mathbb{Z}/p\mathbb{Z}$-action (Step 1);
2. **with non-trivial torsion in $\pi_1$**, since $\pi_1(L(p,1)) \cong \mathbb{Z}/p\mathbb{Z}$ (Step 2);
3. **smoothly embedded in $\mathbb{R}^4$**, via the Dehn-surgery construction in $S^4$ followed by stereographic projection (Step 3).

Taking $p = 2$ gives the explicit example $L(2,1) \cong \mathbb{RP}^3$, with $\pi_1(\mathbb{RP}^3) \cong \mathbb{Z}/2\mathbb{Z}$.

$$
\boxed{L(2,1)\cong\mathbb{RP}^3}
$$

### PROOF COMPLETE
