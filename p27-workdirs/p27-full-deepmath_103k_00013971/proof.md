# Proof: Option 3 is the correct assertion

## Answer: $\boxed{3}$

## Setup

Let $g \in W^{1,1}(0,1) \cap C^1(0,1) \cap C[0,1]$. Since $g \in W^{1,1}(0,1)$ (weak derivative $g' \in L^1(0,1)$) and $g \in C[0,1]$, the function $g$ is absolutely continuous (AC) on $[0,1]$. The $C^1(0,1)$ condition ensures the classical derivative coincides with the weak derivative on $(0,1)$, but does not alter any of the conclusions below.

## Proof that Option 3 is TRUE

**Option 3.** For every $\varepsilon > 0$ there exists $\delta > 0$ such that: for every countable family of non-overlapping intervals $([a_k, b_k])_{k=1}^{+\infty}$ with $\sum_{k=1}^{+\infty}|b_k - a_k| \leq \delta$, we have $\sum_{k=1}^{+\infty}|g(b_k) - g(a_k)| \leq \varepsilon$.

**Proof.** The standard definition of absolute continuity states: $g$ is AC on $[0,1]$ if for every $\varepsilon > 0$ there exists $\delta_0 > 0$ such that for every **finite** family of non-overlapping intervals $([a_k, b_k])_{k=1}^N$ with $\sum_{k=1}^N |b_k - a_k| < \delta_0$, we have $\sum_{k=1}^N |g(b_k) - g(a_k)| < \varepsilon$.

We show the countable version follows. Given $\varepsilon > 0$, pick $\delta_0 > 0$ from the (finite) AC definition applied to $\varepsilon$. Set $\delta = \delta_0 / 2$.

Let $([a_k, b_k])_{k=1}^{+\infty}$ be a countable family of non-overlapping intervals with $\sum_{k=1}^{+\infty} |b_k - a_k| \leq \delta = \delta_0/2 < \delta_0$.

For any finite $N \geq 1$, the finite subfamily $([a_k, b_k])_{k=1}^N$ has total length $\sum_{k=1}^N |b_k - a_k| \leq \sum_{k=1}^{+\infty} |b_k - a_k| \leq \delta < \delta_0$, so by the AC definition:
$$\sum_{k=1}^N |g(b_k) - g(a_k)| < \varepsilon.$$

Since this holds for every $N$, taking $N \to +\infty$:
$$\sum_{k=1}^{+\infty} |g(b_k) - g(a_k)| = \lim_{N \to +\infty} \sum_{k=1}^N |g(b_k) - g(a_k)| \leq \varepsilon. \qquad \blacksquare$$

## Proof that Option 4 is FALSE (key contrast)

**Option 4** replaces "non-overlapping" with "possibly overlapping." This is strictly stronger and fails.

**Counterexample.** Let $g(x) = 2\sqrt{x}$ on $[0,1]$. Then:
- $g \in C[0,1]$: $g(0) = 0$, continuous on $[0,1]$. ✓
- $g \in C^1(0,1)$: $g'(x) = 1/\sqrt{x}$, continuous on $(0,1)$. ✓
- $g \in W^{1,1}(0,1)$: $\int_0^1 |g'(x)|\,dx = \int_0^1 x^{-1/2}\,dx = 2 < +\infty$. ✓

Fix any $\delta > 0$ and any $\varepsilon > 0$. Take $N$ identical (hence overlapping) intervals $[a_k, b_k] = [0, \delta/N]$ for $k = 1, \ldots, N$. Then:
$$\sum_{k=1}^N |b_k - a_k| = N \cdot \frac{\delta}{N} = \delta \leq \delta.$$
But:
$$\sum_{k=1}^N |g(b_k) - g(a_k)| = N \cdot \left|2\sqrt{\delta/N} - 0\right| = N \cdot 2\sqrt{\frac{\delta}{N}} = 2\sqrt{N\delta} \xrightarrow{N \to +\infty} +\infty.$$

Choosing $N$ large enough so that $2\sqrt{N\delta} > \varepsilon$, we violate the condition. Since this works for every $\delta > 0$ and every $\varepsilon > 0$, Option 4 is **FALSE**. $\blacksquare$

## Summary of all options

| Option | Truth | Reason |
|--------|-------|--------|
| 1 | TRUE | Lusin N property: $\lambda(E)=0 \Rightarrow \lambda(g(E))=0$ for AC $g$ |
| 2 | TRUE | Equivalent to Option 5 |
| 3 | **TRUE** | Countable version of AC definition (finite $\Rightarrow$ countable via partial sums) |
| 4 | FALSE | Counterexample $g(x)=2\sqrt{x}$ with overlapping intervals |
| 5 | TRUE | $\lambda(g(E)) \leq \int_E |g'|\,dt$ (coarea/Banach indicatrix) + absolute continuity of $L^1$ integral |
| 6 | TRUE | Option 1 + continuity of measure from below |
| 7 | FALSE | Counterexample $g(x)=x^2$: $E_1=[0,1/2]$, $E_2=[1/2,1]$ give $\lambda(g(E_1))=1/4 \neq 3/4 = \lambda(g(E_2))$ |

The pair (Option 3, Option 4) is the only pair where one assertion is true and the other is false. Option 3 is the countable non-overlapping version of the AC definition (true), while Option 4 allows overlapping intervals (false). This distinction is the key test of the problem.

### PROOF COMPLETE
