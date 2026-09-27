Let me start by understanding the problem.

We have $\alpha \neq 0$ such that for every $\beta < \alpha$, there exists $\beta < \gamma < \alpha$ and an elementary embedding from $V_\gamma$ to $V_\alpha$. Does it follow that $V_\alpha$ models the replacement axiom?

This is a question in set theory about elementary embeddings between ranks of the cumulative hierarchy. Let me think carefully.

First, let me set up notation. $V_\alpha$ denotes the $\alpha$-th stage of the cumulative hierarchy: $V_0 = \emptyset$, $V_{\alpha+1} = \mathcal{P}(V_\alpha)$, $V_\lambda = \bigcup_{\beta<\lambda} V_\beta$ for limit $\lambda$.

An elementary embedding $j: V_\gamma \to V_\alpha$ means that for every formula $\varphi(x_1, \ldots, x_n)$ and all $a_1, \ldots, a_n \in V_\gamma$: $V_\gamma \models \varphi(a_1, \ldots, a_n) \iff V_\alpha \models \varphi(j(a_1), \ldots, j(a_n))$.

The hypothesis: for every $\beta < \alpha$, there exists $\gamma$ with $\beta < \gamma < \alpha$ and an elementary embedding $V_\gamma \to V_\alpha$.

Question: does it follow that $V_\alpha \models \text{Replacement}$?

First, let me recall what Replacement says: For every formula $\varphi(x, y, A)$ with parameters $A$, if $\forall x \in a \, \exists! y \, \varphi(x,y,A)$ then there's a set $b$ such that $\forall y (y \in b \iff \exists x \in a \, \varphi(x,y,A))$. In terms of $V_\alpha$ being a model of Replacement: for every function $f$ definable over $V_\alpha$ (with parameters) whose domain is a set $a \in V_\alpha$, the range is an element of $V_\alpha$.

Known facts:

1. If $j: V_\gamma \to V_\alpha$ is elementary and nontrivial... wait, actually here embeddings could be trivial (identity). Hmm, but identity embedding from $V_\gamma$ to $V_\alpha$ requires $V_\gamma \subseteq V_\alpha$ and elementarity would require $V_\gamma \preceq V_\alpha$, which is impossible unless $\gamma = \alpha$ (since $\emptyset \neq \{\emptyset\}$... wait, actually $V_\gamma \preceq V_\alpha$ with $\gamma < \alpha$ is impossible because... hmm, let me think. Actually, if $V_\gamma \subseteq V_\alpha$ is elementary substructure, take $x = \emptyset \in V_\gamma$. The property "$y = \emptyset$" is satisfied by $\emptyset$; fine. Take any $a \in V_\gamma$. Then "there exists $y$ such that $y = a \cup \{a\}$" — the unique witness is $S(a) = a \cup \{a\}$ which must be in $V_\gamma$ by elementarity (since $V_\gamma$ must contain the witness). Wait more precisely: $V_\alpha \models \exists y (y = S(a))$, so by elementarity $V_\gamma \models \exists y (y = S(a))$, i.e., $V_\gamma$ contains $S(a)$. By induction, $V_\gamma$ contains $a + n$ (iterated successor) for all natural $n$, hence contains arbitrarily high ranks, contradiction with $V_\gamma$ being a set. So indeed no proper elementary substructure relation $V_\gamma \prec V_\alpha$ for $\gamma < \alpha$. Hence all these embeddings are non-trivial (move some ordinal).

Wait, but actually I need to be careful: elementary embedding doesn't have to be inclusion. An elementary embedding $j: V_\gamma \to V_\alpha$ is a map such that formulas are preserved. Standard fact: any elementary embedding between transitive sets (or classes) moves ordinals upward: $j(\xi) \geq \xi$.

So the hypothesis is: cofinally many $\gamma < \alpha$ admit nontrivial elementary embeddings $j_\gamma : V_\gamma \to V_\alpha$.

This looks like a large cardinal flavored question. Let me think about what's known.

A rank $V_\alpha$ satisfying ZFC-like properties: $V_\alpha \models \text{ZFC}$ iff $\alpha$ is inaccessible (uncountable strongly inaccessible, well, $\alpha$ inaccessible). Actually $V_\kappa \models \mathrm{ZFC}_2$? Hmm, $V_\kappa \models \mathrm{ZFC}$ iff $\kappa$ is strongly inaccessible (and uncountable; also need $\kappa > \omega$, and for Power Set etc.).

But we're only asked about Replacement.

When does $V_\alpha$ satisfy Replacement? Known: $V_\alpha \models \text{ZFC} \setminus \{\text{Power Set}\}$... hmm, actually let me think again. 

The standard result: For $\alpha$ a limit ordinal, $V_\alpha \models \text{ZFC}$ iff $\alpha$ is strongly inaccessible. For Replacement alone:

Claim: $V_\alpha \models \text{Replacement}$ iff $\alpha$ is... hmm, not exactly an accessible characterization, but related to "$\alpha$ is a beth fixed point"? No wait.

Hmm, let me think. Replacement in $V_\alpha$: every definable-with-parameters function from a set in $V_\alpha$ has range in $V_\alpha$.

If $\operatorname{cf}(\alpha) < \alpha$... hmm wait, that's not directly relevant since definable functions aren't arbitrary functions.

Actually, there's a classical fact: $V_\alpha \models \mathrm{ZFC}$ iff $\alpha$ is inaccessible. And $V_\alpha \models \mathrm{ZFC}$ minus Replacement iff $\alpha > \omega$ is a strong limit cardinal? Not exactly — Separation holds in every $V_\alpha$ ($\alpha$ limit), Pairing, Union hold when... hmm.

Let me recall: 
- Extensionality, Foundation hold in every $V_\alpha$.
- Empty Set: $\alpha > 0$.
- Pairing: $\alpha$ limit.
- Union: $\alpha$ limit.
- Infinity: $\alpha > \omega$.
- Separation: $\alpha$ limit (any limit).
- Power Set: $\alpha$ limit