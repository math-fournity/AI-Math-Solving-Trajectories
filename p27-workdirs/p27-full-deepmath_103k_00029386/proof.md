# Proof: Initial morphism in Top over Prost implies initial topology

## Problem

In the category **Top** of topological spaces and the category **Prost** of preordered sets with monotone maps, consider a continuous morphism $f: X \to Y$. If $f$ is an initial morphism in **Top** over **Prost**, does it imply that $X$ has the initial topology defined by $f$?

## Answer

$$\boxed{\text{Yes}}$$

## Setup

Let $U: \mathbf{Top} \to \mathbf{Prost}$ be the **specialization preorder functor**:
- $U(X) = (|X|, \leq_X)$ where $x \leq_X y \iff x \in \overline{\{y\}}$ (equivalently, every open set containing $x$ also contains $y$).
- $U(f) = f$ as a monotone map (continuity of $f$ ensures $x \leq_X y \Rightarrow f(x) \leq_Y f(y)$).

Let $f: (X, \tau) \to (Y, \sigma)$ be continuous. The **initial topology** on $X$ defined by $f$ is:
$$\tau_{\mathrm{init}} = \{\, f^{-1}(V) : V \in \sigma \,\}$$
(This is already a topology since $\sigma$ is closed under arbitrary unions and finite intersections, and these operations commute with $f^{-1}$.)

Since $f$ is continuous, $\tau_{\mathrm{init}} \subseteq \tau$.

**Definition (initial morphism).** $f$ is initial in $\mathbf{Top}$ over $\mathbf{Prost}$ iff for every topological space $Z$ and every monotone map $g: U(Z) \to U(X)$ (i.e., $z_1 \leq_Z z_2 \Rightarrow g(z_1) \leq_\tau g(z_2)$), if $f \circ g: Z \to Y$ is continuous, then $g: Z \to X$ is continuous.

**Key reformulation.** Note that $f \circ g: Z \to Y$ continuous means $g^{-1}(f^{-1}(V))$ is open in $Z$ for all $V \in \sigma$, i.e., $g$ is continuous w.r.t. $\tau_{\mathrm{init}}$. So the initiality condition becomes:

> For every $Z$ and every $g: U(Z) \to U(X)$ monotone w.r.t. $(\leq_Z, \leq_\tau)$: if $g$ is continuous w.r.t. $\tau_{\mathrm{init}}$, then $g$ is continuous w.r.t. $\tau$.

## Key facts

**Fact 1 (Specialization preorder of $\tau_{\mathrm{init}}$).** The specialization preorder of $(X, \tau_{\mathrm{init}})$ is:
$$x \leq_{\mathrm{init}} y \iff f(x) \leq_\sigma f(y).$$

*Proof.* $x \leq_{\mathrm{init}} y$ iff every $f^{-1}(V) \in \tau_{\mathrm{init}}$ containing $x$ also contains $y$, iff every $V \in \sigma$ containing $f(x)$ also contains $f(y)$, iff $f(x) \leq_\sigma f(y)$. $\square$

**Fact 2 (Monotonicity gap).** Since $\tau_{\mathrm{init}} \subseteq \tau$, we have $\leq_\tau \subseteq \leq_{\mathrm{init}}$ (finer topology $\Rightarrow$ smaller specialization preorder).

**Fact 3 ($\tau_{\mathrm{init}}$-continuity via Sierpinski).** For the Sierpinski space $S = \{0,1\}$ with topology $\{\emptyset, \{1\}, \{0,1\}\}$ (specialization preorder $0 \leq 1$), a map $g: S \to X$ is continuous w.r.t. $\tau_{\mathrm{init}}$ iff $g(0) \leq_{\mathrm{init}} g(1)$, and continuous w.r.t. $\tau$ iff $g(0) \leq_\tau g(1)$. Since $\leq_\tau \subseteq \leq_{\mathrm{init}}$, the initiality condition for $Z = S$ becomes: if $g(0) \leq_\tau g(1)$ then $g(0) \leq_\tau g(1)$ — trivially true. So Sierpinski space alone cannot distinguish $\tau$ from $\tau_{\mathrm{init}}$; we need a non-Alexandrov test space.

## Proof (by contrapositive)

We prove: if $\tau \neq \tau_{\mathrm{init}}$, then $f$ is **not** initial.

Assume $\tau \supsetneq \tau_{\mathrm{init}}$. We consider two cases.

### Case 1: $\leq_\tau = \leq_{\mathrm{init}}$

Take $Z = (X, \tau_{\mathrm{init}})$ and $g = \mathrm{id}_X$.

- **Monotonicity:** $g$ is monotone w.r.t. $(\leq_{\mathrm{init}}, \leq_\tau)$ iff $\leq_{\mathrm{init}} \subseteq \leq_\tau$. Since $\leq_\tau = \leq_{\mathrm{init}}$, this holds. $\checkmark$
- **$\tau_{\mathrm{init}}$-continuity:** $\mathrm{id}: (X, \tau_{\mathrm{init}}) \to (X, \tau_{\mathrm{init}})$ is continuous. $\checkmark$
- **$\tau$-continuity:** $\mathrm{id}: (X, \tau_{\mathrm{init}}) \to (X, \tau)$ is continuous iff $\tau \subseteq \tau_{\mathrm{init}}$. But $\tau \supsetneq \tau_{\mathrm{init}}$, so this **fails**. $\boldsymbol{\times}$

This violates the initiality condition, so $f$ is not initial.

### Case 2: $\leq_\tau \subsetneq \leq_{\mathrm{init}}$

There exist $x_0, y_0 \in X$ with $x_0 \leq_{\mathrm{init}} y_0$ but $x_0 \not\leq_\tau y_0$.

Since $x_0 \not\leq_\tau y_0$, there exists $U \in \tau$ with $x_0 \in U$ and $y_0 \notin U$.

**Claim:** $U \notin \tau_{\mathrm{init}}$.

*Proof of claim.* If $U = f^{-1}(V)$ for some $V \in \sigma$, then $x_0 \in U$ means $f(x_0) \in V$. Since $x_0 \leq_{\mathrm{init}} y_0$ means $f(x_0) \leq_\sigma f(y_0)$, every open $V \in \sigma$ containing $f(x_0)$ also contains $f(y_0)$, so $y_0 \in f^{-1}(V) = U$. Contradiction with $y_0 \notin U$. $\square$

Now take $Z = (\mathbb{N}, \text{cofinite topology})$. The cofinite topology on $\mathbb{N}$ is $T_1$, so $\leq_Z$ is the discrete (equality) relation. Define $g: \mathbb{N} \to X$ by:
$$g(0) = x_0, \qquad g(n) = y_0 \text{ for } n \geq 1.$$

- **Monotonicity:** Since $\leq_Z$ is equality, $g$ is trivially monotone w.r.t. $(\leq_Z, \leq_\tau)$. $\checkmark$

- **$\tau_{\mathrm{init}}$-continuity:** For any $V \in \sigma$, we check $g^{-1}(f^{-1}(V))$:
  - If $f(x_0) \in V$: since $f(x_0) \leq_\sigma f(y_0)$, we have $f(y_0) \in V$, so $g^{-1}(f^{-1}(V)) = \mathbb{N}$. Open. $\checkmark$
  - If $f(x_0) \notin V$ and $f(y_0) \in V$: $g^{-1}(f^{-1}(V)) = \{1, 2, 3, \ldots\}$, which is cofinite. Open. $\checkmark$
  - If $f(x_0) \notin V$ and $f(y_0) \notin V$: $g^{-1}(f^{-1}(V)) = \emptyset$. Open. $\checkmark$

  So $g$ is continuous w.r.t. $\tau_{\mathrm{init}}$. $\checkmark$

- **$\tau$-continuity fails:** $g^{-1}(U) = \{0\}$ (since $x_0 \in U$ and $y_0 \notin U$). The set $\{0\}$ is finite and nonempty, hence **not open** in the cofinite topology. $\boldsymbol{\times}$

This violates the initiality condition, so $f$ is not initial.

### Conclusion of contrapositive

In both cases, $\tau \neq \tau_{\mathrm{init}}$ implies $f$ is not initial. By contraposition:

$$f \text{ is initial} \implies \tau = \tau_{\mathrm{init}},$$

i.e., $X$ has the initial topology defined by $f$. $\blacksquare$

## Remark on the two test spaces

The proof uses two complementary test spaces:

1. **$Z = (X, \tau_{\mathrm{init}})$ with $g = \mathrm{id}$** — works when $\leq_\tau = \leq_{\mathrm{init}}$ (the identity is monotone). This detects extra open sets that don't change the specialization preorder.

2. **$Z = (\mathbb{N}, \text{cofinite})$ with $g$ mapping $0 \mapsto x_0$, $n \mapsto y_0$** — works when $\leq_\tau \subsetneq \leq_{\mathrm{init}}$. The cofinite topology is $T_1$ (so any map is monotone), yet rich enough to detect non-open finite sets. The pair $(x_0, y_0)$ with $x_0 \leq_{\mathrm{init}} y_0$ ensures $\tau_{\mathrm{init}}$-continuity, while $x_0 \in U$, $y_0 \notin U$ breaks $\tau$-continuity.

The Sierpinski space (tried in Round 1) cannot work because for Sierpinski $S$, continuity w.r.t. $\tau$ is equivalent to monotonicity w.r.t. $\leq_\tau$, making the initiality condition tautological. The cofinite topology breaks this equivalence: it is $T_1$ (so monotonicity is free) but not discrete (so continuity is a real constraint).

### PROOF COMPLETE
