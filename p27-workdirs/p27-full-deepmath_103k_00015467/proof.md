# Solution

**Answer: TRUE.**

## Precise reformulation

The condition "the supremum of $|f(z_j)|$ over all sequences $(z_j)_{j\ge 1}\subset U$ converging to $a$ is unbounded" means

$$\sup\bigl\{\limsup_{j\to\infty}|f(z_j)|:(z_j)\subset U,\ z_j\to a\bigr\}=\infty,$$

which is equivalent to: $f$ is unbounded on $U\cap B(a,r)$ for every $r>0$, i.e.

$$\forall r>0:\ \sup\{|f(z)|:z\in U\cap B(a,r)\}=\infty.$$

Indeed, the supremum over all sequences tending to $a$ equals $\infty$ iff for every $M>0$ there is a sequence $z_j\to a$ with $\limsup|f(z_j)|>M$, iff for every $M,r>0$ there exists $z\in U\cap B(a,r)$ with $|f(z)|>M$.

## The $n=1$ case (warm-up)

For $U\subset\mathbb{C}$ any open set and any $a\in\partial U$, the function $f(z)=1/(z-a)\in H(U)$ (since $a\notin U$) satisfies $|f(z)|\to\infty$ as $z\to a$. So the statement holds trivially.

## General case: Baire category argument

We give a unified proof (valid for all $n\ge 1$) using the Cartan–Thullen theorem and the Baire category theorem.

**Cartan–Thullen theorem.** A domain $U\subset\mathbb{C}^n$ is a domain of holomorphy if and only if $U$ is holomorphically convex, i.e., for every compact $K\subset U$ the holomorphically convex hull

$$\widehat{K}_U=\{z\in U:|f(z)|\le\sup_K|f|\text{ for all }f\in H(U)\}$$

is compact in $U$.

We prove:

> **Claim.** If $U$ is holomorphically convex, then for every $a\in\partial U$ there exists $f\in H(U)$ unbounded on $U\cap B(a,r)$ for every $r>0$.

*Proof by contradiction.* Suppose there exists $a\in\partial U$ such that every $f\in H(U)$ is bounded on $U\cap B(a,r_f)$ for some $r_f>0$.

**Step 1 (Setup).** For $m\ge 1$ and $M\ge 1$ (integers), define

$$U_m:=U\cap B(a,1/m),\qquad H_{m,M}:=\{f\in H(U):\sup_{U_m}|f|\le M\}.$$

**Step 2 ($H_{m,M}$ is closed).** Equip $H(U)$ with the Fréchet topology of uniform convergence on compact subsets of $U$. If $f_k\in H_{m,M}$ and $f_k\to f$ uniformly on compact sets, then for every $z\in U_m$ (the singleton $\{z\}$ is compact) we have $f_k(z)\to f(z)$, so $|f(z)|=\lim|f_k(z)|\le M$. Hence $f\in H_{m,M}$, and $H_{m,M}$ is closed.

**Step 3 (Covering).** By our assumption, every $f\in H(U)$ is bounded on some $U_m$, hence $f\in H_{m,M}$ for some $m$ and some $M\ge\lceil\sup_{U_m}|f|\rceil$. Therefore

$$H(U)=\bigcup_{m=1}^{\infty}\bigcup_{M=1}^{\infty}H_{m,M}.$$

**Step 4 (Baire category).** $H(U)$ with the compact-open topology is a Fréchet space, hence a Baire space. A countable union of closed sets covering a Baire space must have one member with nonempty interior. So there exist $m,M$ such that $H_{m,M}$ has nonempty interior: there exist $f_0\in H(U)$, a compact $K\subset U$, and $\varepsilon>0$ with

$$\{g\in H(U):\sup_K|g-f_0|<\varepsilon\}\subset H_{m,M}.$$

**Step 5 (Deriving a uniform bound).** If $\sup_K|g|<\varepsilon$, then $f_0+g$ and $f_0-g$ both lie in $H_{m,M}$, so on $U_m$:

$$|f_0+g|\le M,\qquad |f_0-g|\le M.$$

By the triangle inequality, $|g|\le M$ on $U_m$. By homogeneity, for any $h\in H(U)$ and any $c>0$ with $c\sup_K|h|<\varepsilon$ (i.e. $g=ch$), we get $c\sup_{U_m}|h|\le M$, hence

$$\sup_{U_m}|h|\le\frac{M}{\varepsilon}\sup_K|h|,\qquad\forall\,h\in H(U).\tag{$\ast$}$$

**Step 6 ($U_m\subset\widehat{K}_U$).** Inequality $(\ast)$ says: for every $z\in U_m$ and every $h\in H(U)$,

$$|h(z)|\le\frac{M}{\varepsilon}\sup_K|h|.$$

Since the constant factor $M/\varepsilon$ can be absorbed by rescaling $h$ (replace $h$ by $(M/\varepsilon)h$ in the hull definition), this is equivalent to: $|h(z)|\le\sup_K|h|$ for all $h\in H(U)$, i.e. $z\in\widehat{K}_U$. Therefore

$$U_m\subset\widehat{K}_U.$$

**Step 7 (Contradiction).** By holomorphic convexity, $\widehat{K}_U$ is compact in $U$, so

$$\delta:=d(\widehat{K}_U,\partial U)>0.$$

On the other hand, $a\in\partial U$ and $U_m=U\cap B(a,1/m)$ is nonempty for all $m$ (since $a$ is a boundary point, every neighborhood of $a$ meets $U$). Pick $z\in U_m$; then $d(z,\partial U)\le|z-a|<1/m$. Choosing $m>1/\delta$ gives $d(z,\partial U)<\delta=d(\widehat{K}_U,\partial U)$, so $z\notin\widehat{K}_U$—contradicting $U_m\subset\widehat{K}_U$ from Step 6.

This contradiction refutes our assumption. Hence there exists $f\in H(U)$ that is unbounded on $U\cap B(a,r)$ for every $r>0$, i.e.,

$$\sup\bigl\{\limsup_{j\to\infty}|f(z_j)|:(z_j)\subset U,\ z_j\to a\bigr\}=\infty.\qquad\square$$

## Conclusion

The statement is **true**: for every boundary point $a\in\partial U$ of a domain of holomorphy $U\subset\mathbb{C}^n$, there exists $f\in H(U)$ such that $\sup\{\limsup_{j}|f(z_j)|:z_j\to a\}=\infty$.

$$\boxed{\text{True}}$$

### PROOF COMPLETE
