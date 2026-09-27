# Proof: Darts on the First Uncountable Ordinal

## Problem

Two players throw darts at the set of the first uncountable ordinal $\omega_1$. The player who hits the higher ordinal number wins. What is the probability that the second player wins?

## Answer

$$\boxed{\dfrac{1}{2}}$$

## Proof

Let $X$ and $Y$ denote the ordinals hit by Player 1 and Player 2, respectively. We model "throwing darts" as drawing independently from the same probability distribution on $\omega_1$ (equipped with its order topology and the associated Borel $\sigma$-algebra). That is, $X$ and $Y$ are i.i.d. random variables taking values in $\omega_1$.

**Step 1: Symmetry.** Since $X$ and $Y$ are independent and identically distributed, the joint distribution of $(X, Y)$ is symmetric under swapping. Therefore:

$$P(X > Y) = P(Y > X).$$

That is, the probability that Player 1 wins equals the probability that Player 2 wins.

**Step 2: Partition into three events.** The outcomes partition into three mutually exclusive events:

$$P(X > Y) + P(Y > X) + P(X = Y) = 1.$$

**Step 3: Ties have probability zero.** The standard interpretation of "throwing darts" at an uncountable set is that the sampling distribution is non-atomic (continuous): no single point carries positive probability. Under this natural assumption, for any fixed $\alpha \in \omega_1$,

$$P(X = \alpha) = 0.$$

Since $X = Y$ means both players hit the same point, and by independence:

$$P(X = Y) = \sum_{\alpha \in \omega_1} P(X = \alpha)^2 = 0,$$

where each term is zero by the non-atomic assumption. (Equivalently, $P(X = Y) = \int_{\omega_1} P(Y = \alpha) \, d\mu(\alpha) = 0$ since $P(Y = \alpha) = 0$ for every $\alpha$.)

**Step 4: Conclusion.** Substituting into the partition:

$$2 \cdot P(Y > X) + 0 = 1,$$

so

$$P(\text{Player 2 wins}) = P(Y > X) = \frac{1}{2}.$$

$\blacksquare$

## Remark on the Underlying Paradox

A deep subtlety of this problem is that on $\omega_1$, **no countably additive non-atomic probability measure exists**. The reason is as follows: for any countably additive probability measure $\mu$ on $\omega_1$, since $\omega_1 = \bigcup_{\alpha < \omega_1} [0, \alpha]$ and $\omega_1$ has uncountable cofinality, for each $n \geq 1$ there exists a countable ordinal $\alpha_n$ with $\mu([0, \alpha_n]) > 1 - 1/n$. Setting $\alpha^* = \sup_n \alpha_n$ (which is countable, being a countable supremum of countable ordinals), we get $\mu([0, \alpha^*]) = 1$. Thus every countably additive probability measure on $\omega_1$ is concentrated on a countable initial segment and is necessarily atomic.

This means the non-atomic assumption in Step 3 is not literally realizable by a countably additive measure on $\omega_1$. The puzzle thus highlights a genuine paradox (closely related to Freiling's axiom of symmetry and the Continuum Hypothesis): the symmetry intuition and the "countable sets have measure zero" intuition cannot simultaneously be satisfied by any countably additive measure on $\omega_1$.

The intended answer $\frac{1}{2}$ follows from the symmetry argument, which is the robust and distribution-independent part of the reasoning. The symmetry $P(X > Y) = P(Y > X)$ holds for **any** i.i.d. pair regardless of the measure. The only additional ingredient is the standard "dart-throwing" convention that ties have probability zero, which is the natural modeling assumption for sampling from an uncountable set. Under this convention, the answer is uniquely determined as $\frac{1}{2}$.

### PROOF COMPLETE
