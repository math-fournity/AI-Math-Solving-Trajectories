# Every Object of Sh(B) Is Projective

**Theorem.** Let $B$ be a complete Boolean algebra and let $\mathrm{Sh}(B)$ denote the topos of sheaves on $B$ (viewed as a locale). Then every object of $\mathrm{Sh}(B)$ is projective.

---

## Proof

We show that every epimorphism in $\mathrm{Sh}(B)$ splits. Recall that an object $P$ of a category is **projective** if and only if every epimorphism $e : E \twoheadrightarrow P$ admits a section $s : P \to E$ with $e \circ s = \mathrm{id}_P$. Moreover, *every* object is projective if and only if every epimorphism splits (apply the definition to the codomain of the epimorphism with $f = \mathrm{id}$).

The proof proceeds in three steps.

### Step 1. $\mathrm{Sh}(B)$ is a Boolean topos

Since $B$ is a Boolean algebra, the locale $B$ satisfies the law of excluded middle: for every $b \in B$, the complement $\neg b$ exists and $b \vee \neg b = \top$. The subobject classifier $\Omega$ in $\mathrm{Sh}(B)$ is the sheaf associated to the presheaf $b \mapsto \{c \in B : c \leq b\}$, and in a Boolean locale this is isomorphic to the coproduct $\mathbf{1} + \mathbf{1}$ (the constant sheaf on a two-element set). Hence $\mathrm{Sh}(B)$ is a **Boolean topos**: its internal logic satisfies the law of excluded middle.

### Step 2. The Boolean-valued universe $V^B$ satisfies the Axiom of Choice

The complete Boolean algebra $B$ gives rise to the **Boolean-valued universe** $V^B$, constructed by transfinite recursion:

$$V^B_\alpha = \{u : \text{dom}(u) \subseteq V^B_{<\alpha},\; \text{dom}(u) \times B \text{ valued}\},$$

where $V^B_{<\alpha} = \bigcup_{\beta < \alpha} V^B_\beta$, and $V^B = \bigcup_\alpha V^B_\alpha$.

Each name $u \in V^B$ is assigned a Boolean truth value $\llbracket \varphi(u_1, \dots, u_n) \rrbracket \in B$ for every formula $\varphi$ of set theory. The fundamental theorem of Boolean-valued models states:

> **Theorem (Scott–Solovay, see Jech *Set Theory* Thm. 14.21 or Bell *Boolean-Valued Models* Ch. 2).** If $V \models \mathrm{ZFC}$, then $V^B \models \mathrm{ZFC}$.

In particular, $V^B \models \mathrm{AC}$.

The proof that $V^B \models \mathrm{AC}$ relies on the **Maximum Principle**, which requires $B$ to be complete:

> **Maximum Principle.** Let $B$ be a complete Boolean algebra. For any formula $\varphi(x, y_1, \dots, y_n)$ and any names $u_1, \dots, u_n \in V^B$, there exists a name $u \in V^B$ such that
> $$\llbracket \exists x\, \varphi(x, u_1, \dots, u_n) \rrbracket = \llbracket \varphi(u, u_1, \dots, u_n) \rrbracket.$$

*Proof that $V^B \models \mathrm{AC}$ using the Maximum Principle.* Suppose $\llbracket f \text{ is a surjection from } A \text{ onto } C \rrbracket = \mathbf{1}$, where $f, A, C \in V^B$ are names. Then

$$\llbracket \forall y \in C,\; \exists x \in A,\; f(x) = y \rrbracket = \mathbf{1}.$$

For each name $y$ with $\llbracket y \in C \rrbracket = \mathbf{1}$, the Maximum Principle yields a name $x_y$ with

$$\llbracket x_y \in A \;\wedge\; f(x_y) = y \rrbracket = \llbracket \exists x \in A,\; f(x) = y \rrbracket = \mathbf{1}.$$

Using the Maximum Principle once more (and the completeness of $B$ to form the required suprema), one constructs a name $g$ for a function $g : C \to A$ such that

$$\llbracket \forall y \in C,\; f(g(y)) = y \rrbracket = \mathbf{1}.$$

Hence $\llbracket \text{every surjection has a right inverse} \rrbracket = \mathbf{1}$, i.e., $V^B \models \mathrm{AC}$. $\square$

### Step 3. AC in $V^B$ implies every epimorphism in $\mathrm{Sh}(B)$ splits

There is a well-known equivalence of categories

$$\mathrm{Sh}(B) \;\simeq\; \mathbf{B}\text{-}\mathbf{Set},$$

where $\mathbf{B}\text{-}\mathbf{Set}$ is the category of $B$-valued sets (sets equipped with a $B$-valued equality) and $B$-valued functions. This equivalence is the topos-theoretic shadow of the correspondence between sheaves on $B$ and names in $V^B$:

- **Objects:** An object $F$ of $\mathrm{Sh}(B)$ corresponds to a $B$-valued set, i.e., a name $\dot{F} \in V^B$ for a set, together with its $B$-valued equality relation.
- **Morphisms:** A sheaf morphism $F \to G$ corresponds to a name for a function $\dot{F} \to \dot{G}$ in $V^B$.
- **Epimorphisms:** A sheaf morphism $e : E \twoheadrightarrow F$ is an epimorphism in $\mathrm{Sh}(B)$ if and only if the corresponding name $\dot{e}$ satisfies $\llbracket \dot{e} \text{ is a surjection} \rrbracket = \mathbf{1}$ in $V^B$.
- **Sections:** A section $s : F \to E$ of $e$ in $\mathrm{Sh}(B)$ corresponds to a name $\dot{s}$ with $\llbracket \dot{e} \circ \dot{s} = \mathrm{id}_{\dot{F}} \rrbracket = \mathbf{1}$.

Now let $e : E \twoheadrightarrow F$ be any epimorphism in $\mathrm{Sh}(B)$. Under the equivalence, $\dot{e}$ is a name for a surjection in $V^B$. Since $V^B \models \mathrm{AC}$ (Step 2), there exists a name $\dot{s}$ for a section:

$$\llbracket \dot{e} \circ \dot{s} = \mathrm{id}_{\dot{F}} \rrbracket = \mathbf{1}.$$

Translating back through the equivalence, $\dot{s}$ corresponds to a sheaf morphism $s : F \to E$ with $e \circ s = \mathrm{id}_F$. Hence $e$ splits.

Since $e$ was an arbitrary epimorphism, **every epimorphism in $\mathrm{Sh}(B)$ splits**, and therefore every object of $\mathrm{Sh}(B)$ is projective. $\blacksquare$

---

## Remark on the Role of Completeness

The completeness of $B$ is essential. The Maximum Principle — which is the engine behind $V^B \models \mathrm{AC}$ — requires that $B$ be complete, because the construction of the witnessing name involves taking suprema of arbitrary families of Boolean truth values. Without completeness, the Maximum Principle fails, and one cannot guarantee that $V^B \models \mathrm{AC}$.

Concretely, the completeness of $B$ also ensures the following sheaf-theoretic property: every epimorphism $e : E \twoheadrightarrow F$ in $\mathrm{Sh}(B)$ is **surjective on sections**, meaning $e_b : E(b) \to F(b)$ is surjective for every $b \in B$. (Given $t \in F(b)$, local surjectivity provides a cover $\{b_i\}$ of $b$ with lifts on each $b_i$; using the Boolean structure, one refines to a maximal antichain $\{c_j\}$ with $\bigvee c_j = b$, and the disjointness of the $c_j$ allows the local lifts to glue to a global lift in $E(b)$.) This surjectivity-on-sections property is a hallmark of complete Boolean algebras and is what makes the gluing argument work.

## Summary

$$\boxed{\text{Yes. Every object of } \mathrm{Sh}(B) \text{ is projective when } B \text{ is a complete Boolean algebra.}}$$

The proof proceeds via the equivalence $\mathrm{Sh}(B) \simeq \mathbf{B}\text{-}\mathbf{Set}$ and the theorem that the Boolean-valued universe $V^B$ satisfies the Axiom of Choice (a consequence of the Maximum Principle for complete Boolean algebras). Since $V^B \models \mathrm{AC}$, every surjection in $V^B$ has a section, which translates under the equivalence to every epimorphism in $\mathrm{Sh}(B)$ splitting, i.e., every object being projective.
