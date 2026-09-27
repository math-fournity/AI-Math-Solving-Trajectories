# Proof: Weak smoothness on decomposable tensors implies strong smoothness

**Answer: YES.** If $\lambda \mapsto T_\lambda[\varphi \otimes \psi]$ is smooth for every pair $\varphi, \psi \in \mathscr{D}(X)$, then $\lambda \mapsto T_\lambda[\Phi]$ is smooth for every $\Phi \in \mathscr{D}(X \times X)$.

$$\boxed{\text{Yes}}$$

---

## Setup and notation

Let $X$ be a compact manifold. We write $E := \mathscr{D}(X)$, a nuclear LF-space (hence barrelled). Its strong dual $E'_\beta$ is $\mathscr{D}'(X)$ with the strong topology. The space $\mathscr{D}(X \times X)$ is canonically isomorphic to the completed injective tensor product $E \hat{\otimes_\varepsilon} E$ (and, by nuclearity, also to $E \hat{\otimes_\pi} E$). We identify $\mathscr{D}'(X \times X) \cong L(E, E'_\beta)$, the space of continuous linear maps $E \to E'_\beta$, via the Schwartz kernel theorem.

For $\varphi \in E$ and $\lambda \in \mathbb{R}$, define
$$S_{\lambda, \varphi} \in E'_\beta, \qquad S_{\lambda,\varphi}[\psi] := T_\lambda[\varphi \otimes \psi], \quad \psi \in E.$$
The hypothesis says: for every $\varphi \in E$, the map $\lambda \mapsto S_{\lambda,\varphi} \in E'_\beta$ is **weakly smooth** (i.e. $\lambda \mapsto S_{\lambda,\varphi}[\psi]$ is $C^\infty$ for every $\psi \in E$), and for every $\psi \in E$, the map $\lambda \mapsto S_{\lambda,\cdot}[\psi]$ is weakly smooth in the $\varphi$-slot.

---

## Lemma (Weakly smooth curves in $\mathscr{D}'$ are strongly smooth)

**Statement.** Let $\Omega$ be an open set in $\mathbb{R}^d$ and let $\lambda \mapsto U_\lambda \in \mathscr{D}'(\Omega)$ be a curve defined on an open interval $I \subset \mathbb{R}$. Suppose $\lambda \mapsto U_\lambda[f]$ is $C^\infty$ for every $f \in \mathscr{D}(\Omega)$ (weak smoothness). Then:

(a) For every $\lambda_0 \in I$ and every $n \geq 1$, the $n$-th derivative
$$U^{(n)}(\lambda_0) := \frac{d^n}{d\lambda^n}\bigg|_{\lambda=\lambda_0} U_\lambda$$
exists in $\mathscr{D}'(\Omega)$ equipped with the **strong** topology $\beta(\mathscr{D}', \mathscr{D})$.

(b) The map $\lambda \mapsto U_\lambda$ is $C^\infty$ as a map $I \to \mathscr{D}'(\Omega)_\beta$.

**Proof of the Lemma.** It suffices to prove (a) for $n=1$; the general case follows by induction (the derivative curve $\lambda \mapsto U'_\lambda$ is again weakly smooth, since $\lambda \mapsto U_\lambda[f]$ is $C^\infty$ implies $\lambda \mapsto U'_\lambda[f]$ is $C^\infty$).

Fix $\lambda_0 \in I$ and let $h \to 0$ with $h \neq 0$. Define the **difference quotient**
$$D_h := \frac{U_{\lambda_0+h} - U_{\lambda_0}}{h} \in \mathscr{D}'(\Omega).$$

*Step 1: Pointwise boundedness.* For each $f \in \mathscr{D}(\Omega)$, the scalar function $\lambda \mapsto U_\lambda[f]$ is $C^1$ (in fact $C^\infty$), so
$$D_h[f] = \frac{U_{\lambda_0+h}[f] - U_{\lambda_0}[f]}{h} \xrightarrow{h \to 0} U'_{\lambda_0}[f] := \frac{d}{d\lambda}\bigg|_{\lambda_0} U_\lambda[f].$$
In particular $\{D_h[f]\}_h$ is convergent, hence bounded, for each $f$.

*Step 2: Equicontinuity via Banach–Steinhaus.* The space $\mathscr{D}(\Omega)$ is an LF-space, hence **barrelled**. The family $\{D_h\}_{0<|h|<\varepsilon} \subset \mathscr{D}'(\Omega) = L(\mathscr{D}(\Omega), \mathbb{R})$ is pointwise bounded by Step 1. By the **Banach–Steinhaus theorem** (uniform boundedness principle for barrelled spaces), the family $\{D_h\}$ is **equicontinuous**: there exists a continuous seminorm $p$ on $\mathscr{D}(\Omega)$ and a constant $C > 0$ such that
$$|D_h[f]| \leq C \cdot p(f), \qquad \forall\, f \in \mathscr{D}(\Omega),\ \forall\, 0 < |h| < \varepsilon. \tag{$\star$}$$

*Step 3: The limit is a distribution.* Define $D[f] := U'_{\lambda_0}[f] = \lim_{h\to 0} D_h[f]$. Passing to the limit in $(\star)$:
$$|D[f]| \leq C \cdot p(f), \qquad \forall\, f \in \mathscr{D}(\Omega).$$
So $D$ is dominated by a continuous seminorm, hence $D \in \mathscr{D}'(\Omega)$ (it is continuous). Moreover $D_h \to D$ in the **strong** topology: for any bounded set $B \subset \mathscr{D}(\Omega)$,
$$\sup_{f \in B} |D_h[f] - D[f]| \xrightarrow{h\to 0} 0$$
because equicontinuity of $\{D_h\}$ (and $D$, which satisfies the same bound) gives a uniform bound $C \cdot \sup_{f\in B} p(f) < \infty$ on $B$, and pointwise convergence + equicontinuity on the bounded set $B$ yields uniform convergence (a standard consequence of the Banach–Steinhaus equicontinuity, or equivalently an $\varepsilon/3$-argument using the equicontinuity to reduce to a finite $\varepsilon$-net on $B$).

This proves (a) for $n=1$ and (b) for $C^1$. Induction on $n$ gives the full result. $\square$

---

## Main proof

We prove by induction on $n \geq 0$ that:

> **$(P_n)$**: For every $\lambda_0 \in \mathbb{R}$, the $n$-th derivative $\frac{d^n}{d\lambda^n}\big|_{\lambda_0} T_\lambda =: T^{(n)}_{\lambda_0}$ exists in $\mathscr{D}'(X \times X)$ with the strong topology, and the map $\lambda \mapsto T^{(n)}_\lambda$ is continuous (in fact, we will show it is weakly smooth, enabling the induction to continue).

**Base case $n = 0$.** $T^{(0)}_\lambda = T_\lambda$ is given, and $\lambda \mapsto T_\lambda[\varphi \otimes \psi]$ is $C^\infty$ by hypothesis. This is the induction hypothesis we need: $T^{(0)}$ is weakly smooth on decomposable tensors.

**Induction step.** Assume $(P_n)$ holds and, moreover, that $\lambda \mapsto T^{(n)}_\lambda[\varphi \otimes \psi]$ is $C^\infty$ for all $\varphi, \psi \in E$ (this is the "weak smoothness on decomposable tensors" property, which we verify propagates through the induction). We prove $(P_{n+1})$.

Fix $\lambda_0 \in \mathbb{R}$. We must show that $\frac{d}{d\lambda}\big|_{\lambda_0} T^{(n)}_\lambda$ exists in $\mathscr{D}'(X \times X)_\beta$ and equals a distribution that we identify.

### Step 1: Reduce to a curve in $L(E, E'_\beta)$

By the Schwartz kernel theorem, $T^{(n)}_\lambda \in \mathscr{D}'(X \times X) \cong L(E, E'_\beta)$. Define
$$A^{(n)}_\lambda : E \to E'_\beta, \qquad A^{(n)}_\lambda(\varphi) := S^{(n)}_{\lambda, \varphi}, \quad \text{where } S^{(n)}_{\lambda,\varphi}[\psi] := T^{(n)}_\lambda[\varphi \otimes \psi].$$
Each $A^{(n)}_\lambda$ is a continuous linear map $E \to E'_\beta$ (this is part of $(P_n)$: $T^{(n)}_{\lambda_0} \in \mathscr{D}'(X\times X)$ corresponds to a continuous map $E \to E'_\beta$).

For fixed $\varphi \in E$, the curve $\lambda \mapsto A^{(n)}_\lambda(\varphi) = S^{(n)}_{\lambda,\varphi} \in E'_\beta$ is **weakly smooth**: $\lambda \mapsto S^{(n)}_{\lambda,\varphi}[\psi] = T^{(n)}_\lambda[\varphi \otimes \psi]$ is $C^\infty$ by the induction hypothesis.

### Step 2: Apply the Lemma to each fixed $\varphi$

By the Lemma, for each fixed $\varphi \in E$, the derivative
$$\frac{d}{d\lambda}\bigg|_{\lambda_0} A^{(n)}_\lambda(\varphi) = \frac{d}{d\lambda}\bigg|_{\lambda_0} S^{(n)}_{\lambda,\varphi} \in E'_\beta$$
exists in the strong topology. Denote this limit by $B(\varphi) \in E'_\beta$. Concretely,
$$B(\varphi)[\psi] = \frac{d}{d\lambda}\bigg|_{\lambda_0} T^{(n)}_\lambda[\varphi \otimes \psi], \qquad \psi \in E. \tag{1}$$

### Step 3: The difference quotients form an equicontinuous family in $L(E, E'_\beta)$

Define, for $h \neq 0$ small,
$$\Delta_h := \frac{A^{(n)}_{\lambda_0+h} - A^{(n)}_{\lambda_0}}{h} \in L(E, E'_\beta).$$

*Each $\Delta_h$ is continuous*: it is a linear combination of continuous maps $A^{(n)}_{\lambda_0+h}, A^{(n)}_{\lambda_0} \in L(E, E'_\beta)$.

*Pointwise boundedness*: For each $\varphi \in E$, the curve $\lambda \mapsto A^{(n)}_\lambda(\varphi) \in E'_\beta$ is weakly smooth, hence strongly $C^1$ by the Lemma. So $\{\Delta_h(\varphi)\}_h$ converges in $E'_\beta$ (to $B(\varphi)$), hence is bounded in $E'_\beta$.

Now we use the **Banach–Steinhaus theorem for $L(E, E'_\beta)$**. The domain $E = \mathscr{D}(X)$ is barrelled (LF-space). The codomain $E'_\beta$ is locally convex. A pointwise-bounded family in $L(E, E'_\beta)$ is equicontinuous when the domain is barrelled. Therefore:

> **$\{\Delta_h\}_{0<|h|<\varepsilon}$ is an equicontinuous family in $L(E, E'_\beta)$.**

Concretely: there exists a continuous seminorm $p$ on $E$, a bounded set $Q \subset E$ (equivalently, a continuous seminorm $q$ on $E$ defining a neighborhood $V_Q = \{u \in E'_\beta : \sup_{\psi \in Q} |u[\psi]| \leq 1\}$), and a constant $C > 0$, such that
$$\sup_{\psi \in Q} |\Delta_h(\varphi)[\psi]| \leq C \cdot p(\varphi), \qquad \forall\, \varphi \in E,\ \forall\, 0 < |h| < \varepsilon. \tag{2}$$

### Step 4: The pointwise limit $B : E \to E'_\beta$ is continuous

We have $\Delta_h(\varphi) \to B(\varphi)$ in $E'_\beta$ for each $\varphi$ (Step 2). Passing to the limit in (2):
$$\sup_{\psi \in Q} |B(\varphi)[\psi]| \leq C \cdot p(\varphi), \qquad \forall\, \varphi \in E. \tag{3}$$
This shows $B : E \to E'_\beta$ is continuous (it maps a neighborhood of $0$ in $E$ into a neighborhood of $0$ in $E'_\beta$). So $B \in L(E, E'_\beta)$.

Moreover, $\Delta_h \to B$ in the strong operator topology, and even **uniformly on bounded sets**: for any bounded $B_0 \subset E$, equicontinuity (2) gives a uniform bound $\sup_{\varphi \in B_0} C \cdot p(\varphi) < \infty$ on $\{\Delta_h(\varphi)\}$ and $B(\varphi)$, and pointwise convergence + equicontinuity on $B_0$ gives
$$\sup_{\varphi \in B_0} \sup_{\psi \in Q} |\Delta_h(\varphi)[\psi] - B(\varphi)[\psi]| \xrightarrow{h \to 0} 0. \tag{4}$$

### Step 5: Apply the Schwartz kernel theorem to $B$

Since $B \in L(E, E'_\beta)$, the Schwartz kernel theorem gives a unique distribution $S \in \mathscr{D}'(X \times X)$ such that
$$S[\varphi \otimes \psi] = B(\varphi)[\psi] = \frac{d}{d\lambda}\bigg|_{\lambda_0} T^{(n)}_\lambda[\varphi \otimes \psi], \qquad \forall\, \varphi, \psi \in E. \tag{5}$$

This $S$ is the candidate for $T^{(n+1)}_{\lambda_0}$.

### Step 6: Identify the derivative on all of $\mathscr{D}(X \times X)$ via nuclear decomposition

We must show that for **every** $\Phi \in \mathscr{D}(X \times X)$ (not just decomposable tensors),
$$\frac{d}{d\lambda}\bigg|_{\lambda_0} T^{(n)}_\lambda[\Phi] = S[\Phi]. \tag{6}$$

**Nuclear decomposition.** Since $E = \mathscr{D}(X)$ is nuclear and $\mathscr{D}(X \times X) \cong E \hat{\otimes}_\pi E$, every $\Phi \in \mathscr{D}(X \times X)$ admits a **nuclear decomposition** (see Treves, *Topological Vector Spaces, Distributions and Kernels*, §51):
$$\Phi = \sum_{l=1}^{\infty} \alpha_l\, \varphi_l \otimes \psi_l, \tag{7}$$
where $\alpha_l \in \mathbb{R}$ with $\sum_{l=1}^\infty |\alpha_l| < \infty$, and $\varphi_l \to 0$, $\psi_l \to 0$ in $E = \mathscr{D}(X)$. (More precisely: there exist continuous seminorms $p, q$ on $E$ such that $\sum_l |\alpha_l|\, p(\varphi_l)\, q(\psi_l) < \infty$, which is the form we will use.)

**Uniform bound from equicontinuity.** From (2) and (3), there is a continuous seminorm $p$ on $E$, a bounded set $Q \subset E$ defining a seminorm $q(u) := \sup_{\psi \in Q}|u[\psi]|$ on $E'_\beta$, and a constant $C > 0$ such that, for all $\varphi \in E$ and all $0 < |h| < \varepsilon$ (and also for the limit $B$):
$$\sup_{\psi \in Q} \left|\frac{T^{(n)}_{\lambda_0+h}[\varphi \otimes \psi] - T^{(n)}_{\lambda_0}[\varphi \otimes \psi]}{h}\right| \leq C\, p(\varphi), \tag{8}$$
$$\sup_{\psi \in Q} |B(\varphi)[\psi]| \leq C\, p(\varphi). \tag{9}$$

We need a bound that controls the pairing against arbitrary $\psi_l$, not just $\psi \in Q$. This is achieved as follows. The equicontinuity (2) says: for every neighborhood $W$ of $0$ in $E'_\beta$, there is a neighborhood $U$ of $0$ in $E$ such that $\Delta_h(U) \subset W$ for all $h$. Taking $W$ to be the polars of larger and larger bounded sets, we obtain: for **every** bounded set $Q' \subset E$, there is a continuous seminorm $p_{Q'}$ on $E$ and a constant $C_{Q'}$ such that
$$\sup_{\psi \in Q'} |\Delta_h(\varphi)[\psi]| \leq C_{Q'}\, p_{Q'}(\varphi), \qquad \forall\, \varphi \in E,\ 0<|h|<\varepsilon, \tag{10}$$
and the same for $B$. In particular, choosing $Q' = \{\psi_l : l \geq 1\} \cup \{0\}$ — which is **bounded** in $E$ because $\psi_l \to 0$ — we get a single seminorm $p'$ and constant $C'$ with
$$|\Delta_h(\varphi_l)[\psi_l]| \leq C'\, p'(\varphi_l), \qquad |B(\varphi_l)[\psi_l]| \leq C'\, p'(\varphi_l), \qquad \forall\, l,\ \forall\, 0<|h|<\varepsilon. \tag{11}$$

Since $\varphi_l \to 0$ in $E$, the sequence $\{p'(\varphi_l)\}$ is bounded, say $p'(\varphi_l) \leq M$ for all $l$. Combining with (11):
$$|\Delta_h(\varphi_l)[\psi_l]| \leq C' M, \qquad |B(\varphi_l)[\psi_l]| \leq C' M. \tag{12}$$

**Dominated convergence for the series.** Now compute:
$$\frac{T^{(n)}_{\lambda_0+h}[\Phi] - T^{(n)}_{\lambda_0}[\Phi]}{h} = \sum_{l=1}^\infty \alpha_l\, \Delta_h(\varphi_l)[\psi_l], \tag{13}$$
$$S[\Phi] = \sum_{l=1}^\infty \alpha_l\, B(\varphi_l)[\psi_l]. \tag{14}$$

Both series converge absolutely: by (12),
$$\sum_l |\alpha_l|\, |\Delta_h(\varphi_l)[\psi_l]| \leq C' M \sum_l |\alpha_l| < \infty, \qquad \sum_l |\alpha_l|\, |B(\varphi_l)[\psi_l]| \leq C'M \sum_l |\alpha_l| < \infty. \tag{15}$$

The **dominating series** $C'M \sum_l |\alpha_l|$ is $h$-independent and finite. For each fixed $l$, $\Delta_h(\varphi_l)[\psi_l] \to B(\varphi_l)[\psi_l]$ as $h \to 0$ (by Step 2, since $\psi_l \in E$). By the **dominated convergence theorem for series** (Weierstrass M-test + termwise convergence with a uniform summable dominating sequence):
$$\sum_{l=1}^\infty \alpha_l\, \Delta_h(\varphi_l)[\psi_l] \xrightarrow{h \to 0} \sum_{l=1}^\infty \alpha_l\, B(\varphi_l)[\psi_l] = S[\Phi]. \tag{16}$$

This proves (6): $\frac{d}{d\lambda}\big|_{\lambda_0} T^{(n)}_\lambda[\Phi] = S[\Phi]$ for every $\Phi \in \mathscr{D}(X \times X)$.

### Step 7: The derivative is a distribution; the induction continues

Equation (6) shows that the scalar function $\lambda \mapsto T^{(n)}_\lambda[\Phi]$ is differentiable at $\lambda_0$ with derivative $S[\Phi]$, for every $\Phi$. Since $S \in \mathscr{D}'(X \times X)$, we have $T^{(n+1)}_{\lambda_0} = S$, and the derivative exists in the strong topology (the convergence $\Delta_h \to B$ is uniform on bounded sets by (4), which translates to strong convergence of the difference quotients of $T^{(n)}_\lambda$ to $S$ in $\mathscr{D}'(X \times X)_\beta$).

**Propagation of the induction hypothesis.** We must verify that $\lambda \mapsto T^{(n+1)}_\lambda[\varphi \otimes \psi]$ is $C^\infty$ for all $\varphi, \psi$. But
$$T^{(n+1)}_\lambda[\varphi \otimes \psi] = \frac{d}{d\lambda} T^{(n)}_\lambda[\varphi \otimes \psi],$$
and by the induction hypothesis $\lambda \mapsto T^{(n)}_\lambda[\varphi \otimes \psi]$ is $C^\infty$, so its derivative is $C^\infty$ as well. This is the weak-smoothness property needed for the next step.

**Continuity.** Since $\lambda \mapsto T^{(n+1)}_\lambda$ is differentiable (in the strong topology) at every $\lambda_0$, it is continuous.

### Conclusion of the induction

By induction, $(P_n)$ holds for all $n \geq 0$. In particular, for every $\Phi \in \mathscr{D}(X \times X)$ and every $n \geq 0$, the $n$-th derivative $\frac{d^n}{d\lambda^n} T_\lambda[\Phi]\big|_{\lambda_0}$ exists and equals $T^{(n)}_{\lambda_0}[\Phi]$, and $\lambda \mapsto T^{(n)}_\lambda[\Phi]$ is continuous. Therefore $\lambda \mapsto T_\lambda[\Phi]$ is $C^\infty$ for every $\Phi \in \mathscr{D}(X \times X)$.

---

## Summary of the argument

1. **Lemma**: A weakly smooth curve in $\mathscr{D}'(\Omega)$ (scalar-valued pairing smooth for each test function) is strongly smooth, with derivatives existing as distributions. Proof: Banach–Steinhaus on the barrelled space $\mathscr{D}(\Omega)$ gives equicontinuity of difference quotients; the pointwise limit is then a distribution, and convergence is strong.

2. **Reduction to operator-valued curves**: Via the kernel theorem, $T_\lambda \in \mathscr{D}'(X\times X)$ corresponds to $A_\lambda \in L(\mathscr{D}(X), \mathscr{D}'(X)_\beta)$. The hypothesis gives weak smoothness of $\lambda \mapsto A_\lambda(\varphi)$ for each $\varphi$.

3. **Equicontinuity of difference quotients in $L(E, E'_\beta)$**: Banach–Steinhaus (domain $E$ barrelled) upgrades pointwise boundedness to equicontinuity of the family $\{\Delta_h\}$.

4. **Limit operator is continuous**: The pointwise limit $B = \lim \Delta_h$ satisfies the same equicontinuity bound, hence $B \in L(E, E'_\beta)$. Kernel theorem gives $S \in \mathscr{D}'(X\times X)$.

5. **Lifting from decomposable tensors to all test functions**: Nuclear decomposition $\Phi = \sum \alpha_l\, \varphi_l \otimes \psi_l$ with $\sum|\alpha_l|<\infty$ and $\varphi_l, \psi_l \to 0$. Equicontinuity gives a uniform (in $h$) bound on each term, dominated convergence for series exchanges limit and summation, yielding $\frac{d}{d\lambda}T_\lambda[\Phi]\big|_{\lambda_0} = S[\Phi]$ for all $\Phi$.

6. **Induction**: The derivative family satisfies the same hypothesis, so all orders follow.

The key ingredients are: **barrelledness** of $\mathscr{D}(X)$ (for Banach–Steinhaus), **nuclearity** of $\mathscr{D}(X)$ (for the nuclear decomposition in Step 6), and the **Schwartz kernel theorem** (to pass between distributions on $X\times X$ and continuous linear maps $E \to E'_\beta$).

$$\boxed{\text{Yes}}$$

### PROOF COMPLETE
