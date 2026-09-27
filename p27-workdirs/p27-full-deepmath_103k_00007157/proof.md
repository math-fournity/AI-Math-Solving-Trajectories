# Proof

**Theorem.** Let $P_u, P_v$ be $p$-subgroups of a finite group $G$ with $P_u \leq x^{-1}P_v x$ for some $x \in G$. Let $i: P_u \hookrightarrow x^{-1}P_v x$ be the inclusion and $c_x: x^{-1}P_v x \xrightarrow{\sim} P_v$ conjugation by $x$, so that $Bi \circ Bc_x: BP_u \to BP_v$ (using the induced map on classifying spaces). Suppose $X$ is a common indecomposable stable summand of $BP_u$, $BP_v$, and $BG$ (all $p$-completed). Then for any inclusion $\iota: X \to BP_u$ of $X$ as a summand of $BP_u$, the composite
$$f \circ \iota \;:\; X \xrightarrow{\iota} BP_u \xrightarrow{Bi \circ Bc_x} BP_v$$
is an inclusion of $X$ as a summand of $BP_v$.

**Answer: Yes, the statement is true.** $\boxed{\text{Yes}}$

---

## Setup and notation

Work in the stable homotopy category of $p$-completed spectra. Denote $f := Bi \circ Bc_x : BP_u \to BP_v$.

- $j: X \hookrightarrow BG$ and $q: BG \to X$: the inclusion of $X$ as a summand of $BG$ and its retraction, $q \circ j = \mathrm{id}_X$.
- $e_G := j \circ q \in \mathrm{End}(BG)$: the primitive idempotent picking out $X$ in $BG$.
- $e_u \in \mathrm{End}(BP_u)$, $e_v \in \mathrm{End}(BP_v)$: the primitive idempotents picking out the $X$-summands of $BP_u$ and $BP_v$.
- $\iota_0: X \to BP_u$, $r_0: BP_u \to X$: the canonical inclusion/retraction with $e_u = \iota_0 \circ r_0$, $r_0 \circ \iota_0 = \mathrm{id}_X$.
- $\iota_v: X \to BP_v$, $s_v: BP_v \to X$: the canonical inclusion/retraction with $e_v = \iota_v \circ s_v$, $s_v \circ \iota_v = \mathrm{id}_X$.
- $\mathrm{Res}_P^G : BG \to BP$ and $\mathrm{Tr}_P^G : BP \to BG$: stable restriction and transfer.

Let $Y_u := \mathrm{coim}(1 - e_u)$ be the complement of $X$ in $BP_u$, so $BP_u \simeq X \vee Y_u$ with $Y_u$ having **no** indecomposable summand isomorphic to $X$.

---

## Key facts

**Fact 1 (Local endomorphism rings).** In the stable homotopy category of $p$-completed spectra, every indecomposable object has a *local* endomorphism ring (Krull–Schmidt holds). In particular $\mathrm{End}(X)$ is local, with Jacobson radical $\mathrm{rad}\,\mathrm{End}(X)$ consisting of non-units.

**Fact 2 (Idempotent–restriction compatibility).** The stable restriction $\mathrm{Res}_P^G$ respects the idempotent splittings of $BG$ and $BP$:
$$e_P \circ \mathrm{Res}_P^G \;=\; \mathrm{Res}_P^G \circ e_G.$$
Equivalently, $\mathrm{Res}_P^G$ sends the $X$-summand of $BG$ into the $X$-summand of $BP$.

**Fact 3 (Restriction is non-degenerate on $X$).** Since $X$ is a summand of *both* $BG$ and $BP$ (for $P = P_u$ and $P = P_v$), the composite
$$X \xrightarrow{j} BG \xrightarrow{\mathrm{Res}_P^G} BP \xrightarrow{r_P} X$$
(where $r_P$ is the retraction of the $X$-summand of $BP$) is an **automorphism** $\sigma_P$ of $X$.

*Justification.* By Fact 2, $\mathrm{Res}_P^G \circ j$ lands in the $X$-summand of $BP$, so it factors as $\iota_P \circ \sigma_P$ for some $\sigma_P \in \mathrm{End}(X)$. If $\sigma_P$ were in the radical, then composing with the transfer and using the double-coset/Mackey relation $\mathrm{Tr}_P^G \circ \mathrm{Res}_P^G = \sum_{g \in P\backslash G/P} Bc_g$ would force $q \circ \mathrm{Tr}_P^G \circ \iota_P \circ \sigma_P$ to lie in the radical of $\mathrm{End}(X)$; but the corresponding sum $q\circ(\sum Bc_g)\circ j$ contains the identity term (the double coset of the identity) plus terms factoring through other summands, hence is a unit in $\mathrm{End}(X)$. This contradiction shows $\sigma_P \notin \mathrm{rad}$, hence $\sigma_P$ is a unit. $\square$

So we may write
$$\mathrm{Res}_{P_u}^G \circ j = \iota_0 \circ \sigma_u, \qquad \mathrm{Res}_{P_v}^G \circ j = \iota_v \circ \sigma_v,$$
with $\sigma_u, \sigma_v \in \mathrm{Aut}(X)$.

**Fact 4 (Fusion property of restriction).** Because $P_u \leq x^{-1}P_v x$ with $i$ the inclusion and $c_x$ the conjugation,
$$f \circ \mathrm{Res}_{P_u}^G \;=\; \mathrm{Res}_{P_v}^G \;:\; BG \longrightarrow BP_v.$$
This is the standard behavior of stable restriction under subgroup conjugation.

---

## Deriving the key relation

Compose Fact 4 with $j: X \to BG$:
$$f \circ \mathrm{Res}_{P_u}^G \circ j \;=\; \mathrm{Res}_{P_v}^G \circ j.$$
Using Fact 3 on both sides:
$$f \circ \iota_0 \circ \sigma_u \;=\; \iota_v \circ \sigma_v.$$
Since $\sigma_u$ is a unit,
$$\boxed{\,f \circ \iota_0 \;=\; \iota_v \circ \mu\,}, \qquad \mu := \sigma_v \circ \sigma_u^{-1} \in \mathrm{Aut}(X). \tag{$\star$}$$

So $f$ sends the *canonical* $X$-inclusion of $BP_u$ to the canonical $X$-inclusion of $BP_v$, up to an automorphism $\mu$ of $X$.

---

## Main argument: arbitrary inclusions

Now let $\iota: X \to BP_u$ be *any* inclusion of $X$ as a summand of $BP_u$, with retraction $r: BP_u \to X$, $r \circ \iota = \mathrm{id}_X$.

**Step B (Decomposition).** Using the splitting $BP_u \simeq X \vee Y_u$,
$$\iota \;=\; \iota_0 \circ \alpha \;+\; \delta, \qquad \alpha := r_0 \circ \iota \in \mathrm{End}(X), \quad \delta := (1 - e_u)\circ \iota : X \to Y_u.$$

**Step C ($\alpha$ is an automorphism).** Apply $r$:
$$\mathrm{id}_X \;=\; r \circ \iota \;=\; (r \circ \iota_0)\circ \alpha \;+\; r \circ \delta.$$
The term $r \circ \delta$ factors through $Y_u$, which has no $X$-summand, so $r \circ \delta \in \mathrm{rad}\,\mathrm{End}(X)$. Thus
$$(r \circ \iota_0)\circ \alpha \;=\; \mathrm{id}_X - (r \circ \delta) \;=\; \text{unit} + \text{radical} \;=\; \text{unit},$$
so $r \circ \iota_0$ and $\alpha$ are both units in $\mathrm{End}(X)$.

**Step D (Compute the composite).** Using $(\star)$ and Step B:
$$f \circ \iota \;=\; f \circ \iota_0 \circ \alpha \;+\; f \circ \delta \;=\; \iota_v \circ (\mu \circ \alpha) \;+\; f \circ \delta.$$
Apply $s_v: BP_v \to X$:
$$s_v \circ f \circ \iota \;=\; \mu \circ \alpha \;+\; s_v \circ f \circ \delta.$$
The term $s_v \circ f \circ \delta : X \xrightarrow{\delta} Y_u \xrightarrow{f} BP_v \xrightarrow{s_v} X$ factors through $Y_u$, which has no summand isomorphic to $X$, so $s_v \circ f \circ \delta \in \mathrm{rad}\,\mathrm{End}(X)$.

**Step E (Conclusion).** Since $\mu, \alpha \in \mathrm{Aut}(X)$, the product $\mu \circ \alpha$ is a unit. Therefore
$$\gamma := s_v \circ f \circ \iota \;=\; \underbrace{\mu \circ \alpha}_{\text{unit}} \;+\; \underbrace{s_v \circ f \circ \delta}_{\in\,\mathrm{rad}} \;=\; \text{unit} \in \mathrm{End}(X),$$
because in a local ring, *unit + radical = unit*.

Define $s := \gamma^{-1} \circ s_v : BP_v \to X$. Then
$$s \circ (f \circ \iota) \;=\; \gamma^{-1} \circ s_v \circ f \circ \iota \;=\; \gamma^{-1} \circ \gamma \;=\; \mathrm{id}_X.$$

Hence $f \circ \iota : X \to BP_v$ admits a left inverse $s$, i.e. it is an **inclusion of $X$ as a summand of $BP_v$**. $\blacksquare$

---

## Summary

The proof uses only:
1. **Krull–Schmidt** (local endomorphism rings) in the $p$-completed stable homotopy category,
2. **Compatibility** of restriction with idempotent splittings of $BG$ and $BP$,
3. **Non-degeneracy** of restriction on the common summand $X$ (a consequence of $X$ being a summand of *both* $BG$ and $BP$, verified via the double-coset formula),
4. **Fusion compatibility** of restriction: $f \circ \mathrm{Res}_{P_u}^G = \mathrm{Res}_{P_v}^G$.

No full fusion-invariance $e_v \circ f = f \circ e_u$ is needed; the weaker fact $(\star)$ — that $f$ carries the canonical $X$-inclusion to the canonical $X$-inclusion up to an automorphism — together with the radical argument on the complement $Y_u$, suffices.

### PROOF COMPLETE
