# Proof

## Answer

$$\boxed{\text{No, in general such } b \in B \text{ need not exist.}}$$

The statement becomes true if the morphism is assumed faithfully flat (surjective), but under the hypotheses as stated — only flat, with reduced fibers — a counterexample exists.

---

## Counterexample

Let
$$B = k[x], \qquad A = k[x, x^{-1}], \qquad \phi: B \hookrightarrow A \text{ the natural inclusion},$$
and take $a = x^{-1} \in A$.

The induced morphism $f = \mathrm{Spec}\,A \to \mathrm{Spec}\,B$ is the open immersion
$$\mathbb{A}^1 \setminus \{0\} \hookrightarrow \mathbb{A}^1,$$
i.e. the inclusion of the standard open $D(x) \subset \mathbb{A}^1_k$.

### Verification of the hypotheses

**(1) Flatness.** Open immersions are flat: $A = B[x^{-1}] = S^{-1}B$ with $S = \{1, x, x^2, \dots\}$, so $A$ is a localization of $B$, hence flat over $B$.

**(2) Reduced scheme-theoretic fibers.** The fibers over $\mathfrak{p} \in \mathrm{Spec}\,B$ are $\mathrm{Spec}(A \otimes_B \kappa(\mathfrak{p}))$. We check each type of point of $\mathrm{Spec}\,B = \mathbb{A}^1_k$:

- **Closed point $(x - c)$, $c \in k^\times$:**
$$A \otimes_B \kappa((x-c)) = k[x,x^{-1}]/(x-c) \cong k,$$
a single reduced point. ✓

- **Closed point $(x)$ (the origin):**
$$A \otimes_B \kappa((x)) = k[x,x^{-1}] \otimes_{k[x]} k[x]_{(x)}/(x).$$
Since $x$ is invertible in $A$ but $x = 0$ in $\kappa((x))$, we have $1 = x \cdot x^{-1} \mapsto 0 \cdot x^{-1} = 0$, so the tensor product is the zero ring. The fiber is **empty**, hence vacuously reduced. ✓

- **Generic point $(0)$:**
$$A \otimes_B \kappa((0)) = k[x, x^{-1}] \otimes_{k[x]} k(x) = k(x),$$
a field, hence reduced. ✓

All fibers are reduced.

**(3) $a = x^{-1}$ is constant on each fiber.** "Constant on a fiber" means $a \otimes 1$ lies in the image of $\kappa(\mathfrak{p}) \to A \otimes_B \kappa(\mathfrak{p})$.

- Over $(x-c)$, $c \neq 0$: $x^{-1} \mapsto c^{-1} \in k = \kappa((x-c))$. ✓
- Over $(x)$: the fiber is empty (zero ring), so the condition is vacuous. ✓
- Over $(0)$: $x^{-1} \in k(x) = \kappa((0))$, and the map $\kappa((0)) \to A \otimes_B \kappa((0)) = k(x)$ is the identity. ✓

So $a = x^{-1}$ is constant on every fiber.

### The element $a$ does not come from $B$

$$x^{-1} \notin k[x] = B.$$

Therefore no $b \in B$ satisfies $\phi(b) = a$. $\square$

---

## Why the counterexample works (mechanism)

The key is that $f$ is **not surjective**: the fiber over the origin $(x)$ is empty. The element $x^{-1}$ is "invisible" at the missing fiber — there is no constraint forcing it to extend to a regular function on all of $\mathbb{A}^1$. The flatness and reduced-fiber conditions are satisfied, but they only constrain behavior on the fibers that actually exist, and the missing fiber leaves a gap through which $a$ can escape the image of $B$.

Algebraically: setting $M = A/\phi(B) = k[x,x^{-1}]/k[x]$, one checks that $M \otimes_B \kappa(\mathfrak{p}) = 0$ for **every** $\mathfrak{p} \in \mathrm{Spec}\,B$ (over $(x)$ the localization kills $M$ since $x$ acts invertibly on $M$ but $x \in \mathfrak{p}$; over every other point $x$ is already invertible in $\kappa(\mathfrak{p})$ so $M \otimes \kappa(\mathfrak{p}) = 0$). Yet $M \neq 0$. The class of $x^{-1}$ in $M$ is a nonzero element that vanishes in every fiber — a phenomenon impossible for finitely generated modules (by Nakayama) but possible here because $M$ is not finitely generated over $B$.

---

## Remark: the faithfully flat case

If one strengthens the hypothesis to **faithfully flat** (i.e. the morphism is surjective), then the answer becomes **Yes**. A sketch:

Suppose $B$ is a domain (as is the case for varieties) and $B \to A$ is faithfully flat with reduced fibers. If $a \in A$ is constant on each fiber, then in particular it is constant on the generic fiber, so $a \otimes 1$ lies in $\kappa((0)) = K := \mathrm{Frac}(B)$ inside $A \otimes_B K$. Since $A$ is flat (hence torsion-free) over $B$, the map $A \to A \otimes_B K$ is injective, so $a = \phi(p/q)$ in $A \otimes_B K$ for some $p/q \in K$, i.e. $\phi(q)\,a = \phi(p)$ in $A$. This means $a \in A \cap \mathrm{Frac}(B)$ (intersection taken in $\mathrm{Frac}(A)$).

It remains to show $A \cap \mathrm{Frac}(B) = B$. Faithful flatness makes $B \hookrightarrow A$ injective. For $a \in A \cap \mathrm{Frac}(B)$, write $a = p/q$ with $p, q \in B$, $q \neq 0$. Then $q\bar{a} = 0$ in $A/B$. From the exact sequence $0 \to B \to A \to A/B \to 0$ and the flatness of $A$, tensoring with $B/(q)$ (using the free resolution $0 \to B \xrightarrow{\cdot q} B \to B/(q) \to 0$) gives
$$\mathrm{Tor}_1^B(A/B,\, B/(q)) \cong \ker\!\big(q : A/B \to A/B\big).$$
Faithful flatness of $A$ over $B$ implies $B/(q) \hookrightarrow A/(q)A$ is injective, and the long exact Tor sequence yields $\mathrm{Tor}_1^B(A/B, B/(q)) = 0$. Hence multiplication by $q$ on $A/B$ is injective, so $q\bar{a} = 0$ forces $\bar{a} = 0$, i.e. $a \in B$.

Thus, under the stronger faithfully flat hypothesis, every fiber-constant element does descend to $B$. The counterexample above shows this strengthening is essential: without surjectivity the conclusion fails.

---

### PROOF COMPLETE
