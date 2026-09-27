# Proof: Non-constant Hodge numbers in a family over the unit disk

**Problem.** Does there exist a family of compact complex manifolds over a unit disk such that the Hodge numbers are not constant in the family?

**Answer.** $\boxed{\text{Yes}}$.

---

## 1. Strategy and the role of the Kähler hypothesis

For a smooth proper holomorphic submersion $\pi\colon \mathcal{X}\to \Delta$ (where $\Delta$ is the unit disk) whose fibers are **Kähler**, a theorem of Kodaira (together with the degeneration at $E_1$ of the Frölicher spectral sequence for Kähler manifolds and Grauert's direct image theorem) implies that the Hodge numbers $h^{p,q}(X_t)=\dim H^q(X_t,\Omega^p_{X_t})$ are **constant** in $t$. Hence any counterexample must be sought among **non-Kähler** compact complex manifolds, in dimension $\geq 3$ (for compact complex surfaces the Frölicher spectral sequence always degenerates at $E_1$, so surfaces cannot provide a counterexample).

We use the **Iwasawa manifold** as the central fiber and exhibit an explicit integrable deformation along which $h^{1,0}$ drops from $3$ to $2$.

---

## 2. The Iwasawa manifold

Let $G$ be the complex Heisenberg group of upper-triangular unipotent $3\times 3$ complex matrices, and let $\Gamma\subset G$ be the cocompact lattice of matrices with entries in $\mathbb{Z}[i]$. The **Iwasawa manifold** is the compact quotient
$$
M \;=\; G/\Gamma .
$$
It is a compact complex $3$-fold. It is **complex-parallelizable**: the holomorphic cotangent bundle $\Omega^1_M$ is trivial, trivialized by left-invariant $(1,0)$-forms $\{\omega_1,\omega_2,\omega_3\}$ satisfying the structure equations
$$
d\omega_1 = 0,\qquad d\omega_2 = 0,\qquad d\omega_3 = \omega_1\wedge\omega_2 .
$$
$M$ is **not Kähler** (it is not a torus, and a compact Kähler parallelizable manifold is a torus).

### 2.1 Hodge and Betti numbers of $M$

Since $\Omega^p_M$ is trivial for every $p$,
$$
h^{p,0}(M)=\dim H^0(M,\Omega^p_M)=\binom{3}{p},
$$
so in particular
$$
h^{1,0}(M)=3,\qquad h^{2,0}(M)=3,\qquad h^{3,0}(M)=1.
$$

The Dolbeault cohomology $H^{0,q}(M)$ of a nilmanifold with nilpotent complex structure can be computed using left-invariant forms (Sakane; Cordero–Fernández–Gray–Ugarte). One obtains
$$
h^{0,1}(M)=2.
$$

The first Betti number is computed via Nomizu's theorem (the real de Rham cohomology of a nilmanifold agrees with the Lie algebra cohomology of the underlying real Lie algebra). The commutator subalgebra of the real Lie algebra of $G$ is $2$-dimensional (spanned by the real and imaginary parts of the center), so the abelianization has dimension $6-2=4$, giving
$$
b_1(M)=4.
$$

### 2.2 The Frölicher spectral sequence does not degenerate at $E_1$

The Frölicher spectral sequence has $E_1^{p,q}=H^q(M,\Omega^p_M)\Rightarrow H^{p+q}_{\mathrm{dR}}(M,\mathbb{C})$. If it degenerated at $E_1$, we would have $b_k=\sum_{p+q=k}h^{p,q}$. For $k=1$:
$$
h^{1,0}(M)+h^{0,1}(M)=3+2=5\;>\;4=b_1(M).
$$
Hence the Frölicher spectral sequence of $M$ **does not degenerate at $E_1$**. This is the mechanism that allows Hodge numbers to jump in deformations.

---

## 3. An integrable deformation

We deform the complex structure of $M$ by mixing $\omega_1$ with its conjugate. For $t\in\Delta$ (the unit disk, so $|t|<1$), define a new frame of $(1,0)$-forms by
$$
\omega_1^{t}=\omega_1+t\,\bar\omega_1,\qquad \omega_2^{t}=\omega_2,\qquad \omega_3^{t}=\omega_3 .
$$

### 3.1 Integrability (Newlander–Nirenberg)

By the Newlander–Nirenberg theorem (in the form: an almost-complex structure defined by a coframe is integrable iff $d\omega^j$ has no $(0,2)$-component for every $j$), we verify integrability.

Clearly $d\omega_1^{t}=0$ and $d\omega_2^{t}=0$. The only nontrivial equation is $d\omega_3^{t}=\omega_1\wedge\omega_2$. We express the right-hand side in the new frame. From $\omega_1^{t}=\omega_1+t\bar\omega_1$ and $\bar\omega_1^{t}=\bar\omega_1+\bar t\,\omega_1$, we solve (valid for $|t|\neq 1$, in particular on $\Delta$):
$$
\omega_1=\frac{\omega_1^{t}-t\,\bar\omega_1^{t}}{1-|t|^2}.
$$
Therefore
$$
d\omega_3^{t}=\omega_1\wedge\omega_2=\frac{1}{1-|t|^2}\bigl(\omega_1^{t}\wedge\omega_2^{t}-t\,\bar\omega_1^{t}\wedge\omega_2^{t}\bigr).
$$
The first term $\omega_1^{t}\wedge\omega_2^{t}$ is of type $(2,0)$ and the second term $\bar\omega_1^{t}\wedge\omega_2^{t}$ is of type $(1,1)$ in the new complex structure. There is **no $(0,2)$-component**. Hence the deformed almost-complex structure is integrable for every $t\in\Delta$.

This gives a smooth family of compact complex manifolds $\pi\colon\mathcal{X}\to\Delta$ with central fiber $M_0=M$.

---

## 4. Computation of $h^{1,0}(M_t)$

A general $(1,0)$-form on $M_t$ is
$$
\alpha=a\,\omega_1^{t}+b\,\omega_2^{t}+c\,\omega_3^{t},\qquad a,b,c\in\mathbb{C}.
$$
Using the structure equation,
$$
d\alpha=c\,d\omega_3^{t}=\frac{c}{1-|t|^2}\bigl(\omega_1^{t}\wedge\omega_2^{t}-t\,\bar\omega_1^{t}\wedge\omega_2^{t}\bigr).
$$
The $(0,2)$-component of $d\alpha$ is zero. The $(1,1)$-component is
$$
\frac{-c\,t}{1-|t|^2}\,\bar\omega_1^{t}\wedge\omega_2^{t}.
$$
The form $\alpha$ is **holomorphic** (i.e. $\bar\partial_t\alpha=0$, equivalently $d\alpha$ is of pure type $(2,0)$) iff the $(1,1)$-component vanishes. For $t\neq 0$ this forces
$$
c=0.
$$
Hence, for $t\neq 0$, the holomorphic $1$-forms are exactly $a\,\omega_1^{t}+b\,\omega_2^{t}$, and
$$
h^{1,0}(M_t)=2\qquad (t\neq 0).
$$
At the central fiber, $h^{1,0}(M_0)=3$ as computed in §2.1.

---

## 5. Conclusion

We have constructed a smooth family $\pi\colon\mathcal{X}\to\Delta$ of compact complex manifolds over the unit disk such that
$$
h^{1,0}(M_0)=3\;\neq\;2=h^{1,0}(M_t)\quad\text{for all }t\in\Delta\setminus\{0\}.
$$
Therefore the Hodge numbers are **not constant** in this family.

$$
\boxed{\text{Yes}}
$$

### PROOF COMPLETE
