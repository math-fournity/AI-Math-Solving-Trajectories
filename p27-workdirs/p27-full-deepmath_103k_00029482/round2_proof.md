**Yes.** For every $x \in (0,1]$, using the Axiom of Choice one can construct a non-Lebesgue-measurable set $A \subseteq [0,1]$ with outer measure $m^*(A) = x$.

The proof proceeds in two stages: (1) construct a Vitali-type set $V \subseteq [0,1]$ with outer measure exactly $1$, then (2) scale it.

---

## Stage 1: A Vitali set with outer measure 1

**Setup.** Define the equivalence relation on $[0,1]$: $a \sim b \iff a - b \in \mathbb{Q}$. Each equivalence class $C = a + \mathbb{Q}$ is countable and dense in $[0,1]$. There are $\mathfrak{c} = |[0,1]|$ many equivalence classes (since $|[0,1]| = \mathfrak{c}$ and each class is countable).

**Goal.** Using AC, pick one representative from each class so that the resulting set $V$ meets *every* closed subset of $[0,1]$ of positive Lebesgue measure. We then show this forces $m^*(V) = 1$.

### Construction (transfinite induction + AC)

Well-order (using AC, equivalently the Well-Ordering Theorem):

- the family of all closed subsets of $[0,1]$ of positive measure as $\{F_\alpha : \alpha < \mathfrak{c}\}$,
- the family of all $\mathbb{Q}$-equivalence classes as $\{C_\alpha : \alpha < \mathfrak{c}\}$.

**Key counting fact.** Every closed $F \subseteq [0,1]$ with $m(F) > 0$ has cardinality $|F| = \mathfrak{c}$ (a positive-measure closed set is uncountable, and every uncountable closed subset of $\mathbb{R}$ has cardinality $\mathfrak{c}$). Since each equivalence class is countable, $F$ intersects exactly $\mathfrak{c}$ many equivalence classes (if it intersected only $<\mathfrak{c}$ classes, then $|F| \le \text{countable} \cdot <\mathfrak{c} < \mathfrak{c}$, contradiction).

**Phase 1 (meeting every positive-measure closed set).** By transfinite recursion over $\alpha < \mathfrak{c}$:

- At stage $\alpha$, suppose we have assigned representatives from classes indexed by a set $S_\alpha \subseteq \mathfrak{c}$ with $|S_\alpha| < \mathfrak{c}$ (since $|\alpha| < \mathfrak{c}$ and we add at most one class per stage).
- The closed set $F_\alpha$ meets $\mathfrak{c}$ many classes, so among them there is a class $C_{f(\alpha)}$ with $f(\alpha) \notin S_\alpha$ (because $\mathfrak{c} \setminus S_\alpha$ still has cardinality $\mathfrak{c}$).
- Pick $r_{f(\alpha)} \in C_{f(\alpha)} \cap F_\alpha$ (nonempty by choice of $f(\alpha)$). Add $f(\alpha)$ to the used set.

This is legitimate at every stage because $|S_\alpha| < \mathfrak{c}$ while $F_\alpha$ offers $\mathfrak{c}$ fresh classes.

**Phase 2 (filling in the remaining classes).** For every class $C_\beta$ not assigned in Phase 1, pick any representative $r_\beta \in C_\beta \cap [0,1]$ (nonempty since each class is dense in $[0,1]$). This uses AC again.

**Result.** $V := \{r_\beta : \beta < \mathfrak{c}\}$ contains exactly one point from each $\mathbb{Q}$-equivalence class, and $V \cap F_\alpha \neq \emptyset$ for every $\alpha < \mathfrak{c}$, i.e. for every positive-measure closed subset of $[0,1]$.

### $m^*(V) = 1$

Suppose for contradiction that $m^*(V) < 1$. By outer regularity of Lebesgue measure, there exists a $G_\delta$ set $G \supseteq V$ with $m(G) = m^*(V) < 1$. Then $[0,1] \setminus G$ is measurable with $m([0,1] \setminus G) = 1 - m(G) > 0$. By inner regularity, there is a closed set $F \subseteq [0,1] \setminus G$ with $m(F) > 0$. But $V \subseteq G$ and $F \subseteq [0,1] \setminus G$, so $V \cap F = \emptyset$ — contradicting the construction, which guarantees $V$ meets every positive-measure closed set. Hence $m^*(V) = 1$.

### $V$ is non-measurable

Suppose $V$ were Lebesgue measurable. Then $m(V) = m^*(V) = 1$. Consider the countably many rational translates $V + q \pmod{1}$ for $q \in \mathbb{Q} \cap [0,1)$. Because $V$ contains one representative per $\mathbb{Q}$-class, these translates are pairwise disjoint and their union is $[0,1)$. Each translate has measure $m(V) = 1$ (translation invariance and the mod-$1$ wrap preserve measure). So

$$1 = m([0,1)) = m\!\left(\bigcup_{q} (V+q \bmod 1)\right) = \sum_{q} m(V+q \bmod 1) = \sum_{q} 1 = \infty,$$

a contradiction. Therefore $V$ is non-measurable.

---

## Stage 2: Scaling to any prescribed outer measure $x \in (0,1]$

Fix $x \in (0,1]$ and define

$$A_x := x \cdot V = \{x \cdot v : v \in V\} \subseteq [0, x] \subseteq [0,1].$$

**Outer measure.** Lebesgue outer measure scales: $m^*(cA) = |c|\, m^*(A)$ for any $c \in \mathbb{R}$ and any $A \subseteq \mathbb{R}$. (This follows directly from the definition $m^*(A) = \inf \sum |I_n|$ over countable interval covers, since scaling a cover of $A$ by $c$ gives a cover of $cA$ with total length scaled by $|c|$, and vice versa.) Therefore

$$m^*(A_x) = m^*(x \cdot V) = x \cdot m^*(V) = x \cdot 1 = x.$$

**Non-measurability.** If $A_x$ were Lebesgue measurable, then $V = \frac{1}{x} A_x$ would be measurable (scaling by a nonzero constant preserves measurability), contradicting Stage 1. Hence $A_x$ is non-measurable.

**Containment.** Since $V \subseteq [0,1]$ and $0 < x \le 1$, we have $A_x \subseteq [0,x] \subseteq [0,1]$.

---

## Use of the Axiom of Choice

AC enters in three essential ways:

1. **Well-ordering** the family of positive-measure closed sets and the family of equivalence classes (each of cardinality $\mathfrak{c}$) — equivalent to AC via the Well-Ordering Theorem.
2. **Selecting representatives** from each equivalence class (Phase 1 picks from $C_{f(\alpha)} \cap F_\alpha$; Phase 2 picks from $C_\beta \cap [0,1]$).
3. **Transfinite recursion** over $\mathfrak{c}$, which requires the well-ordering furnished by AC.

Without AC (or an equivalent choice principle) one cannot pick representatives from uncountably many classes, and indeed models of ZF exist in which every subset of $\mathbb{R}$ is Lebesgue measurable (Solovay's model).

---

## Conclusion

For every $x \in (0,1]$, the set $A_x = xV \subseteq [0,1]$ is non-Lebesgue-measurable and satisfies $m^*(A_x) = x$, constructed using the Axiom of Choice.

$$\boxed{\text{Yes}}$$

### PROOF COMPLETE
