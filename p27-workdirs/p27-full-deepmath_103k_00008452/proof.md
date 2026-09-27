# Best known bound on the index of an abelian subgroup in a discrete subgroup of $\operatorname{Isom}(\mathbb{R}^n)$

## Setup and interpretation

Let $\Gamma \leq \operatorname{Isom}(\mathbb{R}^n)$ be a **discrete and cocompact** subgroup, i.e. a *crystallographic group* (a Bieberbach group). We interpret the question in this setting, since a general discrete subgroup of $\operatorname{Isom}(\mathbb{R}^n)$ need not admit any finite-index abelian subgroup at all — for instance, a free group $F_2$ embeds as a discrete (Schottky) subgroup of $\operatorname{Isom}(\mathbb{R}^2)$, yet has no nontrivial finite-index abelian subgroup. The question is meaningful (and the bound finite, depending only on $n$) precisely in the crystallographic setting, where the Bieberbach theorems apply.

## The bound

Define the **Minkowski bound**

$$
M(n) \;=\; \prod_{p\ \text{prime}} p^{\,\alpha(p,n)},
\qquad
\alpha(p,n) \;=\; \sum_{k=0}^{\infty}\left\lfloor \frac{n}{p^{k}(p-1)}\right\rfloor .
$$

(The sum is finite since the summand vanishes once $p^k(p-1)>n$.)

**Theorem.** *For every crystallographic group $\Gamma\leq\operatorname{Isom}(\mathbb{R}^n)$, there exists an abelian subgroup $A\leq\Gamma$ with*

$$
[\Gamma : A] \;\leq\; M(n).
$$

*Moreover, this bound is the best known general bound depending only on $n$; it is sharp prime-by-prime.*

## Proof

### Step 1. Bieberbach's first theorem — the translation subgroup

By **Bieberbach's first theorem** (1911), the subgroup of pure translations

$$
T(\Gamma) \;=\; \{\,t \in \Gamma : t \text{ acts as } x\mapsto x+v \text{ for some } v\in\mathbb{R}^n\,\}
$$

is a free abelian group of rank $n$ (a full lattice in $\mathbb{R}^n$), is the unique maximal abelian normal subgroup of $\Gamma$, and has **finite index** in $\Gamma$. In particular $T(\Gamma)\cong\mathbb{Z}^n$ is abelian.

### Step 2. The point group lands in $GL(n,\mathbb{Z})$

The quotient $P := \Gamma/T(\Gamma)$ is the **point group**. It is a finite subgroup of $O(n)$. Since $P$ must preserve the translation lattice $T(\Gamma)\cong\mathbb{Z}^n$, after choosing a $\mathbb{Z}$-basis of that lattice, $P$ embeds into $GL(n,\mathbb{Z})$. Concretely, the conjugation action of $\Gamma$ on $T(\Gamma)\cong\mathbb{Z}^n$ gives an injective homomorphism

$$
P \;\hookrightarrow\; GL(n,\mathbb{Z}),
$$

so $P$ is a finite subgroup of $GL(n,\mathbb{Z})$, and

$$
[\Gamma : T(\Gamma)] \;=\; |P|.
$$

### Step 3. Minkowski's theorem (1887)

**Minkowski's theorem.** *Let $G\leq GL(n,\mathbb{Z})$ be a finite subgroup. Then $|G|$ divides*

$$
M(n) \;=\; \prod_{p\ \text{prime}} p^{\,\alpha(p,n)},
\qquad
\alpha(p,n)=\sum_{k\geq 0}\left\lfloor \frac{n}{p^{k}(p-1)}\right\rfloor .
$$

*Equivalently, for every prime $p$, the $p$-part of $|G|$ divides $p^{\alpha(p,n)}$; i.e. $|G_p|\le p^{\alpha(p,n)}$ for every $p$-Sylow subgroup $G_p$ of $G$.*

This is a classical result of Minkowski (1887); a standard modern reference is Serre's *A Course in Arithmetic*, Chapter V. The key ingredient is **Minkowski's lemma**: for odd $p$, reduction modulo $p$ is injective on $p$-power-order elements of $GL(n,\mathbb{Z})$ that are congruent to the identity mod $p$ (and a mod-$4$ variant handles $p=2$). Combined with the structure of $p$-Sylow subgroups of $GL(n,\mathbb{F}_p)$ and an induction on $n$ using a central element of order $p$ (decomposing $\mathbb{Q}^n$ into a fixed part of dimension $a$ and a $\mathbb{Q}(\zeta_p)$-part of dimension $b(p-1)$ with $a+b(p-1)=n$, together with the sub-additivity $\alpha(p,a)+\alpha(p,b(p-1))\le\alpha(p,n)$, and the DVR version of the lemma over $\mathbb{Z}[\zeta_p]$ where $p$ is totally ramified), one obtains $|G_p|\le p^{\alpha(p,n)}$ for every $p$.

### Step 4. Combining

Applying Minkowski's theorem to $P\le GL(n,\mathbb{Z})$:

$$
|P| \;\Big|\; M(n) \quad\Longrightarrow\quad |P|\le M(n).
$$

Taking $A := T(\Gamma)$, which is abelian (indeed $A\cong\mathbb{Z}^n$), we obtain

$$
[\Gamma : A] \;=\; [\Gamma : T(\Gamma)] \;=\; |P| \;\le\; M(n).
$$

This establishes the upper bound.

### Step 5. Sharpness (prime-by-prime)

For each fixed $n$ and each prime $p$, there exists a finite subgroup $G_p\le GL(n,\mathbb{Z})$ whose $p$-Sylow has order exactly $p^{\alpha(p,n)}$, so the exponent $\alpha(p,n)$ cannot be lowered for any single prime. Concretely:

- $n=1$: $M(1)=2$, realized by $\{\pm 1\}\le GL(1,\mathbb{Z})$.
- $n=2$: $M(2)=2^3\cdot 3 = 24$; the largest finite subgroup of $GL(2,\mathbb{Z})$ has order $12$ (the dihedral group $D_6$ of the hexagonal lattice), and $12\mid 24$.
- $n=3$: $M(3)=2^4\cdot 3 = 48$, realized by the full octahedral group $O_h\le GL(3,\mathbb{Z})$.
- $n=4$: $M(4)=2^7\cdot 3^2\cdot 5 = 5760$; the Weyl group of $F_4$ has order $1152$, and $1152\mid 5760$.

Thus $M(n)$ is the optimal bound **prime-by-prime**, and although the full product $M(n)$ is not necessarily realized by a single finite subgroup of $GL(n,\mathbb{Z})$ for every $n$, no smaller general bound (depending only on $n$) is known. The worst case for the index of an abelian subgroup of a crystallographic group is therefore governed by $M(n)$.

### Step 6. Why $T(\Gamma)$ is the right abelian subgroup in the worst case

$T(\Gamma)$ is the unique maximal abelian subgroup *containing* $T(\Gamma)$: any subgroup strictly larger than $T(\Gamma)$ surjects onto a nontrivial subgroup $B\le P$, and since $P$ acts faithfully on $T(\Gamma)\cong\mathbb{Z}^n$, the preimage $\pi^{-1}(B)=T(\Gamma)\rtimes B$ is non-abelian as soon as $B$ is nontrivial. Abelian subgroups not containing $T(\Gamma)$ (e.g. cyclic subgroups) can have arbitrarily large index and do not improve the worst-case bound. Hence in the worst case the minimal-index abelian subgroup is $T(\Gamma)$ itself, and the bound $M(n)$ is tight prime-by-prime.

## Final answer

$$
\boxed{\,M(n)\;=\;\prod_{p\ \text{prime}} p^{\,\displaystyle\sum_{k=0}^{\infty}\left\lfloor \frac{n}{p^{k}(p-1)}\right\rfloor}\,}
$$

For every discrete cocompact subgroup $\Gamma\le\operatorname{Isom}(\mathbb{R}^n)$ (i.e. every $n$-dimensional crystallographic group), the translation subgroup $T(\Gamma)\cong\mathbb{Z}^n$ is abelian and satisfies

$$
[\Gamma : T(\Gamma)] \;\le\; M(n),
$$

by Bieberbach's first theorem ($T(\Gamma)$ is finite-index) combined with Minkowski's theorem (1887) (the point group $P=\Gamma/T(\Gamma)\le GL(n,\mathbb{Z})$ has order dividing $M(n)$). This bound is sharp prime-by-prime and is the best known general bound depending only on $n$.

### PROOF COMPLETE
