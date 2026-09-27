# Maximal Number of Real Intersections of the Unbounded Components of Two Plane Cubics

## Answer

$$\boxed{9}$$

## Proof

We work over the real projective plane $\mathbb{RP}^2$. A **plane cubic curve** is a real algebraic curve defined by a homogeneous polynomial of degree 3 in three variables. We consider smooth (nonsingular) real cubics.

### Step 1: Topology of a Real Cubic in $\mathbb{RP}^2$

By Harnack's theorem, a smooth real curve of genus $g$ has at most $g+1$ connected components in its real locus. A smooth plane cubic has genus $g=1$, so its real locus has at most $2$ connected components. There are two cases:

- **Type II (one component):** The real locus is a single connected component that is **non-contractible** in $\mathbb{RP}^2$ (i.e., it represents the non-trivial element of $H_1(\mathbb{RP}^2, \mathbb{Z}/2) \cong \mathbb{Z}/2$). Such a component is called a **pseudo-line**. In any affine chart $\mathbb{R}^2 \subset \mathbb{RP}^2$, this component is **unbounded**.

- **Type I (two components):** The real locus consists of one **oval** (a contractible component, which is bounded in a suitable affine chart) and one **pseudo-line** (non-contractible, unbounded in the affine chart).

In both cases, the cubic has exactly one **unbounded component** (in the affine sense), which corresponds to the unique **pseudo-line** (non-contractible component) in $\mathbb{RP}^2$.

### Step 2: Parity Constraint on Pseudo-Line Intersections

The unbounded components of $C_1$ and $D_1$ are pseudo-lines in $\mathbb{RP}^2$. Each pseudo-line represents the generator of $H_1(\mathbb{RP}^2, \mathbb{Z}/2) \cong \mathbb{Z}/2$. By mod 2 intersection theory, the intersection number of two pseudo-lines is:

$$[C_1^{\text{unbounded}}] \cdot [D_1^{\text{unbounded}}] \equiv 1 \pmod{2}.$$

Therefore, the two unbounded components must intersect in an **odd** number of real points (counted with multiplicity).

### Step 3: Bézout Upper Bound

By Bézout's theorem, two plane cubics in $\mathbb{CP}^2$ intersect in exactly $3 \times 3 = 9$ points counted with multiplicity. Therefore, the total number of real intersection points (across all components) is at most $9$. In particular, the number of real intersections of the unbounded components is at most $9$.

Combining with Step 2, the number of real intersections of the unbounded components is an **odd** number at most $9$, so it is at most $9$.

### Step 4: Achievability — Two Type II Cubics with 9 Real Transverse Intersections

It remains to show that $9$ is achievable. We construct two smooth real cubics, both of Type II, whose unbounded components (which are their entire real loci) meet in $9$ real transverse points.

**Construction.** Let $E$ be a smooth real cubic of Type II, for instance the projective closure of
$$y^2 = x^3 + x,$$
whose real locus $E(\mathbb{R})$ is a single pseudo-line (topologically a circle). Choose $9$ distinct real points $P_1, \dots, P_9$ on $E(\mathbb{R})$ in general position (no three collinear, no six on a conic).

The space of plane cubics is $\mathbb{P}^9$ (projectively 9-dimensional). The $9$ points $P_1, \dots, P_9$ impose $9$ linear conditions, leaving a **pencil** (a $\mathbb{P}^1$-family) of cubics through all $9$ points. One member of this pencil is $E$ itself.

A pencil of cubics has at most $12$ singular members (by the discriminant). The topological type of the real locus (Type I vs. Type II) is constant on each connected interval of smooth cubics in the pencil, and can change only when passing through a singular member. Since $E$ is a smooth Type II cubic, there exists an open interval in the pencil around $E$ consisting entirely of smooth Type II cubics.

Choose a cubic $D \neq E$ from this interval. Then:

- $D$ is smooth and Type II, so its real locus $D(\mathbb{R})$ is a single pseudo-line (the unbounded component).
- $E$ is smooth and Type II, so $E(\mathbb{R})$ is a single pseudo-line (the unbounded component).
- $E \cap D = \{P_1, \dots, P_9\}$ by Bézout's theorem (both are degree 3, and they share exactly these $9$ points).
- For a general choice of $P_1, \dots, P_9$, all $9$ intersection points are **transverse** (since $D$ is not tangent to $E$ at any of these points).

Thus, the unbounded components of $E$ and $D$ (which are their entire real loci) intersect in exactly $9$ real points.

### Conclusion

The number of real intersections of the unbounded components of two plane cubics is an odd number bounded above by $9$ (by the mod 2 intersection constraint and Bézout's theorem), and $9$ is achieved by the construction above. Therefore, the maximal number is:

$$\boxed{9}$$
