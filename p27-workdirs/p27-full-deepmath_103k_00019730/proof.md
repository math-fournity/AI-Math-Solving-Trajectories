# Proof that $d = 1$

## Problem

Determine the integer $d$ such that the homotopy equivalence $\mu: S^m \wedge S^n \rightarrow S^{m+n}$ satisfies
$$\mu^*(\sigma^{m+n}1) = d \cdot \sigma^m1 \wedge \sigma^n1,$$
where $\mu^*: H^{m+n}(S^{m+n}) \rightarrow H^{m+n}(S^m \wedge S^n)$ is the induced homomorphism, and $\sigma^n 1$ is the image of the unit $1 \in H^0(S^0)$ under the $n$-fold suspension isomorphism $\sigma^n: H^0(S^0) \rightarrow H^n(S^n)$.

## Proof

### Step 1. The suspension isomorphism as left suspension

The (reduced) suspension isomorphism
$$\sigma: \widetilde{H}^k(X) \xrightarrow{\;\cong\;} \widetilde{H}^{k+1}(\Sigma X), \qquad \Sigma X = S^1 \wedge X,$$
is defined by **left suspension**: identifying $\Sigma X = S^1 \wedge X$ and setting
$$\sigma(\alpha) = \beta_1 \wedge \alpha, \qquad \beta_1 := \sigma^1(1) \in \widetilde{H}^1(S^1),$$
where the external smash product $\beta_1 \wedge \alpha \in \widetilde{H}^{k+1}(S^1 \wedge X)$ is induced by the cup product of the two pullback classes under the quotient $(S^1 \times X)/(S^1 \vee X) = S^1 \wedge X$. This is the standard convention (Hatcher, Spanier): the connecting homomorphism of the pair $(\Sigma X, CX)$ carries no explicit sign, so $\sigma(\alpha) = \beta_1 \wedge \alpha$ with coefficient $+1$.

### Step 2. Iterating: $\sigma^n(1) = \beta_1^{\wedge n}$

Iterating the left-suspension definition $n$ times, and using the associativity of the smash product $\Sigma(\Sigma X) = S^1 \wedge (S^1 \wedge X) = (S^1 \wedge S^1) \wedge X$, we obtain
$$\sigma^n(1) = \underbrace{\beta_1 \wedge \beta_1 \wedge \cdots \wedge \beta_1}_{n \text{ factors}} = \beta_1^{\wedge n} \in \widetilde{H}^n\big((S^1)^{\wedge n}\big) = \widetilde{H}^n(S^n).$$
Here $(S^1)^{\wedge n} \cong S^n$ is the standard $n$-sphere obtained as the $n$-fold smash of $S^1$, and $\sigma^n(1)$ is precisely the canonical generator of $\widetilde{H}^n(S^n)$ under this identification.

### Step 3. The class $\sigma^m(1) \wedge \sigma^n(1)$

Using the same notation,
$$\sigma^m(1) \wedge \sigma^n(1) = \beta_1^{\wedge m} \wedge \beta_1^{\wedge n} = \beta_1^{\wedge(m+n)} \in \widetilde{H}^{m+n}\big((S^1)^{\wedge m} \wedge (S^1)^{\wedge n}\big) = \widetilde{H}^{m+n}(S^m \wedge S^n).$$
The key point: the external smash product introduces **no sign** here, because the two factors live on different smash factors $(S^1)^{\wedge m}$ and $(S^1)^{\wedge n}$, and the cup product $p_1^*(\alpha) \smile p_2^*(\beta)$ of classes pulled back from distinct factors carries no Koszul sign.

### Step 4. The map $\mu$ is an associativity regrouping (no swap, no sign)

The standard homotopy equivalence
$$\mu: S^m \wedge S^n = (S^1)^{\wedge m} \wedge (S^1)^{\wedge n} \xrightarrow{\;\cong\;} (S^1)^{\wedge(m+n)} = S^{m+n}$$
is the **associativity regrouping** of the $m+n$ copies of $S^1$: it sends $(x_1 \wedge \cdots \wedge x_m) \wedge (y_1 \wedge \cdots \wedge y_n) \mapsto x_1 \wedge \cdots \wedge x_m \wedge y_1 \wedge \cdots \wedge y_n$. Crucially, $\mu$ **does not permute the order** of the smash factors — it only re-associates the parentheses. Therefore no Koszul sign $(-1)^{mn}$ is introduced. (The sign $(-1)^{mn}$ would arise only from the **swap map** $\tau: S^m \wedge S^n \to S^n \wedge S^m$ that exchanges the two blocks, which is a different map from $\mu$.)

### Step 5. Pull back $\sigma^{m+n}(1)$ along $\mu$

Under the identification $(S^1)^{\wedge(m+n)} = S^{m+n}$, the generator is
$$\sigma^{m+n}(1) = \beta_1^{\wedge(m+n)} \in \widetilde{H}^{m+n}(S^{m+n}).$$
Since $\mu$ is the pure associativity regrouping (no reordering), pulling back along $\mu$ simply re-associates the smash factors of the class:
$$\mu^*\!\left(\beta_1^{\wedge(m+n)}\right) = \beta_1^{\wedge m} \wedge \beta_1^{\wedge n} = \sigma^m(1) \wedge \sigma^n(1).$$
That is,
$$\mu^*(\sigma^{m+n}(1)) = \sigma^m(1) \wedge \sigma^n(1).$$

### Step 6. Verification with $m = n = 1$ (rules out $d = (-1)^{mn}$)

For $m = n = 1$: $S^1 \wedge S^1 = \Sigma S^1 \cong S^2$, and $\mu$ is the suspension homeomorphism. Then
$$\sigma^1(1) \wedge \sigma^1(1) = \beta_1 \wedge \beta_1 = \sigma(\sigma^1(1)) = \sigma^2(1),$$
so $\mu^*(\sigma^2(1)) = \sigma^1(1) \wedge \sigma^1(1)$, giving $d = 1$. This rules out the alternative $d = (-1)^{mn} = -1$.

### Conclusion

Comparing $\mu^*(\sigma^{m+n}(1)) = \sigma^m(1) \wedge \sigma^n(1)$ with the defining equation $\mu^*(\sigma^{m+n}(1)) = d \cdot \sigma^m(1) \wedge \sigma^n(1)$, we read off

$$\boxed{d = 1}.$$

### PROOF COMPLETE
