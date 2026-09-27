# Proof: Cardinality of $\{(\aleph_{\omega_1})^\kappa : 1 \leq \kappa < \aleph_{\omega_1}\}$

## Setup

Let $\lambda = \aleph_{\omega_1}$. Since $\omega_1$ is a regular ordinal and the aleph function is continuous, $\lambda$ is a singular cardinal with cofinality
$$\operatorname{cf}(\lambda) = \operatorname{cf}(\omega_1) = \omega_1.$$

The hypothesis states: for every $\alpha, \beta < \omega_1$, there exists $\gamma < \omega_1$ with $\aleph_\alpha^{\aleph_\beta} = \aleph_\gamma$. Equivalently,
$$\aleph_\alpha^{\aleph_\beta} < \aleph_{\omega_1} \quad \text{for all } \alpha, \beta < \omega_1. \tag{$\star$}$$

Every cardinal $\kappa$ with $1 \leq \kappa < \lambda$ is either finite, $\aleph_0$, or $\aleph_\beta$ for some $0 < \beta < \omega_1$. We split into two cases.

---

## Case 1: $1 \leq \kappa < \omega_1 = \operatorname{cf}(\lambda)$

Since $\kappa < \operatorname{cf}(\lambda)$, every function $f : \kappa \to \lambda$ has bounded range (the range has size $\leq \kappa < \operatorname{cf}(\lambda)$, hence is bounded below $\lambda$). Therefore
$$\lambda^\kappa = \sup_{\alpha < \omega_1} \aleph_\alpha^\kappa. \tag{1}$$

**Finite $\kappa \geq 1$:** $\aleph_\alpha^\kappa = \aleph_\alpha$, so $\lambda^\kappa = \sup_\alpha \aleph_\alpha = \aleph_{\omega_1} = \lambda$.

**$\kappa = \aleph_0$:** By $(\star)$, $\aleph_\alpha^{\aleph_0} = \aleph_{\gamma(\alpha)}$ for some $\gamma(\alpha) < \omega_1$. Since $\aleph_\alpha^{\aleph_0} \geq \aleph_\alpha$, we have $\gamma(\alpha) \geq \alpha$. By regularity of $\omega_1$, $\sup_{\alpha < \omega_1} \gamma(\alpha) = \omega_1$, hence
$$\lambda^{\aleph_0} = \sup_\alpha \aleph_{\gamma(\alpha)} = \aleph_{\omega_1} = \lambda.$$

**Conclusion of Case 1:** $(\aleph_{\omega_1})^\kappa = \aleph_{\omega_1}$ for all $1 \leq \kappa < \omega_1$.

---

## Case 2: $\kappa \geq \omega_1$, i.e., $\kappa = \aleph_\beta$ with $\beta \geq 1$

### Level-function decomposition

Write $\lambda = \sup_{\alpha < \omega_1} \aleph_\alpha$. Every function $g : \kappa \to \lambda$ determines a *level function* $f : \kappa \to \omega_1$ via $f(\xi) = \min\{\alpha : g(\xi) < \aleph_\alpha\}$. Grouping by level function:
$$\lambda^\kappa = \sum_{f \in {}^\kappa \omega_1} \prod_{\xi < \kappa} \aleph_{f(\xi)}. \tag{2}$$

Call $f$ **bounded** if $\operatorname{range}(f) \subseteq \delta$ for some $\delta < \omega_1$, and **unbounded** otherwise.

### Bounded $f$ contribute $\leq \lambda$

If $f$ is bounded by $\delta$, then $\prod_\xi \aleph_{f(\xi)} \leq \aleph_\delta^\kappa < \lambda$ by $(\star)$. The number of bounded $f$ is $\leq \omega_1 \cdot \sup_{\delta < \omega_1} \delta^\kappa$. For each $\delta < \omega_1$, $|\delta| \leq \aleph_0 < \aleph_1 \leq \kappa$, so $\delta^\kappa \leq \aleph_1^\kappa < \lambda$ by $(\star)$ (taking $\alpha = 1$). Thus the number of bounded $f$ is $\leq \omega_1 \cdot \lambda = \lambda$, and their total contribution is $\leq \lambda \cdot \lambda = \lambda$.

### Number of unbounded $f$ is $< \lambda$

The total number of $f \in {}^\kappa \omega_1$ is $\omega_1^\kappa \leq \aleph_1^\kappa < \lambda$ by $(\star)$ (with $\alpha = 1$). Hence the number of unbounded $f$ is also $< \lambda$.

### Key Claim

**For every unbounded $f : \kappa \to \omega_1$ (with $\kappa \geq \omega_1$),**
$$\prod_{\xi < \kappa} \aleph_{f(\xi)} = \prod_{\alpha < \omega_1} \aleph_\alpha. \tag{KC}$$

We prove (KC) by first handling $\kappa = \omega_1$, then extending to $\kappa > \omega_1$.

#### Sub-case $\kappa = \omega_1$: upper bound

We construct an injection $g : \omega_1 \to \omega_1$ with $g(\alpha) \geq f(\alpha)$ for all $\alpha$, by transfinite recursion. At stage $\alpha < \omega_1$, fewer than $\omega_1$ values have been used, while $\{v \geq f(\alpha)\}$ has cardinality $\omega_1$; so an unused value $\geq f(\alpha)$ exists. Then
$$\prod_\alpha \aleph_{f(\alpha)} \leq \prod_\alpha \aleph_{g(\alpha)} = \prod_{\gamma \in \operatorname{range}(g)} \aleph_\gamma \leq \prod_{\gamma < \omega_1} \aleph_\gamma.$$

#### Sub-case $\kappa = \omega_1$: lower bound

We construct an injection $h : \omega_1 \to \omega_1$ with $f(h(\gamma)) \geq \gamma$ for all $\gamma$. For each $\gamma$, the set $\{\alpha : f(\alpha) \geq \gamma\}$ has size $\omega_1$: indeed $\{\alpha : f(\alpha) < \gamma\}$ is bounded (as $f$ is unbounded and $\omega_1$ is regular, the sup of a bounded set of indices is $< \omega_1$). By transfinite recursion we pick $h(\gamma)$ distinct from all previously chosen values. Then
$$\prod_{\gamma < \omega_1} \aleph_\gamma \leq \prod_\gamma \aleph_{f(h(\gamma))} \leq \prod_\alpha \aleph_{f(\alpha)}.$$

This establishes (KC) for $\kappa = \omega_1$, and in particular:
$$\lambda^{\omega_1} = \prod_{\alpha < \omega_1} \aleph_\alpha. \tag{3}$$

#### Sub-case $\kappa = \aleph_\beta$, $\beta \geq 2$: upper bound

We cannot inject $\aleph_\beta$ into $\omega_1$ (domain larger than codomain), so we factor. Let $S_\alpha = f^{-1}(\alpha)$ for $\alpha < \omega_1$. Then
$$\prod_{\xi < \kappa} \aleph_{f(\xi)} = \prod_{\alpha < \omega_1} \aleph_\alpha^{|S_\alpha|}.$$
Each $|S_\alpha| \leq \kappa = \aleph_\beta$, so by $(\star)$, $\aleph_\alpha^{|S_\alpha|} \leq \aleph_\alpha^{\aleph_\beta} < \lambda$. Hence
$$\prod_\alpha \aleph_\alpha^{|S_\alpha|} \leq \prod_\alpha \lambda = \lambda^{\omega_1} = \prod_{\alpha < \omega_1} \aleph_\alpha$$
using (3). This gives the upper bound.

#### Sub-case $\kappa = \aleph_\beta$, $\beta \geq 2$: lower bound

Since $f$ is unbounded, $\operatorname{range}(f)$ is cofinal in $\omega_1$. For $\alpha \in \operatorname{range}(f)$, $|S_\alpha| \geq 1$, so $\aleph_\alpha^{|S_\alpha|} \geq \aleph_\alpha$. Thus
$$\prod_\alpha \aleph_\alpha^{|S_\alpha|} \geq \prod_{\alpha \in \operatorname{range}(f)} \aleph_\alpha.$$
By the **cofinal subproduct lemma** (below), since $\operatorname{range}(f)$ is cofinal in $\omega_1$,
$$\prod_{\alpha \in \operatorname{range}(f)} \aleph_\alpha = \prod_{\alpha < \omega_1} \aleph_\alpha.$$
This gives the lower bound, completing (KC).

### Cofinal subproduct lemma

**If $C \subseteq \omega_1$ is cofinal, then $\prod_{\alpha \in C} \aleph_\alpha = \prod_{\alpha < \omega_1} \aleph_\alpha$.**

*Proof.* The $\leq$ direction is immediate (subproduct). For $\geq$: since $C$ is cofinal and $\omega_1$ is regular, transfinite recursion yields an injection $g : \omega_1 \to C$ with $g(\alpha) \geq \alpha$ (at stage $\alpha$, the set $C \setminus \{\text{used}\}$ above $\alpha$ is nonempty). Then $\prod_\alpha \aleph_\alpha \leq \prod_\alpha \aleph_{g(\alpha)} \leq \prod_{\gamma \in C} \aleph_\gamma$. $\square$

### Assembling Case 2

From (2): the bounded part contributes $\leq \lambda$, and the unbounded part is a sum of $< \lambda$ many terms each equal (by (KC)) to $P := \prod_{\alpha < \omega_1} \aleph_\alpha$. Since $P \geq \lambda^{\omega_1} > \lambda$ (König, see below) and the number of unbounded $f$ is $< \lambda < P$,
$$\lambda^\kappa = \max\!\Big(\lambda,\; (\text{\# unbounded } f) \cdot P\Big) = \max(\lambda, P) = P.$$

**Conclusion of Case 2:** $(\aleph_{\omega_1})^{\aleph_\beta} = \prod_{\alpha < \omega_1} \aleph_\alpha$ for all $\beta \geq 1$.

---

## The two values are distinct

By König's theorem applied to the families $\kappa_\alpha = \aleph_\alpha$ and $\lambda_\alpha = \aleph_{\alpha+1}$ (where $\aleph_\alpha < \aleph_{\alpha+1}$ for all $\alpha$):
$$\sum_{\alpha < \omega_1} \aleph_\alpha < \prod_{\alpha < \omega_1} \aleph_{\alpha+1}.$$
The left side is $\aleph_{\omega_1} = \lambda$. The right side satisfies $\prod_\alpha \aleph_{\alpha+1} \leq \prod_\alpha \aleph_\alpha = P$ (relabeling). Hence $\lambda < P$, so the two values obtained in Cases 1 and 2 are distinct.

---

## Final answer

$$\big\{(\aleph_{\omega_1})^\kappa : 1 \leq \kappa < \aleph_{\omega_1}\big\} = \left\{\aleph_{\omega_1},\; \prod_{\alpha < \omega_1} \aleph_\alpha\right\},$$
a set with two distinct elements. Its cardinality is

$$\boxed{2}$$

### PROOF COMPLETE
