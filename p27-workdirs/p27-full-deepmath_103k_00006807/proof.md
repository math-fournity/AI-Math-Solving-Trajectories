# Solution

**Claim.** The only subfield of $\mathbb{C}$ other than $\mathbb{R}$ that is connected (with the subspace topology from $\mathbb{C}$) is $\mathbb{C}$ itself. Equivalently, the connected subfields of $\mathbb{C}$ are exactly $\mathbb{R}$ and $\mathbb{C}$.

## Key Lemma

**Lemma.** A connected subgroup $H$ of $(\mathbb{R}^2, +)$ is a real vector subspace, i.e.
$$H \in \big\{\{0\},\ \text{a line through the origin},\ \mathbb{R}^2\big\}.$$

*Proof of Lemma.* If $H = \{0\}$ we are done.

**Case 1: $H \neq \{0\}$ is contained in some line $L$ through the origin.** Then $H$ is a connected subgroup of $L \cong \mathbb{R}$. The only connected subgroups of $\mathbb{R}$ are $\{0\}$ and $\mathbb{R}$ itself (a proper nontrivial subgroup of $\mathbb{R}$ is either cyclic hence discrete, or dense; in either case it is disconnected). Since $H \neq \{0\}$, we get $H = L$.

**Case 2: $H$ is not contained in any line through the origin.** Then $H$ contains two $\mathbb{R}$-linearly independent vectors $u, v$. Since $H$ is an additive subgroup, the lattice
$$\Lambda = \mathbb{Z}u + \mathbb{Z}v \subseteq H.$$
The quotient $H/\Lambda$ is a connected subgroup of the torus $\mathbb{R}^2/\Lambda \cong \mathbb{T}^2$.

The connected subgroups of $\mathbb{T}^2$ are well known (from the classification of closed subgroups of compact Lie groups together with the structure of dense one-parameter subgroups):
- $\{0\}$,
- $\mathbb{T}^2$ itself,
- closed $1$-dimensional subtori (circles, corresponding to rational-slope one-parameter subgroups),
- dense $1$-parameter subgroups (irrational-slope one-parameter subgroups).

We examine each possibility for $H/\Lambda$:

- **$H/\Lambda = \{0\}$**: Then $H = \Lambda$, which is discrete. This contradicts $H$ being connected and nontrivial.

- **$H/\Lambda$ is a proper connected subgroup** (a circle or a dense $1$-parameter subgroup): Such a subgroup is the image of a one-parameter subgroup $\varphi: \mathbb{R} \to \mathbb{T}^2$, $\varphi(t) = t \cdot w \pmod{\Lambda}$ for some nonzero $w \in \mathbb{R}^2$. Let $L_0 = \mathbb{R}w$ be the line through the origin in direction $w$. The preimage of $H/\Lambda$ under the quotient map $\pi: \mathbb{R}^2 \to \mathbb{T}^2$ is
$$\pi^{-1}(H/\Lambda) = L_0 + \Lambda = \bigcup_{\lambda \in \Lambda} (L_0 + \lambda).$$
This is a union of parallel lines (translates of $L_0$ by lattice points). Since $H/\Lambda$ is a *proper* subgroup, $L_0 + \Lambda \neq \mathbb{R}^2$, so this is a union of *properly many* distinct parallel lines. Each line $L_0 + \lambda$ is closed in $\mathbb{R}^2$, and distinct parallel lines are disjoint and separated (each is both open and closed in the union, as the lines are pairwise disjoint closed sets with positive separation in any bounded region). Therefore $L_0 + \Lambda$ is **disconnected** — it is a disjoint union of closed-and-open lines.

  But $H \subseteq \pi^{-1}(H/\Lambda) = L_0 + \Lambda$, and $H$ is connected. A connected subset of a disjoint union of clopen components must lie entirely in one component, i.e., $H \subseteq L_0 + \lambda_0$ for some $\lambda_0 \in \Lambda$. Since $H$ is a subgroup containing $0$, we have $0 \in H$, so $H \subseteq L_0$. But this means $H$ is contained in a line through the origin, contradicting the assumption of Case 2.

- **$H/\Lambda = \mathbb{T}^2$**: Then $H = \mathbb{R}^2$, which is indeed a connected subgroup.

Since all other cases lead to contradictions, we conclude $H = \mathbb{R}^2$. $\quad\blacksquare$

## Applying the Lemma to Subfields

Let $K \subseteq \mathbb{C}$ be a subfield that is connected in the subspace topology from $\mathbb{C} \cong \mathbb{R}^2$.

As an additive group, $(K, +)$ is a subgroup of $(\mathbb{C}, +) \cong (\mathbb{R}^2, +)$, and it is connected. By the Lemma, $K$ is one of $\{0\}$, a line through the origin, or $\mathbb{R}^2$.

- **$K = \{0\}$**: Impossible, since a field contains $1 \neq 0$.

- **$K$ is a line through the origin**: Write $K = \{re^{i\theta} : r \in \mathbb{R}\}$ for some fixed $\theta$. For $K$ to be a field it must be closed under multiplication. For $re^{i\theta}, se^{i\theta} \in K$:
$$(re^{i\theta})(se^{i\theta}) = rs \cdot e^{2i\theta}.$$
For this to lie on the same line, we need $e^{2i\theta}$ to be a real multiple of $e^{i\theta}$, i.e., $2\theta \equiv \theta \pmod{\pi}$, giving $\theta \equiv 0 \pmod{\pi}$. Thus $K = \mathbb{R}$ (the real axis). Moreover $K$ must contain $1 = e^{i \cdot 0}$, confirming $\theta = 0 \pmod{\pi}$, so $K = \mathbb{R}$.

- **$K = \mathbb{R}^2 = \mathbb{C}$**: This is indeed a connected subfield of itself.

## The Case $K \subseteq \mathbb{R}$ (Alternative Direct Argument)

For completeness, we verify directly that no proper subfield of $\mathbb{R}$ is connected. Suppose $K \subseteq \mathbb{R}$ is a connected subfield. The subspace topology on $\mathbb{R}$ induced from $\mathbb{C}$ is the usual topology on $\mathbb{R}$, so $K$ is a connected subset of $\mathbb{R}$, hence an interval. Since $K$ is a field of characteristic $0$, it contains $\mathbb{Q}$. The rationals $\mathbb{Q}$ are dense and unbounded (both above and below) in $\mathbb{R}$. The only interval containing $\mathbb{Q}$ is $\mathbb{R}$ itself. Therefore $K = \mathbb{R}$.

## Conclusion

The connected subfields of $\mathbb{C}$ (with the induced topology) are exactly $\mathbb{R}$ and $\mathbb{C}$. Therefore, the subfields of $\mathbb{C}$ other than $\mathbb{R}$ that are connected are:

$$\boxed{\mathbb{C}}$$

### PROOF COMPLETE
