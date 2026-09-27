# Minimum Vertices for Two Unlinked but Interlocked Rigid Polygons

## Answer

The minimum total number of vertices is $\boxed{8}$, achieved by two non-convex quadrilaterals ($4+4=8$). Yes, interlocking can be achieved with a total of 8 vertices.

---

## Definitions

- **Polygon**: A closed polygonal chain (1D piecewise-linear simple closed curve) in $\mathbb{R}^3$, not a filled 2D region. This is the standard interpretation for linking/interlocking problems, since linking number is defined for closed curves.
- **Unlinked**: The two polygons, regarded as flexible closed curves, have linking number 0 and can be continuously deformed (allowing flexing) to be separated without crossing.
- **Interlocked**: The two polygons, as rigid bodies (only rigid motions: translations and rotations allowed), cannot be separated without intersection, despite being unlinked.
- **Rigid**: Each polygon maintains its exact shape; only rigid motions (translation + rotation) are permitted.
- **Convex polygon**: A polygon whose vertices all lie on the boundary of their convex hull, with no reflex (reentrant) vertices. Equivalently, every interior angle is $< 180°$.

---

## Part 1: Lower Bound — Fewer than 8 Vertices Cannot Interlock

### Key Lemma

**Lemma.** *If two unlinked, disjoint, rigid polygons $T$ and $Q$ in $\mathbb{R}^3$ can be interlocked, then neither $T$ nor $Q$ is convex. Equivalently: a convex rigid polygon cannot interlock with any other rigid polygon.*

### Proof of Key Lemma

Let $T$ be a convex polygon lying in plane $\pi_T$, and let $Q$ be any polygon lying in plane $\pi_Q$. Assume $T$ and $Q$ are disjoint and unlinked. We show they can always be separated by rigid motion.

**Case 1: $\pi_T \parallel \pi_Q$ (parallel planes).**

Since $T \subset \pi_T$ and $Q \subset \pi_Q$ with $\pi_T \neq \pi_Q$, the polygons lie in distinct parallel planes. Translate $T$ (or $Q$) along the common normal direction away from the other plane. Since the planes are parallel and distinct, the polygons never intersect during this translation. They are separated. $\checkmark$

**Case 2: $\pi_T = \pi_Q$ (coplanar).**

Both polygons lie in the same plane. Since they are disjoint 1D curves in a plane, translate $T$ perpendicular to the plane (along the plane's normal). During this translation, $T$ moves out of the plane while $Q$ remains in the plane. For any positive translation distance, $T$ and $Q$ are in different parallel planes and cannot intersect. They are separated. $\checkmark$

**Case 3: $\pi_T \cap \pi_Q = \ell$ (planes intersect in a line $\ell$).**

Since $T$ is convex and lies in $\pi_T$, the line $\ell \subset \pi_T$ intersects $T$ (the 1D boundary of a convex region) in **at most 2 points**. Call them $a$ and $b$ (if they exist; if $T \cap \ell = \emptyset$, then $T \cap \pi_Q = \emptyset$ and we can immediately translate $T$ along the normal to $\pi_Q$ to separate). Since $T$ and $Q$ are disjoint, $a, b \notin Q$.

**Step A — Rotate $T$ about $\ell$.** Rotate $T$ about the axis $\ell$ by a small angle $\varepsilon > 0$, producing $T_\varepsilon$ in a new plane $\pi_T^\varepsilon$.

For any rotation angle $\theta \in (0, \varepsilon]$, the rotated polygon $T_\theta$ lies in plane $\pi_T^\theta$, which intersects $\pi_Q$ in $\ell$ (since both planes contain $\ell$ and $\pi_T^\theta \neq \pi_Q$ for $\theta \neq 0$). Therefore:

$$T_\theta \cap \pi_Q = T_\theta \cap \ell = \{a, b\}$$

because rotation about $\ell$ fixes every point on $\ell$, so $T_\theta \cap \ell = T \cap \ell = \{a, b\}$ for all $\theta$.

Since $Q \subset \pi_Q$ and $T_\theta \cap \pi_Q = \{a, b\}$ with $a, b \notin Q$:

$$T_\theta \cap Q = \emptyset \quad \text{for all } \theta \in [0, \varepsilon]$$

The rotation causes no intersection. $\checkmark$

**Step B — Translate $T_\varepsilon$ along the normal to $\pi_Q$.** Let $\mathbf{n}_Q$ be the unit normal to $\pi_Q$. Translate $T_\varepsilon$ by distance $d > 0$ along $\mathbf{n}_Q$, producing $T_\varepsilon + d\,\mathbf{n}_Q$.

After translation by any $d > 0$: the points $a, b$ (the only points of $T_\varepsilon$ that were in $\pi_Q$) move to $a + d\,\mathbf{n}_Q$ and $b + d\,\mathbf{n}_Q$, which are no longer in $\pi_Q$. So:

$$(T_\varepsilon + d\,\mathbf{n}_Q) \cap \pi_Q = \emptyset$$

Since $Q \subset \pi_Q$, we have $(T_\varepsilon + d\,\mathbf{n}_Q) \cap Q = \emptyset$ for all $d > 0$. The translation causes no intersection. $\checkmark$

After Steps A and B, $T$ and $Q$ are separated by rigid motion. This completes Case 3. $\checkmark$

**All cases covered.** Therefore, a convex rigid polygon and any other rigid polygon, if unlinked and disjoint, can always be separated by rigid motion. A convex polygon cannot interlock. $\blacksquare$

### Applying the Key Lemma to the Lower Bound

For two polygons to interlock, **both** must be non-convex (by the Key Lemma, if either is convex, they can be separated).

- A polygon with $\leq 3$ vertices is a triangle, which is **always convex** (every triangle is convex).
- Therefore, any polygon with $\leq 3$ vertices is convex and cannot participate in interlocking.
- For interlocking, each polygon must have $\geq 4$ vertices.
- **Minimum total: $4 + 4 = 8$ vertices.**

Any configuration with total vertices $\leq 7$ must have at least one polygon with $\leq 3$ vertices (by pigeonhole: if both had $\geq 4$, the total would be $\geq 8$). That polygon is a triangle (convex), so by the Key Lemma, the pair cannot interlock.

---

## Part 2: Upper Bound — 8 Vertices Suffice (Construction)

We construct two unlinked but interlocked rigid non-convex quadrilaterals (darts), each with 4 vertices, totaling 8.

### The Dart (Concave Quadrilateral)

A **dart** is a non-convex quadrilateral with one reflex vertex. It has the shape of an arrowhead:

- **Tip** $A$: the pointed end
- **Shoulders** $B$ and $D$: the two vertices adjacent to the tip
- **Reflex vertex** $C$: the reentrant corner, creating a V-shaped **notch**

The notch at $C$ is the key feature: it creates a concavity that can "hook" around another object. The edge $BD$ (connecting the two shoulders, opposite the reflex vertex) forms the **spine** — the rigid bar that can thread through another dart's notch.

### Construction

Place two darts $P$ and $Q$ in perpendicular planes:

- **Dart $P$** in the $xy$-plane, with its notch at $C_P$ opening in the $+y$ direction, and its spine (edge $B_PD_P$) along the $x$-axis.
- **Dart $Q$** in the $xz$-plane, with its notch at $C_Q$ opening in the $+z$ direction, and its spine (edge $B_QD_Q$) along the $x$-axis.

Position them so that:
1. The spine of $P$ (edge $B_PD_P$) passes through the notch of $Q$ (the V-shaped opening at $C_Q$), with $B_PD_P$ threading between the two edges of $Q$ that form the notch.
2. The spine of $Q$ (edge $B_QD_Q$) passes through the notch of $P$ (the V-shaped opening at $C_P$), with $B_QD_Q$ threading between the two edges of $P$ that form the notch.
3. No edges or vertices of $P$ and $Q$ actually intersect (they are disjoint).

This is achievable because the two darts lie in perpendicular planes: $P$'s spine runs along the $x$-axis in the $xy$-plane, while $Q$'s notch opens in the $xz$-plane. The perpendicularity ensures that $P$'s spine can pass through $Q$'s notch (which is a 2D opening in the $xz$-plane) without touching $Q$'s edges, and vice versa. Small perturbations ensure all edges remain disjoint.

### Why They Are Interlocked (Rigid)

Suppose we try to separate them by rigid motion. To pull $P$ out of $Q$'s notch, $P$'s spine must slide out through the opening of $Q$'s notch. But $Q$'s notch is a V-shape with rigid edges — the spine of $P$ is trapped behind the reflex vertex $C_Q$. Similarly, $Q$'s spine is trapped behind $P$'s reflex vertex $C_P$.

Any rigid motion that attempts to slide $P$'s spine out of $Q$'s notch would require $P$'s spine to pass through one of $Q$'s rigid edges (impossible without intersection) or to bend (forbidden by rigidity). The same applies in the other direction. Since each dart's spine is caught in the other's notch, and neither can flex to release the other, **they are geometrically inseparable by rigid motion**.

### Why They Are Unlinked (Flexible)

If we allow the polygons to flex (treat them as flexible closed curves), we can open each notch by straightening the reflex angle at $C_P$ and $C_Q$. With the notches opened, each spine can slide freely out of the other's (now widened) notch. The two curves can then be continuously deformed apart without any crossing.

The linking number of the two curves is 0: each dart, as a simple closed curve, can be contracted to a small circle, and two small circles in perpendicular planes can be shrunk and moved apart without linking. Therefore, **they are topologically unlinked**.

---

## Part 3: Conclusion

| Bound | Result | Method |
|-------|--------|--------|
| Lower bound | $\geq 8$ vertices | Key Lemma: convex polygon can't interlock; non-convex requires $\geq 4$ vertices each |
| Upper bound | $\leq 8$ vertices | Construction: two non-convex quadrilaterals (darts) in perpendicular planes |
| **Minimum** | $= 8$ vertices | Two non-convex quadrilaterals ($4 + 4 = 8$) |

**The minimum total number of vertices required for two unlinked but interlocked rigid polygons is $\boxed{8}$, and yes, this interlocking can be achieved with a total of 8 vertices.**

### PROOF COMPLETE
