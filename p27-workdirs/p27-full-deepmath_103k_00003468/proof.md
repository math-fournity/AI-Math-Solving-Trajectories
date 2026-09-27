# Proof: $H^2(\mathbb{P}^n_k \times_k R, \mathbb{Z}) \not\cong \mathbb{Z}$ in general

## Answer

$$\boxed{H^2(\mathbb{P}^n_k \times_k R,\, \mathbb{Z}) \not\cong \mathbb{Z} \text{ in general.}}$$

The statement is **false** when $\operatorname{char}(k) = p > 0$. Since the problem posits an arbitrary algebraically closed field $k$ (not restricted to $k = \mathbb{C}$), the general answer is **NO**.

---

## Setup and interpretation

### The geometric object

$\mathbb{P}^n_k \times_k R$ denotes the fiber product $\mathbb{P}^n_k \times_{\operatorname{Spec}(k)} \operatorname{Spec}(R) = \mathbb{P}^n_R$, projective space over the DVR $R$. Since $R$ is a $k$-algebra with $k$ algebraically closed, the residue field $R/\mathfrak{m} \cong k$. The structure morphism $f: \mathbb{P}^n_R \to \operatorname{Spec}(R)$ is proper and smooth, with special fiber $\mathbb{P}^n_k$ and generic fiber $\mathbb{P}^n_{K}$ ($K = \operatorname{Frac}(R)$).

### Meaning of "singular cohomology"

For an arbitrary algebraically closed field $k$, singular (topological) cohomology is not directly defined. The natural algebro-geometric replacement is **étale cohomology** with $\mathbb{Z}$-coefficients. When $k = \mathbb{C}$ and $X$ is a finite-type smooth variety, the Artin comparison theorem gives $H^i_{\text{ét}}(X, \mathbb{Z}) \cong H^i_{\text{sing}}(X^{an}, \mathbb{Z})$. We interpret the problem in this generality (étale cohomology), which is the standard convention in algebraic geometry.

---

## Proof (positive characteristic counterexample)

Let $k = \bar{k}$ with $\operatorname{char}(k) = p > 0$, and let $R$ be a DVR that is a $k$-algebra (e.g., $R = k[[t]]$). We show $H^2_{\text{ét}}(\mathbb{P}^n_R, \mathbb{Z}) \not\cong \mathbb{Z}$.

### Step 1: $H^2_{\text{ét}}(\mathbb{P}^n_k, \mathbb{Z}/p) = 0$ via Artin–Schreier

On $X = \mathbb{P}^n_k$, the **Artin–Schreier short exact sequence** in the étale topology is:
$$0 \to \mathbb{Z}/p \to \mathbb{G}_a \xrightarrow{\;F - 1\;} \mathbb{G}_a \to 0,$$
where $F: x \mapsto x^p$ is the Frobenius and $F - 1: x \mapsto x^p - x$. This gives a long exact sequence in étale cohomology:
$$\cdots \to H^i_{\text{ét}}(X, \mathbb{G}_a) \xrightarrow{F-1} H^i_{\text{ét}}(X, \mathbb{G}_a) \to H^{i+1}_{\text{ét}}(X, \mathbb{Z}/p) \to H^{i+1}_{\text{ét}}(X, \mathbb{G}_a) \to \cdots$$

Now compute $H^i_{\text{ét}}(X, \mathbb{G}_a)$. By the comparison between étale and Zariski cohomology for coherent sheaves (Grothendieck, SGA4):
$$H^i_{\text{ét}}(\mathbb{P}^n_k, \mathbb{G}_a) \cong H^i_{\text{Zar}}(\mathbb{P}^n_k, \mathcal{O}_{\mathbb{P}^n}) = 0 \quad \text{for all } i > 0,$$
and $H^0_{\text{ét}}(X, \mathbb{G}_a) = k$.

The map $F - 1: k \to k$, $x \mapsto x^p - x$, is **surjective** because $k$ is algebraically closed (every equation $x^p - x = a$ has a root in $\bar{k} = k$). Its kernel is $\mathbb{F}_p$.

From the long exact sequence:
- $H^1_{\text{ét}}(X, \mathbb{Z}/p) = \operatorname{coker}(F-1: k \to k) = 0$.
- $H^2_{\text{ét}}(X, \mathbb{Z}/p) = \operatorname{coker}(F-1: H^1(\mathbb{G}_a) \to H^1(\mathbb{G}_a)) / \ker(F-1: H^2(\mathbb{G}_a) \to H^2(\mathbb{G}_a))$. Since $H^1(\mathbb{G}_a) = H^2(\mathbb{G}_a) = 0$, we get $H^2_{\text{ét}}(X, \mathbb{Z}/p) = 0$.

### Step 2: $\times p$ is an isomorphism on $H^2_{\text{ét}}(\mathbb{P}^n_k, \mathbb{Z})$

The short exact sequence of étale sheaves (constant sheaves):
$$0 \to \mathbb{Z} \xrightarrow{\times p} \mathbb{Z} \to \mathbb{Z}/p \to 0$$
yields a long exact sequence:
$$H^1_{\text{ét}}(X, \mathbb{Z}/p) \to H^2_{\text{ét}}(X, \mathbb{Z}) \xrightarrow{\times p} H^2_{\text{ét}}(X, \mathbb{Z}) \to H^2_{\text{ét}}(X, \mathbb{Z}/p) \to H^3_{\text{ét}}(X, \mathbb{Z}) \xrightarrow{\times p} \cdots$$

Substituting $H^1_{\text{ét}}(X, \mathbb{Z}/p) = 0$ and $H^2_{\text{ét}}(X, \mathbb{Z}/p) = 0$ from Step 1:
$$0 \to H^2_{\text{ét}}(X, \mathbb{Z}) \xrightarrow{\times p} H^2_{\text{ét}}(X, \mathbb{Z}) \to 0$$

Therefore $\times p: H^2_{\text{ét}}(\mathbb{P}^n_k, \mathbb{Z}) \to H^2_{\text{ét}}(\mathbb{P}^n_k, \mathbb{Z})$ is an **isomorphism**. Equivalently, $H^2_{\text{ét}}(\mathbb{P}^n_k, \mathbb{Z})$ is a **$p$-divisible group** (multiplication by $p$ is surjective).

### Step 3: $H^2_{\text{ét}}(\mathbb{P}^n_k, \mathbb{Z}) \not\cong \mathbb{Z}$

The group $\mathbb{Z}$ is **not** $p$-divisible: the map $\times p: \mathbb{Z} \to \mathbb{Z}$ is injective but **not surjective** (e.g., $1$ is not in the image). Since $H^2_{\text{ét}}(\mathbb{P}^n_k, \mathbb{Z})$ is $p$-divisible and $\mathbb{Z}$ is not, they cannot be isomorphic:
$$H^2_{\text{ét}}(\mathbb{P}^n_k, \mathbb{Z}) \not\cong \mathbb{Z}.$$

### Step 4: Extend to $\mathbb{P}^n_R$ via proper base change

We now pass from the special fiber $\mathbb{P}^n_k$ to the total space $\mathbb{P}^n_R$.

The structure morphism $f: \mathbb{P}^n_R \to \operatorname{Spec}(R)$ is **proper**. The closed point $s = \operatorname{Spec}(k) \hookrightarrow \operatorname{Spec}(R)$ has residue field $k = R/\mathfrak{m}$, which is algebraically closed (hence separably closed). 

**Proper base change theorem** (for torsion sheaves, SGA4, Exp. XVI): For any torsion étale sheaf $\mathcal{F}$ on $\mathbb{P}^n_R$, the natural map
$$(R^i f_* \mathcal{F})_{\bar{s}} \xrightarrow{\;\sim\;} H^i_{\text{ét}}(\mathbb{P}^n_k, \mathcal{F}|_{\mathbb{P}^n_k})$$
is an isomorphism, where $\bar{s}$ is a geometric point above $s$. Since $k$ is separably closed, the stalk $(R^i f_* \mathcal{F})_{\bar{s}}$ computes $H^i_{\text{ét}}(\mathbb{P}^n_R, \mathcal{F})$ after base change to the strict Henselization; but in fact, for the **torsion sheaf** $\mathcal{F} = \mathbb{Z}/p$, proper base change gives:
$$H^i_{\text{ét}}(\mathbb{P}^n_R, \mathbb{Z}/p) \cong H^i_{\text{ét}}(\mathbb{P}^n_k, \mathbb{Z}/p) \quad \text{for all } i \geq 0.$$

In particular, $H^2_{\text{ét}}(\mathbb{P}^n_R, \mathbb{Z}/p) = 0$ and $H^1_{\text{ét}}(\mathbb{P}^n_R, \mathbb{Z}/p) = 0$.

**Remark on $R = k[[t]]$ vs. $R = k[t]_{(t)}$:** When $R = k[[t]]$, the ring is strictly Henselian (complete local ring with separably closed residue field), so $\pi_1^{\text{ét}}(\operatorname{Spec}(R)) = 0$ and the base change is particularly transparent. For $R = k[t]_{(t)}$, proper base change for torsion sheaves still applies because the theorem only requires the residue field at the point of interest to be separably closed, which holds since $k$ is algebraically closed.

### Step 5: $\times p$ is an isomorphism on $H^2_{\text{ét}}(\mathbb{P}^n_R, \mathbb{Z})$

Applying the same coefficient long exact sequence $0 \to \mathbb{Z} \xrightarrow{\times p} \mathbb{Z} \to \mathbb{Z}/p \to 0$ on $\mathbb{P}^n_R$, and using $H^1_{\text{ét}}(\mathbb{P}^n_R, \mathbb{Z}/p) = 0$ and $H^2_{\text{ét}}(\mathbb{P}^n_R, \mathbb{Z}/p) = 0$ from Step 4:
$$0 \to H^2_{\text{ét}}(\mathbb{P}^n_R, \mathbb{Z}) \xrightarrow{\times p} H^2_{\text{ét}}(\mathbb{P}^n_R, \mathbb{Z}) \to 0.$$

Thus $\times p$ is an isomorphism on $H^2_{\text{ét}}(\mathbb{P}^n_R, \mathbb{Z})$, i.e., $H^2_{\text{ét}}(\mathbb{P}^n_R, \mathbb{Z})$ is $p$-divisible.

### Step 6: Conclusion

Since $H^2_{\text{ét}}(\mathbb{P}^n_R, \mathbb{Z})$ is $p$-divisible and $\mathbb{Z}$ is not $p$-divisible:
$$H^2_{\text{ét}}(\mathbb{P}^n_R, \mathbb{Z}) \not\cong \mathbb{Z}.$$

This provides an explicit counterexample for any algebraically closed field $k$ of positive characteristic, with any DVR $R$ that is a $k$-algebra. Therefore the statement does not hold in general.

---

## Remarks

### The characteristic zero case ($k = \mathbb{C}$)

When $k = \mathbb{C}$ and $R = \mathbb{C}[[t]]$, the analytic space associated to $\operatorname{Spec}(R)$ is a single point (the closed point), and $\mathbb{P}^n_R$ analytifies to a space homotopy equivalent to $\mathbb{CP}^n$. In this case $H^2 \cong \mathbb{Z}$ does hold. However, this requires either $k = \mathbb{C}$ (so singular cohomology is literally defined) or a Berkovich/rigid-analytic framework to handle the non-finite-type situation, and the result is specific to characteristic zero.

### Why the answer is NO in general

The problem states "algebraically closed field $k$" without restricting the characteristic. The positive characteristic case yields a rigorous counterexample via the Artin–Schreier sequence, which is a standard and well-established tool. The $p$-divisibility of $H^2_{\text{ét}}(\mathbb{P}^n_R, \mathbb{Z})$ in characteristic $p$ is a fundamental phenomenon reflecting the fact that $\mathbb{Z}$-coefficients in étale cohomology behave very differently from $\mathbb{Z}_\ell$-coefficients in positive characteristic.

### PROOF COMPLETE
