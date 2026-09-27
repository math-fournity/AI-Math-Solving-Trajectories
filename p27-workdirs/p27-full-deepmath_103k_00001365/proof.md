# Analytic Continuation Producing a Different Germ

## The Example

Let

$$f(z) = \log z$$

be the **principal branch** of the logarithm, defined on the neighborhood

$$U = \{z \in \mathbb{C} : \operatorname{Re}(z) > 0\}$$

of $z_0 = 1$. Concretely, $f(z) = \ln|z| + i\,\operatorname{Arg}(z)$ with $\operatorname{Arg}(z) \in (-\pi/2,\, \pi/2)$ on $U$, so that $f(1) = 0$.

Let the path be the unit circle traversed once counterclockwise:

$$\gamma : [0,1] \to \mathbb{C}\setminus\{0\}, \qquad \gamma(t) = e^{2\pi i t},$$

so that $\gamma(0) = \gamma(1) = 1$.

## Analytic Continuation Along $\gamma$

We analytically continue $f$ along $\gamma$ by covering the path with overlapping disks $D_k$ centered at $\gamma(t_k)$ (avoiding the origin) and defining the continuation on each disk by tracking the argument continuously.

On the first disk (near $t=0$), the continuation agrees with $f$ and uses $\arg \in (-\pi/2, \pi/2)$.

As $t$ increases from $0$ to $1$, the point $\gamma(t) = e^{2\pi i t}$ winds once around the origin, and the continuous argument increases from $0$ to $2\pi$. At each intermediate stage the continued function is a well-defined holomorphic branch of $\log$ on a disk not containing the origin.

When $t$ returns to $1$, the continued germ at $z_0 = 1$ is

$$f'(z) = \ln|z| + i\bigl(\operatorname{Arg}(z) + 2\pi\bigr) = f(z) + 2\pi i,$$

where $\operatorname{Arg}$ is again the principal argument in $(-\pi/2,\pi/2)$.

## Verification that $f \neq f'$

Evaluating both germs at $z_0 = 1$:

$$f(1) = 0, \qquad f'(1) = 0 + 2\pi i = 2\pi i.$$

Since $2\pi i \neq 0$, the two germs are **distinct**:

$$f \neq f'.$$

## Why This Is Nontrivial

- $f = \log z$ is single-valued and holomorphic on $U$, so it is a legitimate function defined on a neighborhood of $z_0 = 1$.
- The path $\gamma$ is a closed loop from $z_0$ to $z_0$.
- The analytic continuation exists at every point of $\gamma$ (the origin, the only branch point, is never on the path).
- The monodromy is **nontrivial**: continuing around the branch point at $0$ once shifts the logarithm by $2\pi i$, producing a genuinely different germ. Continuing $n$ times yields $f + 2\pi n i$, giving an infinite-order monodromy action.

## Conclusion

$$\boxed{f(z) = \log z \text{ (principal branch) near } z_0 = 1, \quad \gamma(t)=e^{2\pi i t}; \quad \text{continuation gives } f' = f + 2\pi i \neq f.}$$
